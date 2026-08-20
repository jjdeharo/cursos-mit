# Examen 1 (Test 1, otoño de 2015)

**8.04, Física Cuántica I, otoño de 2015**

**EXAMEN 1**

*Martes 20 de octubre, 9:30–11:00 pm*

Dispone de 90 minutos.

Responda todos los problemas en los cuadernillos proporcionados. Escriba SU NOMBRE y SU SECCIÓN en su(s) cuadernillo(s).

Hay cinco preguntas, con un total de 100 puntos.

No se permiten libros, apuntes ni calculadoras.

Muestre su trabajo CLARAMENTE.

------------------------------------------------------------------------

## Hoja de fórmulas

- $\hbar c \simeq 197.3\ \text{MeV}\cdot\text{fm}$, $m_e c^2 \simeq 0.511\ \text{MeV}$, $m_p c^2 = 938\ \text{MeV}$, $\dfrac{e^2}{\hbar c} \simeq \dfrac{1}{137}$

- Relatividad: $p = \gamma m v$, $E = \gamma m c^2$, $E^2 = p^2 c^2 + m^2 c^4$, $\gamma = \dfrac{1}{\sqrt{1-\beta^2}}$, $\beta = \dfrac{v}{c}$

- Fotones: $E = h\nu$, $p = \dfrac{h}{\lambda}$, o bien $E = \hbar\omega$, $p = \hbar k$

- Longitudes de onda

  de Broglie: $\lambda = \dfrac{h}{p}$, Compton: $\lambda_C = \dfrac{h}{mc}$.

- Operadores de momento y posición

$$p = \frac{\hbar}{i}\frac{\partial}{\partial x}, \qquad [x,p] = i\hbar, \qquad \mathbf{p} = \frac{\hbar}{i}\nabla, \qquad [x_i, p_j] = i\hbar\,\delta_{ij}$$

- Ecuación de Schrödinger

$$i\hbar\frac{\partial \Psi}{\partial t}(x,t) = \left[-\frac{\hbar^2}{2m}\nabla^2 + V(x,t)\right]\Psi(x,t),$$

$$\frac{\partial}{\partial t}\rho(x,t) + \nabla\cdot J(x,t) = 0$$

$$\rho(x,t) = |\Psi(x,t)|^2; \qquad J(x,t) = \frac{\hbar}{m}\,\text{Im}\left[\Psi^*\nabla\Psi\right]$$

- Transformadas de Fourier:

$$\Psi(x) = \frac{1}{\sqrt{2\pi}}\int dk\,\Phi(k)e^{ikx}, \qquad \Phi(k) = \frac{1}{\sqrt{2\pi}}\int dx\,\Psi(x)e^{-ikx}, \qquad \int dx\,|\Psi(x)|^2 = \int dk\,|\Phi(k)|^2$$

$$\begin{aligned}
\Psi(\mathbf{x}) &= \frac{1}{(2\pi)^{3/2}}\int d^3k\,\Phi(\mathbf{k})e^{i\mathbf{k}\cdot\mathbf{x}},\\
\Phi(\mathbf{k}) &= \frac{1}{(2\pi)^{3/2}}\int d^3x\,\Psi(\mathbf{x})e^{-i\mathbf{k}\cdot\mathbf{x}},\\
\int d^3x\,|\Psi(\mathbf{x})|^2 &= \int d^3k\,|\Phi(\mathbf{k})|^2
\end{aligned}$$

$$\frac{1}{2\pi}\int_{-\infty}^{\infty} e^{ikx}\,dx = \delta(k), \qquad \frac{1}{(2\pi)^3}\int e^{i\mathbf{k}\cdot\mathbf{x}}\,d^3x = \delta^{(3)}(\mathbf{k})$$

$$\int_{-\infty}^{+\infty} dx\,\exp\left(-ax^2 + bx\right) = \sqrt{\frac{\pi}{a}}\,\exp\left(\frac{b^2}{4a}\right), \qquad \text{cuando } \text{Re}(a) > 0.$$

- Paquetes de ondas

