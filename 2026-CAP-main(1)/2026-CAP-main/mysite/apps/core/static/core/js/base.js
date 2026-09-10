const main = document.querySelector('main')

main.addEventListener('scroll', () => {
    sessionStorage.setItem(
        'scrollPositionMain',
        main.scrollTop
    );
});

const scrollPositionMain = sessionStorage.getItem('scrollPositionMain');

if (scrollPositionMain !== null) {
    gradeEventos.scrollTo(0, parseInt(scrollPositionMain, 10));
}
