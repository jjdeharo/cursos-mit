# Capítulo 4: Simetrías

La simetría es un concepto importante en física y matemáticas (¡y en arte!). En este capítulo mostramos cómo las matemáticas de la simetría pueden usarse para simplificar el análisis de los modos normales de sistemas simétricos.

## Vídeos de esta clase (YouTube)

- [Clase 6: Osciladores forzados, resonancia](https://www.youtube.com/watch?v=Ahv7Akj2xs4)
- [Clase 7: Simetría, número infinito de osciladores acoplados](https://www.youtube.com/watch?v=b1eKhyC9TTo)

## Resumen previo

En este capítulo introducimos el concepto formal de simetría o invariancia.

1.  Trabajaremos algunos ejemplos del uso de argumentos de simetría para simplificar el análisis de sistemas oscilantes.

## 4.1 Simetrías

Volvamos al sistema de dos péndulos idénticos acoplados por un muelle, discutido en el capítulo 3, en (3.78)-(3.93). Este sistema simple todavía tiene más que enseñarnos. Se muestra en la figura 4.1. Como en (3.78)-(3.93), ambos bloques tienen masa $m$, ambos péndulos tienen longitud $\ell$ y la constante del muelle es $\kappa$. De nuevo denotamos los pequeños desplazamientos de los bloques hacia la derecha como $x_1$ y $x_2$.

![Figura 4.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh4_ES/fig4.1.png)

Figura 4.1: los dos péndulos acoplados, con los desplazamientos $x_1$ y $x_2$ medidos hacia la derecha.

Encontramos los modos normales de este sistema en el capítulo anterior. Pero, de hecho, podríamos haberlos encontrado aún más fácilmente aprovechando la simetría de este sistema. Si reflejamos este sistema en un plano situado a medio camino entre los dos bloques, obtenemos un sistema completamente equivalente. Decimos que el sistema es «invariante» bajo reflexiones en el plano entre los bloques. Sin embargo, aunque la física no cambia con la reflexión, nuestra descripción del sistema sí se ve afectada: las coordenadas se intercambian. El sistema reflejado se muestra en la figura 4.2. Comparando ambas figuras, podemos describir la reflexión por su efecto sobre los desplazamientos,

$$x_1 \to -x_2\,,\qquad x_2\to -x_1\,. \qquad \text{(4.1)}$$

![Figura 4.2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh4_ES/fig4.2.png)

Figura 4.2: el sistema de péndulos acoplados tras la reflexión en el plano entre ambos; las posiciones 1 y 2 quedan intercambiadas, con los desplazamientos $x_2$ y $x_1$ respectivamente, ambos con signo cambiado.

En particular, si

$$X(t) = \begin{pmatrix}x_1(t)\\x_2(t)\end{pmatrix} \qquad \text{(4.2)}$$

es una solución de las ecuaciones de movimiento del sistema, entonces el vector reflejado,

$$\tilde X(t) \equiv \begin{pmatrix}-x_2(t)\\-x_1(t)\end{pmatrix}\,, \qquad \text{(4.3)}$$

también debe ser una solución, porque el sistema reflejado es en realidad idéntico al original. Aunque esto debe ser así por la física, es útil entender cómo funciona la matemática. Para ver matemáticamente que (4.3) es una solución, definimos la matriz de simetría, $S$,

$$S \equiv \begin{pmatrix}0&-1\\-1&0\end{pmatrix}\,, \qquad \text{(4.4)}$$

de modo que $\tilde X(t)$ se relaciona con $X(t)$ mediante multiplicación matricial:

$$\tilde X(t) = \begin{pmatrix}0&-1\\-1&0\end{pmatrix}\begin{pmatrix}x_1(t)\\x_2(t)\end{pmatrix} = SX(t)\,. \qquad \text{(4.5)}$$

El enunciado matemático de la simetría es la siguiente condición sobre las matrices $M$ y $K$ (dos matrices $A$ y $B$ que satisfacen $AB=BA$ se dice que «conmutan»):

$$MS = SM\,, \qquad \text{(4.6)}$$

y

$$KS = SK\,. \qquad \text{(4.7)}$$

Puede comprobar explícitamente que (4.6) y (4.7) son ciertas. De estas ecuaciones se sigue que, si $X(t)$ es una solución de la ecuación de movimiento,

$$M\,\frac{d^2}{dt^2}X(t) = -K\,X(t)\,, \qquad \text{(4.8)}$$

entonces $\tilde X(t)$ también lo es. Para verlo explícitamente, multiplique ambos lados de (4.8) por $S$:

$$SM\,\frac{d^2}{dt^2}X(t) = -SK\,X(t)\,. \qquad \text{(4.9)}$$

Usando (4.6) y (4.7) en (4.9), obtenemos

$$MS\,\frac{d^2}{dt^2}X(t) = -KS\,X(t)\,. \qquad \text{(4.10)}$$

La matriz $S$ es constante, independiente del tiempo, así que podemos pasarla a través de las derivadas temporales en (4.10), obteniendo

$$M\,\frac{d^2}{dt^2}SX(t) = -K\,SX(t)\,. \qquad \text{(4.11)}$$

Pero ahora, usando (4.5), esta es la ecuación de movimiento para $\tilde X(t)$,

$$M\,\frac{d^2}{dt^2}\tilde X(t) = -K\,\tilde X(t)\,. \qquad \text{(4.12)}$$

Así, como prometimos, (4.6) y (4.7) son los enunciados matemáticos de la simetría de reflexión, porque implican, como acabamos de ver explícitamente, que si $X(t)$ es una solución, $\tilde X(t)$ también lo es.

Note que de (4.6) puede demostrar que

$$M^{-1}S = SM^{-1} \qquad \text{(4.13)}$$

multiplicando ambos lados por $M^{-1}$. Entonces (4.13) puede combinarse con (4.7) para dar

$$M^{-1}KS = SM^{-1}K\,. \qquad \text{(4.14)}$$

Usaremos esto más adelante.

Ahora supongamos que el sistema está en un modo normal, por ejemplo

$$X(t) = A^1\cos\omega_1t\,. \qquad \text{(4.15)}$$

Entonces $\tilde X(t)$ es otra solución. Pero tiene la misma dependencia temporal y, por tanto, la misma frecuencia angular. Por ello debe ser proporcional al mismo vector de modo normal, porque ya sabemos, de nuestro análisis anterior, que las dos frecuencias angulares de los modos normales del sistema son distintas, $\omega_1\neq\omega_2$. Cualquier cosa que oscile con frecuencia angular $\omega_1$ debe ser proporcional al modo normal $A^1$:

$$\tilde X(t) \propto A^1\cos\omega_1t\,. \qquad \text{(4.16)}$$

Así, la simetría implica

$$SA^1 \propto A^1\,. \qquad \text{(4.17)}$$

Es decir, esperamos, por la simetría, que los modos normales sean también autovectores de $S$. Esto debe ser cierto siempre que las frecuencias angulares sean distintas. De hecho, podemos comprobar, examinando las soluciones, que esto es cierto. La constante de proporcionalidad es justamente $-1$,

$$SA^1 = \begin{pmatrix}0&-1\\-1&0\end{pmatrix}A^1 = -A^1\,, \qquad \text{(4.18)}$$

y de forma similar

$$SA^2 = \begin{pmatrix}0&-1\\-1&0\end{pmatrix}A^2 = A^2\,. \qquad \text{(4.19)}$$

Además, podemos invertir el argumento. Si $A$ es un autovector de la matriz de simetría $S$, y si todos los autovalores de $S$ son distintos, entonces, gracias a la simetría (4.13), $A$ es un modo normal. Para verlo, considere el vector $M^{-1}KA$ y hágalo actuar con la matriz $S$. Usando (4.14), vemos que si

$$SA = \beta A \qquad \text{(4.20)}$$

entonces

$$S\,M^{-1}KA = M^{-1}K\,SA = \beta\,M^{-1}KA\,. \qquad \text{(4.21)}$$

En palabras, (4.21) significa que $M^{-1}KA$ es un autovector de $S$ con el mismo autovalor que $A$. Pero si los autovalores de $S$ son todos distintos, entonces $M^{-1}KA$ debe ser proporcional a $A$, lo que significa que $A$ es un modo normal. Matemáticamente, podríamos decirlo así: si los autovectores de $S$ son $A^n$ con autovalores $\beta_n$, entonces

$$SA^n = \beta_nA^n\,,\ \text{y}\ \beta_n\neq\beta_m\ \text{para}\ n\neq m \implies A^n\ \text{son modos normales.} \qquad \text{(4.22)}$$

Resulta que, para las simetrías que nos interesan, los autovalores de $S$ son siempre todos distintos.

Así, incluso si no hubiéramos conocido la solución, podríamos haber usado (4.20) para determinar los modos normales ¡sin molestarnos en resolver el problema de autovalores de la matriz $M^{-1}K$! En lugar de resolver el problema de autovalores

$$M^{-1}K\,A^n = \omega_n^2\,A^n\,, \qquad \text{(4.23)}$$

podemos en cambio resolver el problema de autovalores

$$S\,A^n = \beta_n\,A^n\,. \qquad \text{(4.24)}$$

Podría parecer que simplemente hemos cambiado un problema de autovalores por otro. Pero, de hecho, (4.24) es más fácil de resolver, porque podemos usar la simetría para determinar los autovalores, $\beta_n$, sin necesidad de calcular nunca un determinante. La simetría de reflexión tiene la agradable propiedad de que, si la aplica dos veces, vuelve a donde empezó. Esto se refleja en la propiedad de la matriz $S$,

$$S^2 = I\,. \qquad \text{(4.25)}$$

En palabras, esto significa que aplicar la matriz $S$ dos veces le devuelve exactamente el vector con el que empezó. Multiplicando ambos lados de la ecuación de autovalores, (4.24), por $S$, obtenemos

$$A^n = IA^n = S^2A^n = S\beta_nA^n = \beta_n\,SA^n = \beta_n^2A^n\,, \qquad \text{(4.26)}$$

lo que implica

$$\beta_n^2=1 \quad\text{o}\quad \beta_n=\pm1\,. \qquad \text{(4.27)}$$

Esto ahorra trabajo. Una vez conocidos los autovalores de $S$, es más fácil encontrar los autovectores de $S$. Pero, gracias a la simetría, sabemos que los autovectores de $S$ serán también los modos normales, los autovectores de $M^{-1}K$. Y una vez conocidos los modos normales, es directo encontrar la frecuencia angular haciendo actuar $M^{-1}K$ sobre los autovectores de modo normal.

Lo que hemos visto aquí, en un ejemplo simple, es cómo usar la simetría de un sistema oscilante para determinar los modos normales. En el resto de este capítulo generalizaremos esta técnica a una situación mucho más interesante. La idea siempre es la misma:

Podemos encontrar los modos normales resolviendo el problema de autovalores de la matriz de simetría, $S$, en lugar de $M^{-1}K$. Y podemos usar la simetría para determinar los autovalores. $\qquad \text{(4.28)}$

### 4.1.1 Pulsaciones

*(Referencia al programa interactivo 4-1 del disco de programas del curso original.)*

Los inicios de los fenómenos ondulatorios ya pueden verse en este simple ejemplo. Suponga que ponemos a oscilar el sistema desplazando el bloque 1 una cantidad $d$, manteniendo el bloque 2 fijo en su posición de equilibrio, y luego soltando ambos bloques desde el reposo en $t=0$. La solución general tiene la forma

$$X(t) = A^1(b_1\cos\omega_1t+c_1\sin\omega_1t) + A^2(b_2\cos\omega_2t+c_2\sin\omega_2t)\,. \qquad \text{(4.29)}$$

Las posiciones de los bloques en $t=0$ dan la ecuación matricial:

$$X(0) = \begin{pmatrix}d\\0\end{pmatrix} = A^1b_1+A^2b_2\,, \qquad \text{(4.30)}$$

o

$$\begin{aligned} d&=b_1+b_2\\ 0&=-b_1+b_2 \end{aligned} \implies b_1=b_2=\frac{d}{2}\,. \qquad \text{(4.31)}$$

Como ambos bloques se sueltan desde el reposo, sabemos que $c_1=c_2=0$. Podemos verlo de la misma forma examinando las velocidades iniciales de los bloques:

$$\dot X(0) = \begin{pmatrix}0\\0\end{pmatrix} = \omega_1A^1c_1+\omega_2A^2c_2\,, \qquad \text{(4.32)}$$

o

$$\begin{aligned} 0&=c_1+c_2\\ 0&=-c_1+c_2 \end{aligned} \implies c_1=c_2=0\,. \qquad \text{(4.33)}$$

Así,

$$x_1(t) = \frac{d}{2}(\cos\omega_1t+\cos\omega_2t)\,,\qquad x_2(t) = \frac{d}{2}(\cos\omega_1t-\cos\omega_2t)\,. \qquad \text{(4.34)}$$

Lo notable de esta solución es la forma en que la energía se transfiere por completo del bloque 1 al bloque 2 y de vuelta. Para verlo, podemos reescribir (4.34) como (usando (1.64) y otra identidad similar)

$$x_1(t) = d\cos\bar\omega t\cos\delta\omega t\,,\qquad x_2(t) = d\sin\bar\omega t\sin\delta\omega t \qquad \text{(4.35)}$$

donde

$$\bar\omega = \frac{\omega_1+\omega_2}{2}\,,\qquad \delta\omega = \frac{\omega_2-\omega_1}{2}\,. \qquad \text{(4.36)}$$

Cada uno de los bloques presenta «pulsaciones» (*beats*): oscilan con la frecuencia angular promedio, $\bar\omega$, pero la amplitud de la oscilación cambia con la frecuencia angular $\delta\omega$. Tras un tiempo $\pi/2\delta\omega$, la energía se ha transferido casi por completo del bloque 1 al bloque 2. Este comportamiento se muestra en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-4-1" rel="noopener" target="_blank" title="Animación original de Howard Georgi">4-1</a> de su disco de programas. Note cómo las pulsaciones se producen por la interacción entre los dos modos normales. Cuando los dos modos están en fase para uno de los bloques, de modo que ese bloque se mueve con amplitud máxima, los modos están desfasados $180°$ para el otro bloque, de modo que este último está casi quieto.

La transferencia completa de energía, hacia adelante y hacia atrás, del bloque 1 al bloque 2 es una característica tanto de nuestra condición inicial especial —con el bloque 2 en reposo y en su posición de equilibrio— como de la forma especial de los modos normales que se sigue de la simetría de reflexión. Como veremos con más detalle más adelante, este es el mismo tipo de transferencia de energía que ocurre en los fenómenos ondulatorios.

### 4.1.2 Un ejemplo menos trivial

*(Referencia al programa interactivo 4-2 del disco de programas del curso original.)*

Tome una hoja de sierra para metales, fije un extremo y sujete una masa al otro. Esto forma un buen oscilador con esencialmente un solo grado de libertad (porque la hoja de sierra solo se dobla fácilmente hacia adelante y hacia atrás de una manera). Ahora tome seis hojas idénticas y fije un extremo de cada una en un mismo punto, de modo que las hojas se abran en abanico formando ángulos de $60°$ entre sí desde el centro, orientadas de forma que puedan doblarse hacia adelante y hacia atrás en el plano formado por las hojas. Si coloca una masa en el extremo de cada una, en un patrón hexagonal, tendrá seis osciladores desacoplados. Pero si en su lugar coloca imanes idénticos en los extremos, los osciladores quedarán acoplados entre sí de una forma complicada. Puede ver cómo son las oscilaciones de este sistema en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-4-2" rel="noopener" target="_blank" title="Animación original de Howard Georgi">4-2</a> del disco de programas.

![Figura 4.3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh4_ES/fig4.3.png)

Figura 4.3: sistema de seis osciladores de hoja de sierra acoplados, dispuestos en abanico hexagonal alrededor de un centro común; las flechas indican las direcciones en que se miden los desplazamientos $x_1$ a $x_6$, en sentido antihorario alrededor del hexágono.

Si los desplazamientos respecto a las posiciones de equilibrio simétricas son pequeños, el sistema es aproximadamente lineal. A pesar de la aparente complejidad de este sistema, ¡podemos escribir los modos normales y las frecuencias angulares correspondientes con casi ningún esfuerzo! El truco consiste en aprovechar inteligentemente la simetría de este sistema.

Este sistema se ve exactamente igual si lo rotamos $60°$ alrededor de su centro. Por tanto, deberíamos esforzarnos en analizarlo de una manera manifiestamente simétrica. Etiquetemos las masas de 1 a 6, empezando en cualquier lugar y recorriendo el sistema en sentido antihorario. Sea $x_j$ el desplazamiento en sentido antihorario del $j$-ésimo bloque respecto a su posición de equilibrio. Como de costumbre, dispondremos estas coordenadas en un vector (a partir de aquí, supondremos que el lector está suficientemente acostumbrado a los números complejos como para que no sea necesario distinguir entre una coordenada real y una compleja):

$$X = \begin{pmatrix}x_1\\x_2\\x_3\\x_4\\x_5\\x_6\end{pmatrix}\,. \qquad \text{(4.37)}$$

La operación de simetría de rotación se implementa mediante la sustitución cíclica

$$x_1 \to x_2 \to x_3 \to x_4 \to x_5 \to x_6 \to x_1\,. \qquad \text{(4.38)}$$

Esto puede representarse en notación matricial como

$$X \to SX\,, \qquad \text{(4.39)}$$

donde la matriz de simetría, $S$, es

$$S = \begin{pmatrix} 0&1&0&0&0&0\\ 0&0&1&0&0&0\\ 0&0&0&1&0&0\\ 0&0&0&0&1&0\\ 0&0&0&0&0&1\\ 1&0&0&0&0&0 \end{pmatrix}\,. \qquad \text{(4.40)}$$

Note que los unos en la subdiagonal de la matriz $S$, en (4.40), implementan las sustituciones

$$x_1\to x_2\to x_3\to x_4\to x_5\to x_6\,, \qquad \text{(4.41)}$$

mientras que el 1 de la esquina inferior izquierda cierra el círculo con la sustitución

$$x_6\to x_1\,. \qquad \text{(4.42)}$$

La simetría exige que la matriz $K$ de este sistema tenga la siguiente forma:

$$K = \begin{pmatrix} E&-B&-C&-D&-C&-B\\ -B&E&-B&-C&-D&-C\\ -C&-B&E&-B&-C&-D\\ -D&-C&-B&E&-B&-C\\ -C&-D&-C&-B&E&-B\\ -B&-C&-D&-C&-B&E \end{pmatrix}\,. \qquad \text{(4.43)}$$

Note que todos los elementos diagonales son iguales ($E$), como debe ser por la simetría. El $j$-ésimo elemento diagonal de la matriz $K$ es menos la fuerza por unidad de desplazamiento sobre la $j$-ésima masa debida a su propio desplazamiento. Debido a la simetría, cada una de las masas se comporta exactamente igual cuando se desplaza manteniendo fijas todas las demás. Así, todos los elementos diagonales de la matriz $K$, $K_{jj}$, son iguales. Del mismo modo, la simetría garantiza que el efecto del desplazamiento de cada bloque $j$ sobre su vecino $j\pm1$ (con $j+1\to1$ si $j=6$, y $j-1\to6$ si $j=1$ —véase (4.42)) es exactamente el mismo. Así, los elementos de matriz en la subdiagonal ($B$) son todos iguales, junto con las $B$ de las esquinas. Y así sucesivamente. La matriz $K$ satisface entonces (4.7),

$$SK = KS \qquad \text{(4.44)}$$

que, como vimos en (4.13)-(4.12), es el enunciado matemático de la simetría. De hecho, podemos ir hacia atrás y deducir la matriz simétrica más general consistente con (4.44), y comprobar que debe tener la forma (4.43). Esto lo hará en el problema 4.4.

Debido a la simetría, sabemos que si un vector $A$ es un modo normal, entonces el vector $SA$ también es un modo normal con la misma frecuencia. Esto es físicamente obvio: si el sistema oscila con todas sus partes moviéndose al mismo ritmo de cierta manera, también puede oscilar con las partes rotadas $60°$, pero moviéndose por lo demás de la misma forma, y la frecuencia será la misma. Esto sugiere que busquemos modos normales que se comporten de forma simple bajo la transformación de simetría $S$. En particular, si encontramos los autovectores de $S$ y descubrimos que los autovalores de $S$ son todos distintos, entonces sabemos, por (4.22), que todos los autovectores son modos normales. En el ejemplo anterior, encontramos modos que se reproducían a sí mismos multiplicados por $\pm1$ bajo la simetría. En general, sin embargo, no debemos esperar que los autovalores sean reales, porque los modos pueden involucrar exponenciales complejas. En este caso, debemos buscar modos correspondientes a autovalores complejos de $S$ (aunque incluso esto no es la posibilidad más general —en general, podríamos tener que considerar conjuntos de modos que se transforman unos en otros bajo la multiplicación matricial; esto no es necesario aquí porque las transformaciones de simetría conmutan todas entre sí),

$$SA = \beta A\,. \qquad \text{(4.45)}$$

Como arriba, en (4.25)-(4.27), podemos encontrar los posibles autovalores usando la simetría. Note que, como seis rotaciones de $60°$ nos devuelven al punto de partida, la matriz $S$ satisface

$$S^6 = I\,. \qquad \text{(4.46)}$$

De (4.46) se sigue que $\beta^6=1$. Así, $\beta$ es una raíz sexta de la unidad,

$$\beta=\beta_k=e^{2ik\pi/6} \quad\text{para } k=0\text{ a }5\,. \qquad \text{(4.47)}$$

Entonces, para cada $k$, hay un modo normal

$$S\,A^k = \beta_k\,A^k\,. \qquad \text{(4.48)}$$

Explícitamente,

$$SA^k = \begin{pmatrix}A_2^k\\A_3^k\\A_4^k\\A_5^k\\A_6^k\\A_1^k\end{pmatrix} = \beta_k\cdot\begin{pmatrix}A_1^k\\A_2^k\\A_3^k\\A_4^k\\A_5^k\\A_6^k\end{pmatrix}\,. \qquad \text{(4.49)}$$

Si tomamos $A_1^k=1$, podemos resolver todas las demás componentes,

$$A_j^k = (\beta_k)^{j-1}\,. \qquad \text{(4.50)}$$

Así,

$$\begin{pmatrix}A_1^k\\A_2^k\\A_3^k\\A_4^k\\A_5^k\\A_6^k\end{pmatrix} = \begin{pmatrix}1\\e^{2ik\pi/6}\\e^{4ik\pi/6}\\e^{6ik\pi/6}\\e^{8ik\pi/6}\\e^{10ik\pi/6}\end{pmatrix}\,. \qquad \text{(4.51)}$$

Ahora, para determinar las frecuencias angulares correspondientes a los modos normales, debemos evaluar

$$M^{-1}K\,A^k = \omega_k^2\,A^k\,. \qquad \text{(4.52)}$$

Como ya conocemos la forma de los modos normales, esto es directo. Por ejemplo, podemos comparar las primeras componentes de estos dos vectores:

$$\begin{aligned}
\omega_k^2 &= \left(E-Be^{2ik\pi/6}-Ce^{4ik\pi/6}-De^{6ik\pi/6}-Ce^{8ik\pi/6}-Be^{10ik\pi/6}\right)/m\\
&= \frac{E}{m}-\frac{2B}{m}\cos\frac{k\pi}{3}-\frac{2C}{m}\cos\frac{2k\pi}{3}-(-1)^k\frac{D}{m}\,. \qquad \text{(4.53)}
\end{aligned}$$

Note que $\omega_1^2=\omega_5^2$ y $\omega_2^2=\omega_4^2$. Esto tenía que ser así, porque los modos normales correspondientes son pares complejos conjugados,

$$A^5 = A^{1*}\,,\qquad A^4=A^{2*}\,. \qquad \text{(4.54)}$$

Cualquier modo normal complejo debe formar parte de un par junto con su modo normal complejo conjugado, a la misma frecuencia, de modo que podamos construir modos normales reales a partir de ellos. Esto debe ser así porque los modos normales describen un sistema físico real, cuyos desplazamientos son reales. Los modos reales son combinaciones lineales (véase (1.19)) de los modos complejos,

$$A^k+A^{k*} \quad\text{y}\quad (A^k-A^{k*})/i \quad\text{para } k=1\text{ o }2\,. \qquad \text{(4.55)}$$

Estos modos pueden verse en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-4-2" rel="noopener" target="_blank" title="Animación original de Howard Georgi">4-2</a> del disco de programas.

Note que las soluciones reales, (4.55), no son autovectores de la matriz de simetría $S$. Esto es posible porque las frecuencias angulares no son todas distintas. Sin embargo, los autovalores de $S$ sí son todos distintos, de (4.47). Así, aunque podamos construir modos normales que no sean autovectores de $S$, sigue siendo cierto que todos los autovectores de $S$ son modos normales. Esto es lo que usamos en (4.48)-(4.50) para determinar los $A^n$.

Observamos que (4.55) es otro ejemplo de un principio muy importante, (3.117), que usaremos muchas veces en lo que sigue:

Si $A$ y $A'$ son modos normales de un sistema con la misma frecuencia angular, $\omega$, entonces cualquier combinación lineal, $bA+cA'$, también es un modo normal con la misma frecuencia angular. $\qquad \text{(4.56)}$

Los modos normales con la misma frecuencia pueden combinarse linealmente para dar nuevos modos normales (véase el problema 4.3). Por otro lado, una combinación lineal de dos modos normales con frecuencias distintas no da nada muy simple.

Las técnicas usadas aquí podrían haberse usado para cualquier número de masas en una disposición simétrica similar. Con $N$ masas y simetría bajo rotación de $2\pi/N$ radianes, las $N$-ésimas raíces de la unidad reemplazarían a las raíces sextas de la unidad de nuestro ejemplo. Los argumentos de simetría también pueden usarse para determinar los modos normales en situaciones más interesantes, por ejemplo cuando las masas están en los vértices de un cubo. Pero ese caso es más complicado que el que hemos analizado, porque el orden de las transformaciones de simetría importa —las transformaciones no conmutan entre sí—. Puede que quiera volver a este tema después de haber estudiado algo de teoría de grupos.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Aplicar argumentos de simetría para encontrar los modos normales de sistemas de osciladores acoplados, hallando los autovalores y autovectores de la matriz de simetría.

## Problemas

**4.1.** Demuestre explícitamente que (4.7) se cumple para la matriz $K$, (4.43), del sistema de la figura 4.3, calculando $SK$ y $KS$.

**4.2.** Considere un sistema de seis masas idénticas que pueden deslizar sin fricción sobre un anillo circular de radio $R$, cada una conectada a sus dos vecinas más cercanas mediante muelles idénticos, mostrado en equilibrio en la figura.

![Figura](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh4_ES/figs1.png)

Figura: seis masas idénticas dispuestas simétricamente sobre un anillo circular, conectadas entre sí por muelles idénticos a lo largo del anillo, con los desplazamientos $y_j$ medidos tangencialmente al anillo.

1.  Analice los posibles movimientos de este sistema en la región en la que es lineal (note que esto no es exactamente lo mismo que pequeñas oscilaciones). Para ello, defina variables de desplazamiento adecuadas (de modo que pueda usar un argumento de simetría), encuentre la forma de la matriz $K$ y luego siga el análisis de (4.37)-(4.55). Si lo ha hecho correctamente, debería encontrar que uno de los modos tiene frecuencia cero. Explique el significado físico de este modo. Pista: no intente encontrar la forma de la matriz $K$ directamente a partir de las constantes de los muelles y la geometría —esto es un lío—; en su lugar, deduzca cómo debe ser a partir de argumentos de simetría.

2.  Si en $t=0$ las masas están distribuidas uniformemente alrededor del círculo, pero cada dos masas se mueve con velocidad $v$ (en sentido antihorario) mientras las demás están en reposo, encuentre y describa en palabras el movimiento posterior del sistema.

**4.3.**

1.  Demuestre (4.56).

2.  Demuestre que si $A$ y $A'$ son modos normales correspondientes a frecuencias angulares distintas, $\omega$ y $\omega'$ respectivamente, con $\omega^2\neq\omega'^2$, entonces $bA+cA'$ no es un modo normal a menos que $b$ o $c$ sean cero. Pista: necesitará usar el hecho de que tanto $A$ como $A'$ son vectores no nulos.

**4.4.** Demuestre que (4.43) es la matriz simétrica $6\times6$ más general que satisface (4.44).

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.
