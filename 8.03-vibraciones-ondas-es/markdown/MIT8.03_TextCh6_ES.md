# Capítulo 6: Límite continuo y series de Fourier

«Continuo» está en el ojo del observador. La mayoría de los sistemas que consideramos continuos están en realidad formados por partes discretas. En este capítulo mostramos que un sistema discreto puede parecer continuo a escalas de distancia mucho mayores que la separación entre sus partes. También exploraremos la física y las matemáticas de las series de Fourier.

## Vídeos de esta clase (YouTube)

- [Clase 8: Simetría de traslación](https://www.youtube.com/watch?v=J1uHGy1tRmM)
- [Clase 9: Ecuación de ondas, ondas estacionarias, series de Fourier](https://www.youtube.com/watch?v=1JeBWHzrRD4)
- [Clase 10: Ondas viajeras](https://www.youtube.com/watch?v=SnNmbVH5DAM)
- [Clase 11: Ondas sonoras](https://www.youtube.com/watch?v=RhIh1zw0-BM)

## Resumen previo

En este capítulo discutimos la ecuación de ondas, el punto de partida de otros tratamientos de las ondas. La obtendremos como resultado natural de nuestros principios generales de invariancia bajo traslación espacial e interacciones locales, aplicados a sistemas continuos.

1.  Estudiaremos los sistemas discretos invariantes bajo traslación espacial discutidos en el capítulo anterior, en el límite en que la separación entre partes tiende a cero. Argumentaremos que el resultado genérico es un sistema continuo que obedece la ecuación de ondas.

2.  El límite continuo de la cuerda con cuentas es una cuerda continua con oscilaciones transversales. Discutiremos sus modos normales para diversas condiciones de contorno. Veremos que los modos normales de un sistema continuo invariante bajo traslación espacial son los mismos que los de un sistema finito; la única diferencia es que hay un número infinito de ellos. La suma sobre el número infinito de modos normales necesaria para resolver el problema de valores iniciales de tal sistema continuo se llama serie de Fourier.

## 6.1 El límite continuo

Considere un sistema discreto invariante bajo traslación espacial en el que la separación entre masas vecinas es $a$. Si $a$ es muy pequeño, el sistema discreto parece continuo. Para entender esta afirmación, considere la acción de la matriz $M^{-1}K$, (5.8), en la notación del capítulo anterior, en la que los grados de libertad se etiquetan por su posición de equilibrio. La matriz $M^{-1}K$ actúa sobre un vector para producir otro vector. Hemos reemplazado nuestros vectores por funciones de $x$, así que $M^{-1}K$ es algo que actúa sobre una función $A(x)$ para dar otra función. Llamémosla $M^{-1}KA(x)$. Es más fácil ver qué ocurre para la cuerda con cuentas, para la cual $B=C=T/ma$. Entonces

$$M^{-1}KA(x) = \left(\frac{T}{ma}\right)\left(2A(x)-A(x+a)-A(x-a)\right)\,. \qquad \text{(6.1)}$$

Hasta aquí, (6.1) es correcta para cualquier $a$, grande o pequeño.

Siempre que diga que una cantidad dimensional, como la longitud $a$, es grande o pequeña, debe especificar una cantidad de comparación: debe decir grande o pequeña *comparada con qué* (una cantidad adimensional no requiere este paso: un número adimensional es grande si es mucho mayor que uno, y pequeño si es mucho menor que uno). En este caso, la otra cantidad dimensional del problema con dimensiones de longitud es la longitud de onda del modo que nos interesa. Aquí es donde entra el que $a$ sea pequeño. Si solo nos interesan modos con longitud de onda $\lambda=2\pi/k$ muy grande comparada con $a$, entonces $ka$ es un número adimensional muy pequeño, y $A(x+a)$ está muy cerca de $A(x)$. Podemos expandirla en una serie de Taylor rápidamente convergente. Expandiendo (6.1) en serie de Taylor obtenemos

$$M^{-1}KA(x) = -\frac{Ta}{m}\,\frac{\partial^2A(x)}{\partial x^2} + \cdots \qquad \text{(6.2)}$$

donde los puntos suspensivos representan términos de derivadas superiores, más pequeños por potencias del número pequeño $ka$ que el primer término de (6.2). En el límite en que tomamos $a$ realmente diminuto (siempre en comparación con las longitudes de onda que queremos estudiar), podemos reemplazar $m/a$ por la densidad de masa lineal $\rho_L$, o masa por unidad de longitud de la cuerda ahora casi continua, e ignorar los términos de orden superior. En este límite, podemos reemplazar la matriz $M^{-1}K$ por la combinación de derivadas que aparece en el primer término superviviente de la serie de Taylor, (6.2),

$$M^{-1}K \to -\frac{T}{\rho_L}\,\frac{\partial^2}{\partial x^2}\,. \qquad \text{(6.3)}$$

Entonces la ecuación de movimiento para $\psi(x,t)$ se convierte en la ecuación de ondas:

$$\frac{\partial^2}{\partial t^2}\psi(x,t) = \frac{T}{\rho_L}\,\frac{\partial^2}{\partial x^2}\psi(x,t)\,. \qquad \text{(6.4)}$$

La relación de dispersión es

$$\omega^2 = \frac{T}{\rho_L}\,k^2\,. \qquad \text{(6.5)}$$

Esto puede verse directamente sustituyendo el modo normal $e^{ikx}$ en (6.4), o tomando el límite de (5.37)-(5.38) cuando $a\to0$. La ecuación (6.5) es la relación de dispersión de la cuerda continua ideal. La cantidad $\sqrt{T/\rho_L}$ tiene dimensiones de velocidad; se llama la «velocidad de fase», $v_\varphi$. Como discutiremos con mucho más detalle en el capítulo 8 y siguientes, esta es la velocidad con la que las ondas viajeras se mueven por la cuerda.

Llamaremos «aproximación del continuo» a la aproximación de reemplazar un sistema discreto por un sistema continuo que se ve aproximadamente igual para $k\gg1/a$. En realidad, todos los sistemas mecánicos que consideraremos son discretos, al menos a nivel atómico. Sin embargo, si solo nos preocupan las ondas con longitudes de onda macroscópicas, la aproximación del continuo es muy buena.

### 6.1.1 Filosofía y especulación

Nuestro tratamiento de la ecuación de ondas en (6.4) es un poco inusual. En muchos tratamientos de los fenómenos ondulatorios, se le da a la ecuación de ondas un lugar de honor. De hecho, la ecuación de ondas es solo una reformulación de la relación de dispersión, (6.5), que habitualmente es solo una aproximación a lo que realmente está ocurriendo. Casi todos los sistemas que habitualmente tratamos con la ecuación de ondas son en realidad discretos a distancias muy pequeñas. En realidad no podemos llegar del todo al límite continuo que da (6.5). Las ondas de luz, que estudiaremos en los próximos capítulos, hasta donde sabemos, podrían ser una excepción a esta regla, y ser completamente continuas. Sin embargo, en realidad no tenemos derecho a suponer ni siquiera eso. Podría ser que, a distancias muy cortas, muy por debajo de todo lo que podemos observar hoy, la naturaleza de la luz e incluso del espacio y el tiempo cambie de alguna manera, de modo que el espacio y el tiempo mismos tengan cierta escala de longitud característica diminuta, $a$. El análisis anterior muestra que ¡esto no importa! Mientras solo podamos observar el espacio y el tiempo a distancias mucho mayores que $a$, nos parecerán continuos. Entonces, como somos científicos, preocupados por cómo se ve el mundo en nuestros experimentos, y no por cómo se comporta en algún régimen ideal muy más allá de lo que podemos sondear experimentalmente, bien podemos tratarlos como continuos.

## 6.2 Series de Fourier

### 6.2.1 La cuerda con extremos fijos

*(Referencia al programa interactivo 6-1 del disco de programas del curso original.)*

Si estiramos nuestra cuerda continua entre paredes fijas, de modo que $\psi(0)=\psi(\ell)=0$, los modos vienen dados por (5.33) y (5.34), igual que para el sistema discreto. La única diferencia es que ahora $n$ va de 1 a $\infty$, o al menos hasta un $n$ tan grande que la longitud de onda $2\pi/k=2\ell/n$ sea tan pequeña que la aproximación del continuo deje de valer. Esto se sigue de (5.28), que, como aquí $k$ es real, se convierte en

$$-\frac{\pi}{a} < k \le \frac{\pi}{a}\,. \qquad \text{(6.6)}$$

A medida que $a\to0$, el rango permitido de $k$ crece hasta el infinito.

Estos modos de onda estacionaria se animan en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-6-1" rel="noopener" target="_blank" title="Animación original de Howard Georgi">6-1</a> del disco de programas, suponiendo la relación de dispersión (6.5).

Ahora podemos discutir la base física de la serie de Fourier. En (3.77), en el capítulo 3, mostramos que los modos normales de un sistema discreto son linealmente independientes y completos. Eso significa que cualquier desplazamiento del sistema discreto puede escribirse como una única combinación lineal de los modos normales. Físicamente, esto debe ser así para poder resolver el problema de valores iniciales. Nuestra imagen de la cuerda continua es un límite de la cuerda con cuentas en el que el número de cuentas, $N$, tiende a infinito y las cuentas se acercan infinitamente entre sí. Para cada $N$, el desplazamiento más general del sistema puede desarrollarse como una combinación lineal de los $N$ modos normales. Si el límite $N\to\infty$ se comporta razonablemente bien, cabría esperar que el desplazamiento más general de la cuerda continua límite pudiera desarrollarse en términos del número infinito de modos normales del sistema continuo. Este desarrollo es una serie de Fourier. El desplazamiento del sistema continuo se describe mediante una función de la posición a lo largo de la cuerda. Si la función no es demasiado discontinua, el desarrollo en modos normales funciona bien.

Considere la cuerda continua, estirada entre paredes fijas en $x=0$ y $x=\ell$. El desplazamiento transversal de este sistema en cualquier instante se describe mediante una función continua de $x$, $\psi(x)$, con

$$\psi(0) = \psi(\ell) = 0\,. \qquad \text{(6.7)}$$

Así, esperamos, por el argumento anterior, poder expresar cualquier función que no sea demasiado discontinua y que satisfaga (6.7) como una suma de los modos normales dados por (5.33) y (5.34),

$$\psi(x) = \sum_{n=1}^{\infty}c_n\sin\frac{n\pi x}{\ell}\,. \qquad \text{(6.8)}$$

Las constantes $c_n$ se llaman los «coeficientes de Fourier». Pueden encontrarse usando la siguiente identidad:

$$\int_0^\ell dx\,\sin\frac{n\pi x}{\ell}\sin\frac{n'\pi x}{\ell} = \begin{cases}\ell/2 & \text{si } n=n'\\ 0 & \text{si } n\neq n'\end{cases} \qquad \text{(6.9)}$$

de modo que

$$c_n = \frac{2}{\ell}\int_0^\ell dx\,\sin\frac{n\pi x}{\ell}\,\psi(x)\,. \qquad \text{(6.10)}$$

Este es simplemente el método de las coordenadas normales adaptado a la situación continua.

### 6.2.2 Extremos libres

*(Referencia al programa interactivo 6-2 del disco de programas del curso original.)*

La ecuación (6.8) se llama la serie de Fourier de una función que satisface (6.7). Otras condiciones de contorno dan series distintas. Por ejemplo, considere una cuerda con el extremo $x=0$ fijo en $z=0$. Suponga que el otro extremo, en $x=\ell$, está unido a un anillo sin masa que puede deslizar libremente a lo largo de una varilla sin fricción en la dirección $z$, como se muestra en la figura 6.1. Decimos que este sistema tiene un «extremo libre», porque el extremo en $x=\ell$ es libre de deslizar en la dirección transversal, aunque está fijo en la dirección $x$.

![Figura 6.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh6_ES/fig6.1.png)

Figura 6.1: cuerda continua con el extremo $x=0$ fijo y el extremo $x=\ell$ unido a un anillo sin masa que desliza libremente sobre una varilla sin fricción, perpendicular a la cuerda.

Como la varilla no tiene fricción, la fuerza sobre el anillo debida a la varilla no puede tener componente en la dirección $z$. Pero, como el anillo no tiene masa, la fuerza total sobre él debe anularse. Por tanto, la fuerza sobre el anillo debida a la cuerda tampoco puede tener componente en la dirección $z$. Esto implica que la cuerda es horizontal en $x=\ell$. Pero la forma de la cuerda en un instante dado viene dada por la gráfica del desplazamiento transversal, $\psi(x,t)$, frente a $x$ (esta es la razón por la que las oscilaciones transversales son más fáciles de visualizar que las longitudinales; compárese con (7.5)). Así, la pendiente de $\psi(x,t)$ en $x=\ell$ debe anularse. Por tanto, las condiciones de contorno apropiadas para el desplazamiento son

$$\psi(0,t) = 0\,,\qquad \left.\frac{\partial}{\partial x}\psi(x,t)\right|_{x=\ell} = 0\,. \qquad \text{(6.11)}$$

Esto implica que los modos normales también satisfacen condiciones de contorno similares:

$$A_n(0)=0\,,\qquad A_n'(\ell)=0\,. \qquad \text{(6.12)}$$

La primera condición implica que la solución debe tener la forma

$$A_n(x) \propto \sin k_nx \qquad \text{(6.13)}$$

para cierto $k_n$. La segunda condición determina los posibles valores de $k_n$: implica que $\sin k_nx$ debe tener un máximo o un mínimo en $x=\ell$, lo que a su vez implica que

$$k_n\ell = \frac{\pi}{2}+n\pi \qquad \text{(6.14)}$$

donde $n$ es un entero no negativo (no negativo porque podemos elegir todos los $k_n>0$ en (6.13); los valores negativos solo cambian el signo de $A_n(x)$ y no dan lugar a soluciones nuevas). Las soluciones tienen la forma

$$\sin\left(\frac{(2n+1)\pi x}{2\ell}\right) \quad\text{para } n=0\text{ a }\infty\,. \qquad \text{(6.15)}$$

Estos modos normales se animan en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-6-2" rel="noopener" target="_blank" title="Animación original de Howard Georgi">6-2</a>. Con estos modos normales, podemos describir una función arbitraria, $\psi(x)$, que satisfaga las condiciones de contorno de este sistema, (6.11),

$$\psi(0)=0\,,\qquad \psi'(\ell)=0\,. \qquad \text{(6.16)}$$

Así, para tal función, podemos escribir

$$\psi(x) = \sum_{n=1}^{\infty}c_n\sin\left(\frac{(2n+1)\pi x}{2\ell}\right) \qquad \text{(6.17)}$$

donde

$$c_n = \frac{2}{\ell}\int_0^\ell dx\,\sin\left(\frac{(2n+1)\pi x}{2\ell}\right)\psi(x)\,. \qquad \text{(6.18)}$$

### 6.2.3 Ejemplos de series de Fourier

*(Referencia al programa interactivo 6-3 del disco de programas del curso original.)*

Encontremos los coeficientes de Fourier de la siguiente función, definida en el intervalo $[0,1]$:

$$\psi(x) = \begin{cases} x & \text{para } x\le w\,,\\ \dfrac{w(1-x)}{1-w} & \text{para } x>w\,. \end{cases} \qquad \text{(6.19)}$$

Para concretar, tomaremos $w=0.75$, de modo que la función $\psi(x)$ tiene la forma mostrada en la figura 6.2.

![Figura 6.2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh6_ES/fig6.2.png)

Figura 6.2: la función $\psi(x)$ para $w=0.75$ — un triángulo asimétrico que sube linealmente desde $(0,0)$ hasta $(0.75,0.75)$ y baja linealmente hasta $(1,0)$.

Calculamos los coeficientes de Fourier usando (6.10). Como $\ell=1$, esto toma la siguiente forma (véase el problema 6.2):

$$c_n = \int_0^1 dx\,\sin n\pi x\,\psi(x) = \int_0^w dx\,x\sin n\pi x + \int_w^1 dx\,\frac{w(1-x)}{1-w}\sin n\pi x = \frac{\sin n\pi w}{(1-w)n^2\pi^2}\,. \qquad \text{(6.20)}$$

Podemos reconstruir la función, $\psi(x)$, como una suma sobre los modos normales de la cuerda. Veamos los primeros términos de la serie para hacernos una idea de cómo funciona esto. El primer término de la suma, para $w=0.75$, se muestra en la figura 6.3. Esta es necesariamente una mala aproximación, porque la función no es simétrica respecto a $x=1/2$, mientras que el primer término de la suma sí lo es. Los dos primeros términos se muestran en la figura 6.4; esto se ve mucho mejor.

![Figura 6.4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh6_ES/fig6.4.png)

Figura 6.4

![Figura 6.3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh6_ES/fig6.3.png)

Figura 6.3:-6.5: aproximaciones sucesivas de $\psi(x)$ mediante 1, 2 y 6 términos de la serie de Fourier, respectivamente, comparadas con la función triangular original mostrada con línea punteada; la aproximación mejora progresivamente salvo cerca del pico angular.

Los primeros seis términos se muestran en la figura 6.5. Esta es ya una muy buena aproximación, salvo donde la función tiene un pico angular.

Lo que ocurre aquí es que, si incluimos términos de la serie de Fourier solo hasta $n=N$, podemos ver cómo funciona esto con más detalle estudiando la figura 6.6. La curva de trazos largos es el primer término de la serie de Fourier. Evidentemente, es menor que la función $\psi(x)$ (el triángulo punteado) para $x$ grande, y mayor que $\psi(x)$ para $x$ pequeño. El signo y la magnitud del segundo término de la serie de Fourier, la curva de trazos cortos en la figura 6.6, se eligen para compensar esta discrepancia, de modo que la suma (la curva continua) queda mucho más cerca de la función real. El mismo proceso se repite una y otra vez a medida que se avanza a órdenes superiores en la serie de Fourier truncada.

![Figura 6.6](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh6_ES/fig6.6.png)

Figura 6.6: los dos primeros términos de la serie de Fourier de $\psi(x)$ y su suma, mostrando cómo el primer término sobreestima la función para $x$ pequeño y la subestima para $x$ grande, y cómo el segundo término corrige esta discrepancia.

Puede jugar con la serie de Fourier truncada de la función $\psi(x)$ en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-6-3" rel="noopener" target="_blank" title="Animación original de Howard Georgi">6-3</a>. Este programa le permite variar el parámetro $w$, y también el número de términos de la serie de Fourier. Debería observar qué ocurre cerca de $w=1$. Podría pensar que esto causaría problemas para la serie de Fourier, porque el $(1-w)$ del denominador de (6.20) tiende a cero. Sin embargo, el límite en realidad se comporta bien, porque $\sin n\pi w$ también tiende a cero cuando $w\to1$. Sin embargo, la serie de Fourier tiene que «trabajar duro» para $w=1$, para reproducir una función que no se anula en $x=1$ como suma de funciones seno, cada una de las cuales sí se anula en $x=1$. Esta dificultad se refleja en las oscilaciones cerca de $x=1$ para cualquier número razonable de términos en la serie de Fourier.

### 6.2.4 Pulsar una cuerda

*(Referencia a los programas interactivos 6-4 y 6-5 del disco de programas del curso original.)*

Usemos ahora estas matemáticas para resolver un problema de física. Resolveremos el problema de valores iniciales para la cuerda con extremo fijo, para una forma inicial concreta. El problema de valores iniciales aquí es casi exactamente igual al discutido en el capítulo 3, (3.98)-(3.100), para un sistema con un número finito de grados de libertad. La única diferencia es que ahora, como el número de grados de libertad es infinito, la suma sobre modos llega hasta el infinito. No debería preocuparse por el hecho de que el número de modos sea infinito: lo que ese «infinito» realmente significa es «más grande que cualquier número que nos vaya a importar». En la práctica, como vimos en los ejemplos anteriores, los modos superiores eventualmente no marcan mucha diferencia; están asociados a rasgos cada vez más pequeños de la forma. Cuando decimos que el sistema es continuo y que tiene un número infinito de grados de libertad, en realidad estamos suponiendo que los rasgos más pequeños que nos importan en las ondas siguen siendo mucho mayores que la distancia entre las partes del sistema, de modo que podemos truncar nuestra serie de Fourier muy por debajo del límite y aun así tener una buena descripción aproximada del movimiento.

Supongamos que pulsamos la cuerda. Concretamente, supongamos que la cuerda tiene densidad de masa lineal $\rho_L$, tensión $T$, y extremos fijos en $x=0$ y $\ell$. Supongamos además que en $t=0$ la cuerda está en reposo, pero desplazada de su posición de equilibrio hacia la forma $\psi(x)$ dada por (6.19). Si la cuerda se suelta entonces en $t=0$, podemos encontrar el movimiento posterior sumando sobre todos los modos normales con coeficientes fijos multiplicados por $\cos\omega_nt$ y/o $\sin\omega_nt$, donde $\omega_n$ es la frecuencia del modo $\sin(n\pi x/\ell)$, con $k=n\pi/\ell$ (la frecuencia viene dada por (6.5)):

$$\omega_n = \sqrt{\frac{T}{\rho_L}}\,k_n = \sqrt{\frac{T}{\rho_L}}\,\frac{n\pi}{\ell}\,. \qquad \text{(6.22)}$$

En este caso, solo aparecen los términos en $\cos\omega_nt$, porque la velocidad es cero en $t=0$. Así, podemos escribir

$$\psi(x,t) = \sum_{n=1}^{\infty}c_n\sin\frac{n\pi x}{\ell}\cos\omega_nt\,. \qquad \text{(6.23)}$$

Esto satisface las condiciones de contorno en $t=0$, en virtud de la serie de Fourier, (6.8). La desventaja de (6.23) es que nos queda una suma infinita. Para la relación de dispersión simple, (6.5), hay otras formas de resolver este problema, que discutiremos más adelante cuando estudiemos las ondas viajeras. Sin embargo, la ventaja de la solución (6.23) es que no depende de la relación de dispersión.

Podemos resolver el problema aproximadamente usando (6.23), sumando solo los primeros términos de la serie. El ordenador puede hacer esto rápidamente. En el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-6-4" rel="noopener" target="_blank" title="Animación original de Howard Georgi">6-4</a> se muestran los primeros veinte términos de la serie, para $w=1/2$ (y con la relación de dispersión todavía dada por (6.5)). El resultado es sorprendentemente simple; ¡compruébelo! El programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-6-5" rel="noopener" target="_blank" title="Animación original de Howard Georgi">6-5</a> sigue la misma idea, pero le permite variar $w$ y el número de términos de la serie de Fourier. Pruebe con $w=0.75$ y compare con las figuras 6.3-6.5.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Tomar el límite de un sistema discreto invariante bajo traslación espacial cuando la distancia entre las partes tiende a cero, interpretar la física del sistema continuo resultante, y encontrar su relación de dispersión;

2.  Usar la serie de Fourier para plantear y resolver el problema de valores iniciales de una cuerda masiva con diversas condiciones de contorno.

## Problemas

**6.1.** Considere la cuerda continua de (6.7)-(6.10) como el límite continuo de una cuerda con cuentas de $W$ cuentas, cuando $W\to\infty$. Escriba el análogo de (6.8) y (6.10) para $W$ finito. Demuestre que el límite cuando $W\to\infty$ da (6.10). Pista: esto es un ejercicio sobre la definición de una integral como límite de una suma. Pero para hacer la primera parte, necesitará usar coordenadas normales, o demostrar la identidad

$$\sum_{k=1}^{W}\sin\frac{nk\pi}{W+1}\sin\frac{n'k\pi}{W+1} = \begin{cases} b & \text{si } n=n'\neq0\\ 0 & \text{si } n\neq n' \text{ y } n,n'>0 \end{cases}$$

para una constante $b$, y encuentre $b$.

**6.2.** Haga las integrales de (6.20). Pista: use integración por partes y esté atento a cancelaciones milagrosas.

**6.3.** Encuentre los modos normales de la cuerda con dos extremos libres, mostrada en la figura 6.7.

![Figura 6.7](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh6_ES/fig6.7.png)

Figura 6.7: cuerda continua con ambos extremos, en $x=0$ y $x=\ell$, unidos a anillos sin masa que deslizan libremente sobre varillas sin fricción perpendiculares a la cuerda.

**6.4.** Diversión con series de Fourier y fractales

En este problema explorará la serie de Fourier de un conjunto interesante de funciones. Considere una función de la siguiente forma, definida en el intervalo $[0,1]$:

$$f(t) = \sum_{j=0}^{\infty}h^j\,g(\text{frac}(2^jt))\,.$$

donde

$$g(t) = \begin{cases} 1 & \text{para } 0\le t\le w\\ 0 & \text{para } w<t<1-w\\ 1 & \text{para } 1-w\le t\le1 \end{cases}$$

y $\text{frac}(x)$ denota la parte fraccionaria, es decir, $\text{frac}(4.39)=0.39$. Así, $f(t)$ depende de los dos parámetros $h$ y $w$, donde $0<h<1$ y $0<w<1/2$. Por ejemplo, para $h=1/2$ y $w=1/4$, el término $h^0$ se muestra en la figura 6.8.

![Figura 6.8](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh6_ES/fig6.8.png)

Figura 6.8: el término $h^0$ de $f(t)$ para $h=1/2$, $w=1/4$ — una onda cuadrada de altura 2 con “mesetas” de anchura $w$ en cada extremo del intervalo $[0,1]$, unidas por rampas lineales.

Si añadimos el término $h^1$ obtenemos la figura 6.9, y añadiendo el término $h^2$ obtenemos la figura 6.10, y así sucesivamente.

![Figura 6.9](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh6_ES/fig6.9.png)

Figura 6.9 y 6.10: sumas parciales de $f(t)$ incluyendo los términos $h^0+h^1$ y $h^0+h^1+h^2$ respectivamente, mostrando una estructura cada vez más fina y autosimilar, típica de un fractal.

El resultado final es una función muy accidentada, llamada «fractal». No se puede calcular esta función exactamente, pero se pueden incluir suficientes términos para alcanzar cualquier precisión deseada. Como la función es simétrica respecto a $t=1/2$, en realidad solo es necesario graficarla de 0 a 1/2. También, debido a la simetría, puede expresarse mediante una serie de Fourier de cosenos,

$$f(t) = \sum_{k=0}^{\infty}b_k\cos2\pi kt\,.$$

Demuestre que los coeficientes de Fourier vienen dados por

$$b_k = \frac{2}{\pi k}\sum_{j=0}^{\xi(k)}(2h)^j\sin(2\pi kw/2^j)$$

para $k\neq0$, y

$$b_0 = \frac{2w}{1-h}$$

donde la función $\xi(k)$ es el número de veces que el 2 aparece como factor de $k$. Así, $\xi(0)=\xi(1)=\xi(3)=0$, $\xi(2)=1$, $\xi(4)=2$, etc.

Escriba un programa que muestre e imprima el fractal para cierto conjunto de parámetros $h$ y $w$. Muestre también la serie de Fourier truncada,

$$f_m(t) = \sum_{k=0}^{m-1}b_k\cos2\pi kt$$

con $m$ términos, para $m=5$, 10 y 20 (o más, si dispone de un ordenador rápido).

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.
