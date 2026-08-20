# Lección 11

## Vídeos de esta clase (YouTube)

**Lección 11: Uncertainty (cont.). Stationary states. Particle on a circle.**

- [Energy eigenstates for particle on a circle](https://www.youtube.com/watch?v=e0C1Bkcjrdc)
- [Infinite square well energy eigenstates](https://www.youtube.com/watch?v=gMHkf-107Sw)
- [Finite square well energy eigenstates](https://www.youtube.com/watch?v=jd4es6Bo600)

------------------------------------------------------------------------

B. Zwiebach

17 de marzo de 2016

## Contenido

1.  El pozo cuadrado infinito
2.  El pozo cuadrado finito

## 1. El pozo cuadrado infinito

En nuestra última lección examinamos la función de onda cuántica de una partícula que se mueve en un círculo. Aquí introducimos otro modelo de juguete instructivo, el potencial de pozo cuadrado infinito. Este obliga a una partícula a vivir en un intervalo de la recta real, intervalo que convencionalmente se elige como $x \in [0, a]$. En los extremos $0$ y $a$ del intervalo hay paredes duras que impiden que la partícula vaya a $x > a$ y $x < 0$.

El potencial se define de la siguiente manera y se muestra en la figura 1.

$$V(x) =
\begin{cases}
0, & 0 < x < a, \\
\infty, & x \leq 0,\ x \geq a
\end{cases}
\qquad \text{(1.1)}$$

Es razonable suponer que la función de onda debe anularse en la región donde el potencial es infinito.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes11_ES/fig1.png)

Figura 1: El potencial de pozo cuadrado infinito.

Clásicamente, cualquier región donde el potencial exceda la energía de la partícula está prohibida. No así en mecánica cuántica. Pero incluso en mecánica cuántica una partícula no puede estar en una región de potencial infinito. Podremos justificar estas afirmaciones estudiando el pozo cuadrado finito, más complicado, en el límite en que la altura del potencial tiende a infinito. Pero por el momento simplemente establecemos el hecho:

$$\psi(x) = 0 \quad \text{para } x < 0 \text{ y para } x > a. \qquad \text{(1.2)}$$

Dado que la función de onda debe ser continua, debemos tener que se anule en $x = 0$ y en $x = a$:

1.  $\psi(x = 0) = 0$.
2.  $\psi(x = a) = 0$.

Estas son nuestras condiciones de frontera. Podría preguntarse acerca de la continuidad de la primera derivada $\psi'(x)$. Esta derivada se anula fuera del intervalo, y la continuidad diría que $\psi'$ debería anularse en $0$ y en $a$. Pero esto es imposible. ¡Una solución de la ecuación de Schrödinger (una ecuación diferencial de segundo orden) para la cual tanto la función de onda como su derivada se anulan en un punto es idénticamente cero! Si existe una solución, debemos aceptar que $\psi'$ puede tener discontinuidades en una pared infinita. Por lo tanto, no imponemos ninguna condición de frontera sobre $\psi'$. Las dos condiciones anteriores bastarán para hallar una solución. En esa solución, $\psi'$ es discontinua en los extremos.

En la región $x \in [0, a]$ el potencial se anula y la ecuación de Schrödinger toma la forma

$$\frac{d^2\psi}{dx^2} = -\frac{2mE}{\hbar^2}\psi, \qquad \text{(1.3)}$$

y, como hicimos antes, se puede demostrar que la energía $E$ debe ser positiva (¡hágalo!). Esto nos permite definir, como es habitual, una cantidad real $k$ tal que

$$k^2 \equiv \frac{2mE}{\hbar^2} \quad \Rightarrow \quad E = \frac{\hbar^2 k^2}{2m}. \qquad \text{(1.4)}$$

La ecuación diferencial es entonces

$$\frac{d^2\psi}{dx^2} = -k^2\psi, \qquad \text{(1.5)}$$

y la solución general puede escribirse como

$$\psi(x) = c_1 \cos kx + c_2 \sin kx, \qquad \text{(1.6)}$$

con constantes $c_1$ y $c_2$ por determinar. Para esto usamos nuestras condiciones de frontera.

La condición $\psi(x = 0) = 0$ implica que $c_1$ en la ecuación 1.6 debe ser cero. El coeficiente de $\sin kx$ no necesita serlo, ya que esta función se anula automáticamente en $x = 0$. Por lo tanto, la solución hasta ahora es

$$\psi(x) = c_2 \sin kx. \qquad \text{(1.7)}$$

Nótese que si exigiéramos la continuidad de $\psi'$ tendríamos que pedir $\psi'(x = 0) = 0$, y eso haría que $c_2$ fuera igual a cero, con lo cual $\psi$ sería idénticamente cero. Eso no es una solución. No hay partícula si $\psi = 0$.

En este punto debemos imponer la anulación de $\psi$ en $x = a$.

$$c_2 \sin ka = 0 \quad \Rightarrow \quad ka = n\pi \quad \Rightarrow \quad k_n = \frac{n\pi}{a}. \qquad \text{(1.8)}$$

Aquí $n$ debe ser un entero, y la solución sería

$$\psi_n(x) = N \sin\left(\frac{n\pi x}{a}\right), \qquad \text{(1.9)}$$

con $N$ una constante de normalización. ¿Qué enteros $n$ son aceptables aquí? Bueno, $n = 0$ no es aceptable, porque haría que la función de onda fuera cero. Además, $n$ y $-n$ dan la misma función de onda, salvo por un signo. Como el signo de una función de onda es irrelevante, sería doble conteo incluir tanto valores positivos como negativos de $n$. Nos restringimos a que $n$ sea un entero positivo.

Para resolver el coeficiente, utilizamos la condición de normalización; cada $\psi_n(x)$ debe estar normalizada.

$$1 = N^2 \int_0^a \sin^2\left(\frac{n\pi x}{a}\right) dx = N^2 \cdot \frac{a}{2} \quad \Rightarrow \quad N = \sqrt{\frac{2}{a}}. \qquad \text{(1.10)}$$

Por lo tanto, en definitiva, nuestras soluciones son:

$$\psi_n = \sqrt{\frac{2}{a}} \sin\left(\frac{n\pi x}{a}\right), \qquad E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{\hbar^2 \pi^2 n^2}{2ma^2}, \qquad n = 1, 2, \dots. \qquad \text{(1.11)}$$

Cada valor de $n$ da una energía diferente, lo que implica que en el pozo cuadrado infinito unidimensional ¡no hay degeneraciones en el espectro de energía! El estado fundamental —el estado de menor energía— corresponde a $n = 1$ y tiene energía distinta de cero.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes11_ES/fig2.png)

Figura 2: Los cuatro autoestados de energía más bajos para el potencial de pozo cuadrado infinito. La función de onda solución $n$-ésima $\psi_n$ tiene $n - 1$ nodos. Las soluciones son alternadamente simétricas y antisimétricas respecto al punto medio $x = a/2$.

La figura 2 muestra las primeras cuatro soluciones del pozo cuadrado infinito 1-d, etiquetadas de $n = 1$ a $n = 4$. Notamos algunas características:

1.  El estado fundamental $n = 1$ no tiene nodos. Un nodo es un cero de la función de onda que no está en los extremos del dominio de la función de onda. Los ceros en $x = 0$ y $x = a$ no cuentan como nodos. Claramente $\psi_1(x)$ no se anula en ninguna parte del interior de $[0, a]$ y por lo tanto no tiene nodos. De hecho, es cierto que cualquier estado fundamental normalizable de un potencial unidimensional no tiene nodos.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes11_ES/fig3.png)

