# Lección 13: El Potencial de Función Delta, el Teorema del Nodo y el Oscilador Armónico Simple

## Vídeos de esta clase (YouTube)

**Lección 13: Delta function potential. Justifying the node theorem. Simple harmonic oscillator.**

- [Delta function potential I: Preliminaries](https://www.youtube.com/watch?v=vcuY46RwoV0)
- [Delta function potential I: Solving for the bound state](https://www.youtube.com/watch?v=1dW_izzvfOk)
- [Node Theorem](https://www.youtube.com/watch?v=NwPOhzDPHKc)
- [Harmonic oscillator: Differential equation](https://www.youtube.com/watch?v=sxzFpOsvfgU)
- [Behavior of the differential equation](https://www.youtube.com/watch?v=eNf8nH1yEYc)

------------------------------------------------------------------------

*B. Zwiebach* *1 de abril de 2016*

## Contenido

1.  El potencial de función delta
2.  El teorema del nodo
3.  Oscilador armónico

## 1. El potencial de función delta

Consideremos una partícula de masa $m$ moviéndose en un potencial unidimensional. El potencial $V(x)$ es bastante singular: se anula para todo $x$ excepto en $x = 0$, punto en el que tiene intensidad infinita. Más precisamente, el potencial está localizado en una función delta en $x = 0$ y se escribe como

$$V(x) = -\alpha\,\delta(x), \qquad \alpha > 0, \qquad \text{(1.1)}$$

Aquí $\alpha$ es una constante elegida positiva. Debido al signo menos explícito, el potencial es infinitamente negativo en $x = 0$; el potencial es atractivo. El potencial se muestra en la Figura 1, donde representamos la función delta mediante una flecha que apunta hacia abajo.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes13_ES/fig1.png)

Figura 1: Un pozo de función delta.

Queremos saber si este potencial admite estados ligados. Para un estado ligado, la energía $E$ debe ser negativa: esto asegura que toda la región $x \neq 0$ sea clásicamente prohibida, y la función de onda decaerá rápidamente permitiendo una solución normalizada. Se obtiene algo de intuición pensando en la función delta como aproximada por un pozo cuadrado finito en el límite en que el ancho del pozo tiende a cero y la profundidad tiende a infinito de tal manera que el producto, que representa el “área”, sea finito (la función delta es una función de área unitaria, como resulta claro de su integral). En la Figura 2 mostramos dos representaciones mediante pozos finitos y esbozamos la función de onda. Podemos ver que la región central proporciona la curvatura de la función de onda necesaria para tener una derivada suave. En el límite en que el ancho de la región tiende a cero, esperaríamos, si existe un estado ligado, tener una derivada discontinua.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes13_ES/fig2.png)

Figura 2: El potencial de función delta visto como el límite en que el pozo cuadrado finito se vuelve simultáneamente más estrecho y más profundo. Esperamos obtener una función de onda con derivada discontinua.

Podemos obtener más información considerando las unidades. Las constantes dimensionales del problema son $\alpha$, $m$ y $\hbar$. Puesto que una función delta tiene unidades de uno sobre longitud, la constante $\alpha$ debe tener unidades de energía por longitud para que el potencial tenga unidades de energía. Así, tenemos, como unidades,

$$E = \frac{\alpha}{L}, \qquad \text{(1.2)}$$

pero, como es habitual, las unidades de energía son

$$E = \frac{\hbar^2}{mL^2}. \qquad \text{(1.3)}$$

De estas dos ecuaciones encontramos

$$L = \frac{\hbar^2}{m\alpha} \quad\rightarrow\quad E = \frac{m\alpha^2}{\hbar^2}. \qquad \text{(1.4)}$$

Las unidades de energía deben ser transportadas por la combinación anterior de las constantes del problema. Por lo tanto, la energía $E_b$ de cualquier estado ligado debe ser un número multiplicado por esa combinación:

$$E_b = -\#\,\frac{m\alpha^2}{\hbar^2}. \qquad \text{(1.5)}$$

donde $\#$ es un número positivo sin unidades que nos proponemos determinar. Es bueno ver que $\alpha$ aparece en el numerador. Esto significa que, a medida que aumenta la intensidad de la función delta, también aumenta la profundidad del estado ligado, ¡tal como cabría esperar naturalmente!

Pasemos ahora a las ecuaciones relevantes. Queremos encontrar un estado con $E < 0$. La función de onda está restringida por la ecuación de Schrödinger independiente del tiempo

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = (E - V(x))\psi. \qquad \text{(1.6)}$$

Para $x \neq 0$, tenemos $V(x) = 0$, de modo que esto se convierte en

$$\frac{d^2\psi}{dx^2} = -\frac{2mE}{\hbar^2}\psi = \kappa^2\psi, \qquad \kappa^2 \equiv -\frac{2mE}{\hbar^2} > 0. \qquad \text{(1.7)}$$

Las soluciones de esta ecuación diferencial tienen la forma

$$e^{\kappa x}, \qquad e^{-\kappa x}, \qquad \kappa > 0. \qquad \text{(1.8)}$$

El potencial es par: $\delta(-x) = \delta(x)$, de modo que si tenemos un estado fundamental este debe ser par y, por supuesto, no tener nodos. Si existe un estado excitado, debe ser impar y por lo tanto tener un nodo en $x = 0$. La única solución impar que podemos construir con las exponenciales anteriores es $\sinh \kappa x$. Pero una $\psi \sim \sinh \kappa x$ no puede normalizarse, pues diverge en $x = \pm\infty$. Por lo tanto, no puede haber un estado excitado en el potencial de función delta. Si hay estados ligados, ¡hay exactamente uno!

Usemos las soluciones anteriores para construir la función de onda del estado fundamental. Primero, podemos ver que para $x > 0$ debemos descartar la solución $e^{\kappa x}$, porque diverge cuando $x \to \infty$. De manera similar, debemos descartar $e^{-\kappa x}$ para $x < 0$. Puesto que la función de onda debe ser continua en $x = 0$, la solución debe tener la forma

$$\psi(x) = \begin{cases} A\,e^{-\kappa x} & x > 0, \\ A\,e^{\kappa x} & x < 0. \end{cases} \qquad \text{(1.9)}$$

¿Se permite cualquier valor de $\kappa$ para esta solución? No, obtendremos otra restricción al considerar la derivada de la función de onda y comprobar que, como anticipamos, es discontinua. En efecto, la ecuación de Schrödinger nos proporciona una restricción para esta discontinuidad. Partiendo de

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi = E\psi, \qquad \text{(1.10)}$$

integramos esta ecuación desde $-\epsilon$ hasta $\epsilon$, con $0 < \epsilon \ll 1$, un rango que incluye la posición de la función delta. Esto da

$$-\frac{\hbar^2}{2m}\left[\left.\frac{d\psi}{dx}\right|_{\epsilon} - \left.\frac{d\psi}{dx}\right|_{-\epsilon}\right] + \int_{-\epsilon}^{\epsilon} dx\,(-\alpha\delta(x))\psi(x) = E\int_{-\epsilon}^{\epsilon} dx\,\psi(x). \qquad \text{(1.11)}$$

La integral del lado izquierdo devuelve un valor finito debido a la función delta. En el límite $\epsilon \to 0$ la integral del lado derecho se anula porque $\psi(x)$ es finita para todo $x$, mientras que la región de integración se contrae hasta desaparecer. Esto produce

$$-\frac{\hbar^2}{2m}\lim_{\epsilon \to 0}\left[\left.\frac{d\psi}{dx}\right|_{\epsilon} - \left.\frac{d\psi}{dx}\right|_{-\epsilon}\right] - \alpha\psi(0) = 0. \qquad \text{(1.12)}$$

Definimos la discontinuidad $\Delta_0$ de $\psi'$ en $x = 0$ como

$$\Delta_0\!\left(\frac{d\psi}{dx}\right) \equiv \lim_{\epsilon \to 0}\left[\left.\frac{d\psi}{dx}\right|_{\epsilon} - \left.\frac{d\psi}{dx}\right|_{-\epsilon}\right]. \qquad \text{(1.13)}$$

Hemos aprendido entonces que

$$\Delta_0\!\left(\frac{d\psi}{dx}\right) = -\frac{2m\alpha}{\hbar^2}\psi(0). \qquad \text{(1.14)}$$

Nótese que la discontinuidad en $\psi'$ en la posición de la función delta es proporcional al valor de la función de onda en ese punto. En un nodo, una función delta no tendría efecto alguno; $\psi'$ también sería continua allí.

Aplicando la ecuación de discontinuidad a nuestra solución (1.9), tenemos

$$\lim_{\epsilon \to 0}\left[\left.\frac{d\psi}{dx}\right|_{\epsilon} - \left.\frac{d\psi}{dx}\right|_{-\epsilon}\right] = \lim_{\epsilon \to 0}\left[-\kappa A e^{-\kappa\epsilon} - \kappa A e^{-\kappa\epsilon}\right] = -2\kappa A = -\frac{2m\alpha}{\hbar^2}A. \qquad \text{(1.15)}$$

Esta relación fija el valor de $\kappa$

$$\kappa = \frac{m\alpha}{\hbar^2}, \qquad \text{(1.16)}$$

y por lo tanto el valor $E_b$ de la energía del estado ligado

$$E_b = -\frac{\hbar^2\kappa^2}{2m} = -\frac{1}{2}\cdot\frac{m\alpha^2}{\hbar^2}. \qquad \text{(1.17)}$$

Como anticipamos con el análisis de unidades, la respuesta toma la forma requerida (1.5) y la constante indeterminada $\#$ toma el valor $1/2$.

## 2. El teorema del nodo

Recordemos el potencial de pozo infinito

$$V(x) = \begin{cases} 0 & 0 < x < a, \\ \infty & \text{en cualquier otro caso.} \end{cases} \qquad \text{(2.18)}$$

Los estados ligados tienen la forma

$$\psi_n(x) = \sqrt{\frac{2}{a}}\sin\!\left(\frac{n\pi x}{a}\right) \qquad \text{(2.19)}$$

y las energías correspondientes

$$E_n = \frac{\hbar^2 n^2 \pi^2}{2ma^2}, \qquad n = 1, 2, \dots \qquad \text{(2.20)}$$

Nótese que $\psi_n$ tiene $n - 1$ nodos (ceros). (Los puntos $x = 0$ y $x = a$ no son nodos, sino extremos.)

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes13_ES/fig3.png)

Figura 3: Un potencial suave que tiende a infinito cuando $|x| \to \infty$.

Esto nos lleva al teorema del nodo. Consideremos un potencial $V(x)$ que es continuo y satisface $V(x) \to \infty$ cuando $|x| \to \infty$ (Fig. 3). Este potencial tiene un cierto número de estados ligados (autoestados de energía que satisfacen $\psi \to 0$ cuando $|x| \to \infty$), que indexamos como $\psi_1, \psi_2, \psi_3, \dots$. Recordemos también que no existen estados ligados degenerados en una dimensión. El teorema del nodo establece que $\psi_n$ tiene $n - 1$ nodos. Daremos una explicación intuitiva, no rigurosa, de este fenómeno.

Para este argumento recordamos también que $\psi(x_0) = \psi'(x_0) = 0$ implica que $\psi(x) = 0$ para todo $x$. No se puede tener derivada nula en un cero de la función de onda. Esto se aplica tanto a nodos como a extremos finitos.

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes13_ES/fig4.png)

Figura 4: El potencial apantallado $V_a(x)$.

Primero examinamos el potencial y fijamos la ubicación de $x = 0$ en un mínimo. A continuación definimos los potenciales apantallados $V_a(x)$ de la siguiente manera:

$$V_a(x) = \begin{cases} V(x) & |x| < a, \\ \infty & |x| > a. \end{cases} \qquad \text{(2.21)}$$

Como se muestra en la Fig. 4, el potencial apantallado $V_a(x)$ es un pozo infinito de ancho $2a$ cuyo fondo está tomado de $V(x)$. El argumento que sigue se basa en dos supuestos plausibles. Primero: cuando $a \to \infty$ los estados ligados de $V_a(x)$ se convierten en los estados ligados de $V(x)$. Segundo: a medida que $a$ aumenta, la función de onda y su derivada se estiran y deforman continuamente.

Cuando $a$ es muy pequeño, $V_a(x)$ es aproximadamente un pozo infinito muy estrecho con fondo plano: un pozo cuadrado infinito. Esto se debe a que elegimos $x = 0$ como un mínimo, y cualquier mínimo es localmente plano. En este pozo cuadrado infinito el teorema del nodo se cumple. El estado fundamental, por ejemplo, se anulará en los extremos y no tendrá nodos. Ahora argumentaremos que, a medida que la pantalla se agranda, no podemos generar un nodo. Esto se aplica al estado fundamental, como discutimos explícitamente a continuación, y también a todos los demás estados. Si no podemos generar nodos al agrandar la pantalla, el teorema del nodo se aplica a $V(x)$.

¿Por qué es así? Consideremos cómo podríamos desarrollar un nodo adicional mientras estiramos la pantalla. Para empezar, consideremos el estado fundamental en la parte superior de la Figura 5. No hay ningún nodo para este valor de la pantalla y tenemos $\psi'(-a) > 0$ (pared izquierda) y $\psi'(a) < 0$ (pared derecha). Supongamos que al aumentar $a$ producimos un nodo, mostrado para la pantalla mayor $a'$ debajo. Para que esto suceda, el signo de $\psi'$ en uno de los extremos debe cambiar. En el caso mostrado, es el extremo derecho el que experimenta un cambio en el signo de $\psi'$. Con la suposición de estiramiento continuo, tendría que haber alguna pantalla intermedia en la que $\psi' = 0$ en el extremo derecho. Pero en ese caso, $\psi = \psi' = 0$ en ese extremo, y entonces $\psi(x) = 0$ para todo $x$, lo cual es claramente imposible.

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes13_ES/fig5.png)