$$v_{\text{group}} = \frac{d\omega}{dk}, \qquad \Delta k\,\Delta x \simeq 1, \qquad \text{conservación de forma: } t\,\Delta v \le \Delta x$$

- Conjugación hermítica:

$$\int dx\,(K\Psi(x,t))^*\,\Psi(x,t) = \int dx\,\Psi^*(x,t)\,(K^\dagger \Psi(x,t))$$

Si $K^\dagger = K$, entonces $K$ es hermítico.

- Valores esperados

$$\langle Q\rangle(t) = \int dx\,\Psi^*(x,t)\,(Q\Psi(x,t))$$

- Evolución temporal del valor esperado. Para $Q$ hermítico

$$i\hbar\,\frac{d}{dt}\langle Q\rangle = \langle [Q,H]\rangle$$

- Identidad del conmutador

$$[A, BC] = [A,B]C + B[A,C]$$

- Incertidumbre $\Delta Q$ de un operador hermítico $Q$

$$(\Delta Q)^2 = \langle Q^2\rangle - \langle Q\rangle^2 = \langle (Q - \langle Q\rangle)^2\rangle$$

- Principio de incertidumbre: $\Delta x\,\Delta p \ge \dfrac{\hbar}{2}$

------------------------------------------------------------------------

## Problema 1. Estimación y unidades \[10 puntos\]

El tamaño de un protón (más técnicamente, el llamado radio de carga) es de aproximadamente 0.9 fm. ¿Cómo se compara su longitud de onda de Compton con su tamaño? Las posibles respuestas son: la longitud de onda de Compton es \[mucho mayor, un poco mayor, un poco menor, o mucho menor\] que el tamaño. ¿Cuál es?

## Problema 2. Velocidad de grupo \[10 puntos\]

Para una partícula relativista $E^2 = p^2c^2 + m^2c^4$. Evalúe la velocidad de grupo $v_g = \dfrac{d\omega}{dk}$ recordando que $E = \hbar\omega$ y $p = \hbar k$. Deje su respuesta en términos de la velocidad $v$ de la partícula (¡sin ninguna aproximación!).

## Problema 3. Evolución de una partícula libre \[15 puntos\]

Considere el estado de una partícula *libre* de masa $m$ que en el instante inicial (tiempo igual a cero) está representado por la función de onda

$$\Psi(x,0) = \sin k_0 x, \qquad k_0 \in \mathbb{R}.$$

1.  Encuentre la corriente de probabilidad $J(x,0)$.

2.  Si medimos el momento de la partícula (en el instante inicial), ¿cuáles son los posibles valores que podemos obtener?

3.  Calcule $\Psi(x,t)$.

## Problema 4. Mejorando la detección de bombas \[35 puntos\]

Modificamos el interferómetro de Mach-Zehnder para aumentar el porcentaje de bombas de Elitzur-Vaidman que pueden certificarse como funcionales sin detonarlas.

Para ello construimos un divisor de haz con reflectividad $R$ y transmisividad $T$. Un fotón que incide (desde cualquiera de los dos puertos) tiene una probabilidad $R$ de ser reflejado y una probabilidad $T$ de ser transmitido ($R + T = 1$). Sean $r$ y $t$ las raíces cuadradas positivas:

$$r \equiv \sqrt{R}, \qquad t \equiv \sqrt{T}.$$

1.  Construya la matriz $2\times 2$ $U$ que representa el divisor de haz. Para ello, considere qué ocurre cuando un fotón incide sobre el divisor de haz por el lado superior (la entrada en este caso es $\begin{pmatrix}1\\0\end{pmatrix}$) y cuando incide por el lado inferior (la entrada en este caso es $\begin{pmatrix}0\\1\end{pmatrix}$). Para fijar convenciones, $U$ tendrá todos sus elementos positivos (y reales) excepto el elemento inferior derecho (el elemento 2,2). Confirme que $U$ es unitaria.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_Examen1_ES/fig1.png)

Figura: un divisor de haz «BS» golpeado desde arriba y desde abajo, ilustrando las dos situaciones anteriores.

