#!/usr/bin/env python3
"""motion-taste: tính điểm gu từ các vòng chấm mẫu.

Lệnh:
  python3 taste.py status       số vòng, số mẫu, URL đã dùng
  python3 taste.py new-round    tạo data/rounds/round-NN.json trống cho vòng tiếp theo
  python3 taste.py coverage     category / tag còn thiếu bằng chứng, để chọn mẫu vòng sau
  python3 taste.py style [id]   xếp hạng style theo gu, hoặc bằng chứng gu trong một style để thiết kế theo nó
  python3 taste.py export [N]   lệnh ghi mẫu của vòng N lên trang chấm điểm
  python3 taste.py import-ratings <file>  ghi điểm đọc từ trang vào file vòng
  python3 taste.py audit        tính điểm mọi tag, in audit, ghi data/evidence.json và bảng bằng chứng trong motion-taste.md
Tuỳ chọn: --dir <thư mục skill> (mặc định: thư mục cha của scripts/)

Cách tính:
  Điểm của một (category, tag) trên một mẫu = điểm riêng của category nếu người dùng chấm (trọng số 1.0),
  nếu không thì điểm tổng của mẫu (trọng số 0.6). Gộp qua mọi mẫu đã chấm có tag đó.
  Nên: >= 2 mẫu, trung bình >= 4.0 · Tránh: >= 2 mẫu, trung bình <= 2.0 · Mâu thuẫn: >= 2 mẫu, độ lệch chuẩn >= 1.5
  Còn lại: Đang theo dõi. Độ tin cậy: cao (>= 4 mẫu, lệch < 1.0), vừa (>= 2 mẫu, lệch < 1.2), thấp (còn lại).
"""
import argparse, datetime, json, math, os, re, sys

CATS = [
    ("style", "Style"), ("khong_khi", "Không khí"), ("muc_dich", "Mục đích"), ("hook", "Hook"), ("nhip", "Nhịp và cắt cảnh"), ("chuyen_canh", "Chuyển cảnh"), ("chu", "Chữ"),
    ("chuyen_dong", "Chuyển động"), ("mau", "Màu"), ("bo_cuc", "Bố cục"), ("hinh", "Kiểu hình"),
    ("am_thanh", "Âm thanh"), ("phu_de", "Phụ đề"), ("cau_truc", "Cấu trúc"),
]
CAT_NAME = dict(CATS)
W_EXPLICIT, W_OVERALL = 1.0, 0.6
START = "<!-- AUTO:EVIDENCE START"
END = "<!-- AUTO:EVIDENCE END -->"


def paths(base):
    return {
        "rounds": os.path.join(base, "data", "rounds"),
        "evidence": os.path.join(base, "data", "evidence.json"),
        "rules": os.path.join(base, "motion-taste.md"),
        "cats": os.path.join(base, "references", "categories.md"),
    }


def load_rounds(p):
    out = []
    if not os.path.isdir(p["rounds"]):
        return out
    for f in sorted(os.listdir(p["rounds"])):
        if re.fullmatch(r"round-\d+\.json", f):
            fp = os.path.join(p["rounds"], f)
            try:
                with open(fp, encoding="utf-8") as fh:
                    r = json.load(fh)
            except json.JSONDecodeError as e:
                sys.exit(f"Lỗi JSON trong {fp}: {e}")
            r["_file"] = f
            out.append(r)
    out.sort(key=lambda r: r.get("round", 0))
    return out


def canonical_tags(p):
    """Đọc bộ tag chuẩn từ categories.md: tiêu đề '## <id> - ...' và các dòng '| `tag` | ... |'."""
    tags, cur = {}, None
    if not os.path.exists(p["cats"]):
        return tags
    for line in open(p["cats"], encoding="utf-8"):
        m = re.match(r"##\s+([a-z_]+)\s+-", line)
        if m:
            cur = m.group(1)
            tags[cur] = []
            continue
        m = re.match(r"\|\s*`([a-z0-9_]+)`\s*\|", line)
        if m and cur:
            tags[cur].append(m.group(1))
    return tags


