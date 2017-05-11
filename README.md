## EJERCICIOS

### Ejercicio 1 (Python)

Para este ejercicio primero elaboré una función sencilla para comprobar la funcionalidad (listNumeberChecker). 
A continuación, busqué algoritmos para mejorar la eficiencia hasta pasar de un tiempo de 7.7 segundos en las pruebas a 
0.8 segundos con uno de los algoritmos más eficientes.

El algoritmo usado para hallar los números primos es: 
https://es.wikipedia.org/wiki/Criba_de_Erat%C3%B3stenes

Las funciones usadas están en: 

* Búsqueda de números primos: 
http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188

* Factores y divisores:
http://stackoverflow.com/questions/12421969/finding-all-divisors-of-a-number-optimization

He comprendido estas funciones y he tratado de dar prioridad a la optimización: utilizo el mismo código ya que hacerlo de forma manual o en una función solo cambiaría la sintaxis, el contenido sería el mismo.


### Ejercicio 2 (Ajax & Highcharts)

Este ejercicio me ha costado bastante más, sobre todo entender cómo funciona [Highcharts](https://www.highcharts.com/).
Una vez entendido el funcionamiento a través de ejemplos más básicos continué con el desarrollo. 

El ejercicio se compone principalmente de un script que realiza las siguientes tareas: 

* Obtención de datos de las fuentes indicadas mediante JQuery y Ajax.
* Iteración de cada flujo de datos para obtener un array con los campos deseados. 
* Ordenado de los elementos y construcción de las gráficas.

He tratado de optimizar tiempos de respuesta en la visualización de las interfaces.
