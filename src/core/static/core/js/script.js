const productos = [
    {
        id: 1,
        nombre: 'Producto 1',
        precio: 500
    },
    {
        id: 2,
        nombre: 'Producto 2',
        precio: 1000
    },
    {
        id: 3,
        nombre: 'Producto 3',
        precio: 1500
    },
    {
        id: 4,
        nombre: 'Producto 4',
        precio: 2000
    }
]

contadorCarrito = document.querySelector('.contadorCarrito');
let acumuladorCarrito = 0;

if (localStorage.getItem('acumuladorCarrito') === null) {
    contadorCarrito.innerHTML = 0;
} else {
    contadorCarrito.innerHTML = localStorage.getItem('acumuladorCarrito');
}

const seccionPadre = document.querySelector('.productos');

productos.forEach((producto) => {
    const etiquetaProducto = document.createElement('div');
    etiquetaProducto.className = `producto${producto.id}`
    etiquetaProducto.innerHTML = `
            <span>${producto.nombre}</span>
            <span class="valorProducto${producto.id}">${producto.precio}</span>
            <button id="botonAgregarProducto${producto.id}" data-precio="${producto.precio}">Agregar producto</button>
    `;
    seccionPadre.appendChild(etiquetaProducto);

    const botonComprar = document.getElementById(`botonAgregarProducto${producto.id}`);
    botonComprar.addEventListener('click', () => {
        const precioProducto = parseFloat(botonComprar.getAttribute('data-precio'));
        acumuladorCarrito += precioProducto;
        contadorCarrito.innerHTML = acumuladorCarrito;
    });

});






// botonProducto1.addEventListener("click", () => {
//         let valorAlmacenado = Number(contadorCarrito.textContent);
//         valorAlmacenado += Number(valorProducto1);
//         contadorCarrito.innerHTML = valorAlmacenado;
// });

// botonProducto2.addEventListener("click", () => {
//         let valorAlmacenado = Number(contadorCarrito.textContent);
//         valorAlmacenado += Number(valorProducto2);
//         contadorCarrito.innerHTML = valorAlmacenado;
// });

// botonProducto3.addEventListener("click", () => {
//         let valorAlmacenado = Number(contadorCarrito.textContent);
//         valorAlmacenado += Number(valorProducto3);
//         contadorCarrito.innerHTML = valorAlmacenado;
// })


// botonGuardar.addEventListener("click", () => {
//     localStorage.setItem('acumuladorCarrito', Number(contadorCarrito.textContent));
// })

// botonEliminar.addEventListener("click", () => {
//     localStorage.removeItem('acumuladorCarrito');
//     contadorCarrito.innerHTML = 0;
//     valor = 0;
// })


// Pendiente implementar lógica para deletear
// const deleteUserButton = document.querySelectorAll('.deleteUser');
// deleteUserButton.forEach( button=>{
//     let button = confirm('Desea confirmar?');
//     (button)
//     ? alert('Se elimina el usuario')
//     : alert('No se elimina el usuario')
// });