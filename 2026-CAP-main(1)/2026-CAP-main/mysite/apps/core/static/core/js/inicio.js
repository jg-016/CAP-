document.addEventListener('DOMContentLoaded', function () {

    const eventos = document.querySelectorAll('.evento-calendario');
    const colunas = document.querySelectorAll('.colunas-datas > div');

    if (!eventos.length || !colunas.length) {
        return;
    }
    const alturaHora = 15;

    eventos.forEach(function (evento) {

        const dataEvento = evento.dataset.data;
        const inicio = evento.dataset.inicio;
        const fim = evento.dataset.fim;
        let colunaEvento = null;
        let indiceColuna = -1;

        colunas.forEach(function (coluna, index) {
            if (coluna.dataset.data === dataEvento) {
                colunaEvento = coluna;
                indiceColuna = index;
            }
        });

        if (!colunaEvento) {
            return;
        }
        const [horaInicio, minutoInicio] =
            inicio.split(':').map(Number);
        const [horaFim, minutoFim] =
            fim.split(':').map(Number);
        const inicioMinutos =
            horaInicio * 60 + minutoInicio;

        const fimMinutos =
            horaFim * 60 + minutoFim;
        const duracao =
            fimMinutos - inicioMinutos;
        const top =
            (inicioMinutos / 60) * alturaHora;
        const altura =
            (duracao / 60) * alturaHora;
        evento.style.top = `${top}px`;
        evento.style.height = `${altura}px`;
        evento.style.left =
            `calc(${indiceColuna} * (100% / 7))`;
        evento.style.width =
            `calc(100% / 7)`;
    });
});