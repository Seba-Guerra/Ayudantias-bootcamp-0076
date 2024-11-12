
//* ¿Qué es el DOM y por qué es importante?

//*  El DOM (Document Object Model) es una representación de un documento HTML en forma de árbol de objetos. Cada elemento HTML, atributo y texto se convierte en un nodo en este árbol. Al manipular el DOM, podemos modificar el contenido, la estructura y el estilo de una página web utilizando JavaScript.

//*  ¿Por qué es importante manipular el DOM?

//*  Crear interfaces dinámicas: Puedes cambiar el contenido de una página en respuesta a las acciones del usuario, como mostrar u ocultar elementos, actualizar datos en tiempo real o crear animaciones.
//*  Validar formularios: Puedes verificar que los datos ingresados por el usuario sean correctos antes de enviarlos a un servidor.
//*  Crear aplicaciones web interactivas: Puedes construir aplicaciones complejas que respondan a las interacciones del usuario de manera intuitiva.
//*  Conceptos básicos de la manipulación del DOM:

//* Seleccionar elementos:
getElementById(); //*Selecciona un elemento por su ID.
getElementsByClassName(); //*Selecciona elementos por su clase.
getElementsByTagName(); //*Selecciona elementos por su etiqueta.   
querySelector(); //*Selecciona el primer elemento que coincida con un selector CSS.
querySelectorAll(); //*Selecciona todos los elementos que coincidan con un selector CSS.


//* Crear elementos;

createElement(); //*Crea un nuevo elemento.

//* Agregar y eliminar elementos;
appendChild(); //* Agrega un elemento como último hijo.
insertBefore(); //* Inserta un elemento antes de otro.
removeChild(); //* Elimina un elemento.

//* Modificar contenido:
textContent; //*Establece o devuelve el texto de un nodo.
innerHTML; //*Establece o devuelve el HTML de un nodo.

//* Modificar estilos:

style; //* Modifica los estilos en línea de un elemento.

//* Ejemplos practicos:

//* Seleccionar un elemento por ID
const parrafo = document.getElementById("miParrafo");

//* Cambiar el contenido del párrafo
parrafo.textContent = "¡Hola, mundo!";

//* Crear un nuevo elemento
const nuevoElemento = document.createElement("p");
nuevoElemento.textContent = "Este es un nuevo párrafo.";

//* Agregar el nuevo elemento al cuerpo del documento
document.body.appendChild(nuevoElemento);