Figura 3: El pozo cuadrado infinito desplazado hacia la izquierda para hacerlo simétrico respecto al origen.

1.  El primer estado excitado, $n = 2$, tiene un nodo. Está en $x = a/2$, el punto medio del intervalo. El segundo estado excitado, $n = 3$, tiene dos nodos. El patrón de hecho continúa. El $n$-ésimo estado excitado tendrá $n$ nodos.

2.  En la figura, la línea vertical punteada marca el punto medio del intervalo $x = a/2$. Observamos que el estado fundamental es simétrico bajo reflexión respecto a $x = a/2$. El primer estado excitado es antisimétrico; de hecho, su nodo está en $x = a/2$. El segundo estado excitado es nuevamente simétrico. La simetría y la antisimetría se alternan indefinidamente.

3.  La simetría que acabamos de notar no es accidental. Se cumple, en general, para potenciales $V(x)$ que son funciones pares de $x$: $V(-x) = V(x)$. Nuestro potencial no satisface esta ecuación, pero esto podría haberse cambiado fácilmente y sin consecuencias. Podríamos desplazar el pozo de manera que, en lugar de tener $V(x) = 0$ desde $0 \leq x \leq a$, se extienda desde $-a/2 \leq x \leq a/2$ y entonces sería simétrico respecto al origen $x = 0$ (véase la figura 3). Más adelante demostraremos que los estados ligados de un potencial unidimensional par ¡son pares o impares! Aquí solo estamos viendo un ejemplo de tal resultado.

