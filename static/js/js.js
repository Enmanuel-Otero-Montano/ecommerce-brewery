const openSearchForm = document.querySelector(".btn-open-search-form")
const closeSearchForm = document.querySelector(".btn-close-search-form")
const searchFormContainer = document.querySelector(".container-search-form")
const modalOverlay = document.querySelector(".modal-overlay")
const inputSearchBeer = document.getElementById("search-beer")
const menuButton = document.getElementById("btn-menu")
const iconMenuBars = document.querySelector(".icon-menu-open")
const iconMenuClose = document.querySelector(".icon-menu-close")
const headerNav = document.querySelector(".header_nav")

openSearchForm.addEventListener("click", ()=> {
    searchFormContainer.classList.add("container-search-form-show")
    modalOverlay.classList.add("modal-overlay-show")
    inputSearchBeer.focus()
})

closeSearchForm.addEventListener("click", ()=> {
    searchFormContainer.classList.remove("container-search-form-show")
    modalOverlay.classList.remove("modal-overlay-show")
})

menuButton.addEventListener("click", ()=> {
    headerNav.classList.toggle("header_nav-show")
    iconMenuBars.classList.toggle("icon-menu-hide")
    iconMenuClose.classList.toggle("icon-menu-hide")
})