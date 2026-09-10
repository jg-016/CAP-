const gradeEventos = document.querySelector('.scroll-container');

gradeEventos.addEventListener('scroll', () => {
    sessionStorage.setItem(
        'scrollYPositionGradeEventos',
        gradeEventos.scrollTop
    );

    sessionStorage.setItem(
        'scrollXPositionGradeEventos',
        gradeEventos.scrollLeft
    );
});

const scrollYPositionGradeEventos = sessionStorage.getItem('scrollYPositionGradeEventos');
const scrollXPositionGradeEventos = sessionStorage.getItem('scrollXPositionGradeEventos');

if (
    scrollYPositionGradeEventos !== null ||
    scrollXPositionGradeEventos !== null
) {
    gradeEventos.scrollTo(
        scrollXPositionGradeEventos !== null
            ? parseInt(scrollXPositionGradeEventos, 10)
            : 0,
        scrollYPositionGradeEventos !== null
            ? parseInt(scrollYPositionGradeEventos, 10)
            : 0
    );
}