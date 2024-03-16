// mis_tarjetas.js

function generarTarjetas() {
    // Iterar sobre los tipos (supongo que es una lista de objetos)
         tipos.forEach((tipo) => {
        // Crear un div para cada tarjeta de producto
        const productCardDiv = document.createElement("div");
        productCardDiv.className = "col-12 col-md-4 p-5 mt-3";

        // Crear un enlace con una imagen dentro
        const productImageLink = document.createElement("a");
        productImageLink.href = "#";
        const productImage = document.createElement("img");
        productImage.src = "/static/images/nin.jpeg"; // Ruta a la imagen estática
        productImage.className = "rounded-circle img-fluid border";
        productImage.alt = "zapatos";
        productImageLink.appendChild(productImage);

        // Crear un título para el producto
        const productTitle = document.createElement("h5");
        productTitle.className = "text-center mt-3 mb-3";
        productTitle.textContent = `${tipo.nombre}`;

        // Crear un párrafo para mostrar el precio
        const productPrice = document.createElement("p");
        productPrice.className = "text-center mb-0";
        productPrice.textContent = `Q0${tipo.precio.toFixed(2)}`;

        // Crear un botón para añadir al carrito
        const addToCartButton = document.createElement("a");
        addToCartButton.className = "btn btn-success";
        addToCartButton.textContent = "Añadir al Carrito";

        // Agregar todos los elementos al div de la tarjeta de producto
        productCardDiv.appendChild(productImageLink);
        productCardDiv.appendChild(productTitle);
        productCardDiv.appendChild(productPrice);
        productCardDiv.appendChild(addToCartButton);

        // Agregar la tarjeta de producto al contenedor
        productsCardsContainer.appendChild(productCardDiv);
    });

    // Agregar el contenedor al documento (por ejemplo, al body)
    document.body.appendChild(productsCardsContainer);


}

// Llama a la función cuando sea necesario (por ejemplo, en el evento onload)
window.onload = function () {
    generarTarjetas();
};