4.  Las funciones de onda $\psi_n(x)$ con $n = 1, 2, \dots$ forman un conjunto completo que puede utilizarse para expandir cualquier función en el intervalo $x \in [0, a]$ que se anule en los extremos. Si la función no se anula en los extremos, la convergencia de la expansión es delicada, y físicamente tal función de onda sería problemática, ya que se puede verificar que el valor esperado de la energía es infinito.

## 2. El pozo cuadrado finito

Ahora examinamos el pozo cuadrado finito, definido de la siguiente manera y mostrado en la figura 4.

$$V(x) =
\begin{cases}
-V_0, & \text{para } |x| \leq a, \ V_0 > 0, \\
0, & \text{para } |x| \geq a.
\end{cases}
\qquad \text{(2.12)}$$

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes11_ES/fig4.png)

Figura 4: El potencial de pozo cuadrado finito.

Nótese que la energía potencial es cero para $|x| > a$. La energía potencial es negativa e igual a $-V_0$ dentro del pozo, porque definimos $V_0$ como un número positivo. El ancho del pozo es $2a$. Nótese también que hemos colocado el fondo del pozo de manera diferente que en el caso del pozo cuadrado infinito. El fondo del pozo cuadrado infinito estaba en energía potencial cero. Si quisiéramos obtener el pozo cuadrado infinito como límite del pozo cuadrado finito, tendríamos que llevar $V_0$ a infinito, pero se necesita cuidado al comparar energías. Las del pozo cuadrado infinito se miden con respecto a un fondo en energía cero. Las del pozo cuadrado finito se miden con respecto a un fondo en $-V_0$.

Estaremos interesados en estados ligados, es decir, autoestados de energía que sean normalizables. Para esto, la energía $E$ de los estados debe ser negativa. Esto se entiende fácilmente. Si $E > 0$, cualquier solución en la región $x > a$ donde el potencial se anula sería una onda plana, extendiéndose hasta el infinito. Tal solución no sería normalizable. La energía $E$ se muestra como una línea discontinua en la figura. Tenemos

$$-V_0 < E < 0. \qquad \text{(2.13)}$$

Nótese que, como $E$ es negativa, tenemos $E = -|E|$. Para un estado ligado de energía $E$, la energía $\tilde{E}$ medida con respecto al fondo del potencial es

$$\tilde{E} = E - (-V_0) = V_0 - |E| > 0. \qquad \text{(2.14)}$$

Esas $\tilde{E}$ son las que se pueden comparar con las energías del pozo cuadrado infinito en el límite en que $V_0 \to \infty$.

¿Cuáles son las soluciones de estado ligado de la ecuación de Schrödinger con este potencial? Tenemos que examinar cómo se ve la ecuación en las diversas regiones donde el potencial es constante y luego usar condiciones de frontera para acoplar las soluciones a través de los puntos donde el potencial es discontinuo. Tenemos la ecuación; examinemos las regiones, donde, por simplicidad, definimos $\alpha(x)$ mediante

$$\frac{d^2\psi}{dx^2} = -\frac{2m}{\hbar^2}\big(E - V(x)\big)\psi = \alpha(x)\psi, \qquad \text{(2.15)}$$

donde hemos definido el factor $\alpha(x)$ que multiplica a la función de onda en el lado derecho de la ecuación de Schrödinger. Consideramos entonces las dos regiones:

- Región $|x| > a$: $\alpha(x)$ es una constante positiva. La función de onda en esta región se construye con exponenciales reales.

- Región $|x| < a$: $\alpha(x)$ es una constante negativa. La función de onda en esta región se construye con funciones trigonométricas.

El potencial $V(x)$ del pozo cuadrado finito es una función par de $x$: $V(-x) = V(x)$. Podemos, por lo tanto, usar el teorema citado anteriormente (¡y demostrado más adelante!) de que para un potencial par los estados ligados son o simétricos o antisimétricos. Comenzamos buscando soluciones pares, es decir, soluciones $\psi$ para las cuales $\psi(-x) = \psi(x)$.

