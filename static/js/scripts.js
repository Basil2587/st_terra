const sidenav = document.querySelector('.sidenav');
const btn = document.querySelector('.btn');
const img_nav = document.querySelector('.img_nav');
const grid_container = document.querySelector('.grid_container');
document.querySelector('.toggle').onclick = function () {
    this.classList.toggle('active');
    sidenav.classList.toggle('active');
    btn.classList.toggle('btn_active');
    img_nav.classList.toggle('img_active');
    grid_container.classList.toggle('grid_active')
}