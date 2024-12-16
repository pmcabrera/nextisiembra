console.log("en script")

document.addEventListener('DOMContentLoaded', function () {
    // Seleccionamos todos los elementos con la clase 'myElement'
    let elements = document.querySelectorAll('.myElement');
    
    // Iteramos sobre cada uno de los elementos
    elements.forEach(function (element) {
        // Accedemos al texto del elemento
        let text = element.textContent;

        // Reemplazamos la segunda aparición de "(VENTA)"
        let ventaCount = 0;
        text = text.replace(/\(VENTA\)/g, function(match) {
            ventaCount++;
            // Solo eliminamos la segunda aparición
            return ventaCount > 1 ? '' : match;
        });

        // Reemplazamos la segunda aparición de "(COMPRA)"
        let compraCount = 0;
        text = text.replace(/\(COMPRA\)/g, function(match) {
            compraCount++;
            // Solo eliminamos la segunda aparición
            return compraCount > 1 ? '' : match;
        });

        // Volvemos a asignar el texto limpio al elemento
        element.textContent = text;

        // Verificamos el resultado
        console.log(element.textContent);
    });
});