**Soluciones pares.** Dado que el potencial es continuo a trozos, debemos estudiar la ecuación diferencial en dos regiones:

- $|x| < a$

$$\frac{d^2\psi}{dx^2} = -\frac{2m}{\hbar^2}\big(E - (-V_0)\big)\psi = -\frac{2m}{\hbar^2}\big(V_0 - |E|\big)\psi \qquad \text{(2.16)}$$

$V_0 - |E|$ es una constante positiva; por lo tanto, definimos un $k > 0$ real mediante

$$k^2 \equiv \frac{2m}{\hbar^2}\big(V_0 - |E|\big) > 0, \qquad k > 0. \qquad \text{(2.17)}$$

Es interesante notar que esta ecuación no es muy diferente de la ecuación de partícula libre $k^2 = 2mE/\hbar^2$. En efecto, $V_0 - |E|$ es la energía cinética de la partícula y, por lo tanto, $k$ tiene la interpretación usual. La ecuación diferencial a resolver ahora es

$$\psi'' = -k^2\psi, \qquad \text{(2.18)}$$

para la cual la única solución par posible es

$$\psi(x) = \cos kx, \qquad |x| < a. \qquad \text{(2.19)}$$

No incluimos una constante de normalización porque, en esta etapa, no buscamos autoestados normalizados. Obtendremos un autoestado y, aunque no estará normalizado, será normalizable, y eso es todo lo esencial. Lo que buscamos son las energías posibles. Las funciones de onda normalizadas serían útiles para calcular valores esperados.

- $|x| > a$

$$\psi'' = -\frac{2m}{\hbar^2}(E - 0)\psi = \frac{2m|E|}{\hbar^2}\psi \qquad \text{(2.20)}$$

Esta vez definimos una constante real positiva $\kappa$ mediante la relación

$$\kappa^2 = \frac{2m|E|}{\hbar^2}, \qquad \kappa > 0. \qquad \text{(2.21)}$$

La ecuación diferencial a resolver ahora es

$$\psi'' = \kappa^2\psi, \qquad \text{(2.22)}$$

y las soluciones son exponenciales. De hecho, necesitamos exponenciales que decaigan cuando $x \to \pm\infty$, ya que de lo contrario la función de onda no sería normalizable. Esto debería ser físicamente intuitivo: en una región clásicamente prohibida, la probabilidad de estar lejos del pozo debe ser desvanecientemente pequeña. Para $x > a$ elegimos la exponencial decreciente

$$\psi(x) = A\, e^{-\kappa x}, \qquad x > a, \qquad \text{(2.23)}$$

donde $A$ es una constante de normalización a determinar por las condiciones de frontera. De manera más general, dado que la solución es par, tenemos

$$\psi(x) = A\, e^{-\kappa|x|}, \qquad |x| > a. \qquad \text{(2.24)}$$

Ahora es útil notar que $\kappa^2$ y $k^2$ satisfacen una relación simple. Usando sus definiciones anteriores vemos que la energía $|E|$ se cancela en su suma, y tenemos

$$k^2 + \kappa^2 = \frac{2mV_0}{\hbar^2}. \qquad \text{(2.25)}$$

En este punto avanzamos introduciendo constantes adimensionales $\xi$, $\eta$ y $z_0$ de la siguiente manera:

$$\eta \equiv ka > 0, \qquad \xi \equiv \kappa a > 0, \qquad z_0^2 \equiv \frac{2mV_0 a^2}{\hbar^2}. \qquad \text{(2.26)}$$

Claramente $\xi$ es un sustituto de $\kappa$ y $\eta$ es un sustituto de $k$. Ambos dependen de la energía del estado ligado. El parámetro $z_0$, adimensional, solo depende de los datos asociados al potencial (la profundidad $V_0$ y el ancho $2a$) y de la masa $m$ de la partícula. Si se da un potencial, se conoce el número $z_0$. Un potencial muy profundo y/o ancho tiene un $z_0$ muy grande, mientras que un potencial muy poco profundo y/o estrecho tiene un $z_0$ pequeño. Como veremos, el valor de $z_0$ nos indica cuántos estados ligados tiene el pozo cuadrado.

