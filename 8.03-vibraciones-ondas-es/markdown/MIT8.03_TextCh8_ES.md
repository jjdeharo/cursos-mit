# Capítulo 8: Ondas viajeras

En este capítulo mostramos cómo la misma física que da lugar a las oscilaciones de onda estacionaria también origina ondas que se mueven tanto en el espacio como en el tiempo. Después pasamos a introducir el importante ejemplo físico de las ondas de luz.

## Vídeos de esta clase (YouTube)

- [Clase 12: Ecuaciones de Maxwell, ondas electromagnéticas](https://www.youtube.com/watch?v=8kcvyoHsXrw)
- [Clase 13: Medio dispersivo, velocidad de fase, velocidad de grupo](https://www.youtube.com/watch?v=QxemLb8-5AA)

## Resumen previo

En un sistema infinito invariante bajo traslación, las ondas viajeras surgen de forma natural a partir del comportamiento exponencial complejo de las soluciones en el espacio y el tiempo.

1.  Empezamos mostrando la conexión entre las ondas estacionarias y las ondas viajeras en sistemas infinitos. Una onda viajera en un sistema lineal es un par de ondas estacionarias combinadas con una relación de fase especial. Mostramos cómo pueden producirse ondas viajeras en sistemas finitos mediante oscilaciones forzadas apropiadas.

2.  A continuación discutimos la fuerza y la potencia necesarias para producir una onda viajera en una cuerda, e introducimos la útil idea de «impedancia».

3.  Introducimos y discutimos el ejemplo clásico más importante de fenómeno ondulatorio: las ondas electromagnéticas y la luz.

4.  Reexaminamos los sistemas invariantes bajo traslación de circuitos LC acoplados discutidos en el capítulo 5, y mostramos cómo se relacionan con las ondas electromagnéticas.

5.  Discutimos los efectos del amortiguamiento en sistemas invariantes bajo traslación, dando una interpretación física simple del efecto en las ondas viajeras.

6.  Discutimos las ondas viajeras en sistemas con amortiguamiento y en sistemas con cortes de frecuencia altos y/o bajos.

## 8.1 Ondas estacionarias y viajeras

### 8.1.1 ¿Qué es lo que se mueve?

*(Referencia al programa interactivo 8-1 del disco de programas del curso original.)*

Hemos visto que un sistema infinito con invariancia bajo traslación tiene soluciones complejas de la forma

$$e^{\pm ikx}e^{\pm i\omega t}\,, \qquad \text{(8.1)}$$

donde $k$ y $\omega$ están relacionados por la relación de dispersión característica del sistema. Hasta ahora hemos considerado soluciones de onda estacionaria en las que los factores espacial y temporal son cada uno real por separado, es decir,

$$\sin kx\cdot\cos\omega t \propto (e^{ikx}-e^{-ikx})\cdot(e^{i\omega t}+e^{-i\omega t})\,. \qquad \text{(8.2)}$$

Pero podemos combinar las mismas soluciones de otra manera,

$$\psi(x,t) = \cos(kx-\omega t) \propto (e^{ikx}e^{-i\omega t}+e^{-ikx}e^{i\omega t})\,. \qquad \text{(8.3)}$$

Esto se llama una «onda viajera». El sistema subyacente que sostiene la onda no se está moviendo en realidad; lo que se mueve es la onda misma. Si seguimos el punto $x$ para el cual $\psi(x,t)$ tiene cierto valor constante, ese punto se mueve en la dirección $x$ positiva con velocidad constante, llamada la «velocidad de fase»,

$$v_\varphi = \omega(k)/k\,. \qquad \text{(8.4)}$$

En (8.3), por ejemplo, $\psi(x,t)$ vale uno para $x=t=0$, porque el argumento del coseno es cero (también vale uno para $x=2n\pi/k$, para cualquier entero $n$, pero nos centraremos en el único punto $x=0$). A medida que $t$ aumenta, este punto se mueve en la dirección $x$ positiva, porque el argumento del coseno, $kx-\omega t$, se anula para $x=\omega t/k=v_\varphi t$. Esto se ilustra en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-1" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-1</a>.

Seguiremos definiendo todos los modos reales como las partes reales de modos complejos proporcionales a $e^{-i\omega t}$. Así, (8.3) es

$$\cos(kx-\omega t) = \text{Re}\left[e^{ikx}e^{-i\omega t}\right]\,. \qquad \text{(8.5)}$$

En esta notación, una onda que viaja hacia la izquierda es

$$\cos(kx+\omega t) = \text{Re}\left[e^{-ikx}e^{-i\omega t}\right]\,, \qquad \text{(8.6)}$$

mientras que una onda estacionaria es

$$\cos kx\cos\omega t = \frac{1}{2}\text{Re}\left[e^{ikx}e^{-i\omega t}+e^{-ikx}e^{-i\omega t}\right] = \frac{1}{2}\left[\cos(kx-\omega t)+\cos(kx+\omega t)\right]\,. \qquad \text{(8.7)}$$

¡Una onda estacionaria es una combinación de ondas viajeras en direcciones opuestas! Del mismo modo, una onda viajera es una combinación de ondas estacionarias. Por ejemplo,

$$\cos(kx-\omega t) = \cos kx\cos\omega t + \sin kx\sin\omega t\,. \qquad \text{(8.8)}$$

Estas relaciones son importantes porque muestran que la relación entre $k$ y $\omega$, la relación de dispersión, ¡es exactamente la misma para las ondas viajeras que para las ondas estacionarias! Una onda es una onda, viaje o esté estacionaria. De hecho, podemos ir y venir usando (8.7) y (8.8). La relación de dispersión que vincula $k$ y $\omega$ es una propiedad del sistema en el que existen las ondas, no de la onda particular.

El reverso de esta moneda es que las ondas viajeras existen para sistemas con cualquier relación de dispersión. Conocer la velocidad de fase, (8.4), para todo $k$, es equivalente a conocer la relación de dispersión, porque hay que conocer $\omega(k)$. En particular, solo para sistemas continuos simples, como la cuerda estirada (véase (6.5)), $\omega(k)$ es proporcional a $k$ y la velocidad de fase es una constante, independiente de $k$.

### 8.1.2 Condiciones de contorno

*(Referencia al programa interactivo 8-2 del disco de programas del curso original.)*

Las ondas viajeras pueden producirse en sistemas finitos mediante oscilación forzada con una fase apropiada de las oscilaciones en los dos extremos. Un ejemplo simple involucra una cuerda estirada con tensión $T$ y densidad de masa lineal $\rho$. Dadas condiciones de contorno sobre el sistema tales que

$$\psi(0,t)=A\cos\omega t\,,\qquad \psi(L,t)=A\sin\omega t\,, \qquad \text{(8.9)}$$

donde $L$ es la longitud de la cuerda, la frecuencia angular $\omega$ se elige de modo que

$$k = \frac{5\pi}{2L} = \omega\sqrt{\frac{\rho}{T}} = \frac{\omega}{v_\varphi}\,. \qquad \text{(8.10)}$$

Como de costumbre en un problema de oscilación forzada, nos interesa la solución estacionaria en la que el sistema se mueve con la frecuencia angular, $\omega$, de los términos impulsores. Podemos resolver este problema fácilmente descomponiéndolo en dos problemas.

Primero considere la condición de contorno:

$$\psi_1(0,t)=0\,,\qquad \psi_1(L,t)=A\sin\omega t\,. \qquad \text{(8.11)}$$

Esto se resuelve fácilmente con los métodos del capítulo 5. A partir de la condición en $x=0$, sabemos que la solución de $\psi_1(x,t)$ es proporcional a $\sin kx$. Entonces la condición de contorno en $x=L$ da la solución de onda estacionaria:

$$\psi_1(x,t) = A\sin kx\sin\omega t\,. \qquad \text{(8.12)}$$

Considere ahora la condición de contorno

$$\psi_2(0,t)=A\cos\omega t\,,\qquad \psi_2(L,t)=0\,. \qquad \text{(8.13)}$$

Argumentos análogos (empezando en $x=L$) muestran que la solución es la onda estacionaria

$$\psi_2(x,t) = A\cos kx\cos\omega t\,. \qquad \text{(8.14)}$$

Ahora podemos obtener la solución para la condición de contorno (8.9) simplemente sumando estas:

$$\psi(x,t) = \psi_1(x,t)+\psi_2(x,t) = A\cos kx\cos\omega t+A\sin kx\sin\omega t = A\cos(kx-\omega t)\,, \qquad \text{(8.15)}$$

que es una onda que viaja de $x=0$ a $x=L$. El punto crucial es que las dos ondas estacionarias con las que se construye la onda viajera están desfasadas $90°$ entre sí, tanto en el tiempo como en el espacio: se hacen grandes en puntos distintos del espacio y también en instantes distintos, y la interacción entre ambas produce la onda viajera. Esto se ilustra en las figuras 8.1-8.4 para $\omega t=0,\pi/4,\pi/2$ y $3\pi/4$. En cada una de estas figuras, la curva superior es la onda viajera; la curva del medio es (8.14); la curva inferior es (8.12).

![Figura 8.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh8_ES/fig8.1.png)

Figuras 8.1-8.4: instantáneas de la construcción de la onda viajera en $\omega t=0,\pi/4,\pi/2,3\pi/4$; en cada una, la curva superior es la suma de las dos ondas estacionarias mostradas debajo, que se desplaza progresivamente hacia la derecha a medida que avanza el tiempo.

Este sistema se anima en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-2" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-2</a>. Esta animación es importante: vale la pena observarla un rato para hacerse una idea de cómo funciona (8.15), mejor de lo que permiten las imágenes fijas de las figuras 8.1-8.4. Si se concentra en un punto particular de la cuerda, verá que la onda viajera se hace grande cuando una de las ondas estacionarias es máxima mientras la otra está cerca de cero, o (según dónde mire) cuando ambas ondas estacionarias son positivas.

## 8.2 Fuerza, potencia e impedancia

![Figura 8.5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh8_ES/fig8.5.png)

Figura 8.5 y 8.6: fuerza que ejerce una cuerda sobre un agente externo en $x=0$ y en $x=L$, mostrando la componente de la tensión perpendicular a la cuerda, con $\theta\approx\psi'$ para pequeños desplazamientos.

Para producir la onda viajera de (8.15), necesitamos calcular la fuerza requerida en cada extremo. En $x=0$, la fuerza aplicada por el agente externo debe igualar a la componente transversal de la tensión de la cuerda que tira hacia la derecha (dirección $+x$), como se muestra en la figura 8.5:

$$F_0 = -T\sin\theta \approx -T\,\left.\frac{\partial}{\partial x}\psi(x,t)\right|_{x=0}\,. \qquad \text{(8.16)}$$

En $x=L$, como la cuerda llega desde la dirección $-x$, es

$$F_L = T\,\left.\frac{\partial}{\partial x}\psi(x,t)\right|_{x=L}\,, \qquad \text{(8.17)}$$

como se ilustra en la figura 8.6.

En la oscilación forzada, el extremo de la cuerda se mueve solo en la dirección transversal. Así, la potencia suministrada por la fuerza externa en $x=0$, que es $\vec F\cdot\vec v$, es

$$P(t) = -T\,\left.\frac{\partial}{\partial x}\psi(x,t)\right|_{x=0}\,\frac{\partial}{\partial t}\psi(0,t) \qquad \text{(8.18)}$$

donde, como en (2.26), $\psi(x,t)$ es el desplazamiento real respecto al equilibrio del trozo de cuerda en la posición horizontal $x$. Debemos tomar primero la parte real, porque la potencia es una función no lineal del desplazamiento.

Para una onda estacionaria en la cuerda (o cualquier sistema sin fuerzas de fricción), la fuerza y la velocidad están desfasadas $90°$. Por ejemplo, si el desplazamiento es proporcional a $\sin\omega t$, entonces la fuerza transversal en cada extremo también es proporcional a $\sin\omega t$. La velocidad, sin embargo, es proporcional a $\cos\omega t$. Así, la potencia gastada por la fuerza externa es

$$\propto \sin\omega t\cos\omega t = \frac{1}{2}\sin2\omega t\,. \qquad \text{(8.19)}$$

Esto se promedia a cero en medio ciclo. En promedio, no se requiere potencia para mantener la onda estacionaria (en ausencia de amortiguamiento).

En una onda viajera, en cambio, la fuerza y la velocidad son proporcionales. De (8.15) puede ver que

$$\frac{\partial}{\partial x}\psi(x,t) = -\frac{k}{\omega}\,\frac{\partial}{\partial t}\psi(x,t)\,. \qquad \text{(8.20)}$$

Así,

$$F_0 = Z\,\frac{\partial}{\partial t}\psi(0,t)\,,\qquad F_L = -Z\,\frac{\partial}{\partial t}\psi(L,t)\,, \qquad \text{(8.21)}$$

donde la constante $Z$,

$$Z = \frac{Tk}{\omega} = \sqrt{\rho T}\,, \qquad \text{(8.22)}$$

se llama la «impedancia» del sistema de la cuerda. Mide la potencia necesaria para producir la onda viajera. La potencia necesaria en $x=0$ es

$$P_0 = Z\left(\frac{\partial}{\partial t}\psi(0,t)\right)^2 = ZA^2\omega^2\sin^2\omega t\,. \qquad \text{(8.23)}$$

La potencia media gastada es, por tanto,

$$\langle P_0\rangle = ZA^2\omega^2/2\,. \qquad \text{(8.24)}$$

La potencia gastada en $x=0$ para producir la onda viajera es entregada por la cuerda en $x=L$, porque la potencia requerida en $L$ es

$$P_L = -Z\left(\frac{\partial}{\partial t}\psi(L,t)\right)^2 = -ZA^2\omega^2\cos^2\omega t\,. \qquad \text{(8.25)}$$

Si las condiciones de contorno fueran tales que las ondas viajeras fueran en la dirección opuesta, la fuerza en las deducciones anteriores tendría el signo opuesto al de (8.20). Así, siempre se necesita potencia positiva para producir la onda, y se necesita potencia negativa para absorberla. Puede parecer extraño que la potencia entregada a la onda en (8.23) y la potencia entregada por la onda en (8.25) no sean exactamente iguales y opuestas. La suma se anula en promedio, pero oscila con el tiempo. La razón es que la longitud del sistema no es un número entero de longitudes de onda, lo que permite que la energía almacenada en el sistema, la suma de la cinética y la potencial, oscile en función del tiempo.

Note que la fuerza necesaria para absorber una onda viajera, en (8.21), es negativa y proporcional a la velocidad: esta es una fuerza friccional típica. Así, una onda viajera puede ser absorbida completamente por una fuerza friccional (o una resistencia) con exactamente el cociente correcto entre fuerza y velocidad. Si la impedancia del «amortiguador» (así se llama tal resistencia) no es exactamente igual a la de la cuerda, habrá algo de reflexión; volveremos a esto en el próximo capítulo.

### 8.2.1 \* Impedancia compleja

Para la cuerda estirada, un sistema cuya relación de dispersión es equivalente a la ecuación de ondas, (6.4), la fuerza sobre el sistema y la velocidad del desplazamiento, $\partial\psi/\partial t$, son proporcionales para cualquier onda viajera (lo veremos en detalle en el capítulo 10). En general, esto no es cierto. Por ejemplo, considere la cuerda con cuentas de la figura 5.4, estirada de $x=0$ a algún $x$ grande. Suponga además que hay una onda viajera en el sistema de la forma

$$\psi(x,t) = A\cos(kx-\omega t)\,, \qquad \text{(8.26)}$$

ilustrada en la figura 8.7 (para una animación de una onda viajera en un sistema similar, véase el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-6" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-6</a>; el sistema mostrado en ese programa tiene las cuentas sobre muelles, además de sobre una cuerda, pero la forma de la onda viajera es la misma; solo la relación de dispersión es distinta). La línea punteada es la posición de equilibrio de la cuerda.

![Figura 8.7](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh8_ES/fig8.7.png)

Figura 8.7: instantánea de una onda viajera en una cuerda con cuentas, mostrando las cuentas desplazadas siguiendo la envolvente $A\cos(kx-\omega t)$.

Mientras $k$ y $\omega$ estén relacionados por la relación de dispersión, (5.39), (8.26) es una solución de la ecuación de movimiento. La fuerza transversal externa en $x=0$ necesaria para producir la onda viajera está relacionada con la diferencia entre el desplazamiento del primer bloque y el desplazamiento del extremo en $x=0$ (véase la figura 5.5). Es

$$F_0 = \frac{TA}{a}\left(\cos(\omega t-ka)-\cos\omega t\right)\,. \qquad \text{(8.27)}$$

Esto es aproximadamente proporcional a la velocidad solo si $ka$ es muy pequeño, de modo que el lado derecho de (8.27) pueda expandirse en serie de Taylor. Así, en este caso, y en general para un sistema discreto, no podemos definir la impedancia simplemente como en (8.21).

Sin embargo, supongamos que, en lugar de la onda viajera real, (8.26), consideramos una onda viajera armónica compleja con dependencia irreducible en el tiempo y el espacio, de la forma

$$\psi(x,t) = A\,e^{-i(\omega t-kx)}\,. \qquad \text{(8.28)}$$

Entonces, debido a la irreducibilidad en $t$ y $x$ (que proviene de la invariancia bajo traslación), sabemos inmediatamente que tanto la fuerza como la derivada temporal de $\psi$ son proporcionales a $\psi$. Para una solución irreducible, todo es proporcional a $e^{-i(\omega t-kx)}$; así, son también proporcionales entre sí, y podemos definir la impedancia,

$$F = -Z(k)\,\frac{\partial}{\partial t}\psi(x,t) = i\omega A\,Z(k)\,e^{-i(\omega t-kx)}\,. \qquad \text{(8.29)}$$

Por ejemplo, para la cuerda con cuentas, si reemplazamos la solución real, (8.26), por la solución compleja irreducible, (8.28), la fuerza se convierte en

$$F_0 = \frac{TA}{a}\left(e^{-i(\omega t-ka)}-e^{-i\omega t}\right) = \frac{TA}{a}\left(e^{ika}-1\right)e^{-i\omega t}\,. \qquad \text{(8.30)}$$

Así, de (8.29), la impedancia, $Z(k)$, es

$$Z(k) = \frac{T}{\omega a}\,\frac{e^{ika}-1}{i} = \frac{2T}{a\omega}\,e^{ika/2}\sin\frac{ka}{2}\,. \qquad \text{(8.31)}$$

Usando la relación de dispersión, (5.39), podemos escribir esto como

$$Z(k) = e^{ika/2}\sqrt{\frac{mT}{a}}\,. \qquad \text{(8.32)}$$

La impedancia, $Z(k)$, definida por (8.29), es en general compleja y depende de $k$. Sin embargo, podemos encontrar la potencia media necesaria para producir la onda. Como la potencia es una función no lineal del desplazamiento, debemos tomar primero las partes reales de la velocidad y la fuerza complejas antes de calcular la potencia, como en (2.26). Para $A=|A|e^{i\varphi}$ compleja arbitraria,

$$v = \omega|A|\sin(\omega t-kx-\varphi)\,, \qquad \text{(8.33)}$$

$$F = (\text{Im}\,Z(k))\,\omega|A|\cos(\omega t-kx-\varphi) + (\text{Re}\,Z(k))\,\omega|A|\sin(\omega t-kx-\varphi)\,,$$

donde hemos puesto la fase de $A$ dentro de las funciones seno y coseno (véase (1.96)-(1.98)), para dejar claro que solo el valor absoluto de $A$ importa para la potencia media. Entonces, como en (2.26), solo el término en $\sin^2$ contribuye a la potencia promediada en el tiempo, que es

$$\frac{1}{2}(\text{Re}\,Z)\,\omega^2|A|^2\,. \qquad \text{(8.34)}$$

## 8.3 La luz

Las ondas de luz, como las ondas sonoras que discutimos en el capítulo anterior, son intrínsecamente tridimensionales. Sin embargo, como con el sonido, podemos decir mucho sobre la luz que es más o menos independiente de los detalles tridimensionales.

### 8.3.1 Ondas planas

Hay una forma simple de concentrarse en una sola dimensión: buscar soluciones en las que las otras dos dimensiones no intervengan en absoluto. Considere las ecuaciones de Maxwell en el vacío, en términos de los campos vectoriales $\vec E$ y $\vec B$ que describen los campos eléctrico y magnético:

$$\begin{aligned}
\frac{\partial E_y}{\partial x}-\frac{\partial E_x}{\partial y} &= -\frac{\partial B_z}{\partial t}\\
\frac{\partial E_z}{\partial y}-\frac{\partial E_y}{\partial z} &= -\frac{\partial B_x}{\partial t}\\
\frac{\partial E_x}{\partial z}-\frac{\partial E_z}{\partial x} &= -\frac{\partial B_y}{\partial t}
\end{aligned} \qquad \text{(8.35)}$$

$$\begin{aligned}
\frac{\partial B_y}{\partial x}-\frac{\partial B_x}{\partial y} &= \mu_0\epsilon_0\,\frac{\partial E_z}{\partial t}\\
\frac{\partial B_z}{\partial y}-\frac{\partial B_y}{\partial z} &= \mu_0\epsilon_0\,\frac{\partial E_x}{\partial t}\\
\frac{\partial B_x}{\partial z}-\frac{\partial B_z}{\partial x} &= \mu_0\epsilon_0\,\frac{\partial E_y}{\partial t}
\end{aligned} \qquad \text{(8.36)}$$

$$\frac{\partial E_x}{\partial x}+\frac{\partial E_y}{\partial y}+\frac{\partial E_z}{\partial z}=0\,,\qquad \frac{\partial B_x}{\partial x}+\frac{\partial B_y}{\partial y}+\frac{\partial B_z}{\partial z}=0 \qquad \text{(8.37)}$$

donde $\epsilon_0$ y $\mu_0$ son dos constantes llamadas la permitividad y la permeabilidad del espacio vacío (véase, por ejemplo, Purcell, capítulo 9). Busquemos soluciones de estas ecuaciones diferenciales parciales que involucren solo funciones de $z$ y $t$. En este caso, las cosas se simplifican a:

$$0=-\frac{\partial B_z}{\partial t}\,,\qquad -\frac{\partial E_y}{\partial z}=-\frac{\partial B_x}{\partial t}\,,\qquad \frac{\partial E_x}{\partial z}=-\frac{\partial B_y}{\partial t}\,, \qquad \text{(8.38)}$$

$$0=\mu_0\epsilon_0\,\frac{\partial E_z}{\partial t}\,,\qquad -\frac{\partial B_y}{\partial z}=\mu_0\epsilon_0\,\frac{\partial E_x}{\partial t}\,,\qquad \frac{\partial B_x}{\partial z}=\mu_0\epsilon_0\,\frac{\partial E_y}{\partial t}\,, \qquad \text{(8.39)}$$

$$\frac{\partial E_z}{\partial z}=0\,,\qquad \frac{\partial B_z}{\partial z}=0\,. \qquad \text{(8.40)}$$

Estas ecuaciones implican que $E_z$ y $B_z$ son independientes de $z$ y $t$. Como ya hemos supuesto que dependen solo de $z$ y $t$, esto significa que son constantes; las ignoraremos, porque nos interesan las soluciones con dependencia no trivial en $z$ y $t$. Eso deja las componentes $x$ e $y$, que satisfacen (8.38) y (8.39).

Entonces, como (8.38) y (8.39) son invariantes bajo traslaciones en $z$ y $t$, esperamos soluciones exponenciales complejas, en las que todas las componentes son proporcionales a

$$e^{i(\pm kz-\omega t)}\,, \qquad \text{(8.41)}$$

$$E_x(z,t) = \varepsilon_x^\pm\,e^{i(\pm kz-\omega t)}\,,\qquad E_y(z,t) = \varepsilon_y^\pm\,e^{i(\pm kz-\omega t)}\,, \qquad \text{(8.42)}$$

$$B_x(z,t) = \beta_x^\pm\,e^{i(\pm kz-\omega t)}\,,\qquad B_y(z,t) = \beta_y^\pm\,e^{i(\pm kz-\omega t)}\,. \qquad \text{(8.43)}$$

Sustituyendo directamente (8.42) y (8.43) en (8.38) y (8.39), obtenemos

$$\pm k\varepsilon_y^\pm = \omega\beta_x^\pm\,,\qquad \pm k\varepsilon_x^\pm = \omega\beta_y^\pm\,, \qquad \text{(8.44)}$$

$$\pm k\beta_y^\pm = -\mu_0\epsilon_0\omega\varepsilon_x^\pm\,,\qquad \pm k\beta_x^\pm = -\mu_0\epsilon_0\omega\varepsilon_y^\pm\,. \qquad \text{(8.45)}$$

Como de costumbre, hemos escrito la onda con la dependencia temporal irreducible, $e^{-i\omega t}$. Para obtener los campos eléctrico y magnético reales, tomamos la parte real de (8.42) y (8.43). Esto funciona porque las ecuaciones de Maxwell son lineales en los campos eléctrico y magnético. Las amplitudes, $\varepsilon_x^\pm$, etc., pueden ser complejas.

De (8.44) y (8.45), verá que $\varepsilon_y^\pm$ está relacionada con $\beta_x^\pm$, y $\varepsilon_x^\pm$ está relacionada con $\beta_y^\pm$. Para cada relación, hay dos ecuaciones lineales simultáneas homogéneas en las dos incógnitas. Son consistentes solo si el cociente de los coeficientes es el mismo, lo que implica una relación entre $k$ y $\omega$,

$$k^2 = \mu_0\epsilon_0\,\omega^2\,. \qquad \text{(8.46)}$$

Esta es una relación de dispersión,

$$\omega^2 = c^2k^2 = \frac{1}{\mu_0\epsilon_0}\,k^2\,. \qquad \text{(8.47)}$$

La velocidad de fase, $c$, es la velocidad de la luz en el vacío (tendremos más que decir sobre esto en los capítulos 10 y 11). Una vez satisfecha (8.47), podemos resolver para las $\beta^\pm$ en términos de las $\varepsilon^\pm$:

$$\beta_y^\pm = \pm\frac{1}{c}\varepsilon_x^\pm\,,\qquad \beta_x^\pm = \mp\frac{1}{c}\varepsilon_y^\pm\,. \qquad \text{(8.48)}$$

Estas soluciones de las ecuaciones de Maxwell en el vacío son ondas electromagnéticas, u ondas de luz. Estas soluciones simples, que dependen solo de $z$ y $t$, son un ejemplo de soluciones de onda plana. El nombre es apropiado porque los campos eléctrico y magnético de la onda tienen el mismo valor en todos los puntos de cada plano de $z$ constante, para cualquier instante $t$ fijo. Estos planos se propagan en la dirección $\pm z$ con la velocidad de fase $c$.

En general, las ondas electromagnéticas pueden propagarse en cualquier dirección del espacio tridimensional. Sin embargo, los campos eléctrico y magnético que forman la onda son siempre perpendiculares a la dirección en la que viaja la onda, y perpendiculares entre sí.

El tratamiento de las ondas planas electromagnéticas que viajan en la dirección $z$ es análogo a nuestro tratamiento del sonido en el capítulo 7. Allí también la onda dependía solo de $z$. Sin embargo, las ondas electromagnéticas son un poco más complicadas, porque el fenómeno ondulatorio depende tanto del campo eléctrico como del magnético. La razón por la que hemos pospuesto hasta ahora la discusión de las ondas electromagnéticas, a pesar de que son uno de los ejemplos más importantes de fenómenos ondulatorios, es que las relaciones (8.48) entre los campos eléctrico y magnético dependen de la dirección en la que viaja la onda (¡el signo $\pm$!). Es mucho más fácil escribir las soluciones de las ondas viajeras que las de las ondas estacionarias. Incluso para las simples ondas planas viajeras que hemos descrito, que dependen solo de $z$ y $t$, esta relación entre $\vec E$ y $\vec B$, y la dirección de la onda, depende de las propiedades tridimensionales de las ecuaciones de Maxwell. Discutiremos estos temas con mucho más detalle en los capítulos 11 y 12.

### 8.3.2 Interferómetros

Una de las maravillosas características de las ondas de luz es que es relativamente fácil dividirlas y recombinarlas. Esta característica se usa en muchos dispositivos ópticos, uno de los más simples de los cuales es un «interferómetro», una versión del cual (el interferómetro de Michelson) se muestra esquemáticamente en la figura 8.8. Una fuente produce una onda plana (como discutiremos en el capítulo 13, no puede ser exactamente una onda plana, pero no importa por ahora). El espejo semiplateado sirve como «divisor de haz», dejando pasar parte de la luz mientras refleja el resto. Luego los espejos de arriba y de la derecha reflejan los haces de vuelta. Entonces el espejo semiplateado sirve como «recombinador de haz», combinando los haces de arriba y de la derecha en un único haz que continúa hacia la pantalla detectora, donde se mide la intensidad del haz (proporcional al cuadrado del campo eléctrico). Lo importante es que la onda de luz que llega a la pantalla detectora es la suma de dos componentes que son coherentes y que sin embargo han recorrido caminos distintos. Lo que significa «coherente» en este contexto no es solo que la frecuencia sea la misma, sino que la fase de las ondas esté correlacionada. En este caso, eso ocurre simplemente porque las dos componentes que llegan a la pantalla provienen de la misma onda plana incidente.

![Figura 8.8](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh8_ES/fig8.8.png)

Figura 8.8: diagrama esquemático de un interferómetro de Michelson, con una fuente, un espejo semiplateado que divide el haz hacia dos espejos perpendiculares, y una pantalla detectora donde se recombinan los dos haces reflejados.

Ahora bien, la intensidad de la luz que llega a la pantalla depende de la longitud relativa de los dos caminos. Longitudes de camino distintas producirán fases distintas. Si las dos componentes están en fase, las amplitudes se suman y la pantalla se ve brillante: esto se llama «interferencia constructiva». Si las dos componentes están desfasadas $180°$, las amplitudes se restan y la pantalla se ve oscura: hay lo que se llama «interferencia destructiva».

Esto suena bastante trivial, y de hecho lo es (al menos para las ondas electromagnéticas clásicas), pero también es extremadamente útil, porque proporciona una medida muy sensible de los cambios en la longitud de los caminos. En particular, si uno de los espejos se mueve una distancia $d$ (podría ser parte de un montaje experimental diseñado para detectar pequeños movimientos, por ejemplo), la fase relativa de las dos componentes que llegan a la pantalla cambia en $2kd$, donde $k$ es el número de onda angular de la onda plana, porque la longitud del camino de la onda reflejada ha cambiado en $2d$. Así, cada vez que $d$ cambia en un cuarto de la longitud de onda de la luz, la pantalla pasa de brillante a oscura, o viceversa.

Esta es una manera muy útil de medir pequeños cambios de distancia. En la práctica, el haz incidente no es exactamente una onda plana (eso, como veremos en detalle más adelante, ¡requeriría un experimento infinito!), así que la intensidad de la luz no es uniforme sobre la pantalla. En su lugar, hay zonas claras y oscuras conocidas como «franjas». A medida que se mueve el espejo, las franjas se desplazan, y se pueden contar las franjas que pasan por un punto dado para llevar la cuenta del número de cambios de brillante a oscuro.

### 8.3.3 Interferencia cuántica

Hay otra forma de pensar en el interferómetro que lo hace parecer mucho menos trivial. Como discutiremos varias veces en este libro, y aprenderá con más detalle cuando estudie mecánica cuántica, la luz no es solo una onda: también está formada por partículas individuales de luz llamadas fotones. No lo nota a menos que baje mucho la intensidad de la onda de luz. Pero, de hecho, puede bajar tanto la intensidad que puede detectar fotones individuales llegando a la pantalla. Ahora ya no está tan claro qué está ocurriendo. Un fotón individual no puede dividirse en dos partes en el divisor y el recombinador de haz. Como veremos más adelante, la energía del fotón está determinada por la frecuencia de la luz; no puede dividirse. Podría pensar, por tanto, que el fotón individual tendría que ir por un camino o por el otro. Pero entonces, ¿cómo puede haber interferencia entre los dos caminos? No hay respuesta a esta pregunta que tenga «sentido» en la física clásica de partículas. Sin embargo, cuando se hace el experimento, el número de fotones que llegan a la pantalla depende de la diferencia de longitudes entre los dos caminos exactamente como se esperaría por la descripción ondulatoria. La probabilidad de que un fotón golpee un punto dado de la pantalla es proporcional a la intensidad de la onda clásica correspondiente. Si las longitudes de los caminos producen interferencia destructiva, no pasan fotones. Y no solo eso: experimentos similares pueden hacerse con otras partículas, ¡como los neutrones! Quizá la interferencia no sea tan trivial después de todo.

## 8.4 Líneas de transmisión

Hemos visto que un sistema invariante bajo traslación de inductores y condensadores puede transportar ondas. Preguntémonos qué ocurre cuando tomamos el límite continuo de tal sistema; esto dará una visión interesante de las ondas electromagnéticas. La relación de dispersión del sistema de la figura 5.23 viene dada por (5.75),

$$\omega^2 = \frac{4}{L_aC_a}\sin^2\frac{ka}{2}\,. \qquad \text{(8.49)}$$

donde $L_a$ y $C_a$ son la inductancia y la capacitancia de los inductores y condensadores del sistema, con separación $a$ entre partes vecinas. Para tomar el límite continuo, debemos reemplazar la inductancia y la capacitancia, $L_a$ y $C_a$, por cantidades que esperamos tengan límites finitos cuando $a\to0$. Esperamos, por la analogía (5.69) entre circuitos LC y sistemas de muelles y masas, y por la discusión al principio del capítulo 7 sobre el límite continuo del sistema de masas y muelles, que las cantidades relevantes sean:

$$\begin{aligned}
&\frac{L_a}{a} \to \text{inductancia por unidad de longitud}\\
&K_aa \to \frac{a}{C_a} \to \text{recíproco de la capacitancia por unidad de longitud}
\end{aligned} \qquad \text{(8.50)}$$

Estas dos cantidades pueden calcularse directamente a partir de la inductancia y la capacitancia de una longitud finita, $\ell$, del sistema que contiene muchas unidades individuales. Los inductores están conectados en serie, así que las inductancias individuales se suman para dar la inductancia total. Así, si la longitud $\ell$ es $na$, de modo que el sistema finito contiene $n$ inductores, la inductancia total es $L=nL_a$. Entonces

$$\frac{L}{\ell} = \frac{L_a}{a}\,. \qquad \text{(8.51)}$$

Las capacitancias funcionan de la misma manera porque están conectadas en paralelo, y las capacitancias en paralelo se suman. Así,

$$\frac{C}{\ell} = \frac{C_a}{a}\,. \qquad \text{(8.52)}$$

Por tanto, al tomar el límite $a\to0$ de (8.49), podemos escribir

$$L_a = a\,\frac{L}{\ell}\,,\qquad C_a = a\,\frac{C}{\ell}\,. \qquad \text{(8.53)}$$

Esto da la siguiente relación de dispersión:

$$\omega^2 = \frac{\ell^2}{LC}\,\frac{4\sin^2\frac{ka}{2}}{a^2} \to \frac{\ell^2}{LC}\,k^2\,. \qquad \text{(8.54)}$$

Un sistema continuo como este, con inductancia y capacitancia fijas por unidad de longitud, se llama línea de transmisión. Llamaremos a (8.54) la relación de dispersión de una línea de transmisión sin resistencia. Una línea de transmisión puede usarse para enviar ondas eléctricas, igual que una cuerda continua transmite ondas mecánicas. En el sistema continuo, la variable de desplazamiento, la carga desplazada, se convierte en una función de la posición a lo largo de la línea de transmisión. Si la línea de transmisión se extiende en la dirección $z$, podemos describir las cargas de la línea mediante una función $Q(z,t)$, que es la carga que se ha desplazado a través del punto $z$ de la línea en el instante $t$. La derivada temporal de $Q(z,t)$ es la corriente en el punto $z$ e instante $t$:

$$I(z,t) = \frac{\partial Q(z,t)}{\partial t}\,. \qquad \text{(8.55)}$$

### 8.4.1 Línea de transmisión de placas paralelas

Vale la pena trabajar un ejemplo concreto de línea de transmisión. El ejemplo que usaremos es el de dos largas tiras conductoras paralelas. Imagine un sistema infinito en el que las tiras se extienden paralelas entre sí en planos de $y$ constante, hacia el infinito en la dirección $z$. Suponga que las tiras son suficientemente delgadas como para despreciar su grosor. Suponga además que la anchura de las tiras, $w$, es mucho mayor que la separación, $s$. Una sección transversal de esta línea de transmisión en el plano $x$-$y$ se muestra en la figura 8.9. En la figura, la dirección $z$ sale del plano del papel, hacia usted. Seguiremos el movimiento de las cargas en el conductor superior, y supondremos que el conductor inferior está conectado a tierra (con voltaje fijo en $V=0$).

![Figura 8.9](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh8_ES/fig8.9.png)

Figura 8.9: sección transversal de la línea de transmisión de placas paralelas, mostrando dos tiras conductoras de anchura $w$ separadas verticalmente una distancia $s$.

Encontraremos la relación de dispersión de la línea de transmisión calculando la capacitancia y la inductancia de un tramo de la línea de longitud $\ell$. Será útil hacerlo usando consideraciones de energía. Suponga que hay una carga, $Q$, distribuida uniformemente sobre la placa superior del condensador, y una corriente, $I$, fluyendo uniformemente hacia afuera del plano $x$-$y$, en la dirección $z$, a lo largo del conductor superior (y de vuelta hacia el plano a lo largo del conductor inferior). La energía almacenada en la longitud $\ell$ de la línea de transmisión es entonces

$$\frac{1}{2C}Q^2 + \frac{1}{2}LI^2\,, \qquad \text{(8.56)}$$

donde $C$ y $L$ son la capacitancia y la inductancia (véase, por ejemplo, Halliday y Resnick, parte 2).

La energía en realidad se almacena en los campos eléctrico y magnético producidos por la carga y la corriente. En esta configuración, los campos eléctrico y magnético están casi enteramente entre las dos placas del tramo de línea de transmisión. Si $Q$ e $I$ son positivos, los campos eléctrico y magnético son como se muestra en las figuras 8.10 y 8.11. En la figura 8.10, la línea punteada es la sección transversal de una región en forma de caja que puede usarse para calcular el campo eléctrico, usando la ley de Gauss. En la figura 8.11, el camino punteado puede usarse para calcular el campo magnético, usando la ley de Ampère. Los campos eléctrico y magnético son aproximadamente constantes entre las tiras, pero caen rápidamente a casi cero fuera de ellas.

![Figura 8.11](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh8_ES/fig8.11.png)

Figura 8.11

![Figura 8.10](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh8_ES/fig8.10.png)

Figura 8.10: el campo eléctrico producido por la carga en la línea de transmisión, apuntando de la placa superior a la inferior, con una región gaussiana en forma de caja para aplicar la ley de Gauss. Figura 8.11: el campo magnético producido por la corriente, apuntando horizontalmente entre las placas, con un camino amperiano rectangular para aplicar la ley de Ampère.

La densidad de carga en la placa superior es aproximadamente uniforme y viene dada por la carga total dividida entre el área, $w\ell$,

$$\sigma \approx \frac{Q}{w\ell}\,. \qquad \text{(8.57)}$$

Entonces podemos aplicar la ley de Gauss a una pequeña región en forma de caja, cuya sección transversal se muestra en la figura 8.10, y concluir que el campo eléctrico en el interior viene dado por

$$E_y \approx -\frac{Q}{\epsilon_0w\ell} \qquad \text{(8.58)}$$

La densidad de energía almacenada en el campo eléctrico entre las placas es, por tanto,

$$u_E = \frac{\epsilon_0}{2}E^2 \approx \frac{Q^2}{2\epsilon_0w^2\ell^2}\,. \qquad \text{(8.59)}$$

La energía total almacenada en el campo eléctrico se obtiene entonces multiplicando $u_E$ por el volumen entre las placas, dando

$$\frac{1}{2}\,\frac{s}{\epsilon_0w\ell}\,Q^2 \qquad \text{(8.60)}$$

así, comparando con (8.56),

$$C = \frac{\epsilon_0w\ell}{s}\,. \qquad \text{(8.61)}$$

Podemos calcular la inductancia de forma similar. La ley de Ampère, aplicada a un camino que rodea el conductor superior (como se muestra en la figura 8.11), da

$$B_x \approx \frac{\mu_0I}{w}\,. \qquad \text{(8.62)}$$

La densidad de energía almacenada en el campo magnético entre las placas es, por tanto,

$$u_B = \frac{1}{2\mu_0}B^2 \approx \frac{\mu_0I^2}{2w^2}\,. \qquad \text{(8.63)}$$

La energía total almacenada en el campo magnético se obtiene entonces multiplicando $u_B$ por el volumen entre las placas, dando

$$\frac{1}{2}\,\frac{\mu_0s\ell}{w}\,I^2 \qquad \text{(8.64)}$$

así, comparando con (8.56),

$$L = \frac{\mu_0s\ell}{w}\,. \qquad \text{(8.65)}$$

Ahora podemos sustituir (8.61) y (8.65) en (8.54), para obtener la relación de dispersión de esta línea de transmisión:

$$\omega^2 = \frac{1}{\mu_0\epsilon_0}\,k^2 = c^2k^2\,, \qquad \text{(8.66)}$$

¡donde $c$ es la velocidad de la luz!

### 8.4.2 Ondas en la línea de transmisión

La relación de dispersión, (8.66), se parece sospechosamente a la relación de dispersión de las ondas electromagnéticas. De hecho, los campos eléctrico y magnético entre las tiras de la línea de transmisión tienen exactamente la forma de una onda electromagnética. Para verlo explícitamente, consideremos una onda viajera en la línea de transmisión, y la carga, $Q(z,t)$, desplazada a través de $z$, con la dependencia exponencial compleja irreducible en $z$ y $t$,

$$Q(z,t) = q\,e^{i(kz-\omega t)}\,. \qquad \text{(8.67)}$$

Esta onda viaja en la dirección $z$ positiva, alejándose hacia usted en el diagrama de la figura 8.9.

En cualquier instante fijo $t$ y posición $z$, los campos eléctrico y magnético dentro de la línea de transmisión se ven como en las figuras 8.10 y 8.11 (o ambos pueden apuntar en la dirección opuesta). Podemos encontrar el campo magnético igual que hicimos arriba, porque la corriente en cualquier punto de la línea viene dada por (8.55), así que

$$B_x(z,t) \approx \frac{\mu_0I(z,t)}{w} = \frac{\mu_0}{w}\,\frac{\partial}{\partial t}Q(z,t) = -i\,\frac{\mu_0\omega q}{w}\,e^{i(kz-\omega t)}\,. \qquad \text{(8.68)}$$

Para encontrar el campo eléctrico como función de $z$ y $t$, necesitamos la densidad de carga a lo largo de la línea. Una vez que la tenemos, podemos encontrar el campo eléctrico usando la ley de Gauss, como arriba. Resulta una densidad de carga no nula si la cantidad de carga desplazada cambia en función de $z$. Es más fácil encontrar la densidad de carga volviendo al sistema discreto discutido en el capítulo 5, y a (5.72). En el lenguaje en el que etiquetamos las partes del sistema por sus posiciones, la carga $q_j$ del sistema discreto se convierte en $q(z,t)$, donde $z=ja$. Cuando $a\to0$, esto corresponde a una densidad de carga lineal a lo largo de la línea de transmisión de

$$\rho(z,t) = \frac{q(z,t)}{a}\,. \qquad \text{(8.69)}$$

En este lenguaje, (5.72) se convierte en

$$q(z,t) = Q(z,t) - Q(z+a,t)\,, \qquad \text{(8.70)}$$

donde $Q(z,t)$ es la carga desplazada a través del inductor en la posición $z$ en el instante $t$. Combinando (8.69) y (8.70) da

$$\rho(z,t) = \frac{Q(z,t)-Q(z+a,t)}{a}\,. \qquad \text{(8.71)}$$

Tomando el límite cuando $a\to0$, da

$$\rho(z,t) = -\frac{\partial}{\partial z}Q(z,t) = -ikq\,e^{i(kz-\omega t)}\,. \qquad \text{(8.72)}$$

Esta densidad de carga lineal se distribuye sobre la anchura de la tira superior de la línea de transmisión, dando una densidad de carga superficial de

$$\sigma(z,t) = \frac{\rho(z,t)}{w} = -i\,\frac{kq}{w}\,e^{i(kz-\omega t)}\,. \qquad \text{(8.73)}$$

Ahora el campo eléctrico, por la ley de Gauss, es

$$E_y = -\frac{\sigma(z,t)}{\epsilon_0} = i\,\frac{kq}{\epsilon_0w}\,e^{i(kz-\omega t)}\,. \qquad \text{(8.74)}$$

Comparando (8.68) con (8.74), puede ver que se satisface (8.45), de modo que este par de campos eléctrico y magnético forma parte de una onda plana electromagnética viajera.

Lo que ocurre aquí es que el papel de las cargas y corrientes en las tiras de la línea de transmisión es confinar las ondas electromagnéticas. Sin los conductores, sería imposible producir un fragmento de onda plana, como veremos con mucho más detalle en el capítulo 13.

Mientras tanto, note que el modo con $\omega=0$ y $k=0$ debe tratarse con cuidado, igual que el modo $\omega=k=0$ de la cuerda con cuentas discutido en el capítulo 5. El modo en el que la carga desplazada es proporcional a $z$ (véase (5.41)) describe una situación en la que toda la línea de transmisión infinita está cargada; esto no es muy interesante en el caso finito. Sin embargo, el modo independiente de $z$ pero creciente con el tiempo, proporcional a $t$, sí es importante: describe la situación en la que fluye una corriente constante por los conductores. Dentro de la línea de transmisión, en este caso, hay un campo magnético constante.

## 8.5 Amortiguamiento

Es instructivo, llegados a este punto, considerar las ondas en sistemas con fuerzas de fricción. Hemos pospuesto esto hasta ahora porque será más fácil entender qué ocurre en sistemas con amortiguamiento ahora que hemos discutido las ondas viajeras.

La observación clave es que, en un sistema invariante bajo traslación, incluso en presencia de amortiguamiento, los modos normales del sistema infinito son exactamente los mismos que sin amortiguamiento, porque siguen estando determinados por la invariancia bajo traslación. Los modos normales siguen siendo de la forma $e^{\pm ikx}$, caracterizados por el número de onda angular $k$. Solo la relación de dispersión es distinta. Para ver esto en detalle, recapitulemos los argumentos del capítulo 5.

La relación de dispersión de un sistema sin amortiguamiento se determina por la solución de la ecuación de autovalores

$$\left[-\omega^2+M^{-1}K\right]A^k = 0\,, \qquad \text{(8.75)}$$

donde $A^k$ es el modo normal con número de onda $k$,

$$A_j^k \propto e^{ijka}\,, \qquad \text{(8.76)}$$

con dependencia temporal $e^{-i\omega t}$ (en presencia de amortiguamiento, el signo de $i$ importa: las relaciones de abajo tendrían otro aspecto si hubiéramos usado $e^{i\omega t}$, y no podríamos usar $\cos\omega t$ o $\sin\omega t$). Ya sabemos que $A^k$ es un modo normal, por la invariancia bajo traslación; esto implica que es un autovector de $M^{-1}K$. El autovalor es cierta función de $k$; la llamaremos $\omega_0^2(k)$, de modo que

$$M^{-1}K\,A^k = \omega_0^2(k)\,A^k\,. \qquad \text{(8.77)}$$

Esta función $\omega_0^2(k)$ determina la relación de dispersión del sistema sin amortiguamiento, porque la ecuación de autovalores, (8.75), implica ahora

$$\omega^2 = \omega_0^2(k)\,. \qquad \text{(8.78)}$$

Ahora podemos modificar la discusión anterior para incluir el amortiguamiento en el sistema infinito invariante bajo traslación. En presencia de amortiguamiento, la ecuación de movimiento tiene la forma

$$M\,\frac{d^2}{dt^2}\psi(t) = -M\gamma\,\frac{d}{dt}\psi(t) - K\psi(t)\,, \qquad \text{(8.79)}$$

donde $M\gamma$ es la matriz que describe el amortiguamiento dependiente de la velocidad. Entonces, para un modo normal,

$$\psi(t) = A^k\,e^{-i\omega t}\,, \qquad \text{(8.80)}$$

la ecuación de autovalores ahora se ve así:

$$\left[-\omega^2-i\gamma\omega+M^{-1}K\right]A^k = 0\,. \qquad \text{(8.81)}$$

Ahora, igual que en (8.77) arriba, por la invariancia bajo traslación sabemos que $A^k$ es un autovector tanto de $M^{-1}K$ como de $\gamma$,

$$M^{-1}K\,A^k = \omega_0^2(k)\,A^k\,,\qquad \gamma\,A^k = \gamma(k)\,A^k\,. \qquad \text{(8.82)}$$

Entonces, como arriba, la ecuación de autovalores se convierte en la relación de dispersión

$$\omega^2 = \omega_0^2(k) - i\gamma(k)\omega\,. \qquad \text{(8.83)}$$

Para todo $k$, $\gamma(k)\ge0$, porque, como veremos en (8.84) más abajo, la fuerza es una fuerza de fricción. Si $\gamma(k)$ fuera negativo para algún $k$, la fuerza «friccional» estaría inyectando energía al sistema en vez de amortiguarlo. Note también que si $\gamma=\gamma I$, entonces $\gamma(k)=\gamma$, independiente de $k$. Sin embargo, en general, el amortiguamiento dependerá de $k$: modos con distinto $k$ pueden amortiguarse de forma diferente.

En (8.83) vemos la característica nueva de los sistemas invariantes bajo traslación con amortiguamiento: la única diferencia es que la relación de dispersión se vuelve compleja. Tanto $\omega_0^2(k)$ como $\gamma(k)$ son reales para $k$ real. Debido a la $i$ explícita en (8.83), o bien $\omega$ o bien $k$ (o ambos) deben ser complejos para satisfacer la ecuación de movimiento.

### 8.5.1 Oscilaciones libres

Para las oscilaciones libres, los números de onda angulares, $k$, de los modos permitidos quedan determinados por las condiciones de contorno. Típicamente, los valores permitidos de $k$ son reales y $\omega_0^2(k)$ es positivo (correspondiendo a un equilibrio estable en ausencia de amortiguamiento). Entonces los modos de oscilación libre son análogos a las oscilaciones libres de un oscilador amortiguado discutidas en el capítulo 2. De hecho, si sustituimos $\alpha\to-i\omega$ y $\gamma\to\gamma(k)$ en (2.5), obtenemos precisamente (8.83). Así, podemos retomar la solución de (2.6),

$$-i\omega = -\frac{\gamma(k)}{2} \pm \sqrt{\frac{\gamma(k)^2}{4}-\omega_0^2(k)}\,. \qquad \text{(8.84)}$$

Esto describe una solución que se extingue exponencialmente con el tiempo. Que oscile o se extinga suavemente depende del cociente entre $\gamma(k)$ y $\omega_0(k)$, como se discutió en el capítulo 2.

### 8.5.2 Oscilación forzada

*(Referencia a los programas interactivos 8-3 a 8-5 del disco de programas del curso original.)*

Consideremos ahora una oscilación forzada, en la que impulsamos un extremo de un sistema invariante bajo traslación con frecuencia angular $\omega$. Después de que las oscilaciones libres se hayan extinguido, quedamos con una oscilación a la única frecuencia angular real, $\omega$. Como siempre, en los problemas de oscilación forzada, pensamos en el desplazamiento real del extremo del sistema como la parte real de un desplazamiento complejo proporcional a $e^{-i\omega t}$. Entonces se aplica la relación de dispersión, (8.83). Ahora la relación de dispersión determina $k$, y $k$ debe ser complejo.

Puede haber notado que ninguna de las relaciones de dispersión que hemos estudiado hasta ahora dependen del signo de $k$. Esto no es casualidad. La razón es que todos los sistemas que hemos estudiado tienen la propiedad de simetría de reflexión: podríamos cambiar $x\to-x$ sin afectar la física. De hecho, un sistema invariante bajo traslación que no tuviera esta simetría sería un poco peculiar. Mientras el sistema sea invariante bajo reflexiones, $x\to-x$, la relación de dispersión no puede depender del signo de $k$. La razón es que, cuando $x\to-x$, el modo $e^{ikx}$ se convierte en $e^{-ikx}$. Si $x\to-x$ es una simetría, estos dos modos con números de onda angulares $k$ y $-k$ deben ser físicamente equivalentes, y por tanto deben tener la misma frecuencia. Así, las dos soluciones para $\omega$ fijo deben tener la forma:

$$k = \pm(k_r+ik_i) \qquad \text{(8.85)}$$

Debido al signo $\pm$, podemos elegir $k_r>0$ en (8.85).

En sistemas con fuerzas de fricción, siempre encontramos

$$k_i \ge 0 \quad\text{para } k_r>0\,. \qquad \text{(8.86)}$$

La razón de esto es fácil de ver si considera las ondas viajeras, que tienen la forma

$$e^{-i\omega t}e^{\pm i(k_r+ik_i)x} \qquad \text{(8.87)}$$

o

$$e^{i(\pm k_rx-\omega t)}e^{\mp k_ix}\,. \qquad \text{(8.88)}$$

De (8.88) debería ser evidente qué ocurre. Cuando el signo $\pm$ es $+$, la onda va en la dirección $+x$, así que el signo de la exponencial real es tal que la amplitud de la onda disminuye a medida que $x$ aumenta: ¡la onda se va apagando a medida que viaja! Esto es lo que debe ocurrir con una fuerza friccional. El otro signo requeriría una fuente de energía en el medio, de modo que la amplitud de la onda crecería exponencialmente al viajar. Un fragmento de una onda viajera amortiguada infinita se anima en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-3" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-3</a>.

La forma (8.88) tiene algunas consecuencias interesantes para los problemas de oscilación forzada en presencia de amortiguamiento. En sistemas discretos amortiguados, incluso en un modo normal, las partes del sistema no oscilan todas en fase. En sistemas continuos amortiguados, la distinción entre ondas viajeras y ondas estacionarias se difumina.

Considere un problema de oscilación forzada para la oscilación transversal de una cuerda con un extremo, en $x=0$, fijo, y el otro extremo, $x=L$, impulsado a frecuencia $\omega$. No importará hasta el final de nuestro análisis si la cuerda es continua o tiene cuentas con separación $a$ tal que $na=L$ para $n$ entero. Las condiciones de contorno son

$$\psi(L,t)=A\cos\omega t\,,\qquad \psi(0,t)=0\,. \qquad \text{(8.89)}$$

Como de costumbre, consideramos $\psi(x,t)$ como la parte real de un desplazamiento complejo, $\tilde\psi(x,t)$, que satisface

$$\tilde\psi(L,t)=Ae^{-i\omega t}\,,\qquad \tilde\psi(0,t)=0\,. \qquad \text{(8.90)}$$

Si $k$, para la frecuencia angular dada $\omega$, viene dado por (8.85), entonces los modos relevantes del sistema infinito son los de (8.87), y debemos encontrar una combinación lineal de estos dos que satisfaga (8.89). La respuesta es

$$\tilde\psi(x,t) = A\left[\frac{e^{i(k_r+ik_i)x}-e^{-i(k_r+ik_i)x}}{e^{i(k_r+ik_i)L}-e^{-i(k_r+ik_i)L}}\right]e^{-i\omega t}\,. \qquad \text{(8.91)}$$

El factor entre corchetes está construido para anularse en $x=0$ y valer 1 en $x=L$.

Para una cuerda continua, la solución (8.91) se anima en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-4" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-4</a>. Lo interesante de esto es que, cerca del extremo $x=L$, la solución se parece a una onda viajera. La razón es que ahí los factores exponenciales reales de (8.91) refuerzan la onda que se mueve hacia la izquierda y suprimen la que se mueve hacia la derecha, de modo que la solución es casi exactamente una onda viajera moviéndose hacia la izquierda. Por otro lado, cerca de $x=0$, los factores exponenciales reales son comparables, y la solución es casi exactamente una onda estacionaria. Discutiremos el comportamiento más complicado del medio en el próximo capítulo.

La misma solución funciona para una cuerda con cuentas (aunque la relación de dispersión será distinta). Un ejemplo se muestra en la animación del programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-5" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-5</a>. Ahí puede ver muy claramente que las partes del sistema no están todas en fase.

## 8.6 Cortes de frecuencia altos y bajos

### 8.6.1 Más sobre péndulos acoplados

*(Referencia al programa interactivo 8-6 del disco de programas del curso original.)*

En la sección anterior, vimos cómo el número de onda angular, $k$, puede volverse complejo en un sistema con fricción. Hay otra forma importante en la que $k$ puede volverse complejo. Considere la relación de dispersión del sistema de péndulos acoplados, (5.35), que podemos reescribir así:

$$\omega^2 = \omega_\ell^2 + \omega_c^2\sin^2\frac{ka}{2}\,. \qquad \text{(8.92)}$$

Aquí $a$ es la distancia entre bloques, $\omega_\ell$ es la frecuencia de un único péndulo no acoplado, y $\omega_c^2$ es una frecuencia asociada al acoplamiento entre bloques vecinos,

$$\omega_c^2 = \frac{4K}{m} \qquad \text{(8.93)}$$

donde $m$ es la masa de un bloque y $K$ es la constante de los muelles de acoplamiento.

Las ondas viajeras en un sistema con una relación de dispersión como (8.92) se animan en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-6" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-6</a>. Para hacer la física más fácil de ver, este sistema es una cuerda con cuentas con oscilaciones transversales. Sin embargo, para producir el término $\omega_\ell^2$ de (8.92), también hemos unido cada cuenta mediante un muelle a una posición de equilibrio a lo largo de la línea punteada. En este caso, el acoplamiento entre cuentas proviene de la cuerda, así que el análogo de (8.93) es

$$\omega_c^2 = \frac{4T}{ma}\,. \qquad \text{(8.94)}$$

Los parámetros del sistema se eligen de modo que, en términos de una frecuencia de referencia, $\omega_0$,

$$\omega_\ell^2 = 25\omega_0^2\,,\qquad \omega_c^2 = 24\omega_0^2\,. \qquad \text{(8.95)}$$

Las propiedades de las ondas en este sistema difieren dramáticamente en función de $\omega$. Una forma de verlo es ir hacia atrás y notar que, para $k$ real, como $\sin^2(ka/2)$ debe estar entre 0 y 1, $\omega$ está restringida,

$$\omega_\ell \le \omega \le \sqrt{\omega_\ell^2+\omega_c^2} \equiv \omega_h\,. \qquad \text{(8.96)}$$

Para $k$ en esta región «permitida»,

$$\sin^2\frac{ka}{2} = \frac{\omega^2-\omega_\ell^2}{\omega_c^2} \qquad \text{(8.97)}$$

está entre 0 y 1, al igual que

$$\cos^2\frac{ka}{2} = \frac{\omega_h^2-\omega^2}{\omega_c^2}\,. \qquad \text{(8.98)}$$

Las dos frecuencias, $\omega_\ell$ y $\omega_h$, se llaman cortes de frecuencia baja y alta. El sistema de péndulos acoplados solo admite ondas viajeras para frecuencias $\omega$ entre los cortes de frecuencia alta y baja. Es solo en esta región donde la relación de dispersión puede satisfacerse con $\omega$ y $k$ reales. Para $\omega<\omega_\ell$ o $\omega>\omega_h$, el sistema oscila, pero no hay nada parecido a una onda viajera. Puede verlo en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-6" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-6</a>, cambiando la frecuencia hacia arriba y hacia abajo con las teclas de flecha.

Para cualquier $\omega$, siempre podemos resolver la relación de dispersión. Sin embargo, en algunas regiones de frecuencia, el resultado será complejo, como en (8.85). Esperamos $k_i=0$ en la región permitida, (8.96). La solución de (8.92) para $k_r$ y $k_i$ en función de $\omega$ se muestra en las gráficas de la figura 8.12. Aquí, $k_r$ y $k_i$ se representan frente a $\omega$ para la relación de dispersión, (8.92), con $\omega_\ell=5\omega_0$ y $\omega_h=7\omega_0$. $k_i$ es la línea punteada. Note la dependencia muy rápida de $k_i$ cerca de los cortes de frecuencia alta y baja.

![Figura 8.12](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh8_ES/fig8.12.png)

Figura 8.12: $k_ra$ y $k_ia$ en función de $\omega$; en la región permitida entre $\omega_\ell$ y $\omega_h$, $k_r$ crece suavemente de $0$ a $\pi/a$ mientras $k_i=0$; fuera de esa región, $k_i$ crece rápidamente desde cero mientras $k_r$ permanece en $0$ o $\pi/a$.

A medida que $\omega$ disminuye, en la región permitida (8.96), $\sin(ka/2)$ disminuye. En el corte de frecuencia baja, $\omega=\omega_\ell$, $\sin(ka/2)$, y por tanto $k$, tiende a cero. Esto significa que, a medida que la frecuencia disminuye, la longitud de onda de las ondas viajeras se hace cada vez más larga, hasta que, en la frecuencia de corte, se vuelve infinita. En el corte de frecuencia baja, cada péndulo de la cadena infinita oscila en fase. Los muelles que los acoplan son entonces irrelevantes, porque siempre mantienen sus longitudes de equilibrio. Esto es posible precisamente porque $\omega_\ell$ es la frecuencia de oscilación del péndulo no acoplado, así que no se necesita acoplamiento para que un péndulo individual oscile a frecuencia $\omega_\ell$.

Si $\omega$ está por debajo del corte de frecuencia baja, $\omega_\ell$, $\sin^2(ka/2)$ debe volverse negativo para satisfacer la relación de dispersión, (8.92). Por tanto, $\sin(ka/2)$ debe ser un número puramente imaginario,

$$k = \pm ik_i\,. \qquad \text{(8.99)}$$

La solución general para la onda es entonces

$$\psi(x,t) = A\,e^{-k_ix}e^{-i\omega t} + B\,e^{k_ix}e^{-i\omega t}\,. \qquad \text{(8.100)}$$

En un sistema finito de péndulos acoplados, ambos términos pueden estar presentes. En un sistema semiinfinito impulsado en $x=0$ y que se extiende hasta $x\to\infty$, la constante $B$ debe anularse, para evitar un crecimiento exponencial de la onda en el infinito. Así, la onda cae exponencialmente para $x$ grande. Además, la solución es un producto de una función real de $x$ y una función exponencial compleja de $t$: esto es una onda estacionaria. No hay onda viajera. Puede verlo en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-6" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-6</a> a bajas frecuencias.

La física de esta oscilación por debajo del corte de frecuencia baja es particularmente clara en el límite extremo, $\omega\to0$. A frecuencia cero, no hay movimiento. El análogo de un problema de oscilación forzada es simplemente desplazar un péndulo respecto al equilibrio y observar qué le ocurre al resto. Claramente, lo que ocurre es que el desplazamiento del primer péndulo produce una fuerza sobre el siguiente, debida al muelle de acoplamiento, que lo aleja del equilibrio, pero no tanto como al primero. Su desplazamiento es menor que el del primero por cierto factor $\epsilon=e^{-k_ia}$. Entonces el segundo péndulo tira del tercero, pero de nuevo el desplazamiento es menor por el mismo factor. ¡Y así sucesivamente! En un sistema infinito, esto da lugar al desplazamiento exponencialmente decreciente de (8.100), con $B=0$. A medida que la frecuencia aumenta, el efecto de la inercia (más precisamente, el término $ma$ en $F=ma$) aumenta el desplazamiento del segundo bloque (y de cada uno de los siguientes), hasta que, por encima del corte de frecuencia baja, el efecto de la inercia es lo bastante grande como para competir en pie de igualdad con el efecto de la fuerza restauradora, y puede producirse una verdadera onda viajera.

El corte de frecuencia baja no es peculiar del sistema discreto: ocurre siempre que hay una fuerza restauradora para $k=0$ en el sistema infinito. Más adelante, en el capítulo 11, veremos que un fenómeno similar puede ocurrir en sistemas bidimensionales y tridimensionales, incluso cuando no hay fuerza restauradora en $k=0$.

El corte de frecuencia alta, en cambio, depende de la separación finita entre bloques. A medida que $\omega$ aumenta, en la región permitida (8.96), $\sin(ka/2)$ aumenta, $k$ aumenta, y por tanto $\cos(ka/2)$ disminuye. En el corte de frecuencia alta, $\omega=\omega_h$, $\sin(ka/2)=1$ y $\cos(ka/2)=0$. Pero

$$\sin\frac{ka}{2}=1 \implies k=\frac{\pi}{a} \qquad \text{(8.101)}$$

lo que a su vez significa

$$e^{ika}=e^{-ika}=-1\,. \qquad \text{(8.102)}$$

Así, el desplazamiento de los bloques simplemente alterna, porque

$$\psi_j = \psi(ja,t) \propto e^{ij\pi} = (-1)^j\,. \qquad \text{(8.103)}$$

Esto es lo más ondulado que puede llegar a ser el sistema discreto. En un sistema discreto con separación entre bloques $a$, la máxima parte real posible de $k$ es $\pi/a$ (porque $k$ puede redefinirse en un múltiplo de $2\pi/a$ sin cambiar los desplazamientos de ninguno de los bloques —véase (5.28)). Esta cota es el origen del corte de frecuencia alta.

Puede verlo en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-6" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-6</a>. La frecuencia empieza en $6\omega_0$; en este punto, $k_ra$ es bastante pequeño (y $k_i=0$), y la onda se ve suave. A medida que la frecuencia aumenta hacia $\omega_h$, la onda se ve cada vez más dentada, hasta que, en $\omega=\omega_h$, las cuentas vecinas se mueven en direcciones opuestas.

Para $\omega>\omega_h$, $\sin(ka/2)$ es mayor que 1, y $\cos(ka/2)$ es negativo. Esto implica que $k$ tiene la forma

$$k = \frac{\pi}{a} \pm ik_i\,. \qquad \text{(8.104)}$$

Entonces la solución general para el desplazamiento es

$$\psi(x,t) = A\,e^{-k_ix}e^{i\pi x/a}e^{-i\omega t} + B\,e^{k_ix}e^{i\pi x/a}e^{-i\omega t}\,. \qquad \text{(8.105)}$$

Como en (8.100), hay un término que decae exponencialmente y otro que crece exponencialmente. Aquí, sin embargo, hay también un factor de fase, $e^{i\pi x/a}$, que parece que pudiera dar lugar a una onda viajera. Pero, de hecho, esto no es realmente una fase: simplemente produce la alternancia del desplazamiento de un bloque al siguiente. Vemos esto si solo miramos los desplazamientos de los bloques (como en (8.103)):

$$\psi_j = \psi(ja,t) = A(-1)^je^{-k_ix}e^{-i\omega t} + B(-1)^je^{k_ix}e^{-i\omega t}\,. \qquad \text{(8.106)}$$

Como en (8.100), en un sistema semiinfinito que se extiende hasta $x\to\infty$, debemos tener $B=0$, y no hay onda viajera.

Una de las cosas llamativas del programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-6" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-6</a> es el cambio muy rápido de una solución de onda viajera en la región permitida a una solución de onda estacionaria con decaimiento exponencial rápido de la amplitud en las regiones de frecuencia alta y baja. Esto también se ve en la figura 8.12, en el cambio rápido de $k_i$ cerca de los cortes. La razón es que $k$ tiene una dependencia en raíz cuadrada de la frecuencia cerca de los cortes.

En el sistema infinito, la solución fuera de la región permitida es una onda estacionaria pura. En ausencia de amortiguamiento, el trabajo realizado por la fuerza que produce la onda se promedia a cero con el tiempo. En un sistema finito, sin embargo, es posible transferir energía de un extremo del sistema al otro, incluso por debajo del corte de frecuencia baja o por encima del corte de frecuencia alta. La razón es que, en un sistema finito, tanto el término $A$ como el $B$ de (8.100) (o (8.106)) pueden ser no nulos. Si $A$ y $B$ son ambos reales (o «relativamente reales», es decir, tienen la misma fase), no hay transferencia de energía: la solución es el producto de una función real de $x$ (o $j$) y una función exponencial oscilante de $t$, así que se ve como una onda estacionaria. Sin embargo, si $A$ y $B$ tienen fases distintas, la oscilación se parece a una onda viajera y puede transferirse energía. Este proceso se vuelve exponencialmente menos eficiente a medida que aumenta la longitud del sistema. Discutiremos esto con más detalle en el capítulo 11.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Construir modos de onda viajera de un sistema infinito invariante bajo traslación;

2.  Descomponer una onda viajera en un par de ondas estacionarias, y una onda estacionaria en un par de ondas viajeras «moviéndose» en direcciones opuestas;

3.  Resolver problemas de oscilación forzada con soluciones de onda viajera y calcular las fuerzas que actúan sobre el sistema;

4.  Calcular la potencia y la potencia media necesarias para producir una onda, y definir y calcular la impedancia;

5.  Analizar sistemas invariantes bajo traslación con amortiguamiento;

6.  Entender los orígenes físicos de los cortes de frecuencia alta y baja, y poder analizar el comportamiento de sistemas impulsados por encima y por debajo de las frecuencias de corte.

## Problemas

**8.1.** Una cuerda infinita con tensión $T$ y densidad de masa lineal $\rho$ está estirada a lo largo del eje $x$. Se aplica una fuerza en la dirección $y$ en $x=0$, de modo que la cuerda en $x=0$ oscila en la dirección $y$ con desplazamiento

$$A(t) = D\cos\omega t\,.$$

Esto produce dos ondas viajeras que se alejan de $x=0$ en las direcciones $\pm x$.

1.  Encuentre la fuerza aplicada en $x=0$.

2.  Encuentre la potencia media suministrada por la fuerza.

**8.2.** Para el aire en condiciones normales de temperatura y presión, la presión es $1.01\times10^6\ \text{dyn/cm}^2$, la densidad es $1.29\times10^{-3}\ \text{g/cm}^3$. Use estos valores para encontrar la amplitud de desplazamiento de las ondas sonoras con una frecuencia de 440 ciclos/s (hercios), que transportan una potencia por unidad de área de $10^{-3}\ \text{W/cm}^2$.

**8.3.** Considere el siguiente circuito: seis nodos con voltajes $V_0$ a $V_6$, conectados en cadena por inductores idénticos, con condensadores idénticos a tierra y una resistencia en cada tramo.

Todos los condensadores tienen la misma capacitancia, $C\approx0.00667\ \mu\text{F}$, y todos los inductores tienen la misma inductancia, $L\approx150\ \mu\text{H}$, y la misma resistencia, $R\approx15\ \Omega$ (este es el mismo problema que (5.4), pero con resistencia no nula). El hilo de abajo está conectado a tierra, de modo que $V_0=0$. Este circuito es un análogo eléctrico de los sistemas invariantes bajo traslación de osciladores mecánicos acoplados que hemos discutido en este capítulo.

1.  Demuestre que la relación de dispersión de este sistema es

$$\omega^2 + i\omega\frac{R}{L} = \frac{2}{LC}(1-\cos ka)\,.$$

Cuando aplica una señal oscilante armónicamente desde un generador de señales, a través de un cable coaxial, a $V_6$, se inducen distintos voltajes oscilantes a lo largo de la línea. Es decir, si

$$V_6(t) = V\cos\omega t\,,$$

entonces $V_j(t)$ tiene la forma

$$V_j(t) = A_j\cos\omega t + B_j\sin\omega t\,.$$

1.  Encuentre $A_1$, $B_1$ y $|A_1+iB_1|$, y grafique cada uno en función de $\omega$, desde $\omega=0$ hasta $2/\sqrt{LC}$. No se preocupe por simplificar expresiones complicadas, siempre que pueda graficarlas. ¿Cuántas de las resonancias puede identificar en cada una de las gráficas? Pista: use la identidad trigonométrica del problema 1.2e,

$$\sin6x = \sin x\left(32\cos^5x-32\cos^3x+6\cos x\right)$$

para expresar $A_1+iB_1$ en términos de $\cos ka$. Note que esta identidad es cierta incluso si $x$ es un número complejo. Luego use la relación de dispersión para expresar $\cos ka$ en términos de $\omega$. Encuentre $A_1$ y $B_1$ tomando las partes real e imaginaria de $A_1+iB_1$. Finalmente, programe un ordenador para construir las gráficas.

1.  Encuentre las posiciones de las resonancias directamente, usando los argumentos del capítulo 5, y demuestre que están donde se esperaría.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.
