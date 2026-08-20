# Capítulo 5: Ondas

El clímax de este libro llega pronto. Aquí identificamos las características cruciales de un sistema que admite ondas: la invariancia bajo traslación espacial y las interacciones locales.

## Vídeos de esta clase (YouTube)

- [Clase 6: Osciladores forzados, resonancia](https://www.youtube.com/watch?v=Ahv7Akj2xs4)
- [Clase 7: Simetría, número infinito de osciladores acoplados](https://www.youtube.com/watch?v=b1eKhyC9TTo)
- [Clase 8: Simetría de traslación](https://www.youtube.com/watch?v=J1uHGy1tRmM)
- [Clase 9: Ecuación de ondas, ondas estacionarias, series de Fourier](https://www.youtube.com/watch?v=1JeBWHzrRD4)

## Resumen previo

Identificamos la invariancia bajo traslación espacial de la clase de sistemas infinitos en los que ocurren los fenómenos ondulatorios.

1.  Los argumentos de simetría no pueden aplicarse directamente a sistemas finitos que admiten ondas, como una serie de péndulos acoplados. Sin embargo, mostramos que, si los acoplamientos son solo entre bloques vecinos, el concepto de simetría todavía puede usarse para entender las oscilaciones. En este caso decimos que las interacciones son «locales». La idea es separar la física en dos componentes distintos: la física del interior y la física de las fronteras, que se incorpora en forma de condiciones de contorno. El interior puede considerarse parte de un sistema infinito con invariancia bajo traslación espacial, una simetría bajo traslaciones en cierta distancia $a$. En este caso, los modos normales se llaman ondas estacionarias.
2.  Después introducimos una notación diseñada para aprovechar al máximo la invariancia bajo traslación espacial del sistema infinito. Introducimos el número de onda angular, $k$, que desempeña para la dependencia espacial de la onda el mismo papel que la frecuencia angular, $\omega$, desempeña para su dependencia temporal.
3.  Describimos los modos normales de oscilación transversal de una cuerda con cuentas. Los modos son «ondulados».
4.  Estudiamos los modos normales de una cuerda con cuentas finita con extremos libres, como otro ejemplo de condiciones de contorno.
5.  Estudiamos un tipo de problema de oscilación forzada particularmente importante para sistemas invariantes bajo traslación con interacciones locales. Si la fuerza impulsora actúa solo en los extremos del sistema, la solución puede encontrarse simplemente usando condiciones de contorno.
6.  Aplicamos la idea de invariancia bajo traslación espacial a un sistema de circuitos LC acoplados.

## 5.1 Invariancia bajo traslación espacial

![Figura 5.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.1.png)

Figura 5.1: sistema finito de $N$ péndulos acoplados idénticos, en línea, cada uno conectado a sus vecinos mediante un muelle, con los dos extremos anclados a paredes fijas.

El sistema típico de osciladores acoplados que admite ondas es como el sistema de $N$ péndulos acoplados idénticos mostrado en la figura 5.1. Este sistema es una generalización del sistema de dos péndulos acoplados que estudiamos en los capítulos 3 y 4. Suponga que cada masa de péndulo tiene masa $m$, cada péndulo tiene longitud $\ell$, cada muelle tiene constante $\kappa$ y la separación de equilibrio entre masas es $a$. Suponga además que no hay fricción y que los péndulos están obligados a oscilar solo en la dirección en la que se estiran los muelles. Nos interesa la oscilación libre de este sistema, sin fuerza externa. Tal oscilación, cuando el movimiento es paralelo a la dirección en la que el sistema se extiende en el espacio, se llama «oscilación longitudinal». Llame $\psi_j$ al desplazamiento longitudinal de la $j$-ésima masa respecto al equilibrio. Podemos organizar los desplazamientos en un vector $\Psi$ (por razones que quedarán claras más abajo, sería confuso usar $X$, así que elegimos otra letra, la griega psi, que se escribe $\psi$ en minúscula y $\Psi$ en mayúscula):

$$\Psi = \begin{pmatrix}\psi_1\\\psi_2\\\psi_3\\\vdots\\\psi_N\end{pmatrix}\,. \qquad \text{(5.1)}$$

Entonces las ecuaciones de movimiento (para pequeñas oscilaciones longitudinales) son

$$\frac{d^2\Psi}{dt^2} = -M^{-1}K\,\Psi \qquad \text{(5.2)}$$

donde $M$ es la matriz diagonal con $m$ en la diagonal,

$$M = \begin{pmatrix} m&0&0&\cdots&0\\ 0&m&0&\cdots&0\\ 0&0&m&\cdots&0\\ \vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&m \end{pmatrix}\,, \qquad \text{(5.3)}$$

y $K$ tiene elementos diagonales $(mg/\ell+2\kappa)$, elementos en la subdiagonal $-\kappa$, y ceros en el resto,

$$K = \begin{pmatrix} mg/\ell+2\kappa & -\kappa & 0 & \cdots & 0\\ -\kappa & mg/\ell+2\kappa & -\kappa & \cdots & 0\\ 0 & -\kappa & mg/\ell+2\kappa & \cdots & 0\\ \vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&mg/\ell+2\kappa \end{pmatrix}\,. \qquad \text{(5.4)}$$

El $-\kappa$ de la subdiagonal tiene exactamente el mismo origen que el $-\kappa$ de la matriz $K$ $2\times2$ de (3.78): describe el acoplamiento de dos bloques vecinos por el muelle. El $(mg/\ell+2\kappa)$ de la diagonal es análogo al $(mg/\ell+\kappa)$ de la diagonal de (3.78). La diferencia en el factor 2 del coeficiente de $\kappa$ surge porque hay dos muelles, uno a cada lado, que contribuyen a la fuerza restauradora sobre cada bloque en el sistema de la figura 5.1, mientras que solo había uno en el sistema de la figura 3.1. Así, $M^{-1}K$ tiene la forma

$$M^{-1}K = \begin{pmatrix} 2B&-C&0&\cdots&0\\ -C&2B&-C&\cdots&0\\ 0&-C&2B&\cdots&0\\ \vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&2B \end{pmatrix} \qquad \text{(5.5)}$$

donde

$$2B = g/\ell+2\kappa/m\,,\qquad C=\kappa/m\,. \qquad \text{(5.6)}$$

Es interesante comparar la matriz (5.5) con la matriz (4.43) del capítulo anterior. En ambos casos, los elementos diagonales son todos iguales, por la simetría; lo mismo ocurre con los elementos de la subdiagonal. Sin embargo, en (5.5), todos los demás elementos son cero, porque las interacciones son solo entre bloques vecinos más cercanos. Llamamos «locales» a tales interacciones. En (4.43), en cambio, cada masa interactúa con todas las demás. Usaremos la naturaleza local de las interacciones más abajo.

Podríamos intentar encontrar los modos normales de este sistema directamente, hallando los autovectores de $M^{-1}K$, pero hay una técnica mucho más fácil y de utilidad más general. Podemos dividir la física del sistema en dos partes: la física de los péndulos acoplados, y la física de las paredes. Para ello, primero consideramos un sistema infinito sin paredes en absoluto.

### 5.1.1 El sistema infinito

![Figura 5.2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.2.png)

Figura 5.2: fragmento de un sistema infinito de péndulos acoplados, extendiéndose indefinidamente a ambos lados del bloque 1 al N, con los mismos muelles de acoplamiento.

Note que en la figura 5.2 no hemos cambiado en absoluto el interior del sistema de la figura 5.1: simplemente hemos reemplazado las paredes por una continuación del interior.

Ahora podemos encontrar todos los modos del sistema infinito de la figura 5.2 muy fácilmente, aprovechando un argumento de simetría. El sistema infinito de la figura 5.2 se ve igual si se traslada, moviéndolo a la izquierda o a la derecha en un múltiplo de la separación de equilibrio, $a$. Tiene la propiedad de «invariancia bajo traslación espacial». La invariancia bajo traslación espacial es la simetría del sistema infinito bajo traslaciones en múltiplos de $a$. En este ejemplo, debido a los bloques discretos y a la longitud finita de los muelles, la invariancia bajo traslación espacial es «discreta»: solo las traslaciones por múltiplos enteros de $a$ dan la misma física. Más adelante discutiremos sistemas continuos que tienen invariancia bajo traslación espacial continua; sin embargo, veremos que tales sistemas pueden analizarse con las mismas técnicas que introducimos en este capítulo.

Podemos usar la simetría de la invariancia bajo traslación espacial, igual que usamos las simetrías de reflexión y rotación discutidas en el capítulo anterior, para encontrar los modos normales del sistema infinito. La invariancia discreta bajo traslación espacial del sistema infinito (la simetría bajo traslaciones en múltiplos de $a$) nos permite encontrar los modos normales del sistema infinito de forma simple.

La mayoría de los modos que encontremos usando la invariancia bajo traslación espacial del sistema infinito de la figura 5.2 no tendrán nada que ver con el sistema finito de la figura 5.1. Pero si podemos encontrar combinaciones lineales de los modos normales del sistema infinito de la figura 5.2 en las que los bloques $0$ y $N+1$ permanezcan fijos, entonces deben ser soluciones de las ecuaciones de movimiento del sistema de la figura 5.1. La razón es que las interacciones entre los bloques son «locales» —ocurren solo entre bloques vecinos más cercanos—. Así, el bloque 1 «sabe» qué hace el bloque 0, pero no qué hace el bloque $-1$. Si el bloque 0 está inmóvil, bien podría ser una pared, porque los bloques del otro lado no afectan en absoluto al bloque 1 (ni a ninguno de los bloques 1 a $N$). La naturaleza local de la interacción nos permite incorporar la física de las paredes como una condición de contorno, después de resolver el problema infinito. Este mismo truco también nos permitirá resolver muchos otros problemas.

Veamos cómo funciona esto para el sistema de la figura 5.1. Primero, usamos la simetría bajo traslaciones para encontrar los modos normales del sistema infinito de la figura 5.2. Como en los dos capítulos anteriores, describimos las soluciones en términos de un vector, $A$. Pero ahora $A$ tiene un número infinito de componentes, $A_j$, donde el entero $j$ va de $-\infty$ a $+\infty$. Es un poco incómodo escribir este vector infinito, pero podemos representar un fragmento de él:

$$A = \begin{pmatrix}\vdots\\A_0\\A_1\\A_2\\A_3\\\vdots\\A_N\\A_{N+1}\\\vdots\end{pmatrix}\,. \qquad \text{(5.7)}$$

Del mismo modo, la matriz $M^{-1}K$ del sistema es una matriz infinita, no fácil de escribir en su totalidad, pero cualquier fragmento de ella (a lo largo de la diagonal) se ve como el interior de (5.5):

$$\begin{pmatrix}\ddots&\ddots&\ddots&\ddots&\ddots&\ddots\\ \cdots&2B&-C&0&0&\cdots\\ \cdots&-C&2B&-C&0&\cdots\\ \cdots&0&-C&2B&-C&\cdots\\ \cdots&0&0&-C&2B&\cdots\\ \ddots&\ddots&\ddots&\ddots&\ddots&\ddots \end{pmatrix}\,. \qquad \text{(5.8)}$$

Este sistema es «invariante bajo traslación espacial» porque se ve igual si se desplaza una distancia $a$ hacia la izquierda. Esto mueve el bloque $j+1$ a donde estaba el bloque $j$, así que, si hay un modo con componentes $A_j$, debe haber otro modo con la misma frecuencia, representado por un vector $A'=SA$, con componentes

$$A'_j = A_{j+1}\,. \qquad \text{(5.9)}$$

La matriz de simetría, $S$, es una matriz infinita con unos en la subdiagonal. Estos son análogos a los unos de la subdiagonal en (4.40). Sin embargo, ahora la transformación nunca se cierra sobre sí misma: no hay análogo del 1 de la esquina inferior izquierda de (4.40), porque la matriz infinita no tiene esquina. Queremos encontrar los autovalores y autovectores de la matriz $S$, que satisfacen

$$A' = SA = \beta A \qquad \text{(5.10)}$$

o, equivalentemente (de (5.9)), los modos en los que $A_j$ y $A'_j$ son proporcionales:

$$A'_j = \beta A_j = A_{j+1} \qquad \text{(5.11)}$$

donde $\beta$ es alguna constante no nula (el cero no sirve para $\beta$, porque la ecuación de autovalores no tendría solución).

La ecuación (5.11) puede resolverse así: elija $A_0=1$. Entonces $A_1=\beta$, $A_2=\beta^2$, etc., de modo que $A_j=(\beta)^j$ para todo $j$ no negativo. También podemos reescribir (5.11) como $A_{j-1}=\beta^{-1}A_j$, de modo que $A_{-1}=\beta^{-1}$, $A_{-2}=\beta^{-2}$, etc. Así, la solución es

$$A_j = (\beta)^j \qquad \text{(5.12)}$$

para todo $j$. Note que esta solución funciona para cualquier valor no nulo de $\beta$, a diferencia de los ejemplos que discutimos en el capítulo anterior. La razón es que una traslación en $a$, a diferencia de las simetrías de reflexión y rotación de $60°$ discutidas en el capítulo 4, nunca lo devuelve a donde empezó, sin importar cuántas veces la repita. Además, el sistema infinito, con un número infinito de grados de libertad, tiene un número infinito de modos normales distintos, correspondientes a distintos valores de $\beta$.

Para cada valor de $\beta$, hay un autovector único (salvo multiplicación por una constante global), $A$. Sabemos que es único porque lo hemos construido explícitamente en (5.12). Por tanto, todos los autovalores de $S$ son distintos. Así, de (4.22), sabemos que cada uno de los autovectores es un modo normal del sistema infinito. Como hay una correspondencia biunívoca entre números no nulos, $\beta$, y modos normales, podemos (al menos por ahora —encontraremos una notación mejor más adelante) etiquetar los modos normales por el autovalor, $\beta$, de la matriz de simetría $S$. Llamaremos al autovector correspondiente $A^\beta$, de modo que (5.12) puede escribirse

$$A_j^\beta = \beta^j\,. \qquad \text{(5.13)}$$

Ahora que conocemos la forma de los modos normales, es fácil obtener las frecuencias correspondientes haciendo actuar la matriz $M^{-1}K$, (5.8), sobre (5.12). Esto da

$$\omega^2A_j^\beta = 2BA_j^\beta - CA_{j+1}^\beta - CA_{j-1}^\beta\,, \qquad \text{(5.14)}$$

o, sustituyendo (5.13),

$$\omega^2\beta^j = 2B\beta^j - C\beta^{j+1} - C\beta^{j-1} = (2B-C\beta-C\beta^{-1})\beta^j\,. \qquad \text{(5.15)}$$

Esto es cierto para todo $j$, lo que muestra que (5.13) es en efecto un autovector (ya lo sabíamos por el argumento de simetría, (4.22), pero está bien comprobarlo cuando es posible), y el autovalor es

$$\omega^2 = 2B - C\beta - C\beta^{-1}\,. \qquad \text{(5.16)}$$

Note que, para casi cualquier valor de $\omega^2$, hay dos modos normales, porque podemos intercambiar $\beta$ y $\beta^{-1}$ sin cambiar (5.16). Las únicas excepciones son

$$\omega^2 = 2B \pm 2C\,, \qquad \text{(5.17)}$$

correspondientes a $\beta=\pm1$. El hecho de que haya como máximo dos modos normales para cada valor de $\omega^2$ tendrá una consecuencia dramática: significa que solo tenemos que tratar con dos modos normales a la vez para implementar la física de la frontera. Esta es una característica especial del sistema unidimensional que no comparten los sistemas bidimensionales y tridimensionales. Como veremos, esto hace que el sistema unidimensional sea muy fácil de manejar.

### 5.1.2 Condiciones de contorno

*(Referencia al programa interactivo 5-1 del disco de programas del curso original.)*

Ya hemos resuelto el problema de la oscilación del sistema infinito. Armados con este resultado, podemos reincorporar la física de las paredes. Cualquier $\beta$ (salvo $\beta=\pm1$) da un par de modos normales para el sistema infinito de la figura 5.2. Pero solo valores especiales de $\beta$ funcionarán para el sistema finito de la figura 5.1. Para encontrar los modos normales del sistema de la figura 5.1, usamos (4.56), el hecho de que cualquier combinación lineal de los dos modos normales con la misma frecuencia angular, $\omega$, también es un modo normal. Si podemos encontrar una combinación lineal que se anule en $j=0$ y en $j=N+1$, será un modo normal del sistema de la figura 5.1. Es la anulación del modo normal en $j=0$ y $j=N+1$ lo que constituye las «condiciones de contorno» de este sistema finito en particular.

Empecemos tratando de satisfacer la condición de contorno en $j=0$. Para cada posible valor de $\omega^2$, solo tenemos que preocuparnos por dos modos normales, las dos soluciones de (5.16) para $\beta$. Mientras $\beta\neq\pm1$, podemos encontrar una combinación que se anule en $j=0$; basta restar los dos modos $A^\beta$ y $A^{\beta^{-1}}$ para obtener un vector

$$A = A^\beta - A^{\beta^{-1}}\,, \qquad \text{(5.18)}$$

o, en componentes,

$$A_j \propto A_j^\beta - A_j^{\beta^{-1}} = \beta^j-\beta^{-j}\,. \qquad \text{(5.19)}$$

Lo primero que hay que notar sobre (5.19) es que $A_j$ no puede anularse para ningún $j\neq0$ a menos que $|\beta|=1$. Así, si vamos a tener alguna posibilidad de satisfacer la condición de contorno en $j=N+1$, debemos suponer que

$$\beta = e^{i\theta}\,. \qquad \text{(5.20)}$$

Entonces, de (5.19),

$$A_j \propto \sin j\theta\,. \qquad \text{(5.21)}$$

Ahora podemos satisfacer la condición de contorno en $j=N+1$ imponiendo $A_{N+1}=0$. Esto implica $\sin[(N+1)\theta]=0$, o

$$\theta = n\pi/(N+1)\,,\quad\text{para } n\text{ entero}\,. \qquad \text{(5.22)}$$

Así, los modos normales del sistema de la figura 5.1 son

$$A_j^n = \sin\left(\frac{jn\pi}{N+1}\right)\,,\quad\text{para } n=1,2,\ldots,N\,. \qquad \text{(5.23)}$$

Otros valores de $n$ no dan modos nuevos: simplemente repiten los $N$ modos ya mostrados en (5.23). Las frecuencias correspondientes se obtienen sustituyendo (5.20)-(5.21) en (5.16), dando

$$\omega^2 = 2B - 2C\cos\theta = 2B - 2C\cos\left(\frac{n\pi}{N+1}\right)\,. \qquad \text{(5.24)}$$

A partir de aquí, el análisis del movimiento del sistema es igual que para cualquier otro sistema de osciladores acoplados. Como se discutió en el capítulo 3, podemos descomponer un movimiento general y expresarlo como suma de los modos normales. Esto se ilustra para el sistema de péndulos acoplados en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-5-1" rel="noopener" target="_blank" title="Animación original de Howard Georgi">5-1</a> del disco de programas. Lo nuevo de este sistema es la manera en que obtuvimos los modos normales, y su forma peculiarmente simple, en términos de funciones trigonométricas. Obtendremos más intuición sobre el significado de estos modos en la siguiente sección. Mientras tanto, note la forma en que los modos simples pueden combinarse para dar el movimiento muy complicado del sistema completo.

## 5.2 $k$ y relaciones de dispersión

Hasta ahora, la separación de equilibrio entre los bloques, $a$, no ha aparecido en el análisis. Todo lo que hemos dicho hasta ahora sería cierto incluso si los muelles tuvieran longitudes aleatorias, siempre que todas las constantes de muelle fueran iguales. En tal caso, la «invariancia bajo traslación espacial» que usamos para resolver el problema sería un artificio puramente matemático, que transforma el sistema original en un sistema distinto con el mismo tipo de pequeñas oscilaciones. Sin embargo, habitualmente, en aplicaciones físicas, la invariancia bajo traslación espacial es real y todas las distancias entre bloques son iguales. Entonces es muy útil etiquetar los bloques por su posición de equilibrio. Tomemos $x=0$ como la posición de la pared izquierda (o del bloque 0). Entonces el primer bloque está en $x=a$, el segundo en $x=2a$, etc., como se muestra en la figura 5.3. Podemos describir el desplazamiento de todos los bloques mediante una función $\psi(x,t)$, donde $\psi(ja,t)$ es el desplazamiento del $j$-ésimo bloque (el que tiene posición de equilibrio $ja$). Por supuesto, esta función no está muy bien definida, porque solo nos importan sus valores en un conjunto discreto de puntos. Sin embargo, como veremos más abajo al discutir la cuerda con cuentas, nos ayudará a entender lo que ocurre si dibujamos una curva suave que pase por estos puntos.

![Figura 5.3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.3.png)

Figura 5.3: los péndulos acoplados etiquetados por su posición de equilibrio, $x=0, a, 2a, \ldots, (N+1)a$.

Del mismo modo, podemos describir un modo normal del sistema de la figura 5.1 (o del sistema infinito de la figura 5.2) como una función $A(x)$, donde

$$A(ja) = A_j\,. \qquad \text{(5.25)}$$

En este lenguaje, la invariancia bajo traslación espacial, (5.11), se convierte en

$$A(x+a) = \beta A(x)\,. \qquad \text{(5.26)}$$

Es convencional escribir la constante $\beta$ como una exponencial

$$\beta = e^{ika}\,. \qquad \text{(5.27)}$$

Cualquier número complejo no nulo puede escribirse como una exponencial de esta forma. De hecho, podemos cambiar $k$ por un múltiplo de $2\pi/a$ sin cambiar $\beta$, así que podemos elegir la parte real de $k$ entre $-\pi/a$ y $\pi/a$:

$$-\frac{\pi}{a} < \text{Re}\,k \le \frac{\pi}{a}\,. \qquad \text{(5.28)}$$

Si sustituimos (5.13) y (5.27) en (5.25), obtenemos

$$A^\beta(ja) = e^{ikja}\,. \qquad \text{(5.29)}$$

Esto sugiere que tomemos la función que describe el modo normal correspondiente a (5.27) como

$$A(x) = e^{ikx}\,. \qquad \text{(5.30)}$$

El modo queda determinado por el número $k$ que satisface (5.28).

El parámetro $k$ (cuando es real) se llama el número de onda angular del modo. Mide la «ondulación» del modo normal, en radianes por unidad de distancia. La «longitud de onda» del modo es la longitud más pequeña, $\lambda$ (letra griega lambda), tal que un cambio de $x$ en $\lambda$ deja el modo sin cambiar,

$$A(x+\lambda) = A(x)\,. \qquad \text{(5.31)}$$

En otras palabras, la longitud de onda es la longitud de un ciclo completo de la onda, $2\pi$ radianes. Así, la longitud de onda, $\lambda$, y el número de onda angular, $k$, son inversamente proporcionales, con un factor de $2\pi$,

$$\lambda = \frac{2\pi}{k}\,. \qquad \text{(5.32)}$$

En este lenguaje, los modos normales del sistema de la figura 5.1 se describen mediante las funciones

$$A^n(x) = \sin kx\,, \qquad \text{(5.33)}$$

con

$$k = \frac{n\pi}{L}\,, \qquad \text{(5.34)}$$

donde $L=(N+1)a$ es la longitud total del sistema. Lo importante de (5.33) y (5.34) es que no dependen de los detalles del sistema; ni siquiera dependen de $N$. Los modos normales siempre tienen la misma forma, cuando el sistema tiene longitud $L$. Por supuesto, a medida que $N$ aumenta, aumenta el número de modos. Para $L$ fija, esto ocurre porque $a=L/(N+1)$ disminuye cuando $N$ aumenta, y por tanto el rango permitido de $k$ (recuerde (5.28)) aumenta.

Las formas (5.33) de los modos normales del sistema invariante bajo traslación espacial se llaman «ondas estacionarias». Veremos con más detalle más abajo por qué la palabra «onda» es apropiada. La palabra «estacionaria» se refiere al hecho de que, aunque las ondas cambian con el tiempo, no parecen moverse en la dirección $x$, a diferencia de las «ondas viajeras» que discutiremos en el capítulo 8 y más adelante.

### 5.2.1 La relación de dispersión

En términos del número de onda angular $k$, la frecuencia del modo es (de (5.16) y (5.27))

$$\omega^2 = 2B - 2C\cos ka\,. \qquad \text{(5.35)}$$

Tal relación entre $k$ (en realidad $k^2$, porque $\cos ka$ es una función par de $k$) y $\omega^2$ se llama «relación de dispersión» (más adelante aprenderemos por qué el nombre es apropiado). La forma específica (5.35) es una característica del sistema infinito particular de la figura 5.2: depende de las masas, las constantes de los muelles, las longitudes de los péndulos y las separaciones.

Pero no depende de las condiciones de contorno. De hecho, veremos más abajo que (5.35) será útil para condiciones de contorno muy distintas de las del sistema de la figura 5.1.

La relación de dispersión depende únicamente de la física del sistema infinito. $\qquad \text{(5.36)}$

De hecho, es solo a través de la relación de dispersión que los detalles de la física del sistema infinito entran en el problema. La forma de los modos, $e^{\pm ikx}$, ya está determinada por las propiedades generales de linealidad e invariancia bajo traslación espacial.

Llamaremos a (5.35) la relación de dispersión de los péndulos acoplados. Le hemos dado un nombre especial porque volveremos a ella muchas veces en lo que sigue. La física esencial es que hay dos fuentes de fuerza restauradora: la gravedad, que tiende a mantener todas las masas en equilibrio; y los muelles de acoplamiento, que tienden a mantener fijas las separaciones entre las masas, pero no se ven afectados si todas las masas se desplazan la misma distancia. En (5.35), las constantes siempre satisfacen $B\ge C$, como se ve en (5.6).

El límite $B=C$ es especialmente interesante: ocurre cuando no hay gravedad (o $\ell\to\infty$). La relación de dispersión es entonces

$$\omega^2 = 2B(1-\cos ka) = 4B\sin^2\frac{ka}{2}\,. \qquad \text{(5.37)}$$

Note que el modo con $k=0$ tiene ahora frecuencia cero, porque todas las masas pueden desplazarse a la vez sin fuerza restauradora.

## 5.3 Ondas

### 5.3.1 La cuerda con cuentas

![Figura 5.4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.4.png)

Figura 5.4: cuerda con cuentas en equilibrio, mostrando varias cuentas espaciadas regularmente sobre una cuerda tensa y recta.

Otro sistema instructivo es la cuerda con cuentas, sometida a oscilaciones transversales. Las oscilaciones se llaman «transversales» si el movimiento es perpendicular a la dirección en la que se extiende el sistema. Considere una cuerda sin masa, con tensión $T$, a la que se atan cuentas idénticas de masa $m$ a intervalos regulares, $a$. Una parte de tal sistema, en su configuración de equilibrio, se muestra en la figura 5.4. Las cuentas no pueden oscilar longitudinalmente, porque la cuerda se rompería (más precisamente, la cuerda tiene una constante de fuerza muy grande y no lineal para el estiramiento longitudinal; las oscilaciones longitudinales tienen una frecuencia mucho mayor y están mucho más fuertemente amortiguadas que las transversales, así que podemos ignorarlas en el rango de frecuencias de los modos transversales; véase la discusión del muelle masivo «ligero» en el capítulo 7). Sin embargo, para pequeñas oscilaciones transversales, el estiramiento de la cuerda es despreciable, y la tensión y la componente horizontal de la fuerza de la cuerda son aproximadamente constantes. La componente horizontal de la fuerza sobre cada bloque, debida a la cuerda de su derecha, se cancela con la componente horizontal debida a la cuerda de su izquierda. La fuerza horizontal total sobre cada bloque es cero (debe serlo, porque los bloques no se mueven horizontalmente). Pero las cuerdas producen una fuerza restauradora transversal cuando las cuentas vecinas no tienen el mismo desplazamiento transversal, como se ilustra en la figura 5.5. Se muestra la fuerza de la cuerda sobre la cuenta 1, junto con su componente transversal. Las líneas punteadas completan triángulos semejantes, de modo que $F/T=(\psi_2-\psi_1)/a$. Puede ver en la figura 5.5 que la fuerza restauradora, $F$ en la figura, es lineal para pequeñas oscilaciones transversales, y corresponde a una constante de muelle $T/a$.

![Figura 5.5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.5.png)

Figura 5.5: dos cuentas vecinas, 1 y 2, en una cuerda con cuentas, mostrando la fuerza de tensión $T$ a lo largo de la cuerda entre ambas y su componente transversal $F \approx (T/a)(\psi_2-\psi_1)$ sobre la cuenta 1.

Así, (5.37) es también la relación de dispersión para las pequeñas oscilaciones transversales de la cuerda con cuentas, con

$$B = \frac{T}{ma}\,, \qquad \text{(5.38)}$$

donde $T$ es la tensión de la cuerda, $m$ es la masa de la cuenta y $a$ es la separación entre cuentas. La relación de dispersión para la cuerda con cuentas puede escribirse entonces como

$$\omega^2 = \frac{4T}{ma}\sin^2\frac{ka}{2}\,. \qquad \text{(5.39)}$$

Esta relación de dispersión, (5.39), tiene la propiedad interesante de que $\omega\to0$ cuando $k\to0$. Esto se discute desde el punto de vista de la simetría en el apéndice C, donde se discute la conexión de esta relación de dispersión con lo que se llaman «bosones de Goldstone». Aquí deberíamos discutir las propiedades especiales del modo $k=0$, con frecuencia angular exactamente nula, $\omega=0$. Este caso es distinto de todos los demás valores de frecuencia angular, porque no obtenemos una dependencia temporal distinta al conjugar la exponencial compleja irreducible, $e^{-i\omega t}$. Pero necesitamos dos soluciones para describir las posibles condiciones iniciales del sistema, porque podemos especificar tanto un desplazamiento como una velocidad para cada cuenta. La resolución de este dilema es similar a la discutida para el amortiguamiento crítico en el capítulo 2 (véase (2.12)). Si nos acercamos a $\omega=0$ desde $\omega$ no nulo, podemos formar dos soluciones independientes así (puede evaluar estos límites fácilmente, usando el desarrollo de Taylor de $e^x=1+x+\cdots$):

$$\lim_{\omega\to0}\frac{e^{-i\omega t}+e^{i\omega t}}{2}=1\,,\qquad \lim_{\omega\to0}\frac{e^{-i\omega t}-e^{i\omega t}}{-2i\omega}=t\,. \qquad \text{(5.40)}$$

La primera, para $k=0$, describe una situación en la que todas las cuentas están en una posición fija. La segunda describe una situación en la que todas las cuentas se mueven juntas con velocidad constante en la dirección transversal.

Se pueden decir cosas precisamente análogas sobre la dependencia en $x$ del modo $k=0$. De nuevo, acercándonos a $k=0$ desde $k$ no nulo, podemos formar dos modos,

$$\lim_{k\to0}\frac{e^{ikx}+e^{-ikx}}{2}=1\,,\qquad \lim_{k\to0}\frac{e^{ikx}-e^{-ikx}}{2ik}=x\,. \qquad \text{(5.41)}$$

El segundo modo aquí describe una situación en la que cada cuenta sucesiva está más desplazada que la anterior. La fuerza transversal sobre cada cuenta, debida a la cuerda de la izquierda, se cancela con la fuerza de la cuerda de la derecha.

### 5.3.2 Extremos fijos

*(Referencia al programa interactivo 5-2 del disco de programas del curso original.)*

![Figura 5.6](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.6.png)

Figura 5.6: cuerda con cuentas de cuatro cuentas numeradas 1 a 4, con ambos extremos fijos a paredes.

Supongamos ahora que consideramos una cuerda con cuentas finita, con sus extremos fijos en $x=0$ y $x=L=(N+1)a$, como se muestra en la figura 5.6. El análisis de los modos normales de este sistema es exactamente el mismo que el del problema de los péndulos acoplados al principio del capítulo. De nuevo, imaginamos que el sistema finito es parte de un sistema infinito con invariancia bajo traslación espacial, y buscamos combinaciones lineales de modos tales que las cuentas en $x=0$ y $x=L$ estén fijas. De nuevo esto conduce a (5.33). Las únicas diferencias son:

1.  Las frecuencias de los modos son distintas, porque la relación de dispersión ahora viene dada por (5.39);
2.  (5.33) describe los desplazamientos transversales de las cuentas.

Este es un ejemplo muy bonito de los modos normales de onda estacionaria, (5.33), porque las formas se ven más fácilmente que para las oscilaciones longitudinales. Para cuatro cuentas ($N=4$), los cuatro modos normales independientes se ilustran en las figuras 5.7-5.10, donde hemos hecho invisibles las cuerdas de acoplamiento por claridad. Las cuentas imaginarias fijas que hacen el papel de las paredes se muestran (discontinuas) en $x=0$ y $x=L$. Superpuesta a las posiciones de las cuentas está la función continua $\sin kx$, para cada valor de $k$, representada con una línea punteada. Note que esta función no describe las posiciones de las cuerdas de acoplamiento, que están estiradas en línea recta entre cuentas vecinas.

![Figura 5.7](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.7.png)

Figura 5.7:-5.10: los cuatro modos normales de la cuerda con cuentas de 4 cuentas y extremos fijos, para $n=1,2,3,4$; cada figura muestra la curva $\sin(n\pi x/L)$ pasando por las cuentas, con un número creciente de nodos y “ondulaciones” a medida que $n$ aumenta.

Son imágenes como las figuras 5.7-5.10 las que justifican la palabra «onda» para estas soluciones de onda estacionaria: son, francamente, onduladas, y exhiben la dependencia espacial senoidal que es la característica esencial de los fenómenos ondulatorios.

La oscilación transversal de una cuerda con cuentas con ambos extremos fijos se ilustra en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-5-2" rel="noopener" target="_blank" title="Animación original de Howard Georgi">5-2</a>, donde se muestra una oscilación general junto con los modos normales de los que está formada. Note las distintas frecuencias de los distintos modos normales, con la frecuencia aumentando a medida que los modos se vuelven más ondulados. A menudo usaremos la cuerda con cuentas como ejemplo ilustrativo, porque los modos son muy fáciles de visualizar.

## 5.4 Extremos libres

Trabajemos un ejemplo de oscilación forzada con un tipo distinto de condición de contorno. Considere las oscilaciones transversales de una cuerda con cuentas. Para concretar, tomaremos cuatro cuentas, de modo que este es un sistema de cuatro osciladores acoplados. Sin embargo, en lugar de acoplar las cuerdas de los extremos a paredes fijas, las uniremos a anillos sin masa que pueden deslizar libremente en la dirección transversal sobre varillas sin fricción. Se dice entonces que la cuerda tiene sus extremos libres (al menos para el movimiento transversal). Entonces el sistema se ve como el diagrama de la figura 5.11, donde los osciladores se mueven hacia arriba y hacia abajo en el plano del papel. Encontremos sus modos normales.

![Figura 5.11](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.11.png)

Figura 5.11: cuerda con cuentas de cuatro cuentas, con ambos extremos unidos a anillos sin masa que deslizan libremente sobre varillas verticales sin fricción, en lugar de a paredes fijas.

### 5.4.1 Modos normales para extremos libres

*(Referencia al programa interactivo 5-3 del disco de programas del curso original.)*

Como antes, imaginamos que esto es parte de un sistema infinito de cuentas con invariancia bajo traslación espacial. Esto se muestra en la figura 5.12. Aquí, los anillos sin masa que deslizan sobre varillas sin fricción se han reemplazado por las cuentas imaginarias (discontinuas) 0 y 5. La relación de dispersión es exactamente la misma que para cualquier otra cuerda con cuentas infinita, (5.39). La pregunta entonces es: ¿qué tipo de condición de contorno en el sistema infinito corresponde a la condición de contorno física de que las cuentas de los extremos son libres por un lado? La respuesta es que la primera cuenta imaginaria de cada lado debe moverse hacia arriba y hacia abajo junto con la última cuenta real, de modo que la cuerda de acoplamiento de la cuenta 0 sea horizontal y no ejerza fuerza restauradora transversal sobre la cuenta 1, y la cuerda de acoplamiento de la cuenta 5 sea horizontal y no ejerza fuerza restauradora transversal sobre la cuenta 4:

$$A_0=A_1\,, \qquad \text{(5.42)}$$

$$A_4=A_5\,; \qquad \text{(5.43)}$$

![Figura 5.12](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.12.png)

Figura 5.12: satisfaciendo las condiciones de contorno en el sistema finito, con las cuentas imaginarias 0 y 5 unidas rígidamente a las cuentas reales 1 y 4, respectivamente.

Trabajaremos en la notación en la que las cuentas se etiquetan por su posición de equilibrio. Los modos normales del sistema infinito son entonces $e^{\pm ikx}$. Pero todavía no hemos tenido que decidir dónde pondremos el origen. ¿Cómo formamos una combinación lineal de los modos exponenciales complejos, $e^{\pm ikx}$, y elegimos $k$ de modo que sea consistente con esta condición de contorno? Empecemos con (5.42). Podemos escribir la combinación lineal, sea cual sea, en la forma

$$\cos(kx-\theta)\,. \qquad \text{(5.44)}$$

Cualquier combinación lineal real de $e^{\pm ikx}$ puede escribirse así, salvo una constante multiplicativa global (véase (1.96)). Ahora bien, si

$$\cos(kx_0-\theta) = \cos(kx_1-\theta)\,, \qquad \text{(5.45)}$$

donde $x_j$ es la posición del $j$-ésimo bloque, entonces o bien

1.  $\cos(kx-\theta)$ tiene un máximo o un mínimo en $(x_0+x_1)/2$, o
2.  $kx_1-kx_0$ es un múltiplo de $2\pi$.

Consideremos el caso 1 (veremos que el caso 2 no da modos adicionales). Elegiremos nuestras coordenadas de modo que el punto $(x_0+x_1)/2$, a medio camino entre $x_0$ y $x_1$, sea $x=0$. No nos importa la normalización global, así que, si la función tiene un mínimo ahí, la multiplicaremos por $-1$, para convertirlo en un máximo. Así, en el caso 1, la función $\cos(kx-\theta)$ tiene un máximo en $x=0$, lo que implica que podemos tomar $\theta=0$. Así, la función es simplemente $\cos kx$. El sistema con este etiquetado se muestra en la figura 5.13. El desplazamiento de la $j$-ésima cuenta es entonces

$$A_j = \cos[ka(j-1/2)]\,. \qquad \text{(5.46)}$$

![Figura 5.13](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.13.png)

Figura 5.13: el mismo sistema de osciladores, etiquetado de forma más conveniente, con el origen $x=0$ situado a medio camino entre las cuentas imaginarias 0 y la cuenta 1, de modo que las cuentas reales quedan en $x=a/2, 3a/2, 5a/2, 7a/2$.

Ahora debería quedar claro cómo imponer la condición de contorno, (5.43), en el otro extremo. Queremos tener un máximo o un mínimo a medio camino entre la cuenta 4 y la cuenta 5, en $x=4a$. Obtenemos un máximo o un mínimo cada vez que el argumento del coseno es un múltiplo entero de $\pi$. El argumento del coseno en $x=4a$ es $4ka$, donde $k$ es el número de onda angular. Así, la condición de contorno se satisfará si el modo tiene $4ka=n\pi$ para $n$ entero. Entonces

$$\cos[ka(4-1/2)] = \cos[ka(5-1/2)] \implies ka=\frac{n\pi}{4}\,. \qquad \text{(5.47)}$$

Así, los modos son

$$A_j = \cos[ka(j-1/2)] \quad\text{con } k=\frac{n\pi}{4a}\,,\ \text{para } n=0\text{ a }3\,. \qquad \text{(5.48)}$$

Para $n>3$, los modos simplemente se repiten, porque $k\ge\pi/a$.

En (5.48), $n=0$ es el modo trivial en el que todas las cuentas se mueven juntas hacia arriba y hacia abajo. Esto es posible porque no hay ninguna fuerza restauradora cuando todas las cuentas se mueven juntas. Como se discutió arriba (véase (5.40)), las cuentas pueden moverse todas con velocidad constante, porque $\omega=0$ para este modo. Note que el caso 2 anterior da el mismo modo, y nada más, porque si $kx_1-kx_0=2n\pi$, entonces (5.44) tiene el mismo valor para todas las $x_j$. Los modos restantes se muestran en las figuras 5.14-5.16. Este sistema se ilustra en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-5-3" rel="noopener" target="_blank" title="Animación original de Howard Georgi">5-3</a> del disco de programas.

![Figura 5.14](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.14.png)

Figura 5.14:-5.16: los modos $n=1,2,3$ de la cuerda con cuentas de extremos libres, mostrando $A_j = \cos[(j-1/2)n\pi/4]$ para cada valor de $n$, con ondulación creciente.

## 5.5 Oscilaciones forzadas y condiciones de contorno

Las oscilaciones forzadas pueden analizarse con los métodos del capítulo 3. Esto siempre funciona, incluso para una fuerza que actúa sobre cada parte del sistema de forma independiente. Sin embargo, muy a menudo, para un sistema invariante bajo traslación espacial, nos interesa un tipo distinto de problema de oscilación forzada: uno en el que la fuerza externa actúa solo en un extremo (o en ambos). En este caso, podemos resolver el problema de una forma mucho más simple, usando condiciones de contorno. Un ejemplo de este tipo se muestra en la figura 5.17.

![Figura 5.17](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.17.png)

Figura 5.17: sistema de péndulos acoplados igual al de la figura 5.1, pero con la pared derecha reemplazada por un agente externo que mueve el extremo del último muelle.

Este es el sistema de (5.1), salvo que se ha eliminado una pared y el extremo del muelle está obligado, por algún agente externo, a moverse hacia adelante y hacia atrás con un desplazamiento

$$z\cos\omega_dt\,. \qquad \text{(5.49)}$$

Como de costumbre, en un problema de oscilación forzada, primero consideramos el término impulsor, en este caso el desplazamiento fijo del bloque $N+1$, (5.49), como la parte real de un término impulsor exponencial complejo,

$$z\,e^{-i\omega_dt}\,. \qquad \text{(5.50)}$$

Luego buscamos una solución estacionaria en la que todo el sistema oscila con la frecuencia impulsora $\omega_d$, con la dependencia temporal irreducible $e^{-i\omega_dt}$.

Si hay amortiguamiento debido a una fuerza de fricción, por pequeña que sea, esta será la solución estacionaria que sobrevive después de que todas las oscilaciones libres se hayan extinguido. Podemos encontrar tales soluciones con el mismo tipo de truco que usamos para encontrar los modos de oscilación libre del sistema: buscamos modos del sistema infinito y los combinamos para satisfacer las condiciones de contorno.

Esta situación es distinta del problema de oscilación libre. En un problema típico de oscilación libre, las condiciones de contorno fijan $k$; luego determinamos $\omega$ a partir de la relación de dispersión. En este caso, las condiciones de contorno determinan $\omega_d$ en su lugar. Ahora debemos usar la relación de dispersión, (5.35), para encontrar el número de onda $k$.

Resolviendo (5.35) obtenemos

$$k = \frac{1}{a}\cos^{-1}\left(\frac{2B-\omega_d^2}{2C}\right)\,. \qquad \text{(5.51)}$$

Debemos combinar los modos del sistema infinito, $e^{\pm ikx}$, para satisfacer las condiciones de contorno en $x=0$ y $x=(N+1)a=L$. Como en el sistema (5.1), la condición de que el sistema esté inmóvil en $x=0$ conduce a un modo de la forma

$$\psi(x,t) = y\sin kx\,e^{-i\omega_dt} \qquad \text{(5.52)}$$

para cierta amplitud $y$. Pero ahora la condición en $x=L=(N+1)a$ determina, no el número de onda (que ya está fijado por la relación de dispersión), sino la amplitud $y$.

$$\psi(L,t) = y\sin kL\,e^{-i\omega_dt} = z\,e^{-i\omega_dt}\,. \qquad \text{(5.53)}$$

Así,

$$y = \frac{z}{\sin kL}\,. \qquad \text{(5.54)}$$

Note que si $\omega_d$ es una frecuencia de modo normal del sistema (5.1) sin amortiguamiento, entonces (5.54) no tiene sentido, porque $\sin kL$ se anula. Así debe ser: corresponde a la amplitud infinita producida por una fuerza impulsora en resonancia con una frecuencia normal de un sistema sin fricción. En presencia de amortiguamiento, sin embargo, como discutiremos en el capítulo 8, el número de onda $k$ es complejo, porque la relación de dispersión es compleja. Veremos más adelante que, si $k$ es complejo, $\sin kL$ no puede anularse. Incluso si el amortiguamiento es muy pequeño, por supuesto, no obtenemos un infinito real en la amplitud al acercarnos a la resonancia: eventualmente, los efectos no lineales toman el control. Si es la no linealidad o el amortiguamiento lo más importante cerca de una resonancia dada depende de los detalles del sistema físico (note también que, cuando $\sin kL$ es complejo, las partes del sistema no oscilan todas en fase, aunque todas oscilan a la misma frecuencia).

### 5.5.1 Oscilaciones forzadas con un extremo libre

![Figura 5.18](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.18.png)

Figura 5.18: masa sobre un muelle, con el otro extremo del muelle movido externamente de forma oscilante.

Como otro ejemplo, discutiremos de nuevo las oscilaciones longitudinales forzadas del sistema simple de una masa sobre un muelle, mostrado en la figura 5.18. La física aquí es la misma que la del sistema de la figura 2.9, salvo que, para empezar, ignoraremos el amortiguamiento. El bloque tiene masa $m$. El muelle tiene constante $K$ y longitud de equilibrio $a$. Para concretar, imagine que este bloque está sobre una mesa casi sin fricción, y que usted sostiene el otro extremo del muelle, moviéndolo hacia adelante y hacia atrás sobre la mesa, paralelamente a la dirección del muelle, con desplazamiento

$$d_0\cos\omega_dt\,. \qquad \text{(5.55)}$$

La pregunta es: ¿cómo se mueve el bloque? Ya sabemos resolver este problema desde el capítulo 2. Ahora lo haremos de una forma distinta, usando la invariancia bajo traslación espacial, las interacciones locales y las condiciones de contorno. Puede parecer sorprendente que podamos tratar este problema con las técnicas que hemos desarrollado para sistemas invariantes bajo traslación espacial, porque solo hay un bloque. Sin embargo, eso es lo que vamos a hacer. Ciertamente nada nos impide extender este sistema a un sistema infinito, repitiendo la combinación bloque-muelle. El sistema infinito tiene entonces la relación de dispersión de la cuerda con cuentas (o de los péndulos acoplados con $\ell\to\infty$):

$$\omega_d^2 = \frac{4K}{m}\sin^2\frac{ka}{2}\,. \qquad \text{(5.56)}$$

La parte relevante del sistema infinito se muestra en la figura 5.19. La idea es que podemos imponer condiciones de contorno sobre el sistema infinito, figura 5.19, que lo hagan equivalente a la figura 5.18.

![Figura 5.19](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.19.png)

Figura 5.19: fragmento del sistema infinito de masas y muelles, mostrando las masas 0, 1 y 2.

Empezamos imaginando que el desplazamiento es complejo, $d_0e^{-i\omega_dt}$, de modo que al final tomaremos la parte real para recuperar el resultado real de (5.55). Así, tomamos

$$\psi_2(t) = d_0\,e^{-i\omega_dt}\,. \qquad \text{(5.57)}$$

Entonces, para garantizar que no haya fuerza sobre el bloque 1 debida al muelle imaginario de la izquierda, debemos tomar

$$\psi_0(t) = \psi_1(t)\,. \qquad \text{(5.58)}$$

Para satisfacer (5.58), podemos argumentar, como en la figura 5.13, que

$$\psi(x,t) = z(t)\cos kx \qquad \text{(5.59)}$$

donde $x$ se define como en la figura 5.20.

![Figura 5.20](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.20.png)

Figura 5.20: una mejor definición del origen de $x$, con el origen a medio camino entre las masas 0 y 1.

Ahora, como la posición de equilibrio del bloque 2 es $3a/2$, sustituimos

$$\psi_2(t) = z(t)\cos\frac{3ka}{2} \qquad \text{(5.60)}$$

en (5.57), para obtener

$$z(t) = \frac{d_0}{\cos\frac{3ka}{2}}\,e^{-i\omega_dt}\,. \qquad \text{(5.61)}$$

Entonces el resultado final es

$$\psi_1(t) = \frac{\cos\frac{ka}{2}}{\cos\frac{3ka}{2}}\,d_0\,e^{-i\omega_dt} \qquad \text{(5.62)}$$

o, en forma real,

$$\psi_1(t) = \frac{\cos\frac{ka}{2}}{\cos\frac{3ka}{2}}\,d_0\cos\omega_dt\,. \qquad \text{(5.63)}$$

Ahora podemos usar la relación de dispersión. Primero usamos trigonometría,

$$\cos3y = \cos^3y-3\cos y\sin^2y = \cos y\left(1-4\sin^2y\right) \qquad \text{(5.64)}$$

para escribir

$$\psi_1(t) = \frac{1}{1-4\sin^2\frac{ka}{2}}\,d_0\cos\omega_dt \qquad \text{(5.65)}$$

o, sustituyendo (5.56),

$$\psi_1(t) = \frac{\omega_0^2}{\omega_0^2-\omega_d^2}\,d_0\cos\omega_dt\,, \qquad \text{(5.66)}$$

donde $\omega_0$ es la frecuencia de oscilación libre del sistema,

$$\omega_0^2 = \frac{K}{m}\,. \qquad \text{(5.67)}$$

Esta es exactamente la misma fórmula de resonancia que obtuvimos en el capítulo 2.

### 5.5.2 Generalización

La verdadera ventaja del procedimiento que usamos para resolver este problema es que es fácil de generalizar. Por ejemplo, supongamos que consideramos el sistema mostrado en la figura 5.21.

![Figura 5.21](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.21.png)

Figura 5.21: sistema con dos bloques en línea, unidos por muelles, con el extremo derecho movido externamente.

Aquí podemos pasar al mismo sistema infinito y argumentar que la solución es proporcional a $\cos kx$, donde $x$ se define como en la figura 5.22. Entonces el mismo argumento conduce al resultado para los desplazamientos de los bloques 1 y 2:

$$\psi_1(t) = \frac{\cos\frac{ka}{2}}{\cos\frac{5ka}{2}}\,d_0\cos\omega_dt\,,\qquad \psi_2(t) = \frac{\cos\frac{3ka}{2}}{\cos\frac{5ka}{2}}\,d_0\cos\omega_dt\,. \qquad \text{(5.68)}$$

![Figura 5.22](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.22.png)

Figura 5.22: el sistema infinito correspondiente, con el origen definido a medio camino entre las masas 0 y 1.

Debería poder generalizar esto a un número arbitrario de bloques.

## 5.6 Circuitos LC acoplados

Vimos en el capítulo 1 la analogía entre el circuito LC de la figura 1.10 y el sistema correspondiente de una masa y muelles de la figura 1.11. En esta sección discutimos qué ocurre cuando combinamos circuitos LC en un sistema invariante bajo traslación espacial.

Por ejemplo, considere un circuito infinito invariante bajo traslación espacial, del que se muestra un fragmento en la figura 5.23. Podría suponerse, basándose en la discusión del capítulo 1, que el circuito de la figura 5.23 es análogo a la combinación de muelles y masas mostrada en la figura 5.24, con la correspondencia entre ambos sistemas:

![Figura 5.24](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.24.png)

Figura 5.24

$$m \leftrightarrow L\,,\qquad K \leftrightarrow 1/C\,,\qquad x_j \leftrightarrow Q_j \qquad \text{(5.69)}$$

donde $x_j$ es el desplazamiento del $j$-ésimo bloque hacia la derecha, y $Q_j$ es la carga que ha «pasado» a través del $j$-ésimo inductor desde la situación de equilibrio con los condensadores descargados.

![Figura 5.23](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.23.png)

Figura 5.23: circuito infinito de inductores $L$ y condensadores $C$ conectados alternativamente, con separación $a$ entre elementos idénticos. Figura 5.24: sistema mecánico análogo — cadena infinita de masas $m$ conectadas por muelles $K$.

De hecho, esto es correcto, y podríamos usar (5.69) para escribir la relación de dispersión de la figura 5.23. Sin embargo, con nuestras potentes herramientas de linealidad e invariancia bajo traslación espacial, podemos resolver el problema desde cero sin demasiado esfuerzo. La estrategia será escribir lo que sabemos que debe parecer la solución, por la invariancia bajo traslación espacial, y luego trabajar hacia atrás para encontrar la relación de dispersión.

El punto de partida debería resultarle familiar a estas alturas. Como el sistema es lineal e invariante bajo traslación espacial, los modos del sistema infinito son proporcionales a $e^{\pm ikx}$. Por tanto, todas las cantidades físicas de un modo —voltajes, cargas, corrientes, lo que sea— también deben ser proporcionales a $e^{\pm ikx}$. En este caso, la variable $x$ es realmente solo una etiqueta: las propiedades eléctricas del circuito no dependen mucho de la disposición de los elementos en el espacio (esto no es exactamente cierto, sin embargo: la relatividad impone restricciones; véase el capítulo 11). La relación de dispersión dependerá solo de $ka$, donde $a$ es la separación entre las partes idénticas del sistema (véase (5.35)). Sin embargo, es más fácil pensar en el sistema si se dispone físicamente en una configuración invariante bajo traslación espacial, como en la figura 5.23.

![Figura 5.25](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.25.png)

Figura 5.25: etiquetado del sistema infinito de circuitos LC acoplados, con los inductores numerados $-2,-1,0,1$ y los condensadores en las posiciones intermedias.

En particular, etiquetemos los inductores y condensadores como se muestra en la figura 5.25. Entonces la carga desplazada a través del $j$-ésimo inductor, en el modo con número de onda angular $k$, es

$$Q_j(t) = q\,e^{ijka}\,e^{-i\omega t} \qquad \text{(5.70)}$$

para alguna carga constante $q$. Note que igualmente podríamos haber tomado la dependencia temporal como $\cos\omega t$, $\sin\omega t$, o $e^{i\omega t}$; no importa para el argumento siguiente. Lo que importa es que, al derivar $Q_j(t)$ dos veces respecto al tiempo, obtenemos $-\omega^2Q_j(t)$. La corriente a través del $j$-ésimo inductor es

$$I_j = \frac{d}{dt}Q_j(t) = -i\omega q\,e^{ijka}\,e^{-i\omega t}\,. \qquad \text{(5.71)}$$

La carga en el $j$-ésimo condensador, que llamaremos $q_j$, también es proporcional a $e^{ijka}e^{-i\omega t}$, pero de hecho podemos calcularla directamente. La carga, $q_j$, es simplemente

$$q_j = Q_j - Q_{j+1} \qquad \text{(5.72)}$$

porque la carga desplazada a través del $j$-ésimo inductor debe fluir hacia el $j$-ésimo condensador, o pasar a través del inductor $j+1$, de modo que $Q_j=q_j+Q_{j+1}$. Ahora podemos calcular el voltaje, $V_j$, de cada condensador,

$$V_j = \frac{1}{C}(Q_j-Q_{j+1}) = \frac{q}{C}\left(1-e^{ika}\right)e^{ijka}\,e^{-i\omega t}\,, \qquad \text{(5.73)}$$

y luego calcular la caída de voltaje a través de los inductores,

$$L\,\frac{dI_j}{dt} = V_{j-1}-V_j\,, \qquad \text{(5.74)}$$

sustituyendo (5.71) y (5.73) en (5.74), y dividiendo ambos lados por el factor común $-qL\,e^{ijka}e^{-i\omega t}$, obtenemos la relación de dispersión,

$$\omega^2 = -\frac{1}{LC}\left(1-e^{ika}\right)\left(e^{-ika}-1\right) = \frac{4}{LC}\sin^2\frac{ka}{2}\,. \qquad \text{(5.75)}$$

Esto corresponde a (5.37) con $B=1/LC$. Esto es justamente lo que esperamos de (5.69). Llamaremos a (5.75) la relación de dispersión de los circuitos LC acoplados.

### 5.6.1 Un ejemplo de circuitos LC acoplados

![Figura 5.26](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.26.png)

Figura 5.26: circuito con tres inductores en serie, cada uno conectado a un condensador a tierra, formando un sistema finito. Figura 5.27: sistema mecánico análogo, tres masas conectadas por cuatro muelles entre dos paredes fijas.

Usemos los resultados de esta sección para estudiar un ejemplo finito, con condiciones de contorno. Considere el circuito mostrado en la figura 5.26. Este circuito es análogo a la combinación de muelles y masas mostrada en la figura 5.27.

![Figura 5.27](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.27.png)

Figura 5.27

Ya sabemos que esto es cierto para el interior. Solo queda entender las condiciones de contorno en los extremos. Si etiquetamos los inductores como se muestra en la figura 5.28, podemos imaginar que este sistema es parte del sistema infinito mostrado en la figura 5.23, con las cargas obligadas a satisfacer

$$Q_0=Q_4=0\,. \qquad \text{(5.76)}$$

![Figura 5.28](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.28.png)

Figura 5.28: etiquetado de los inductores del circuito de la figura 5.26, numerados 1, 2 y 3.

Esto debe ser correcto: no puede desplazarse carga a través de los inductores 0 y 4, porque en la figura 5.26 estos no existen. Esto es justamente lo que esperamos de la analogía con el sistema de (5.27), donde el desplazamiento de los bloques 0 y 4 debe anularse, porque ocupan el lugar de las paredes fijas.

Ahora podemos escribir inmediatamente la solución para los modos normales, en analogía con (5.21) y (5.22),

$$Q_j \propto \sin\frac{jn\pi}{4} \qquad \text{(5.77)}$$

para $n=1$ a $3$.

### 5.6.2 Un problema de oscilación forzada para circuitos LC acoplados

![Figura 5.29](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.29.png)

Figura 5.29: circuito con tres inductores, con una fuente de voltaje oscilante conectada en un extremo. Figura 5.30: los voltajes $V_0$ a $V_3$ en los distintos nodos del sistema de la figura 5.29.

Un ejemplo algo más práctico puede ser instructivo. Considere el circuito mostrado en la figura 5.29. El símbolo de fuente en la figura representa una fuente de voltaje que varía armónicamente. Supondremos que el voltaje en este punto del circuito está fijado por la fuente, de modo que

![Figura 5.30](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.30.png)

Figura 5.30

$$V\cos\omega t\,. \qquad \text{(5.78)}$$

Nos gustaría encontrar los voltajes en los otros nodos del sistema, como se muestra en la figura 5.30, con

$$V_3 = V\cos\omega t\,. \qquad \text{(5.79)}$$

Podríamos resolver este problema usando las cargas desplazadas; sin embargo, es un poco más fácil usar el hecho de que todas las cantidades físicas del sistema infinito de la figura 5.23 son proporcionales a $e^{ikx}$ en un modo con número de onda angular $k$. Como este es un problema de oscilación forzada (y, como de costumbre, ignoramos las posibles oscilaciones libres del sistema y buscamos la solución estacionaria), $k$ queda determinado por $\omega$ mediante la relación de dispersión del sistema infinito de circuitos LC acoplados, (5.75).

Lo otro que necesitamos es que

$$V_0=0\,, \qquad \text{(5.80)}$$

porque el circuito está cortocircuitado en ese extremo. Así, debemos combinar los dos modos del sistema infinito, $e^{\pm ikx}$, en $\sin kx$, y la solución tiene la forma

$$V_j \propto \sin jka\,. \qquad \text{(5.81)}$$

Podemos satisfacer la condición de contorno en el otro extremo tomando

$$V_j = \frac{V}{\sin3ka}\sin jka\,\cos\omega t\,. \qquad \text{(5.82)}$$

Esta es la solución.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Reconocer un sistema finito como parte de un sistema infinito invariante bajo traslación espacial;
2.  Encontrar los modos normales del sistema finito como combinaciones lineales de modos normales del sistema infinito invariante bajo traslación espacial, consistentes con la física de las fronteras, imponiendo condiciones de contorno;
3.  Describir los modos normales de un sistema invariante bajo traslación espacial en términos de un número de onda angular, $k$;
4.  Encontrar la relación de dispersión que relaciona la frecuencia angular, $\omega$, con el número de onda angular, $k$;
5.  Resolver problemas de oscilación forzada usando condiciones de contorno;
6.  Analizar sistemas invariantes bajo traslación espacial de circuitos LC acoplados.

## Problemas

**5.1.** Considere las pequeñas oscilaciones longitudinales del sistema mostrado a continuación: cuatro péndulos acoplados idénticos en línea, entre dos paredes fijas, cada masa de masa $m$, cada péndulo de longitud $\ell$, cada muelle de constante $\kappa$, con separación de equilibrio $a$ entre las masas.

1.  Encuentre la matriz $M^{-1}K$ de este sistema en la base en la que los desplazamientos de los bloques respecto al equilibrio se miden todos hacia la derecha y se organizan en un vector de la forma obvia,

$$X(t) = \begin{pmatrix}x_1(t)\\x_2(t)\\x_3(t)\\x_4(t)\end{pmatrix}\,.$$

1.  Clasifique como VERDADERO o FALSO cada una de las siguientes afirmaciones sobre los modos normales de este sistema. Si es posible, explique sus respuestas cualitativamente, es decir, en palabras en lugar de sustituir en una fórmula, y discuta la generalidad de sus resultados.

    1.  En el modo normal de frecuencia más baja, todos los bloques se mueven en la misma dirección cuando se mueven.
    2.  En el modo normal de segunda frecuencia más baja, el primer y el segundo bloque tienen el mismo desplazamiento.
    3.  En el modo normal de frecuencia más alta, los bloques vecinos se mueven en direcciones opuestas cuando se mueven.

2.  Encuentre las frecuencias angulares de cada uno de los modos normales. Pista: puede querer usar la relación de dispersión de los péndulos acoplados,

$$\omega^2 = 2B-2C\cos ka$$

donde

$$B = \frac{g}{2\ell}+\frac{\kappa}{m}\,,\qquad C=\frac{\kappa}{m}\,.$$

**5.2.** Considere el sistema de cinco bloques mostrado en la figura, todos de masa $m$, obligados a moverse solo horizontalmente. Los muelles largos, con seis espiras, tienen constante $K$. Los muelles más cortos, con tres espiras, tienen constante $2K$. Los muelles más cortos aún, con dos espiras, tienen constante $3K$ (como verá en el capítulo 7, esto es lo esperado si todos los muelles están hechos del mismo material).

![Figura](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/figs1.png)

Figura: cinco bloques en línea entre dos paredes fijas, conectados por una alternancia de muelles largos (constante $K$), medianos (constante $2K$) y cortos (constante $3K$), en un patrón simétrico.

Encuentre los modos normales del sistema y las frecuencias correspondientes. Asegúrese de justificar cualquier suposición que haga sobre los modos normales. Pista: intente encontrar un sistema infinito con invariancia bajo traslación espacial que contenga a este de tal forma que pueda incorporar la física de las paredes como condición de contorno. Otra pista: esto solo funciona de forma simple si los muelles de tres espiras tienen exactamente el doble de la constante de los muelles largos. Su respuesta debería explicar por qué.

**5.3.** En la cuerda con cuentas mostrada a continuación, el intervalo entre cuentas vecinas es $a$, y la distancia entre las cuentas de los extremos y las paredes es $a/2$. Todas las cuentas tienen masa $m$ y están obligadas a moverse solo verticalmente, en el plano del papel.

![Figura](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/figs2.png)

Figura: cinco cuentas numeradas 1 a 5 sobre una cuerda, separadas una distancia $a$ entre sí y $a/2$ de las paredes en ambos extremos.

Demuestre que la física de la pared izquierda puede incorporarse pasando a un sistema infinito y exigiendo la condición de contorno $A_0=-A_1$.

1.  Fácil: encuentre la condición de contorno análoga para la pared derecha.

2.  Encuentre los modos normales y las frecuencias correspondientes.

**5.4.** Considere el siguiente circuito: seis nodos con voltajes $V_0$ a $V_6$, conectados en cadena por inductores idénticos, con condensadores idénticos a tierra en cada nodo intermedio, y el nodo central conectado a tierra.

Todos los condensadores tienen la misma capacitancia, $C\approx0.00667\ \mu\text{F}$, y todos los inductores tienen la misma inductancia, $L\approx150\ \mu\text{H}$, y ninguna resistencia. El hilo central está conectado a tierra. Este circuito es un análogo eléctrico de los sistemas invariantes bajo traslación espacial de osciladores mecánicos acoplados que hemos discutido en este capítulo.

Cuando aplica una señal oscilante armónicamente desde un generador de señales, a través de un cable coaxial, a $V_6$, se inducen distintos voltajes oscilantes a lo largo de la línea. Es decir, si

$$V_6(t) = V\cos\omega t\,,$$

entonces $V_j(t)$ tiene la forma

$$V_j(t) = A_j\cos\omega t + B_j\sin\omega t\,.$$

Encuentre $A_j$ y $B_j$.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.
