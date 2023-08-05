# Redes - Laboratorio 2 - Primera parte |  Esquema de detección y corrección de errores

## Autores
- Luis Pedro González Aldana
- Axel Leonardo López

## Uso 

## Instrucciones

### Antecedentes
El ruido y los errores de transmisión suceden en toda comunicación, y es parte de los retos al momento de implementar este tipo de sistemas el manejar adecuadamente las fallas que puedan ocurrir. Por lo tanto, a lo largo de la evolución del Internet se han desarrollado distintos mecanismos que sirven tanto para la detección como para la corrección de errores.

### Objetivos 
- Comprender a detalle el funcionamiento de los algoritmos de detección y corrección.
- Implementar los algoritmos de detección y corrección de errores.
- Identificar las ventajas y desventajas de cada uno de los algoritmos

### Desarrollo 
Existen dos grandes familias de algoritmos para el manejo de errores: de detección y de corrección. Ambos tienen sus ventajas y desventajas y son principalmente utilizados en distintos medios.

En este laboratorio se estará revisando al menos un algoritmo de cada uno de ellos, y cada estudiante trabajará la infraestructura para probarlo. El laboratorio será trabajado en parejas y un único trío en caso de ser un número impar de estudiantes. Los mismos grupos trabajarán en la segunda parte del laboratorio. 

#### Implementación de algoritmos
Para esta fase se deberán de implementar mínimo dos algoritmos (uno por cada miembro, o tres en caso del trío). De estos algoritmos, como mínimo, uno debe de ser de corrección de errores y otro de detección de errores. Se debe implementar cada algoritmo en su versión del emisor (cálculo de la información necesaria para verificar la integridad) y del receptor (uso de la información proporcionada por el emisor para comprobar la integridad). Los algoritmos deben implementarse en dos lenguajes de programación distintos, de tal forma que un receptor en lenguaje B pueda validar un mensaje codificado (por el mismo algoritmo) en lenguaje A.
##### Lista de algoritmos sugeridos
**Corrección de errrores** 
- *Código de hamming*: Para cualquier código (n, m) que cumpla $$(m+r+1)<=2^r$$
- *Código de convolucionales (Algoritmo de Viterbi)*: Para cualquier trama de longitud k. La tasa de código es 2:1 (por cada bit de entrada, salen dos). O sea, la salida son 2k bits. 

**Detección de errores**
- *Fletcher checksum*: Para cualquier trama de longitud k, con bloques de 8, 16 o 32. k debe corresponder al bloque utilizazdo (mayor que el bloque, se agregan 0s de padding)
- *CRC-32*: Para cualquier trama de longitud n, $M_n(x)$  y el polinomio estándar para CRC-32 (uno de 32 bits , investigar cual es), donde n>32


##### Emisor
En el caso del emisor se deben seguir los pasos generales: 
1. Solicitar un trama en binario (i.e: "110101")
2. Calcular la información adicional que requiera el algoritmo seleccionado para detectar/corregir errores. 
3. Devolver el mensaje en binario concatenando con la información adicional requerida para la detección/corrección de errores (i.e: "1101010")
##### Receptor
1. Solicitar un mensaje en binario concatenado con la información adicional requerida por el algoritmo. 
2. Realizar la deteccíon/correción de errores utilizando la información adicional proporcionado por el emisor.
3. Devolver la siguiente información correspondiente con cada caso: 
- No se detectaron errores: mostrar le trama receibida
- Se detectaron errores: indicar que la trama se descarta por detectar errores. 
- Se detectaron errores y corrigieron errores: indicar que se corrigieron errores, indicar posición de los bits que se corrigieron y mostrar la trama corrgida.  


### Pruebas
Utilizando los algoritmos implementador realizar pruebas de detección/correción. 

- Utilizar mínnimo **tres tramas distintas sin manipular** en el lado del receptor. Se debe evidenciar que el receptor no detecta errores y muestra la trama. 
- Utilizar mínimo otras tres tramas distintas donde se modifique manualmente un bit al momento de pasarlas al receptor. Se debe evidenciar que el algoritmo detecta/errores los
errores. 
- Utilizar mínimo otras tres tramas distintas donde se modifique manualmente por los
menos dos bits al momento de pasarlas al receptor. Se debe evidenciar que el algoritmo
detecta/corrige los errores. Si el algoritmo no es capaz de detectar alguna de las tramas
con errores, justificar la razón en la discusión del reporte.
- Utilizar una trama modificada especialmente para que el algoritmo del lado del receptor
no sea capaz de detectar error e indicar por qué la trama no fue detectada en la discusión
del reporte

#### Notas
**Las mismas tramas se deben utilizar para ambos algoritmos
**En caso de errores no detectados, sólo pueden justificarse en caso de que sean por una
debilidad del algoritmo, no por errores de implementación del algoritmo.

### Reporte
Al finalizar la actividad debe de realizarse un reporte grupal donde se incluyan las siguientes
secciones:
- Nombres y carnés
- Título de la práctica
- Descripción de la práctica:
1. Incluir explicación de los algoritmos utilizados
- Resultados: 
1. Incluir las tramas utilizadas, las tramas devueltas por el emisor, indicar los bits cambiados de forma manual, y los mensajes del receptor para cada uno de los
casos solicitados
2. Evidenciar sus pruebas con capturas de pantalla, etc..
- Discusión
1. Análisis exhaustivo de los resultados, errores, algoritmos etc..
2. ¿Hubo casos donde no fue posible detectar errores? ¿Por qué?
- Comentario grupal sobre el tema (errores)
- Conclusiones
- Citas y Referencias



## Implementación

### Lenguajes seleccionados
- JavaScript (colocar el archivo javascript_version/index.html en el navegador)
- Python (Correr el archivo python_version/main.py con el comando python main.py)

### Algoritmos 
- Hamming (Correción)
- Fletcher checksum (detección)

### Nota importante
En cada lenguaje se debe implementar dos algoritmos (uno de correción y otro de detección), y por cada algoritmo se debe implementar el caso de un emisor y el caso de un receptor. 
