// motion-taste probe: dán nguyên file này vào javascript_tool trên trang đang có video (Vimeo, YouTube…).
// Nó định nghĩa window.__mt(opts) rồi chạy luôn. Kết quả:
//  - đo nhịp: số cú cắt, độ dài shot trung bình, % khung gần như đứng yên trong đoạn [cutStart, cutStart+cutSecs]
//  - phủ lên trang một contact sheet (lưới khung hình có mốc giờ) để chụp MỘT ảnh thay vì nhiều ảnh
// Gọi lại với tuỳ chọn: await __mt({n:12, cutStart:10, cutSecs:15}); bỏ lớp phủ: __mtClose()
window.__mtClose = () => document.getElementById("__mt")?.remove();
window.__mt = async ({ n = 12, cutStart = null, cutSecs = 15 } = {}) => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const vids = [...document.querySelectorAll("video")];
  const v = vids.find(x => x.getBoundingClientRect().width > 50) || vids[0];
  if (!v) return { error: "no video" };
  v.muted = true;
  try { await v.play(); } catch (e) {}
  await sleep(800);
  v.pause();
  const dur = v.duration, W = v.videoWidth || 1280, H = v.videoHeight || 720;
  const ready = async () => { const t0 = Date.now(); while ((v.seeking || v.readyState < 3) && Date.now() - t0 < 12000) await sleep(150); };
  const seek = async t => { v.pause(); v.currentTime = t; await ready(); try { await v.play(); } catch (e) {} await sleep(180); v.pause(); await sleep(120); };
  // 1) nhịp: phát thật trong cutSecs giây, so khác biệt giữa các khung 48x27
  const cs = cutStart ?? Math.min(Math.max(0, dur * 0.2), Math.max(0, dur - cutSecs - 1));
  const c = document.createElement("canvas"); c.width = 48; c.height = 27;
  const g = c.getContext("2d", { willReadFrequently: true });
  v.currentTime = cs; await ready(); try { await v.play(); } catch (e) {}
  let prev = null; const D = []; const tS = Date.now();
  while (v.currentTime < cs + cutSecs && !v.ended && Date.now() - tS < (cutSecs + 6) * 1000) {
    g.drawImage(v, 0, 0, 48, 27);
    let d; try { d = g.getImageData(0, 0, 48, 27).data; } catch (e) { v.pause(); return { error: "canvas tainted" }; }
    if (prev) { let s = 0; for (let i = 0; i < d.length; i += 4) s += Math.abs(d[i] - prev[i]) + Math.abs(d[i + 1] - prev[i + 1]) + Math.abs(d[i + 2] - prev[i + 2]); D.push([v.currentTime, s / (d.length / 4 * 3)]); }
    prev = d.slice(); await sleep(80);
  }
  v.pause();
  const cuts = [];
  for (let i = 0; i < D.length; i++) {
    const w = D.slice(Math.max(0, i - 5), i).map(x => x[1]).sort((a, b) => a - b);
    const med = w.length ? w[Math.floor(w.length / 2)] : 0;
    if (D[i][1] > 45 && D[i][1] > med * 3 && (!cuts.length || D[i][0] - cuts[cuts.length - 1] > 0.25)) cuts.push(+D[i][0].toFixed(2));
  }
  const m = D.map(x => x[1]);
  const span = D.length ? D[D.length - 1][0] - D[0][0] : 0;
  // 2) contact sheet: 3 khung hook (0,3 / 1 / 2 s) + phần còn lại rải đều
  const times = [0.3, 1, 2];
  for (let i = 1; times.length < n; i++) times.push(Math.min(dur - 0.3, 2 + (dur - 2.3) * i / (n - 3)));
  const tall = H > W, cols = tall ? 6 : 4, rows = Math.ceil(n / cols);
  const cw = tall ? 200 : 320, ch = Math.round(cw * H / W);
  const sheet = document.createElement("canvas"); sheet.width = cols * cw; sheet.height = rows * ch;
  const sg = sheet.getContext("2d"); sg.fillStyle = "#111"; sg.fillRect(0, 0, sheet.width, sheet.height);
  sg.font = "bold 15px monospace";
  for (let i = 0; i < times.length; i++) {
    await seek(times[i]);
    const x = (i % cols) * cw, y = Math.floor(i / cols) * ch;
    sg.drawImage(v, x, y, cw - 2, ch - 2);
    const lab = times[i].toFixed(1) + "s"; sg.fillStyle = "rgba(0,0,0,.7)"; sg.fillRect(x, y, 14 + lab.length * 9, 22);
    sg.fillStyle = "#ffd84d"; sg.fillText(lab, x + 6, y + 16);
  }
  window.__mtClose();
  const ov = document.createElement("div"); ov.id = "__mt";
  ov.style.cssText = "position:fixed;inset:0;z-index:2147483647;background:#111;display:flex;align-items:center;justify-content:center";
  sheet.style.cssText = "max-width:100vw;max-height:100vh;width:auto;height:auto";
  ov.appendChild(sheet); document.body.appendChild(ov);
  return {
    dur: +dur.toFixed(1), size: W + "x" + H, times: times.map(t => +t.toFixed(1)),
    pace: { from: +cs.toFixed(1), secs: +span.toFixed(1), cuts: cuts.length, avgShot: cuts.length ? +(span / cuts.length).toFixed(2) : null, cutTimes: cuts,
            motion: Math.round(m.reduce((a, b) => a + b, 0) / (m.length || 1)), stillPct: Math.round(100 * m.filter(x => x < 2).length / (m.length || 1)) }
  };
};
await __mt();
