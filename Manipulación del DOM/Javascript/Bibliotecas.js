//* ¿Por qué usar bibliotecas para manipular el DOM?

//* Abstracción: Las bibliotecas proporcionan una capa de abstracción sobre el DOM nativo, ocultando los detalles más complejos y ofreciendo una API más intuitiva.

//* Facilidad de uso: Muchas tareas comunes, como seleccionar elementos, modificar estilos, manejar eventos y realizar animaciones, se vuelven mucho más sencillas con las bibliotecas.

//* Mayor eficiencia: Algunas bibliotecas optimizan la manipulación del DOM, lo que puede mejorar el rendimiento de tus aplicaciones.

//* Funcionalidades adicionales: Además de las operaciones básicas del DOM, las bibliotecas suelen ofrecer funcionalidades adicionales como AJAX, efectos especiales, herramientas de desarrollo y más.

//* Bibliotecas populares para manipular el DOM:

//* jQuery: La biblioteca más conocida y utilizada durante muchos años. Aunque su uso ha disminuido con el auge de los frameworks modernos, sigue siendo una excelente opción para proyectos más pequeños
//* o como base para aprender los conceptos básicos de la manipulación del DOM.

//* React: Un framework de JavaScript para construir interfaces de usuario. Utiliza un DOM virtual para mejorar el rendimiento y ofrece un enfoque declarativo para la construcción de componentes.

//* Angular: Otro framework popular que también utiliza un DOM virtual y ofrece una arquitectura más estructurada para el desarrollo de aplicaciones web a gran escala.

//* Vue.js: Un framework progresivo que se enfoca en la facilidad de uso y la flexibilidad. Ofrece una sintaxis clara y concisa para manipular el DOM.

//* Svelte: Un compilador que convierte componentes personalizados en código JavaScript eficiente, evitando la manipulación directa del DOM en tiempo de ejecución.

//* Ejemplo de Jquery:

//*Cómo importar o "Instalar la librería"

<script
  src="https://code.jquery.com/jquery-3.7.1.js"
  integrity="sha256-eKhayi8LEQwp4NKxN+CfCh+3qOVUtJn3QNZ0TciWLP4="
  crossorigin="anonymous"
></script>;

$(document).ready(function () {
  // Seleccionar un elemento por ID
  $("#miElemento").click(function () {
    // Cambiar el color de fondo del elemento
    $(this).css("background-color", "blue");
  });
});

//* Ejemplos de Jquery (Página WEB)

//* DOM Traversal and Manipulation:
//* Get the <button> element with the class 'continue' and change its HTML to 'Next Step...';

$("button.continue").html("Next Step...");

//* Event Handling:
//* Show the #banner-message element that is hidden with display:none in its CSS when any button in #button-container is clicked.

var hiddenBox = $("#banner-message");
$("#button-container button").on("click", function (event) {
  hiddenBox.show();
});

//* Ajax
//* Call a local script on the server /api/getWeather with the query parameter zipcode=97201 and replace the element #weather-temp's html with the returned text.

$.ajax({
  url: "/api/getWeather",
  data: {
    zipcode: 97201,
  },
  success: function (result) {
    $("#weather-temp").html("<strong>" + result + "</strong> degrees");
  },
});
