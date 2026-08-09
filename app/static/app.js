async function refresh() {
  const response = await fetch('/api/system');
  const data = await response.json();

  document.getElementById('cpu').textContent = `${data.cpu_percent}%`;
  document.getElementById('memory').textContent = `${data.memory_percent}%`;
  document.getElementById('disk').textContent = `${data.disk_percent}%`;
  document.getElementById('host').textContent = data.hostname;

  const network = document.getElementById('network');
  network.innerHTML = data.network.length
    ? data.network.map(item => `<div class="network-row"><span>${item.interface}</span><code>${item.address}</code></div>`).join('')
    : '<p>No IPv4 interface found.</p>';
}

refresh();
setInterval(refresh, 5000);