Figura 5: Introducir un solo nodo requiere cambiar el signo de la derivada en el extremo derecho: $\psi'(a) < 0$ pero $\psi'(a') > 0$. En alguna pantalla intermedia, el valor de $\psi'$ en el extremo derecho debe hacerse cero. Pero esto es imposible.

![Figura 6](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes13_ES/fig6.png)

Figura 6: Introducir dos nodos haciendo que la función de onda cruce el eje $x$ entre los dos límites (compárense la parte superior e inferior). Esto no es posible, ya que requeriría, en una pantalla intermedia (en medio), que $\psi = \psi' = 0$ en algún punto.

Es posible introducir nodos sin cambiar el signo de $\psi'$ en ninguno de los extremos. En este proceso, mostrado en la Fig. 6, la función de onda se hunde y produce dos nodos nuevos. Sin embargo, este proceso no puede tener lugar. En efecto, para alguna pantalla intermedia la función de onda debe ser tangente al eje $x$, y en ese punto tendríamos $\psi = \psi' = 0$, lo cual es imposible.

Concluimos que no podemos cambiar el número de nodos de ninguna función de onda al estirar la pantalla. El $n$-ésimo estado excitado del pozo cuadrado infinito diminuto, con $n - 1$ nodos, se convertirá en el $n$-ésimo estado excitado de $V(x)$ con $n - 1$ nodos. En el pozo cuadrado infinito diminuto, los niveles de energía están ordenados en energía creciente según el número de nodos. Lo mismo se cumple en todas las etapas de la pantalla en estiramiento y, por lo tanto, es cierto para $V(x)$. Dos niveles de energía consecutivos cualesquiera no pueden permutarse porque, por continuidad, esto requeriría una situación de degeneración, lo cual no es posible.

## 3. Oscilador armónico

El oscilador armónico clásico es un sistema dinámico rico e interesante. Nos permite comprender muchos tipos de oscilaciones en sistemas complejos. La energía total $E$ de una partícula de masa $m$ que se mueve en una dimensión bajo la acción de una fuerza restauradora $F = -kx$, $k > 0$, se escribe habitualmente como

$$E = \tfrac{1}{2}mv^2 + \tfrac{1}{2}kx^2. \qquad \text{(3.22)}$$

El primer término es la energía cinética y el segundo término es la energía potencial

$$V(x) = \tfrac{1}{2}kx^2. \qquad \text{(3.23)}$$

El potencial es cuadrático en $x$. En un sistema así, la partícula realiza un movimiento oscilatorio con frecuencia angular $\omega$ dada por

$$\omega = \sqrt{\frac{k}{m}} \quad\rightarrow\quad k = m\omega^2. \qquad \text{(3.24)}$$

Intercambiando $k$ por $\omega$ y usando el momento para expresar la energía cinética, podemos reescribir $E$ como sigue

$$E = \frac{p^2}{2m} + \tfrac{1}{2}m\omega^2 x^2. \qquad \text{(3.25)}$$

Esto es todo para el oscilador armónico clásico.

El potencial cuadrático es ubicuo en física, ya que surge en primera aproximación cuando expandimos un potencial arbitrario alrededor de un mínimo. Para mostrar esto, consideremos un potencial arbitrario $V(x)$ con un mínimo en $x_0$. Para $x \approx x_0$, podemos usar una expansión de Taylor para escribir

$$V(x) = V(x_0) + (x - x_0)V'(x_0) + \tfrac{1}{2}(x - x_0)^2 V''(x_0) + O((x-x_0)^3). \qquad \text{(3.26)}$$

Puesto que $x_0$ es un punto crítico, $V'(x_0) = 0$. Descartando los términos de orden superior, tenemos entonces que el potencial es aproximadamente cuadrático

$$V(x) \approx V(x_0) + \tfrac{1}{2}V''(x_0)(x - x_0)^2. \qquad \text{(3.27)}$$

Esta es una buena aproximación para $x$ cercano a $x_0$. Puesto que $x_0$ es un mínimo, $V''(x_0) > 0$ y esto es un oscilador armónico centrado en $x_0$ y con $k = V''(x_0)$. La constante aditiva $V(x_0)$ no tiene efecto sobre la dinámica.

Ante la pregunta de definir un oscilador armónico cuántico, nos inspiramos en la expresión anterior (3.25) para la energía y declaramos que $\hat{x}$ y $\hat{p}$ serán operadores con $[\hat{x}, \hat{p}] = i\hbar$ y que el hamiltoniano $\hat{H}$ está dado por

$$\hat{H} = \frac{\hat{p}^2}{2m} + \tfrac{1}{2}m\omega^2 \hat{x}^2, \qquad [\hat{x}, \hat{p}] = i\hbar. \qquad \text{(3.28)}$$

El potencial del oscilador armónico aquí es

$$V(x) = \tfrac{1}{2}m\omega^2 x^2. \qquad \text{(3.29)}$$

Nótese que $\omega$ tiene unidades de frecuencia: $[\omega] = 1/T$. Podemos usar esto para construir una energía característica $\hbar\omega$. El oscilador armónico cuántico es un sistema bastante natural, directamente inspirado en el oscilador clásico.

Nuestro primer paso es encontrar los autoestados de energía, las soluciones de la ecuación de Schrödinger independiente del tiempo:

$$-\frac{\hbar^2}{2m}\frac{d^2\varphi(x)}{dx^2} + \tfrac{1}{2}m\omega^2 x^2 \varphi(x) = E\varphi(x). \qquad \text{(3.30)}$$

Aquí tanto $E$ como $\varphi(x)$ son desconocidos. Esperamos que los autoestados de energía existan solo para ciertos valores cuantizados de $E$.

Como primer paso, limpiaremos la ecuación de constantes dimensionales. Esto nos ayuda a apreciar mejor la ecuación en cuestión. Además, nos permitiría implementar fácilmente la ecuación en una computadora. Cada término de la ecuación debe tener unidades de energía multiplicadas por unidades de $\varphi$, como podemos ver observando el lado derecho de la ecuación. Nótese que las unidades de $\varphi$ no son relevantes para la consistencia de la ecuación, ya que $\varphi$ aparece en cada término. Podemos, por lo tanto, ignorar las unidades de $\varphi$. Las unidades de energía en el lado izquierdo se construyen en el primer término mediante una combinación de constantes y derivadas, y en el segundo término mediante una combinación de constantes y potencias de $x$. Si pudiéramos trabajar con una coordenada adimensional $u$ en lugar de $x$, las unidades de energía tendrían que ser producidas únicamente por las constantes del problema y, como hemos visto, la única posibilidad es $\hbar\omega$. ¡Un factor común $\hbar\omega$ simplificará entonces enormemente la estructura de la ecuación, ya que nos permitirá definir una energía adimensional!

Comenzamos, por lo tanto, introduciendo una coordenada adimensional $u$ para reemplazar la coordenada convencional $x$. Establecemos

$$x = a\,u, \qquad u \text{ adimensional}, \qquad [a] = L, \qquad \text{(3.31)}$$

donde $a$ debe ser una constante con unidades de longitud. Para determinar $a$ en términos de $\hbar$, $m$ y $\omega$, igualamos una energía cinética característica a una energía potencial característica:

$$\frac{\hbar^2}{ma^2} = m\omega^2 a^2 \quad\rightarrow\quad a^2 = \frac{\hbar}{m\omega}. \qquad \text{(3.32)}$$

Ahora, sustituyendo $x = au$ en la ecuación de Schrödinger independiente del tiempo obtenemos

$$-\frac{\hbar^2}{2ma^2}\frac{d^2\varphi(u)}{du^2} + \tfrac{1}{2}m\omega^2 a^2 u^2 \varphi(u) = E\varphi(u). \qquad \text{(3.33)}$$

Aquí hemos usado

$$\frac{d}{dx} = \frac{du}{dx}\frac{d}{du} = \frac{1}{a}\frac{d}{du}. \qquad \text{(3.34)}$$

Nótese que $\dfrac{\hbar^2}{ma^2} = \hbar\omega$ y $m\omega^2 a^2 = \hbar\omega$, de modo que tenemos

$$-\tfrac{1}{2}\hbar\omega\,\frac{d^2\varphi(u)}{du^2} + \tfrac{1}{2}\hbar\omega\,u^2 \varphi(u) = E\varphi(u). \qquad \text{(3.35)}$$

Podemos ver que las cosas están funcionando. Como se esperaba, las unidades de energía en el lado izquierdo son transportadas por $\hbar\omega$. Multiplicando por $\dfrac{2}{\hbar\omega}$, llegamos a

$$-\frac{d^2\varphi(u)}{du^2} + u^2 \varphi(u) = \mathcal{E}\varphi(u), \qquad \text{(3.36)}$$

donde hemos definido una energía adimensional $\mathcal{E}$:

$$\mathcal{E} \equiv \frac{2E}{\hbar\omega}, \qquad E = \tfrac{1}{2}\hbar\omega\,\mathcal{E}. \qquad \text{(3.37)}$$

Si conocemos el número puro $\mathcal{E}$ entonces conocemos la energía $E$. Reordenando, llegamos a la versión limpia de la ecuación de Schrödinger independiente del tiempo:

$$\frac{d^2\varphi}{du^2} = (u^2 - \mathcal{E})\varphi. \qquad \text{(3.38)}$$

Esta es nuestra versión simplificada y adimensional de la ecuación de Schrödinger independiente del tiempo. Es claramente menos recargada que (3.30).

La ecuación diferencial anterior debe tener soluciones para todos los valores del parámetro de energía $\mathcal{E}$; después de todo, ¡podría integrarse en una computadora! La cuantización debe surgir porque las soluciones no son normalizables excepto para valores especiales de $\mathcal{E}$. Para entender esta cuestión tal como se relaciona con la ecuación, examinamos las soluciones para valores grandes de $|u|$. En este límite, $\mathcal{E}$ puede ignorarse en comparación con $u^2$, y tenemos la ecuación aproximada

$$\varphi''(u) \approx u^2 \varphi(u). \qquad \text{(3.39)}$$

¡Esta ecuación no puede resolverse mediante ningún polinomio! Si $\varphi$ es un polinomio de grado $n$, el grado del lado izquierdo sería $n - 2$ y el del lado derecho $n + 2$. Esto no puede funcionar. Probemos una solución de la forma

$$\varphi(u) = u^k e^{\alpha u^2/2}. \qquad \text{(3.40)}$$

El término dominante en $\varphi''$ aparece cuando derivamos la exponencial:

$$\varphi''(u) \approx \alpha^2 u^2 \varphi(u) \qquad \text{cuando } |u| \to \infty. \qquad \text{(3.41)}$$

Comparando con (3.39) tenemos soluciones para $\alpha = \pm 1$, en cuyo caso tenemos

$$\varphi(u) \approx A u^k e^{-u^2/2} + B u^k e^{u^2/2} \qquad \text{cuando } |u| \to \infty. \qquad \text{(3.42)}$$

La solución con coeficiente $B$ no daría lugar a un autoestado de energía porque diverge cuando $|u| \to \infty$ y no sería normalizable. Nótese que el factor $u^k$ no desempeñó ningún papel en el análisis. Este factor, sin embargo, sugiere que un polinomio multiplicando $e^{\pm u^2/2}$ podría ser una solución de la ecuación diferencial.

Este análisis sugiere que, para nuestros propósitos, deberíamos escribir

$$\varphi(u) = h(u)e^{-u^2/2}. \qquad \text{(3.43)}$$

Nótese que no hay ninguna suposición ni pérdida de generalidad al escribir esta expresión. En efecto, cualquier función $\varphi(u)$ puede escribirse como alguna otra función multiplicada por $e^{-u^2/2}$, como resulta inmediatamente claro ($\varphi(u)e^{u^2/2})e^{-u^2/2}$. Al escribir (3.43) solo estamos esperando que la ecuación diferencial para $h(u)$ sea más simple. Claramente, si encontramos $h(u)$ hemos encontrado $\varphi(u)$. De hecho, esperamos que $h(u)$ sea un polinomio porque el ansatz captura la dependencia para $|u|$ grande que impide que la solución para $\varphi(u)$ sea un polinomio.

Sustituyendo (3.43) en (3.38) y simplificando, encontramos una ecuación diferencial lineal de segundo orden para $h(u)$:

$$\frac{d^2h}{du^2} - 2u\frac{dh}{du} + (\mathcal{E} - 1)h = 0. \qquad \text{(3.44)}$$

De hecho, es posible ver en este punto que obtener una solución polinómica requiere la cuantización de $\mathcal{E}$. En efecto, supongamos que $h(u)$ es un polinomio de grado $j$:

$$h(u) = u^j + \alpha_1 u^{j-1} + \alpha_2 u^{j-2} + \dots \qquad \text{(3.45)}$$

En la ecuación anterior, el primer término da lugar a un polinomio de grado $j - 2$. Cada uno de los otros dos términos son polinomios de grado $j$. Para que la ecuación tenga sentido, el coeficiente de las contribuciones al coeficiente de $u^j$ y $u^{j-1}$ debe anularse. El coeficiente de $u^j$ es

$$\text{Coeficiente de } u^j: \quad -2j + \mathcal{E} - 1 = 0 \quad\rightarrow\quad \mathcal{E} = 2j + 1. \qquad \text{(3.46)}$$

Así, obtenemos la cuantización de la energía: una solución polinómica $h(u)$ de grado $j$ requiere $\mathcal{E} = 2j + 1$. Podría preguntarse acerca del término subdominante de grado $j - 1$, cuyo coeficiente también debe anularse.

$$\text{Coeficiente de } u^{j-1}: \quad (-2(j-1) + \mathcal{E} - 1)\alpha_1 = 0. \qquad \text{(3.47)}$$

Puesto que la energía $\mathcal{E}$ ya ha sido fijada, la única manera de satisfacer esta condición es hacer $\alpha_1 = 0$. Así, el polinomio es en realidad de la forma

$$h(u) = u^j + \alpha_2 u^{j-2} + \dots \qquad \text{(3.48)}$$

Si esto debe conducir a un autoestado de energía, la anulación de $\alpha_1$ podría haberse anticipado. Puesto que el potencial del oscilador armónico es par, sabemos que los estados ligados deben ser pares o impares. Puesto que $e^{-u^2/2}$ es par, la solución $\varphi(u)$ será par o impar si $h(u)$ es par o impar. Si $\alpha_1$ no se hubiera anulado, $h(u)$ tendría dos potencias consecutivas de $u$ y no podría ser ni par ni impar.

Podemos analizar la ecuación de manera más sistemática mediante una expansión en serie:

$$h(u) = \sum_{k=0}^{\infty} a_k u^k. \qquad \text{(3.49)}$$

Una forma sencilla de sustituir en la ecuación diferencial (3.44) es seleccionar de cada término la contribución al coeficiente de $u^j$. Para esto podemos imaginar los términos $a_j u^j + a_{j+1}u^{j+1} + a_{j+2}u^{j+2}$ en $h(u)$ y seleccionar la parte que contribuye al coeficiente de $u^j$:

$$\begin{aligned}
\text{Contribución de: } &\frac{d^2h}{du^2}: \quad (j+2)(j+1)a_{j+2} \\
\text{Contribución de: } &-2u\frac{dh}{du}: \quad -2ja_j \\
\text{Contribución de: } &(\mathcal{E}-1)h: \quad (\mathcal{E}-1)a_j
\end{aligned} \qquad \text{(3.50)}$$

El coeficiente total de $u^j$ en el lado izquierdo de la ecuación diferencial debe anularse, para todos los valores de $j$, para que la ecuación diferencial se satisfaga. Por lo tanto

$$(j+2)(j+1)a_{j+2} - 2ja_j + (\mathcal{E}-1)a_j = 0, \qquad j = 0, 1, 2, \dots \qquad \text{(3.51)}$$

Esto puede escribirse como una relación de recurrencia:

$$a_{j+2} = \frac{2j + 1 - \mathcal{E}}{(j+2)(j+1)}\,a_j, \qquad \text{(3.52)}$$

Esta es una relación de recurrencia de dos pasos. Si se elige algún $a_0$, se puede construir una solución que contenga solo coeficientes pares, $a_2, a_4, \dots$, determinados recursivamente por la relación anterior. Esa solución, de la forma

$$a_0 + a_2 u^2 + a_4 u^4 + \cdots \qquad \text{(3.53)}$$

sería par. Otra solución se construye eligiendo algún $a_1$ y luego usando la recurrencia anterior para hallar $a_3, a_5, \dots$. Esa solución, de la forma

$$a_1 u + a_3 u^3 + \cdots \qquad \text{(3.54)}$$

sería impar. Para cualquier valor arbitrario de $\mathcal{E}$ ambas soluciones de la ecuación diferencial (3.44) existen, pero ninguna de las dos sería polinómica ni se esperaría que fuera un buen autoestado de energía. La solución general de (3.44) con $\mathcal{E}$ arbitraria queda así determinada por las dos constantes $(a_0, a_1)$, ya que juntas determinan todos los coeficientes. Esto tiene sentido, porque $a_0 = h(0)$ y $a_1 = h'(0)$, y la solución de una ecuación diferencial de segundo orden queda determinada al conocer la función y su derivada en cualquier punto.

Demostremos ahora que si la serie para $h(u)$ nunca termina, la $\varphi(u)$ correspondiente no es un autoestado de energía aceptable. Veamos cuál sería el comportamiento para $u$ grande de $h(u)$ si no termina. Para $j$ grande, la relación de recurrencia (3.52) da

$$\frac{a_{j+2}}{a_j} \approx \frac{2}{j}. \qquad \text{(3.55)}$$

¿Qué tipo de función crece de esta manera? Nótese que

$$e^{u^2} = \sum_{n=0}^{\infty} \frac{1}{n!}\left(u^2\right)^n = \sum_{j \in \text{par}} \frac{1}{(j/2)!}\,u^j. \qquad \text{(3.56)}$$

Esta serie tiene coeficientes $c_j = \dfrac{1}{(j/2)!}$ para $j$ par, por lo que vemos que

$$\frac{c_{j+2}}{c_j} = \frac{(j/2)!}{((j+2)/2)!} = \frac{2}{j+2} \approx \frac{2}{j}, \qquad \text{(3.57)}$$

para $j$ grande. Este es justamente el comportamiento observado en (3.55) para $h(u)$. Así, si la serie para $h(u)$ no termina, la función de onda se comporta como

$$\varphi(u) = h(u)e^{-u^2/2} \sim e^{u^2}e^{-u^2/2} \sim e^{u^2/2}, \qquad \text{(3.58)}$$

que es la solución mala que identificamos en (3.42). Esto demuestra que $h(u)$ debe ser un polinomio y que la relación de recurrencia debe terminar para que obtengamos un autoestado de energía.

Ahora discutimos cómo obtener un $h(u)$ polinómico, aunque la conclusión principal ya se anticipó en (3.46). Si $h(u)$ debe ser de grado $j$, debe tener $a_j$ no nulo y $a_{j+2}$ nulo, según lo determinado por la relación de recurrencia (3.52). El numerador de esta relación de recurrencia debe anularse y debemos elegir $\mathcal{E}$ tal que

$$2j + 1 - \mathcal{E} = 0. \qquad \text{(3.59)}$$

La solución tomará entonces la forma:

$$h(u) = a_j u^j + a_{j-2}u^{j-2} + \cdots, \qquad \text{(3.60)}$$

con potencias que decrecen en pasos de dos, porque esto es lo que exige la relación de recurrencia para tener una solución. La solución será, por lo tanto, automáticamente par (si $j$ es par) o impar (si $j$ es impar). Digamos que $j$ es par y la solución es par con energía $2j + 1$ según lo requerido. La segunda solución de la ecuación diferencial para ese valor de la energía sería impar, pero la energía $2j + 1$ que hizo terminar la solución par no hará terminar la solución impar. Esto significa que la segunda solución de la ecuación diferencial no es un autoestado de energía.

Solemos llamar al grado $j$ de la solución con la letra $n$. Entonces,

$$\mathcal{E} = 2n + 1, \qquad n = 0, 1, 2, \dots \qquad \text{(3.61)}$$

corresponde a la solución polinómica

$$h_n(u) = a_n u^n + a_{n-2}u^{n-2} + \cdots, \qquad n = 0, 1, 2, \dots \qquad \text{(3.62)}$$

La energía de la solución $\varphi_n(u) = h_n(u)e^{-u^2/2}$ es

$$E = \frac{\hbar\omega}{2}\mathcal{E} = \frac{\hbar\omega}{2}(2n+1). \qquad \text{(3.63)}$$

Tenemos

$$E_n = \hbar\omega\left(n + \tfrac{1}{2}\right), \qquad n = 0, 1, 2, \dots \qquad \text{(3.64)}$$

Vemos que las energías están cuantizadas y los niveles de energía están espaciados uniformemente. La energía del estado fundamental es $E_0 = \hbar\omega/2$. Las correspondientes soluciones en serie de potencias $h_n(u)$ son los polinomios de Hermite, habitualmente denotados como $H_n(u)$

$$H_n(u) = 2^n u^n \pm \cdots \qquad \text{(3.65)}$$

El factor $2^n$ aquí es una elección de convención. Los polinomios de Hermite son soluciones de (3.44) con $\mathcal{E} = 2n + 1$, y por lo tanto satisfacen la ecuación diferencial

$$\frac{d^2H_n}{du^2} - 2u\frac{dH_n}{du} + 2nH_n = 0. \qquad \text{(3.66)}$$

Los primeros polinomios de Hermite son

$$\begin{aligned}
H_0(u) &= 1 \\
H_1(u) &= 2u \\
H_2(u) &= 4u^2 - 2 \\
H_3(u) &= 8u^3 - 12u.
\end{aligned} \qquad \text{(3.67)}$$

La función generadora de los polinomios de Hermite es una exponencial, con parámetro formal $z$:

$$e^{-z^2+2zu} = \sum_{n=0}^{\infty} \frac{z^n}{n!}H_n(u). \qquad \text{(3.68)}$$

No es demasiado difícil demostrar que los polinomios definidos por esta expansión satisfacen la ecuación diferencial requerida (3.66) y están normalizados como se afirmó en (3.65).

Escribamos los autoestados de energía en términos de $x$. Recordando que $u^2 = x^2/a^2$, donde $a^2 = \hbar/(m\omega)$, la relación

$$\varphi_n(u) \sim H_n(u)e^{-u^2/2}, \qquad \text{(3.69)}$$

nos da entonces

$$\varphi_n(x) = N_n\,H_n\!\left(\sqrt{\frac{m\omega}{\hbar}}\,x\right) e^{-\frac{m\omega}{2\hbar}x^2}, \qquad n = 0, 1, 2, \dots, \qquad \text{(3.70)}$$

donde $N_n$ es una constante de normalización.

*Andrew Turner transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare https://ocw.mit.edu

8.04 Física Cuántica I Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.