Multiplicando (2.25) por $a^2$ y usando nuestras definiciones anteriores obtenemos

$$\eta^2 + \xi^2 = z_0^2. \qquad \text{(2.27)}$$

Dejemos claro que resolver para $\xi$ es en realidad como resolver para la energía. De la ecuación (2.21), podemos ver

$$\xi^2 = \kappa^2 a^2 = \frac{2m|E|a^2}{\hbar^2} = \frac{2mV_0 a^2}{\hbar^2}\cdot\frac{|E|}{V_0} = z_0^2\,\frac{|E|}{V_0}, \qquad \text{(2.28)}$$

y de esto obtenemos

$$\frac{|E|}{V_0} = \frac{\xi^2}{z_0^2}. \qquad \text{(2.29)}$$

Esta es una ecuación agradable: el lado izquierdo da la energía como fracción de la profundidad $V_0$ del pozo, y el lado derecho involucra $\xi$ y la constante $z_0$ del potencial. La cantidad $\eta$ también codifica la energía de una manera ligeramente diferente. De (2.17) tenemos

$$\eta^2 = k^2 a^2 \equiv \frac{2ma^2}{\hbar^2}\big(V_0 - |E|\big), \qquad \text{(2.30)}$$

y usando (2.14) vemos que esto proporciona la energía $\tilde{E}$, medida con respecto al fondo del potencial:

$$\tilde{E} = V_0 - |E| = \eta^2\,\frac{\hbar^2}{2ma^2}. \qquad \text{(2.31)}$$

Esta fórmula es conveniente para entender cómo aparecen los niveles de energía del pozo cuadrado infinito en el límite en que la profundidad del pozo finito tiende a infinito. Nótese que la respuesta anterior para las energías está dada por el número adimensional $\eta$ multiplicado por la energía característica de un pozo infinito de ancho $a$.

Completemos finalmente la construcción. Debemos imponer la continuidad de la función de onda y la continuidad de $\psi'$ en $x = a$. Usando las expresiones para $\psi$ para $x < a$ y para $x > a$, estas condiciones dan

$$\psi \text{ continua en } x = a \ \Rightarrow \ \cos(ka) = A e^{-\kappa a}$$

$$\psi' \text{ continua en } x = a \ \Rightarrow \ -k\sin(ka) = -\kappa A e^{-\kappa a}, \qquad \text{(2.32)}$$

Dividiendo la segunda ecuación por la primera eliminamos la constante $A$ y encontramos una segunda relación entre $k$ y $\kappa$. ¡Esto es exactamente lo que se necesita! El resultado es

$$k\tan ka = \kappa \quad \Rightarrow \quad ka\tan ka = \kappa a \quad \Rightarrow \quad \xi = \eta \tan \eta. \qquad \text{(2.33)}$$

Nuestra tarea de hallar los estados ligados se reduce ahora a hallar soluciones de las ecuaciones simultáneas

$$\text{Soluciones pares: } \quad \eta^2 + \xi^2 = z_0^2, \qquad \xi = \eta\tan\eta, \qquad \xi, \eta > 0. \qquad \text{(2.34)}$$

Estas ecuaciones pueden resolverse numéricamente para hallar todas las soluciones que existen para un valor fijo dado de $z_0$. Cada solución representa un estado ligado. Podemos entender el espacio de soluciones graficando estas dos ecuaciones en el primer cuadrante de un plano $(\eta, \xi)$, como se muestra en la figura 5.

La primera ecuación en (2.34) es un trozo de una circunferencia de radio $z_0$. La segunda ecuación, $\xi = \eta \tan \eta$, da infinitas curvas a medida que $\eta$ crece de cero a infinito. El valor de $\xi$ tiende a infinito a medida que $\eta$ se aproxima a cada múltiplo impar de $\pi/2$. Los estados ligados están representados por las intersecciones en la gráfica (puntos gruesos).

