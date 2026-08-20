# Capítulo 18: Dispersión en una dimensión

## Vídeos de esta clase (YouTube)

**Lección 18: Scattering in 1D (cont.). Example. Levinson’s theorem.**

- [Incident packet and delay for reflection](https://www.youtube.com/watch?v=EJWG9-etPFw)
- [Phase shift for a potential well](https://www.youtube.com/watch?v=sWmY5KME7oo)
- [Excursion of the phase shift](https://www.youtube.com/watch?v=Cb_3sOYLjUI)
- [Levinson’s theorem, part 1](https://www.youtube.com/watch?v=GyukKStk6Ls)
- [Levinson’s theorem, part 2](https://www.youtube.com/watch?v=yhI3jTX4dY4)

------------------------------------------------------------------------

*B. Zwiebach* *26 de abril de 2016*

## 1. Dispersión en una dimensión

Los físicos aprenden mucho de los experimentos de dispersión. Rutherford aprendió sobre la estructura del átomo dispersando partículas alfa contra láminas delgadas de oro. Tenemos dispersión elástica si las partículas no cambian de tipo; esto normalmente requiere energías bajas. A energías altas, la dispersión se vuelve bastante complicada debido a la creación de nuevas partículas.

La dispersión de una partícula contra un blanco fijo se estudia trabajando con una partícula que se mueve en un potencial, el potencial creado por el blanco. Incluso en el caso de colisiones entre partículas, generalmente es posible estudiar el problema usando coordenadas del centro de masas y, de nuevo, considerando la dispersión en un potencial.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes18_ES/fig1.png)

Figura 1: Un potencial de alcance R. El potencial se anula para x &gt; R y es infinito para x ≤ 0.

Consideramos la dispersión (elástica) en el potencial general mostrado en la Fig. 1. Este potencial viene dado por

$$V(x) = \begin{cases} V(x) & 0 < x < R, \\ 0 & x > R, \\ \infty & x < 0. \end{cases} \qquad \text{(1.1)}$$

A esto lo llamamos un potencial de alcance finito, porque la parte no trivial $V(x)$ del potencial no se extiende más allá de una distancia $R$ desde el origen. Además, tenemos una pared de potencial infinito en $x = 0$. Así, toda la física ocurre en $x > 0$, y las ondas entrantes desde $x \to \infty$ acabarán reflejándose de vuelta, dando al físico información sobre el potencial. La restricción a $x > 0$ también será útil cuando más adelante estudiemos el caso más físico de la dispersión en tres dimensiones. En ese caso, al usar coordenadas esféricas, tenemos $r > 0$ y la mayoría de los conceptos que aprenderemos aquí se aplicarán.

Consideremos primero el caso en que $V(x) = 0$, de modo que

$$V(x) = \begin{cases} 0 & x > 0, \\ \infty & x < 0, \end{cases} \qquad \text{(1.2)}$$

como se muestra en la figura 2. Tenemos una partícula libre, salvo por la pared en $x = 0$. Las soluciones pueden construirse usando combinaciones lineales de autoestados de momento $e^{\pm ikx}$ donde

$$k^2 = \frac{2mE}{\hbar^2}. \qquad \text{(1.3)}$$

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes18_ES/fig2.png)

Figura 2: El potencial nulo y sus autoestados de energía $\varphi(x) = \sin kx$ son necesarios para compararlos con el problema en el que $V(x) \neq 0$.

La solución tiene una onda entrante $e^{-ikx}$ y una onda saliente $e^{ikx}$ combinadas de tal manera que $\varphi(0) = 0$, como exige la presencia de la pared:

$$\varphi(x) \sim e^{ikx} - e^{-ikx}. \qquad \text{(1.4)}$$

Mejor aún, podemos dividir esta solución entre $2i$ para hallar

$$\varphi(x) = -\frac{e^{-ikx}}{2i} + \frac{e^{ikx}}{2i} = \sin kx. \qquad \text{(1.5)}$$

La onda entrante es el primer término a la derecha del primer signo igual, y la onda reflejada es el segundo término. Ambas transportan la misma cantidad de flujo de probabilidad, pero en direcciones opuestas.

Consideremos ahora el caso $V(x) \neq 0$. Este potencial actúa siempre sobre el rango finito $0 < x < R$, y eventualmente nos interesará calcular la función de onda del autoestado de energía $\psi(x)$ en esta región. Por el momento, sin embargo, consideremos $\psi(x)$ en la región $x > R$. Tomaremos la onda entrante como la misma que teníamos para la solución de potencial nulo $\varphi(x)$:

$$\text{Onda entrante:} \qquad -\frac{e^{-ikx}}{2i} \qquad \text{(1.6)}$$

La onda saliente que debe añadirse a lo anterior requiere un $e^{ikx}$, para tener la misma energía que la solución de la onda entrante. Ahora afirmamos que la solución más general incluye un factor de fase, de modo que tenemos

$$\text{Onda saliente:} \qquad e^{2i\delta} \frac{e^{ikx}}{2i}, \qquad \delta \in \mathbb{R}. \qquad \text{(1.7)}$$

Observamos que la fase $\delta$ no puede ser función de $x$: la ecuación de Schrödinger libre para $x > R$ solo permite fases lineales en $x$, pero eso cambiaría el valor del momento asociado a la onda saliente, que ya hemos argumentado debe ser $k$. Además, $\delta$ no puede ser compleja, porque entonces dejaríamos de tener igualdad entre los flujos de probabilidad incidente y reflejado. Esta condición exige que la norma al cuadrado de los números que multiplican a las exponenciales $e^{\pm ikx}$ sea la misma. Así, $\delta$ es una función real que depende de la energía $E$ del autoestado y, por supuesto, del potencial $V(x)$. Un rango natural para $\delta$ es de cero a $2\pi$, pero será más fácil dejar que recorra todos los números reales $\mathbb{R}$, con el fin de lograr una $\delta$ que sea una función continua de la energía. Reuniendo las componentes incidente y reflejada de la solución para $x > R$, obtenemos

$$\psi(x) = \frac{1}{2i}\left(-e^{-ikx} + e^{ikx+2i\delta}\right) = e^{i\delta}\sin(kx+\delta), \qquad \text{para } x > R. \qquad \text{(1.8)}$$

A esto se le llama la solución canónica para $x > R$. Para cualquier rasgo particular de la solución $\varphi(x)$ que encontremos en $kx = a_0$, es decir en $x = a_0/k$, encontraríamos el mismo rasgo en $\psi(x)$ en $k\tilde{x} + \delta = a_0$, es decir en $\tilde{x} = a_0/k - \delta/k$. Para $\delta > 0$ pequeño, la onda se ve arrastrada hacia adentro en una cantidad $\delta/k$, y el potencial ejerce atracción. Para $\delta < 0$ pequeño, la onda se ve empujada hacia afuera en una cantidad $|\delta|/k$, y el potencial ejerce repulsión. Nótese también que $\delta$ y $\delta \pm \pi$ dan exactamente el mismo $\psi(x)$. Esto se ve más fácilmente a partir de la primera forma en (1.8).

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes18_ES/fig3.png)

Figura 3: La solución $\varphi(x)$ para potencial nulo se muestra con línea discontinua. Para $x > R$, la solución $\psi(x)$ se muestra como línea continua. En comparación con $\varphi(x)$, está desplazada espacialmente hacia el origen en una distancia $\delta/k$.

Definimos la onda dispersada $\psi_s(x)$ como la onda adicional en la solución $\psi(x)$ que se anularía en el caso de potencial nulo, es decir

$$\psi(x) = \varphi(x) + \psi_s(x). \qquad \text{(1.9)}$$

Nótese que tanto $\varphi$ como $\psi$ tienen la misma onda incidente, así que $\psi_s$ debe ser una onda saliente. Encontramos, en efecto,

$$\psi_s(x) = \psi(x) - \varphi(x) = -\frac{e^{-ikx}}{2i} + \frac{e^{ikx+2i\delta}}{2i} + \frac{e^{-ikx}}{2i} - \frac{e^{ikx}}{2i} = \frac{e^{ikx+2i\delta}}{2i} - \frac{e^{ikx}}{2i}, \qquad \text{(1.10)}$$

y por lo tanto obtenemos

$$\psi_s(x) = e^{i\delta}\sin\delta \, e^{ikx} = A_s e^{ikx}, \qquad \text{con} \quad A_s \equiv e^{i\delta}\sin\delta. \qquad \text{(1.11)}$$

A $A_s$ se le llama la amplitud de dispersión, siendo la amplitud de la onda dispersada. Aunque todavía no podemos normalizar nuestros estados (para eso necesitamos paquetes de onda), la probabilidad de dispersión queda capturada por

$$|A_s|^2 = \sin^2\delta. \qquad \text{(1.12)}$$

### 1.1 Retardo temporal

La cantidad $\delta(E)$ determina el retardo temporal de un paquete de ondas reflejado, en comparación con un paquete de ondas que encontrara un potencial nulo. En efecto, afirmamos que el retardo viene dado por

$$\Delta t = 2\hbar\, \delta'(E), \qquad \text{(1.13)}$$

donde la prima denota derivada respecto del argumento, y la evaluación se realiza para la energía central de la superposición que forma el paquete de ondas. Si $\Delta t < 0$, la partícula pasa menos tiempo cerca de $x = 0$, ya sea porque el potencial es atractivo y la partícula se acelera, o porque el potencial es repulsivo y la partícula rebota antes de alcanzar $x = 0$. Si $\Delta t > 0$, la partícula pasa más tiempo cerca de $x = 0$, típicamente porque se frena o queda temporalmente atrapada en el potencial.

Escribimos la onda entrante en la forma

$$\psi_{\text{inc}}(x,t) = \int_0^\infty dk\, g(k)\, e^{-ikx} e^{-iE(k)t/\hbar}, \qquad x > R, \qquad \text{(1.14)}$$

donde $g(k)$ es una función real con un máximo alrededor de $k = k_0$. Escribimos la onda reflejada asociada notando que lo anterior es una superposición de ondas como en (1.6), y la onda reflejada debe ser la superposición asociada de ondas como en (1.7). Debemos entonces cambiar el signo del momento, cambiar el signo global y multiplicar por la fase $e^{2i\delta}$:

$$\psi_{\text{refl}}(x,t) = -\int_0^\infty dk\, g(k)\, e^{ikx} e^{2i\delta(k)} e^{-iE(k)t/\hbar}, \qquad x > R. \qquad \text{(1.15)}$$

Usamos ahora la aproximación de fase estacionaria para averiguar el movimiento del máximo del paquete de ondas. Debemos tener una fase estacionaria cuando $k = k_0$:

$$0 = \left. \frac{d}{dk}\left(kx + 2\delta(k) - \frac{E(k)t}{\hbar}\right) \right|_{k_0}$$

$$= x + 2\left.\frac{d\delta}{dk}\right|_{k_0} - \left.\frac{dE}{dk}\right|_{k_0}\frac{t}{\hbar}$$

$$= x + 2\left.\frac{dE}{dk}\right|_{k_0} \left.\frac{d\delta}{dE}\right|_{E(k_0)} - \left.\frac{dE}{dk}\right|_{k_0}\frac{t}{\hbar}$$

$$= x + \frac{1}{\hbar}\left.\frac{dE}{dk}\right|_{k=k_0}\left(2\hbar\left.\frac{d\delta}{dE}\right|_{E(k_0)} - t\right)$$

$$= x + \frac{\hbar k_0}{m}\left(2\hbar\left.\frac{d\delta}{dE}\right|_{E(k_0)} - t\right), \qquad \text{(1.16)}$$

lo que da

$$x = \frac{\hbar k_0}{m}\left(t - 2\hbar\left.\frac{d\delta}{dE}\right|_{E(k_0)}\right). \qquad \text{(1.17)}$$

Aquí $\hbar k_0/m$ es la conocida velocidad de grupo $v_0$ del paquete de ondas. Si no hubiera habido desfase $\delta$, digamos porque $V(x) = 0$, no habría retardo temporal y el máximo del paquete de ondas reflejado seguiría la recta $x = v_0 t$. Por lo tanto, el retardo, como se afirmó, viene dado por

$$\Delta t = 2\hbar\, \delta'(E(k_0)). \qquad \text{(1.18)}$$

Podemos comparar el retardo temporal con un tiempo natural del problema. Reescribimos primero

$$\Delta t = 2\hbar\, \frac{dk}{dE}\frac{d\delta}{dk} = \frac{2\dfrac{d\delta}{dk}}{\dfrac{1}{\hbar}\dfrac{dE}{dk}}. \qquad \text{(1.19)}$$

Sabemos que

$$\frac{1}{\hbar}\frac{dE}{dk} = \frac{d\omega}{dk} = v_0, \qquad \text{(1.20)}$$

de modo que podemos escribir entonces

$$\frac{d\delta}{dk} = \frac{\Delta t}{2}v_0. \qquad \text{(1.21)}$$

Multiplicando esto por $\frac{1}{R}$, tenemos

$$\frac{1}{R}\frac{d\delta}{dk} = \frac{\Delta t}{2R/v_0} = \frac{\text{retardo}}{\text{tiempo de tránsito libre}}. \qquad \text{(1.22)}$$

El lado izquierdo carece de unidades, y el lado derecho es el cociente entre el retardo temporal y el tiempo que tardaría la partícula libre en viajar hacia adentro y hacia afuera del rango $R$.

### 1.2 Un ejemplo

Consideremos el siguiente ejemplo en el que tenemos un potencial atractivo:

$$V(x) = \begin{cases} -V_0, & \text{para } 0 < x < a, \\ 0, & \text{para } x > a, \\ \infty, & \text{para } x < 0. \end{cases} \qquad \text{(1.23)}$$

El potencial se muestra en la Figura 4, donde la energía $E > 0$ del autoestado de energía se indica con una línea discontinua. La solución tiene la forma

$$\psi(x) = \begin{cases} e^{i\delta}\sin(kx+\delta) & x > a, \\ A\sin(k'x) & 0 < x < a. \end{cases} \qquad \text{(1.24)}$$

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes18_ES/fig4.png)

Figura 4: Un potencial atractivo. Nos interesa calcular los autoestados de energía para todo $E > 0$.

La solución en la región $x > a$ es simplemente la solución canónica, y la solución en la región $x < a$ se sigue de que debemos tener $\psi(0) = 0$. Las constantes $k$ y $k'$ vienen dadas por

$$k^2 = \frac{2mE}{\hbar^2}, \qquad k'^2 = \frac{2m(E+V_0)}{\hbar^2}. \qquad \text{(1.25)}$$

Haciendo coincidir $\psi$ y $\psi'$ en $x = a$ encontramos las condiciones que finalmente nos darán el desfase desconocido $\delta$:

$$A\sin(k'a) = e^{i\delta}\sin(ka+\delta) \qquad \text{(1.26)}$$

$$k'A\cos(k'a) = k e^{i\delta}\cos(ka+\delta). \qquad \text{(1.27)}$$

Dividiendo la segunda ecuación entre la primera, llegamos a

$$k\cot(ka+\delta) = k'\cot k'a. \qquad \text{(1.28)}$$

Usamos ahora la identidad

$$\cot(A+B) = \frac{\cot A \cot B - 1}{\cot A + \cot B}, \qquad \text{(1.29)}$$

a partir de la cual encontramos

$$\frac{k'}{k}\cot k'a = \cot(ka+\delta) = \frac{\cot ka \cot\delta - 1}{\cot ka + \cot\delta}. \qquad \text{(1.30)}$$

Resolviendo esta ecuación para $\cot\delta$ obtenemos

$$\cot\delta = \frac{\tan ka + \dfrac{k'}{k}\cot k'a}{1 - \dfrac{k'}{k}\cot k'a \tan ka}. \qquad \text{(1.31)}$$

Aunque esta es una fórmula complicada de analizar directamente, siempre podemos graficarla con una computadora para diferentes valores de $V_0$. Como es habitual, caracterizamos el pozo por la constante $z_0$, definida por

$$z_0^2 = \frac{2mV_0 a^2}{\hbar^2}. \qquad \text{(1.32)}$$

Nótese también que

$$k'a = \sqrt{z_0^2 + (ka)^2}. \qquad \text{(1.33)}$$

La Figura 5 muestra el factor de fase $\delta$, la cantidad $\sin^2\delta$, el retardo temporal $\frac{1}{a}\frac{d\delta}{dk}$, y la amplitud $|A|$ dentro del pozo como funciones de $ka$, para $z_0^2 = 3.40$.

Nótese que la fase $\delta$ comienza en $0$ para energía nula y alcanza $-\pi$ para energía infinita. La excursión de la fase es entonces $\pi$ y, como veremos, esto ocurre porque para este valor de $z_0$ el potencial tendría un estado ligado.

El valor de $|A_s|^2 = \sin^2\delta$ representa la probabilidad de dispersión y alcanza su máximo para el valor de $ka$ en el que la fase $\delta$ tiene valor absoluto $\pi/2$.

A continuación en la gráfica está el retardo adimensional $\frac{1}{a}\frac{d\delta}{dk}$. Nótese que el retardo es negativo. Esto se explica fácilmente: al moverse la partícula sobre el pozo, su energía cinética aumenta en $V_0$, la partícula se acelera al llegar y rebotar contra la pared.

La última gráfica muestra la magnitud $|A|$ de la constante que da la amplitud de la función de onda en la región $0 < x < a$.

A energía muy grande $E \gg V_0$, la partícula apenas nota el potencial. En efecto, vemos que $\delta$ se aproxima a $-\pi$, lo cual, como se señaló bajo (1.8), es equivalente a $\delta = 0$ y significa que no hay desfase. En consecuencia $\sin^2\delta \to 0$, lo que significa que no hay dispersión. También tenemos $\frac{1}{a}\frac{d\delta}{dk} \to 0$, lo que significa que no hay retardo temporal y, finalmente, $|A| \to 1$ como en la solución libre.

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes18_ES/fig5.png)

Figura 5: Varias cantidades graficadas en función de $ka$, para $z_0^2 = 3.40$. Arriba: el desfase, yendo de cero a $-\pi$. Segundo: la amplitud de dispersión $|A_s|^2 = \sin^2\delta$. Tercero: el retardo relativo al tiempo de tránsito libre. Último: la norma $|A|$ de la amplitud de la onda dentro del pozo.

*Andrew Turner transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare https://ocw.mit.edu

8.04 Física Cuántica I Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.
