document.getElementById('calendar-fab').addEventListener('click', openCreateModal);

function openCreateModal() {
  const ws = getWeekStart();
  document.getElementById('titulo').value = '';
  document.getElementById('data').value = dateStr(ws);
  document.getElementById('inicio').value = '08:00';
  document.getElementById('fim').value = '09:00';
  document.getElementById('descricao').value = '';
  document.getElementById('eventModalOverlay').classList.add('open');
}

function closeCreateModal() {
  document.getElementById('eventModalOverlay').classList.remove('open');
}

// Fecha ao clicar fora do modal
document.getElementById('eventModalOverlay').addEventListener('click', function(e) {
  if (e.target === this) closeCreateModal();
});

// Funções auxiliares (copiadas do calendario.html)
function getWeekStart() {
  const start = new Date();
  const dayIndex = start.getDay();
  const diffToSunday = (dayIndex + 1) % 7;
  start.setDate(start.getDate() - diffToSunday);
  return start;
}

function dateStr(date) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}


