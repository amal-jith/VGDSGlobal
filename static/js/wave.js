function generateWavePath(offset = 0, height = 40, frequency = 1, phase = 0) {
  const points = [];
  const width = 1440;
  for (let x = 0; x <= width; x += 20) {
    const y = Math.sin((x + offset + phase) * 0.01 * frequency) * height + 60;
    points.push(`${x},${y}`);
  }
  return "M" + points.join(" L");
}

let offset = 0;
function animate() {
  offset += 2;
  document.getElementById("wave1").setAttribute("d", generateWavePath(offset, 20, 1, 0));
  document.getElementById("wave2").setAttribute("d", generateWavePath(offset, 30, 0.8, 100));
  document.getElementById("wave3").setAttribute("d", generateWavePath(offset, 15, 1.2, 200));
  requestAnimationFrame(animate);
}
animate();