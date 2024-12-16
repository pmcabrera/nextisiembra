// // Seleccionamos el aside y el botón de cierre
// const aside = document.querySelector('aside');
// const closeButton = document.querySelector('.close-btn');
// const calculatorIcon = document.querySelector('.picker-link');

// // Función para abrir el aside (cambia a clase 'open')
// function openAside() {
//     aside.classList.add('open');
//     aside.classList.remove('close');
// }

// // Función para cerrar el aside (cambia a clase 'close')
// function closeAside() {
//     aside.classList.add('close');
//     aside.classList.remove('open');
// }

// // Evento para cuando se hace clic en el ícono de la calculadora
// calculatorIcon.addEventListener('click', openAside);

// // Evento para cuando se hace clic en la 'X'
// closeButton.addEventListener('click', closeAside);

document.addEventListener('DOMContentLoaded', () => {
    const aside = document.querySelector('aside');
    const closeButton = document.querySelector('.close-btn');

    console.log('estoy en js'); // Para verificar que el JS se está ejecutando

    // Maneja el clic en el botón de cerrar
    if (closeButton) {
        closeButton.addEventListener('click', (event) => {
            event.stopPropagation(); // Evita que el clic en el botón cierre el aside
            aside.classList.remove('open'); // Cambia a estado closed
            aside.classList.add('close'); // Asegúrate de que esté en estado closed
        });
    } else {
        console.error('El botón de cierre no se encontró.'); // Mensaje de error si no se encuentra
    }

    // Maneja el clic en el aside para abrirlo
    aside.addEventListener('click', () => {
        aside.classList.remove('close'); // Asegúrate de que esté en estado abierto
        aside.classList.add('open'); // Cambia a estado open
    });

    // Cierra el aside al hacer scroll
    window.addEventListener('scroll', () => {
        if (aside.classList.contains('open')) {
            aside.classList.remove('open'); // Cambia a estado closed
            aside.classList.add('close'); // Asegúrate de que esté en estado closed
        }
    });
});

document.addEventListener('visibilitychange', function() {
    const video = document.getElementById('video-background');
    if (document.visibilityState === 'visible' && video.paused) {
        video.play(); // Reinicia el video si está pausado
    }
});


document.querySelectorAll('input[name="tecnologia"]').forEach(radio => {
    radio.addEventListener('change', function() {
        // Remover la clase 'active' de todos los elementos .border-radio
        document.querySelectorAll('.border-radio').forEach(div => {
            div.classList.remove('active');
        });
        
        // Agregar la clase 'active' al div padre del radio seleccionado
        if (this.checked) {
            this.closest('.border-radio').classList.add('active');
        }
    });
});

