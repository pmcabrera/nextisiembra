(function($) {
	$(document).ready(function() {
		"use strict";
		
	// DROPDOWN TOGGLE 
    $('.site-navigation .inner ul li a').on('click', function (e) {
      $(this).parent().children('.site-navigation .inner ul li ul').toggle();
      return true;
    });
		
		
	// DATA BACKGROUND IMAGE
			var pageSection = $(".bg-image");
			pageSection.each(function(indx){
				if ($(this).attr("data-background")){
					$(this).css("background-image", "url(" + $(this).data("background") + ")");
				}
			});
		
		
		// HAMBURGER MENU
		$('.hamburger').on('click', function(e) {
			if ($(".site-navigation").hasClass("active")) {
				$(".hamburger").toggleClass("open");
				$("body").toggleClass("overflow");
				$(".site-navigation").removeClass("active");
				$(".site-navigation").css("transition-delay", "0.9s");
				$(".site-navigation .inner").css("transition-delay", "0s");
				$(".site-navigation .bottom").css("transition-delay", "0.1s");
				$(".site-navigation .layers span:nth-child(1)").css("transition-delay", "0.35s");
				$(".site-navigation .layers span:nth-child(2)").css("transition-delay", "0.50s");
				$(".site-navigation .layers span:nth-child(3)").css("transition-delay", "0.65s");
			} else
			{
				$(".site-nagivation").addClass('active');
				$(".hamburger").toggleClass("open");
				$("body").toggleClass("overflow");
				$(".site-navigation").toggleClass("active");
				$(".site-navigation").css("transition-delay", "0s");
				$(".site-navigation .inner").css("transition-delay", "0.65s");
				$(".site-navigation .bottom").css("transition-delay", "0.80s");
				
			}
			$(this).toggleClass("active");
		});
		
		
		
		
		// PAGE TRANSITION
			$('body a').on('click', function(e) {
				var target = $(this).attr('target');
				var fancybox = $(this).data('fancybox');
				var url = this.getAttribute("href"); 
				if ( target != '_blank' && typeof fancybox == 'undefined' && url.indexOf('#') < 0  ){
					e.preventDefault(); 
						var url = this.getAttribute("href"); 
						if( url.indexOf('#') != -1 ) {
							var hash = url.substring(url.indexOf('#'));

					if( $('body ' + hash ).length != 0 ){
					$('.page-transition').removeClass("active");

					}
					}
					else {
					$('.page-transition').toggleClass("active");
					setTimeout(function(){
					window.location = url;
					},1300); }}
			});



	// SWITHER
			$('.switcher .holder').on('click', function(e) {
			$(this).toggleClass("switch");
			$('.pricing-block').toggleClass("change");
			});

	


	// PARALLAX
			$.stellar({
				horizontalScrolling: false,
				verticalOffset: 0,
				responsive:true
			});
		
		
		
		
	// CONTACT FORM INPUT LABEL
			function checkForInput(element) {
			  const $label = $(element).siblings('span');
			  if ($(element).val().length > 0) {
				$label.addClass('label-up');
			  } else {
				$label.removeClass('label-up');
			  }
			}

			// The lines below are executed on page load
			$('input, textarea').each(function() {
			  checkForInput(this);
			});

			// The lines below (inside) are executed on change & keyup
			$('input, textarea').on('change keyup', function() {
			  checkForInput(this);  
			});
		
		


		
		});
	// END DOCUMENT READY


	var swiper = new Swiper('.carousel-slider', {
		  slidesPerView: 'auto',
		  spaceBetween: 5,
				centeredSlides: true,
				loop: true,
			navigation: {
				nextEl: '.swiper-button-next',
				prevEl: '.swiper-button-prev',
				},
		  pagination: {
			el: '.swiper-pagination',
			clickable: true,
		  }
		});
	
	
	
	
	
	var swiper = new Swiper('.simple-slider', {
      slidesPerView: 1,
      spaceBetween: 0,
			centeredSlides: true,
			loop: true,
		navigation: {
			nextEl: '.swiper-button-next',
			prevEl: '.swiper-button-prev',
			}
    });
	
	
	
	// COUNTER
			 $(document).scroll(function(){
				$('.odometer').each( function () {
					var parent_section_postion = $(this).closest('section').position();
					var parent_section_top = parent_section_postion.top;
					if ($(document).scrollTop() > parent_section_top - 300) {
						if ($(this).data('status') == 'yes') {
							$(this).html( $(this).data('count') );
							$(this).data('status', 'no')
						}
					}
				});
			});
	
	



	// WOW ANIMATION 
			wow = new WOW(
			{
				animateClass: 'animated',
				offset:       50
			}
			);
			wow.init();
	
	
	
	
	// PRELOADER
$(window).load(function() {
  $("body").addClass("page-loaded");
});
	

//counter
document.addEventListener('DOMContentLoaded', () => {
	const counters = document.querySelectorAll('.counter');
  
	// Función que incrementa los números
	function startCounter(counter) {
	  const target = +counter.getAttribute('data-target');  // Obtener el valor objetivo
	  let count = 0;
	  const speed = 500;  // Velocidad del contador en milisegundos
  
	  function updateCounter() {
		const increment = target / speed;
		if (count < target) {
		  count = Math.ceil(count + increment);  // Aumenta el contador
		  counter.textContent = count;  // Actualiza el contenido del contador
		  setTimeout(updateCounter, 1);  // Llama nuevamente a la función para continuar
		} else {
		  counter.textContent = target;  // Asegura que el contador se detenga en el valor final
		}
	  }
  
	  updateCounter();  // Llama a la función al inicio
	}
  
	// Configuración del Intersection Observer
	const observer = new IntersectionObserver((entries, observer) => {
	  entries.forEach(entry => {
		// Si el contador es visible
		if (entry.isIntersecting) {
		  const counter = entry.target;
		  startCounter(counter);  // Inicia el contador
		  observer.unobserve(counter);  // Deja de observar el elemento para evitar que el contador se reinicie continuamente
		}
	  });
	}, {
	  threshold: 0.5 // Se activa cuando el 50% del contador es visible en la pantalla
	});
  
	// Observa cada uno de los contadores
	counters.forEach(counter => {
	  observer.observe(counter);
	});
  });
  
	
})(jQuery);


document.addEventListener('DOMContentLoaded', function () {
	const swiper = new Swiper('.testimonials-slider', {
	  loop: true,  // Permite el desplazamiento circular (bucle)
	  centeredSlides: true,  // Centra la diapositiva activa
	  slidesPerView: 1.5,  // Muestra parcialmente las diapositivas adyacentes
	  spaceBetween: 20,  // Espacio entre las diapositivas
	  navigation: {
		nextEl: '.swiper-button-next2',  // Flecha siguiente
		prevEl: '.swiper-button-prev2',  // Flecha anterior
	  },
	});
  });
  
  
  

