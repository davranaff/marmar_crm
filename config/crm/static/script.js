// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];


let projectBtns = document.querySelectorAll('.modal-project-btn')

projectBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        modal = document.querySelector('#modal-project-' + btn.getAttribute('id'))

        modal.style.display = "block";
    })
})

function closeModal(id) {
    document.querySelector('.modal#' + id).style.display = "none"
}

// When the user clicks on the button, open the modal
btn.onclick = function () {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}


// Get the modal
var editmodal = document.getElementById("EditModal");
``
// Get the button that opens the modal
var editbtn = document.getElementById("Editbtn");

// Get the <span> element that closes the modal
var editspan = document.getElementsByClassName("editclose")[0];

// When the user clicks on the button, open the modal
editbtn.onclick = function () {
    editmodal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
// editspan.onclick = function () {
//     editmodal.style.display = "none";
// }

let burger = document.querySelector('.hamburger-menu')
let burgerMenu = document.querySelector('.burger-menu')
let navbarBurger = document.querySelector('.navbar-burger')



burger.addEventListener('click', () => navbarBurger.style.display = 'inline')
burgerMenu.addEventListener('click', () => navbarBurger.style.display = 'none')