def valid_score(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and 1 <= x <= 5


def norm_score(x):
    """'+' -> 5, '-' -> 1, số dạng chuỗi -> số; còn lại giữ nguyên để báo lỗi."""
    if isinstance(x, str):
        x = x.strip()
        if x == "+":
            return 5
        if x == "-":
            return 1
        try:
            return float(x)
        except ValueError:
            return x
    return x


def collect(rounds, warn):
    """Trả về (stats theo (cat, tag), danh sách mẫu đã chấm, kiểm tra lặp lại)."""
    stats, rated, by_id = {}, [], {}
    for r in rounds:
        for s in r.get("samples", []):
            by_id[s.get("id")] = s
    for r in rounds:
        for s in r.get("samples", []):
            sid = s.get("id", "?")
            rt = s.get("rating")
            if not rt:
                continue
            ov = rt["overall"] = norm_score(rt.get("overall"))
            rt["categories"] = {c: norm_score(v) for c, v in (rt.get("categories") or {}).items()}
            if not valid_score(ov):
                warn.append(f"{sid}: điểm tổng không hợp lệ ({ov!r}), bỏ qua mẫu")
                continue
            rated.append(s)
            if s.get("repeat_of"):
                continue  # mẫu chiếu lại chỉ dùng để kiểm tra nhất quán, không cộng điểm hai lần
            cat_scores = rt.get("categories") or {}
            for c, v in cat_scores.items():
                if c not in CAT_NAME:
                    warn.append(f"{sid}: category lạ trong rating '{c}'")
                elif not valid_score(v):
                    warn.append(f"{sid}: điểm category {c} không hợp lệ ({v!r})")
            for c, b in (s.get("breakdown") or {}).items():
                if c not in CAT_NAME:
                    warn.append(f"{sid}: category lạ trong breakdown '{c}'")
                    continue
                v = cat_scores.get(c)
                score, w = (v, W_EXPLICIT) if valid_score(v) else (ov, W_OVERALL)
                for t in (b or {}).get("tags", []):
                    st = stats.setdefault((c, t), {"items": [], "kinds": set()})
                    st["items"].append({"id": sid, "score": score, "w": w, "explicit": w == W_EXPLICIT,
                                        "note": (b or {}).get("note", "")})
                    st["kinds"].add(s.get("kind", "?"))
    repeats = []
    for s in rated:
        o = s.get("repeat_of")
        if o:
            orig = by_id.get(o)
            if orig and orig.get("rating") and valid_score(orig["rating"].get("overall")):
                d = abs(s["rating"]["overall"] - orig["rating"]["overall"])
                repeats.append({"id": s["id"], "of": o, "before": orig["rating"]["overall"],
                                "after": s["rating"]["overall"], "diff": d})
    return stats, rated, repeats


def summarize(stats):
    rows = []
    for (c, t), st in stats.items():
        it = st["items"]
        ws = sum(i["w"] for i in it)
        mean = sum(i["score"] * i["w"] for i in it) / ws
        sd = math.sqrt(sum(i["w"] * (i["score"] - mean) ** 2 for i in it) / ws)
        n = len({i["id"] for i in it})
        if n >= 2 and sd >= 1.5:
            status = "Mâu thuẫn"
        elif n >= 2 and mean >= 4.0:
            status = "Nên"
        elif n >= 2 and mean <= 2.0:
            status = "Tránh"
        else:
            status = "Đang theo dõi"
        if n >= 4 and sd < 1.0:
            conf = "cao"
        elif n >= 2 and sd < 1.2:
            conf = "vừa"
        else:
            conf = "thấp"
        kinds = st["kinds"] - {"?"}
        scope = "cả hai" if kinds == {"motion", "animation"} else (next(iter(kinds)) if len(kinds) == 1 else "?")
        rows.append({"category": c, "tag": t, "mean": round(mean, 2), "sd": round(sd, 2), "n": n,
                     "explicit": sum(1 for i in it if i["explicit"]), "status": status, "confidence": conf,
                     "scope": scope, "samples": sorted({i["id"] for i in it}),
                     "notes": [f'{i["id"]}: {i["note"]}' for i in it if i["note"]]})
    order = {c: k for k, (c, _) in enumerate(CATS)}
    rows.sort(key=lambda r: (order.get(r["category"], 99), -r["mean"], r["tag"]))
    return rows


def evidence_block(rows, rated, repeats, rounds):
    today = datetime.date.today().isoformat()
    L = [f"{START} - phần dưới đây do scripts/taste.py audit viết lại, đừng sửa tay -->",
         "## Bảng bằng chứng",
         f"Cập nhật {today} · {len(rounds)} vòng · {len(rated)} mẫu đã chấm. "
         "Điểm = trung bình có trọng số (điểm riêng của category x1.0, điểm tổng của mẫu x0.6).", ""]
    if not rows:
        L += ["_(Chưa có dữ liệu.)_", END]
        return "\n".join(L)
    L += ["| Category | Tag | Điểm | Lệch | Số mẫu | Trạng thái | Tin cậy | Phạm vi | Mẫu |",
          "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        L.append(f'| {CAT_NAME.get(r["category"], r["category"])} | `{r["tag"]}` | {r["mean"]:.2f} | {r["sd"]:.2f} | '
                 f'{r["n"]} | {r["status"]} | {r["confidence"]} | {r["scope"]} | {", ".join(r["samples"])} |')
    if repeats:
        L += ["", "Kiểm tra nhất quán: " + "; ".join(
            f'{x["id"]} (chiếu lại {x["of"]}): {x["before"]} rồi {x["after"]}' for x in repeats)]
    L.append(END)
    return "\n".join(L)


def write_block(p, block):
    fp = p["rules"]
    text = open(fp, encoding="utf-8").read() if os.path.exists(fp) else "# Motion taste\n"
    s, e = text.find(START), text.find(END)
    if s != -1 and e != -1 and e > s:
        text = text[:s] + block + text[e + len(END):]
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    with open(fp, "w", encoding="utf-8") as fh:
        fh.write(text)


def cmd_status(p, rounds):
    rated = [s for r in rounds for s in r.get("samples", []) if s.get("rating")]
    allp = [s for r in rounds for s in r.get("samples", [])]
    print(f"Vòng: {len(rounds)} · Mẫu: {len(allp)} · Đã chấm: {len(rated)}")
    for r in rounds:
        ss = r.get("samples", [])
        done = sum(1 for s in ss if s.get("rating"))
        print(f'  {r["_file"]}: vòng {r.get("round")}, {r.get("focus", "")}, {done}/{len(ss)} mẫu đã chấm')
    pend = [s["id"] for s in allp if not s.get("rating")]
    if pend:
        print("Chưa chấm:", ", ".join(pend))
    print("URL đã dùng:")
    for s in allp:
        print(f'  {s.get("id")}: {s.get("url", "")}')


def cmd_new_round(p, rounds):
    n = max([r.get("round", 0) for r in rounds] + [0]) + 1
    if rounds and any(not s.get("rating") for s in rounds[-1].get("samples", [])):
        print(f'Lưu ý: {rounds[-1]["_file"]} còn mẫu chưa chấm.')
    os.makedirs(p["rounds"], exist_ok=True)
    fp = os.path.join(p["rounds"], f"round-{n:02d}.json")
    if os.path.exists(fp):
        sys.exit(f"{fp} đã tồn tại.")
    data = {"round": n, "date": datetime.date.today().isoformat(),
            "focus": "khám phá" if n == 1 else "thu hẹp", "hard_rules": [], "samples": []}
    with open(fp, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    print(fp)
    print(f'Id mẫu: r{n}s1, r{n}s2, ...')


def cmd_coverage(p, rounds):
    warn = []
    stats, rated, _ = collect(rounds, warn)
    rows = summarize(stats)
    canon = canonical_tags(p)
    print(f"Đã chấm {len(rated)} mẫu.\n")
    for c, name in CATS:
        cr = [r for r in rows if r["category"] == c]
        decided = [r for r in cr if r["status"] in ("Nên", "Tránh") and r["confidence"] != "thấp"]
        conflict = [r["tag"] for r in cr if r["status"] == "Mâu thuẫn"]
        seen = {r["tag"]: r["n"] for r in cr}
        thin = [t for t in canon.get(c, []) if seen.get(t, 0) < 2]
        flag = "đủ" if decided else "THIẾU"
        print(f"{name} [{flag}]: đã có rule {', '.join(r['tag'] for r in decided) or '-'}")
        if conflict:
            print(f"    mâu thuẫn: {', '.join(conflict)}")
        if thin:
            print(f"    ít bằng chứng (< 2 mẫu): {', '.join(thin)}")
    kinds = {}
    for s in rated:
        kinds[s.get("kind", "?")] = kinds.get(s.get("kind", "?"), 0) + 1
    print(f"\nLoại mẫu đã chấm: {kinds or '-'}")
    for w in warn:
        print("Cảnh báo:", w)


def cmd_audit(p, rounds):
    warn = []
    stats, rated, repeats = collect(rounds, warn)
    rows = summarize(stats)
    canon = canonical_tags(p)
    known = {t for ts in canon.values() for t in ts}
    new_tags = sorted({f'{r["category"]}.{r["tag"]}' for r in rows if r["tag"] not in known})
    with open(p["evidence"], "w", encoding="utf-8") as fh:
        json.dump({"updated": datetime.date.today().isoformat(), "rounds": len(rounds), "rated": len(rated),
                   "tags": rows, "repeats": repeats}, fh, ensure_ascii=False, indent=2)
    write_block(p, evidence_block(rows, rated, repeats, rounds))

    last = rounds[-1] if rounds else {}
    rated_ids = {s["id"] for s in rated}
    last_ids = {s["id"] for s in last.get("samples", []) if s.get("id") in rated_ids}
    print(f"# Audit (sau vòng {last.get('round', 0)})")
    print(f"Đã chấm vòng này: {len(last_ids)} mẫu · tổng {len(rated)} mẫu qua {len(rounds)} vòng")
    if repeats:
        ok = sum(1 for x in repeats if x["diff"] <= 1)
        print(f"Nhất quán: {ok}/{len(repeats)} mẫu chiếu lại lệch <= 1 điểm")
        for x in repeats:
            print(f'  {x["id"]} chiếu lại {x["of"]}: {x["before"]} rồi {x["after"]}')
    else:
        print("Nhất quán: chưa có mẫu chiếu lại")
    for title, st in (("Nên", "Nên"), ("Tránh", "Tránh"), ("Mâu thuẫn", "Mâu thuẫn")):
        sel = [r for r in rows if r["status"] == st]
        print(f"\n## {title} ({len(sel)})")
        for r in sel:
            touched = "  <- có bằng chứng mới" if set(r["samples"]) & last_ids else ""
            print(f'- {CAT_NAME[r["category"]]} `{r["tag"]}`: {r["mean"]:.2f} (lệch {r["sd"]:.2f}, {r["n"]} mẫu, '
                  f'tin cậy {r["confidence"]}, {r["scope"]}){touched}')
            for nt in r["notes"][:4]:
                print(f"    · {nt}")
    watch = [r for r in rows if r["status"] == "Đang theo dõi"]
    print(f"\n## Đang theo dõi ({len(watch)})")
    for r in watch:
        print(f'- {CAT_NAME[r["category"]]} `{r["tag"]}`: {r["mean"]:.2f} ({r["n"]} mẫu)')
    hard = [(r.get("round"), h) for r in rounds for h in r.get("hard_rules", [])]
    if hard:
        print("\n## Luật cứng đã ghi nhận")
        for rn, h in hard:
            print(f"- (vòng {rn}) {h}")
    missing = [CAT_NAME[c] for c, _ in CATS
               if not any(r["category"] == c and r["status"] in ("Nên", "Tránh") and r["confidence"] != "thấp"
                          for r in rows)]
    print("\n## Category chưa có rule (độ tin cậy vừa trở lên)")
    print(", ".join(missing) if missing else "Không còn - bộ rule đã phủ mọi category.")
    notes = [(s["id"], s["rating"].get("note")) for s in rated if s["id"] in last_ids and s["rating"].get("note")]
    if notes:
        print("\n## Ghi chú của người dùng vòng này")
        for sid, n in notes:
            print(f"- {sid}: {n}")
    if new_tags:
        print("\n## Tag ngoài bộ chuẩn")
        print(", ".join(new_tags))
    for w in warn:
        print("Cảnh báo:", w)
    print(f"\nĐã ghi {p['evidence']} và bảng bằng chứng trong {p['rules']}")


def cmd_export(p, rounds, arg):
    """In ra JSON cho ArtifactData action "batch": meta/current + samples/<id> của một vòng (mặc định vòng mới nhất)."""
    if not rounds:
        sys.exit("Chưa có vòng nào.")
    r = next((x for x in rounds if str(x.get("round")) == str(arg)), rounds[-1]) if arg else rounds[-1]
    ops = [{"op": "set", "collection": "meta", "doc_id": "current",
            "data": {"round": r["round"], "focus": r.get("focus", ""), "date": r.get("date", "")}}]
    for i, s in enumerate(r.get("samples", []), 1):
        doc = {k: s.get(k) for k in ("title", "url", "source", "creator", "duration_s", "format", "kind", "family", "summary", "breakdown")}
        doc.update({"round": r["round"], "order": i, "frames": s.get("frames") or [f'frames/{s["id"]}-{k}.jpg' for k in (1, 2, 3)]})
        ops.append({"op": "set", "collection": "samples", "doc_id": s["id"], "data": doc})
    print(json.dumps(ops, ensure_ascii=False))


def cmd_import(p, rounds, arg):
    """Đọc điểm từ trang artifact (file JSON: danh sách doc của collection ratings, mỗi doc có id/doc_id và data,
    hoặc dict {sampleId: data}) rồi ghi vào rating của mẫu tương ứng trong các file round."""
    if not arg or not os.path.exists(arg):
        sys.exit("Cần đường dẫn file JSON điểm chấm.")
    raw = json.load(open(arg, encoding="utf-8"))
    if isinstance(raw, dict) and "documents" in raw:
        raw = raw["documents"]
    items = {}
    if isinstance(raw, dict):
        items = raw
    else:
        for d in raw:
            sid = d.get("doc_id") or d.get("id") or (d.get("data") or {}).get("sample")
            items[sid] = d.get("data", d)
    changed = 0
    for r in rounds:
        touched = False
        hard = list(r.get("hard_rules", []))
        for s in r.get("samples", []):
            d = items.get(s["id"])
            if not d or not d.get("overall"):
                continue
            cats = {c: v for c, v in (d.get("categories") or {}).items() if v in (1, 5, "+", "-") or valid_score(v)}
            s["rating"] = {"overall": d["overall"], "categories": cats, "note": d.get("note", "")}
            if d.get("hard"):
                note = (d.get("note") or "").strip()
                h = (f'{note} ({s["id"]})' if note
                     else f'Không bao giờ dùng kiểu: {s.get("family") or s.get("title")} ({s["id"]})')
                if h not in hard:
                    hard.append(h)
            touched = True
            changed += 1
        if touched:
            r["hard_rules"] = hard
            fp = os.path.join(p["rounds"], r["_file"])
            out = {k: v for k, v in r.items() if k != "_file"}
            with open(fp, "w", encoding="utf-8") as fh:
                json.dump(out, fh, ensure_ascii=False, indent=2)
    print(f"Đã ghi điểm cho {changed} mẫu.")


def cmd_style(p, rounds, arg, cat="style"):
    """Không có arg: xếp hạng các style (hoặc mục đích) theo điểm người dùng. Có arg: bằng chứng gu bên trong nó."""
    word = {"style": "style", "muc_dich": "mục đích"}[cat]
    canon = canonical_tags(p).get(cat, [])
    warn = []
    stats, rated, _ = collect(rounds, warn)
    rows = summarize(stats)
    style_rows = {r["tag"]: r for r in rows if r["category"] == cat}
    if not arg:
        print(f"# {word.capitalize()} theo gu của bạn (điểm trung bình, số mẫu)")
        for r in sorted(style_rows.values(), key=lambda r: -r["mean"]):
            print(f'- `{r["tag"]}`: {r["mean"]:.2f} ({r["n"]} mẫu, {r["status"]}, tin cậy {r["confidence"]})')
        untested = [t for t in canon if t not in style_rows]
        if untested:
            print("\nChưa có mẫu nào được chấm: " + ", ".join(untested))
        return
    if canon and arg not in canon:
        print(f"Không có {word} `{arg}`. Các {word}: " + ", ".join(canon))
        sys.exit(1)
    sub = []
    for r in rounds:
        ss = [s for s in r.get("samples", []) if arg in ((s.get("breakdown") or {}).get(cat) or {}).get("tags", [])]
        if ss:
            sub.append({**r, "samples": ss})
    print(f"# {word.capitalize()} `{arg}`")
    sr = style_rows.get(arg)
    if sr:
        print(f'Điểm của bạn cho {word} này: {sr["mean"]:.2f} ({sr["n"]} mẫu, {sr["status"]}, tin cậy {sr["confidence"]})')
        if sr["mean"] <= 2.0:
            print(f"CẢNH BÁO: bạn đã chấm thấp {word} này - hỏi lại người dùng trước khi thiết kế theo nó.")
    else:
        print(f"Chưa có mẫu nào của {word} này được chấm - chỉ dùng mặc định trong " + ("styles.md" if cat == "style" else "purposes.md") + " + rule chung.")
    for r in sub:
        for s in r["samples"]:
            rt = s.get("rating") or {}
            print(f'- {s["id"]} {s.get("title","")}: {rt.get("overall","chưa chấm")} {("· " + rt["note"]) if rt.get("note") else ""}')
    if sub:
        st2, _, _ = collect(sub, [])
        inner = [r for r in summarize(st2) if r["category"] != cat]
        print(f"\n## Trong {word} này, bạn thích / ghét")
        for r in inner:
            if r["mean"] >= 4 or r["mean"] <= 2:
                mark = "thích" if r["mean"] >= 4 else "ghét"
                print(f'- {CAT_NAME[r["category"]]} `{r["tag"]}`: {r["mean"]:.2f} ({mark}, {r["n"]} mẫu)')
                for nt in r["notes"][:2]:
                    print(f"    · {nt}")
    print(f"\n## Rule chung (mọi {word})")
    hard = [h for r in rounds for h in r.get("hard_rules", [])]
    for h in hard:
        print(f"- LUẬT CỨNG: {h}")
    for r in rows:
        if r["category"] != cat and r["status"] in ("Nên", "Tránh") and r["confidence"] != "thấp":
            print(f'- {r["status"]}: {CAT_NAME[r["category"]]} `{r["tag"]}` ({r["mean"]:.2f}, tin cậy {r["confidence"]})')


STYLES_DIR = os.path.expanduser("~/.claude/skills/motion-styles")


def cmd_style_feedback(p, rounds, arg):
    """Đặc điểm người dùng thích/ghét trong từng style (từ điểm chấm) -> đề xuất luật riêng cho motion-styles/<style>/.

    Chỉ dùng điểm riêng theo category (+ / - trên trang chấm) và mẫu "Rất thích" / "Không bao giờ". Ghi đề xuất vào
    motion-styles/<style>/taste-proposals.md để người dùng duyệt; KHÔNG sửa rules.md.
    """
    only = int(arg) if arg and str(arg).isdigit() else None
    have = set()
    if os.path.isdir(STYLES_DIR):
        act = os.path.join(STYLES_DIR, "ACTIVE")  # chỉ style đang dùng (motion-styles/ACTIVE)
        ids = [l.strip() for l in open(act, encoding="utf-8") if l.strip() and not l.startswith("#")] if os.path.exists(act) else os.listdir(STYLES_DIR)
        have = set(d for d in ids if os.path.exists(os.path.join(STYLES_DIR, d, "rules.md")))
    per, missing = {}, {}
    for r in rounds:
        if only and r.get("round") != only:
            continue
        for s in r.get("samples", []):
            rt = s.get("rating") or {}
            if not valid_score(rt.get("overall")) and not rt.get("categories"):
                continue
            bd = s.get("breakdown") or {}
            for st in (bd.get("style") or {}).get("tags", []):
                target = per if st in have else missing
                target.setdefault(st, []).append((r.get("round"), s, rt))
    today = datetime.date.today().isoformat()
    print(f"# Đặc điểm theo style từ điểm chấm motion-taste" + (f" (vòng {only})" if only else " (mọi vòng)"))
    for st, items in sorted(per.items()):
        rules = open(os.path.join(STYLES_DIR, st, "rules.md"), encoding="utf-8").read()
        like, avoid, whole = [], [], []
        for rnd, s, rt in items:
            sid, cats, note = s["id"], rt.get("categories") or {}, rt.get("note") or ""
            known = sid in rules
            for c, v in cats.items():
                sc = norm_score(v)
                if sc is None or c not in (s.get("breakdown") or {}):
                    continue
                b = s["breakdown"][c]
                line = f'- {CAT_NAME.get(c, c)}: {b.get("note") or ", ".join(b.get("tags", []))} ({sid}, {CAT_NAME.get(c, c)} {"+" if sc >= 4 else "-"}, tổng {rt.get("overall")})' + (" · mẫu này đã được dẫn trong rules.md" if known else "")
                (like if sc >= 4 else avoid if sc <= 2 else []).append(line)
            ov = rt.get("overall")
            if (valid_score(ov) and (ov >= 5 or ov <= 2)) or note:
                whole.append(f'- {sid} "{s.get("title","")}" · tổng {ov}' + (f' · ghi chú: "{note}"' if note else "") + f' · {s.get("summary","")}' + (" · mẫu này đã được dẫn trong rules.md" if known else ""))
        out = [f"# Đề xuất từ motion-taste cho style `{st}` (chờ duyệt)", f"Tạo {today} bởi `taste.py style-feedback`. Duyệt từng dòng rồi mới ghi vào `rules.md` (nguồn: mã mẫu motion-taste).", "",
               "## Đặc điểm bạn thích (category +) → ứng viên Nên", *(like or ["- (chưa có)"]), "",
               "## Đặc điểm bạn không thích (category -) → ứng viên Tránh", *(avoid or ["- (chưa có)"]), "",
               "## Mẫu Rất thích / Không thích / Không bao giờ / có ghi chú → ngữ cảnh (≤ 2 điểm là ứng viên Tránh cả mẫu)", *(whole or ["- (chưa có)"]), ""]
        with open(os.path.join(STYLES_DIR, st, "taste-proposals.md"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(out))
        new = sum(1 for l in like + avoid if "đã được dẫn" not in l)
        print(f"- `{st}`: {len(items)} mẫu · {len(like)} đặc điểm thích, {len(avoid)} không thích ({new} mới) → motion-styles/{st}/taste-proposals.md")
    if missing:
        print("\nStyle có mẫu chấm nhưng không nằm trong các style đang dùng của motion-styles (bỏ qua; chỉ tạo/bật khi người dùng muốn):")
        for st, items in sorted(missing.items()):
            print(f"- `{st}`: {len(items)} mẫu ({', '.join(s['id'] for _, s, _ in items)})")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["status", "new-round", "coverage", "audit", "export", "import-ratings", "style", "purpose", "style-feedback"])
    ap.add_argument("arg", nargs="?", help="export: số vòng · import-ratings: file JSON điểm · style/purpose: id (bỏ trống để xếp hạng)")
    ap.add_argument("--dir", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    a = ap.parse_args()
    p = paths(a.dir)
    rounds = load_rounds(p)
    if a.cmd == "export":
        return cmd_export(p, rounds, a.arg)
    if a.cmd == "import-ratings":
        return cmd_import(p, rounds, a.arg)
    if a.cmd == "style":
        return cmd_style(p, rounds, a.arg)
    if a.cmd == "style-feedback":
        return cmd_style_feedback(p, rounds, a.arg)
    if a.cmd == "purpose":
        return cmd_style(p, rounds, a.arg, "muc_dich")
    {"status": cmd_status, "new-round": cmd_new_round, "coverage": cmd_coverage, "audit": cmd_audit}[a.cmd](p, rounds)


if __name__ == "__main__":
    main()
