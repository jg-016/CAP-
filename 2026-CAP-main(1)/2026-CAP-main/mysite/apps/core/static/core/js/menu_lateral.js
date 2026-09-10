const menuLateral = document.querySelector('.menu-lateral')
const calendarios = document.querySelectorAll('.item-menu.calendario')
const turmas = document.querySelectorAll('.item-menu.turma')

menuLateral.addEventListener('scroll', () => {
    sessionStorage.setItem(
        'scrollPositionMenuLateral',
        menuLateral.scrollTop
    );
});


calendarios.forEach((calendario) => {
    const retorno = encodeURIComponent(window.location.pathname);
    const botaoMenu = calendario.querySelector(':scope > .botao-menu');
    const idCalendario = calendario.dataset.idCalendario;

    botaoMenu.addEventListener('click', (event) => {
        event.preventDefault();
        event.stopPropagation();

        window.location.href = `/alterar_visibilidade_calendario/${idCalendario}?next=${retorno}`;
    });
});

turmas.forEach((turma) => {
    const retorno = encodeURIComponent(window.location.pathname);
    const botaoMenu = turma.querySelector(':scope > .botao-menu')
    const idTurma = turma.dataset.idTurma

    botaoMenu.addEventListener('click', (event) => {
        event.preventDefault();
        event.stopPropagation();
        
        window.location.href = `/alterar_visibilidade_turma/${idTurma}?next=${retorno}`;
    })
})

const scrollPositionMenuLateral = sessionStorage.getItem('scrollPositionMenuLateral');

if (scrollPositionMenuLateral !== null) {
    menuLateral.scrollTo(0, parseInt(scrollPositionMenuLateral, 10));
}