En la figura vemos dos intersecciones, lo que significa dos estados ligados. La primera intersección ocurre cerca de $\eta = \pi/2$ y con $\xi$ grande, $\xi \sim z_0$. Este es el estado fundamental, o el estado ligado más profundamente unido. Esto puede verse a partir de (2.29). Alternativamente, puede verse a partir de la ecuación (2.31), notando que esta es la solución con menor $\eta$. La segunda solución ocurre para $\eta$ cerca de $3\pi/2$. A medida que el radio de la circunferencia se hace más grande, obtenemos más y más intersecciones; $z_0$ controla el número de estados ligados pares. Finalmente, nótese que siempre existe una solución par, sin importar cuán pequeño sea $z_0$, porque el arco de la circunferencia siempre intersectará la primera curva de la gráfica $\xi = \eta \tan \eta$. Por lo tanto, siempre existe al menos un estado ligado, sin importar cuán poco profundo sea el pozo finito.

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes11_ES/fig5.png)

Figura 5: Representación gráfica de las ecuaciones simultáneas (2.34). Las intersecciones de la circunferencia con la función $\eta \tan \eta$ representan las soluciones de estado ligado par en el potencial de pozo cuadrado finito. El estado ligado más profundo es el de menor $\eta$.

![Figura 6](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes11_ES/fig6.png)

Figura 6: Representación gráfica de (2.36). Las intersecciones de la circunferencia con las curvas $\xi = -\eta \cot \eta$ son soluciones de estado ligado impar en el potencial de pozo cuadrado finito. En el caso mostrado hay solo un estado ligado.

**Soluciones impares.** Para las soluciones impares, todas nuestras definiciones ($k$, $\kappa$, $z_0$, $\eta$, $\xi$) permanecen iguales. La función de onda ahora tiene la forma

$$\psi(x) =
\begin{cases}
\sin kx, & |x| < a \\
A e^{-\kappa|x|}, & |x| > a
\end{cases}
\qquad \text{(2.35)}$$

Acoplando $\psi$ y $\psi'$ en $x = a$ ahora da $\xi = -\eta\cot\eta$ (¡hágalo!). Como resultado, las ecuaciones simultáneas relevantes son ahora

$$\text{Soluciones impares: } \quad \eta^2 + \xi^2 = z_0^2, \qquad \xi = -\eta\cot\eta, \qquad \xi,\eta > 0. \qquad \text{(2.36)}$$

En la figura 6 la curva $\xi = -\eta\cot\eta$ no aparece para $\eta < \pi/2$ porque $\xi$ es entonces negativa. Para $z_0 < \pi/2$ no hay soluciones de estado ligado impar, pero aún tenemos el estado ligado par.

Podríamos haber anticipado la cuantización de la energía mediante el siguiente argumento. Suponga que intenta calcular autoestados de energía que, en lo que respecta a resolver la ecuación de Schrödinger, están determinados salvo por una normalización global. Suponga que no sabe que la energía está cuantizada y fija alguna energía arbitraria y calcula. Tanto en el caso par como en el impar, podemos fijar el coeficiente de la función $\sin kx$ o $\cos kx$ dentro del pozo igual a uno. El coeficiente de la exponencial decreciente fuera del pozo estaba indeterminado; lo llamamos $A$. Por lo tanto, tenemos solo una incógnita, $A$. Pero tenemos dos ecuaciones, porque imponemos la continuidad de $\psi$ y de $\psi'$ en $x = a$. Si tenemos una incógnita y dos ecuaciones, no hay razón para creer que existe una solución. De hecho, generalmente no la hay. Pero entonces, si pensamos en la energía $E$ como una incógnita, esa energía aparece en varios lugares de las ecuaciones (en $k$ y $\kappa$) y, por lo tanto, teniendo dos incógnitas $A$ y $E$ y dos ecuaciones, deberíamos esperar ¡una única solución! Esto es precisamente lo que ocurrió.

![Figura 7](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes11_ES/fig7.png)

Figura 7: Esquema de los autoestados de energía de un potencial de pozo cuadrado finito. Las energías son $E_1 < E_2 < E_3$.

En la figura 7 esbozamos los autoestados de energía de un potencial de pozo cuadrado con tres estados ligados de energías $E_1 < E_2 < E_3$. Algunas características de las funciones de onda son evidentes: alternan entre par, impar y par. Tienen cero, uno y dos nodos, respectivamente. La segunda derivada de $\psi$ es negativa para $|x| < a$ y positiva para $|x| > a$ (de hecho, es discontinua en $x = \pm a$). El decaimiento exponencial en la región $|x| > a$ es más rápido para el estado fundamental y más lento para el estado menos ligado.

*Sarah Geller transcribió los apuntes de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare

https://ocw.mit.edu

8.04 Física Cuántica I

Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.
