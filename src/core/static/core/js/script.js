const botonProducto1 = document.getElementById("botonAgregarProducto1");
const botonProducto2 = document.getElementById("botonAgregarProducto2");
const botonProducto3 = document.getElementById("botonAgregarProducto3");

const botonGuardar = document.querySelector(".botonGuardar");
const botonEliminar = document.querySelector(".botonEliminar");

const valorProducto1 = document.querySelector(".valorProducto1").textContent;
const valorProducto2 = document.querySelector(".valorProducto2").textContent;
const valorProducto3 = document.querySelector(".valorProducto3").textContent;
const contadorCarrito = document.querySelector(".contadorCarrito");


if (localStorage.getItem('acumuladorCarrito') === null) {
    contadorCarrito.innerHTML = 0;
} else {
    contadorCarrito.innerHTML = localStorage.getItem('acumuladorCarrito');
}


botonProducto1.addEventListener("click", () => {
        let valorAlmacenado = Number(contadorCarrito.textContent);
        valorAlmacenado += Number(valorProducto1);
        contadorCarrito.innerHTML = valorAlmacenado;
});

botonProducto2.addEventListener("click", () => {
        let valorAlmacenado = Number(contadorCarrito.textContent);
        valorAlmacenado += Number(valorProducto2);
        contadorCarrito.innerHTML = valorAlmacenado;
});

botonProducto3.addEventListener("click", () => {
        let valorAlmacenado = Number(contadorCarrito.textContent);
        valorAlmacenado += Number(valorProducto3);
        contadorCarrito.innerHTML = valorAlmacenado;
})


botonGuardar.addEventListener("click", () => {
    localStorage.setItem('acumuladorCarrito', Number(contadorCarrito.textContent));
})

botonEliminar.addEventListener("click", () => {
    localStorage.removeItem('acumuladorCarrito');
    contadorCarrito.innerHTML = 0;
    valor = 0;
})


// Pendiente implementar lógica para deletear
// const deleteUserButton = document.querySelectorAll('.deleteUser');
// deleteUserButton.forEach( button=>{
//     let button = confirm('Desea confirmar?');
//     (button)
//     ? alert('Se elimina el usuario')
//     : alert('No se elimina el usuario')
// });



