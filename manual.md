# Compilador Frankie

Este lenguaje y IDE fueron creados por Francisco Simon y Antonio Alcántara.

### Comprendiendo las secciones

En esta vista hay 4 secciones y 4 botones hasta abajo.

En la seccion verde se agregaran las variables globales que vayamos creando.
En la seccion amarilla se agregaran los vectores globales que vayamos creando.
En la seccion azul se agregaran las nuevas fuciones que vayamos creando.
En la seccion gris se ejectara nuestro programa principal. Este puede ser visto como el "main".

### Ejecutando el codigo

En la seccion inferior existe un boton rojo que dice "Ejecutar", el cual, tomara el codigo que hayamos creado y lo compilara. El resultado de nuestro codigo se ira añadiendo a la parte inferior de los botones.

### Codigo principal

En esta sera ejecutado el codigo principal que ira llamando a otras funciones y ejecutara las operaciones que vayamos añadiendo.

Esta seccion cuenta con sus propios botones que serviran unicamente para esta seccion.
  * Variable. Añadira una variable local a esta seccion a travez de un pop up que nos solicitara un tipo de dato y un nombre para la variable.
  * Operacion. Añadira operaciones personalizadas que queramos hacer. Se abrira un pop-up con un campo de texto para poder escribir lo que se desee.
  * Vector. Boton para crear un vector.
  * Condicion. Este boton nos ayudara a escribir condicionales, que seran usados para redireccionar el flujo del programa. Se abira un pop-up que nos pedira una condicion y posteriormente nos pedira seleccionar si queremos o no agregar otro flujo.
  * Ciclos. Boton para acricar ciclos. Este boton accionara un pop-up que nos solicitara agregar una condicion para saber si seguir dentro de el ciclo o salir.


### Creando una variable

Al momento de dar clic en el boton verde llamado "Variable" se abira un pop-up que servira para agregar variables globales, las cuales, se agregaran a la seccion donde este el boton. En caso de ser el boton inferior, se agregara en la seccion verde.

El pop-up nos pedira seleccionar algun tipo de dato y su nombre. Al dar click al boton de agregar en el pop up, automaticamente se agregara la variable en la seccion correspondiente.

  * Entero. Numeros enteros.
  * Flotantes. Numeros con punto decimal.
  * Booleano. Valores binareos, este puede ser true o false.
  * Frase. Cadena de caracteres, palabras.

### Creando una funcion

Al dar clic en el boton azul de funcion se abrira un pop-up que servira de para agregar una nueva funcion en nuestro programa.

El pop-up nos pedira  seleccionar algun tipo de dato para la funcion, asi como un nombre para esta. Adicionalmente podremos elegir si queremos agregar parametros, para esto eligiremos un tipo de dato y un nombre para cada parametro que desemos agregara.

La funcion se agregara automaticamente a la seccion azul y apareceran botones especiales para esta funcion.

#### Return

Este boton es unico de las funciones y nos ayuda para regresar un valor una vez que se termine de ejectuar todas las lineas de codigo dentro de esta funcion.

### Creando una operacion

Al momento de dar clic en este boton, se accionara un pop-up con un campo de texto para escribir cualquier operacion que deseemos. La siguiente lista son las operaciones posibles.
  * Asignacion : a = 5 ;
  * Suma : a = b + c ;
  * Resta : a = b - c ;
  * Multiplicacion : a = b * c ;
  * Division : a = b / c ;

Se pueden combinar las operaciones como en el siguiente ejemplo:
  * a = b + c - d * e;

Tambien se puede hacer uso de la funcion "print()" para mostrar algun resultado, por ejemplo:
  * print( a ) ;

### Creando una condicion

Al dar clic al boton gris de condicion se abrira un pop-up que nos solicitara una condicion para cumplir. En caso de que la condicion se cumpla se ejecutara lo que este adentro de esas llaves de ese bloque( { } ). Se puede agregar de manera opcional si queiremos agregar otro flujo dando clic a "Si" en la pregunta "Agregar Else ?". Por ultimo, este bloque de codigo se agregara a nuestro codigo y apareceran mas botones para seguir dando continuidad.

### Creando un ciclo
Al dar clic al boton negro que dice "Ciclo" se abrira un pop up, el cual nos pedira una condicion para saber que flujo seguir. Si se sumple la condicion, se ejecutara lo que este dentro de esas llaves de ese bloque( { } ). este bloque de codigo se agregara a nuestro codigo y apareceran mas botones para seguir dando continuidad.
