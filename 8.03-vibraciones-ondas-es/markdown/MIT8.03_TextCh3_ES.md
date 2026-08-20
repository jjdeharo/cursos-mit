# Capítulo 3: Modos normales

Los sistemas con varios grados de libertad parecen mucho más complicados que el oscilador armónico simple. Lo que veremos en este capítulo es que esto es una ilusión. Cuando lo miramos de la manera adecuada, podemos ver los osciladores simples dentro del sistema más complicado.

## Vídeos de esta clase (YouTube)

- [Clase 4: Osciladores acoplados, modos normales](https://www.youtube.com/watch?v=BX4QPdP7fT8)
- [Clase 5: Modos normales (continuación)](https://www.youtube.com/watch?v=I0YACDaY-ww)

## Resumen previo

En este capítulo discutimos la oscilación armónica en sistemas con más de un grado de libertad.

1.  Escribiremos las ecuaciones de movimiento de un sistema de partículas sometidas a fuerzas restauradoras lineales generales, sin amortiguamiento.
2.  A continuación, introducimos las matrices y la multiplicación de matrices, y mostramos cómo pueden usarse para simplificar la descripción de las ecuaciones de movimiento deducidas en la sección anterior.
3.  Después usaremos la invariancia bajo traslación temporal para encontrar las soluciones irreducibles de las ecuaciones de movimiento en forma matricial. Esto conducirá a la idea de «modos normales». Luego mostraremos cómo combinar los modos normales para construir la solución general de las ecuaciones de movimiento.
4.  - Introduciremos la idea de «coordenadas normales» y mostraremos cómo pueden usarse para automatizar la solución del problema de valores iniciales.
5.  - Discutiremos la oscilación forzada amortiguada en sistemas con muchos grados de libertad.

## 3.1 Más de un grado de libertad

En general, el número de grados de libertad de un sistema es el número de coordenadas independientes necesarias para especificar la configuración del sistema. Cuantos más grados de libertad tenga el sistema, mayor será el número de formas independientes en que puede moverse. Cabría pensar que, cuantos más movimientos posibles, más complicado será analizar el sistema. Sin embargo, usando las herramientas del álgebra lineal, veremos que podemos tratar sistemas con muchos grados de libertad de forma directa.

### 3.1.1 Dos osciladores acoplados

![Figura 3.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh3_ES/fig3.1.png)

Figura 3.1: dos péndulos de longitud $\ell$ colgando de soportes fijos, con sus masas conectadas entre sí por un muelle horizontal.

Considere el sistema de dos péndulos mostrado en la figura 3.1. Los péndulos consisten en varillas rígidas pivotadas en su extremo superior, de modo que oscilan sin fricción en el plano del papel. Las masas en los extremos de las varillas están acopladas por un muelle. Consideraremos el movimiento libre del sistema, sin más fuerzas externas que la gravedad. Este es un ejemplo clásico de dos «osciladores acoplados». El muelle que conecta los dos osciladores es el acoplamiento. Supondremos que el muelle de la figura 3.1 no está estirado cuando los dos péndulos cuelgan verticalmente, como se muestra. Entonces la configuración de equilibrio es la mostrada en la figura 3.1. Este es un ejemplo de un sistema con dos grados de libertad, porque se necesitan dos cantidades —los desplazamientos de cada uno de los dos bloques respecto al equilibrio— para especificar la configuración del sistema. Por ejemplo, si las oscilaciones son pequeñas, podemos especificar la configuración dando el desplazamiento horizontal de cada uno de los dos bloques respecto a la posición de equilibrio.

Suponga que el bloque 1 tiene masa $m_1$, el bloque 2 tiene masa $m_2$, ambos péndulos tienen longitud $\ell$ y la constante del muelle es $\kappa$ (letra griega kappa). Denote los (pequeños) desplazamientos horizontales de los bloques hacia la derecha como $x_1$ y $x_2$, como se muestra en la figura 3.2. Podríamos haber llamado a estas masas y desplazamientos de cualquier otra forma, pero es muy conveniente usar el mismo símbolo, $x$, con subíndices distintos. Entonces podemos escribir la ley de Newton, $F=ma$, en una forma compacta y útil,

$$m_j\,\frac{d^2}{dt^2}x_j = F_j\,, \qquad \text{(3.1)}$$

para $j=1$ a $2$, donde $F_1$ es la fuerza horizontal sobre el bloque 1 y $F_2$ es la fuerza horizontal sobre el bloque 2. Como hay dos valores de $j$, (3.1) representa dos ecuaciones: una para $j=1$ y otra para $j=2$. Estas son las dos ecuaciones de movimiento del sistema con dos grados de libertad. A menudo nos referiremos a todas las masas, desplazamientos o fuerzas a la vez como $m_j$, $x_j$ o $F_j$, respectivamente. Por ejemplo, diremos que $F_j$ es la fuerza horizontal sobre el $j$-ésimo bloque. Este es un ejemplo del uso de «índices» ($j$ es un índice) para simplificar la descripción de un sistema con más de un grado de libertad.

![Figura 3.2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh3_ES/fig3.2.png)

Figura 3.2: los mismos dos péndulos, ahora desplazados de su posición de equilibrio en las cantidades horizontales $x_1$ y $x_2$.

Cuando los bloques se mueven horizontalmente, también se mueven verticalmente, porque la longitud de los péndulos permanece fija. Como el desplazamiento vertical es de segundo orden en las $x_j$,

$$y_j \approx \frac{x_j^2}{2}\,, \qquad \text{(3.2)}$$

podemos ignorarlo al pensar en el muelle. El muelle permanece aproximadamente horizontal para oscilaciones pequeñas.

Para encontrar la ecuación de movimiento de este sistema, debemos encontrar las fuerzas, $F_j$, en función de los desplazamientos, $x_j$. Es la linealidad aproximada del sistema la que nos permite hacer esto de forma útil. Las fuerzas producidas por el muelle (ley de Hooke) y las fuerzas horizontales sobre los péndulos debidas a la tensión de la cuerda (que a su vez se debe a la gravedad) son ambas funciones aproximadamente lineales de los desplazamientos, para desplazamientos pequeños. Además, las fuerzas se anulan cuando ambos desplazamientos son nulos, porque el sistema está en equilibrio.

![Figura 3.3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh3_ES/fig3.3.png)

Figura 3.3: los dos péndulos con el bloque 2 desplazado una cantidad $x_2$ y el bloque 1 mantenido en su posición de equilibrio.

Así, cada una de las fuerzas es cierta constante (distinta para cada bloque) multiplicada por $x_1$, más otra constante multiplicada por $x_2$. Conviene escribir esto así:

$$F_1 = -K_{11}x_1 - K_{12}x_2\,,\qquad F_2 = -K_{21}x_1 - K_{22}x_2\,, \qquad \text{(3.3)}$$

o, más compactamente,

$$F_j = -\sum_{k=1}^{2}K_{jk}\,x_k \qquad \text{(3.4)}$$

para $j=1$ a $2$. Hemos escrito las cuatro constantes como $K_{11}$, $K_{12}$, $K_{21}$ y $K_{22}$ para escribir la fuerza de esta forma compacta. Más adelante llamaremos a estas constantes los elementos de la matriz $K$. Con esta notación, las ecuaciones de movimiento son

$$m_j\,\frac{d^2}{dt^2}x_j = -\sum_{k=1}^{2}K_{jk}\,x_k \qquad \text{(3.5)}$$

para $j=1$ a $2$.

![Figura 3.4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh3_ES/fig3.4.png)

Figura 3.4: fuerzas sobre los dos bloques del sistema de la figura 3.3 — las tensiones $T_1$ y $T_2$ de las cuerdas, las fuerzas del muelle $\kappa x_2$ sobre el bloque 1 y $-\kappa x_2$ sobre el bloque 2, y los pesos $m_1g$ y $m_2g$.

Debido a la linealidad del sistema, podemos encontrar las constantes $K_{jk}$ considerando los desplazamientos de los bloques uno a la vez. Luego encontramos la fuerza total usando (3.4). Por ejemplo, supongamos que desplazamos el bloque 2 manteniendo el bloque 1 fijo en su posición de equilibrio, y observamos las fuerzas sobre ambos bloques. Esto nos permitirá calcular $K_{12}$ y $K_{22}$. El sistema con el bloque 2 desplazado se muestra en la figura 3.3. Las fuerzas sobre los bloques se muestran en la figura 3.4, donde $T_j$ es la tensión de la cuerda del $j$-ésimo péndulo. $F_{12}$ es la fuerza sobre el bloque 1 debida al desplazamiento del bloque 2. $F_{22}$ es la fuerza sobre el bloque 2 debida a su propio desplazamiento. Para desplazamientos pequeños, la fuerza restauradora del muelle es casi horizontal e igual a $\kappa x_2$ sobre el bloque 1 y $-\kappa x_2$ sobre el bloque 2. Asimismo, en el límite de desplazamiento pequeño, la componente vertical de la fuerza de la tensión $T_2$ casi cancela la fuerza gravitatoria sobre el bloque 2, $m_2g$, de modo que la componente horizontal de la tensión da una fuerza restauradora $-x_2m_2g/\ell$ sobre el bloque 2. Para el bloque 1, la fuerza de la tensión $T_1$ simplemente cancela la fuerza gravitatoria $m_1g$. Así,

$$F_{12} \approx \kappa x_2\,,\qquad F_{22} \approx -\frac{m_2g\,x_2}{\ell} - \kappa x_2\,, \qquad \text{(3.6)}$$

y

$$K_{12} \approx -\kappa\,,\qquad K_{22} \approx \frac{m_2g}{\ell}+\kappa\,. \qquad \text{(3.7)}$$

Un argumento análogo muestra que

$$K_{21} \approx -\kappa\,,\qquad K_{11} \approx \frac{m_1g}{\ell}+\kappa\,. \qquad \text{(3.8)}$$

Note que

$$K_{12} = K_{21}\,. \qquad \text{(3.9)}$$

Veremos más abajo que este es un ejemplo de una relación muy general.

### 3.1.2 Linealidad y modos normales

*(Referencia al programa interactivo 3-1 del disco de programas del curso original.)*

Veremos en este capítulo que el movimiento más general posible de este sistema, y de cualquier sistema así de osciladores, puede descomponerse en soluciones particularmente simples, en las que todos los grados de libertad oscilan con la misma frecuencia. Estas soluciones simples se llaman «modos normales». Los desplazamientos del movimiento más general pueden escribirse como sumas de las soluciones simples. Estudiaremos esto en detalle más adelante, pero puede ser útil verlo primero. Para este sistema, el modo normal de frecuencia menor es aquel en el que los desplazamientos de los dos bloques son iguales:

$$x_1(t) = x_2(t) = b_1\cos(\omega_1t-\theta_1)\,. \qquad \text{(3.10)}$$

El otro modo normal es aquel en el que los desplazamientos de los dos bloques son opuestos:

$$x_1(t) = -x_2(t) = b_2\cos(\omega_2t-\theta_2)\,. \qquad \text{(3.11)}$$

La suma de estos dos movimientos simples da el movimiento mucho más complicado que se muestra en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-3-1" rel="noopener" target="_blank" title="Animación original de Howard Georgi">3-1</a>.

### 3.1.3 $n$ osciladores acoplados

Antes de intentar resolver las ecuaciones de movimiento, (3.5), generalicemos la discusión a sistemas con más grados de libertad. Considere la oscilación de un sistema de $n$ partículas conectadas por diversos muelles, sin amortiguamiento. Nuestro análisis será completamente general, pero, por simplicidad, hablaremos de las partículas como si estuvieran obligadas a moverse en la dirección $x$, de modo que podamos medir el desplazamiento de la $j$-ésima partícula respecto al equilibrio con la coordenada $x_j$. Entonces la configuración de equilibrio es aquella en la que todas las $x_j$ son cero.

La ley de Newton, $F=ma$, para el movimiento del sistema da

$$m_j\,\frac{d^2x_j}{dt^2} = F_j \qquad \text{(3.12)}$$

donde $m_j$ es la masa de la $j$-ésima partícula y $F_j$ es la fuerza sobre ella. Como el sistema es lineal, esperamos poder escribir la fuerza de la siguiente forma (como en (3.4)):

$$F_j = -\sum_{k=1}^{n}K_{jk}\,x_k \qquad \text{(3.13)}$$

para $j=1$ a $n$. La constante, $-K_{jk}$, es la fuerza por unidad de desplazamiento de la $j$-ésima partícula debida a un desplazamiento $x_k$ de la $k$-ésima partícula. Note que todas las $F_j$ se anulan en el equilibrio, cuando todas las $x_j$ son cero. Así, las ecuaciones de movimiento son

$$m_j\,\frac{d^2x_j}{dt^2} = -\sum_k K_{jk}\,x_k \qquad \text{(3.14)}$$

para $j=1$ a $n$.

Para medir $K_{jk}$, haga un pequeño desplazamiento $x_k$ de la $k$-ésima partícula, manteniendo fijas en cero a todas las demás partículas (posición supuesta de equilibrio). Luego mida la fuerza, $F_{jk}$, sobre la $j$-ésima partícula, con solo la $k$-ésima partícula desplazada. Como el sistema es lineal (porque está hecho de muelles, o en general, mientras el desplazamiento sea suficientemente pequeño), la fuerza es proporcional al desplazamiento $x_k$. El cociente entre $F_{jk}$ y $x_k$ es $-K_{jk}$:

$$K_{jk} = -F_{jk}/x_k \quad\text{cuando } x_\ell=0 \text{ para } \ell\neq k\,. \qquad \text{(3.15)}$$

Note que $K_{jk}$ se define con un signo $-$, de modo que un $K$ positivo es una fuerza opuesta al desplazamiento, y por tanto tiende a devolver el sistema al equilibrio.

Como el sistema es lineal, la fuerza total debida a un desplazamiento arbitrario es la suma de las contribuciones de cada desplazamiento. Así,

$$F_j = \sum_k F_{jk} = -\sum_k K_{jk}\,x_k\,. \qquad \text{(3.16)}$$

Tratemos ahora de entender (3.9). Si consideramos sistemas sin amortiguamiento, las fuerzas pueden derivarse de una energía potencial,

$$F_j = -\frac{\partial V}{\partial x_j}\,. \qquad \text{(3.17)}$$

Pero entonces, derivando la ecuación (3.16), encontramos que

$$K_{jk} = \frac{\partial^2V}{\partial x_j\partial x_k}\,. \qquad \text{(3.18)}$$

Las derivadas parciales conmutan entre sí, así que la ecuación (3.18) implica

$$K_{jk} = K_{kj}\,. \qquad \text{(3.19)}$$

En palabras: la fuerza sobre la partícula $j$ debida al desplazamiento de la partícula $k$ es igual a la fuerza sobre la partícula $k$ debida al desplazamiento de la partícula $j$.

## 3.2 Matrices

Es muy útil reescribir la ecuación (3.14) en notación matricial. Debido a la linealidad de las ecuaciones de movimiento del movimiento armónico, será muy útil tener a mano las herramientas del álgebra lineal para nuestro estudio de los fenómenos ondulatorios. Si no ha estudiado álgebra lineal (o no entendió gran parte de ella en sus cursos de matemáticas), NO SE ALARME. Empezaremos desde cero, describiendo las propiedades de las matrices y la multiplicación de matrices. Lo importante que debe tener presente es que las matrices no son nada profundo ni mágico: son simplemente herramientas de contabilidad diseñadas para facilitarle la vida cuando trata con más de una ecuación a la vez.

Una matriz es un arreglo rectangular de números. Una matriz $N\times M$ tiene $N$ filas y $M$ columnas. Las matrices pueden sumarse y restarse simplemente sumando y restando cada una de sus componentes. La diferencia surge en la multiplicación. Es muy conveniente definir una ley de multiplicación que defina el producto de una matriz $N\times M$ por la izquierda con una matriz $M\times L$ por la derecha (¡el orden importa!) como una matriz $N\times L$ de la siguiente forma:

Llame $A$ a la matriz $N\times M$, y sea $A_{jk}$ el número en la fila $j$ y columna $k$, para $1\le j\le N$ y $1\le k\le M$. Estas componentes individuales de la matriz se llaman elementos de matriz. En términos de sus elementos, la matriz $A$ se ve así:

$$A = \begin{pmatrix} A_{11} & A_{12} & \cdots & A_{1M}\\ A_{21} & A_{22} & \cdots & A_{2M}\\ \vdots & \vdots & \ddots & \vdots\\ A_{N1} & A_{N2} & \cdots & A_{NM} \end{pmatrix}\,. \qquad \text{(3.20)}$$

Llame $B$ a la matriz $M\times L$, con elementos $B_{kl}$ para $1\le k\le M$ y $1\le l\le L$:

$$B = \begin{pmatrix} B_{11} & B_{12} & \cdots & B_{1L}\\ B_{21} & B_{22} & \cdots & B_{2L}\\ \vdots & \vdots & \ddots & \vdots\\ B_{M1} & B_{M2} & \cdots & B_{ML} \end{pmatrix}\,. \qquad \text{(3.21)}$$

Llame $C$ a la matriz $N\times L$, con elementos $C_{jl}$ para $1\le j\le N$ y $1\le l\le L$:

$$C = \begin{pmatrix} C_{11} & C_{12} & \cdots & C_{1L}\\ C_{21} & C_{22} & \cdots & C_{2L}\\ \vdots & \vdots & \ddots & \vdots\\ C_{N1} & C_{N2} & \cdots & C_{NL} \end{pmatrix}\,. \qquad \text{(3.22)}$$

Entonces la matriz $C$ se define como el producto de matrices $AB$ si

$$C_{jl} = \sum_{k=1}^{M}A_{jk}\cdot B_{kl}\,. \qquad \text{(3.23)}$$

La ecuación (3.23) es el enunciado algebraico de la «regla fila-columna». Para calcular el elemento $j\ell$ de la matriz producto, $AB$, tome la fila $j$ de la matriz $A$ y la columna $\ell$ de la matriz $B$, y forme su producto escalar (correspondiente a la suma sobre $k$ en (3.23)).

Por ejemplo,

$$\begin{pmatrix} 2 & 3\\ 0 & 1\\ 2 & -1 \end{pmatrix} \cdot \begin{pmatrix} 1 & 0 & 2\\ 0 & 1 & 3 \end{pmatrix} = \begin{pmatrix} 2 & 3 & 13\\ 0 & 1 & 3\\ 2 & -1 & 1 \end{pmatrix}\,. \qquad \text{(3.25)}$$

Es fácil comprobar que el producto matricial así definido es asociativo, $(AB)C=A(BC)$. Sin embargo, en general no es conmutativo, $AB\neq BA$. De hecho, si las matrices no son cuadradas, ¡el producto en el orden opuesto puede ni siquiera tener sentido! El producto matricial $AB$ solo tiene sentido si el número de columnas de $A$ coincide con el número de filas de $B$. ¡Cuidado!

Salvo por el hecho de que no es conmutativa, la multiplicación de matrices se comporta de forma muy parecida a la multiplicación ordinaria. Por ejemplo, existen matrices «identidad». La matriz identidad $N\times N$, llamada $I$, tiene ceros en todas partes salvo unos en la diagonal. Por ejemplo, la matriz identidad $3\times 3$ es

$$I = \begin{pmatrix} 1&0&0\\0&1&0\\0&0&1 \end{pmatrix}\,. \qquad \text{(3.26)}$$

La matriz identidad $N\times N$ satisface

$$\begin{aligned}
& IA=AI=A \text{ para cualquier matriz } N\times N,\ A;\\
& IB=B \text{ para cualquier matriz } N\times M,\ B;\\
& CI=C \text{ para cualquier matriz } M\times N,\ C. \qquad \text{(3.27)}
\end{aligned}$$

Nos concentraremos principalmente en matrices «cuadradas» (es decir, $N\times N$).

Las matrices nos permiten manejar muchas ecuaciones lineales a la vez.

Un vector columna de dimensión $N$ puede verse como una matriz $N\times1$. Llamaremos a este objeto un «$N$-vector». No debe confundirse con un vector de coordenadas en el espacio tridimensional. Del mismo modo, podemos pensar en un vector fila de dimensión $N$ como una matriz $1\times N$. La multiplicación matricial también puede describir el producto de una matriz por un vector, dando otro vector. El caso particularmente importante que necesitaremos para analizar los fenómenos ondulatorios involucra matrices cuadradas. Considere una matriz $N\times N$, $A$, que multiplica a un $N$-vector $X$, dando otro $N$-vector $F$. La matriz cuadrada $A$ tiene $N^2$ elementos, $A_{jk}$, para $j$ y $k=1$ a $N$. Los vectores $X$ y $F$ tienen cada uno $N$ componentes, $X_j$ y $F_j$, para $j=1$ a $N$. Entonces la ecuación matricial

$$AX=F \qquad \text{(3.28)}$$

representa en realidad $N$ ecuaciones:

$$\sum_{k=1}^{N}A_{jk}\cdot X_k = F_j \qquad \text{(3.29)}$$

para $j=1$ a $N$. En otras palabras, estas son $N$ ecuaciones lineales simultáneas para las $N$ incógnitas $X_j$. Ya sabe, por sus estudios de álgebra, cómo resolver las $X_j$ en función de las $F_j$ y las $A_{jk}$, pero es muy útil hacerlo en notación matricial. A veces podemos encontrar la «inversa» de la matriz $A$, $A^{-1}$, que tiene la propiedad

$$A\,A^{-1} = A^{-1}A = I\,, \qquad \text{(3.30)}$$

donde $I$ es la matriz identidad discutida en (3.26) y (3.27). Si podemos encontrar tal matriz, entonces las $N$ ecuaciones lineales simultáneas, (3.29), tienen una solución única que podemos escribir de forma muy compacta. Multiplicando ambos lados de (3.29) por $A^{-1}$, y usando (3.30) y (3.27) en el lado izquierdo para eliminar $A^{-1}A$, podemos escribir la solución así:

$$X = A^{-1}F\,. \qquad \text{(3.31)}$$

### 3.2.1 \* Inversa y determinante

Podemos calcular $A^{-1}$ en términos del «determinante» de $A$. El determinante de la matriz $A$ es una suma de productos de los elementos de $A$ con las siguientes propiedades:

- Hay $N!$ términos en la suma;
- Cada término de la suma es un producto de $N$ elementos de matriz distintos;
- En cada producto, cada número de fila y cada número de columna aparece exactamente una vez;
- Cada uno de esos productos puede obtenerse a partir del producto de los elementos diagonales, $A_{11}A_{22}\cdots A_{NN}$, mediante una secuencia de intercambios de las etiquetas de columna. Por ejemplo, $A_{12}A_{21}A_{33}\cdots A_{NN}$ involucra un intercambio, mientras que $A_{12}A_{23}A_{31}A_{44}\cdots A_{NN}$ requiere dos.
- El coeficiente de un producto en el determinante es $+1$ si involucra un número par de intercambios, y $-1$ si involucra un número impar de intercambios.

Así, el determinante de una matriz $2\times2$, $A$, es

$$\det A = A_{11}A_{22} - A_{12}A_{21}\,. \qquad \text{(3.32)}$$

El determinante de una matriz $3\times3$, $A$, es

$$\det A = A_{11}A_{22}A_{33} + A_{12}A_{23}A_{31} + A_{13}A_{21}A_{32} - A_{11}A_{23}A_{32} - A_{13}A_{22}A_{31} - A_{12}A_{21}A_{33}\,. \qquad \text{(3.33)}$$

A menos que tenga muy mala suerte, nunca tendrá que calcular a mano el determinante de una matriz mayor que $3\times3$. Si tiene esa mala suerte, lo mejor es usar un procedimiento inductivo que lo construya a partir de los determinantes de submatrices menores, que discutiremos más abajo.

Si $\det A=0$, la matriz no tiene inversa: no es «invertible». En ese caso, las ecuaciones lineales simultáneas no tienen ninguna solución, o tienen infinitas. Si $\det A\neq0$, la matriz inversa existe y viene dada de forma única por

$$A^{-1} = \frac{\tilde A}{\det A} \qquad \text{(3.34)}$$

donde $\tilde A$ es la matriz de cofactores, definida por sus elementos como sigue:

$$(\tilde A)_{jk} = \det A^{(jk)} \qquad \text{(3.35)}$$

con

$$\begin{aligned}
A^{(jk)}_{\ell m} &= 1 \text{ si } m=j \text{ y } \ell=k;\\
A^{(jk)}_{\ell m} &= 0 \text{ si } m=j \text{ y } \ell\neq k;\\
A^{(jk)}_{\ell m} &= 0 \text{ si } m\neq j \text{ y } \ell=k;\\
A^{(jk)}_{\ell m} &= A_{\ell m} \text{ si } m\neq j \text{ y } \ell\neq k\,.
\end{aligned}$$

En otras palabras, $A^{(jk)}$ se obtiene de la matriz $A$ reemplazando el elemento $kj$ por 1 y todos los demás elementos de la fila $k$ o la columna $j$ por 0.

Por ejemplo, si

$$A = \begin{pmatrix} 4&3\\5&2 \end{pmatrix} \qquad \text{(3.38)}$$

entonces

$$A^{(11)} = \begin{pmatrix} 1&0\\0&2 \end{pmatrix}\,,\qquad A^{(12)} = \begin{pmatrix} 0&3\\1&0 \end{pmatrix}\,,\qquad A^{(21)} = \begin{pmatrix} 0&1\\5&0 \end{pmatrix}\,,\qquad A^{(22)} = \begin{pmatrix} 4&0\\0&1 \end{pmatrix}\,. \qquad \text{(3.39)}$$

Así,

$$\tilde A = \begin{pmatrix} 2&-3\\-5&4 \end{pmatrix} \qquad \text{(3.40)}$$

y como $\det A = 4\cdot2-5\cdot3=-7$,

$$A^{-1} = \begin{pmatrix} -2/7 & 3/7\\ 5/7 & -4/7 \end{pmatrix}\,. \qquad \text{(3.41)}$$

$A^{-1}$ satisface $AA^{-1}=A^{-1}A=I$, donde $I$ es la matriz identidad:

$$I = \begin{pmatrix} 1&0\\0&1 \end{pmatrix}\,. \qquad \text{(3.42)}$$

En términos de las submatrices $A^{(jk)}$, podemos definir el determinante inductivamente, como prometimos. De hecho, la razón por la que (3.30) funciona es que el determinante puede escribirse como

$$\det A = \sum_{k=1}^{N}A_{1k}\,\det A^{(k1)}\,. \qquad \text{(3.43)}$$

De hecho, esto es cierto para cualquier fila, no solo $j=1$. La relación (3.30) puede reescribirse como

$$\sum_{k=1}^{N}A_{jk}\,\det A^{(kj')} = \begin{cases} \det A & \text{para } j=j'\\ 0 & \text{para } j\neq j' \end{cases} \qquad \text{(3.44)}$$

Los determinantes de las submatrices, $\det A^{(k1)}$, en (3.43), pueden a su vez calcularse mediante el mismo procedimiento. El resultado es una definición del determinante que se refiere a sí misma. Sin embargo, el proceso eventualmente termina, porque las matrices se hacen cada vez más pequeñas, y el determinante siempre puede calcularse de esta manera. El único problema de este procedimiento es que es muy tedioso para una matriz grande: para una matriz $n\times n$, hay que calcular y sumar $n!$ términos. Para $n$ grande, esto es impracticable. Una de las ventajas de las técnicas que discutiremos en los próximos capítulos es que podremos evitar tales cálculos.

### 3.2.2 Más hechos útiles sobre matrices

Suponga que $A$ y $B$ son matrices $N\times N$ y $v$ es un $N$-vector.

1.  Si conoce las inversas de $A$ y $B$, puede encontrar la inversa del producto, $AB$, multiplicando las inversas en orden inverso:

$$(AB)^{-1} = B^{-1}A^{-1}\,. \qquad \text{(3.45)}$$

1.  El determinante del producto, $AB$, es el producto de los determinantes:

$$\det(AB) = \det A\,\det B\,, \qquad \text{(3.46)}$$

así que si $\det(AB)=0$, entonces $A$ o $B$ tiene determinante nulo.

1.  Una matriz multiplicada por un vector no nulo solo puede dar cero si el determinante de la matriz se anula:

$$Av=0 \implies \det A=0 \text{ o } v=0\,. \qquad \text{(3.47)}$$

Este es el enunciado, en lenguaje matricial, de que $N$ ecuaciones lineales homogéneas en $N$ incógnitas pueden tener una solución no trivial, $v\neq0$, solo si el determinante de los coeficientes se anula.

1.  De igual modo, si $\det A=0$, existe un vector no nulo, $v$, que es aniquilado por $A$:

$$\det A=0 \implies \exists\, v\neq0 \text{ tal que } Av=0\,. \qquad \text{(3.48)}$$

Este es el enunciado, en lenguaje matricial, de que $N$ ecuaciones lineales homogéneas en $N$ incógnitas sí tienen una solución no trivial, $v\neq0$, si el determinante de los coeficientes se anula.

1.  La transpuesta de una matriz $N\times M$, $A$, denotada $A^T$, es la matriz $M\times N$ obtenida reflejando la matriz respecto a una diagonal que pasa por la esquina superior izquierda. Note que si $N\neq M$, la transposición cambia la forma de la matriz. Solo para matrices cuadradas la transpuesta devuelve una matriz del mismo tipo. Una matriz cuadrada igual a su transpuesta se llama matriz «simétrica».

### 3.2.3 Ecuaciones de autovalores

Haremos un uso extenso del concepto de «ecuación de autovalores». Para una matriz $N\times N$, $R$, la ecuación de autovalores tiene la forma:

$$Rc = hc\,, \qquad \text{(3.51)}$$

donde $c$ es un $N$-vector no nulo, y $h$ es un número. La idea es encontrar tanto el número $h$, llamado el autovalor, como el vector $c$, llamado el autovector. Este es el problema que discutimos en el capítulo 1, en (1.78), en relación con la invariancia bajo traslación temporal, pero ahora escrito en forma matricial.

Un par de ejemplos pueden ser útiles. Suponga que $R$ es una matriz diagonal, como

$$R = \begin{pmatrix} 2&0\\0&1 \end{pmatrix}\,. \qquad \text{(3.52)}$$

Entonces los autovalores son justamente los elementos diagonales, 2 y 1, y los autovectores son los vectores en las direcciones coordenadas,

$$R\begin{pmatrix}1\\0\end{pmatrix} = 2\begin{pmatrix}1\\0\end{pmatrix}\,,\qquad R\begin{pmatrix}0\\1\end{pmatrix} = 1\begin{pmatrix}0\\1\end{pmatrix}\,. \qquad \text{(3.53)}$$

Un ejemplo menos obvio es

$$R = \begin{pmatrix}2&1\\1&2\end{pmatrix}\,. \qquad \text{(3.54)}$$

Esta vez los autovalores son 3 y 1, y los autovectores son los siguientes:

$$R\begin{pmatrix}1\\1\end{pmatrix} = 3\begin{pmatrix}1\\1\end{pmatrix}\,,\qquad R\begin{pmatrix}1\\-1\end{pmatrix} = 1\begin{pmatrix}1\\-1\end{pmatrix}\,. \qquad \text{(3.55)}$$

Puede parecer extraño que, en la ecuación de autovalores, tanto el autovalor como el autovector sean incógnitas. La razón de que esto funcione es que, para la mayoría de los valores de $h$, la ecuación (3.51) no tiene solución. Para verlo, escribimos (3.51) como un conjunto de ecuaciones lineales homogéneas para las componentes del autovector $c$,

$$(R-hI)c = 0\,. \qquad \text{(3.56)}$$

El conjunto de ecuaciones (3.56) tiene soluciones no nulas para $c$ solo si el determinante de la matriz de coeficientes, $R-hI$, se anula. Pero esto solo ocurrirá para $N$ valores de $h$, porque la condición

$$\det(R-hI) = 0 \qquad \text{(3.57)}$$

es una ecuación de grado $N$ en $h$. Para cada $h$ que resuelva (3.57), podemos encontrar una solución para $c$. Daremos algunos ejemplos de este procedimiento más abajo.

### 3.2.4 La ecuación matricial de movimiento

Es muy útil reescribir la ecuación de movimiento, (3.14), en notación matricial. Defina un vector columna $X$, cuya fila $j$ (desde arriba) es la coordenada $x_j$:

$$X = \begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix}\,. \qquad \text{(3.58)}$$

Defina la «matriz $K$», una matriz $n\times n$ que tiene el coeficiente $K_{jk}$ en su fila $j$, columna $k$:

$$K = \begin{pmatrix} K_{11}&K_{12}&\cdots&K_{1n}\\ K_{21}&K_{22}&\cdots&K_{2n}\\ \vdots&\vdots&\ddots&\vdots\\ K_{n1}&K_{n2}&\cdots&K_{nn} \end{pmatrix}\,. \qquad \text{(3.59)}$$

Se dice que $K_{jk}$ es el «elemento $jk$» de la matriz $K$. Debido a la ecuación (3.19), la matriz $K$ es simétrica, $K=K^T$.

Defina la matriz diagonal $M$, con $m_j$ en la fila $j$, columna $j$, y ceros en el resto:

$$M = \begin{pmatrix} m_1&0&\cdots&0\\ 0&m_2&\cdots&0\\ \vdots&\vdots&\ddots&\vdots\\ 0&0&\cdots&m_n \end{pmatrix}\,. \qquad \text{(3.60)}$$

$M$ se llama la «matriz de masas».

Usando estas definiciones, podemos reescribir (3.14) en notación matricial así:

$$M\,\frac{d^2X}{dt^2} = -KX\,. \qquad \text{(3.61)}$$

No hay nada muy sofisticado en esto. Simplemente hemos usado la notación matricial para eliminar el signo de sumatoria de (3.14). La suma ahora está implícita en la multiplicación matricial de (3.61). Esto es útil porque ahora podemos usar las propiedades de las matrices y su multiplicación, discutidas arriba, para manipular (3.61). Por ejemplo, podemos simplificar un poco (3.61) multiplicando por la izquierda por $M^{-1}$, para obtener

$$\frac{d^2X}{dt^2} = -M^{-1}K\,X\,. \qquad \text{(3.62)}$$

## 3.3 Modos normales

Si solo hay un grado de libertad, entonces tanto $X$ como $M^{-1}$ son simples números, y las soluciones de la ecuación de movimiento, (3.62), tienen la forma de una amplitud constante multiplicada por un factor exponencial. De hecho, vimos que esta forma está relacionada con un hecho muy general de la física: la invariancia bajo traslación temporal, (1.33). Los argumentos del capítulo 1, (1.71)-(1.85), no dependían del número de grados de libertad. Así, muestran que, también aquí, podemos encontrar soluciones irreducibles que se reproducen a sí mismas salvo una constante global al reajustar los relojes. Como en el capítulo 1, el primer paso es permitir que las soluciones sean complejas. Es decir, reemplazamos (3.62) por

$$\frac{d^2Z}{dt^2} = -M^{-1}K\,Z\,, \qquad \text{(3.63)}$$

donde $Z$ es un $n$-vector complejo, con componentes $z_j$. Las partes reales de las componentes de $Z$ son las componentes de una solución real que satisface (3.62),

$$x_j = \text{Re}\,z_j\,. \qquad \text{(3.64)}$$

Diremos que el vector real $X$ es la parte real del vector complejo $Z$,

$$X = \text{Re}\,Z\,, \qquad \text{(3.65)}$$

si se satisface (3.64).

Igual que en el capítulo 1, sabemos que podemos encontrar soluciones irreducibles que tienen la misma forma, salvo una constante global, al reajustar los relojes. Sabemos, por (1.85), que estas tienen la forma

$$Z(t) = A\,e^{-i\omega t} \qquad \text{(3.66)}$$

donde $A$ es cierto $n$-vector constante y la frecuencia angular, $\omega$, sigue siendo simplemente un número. Ahora, si $t\to t+a$,

$$Z(t) \to Z(t+a) = e^{-i\omega a}\,Z(t)\,. \qquad \text{(3.67)}$$

Aunque la forma irreducible, (3.66), proviene solo de la invariancia bajo traslación temporal, aún debemos examinar las ecuaciones de movimiento para determinar el vector $A$ y la frecuencia angular $\omega$. Sustituyendo (3.66) en (3.63), derivando y cancelando los factores exponenciales de ambos lados, encontramos que (3.66) es una solución si

$$\omega^2A = M^{-1}K\,A\,. \qquad \text{(3.68)}$$

Esta ecuación matricial es una ecuación de autovalores de la forma que discutimos en (3.51)-(3.57). $\omega^2$ es el autovalor de la matriz $M^{-1}K$, y $A$ es el autovector correspondiente. Veamos qué significa físicamente.

La parte real del vector columna $Z$ especifica el desplazamiento de cada uno de los grados de libertad del sistema. La ecuación de autovalores, (3.68), no involucra números complejos (porque no hemos incluido amortiguamiento). Por tanto (como veremos explícitamente más abajo), podemos elegir las soluciones de modo que todas las componentes de $A$ sean reales. Entonces la parte real de las soluciones complejas que buscamos en (3.66) es

$$X(t) = A\cos\omega t\,, \qquad \text{(3.69)}$$

o, en términos de las componentes de $A$,

$$A = \begin{pmatrix}a_1\\a_2\\\vdots\end{pmatrix}\,,\qquad x_1(t)=a_1\cos\omega t\,,\ x_2(t)=a_2\cos\omega t\,,\ \text{etc.} \qquad \text{(3.70)–(3.71)}$$

No solo todo se mueve con la misma frecuencia, sino que las razones entre los desplazamientos de los distintos grados de libertad quedan fijas. Todo oscila en fase. La única diferencia entre el movimiento de los distintos grados de libertad son sus distintas amplitudes, dadas por las distintas componentes de $A$.

Vale la pena repetir el punto: la invariancia bajo traslación temporal y la linealidad implican que siempre podemos encontrar soluciones irreducibles, (3.67), en las que todos los grados de libertad oscilan con la misma frecuencia. La información adicional que conduce a (3.69) es dinámica. Si no hay amortiguamiento, todas las componentes de $A$ pueden elegirse reales, y todos los grados de libertad oscilan no solo con la misma frecuencia, sino también con la misma fase.

Si tal solución ha de satisfacer las ecuaciones de movimiento, la aceleración también debe ser proporcional a $A$, para que los desplazamientos individuales no se desincronicen. Pero eso es justo lo que nos dice (3.68): $-M^{-1}K$ es la matriz que, actuando sobre el desplazamiento, da la aceleración. La ecuación de autovalores (3.68) significa que la aceleración vuelve a ser proporcional a $A$. La constante de proporcionalidad, $\omega^2$, es la fuerza restauradora por unidad de desplazamiento y por unidad de masa, para el desplazamiento particular especificado por $A$.

Ya hemos discutido la estructura matemática de la ecuación de autovalores en (3.51)-(3.57). Lo haremos de nuevo, para enfatizar, en el caso de interés físico, (3.68). Debería quedar claro que no todo valor de $A$ y $\omega^2$ da una solución de (3.68). Resolveremos para los valores permitidos encontrando primero los posibles valores de $\omega^2$ y luego los correspondientes valores de $A$. Para encontrar los autovalores, note que (3.68) puede reescribirse como

$$\left[M^{-1}K-\omega^2I\right]A = 0\,, \qquad \text{(3.72)}$$

donde $I$ es la matriz identidad $n\times n$. (3.72) es simplemente una forma compacta de representar $n$ ecuaciones lineales homogéneas en las $n$ componentes de $A$, cuyos coeficientes dependen de $\omega^2$. Vimos en (3.47) y (3.48) que, para sistemas de $n$ ecuaciones lineales homogéneas en $n$ incógnitas, existe una solución no nula si y solo si el determinante de la matriz de coeficientes se anula. La razón es que, si el determinante fuera no nulo, la matriz $M^{-1}K-\omega^2I$ tendría inversa, y podríamos usar (3.31) para concluir que la única solución para el vector $A$ es $A=0$. Así, para tener una amplitud $A$ no nula, debemos tener

$$\det\left[M^{-1}K-\omega^2I\right] = 0\,. \qquad \text{(3.73)}$$

(3.73) es una ecuación polinómica para $\omega^2$, de grado $n$ en $\omega^2$, porque el término del determinante proveniente del producto de todos los elementos diagonales de la matriz contiene una pieza que se comporta como $[\omega^2]^n$. Todos los coeficientes del polinomio son reales. Físicamente, esperamos que todas las soluciones para $\omega^2$ sean reales y positivas siempre que el sistema esté en equilibrio estable, porque esperamos que tales sistemas oscilen. Matemáticamente, podemos mostrar que $\omega^2$ es siempre real, mientras todas las masas sean positivas. Haremos esto más abajo, en (3.127)-(3.130).

Los $\omega^2$ negativos están asociados al equilibrio inestable. Por ejemplo, considere una masa en el extremo de una varilla rígida, libre para oscilar en el campo gravitatorio terrestre en un plano vertical alrededor de un pivote sin fricción, como se muestra en la figura 3.5. La masa puede moverse a lo largo de la línea punteada. La posición de equilibrio estable se indica con la línea continua. La posición de equilibrio inestable se indica con la línea discontinua.

![Figura 3.5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh3_ES/fig3.5.png)

Figura 3.5: masa sobre una varilla rígida, libre para oscilar en el campo gravitatorio terrestre en un plano vertical; el punto más bajo es el equilibrio estable y el punto más alto es el equilibrio inestable.

Cuando la masa está en el punto de equilibrio inestable, la más mínima perturbación hará que caiga. Una vez alejada del equilibrio, el desplazamiento crece exponencialmente hasta que el ángulo respecto a la vertical se vuelve tan grande que las no linealidades de la ecuación de movimiento de este sistema toman el control.

Una vez que hemos encontrado los posibles valores de $\omega^2$, podemos sustituir cada uno de nuevo en (3.72) para obtener el $A$ correspondiente. Como (3.72) es homogénea, la escala global de $A$ no queda determinada, pero todas las razones $a_j/a_k$ sí quedan fijas para cada $\omega^2$.

### 3.3.1 Modos normales y frecuencias

El vector $A$ se llama el «modo normal» del sistema asociado a la frecuencia $\omega$. Como $A$ es real (en ausencia de fricción), las soluciones complejas, (3.66), pueden combinarse en soluciones reales, como (3.69). La solución real general tiene la forma

$$X(t) = \text{Re}\left[(b+ic)Z(t)\right] = bA\cos\omega t + cA\sin\omega t = dA\cos(\omega t-\theta) \qquad \text{(3.74)}$$

donde $b$ y $c$ (o $d$ y $\theta$) son números reales.

Ahora podemos construir la solución completa de la ecuación de movimiento. Debido a la linealidad, la obtenemos sumando todas las soluciones de modo normal, con coeficientes arbitrarios que deben fijarse mediante las condiciones iniciales.

Ahora podemos ver que el número de modos normales distintos es siempre igual a $n$, el número de grados de libertad. Etiquete los modos normales como $A^\alpha$, donde $\alpha$ es una etiqueta que (como argumentaremos más abajo) va de 1 a $n$. Etiquete las frecuencias correspondientes como $\omega_\alpha$. Entonces el movimiento más general posible del sistema es una suma de todos los modos normales,

$$Z(t) = \sum_{\alpha=1}^{n}w_\alpha\,A^\alpha\,e^{-i\omega_\alpha t} \qquad \text{(3.75)}$$

o, en forma real (con $w=b+ic$),

$$X(t) = \sum_{\alpha=1}^{n}\left[b_\alpha A^\alpha\cos(\omega_\alpha t)+c_\alpha A^\alpha\sin(\omega_\alpha t)\right] = \sum_{\alpha=1}^{n}d_\alpha A^\alpha\cos(\omega_\alpha t-\theta_\alpha) \qquad \text{(3.76)}$$

donde $b_\alpha$ y $c_\alpha$ (o $d_\alpha$ y $\theta_\alpha$) son números reales que deben determinarse a partir de las condiciones iniciales del sistema. Note que el conjunto de todos los vectores de modo normal debe ser «completo», en el sentido matemático de que cualquier configuración posible de este sistema puede describirse como una combinación lineal de modos normales. De lo contrario, no podríamos satisfacer condiciones iniciales arbitrarias con la solución (3.76). Esto puede demostrarse matemáticamente (porque la matriz $K$ es simétrica y las masas son positivas), pero el argumento físico nos bastará aquí. Del mismo modo, ningún modo normal puede ser una combinación lineal de los demás, porque cada uno corresponde a un movimiento posible independiente del sistema físico, con su propia frecuencia. La forma matemática de decir esto es que el conjunto de todos los modos normales es «linealmente independiente».

Como el conjunto de modos normales debe ser tanto completo como linealmente independiente, debe haber exactamente $n$ modos normales, donde, de nuevo, $n$ es el número de grados de libertad. $\qquad \text{(3.77)}$

Si hubiera menos de $n$ modos normales, no podrían describir todas las configuraciones posibles de los $n$ grados de libertad. Si hubiera más de $n$, no podrían ser $n$ vectores linealmente independientes: al menos uno de ellos podría escribirse como combinación lineal de los demás. Como veremos más adelante, (3.77) es el principio físico detrás del análisis de Fourier.

Vale la pena notar que resolver la ecuación de autovalores, (3.68), se vuelve difícil muy rápidamente a medida que aumenta el número de grados de libertad. Primero hay que calcular el determinante de una matriz $n\times n$; si todos los elementos son no nulos, esto requiere sumar $n!$ términos. Una vez hecho esto, aún hay que resolver una ecuación polinómica de grado $n$. Para $n>3$, esto no puede hacerse analíticamente salvo en casos especiales.

Por otro lado, siempre es sencillo comprobar si un vector dado es un autovector de una matriz dada y, si lo es, calcular el autovalor. Usaremos este hecho en los problemas al final del capítulo.

### 3.3.2 De vuelta al ejemplo $2\times2$

Volvamos al ejemplo del principio de este capítulo, en el caso especial en que los dos bloques del péndulo tienen la misma masa, $m_1=m_2=m$. Aunque simple, este será un sistema muy importante para nuestra comprensión de los fenómenos ondulatorios. Veamos cómo las técnicas que hemos desarrollado nos permiten resolver las frecuencias permitidas y los vectores $A$ correspondientes, los modos normales. De (3.7) y (3.8), la matriz $K$ tiene la forma

$$K = \begin{pmatrix} mg/\ell+\kappa & -\kappa\\ -\kappa & mg/\ell+\kappa \end{pmatrix}\,. \qquad \text{(3.78)}$$

La matriz $M$ es

$$M = \begin{pmatrix} m&0\\0&m \end{pmatrix}\,. \qquad \text{(3.79)}$$

Así, de (3.78) y (3.79),

$$M^{-1}K = \begin{pmatrix} g/\ell+\kappa/m & -\kappa/m\\ -\kappa/m & g/\ell+\kappa/m \end{pmatrix}\,. \qquad \text{(3.80)}$$

La matriz $M^{-1}K-\omega^2I$ es

$$M^{-1}K-\omega^2I = \begin{pmatrix} g/\ell+\kappa/m-\omega^2 & -\kappa/m\\ -\kappa/m & g/\ell+\kappa/m-\omega^2 \end{pmatrix}\,. \qquad \text{(3.81)}$$

Para encontrar los autovalores de $M^{-1}K$, formamos el determinante

$$\det\left[M^{-1}K-\omega^2I\right] = (g/\ell+\kappa/m-\omega^2)^2 - (\kappa/m)^2 = (\omega^2-g/\ell)(\omega^2-g/\ell-2\kappa/m) = 0\,. \qquad \text{(3.82)}$$

Así, las frecuencias angulares de los modos normales son

$$\omega_1^2 = g/\ell\,,\qquad \omega_2^2 = g/\ell+2\kappa/m\,. \qquad \text{(3.83)}$$

Para encontrar los modos normales correspondientes, sustituimos estas frecuencias de vuelta en la ecuación de autovalores. Para $\omega_1^2$, el vector de modo normal, $A^1$,

$$A^1 = \begin{pmatrix} a_1^1\\a_2^1 \end{pmatrix}\,, \qquad \text{(3.84)}$$

satisface la ecuación matricial

$$[M^{-1}K-\omega_1^2I]A^1 = 0\,. \qquad \text{(3.85)}$$

De (3.81) y (3.83),

$$M^{-1}K-\omega_1^2I = \begin{pmatrix} \kappa/m & -\kappa/m\\ -\kappa/m & \kappa/m \end{pmatrix}\,. \qquad \text{(3.86)}$$

Así, (3.85) se convierte en

$$\begin{pmatrix} \kappa/m & -\kappa/m\\ -\kappa/m & \kappa/m \end{pmatrix}\begin{pmatrix} a_1^1\\a_2^1 \end{pmatrix}=0 \implies \frac{\kappa}{m}\begin{pmatrix} a_1^1-a_2^1\\ -a_1^1+a_2^1 \end{pmatrix}=0 \implies a_1^1=a_2^1\,. \qquad \text{(3.87)}$$

Podemos tomar $a_1^1=1$, porque podemos multiplicar el vector de modo normal por el número que queramos: solo importa la razón $a_1^1/a_2^1$. Así, por ejemplo, podemos tomar

$$A^1 = \begin{pmatrix}1\\1\end{pmatrix}\,. \qquad \text{(3.88)}$$

Esto da (3.10). El desplazamiento en este modo normal se muestra en la figura 3.6.

![Figura 3.6](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh3_ES/fig3.6.png)

Figura 3.6: los dos péndulos moviéndose en la misma dirección, con el muelle sin estirar — el modo normal $A^1$.

Para $\omega_2^2$, el vector de modo normal, $A^2$,

$$A^2 = \begin{pmatrix} a_1^2\\a_2^2 \end{pmatrix}\,, \qquad \text{(3.89)}$$

satisface la ecuación matricial (donde se sobreentiende la matriz identidad que multiplica a $\omega_2^2$)

$$[M^{-1}K-\omega_2^2]A^2 = 0\,. \qquad \text{(3.90)}$$

Esta vez, (3.81) y (3.83) dan

$$M^{-1}K-\omega_2^2 = \begin{pmatrix} -\kappa/m & -\kappa/m\\ -\kappa/m & -\kappa/m \end{pmatrix}\,. \qquad \text{(3.91)}$$

Así, (3.90) se convierte en

$$\begin{pmatrix} -\kappa/m & -\kappa/m\\ -\kappa/m & -\kappa/m \end{pmatrix}\begin{pmatrix} a_1^2\\a_2^2 \end{pmatrix}=0 \implies -\frac{\kappa}{m}\begin{pmatrix} a_1^2+a_2^2\\ a_1^2+a_2^2 \end{pmatrix}=0 \implies a_1^2=-a_2^2\,. \qquad \text{(3.92)}$$

De nuevo, solo importa la razón $a_1^2/a_2^2$, así que podemos tomar

$$A^2 = \begin{pmatrix}1\\-1\end{pmatrix}\,. \qquad \text{(3.93)}$$

Esto da (3.11). El desplazamiento en este modo normal se muestra en la figura 3.7.

![Figura 3.7](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh3_ES/fig3.7.png)

Figura 3.7: los dos péndulos moviéndose en direcciones opuestas, estirando y comprimiendo el muelle alternadamente — el modo normal $A^2$.

La física de estos modos es fácil de entender. En el modo 1, los bloques se mueven juntos y el muelle nunca se estira respecto a su posición de equilibrio. Así, la frecuencia es simplemente $g/\ell$, la misma que la de un péndulo no acoplado. En el modo 2, los bloques se mueven en direcciones opuestas, de modo que el muelle se estira el doble del desplazamiento de cada bloque. Por tanto hay una fuerza restauradora adicional de $2\kappa$, y el cuadrado de la frecuencia angular es correspondientemente mayor.

### 3.3.3 $n=2$ — el caso general

Trabajemos explícitamente el caso $n=2$ para una matriz $K$ arbitraria,

$$M^{-1}K = \begin{pmatrix} K_{11}/m_1 & K_{12}/m_1\\ K_{12}/m_2 & K_{22}/m_2 \end{pmatrix}\,, \qquad \text{(3.94)}$$

donde hemos usado $K_{21}=K_{12}$. Entonces (3.73) se convierte en

$$\left(\frac{K_{11}K_{22}-K_{12}^2}{m_1m_2}\right) - \left(\frac{K_{11}}{m_1}+\frac{K_{22}}{m_2}\right)\omega^2 + \omega^4 = 0\,, \qquad \text{(3.95)}$$

con soluciones

$$\omega^2 = \frac12\left(\frac{K_{11}}{m_1}+\frac{K_{22}}{m_2}\right) \pm \sqrt{\frac14\left(\frac{K_{11}}{m_1}-\frac{K_{22}}{m_2}\right)^2 + \frac{K_{12}^2}{m_1m_2}}\,. \qquad \text{(3.96)}$$

Para cada $\omega^2$, podemos tomar $a_1=1$. Entonces

$$a_2 = \frac{m_1\omega^2-K_{11}}{K_{12}}\,. \qquad \text{(3.97)}$$

Como anticipamos, los autovectores resultaron ser reales. Esta es una consecuencia general de la realidad de $M^{-1}K$ y $\omega^2$. Vale la pena repetir el argumento. Cuando todos los elementos de la matriz $M^{-1}K-\omega^2I$ son reales, las razones $a_j/a_k$ son reales (porque se obtienen resolviendo un sistema de ecuaciones lineales simultáneas con coeficientes reales). Así, si elegimos una componente del vector $A$ para que sea real (multiplicando, si es necesario, por un número complejo), todas las componentes serán reales. Físicamente, esto significa que, para la solución (3.66), las distintas partes del sistema oscilan no solo con la misma frecuencia, sino con la misma fase, salvo un posible signo. Esto es cierto solo porque hemos ignorado el amortiguamiento. Volveremos a esta cuestión en la última sección (una sección opcional no apta para los débiles de corazón).

### 3.3.4 El problema de valores iniciales

Una vez que ha resuelto los modos normales y las frecuencias correspondientes, es sencillo combinarlos en la solución más general de las ecuaciones de movimiento para el conjunto de $N$ osciladores acoplados, (3.76):

$$X(t) = \sum_\alpha \left(b_\alpha A^\alpha\cos\omega_\alpha t + c_\alpha A^\alpha\sin\omega_\alpha t\right)\,. \qquad \text{(3.98)}$$

Las $2N$ constantes $b_\alpha$ y $c_\alpha$ están determinadas por las condiciones iniciales. Las $b_\alpha$ están relacionadas con los desplazamientos iniciales, $X(0)$:

$$X(0) = \sum_\alpha b_\alpha A^\alpha\,. \qquad \text{(3.99)}$$

En palabras: $b_\alpha$ es el coeficiente del modo normal $A^\alpha$ en el desplazamiento inicial $X(0)$. Las $c_\alpha$ están relacionadas con las velocidades iniciales, $dX(t)/dt|_{t=0}$:

$$\left.\frac{dX(t)}{dt}\right|_{t=0} = \sum_\alpha c_\alpha\,\omega_\alpha\,A^\alpha\,. \qquad \text{(3.100)}$$

Las ecuaciones (3.99) y (3.100) son dos conjuntos de ecuaciones lineales simultáneas para las $b_\alpha$ y $c_\alpha$. Pueden resolverse a mano; esto es bastante fácil para un número pequeño de grados de libertad. Veremos en la siguiente sección que también podemos obtener las soluciones directamente, con muy poco trabajo adicional, manipulando los modos normales.

Mientras tanto, deberíamos detenernos de nuevo a considerar la física de (3.98). Esto muestra explícitamente cómo el movimiento más general del sistema puede descomponerse en los movimientos simples asociados a los modos normales. Vale la pena contemplar un ejemplo (real, animado, o preferiblemente ambos) en este punto. Intente construir el sistema de la figura 3.1; cualquier par de osciladores idénticos conectados por un muelle relativamente débil servirá. Convénzase de que existen los modos normales. Si pone el sistema a oscilar con los bloques moviéndose de la misma manera y con la misma amplitud, permanecerán así. Si los pone a moverse en direcciones opuestas con la misma amplitud, seguirán haciéndolo. Ahora provoque un movimiento aleatorio; vea si puede entender cómo descomponerlo en modos normales.

## 3.4 \* Coordenadas normales y valores iniciales

Hay otra forma de ver las soluciones de (3.14). Podemos encontrar combinaciones lineales de las coordenadas originales que oscilan con una sola frecuencia, sin importar qué más esté pasando. Esta construcción también es útil: nos permite usar la forma de los modos normales para simplificar la solución del problema de valores iniciales.

Para ver cómo funciona esto, volvamos al ejemplo simple de los dos péndulos idénticos, (3.78)-(3.93). El movimiento más general posible de este sistema se ve así:

$$X(t) = bA^1\cos(\omega_1t-\theta_1) + cA^2\cos(\omega_2t-\theta_2)\,, \qquad \text{(3.101)}$$

o, usando (3.88) y (3.93),

$$x_1(t) = b\cos(\omega_1t-\theta_1)+c\cos(\omega_2t-\theta_2)\,,\qquad x_2(t) = b\cos(\omega_1t-\theta_1)-c\cos(\omega_2t-\theta_2)\,. \qquad \text{(3.102)}$$

El movimiento de cada bloque no es armónico, pues involucra dos frecuencias distintas y cuatro constantes que deben determinarse resolviendo el problema de valores iniciales para ambos bloques.

Pero considere la combinación lineal

$$X^1(t) \equiv x_1(t)+x_2(t)\,. \qquad \text{(3.103)}$$

En esta combinación, toda dependencia de $c$ y $\theta_2$ desaparece,

$$X^1(t) = 2b\cos(\omega_1t-\theta_1)\,. \qquad \text{(3.104)}$$

Esta combinación oscila con una única frecuencia, $\omega_1$, y depende solo de dos constantes, $b$ y $\theta_1$, sin importar cuáles sean las condiciones iniciales. Del mismo modo,

$$X^2(t) \equiv x_1(t)-x_2(t) \qquad \text{(3.105)}$$

oscila con la frecuencia $\omega_2$,

$$X^2(t) = 2c\cos(\omega_2t-\theta_2)\,. \qquad \text{(3.106)}$$

$X^1$ y $X^2$ se llaman «coordenadas normales». Podemos describir el movimiento del sistema tanto en términos de $X^1$ y $X^2$ como en términos de $x_1$ y $x_2$. Podemos ir y venir entre ambas usando las definiciones (3.103) y (3.105). Aunque $x_1$ y $x_2$ son más naturales desde el punto de vista de la configuración física del sistema, figura 3.1, $X^1$ y $X^2$ son más convenientes para entender la solución. Como veremos más abajo, yendo y viniendo entre coordenadas físicas y coordenadas normales, podemos simplificar el análisis del problema de valores iniciales.

Resulta que es posible construir coordenadas normales para cualquier sistema de modos normales. Considere un modo normal $A^\alpha$ correspondiente a una frecuencia $\omega_\alpha$. Construya el vector fila

$$B^\alpha = A^{\alpha T}M \qquad \text{(3.107)}$$

donde $A^{\alpha T}$ es la transpuesta de $A^\alpha$, un vector fila con $a_j^\alpha$ en la columna $j$.

El vector fila $B^\alpha$ es también un autovector de la matriz $M^{-1}K$, pero esta vez por la izquierda. Es decir,

$$B^\alpha\,M^{-1}K = \omega_\alpha^2\,B^\alpha\,. \qquad \text{(3.108)}$$

Para deducir (3.108), note que (3.68) puede transponerse para dar

$$A^{\alpha T}KM^{-1} = \omega_\alpha^2\,A^{\alpha T} \qquad \text{(3.109)}$$

porque $M^{-1}$ y $K$ son ambas simétricas (véase (3.18), y note que el orden de $M^{-1}$ y $K$ se invierte al transponer). Entonces

$$B^\alpha M^{-1}K = A^{\alpha T}MM^{-1}K = A^{\alpha T}KM^{-1}M = \omega_\alpha^2\,A^{\alpha T}M = \omega_\alpha^2\,B^\alpha\,. \qquad \text{(3.110)–(3.111)}$$

Dado un vector fila que satisface (3.108), podemos formar la combinación lineal de coordenadas

$$X^\alpha = B^\alpha\cdot X = \sum_j b_j^\alpha\,x_j\,. \qquad \text{(3.112)}$$

Entonces $X^\alpha$ es la coordenada normal que oscila con frecuencia angular $\omega_\alpha$, porque

$$\frac{d^2X^\alpha}{dt^2} = B^\alpha\cdot\frac{d^2X}{dt^2} = -B^\alpha M^{-1}KX = -\omega_\alpha^2\,B^\alpha\cdot X = -\omega_\alpha^2\,X^\alpha\,. \qquad \text{(3.113)}$$

Así, cada coordenada normal se comporta exactamente como la coordenada de un sistema con un único grado de libertad. Los vectores $B^\alpha$ a partir de los cuales se construyen las coordenadas normales llevan la misma cantidad de información que los modos normales; de hecho, podemos ir y venir entre ambos usando (3.107).

### 3.4.1 Más sobre el problema de valores iniciales

Mostramos aquí cómo usar los modos normales y las coordenadas normales para simplificar la solución del problema de valores iniciales de sistemas de osciladores acoplados. Al mismo tiempo, podemos usar nuestra intuición física para aprender algo sobre las matemáticas del problema de autovalores. Nos gustaría encontrar las constantes $b_\alpha$ y $c_\alpha$ determinadas por (3.99) y (3.100) sin resolver realmente estas ecuaciones lineales. En efecto, hay una forma fácil: podemos aprovechar las propiedades especiales de las coordenadas normales. Considere la combinación

$$B^\beta A^\alpha\,. \qquad \text{(3.114)}$$

Esta combinación es simplemente un número, porque es un vector fila multiplicado por un vector columna a la derecha. Sabemos, por (3.112), que $X^\beta=B^\beta X$ es la coordenada normal que oscila con frecuencia $\omega_\beta$, es decir,

$$B^\beta X(t) \propto e^{\pm i\omega_\beta t}\,. \qquad \text{(3.115)}$$

Por otro lado, los únicos términos de (3.98) que oscilan con esta frecuencia son aquellos para los que $\omega_\alpha=\omega_\beta$. Así, si $\omega_\beta$ no es igual a $\omega_\alpha$, entonces $B^\beta A^\alpha$ debe anularse, para ser consistentes con (3.115).

Si el sistema tiene dos o más modos normales con distintos vectores $A$, pero la misma frecuencia, no podemos usar (3.115) para distinguirlos. En esta situación, decimos que los modos son «degenerados». Suponga que $A^1$ y $A^2$ son dos modos distintos con la misma frecuencia,

$$M^{-1}KA^1 = \omega^2A^1\,,\qquad M^{-1}KA^2 = \omega^2A^2\,. \qquad \text{(3.116)}$$

Como los autovalores son iguales, cualquier combinación lineal de los dos vectores de modo sigue siendo un modo normal con la misma frecuencia,

$$M^{-1}K\left(\beta_1A^1+\beta_2A^2\right) = \omega^2\left(\beta_1A^1+\beta_2A^2\right)\,, \qquad \text{(3.117)}$$

para cualesquiera constantes $\beta_1$ y $\beta_2$.

Ahora, si $A^{1T}MA^2\neq0$, podemos usar (3.117) para elegir un nuevo $A^2$ así:

$$A^2 \to A^2 - \frac{A^{1T}MA^2}{A^{1T}MA^1}\,A^1\,. \qquad \text{(3.118)}$$

Este nuevo modo normal satisface

$$A^{1T}MA^2 = 0\,. \qquad \text{(3.119)}$$

La construcción de (3.118) puede extenderse a cualquier número de modos normales de la misma frecuencia. Así, incluso si tenemos varios modos normales con la misma frecuencia, podemos usar la linealidad del sistema para elegir los modos normales de modo que satisfagan

$$B^\beta A^\alpha = A^{\beta T}MA^\alpha = 0 \quad\text{para } \beta\neq\alpha\,. \qquad \text{(3.120)}$$

Casi siempre supondremos que hemos hecho esto.

Podemos usar (3.120) para simplificar el problema de valores iniciales. Considere (3.99). Si multiplicamos esta ecuación vectorial por ambos lados por el vector fila $B^\beta$, obtenemos

$$B^\beta X(0) = B^\beta\sum_\alpha b_\alpha A^\alpha = \sum_\alpha b_\alpha\,B^\beta A^\alpha = b_\beta\,B^\beta A^\beta\,, \qquad \text{(3.121)}$$

donde el último paso se sigue de (3.120), que implica que la suma sobre $\alpha$ solo contribuye para $\alpha=\beta$. Así, podemos calcular $b_\alpha$ directamente a partir de los modos normales y $X(0)$,

$$b_\alpha = \frac{B^\alpha X(0)}{B^\alpha A^\alpha}\,. \qquad \text{(3.122)}$$

De forma similar,

$$\omega_\alpha c_\alpha = \frac{1}{B^\alpha A^\alpha}\,B^\alpha\left.\frac{dX(t)}{dt}\right|_{t=0}\,. \qquad \text{(3.123)}$$

El punto es que ya hemos resuelto ecuaciones lineales simultáneas como (3.99) al encontrar los autovectores de $M^{-1}K$, así que no es necesario volver a hacerlo para hallar $b_\alpha$ y $c_\alpha$. Físicamente, sabemos que la coordenada normal $X^\alpha$ debe ser proporcional al coeficiente del modo normal $A^\alpha$ en el movimiento. La expresión precisa de esto es (3.122).

### 3.4.2 \* Matrices a partir de vectores

También podemos usar (3.120) y el requisito físico de independencia lineal de los modos normales para escribir $M^{-1}K$ y la matriz identidad en términos de los modos normales.

Consideremos primero la matriz identidad. Podemos pensar en la matriz identidad como una «máquina» que toma cualquier vector y devuelve el mismo vector. Pero, usando (3.120), podemos construir tal máquina a partir de los modos normales. Considere la matriz $H$, definida como sigue:

$$H = \sum_\alpha \frac{A^\alpha B^\alpha}{B^\alpha A^\alpha}\,. \qquad \text{(3.124)}$$

Note que $H$ es una matriz porque $A^\alpha B^\alpha$ en el numerador es el producto de un vector columna por un vector fila a la derecha, en lugar de a la izquierda. Si hacemos actuar $H$ sobre uno de los vectores de modo normal, $A^\beta$, y usamos (3.120), es fácil ver que solo el término $\alpha=\beta$ de la suma contribuye, y $H\cdot A^\beta=A^\beta$. Pero como los modos normales son un conjunto completo de $N$ vectores linealmente independientes, esto implica que $H\cdot V=V$ para cualquier vector $V$. Así, $H$ es la matriz identidad,

$$H = I\,. \qquad \text{(3.125)}$$

Podemos usar esta forma de $I$ para obtener una expresión de $M^{-1}K$ como suma sobre los modos normales. Considere el producto $M^{-1}K\cdot H=M^{-1}K$, y use la condición de autovalores $M^{-1}KA^\alpha=\omega_\alpha^2A^\alpha$ para obtener

$$M^{-1}K = \sum_\alpha \frac{\omega_\alpha^2\,A^\alpha B^\alpha}{B^\alpha A^\alpha}\,. \qquad \text{(3.126)}$$

En lenguaje matemático, lo que ocurre en (3.124) y (3.126) es un cambio de la base en la que describimos las matrices que actúan sobre nuestro espacio vectorial: pasamos de la base original, formada por un conjunto obvio de desplazamientos independientes de los grados de libertad, a la base menos obvia pero más útil de los modos normales.

### 3.4.3 \* $\omega^2$ es real

Podemos usar (3.120) para mostrar que todos los autovalores de $M^{-1}K$ son reales. Este es un ejemplo particular de un importante teorema matemático general que usará con frecuencia cuando estudie mecánica cuántica. Para demostrarlo, supongamos lo contrario y deduzcamos una contradicción. Si $\omega^2$ es un autovalor complejo con autovector $A$, entonces el conjugado complejo, $\omega^{2*}$, también es un autovalor, con autovector $A^*$. Esto debe ser así porque la matriz $M^{-1}K$ es real, lo que implica que podemos tomar el conjugado complejo de la ecuación de autovalores,

$$M^{-1}KA = \omega^2A\,, \qquad \text{(3.127)}$$

para obtener

$$M^{-1}KA^* = \omega^{2*}A^*\,. \qquad \text{(3.128)}$$

Entonces, si $\omega^2$ es complejo, $\omega^2$ y $\omega^{2*}$ son distintos, y (3.120) implica

$$A^{*T}MA = 0\,. \qquad \text{(3.129)}$$

Pero (3.129) es imposible a menos que $A=0$ o al menos una de las masas de $M$ sea negativa. Para verlo, expandámosla en las componentes de $A$:

$$A^{*T}MA = \sum_{j=1}^{n}a_j^*\,m_j\,a_j = \sum_{j=1}^{n}m_j\,|a_j|^2\,. \qquad \text{(3.130)}$$

Cada uno de los términos de (3.130) es positivo o nulo. Así, las únicas soluciones de la ecuación de autovalores, (3.127), para $\omega^2$ complejo, son las triviales, en las que $A=0$ en ambos lados. Todos los modos normales tienen $\omega^2$ real.

Así, solo hay tres posibilidades. $\omega^2>0$ corresponde a equilibrio estable y oscilación armónica. $\omega^2<0$, en cuyo caso $\omega$ es puramente imaginario, ocurre cuando el equilibrio es inestable. $\omega^2=0$ es la situación en la que el equilibrio es neutro y podemos deformar el sistema sin fuerza restauradora.

## 3.5 \* Oscilaciones forzadas y resonancia

Una de las ventajas del formalismo matricial que hemos introducido es que, en lenguaje matricial, podemos trasladar casi sin cambios la discusión anterior sobre la oscilación forzada y la resonancia del capítulo 2 a sistemas con más de un grado de libertad. Simplemente tenemos que reemplazar números por los vectores y matrices apropiados. En particular, la fuerza $F(t)$ en la ecuación de movimiento, (2.2), se convierte en un vector que describe la fuerza sobre cada uno de los grados de libertad del sistema. La única restricción aquí es que la frecuencia de oscilación sea la misma para cada componente de la fuerza. El $\omega_0^2$ de la ecuación de movimiento, (2.2), se convierte en la matriz $M^{-1}K$. El término friccional $\gamma$ se convierte en una matriz. En términos de la matriz $\gamma$, el vector de fuerza friccional es $M\gamma\,dZ/dt$ (compárese con (2.1)). Entonces podemos buscar una solución estacionaria irreducible de la ecuación de movimiento, de la forma

$$Z(t) = W\,e^{-i\omega t} \qquad \text{(3.131)}$$

donde $W$ es un vector constante, lo que da la ecuación matricial

$$\left[-\omega^2-i\gamma\omega+M^{-1}K\right]W = M^{-1}F_0\,. \qquad \text{(3.132)}$$

Formalmente, podemos resolver esto multiplicando por la matriz inversa:

$$W = \left[M^{-1}K-\omega^2-i\gamma\omega\right]^{-1}M^{-1}F_0\,. \qquad \text{(3.133)}$$

Si $\gamma$ fuera cero en la matriz

$$\left[-\omega^2-i\gamma\omega+M^{-1}K\right]\,, \qquad \text{(3.134)}$$

entonces sabemos que la matriz inversa no existiría para ningún valor de $\omega$ correspondiente a una frecuencia de oscilación libre del sistema, $\omega_0$, porque el determinante de la matriz $M^{-1}K-\omega_0^2$ es cero. La amplitud $W$ tendería a $\infty$ en este límite, en la dirección del modo normal asociado a la frecuencia impulsora, siempre que la fuerza impulsora tenga una componente en la dirección del modo normal. Para $\omega$ cercano a $\omega_0$, si no hay amortiguamiento, la amplitud de la respuesta es muy grande, proporcional a $1/(\omega_0^2-\omega^2)$, casi en la dirección del modo normal. Sin embargo, en presencia de amortiguamiento, la amplitud de la respuesta no diverge, ni siquiera para $\omega=\omega_0$, porque el término $i\gamma\omega$ sigue siendo no nulo.

Podemos ver todo esto explícitamente si la matriz de amortiguamiento $\gamma$ es proporcional a la matriz identidad,

$$\gamma = \gamma I\,. \qquad \text{(3.135)}$$

Entonces podemos usar (3.124)-(3.126) para escribir $M^{-1}K-\omega^2-i\gamma\omega$ como una suma sobre los modos normales, así:

$$\left[M^{-1}K-\omega^2-i\gamma\omega\right] = \sum_\alpha\left(\omega_\alpha^2-\omega^2-i\gamma\omega\right)\frac{A^\alpha B^\alpha}{B^\alpha A^\alpha}\,. \qquad \text{(3.136)}$$

Entonces la matriz inversa puede construirse de forma similar, simplemente invirtiendo el factor del numerador:

$$\left[M^{-1}K-\omega^2-i\gamma\omega\right]^{-1} = \sum_\alpha\left(\omega_\alpha^2-\omega^2-i\gamma\omega\right)^{-1}\frac{A^\alpha B^\alpha}{B^\alpha A^\alpha}\,. \qquad \text{(3.137)}$$

Usando (3.137), podemos reescribir (3.133) como

$$W = \sum_\alpha \frac{A^\alpha}{\omega_\alpha^2-\omega^2-i\gamma\omega}\,\frac{B^\alpha M^{-1}F_0}{B^\alpha A^\alpha}\,. \qquad \text{(3.138)}$$

Esto tiene una interpretación simple. El segundo factor del lado derecho de (3.138) es el coeficiente del modo normal $A^\alpha$ en el término impulsor, $M^{-1}F_0$. Este coeficiente se multiplica por el número complejo

$$\left[\frac{1}{\omega_\alpha^2-\omega^2-i\gamma\omega}\right]\,, \qquad \text{(3.139)}$$

que es exactamente análogo al factor de (2.21) en el caso unidimensional. Así, si $\gamma\propto I$, entonces, para cada modo normal, la oscilación forzada funciona exactamente igual que para un grado de libertad. Si $\gamma$ no es proporcional a la identidad, las fórmulas son un poco más complicadas, pero la física es cualitativamente la misma.

### 3.5.1 Ejemplo

Ilustraremos estas consideraciones con nuestro ejemplo favorito, el sistema de dos osciladores acoplados idénticos, con matriz $M^{-1}K$ dada por (3.80). Imaginaremos que el sistema está sumergido en un fluido viscoso que da un amortiguamiento uniforme $\gamma=\gamma I$, y que hay una fuerza periódica que actúa el doble de fuerte sobre el bloque 1 que sobre el bloque 2 (por ejemplo, podríamos dar a los bloques cargas eléctricas $2q$ y $q$ y someterlos a un campo eléctrico periódico), de modo que la fuerza es

$$F(t) = \begin{pmatrix}2\\1\end{pmatrix}f_0\cos\omega t = \text{Re}\left[\begin{pmatrix}2\\1\end{pmatrix}f_0e^{-i\omega t}\right]\,. \qquad \text{(3.140)}$$

Así,

$$M^{-1}F_0 = \begin{pmatrix}2\\1\end{pmatrix}\frac{f_0}{m}\,. \qquad \text{(3.141)}$$

Ahora, para usar (3.133), solo necesitamos invertir la matriz

$$[M^{-1}K-\omega^2-i\gamma\omega] = \begin{pmatrix} g/\ell+\kappa/m-\omega^2-i\gamma\omega & -\kappa/m\\ -\kappa/m & g/\ell+\kappa/m-\omega^2-i\gamma\omega \end{pmatrix}\,. \qquad \text{(3.142)}$$

Esto es bastante sencillo de hacer a mano. Lo haremos primero, y luego compararemos el resultado con (3.137). El determinante es

$$\left(\frac{g}{\ell}+\frac{\kappa}{m}-\omega^2-i\gamma\omega\right)^2 - \left(\frac{\kappa}{m}\right)^2 = \left(\frac{g}{\ell}+\frac{2\kappa}{m}-\omega^2-i\gamma\omega\right)\cdot\left(\frac{g}{\ell}-\omega^2-i\gamma\omega\right)\,. \qquad \text{(3.143)}$$

Aplicando (3.34), encontramos

$$\begin{aligned}
[M^{-1}K-\omega^2-i\gamma\omega]^{-1} = {} & \frac{1}{\left(\frac{g}{\ell}+\frac{2\kappa}{m}-\omega^2-i\gamma\omega\right)\left(\frac{g}{\ell}-\omega^2-i\gamma\omega\right)}\\
& \begin{pmatrix} g/\ell+\kappa/m-\omega^2-i\gamma\omega & \kappa/m\\ \kappa/m & g/\ell+\kappa/m-\omega^2-i\gamma\omega \end{pmatrix}\,. \qquad \text{(3.144)}
\end{aligned}$$

Si aislamos la contribución de los dos ceros del denominador de (3.144), podemos escribir

$$\begin{aligned}
[M^{-1}K-\omega^2-i\gamma\omega]^{-1} = {} & \frac{1}{2\left(\frac{g}{\ell}-\omega^2-i\gamma\omega\right)}\begin{pmatrix}1&1\\1&1\end{pmatrix}\\
& + \frac{1}{2\left(\frac{g}{\ell}+\frac{2\kappa}{m}-\omega^2-i\gamma\omega\right)}\begin{pmatrix}1&-1\\-1&1\end{pmatrix} \qquad \text{(3.145)}
\end{aligned}$$

que es justamente (3.137), como prometimos. Sustituyendo ahora en (3.133), encontramos

$$W = \frac{1}{2\left(\frac{g}{\ell}-\omega^2-i\gamma\omega\right)}\begin{pmatrix}3\\3\end{pmatrix}\frac{f_0}{m} + \frac{1}{2\left(\frac{g}{\ell}+\frac{2\kappa}{m}-\omega^2-i\gamma\omega\right)}\begin{pmatrix}1\\-1\end{pmatrix}\frac{f_0}{m}$$

$$= \frac{1}{2}\,\frac{\left(\frac{g}{\ell}-\omega^2\right)+i\gamma\omega}{\left(\frac{g}{\ell}-\omega^2\right)^2+(\gamma\omega)^2}\begin{pmatrix}3\\3\end{pmatrix}\frac{f_0}{m} + \frac12\,\frac{\left(\frac{g}{\ell}+\frac{2\kappa}{m}-\omega^2\right)+i\gamma\omega}{\left(\frac{g}{\ell}+\frac{2\kappa}{m}-\omega^2\right)^2+(\gamma\omega)^2}\begin{pmatrix}1\\-1\end{pmatrix}\frac{f_0}{m}\,, \qquad \text{(3.146)}$$

de donde podemos leer el resultado final:

$$X(t) = \text{Re}\left(We^{-i\omega t}\right) = \begin{pmatrix} \alpha_1\cos\omega t+\beta_1\sin\omega t\\ \alpha_2\cos\omega t+\beta_2\sin\omega t \end{pmatrix} \qquad \text{(3.147)}$$

donde

$$\alpha_{1(2)} = \frac{3\left(\frac{g}{\ell}-\omega^2\right)}{\left(\frac{g}{\ell}-\omega^2\right)^2+(\gamma\omega)^2}\,\frac{f_0}{2m} \pm \frac{\left(\frac{g}{\ell}+\frac{2\kappa}{m}-\omega^2\right)}{\left(\frac{g}{\ell}+\frac{2\kappa}{m}-\omega^2\right)^2+(\gamma\omega)^2}\,\frac{f_0}{2m} \qquad \text{(3.148)}$$

y

$$\beta_{1(2)} = \frac{3\gamma\omega}{\left(\frac{g}{\ell}-\omega^2\right)^2+(\gamma\omega)^2}\,\frac{f_0}{2m} \pm \frac{\gamma\omega}{\left(\frac{g}{\ell}+\frac{2\kappa}{m}-\omega^2\right)^2+(\gamma\omega)^2}\,\frac{f_0}{2m} \qquad \text{(3.149)}$$

(donde el signo superior corresponde al subíndice 1 y el inferior al subíndice 2).

La potencia entregada por la fuerza externa es la suma, sobre todos los grados de libertad, de la fuerza por la velocidad. En lenguaje matricial, esto puede escribirse como

$$P(t) = F(t)^T\cdot\frac{dX(t)}{dt}\,. \qquad \text{(3.150)}$$

La potencia media perdida por la fuerza de fricción proviene del término en $\cos^2\omega t$ de (3.150), y es

$$\frac{1}{\left(\frac{g}{\ell}-\omega^2\right)^2+(\gamma\omega)^2}\,\frac{9\gamma\omega^2f_0^2}{4m} + \frac{1}{\left(\frac{g}{\ell}+\frac{2\kappa}{m}-\omega^2\right)^2+(\gamma\omega)^2}\,\frac{\gamma\omega^2f_0^2}{4m}\,. \qquad \text{(3.151)}$$

La figura 3.8 muestra una gráfica de esto (para $\kappa/m=3g/2\ell$ y $\gamma^2=g/4\ell$). Hay dos cosas que observar en la figura 3.8. Primero, note los dos picos de resonancia, en $\omega^2=g/\ell$ y $\omega^2=g/\ell+2\kappa/m=4g/\ell$. Segundo, note que el primer pico es mucho más pronunciado que el segundo. Esto se debe a que la fuerza está más alineada con la dirección del modo normal de frecuencia menor, por lo que es más eficiente excitando ese modo.

![Figura 3.8](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh3_ES/fig3.8.png)

Figura 3.8: potencia media disipada por fricción en función de $\omega$, mostrando dos picos de resonancia en $\omega=\sqrt{g/\ell}$ y $\omega=2\sqrt{g/\ell}$, el primero mucho más alto que el segundo.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Escribir las ecuaciones de movimiento de un sistema con más de un grado de libertad en forma matricial;
2.  Encontrar las matrices $M$ y $K$ a partir de la física del sistema;
3.  Sumar, restar y multiplicar matrices;
4.  Encontrar el determinante y la inversa de matrices $2\times2$ y $3\times3$;
5.  Encontrar los modos normales y las frecuencias correspondientes de un sistema con dos grados de libertad, lo que significa encontrar los autovectores y autovalores de una matriz $2\times2$;
6.  Comprobar si un vector dado es un modo normal de un sistema con más de dos grados de libertad, y, si lo es, encontrar la frecuencia angular correspondiente;
7.  Dados los modos normales y las frecuencias correspondientes, junto con las posiciones y velocidades iniciales de todas las partes de cualquier sistema, encontrar el movimiento de todas las partes en cualquier instante posterior;
8.  - Ir y venir entre modos normales y coordenadas normales;
9.  - Reconstruir la matriz $M^{-1}K$ a partir de los modos normales y las coordenadas normales;
10. - Resolver explícitamente las oscilaciones libres de un sistema con dos grados de libertad con amortiguamiento, y poder analizar sistemas con tres o más grados de libertad si se le dan los autovectores;
11. - Resolver explícitamente problemas de oscilación forzada, con o sin amortiguamiento, para sistemas con tres o menos grados de libertad.

## Problemas

**3.1.** El vector columna de 3 componentes $A$, el vector fila de 3 componentes $B$ y la matriz $3\times3$ $C$ se definen así:

$$A = \begin{pmatrix}0\\2\\1\end{pmatrix}\,,\qquad B = \begin{pmatrix}3&-2&1\end{pmatrix}\,,\qquad C = \begin{pmatrix}1&1&1\\0&-2&1\\2&2&0\end{pmatrix}\,.$$

Calcule los siguientes objetos:

$$BA\,,\qquad BC\,,\qquad AB\,.$$

**3.2.** Considere la oscilación vertical del sistema de muelles y masas mostrado a continuación, con constantes $K_A=78$, $K_B=15$ y $K_C=6$ (todas en dinas/cm).

![Figura](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh3_ES/figs1.png)

Figura: dos masas colgando verticalmente; el muelle $K_A$ une un soporte fijo con la masa de 3 g, el muelle $K_B$ une la masa de 3 g con la masa de 1 g, y el muelle $K_C$ une la masa de 1 g con otro soporte fijo.

Encuentre los modos normales, las coordenadas normales y las frecuencias angulares asociadas. Si el bloque de 1 g se desplaza 1 cm hacia arriba desde su posición de equilibrio, con el bloque de 3 g mantenido en su posición de equilibrio, y ambos bloques se sueltan desde el reposo, describa el movimiento posterior de ambos bloques.

**3.3.** Considere el sistema de muelles y masas mostrado a continuación, con constantes de muelle (en N/m) $2110$, $90$, $81$ y $1701$ (de izquierda a derecha), $m_1=100$ kg, $m_2=9$ kg y $m_3=81$ kg.

![Figura](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh3_ES/figs2.png)

Figura: tres masas en línea horizontal, conectadas por cuatro muelles: uno a la pared izquierda ($K=2110$), uno entre $m_1$ y $m_2$ ($K=90$), uno entre $m_2$ y $m_3$ ($K=81$) y uno a la pared derecha ($K=1701$).

1.  ¿Cuáles de los siguientes vectores son modos normales del sistema, y cuáles son las frecuencias angulares correspondientes? Note que la matriz $M^{-1}K$ puede parecer un poco complicada.

$$\begin{pmatrix}\psi_1\\\psi_2\\\psi_3\end{pmatrix} = \begin{pmatrix}9\\0\\10\end{pmatrix},\ \begin{pmatrix}9\\60\\10\end{pmatrix},\ \begin{pmatrix}9\\-30\\10\end{pmatrix},\ \begin{pmatrix}9\\30\\10\end{pmatrix},\ \begin{pmatrix}9\\0\\-10\end{pmatrix}$$

1.  Si el sistema se suelta desde el reposo con un desplazamiento inicial (medido en mm)

$$\begin{pmatrix}\psi_1\\\psi_2\\\psi_3\end{pmatrix} = \begin{pmatrix}9\\0\\10\end{pmatrix}\,,$$

¿cuánto tiempo tarda en volver por primera vez a su configuración inicial?

\*\*3.4 \*.\*\* Un sistema de cuatro masas conectadas por muelles se describe mediante una matriz de masas

$$M = \begin{pmatrix}1&0&0&0\\0&2&0&0\\0&0&1&0\\0&0&0&2\end{pmatrix}$$

y una matriz $K$

$$K = \begin{pmatrix}29&-10&-4&-2\\-10&58&-14&-2\\-4&-14&31&-26\\-2&-2&-26&74\end{pmatrix}$$

1.  ¿Cuáles de los siguientes vectores son modos normales?

$$\begin{pmatrix}1\\2\\1\\1\end{pmatrix},\ \begin{pmatrix}1\\1\\2\\1\end{pmatrix},\ \begin{pmatrix}2\\1\\1\\1\end{pmatrix},\ \begin{pmatrix}2\\1\\-1\\-1\end{pmatrix},\ \begin{pmatrix}4\\-3\\0\\1\end{pmatrix},\ \begin{pmatrix}0\\1\\-4\\3\end{pmatrix}$$

1.  Para cada modo normal, encuentre la frecuencia angular correspondiente. Pista: esto requiere algo de aritmética. Si es perezoso, puede usar una calculadora programable o escribir un pequeño programa de ordenador para comprobarlo. Pero el objetivo de este problema es mostrarle que la cantidad de trabajo necesaria para comprobar si los vectores son modos normales es realmente pequeña comparada con el trabajo de encontrar los modos desde cero.

2.  Si los bloques se sueltan desde el reposo con un desplazamiento inicial proporcional a

$$\begin{pmatrix}1\\1\\-1\\1\end{pmatrix}\,,$$

¿qué modo normal está ausente del movimiento posterior?

1.  Encuentre las coordenadas normales correspondientes a cada uno de los modos normales del sistema.

**3.5.** Considere las oscilaciones longitudinales del sistema mostrado a continuación: dos bloques que pueden deslizar horizontalmente sin fricción, conectados por muelles de $15$, $90$ y $10$ dinas/cm (de izquierda a derecha, el primero y el último anclados a paredes fijas). El bloque 1 tiene una masa de 15 gramos y el bloque 2 una masa de 10 gramos. Los desplazamientos de los bloques respecto al equilibrio se miden ambos hacia la derecha.

1.  Demuestre que la matriz $M^{-1}K$ de este sistema es

$$M^{-1}K = \begin{pmatrix}7&-6\\-9&10\end{pmatrix}\,.$$

1.  Demuestre que los modos normales son

$$A^1 = \begin{pmatrix}1\\1\end{pmatrix}\,,\qquad A^2 = \begin{pmatrix}2\\-3\end{pmatrix}\,.$$

Encuentre las frecuencias angulares correspondientes, $\omega_1$ y $\omega_2$.

**3.6.** Considere las oscilaciones longitudinales del sistema mostrado a continuación: dos bloques que pueden deslizar horizontalmente sin fricción, conectados por tres muelles de constantes $K_1$, $K_2$ y $K_3$ (el primero y el último anclados a paredes fijas). Los desplazamientos de los bloques respecto al equilibrio se miden ambos hacia la derecha. El bloque 1 tiene una masa de 15 gramos y el bloque 2 una masa de 10 gramos. Los modos normales de este sistema son

$$A^1 = \begin{pmatrix}1\\3\end{pmatrix}\,,\qquad A^2 = \begin{pmatrix}2\\-1\end{pmatrix}\,,$$

con frecuencias correspondientes

$$\omega_1 = 1\ \text{s}^{-1}\,,\qquad \omega_2 = 2\ \text{s}^{-1}\,.$$

1.  Si el sistema está en reposo en $t=0$, con desplazamientos $x_1(0)=5$ cm, $x_2(0)=0$, es decir,

$$X(0) = \begin{pmatrix}x_1(0)\\x_2(0)\end{pmatrix} = \begin{pmatrix}5\\0\end{pmatrix}\,\text{cm}\,,$$

encuentre el desplazamiento del bloque 2 en el instante $t=\pi$ s.

1.  Encuentre $K_1$, $K_2$ y $K_3$.

\*\*3.7 \*.\*\* En el sistema del problema (3.5), suponga que sumergimos el sistema en un fluido amortiguador de modo que

$$\gamma = \begin{pmatrix}\gamma&0\\0&\gamma\end{pmatrix}$$

con $\gamma=1\ \text{s}^{-1}$, y que se aplica una fuerza externa de la siguiente forma (en dinas):

$$F(t) = f\cos\omega t = \begin{pmatrix}1\\0\end{pmatrix}\cos\omega t\,.$$

Encuentre y grafique la potencia media perdida por la fuerza de fricción en función de $\omega$, desde $\omega=0$ hasta $10\ \text{s}^{-1}$.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.
