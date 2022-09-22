const openSearchForm = document.querySelector(".btn-open-search-form")
const closeSearchForm = document.querySelector(".btn-close-search-form")
const searchFormContainer = document.querySelector(".container-search-form")
const modalOverlay = document.querySelector(".modal-overlay")
const inputSearchBeer = document.getElementById("search-beer")
const menuButtonOpen = document.getElementById("btn-menu-open")
const menuButtonClose = document.getElementById("btn-menu-close")
const headerNav = document.querySelector(".header_nav")
const formSelectOrder = document.getElementById("ordenar")
const selectOptionsOrder = document.querySelectorAll(".select-options-order")
const formOrder = document.getElementById("form-ordenar")
const formOrderButton = document.getElementById("form-ordenar_btn")
const inputOrderValue = document.getElementById("input-order")

openSearchForm.addEventListener("click", ()=> {
    searchFormContainer.classList.add("container-search-form-show")
    modalOverlay.classList.add("modal-overlay-show")
    inputSearchBeer.focus()
})

closeSearchForm.addEventListener("click", ()=> {
    searchFormContainer.classList.remove("container-search-form-show")
    modalOverlay.classList.remove("modal-overlay-show")
})

menuButtonOpen.addEventListener("click", ()=> {
    headerNav.classList.add("header_nav-show")
    modalOverlay.classList.add("modal-overlay-show")
})

menuButtonClose.addEventListener("click", ()=> {
    headerNav.classList.remove("header_nav-show")
    modalOverlay.classList.remove("modal-overlay-show")
})

formSelectOrder.addEventListener("change", ()=> {
    inputOrderValue.value = formSelectOrder.value
    formOrderButton.click()
})