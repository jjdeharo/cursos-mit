# Capítulo 10: Señales y análisis de Fourier

Las ondas viajeras de frecuencia definida transportan energía, pero no información. Sencillamente están ahí, siempre han estado y siempre estarán. Para enviar información hay que enviar una señal no armónica.

## Vídeos de esta clase (YouTube)

- [Clase 14: Transformada de Fourier, radio AM](https://www.youtube.com/watch?v=VGAlyJ7e0IQ)
- [Clase 15: Principio de incertidumbre, ondas en 2D](https://www.youtube.com/watch?v=In0E5_JrPpo)

## Resumen previo

En este capítulo veremos cómo funciona esto en el contexto de un problema de oscilación forzada. Por el camino encontraremos una sutileza en la noción de la velocidad con la que se mueve una onda viajera: la velocidad de fase puede no coincidir con la velocidad de propagación de la señal.

1.  Empezamos estudiando la propagación de un pulso transversal en una cuerda tensada. Resolvemos el problema de dos maneras: con un truco que funciona en este caso especial, y con la técnica más potente de la transformación de Fourier. Introducimos el concepto de «velocidad de grupo», la velocidad a la que realmente pueden enviarse señales en un sistema real.

2.  Discutimos, primero con un ejemplo y después en general, el contrapunto entre una función y su transformada de Fourier. Establecemos la conexión con los conceptos físicos de ancho de banda y fidelidad en la transmisión de señales, y con la relación de incertidumbre de Heisenberg en mecánica cuántica.

3.  Desarrollamos con cierto detalle un ejemplo de dispersión de un paquete de ondas.

4.  Discutimos con más detalle la relación de dispersión de las ondas electromagnéticas y exploramos la cuestión de si la luz viaja realmente a la velocidad de la luz.

## 10.1 Señales en oscilación forzada

### 10.1.1 Un pulso en una cuerda

Empezamos con el siguiente problema ilustrativo: las oscilaciones transversales de una cuerda semiinfinita tensada de $x = 0$ a $\infty$, forzada en $x = 0$ con una señal transversal arbitraria $f(t)$, y con la condición de contorno en el infinito de que no hay ondas viajeras entrantes. Este sistema sencillo se muestra en la figura 10.1.

![Figura 10.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.1.png)

Figura 10.1: una cuerda semiinfinita.

Hay una manera elegante de obtener la respuesta a este problema, que solo funciona para un sistema con la relación de dispersión sencilla

$$\omega^2 = v^2 k^2.\qquad\text{(10.1)}$$

El truco consiste en notar que la relación de dispersión (10.1) implica que el sistema satisface la ecuación de ondas, (6.4), o sea

$$\frac{\partial^2}{\partial t^2}\psi(x, t) = v^2\frac{\partial^2}{\partial x^2}\psi(x, t).\qquad\text{(10.2)}$$

Es un hecho matemático (discutiremos su física más abajo) que la solución general de la ecuación de ondas unidimensional, (10.2), es una suma de ondas que se mueven hacia la derecha y hacia la izquierda con formas arbitrarias,

$$\psi(x, t) = g(x - vt) + h(x + vt),\qquad\text{(10.3)}$$

donde $g$ y $h$ son funciones arbitrarias. Puede comprobar, usando la regla de la cadena, que (10.3) satisface (10.2):

$$\frac{\partial^2}{\partial t^2}\left(g(x - vt) + h(x + vt)\right) = v^2\left(g''(x - vt) + h''(x + vt)\right) = v^2\frac{\partial^2}{\partial x^2}\left(g(x - vt) + h(x + vt)\right).$$

Dado este hecho matemático, podemos hallar las funciones $g$ y $h$ que resuelven nuestro problema concreto imponiendo las condiciones de contorno. La condición de contorno en el infinito implica

$$h = 0,$$

porque la función $h$ describe una onda que se mueve en la dirección $-x$. La condición de contorno en $x = 0$ implica

$$g(-vt) = f(t),$$

lo que da

$$\psi(x, t) = f(t - x/v).\qquad\text{(10.7)}$$

Esto describe la señal $f(t)$ propagándose por la cuerda a la velocidad de fase $v$ sin cambio de forma.

Para la función sencilla

$$f(t) = \begin{cases} 1 - |t| & \text{para } |t| \leq 1 \\ 0 & \text{para } |t| > 1 \end{cases}\qquad\text{(10.8)}$$

la forma de la cuerda en una sucesión de instantes se muestra en la figura 10.2 y está animada en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-10-1" rel="noopener" target="_blank" title="Animación original de Howard Georgi">10-1</a>.

![Figura 10.2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.2.png)

Figura 10.2: un pulso triangular propagándose por una cuerda tensada.

### 10.1.2 Integrales de Fourier

Pensemos en este problema de una manera más física. Por el camino entenderemos la física de la solución general, (10.3). Puede parecer extraño decir esto en una sección titulada «Integrales de Fourier». Sin embargo, veremos que las matemáticas de las integrales de Fourier tienen una interpretación física directa y sencilla.

La idea es usar la linealidad de forma astuta para resolver este problema. Podemos descomponer $f(t)$ en sus frecuencias angulares componentes. Ya sabemos resolver el problema de la oscilación forzada para cada frecuencia angular. Después podemos tomar las soluciones individuales y volver a sumarlas para reconstruir la solución del problema completo. La ventaja de este procedimiento es que funciona para cualquier relación de dispersión, no solo para (10.1).

Como puede haber una distribución continua de frecuencias en una señal arbitraria, no podemos escribir $f(t)$ simplemente como una suma sobre componentes: necesitamos una integral de Fourier,

$$f(t) = \int_{-\infty}^{\infty} d\omega\, C(\omega)\,e^{-i\omega t}.\qquad\text{(10.9)}$$

La física de (10.9) es simplemente la linealidad y la invariancia bajo traslación temporal. Sabemos que podemos elegir los modos normales del sistema libre con una dependencia temporal exponencial irreducible, gracias a la invariancia bajo traslación temporal. Puesto que los modos normales describen todos los movimientos posibles del sistema, sabemos que, tomando una combinación lineal adecuada de modos normales, podemos encontrar una solución en la que el movimiento del extremo del sistema esté descrito por la función $f(t)$. La única sutileza de (10.9) es que hemos supuesto que todos los valores de $\omega$ que aparecen en la integral son reales. Esto es apropiado porque una parte imaginaria no nula de $\omega$ en $e^{-i\omega t}$ describe una función que va exponencialmente a infinito cuando $t \to \pm\infty$. Físicamente, esas cosas nunca nos interesan. De hecho, lo que realmente nos interesa son funciones que van a cero cuando $t \to \pm\infty$, y esas quedan bien descritas por la integral sobre $\omega$ real, (10.9).

Nótese que si $f(t)$ es real en (10.9), entonces

$$f(t)^* = \int d\omega\, C(\omega)^*\,e^{i\omega t} = \int d\omega\, C(-\omega)^*\,e^{-i\omega t},$$

y por tanto

$$C(-\omega)^* = C(\omega).\qquad\text{(10.12)}$$

En realidad es más fácil trabajar con la integral de Fourier compleja, (10.9), con la dependencia temporal exponencial compleja irreducible, que con desarrollos reales en términos de $\cos\omega t$ y $\sin\omega t$. Pero también puede encontrar las formas reales en otros libros. Siempre se puede traducir de (10.9) usando la identidad de Euler

$$e^{i\theta} = \cos\theta + i\sin\theta.$$

Para cada valor de $\omega$ podemos escribir la solución del problema de oscilación forzada incorporando la condición de contorno en $\infty$. Cada componente de frecuencia de la fuerza produce una onda que viaja en la dirección $+x$:

$$e^{-i\omega t} \to e^{-i\omega t + ikx}.\qquad\text{(10.13)}$$

Entonces podemos usar la linealidad para construir la solución sumando las ondas viajeras individuales de (10.13) con los coeficientes $C(\omega)$ de (10.9). Así,

$$\psi(x, t) = \int d\omega\, C(\omega)\,e^{-i\omega t + ikx},\qquad\text{(10.14)}$$

donde $\omega$ y $k$ están relacionados por la relación de dispersión.

La ecuación (10.14) es cierta con bastante generalidad para cualquier sistema unidimensional y cualquier relación de dispersión, pero el resultado es particularmente sencillo para un sistema no dispersivo, como la cuerda continua con una relación de dispersión de la forma (10.1). Podemos usar (10.1) en (10.14) sustituyendo

$$k = \omega/v.\qquad\text{(10.15)}$$

Nótese que, mientras que $k^2$ queda determinado por la relación de dispersión, el signo de $k$, para un $\omega$ dado, lo determina la condición de contorno en el infinito. $k$ y $\omega$ deben tener el mismo signo, como en (10.15), para describir una onda que viaja en la dirección $+x$. Poniendo (10.15) en (10.14) se obtiene

$$\psi(x, t) = \int d\omega\, C(\omega)\,e^{-i\omega t + i\omega x/v} = \int d\omega\, C(\omega)\,e^{-i\omega(t - x/v)}.$$

Comparando esto con (10.9) se obtiene (10.7).

Intentemos entender en palabras lo que está ocurriendo. La integral de Fourier, (10.9), expresa la señal como una combinación lineal de ondas viajeras armónicas. La relación (10.15), que se sigue de la relación de dispersión (10.1) y de la condición de contorno en $\infty$, implica que cada una de las infinitas ondas viajeras armónicas se mueve con la misma velocidad de fase. Por tanto, las ondas se mantienen exactamente en la misma relación unas con otras conforme se mueven, y la señal nunca se distorsiona: simplemente se desplaza con las ondas.

La señal no armónica se llama «paquete de ondas». Como hemos visto, puede descomponerse en ondas armónicas por medio de la integral de Fourier, (10.9).

## 10.2 Medios dispersivos y velocidad de grupo

Para cualquier otra relación de dispersión, la señal cambia de forma al propagarse, porque las distintas componentes armónicas viajan a velocidades diferentes. Con el tiempo, las distintas partes de la señal se desfasan y la señal se dispersa. Por eso a un medio así se le llama «dispersivo». Este es el origen del nombre «relación de dispersión».

### 10.2.1 Velocidad de grupo

Si es astuto, puede enviar señales en un medio dispersivo. El truco consiste en enviar la señal no directamente como la función $f(t)$, sino como una modulación de una señal armónica, de la forma

$$f(t) = f_s(t)\cos\omega_0 t,\qquad\text{(10.17)}$$

donde $f_s(t)$ es la señal. Muy a menudo querrá hacer esto de todos modos, porque puede que las frecuencias importantes de su señal no coincidan con las frecuencias de las ondas con las que quiere enviarla. Un ejemplo es la transmisión de radio AM, en la que la señal procede del sonido, con una frecuencia típica de unos cientos de ciclos por segundo (Hz), pero se transporta como una modulación de la amplitud de una onda de radio electromagnética, con una frecuencia de unos millones de ciclos por segundo.[1]

Puede hacerse una idea de lo que va a ocurrir en este caso considerando la suma de dos ondas viajeras con frecuencias y números de onda distintos,

$$\cos(k_+x - \omega_+t) + \cos(k_-x - \omega_-t)\qquad\text{(10.18)}$$

donde

$$k_\pm = k_0 \pm k_s, \qquad \omega_\pm = \omega_0 \pm \omega_s,\qquad\text{(10.19)}$$

para

$$k_s \ll k_0, \qquad \omega_s \ll \omega_0.\qquad\text{(10.20)}$$

La suma puede escribirse como un producto de cosenos:

$$2\cos(k_sx - \omega_st)\cdot\cos(k_0x - \omega_0t).\qquad\text{(10.21)}$$

Debido a (10.20), el primer factor varía lentamente en $x$ y $t$ comparado con el segundo. El resultado puede pensarse como una onda armónica de frecuencia $\omega_0$ con una amplitud que varía lentamente, proporcional al primer factor. La dependencia espacial de (10.21) se muestra en la figura 10.3.

![Figura 10.3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.3.png)

Figura 10.3: la función (10.21) para $t = 0$ y $k_0/k_s = 10$.

Debe pensar en el primer factor de (10.21) como la señal. El segundo factor se llama «onda portadora». Entonces (10.21) describe una señal que se mueve con velocidad

$$v_s = \frac{\omega_s}{k_s}\qquad\text{(10.22)}$$

mientras que las ondas más pequeñas asociadas al segundo factor se mueven con velocidad

$$v_0 = \frac{\omega_0}{k_0}.\qquad\text{(10.23)}$$

Estas dos velocidades no serán, en general, la misma. Si se satisface (10.20), entonces (como mostraremos con más detalle abajo) $v_0$ será aproximadamente la velocidad de fase. En el límite en que $k_+ - k_- = 2k_s$ se hace muy pequeño, (10.22) se convierte en una derivada:

$$v_s = \left.\frac{\partial\omega}{\partial k}\right|_{k = k_0}.\qquad\text{(10.24)}$$

A esto se le llama «velocidad de grupo». Mide la velocidad a la que puede enviarse realmente la señal.

La dependencia temporal de (10.21) está animada en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-10-2" rel="noopener" target="_blank" title="Animación original de Howard Georgi">10-2</a>. Fíjese en cómo las ondas portadoras se desplazan a través de la señal. En esta animación, la velocidad de grupo es menor que la velocidad de fase, así que las ondas portadoras aparecen en la parte trasera de cada pulso de la señal y avanzan hacia el frente.

Veamos cómo funciona esto en general para señales $f(t)$ interesantes. Supongamos que, para cierto rango de frecuencias cercanas a una frecuencia $\omega_0$, la relación de dispersión varía lentamente. Entonces podemos tomarla como aproximadamente lineal desarrollando $\omega(k)$ en serie de Taylor alrededor de $k_0$ y quedándonos solo con los dos primeros términos. Es decir,

$$\omega = \omega(k) = \omega_0 + (k - k_0)\left.\frac{\partial\omega}{\partial k}\right|_{k = k_0}, \qquad \omega_0 \equiv \omega(k_0),\qquad\text{(10.25)}$$

y los términos de orden superior son despreciables para un rango de frecuencias

$$\omega_0 - \Delta\omega < \omega < \omega_0 + \Delta\omega,\qquad\text{(10.26)}$$

donde $\Delta\omega$ es una constante que depende de $\omega_0$ y de los detalles de los términos de orden superior. Entonces puede enviar una señal de la forma

$$f(t)\cdot e^{-i\omega_0 t}\qquad\text{(10.28)}$$

(una forma compleja de (10.17)), donde $f(t)$ satisface (10.9) con

$$C(\omega) \approx 0 \quad \text{para } |\omega - \omega_0| > \Delta\omega.$$

Esto describe una señal que tiene una onda portadora de frecuencia $\omega_0$, modulada por la parte interesante de la señal, $f(t)$, que actúa como una amplitud variable en el tiempo para la portadora $e^{-i\omega_0 t}$. La estrategia de enviar una señal como una amplitud variable sobre una onda portadora se llama modulación de amplitud.

Normalmente, los términos de orden superior de (10.25) solo son despreciables si $\Delta\omega \ll \omega_0$. Si los despreciamos, podemos escribir (10.25) como

$$\omega = vk + a, \qquad k = \omega/v + b,\qquad\text{(10.29)}$$

donde $a$ y $b$ son constantes que podemos determinar a partir de (10.25),

$$a = \omega_0 - vk_0, \qquad b = k_0 - \omega_0/v,\qquad\text{(10.30)}$$

y $v$ es la velocidad de grupo

$$v = \left.\frac{\partial\omega}{\partial k}\right|_{k = k_0}.\qquad\text{(10.32)}$$

Para la señal (10.28),

$$f(t)\,e^{-i\omega_0 t} = \int d\omega\, C(\omega)\,e^{-i(\omega + \omega_0)t} = \int d\omega\, C(\omega - \omega_0)\,e^{-i\omega t}.$$

Así, (10.14) queda

$$\psi(x, t) = \int d\omega\, C(\omega - \omega_0)\,e^{-i\omega t}e^{ikx},$$

pero entonces (10.29) da

$$\begin{aligned}
\psi(x, t) &= \int d\omega\, C(\omega - \omega_0)\,e^{-i\omega t + i(\omega/v + b)x} \\
&= \int d\omega\, C(\omega - \omega_0)\,e^{-i\omega(t - x/v) + ibx} \\
&= \int d\omega\, C(\omega)\,e^{-i(\omega + \omega_0)(t - x/v) + ibx} \\
&= f(t - x/v)\,e^{-i\omega_0(t - x/v) + ibx}.
\end{aligned}\qquad\text{(10.35)}$$

La modulación $f(t)$ viaja sin cambio de forma a la velocidad de grupo $v$ dada por (10.32), mientras podamos ignorar el término de orden superior de la relación de dispersión. La velocidad de fase

$$v_\phi = \frac{\omega}{k}\qquad\text{(10.36)}$$

no tiene nada que ver con la transmisión de información, pero obsérvese que, debido al $e^{ibx}$ adicional de (10.35), la onda portadora viaja a la velocidad de fase.

Puede ver la diferencia entre velocidad de fase y velocidad de grupo en su piscina o su bañera creando un paquete de ondas formado por varias ondas más cortas.

## 10.3 Ancho de banda, fidelidad e incertidumbre

La relación (10.9) puede invertirse para dar $C(\omega)$ en términos de $f(t)$ como sigue:

$$C(\omega) = \frac{1}{2\pi}\int_{-\infty}^{\infty} dt\, f(t)\,e^{i\omega t}.\qquad\text{(10.37)}$$

Esta es la «transformada de Fourier inversa». Es muy importante, porque nos permite ir y venir entre la señal y la distribución de frecuencias que contiene. Obtendremos este resultado de dos maneras: primero, con un argumento elegante que volveremos a usar y explicaremos con más detalle en el capítulo 13; después, volviendo a la serie de Fourier discutida en el capítulo 6 para ondas en una cuerda finita, y tomando el límite en que la longitud de la cuerda tiende a infinito.

El argumento elegante es este. Es muy razonable que la integral de (10.37) sea proporcional a $C(\omega)$, porque si insertamos (10.9) y reordenamos el orden de integración obtenemos

$$\int d\omega'\, C(\omega')\int dt\, e^{i(\omega - \omega')t}.$$

La integral en $t$ promedia a cero salvo que $\omega = \omega'$. Así, la integral en $\omega'$ es simplemente proporcional a $C(\omega)$ multiplicada por un factor constante. El factor $1/2\pi$ puede obtenerse haciendo algunas integrales explícitamente. Por ejemplo, si

$$f(t) = e^{-\Gamma|t|},\qquad\text{(10.39)}$$

para $\Gamma > 0$, entonces, como mostraremos explícitamente en (10.49)-(10.56), (10.37) da

$$2\pi C(\omega) = \frac{2\Gamma}{\Gamma^2 + \omega^2},\qquad\text{(10.40)}$$

que a su vez puede llevarse de vuelta a (10.9) para dar (10.39). Para $t = 0$, la integral puede hacerse mediante la sustitución trigonométrica $\omega \to \Gamma\tan\theta$:

$$1 = f(0) = \int d\omega\, C(\omega)\,e^{-i\omega\cdot 0} = \frac{1}{\pi}\int_{-\infty}^{\infty} d\omega\,\frac{\Gamma}{\Gamma^2 + \omega^2} = \frac{1}{\pi}\int_{-\pi/2}^{\pi/2} d\theta = 1.\qquad\text{(10.41)}$$

Para obtener la transformada de Fourier inversa, (10.37), como límite de una serie de Fourier, conviene usar una condición de contorno ligeramente distinta de las que discutimos en el capítulo 6 (extremos fijos y extremos libres). En su lugar, consideremos una cuerda tensada de $x = -\pi\ell$ a $x = \pi\ell$, en la que suponemos que el desplazamiento de la cuerda respecto del equilibrio en $x = \pi\ell$ es el mismo que el desplazamiento en $x = -\pi\ell$:[2]

$$\psi(-\pi\ell, t) = \psi(\pi\ell, t).\qquad\text{(10.42)}$$

El requisito (10.42) se llama «condiciones de contorno periódicas», porque implica que la función $\psi$ que describe el desplazamiento de la cuerda es periódica en $x$ con periodo $2\pi\ell$. Los modos normales del sistema infinito que satisfacen (10.42) son

$$e^{inx/\ell},\qquad\text{(10.43)}$$

para $n$ entero, porque cambiar $x$ en $2\pi\ell$ en (10.43) solo cambia la fase de la exponencial en $2\pi$. Así, si $\psi(x)$ es una función arbitraria que satisface $\psi(-\pi\ell) = \psi(\pi\ell)$, deberíamos poder desarrollarla en los modos normales de (10.43),

$$\psi(x) = \sum_{n = -\infty}^{\infty} c_n\,e^{-inx/\ell}.\qquad\text{(10.44)}$$

Análogamente, para una función $f(t)$ que satisfaga $f(-\pi T) = f(\pi T)$ para algún tiempo $T$ grande, esperamos poder desarrollarla como sigue:

$$f(t) = \sum_{n = -\infty}^{\infty} c_n\,e^{-int/T},\qquad\text{(10.45)}$$

donde hemos cambiado el signo del exponente para concordar con (10.9). Mostraremos que, cuando $T \to \infty$, esto se vuelve equivalente a (10.9).

La ecuación (10.44) es el análogo de (6.8) para la condición de contorno (10.42). La suma va de $-\infty$ a $\infty$ en vez de de $0$ a $\infty$ porque los modos de (10.43) son distintos para $n$ y $-n$. Para esta serie de Fourier, la inversa es

$$c_m = \frac{1}{2\pi T}\int_{-\pi T}^{\pi T} dt\, e^{imt/T} f(t),\qquad\text{(10.46)}$$

donde hemos usado la identidad

$$\frac{1}{2\pi T}\int_{-\pi T}^{\pi T} dt\, e^{imt/T}e^{-int/T} = \begin{cases} 1 & \text{para } m = n, \\ 0 & \text{para } m \neq n. \end{cases}\qquad\text{(10.47)}$$

Supongamos ahora que $f(t)$ tiende a 0 para $|t|$ grande (nótese que esto es coherente con la condición de contorno periódica (10.42)) lo bastante deprisa como para que la integral de (10.46) esté bien definida cuando $T \to \infty$ para todo $m$. Entonces, por el factor $1/T$ de (10.46), todos los $c_n$ tienden a cero como $1/T$. Así pues, deberíamos multiplicar $c_n$ por $T$ para obtener algo finito en el límite. Comparando (10.45) con (10.9), vemos que deberíamos tomar $\omega$ igual a $n/T$.

Así, la relación (10.45) es un análogo de la integral de Fourier (10.9), donde la correspondencia es

$$\frac{1}{T} \to d\omega, \qquad \frac{n}{T} \to \omega, \qquad c_n T \to C(\omega).\qquad\text{(10.48)}$$

En el límite $T \to \infty$, la suma se convierte en una integral sobre $\omega$. Multiplicando ambos miembros de (10.46) por $T$ y haciendo la sustitución de (10.48) se obtiene (10.37).

### 10.3.1 Un ejemplo resoluble

Como práctica en el manejo de integrales de funciones complejas, haremos con todo detalle la integración que lleva a (10.40), con todos los pasos:

$$2\pi C(\omega) = \int_{-\infty}^{\infty} dt\, e^{-\Gamma|t|}e^{i\omega t}.\qquad\text{(10.49)}$$

Primero nos deshacemos del valor absoluto:

$$= \int_0^{\infty} dt\, e^{-\Gamma t}e^{i\omega t} + \int_{-\infty}^{0} dt\, e^{\Gamma t}e^{i\omega t}$$

y escribimos la segunda integral como una integral de 0 a $\infty$:

$$= \int_0^{\infty} dt\, e^{-\Gamma t}e^{i\omega t} + \int_0^{\infty} dt\, e^{-\Gamma t}e^{-i\omega t} = \int_0^{\infty} dt\, e^{-\Gamma t}e^{i\omega t} + \text{complejo conjugado},$$

pero sabemos derivar exponenciales, incluso complejas (véase la discusión de (3.108)), así que podemos escribir

$$\frac{\partial}{\partial t}\left(e^{-\Gamma t}e^{i\omega t}\right) = (-\Gamma + i\omega)\,e^{-\Gamma t}e^{i\omega t}.$$

Por tanto,

$$\int_0^{\infty} dt\, e^{-\Gamma t}e^{i\omega t} = \frac{1}{-\Gamma + i\omega}\int_0^{\infty} dt\,\frac{\partial}{\partial t}\left(e^{-\Gamma t}e^{i\omega t}\right)$$

o, usando el teorema fundamental del cálculo integral,

$$= \frac{1}{-\Gamma + i\omega}\left.e^{-\Gamma t}e^{i\omega t}\right|_0^{\infty} = \frac{1}{\Gamma - i\omega}.$$

Esta función de $\omega$ se llama un «polo». Aunque la función se comporta perfectamente bien para $\omega$ real, se dispara para $\omega = -i\Gamma$, que es la posición del polo en el plano complejo. Ahora solo tenemos que añadir el complejo conjugado para obtener

$$2\pi C(\omega) = \frac{1}{\Gamma - i\omega} + \frac{1}{\Gamma + i\omega} = \frac{\Gamma + i\omega}{\Gamma^2 + \omega^2} + \frac{\Gamma - i\omega}{\Gamma^2 + \omega^2} = \frac{2\Gamma}{\Gamma^2 + \omega^2},\qquad\text{(10.56)}$$

que es (10.40). Ya comprobamos, en (10.41), que el factor $1/2\pi$ tiene sentido.

El par (10.39)-(10.40) ilustra un hecho muy general sobre las señales y sus espectros de frecuencia asociados. En la figura 10.4 representamos $f(t)$ para $\Gamma = 0.5$ y $\Gamma = 2$, y en la figura 10.5 representamos $C(\omega)$ para los mismos valores de $\Gamma$. Nótese que, conforme $\Gamma$ aumenta, la señal se vuelve más aguda cerca de $t = 0$, pero el espectro de frecuencias se ensancha. Y, recíprocamente, si $\Gamma$ es pequeño, de modo que $C(\omega)$ está muy concentrada cerca de $\omega = 0$, entonces $f(t)$ está extendida en el tiempo. Este comportamiento complementario es general: para resolver tiempos cortos hace falta un espectro amplio de frecuencias.

![Figura 10.4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.4.png)

Figura 10.4: $f(t) = e^{-\Gamma|t|}$ para $\Gamma = 0.5$ y $\Gamma = 2$.

![Figura 10.5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.5.png)

Figura 10.5: $C(\omega)$ para los mismos valores de $\Gamma$.

### 10.3.2 Generalidades amplias

Podemos enunciar este hecho de forma muy general usando una definición matemática precisa de la anchura de la señal en el tiempo y de la anchura del espectro en frecuencia.

Definiremos la intensidad de la señal como proporcional a $|f(t)|^2$. Entonces podemos definir el valor medio de cualquier función $g(t)$ pesado con la intensidad de la señal como sigue:

$$\langle g(t)\rangle = \frac{\int_{-\infty}^{\infty} dt\, g(t)\,|f(t)|^2}{\int_{-\infty}^{\infty} dt\,|f(t)|^2}.\qquad\text{(10.57)}$$

Esto pesa más $g(t)$ allí donde la señal es más intensa.

Por ejemplo, $\langle t\rangle$ es el tiempo medio, es decir, el valor del tiempo alrededor del cual la señal es más intensa. Entonces

$$\left\langle[t - \langle t\rangle]^2\right\rangle \equiv \Delta t^2\qquad\text{(10.58)}$$

mide la desviación cuadrática media respecto del tiempo medio, así que es una medida de la anchura de la señal.

Podemos definir el valor medio de una función de $\omega$ de manera análoga, integrando sobre la intensidad del espectro de frecuencias. Pero aquí está el truco: gracias a (10.9) y (10.37) podemos ir y venir entre $f(t)$ y $C(\omega)$ a voluntad. Ambas llevan la misma información. Deberíamos poder calcular promedios de funciones de $\omega$ mediante una integral sobre $t$. Y, en efecto, podemos. Considere la integral

$$\int d\omega\,\omega\,C(\omega)\,e^{-i\omega t} = i\frac{\partial}{\partial t}\int d\omega\, C(\omega)\,e^{-i\omega t} = i\frac{\partial}{\partial t}f(t).$$

Esto muestra que multiplicar $C(\omega)$ por $\omega$ equivale a derivar la $f(t)$ correspondiente y multiplicar por $i$.

Así, podemos calcular $\langle\omega\rangle$ como

$$\langle\omega\rangle = \frac{\int_{-\infty}^{\infty} dt\, f(t)^*\,i\frac{\partial}{\partial t}f(t)}{\int_{-\infty}^{\infty} dt\,|f(t)|^2}\qquad\text{(10.60)}$$

y

$$\Delta\omega^2 \equiv \left\langle[\omega - \langle\omega\rangle]^2\right\rangle = \frac{\int_{-\infty}^{\infty} dt\,\left|\left(i\frac{\partial}{\partial t} - \langle\omega\rangle\right)f(t)\right|^2}{\int_{-\infty}^{\infty} dt\,|f(t)|^2}.\qquad\text{(10.61)}$$

$\Delta\omega$ es una medida de la anchura del espectro de frecuencias, o «ancho de banda».

Ahora podemos enunciar y demostrar el resultado siguiente:

$$\Delta t\,\Delta\omega \geq \frac{1}{2}.\qquad\text{(10.62)}$$

Una consecuencia importante de este teorema es que, para un ancho de banda $\Delta\omega$ dado, la anchura temporal de la señal no puede ser arbitrariamente pequeña, sino que está acotada por

$$\Delta t \geq \frac{1}{2\Delta\omega}.\qquad\text{(10.63)}$$

Cuanto menor sea el valor mínimo posible de $\Delta t$ que puede enviar, mayor será la «fidelidad» que puede alcanzar. Un $\Delta t$ menor significa que puede enviar señales con detalles más finos. Pero (10.63) significa que, cuanto menor es el ancho de banda, mayor es el $\Delta t$ mínimo y menor la fidelidad.

Para demostrar (10.62), considere la función[3]

$$\left([t - \langle t\rangle] - i\kappa\left(i\frac{\partial}{\partial t} - \langle\omega\rangle\right)\right)f(t) = r(t),\qquad\text{(10.64)}$$

que depende del parámetro enteramente libre $\kappa$.

Ahora fíjese en el cociente

$$\frac{\int_{-\infty}^{\infty} dt\,|r(t)|^2}{\int_{-\infty}^{\infty} dt\,|f(t)|^2}.\qquad\text{(10.65)}$$

Este cociente es obviamente positivo, porque los integrandos del numerador y del denominador son ambos positivos. Lo que haremos será elegir $\kappa$ de forma astuta, de modo que el hecho de que el cociente sea positivo nos diga algo interesante.

Primero simplificaremos (10.65). En los términos de (10.65) que involucran derivadas de $f(t)^*$, podemos integrar por partes (y desechar los términos de contorno, porque suponemos que $f(t)$ tiende a cero en el infinito) para que las derivadas actúen sobre $f(t)$. Entonces (10.65) queda

$$\Delta t^2 + \kappa^2\Delta\omega^2 + \kappa\,\frac{\int_{-\infty}^{\infty} dt\, f(t)^*\left(t\frac{\partial}{\partial t} - \frac{\partial}{\partial t}t\right)f(t)}{\int_{-\infty}^{\infty} dt\,|f(t)|^2}.\qquad\text{(10.66)}$$

Todos los demás términos se cancelan. Pero

$$\frac{\partial}{\partial t}\left[t f(t)\right] = f(t) + t\frac{\partial}{\partial t}f(t).\qquad\text{(10.67)}$$

Así, el último término de (10.66) es simplemente $-\kappa$, y (10.65) queda

$$\Delta t^2 + \kappa^2\Delta\omega^2 - \kappa.\qquad\text{(10.68)}$$

(10.68) es claramente mayor o igual que cero para cualquier valor de $\kappa$, porque es un cociente de integrales positivas. Para sacar la máxima información del hecho de que es positivo, deberíamos elegir $\kappa$ de modo que (10.65) (= (10.68)) sea lo más pequeño posible. Dicho de otro modo, deberíamos hallar el valor de $\kappa$ que minimiza (10.68). Si derivamos (10.68) e igualamos el resultado a cero, encontramos

$$\kappa_{\min} = \frac{1}{2\Delta\omega^2}.$$

Ahora podemos llevar esto de vuelta a (10.68) para hallar el mínimo, que sigue siendo mayor o igual que cero. Es

$$\Delta t^2 - \frac{1}{4\Delta\omega^2} \geq 0,$$

lo que da inmediatamente (10.62).

La ecuación (10.62) aparece en muchos lugares de la física. Un ejemplo sencillo es el ancho de banda en las transmisiones de radio AM. Una emisora comercial de AM típica emite en una banda de frecuencia de unos 5000 ciclos/s (5 kc) a cada lado de la frecuencia de la portadora. Así,

$$\Delta\omega = 2\pi\Delta\nu \approx 3\times10^4\ \text{s}^{-1},\qquad\text{(10.71)}$$

y no pueden enviar señales que separen tiempos menores que unos pocos $\times10^{-5}$ segundos. Esto es suficiente para la palabra y aceptable para algo de música.

Un ejemplo famoso de (10.62) viene de la mecánica cuántica. Hay una relación completamente análoga entre la anchura espacial de un paquete de ondas, $\Delta x$, y la anchura de los valores de $k$ necesarios para producirlo, $\Delta k$:

$$\Delta x\,\Delta k \geq \frac{1}{2}.\qquad\text{(10.72)}$$

En mecánica cuántica, el momento de una partícula está relacionado con el valor de $k$ de la onda que la describe por

$$p = \hbar k,\qquad\text{(10.73)}$$

donde $\hbar$ es la constante de Planck $h$ dividida por $2\pi$. Así, (10.72) implica

$$\Delta x\,\Delta p \geq \frac{\hbar}{2}.\qquad\text{(10.74)}$$

Este es el enunciado matemático del hecho de que la posición y el momento de una partícula no pueden especificarse simultáneamente. Es la relación de incertidumbre de Heisenberg.

## 10.4 Dispersión de paquetes de ondas

En un experimento real de dispersión no nos interesa una onda armónica entrante que haya existido siempre y vaya a existir siempre. Lo que nos interesa es un paquete de ondas entrante limitado en el tiempo. En esta sección discutimos dos ejemplos de dispersión de paquetes de ondas.

### 10.4.1 Dispersión en una frontera

Empezamos con el más fácil de los dos ejemplos. Considere la dispersión de un paquete de ondas en la frontera entre dos cuerdas semiinfinitas sin dispersión, ambas con tensión $T$ y densidades distintas, $\rho_I$ y $\rho_{II}$, como se muestra en la figura 9.1. Las relaciones de dispersión son:

$$\omega = \begin{cases} v_I k = \sqrt{\dfrac{T}{\rho_I}}\,k & \text{en la región I} \\[8pt] v_{II} k = \sqrt{\dfrac{T}{\rho_{II}}}\,k & \text{en la región II} \end{cases}\qquad\text{(10.75)}$$

donde $v_I$ y $v_{II}$ son las velocidades de fase en las dos regiones.

Concretamente, suponemos que la condición de contorno en $-\infty$ es que hay una onda entrante,

$$f(x - vt)$$

en la región I, pero ninguna onda entrante en la región II, y queremos hallar las ondas salientes: la onda reflejada en la región I y la transmitida en la región II.

Podemos resolver este problema sin descomponer el paquete de ondas en sus componentes armónicas, con un truco análogo al usado al principio de este capítulo para resolver el problema de oscilación forzada de la figura 10.1. La solución más general de las condiciones de contorno en $\pm\infty$ es

$$\psi(x, t) = \begin{cases} f(t - x/v_I) + g(t + x/v_I) & \text{en la región I} \\[4pt] h(t - x/v_{II}) & \text{en la región II} \end{cases}\qquad\text{(10.77)}$$

donde $g$ y $h$ son funciones arbitrarias. Para determinar realmente las ondas reflejada y transmitida debemos imponer las condiciones de contorno en $x = 0$: que el desplazamiento sea continuo (porque la cuerda no se rompe) y que su derivada respecto de $x$ sea continua (porque el nudo que une las dos cuerdas no tiene masa):

$$f(t) + g(t) = h(t),\qquad\text{(10.78)}$$

y

$$\left.\frac{\partial}{\partial x}\left[f(t - x/v_I) + g(t + x/v_I)\right]\right|_{x=0} = \left.\frac{\partial}{\partial x}h(t - x/v_{II})\right|_{x=0}.\qquad\text{(10.79)}$$

Usando la regla de la cadena en (10.79), podemos relacionar las derivadas parciales respecto de $x$ con las derivadas de las funciones,

$$\frac{1}{v_I}\left(-f'(t - x/v_I) + g'(t + x/v_I)\right)\bigg|_{x=0} = -\frac{1}{v_{II}}h'(t - x/v_{II})\bigg|_{x=0},$$

o sea,

$$-f'(t) + g'(t) = -\frac{v_I}{v_{II}}h'(t).\qquad\text{(10.81)}$$

Derivando (10.78), obtenemos

$$f'(t) + g'(t) = h'(t).\qquad\text{(10.82)}$$

Ahora, para cada valor de $t$, (10.81) y (10.82) forman un par de ecuaciones lineales simultáneas que pueden resolverse para $g'(t)$ y $h'(t)$ en términos de $f'(t)$:

$$g'(t) = \frac{1 - v_I/v_{II}}{1 + v_I/v_{II}}f'(t), \qquad h'(t) = \frac{2}{1 + v_I/v_{II}}f'(t).$$

Deshaciendo las derivadas, podemos escribir

$$g(t) = \frac{1 - v_I/v_{II}}{1 + v_I/v_{II}}f(t) + k_1, \qquad h(t) = \frac{2}{1 + v_I/v_{II}}f(t) + k_2,$$

donde $k_1$ y $k_2$ son constantes independientes de $t$. De hecho, debemos tener $k_1 = k_2$ para satisfacer (10.78), y sumar la misma constante en ambas regiones es irrelevante, porque corresponde simplemente a nuestra libertad de desplazar toda la cuerda hacia arriba o hacia abajo en la dirección transversal. Concluimos, por tanto, que

$$g(t) = \frac{1 - v_I/v_{II}}{1 + v_I/v_{II}}f(t), \qquad h(t) = \frac{2}{1 + v_I/v_{II}}f(t)$$

y la solución (10.77) queda

$$\psi(x, t) = \begin{cases} f(t - x/v_I) + \dfrac{1 - v_I/v_{II}}{1 + v_I/v_{II}}f(t + x/v_I) & \text{en la región I,} \\[10pt] \dfrac{2}{1 + v_I/v_{II}}f(t - x/v_{II}) & \text{en la región II.} \end{cases}\qquad\text{(10.86)}$$

El mismo resultado surge si descomponemos el paquete de ondas entrante en sus componentes armónicas. Para cada componente armónica, los coeficientes de reflexión y transmisión son los mismos (de (9.16)):

$$\tau = \frac{2Z_I}{Z_I + Z_{II}} = \frac{2}{1 + v_I/v_{II}}, \qquad R = \frac{Z_I - Z_{II}}{Z_I + Z_{II}} = \frac{1 - v_I/v_{II}}{1 + v_I/v_{II}}.$$

Cuando ahora volvemos a juntar las componentes armónicas para obtener los paquetes de ondas dispersado y transmitido, los coeficientes $\rho$ y $\tau$ aparecen simplemente como constantes globales delante del pulso original, como en (10.86).

Este proceso de dispersión está animado en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-10-3" rel="noopener" target="_blank" title="Animación original de Howard Georgi">10-3</a>. Ahí puede introducir distintos valores de $v_{II}/v_I$ para ver cómo se ven afectadas la reflexión y la transmisión. Nótese que un $v_{II}/v_I$ muy pequeño corresponde a un cociente de impedancias $Z_{II}/Z_I$ grande, lo que significa que la cuerda de la región II apenas se mueve. Entonces obtenemos un pulso reflejado que es simplemente el pulso entrante volcado por debajo de la cuerda. En el límite extremo $v_{II}/v_I \to \infty$, el contorno en $x = 0$ actúa como un extremo fijo. Un $v_{II}/v_I$ muy grande corresponde a un cociente de impedancias $Z_{II}/Z_I$ pequeño, en cuyo caso la cuerda de la región I apenas nota la cuerda de la región II. En el límite $v_{II}/v_I \to 0$, el contorno en $x = 0$ actúa como un extremo libre.

### 10.4.2 Una masa sobre una cuerda

Un ejemplo más interesante de dispersión de paquetes de ondas, que puede resolverse con las matemáticas que ya hemos hecho, es la dispersión de un paquete de ondas entrante con la forma de (10.39) que se encuentra con una masa sobre una cuerda. Aquí la relación de dispersión es trivial, así que el paquete se propaga sin cambio de forma hasta que «choca» con la masa. Pero entonces ocurren cosas interesantes. Esta vez, cuando descomponemos el paquete en sus componentes armónicas, los coeficientes de reflexión y transmisión dependen de $\omega$. Cuando los volvemos a sumar para obtener los paquetes reflejado y transmitido, encontraremos que la forma ha cambiado. Lo desarrollaremos en detalle. El montaje, ya familiar, se muestra en la figura 10.6.

![Figura 10.6](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.6.png)

Figura 10.6: una masa sobre una cuerda.

Para una onda armónica entrante de amplitud $A$, el desplazamiento es

$$\psi(x, t) = A e^{ikx}e^{-i\omega t} + R\,A e^{-ikx}e^{-i\omega t} \quad \text{para } x \leq 0$$

$$\psi(x, t) = \tau\,A e^{ikx}e^{-i\omega t} \quad \text{para } x \geq 0$$

La solución para $R$ y $\tau$ se obtuvo en el capítulo anterior en (9.39)-(9.45). Sin embargo, el parámetro $\epsilon$ de (9.38) depende de $\omega$. Para desenredar la dependencia en frecuencia de los paquetes dispersados, escribimos $R$ y $\tau$ como

$$\tau = \frac{2\Omega}{2\Omega - i\omega}, \qquad R = \frac{i\omega}{2\Omega - i\omega}\qquad\text{(10.90)}$$

donde

$$\Omega = \frac{T}{mv} = \frac{\sqrt{\rho T}}{m}$$

es independiente de $\omega$: depende solo de los parámetros fijos de la cuerda y de la masa. Nótese que, en la notación de (9.38), $\epsilon = \Omega/\omega$.

Supongamos que no tenemos una onda armónica entrante, sino un pulso entrante:

$$\psi_{\text{in}}(x - vt) = A e^{-\Gamma|t - x/v|}.\qquad\text{(10.92)}$$

Ahora la situación es más interesante. Esperamos una solución de la forma

$$\psi(x, t) = \psi_{\text{in}}(x - vt) + \psi_R(x + vt) \quad \text{para } x \leq 0$$

$$\psi(x, t) = \psi_\tau(x - vt) \quad \text{para } x \geq 0$$

donde $\psi_\tau(x - vt)$ es la onda transmitida, que viaja en la dirección $+x$, y $\psi_R(x + vt)$ es la onda reflejada, que viaja en la dirección $-x$. Para obtener las ondas reflejada y transmitida usaremos la superposición y descompondremos $\psi_{\text{in}}$ en componentes armónicas. Podemos entonces usar (10.90) para determinar la dispersión de cada una de las componentes, y después volver a juntar las piezas para obtener la solución. Así pues, empezamos transformando por Fourier $\psi_{\text{in}}$:

$$\psi_{\text{in}}(x, t) = \int d\omega\, e^{-i\omega(t - x/v)}\,C_{\text{in}}(\omega).$$

Sabemos, de nuestra discusión sobre señales, que

$$C_{\text{in}}(\omega) = \frac{1}{2\pi}\int dt\, e^{i\omega t}\,\psi_{\text{in}}(0, t) = \frac{A}{2\pi}\left(\frac{1}{\Gamma - i\omega} + \frac{1}{\Gamma + i\omega}\right).$$

Ahora, para obtener los pulsos reflejado y transmitido, multiplicamos las componentes de $\psi_{\text{in}}$ por las amplitudes de reflexión y transmisión $R$ y $\tau$ para $\psi_{\text{in}}$ unidad:

$$C_\tau(\omega) = \frac{A}{2\pi}\left(\frac{1}{\Gamma - i\omega} + \frac{1}{\Gamma + i\omega}\right)\frac{2\Omega}{2\Omega - i\omega}\qquad\text{(10.98)}$$

$$C_R(\omega) = \frac{A}{2\pi}\left(\frac{1}{\Gamma - i\omega} + \frac{1}{\Gamma + i\omega}\right)\frac{i\omega}{2\Omega - i\omega}\qquad\text{(10.99)}$$

Ahora tenemos que invertir el proceso y hallar las transformadas de Fourier de estas para obtener los pulsos reflejado y transmitido. Esto es directo, porque podemos reescribir (10.98) y (10.99) en términos de polos simples en $\omega$. Después podemos trabajar hacia atrás para obtener las transformadas de Fourier: sabemos de (10.55) que cada término es la transformada de Fourier de una exponencial. Es directo, aunque tedioso, volver a juntarlos. El resultado se reproduce abajo (nótese que hemos combinado los dos términos de cada expresión proporcionales a $1/(2\Omega - i\omega)$):

$$C_\tau(\omega) = A\,\frac{1}{2\pi}\frac{2\Omega}{2\Omega - \Gamma}\left(\frac{1}{\Gamma - i\omega} - \frac{1}{2\Omega - i\omega}\right) + \frac{1}{2\pi}\frac{2\Omega}{2\Omega + \Gamma}\left(\frac{1}{\Gamma + i\omega} + \frac{1}{2\Omega - i\omega}\right);\qquad\text{(10.100)}$$

$$C_R(\omega) = A\,\frac{1}{2\pi}\frac{1}{2\Omega - \Gamma}\left(\frac{\Gamma}{\Gamma - i\omega} - \frac{2\Omega}{2\Omega - i\omega}\right) + \frac{1}{2\pi}\frac{1}{2\Omega + \Gamma}\left(-\frac{\Gamma}{\Gamma + i\omega} + \frac{2\Omega}{2\Omega - i\omega}\right).\qquad\text{(10.101)}$$

Ahora podemos trabajar hacia atrás en (10.100) y (10.101) para obtener las transformadas de Fourier. Sabemos de (10.55) que cada término es la transformada de Fourier de una exponencial. Es directo, aunque tedioso, volver a juntarlos. El resultado se reproduce abajo (nótese que hemos combinado los dos términos de cada expresión proporcionales a $1/(2\Omega - i\omega)$):

$$\begin{aligned}
\psi_\tau(x, t) = {} & \frac{2\Omega}{2\Omega - \Gamma}\,\theta(t - x/v)\,A e^{-\Gamma(t - x/v)}\\
& - \frac{4\Omega\Gamma}{4\Omega^2 - \Gamma^2}\,\theta(t - x/v)\,A e^{-2\Omega(t - x/v)}\\
& + \frac{2\Omega}{2\Omega + \Gamma}\,\theta(-t + x/v)\,A e^{\Gamma(t - x/v)}\qquad\text{(10.102)}
\end{aligned}$$

y

$$\begin{aligned}
\psi_r(x, t) = {} & \frac{2\Gamma}{2\Omega - \Gamma}\,\theta(t + x/v)\,A e^{-\Gamma(t + x/v)}\\
& - \frac{4\Omega\Gamma}{4\Omega^2 - \Gamma^2}\,\theta(t + x/v)\,A e^{-2\Omega(t + x/v)}\\
& - \frac{2\Gamma}{2\Omega + \Gamma}\,\theta(-t - x/v)\,A e^{\Gamma(t + x/v)}\qquad\text{(10.103)}
\end{aligned}$$

donde

$$\theta(t) = \begin{cases} 1 & \text{para } t \geq 0, \\ 0 & \text{para } t < 0. \end{cases}\qquad\text{(10.104)}$$

![Figura 10.7](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.7.png)

Figura 10.7: un paquete de ondas en una cuerda tensada, en $t = -2$.

![Figura 10.8](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.8.png)

Figura 10.8: $t = -1$.

Estas fórmulas no son muy transparentes ni informativas, pero podemos meterlas en un ordenador y mirar el resultado. Representaremos el resultado en el límite $2\Omega \to \Gamma$. Los resultados (10.102) y (10.103) parecen singulares en este límite pero, en realidad, el límite existe y es perfectamente suave.[4] En las figuras 10.7-10.12 mostramos $\psi(x, t)$ para $\Gamma = v = 1$ en unidades arbitrarias, para valores de $t$ desde $-2$ hasta 3.

![Figura 10.9](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.9.png)

Figura 10.9: $t = 0$.

![Figura 10.10](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.10.png)

Figura 10.10: $t = 1$.

![Figura 10.11](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.11.png)

Figura 10.11: $t = 2$.

En $t = -2$ se ve el pulso acercándose a la masa para $t$ negativo. En $t = -1$ empieza a apreciarse el efecto de la masa sobre la cuerda. Para $t = 0$, la cuerda a la izquierda de $x = 0$ se mueve rápidamente hacia abajo. En $t = 1$, el movimiento descendente de la cuerda para $x < 0$ ha continuado y ha empezado a formar el pulso reflejado. Para $t = 2$ se ve cómo las ondas transmitida y reflejada empiezan a separarse. Para $t = 3$ se ve que los pulsos reflejado y transmitido se han separado casi por completo y que la masa ha vuelto casi a su posición de equilibrio. Para $t$ positivo grande, el pulso se ha dividido en una onda reflejada y otra transmitida.

![Figura 10.12](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.12.png)

Figura 10.12: $t = 3$.

Lo realmente interesante ocurre entre $t = 0$ y $t = 1$, así que lo miraremos en una escala temporal más fina en las figuras 10.13-10.16. Para apreciarlo de verdad, debería verlo en movimiento: está animado en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-10-4" rel="noopener" target="_blank" title="Animación original de Howard Georgi">10-4</a>.

![Figura 10.13](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.13.png)

Figura 10.13: $t = 0.2$.

![Figura 10.14](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.14.png)

Figura 10.14: $t = 0.4$.

![Figura 10.15](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.15.png)

Figura 10.15: $t = 0.6$.

![Figura 10.16](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.16.png)

Figura 10.16: $t = 0.8$.

## 10.5 ¿Es $c$ la velocidad de la luz?

Hemos visto que una onda electromagnética en la dirección $z$ que satisface las ecuaciones de Maxwell en el espacio libre tiene la relación de dispersión (8.47), de modo que la luz, al menos en el vacío, viaja a la velocidad de la luz. Pero ¿es correcta la teoría? ¿Cómo comprobamos la relación de dispersión? De hecho, las pruebas más sensibles de las ecuaciones de Maxwell no involucran ondas viajeras: provienen de observaciones de campos magnéticos que se extienden a distancias astrofísicas (¡como la galaxia!). Sin embargo, hay una manera interesante, aunque no muy sensible, de buscar correcciones a (8.47) que involucra directamente la velocidad de la luz. Antes de discutirla, hagamos una breve digresión para hablar con más detalle de los fotones, las partículas de luz que describimos brevemente en el capítulo 8.

La luz es un fenómeno ondulatorio, como hemos visto. De hecho, las propiedades ondulatorias de la luz son evidentes en nuestra experiencia cotidiana. Es menos evidente a partir de esa experiencia, pero igualmente cierto, que la luz también consta de fotones. Esto se hace obvio cuando se trabaja con luz a intensidades muy bajas o a energías muy altas. Que ambas afirmaciones puedan ser ciertas simultáneamente es uno de los (muchos) milagros de la mecánica cuántica.

La mecánica cuántica nos dice que todas las partículas tienen propiedades ondulatorias. Una partícula con momento $p$ y energía $E$ tiene asociadas una frecuencia angular y un número de onda angular relacionados por

$$E = \hbar\omega, \qquad p = \hbar k,\qquad\text{(10.105)}$$

donde $\hbar$ es la constante de Planck dividida por $2\pi$. Esta combinación aparece de forma tan ubicua en mecánica cuántica que tiene su propio símbolo, y los físicos casi siempre usamos $\hbar$ en vez de $h$. La razón es simplemente que $h$ está relacionada con la frecuencia $\nu$, en vez de con la frecuencia angular $\omega$, y hemos visto que $\omega$ es la medida más conveniente para la mayoría de los propósitos. Además, la energía y el momento de la partícula están relacionados así:

$$E^2 = p^2c^2 + m^2c^4, \qquad v = c\,\frac{pc}{E}\qquad\text{(10.106)}$$

donde $m$ es la masa en reposo y $v$ es la velocidad clásica.

Si ponemos (10.105) en (10.106), obtenemos una relación de dispersión para la onda mecanocuántica asociada a la partícula,

$$\omega^2 = c^2k^2 + \omega_0^2, \qquad \omega_0 = \frac{mc^2}{\hbar}.\qquad\text{(10.107)}$$

¡La velocidad clásica es la velocidad de grupo de la onda mecanocuántica!

$$v = \frac{pc^2}{E} = \frac{c^2 k}{\omega} = \frac{\partial\omega}{\partial k}.$$

De hecho, las partículas, en una imagen mecanocuántica, corresponden a paquetes de ondas que se mueven con la velocidad de grupo.

La relación de dispersión mecanocuántica, (10.107), concuerda con (8.47) solo si $m = 0$. Así pues, podemos reformular la pregunta de si (8.47) es correcta preguntando: «¿es realmente nula la masa del fotón?».

Parecería que deberíamos poder comprobar esta idea observando dos fotones de frecuencias distintas emitidos al mismo tiempo desde un objeto lejano y comprobando si llegan al mismo tiempo. Hay un fallo evidente en este plan: si el objeto está tan lejos que no podemos llegar hasta él, ¿cómo sabemos que los dos fotones fueron emitidos al mismo tiempo? De hecho, la astrofísica nos ha proporcionado una manera de sortear esta dificultad: podemos mirar los púlsares. Los púlsares son (presumiblemente) restos de estrellas de neutrones en rotación procedentes de explosiones de supernova, que emiten luz hacia la Tierra a intervalos regulares. Por ejemplo, el púlsar 1937+21 es tan regular que el instante de salida de los fotones puede determinarse con una precisión de unos pocos microsegundos (µs).[5] Además está a unos 16 000 años luz, así que los fotones de mayor frecuencia (los más rápidos) tienen tiempo de sobra para adelantarse. Cuando se hace este experimento, se encuentra un $\omega_0$ no nulo, de unos $1.7\times10^4\ \text{s}^{-1}$, que corresponde a una masa de unos $1.26\times10^{-49}$ g. Puede parecer una masa bastante pequeña, pero de hecho es ridículamente grande para un fotón: por estudios del campo magnético galáctico sospechamos que es menor que $4\times10^{-65}$ g.[6] Así que está ocurriendo alguna otra cosa.

El problema de esta medida como prueba de la relación de dispersión es que ahí fuera hay electrones: electrones libres en el espacio interestelar ($10^{-1}$ a $10^{-2}$ cm$^{-3}$). Esos electrones del espacio se agitarán en el campo $E$; eso producirá una densidad de corriente que afectará a las ecuaciones de Maxwell y eso, a su vez, afectará a la relación de dispersión. Analicemos el efecto de este plasma diluido suponiendo que la densidad de electrones es constante. Entonces (al menos para las ondas de radio de longitud de onda larga que interesan en estos experimentos) todavía podemos usar la invariancia bajo traslación para entender lo que ocurre. Considere una onda plana en la dirección $z$ y suponga que el campo eléctrico de la onda plana está en la dirección $x$. Entonces sigue siendo cierto que, a un $\omega$ dado,

$$E_x(\vec{r}, t) = E_0 e^{i(kz - \omega t)}, \qquad B_y(\vec{r}, t) = B_0 e^{i(kz - \omega t)},\qquad\text{(10.108)}$$

para algún $k$. Para hallar $k$ debemos mirar el efecto de los campos eléctricos sobre los electrones y volver después a las ecuaciones de Maxwell. Los campos son muy pequeños y, para campos pequeños, las velocidades inducidas de los electrones, $v$, son pequeñas. Así, podemos despreciar $B$. Entonces la fuerza sobre un electrón en el punto $(\vec{r}, t)$ es

$$F_x(\vec{r}, t) = e\,E_x(\vec{r}, t) = e\,E_0 e^{i(kz - \omega t)} = m\,a_x(\vec{r}, t).\qquad\text{(10.110)}$$

El desplazamiento del electrón tiene la misma forma:

$$d_x(\vec{r}, t) = d_0 e^{i(kz - \omega t)}$$

lo que implica

$$a_x(\vec{r}, t) = -\omega^2 d_0 e^{i(kz - \omega t)}.\qquad\text{(10.112)}$$

Comparando (10.110) y (10.112) se obtiene

$$d_0 = -\frac{e\,E_0}{m\,\omega^2}.$$

Así, los electrones se desplazan $180°$ desfasados respecto del campo eléctrico y en la misma dirección. Entonces la velocidad del electrón es

$$v_x = \frac{i\,e\,E_0}{m\,\omega}e^{i(kz - \omega t)}.$$

El movimiento de los electrones da lugar a una densidad de corriente:[7]

$$J_x = \frac{i\,e^2 N\,E_0}{m\,\omega}e^{i(kz - \omega t)},$$

donde $N$ es la densidad numérica de electrones.

Poniendo esto en las ecuaciones de Maxwell relevantes, encontramos

$$k\,E_0 = \omega\,B_0, \qquad -k\,B_0 = -\omega\mu_0\varepsilon_0 E_0 + \mu_0\frac{i\,e^2 N E_0}{m\,\omega}\cdot\frac{1}{i},$$

o, usando $c = 1/\sqrt{\mu_0\varepsilon_0}$, (8.47),

$$\frac{k^2}{\omega} = \frac{\omega}{c^2} - \frac{e^2 N}{c^2 m\,\varepsilon_0\,\omega},$$

o, despejando $\omega^2$,

$$\omega^2 = c^2k^2 + \omega_0^2, \qquad \text{con } \omega_0^2 = \frac{e^2 N}{m\,\varepsilon_0}.\qquad\text{(10.118)}$$

La constante $\omega_0$ de (10.118) se llama «frecuencia de plasma». Lo asombroso es que se comporta exactamente igual que una masa del fotón. Para $N \approx 10^{-2}$ cm$^{-3}$, esto es coherente con la observación del púlsar.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Resolver un problema de oscilación forzada para una cuerda tensada con un desplazamiento arbitrario dependiente del tiempo en el extremo;

2.  Descomponer una señal arbitraria en componentes armónicas mediante la transformación de Fourier;

3.  Calcular la velocidad de grupo de un sistema dispersivo;

4.  Comprender las relaciones entre una función y su transformada de Fourier que llevan a la relación entre ancho de banda y fidelidad;

5.  Ser capaz de describir la dispersión de un paquete de ondas;

6.  Comprender el efecto de las cargas libres sobre la relación de dispersión de las ondas electromagnéticas.

## Problemas

**10.1.** ¿Es posible que un medio que soporta ondas electromagnéticas tenga la relación de dispersión $\omega^2 = c^2k^2 - \omega_0^2$ para $\omega_0$ real? ¿Por qué sí o por qué no?

**10.2.** Una cuerda con cuentas tiene las cuentas vecinas separadas una distancia $a$. Si la velocidad de grupo máxima posible para las ondas en la cuerda es $v$, halle $T/m$.

**10.3.** En el próximo capítulo deduciremos la relación de dispersión de las ondas en el agua (o, al menos, en una imagen idealizada del agua). Si el agua es profunda, la relación de dispersión es

$$\omega^2 = gk + \frac{T k^3}{\rho}$$

donde $g$ es la aceleración de la gravedad, 980 en unidades cgs, $T$ es la tensión superficial, 72, y $\rho$ es la densidad, 1.0. Halle la velocidad de grupo y la velocidad de fase en función de la longitud de onda. ¿Cuándo son iguales?

**10.4.** Considere las oscilaciones longitudinales del sistema de bloques y muelles sin masa que se muestra abajo. Cada bloque tiene masa $m$. Cada muelle tiene constante $K$. La separación de equilibrio entre los bloques es $a$. El anillo de la izquierda se mueve adelante y atrás con desplazamiento $B\cos\omega t$. Esto produce una onda viajera en el sistema que se mueve hacia la derecha para $\omega < 2\sqrt{K/m}$. No hay onda viajera moviéndose hacia la izquierda.

La relación de dispersión del sistema es

$$\omega^2 = \frac{4K}{m}\sin^2\frac{ka}{2}.$$

**a.** Suponga que $\omega = \sqrt{K/m}$. Halle la velocidad de fase de las ondas viajeras a esta frecuencia.

**b.** Para $\omega = \sqrt{K/m}$, halle el desplazamiento del primer bloque en el instante $t = \pi/2\omega$. Exprese la respuesta como $B$ multiplicada por un número puro.

**c.** Halle la velocidad de grupo en el límite $\omega \to 2\sqrt{K/m}$.

**d.** Halle el promedio temporal de la potencia suministrada por la fuerza sobre el anillo en el límite $\omega \to 2\sqrt{K/m}$.

**e.** Explique la relación entre las respuestas de los apartados c y d. Puede que sea capaz de hacer este apartado incluso si se ha liado con el álgebra: piense en la física e intente entender qué debe estar ocurriendo.

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*

[1] Véase (10.71), más abajo.

[2] Un ejemplo de sistema físico con este tipo de condición de contorno sería una cuerda tensada alrededor de un cilindro sin fricción de radio $\ell$ y, por tanto, de circunferencia $2\pi\ell$. Entonces (10.42) sería cierta porque $x = -\pi\ell$ describe el mismo punto de la cuerda que $x = \pi\ell$.

[3] Este es un truco tomado de un análisis similar que conduce al principio de incertidumbre de Heisenberg en mecánica cuántica. No se preocupe si no le resulta obvio de dónde sale. Lo importante es el resultado.

[4] La aparente singularidad es similar a una que aparece al aproximarse al amortiguamiento crítico, discutido en (2.12).

[5] Véase G. Barbiellini y G. Cocconi, *Nature* **329** (1987) 21.

[6] Chibisov, *Soviet Physics - Uspekhi*, **19** (1986) 624.

[7] Nótese que el resultado es inversamente proporcional a la masa del electrón. Por eso nos concentramos en los electrones y no en los protones: ¡los protones no se mueven tan deprisa!