El interferómetro con los detectores D0 y D1 (mostrado a continuación) utiliza dos copias idénticas del divisor de haz. El fotón entrante llega por el lado superior.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_Examen1_ES/fig2.png)

Figura: el interferómetro completo: el fotón entra por arriba en el primer divisor de haz BS, se refleja en dos espejos M —uno en la rama superior y otro en la rama inferior, donde se sitúa la bomba—, y ambos caminos se recombinan en un segundo divisor de haz BS antes de llegar a los detectores D0 y D1.

1.  Se inserta una bomba defectuosa en la rama inferior del interferómetro. ¿Cuáles son las probabilidades de detección $P_0$ y $P_1$ en D0 y D1, respectivamente?

2.  Se inserta una bomba en funcionamiento en la rama inferior del interferómetro. ¿Cuál es la probabilidad de detonación $P_{\text{boom}}$ y las probabilidades de detección $P_0$ y $P_1$? Exprese sus respuestas en términos de $R$ y $T$.

3.  Se prueban bombas hasta estar razonablemente seguro de que, o bien no funcionan, o bien son operativas. ¿Qué fracción $f$ de las bombas operativas puede certificarse como buena sin detonarlas? Dé su respuesta en términos de $R$. ¿Cuál es el máximo valor posible de $f$?

## Problema 5. Solapamiento entre gaussianas en movimiento \[30 puntos\]

Hemos aprendido (en las tareas) que el solapamiento $\int dx\,\Psi_1^*\Psi_2$ entre dos paquetes de ondas distintos $\Psi_1$ y $\Psi_2$ es, en general, independiente del tiempo.

El siguiente EJEMPLO parece estar en tensión con este hecho: consideremos dos gaussianas que coinciden en $t = 0$ pero que se mueven en direcciones opuestas con momentos grandes comparados con sus incertidumbres de momento. Ahora hacemos dos afirmaciones:

1.  En $t = 0$ el solapamiento es grande.
2.  Una vez que los centros de los paquetes están separados por un pequeño múltiplo de la incertidumbre de posición, el solapamiento es pequeño.

El propósito de este problema es encontrar el fallo en las afirmaciones del EJEMPLO.

Considere una partícula libre y un paquete de ondas gaussiano normalizado $\hat\Psi$ en el instante inicial:

$$\hat\Psi(x,0) = \frac{1}{(2\pi)^{1/4}\sqrt{a}}\exp\left(-\frac{x^2}{4a^2}\right).$$

A partir de este creamos dos paquetes de ondas $\Psi_1$ y $\Psi_2$:

$$\Psi_1(x,0) \equiv e^{iqx/\hbar}\,\hat\Psi(x,0),$$

$$\Psi_2(x,0) \equiv e^{-iqx/\hbar}\,\hat\Psi(x,0).$$

Aquí $q$ es una cantidad real con unidades de momento.

1.  ¿Cuál es $\langle p\rangle$ para $\hat\Psi(x,0)$? ¿Cambiará este valor esperado con el tiempo? Explique.

2.  ¿Cuál es $\langle p\rangle$ para $\Psi_1(x,0)$? ¿Cuál es $\langle p\rangle$ para $\Psi_2(x,0)$? ¿Cambian estos valores esperados con el tiempo?

3.  Calcule el solapamiento en el instante inicial $\gamma(0)$ de los dos paquetes:

$$\gamma(0) = \int \Psi_1^*(x,0)\,\Psi_2(x,0)\,dx.$$

La siguiente integral puede ser útil:

$$\int_{-\infty}^{\infty} e^{-ax^2 + bx}\,dx = \sqrt{\frac{\pi}{a}}\,\exp\left(\frac{b^2}{4a}\right), \qquad \text{cuando } \text{Re}(a) > 0.$$

1.  Escriba una desigualdad que exprese el hecho de que el momento de los paquetes de ondas es grande comparado con la incertidumbre de momento. ¿Qué estaba mal en las afirmaciones del EJEMPLO?

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*
