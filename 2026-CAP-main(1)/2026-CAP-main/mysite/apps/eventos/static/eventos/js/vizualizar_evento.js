function abrirModal() {
    document.getElementById("modalEvento").style.display = "flex";
}


function fecharModal() {
    document.getElementById("modalEvento").style.display = "none";
}

const createModal = document.getElementById('eventModal');
const editModal = document.getElementById('editEventModal');
const closeButtons = document.querySelectorAll('.modal .close');
const cancelButtons = document.querySelectorAll('.btn-cancel');
const addEventButtons = document.querySelectorAll('.adicionar-evento');
const editEventButtons = document.querySelectorAll('.editar-evento');
const deleteButton = document.getElementById('edit-delete');

function showModal(modal) {
    if (modal) {
        modal.style.display = 'block';
    }
}

function hideModal(modal) {
    if (modal) {
        modal.style.display = 'none';
    }
}

function closeAllModals() {
    hideModal(createModal);
    hideModal(editModal);
}
function openCreateModal() {
    if (!createModal) return;
    const form = createModal.querySelector('form');
    if (form) {
        form.reset();
    }
    showModal(createModal);
}

function openEditModal(eventData = {}) {
    if (!editModal) return;
    editModal.querySelector('#edit-event-id').value = eventData.id || '';
    editModal.querySelector('#edit-title').value = eventData.title || '';
    editModal.querySelector('#edit-date').value = eventData.date || '';
    editModal.querySelector('#edit-start-time').value = eventData.start_time || '';
    editModal.querySelector('#edit-end-time').value = eventData.end_time || '';
    editModal.querySelector('#edit-description').value = eventData.description || '';

    showModal(editModal);
}

if (addEventButtons.length) {
    addEventButtons.forEach(button => {
        button.addEventListener('click', event => {
            event.preventDefault();
            openCreateModal();
        });
    });
}

if (editEventButtons.length) {
    editEventButtons.forEach(button => {
        button.addEventListener('click', event => {
            event.preventDefault();
            const target = event.currentTarget;
            openEditModal({
                id: target.dataset.eventId,
                title: target.dataset.title,
                date: target.dataset.date,
                start_time: target.dataset.startTime,
                end_time: target.dataset.endTime,
                description: target.dataset.description,
            });
        });
    });
}
closeButtons.forEach(button => button.addEventListener('click', closeAllModals));
cancelButtons.forEach(button => button.addEventListener('click', closeAllModals));

if (deleteButton) {
    deleteButton.addEventListener('click', () => {
        if (confirm('Deseja excluir este evento?')) {
            closeAllModals();
        }
    });
}
window.addEventListener('click', event => {
    if (event.target === createModal || event.target === editModal) {
        closeAllModals();
    }
});
