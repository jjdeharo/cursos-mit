# Capítulo 7: Oscilaciones longitudinales y sonido

Las oscilaciones transversales de un sistema continuo son fáciles de visualizar, porque se puede ver directamente la función que describe el desplazamiento. Las matemáticas de las oscilaciones longitudinales de un sistema continuo, lineal e invariante bajo traslación espacial son las mismas. Deben serlo, porque quedan completamente determinadas por la invariancia bajo traslación espacial. Pero la física es distinta.

## Vídeos de esta clase (YouTube)

- [Clase 10: Ondas viajeras](https://www.youtube.com/watch?v=SnNmbVH5DAM)
- [Clase 11: Ondas sonoras](https://www.youtube.com/watch?v=RhIh1zw0-BM)

## Resumen previo

En este capítulo introducimos dos sistemas físicos con oscilaciones longitudinales: muelles masivos y tubos de órgano.

1.  Describimos el muelle masivo como el límite continuo de un sistema de masas conectadas por muelles sin masa, y estudiamos sus modos normales para diversas condiciones de contorno.

2.  Discutimos con cierto detalle el sistema de una masa en el extremo de un muelle masivo. Cuando el muelle es «ligero», este es un ejemplo importante de física con dos «escalas» distintas.

3.  Discutimos la física de las ondas sonoras en un tubo, por analogía con las oscilaciones del muelle masivo. También introducimos la aproximación de «Helmholtz» para el modo más bajo de una botella.

## 7.1 Modos longitudinales en un muelle masivo

Hasta ahora, en nuestras extensas discusiones sobre ondas en sistemas de muelles y bloques, hemos supuesto que los únicos grados de libertad son los asociados al movimiento de los bloques. Esta es una suposición razonable a bajas frecuencias, cuando los bloques son muy pesados comparados con los muelles, porque los bloques se mueven tan lentamente que los muelles tienen tiempo de reajustarse y son siempre casi uniformes (lo formalizaremos más abajo). En este caso, la relación de dispersión de las oscilaciones longitudinales de los bloques es justamente la relación de dispersión de los péndulos acoplados, (5.35), en el límite en que ignoramos la gravedad y conservamos solo el acoplamiento entre las masas producido por la constante del muelle, $K$. En otras palabras, tomamos el límite de (5.35) cuando $g/\ell\to0$. El resultado puede escribirse como

$$\omega^2 = \frac{4K_a}{m}\sin^2\frac{ka}{2} \qquad \text{(7.1)}$$

donde $K_a$ es la constante de los muelles, $m$ es la masa de los bloques, y $a$ es la separación de equilibrio. Hemos puesto un subíndice $a$ en $K_a$ porque querremos variar la constante del muelle a medida que variamos la separación entre los bloques en la discusión que sigue.

Ahora bien, ¿qué ocurre cuando los bloques desaparecen, pero el muelle es masivo? Podemos averiguarlo considerando el límite de (7.1) cuando $a\to0$. En este límite, los bloques masivos y el muelle sin masa se funden entre sí, de modo que el resultado se parece a un muelle uniforme y masivo. Para tomar el límite, sin embargo, debemos entender qué variables describen el muelle masivo y tienen un límite finito cuando $a\to0$. Una de esas variables es la densidad de masa lineal,

$$\rho_L = \lim_{a\to0}\frac{m}{a}\,. \qquad \text{(7.2)}$$

Debemos hacer que las masas de los bloques tiendan a cero cuando $a\to0$, para mantener $\rho_L$ finita.

Para entender qué le ocurre a $K_a$ cuando $a\to0$, considere qué pasa cuando corta un muelle por la mitad. Cuando un muelle se estira, cada mitad contribuye la mitad del desplazamiento. Pero la tensión es uniforme a lo largo de todo el muelle estirado. Así, la constante de media muelle es el doble de la del muelle completo, porque la mitad del desplazamiento da la misma fuerza. Esta relación se ilustra en la figura 7.1. El muelle central no está estirado. El muelle de arriba está estirado una cantidad $x$ hacia la derecha. Abajo se muestra el mismo muelle estirado, todavía estirado $x$, pero ahora simétricamente. Comparando arriba y abajo, puede ver que la fuerza de retorno de estirar el muelle una cantidad $x$ es la misma que la de estirar media muelle una cantidad $x/2$.

![Figura 7.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh7_ES/fig7.1.png)

Figura 7.1: arriba, un muelle completo estirado una cantidad $x$ hacia la derecha; abajo, el mismo muelle dividido en dos mitades, cada una estirada simétricamente una cantidad $x/2$, mostrando que la fuerza de retorno es la misma.

El diagrama de la figura 7.1 es un ejemplo del siguiente resultado. En general, la constante de muelle, $K_a$, no depende solo de qué está hecho el muelle, sino de cuán largo es. Pero la cantidad $K_aa$, donde $a$ es la longitud del muelle, es en realidad independiente de $a$, para un muelle hecho de material uniforme. Así, deberíamos tomar el límite $a\to0$ manteniendo $K_aa$ fijo.

Esto implica que la relación de dispersión del muelle masivo es

$$\omega^2 = \frac{K_aa}{\rho_L}\,k^2\,, \qquad \text{(7.3)}$$

donde hemos usado el desarrollo en serie de Taylor de $\sin x$, (1.58), y conservado solo el primer término. Según la discusión anterior, podemos reescribir esto como

$$\omega^2 = \frac{K\ell}{\rho_L}\,k^2 \qquad \text{(7.4)}$$

donde $\ell$ es la longitud del muelle y $K$ es la constante del muelle completo.

Note que, en las oscilaciones longitudinales de un material continuo en la dirección $x$, la posición de equilibrio, $x$, en realidad no describe la posición $x$ del material. Como el desplazamiento es longitudinal, la posición $x$ real del punto del muelle con posición de equilibrio $x$ es

$$x+\psi(x,t)\,, \qquad \text{(7.5)}$$

donde $\psi$ es el desplazamiento. Necesitará esto para el problema 7.1.

### 7.1.1 Extremos fijos

*(Referencia al programa interactivo 7-1 del disco de programas del curso original.)*

Suponga que tenemos un muelle masivo de longitud $\ell$, con sus extremos fijos en $x=0$ y $x=\ell$. Entonces el desplazamiento, $\psi(x,t)$, debe anularse en los extremos,

$$\psi(0,t)=0\,,\qquad \psi(\ell,t)=0\,. \qquad \text{(7.6)}$$

Los modos del sistema son los mismos que para cualquier otro sistema invariante bajo traslación espacial. Las combinaciones lineales de los modos exponenciales complejos del sistema infinito que satisfacen (7.6) son

$$A_n(x) = \sin\frac{n\pi x}{\ell}\,, \qquad \text{(7.7)}$$

con número de onda angular

$$k_n = \frac{n\pi}{\ell} \qquad \text{(7.8)}$$

y frecuencia (a partir de la relación de dispersión, (7.4))

$$\omega_n = \sqrt{\frac{K\ell}{\rho_L}}\,k_n = \sqrt{\frac{K\ell}{\rho_L}}\,\frac{n\pi}{\ell}\,. \qquad \text{(7.9)}$$

Sin embargo, como las oscilaciones son longitudinales, los modos se ven muy distintos de los modos transversales de la cuerda que estudiamos en el capítulo anterior. La posición del punto de la cuerda cuya posición de equilibrio es $x$, en el $n$-ésimo modo normal, tiene la forma general (de (7.5))

$$x + \epsilon\sin\frac{n\pi x}{\ell}\cos(\omega_nt+\varphi) \qquad \text{(7.10)}$$

donde $\epsilon$ y $\varphi$ son la amplitud y la fase de la oscilación.

Los nueve modos más bajos de (7.10) se animan en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-7-1" rel="noopener" target="_blank" title="Animación original de Howard Georgi">7-1</a>. Compárelos con los modos animados en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-6-1" rel="noopener" target="_blank" title="Animación original de Howard Georgi">6-1</a>. Las matemáticas son las mismas, pero la física es muy distinta, debido a (7.5). Observe con atención estas dos animaciones hasta que pueda visualizar la relación entre ambas: entonces habrá entendido (7.5).

### 7.1.2 Extremos libres

*(Referencia al programa interactivo 7-2 del disco de programas del curso original.)*

Consideremos ahora la situación en la que el extremo del muelle en $x=0$ está fijo, pero el extremo en $x=\ell$ es libre. Las condiciones de contorno en este caso son análogas a las de los modos normales de la cuerda con un extremo fijo. El desplazamiento en $x=0$ debe anularse porque ese extremo está fijo. Además, la derivada del desplazamiento en $x=\ell$ debe anularse. Puede verlo considerando el muelle continuo como el límite de masas discretas acopladas por muelles. Como vimos en (5.43), la última masa real debe tener el mismo desplazamiento que la primera masa «imaginaria»,

$$\psi(\ell,t) = \psi(\ell+a,t)\,. \qquad \text{(7.11)}$$

Por tanto, para el sistema finito con un extremo libre en $\ell$, tenemos la relación

$$\frac{\psi(\ell,t)-\psi(\ell+a,t)}{a} = 0 \quad\text{para todo } a\,. \qquad \text{(7.12)}$$

En el límite en que la distancia entre masas tiende a cero, esto se convierte en la condición de que la derivada del desplazamiento, $\psi$, respecto a $x$ se anule en $x=\ell$,

$$\left.\frac{\partial}{\partial x}\psi(x,t)\right|_{x=\ell} = 0\,. \qquad \text{(7.13)}$$

Así, las condiciones de contorno para el desplazamiento son las mismas que en (6.11), para la oscilación transversal de una cuerda continua con $x=0$ fijo y $x=\ell$ libre,

$$\psi(0,t)=0\,,\qquad \left.\frac{\partial}{\partial x}\psi(x,t)\right|_{x=\ell}=0\,. \qquad \text{(7.14)}$$

Esto, a su vez, implica que los modos normales son los mismos que para la cuerda oscilando transversalmente, (6.15),

$$A_n(x) = \sin\left(\frac{(2n+1)\pi x}{2\ell}\right) \quad\text{para } n=0\text{ a }\infty\,. \qquad \text{(7.15)}$$

Sin embargo, de nuevo debido a (7.5), estos modos se ven muy distintos de los de la cuerda. Los primeros nueve se animan en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-7-2" rel="noopener" target="_blank" title="Animación original de Howard Georgi">7-2</a> (compárese con el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-6-2" rel="noopener" target="_blank" title="Animación original de Howard Georgi">6-2</a>).

## 7.2 Una masa sobre un muelle ligero

Volvamos al sistema que estudiamos al principio mismo del libro, el oscilador armónico construido colocando una masa en el extremo de un muelle ligero. Ahora estamos en posición de entender con precisión qué significa «ligero» para este sistema, porque ahora podemos permitir que el muelle tenga una densidad de masa lineal no nula, $\rho_L$, y encontrar los modos normales de este sistema. Después podremos ver qué ocurre cuando $\rho_L\to0$.

Para concretar, considere un muelle con longitud de equilibrio $\ell$ y constante $K$, fijo en $x=0$ y obligado a oscilar solo en la dirección $x$ (es decir, longitudinalmente). Ahora una una masa, $m$, al extremo libre (con posición de equilibrio $x=\ell$). El muelle, para $0<x<\ell$, puede considerarse parte de un sistema invariante bajo traslación espacial. Para encontrar los modos normales de este sistema, buscamos una combinación lineal de los modos del muelle infinito (para un $\omega$ dado) que reproduzca la física en $x=0$ y $x=\ell$. El extremo fijo en $x=0$ es fácil: fija la forma de los modos para que sean proporcionales a

$$\sin k_nx \qquad \text{(7.16)}$$

con frecuencia

$$\omega_n = \sqrt{\frac{K\ell}{\rho_L}}\,k_n\,. \qquad \text{(7.17)}$$

Como siempre, $k_n$ y $\omega_n$ están relacionados por la relación de dispersión, (7.4). Ahora, para determinar los posibles valores de $k_n$, exigimos que se satisfaga $F=ma$ para la masa. Suponga, por ejemplo, que la amplitud de la oscilación es $A$ (una longitud). Entonces el desplazamiento del punto del muelle con posición de equilibrio $x$ es

$$\psi(x,t) = A\sin k_nx\cos\omega_nt\,, \qquad \text{(7.18)}$$

y el desplazamiento de la masa queda determinado por el desplazamiento del extremo del muelle,

$$x(t) \equiv \psi(\ell,t) = A\sin k_n\ell\cos\omega_nt\,. \qquad \text{(7.19)}$$

La aceleración es

$$a(t) = \frac{\partial^2}{\partial t^2}\psi(\ell,t) = -\omega_n^2A\sin k_n\ell\cos\omega_nt \qquad \text{(7.20)}$$

![Figura 7.2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh7_ES/fig7.2.png)

Figura 7.2: el estiramiento del último tramo de muelle es $\psi(\ell,t)-\psi(\ell-a,t)$, mostrando el muelle en equilibrio y estirado, con la masa $m$ en el extremo derecho.

Para encontrar la fuerza sobre la masa, considere el muelle masivo como el límite continuo, cuando $a\to0$, de masas conectadas por muelles sin masa de longitud de equilibrio $a$, como al principio del capítulo. Entonces la fuerza sobre la masa del extremo está determinada por el estiramiento del último muelle de la serie. Esto, a su vez, es la diferencia entre el desplazamiento del sistema en $x=\ell$ y en $x=\ell-a$, como se ilustra en la figura 7.2. Así, la fuerza es

$$F = -K_a\left[\psi(\ell,t)-\psi(\ell-a,t)\right]\,. \qquad \text{(7.21)}$$

Para tomar el límite $a\to0$, reescribimos esto como

$$F = -K_aa\,\frac{\psi(\ell,t)-\psi(\ell-a,t)}{a}\,. \qquad \text{(7.22)}$$

Ahora, en el límite continuo, $K_aa$ es $K\ell$, y el último factor tiende a una derivada, $\partial\psi(x,t)/\partial x|_{x=\ell}$. El resultado final para la fuerza es, por tanto (note que esto también da una deducción alternativa de la condición de contorno para un extremo libre, (7.14)):

$$F = -K\ell\,\left.\frac{\partial}{\partial x}\psi(x,t)\right|_{x=\ell} = -K\ell\,k_nA\cos k_n\ell\cos\omega_nt\,. \qquad \text{(7.23)}$$

Note que las unidades cuadran: $K\ell$ es una fuerza, y $\partial\psi/\partial x$ es adimensional.

Sustituyendo (7.20) y (7.23) en $F=ma$, y cancelando un factor $-A\cos\omega_nt$ en ambos lados, obtenemos

$$K\ell\,k_n\cos k_n\ell = m\omega_n^2\sin k_n\ell\,. \qquad \text{(7.24)}$$

Usando la relación de dispersión para eliminar $\omega_n^2$, obtenemos

$$k_n\ell\tan k_n\ell = \frac{\rho_L\ell}{m}\,. \qquad \text{(7.25)}$$

Hemos multiplicado ambos lados de (7.25) por $\ell$ para trabajar con la variable adimensional $k_n\ell$ (que es $2\pi$ veces el número de longitudes de onda que caben en el muelle) y el número adimensional

$$\epsilon \equiv \frac{\rho_L\ell}{m} \qquad \text{(7.26)}$$

(que es el cociente entre la masa del muelle, $\rho_L\ell$, y la masa $m$). El muelle es ligero si $\epsilon$ es mucho menor que uno.

El punto importante es que (7.25) tiene una única solución para $k_n\ell$ que tiende a cero cuando $\epsilon\to0$. Como $\tan k\ell\approx k\ell$ para $k\ell$ pequeño, es

$$k_0\ell \approx \sqrt\epsilon\,. \qquad \text{(7.27)}$$

Para todas las demás soluciones, la pequeñez del lado izquierdo de (7.25) debe provenir de que $\tan k_n\ell$ sea muy pequeño,

$$k_n\ell \approx n\pi \quad\text{para } n=1\text{ a }\infty\,. \qquad \text{(7.28)}$$

Pero (7.28) implica

$$x(t) \equiv \psi(\ell,t) = A\sin k_n\ell\cos\omega_nt \approx 0 \quad\text{para } n=1\text{ a }\infty\,. \qquad \text{(7.29)}$$

En otras palabras, en todas las soluciones excepto $k_0$, la masa apenas se mueve, y es el muelle el que hace casi toda la oscilación, pareciéndose mucho a un sistema con dos extremos fijos. Además, las frecuencias de todos los modos, salvo el modo $k_0$, son grandes,

$$\omega_n \approx n\pi\sqrt{\frac{K}{\rho_L\ell}} \quad\text{para } n=1\text{ a }\infty\,, \qquad \text{(7.30)}$$

mientras que la frecuencia del modo $k_0$ es

$$\omega_0 \approx \sqrt{\frac{K}{m}}\,. \qquad \text{(7.31)}$$

Para $\epsilon$ pequeño (masa grande), el modo $k_0$ está asociado principalmente a la oscilación de la masa, y tiene aproximadamente la frecuencia que encontramos para el caso del muelle sin masa. Los demás modos están en un rango de frecuencias completamente distinto: están asociados a las oscilaciones del muelle. Este es un ejemplo importante de cómo un único sistema puede comportarse de formas muy distintas en diferentes regímenes de frecuencia.

## 7.3 La velocidad del sonido

![Figura 7.3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh7_ES/fig7.3.png)

Figura 7.3: tubo de órgano vertical, de longitud $z=0$ a $z=\ell$.

La física de las ondas sonoras es obviamente un problema tridimensional. Sin embargo, podemos aprender mucho sobre el sonido considerando el movimiento del aire en una sola dimensión. Considere, por ejemplo, ondas estacionarias en el aire de un tubo largo y estrecho, como un tubo de órgano, mostrado esquemáticamente en la figura 7.3. Aquí ignoraremos el movimiento del aire perpendicular a la longitud del tubo, y consideraremos solo el movimiento unidimensional a lo largo del tubo. Como veremos más adelante, cuando podamos tratar problemas tridimensionales, esto es razonable a bajas frecuencias, para las que no pueden excitarse los modos transversales de oscilación. Si consideramos solo el movimiento unidimensional, podemos trazar una analogía entre las oscilaciones del aire en el tubo y las ondas longitudinales en un muelle masivo.

Está claro cuál es el análogo de $\rho_L$: la densidad de masa lineal del aire en el tubo es

$$\rho_L = \rho A \qquad \text{(7.32)}$$

donde $A$ es el área de la sección transversal del tubo. La pregunta entonces es: ¿cuál es $K\ell$ para un tubo de aire?

Considere colocar un pistón en la parte superior del tubo, como se muestra en la figura 7.4. Con el pistón en la parte superior, no hay fuerza sobre él, porque la presión del aire en el tubo es igual a la presión del aire de la habitación exterior. Sin embargo, si el pistón se empuja hacia adentro una distancia $dz$, como se muestra en la figura 7.5, el volumen del aire en el tubo disminuye en

$$-dV = A\,dz\,. \qquad \text{(7.33)}$$

![Figura 7.4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh7_ES/fig7.4.png)

Figura 7.4 y 7.5: el tubo de órgano con un pistón en la parte superior; el aire del tubo actúa como un muelle; al empujar el pistón hacia adentro una distancia $dz$, cambia el volumen del aire encerrado.

Si el pistón se moviera lo bastante despacio como para que la temperatura del gas se mantuviera constante, entonces la presión sería simplemente inversamente proporcional al volumen. Sin embargo, en una onda sonora, el movimiento del aire es tan rápido que casi no hay tiempo para que fluya calor dentro o fuera del sistema. Tal cambio de volumen se llama «adiabático». Cuando el volumen disminuye adiabáticamente, la temperatura sube (porque la fuerza sobre el pistón realiza trabajo) y la presión aumenta más rápido que $1/V$, como

$$p \propto V^{-\gamma} \qquad \text{(7.34)}$$

donde $\gamma$ es una constante positiva que depende de las propiedades termodinámicas del gas. Más precisamente, $\gamma$ es el cociente entre el calor específico a presión constante y el calor específico a volumen constante (véase, por ejemplo, Halliday y Resnick):

$$\gamma = C_P/C_V \qquad \text{(7.35)}$$

En el aire, en condiciones normales de temperatura y presión,

$$\gamma_{\text{aire}} \approx 1.40\,. \qquad \text{(7.36)}$$

Ahora podemos escribir, a partir de (7.34),

$$\frac{dp}{p} = -\gamma\,\frac{dV}{V} \qquad \text{(7.37)}$$

o

$$dp = -\gamma p\,\frac{dV}{V} \approx \frac{\gamma A\,p_0}{V}\,dz = \frac{\gamma p_0}{\ell}\,dz \qquad \text{(7.38)}$$

donde $p_0$ es la presión de equilibrio (ambiente). Entonces la fuerza sobre el pistón es

$$dF = A\,dp = \frac{\gamma A^2p_0}{V}\,dz = \frac{\gamma A p_0}{\ell}\,dz \qquad \text{(7.39)}$$

de modo que

$$K = \frac{dF}{dz} = \frac{\gamma A p_0}{\ell} \qquad \text{(7.40)}$$

y $K\ell$ es

$$K\ell = \gamma A p_0\,. \qquad \text{(7.41)}$$

Así, esperamos que la relación de dispersión sea

$$\omega^2 = v_{\text{sonido}}^2k^2 = \frac{K\ell}{\rho_L}\,k^2 = \frac{\gamma p_0}{\rho}\,k^2 \qquad \text{(7.42)}$$

donde hemos definido la «velocidad del sonido», $v_{\text{sonido}}$, como

$$v_{\text{sonido}}^2 = \frac{\gamma p_0}{\rho}\,. \qquad \text{(7.43)}$$

Para el aire en condiciones normales de temperatura y presión,

$$v_{\text{sonido}} \approx 332\ \frac{\text{m}}{\text{s}}\,. \qquad \text{(7.44)}$$

Como veremos en el próximo capítulo, esta es en realidad la velocidad a la que viajan las ondas sonoras. Por ahora, es simplemente un parámetro en nuestro cálculo de los modos normales.

En el tubo mostrado en la figura 7.3, el desplazamiento del aire, que llamaremos $\psi(z,t)$, debe anularse en $z=0$, porque el fondo del tubo está cerrado y no hay adónde ir para el gas.

La derivada en $z$ de $\psi$ debe anularse en $z=\ell$, porque el exceso de presión es proporcional a $-\partial\psi/\partial z$. La presión es proporcional a la fuerza en nuestra analogía con las ondas longitudinales en el muelle masivo. Usando (7.41) y (7.23), esperamos que la fuerza longitudinal sea

$$\pm\gamma A p_0\,\frac{\partial\psi}{\partial z} \qquad \text{(7.45)}$$

o que el exceso de presión sea

$$p - p_0 = -\gamma p_0\,\frac{\partial\psi}{\partial z}\,. \qquad \text{(7.46)}$$

Queremos el signo negativo porque, para $\partial\psi/\partial z>0$, el aire se está expandiendo y tiene menor presión.

Así, para una onda estacionaria en el tubo de la figura 7.3, esperamos las condiciones de contorno

$$\psi(0,t)=0\,,\qquad \left.\frac{\partial}{\partial z}\psi(z,t)\right|_{z=\ell}=0\,, \qquad \text{(7.47)}$$

para las cuales la solución es

$$\psi(z,t) = \sin kz\cos\omega t \qquad \text{(7.48)}$$

$$k = \frac{(n+1/2)\pi}{\ell}\,,\qquad \omega=vk\,, \qquad \text{(7.49)}$$

donde $v=v_{\text{sonido}}$, para $n$ entero no negativo. En particular, el modo de frecuencia más baja del tubo corresponde a $n=0$,

$$\omega = \frac{v\pi}{2\ell}\,,\qquad \nu = \frac{\omega}{2\pi} = \frac{v}{4\ell}\,. \qquad \text{(7.50)}$$

### 7.3.1 La aproximación de Helmholtz

Consideremos un problema ligeramente distinto. ¿Cuál es el modo de frecuencia más baja de una botella de refresco de un litro, mostrada en la figura 7.6? Un conjunto típico de parámetros es:

$$\begin{aligned}
A &\approx 2.85\ \text{cm}^2\ \text{: área del cuello}\\
\ell &\approx 5.7\ \text{cm}\ \text{: longitud del cuello}\\
L &\approx 25\ \text{cm}\ \text{: longitud de la botella}\\
V_0 &\approx 1000\ \text{cm}^3\ \text{: volumen del cuerpo}
\end{aligned} \qquad \text{(7.51)}$$

![Figura 7.6](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh7_ES/fig7.6.png)

Figura 7.6: botella de refresco de un litro, mostrando el cuello de longitud $\ell$ y el cuerpo de longitud $L$ y volumen $V_0$.

Sustituyendo la longitud, $L$, de la botella en (7.50), da $\nu\approx332$ hercios. En la afinación estándar americana (véase la tabla 7.1), esto es un Mi por encima del Do central.

Esto es obviamente incorrecto. Si alguna vez ha soplado en su botella de refresco, sabe que la frecuencia del modo más bajo es mucho menor que esa. El problema, por supuesto, es que la botella de refresco no tiene ni remotamente la forma de un tubo. Determinar los modos es un complicado problema tridimensional. Resulta, sin embargo, que podemos encontrar el modo más bajo con una aproximación bastante decente, de forma bastante fácil.

La idea es que, en el modo más bajo, el aire del cuello de la botella se mueve rápidamente, pero en el cuerpo de la botella, el aire se dispersa rápidamente, de modo que apenas se mueve. La idea de la aproximación de Helmholtz es tratar el aire del cuello como un único bloque, de masa

$$\rho A\ell\,, \qquad \text{(7.52)}$$

y tratar el cuerpo como un muelle que contribuye fuerza restauradora, pero no inercia (porque el aire apenas se mueve). Entonces todo lo que tenemos que hacer es calcular la $K$ del «muelle». Esto es fácil, usando (7.38). En este caso,

$$dV = A\,dz\,, \qquad \text{(7.53)}$$

así que

$$dp = -\gamma p\,\frac{A\,dz}{V} \approx -\gamma p_0\,\frac{A\,dz}{V_0} \qquad \text{(7.54)}$$

y

$$F \approx -\gamma p_0\,\frac{A^2\,dz}{V_0} \qquad \text{(7.55)}$$

o

$$\text{«}K\text{»} = \gamma p_0\,\frac{A^2}{V_0}\,. \qquad \text{(7.56)}$$

Entonces, usando $\omega^2=K/m$, esperamos

$$\omega = \sqrt{\frac{\gamma A^2p_0/V_0}{\rho A\ell}} = v\sqrt{\frac{A}{\ell V_0}}\,. \qquad \text{(7.57)}$$

Para la botella de refresco, (7.51), esto da

$$\nu \approx 118\ \text{hercios} \qquad \text{(7.58)}$$

o aproximadamente un Si♭ por debajo del Do grave. Esto es bastante correcto (véase el problema 7.5).

### 7.3.2 Correcciones a Helmholtz

Hay muchas correcciones posibles a (7.57) que podrían considerarse. Una es incluir el llamado «efecto de extremo». El punto es que la velocidad del aire en el modo más bajo no cae a cero inmediatamente al pasar los extremos del cuello. Así, la masa real es algo mayor que $\rho A\ell$. Según la experiencia acumulada, se obtiene un mejor resultado reemplazando

$$\ell \to \ell + 0.6\,r \qquad \text{(7.59)}$$

donde $r$ es el radio del cuello.

Aquí discutiremos otra corrección que puede tratarse sistemáticamente usando los métodos de la invariancia bajo traslación espacial y las interacciones locales. Si la botella tiene un cuello largo, probablemente no sea buena idea tratar el aire del cuello como una masa sólida. Además, hay una alternativa simple: una analogía mejor para el cuello es un muelle masivo con $K\ell=\gamma Ap_0$. Como el cuello es un sistema esencialmente unidimensional e invariante bajo traslación espacial, esperamos un desplazamiento de la forma

$$y\cos\frac{\omega z}{v} \qquad \text{(7.60)}$$

en el cuello, donde $z=0$ es el extremo abierto e $y$ es el desplazamiento del aire en $z=0$. Así, donde el cuello se une al cuerpo, el desplazamiento es

$$y\cos\frac{\omega\ell}{v}\,. \qquad \text{(7.61)}$$

La fuerza en este punto, debida a la compresión del aire en el cuello, es (de (7.45))

$$F_{\text{cuello}} = -\gamma Ap_0\,\frac{\partial\psi}{\partial z} = \frac{\gamma Ap_0\,\omega}{v}\,y\sin\frac{\omega\ell}{v}\,. \qquad \text{(7.62)}$$

Esta debe ser el negativo de la fuerza del aire en el cuerpo, a partir de (7.39),

$$-F_{\text{cuerpo}} = \frac{\gamma A^2p_0}{V_0}\,y\cos\frac{\omega\ell}{v}\,, \qquad \text{(7.63)}$$

o

$$\frac{\omega V_0}{Av}\tan\frac{\omega\ell}{v} = 1\,. \qquad \text{(7.64)}$$

Explorará las consecuencias de esto en el problema 7.5.

Este análisis no distingue entre el área de la parte superior y la inferior del cuello. Quizá el área en la parte inferior sea más apropiada: lo que importa es el área en el punto donde la onda del cuello se empalma con el cuerpo, que determina la fuerza por unidad de área en ese punto.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Encontrar el movimiento de un punto de un muelle continuo que oscila longitudinalmente en uno de sus modos normales, para diversas condiciones de contorno;

2.  Resolver los modos normales de un sistema formado por una masa unida a un muelle masivo;

3.  Deducir la relación de dispersión de las ondas sonoras y encontrar los modos normales de las oscilaciones del aire en un tubo;

4.  Usar la aproximación de Helmholtz para estimar la frecuencia del modo más bajo de una botella.

## Problemas

**7.1.** Deduzca (7.45) directamente, considerando el volumen del elemento de aire en el tubo entre $z$ y $z+dz$, y usando (7.38).

**7.2.** Use una analogía con (7.16)-(7.31) para encontrar (¡aproximadamente!) los modos normales y las frecuencias correspondientes del sistema mostrado en la figura 6.1, pero con un anillo masivo, de masa $m$, deslizando sobre la varilla sin fricción.

**7.3.** Un muelle continuo masivo, de masa $m$, longitud $L$ y constante $K$, cuelga verticalmente. El sistema se muestra en reposo, en su configuración de equilibrio, en la figura 7.7. La constante del muelle es grande, satisfaciendo $KL\gg mg$, de modo que la gravedad no desempeña ningún papel importante aquí, salvo mantener el muelle vertical. Suponga ahora que el soporte del que cuelga el muelle se hace subir y bajar, de modo que la parte superior del muelle se mueve verticalmente con desplazamiento $\epsilon\cos\omega t$, como se muestra en la figura 7.8. Encuentre la posición $z$ del extremo inferior del muelle en función del tiempo. Ignore el amortiguamiento.

![Figura 7.7](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh7_ES/fig7.7.png)

Figura 7.7: muelle masivo colgando verticalmente en equilibrio, de $z=0$ a $z=L$. Figura 7.8: el mismo muelle, con el soporte superior moviéndose como $z(t)=L+\epsilon\cos\omega t$ y se pregunta por la posición del extremo inferior.

**7.4.** Un sistema análogo al del problema 7.3 es un tubo de aire con un pistón en la parte superior y el fondo abierto, como se muestra en la figura 7.9. Si el área de la sección transversal del tubo es $A$, ¿cuál es, en este sistema, el análogo de la constante de muelle, $K$, del problema 7.3? Asegúrese de que su respuesta tenga unidades de fuerza por unidad de distancia.

![Figura 7.8](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh7_ES/fig7.8.png)

Figura 7.8

![Figura 7.9](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh7_ES/fig7.9.png)

Figura 7.9: tubo de aire vertical, de $z=0$ (abierto) a $z=L$ (pistón en la parte superior).

**7.5.** EXPERIMENTO PERSONAL — Demuestre que, cuando $\omega\ell/v$ es pequeño, (7.64) se reduce a la aproximación de Helmholtz, (7.57), mientras que para $V_0\approx0$, cuando la botella es todo cuello, se reduce al resultado de los modos de un tubo uniforme con un extremo abierto y otro cerrado, (7.50).

¡Haga el experimento! Busque una selección de al menos cuatro botellas, al menos una de las cuales tenga un cuello muy largo. Mida la frecuencia del modo más bajo de cada una, y describa cómo lo hizo. Para cada botella, tabule lo siguiente (en unidades cgs):

1.  Una descripción (por ejemplo, botella de refresco, 1000 ml)
2.  $A_t$ (el área de la parte superior del cuello)
3.  $A_b$ (el área de la parte inferior del cuello)
4.  $r$ (el radio del cuello)
5.  $\ell$ (la longitud del cuello)
6.  $V_{\text{cuerpo}}$ (el volumen del cuerpo)
7.  $\nu$ (la frecuencia del modo más bajo)
8.  $\omega$ (la frecuencia angular del modo más bajo)
9.  $\omega^2V_0\ell/Av^2$ (=1 en la aproximación de Helmholtz)
10. $(\omega V_0/Av)\tan(\omega\ell/v)$ (=1 en la aproximación (7.64))

Vea si puede apreciar el efecto de extremo, (7.59), o distinguir el área de la parte superior del cuello de la inferior —es decir, vea cuál funciona mejor en (7.57)—. Comente, de la forma más cuantitativa posible, los errores de su experimento y los méritos relativos de las expresiones aproximadas que ha puesto a prueba.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.
