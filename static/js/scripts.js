function updateTime() {
    const now = new Date();
    let h = String(now.getHours()).padStart(2, '0');
    let m = String(now.getMinutes()).padStart(2, '0');
    let s = String(now.getSeconds()).padStart(2, '0');
    document.getElementById("liveTime").innerHTML = `${h}:${m}:${s}`;
}
setInterval(updateTime, 1000);
updateTime();
