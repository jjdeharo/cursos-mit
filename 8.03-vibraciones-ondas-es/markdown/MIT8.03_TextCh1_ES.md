# Capítulo 1: Oscilación armónica

Los osciladores son los componentes básicos de las ondas. Empezamos analizando el oscilador armónico. Identificaremos los principios generales que hacen que el oscilador armónico sea tan especial e importante. Para aprovechar estos principios, debemos introducir la herramienta matemática de los números complejos. Pero la ventaja de introducir estas matemáticas es que podemos entender la solución del problema del oscilador armónico de una forma nueva. Mostraremos que las propiedades de linealidad e invariancia bajo traslación temporal conducen a soluciones que son funciones exponenciales complejas del tiempo.

## Vídeos de esta clase (YouTube)

- [Clase 1: Oscilaciones periódicas, osciladores armónicos](https://www.youtube.com/watch?v=4ysFC9vd3GE)

## Resumen previo

En este capítulo discutimos la oscilación armónica en sistemas con un único grado de libertad.

1.  Empezamos con un repaso del oscilador armónico simple, señalando que la ecuación de movimiento de un oscilador libre es lineal e invariante bajo traslación temporal;
2.  Discutimos la linealidad con más detalle, argumentando que es la situación genérica para pequeñas oscilaciones en torno a un punto de equilibrio estable;
3.  Discutimos la invariancia bajo traslación temporal del oscilador armónico, y la conexión entre la oscilación armónica y el movimiento circular uniforme;
4.  Introducimos los números complejos y discutimos su aritmética;
5.  Usando números complejos, encontramos soluciones de la ecuación de movimiento del oscilador armónico que se comportan de la forma más simple posible bajo traslaciones temporales. Llamamos a estas soluciones «irreducibles». Mostramos que son en realidad exponenciales complejas.
6.  Discutimos un circuito LC y trazamos una analogía entre él y un sistema de una masa y muelles.
7.  Discutimos las unidades.
8.  Damos un ejemplo simple de oscilador no lineal.

## 1.1 El oscilador armónico

Cuando estudió mecánica, probablemente aprendió sobre el oscilador armónico. Empezaremos nuestro estudio de los fenómenos ondulatorios repasando este sistema físico simple pero importante. Considere un bloque de masa $m$, libre para deslizar sobre un carril de aire sin fricción, pero unido a un muelle ligero que obedece la ley de Hooke, con su otro extremo unido a una pared fija. Una representación esquemática de este sistema físico se muestra en la figura 1.1.

![Figura 1.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.1.png)

Figura 1.1: bloque de masa $m$ sobre un carril de aire horizontal, unido mediante un muelle a una pared fija a su izquierda.

Este sistema tiene un único grado de libertad relevante. En general, el número de grados de libertad de un sistema es el número de coordenadas que deben especificarse para determinar completamente su configuración. En este caso, como el muelle es ligero, podemos suponer que está estirado uniformemente desde la pared fija hasta el bloque. Entonces la única coordenada importante es la posición del bloque.

En esta situación, la gravedad no desempeña ningún papel en el movimiento del bloque. La fuerza gravitatoria queda cancelada por una fuerza vertical del carril de aire. La única fuerza relevante que actúa sobre el bloque proviene del estiramiento o compresión del muelle. Cuando el muelle está relajado, no hay fuerza sobre el bloque y el sistema está en equilibrio. La ley de Hooke nos dice que la fuerza del muelle viene dada por una constante negativa, $-K$, multiplicada por el desplazamiento del bloque respecto a su posición de equilibrio. Así, si la posición del bloque en cierto instante es $x$ y su posición de equilibrio es $x_0$, la fuerza sobre el bloque en ese instante es

$$F = -K(x - x_0)\,. \qquad \text{(1.1)}$$

La constante $K$ se llama «constante del muelle». Tiene unidades de fuerza por unidad de distancia, o $MT^{-2}$ en términos de $M$ (la unidad de masa), $L$ (la unidad de longitud) y $T$ (la unidad de tiempo). Siempre podemos elegir medir la posición $x$ del bloque con nuestro origen en la posición de equilibrio. Si hacemos esto, entonces $x_0 = 0$ en (1.1) y la fuerza sobre el bloque toma la forma más simple

$$F = -Kx\,. \qquad \text{(1.2)}$$

La oscilación armónica resulta de la interacción entre la fuerza de la ley de Hooke y la ley de Newton, $F=ma$. Sea $x(t)$ el desplazamiento del bloque en función del tiempo, $t$. Entonces la ley de Newton implica

$$m\,\frac{d^2}{dt^2}x(t) = -K\,x(t)\,. \qquad \text{(1.3)}$$

Una ecuación de esta forma, que involucra no solo la función $x(t)$ sino también sus derivadas, se llama «ecuación diferencial». La ecuación diferencial (1.3) es la «ecuación de movimiento» del sistema de la figura 1.1. Como el sistema tiene un único grado de libertad, hay una única ecuación de movimiento. En general, debe haber una ecuación de movimiento por cada coordenada independiente necesaria para especificar la configuración del sistema.

La solución más general de la ecuación diferencial de movimiento (1.3) es una suma de una constante por $\cos\omega t$ más una constante por $\sin\omega t$,

$$x(t) = a\cos\omega t + b\sin\omega t\,, \qquad \text{(1.4)}$$

donde

$$\omega \equiv \sqrt{\frac{K}{m}} \qquad \text{(1.5)}$$

es una constante con unidades de $T^{-1}$ llamada «frecuencia angular». La frecuencia angular será una cantidad muy importante en nuestro estudio de los fenómenos ondulatorios. Casi siempre la denotaremos con la letra griega minúscula $\omega$ (omega).

Como la ecuación involucra una segunda derivada temporal pero ninguna derivada de orden superior, la solución más general contiene dos constantes. Esto es justo lo que esperamos de la física, porque podemos obtener una solución distinta para cada valor de la posición y la velocidad del bloque en el instante inicial. Generalmente, pensaremos en determinar la solución en términos de la posición y la velocidad del bloque cuando ponemos en marcha el movimiento, en un instante que convencionalmente tomamos como $t=0$. Por esta razón, el proceso de determinar la solución en términos de la posición y la velocidad en un instante dado se llama «problema de valores iniciales». Los valores de la posición y la velocidad en $t=0$ se llaman condiciones iniciales. Por ejemplo, podemos escribir la solución más general (1.4) en términos de $x(0)$ y $x'(0)$, el desplazamiento y la velocidad del bloque en el instante $t=0$. Poniendo $t=0$ en (1.4) da $a = x(0)$. Derivando y poniendo luego $t=0$ da $b = \omega^{-1}x'(0)$. Así

$$x(t) = x(0)\cos\omega t + \frac{1}{\omega}x'(0)\sin\omega t\,. \qquad \text{(1.6)}$$

Por ejemplo, supongamos que el bloque tiene una masa de 1 kilogramo y que el muelle mide 0.5 metros, con una constante de muelle $K$ de 100 newtons por metro. Para hacerse una idea de lo que significa esta constante, considere colgar el muelle verticalmente (véase el problema 1.1). La fuerza gravitatoria sobre el bloque es

$$mg \approx 9.8\ \text{newtons}\,. \qquad \text{(1.7)}$$

En equilibrio, la fuerza gravitatoria cancela la fuerza del muelle, así que el muelle se estira

$$\frac{mg}{K} \approx 0.098\ \text{metros} = 9.8\ \text{centímetros}\,. \qquad \text{(1.8)}$$

Para esta masa y esta constante de muelle, la frecuencia angular $\omega$ del sistema de la figura 1.1 es

$$\omega = \sqrt{\frac{K}{M}} = \sqrt{\frac{100\ \text{N/m}}{1\ \text{kg}}} = 10\ \frac{1}{\text{s}}\,. \qquad \text{(1.9)}$$

Si, por ejemplo, el bloque se desplaza 0.01 m (1 cm) de su posición de equilibrio y se suelta desde el reposo en $t=0$, la posición en cualquier instante posterior $t$ viene dada (en metros) por

$$x(t) = 0.01 \times \cos 10t\,. \qquad \text{(1.10)}$$

La velocidad (en metros por segundo) es

$$x'(t) = -0.1 \times \sin 10t\,. \qquad \text{(1.11)}$$

El movimiento es periódico, en el sentido de que el sistema oscila —repite el mismo movimiento una y otra vez indefinidamente. Tras un tiempo

$$\tau = \frac{2\pi}{\omega} \approx 0.628\ \text{s} \qquad \text{(1.12)}$$

el sistema vuelve exactamente a donde estaba en $t=0$, con el bloque instantáneamente en reposo con desplazamiento 0.01 metros. El tiempo $\tau$ (letra griega tau) se llama el «periodo» de la oscilación. Sin embargo, la solución (1.6) es más que simplemente periódica: es un movimiento «armónico simple», lo que significa que en el movimiento aparece una única frecuencia.

La frecuencia angular, $\omega$, es la inversa del tiempo requerido para que la fase de la onda cambie en un radián. La «frecuencia», usualmente denotada por la letra griega $\nu$ (nu), es la inversa del tiempo requerido para que la fase cambie un ciclo completo, o $2\pi$ radianes, y así vuelva a su estado original. La frecuencia se mide en hercios, o ciclos por segundo. Así, la frecuencia angular es mayor que la frecuencia por un factor de $2\pi$,

$$\omega\ (\text{en radianes/segundo}) = 2\pi\ (\text{radianes/ciclo}) \cdot \nu\ (\text{ciclos/segundo})\,. \qquad \text{(1.13)}$$

La frecuencia, $\nu$, es la inversa del periodo, $\tau$, de (1.12),

$$\nu = \frac{1}{\tau}\,. \qquad \text{(1.14)}$$

El movimiento armónico simple como (1.6) ocurre en una amplísima variedad de sistemas físicos. La pregunta con la que comenzaremos nuestro estudio de los fenómenos ondulatorios es la siguiente: ¿por qué aparecen soluciones de la forma (1.6) de manera tan ubicua en física? ¿Qué tienen en común los sistemas que oscilan armónicamente? Por supuesto, la respuesta matemática a esta pregunta es que todos estos sistemas tienen ecuaciones de movimiento esencialmente de la misma forma que (1.3). Encontraremos una respuesta más profunda y física que después podremos generalizar a sistemas más complicados. Las características clave que todos estos sistemas comparten con la masa en el muelle son la linealidad y la invariancia bajo traslación temporal de las ecuaciones de movimiento (al menos de forma aproximada). Son estas dos propiedades las que determinan el comportamiento oscilatorio en sistemas que van desde muelles hasta bobinas y condensadores.

Cada una de estas dos propiedades es interesante por sí sola, pero juntas son mucho más poderosas. Determinan casi por completo la forma de las soluciones. Veremos que si el sistema es lineal e invariante bajo traslación temporal, siempre podemos escribir su movimiento como una suma de movimientos simples en los que la dependencia temporal es o bien oscilación armónica o bien decaimiento (o crecimiento) exponencial.

## 1.2 Pequeñas oscilaciones y linealidad

Un sistema con un grado de libertad es lineal si su ecuación de movimiento es una función lineal de la coordenada $x$ que especifica la configuración del sistema. Dicho de otro modo, la ecuación de movimiento debe ser una suma de términos, cada uno de los cuales contiene como máximo una potencia de $x$. La ecuación de movimiento involucra una segunda derivada, pero ninguna derivada de orden superior, así que una ecuación de movimiento lineal tiene la forma general:

$$\alpha\,\frac{d^2}{dt^2}x(t) + \beta\,\frac{d}{dt}x(t) + \gamma\,x(t) = f(t)\,. \qquad \text{(1.15)}$$

Si todos los términos involucran exactamente una potencia de $x$, la ecuación de movimiento es «homogénea». La ecuación (1.15) no es homogénea debido al término del lado derecho. El término «inhomogéneo», $f(t)$, representa una fuerza externa. La ecuación homogénea correspondiente sería:

$$\alpha\,\frac{d^2}{dt^2}x(t) + \beta\,\frac{d}{dt}x(t) + \gamma\,x(t) = 0\,. \qquad \text{(1.16)}$$

En general, $\alpha$, $\beta$ y $\gamma$, así como $f$, podrían ser funciones de $t$. Sin embargo, eso rompería la invariancia bajo traslación temporal que discutiremos con más detalle más abajo y haría el sistema mucho más complicado. Casi siempre supondremos que $\alpha$, $\beta$ y $\gamma$ son constantes. La ecuación de movimiento para la masa sobre un muelle, (1.3), es de esta forma general, pero con $\beta$ y $f$ iguales a cero. Como veremos en el capítulo 2, podemos incluir el efecto de las fuerzas de fricción permitiendo un $\beta$ no nulo, y el efecto de fuerzas externas permitiendo un $f$ no nulo.

La linealidad de la ecuación de movimiento (1.15) implica que si $x_1(t)$ es una solución para la fuerza externa $f_1(t)$,

$$\alpha\,\frac{d^2}{dt^2}x_1(t) + \beta\,\frac{d}{dt}x_1(t) + \gamma\,x_1(t) = f_1(t)\,, \qquad \text{(1.17)}$$

y $x_2(t)$ es una solución para la fuerza externa $f_2(t)$,

$$\alpha\,\frac{d^2}{dt^2}x_2(t) + \beta\,\frac{d}{dt}x_2(t) + \gamma\,x_2(t) = f_2(t)\,, \qquad \text{(1.18)}$$

entonces la suma,

$$x_{12}(t) = A\,x_1(t) + B\,x_2(t)\,, \qquad \text{(1.19)}$$

para constantes $A$ y $B$, es una solución para la fuerza externa $Af_1 + Bf_2$,

$$\alpha\,\frac{d^2}{dt^2}x_{12}(t) + \beta\,\frac{d}{dt}x_{12}(t) + \gamma\,x_{12}(t) = Af_1(t) + Bf_2(t)\,. \qquad \text{(1.20)}$$

La suma $x_{12}(t)$ se llama «combinación lineal» de las dos soluciones $x_1(t)$ y $x_2(t)$. En el caso del movimiento «libre», es decir, sin fuerza externa, si $x_1(t)$ y $x_2(t)$ son soluciones, entonces la suma $Ax_1(t) + Bx_2(t)$ también es una solución.

La solución más general de cualquiera de estas ecuaciones involucra dos constantes que deben fijarse mediante las condiciones iniciales, por ejemplo la posición y velocidad iniciales de la partícula, como en (1.6). Se sigue de (1.20) que siempre podemos escribir la solución más general para cualquier fuerza externa $f(t)$ como una suma de la «solución general» de la ecuación homogénea (1.16) y cualquier solución «particular» de (1.15).

Ningún sistema es exactamente lineal. La «linealidad» nunca es exactamente «cierta». Sin embargo, la idea de linealidad es extremadamente importante, porque es una aproximación útil en un número muy grande de sistemas, por una muy buena razón física. En casi cualquier sistema en el que las propiedades sean funciones suaves de las posiciones de sus partes, los pequeños desplazamientos respecto al equilibrio producen fuerzas restauradoras aproximadamente lineales. La diferencia entre algo que es «cierto» y algo que es una aproximación útil es la diferencia esencial entre las matemáticas y la física. En el mundo real, las preguntas son demasiado interesantes para tener respuestas exactas. Si consigue entender la respuesta dentro de una aproximación bien definida, ha aprendido algo importante.

Para ver la naturaleza genérica de la linealidad, considere una partícula que se mueve en el eje $x$ con energía potencial $V(x)$. La fuerza sobre la partícula en el punto $x$ es menos la derivada de la energía potencial,

$$F = -\frac{d}{dx}V(x)\,. \qquad \text{(1.21)}$$

Una fuerza que puede derivarse de una energía potencial de esta forma se llama fuerza «conservativa».

En un punto de equilibrio, $x_0$, la fuerza se anula, y por tanto la derivada de la energía potencial se anula:

$$F = -\left.\frac{d}{dx}V(x)\right|_{x=x_0} = -V'(x_0) = 0\,. \qquad \text{(1.22)}$$

Podemos describir las pequeñas oscilaciones del sistema en torno al equilibrio de la forma más simple si redefinimos el origen de modo que $x_0=0$. Entonces el desplazamiento respecto al equilibrio es la coordenada $x$. Podemos expandir la fuerza en serie de Taylor:

$$F(x) = -V'(x) = -V'(0) - x\,V''(0) - \frac{1}{2}x^2\,V'''(0) + \cdots \qquad \text{(1.23)}$$

El primer término en (1.23) se anula porque este sistema está en equilibrio en $x=0$, de acuerdo con (1.22). El segundo término tiene la forma de la ley de Hooke, con

$$K = V''(0)\,. \qquad \text{(1.24)}$$

El equilibrio es estable si la segunda derivada de la energía potencial es positiva, de modo que $x=0$ es un mínimo local de la energía potencial.

El punto importante es que, para $x$ suficientemente pequeño, el tercer término de (1.23), y todos los siguientes, serán mucho menores que el segundo. El tercer término es despreciable si

$$\left|x\,V'''(0)\right| \ll V''(0)\,. \qquad \text{(1.25)}$$

Típicamente, cada derivada adicional trae consigo un factor $1/L$, donde $L$ es la distancia sobre la cual la energía potencial cambia una fracción apreciable. Entonces (1.25) se convierte en

$$x \ll L\,. \qquad \text{(1.26)}$$

Solo hay dos formas en que una fuerza derivada de una energía potencial puede dejar de ser aproximadamente lineal para oscilaciones suficientemente pequeñas en torno al equilibrio estable:

1.  Si el potencial no es suave, de modo que la primera o la segunda derivada del potencial no está bien definida en el punto de equilibrio, entonces no podemos hacer un desarrollo de Taylor y el argumento de (1.23) no funciona. Daremos un ejemplo de este tipo al final de este capítulo.

2.  Aunque las derivadas existan en el punto de equilibrio $x=0$, puede ocurrir que $V''(0)=0$. En este caso, para tener un equilibrio estable, también debemos tener $V'''(0)=0$; de lo contrario, un pequeño desplazamiento en una dirección u otra crecería con el tiempo. Entonces el siguiente término del desarrollo de Taylor domina para $x$ pequeño, dando una fuerza proporcional a $x^3$.

![Figura 1.2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.2.png)

Figura 1.2: energía potencial de la ecuación (1.27), $V(x) = E(L/x + x/L)$, mostrada para $x$ entre 0 y $5L$; presenta un mínimo en $x=L$.

Ambos casos excepcionales son muy raros en la naturaleza. Habitualmente, la energía potencial es una función suave del desplazamiento y no hay razón para que $V''(0)$ se anule. La situación genérica es que las pequeñas oscilaciones en torno al equilibrio estable son lineales.

Puede ser útil un ejemplo. Casi cualquier función de energía potencial con un punto de equilibrio estable sirve, siempre que sea suave. Por ejemplo, considere la energía potencial

$$V(x) = E\left(\frac{L}{x} + \frac{x}{L}\right)\,. \qquad \text{(1.27)}$$

Esto se muestra en la figura 1.2. El mínimo (al menos para $x$ positivo) ocurre en $x=L$, así que primero redefinimos $x = X+L$, de modo que

$$V(X) = E\left(\frac{L}{X+L} + \frac{X+L}{L}\right)\,. \qquad \text{(1.28)}$$

La fuerza correspondiente es

$$F(X) = E\left(\frac{L}{(X+L)^2} - \frac{1}{L}\right)\,. \qquad \text{(1.29)}$$

Podemos mirar cerca de $X=0$ y expandir en serie de Taylor:

$$F(X) = -2\frac{E}{L}\left(\frac{X}{L}\right) + 3\frac{E}{L}\left(\frac{X}{L}\right)^2 + \cdots \qquad \text{(1.30)}$$

Ahora, el cociente entre el primer término no lineal y el término lineal es

$$\frac{3X}{2L}\,, \qquad \text{(1.31)}$$

que es pequeño si $X \ll L$.

En otras palabras, cuanto más cerca esté del punto de equilibrio, más se parece la energía potencial real a la parábola que esperaríamos de la energía potencial de una fuerza lineal tipo ley de Hooke. Puede verlo gráficamente ampliando una pequeña región en torno al punto de equilibrio. En la figura 1.3, el rectángulo punteado de la figura 1.2 se ha ampliado hasta convertirse en un cuadrado. Note que se parece mucho más a una parábola que la figura 1.2. Si repitiéramos el procedimiento y volviéramos a ampliar una pequeña región en torno al punto de equilibrio, no podría detectar a simple vista el término cúbico.

![Figura 1.3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.3.png)

Figura 1.3: ampliación del pequeño rectángulo punteado de la figura 1.2, entre $0.9L$ y $1.1L$, mostrando una forma mucho más parabólica.

A menudo, la aproximación lineal es incluso mejor, porque el término de orden $x^2$ se anula por simetría. Por ejemplo, cuando el sistema es simétrico respecto a $x=0$, de modo que $V(x)=V(-x)$, el término de orden $x^3$ (y todos los $x^n$ con $n$ impar) en la energía potencial se anula, y entonces no hay término de orden $x^2$ en la fuerza.

Para un muelle típico, la linealidad (la ley de Hooke) es una excelente aproximación para desplazamientos pequeños. Sin embargo, siempre hay términos no lineales que se vuelven importantes si los desplazamientos son suficientemente grandes. Habitualmente, en este libro nos limitaremos a las pequeñas oscilaciones y supondremos que nuestros sistemas son lineales. Sin embargo, no debe concluir que el tema de los sistemas no lineales carece de interés. De hecho, es un área muy activa de la investigación actual en física.

## 1.3 Invariancia bajo traslación temporal

### 1.3.1 Movimiento circular uniforme

*(Referencia al programa interactivo 1-1 del disco de programas del curso original.)*

Cuando $\alpha$, $\beta$ y $\gamma$ en (1.15) no dependen del tiempo $t$, y en ausencia de fuerza externa, es decir, para el movimiento libre, el tiempo entra en (1.15) solo a través de las derivadas. Entonces la ecuación de movimiento tiene la forma

$$\alpha\,\frac{d^2}{dt^2}x(t) + \beta\,\frac{d}{dt}x(t) + \gamma\,x(t) = 0\,. \qquad \text{(1.32)}$$

La ecuación de movimiento del oscilador armónico no amortiguado, (1.3), tiene esta forma con $\alpha=m$, $\beta=0$ y $\gamma=K$. Las soluciones de (1.32) tienen la propiedad de que

$$\text{si } x(t) \text{ es una solución, } x(t+a) \text{ también lo será.} \qquad \text{(1.33)}$$

Matemáticamente, esto es cierto porque las operaciones de derivar respecto al tiempo y sustituir $t \to t+a$ pueden hacerse en cualquier orden gracias a la regla de la cadena

$$\frac{d}{dt}x(t+a) = \left[\frac{d}{dt}(t+a)\right]\left[\frac{d}{dt'}x(t')\right]_{t'=t+a} = \left[\frac{d}{dt'}x(t')\right]_{t'=t+a}\,. \qquad \text{(1.34)}$$

La razón física de (1.33) es que podemos cambiar el ajuste inicial de nuestro reloj y la física se verá igual. La solución $x(t+a)$ puede obtenerse a partir de la solución $x(t)$ cambiando el ajuste del reloj en $a$. La etiqueta temporal ha sido «trasladada» en $a$. Nos referiremos a la propiedad (1.33) como invariancia bajo traslación temporal.

La mayoría de los sistemas físicos en los que pueda pensar son invariantes bajo traslación temporal en ausencia de fuerza externa. Para obtener un oscilador sin invariancia bajo traslación temporal, tendría que hacer algo bastante extraño, como hacer que la constante del muelle dependiera del tiempo.

Para el movimiento libre del oscilador armónico, aunque la ecuación de movimiento es ciertamente invariante bajo traslación temporal, la manifestación de esta invariancia en la solución (1.6) no es tan simple como podría ser. Las dos partes de la solución, una proporcional a $\cos\omega t$ y la otra a $\sin\omega t$, se mezclan al reajustar el reloj. Por ejemplo,

$$\cos[\omega(t+a)] = \cos\omega a\cos\omega t - \sin\omega a\sin\omega t\,. \qquad \text{(1.35)}$$

Será muy útil encontrar otra forma de escribir la solución que se comporte de manera más simple al reajustar los relojes. Para ello, tendremos que trabajar con números complejos.

Para motivar la introducción de los números complejos, comenzaremos mostrando la relación entre el movimiento armónico simple y el movimiento circular uniforme. Considere el movimiento circular uniforme en el plano $x$-$y$ alrededor de un círculo centrado en el origen, $x=y=0$, con radio $R$ y velocidad en sentido horario $v=R\omega$. Las coordenadas $x$ e $y$ del movimiento son

$$x(t) = R\cos(\omega t - \varphi)\,,\qquad y(t) = -R\sin(\omega t - \varphi)\,, \qquad \text{(1.36)}$$

donde $\varphi$ es el ángulo en radianes, medido en sentido antihorario, de la posición en $t=0$ respecto al eje $x$ positivo. La $x(t)$ de (1.36) es idéntica a la $x(t)$ de (1.6) con

$$x(0) = R\cos\varphi\,,\qquad x'(0) = \omega R\sin\varphi\,. \qquad \text{(1.37)}$$

El movimiento armónico simple es equivalente a una componente del movimiento circular uniforme. Esta relación se ilustra en la figura 1.4. A medida que el punto se mueve alrededor del círculo con velocidad constante $R\omega$, la coordenada $x$ ejecuta un movimiento armónico simple con velocidad angular $\omega$. Si lo deseamos, podemos elegir las dos constantes necesarias para fijar la solución de (1.3) como $R$ y $\varphi$, en lugar de $x(0)$ y $x'(0)$. En este lenguaje, la acción de reajustar el reloj es más transparente: reajustar el reloj cambia el valor de $\varphi$ sin cambiar nada más.

![Figura 1.4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.4.png)

Figura 1.4: circunferencia de radio $R$ recorrida con velocidad angular $\omega$ en sentido horario; la proyección sobre el eje $x$ ejecuta movimiento armónico simple.

Pero nos gustaría aún más. La idea clave es que la linealidad nos otorga una libertad considerable. Podemos sumar soluciones de las ecuaciones de movimiento y multiplicarlas por constantes, y el resultado sigue siendo una solución. Nos gustaría usar esta libertad para elegir soluciones que se comporten de la forma más simple posible bajo traslaciones temporales.

El comportamiento más simple posible para una solución $z(t)$ bajo traslación temporal es

$$z(t+a) = h(a)\,z(t)\,. \qquad \text{(1.38)}$$

Es decir, nos gustaría encontrar una solución que se reproduzca a sí misma salvo una constante global, $h(a)$, cuando reajustamos nuestros relojes en $a$. Como siempre somos libres de multiplicar una solución de una ecuación de movimiento lineal homogénea por una constante, el cambio de $z(t)$ a $h(a)z(t)$ no supone gran cosa. Llamaremos a una solución que satisface (1.38) una «solución irreducible» respecto a las traslaciones temporales, porque su comportamiento bajo traslaciones temporales (reajustes del reloj) es lo más simple que puede ser.

Resulta que, para sistemas cuyas ecuaciones de movimiento son lineales e invariantes bajo traslación temporal, como veremos con más detalle más abajo, siempre podemos encontrar soluciones irreducibles que tienen la propiedad (1.38). Sin embargo, para el movimiento armónico simple, esto requiere números complejos. Puede verlo notando que cambiar el ajuste del reloj en $\pi/\omega$ simplemente cambia el signo de la solución con frecuencia angular $\omega$, porque tanto el término coseno como el seno cambian de signo:

$$\cos(\omega t+\pi) = -\cos\omega t\,,\qquad \sin(\omega t+\pi) = -\sin\omega t\,. \qquad \text{(1.39)}$$

Pero entonces, de (1.38) y (1.39), podemos escribir

$$-z(t) = z(t+\pi/\omega) = z(t+\pi/2\omega+\pi/2\omega) = h(\pi/2\omega)\,z(t+\pi/2\omega) = h(\pi/2\omega)^2\,z(t)\,. \qquad \text{(1.40)}$$

Así, no podemos encontrar tal solución a menos que $h(\pi/2\omega)$ tenga la propiedad

$$[h(\pi/2\omega)]^2 = -1\,. \qquad \text{(1.41)}$$

¡El cuadrado de $h(\pi/2\omega)$ es $-1$! Por tanto, nos vemos obligados a considerar los números complejos. Cuando terminemos de introducirlos, volveremos a (1.38) y mostraremos que siempre podemos encontrar soluciones de esta forma para sistemas lineales e invariantes bajo traslación temporal.

## 1.4 Números complejos

La raíz cuadrada de $-1$, llamada $i$, es importante en física y matemáticas por muchas razones. Las cantidades físicas medibles siempre pueden describirse con números reales: nunca obtendrá una lectura de $i$ metros en su regla. Sin embargo, veremos que cuando $i$ se incluye junto con los números reales y las operaciones aritméticas habituales (suma, resta, multiplicación y división), el álgebra, la trigonometría y el cálculo se simplifican. Aunque los números complejos no son necesarios para describir los fenómenos ondulatorios, nos permitirán discutirlos de forma más simple y esclarecedora.

### 1.4.1 Algunas definiciones

Un número imaginario es un número de la forma $i$ por un número real.

Un número complejo, $z$, es una suma de un número real y un número imaginario: $z=a+ib$.

Las partes real e «imaginaria», $\text{Re}(z)$ y $\text{Im}(z)$, del número complejo $z=a+ib$:

$$\text{Re}(z) = a\,,\qquad \text{Im}(z) = b\,. \qquad \text{(1.42)}$$

Note que la parte imaginaria es en realidad un número real: el coeficiente real de $i$ en $z=a+ib$.

El conjugado complejo, $z^*$, del número complejo $z$, se obtiene cambiando el signo de $i$:

$$z^* = a - ib\,. \qquad \text{(1.43)}$$

Note que $\text{Re}(z) = (z+z^*)/2$ y $\text{Im}(z) = (z-z^*)/2i$.

El plano complejo: como un número complejo $z$ queda especificado por dos números reales, puede pensarse como un vector bidimensional, con componentes $(a,b)$. La parte real de $z$, $a=\text{Re}(z)$, es la componente $x$, y la parte imaginaria de $z$, $b=\text{Im}(z)$, es la componente $y$.

![Figura 1.5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.5.png)

Figura 1.5 y 1.6: dos vectores en el plano complejo. La figura 1.5 muestra $2+i \leftrightarrow (2,1)$, con ángulo $\theta = \arg(2+i) = \arctan(1/2)$ medido desde el eje $x$ positivo. La figura 1.6 muestra $-1.5-2i \leftrightarrow (-1.5,-2)$, con $\theta = \arg(-1.5-2i) = \arctan(4/3)+\pi$.

El valor absoluto, $|z|$, de $z$, es la longitud del vector $(a,b)$:

$$|z| = \sqrt{a^2+b^2} = \sqrt{z^*z}\,. \qquad \text{(1.44)}$$

El valor absoluto $|z|$ es siempre un número real no negativo.

El argumento o fase, $\arg(z)$, de un número complejo $z$ no nulo, es el ángulo, en radianes, del vector $(a,b)$ en sentido antihorario desde el eje $x$:

$$\arg(z) = \begin{cases} \arctan(b/a) & \text{para } a \ge 0\,, \\ \arctan(b/a) + \pi & \text{para } a < 0\,. \end{cases} \qquad \text{(1.45)}$$

Como cualquier ángulo, $\arg(z)$ puede redefinirse sumando un múltiplo de $2\pi$ radianes o $360°$ (véanse las figuras 1.5 y 1.6).

### 1.4.2 Aritmética

*(Referencia al programa interactivo 1-2 del disco de programas del curso original.)*

Las operaciones aritméticas de suma, resta y multiplicación de números complejos se definen tratando $i$ como una variable algebraica, usando la propiedad distributiva y la relación $i^2=-1$. Así, si $z=a+ib$ y $z'=a'+ib'$, entonces

$$\begin{aligned}
z+z' &= (a+a') + i(b+b')\,,\\
z-z' &= (a-a') + i(b-b')\,,\\
zz' &= (aa'-bb') + i(ab'+ba')\,.
\end{aligned} \qquad \text{(1.46)}$$

Por ejemplo:

$$(3+4i)+(-2+7i) = (3-2)+(4+7)i = 1+11i\,, \qquad \text{(1.47)}$$

$$(3+4i)\cdot(5+7i) = (3\cdot5-4\cdot7) + (3\cdot7+4\cdot5)i = -13+41i\,. \qquad \text{(1.48)}$$

Vale la pena jugar con la multiplicación compleja y familiarizarse con el plano complejo.

La división es más complicada. Dividir un número complejo $z$ por un número real $r$ es fácil: basta dividir tanto la parte real como la imaginaria por $r$, obteniendo $z/r = a/r + ib/r$. Para dividir por un número complejo $z'$, podemos usar el hecho de que $z'^*z'=|z'|^2$ es real. Si multiplicamos el numerador y el denominador de $z/z'$ por $z'^*$, podemos escribir:

$$z/z' = z'^*z/|z'|^2 = \frac{aa'+bb'}{a'^2+b'^2} + i\,\frac{ba'-ab'}{a'^2+b'^2}\,. \qquad \text{(1.49)}$$

Por ejemplo:

$$(3+4i)/(2+i) = (3+4i)\cdot(2-i)/5 = (10+5i)/5 = 2+i\,. \qquad \text{(1.50)}$$

Con estas definiciones para las operaciones aritméticas, el valor absoluto se comporta de forma muy simple bajo multiplicación y división. Bajo multiplicación, el valor absoluto del producto de dos números complejos es el producto de los valores absolutos:

$$|zz'| = |z|\,|z'|\,. \qquad \text{(1.51)}$$

La división funciona igual, siempre que no divida por cero:

$$|z/z'| = |z|/|z'| \quad \text{si } z' \neq 0\,. \qquad \text{(1.52)}$$

Los matemáticos llaman «álgebra de división» a un conjunto de objetos sobre el que se definen la suma y la multiplicación y para el cual existe un valor absoluto que satisface (1.51) y (1.52). Es un hecho matemático curioso (aunque irrelevante para nosotros) que los números complejos son una de solo cuatro álgebras de división, siendo las otras los números reales y objetos más exóticos llamados cuaterniones y octoniones, obtenidos relajando los requisitos de conmutatividad y asociatividad (respectivamente) de las leyes de multiplicación.

Lo maravilloso de los números complejos desde el punto de vista del álgebra es que todas las ecuaciones polinómicas tienen solución. Por ejemplo, la ecuación $x^2-2x+5=0$ no tiene soluciones reales, pero tiene dos soluciones complejas, $x=1\pm 2i$. En general, una ecuación de la forma $p(x)=0$, donde $p(x)$ es un polinomio de grado $n$ con coeficientes complejos (o reales), tiene $n$ soluciones si se permiten números complejos, pero puede no tener ninguna si $x$ se restringe a ser real.

Note que el conjugado complejo de cualquier suma, producto, etc. de números complejos puede obtenerse simplemente cambiando el signo de $i$ dondequiera que aparezca. Esto implica que si el polinomio $p(z)$ tiene coeficientes reales, las soluciones de $p(z)=0$ aparecen en pares conjugados complejos. Es decir, si $p(z)=0$, entonces $p(z^*)=0$ también.

### 1.4.3 Exponenciales complejas

Considere un número complejo $z=a+ib$ con valor absoluto 1. Como $|z|=1$ implica $a^2+b^2=1$, podemos escribir $a$ y $b$ como el coseno y el seno de un ángulo $\theta$.

$$z = \cos\theta + i\sin\theta \quad \text{para } |z|=1\,. \qquad \text{(1.53)}$$

Como

$$\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{b}{a} \qquad \text{(1.54)}$$

el ángulo $\theta$ es el argumento de $z$:

$$\arg(\cos\theta+i\sin\theta) = \theta\,. \qquad \text{(1.55)}$$

Pensemos en $z$ como función de $\theta$ y consideremos el cálculo. La derivada respecto a $\theta$ es:

$$\frac{\partial}{\partial\theta}(\cos\theta+i\sin\theta) = -\sin\theta+i\cos\theta = i(\cos\theta+i\sin\theta) \qquad \text{(1.56)}$$

Una función que, al derivarla, se reproduce a sí misma salvo una constante es una exponencial. En particular, si tuviéramos una función de $\theta$, $f(\theta)$, que satisficiera $\partial f(\theta)/\partial\theta = kf(\theta)$ para $k$ real, concluiríamos que $f(\theta)=e^{k\theta}$. Así, si queremos que el cálculo funcione de la misma manera para los números complejos que para los reales, debemos concluir que

$$e^{i\theta} = \cos\theta + i\sin\theta\,. \qquad \text{(1.57)}$$

Podemos comprobar esta relación notando que los desarrollos de Taylor de ambos lados son iguales. Los desarrollos de Taylor de las funciones exponencial, coseno y seno son:

$$\begin{aligned}
e^x &= 1 + x + \frac{x^2}{2} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots\\
\cos(x) &= 1 - \frac{x^2}{2} + \frac{x^4}{4!} - \cdots\\
\sin(x) &= x - \frac{x^3}{3!} + \cdots
\end{aligned} \qquad \text{(1.58)}$$

Así, el desarrollo de Taylor del lado izquierdo de (1.57) es

$$1 + i\theta + (i\theta)^2/2 + (i\theta)^3/3! + \cdots \qquad \text{(1.59)}$$

mientras que el desarrollo del lado derecho es

$$(1-\theta^2/2+\cdots) + i(\theta-\theta^3/6+\cdots) \qquad \text{(1.60)}$$

Las potencias de $i$ en (1.59) funcionan justo de la manera adecuada para reproducir el patrón de signos menos en (1.60).

Además, la ley de multiplicación funciona correctamente:

$$e^{i\theta}e^{i\theta'} = (\cos\theta+i\sin\theta)(\cos\theta'+i\sin\theta') = \cos(\theta+\theta') + i\sin(\theta+\theta') = e^{i(\theta+\theta')}\,. \qquad \text{(1.61)}$$

Así, (1.57) tiene sentido en todos los aspectos. Esta conexión entre las exponenciales complejas y las funciones trigonométricas se llama identidad de Euler. Es extremadamente útil. Entre otras cosas, la lógica puede invertirse y las funciones trigonométricas pueden «definirse» algebraicamente en términos de exponenciales complejas:

$$\cos\theta = \frac{e^{i\theta}+e^{-i\theta}}{2}\,,\qquad \sin\theta = \frac{e^{i\theta}-e^{-i\theta}}{2i} = -i\,\frac{e^{i\theta}-e^{-i\theta}}{2}\,. \qquad \text{(1.62)}$$

Usando (1.62), las identidades trigonométricas pueden deducirse muy fácilmente. Por ejemplo:

$$\cos 3\theta = \text{Re}(e^{3i\theta}) = \text{Re}((e^{i\theta})^3) = \cos^3\theta - 3\cos\theta\sin^2\theta\,. \qquad \text{(1.63)}$$

Otro ejemplo que nos será útil más adelante es:

$$\begin{aligned}
\cos(\theta+\theta') + \cos(\theta-\theta') &= \frac{e^{i(\theta+\theta')}+e^{-i(\theta+\theta')}+e^{i(\theta-\theta')}+e^{-i(\theta-\theta')}}{2}\\
&= \frac{(e^{i\theta}+e^{-i\theta})(e^{i\theta'}+e^{-i\theta'})}{2} = 2\cos\theta\cos\theta'\,. \qquad \text{(1.64)}
\end{aligned}$$

Todo número complejo no nulo puede escribirse como el producto de un número real positivo (su valor absoluto) y un número complejo de valor absoluto 1. Así,

$$z = x+iy = R\,e^{i\theta} \quad \text{donde } R=|z|\,,\ \theta = \arg(z)\,. \qquad \text{(1.65)}$$

En el plano complejo, (1.65) expresa el hecho de que un vector bidimensional puede escribirse en coordenadas cartesianas, $(x,y)$, o en coordenadas polares, $(R,\theta)$. Por ejemplo, $\sqrt3+i = 2e^{i\pi/6}$; $1+i = \sqrt2\,e^{i\pi/4}$; $-8i = 8e^{3i\pi/2}=8e^{-i\pi/2}$. La figura 1.7 muestra el número complejo $1+i=\sqrt2\,e^{i\pi/4}$.

![Figura 1.7](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.7.png)

Figura 1.7: el número complejo $1+i$ representado como un vector de módulo $\sqrt2$ y ángulo $\pi/4$ respecto al eje real.

La relación (1.65) da otra forma útil de pensar en la multiplicación de números complejos. Si

$$z_1 = R_1 e^{i\theta_1}\quad\text{y}\quad z_2 = R_2 e^{i\theta_2}\,, \qquad \text{(1.66)}$$

entonces

$$z_1 z_2 = R_1 R_2\, e^{i(\theta_1+\theta_2)}\,. \qquad \text{(1.67)}$$

En palabras: para multiplicar dos números complejos, se multiplican los valores absolutos y se suman los argumentos.

La ecuación (1.57) da lugar a varias relaciones que pueden parecer sorprendentes hasta que se acostumbre a ellas. Por ejemplo: $e^{i\pi}=-1$; $e^{i\pi/2}=i$; $e^{2i\pi}=1$. Estas tienen una interpretación en el plano complejo, donde $e^{i\theta}$ es el vector unitario $(\cos\theta,\sin\theta)$, en un ángulo $\theta$ medido en sentido antihorario desde el eje $x$. Entonces $-1$ está a $180°$ o $\pi$ radianes en sentido antihorario desde el eje $x$, mientras que $i$ está sobre el eje $y$, a $90°$ o $\pi/2$ radianes del eje $x$. $2\pi$ radianes son $360°$, y por tanto nos hacen volver completamente al eje $x$. Estas relaciones se muestran en la figura 1.8.

![Figura 1.8](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.8.png)

Figura 1.8: círculo unidad en el plano complejo mostrando los puntos $1=e^{2i\pi}$, $i=e^{i\pi/2}$, $-1=e^{i\pi}$ y $-i=e^{-i\pi/2}=e^{3i\pi/2}$.

### 1.4.4 Notación

No es estrictamente necesario tener una notación que distinga entre números reales y complejos. La razón es que, como hemos visto, las reglas de la aritmética, el álgebra y el cálculo se aplican a los números reales y complejos exactamente de la misma manera. Sin embargo, a algunos lectores les puede resultar útil que se les recuerde cuándo una cantidad es compleja. Esto es probablemente particularmente útil para cantidades como $x$, que representan coordenadas físicas. Por ello, al menos durante los primeros capítulos, hasta que el lector esté completamente «complejizado», distinguiremos entre «coordenadas» reales y complejas. Si son reales, usaremos las letras $x$ e $y$. Si son complejas, usaremos $z$ y $w$.

## 1.5 Soluciones exponenciales

Ya estamos listos para traducir las condiciones de linealidad e invariancia bajo traslación temporal a matemáticas. Lo que veremos es que estas dos propiedades conducen automáticamente a soluciones irreducibles que satisfacen (1.38), y además que estas soluciones irreducibles son simplemente exponenciales. No necesitamos usar ningún otro detalle sobre la ecuación de movimiento para obtener este resultado. Por tanto, nuestros argumentos se aplicarán a situaciones mucho más complicadas, en las que haya amortiguamiento, más grados de libertad, o ambas cosas. Mientras el sistema tenga invariancia bajo traslación temporal y linealidad, las soluciones serán sumas de soluciones exponenciales irreducibles.

Hemos visto que las soluciones de ecuaciones diferenciales lineales homogéneas con coeficientes constantes, de la forma

$$M\,\frac{d^2}{dt^2}x(t) + K\,x(t) = 0\,, \qquad \text{(1.68)}$$

tienen las propiedades de linealidad e invariancia bajo traslación temporal. La ecuación del movimiento armónico simple es de esta forma. Las coordenadas son reales, y las constantes $M$ y $K$ son reales porque son cosas físicas como masas y constantes de muelle. Sin embargo, queremos permitirnos el lujo de considerar también soluciones complejas, así que consideramos la misma ecuación con variables complejas:

$$M\,\frac{d^2}{dt^2}z(t) + K\,z(t) = 0\,. \qquad \text{(1.69)}$$

Note la relación entre las soluciones de (1.68) y (1.69). Como los coeficientes $M$ y $K$ son reales, para cada solución $z(t)$ de (1.69), el conjugado complejo, $z(t)^*$, también es una solución. La ecuación diferencial sigue siendo cierta al cambiar el signo de todas las $i$.

A partir de estas dos soluciones, podemos construir dos soluciones reales:

$$x_1(t) = \text{Re}(z(t)) = (z(t)+z(t)^*)/2\,;\qquad x_2(t) = \text{Im}(z(t)) = (z(t)-z(t)^*)/2i\,. \qquad \text{(1.70)}$$

Todo esto es posible gracias a la linealidad, que nos permite ir y venir entre soluciones reales y complejas formando combinaciones lineales, como en (1.70). Estas son soluciones de (1.68). Note que $x_1(t)$ y $x_2(t)$ son justamente las partes real e imaginaria de $z(t)$. El punto importante es que siempre puede reconstruir las soluciones físicas reales de la ecuación de movimiento a partir de la solución compleja. Puede hacer toda la matemática usando variables complejas, lo que la hace mucho más fácil. Luego, al final, puede obtener la solución física de interés simplemente tomando la parte real de su solución compleja.

Volvamos ahora a la solución de (1.69). Lo que queremos mostrar es que llegamos a soluciones irreducibles y exponenciales para cualquier sistema con invariancia bajo traslación temporal y linealidad. Así entenderemos por qué siempre podemos encontrar soluciones irreducibles, no solo en (1.69), sino en situaciones mucho más complicadas, con amortiguamiento o más grados de libertad.

Hay dos elementos cruciales:

1.  La invariancia bajo traslación temporal, (1.33), que exige que $x(t+a)$ sea una solución si $x(t)$ es una solución;
2.  La linealidad, que nos permite formar combinaciones lineales de soluciones para obtener nuevas soluciones.

Resolveremos (1.68) usando únicamente estos dos elementos. Esto nos permitirá generalizar inmediatamente nuestra solución a cualquier sistema en el que estén presentes las propiedades anteriores.

Una forma de usar la linealidad es elegir un conjunto «base» de soluciones, $x_j(t)$ para $j=1$ hasta $n$, que sea «completo» y «linealmente independiente». Para el oscilador armónico, bastan dos soluciones, así que $n=2$. Pero nuestro análisis será mucho más general y se aplicará, por ejemplo, a sistemas lineales con más grados de libertad, así que dejaremos $n$ libre. Que el conjunto sea «completo» significa que cualquier solución $z(t)$ (que puede ser compleja) puede expresarse como una combinación lineal de las $x_j(t)$,

$$z(t) = \sum_{j=1}^n c_j\,x_j(t)\,. \qquad \text{(1.72)}$$

Que sean «linealmente independientes» significa que ninguna de las $x_j(t)$ puede expresarse como combinación lineal de las demás, de modo que la única combinación lineal de las $x_j(t)$ que se anula es la combinación trivial, con todos los coeficientes nulos,

$$\sum_{j=1}^n c_j\,x_j(t) = 0 \implies c_j = 0\,. \qquad \text{(1.73)}$$

Veamos ahora si podemos encontrar una solución irreducible que se comporte de forma simple ante un cambio en el ajuste inicial del reloj, como en (1.38),

$$z(t+a) = h(a)\,z(t) \qquad \text{(1.74)}$$

para alguna función (posiblemente compleja) $h(a)$. En términos de las soluciones base, esto es

$$z(t+a) = h(a)\sum_{k=1}^n c_k\,x_k(t)\,. \qquad \text{(1.75)}$$

Pero cada una de las soluciones base también se transforma en una solución bajo una traslación temporal, y cada nueva solución puede a su vez escribirse como una combinación lineal de las soluciones base, así:

$$x_j(t+a) = \sum_{k=1}^n R_{jk}(a)\,x_k(t)\,. \qquad \text{(1.76)}$$

Así,

$$z(t+a) = \sum_{j=1}^n c_j\,x_j(t+a) = \sum_{j,k=1}^n c_j\,R_{jk}(a)\,x_k(t)\,. \qquad \text{(1.77)}$$

Comparando (1.75) y (1.77), y usando (1.73), vemos que podemos encontrar una solución irreducible si y solo si

$$\sum_{j=1}^n c_j\,R_{jk}(a) = h(a)\,c_k \quad\text{para todo } k\,. \qquad \text{(1.78)}$$

Esto se llama una «ecuación de autovalores». Tendremos mucho más que decir sobre las ecuaciones de autovalores en el capítulo 3, cuando discutamos la notación matricial. Por ahora, note que (1.78) es un sistema de $n$ ecuaciones simultáneas homogéneas en las $n$ incógnitas $c_j$. Podemos reescribirlo como

$$\sum_{j=1}^n c_j\,S_{jk}(a) = 0 \quad\text{para todo } k\,, \qquad \text{(1.79)}$$

donde

$$S_{jk}(a) = \begin{cases} R_{jk}(a) & \text{para } j\neq k\,, \\ R_{jk}(a) - h(a) & \text{para } j=k\,. \end{cases} \qquad \text{(1.80)}$$

Podemos encontrar una solución de (1.78) si y solo si existe una solución de la ecuación de determinante

$$\det S_{jk}(a) = 0\,. \qquad \text{(1.81)}$$

(Discutiremos el determinante en detalle en el capítulo 3, así que si ha olvidado este resultado del álgebra, no se preocupe por ahora.)

(1.81) es una ecuación de grado $n$ en la variable $h(a)$. Puede no tener soluciones reales, pero siempre tiene $n$ soluciones complejas para $h(a)$ (aunque algunos de los valores de $h(a)$ pueden repetirse). Para cada solución de $h(a)$, podemos encontrar un conjunto de $c_j$ que satisfaga (1.78). Las distintas combinaciones lineales $z(t)$ construidas de esta forma constituirán un conjunto linealmente independiente de soluciones irreducibles, cada una satisfaciendo (1.74) para algún $h(a)$. Si hay $n$ valores distintos de $h(a)$, la situación habitual, formarán un conjunto completo de soluciones irreducibles de las ecuaciones de movimiento. Entonces podemos tomar directamente nuestras soluciones como irreducibles, satisfaciendo (1.74). Más adelante veremos qué ocurre cuando algunos de los $h(a)$ se repiten, de modo que hay menos de $n$ valores distintos.

Ahora, para cada solución irreducible, podemos ver cuáles deben ser las funciones $h(a)$ y $z(a)$. Si derivamos ambos lados de (1.74) respecto a $a$, obtenemos

$$z'(t+a) = h'(a)\,z(t)\,. \qquad \text{(1.82)}$$

Poniendo $a=0$ da

$$z'(t) = H\,z(t) \qquad \text{(1.83)}$$

donde

$$H \equiv h'(0)\,. \qquad \text{(1.84)}$$

Esto implica

$$z(t) \propto e^{Ht}\,. \qquad \text{(1.85)}$$

¡Así, la solución irreducible es una exponencial! Hemos mostrado que (1.71) conduce a soluciones irreducibles y exponenciales, sin usar ningún detalle de la dinámica.

### 1.5.1 \* Construyendo la exponencial

Hay otra forma de ver lo que (1.74) implica para la forma de la solución irreducible, que ni siquiera involucra resolver la sencilla ecuación diferencial (1.83). Empecemos poniendo $t=0$ en (1.74). Esto da

$$h(a) = z(a)/z(0)\,. \qquad \text{(1.86)}$$

$h(a)$ es proporcional a $z(a)$. Esto es particularmente simple si elegimos multiplicar nuestra solución irreducible por una constante de modo que $z(0)=1$. Entonces (1.86) da

$$h(a) = z(a) \qquad \text{(1.87)}$$

y por tanto

$$z(t+a) = z(t)\,z(a)\,. \qquad \text{(1.88)}$$

Consideremos qué ocurre para $t=\epsilon \ll 1$ muy pequeño. Haciendo un desarrollo de Taylor, podemos escribir

$$z(\epsilon) = 1 + H\epsilon + O(\epsilon^2) \qquad \text{(1.89)}$$

donde $H=z'(0)$, de (1.84) y (1.87). Usando (1.88), podemos mostrar que

$$z(N\epsilon) = [z(\epsilon)]^N\,. \qquad \text{(1.90)}$$

Entonces, para cualquier $t$, podemos escribir (tomando $t=N\epsilon$)

$$z(t) = \lim_{N\to\infty}[z(t/N)]^N = \lim_{N\to\infty}[1+H(t/N)]^N = e^{Ht}\,. \qquad \text{(1.91)}$$

Así, de nuevo vemos que la solución irreducible respecto a la invariancia bajo traslación temporal es simplemente una exponencial:

$$z(t) = e^{Ht}\,. \qquad \text{(1.92)}$$

### 1.5.2 ¿Qué es $H$?

Cuando sustituimos la solución irreducible, $e^{Ht}$, en (1.69), las derivadas simplemente bajan potencias de $H$, así que la ecuación se convierte en una ecuación puramente algebraica (eliminando un factor global $e^{Ht}$)

$$M H^2 + K = 0\,. \qquad \text{(1.93)}$$

Ahora, por fin, podemos ver la relevancia de los números complejos en la discusión anterior sobre la invariancia bajo traslación temporal. Para $M$ y $K$ positivos, la ecuación (1.93) no tiene ninguna solución si restringimos $H$ a ser real. No podemos encontrar ninguna solución irreducible real. Pero siempre hay dos soluciones para $H$ entre los números complejos. En este caso, la solución es

$$H = \pm i\omega \quad\text{donde } \omega = \sqrt{\frac{K}{M}}\,. \qquad \text{(1.94)}$$

Es solo en este último paso, donde efectivamente calculamos $H$, que entran los detalles de (1.69). Hasta (1.93), todo se seguía simplemente de los principios generales, (1.71).

Ahora, como antes, a partir de estas dos soluciones podemos construir dos soluciones reales tomando las partes real e imaginaria de $z(t)=e^{\pm i\omega t}$.

$$x_1(t) = \text{Re}(z(t)) = \cos\omega t\,,\qquad x_2(t) = \text{Im}(z(t)) = \pm\sin\omega t\,. \qquad \text{(1.95)}$$

Las traslaciones temporales mezclan estas dos soluciones reales. Por eso las soluciones exponenciales complejas irreducibles son más fáciles de manejar. La cantidad $\omega$ es la frecuencia angular que vimos en (1.5), en la solución de la ecuación de movimiento del oscilador armónico. Cualquier combinación lineal de tales soluciones puede escribirse en términos de una «amplitud» y una «fase», de la siguiente manera: para $c$ y $d$ reales,

$$\begin{aligned}
c\cos(\omega t)+d\sin(\omega t) &= c\,\frac{e^{i\omega t}+e^{-i\omega t}}{2} - id\,\frac{e^{i\omega t}-e^{-i\omega t}}{2} = \text{Re}\left[(c+id)e^{-i\omega t}\right]\\
&= \text{Re}\left[A e^{i\theta}e^{-i\omega t}\right] = \text{Re}\left[A e^{-i(\omega t-\theta)}\right] = A\cos(\omega t-\theta)\,. \qquad \text{(1.96)}
\end{aligned}$$

donde $A$ es un número real positivo llamado la amplitud,

$$A = \sqrt{c^2+d^2}\,, \qquad \text{(1.97)}$$

y $\theta$ es un ángulo llamado la fase,

$$\theta = \arg(c+id)\,. \qquad \text{(1.98)}$$

Estas relaciones son otro ejemplo de la equivalencia entre coordenadas cartesianas y polares, discutida tras (1.65). El par $c$ y $d$ son las coordenadas cartesianas en el plano complejo del número complejo $c+id$. La amplitud, $A$, y la fase, $\theta$, son la representación en coordenadas polares del mismo número complejo. (1.96) muestra que $c$ y $d$ son también los coeficientes de $\cos\omega t$ y $\sin\omega t$ en la parte real del producto de este número complejo con $e^{-i\omega t}$. Esta relación se ilustra en la figura 1.9 (note la relación con la figura 1.4). Mientras $z$ se mueve en sentido horario con velocidad angular constante, $\omega$, alrededor del círculo $|z|=A$ en el plano complejo, la parte real de $z$ realiza un movimiento armónico simple, $A\cos(\omega t-\theta)$.

![Figura 1.9](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.9.png)

Figura 1.9: representación en el plano complejo del número $A e^{-i(\omega t - \theta)}$, con coordenadas cartesianas $c,d$ y fase $\theta$; la proyección real ejecuta $A\cos(\omega t - \theta)$.

Ahora que conoce los números complejos y las exponenciales complejas, debería volver a la relación entre el movimiento armónico simple y el movimiento circular uniforme ilustrada en la figura 1.4. El movimiento circular uniforme puede interpretarse como un movimiento en el plano complejo de

$$z(t) = e^{-i\omega t}\,. \qquad \text{(1.99)}$$

A medida que $t$ cambia, $z(t)$ se mueve con velocidad constante en sentido horario alrededor del círculo unidad en el plano complejo. La parte real, $\cos\omega t$, ejecuta un movimiento armónico simple.

Note que igual de fácilmente podríamos haber tomado nuestra solución compleja como $e^{+i\omega t}$. Esto correspondería a un movimiento antihorario en el plano complejo, pero la parte real, que es lo único que importa físicamente, no cambiaría. Es convencional en física tomar soluciones complejas proporcionales a $e^{-i\omega t}$. Esto es puramente una convención; no hay física en ello. Sin embargo, es suficientemente universal en la literatura de física como para que intentemos hacerlo así de manera consistente aquí.

## 1.6 Circuitos LC

Uno de los ejemplos más importantes de un sistema oscilante es un circuito LC. Probablemente estudió estos circuitos en su curso de electricidad y magnetismo. Al igual que un muelle que obedece la ley de Hooke, este sistema es lineal, porque las relaciones entre carga, corriente, voltaje, etc., para inductores, condensadores y resistencias ideales, son lineales. Aquí queremos hacer explícita la analogía entre un circuito LC particular y un sistema de una masa sobre un muelle. El circuito LC, con un inductor sin resistencia de inductancia $L$ y un condensador de capacitancia $C$, se muestra en la figura 1.10. Normalmente no pensaríamos en esto como un circuito en absoluto, porque no hay batería ni otra fuente de energía eléctrica. Sin embargo, podríamos imaginar, por ejemplo, que el condensador se cargó inicialmente al montar el circuito. Entonces circularía corriente al cerrar el circuito. De hecho, en ausencia de resistencia, la corriente seguiría oscilando para siempre. Veremos que este circuito es análogo a la combinación de muelles y una masa mostrada en la figura 1.11. La frecuencia de oscilación del sistema mecánico es

$$\omega = \sqrt{\frac{K}{m}}\,. \qquad \text{(1.100)}$$

![Figura 1.10](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.10.png)

Figura 1.10: circuito LC formado por un inductor $L$ y un condensador $C$ en un lazo cerrado. Figura 1.11: sistema mecánico análogo, una masa $m$ unida a un muelle de constante $K$ y a una pared fija.

Podemos describir la configuración del sistema mecánico de la figura 1.10 en términos de $x$, el desplazamiento del bloque hacia la derecha. Podemos describir la configuración del circuito LC de la figura 1.10 en términos de $Q$, la carga que ha «pasado» a través del inductor desde la situación de equilibrio con el condensador descargado. En este caso, la carga desplazada a través del inductor va enteramente al condensador, porque no tiene otro sitio adonde ir, como se muestra en la figura 1.12. La corriente a través del inductor es la derivada temporal de la carga que ha pasado,

![Figura 1.11](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.11.png)

Figura 1.11

$$I = \frac{dQ}{dt}\,. \qquad \text{(1.101)}$$

![Figura 1.12](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.12.png)

Figura 1.12: carga $Q$ desplazada a través del inductor, acumulándose como $+Q$ en una placa del condensador y $-Q$ en la otra.

Para ver cómo funciona el circuito LC, podemos examinar los voltajes en distintos puntos del sistema, como se muestra en la figura 1.13. Para un inductor, la caída de voltaje a través de él es la tasa de cambio de la corriente que lo atraviesa, o

$$-L\,\frac{dI}{dt} = V\,. \qquad \text{(1.102)}$$

![Figura 1.13](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.13.png)

Figura 1.13: voltaje y corriente en el circuito LC; el voltaje es $0$ en los extremos del inductor salvo por la caída debida a él, y $V=Q/C$ en el condensador.

Para el condensador, la carga almacenada es el voltaje por la capacitancia, o

$$V = Q/C\,. \qquad \text{(1.103)}$$

Juntando (1.101), (1.102) y (1.103) obtenemos

$$L\,\frac{dI}{dt} = L\,\frac{d^2Q}{dt^2} = -\frac{1}{C}Q\,. \qquad \text{(1.104)}$$

La correspondencia entre los dos sistemas es la siguiente:

$$m \leftrightarrow L\,,\qquad K \leftrightarrow 1/C\,,\qquad x \leftrightarrow Q\,. \qquad \text{(1.105)}$$

Al hacer las sustituciones de (1.105), la ecuación de movimiento de la masa sobre el muelle, (1.3), se convierte en (1.104). Así, conociendo la solución (1.6) para la masa sobre el muelle, podemos concluir inmediatamente que la carga desplazada en este circuito LC oscila con frecuencia

$$\omega = \sqrt{\frac{1}{LC}}\,. \qquad \text{(1.106)}$$

## 1.7 Unidades — desplazamiento y energía

Hemos visto ya dos tipos de sistemas físicos muy diferentes que presentan oscilación armónica simple. Hay otros posibles, y daremos otro ejemplo a continuación. Este es un buen momento para discutir las unidades de las ecuaciones de movimiento. La ecuación de movimiento «genérica» para el movimiento armónico simple sin amortiguamiento tiene esta forma:

$$M\,\frac{d^2\mathcal{X}}{dt^2} = -K\,\mathcal{X} \qquad \text{(1.107)}$$

donde

$$\begin{aligned}
&\mathcal{X}\ \text{es la coordenada generalizada,}\\
&M\ \text{es la masa generalizada,}\\
&K\ \text{es la constante de muelle generalizada.}
\end{aligned} \qquad \text{(1.108)}$$

En el movimiento armónico simple de una masa puntual, $\mathcal{X}$ es justamente el desplazamiento respecto al equilibrio, $x$; $M$ es la masa, $m$; y $K$ es la constante del muelle, $K$.

Las unidades apropiadas para $M$ y $K$ dependen de las unidades de $\mathcal{X}$. Se determinan convencionalmente exigiendo que

$$\frac{1}{2}M\left(\frac{d\mathcal{X}}{dt}\right)^2 \qquad \text{(1.109)}$$

sea la energía «cinética» del sistema debida al cambio de la coordenada con el tiempo, y que

$$\frac{1}{2}K\mathcal{X}^2 \qquad \text{(1.110)}$$

sea la energía «potencial» del sistema, almacenada en el muelle generalizado.

Tiene buen sentido físico conceder a la energía un estatus especial en estos problemas, porque, en ausencia de fricción y fuerzas externas, la energía total —la suma de la energía cinética (1.109) y la energía potencial (1.110)— es constante. En la oscilación, la energía se almacena alternadamente en energía cinética y potencial. Cuando el sistema está en su configuración de equilibrio pero moviéndose con su velocidad máxima, toda la energía es cinética. Cuando el sistema se detiene instantáneamente en su desplazamiento máximo, toda la energía es potencial. De hecho, a veces es más fácil identificar $M$ y $K$ calculando las energías cinética y potencial que encontrando directamente la ecuación de movimiento. Usaremos este truco en el capítulo 11 para discutir las ondas de agua.

Por ejemplo, en un circuito LC en unidades del SI, tomamos nuestra coordenada generalizada como una carga, $Q$, en culombios. La energía se mide en julios, o voltios por culombios. La constante de muelle generalizada tiene unidades de

$$\frac{\text{julios}}{\text{culombios}^2} = \frac{\text{voltios}}{\text{culombios}} \qquad \text{(1.111)}$$

que es la inversa de la unidad de capacitancia, culombios por voltio, o faradios. La masa generalizada tiene unidades de

$$\frac{\text{julios}\times\text{segundos}^2}{\text{culombios}^2} = \frac{\text{voltios}\times\text{segundos}}{\text{amperios}} \qquad \text{(1.112)}$$

que es una unidad de inductancia (henrios). Esto es lo que usamos en nuestra correspondencia entre el circuito LC y el oscilador mecánico, (1.105).

También podemos añadir una fuerza generalizada al lado derecho de (1.107). La fuerza generalizada tiene unidades de energía sobre desplazamiento generalizado. Esto es correcto porque, cuando la ecuación de movimiento se multiplica por el desplazamiento, (1.109) y (1.110) implican que cada uno de los términos tiene unidades de energía. Así, por ejemplo, en el circuito LC, la fuerza generalizada es un voltaje.

### 1.7.1 Energía constante

La energía total es la suma de la energía cinética más la potencial, de (1.109) y (1.110),

$$E = \frac{1}{2}M\left(\frac{d\mathcal{X}}{dt}\right)^2 + \frac{1}{2}K\mathcal{X}^2\,. \qquad \text{(1.113)}$$

Si no actúan fuerzas externas sobre el sistema, la energía total debe ser constante. Puede verse de (1.113) que la energía puede ser constante para una solución oscilante solo si la frecuencia angular, $\omega$, es $\sqrt{K/M}$. Suponga, por ejemplo, que el desplazamiento generalizado del sistema tiene la forma

$$\mathcal{X}(t) = A\sin\omega t\,, \qquad \text{(1.114)}$$

donde $A$ es una amplitud con las unidades de $\mathcal{X}$. Entonces la velocidad generalizada es

$$\frac{d}{dt}\mathcal{X}(t) = A\omega\cos\omega t\,. \qquad \text{(1.115)}$$

Para que la energía sea constante, debemos tener

$$K = \omega^2 M\,. \qquad \text{(1.116)}$$

Entonces, la energía total, de (1.109) y (1.110), es

$$\frac{1}{2}M\omega^2 A^2\cos^2\omega t + \frac{1}{2}KA^2\sin^2\omega t = \frac{1}{2}KA^2\,. \qquad \text{(1.117)}$$

### 1.7.2 El péndulo de torsión

Puede ser útil otro ejemplo más. Consideremos el péndulo de torsión, mostrado en la figura 1.14.

![Figura 1.14](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.14.png)

Figura 1.14: dos vistas de un péndulo de torsión —una barra o mancuerna suspendida por su centro mediante un hilo o fibra desde un soporte superior; la vista superior muestra el ángulo de torsión $\theta$.

Un péndulo de torsión es un oscilador simple pero muy útil, formado por una mancuerna o varilla sostenida por su centro mediante un hilo o fibra, colgada de un soporte superior. Cuando la mancuerna se tuerce un ángulo $\theta$, como se muestra en la vista superior de la figura 1.14, el hilo se retuerce y proporciona un par restaurador sobre la mancuerna. Para un hilo o fibra adecuados, este par restaurador es casi lineal incluso para ángulos de desplazamiento bastante grandes. En este sistema, la variable natural para el desplazamiento es el ángulo $\theta$. Entonces la ecuación de movimiento es

$$I\,\frac{d^2\theta}{dt^2} = -\alpha\theta\,, \qquad \text{(1.118)}$$

donde $I$ es el momento de inercia de la mancuerna respecto a su centro y $-\alpha\theta$ es la fuerza restauradora. Así, la masa generalizada es el momento de inercia, $I$, con unidades de longitud al cuadrado por masa, y la constante de muelle generalizada es la constante $\alpha$, con unidades de par. Como es de esperar, de (1.109) y (1.110), la energía cinética y potencial son (respectivamente)

$$\frac{1}{2}I\left(\frac{d\theta}{dt}\right)^2 \quad\text{y}\quad \frac{1}{2}\alpha\theta^2\,. \qquad \text{(1.119)}$$

## 1.8 Un oscilador no lineal simple

Para ilustrar algunas de las diferencias entre osciladores lineales y no lineales, daremos un ejemplo muy simple de oscilador no lineal. Considere la siguiente ecuación de movimiento no lineal:

$$m\,\frac{d^2}{dt^2}x = \begin{cases} -F_0 & \text{para } x>0\,,\\ F_0 & \text{para } x<0\,,\\ 0 & \text{para } x=0\,. \end{cases} \qquad \text{(1.120)}$$

Esto describe una partícula de masa $m$ sometida a una fuerza hacia la izquierda, $-F_0$, cuando la partícula está a la derecha del origen ($x(t)>0$), una fuerza hacia la derecha, $F_0$, cuando la partícula está a la izquierda del origen ($x(t)<0$), y ninguna fuerza cuando la partícula está justo en el origen.

La energía potencial de este sistema crece linealmente a ambos lados de $x=0$. No puede derivarse en $x=0$, porque la derivada no es continua allí. Así, no podemos desarrollar en serie de Taylor la energía potencial (ni la fuerza) en torno al punto $x=0$, y los argumentos de (1.21)-(1.24) no se aplican.

Es fácil encontrar una solución de (1.120). Suponga que en el instante $t=0$ la partícula está en el origen pero moviéndose con velocidad positiva $v$. La partícula se mueve inmediatamente a la derecha del origen y desacelera con aceleración constante, $-F_0/m$, de modo que

$$x(t) = vt - \frac{F_0}{2m}t^2 \quad\text{para } t\le\tau\,, \qquad \text{(1.121)}$$

donde

$$\tau = \frac{2mv}{F_0} \qquad \text{(1.122)}$$

es el tiempo requerido para que la partícula dé la vuelta y regrese al origen. En el instante $t=\tau$, la partícula pasa a la izquierda del origen. En ese punto se mueve con velocidad $-v$, y el proceso se repite para $x$ negativo y aceleración positiva $F_0/m$. Entonces la solución continúa en la forma

$$x(t) = -v(t-\tau) + \frac{F_0}{2m}(t-\tau)^2 \quad\text{para } \tau\le t\le 2\tau\,. \qquad \text{(1.123)}$$

Luego todo el proceso se repite. El movimiento de la partícula, mostrado en la figura 1.15, se parece superficialmente a una oscilación armónica, pero la curva es en realidad una secuencia de parábolas empalmadas, en lugar de una onda senoidal.

![Figura 1.15](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.15.png)

Figura 1.15: posición $x(t)$, en unidades de $mv^2/(2F_0)$ en el eje vertical y $\tau$ en el horizontal, formada por arcos de parábola alternos entre $0$ y $\pm mv^2/(2F_0)$, con periodo $2\tau$.

La ecuación de movimiento, (1.120), es invariante bajo traslación temporal. Claramente, podemos hacer arrancar la partícula desde el origen con velocidad $v$ en cualquier instante $t_0$. La solución entonces se ve como la mostrada en la figura 1.15, pero trasladada en el tiempo por $t_0$. La solución tiene la forma

$$x_{t_0}(t) = x(t-t_0) \qquad \text{(1.124)}$$

donde $x(t)$ es la función descrita por (1.121), (1.123), etc. Esto se muestra en la figura 1.16 para $t_0=3\tau/4$. La curva punteada corresponde a $t_0=0$.

![Figura 1.16](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.16.png)

Figura 1.16: la misma trayectoria en zigzag parabólico que la figura 1.15, pero desplazada en el tiempo un valor $t_0 = 3\tau/4$; la curva punteada muestra la trayectoria original sin desplazar.

Al igual que el oscilador armónico, este sistema oscila de forma regular e indefinida. Sin embargo, en este caso, el periodo de la oscilación, el tiempo que tarda en repetirse, $2\tau$, depende de la amplitud de la oscilación, o equivalentemente, de la velocidad inicial, $v$. El periodo es proporcional a $v$, según (1.122). El movimiento de la partícula, arrancando desde el origen en $t=t_0$, para una velocidad inicial $v/2$, se muestra en la figura 1.17. La curva punteada corresponde a una velocidad inicial $v$.

![Figura 1.17](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.17.png)

Figura 1.17: la misma familia de trayectorias parabólicas, pero con una velocidad inicial $v/2$, de modo que el periodo se duplica respecto al caso de velocidad $v$, mostrado en trazo punteado para comparar.

Aunque la ecuación de movimiento no lineal, (1.120), es invariante bajo traslación temporal, la simetría es mucho menos útil porque el sistema carece de linealidad. Desde nuestro punto de vista, lo importante de la linealidad (aparte del hecho de que es una buena aproximación en tantos sistemas físicos importantes) es que nos permite elegir una base conveniente para las soluciones de la ecuación de movimiento. Las elegimos de modo que se comporten de forma simple bajo traslaciones temporales. Entonces, gracias a la linealidad, podemos construir cualquier solución como una combinación lineal de las soluciones base. En una situación como (1.120), no tenemos esta opción.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Analizar la física de un oscilador armónico, incluyendo encontrar la constante del muelle, plantear la ecuación de movimiento, resolverla e imponer las condiciones iniciales;
2.  Encontrar la «constante de muelle» aproximada para pequeñas oscilaciones en torno a un punto de equilibrio y estimar el desplazamiento a partir del cual la linealidad deja de ser válida;
3.  Entender la conexión entre la oscilación armónica y el movimiento circular uniforme;
4.  Usar la aritmética compleja y las exponenciales complejas;
5.  Resolver ecuaciones de movimiento lineales homogéneas usando soluciones irreducibles que son exponenciales complejas;
6.  Entender y explicar la diferencia entre frecuencia y frecuencia angular;
7.  Analizar las oscilaciones de circuitos LC;
8.  Calcular cantidades físicas para sistemas oscilantes en unidades del SI;
9.  Entender la invariancia bajo traslación temporal en sistemas no lineales.

## Problemas

**1.1.** Para la masa y el muelle discutidos en (1.1)-(1.8), suponga que el sistema cuelga verticalmente en el campo gravitatorio terrestre, con el extremo superior del muelle fijo. Demuestre que la frecuencia de las oscilaciones verticales viene dada por (1.5). Explique por qué la gravedad no afecta a la frecuencia angular.

**1.2.**

1.  Encuentre una expresión para $\cos 7\theta$ en términos de $\cos\theta$ y $\sin\theta$, usando exponenciales complejas y el desarrollo del binomio.

2.  Haga lo mismo para $\sin 5\theta$.

3.  Use exponenciales complejas para encontrar una expresión para $\sin(\theta_1+\theta_2+\theta_3)$ en términos de los senos y cosenos de los ángulos individuales.

4.  ¿Recuerda la «fórmula del ángulo mitad»,

$$\cos^2\frac{\theta}{2} = \frac{1}{2}(1+\cos\theta)\ ?$$

Use exponenciales complejas para demostrar la «fórmula del quinto ángulo»,

$$\cos^5\frac{\theta}{5} = \frac{10}{16}\cos\frac{\theta}{5} + \frac{5}{16}\cos\frac{3\theta}{5} + \frac{1}{16}\cos\theta\,.$$

1.  Use exponenciales complejas para demostrar la identidad

$$\sin 6x = \sin x\left(32\cos^5x - 32\cos^3x + 6\cos x\right)\,.$$

**1.3.**

1.  Escriba $i+\sqrt3$ en la forma $Re^{i\theta}$. Escriba $\theta$ como un número racional multiplicado por $\pi$.

2.  Haga lo mismo para $i-\sqrt3$.

3.  Demuestre que las dos raíces cuadradas de $Re^{i\theta}$ son $\pm\sqrt{R}\,e^{i\theta/2}$. (Pista: esto es fácil, no se esfuerce demasiado.)

4.  Use el resultado de c. para encontrar las raíces cuadradas de $2i$ y de $2+2i\sqrt3$.

**1.4.** Encuentre las seis soluciones de la ecuación $z^6=1$ y escriba cada una en la forma $A+iB$, representándolas en el plano complejo. (Pista: escriba $z=Re^{i\theta}$ con $R$ real y positivo, y encuentre $R$ y $\theta$.)

**1.5.** Encuentre tres soluciones independientes de la ecuación diferencial

$$\frac{d^3}{dt^3}f(t) + f(t) = 0\,.$$

Debe usar exponenciales complejas para deducir las soluciones, pero exprese los resultados en forma real.

**1.6.** Un bloque de masa $M$ desliza sin fricción entre dos muelles de constantes $K$ y $2K$, como se muestra en la figura. El bloque está obligado a moverse solo hacia la izquierda y hacia la derecha en el papel, así que el sistema tiene un único grado de libertad.

![Figura](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/figs1.png)

Figura: bloque $M$ entre un muelle de constante $K$ a su izquierda y otro de constante $2K$ a su derecha, ambos anclados a paredes fijas.

Calcule la frecuencia angular de la oscilación. Si la velocidad del bloque en su posición de equilibrio es $v$, calcule la amplitud de la oscilación.

**1.7.** Una partícula de masa $m$ se mueve en el eje $x$ con energía potencial

$$V(x) = \frac{E_0}{a^4}\left(x^4+4ax^3-8a^2x^2\right)\,.$$

Encuentre las posiciones en las que la partícula está en equilibrio estable. Encuentre la frecuencia angular de las pequeñas oscilaciones en torno a cada posición de equilibrio. ¿Qué entiende por pequeñas oscilaciones? Sea cuantitativo y dé una respuesta separada para cada punto de equilibrio estable.

**1.8.** Para el péndulo de torsión de la figura 1.14, suponga que el péndulo consiste en dos masas de 0.01 kg sobre una varilla ligera de longitud total 0.1 m. Si la constante de muelle generalizada, $\alpha$, es $5\times10^{-7}\ \text{N}\,\text{m}$, encuentre la frecuencia angular del oscilador.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.
