//todo ¿Qué es un evento?

//todo Un evento es una acción que ocurre en una página web, como hacer clic en un botón, pasar el ratón sobre un elemento o escribir en un campo de texto. Al manejar estos eventos, podemos ejecutar código JavaScript específico en respuesta a cada acción.

//todo ¿Cómo manejar eventos?

//todo Existen varias formas de manejar eventos en JavaScript:

//todo Atributos de eventos en HTML:

//todo Se asignan directamente en la etiqueta HTML del elemento.
Ejemplo: <button onclick="miFuncion()">Haz clic</button>;

//todo Propiedades de eventos en JavaScript:

//todo Se asignan a un elemento después de que haya sido cargado en la página.
Ejemplo: document.getElementById("miBoton").onclick = miFuncion;

//todo Event Listeners:

//todo Son la forma más flexible y recomendada de manejar eventos.
Ejemplo: document
  .getElementById("miBoton")
  .addEventListener("click", miFuncion);

//todo Ejemplo: Event Listener

//todo Seleccionar el botón
const miBoton = document.getElementById("miBoton");

//todo Función que se ejecutará cuando se haga clic en el botón
function miFuncion() {
  alert("¡Hiciste clic en el botón!");
}

//todo Agregar el event listener
miBoton.addEventListener("click", miFuncion);

//todo Tipos de eventos comunes:

//todo click: Se produce cuando se hace clic en un elemento.
//todo mouseover: Se produce cuando el ratón pasa sobre un elemento.
//todo mouseout: Se produce cuando el ratón sale de un elemento.
//todo keydown: Se produce cuando se presiona una tecla.
//todo keyup: Se produce cuando se suelta una tecla.
//todo change: Se produce cuando cambia el valor de un elemento (por ejemplo, un input).
//todo submit: Se produce cuando se envía un formulario.
