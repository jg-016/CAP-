document.addEventListener('DOMContentLoaded', function () {
    const createModal = document.getElementById('eventModal');
    const editModal = document.getElementById('editEventModal');
    const addEventButtons =
        document.querySelectorAll('.botao-criar-evento');
    const cancelButtons =
        document.querySelectorAll('.botao-cancelar-evento');
    const closeButtons =
        document.querySelectorAll('.modal .close');
    const editEventButtons =
        document.querySelectorAll('.editar-evento');
    const deleteButton =
        document.getElementById('edit-delete');
    function showModal(modal) {
        if (modal) {
            modal.style.display = 'flex';
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

        if (!createModal) {
            return;
        }
        const form = createModal.querySelector('form');
        if (form) {
            form.reset();
        }
        showModal(createModal);
    }

    window.openCreateModal = openCreateModal;

    addEventButtons.forEach(function (button) {

        button.addEventListener('click', function (event) {
            event.preventDefault();
            openCreateModal();
        });
    });
    cancelButtons.forEach(function (button) {

        button.addEventListener('click', function () {
            closeAllModals();
        });

    });
    closeButtons.forEach(function (button) {

        button.addEventListener('click', function () {
            closeAllModals();

        });
    });
    window.addEventListener('click', function (event) {

        if (event.target === createModal) {
            hideModal(createModal);

        }

        if (event.target === editModal) {
            hideModal(editModal);
        }

    });

    function openEditModal(eventData = {}) {

        if (!editModal) {
            return;
        }

        const id =
            editModal.querySelector('#edit-event-id');
        const title =
            editModal.querySelector('#edit-title');
        const date =
            editModal.querySelector('#edit-date');
        const startTime =
            editModal.querySelector('#edit-start-time');
        const endTime =
            editModal.querySelector('#edit-end-time');
        const description =
            editModal.querySelector('#edit-description');

        if (id) {
            id.value = eventData.id || '';
        }
        if (title) {
            title.value = eventData.title || '';
        }
        if (date) {
            date.value = eventData.date || '';
        }
        if (startTime) {
            startTime.value = eventData.start_time || '';
        }
        if (endTime) {
            endTime.value = eventData.end_time || '';
        }
        if (description) {
            description.value = eventData.description || '';
        }
        showModal(editModal);

    }


    editEventButtons.forEach(function (button) {
        button.addEventListener('click', function (event) {

            event.preventDefault();
            const target = event.currentTarget;

            openEditModal({

                id: target.dataset.eventId,
                title: target.dataset.title,
                date: target.dataset.date,
                start_time: target.dataset.startTime,
                end_time: target.dataset.endTime,
                description: target.dataset.description

            });
        });
    });
    if (deleteButton) {

        deleteButton.addEventListener('click', function () {
            if (confirm('Deseja excluir este evento?')) {
                closeAllModals();
            }
        });
    }
    function posicionarEventos() {
        const eventos =
            document.querySelectorAll('.evento-calendario');
        const colunas =
            document.querySelectorAll(
                '.colunas-datas > div'
            );
        const grade =
            document.querySelector('.grade-eventos');
        if (!eventos.length) {
            return;
        }
        if (!colunas.length) {
            return;
        }
        if (!grade) {
            return;
        }
        const alturaGrade =
            grade.clientHeight;
        const minutosDoDia =
            24 * 60;


        eventos.forEach(function (evento) {
            const data =
                evento.dataset.data;
            const inicio =
                evento.dataset.inicio;
            const fim =
                evento.dataset.fim;
            if (!data || !inicio || !fim) {
                return;
            }
            const coluna =
                Array.from(colunas).find(function (coluna) {

                    return coluna.dataset.data === data;

                });
            if (!coluna) {
                return;
            }
            const partesInicio =
                inicio.split(':');
            const partesFim =
                fim.split(':');
            const horaInicio =
                Number(partesInicio[0]);
            const minutoInicio =
                Number(partesInicio[1]);
            const horaFim =
                Number(partesFim[0]);
            const minutoFim =
                Number(partesFim[1]);
            const inicioEmMinutos =
                horaInicio * 60 + minutoInicio;
            const fimEmMinutos =
                horaFim * 60 + minutoFim;
            const top =
                (inicioEmMinutos / minutosDoDia)
                * alturaGrade;
            const height =
                ((fimEmMinutos - inicioEmMinutos)
                / minutosDoDia)
                * alturaGrade;
            evento.style.top =
                `${top}px`;
            evento.style.height =
                `${height}px`;
            evento.style.left =
                `${coluna.offsetLeft + 4}px`;
            evento.style.width =
                `${coluna.offsetWidth - 8}px`;

        });

    }
    posicionarEventos();
    window.addEventListener(
        'resize',
        posicionarEventos
    );


});
