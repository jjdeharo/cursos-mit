# 8.04-fisica-cuantica-i-es — curso completo

Traducción no oficial de materiales de MIT OpenCourseWare, con asistencia
de IA. Licencia CC BY-NC-SA 4.0. Fórmulas en LaTeX.


---

<!-- MIT8.04_Examen1_ES.md -->

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


---

<!-- MIT8.04_Examen2_ES.md -->

# Examen 2 (Test 2, otoño de 2015)

**8.04, Física Cuántica I, otoño de 2015**

**TEST 2**

*Martes 17 de noviembre, 21:30–23:00*

**Dispone de 90 minutos.**

Responda todos los problemas en los cuadernillos en blanco proporcionados. Escriba SU NOMBRE y SU SECCIÓN en su(s) cuadernillo(s).

Hay cinco preguntas, con un total de 100 puntos.

No se permiten libros, apuntes ni calculadoras.

**Muestre su trabajo con CLARIDAD.**

## Hoja de fórmulas

- $\hbar c \simeq 197.3\ \text{MeV}\cdot\text{fm}$, $m_e c^2 \simeq 0.511\ \text{MeV}$, $m_p c^2 = 938\ \text{MeV}$, $\dfrac{e^2}{\hbar c} \simeq \dfrac{1}{137}$

- Relatividad: $p = \gamma m v$, $E = \gamma m c^2$, $E^2 = p^2c^2 + m^2c^4$, $\gamma = \dfrac{1}{\sqrt{1-\beta^2}}$, $\beta = \dfrac{v}{c}$

- Fotones: $E = h\nu$, $p = \dfrac{h}{\lambda}$, o bien $E = \hbar\omega$, $p = \hbar k$

- Longitudes de onda: de Broglie: $\lambda = \dfrac{h}{p}$, Compton: $\lambda_C = \dfrac{h}{mc}$.

- Operadores de momento y posición
  $$p = \frac{\hbar}{i}\frac{\partial}{\partial x}, \qquad [x,p] = i\hbar, \qquad \mathbf{p} = \frac{\hbar}{i}\nabla, \qquad [x_i, p_j] = i\hbar\,\delta_{ij}$$

- Ecuación de Schrödinger
  $$i\hbar\frac{\partial \Psi}{\partial t}(x,t) = \left[-\frac{\hbar^2}{2m}\nabla^2 + V(x,t)\right]\Psi(x,t),$$

  $$\frac{\partial}{\partial t}\rho(x,t) + \nabla\cdot J(x,t) = 0$$

  $$\rho(x,t) = |\Psi(x,t)|^2; \qquad J(x,t) = \frac{\hbar}{m}\text{Im}\left[\Psi^*\nabla\Psi\right]$$

- Transformadas de Fourier:
  $$\Psi(x) = \frac{1}{\sqrt{2\pi}}\int dk\, \Phi(k) e^{ikx}, \qquad \Phi(k) = \frac{1}{\sqrt{2\pi}}\int dx\, \Psi(x) e^{-ikx}, \qquad \int dx\,|\Psi(x)|^2 = \int dk\,|\Phi(k)|^2$$
  $$\begin{aligned}
  \Psi(x) &= \frac{1}{(2\pi)^{3/2}}\int d^3k\, \Phi(k) e^{i\mathbf{k}\cdot\mathbf{x}},\\
  \Phi(k) &= \frac{1}{(2\pi)^{3/2}}\int d^3x\, \Psi(x) e^{-i\mathbf{k}\cdot\mathbf{x}},\\
  \int d^3x\,|\Psi(x)|^2 &= \int d^3k\,|\Phi(k)|^2
  \end{aligned}$$
  $$\frac{1}{2\pi}\int_{-\infty}^{\infty} e^{ikx}\,dx = \delta(k), \qquad \frac{1}{(2\pi)^3}\int_{-\infty}^{\infty} e^{i\mathbf{k}\cdot\mathbf{x}}\,d^3x = \delta^{(3)}(k)$$

  $$\int_{-\infty}^{+\infty} dx\, \exp\left(-ax^2+bx\right) = \sqrt{\frac{\pi}{a}}\exp\left(\frac{b^2}{4a}\right), \quad \text{cuando } \text{Re}(a) > 0.$$

- Paquetes de ondas
  $$v_{\text{grupo}} = \frac{d\omega}{dk}, \qquad \Delta k\,\Delta x \simeq 1, \qquad \text{conservación de la forma: } t\,\Delta v \le \Delta x$$

- Conjugación hermítica:
  $$\int dx\,(K\Psi(x,t))^*\Psi(x,t) = \int dx\,\Psi^*(x,t)\left(K^\dagger \Psi(x,t)\right)$$

Si $K^\dagger = K$, entonces $K$ es hermítico.

- Valores esperados
  $$\langle Q\rangle(t) = \int dx\,\Psi^*(x,t)\big(Q\Psi(x,t)\big)$$

- Evolución temporal del valor esperado. Para $Q$ hermítico
  $$i\hbar\frac{d}{dt}\langle Q\rangle = \langle [Q,H]\rangle$$

- Identidad del conmutador
  $$[A,BC] = [A,B]C + B[A,C]$$

- Incertidumbre $\Delta Q$ de un operador hermítico $Q$
  $$(\Delta Q)^2 = \langle Q^2\rangle - \langle Q\rangle^2 = \langle (Q-\langle Q\rangle)^2\rangle$$

- Principio de incertidumbre: $\Delta x\,\Delta p \ge \dfrac{\hbar}{2}$

- Estado estacionario:
  $$\Psi(x,t) = \psi(x) e^{-iEt/\hbar}, \qquad -\frac{\hbar^2}{2m}\nabla^2\psi(x) + V(x)\psi(x) = E\,\psi(x)$$

- Pozo infinito
  $$V(x) = \begin{cases} 0, & \text{para } 0 < x < a, \\ \infty & \text{en cualquier otro caso} \end{cases}$$

  $$\psi_n(x) = \sqrt{\frac{2}{a}}\sin\frac{n\pi x}{a}, \qquad E_n = \frac{\hbar^2\pi^2 n^2}{2ma^2}, \qquad n=1,2,\ldots$$

- Estados ligados del pozo finito: $E \le 0$
  $$V(x) = \begin{cases} -V_0, & \text{para } |x| < a, \quad V_0 > 0 \\ 0 & \text{para } |x| > a \end{cases}$$

  $$\eta^2 \equiv \frac{2m(E+V_0)a^2}{\hbar^2}, \qquad \xi^2 \equiv \frac{2m|E|a^2}{\hbar^2}, \qquad z_0^2 \equiv \frac{2mV_0a^2}{\hbar^2}$$

  $$\rightarrow \quad \frac{|E|}{V_0} = \frac{\xi^2}{z_0^2}, \qquad \xi^2+\eta^2 = z_0^2$$

  $$\text{Soluciones pares: } \xi = \eta\tan\eta \qquad \text{Soluciones impares: } \xi = -\eta\cot\eta$$

- Potencial delta de Dirac:
  $$V = -\alpha\,\delta(x),\quad \alpha>0, \qquad \text{Estado ligado: } E = -\frac{m\alpha^2}{2\hbar^2}$$

- Oscilador armónico
  $$\hat H = \frac{1}{2m}\hat p^2 + \frac{1}{2}m\omega^2 \hat x^2 = \hbar\omega\left(\hat N + \frac{1}{2}\right), \qquad \hat N = \hat a^\dagger \hat a$$

  $$\hat a = \sqrt{\frac{m\omega}{2\hbar}}\left(\hat x + \frac{i\hat p}{m\omega}\right), \qquad \hat a^\dagger = \sqrt{\frac{m\omega}{2\hbar}}\left(\hat x - \frac{i\hat p}{m\omega}\right),$$

  $$\hat x = \sqrt{\frac{\hbar}{2m\omega}}(\hat a + \hat a^\dagger), \qquad \hat p = i\sqrt{\frac{m\omega\hbar}{2}}(\hat a^\dagger - \hat a),$$

  $$[\hat x,\hat p] = i\hbar, \qquad [\hat a,\hat a^\dagger] = 1, \qquad [\hat N,\hat a] = -\hat a, \qquad [\hat N,\hat a^\dagger] = \hat a^\dagger.$$

  $$\hat a\,\varphi_0 = 0, \qquad \varphi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}\exp\left(-\frac{m\omega}{2\hbar}x^2\right).$$

  $$\varphi_n = \frac{1}{\sqrt{n!}}(\hat a^\dagger)^n \varphi_0$$

  $$\hat H\varphi_n = E_n\varphi_n = \hbar\omega\left(n+\frac{1}{2}\right)\varphi_n, \qquad \hat N\varphi_n = n\,\varphi_n, \qquad (\varphi_m,\varphi_n) = \delta_{mn}$$

  $$\hat a^\dagger\varphi_n = \sqrt{n+1}\,\varphi_{n+1}, \qquad \hat a\,\varphi_n = \sqrt{n}\,\varphi_{n-1}.$$

## Problema 1

**Dibujar funciones de onda \[20 puntos\]**

En la primera página interior de su cuadernillo se adjunta un potencial simétrico (es también la última página de este examen). El potencial es infinito para $|x| > a$ y es una función par de $x$. En la figura se indican, como líneas discontinuas horizontales, el primer nivel de energía (estado fundamental), el segundo y el quinto. Dibuje las funciones de onda asociadas. Preste atención a la simetría, la convexidad o concavidad, los puntos de inflexión, los nodos, la amplitud y la longitud de onda.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_Examen2_ES/fig1.png)

Figura: un pozo infinito simétrico en $-a < x < a$ ($V=\infty$ para $|x|<-a$ y para $x>a$), con una barrera suave, en forma de joroba, centrada en $x=0$. Se indican tres niveles de energía discontinuos, $E_1$ (por debajo de la cresta de la joroba), $E_2$ (ligeramente por encima de la cresta) y $E_5$ (mucho más alto, cerca del techo del pozo). Debajo se dejan ejes en blanco, rotulados $\psi_1$, $\psi_2$ y $\psi_5$, para que el estudiante dibuje las funciones de onda correspondientes.

## Problema 2

**Limpiando unidades \[15 puntos\]**

En el átomo de hidrógeno, la escala de longitud es el radio de Bohr $a_0$, dado por

$$a_0 = \frac{\hbar^2}{me^2}.$$

Considere ahora la «ecuación radial» para la parte radial $\psi(r)$ de la función de onda:

$$\left[-\frac{\hbar^2}{2m}\frac{d^2}{dr^2} + \frac{\hbar^2\,\ell(\ell+1)}{2mr^2} - \frac{e^2}{r}\right]\psi(r) = E\,\psi(r).$$

Aquí $\ell$ es un entero no negativo. Simplifique la ecuación definiendo una coordenada adimensional $u$ y una energía adimensional $\mathcal{E}$ de modo que la ecuación tome la forma:

$$\left(-\frac{d^2}{du^2} + \ldots\right)\psi(u) = \mathcal{E}\,\psi(u).$$

1.  ¿Cómo están relacionadas $r$ y $u$?

2.  ¿Cómo están relacionadas $E$ y $\mathcal{E}$?

3.  Complete la ecuación anterior.

## Problema 3

**Ejercicios con el oscilador armónico \[15 puntos\]**

1.  Calcule $\left(\varphi_n,\ (\hat x)^3\,\varphi_n \right)$.

2.  Calcule $\left(\varphi_0,\ (\hat x)^{10}\,\varphi_{10} \right)$.

## Problema 4

**Estado fundamental y primer estado excitado de un potencial \[20 puntos\]**

Considere el potencial par esbozado a continuación, de altura $V_0$ salvo por una depresión alrededor de $x=0$, cerca de la cual el potencial se describe con precisión mediante una función cuadrática:

$$V(x) \simeq \frac{1}{2}\alpha x^2, \qquad x \text{ cerca de } 0,$$

donde $\alpha > 0$ es una constante.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_Examen2_ES/fig2.png)

Figura: un potencial que vale aproximadamente $V_0$ (constante) lejos del origen, con un pozo estrecho y profundo en $x=0$ que desciende bruscamente hasta cerca de cero, ilustrando la depresión cuadrática cerca del origen.

1.  Use el oscilador armónico para dar una estimación de la energía del estado fundamental. Encuentre una desigualdad que deban satisfacer $\alpha$, $V_0$, $m$ y $\hbar$ para que su resultado sea preciso.

2.  Considere ahora el potencial par construido usando dos copias del potencial anterior, con centros bien separados en $\pm x_0$.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_Examen2_ES/fig3.png)

Figura: el potencial $V(x) = V(-x)$ vale $V_0$ para $x$ cerca de $0$, con dos pozos estrechos y profundos idénticos al de la parte (a), uno centrado en $-x_0$ y otro en $x_0$.

Dé las energías aproximadas del estado fundamental y del primer estado excitado de este potencial y dibuje las funciones de onda asociadas. Escriba una desigualdad que involucre $x_0$, $\alpha$, $\hbar$ y $m$ necesaria para la precisión de su resultado.

1.  Combine sus dos desigualdades en la forma

$$\ldots \ll \alpha \ll \ldots$$

donde los puntos suspensivos representan las cantidades que debe escribir explícitamente.

## Problema 5

**Del pozo cuadrado a la función delta \[30 puntos\]**

En este problema se le pide derivar la energía del estado ligado de una partícula de masa $m$ en el potencial delta de Dirac

$$V_\delta(x) = -\alpha\,\delta(x), \qquad \alpha > 0,$$

partiendo del problema de una partícula de masa $m$ en un potencial de pozo cuadrado finito. Para ello, considere un pozo cuadrado con potencial $V_a(x)$:

$$V_a(x) = \begin{cases} -V_0, & \text{para } |x| < a, \quad V_0 > 0 \\ 0 & \text{para } |x| > a \end{cases}$$

Pensamos en la anchura total $2a$ como un regulador, es decir, un parámetro que se hará tender a cero en el límite en que el potencial $V_a$ se vuelve infinitesimalmente estrecho para representar el potencial delta $V_\delta$.

Puede pensar en una función delta negativa como el límite de un pozo cuya anchura y altura tienden simultáneamente a cero e infinito, respectivamente, manteniendo el área del pozo igual a uno.

Si el regulador funciona correctamente, la respuesta final para la energía de la función delta no debe depender de $a$.

1.  Para un valor dado de $a$, fije el valor de $V_0$ de modo que, en el límite $a \to 0$, el potencial $V_a$ represente correctamente a $V_\delta$. Dé su respuesta en términos de $\alpha$ y $a$.

2.  ¿Cuál es el valor de $z_0^2$ para el pozo $V_a$? ¿Qué le ocurre a $z_0$ cuando $a \to 0$? Explique por qué este comportamiento es razonable.

3.  Trabaje con $a$ muy pequeño pero distinto de cero, y calcule las aproximaciones dominantes de $\eta$ y $\xi$ en términos de $z_0$.

4.  Determine la energía del estado ligado del potencial delta a partir de su análisis del pozo. ¿Obtiene la respuesta correcta?

**NOTA:** Al tratarse de un problema de tipo demostración, ¡muestre su trabajo con claridad!

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*


---

<!-- MIT8.04_ExamenFinal_ES.md -->

# Examen Final (Final Test, otoño de 2015)

**8.04, Física Cuántica I, otoño de 2015**

**EXAMEN FINAL**

**Viernes 18 de diciembre, 13:30–16:30**

Tiene 3 horas = 180 minutos.

Responda todos los problemas en los cuadernillos proporcionados. Escriba SU NOMBRE y SU SECCIÓN en su(s) cuadernillo(s).

Hay seis preguntas, con un total de 105 puntos. Las tres primeras preguntas son más cortas; las tres últimas preguntas son más largas.

No se permiten libros, apuntes ni calculadoras.

Muestre su trabajo CLARAMENTE.

------------------------------------------------------------------------

## Formulario

- $\hbar c \simeq 197.3\ \text{MeV}\cdot\text{fm}\,, \quad m_e c^2 \simeq 0.511\ \text{MeV}\,, \quad m_p c^2 = 938\ \text{MeV}\,, \quad \dfrac{e^2}{\hbar c} \simeq \dfrac{1}{137}$

- Relatividad: $p = \gamma m v\,, \quad E = \gamma m c^2\,, \quad E^2 = p^2 c^2 + m^2 c^4\,, \quad \gamma = \dfrac{1}{\sqrt{1-\beta^2}}\,, \quad \beta = \dfrac{v}{c}$

- Fotones: $E = h\nu\,, \quad p = \dfrac{h}{\lambda}\,, \qquad$ o bien $\qquad E = \hbar\omega\,, \quad p = \hbar k$

- Longitudes de onda

  de Broglie: $\lambda = \dfrac{h}{p}\,, \qquad$ Compton: $\lambda_C = \dfrac{h}{mc}$.

- Operadores de momento y posición

$$p = \frac{\hbar}{i}\frac{\partial}{\partial x}\,, \quad [x,p] = i\hbar\,, \qquad \mathbf{p} = \frac{\hbar}{i}\nabla\,, \quad [x_i,p_j] = i\hbar\,\delta_{ij}\,, \quad [p_i, f(\mathbf{x})] = \frac{\hbar}{i}\frac{\partial f}{\partial x_i}$$

- Ecuación de Schrödinger

$$i\hbar \frac{\partial \Psi}{\partial t}(\mathbf{x},t) = \left(-\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{x},t)\right)\Psi(\mathbf{x},t)\,,$$

$$\frac{\partial}{\partial t}\rho(\mathbf{x},t) + \nabla\cdot\mathbf{J}(\mathbf{x},t) = 0$$

$$\rho(\mathbf{x},t) = |\Psi(\mathbf{x},t)|^2\,; \qquad \mathbf{J}(\mathbf{x},t) = \frac{\hbar}{m}\text{Im}\left[\Psi^*\nabla\Psi\right]$$

- Transformadas de Fourier:

$$\Psi(x) = \frac{1}{\sqrt{2\pi}}\int dk\, \Phi(k)e^{ikx}\,, \quad \Phi(k) = \frac{1}{\sqrt{2\pi}}\int dx\, \Psi(x)e^{-ikx}\,, \quad \int dx\,|\Psi(x)|^2 = \int dk\,|\Phi(k)|^2$$

$$\begin{aligned}
\Psi(\mathbf{x}) &= \frac{1}{(2\pi)^{3/2}}\int d^3k\, \Phi(\mathbf{k})e^{i\mathbf{k}\cdot\mathbf{x}}\,,\\
\Phi(\mathbf{k}) &= \frac{1}{(2\pi)^{3/2}}\int d^3x\, \Psi(\mathbf{x})e^{-i\mathbf{k}\cdot\mathbf{x}}\,,\\
\int d^3x\,|\Psi(\mathbf{x})|^2 &= \int d^3k\,|\Phi(\mathbf{k})|^2
\end{aligned}$$

$$\frac{1}{2\pi}\int_{-\infty}^{\infty} e^{ikx}\,dx = \delta(k)\,, \qquad \frac{1}{(2\pi)^3}\int_{-\infty}^{\infty} e^{i\mathbf{k}\cdot\mathbf{x}}\,d^3x = \delta^{(3)}(\mathbf{k})$$

$$\int_{-\infty}^{+\infty} dx\, \exp\!\left(-ax^2+bx\right) = \sqrt{\frac{\pi}{a}}\exp\!\left(\frac{b^2}{4a}\right)\,, \qquad \text{cuando } \text{Re}(a) > 0\,.$$

- Paquetes de ondas

$$v_{\text{grupo}} = \frac{d\omega}{dk}\,, \qquad \Delta k\,\Delta x \simeq 1\,, \qquad \text{sin distorsión de forma: } t\,\Delta v \le \Delta x$$

- Conjugación hermítica:

$$\int dx\, \left(K\Psi(x,t)\right)^*\Psi(x,t) = \int dx\, \Psi^*(x,t)\left(K^\dagger \Psi(x,t)\right)$$

Si $K^\dagger = K$, entonces $K$ es hermítico.

- Valores esperados

$$\langle Q\rangle(t) = \int dx\, \Psi^*(x,t)\left(Q\Psi(x,t)\right)$$

- Evolución temporal del valor esperado. Para $Q$ hermítico

$$i\hbar \frac{d}{dt}\langle Q\rangle = \langle [Q,H]\rangle$$

- Identidad del conmutador

$$[A,BC] = [A,B]C + B[A,C]$$

- Incertidumbre $\Delta Q$ de un operador hermítico $Q$

$$(\Delta Q)^2 = \langle Q^2\rangle - \langle Q\rangle^2 = \langle (Q-\langle Q\rangle)^2\rangle$$

- Principio de incertidumbre: $\Delta x\,\Delta p \ge \dfrac{\hbar}{2}$

$$\Delta x = \frac{\Delta}{\sqrt{2}} \quad \text{y} \quad \Delta p = \frac{\hbar}{\sqrt{2}\Delta} \quad \text{para} \quad \psi \sim \exp\!\left(-\frac{1}{2}\frac{x^2}{\Delta^2}\right)$$

- Estado estacionario:

$$\Psi(x,t) = \psi(x)e^{-iEt/\hbar}\,, \qquad -\frac{\hbar^2}{2m}\frac{d^2}{dx^2}\psi(x) + V(x)\psi(x) = E\,\psi(x)$$

- Pozo infinito de potencial

$$V(x) = \begin{cases} 0\,, & \text{para } 0 < x < a\,, \\ \infty & \text{en los demás casos} \end{cases}$$

$$\psi_n(x) = \sqrt{\frac{2}{a}}\sin\frac{n\pi x}{a}\,, \qquad E_n = \frac{\hbar^2\pi^2 n^2}{2ma^2}\,, \qquad n=1,2,\ldots$$

- Estados ligados del pozo finito de potencial: $E \le 0$

$$V(x) = \begin{cases} -V_0\,, & \text{para } |x|<a\,, \quad V_0 > 0 \\ 0 & \text{para } |x|>a \end{cases}$$

$$\eta^2 \equiv \frac{2m(E+V_0)a^2}{\hbar^2}\,, \qquad \xi^2 \equiv \frac{2m|E|a^2}{\hbar^2}\,, \qquad z_0^2 \equiv \frac{2mV_0 a^2}{\hbar^2}$$

$$\to \quad \frac{|E|}{V_0} = \frac{\xi^2}{z_0^2}\,, \qquad \xi^2 + \eta^2 = z_0^2$$

$$\text{Soluciones pares: } \xi = \eta\tan\eta \qquad\qquad \text{Soluciones impares: } \xi = -\eta\cot\eta$$

- Potencial delta de Dirac:

$$V = -\alpha\,\delta(x)\,, \quad \alpha > 0\,, \qquad \text{Estado ligado: } E = -\frac{m\alpha^2}{2\hbar^2}$$

- Oscilador armónico

$$\hat H = \frac{1}{2m}\hat p^2 + \frac{1}{2}m\omega^2 \hat x^2 = \hbar\omega\left(\hat N + \frac12\right)\,, \qquad \hat N = \hat a^\dagger \hat a$$

$$\hat a = \sqrt{\frac{m\omega}{2\hbar}}\left(\hat x + \frac{i\hat p}{m\omega}\right)\,, \qquad \hat a^\dagger = \sqrt{\frac{m\omega}{2\hbar}}\left(\hat x - \frac{i\hat p}{m\omega}\right)\,,$$

$$\hat x = \sqrt{\frac{\hbar}{2m\omega}}(\hat a + \hat a^\dagger)\,, \qquad \hat p = i\sqrt{\frac{m\omega\hbar}{2}}(\hat a^\dagger - \hat a)\,,$$

$$[\hat x,\hat p] = i\hbar\,, \quad [\hat a,\hat a^\dagger] = 1\,, \quad [\hat N,\hat a] = -\hat a\,, \quad [\hat N,\hat a^\dagger] = \hat a^\dagger\,.$$

$$\hat a \phi_0 = 0\,, \qquad \phi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}\exp\!\left(-\frac{m\omega}{2\hbar}x^2\right)\,.$$

$$\phi_n = \frac{1}{\sqrt{n!}}(\hat a^\dagger)^n \phi_0$$

$$\hat H\phi_n = E_n\phi_n = \hbar\omega\left(n+\frac12\right)\phi_n\,, \qquad \hat N\phi_n = n\phi_n\,, \qquad (\phi_m,\phi_n) = \delta_{mn}$$

$$\hat a^\dagger \phi_n = \sqrt{n+1}\,\phi_{n+1}\,, \qquad \hat a\,\phi_n = \sqrt{n}\,\phi_{n-1}\,.$$

- Estados de energía positiva

$$\psi(x) = Ae^{ikx} + Be^{-ikx}\,, \qquad J = \frac{\hbar k}{m}\left(|A|^2-|B|^2\right)\,, \qquad E = \frac{\hbar^2 k^2}{2m}$$

- Dispersión (scattering) en 1D. $V(x) = \infty$ para $x \le 0$. Solución $\phi(x) = \sin kx$ cuando $V=0$.

$$\psi(x) = e^{i\delta(k)}\sin\!\left(kx+\delta(k)\right)\,, \qquad x > R \ (R \text{ es el alcance})$$

Onda dispersada: $\psi = \phi + \psi_s$

$$\psi_s = A_s e^{ikx}\,, \qquad A_s = e^{i\delta}\sin\delta$$

$$\text{Retardo temporal: } \Delta t = 2\hbar\frac{d\delta}{dE} \quad \to \quad \frac{1}{R}\frac{d\delta}{dk} = \frac{\Delta t}{\text{tiempo de tránsito libre}}$$

$$N_{\text{ligados}} = \frac{1}{\pi}\left(\delta(0)-\delta(\infty)\right) \qquad \text{(teorema de Levinson)}$$

Resonancias: crecimiento rápido de $\delta$, gran retardo temporal, gran amplitud en la región interior.

- Momento angular orbital

$$\hat L_x = \hat y\,\hat p_z - \hat z\,\hat p_y\,, \qquad \hat L_y = \hat z\,\hat p_x - \hat x\,\hat p_z\,, \qquad \hat L_z = \hat x\,\hat p_y - \hat y\,\hat p_x\,.$$

$$[\hat L_x,\hat L_y] = i\hbar\,\hat L_z\,, \qquad [\hat L_y,\hat L_z] = i\hbar\,\hat L_x\,, \qquad [\hat L_z,\hat L_x] = i\hbar\,\hat L_y\,.$$

$$\hat L^2 \equiv \hat L_x\hat L_x + \hat L_y\hat L_y + \hat L_z\hat L_z\,, \qquad [\hat L^2,\hat L_i] = 0$$

$$\nabla^2 = \frac{1}{r}\frac{\partial^2}{\partial r^2}r + \frac{1}{r^2}\left(\frac{\partial^2}{\partial\theta^2} + \cot\theta\frac{\partial}{\partial\theta} + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}\right)$$

$$\hat L^2 = -\hbar^2\left(\frac{\partial^2}{\partial\theta^2} + \cot\theta\frac{\partial}{\partial\theta} + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}\right)$$

$$\hat L_z = \frac{\hbar}{i}\frac{\partial}{\partial\phi}\,; \qquad \hat L_\pm = \hbar e^{\pm i\phi}\left(\pm\frac{\partial}{\partial\theta} + i\cot\theta\frac{\partial}{\partial\phi}\right)$$

- Armónicos esféricos

$$Y_{\ell,m}(\theta,\phi) \equiv \mathcal{N}_{\ell,m}\,P_\ell^m(\cos\theta)\,e^{im\phi}$$

$$\hat L_z Y_{\ell m} = \hbar m\, Y_{\ell m}$$

$$\hat L^2 Y_{\ell m} = \hbar^2 \ell(\ell+1)\, Y_{\ell m}$$

$$\int d\Omega\, Y_{\ell'm'}^*(\theta,\phi)\, Y_{\ell m}(\theta,\phi) = \delta_{\ell'\ell}\,\delta_{m'm}\,, \qquad \int d\Omega = \int_0^{2\pi}d\phi \int_{-1}^{1} d(\cos\theta)$$

$$Y_{0,0}(\theta,\phi) = \frac{1}{\sqrt{4\pi}}\,; \qquad Y_{1,\pm1}(\theta,\phi) = \mp\sqrt{\frac{3}{8\pi}}\sin\theta\,\exp(\pm i\phi)\,; \qquad Y_{1,0}(\theta,\phi) = \sqrt{\frac{3}{4\pi}}\cos\theta$$

- Potenciales centrales: $V(\mathbf{r}) = V(r)$

$$\psi(r,\theta,\phi) = \frac{u(r)}{r}\,Y_{\ell m}(\theta,\phi)$$

$$\left(-\frac{\hbar^2}{2m}\frac{d^2}{dr^2} + V(r) + \frac{\hbar^2\ell(\ell+1)}{2mr^2}\right)u(r) = E\,u(r)$$

$$u(r) \sim r^{\ell+1}\,, \qquad \text{cuando } r \to 0\,.$$

- Átomo de hidrógeno:

$$H = \frac{p^2}{2m} - \frac{Ze^2}{r}$$

$$E_n = -\frac{Z^2 e^2}{2a_0}\frac{1}{n^2}\,, \qquad a_0 = \frac{\hbar^2}{me^2} \simeq 0.529\times 10^{-10}\ \text{m}\,, \qquad \frac{e^2}{2a_0} \simeq 13.6\ \text{eV}$$

$$\psi_{n,\ell,m}(\vec{x}) = A\left(\frac{r}{a_0}\right)^\ell \Big(\text{Polinomio en } \tfrac{r}{a_0} \text{ de grado } n-(\ell+1)\Big)\, e^{-\frac{Zr}{na_0}}\, Y_{\ell,m}(\theta,\phi)$$

$$n = 1,2,\ldots\,, \qquad \ell = 0,1,\ldots,n-1\,, \qquad m = -\ell,\ldots,\ell$$

$$\psi_{n,\ell,m}(\vec{x}) = \frac{u_{n\ell}(r)}{r}\,Y_{\ell,m}(\theta,\phi)$$

$$u_{1,0}(r) = \frac{2r}{a_0^{3/2}}\exp(-r/a_0)$$

$$u_{2,0}(r) = \frac{2r}{(2a_0)^{3/2}}\left(1-\frac{r}{2a_0}\right)\exp(-r/2a_0)$$

$$u_{2,1}(r) = \frac{1}{\sqrt3}\frac{1}{(2a_0)^{3/2}}\frac{r^2}{a_0}\exp(-r/2a_0)$$

------------------------------------------------------------------------

## Problema 1. Teorema del virial para potenciales unidimensionales \[15 puntos\]

1.  Sea $\psi(x)$ un autoestado de energía. Explique por qué el valor esperado $\langle [H,\Omega]\rangle$ del conmutador de $H$ con un operador arbitrario $\Omega$ se anula en el estado $\psi$.

2.  Elija $\Omega = xp$, y tome

$$H = \frac{p^2}{2m} + V(x)\,.$$

Use el resultado del apartado (a) para hallar una relación entre el valor esperado $\langle T\rangle$ de la energía cinética y el valor esperado de una combinación de $x$ y la derivada $V'(x)$ del potencial respecto a su argumento. Ambos valores esperados se toman sobre un autoestado de energía.

1.  ¿Qué implica su resultado del apartado (b) para la relación entre $\langle T\rangle$ y $\langle V\rangle$ en el caso del oscilador armónico unidimensional?

## Problema 2. Órbita del electrón en el átomo de hidrógeno \[15 puntos\]

A lo largo de este problema consideramos un átomo de hidrógeno con número cuántico principal $n$ fijo, con $\ell = n-1$, y $m = n-1$. El valor de $n$ es arbitrario y posiblemente grande.

1.  Escriba la función de onda $\psi_{n,\ell,m}(r,\theta,\phi)$ en términos del armónico esférico correspondiente y un factor radial completamente determinado salvo por una constante de normalización adimensional global $N$.

2.  Dé, salvo normalización, la densidad de probabilidad radial $P(r)$ tal que $P(r)\,dr$ es la probabilidad de encontrar al electrón en el intervalo $(r, r+dr)$. ¿Para qué valor de $r$ es $P(r)$ máxima? Para $n$ grande, este es de hecho un máximo bastante pronunciado.

3.  Se sabe que, salvo normalización,

$$|Y_{\ell,\ell}(\theta,\phi)|^2 \simeq (\sin\theta)^{2\ell}\,.$$

Dibuje $|Y_{\ell,\ell}|^2$ en función de $\theta \in [0,\pi]$ cuando $\ell$ es un entero grande. Describa, con palabras y/o con un dibujo, el lugar geométrico donde es probable encontrar al electrón para $n$ grande y $\ell = m = n-1$.

## Problema 3. Determinación del paquete de ondas saliente \[15 puntos\]

En un problema de dispersión (scattering) unidimensional con un potencial de alcance $R$, escribimos la solución $\psi(x)$ para $x > R$ como

$$\psi(x) = e^{i\delta(k)}\sin\!\left(kx+\delta(k)\right)\,, \qquad x > R\,.$$

1.  Descomponga esta $\psi(x)$ en la suma de una onda incidente $\psi_{\text{inc}}(x)$ que viaja hacia $x=0$ y una onda saliente $\psi_{\text{out}}(x)$ que se aleja de $x=0$.

2.  Enviamos un paquete de ondas localizado $\Psi_{\text{inc}}(x,t)$ dado por

$$\Psi_{\text{inc}}(x,t) = \int_0^\infty dk\, f(k)\, e^{-ikx}\, e^{-iE(k)t/\hbar}\,, \qquad x > R\,,$$

con $f(k)$ una función cuya magnitud presenta un pico agudo en $k=k_0>0$. Escriba una expresión análoga para el paquete de ondas saliente asociado $\Psi_{\text{out}}(x,t)$.

1.  Use la aproximación de fase estacionaria para hallar la relación entre $x$ y $t$ que describe el movimiento del paquete saliente $\Psi_{\text{out}}(x,t)$.

## Problema 4. Hacia la detección perfecta de bombas \[20 puntos\]

Modificamos el dispositivo de Mach-Zehnder para aumentar hasta el 100% la fracción de bombas de Elitzur-Vaidman (EV) que pueden certificarse como operativas sin detonarlas. Una bomba EV se activa mediante un detector de fotones: si el detector está operativo, cualquier fotón incidente sobre él hará explotar la bomba; si está defectuoso, el detector deja pasar todos los fotones y la bomba no explota.

Para mejorar la detección usamos un divisor de haz de alta reflectividad, en adelante llamado BS (*beam-splitter*), representado por una matriz unitaria $2\times 2$, $U$, de la forma

$$U = \begin{pmatrix} \cos\dfrac{\pi}{2N} & i\sin\dfrac{\pi}{2N} \\[2mm] i\sin\dfrac{\pi}{2N} & \cos\dfrac{\pi}{2N} \end{pmatrix}\,,$$

con $N$ un entero positivo grande y fijo. Note que BS es un divisor de haz con reflectividad $R$ y transmisividad $T$ dadas por

$$R = \left(\cos\frac{\pi}{2N}\right)^2\,, \qquad T = \left(\sin\frac{\pi}{2N}\right)^2\,, \qquad R+T=1\,.$$

Imaginaremos el divisor de haz BS colocado verticalmente, con un fotón a la izquierda de BS representado por $\begin{pmatrix}1\\0\end{pmatrix}$ y un fotón a la derecha de BS representado por $\begin{pmatrix}0\\1\end{pmatrix}$. Esto es válido tanto para fotones que se mueven hacia BS como para los que se alejan de él.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_ExamenFinal_ES/fig1.png)

Figura: un fotón incidente representado por $\begin{pmatrix}1\\0\end{pmatrix}$ se acerca a BS desde la izquierda; otro fotón representado por $\begin{pmatrix}0\\1\end{pmatrix}$ se acerca a BS desde la derecha.

Fórmula útil:

$$\begin{pmatrix}\cos\alpha & i\sin\alpha \\ i\sin\alpha & \cos\alpha\end{pmatrix}\begin{pmatrix}\cos\beta & i\sin\beta \\ i\sin\beta & \cos\beta\end{pmatrix} = \begin{pmatrix}\cos(\alpha+\beta) & i\sin(\alpha+\beta) \\ i\sin(\alpha+\beta) & \cos(\alpha+\beta)\end{pmatrix}\,.$$

1.  Calcule la $k$-ésima potencia $U^k$ de la matriz $U$.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_ExamenFinal_ES/fig2.png)

Figura: una cavidad con el divisor de haz BS entre dos espejos perfectamente reflectantes $M_1$ (izquierda) y $M_2$ (derecha); un fotón entra desde la izquierda hacia BS. Se indican el «lado izquierdo» y el «lado derecho» de la cavidad, separados por BS.

1.  Ahora construimos una cavidad en la que el divisor de haz BS se coloca entre espejos perfectamente reflectantes $M_1$ y $M_2$, a distancias iguales a la izquierda y a la derecha. Se envía un fotón desde la izquierda, como se muestra en la figura. El fotón incidirá sobre BS y se dividirá; las componentes reflejada y transmitida rebotarán en los espejos e incidirán sobre BS por segunda vez, y así sucesivamente.

Tras $k$ incidencias sobre BS, ¿cuál es la probabilidad $p_L(k)$ de que el fotón se encuentre en el lado izquierdo de la cavidad, y cuál es la probabilidad $p_R(k)$ de que se encuentre en el lado derecho de la cavidad? ¿Cuáles son esas probabilidades para $k=N$?

1.  Se inserta un detector de fotones en el lado derecho de la cavidad, de modo que cualquier fotón que llegue al lado derecho será detectado (¡y absorbido!). Como antes, se envía un fotón desde la izquierda. Tras esperar el tiempo necesario para $N$ incidencias sobre BS, ¿cuál es la probabilidad $P_L(N)$ de que el fotón se encuentre en el lado izquierdo de la cavidad? ¿Cuál es la probabilidad $P_D(N)$ de que el fotón haya sido detectado?

2.  Estime $P_L(N)$ y $P_D(N)$ en el límite en que $N$ es grande. Fórmulas útiles: $\cos\epsilon \simeq 1-\tfrac12\epsilon^2$, $(1+\epsilon)^k \simeq 1+k\epsilon$ para $\epsilon$ suficientemente pequeño.

3.  Dada una bomba EV, la insertamos en el lado derecho de la cavidad. Enviamos un fotón desde la izquierda y esperamos el tiempo necesario para $N$ incidencias sobre BS. Llegado ese punto, si el laboratorio no ha estallado, buscamos el fotón.

<!-- -->

1.  ¿Qué podemos concluir si el fotón se encuentra en el lado izquierdo de la cavidad?

2.  ¿Cuál es la probabilidad $P_E(N)$ de que una bomba EV operativa explote en este experimento? Dé un valor aproximado para $N=250$.

## Problema 5. Pozo infinito de potencial con una dimensión extra: un cilindro truncado \[20 puntos\]

Una partícula en un pozo infinito de potencial unidimensional de anchura $a$ puede pensarse como una partícula obligada a moverse en un segmento de línea de longitud $a$. Consideremos una partícula que se mueve en un pequeño cilindro de longitud $a$. El cilindro tiene circunferencia $L$ y puede representarse como una región rectangular en el plano $(x,y)$, con la coordenada $y$ a lo largo de la circunferencia del cilindro, identificando las líneas horizontales marcadas con flechas.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_ExamenFinal_ES/fig3.png)

Figura: un rectángulo en el plano $(x,y)$ de anchura $a$ (eje $x$) y altura $L$ (eje $y$); los bordes horizontales superior e inferior, marcados con flechas en la misma dirección, están identificados entre sí, representando así un cilindro de longitud $a$ y circunferencia $L$.

El sistema se describe mediante la ecuación de Schrödinger (ES) bidimensional con un potencial que se anula en el rectángulo $\{(x,y): 0 \le x \le a,\ 0 \le y \le L\}$, y que es infinito en los bordes verticales $x=0$ y $x=a$.

1.  Realice la separación de variables en la ES y dé las dos ecuaciones que permiten determinar los autoestados de energía. Indique las condiciones de contorno que se aplican.

2.  Resuelva para los autovalores de energía $E_{n\ell}$ y los autoestados normalizados $\psi_{n\ell}(x,y)$, donde $n$ y $\ell$ son números cuánticos asociados a la dependencia en $x$ y en $y$, respectivamente. Indique con precisión los rangos que recorren $n$ y $\ell$.

3.  ¿Cuál es la energía del estado fundamental de la partícula?

4.  Suponga, de aquí en adelante, que $a$ y $L$ son tales que no ocurren degeneraciones accidentales (las degeneraciones accidentales son aquellas que requieren relaciones especiales entre $a$ y $L$). ¿Cuál es la lista de autovalores de energía de la partícula en el cilindro que coinciden con los del segmento unidimensional $x\in[0,a]$?

5.  ¿Cuáles son (o cuál es) los niveles de energía más bajos que existen en el cilindro pero que no existen en el segmento?

6.  La dimensión $y$ que convierte el segmento en un cilindro puede considerarse como una pequeña dimensión extra aún no detectada. Suponga que el tamaño $L$ de la dimensión extra es aproximadamente 1000 veces menor que el tamaño $a$ del pequeño intervalo en el que un experimentador ha localizado una partícula. Suponga también que la longitud $a$ y la masa $m$ de la partícula son tales que

$$\frac{\hbar^2}{2ma^2} = 1\ \text{eV}\,.$$

Estime la energía mínima que el experimentador necesita explorar para encontrar evidencia de la dimensión extra.

## Problema 6. Transmisión resonante a través de dos funciones delta \[20 puntos\]

Considere un potencial con dos funciones delta de intensidad positiva, una en $x=-a$ y otra en $x=a$:

$$V(x) = g\,\delta(x+a) + g\,\delta(x-a)\,.$$

Note la combinación adimensional $\lambda$ que representa la intensidad efectiva del potencial:

$$\lambda = \frac{mag}{\hbar^2} \ge 0\,.$$

Al resolver el problema general de dispersión de una partícula incidente desde la izquierda, se plantea una función de onda

$$\psi(x) = \begin{cases} A e^{ikx} + B e^{-ikx}\,, & x < -a\,, \\ C e^{ikx} + D e^{-ikx}\,, & |x| < a\,, \\ F e^{ikx}\,, & x > a\,. \end{cases}$$

Aquí $A, B, C, D, F$ son constantes complejas que deben ajustarse para que esta sea una solución de la ecuación de Schrödinger independiente del tiempo. Nos interesa hallar las energías para las cuales hay transmisión resonante, es decir, ¡el coeficiente de transmisión vale uno!

1.  ¿Cuál de las constantes complejas en el ansatz anterior para $\psi$ debe anularse para que haya transmisión resonante? Explique brevemente.

2.  Suponga que esa constante se anula y halle las cuatro ecuaciones que implementan las condiciones de contorno. Simplifíquelas y escríbalas en la forma:

$$C + D\, e^{\cdots} = \cdots$$

$$C + D\, e^{\cdots} = \cdots$$

$$C - D\, e^{\cdots} = \cdots$$

$$C - D\, e^{\cdots} = \cdots$$

Las expresiones indicadas por puntos suspensivos deben escribirse en términos de $ka$, $\lambda$, las constantes del ansatz para $\psi$ y constantes numéricas.

1.  Afirmamos ahora que la existencia de una solución para las ecuaciones anteriores requiere

$$\xi\cot\xi = -2\lambda\,, \qquad \text{con } \xi = 2ka\,. \tag{1}$$

¡No es necesario que lo demuestre! Muestre una gráfica de $\xi\cot\xi$ para $\xi\in[0,3\pi]$. Muestre la recta $-2\lambda$ en la gráfica, tanto para $\lambda$ muy pequeño como para $\lambda$ muy grande. Para $\lambda \ll 1$, ¿cuáles son los valores aproximados de $ka$ para transmisión perfecta? Para $\lambda \gg 1$, ¿cuáles son los valores aproximados de $ka$ para transmisión perfecta?

1.  Bajo la condición (1) puede demostrarse que

$$\frac{C}{D} = -\frac{1}{\cos(2ka)}\,, \qquad C = \left(1+\frac{\lambda}{ika}\right)A\,.$$

Considere el caso $\lambda \gg 1$ y la primera transmisión resonante. Halle una fórmula aproximada para $\psi$ en la región $|x|<a$ y, fijando $A=1$, haga un esbozo aproximado de $|\psi(x)|^2$ para todo $x$. ¡Comente las características de su gráfica!

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*


---

<!-- MIT8.04_LecNotes10_ES.md -->

# Lección 10: Resolución de la ecuación de Schrödinger independiente del tiempo

## Vídeos de esta clase (YouTube)

**Lección 10: Uncertainty (cont.). Stationary states. Particle on a circle.**

- [Uncertainty and eigenstates](https://www.youtube.com/watch?v=1D4VPbhDy_A)
- [Stationary states: key equations](https://www.youtube.com/watch?v=8KQ-yK2xm60)
- [Expectation values on stationary states](https://www.youtube.com/watch?v=M2i8R6kMXKA)
- [Comments on the spectrum and continuity conditions](https://www.youtube.com/watch?v=gMnQ21-pjOA)
- [Solving particle on a circle](https://www.youtube.com/watch?v=2EV1vJAAo8M)

------------------------------------------------------------------------

B. Zwiebach

14 de marzo de 2016

## Contenido

1.  Estados estacionarios
2.  Resolución para los autoestados de energía
3.  Partícula libre en un círculo

## 1. Estados estacionarios

Consideremos la ecuación de Schrödinger para la función de onda $\Psi(x, t)$ bajo el supuesto de que la energía potencial $V$ es independiente del tiempo:

$$i\hbar \frac{\partial \Psi}{\partial t} = \hat{H}\Psi(x, t) = \left( -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x) \right) \Psi(x, t) \qquad \text{(1.1)}$$

donde hemos mostrado la forma del operador hamiltoniano $\hat{H}$ con el potencial independiente del tiempo $V(x)$. Los estados estacionarios son una clase de soluciones muy útil de esta ecuación diferencial. La propiedad distintiva de un estado estacionario es que la dependencia espacial y temporal de la función de onda se factorizan. Es decir,

$$\Psi(x, t) = g(t)\, \psi(x) \qquad \text{(1.2)}$$

para ciertas funciones $g$ y $\psi$. Para que exista una solución separable de este tipo necesitamos que el potencial sea independiente del tiempo, como veremos a continuación. La solución $\Psi(x, t)$ depende del tiempo, pero se denomina estacionaria debido a una propiedad de los observables. El valor esperado de los observables sin dependencia temporal explícita en estados arbitrarios sí depende del tiempo. En un estado estacionario no depende del tiempo, como demostraremos.

Usemos el ansatz (1.2) para $\Psi$ en la ecuación de Schrödinger. Obtenemos entonces

$$i\hbar \left( \frac{dg(t)}{dt} \right) \psi(x) = g(t)\, \hat{H}\psi(x) \qquad \text{(1.3)}$$

porque $g(t)$ puede desplazarse a través de $\hat{H}$. Podemos entonces dividir esta ecuación por $\Psi(x,t) = g(t)\psi(x)$, obteniendo

$$i\hbar \frac{1}{g(t)} \frac{dg(t)}{dt} = \frac{1}{\psi(x)} \hat{H}\psi(x) \qquad \text{(1.4)}$$

El lado izquierdo es una función solo de $t$, mientras que el lado derecho es una función solo de $x$ (un potencial dependiente del tiempo habría arruinado esto). La única forma en que ambos lados pueden ser iguales entre sí para todos los valores de $t$ y $x$ es que ambos lados sean iguales a una constante $E$ con unidades de energía, porque $\hat{H}$ tiene unidades de energía. Obtenemos así dos ecuaciones separadas. La primera es

$$i\hbar \frac{dg}{dt} = E g \qquad \text{(1.5)}$$

Esta se resuelve mediante

$$g(t) = e^{-iEt/\hbar} \qquad \text{(1.6)}$$

y la solución más general es simplemente una constante multiplicada por el lado derecho anterior. Del lado dependiente de $x$ de la igualdad obtenemos

$$\hat{H}\psi(x) = E\psi(x) \qquad \text{(1.7)}$$

Esta ecuación es una ecuación de autovalores para el operador hermítico $\hat{H}$. Hemos mostrado que los autovalores de los operadores hermíticos deben ser reales, por lo que la constante $E$ debe ser real. La ecuación anterior se denomina la ecuación de Schrödinger independiente del tiempo. Más explícitamente se escribe

$$\left( -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x) \right) \psi(x) = E\psi(x) \qquad \text{(1.8)}$$

Nótese que esta ecuación no determina la normalización global de $\psi$. Por lo tanto, podemos escribir la solución completa sin pérdida de generalidad usando la $g(t)$ dada anteriormente:

$$\text{Estado estacionario:}\quad \Psi(x, t) = e^{-iEt/\hbar}\, \psi(x), \quad \text{con } E \in \mathbb{R} \ \text{ y } \ \hat{H}\psi = E\psi \qquad \text{(1.9)}$$

Nótese que no solo $\psi(x)$ es un autoestado del operador hamiltoniano $\hat{H}$, sino que el estado estacionario completo también es un autoestado de $\hat{H}$:

$$\hat{H}\Psi(x, t) = E\Psi(x, t) \qquad \text{(1.10)}$$

ya que la función dependiente del tiempo en $\Psi$ se cancela.

Hemos notado que la energía $E$ debe ser real. Si no lo fuera, también tendríamos problemas para normalizar el estado estacionario de manera consistente. La condición de normalización para $\Psi$, si $E$ no fuera real, daría

$$\begin{aligned}
1 &= \int dx\, \Psi^*(x,t)\Psi(x,t) = \int dx\, e^{iE^*t/\hbar} e^{-iEt/\hbar} \psi^*(x)\psi(x)\\
&= e^{i(E^*-E)t/\hbar} \int dx\, \psi^*(x)\psi(x) = e^{2\,\mathrm{Im}(E)t/\hbar} \int dx\, \psi^*(x)\psi(x) \qquad \text{(1.11)}
\end{aligned}$$

La expresión final tiene una dependencia temporal debida a la exponencial. Por otro lado, la condición de normalización establece que esta expresión debe ser igual a uno. De ello se sigue que el exponente debe ser cero, es decir, $E$ es real. Dado esto, vemos también que la condición de normalización arroja

$$\int_{-\infty}^{\infty} dx\, \psi^*(x)\psi(x) = 1 \qquad \text{(1.12)}$$

¿Cómo interpretamos el autovalor $E$? Usando (1.10) vemos que el valor esperado de $\hat{H}$ en el estado $\Psi$ es efectivamente la energía

$$\langle\langle \hat{H} \rangle\rangle_\Psi = \int dx\, \Psi^*(x,t)\, \hat{H}\Psi(x,t) = \int dx\, \Psi^*(x,t)\, E\Psi(x,t) = E \int dx\, \Psi^*(x,t)\Psi(x,t) = E \qquad \text{(1.13)}$$

Dado que el estado estacionario es un autoestado de $\hat{H}$, la incertidumbre $\Delta H$ del hamiltoniano en un estado estacionario es cero.

Hay dos observaciones importantes sobre los estados estacionarios:

**(1)** El valor esperado de cualquier operador independiente del tiempo $\hat{Q}$ en un estado estacionario $\Psi$ es independiente del tiempo:

$$\langle\langle \hat{Q} \rangle\rangle_{\Psi(x,t)} = \int dx\, \Psi^*(x,t)\, \hat{Q}\Psi(x,t) = \int dx\, e^{iEt/\hbar}\psi^*(x)\, \hat{Q} e^{-iEt/\hbar}\psi(x)$$

$$= \int dx\, e^{iEt/\hbar} e^{-iEt/\hbar} \psi^*(x)\hat{Q}\psi(x) = \int dx\, \psi^*(x)\hat{Q}\psi(x) = \langle\langle \hat{Q} \rangle\rangle_{\psi(x)} \qquad \text{(1.14)}$$

ya que el último valor esperado es manifiestamente independiente del tiempo.

**(2)** La superposición de estados estacionarios con energías diferentes no es estacionaria. Esto es claro porque un estado estacionario requiere una solución factorizada de la ecuación de Schrödinger: si sumamos dos soluciones factorizadas con energías diferentes, estas tendrán dependencias temporales distintas y el estado total no podrá factorizarse. Ahora mostraremos que un observable independiente del tiempo $\hat{Q}$ puede tener un valor esperado dependiente del tiempo en tal estado. Consideremos una superposición

$$\Psi(x, t) = c_1 e^{-iE_1 t/\hbar} \psi_1(x) + c_2 e^{-iE_2 t/\hbar} \psi_2(x) \qquad \text{(1.15)}$$

donde $\psi_1$ y $\psi_2$ son autoestados de $\hat{H}$ con energías $E_1$ y $E_2$, respectivamente. Consideremos un operador hermítico $\hat{Q}$. Con el sistema en el estado (1.15), su valor esperado es

$$\langle\langle \hat{Q} \rangle\rangle_\Psi = \int_{-\infty}^{\infty} dx\, \Psi^*(x,t)\, \hat{Q}\Psi(x,t)$$

$$= \int_{-\infty}^{\infty} dx \left[ c_1^* e^{iE_1 t/\hbar}\psi_1^*(x) + c_2^* e^{iE_2 t/\hbar}\psi_2^*(x) \right] \left[ c_1 e^{-iE_1 t/\hbar}\hat{Q}\psi_1(x) + c_2 e^{-iE_2 t/\hbar}\hat{Q}\psi_2(x) \right]$$

$$= \int_{-\infty}^{\infty} dx \Big[ |c_1|^2 \psi_1^*\hat{Q}\psi_1 + |c_2|^2 \psi_2^*\hat{Q}\psi_2 + c_1^* c_2\, e^{i(E_1-E_2)t/\hbar}\, \psi_1^*\hat{Q}\psi_2 + c_2^* c_1\, e^{-i(E_1-E_2)t/\hbar}\, \psi_2^*\hat{Q}\psi_1 \Big] \qquad \text{(1.16)}$$

Ahora vemos la posible dependencia temporal que surge de los términos cruzados. Los dos primeros términos son valores esperados simples e independientes del tiempo. Usando la hermiticidad de $\hat{Q}$ en el último término obtenemos entonces

$$\langle\langle \hat{Q} \rangle\rangle_\Psi = |c_1|^2 \langle\langle \hat{Q} \rangle\rangle_{\psi_1} + |c_2|^2 \langle\langle \hat{Q} \rangle\rangle_{\psi_2}$$

$$+\, c_1^* c_2\, e^{i(E_1-E_2)t/\hbar} \int_{-\infty}^{\infty} dx\, \psi_1^*\hat{Q}\psi_2 + c_1 c_2^*\, e^{-i(E_1-E_2)t/\hbar} \int_{-\infty}^{\infty} dx\, \psi_1 (\hat{Q}\psi_2)^* \qquad \text{(1.17)}$$

Los dos últimos términos son complejos conjugados entre sí y por lo tanto

$$\langle\langle \hat{Q} \rangle\rangle_\Psi = |c_1|^2 \langle\langle \hat{Q} \rangle\rangle_{\psi_1} + |c_2|^2 \langle\langle \hat{Q} \rangle\rangle_{\psi_2} + 2\,\mathrm{Re}\left[ c_1^* c_2\, e^{i(E_1-E_2)t/\hbar} \int_{-\infty}^{\infty} dx\, \psi_1^*\hat{Q}\psi_2 \right] \qquad \text{(1.18)}$$

Vemos que este valor esperado depende del tiempo si $E_1 \neq E_2$ y $(\psi_1, \hat{Q}\psi_2)$ es distinto de cero. El valor esperado completo $\langle\langle \hat{Q} \rangle\rangle_\Psi$ es real, como debe serlo para cualquier operador hermítico.

## 2. Resolución para los autoestados de energía

Ahora estudiaremos las soluciones de la ecuación de Schrödinger independiente del tiempo

$$\hat{H}\psi(x) = E\, \psi(x) \qquad \text{(2.19)}$$

Dado un hamiltoniano $\hat{H}$, nos interesa encontrar los autoestados $\psi$ y los autovalores $E$, que resultan ser las energías correspondientes. Quizás la característica más interesante de la ecuación anterior es que, en general, el valor de $E$ no puede ser arbitrario. Al igual que las matrices de tamaño finito tienen un conjunto de autovalores, la ecuación de Schrödinger independiente del tiempo anterior puede tener un conjunto discreto de energías posibles. También se permite un conjunto continuo de energías posibles, lo cual a veces es importante. En efecto, hay muchas soluciones para cualquier potencial dado. Suponiendo, por conveniencia, que los autoestados y sus energías pueden contarse, escribimos

$$\psi_1(x)\,, \ E_1 \qquad \psi_2(x)\,, \ E_2 \qquad \dots \qquad \text{(2.20)}$$

Nuestra discusión anterior sobre operadores hermíticos se aplica aquí. Los autoestados de energía pueden organizarse para formar un conjunto completo de funciones ortonormales:

$$\int \psi_i^*(x)\psi_j(x) = \delta_{ij} \qquad \text{(2.21)}$$

Consideremos la ecuación de Schrödinger independiente del tiempo escrita como

$$\frac{d^2\psi}{dx^2} = -\frac{2m}{\hbar^2}\left(E - V(x)\right)\psi \qquad \text{(2.22)}$$

Las soluciones $\psi(x)$ dependen de las propiedades del potencial $V(x)$. Es difícil hacer afirmaciones generales sobre la función de onda a menos que restrinjamos los tipos de potenciales. Sin duda consideraremos potenciales continuos. También consideraremos potenciales que no son continuos pero que son continuos a trozos, es decir, que tienen cierto número de discontinuidades. Nuestros potenciales pueden fácilmente no estar acotados. Permitimos funciones delta en los potenciales unidimensionales, pero no consideramos potencias o derivadas de funciones delta. Permitimos potenciales que se vuelven infinitos positivos más allá de ciertos puntos. Estos puntos representan paredes duras.

Queremos entender las propiedades generales de $\psi$ y el comportamiento de $\psi$ en los puntos donde el potencial $V(x)$ puede tener discontinuidades u otras singularidades. Afirmamos: debemos tener una función de onda continua. Si $\psi$ fuera discontinua, entonces $\psi'$ contendría funciones delta y $\psi''$, en el lado izquierdo de la ecuación anterior, contendría derivadas de funciones delta. Esto requeriría que el lado derecho tuviera derivadas de funciones delta, y estas tendrían que aparecer en el potencial. Dado que hemos declarado que nuestros potenciales no contienen derivadas de funciones delta, debemos tener efectivamente una $\psi$ continua.

Consideremos ahora cuatro posibilidades respecto al potencial:

**(1)** $V(x)$ es continuo. En este caso, la continuidad de $\psi(x)$ y (2.22) implican que $\psi''$ también es continua. Esto requiere que $\psi'$ sea continua.

**(2)** $V(x)$ tiene discontinuidades finitas. En este caso $\psi''$ tiene discontinuidades finitas: incluye el producto de una $\psi$ continua por una $V$ discontinua. Pero entonces $\psi'$ debe ser continua, con derivada no continua.

**(3)** $V(x)$ contiene funciones delta. En este caso $\psi''$ también contiene funciones delta: es proporcional al producto de una $\psi$ continua y una función delta en $V$. Por lo tanto $\psi'$ tiene discontinuidades finitas.

**(4)** $V(x)$ contiene una pared dura. Se dice que un potencial que es finito inmediatamente a la izquierda de $x = a$ y se vuelve infinito para $x > a$ tiene una pared dura en $x = a$. En tal caso, la función de onda se anulará para $x \geq a$. La pendiente $\psi'$ será finita cuando $x \to a$ por la izquierda, y se anulará para $x > a$. Por lo tanto $\psi'$ es discontinua en la pared.

En los dos primeros casos $\psi'$ es continua, y en los dos últimos puede tener una discontinuidad finita. En conclusión

$$\begin{gathered}
\text{Tanto } \psi \text{ como } \psi' \text{ son continuas a menos que el potencial tenga funciones}\\
\text{delta o paredes duras, en cuyo caso } \psi' \text{ puede tener discontinuidades finitas.} \qquad \text{(2.23)}
\end{gathered}$$

Demos un argumento ligeramente distinto para la continuidad de $\psi$ y $\dfrac{d\psi}{dx}$ en el caso de un potencial con una discontinuidad finita, como el escalón mostrado en la Fig. 1.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes10_ES/fig1.png)

Figura 1: Un potencial $V(x)$ con una discontinuidad finita en $x = a$.

Integremos ambos lados de (2.22) de $a - \epsilon$ a $a + \epsilon$, y luego tomemos $\epsilon \to 0$. Encontramos

$$\int_{a-\epsilon}^{a+\epsilon} \frac{d}{dx}\left(\frac{d\psi}{dx}\right) dx = -\frac{2m}{\hbar^2} \int_{a-\epsilon}^{a+\epsilon} dx\, (E - V(x))\psi(x) \qquad \text{(2.24)}$$

El integrando del lado izquierdo es una derivada total, así que tenemos

$$\left. \frac{d\psi}{dx} \right|_{a+\epsilon} - \left. \frac{d\psi}{dx} \right|_{a-\epsilon} = \frac{2m}{\hbar^2} \int_{a-\epsilon}^{a+\epsilon} dx\, (V(x) - E)\psi(x) \qquad \text{(2.25)}$$

Por definición, la discontinuidad de la derivada de $\psi$ en $x=a$ es el límite cuando $\epsilon \to 0$ del lado izquierdo:

$$\Delta_a\!\left(\frac{d\psi}{dx}\right) \equiv \lim_{\epsilon \to 0} \left( \left. \frac{d\psi}{dx} \right|_{a+\epsilon} - \left. \frac{d\psi}{dx} \right|_{a-\epsilon} \right) \qquad \text{(2.26)}$$

Sustituyendo en (2.25) tenemos entonces

$$\Delta_a\!\left(\frac{d\psi}{dx}\right) = \lim_{\epsilon \to 0} \frac{2m}{\hbar^2} \int_{a-\epsilon}^{a+\epsilon} dx\, (V(x) - E)\psi(x) \qquad \text{(2.27)}$$

El potencial $V$ es discontinuo pero no infinito alrededor de $x = a$, tampoco $\psi$ es infinita alrededor de $x = a$ y, por supuesto, se supone que $E$ es finita. A medida que el rango de integración se hace infinitesimalmente pequeño alrededor de $x = a$, el integrando permanece finito y la integral tiende a cero. Tenemos así

$$\Delta_a\!\left(\frac{d\psi}{dx}\right) = 0 \qquad \text{(2.28)}$$

No hay discontinuidad en $\dfrac{d\psi}{dx}$. Esto nos da una de nuestras condiciones de contorno.

Para conocer la continuidad de $\psi$ reconsideramos la primera integral de la ecuación diferencial. La integración que llevó a (2.25), ahora aplicada al rango desde $x_0 < a$ hasta $x$, arroja

$$\left. \frac{d\psi(x)}{dx} \right. = \left. \frac{d\psi}{dx} \right|_{x_0} - \frac{2m}{\hbar^2} \int_{x_0}^{x} (E - V(x'))\, dx' \qquad \text{(2.29)}$$

Nótese que la integral del lado derecho es una función acotada de $x$. Ahora integramos de nuevo desde $a - \epsilon$ hasta $a + \epsilon$. Dado que el primer término del lado derecho es una constante, encontramos

$$\psi(a+\epsilon) - \psi(a-\epsilon) = \left. \frac{d\psi}{dx} \right|_{x_0} \cdot 2\epsilon - \frac{2m}{\hbar^2} \int_{a-\epsilon}^{a+\epsilon} dx \int_{x_0}^{x} dx'\, (E - V(x')) \qquad \text{(2.30)}$$

Tomando el límite $\epsilon \to 0$, el primer término del lado derecho claramente se anula y el segundo término también tiende a cero porque $\int_{x_0}^{x} dx'\,(E - V(x'))$ es una función acotada de $x$. Como resultado tenemos

$$\Delta_a \psi = 0 \qquad \text{(2.31)}$$

lo que muestra que la función de onda es continua en $x = a$. Esta es nuestra segunda condición de contorno.

## 3. Partícula libre en un círculo

Consideremos ahora el problema de una partícula confinada a un círculo de circunferencia $L$. La coordenada a lo largo del círculo se denomina $x$ y podemos ver el círculo como el intervalo $x \in [0, L]$ con los extremos identificados. Quizás sea más claro matemáticamente pensar en el círculo como la recta real completa $x$ con la identificación

$$x \sim x + L \qquad \text{(3.1)}$$

lo que significa que dos puntos cuyas coordenadas están relacionadas de esta manera deben considerarse el mismo punto. De ello se sigue que tenemos la condición de periodicidad

$$\psi(x + L) = \psi(x) \qquad \text{(3.2)}$$

De esto se sigue que no solo $\psi$ es periódica, sino que todas sus derivadas también lo son.

Se supone que la partícula es libre y por lo tanto $V(x) = 0$. La ecuación de Schrödinger independiente del tiempo es entonces

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\, \psi(x) \qquad \text{(3.3)}$$

Antes de resolverla, mostremos que toda solución debe tener $E \geq 0$. Para ello multiplicamos la ecuación anterior por $\psi^*(x)$ e integramos sobre el círculo $x \in [0, L)$. Dado que $\psi$ está normalizada, obtenemos

$$-\frac{\hbar^2}{2m} \int_0^L \psi^*(x)\, \frac{d^2\psi}{dx^2}\, dx = E \int \psi^*(x)\psi(x)\, dx = E \qquad \text{(3.4)}$$

El integrando del lado izquierdo puede reescribirse como

$$-\frac{\hbar^2}{2m} \int_0^L \left[ \frac{d}{dx}\left(\psi^* \frac{d\psi}{dx}\right) - \frac{d\psi^*}{dx}\frac{d\psi}{dx} \right] dx = E \qquad \text{(3.5)}$$

y la derivada total se puede integrar

$$-\frac{\hbar^2}{2m} \left[ \left. \psi^* \frac{d\psi}{dx} \right|_{x=L} - \left. \psi^* \frac{d\psi}{dx} \right|_{x=0} \right] + \frac{\hbar^2}{2m} \int_0^L \left| \frac{d\psi}{dx} \right|^2 dx = E \qquad \text{(3.6)}$$

Dado que $\psi(x)$ y sus derivadas son periódicas, las contribuciones de $x = L$ y $x = 0$ se cancelan y quedamos con

$$E = \frac{\hbar^2}{2m} \int_0^L \left| \frac{d\psi}{dx} \right|^2 dx \geq 0 \qquad \text{(3.7)}$$

lo que establece nuestra afirmación. También vemos que $E = 0$ requiere que $\psi$ sea constante (¡y no nula!).

Habiendo mostrado que todas las soluciones deben tener $E \geq 0$, volvamos a la ecuación de Schrödinger, que puede reescribirse como

$$\frac{d^2\psi}{dx^2} = -\frac{2mE}{\hbar^2}\, \psi \qquad \text{(3.8)}$$

Podemos entonces definir $k$ mediante

$$k^2 \equiv \frac{2mE}{\hbar^2} \geq 0 \qquad \text{(3.9)}$$

Dado que $E \geq 0$, la constante $k$ es real. Nótese que esta definición es muy natural, ya que hace que

$$E = \frac{\hbar^2 k^2}{2m} \qquad \text{(3.10)}$$

lo cual significa que, como es habitual, $p = \hbar k$. Usando $k^2$, la ecuación diferencial se convierte en la familiar

$$\frac{d^2\psi}{dx^2} = -k^2\psi \qquad \text{(3.11)}$$

Podríamos escribir la solución general en términos de senos y cosenos de $kx$, pero usemos exponenciales complejas:

$$\psi(x) \sim e^{ikx} \qquad \text{(3.12)}$$

Esto resuelve la ecuación diferencial y, además, es un autoestado de momento. La condición de periodicidad (3.2) requiere

$$e^{ik(x+L)} = e^{ikx} \ \Rightarrow\ e^{ikL} = 1 \ \Rightarrow\ kL = 2\pi n\,, \ n \in \mathbb{Z} \qquad \text{(3.13)}$$

Vemos que el momento está cuantizado porque el número de onda está cuantizado. El número de onda tiene los valores discretos posibles

$$k_n \equiv \frac{2\pi n}{L}\,, \quad n \in \mathbb{Z} \qquad \text{(3.14)}$$

Todos los enteros, positivos y negativos, están permitidos y de hecho son necesarios porque todos corresponden a valores distintos del momento $p_n = \hbar k_n$. Las soluciones de la ecuación de Schrödinger pueden entonces indexarse mediante el entero $n$:

$$\psi_n(x) = N e^{ik_n x} \qquad \text{(3.15)}$$

donde $N$ es una constante de normalización real. Su valor se determina a partir de

$$1 = \int_0^L \psi_n^*(x)\psi_n(x)\, dx = \int_0^L N^2\, dx = N^2 L \ \Rightarrow\ N = \frac{1}{\sqrt{L}} \qquad \text{(3.16)}$$

así que tenemos

$$\psi_n(x) = \frac{1}{\sqrt{L}}\, e^{ik_n x} = \frac{1}{\sqrt{L}}\, e^{\frac{2\pi i n x}{L}} \qquad \text{(3.17)}$$

Las energías asociadas son

$$E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{\hbar^2\, 4\pi^2 n^2}{2mL^2} = \frac{2\pi^2 \hbar^2 n^2}{mL^2} \qquad \text{(3.18)}$$

Hay infinitos autoestados de energía. Tenemos estados degenerados porque $E_n$ es simplemente una función de $|n|$ y por lo tanto es la misma para $n$ y $-n$. En efecto, $\psi_n$ y $\psi_{-n}$ tienen ambos energía $E_n$. El único autoestado no degenerado es $\psi_0 = \dfrac{1}{\sqrt{L}}$, que es una función de onda constante con energía cero.

Cada vez que encontramos autoestados de energía degenerados debemos preguntarnos qué hace diferentes a esos estados, dado que tienen la misma energía. Para responder a esto hay que encontrar un observable que tome valores distintos en los estados. Afortunadamente, en nuestro caso conocemos la respuesta. Nuestros estados degenerados pueden distinguirse por su momento: $\psi_n$ tiene momento $\dfrac{2\pi n \hbar}{L}$ y $\psi_{-n}$ tiene momento $\left(-\dfrac{2\pi n \hbar}{L}\right)$.

Dados dos autoestados de energía degenerados, cualquier combinación lineal de estos estados es un autoestado con la misma energía. En efecto, si

$$\hat{H}\psi_1 = E\psi_1\,, \qquad \hat{H}\psi_2 = E\psi_2 \qquad \text{(3.19)}$$

entonces

$$\hat{H}(a\psi_1 + b\psi_2) = a\hat{H}\psi_1 + b\hat{H}\psi_2 = aE\psi_1 + bE\psi_2 = E(a\psi_1 + b\psi_2) \qquad \text{(3.20)}$$

Por lo tanto podemos formar dos combinaciones lineales de los autoestados degenerados $\psi_n$ y $\psi_{-n}$ para obtener otra descripción de los autoestados de energía:

$$\psi_n + \psi_{-n} \sim \cos(k_n x)\,,$$

$$\psi_n - \psi_{-n} \sim \sin(k_n x)\,. \qquad \text{(3.21)}$$

Aunque estos son autoestados de energía reales, no son autoestados de momento. Solo nuestras exponenciales son autoestados simultáneos tanto de $\hat{H}$ como de $\hat{p}$.

Los autoestados de energía $\psi_n$ son automáticamente ortonormales, ya que son autoestados de $\hat{p}$ sin degeneraciones (y, como recordarán, los autoestados de un operador hermítico con autovalores distintos son automáticamente ortogonales):

$$\int_0^L \psi_n^*(x)\psi_m(x)\, dx = \frac{1}{L} \int_0^L e^{\frac{2\pi i (m-n) x}{L}}\, dx = \delta_{mn} \qquad \text{(3.22)}$$

También son completos: podemos entonces construir una función de onda general como una superposición que es de hecho una serie de Fourier. Para cualquier $\Psi(x,0)$ que satisfaga la condición de periodicidad, podemos escribir

$$\Psi(x, 0) = \sum_{n \in \mathbb{Z}} a_n \psi_n(x) \qquad \text{(3.23)}$$

donde, como debe comprobarse, los coeficientes $a_n$ se determinan mediante las integrales

$$a_n = \int_0^L dx\, \psi_n^*(x)\, \Psi(x, 0) \qquad \text{(3.24)}$$

El estado inicial $\Psi(x, 0)$ se evoluciona entonces fácilmente en el tiempo:

$$\Psi(x, t) = \sum_{n \in \mathbb{Z}} a_n \psi_n(x)\, e^{-\frac{iE_n t}{\hbar}} \qquad \text{(3.25)}$$

[1]

------------------------------------------------------------------------

MIT OpenCourseWare

https://ocw.mit.edu

8.04 Física Cuántica I

Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

[1] Andrew Turner transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.


---

<!-- MIT8.04_LecNotes11_ES.md -->

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


---

<!-- MIT8.04_LecNotes12_ES.md -->

# Clase 12

## Vídeos de esta clase (YouTube)

**Lección 12: Properties of 1D energy eigenstates. Qualitative properties of wavefunctions. Shooting method.**

- [Nondegeneracy of bound states in 1D. Real solutions](https://www.youtube.com/watch?v=EdXaUfRynx8)
- [Potentials that satisfy V(-x) = V(x)](https://www.youtube.com/watch?v=AtjMKPzNIXQ)
- [Qualitative insights: Local de Broglie wavelength](https://www.youtube.com/watch?v=QMeKIiufg5s)
- [Correspondence principle: amplitude as a function of position](https://www.youtube.com/watch?v=79GY-hI_emE)
- [Local picture of the wavefunction](https://www.youtube.com/watch?v=fWCGM2auQPs)
- [Energy eigenstates on a generic symmetric potential. Shooting method](https://www.youtube.com/watch?v=45M-BtYAcwg)

------------------------------------------------------------------------

*B. Zwiebach* *20 de marzo de 2016*

## Contenido

1.  Propiedades generales
2.  Estados ligados en potenciales que varían lentamente
3.  Esbozo del comportamiento de la función de onda en distintas regiones
4.  Método de disparo

## 1. Propiedades generales

Demostrarás los siguientes hechos en tu tarea:

1.  Dada la ecuación de Schrödinger con potencial $V(x)$

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + (V(x) - E)\psi = 0 \qquad \text{(1.1)}$$

no existen estados propios de energía con $E < \min_x V(x)$. En otras palabras, la situación indicada en la Figura 1 no puede ocurrir.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig1.png)

Figura 1: No existen soluciones con energía $E$ menor que el mínimo del potencial $V(x)$.

1.  Para un potencial unidimensional definido sobre $-\infty \le x \le \infty$, no existen estados ligados degenerados. Recordemos que un estado ligado es un estado propio de energía normalizable. Dado esto, $\lim_{x\to\infty}\psi = 0$.

Mostraremos ahora que el hecho de que $V(x)$ sea real nos permite trabajar con funciones de onda $\psi(x)$ reales. Aunque existen soluciones complejas, podemos elegir soluciones reales sin pérdida de generalidad.

**Teorema 1.** Los estados propios de energía $\psi(x)$ pueden elegirse reales.

**Demostración.** Consideremos nuestra ecuación principal para la función de onda compleja $\psi(x)$:

$$\psi'' + \frac{2m}{\hbar^2}(E - V(x))\psi = 0 . \qquad \text{(1.2)}$$

Dado que $(\psi'')^* = (\psi^*)''$ y $V(x)$ es real, la conjugación compleja de la ecuación anterior da

$$(\psi^*)'' + \frac{2m}{\hbar^2}(E - V(x))\psi^* = 0 . \qquad \text{(1.3)}$$

Vemos que $\psi^*(x)$ es otra solución de la ecuación de Schrödinger con la misma energía. La solución $\psi^*(x)$ es distinta de $\psi(x)$ si no existe una constante $c$ tal que $\psi^* = c\psi$. En ese caso $\psi^*$ y $\psi$ representan dos soluciones degeneradas y, por superposición, podemos obtener dos soluciones reales degeneradas:

$$\psi_r \equiv \frac{1}{2}(\psi + \psi^*) , \qquad \psi_{im} \equiv \frac{1}{2i}(\psi - \psi^*) . \qquad \text{(1.4)}$$

Estas son, por supuesto, las partes real e imaginaria de $\psi$. Si $\psi^* = c\psi$, las partes real e imaginaria producen la misma solución real. En cualquier caso podemos trabajar con una solución real. $\blacksquare$

Si nos ocupamos de estados ligados de potenciales unidimensionales, se puede afirmar algo más fuerte: no es que podamos elegir trabajar con soluciones reales, sino que cualquier solución es, de entrada, esencialmente real.

**Corolario 1.** Cualquier estado ligado $\psi(x)$ de un potencial unidimensional es real, salvo una fase constante global.

**Demostración.** Recordemos que en potenciales unidimensionales no existen estados ligados degenerados. Esto significa que las dos soluciones reales $\psi_r$ y $\psi_{im}$ consideradas arriba deben ser iguales salvo una constante, que solo puede ser real:

$$\psi_{im}(x) = c\,\psi_r(x) , \quad \text{con } c \in \mathbb{R} . \qquad \text{(1.5)}$$

De aquí se sigue que $\psi = \psi_r + i\psi_{im} = (1+ic)\psi_r$. Escribiendo $1+ic = \sqrt{1+c^2}\, e^{i\beta}$ con $\beta$ real, se muestra que $\psi$ es, salvo una fase constante $\beta$, igual a una solución real. $\blacksquare$

Nuestro siguiente resultado muestra que, para un potencial que es una función simétrica de $x$, podemos trabajar con estados propios de energía que sean funciones simétricas o antisimétricas de $x$.

**Teorema 2.** Si $V(-x) = V(x)$, los estados propios de energía pueden elegirse pares o impares bajo $x \to -x$.

**Demostración.** Nuevamente, partimos de nuestra ecuación principal

$$\psi'' + \frac{2m}{\hbar^2}(E - V(x))\psi = 0 . \qquad \text{(1.6)}$$

Recordemos que las primas denotan aquí derivada respecto del argumento, de modo que $\psi''(x)$ significa la función “segunda-derivada-de-$\psi$” evaluada en $x$. De igual manera $\psi''(-x)$ significa la función “segunda-derivada-de-$\psi$” evaluada en $-x$. Así podemos cambiar $x$ por $-x$ sin problema en la ecuación anterior, obteniendo

$$\psi''(-x) + \frac{2m}{\hbar^2}(E - V(x))\psi(-x) = 0 , \qquad \text{(1.7)}$$

donde usamos que $V$ es par. Ahora queremos dejar claro que la ecuación anterior implica que $\psi(-x)$ es otra solución de la ecuación de Schrödinger con la misma energía. Para esto definamos una función $\varphi(x)$ y tomemos dos derivadas de ella:

$$\varphi(x) \equiv \psi(-x) \;\;\to\;\; \frac{d}{dx}\varphi(x) = \psi'(-x)\cdot(-1) , \quad \frac{d^2}{dx^2}\varphi(x) = \psi''(-x) . \qquad \text{(1.8)}$$

Usando esto, la ecuación (1.7) se convierte en

$$\frac{d^2}{dx^2}\varphi(x) + \frac{2m}{\hbar^2}(E - V(x))\varphi(x) = 0 . \qquad \text{(1.9)}$$

lo que muestra que $\varphi(x) = \psi(-x)$ es una solución degenerada de la ecuación de Schrödinger. Con las soluciones degeneradas $\psi(x)$ y $\psi(-x)$ podemos ahora formar combinaciones simétrica (s) y antisimétrica (a) que son, respectivamente, pares e impares bajo $x \to -x$:

$$\psi_s(x) \equiv \frac{1}{2}\big(\psi(x) + \psi(-x)\big) , \qquad \psi_a(x) \equiv \frac{1}{2}\big(\psi(x) - \psi(-x)\big) . \qquad \text{(1.10)}$$

Estas son las soluciones que se afirmaba que existían. $\blacksquare$

Notemos que la demostración anterior no funcionaría para el caso de potenciales impares $V(-x) = -V(x)$. ¡No podemos decir mucho en ese caso!

Nuevamente, si nos centramos en estados ligados de potenciales pares unidimensionales, la ausencia de degeneración tiene una implicación más fuerte: las soluciones son automáticamente pares o impares.

**Corolario 2.** Cualquier estado ligado de un potencial par unidimensional es par o impar.

**Demostración.** La ausencia de degeneración implica que las soluciones $\psi(x)$ y $\psi(-x)$ deben ser la misma solución. Por el corolario 1, podemos elegir $\psi(x)$ real y así debemos tener

$$\psi(-x) = c\,\psi(x) , \quad \text{con } c \in \mathbb{R} . \qquad \text{(1.11)}$$

Haciendo $x \to -x$ en la ecuación anterior obtenemos $\psi(x) = c\,\psi(-x) = c^2\,\psi(x)$, de donde aprendemos que $c^2 = 1$. Las únicas posibilidades son $c = \pm 1$. Así, $\psi(x)$ es automáticamente par o impar bajo $x \to -x$. $\blacksquare$

Usamos el resultado de este teorema para hallar los estados ligados del pozo cuadrado finito. Puesto que ese potencial es par, pudimos restringir nuestro trabajo a la búsqueda de estados ligados pares y estados ligados impares. ¡El potencial no puede tener estados ligados que no sean ni pares ni impares!

## 2. Estados ligados en potenciales que varían lentamente

Consideraremos ahora algunas ideas que la física clásica nos aporta sobre el comportamiento de los estados propios de energía. Esto se denomina a veces la **aproximación semiclásica**, porque la física clásica a veces puede dar una descripción aproximada de la física cuántica.

Comenzamos con un ejemplo que ya entendemos. Consideramos la energía total $E$ de una partícula, que es la suma de una energía potencial $V$ y una energía cinética $K$. Cuando $V$ es función de la posición, $K$ también debe ser función de la posición para que la suma $E$ se conserve, como debe ocurrir. En nuestro primer ejemplo, mostrado en la Figura 2, el potencial $V$ es constante y la energía $E$ es mayor que $V$. Una partícula en tal potencial tendrá una energía cinética $K$ constante y por tanto un momento constante $p = \sqrt{2mK}$. Es un hecho que la onda que representa a la partícula cuántica tiene una longitud de onda de de Broglie $\lambda$ igual a la constante de Planck $h$ dividida entre el momento clásico.

En efecto, a partir de la ecuación de Schrödinger

$$\psi'' = -\frac{2m}{\hbar^2}(E-V)\psi = -\frac{2mK}{\hbar^2}\psi = -\frac{p^2}{\hbar^2}\psi , \qquad \text{(2.1)}$$

que lleva a soluciones reales de la forma

$$\psi \sim \cos\left(\frac{p}{\hbar}x\right) = \cos\left(\frac{2\pi}{h/p}x\right) , \qquad \text{(2.2)}$$

donde vemos que la longitud de onda de $\psi$ es la longitud de onda de de Broglie de una partícula con momento $p$. Esta función de onda es real y por tanto no es un estado propio de momento. Representa una superposición de un estado con momento $p$ y un estado de momento $-p$. Incluso en el caso clásico, la energía cinética $K$ solo determina $p^2$ y no el signo de $p$. Nuestro interés aquí está en funciones de onda reales $\psi(x)$, apropiadas para estados propios de energía, y lo que hemos visto es que, para un potencial constante, la longitud de onda de $\psi(x)$ es la longitud de onda de de Broglie asociada al momento clásico.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig2.png)

Figura 2: A la izquierda, un ejemplo de potencial constante, $V = V_0 < E$, donde $K$ es la energía cinética y $E = K + V_0$ es la energía total. A la derecha, un esbozo de la función de onda para una partícula en este potencial. $V$ constante $\Rightarrow$ $K$ constante, por tanto el momento también es constante.

Consideremos ahora la situación mostrada en la Figura 3, donde imaginamos una partícula clásica moviéndose en un potencial $V(x)$ linealmente creciente. Esta vez la energía cinética $K(x)$ también depende de la posición. Como resultado, el momento de la partícula clásica $p(x) = \sqrt{2mK(x)}$ también depende de la posición. La idea ahora es que, si el potencial varía lentamente, en buena aproximación la función de onda tendrá una longitud de onda de de Broglie dependiente de la posición $\lambda(x)$ dada por

$$\lambda(x) = \frac{h}{p(x)} . \qquad \text{(2.3)}$$

Con esto queremos decir que $\psi$ es alguna combinación de funciones

$$\cos\left(\frac{2\pi x}{\lambda(x)}\right), \quad \sin\left(\frac{2\pi x}{\lambda(x)}\right) . \qquad \text{(2.4)}$$

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig3.png)

Figura 3: Un potencial que varía linealmente, $V(x) = \alpha x$. La energía $E = K + V(x)$ es fija, y al aumentar $x$, $K(x)$ disminuye, $p(x)$ disminuye y $\lambda(x)$ aumenta, resultando en una función de onda de longitud de onda creciente.

Como vemos en la Figura 3, debido al crecimiento lineal de $V(x)$, una partícula con energía total $E$ tendrá una energía cinética $K(x)$ decreciente al aumentar $x$. Así, el momento clásico disminuirá, y anticipamos que la función de onda tendrá una longitud de onda de de Broglie local $\lambda(x)$ creciente al aumentar $x$. Esto se ilustra a la derecha de la figura. Discutiremos más adelante qué esperamos que ocurra con la amplitud de la función de onda.

La aproximación semiclásica —igualar la longitud de onda de $\psi(x)$ a la longitud de onda de de Broglie de la partícula clásica— es precisa cuando el potencial cambia lentamente. Por “lentamente” queremos decir que el cambio en el potencial a lo largo de una distancia comparable a la longitud de onda de de Broglie local es muy pequeño comparado con el propio potencial:

$$\lambda(x)\left|\frac{dV}{dx}\right| \ll |V(x)| . \qquad \text{(2.5)}$$

El lado izquierdo de la desigualdad es una estimación del cambio de $V$ a lo largo de una distancia $\lambda(x)$, y por tanto esta cantidad debe ser muy pequeña comparada con el potencial para que la aproximación semiclásica sea válida. Esta desigualdad es la condición clave para la aproximación semiclásica. De hecho, es la condición que permite establecer el análisis WKB de la ecuación de Schrödinger (¡asunto de 8.06!).

En la Figura 4 mostramos un potencial arbitrario $V(x)$ y consideramos el movimiento clásico de una partícula de energía total $E$. Para cualquier punto $x_0$, tenemos $V(x_0) + K(x_0) = E$. La energía cinética máxima ocurre en el valor mínimo del potencial. Clásicamente una partícula no puede tener energía cinética negativa, por lo que la partícula no puede encontrarse en puntos donde $V(x)$ es mayor que la energía $E$. En la figura, esto ocurre para $x > x_R$ y para $x < x_L$, y estas regiones se llaman **regiones clásicamente prohibidas**. Una partícula de energía $E$ oscilará de $x_L$ a $x_R$ y de vuelta. Al moverse, su velocidad cambia, siendo una función $v(x)$ de la posición. Los puntos $x_L$ y $x_R$ se llaman **puntos de retorno**, porque en ellos el movimiento de la partícula se invierte.

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig4.png)

Figura 4: Un potencial arbitrario que muestra los puntos de retorno $x_L$ y $x_R$. La región a la derecha de $x_R$ y la región a la izquierda de $x_L$ son regiones clásicamente prohibidas. En cualquier punto $x \in [x_L, x_R]$ la suma de la energía potencial $V(x)$ y la energía cinética $K(x)$ es igual a la energía total $E$.

La partícula clásica que oscila pasa más tiempo en las regiones donde su velocidad es pequeña y menos tiempo en las regiones donde su velocidad es grande. Esto tiene implicaciones cuánticas. En efecto, en la aproximación semiclásica encontramos que la amplitud de la función de onda es mayor en los lugares donde la partícula pasa más tiempo y menor en los lugares donde pasa menos tiempo. Esto puede cuantificarse. Consideremos la probabilidad $|\psi(x)|^2 dx$ de encontrar la partícula dentro de la región infinitesimal $dx$ alrededor de $x$. Esto se establece proporcional a la fracción de tiempo que la partícula pasa en $dx$:

$$|\psi(x)|^2 dx \simeq \frac{dt}{T} , \qquad \text{(2.6)}$$

donde $dt$ es el tiempo requerido para recorrer $dx$ y $T$ es el semiperiodo de oscilación, el tiempo para ir del punto de retorno izquierdo al punto de retorno derecho. Con $v(x)$ la velocidad local de la partícula, tenemos

$$|\psi(x)|^2 dx \simeq \frac{dx}{v(x)T} = \frac{m}{T}\frac{1}{p(x)}dx \;\;\to\;\; |\psi(x)|^2 \sim \frac{1}{p(x)} . \qquad \text{(2.7)}$$

Esta relación debe interpretarse con cuidado. Recordemos que $\psi(x)$ tiene longitud de onda muy pequeña para $p(x)$ grande. Así $|\psi(x)|^2$ oscila entre cero y algún valor máximo en distancias muy cortas a lo largo de $x$. Por otro lado, el momento $p(x)$ que aparece en el lado derecho no presenta tales oscilaciones. Por tanto, con $|\psi(x)|^2$ en la relación anterior en realidad queremos decir el promedio de $|\psi(x)|^2$ sobre unas pocas oscilaciones cerca de $x$, en otras palabras, el cuadrado de la amplitud de la onda $\psi(x)$. Escribiendo la amplitud (un número real positivo, por supuesto) como $\mathrm{Amp}(\psi(x))$, tenemos

$$\mathrm{Amp}(\psi(x)) \sim \frac{1}{\sqrt{p(x)}} \sim \sqrt{\lambda(x)} . \qquad \text{(2.8)}$$

La amplitud de la onda es proporcional a la raíz cuadrada de la longitud de onda de de Broglie. Así, en la Figura 5, el momento de la partícula disminuye y $\lambda(x)$ aumenta al aumentar $x$. Por tanto esperamos que la amplitud de la onda aumente, como se esboza a la derecha.

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig5.png)

Figura 5: Un potencial $V(x)$ y una energía cinética que disminuye al aumentar $x$. Entonces la longitud de onda de de Broglie aumenta con $x$. La ecuación 2.8 implica entonces que la amplitud de $\psi(x)$ también aumenta con $x$.

Como ilustración sencilla de la importancia de promediar $|\psi|^2$, consideremos un estado de energía grande en el potencial de pozo infinito, como se muestra en la Fig. 6. Dentro de la caja, la partícula clásica “rebota” entre las paredes con velocidad constante. Como resultado, la partícula pasa la misma cantidad de tiempo en cada intervalo $dx$ de igual tamaño dentro de la caja. La distribución de probabilidad clásica $P_{cl}$ dentro de la caja es uniforme:

$$P_{cl}(x)dx = \frac{1}{a}dx \;\;\to\;\; P_{cl}(x) = \frac{1}{a} , \qquad \text{(2.9)}$$

ya que la integral sobre la caja $x \in [0,a]$ de $P_{cl}(x)dx$ da uno. Consideremos ahora un estado propio de energía $\psi_n(x)$ con $n$ grande:

$$\psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi x}{a}\right) \;\;\to\;\; |\psi_n(x)|^2 = \frac{2}{a}\sin^2\left(\frac{n\pi x}{a}\right) . \qquad \text{(2.10)}$$

La densidad de probabilidad mecánico-cuántica asociada $P_{qm}$ es

$$P_{qm}(x) = |\psi_n(x)|^2 = \frac{2}{a}\sin^2\left(\frac{n\pi x}{a}\right) , \qquad \text{(2.11)}$$

y es, para $n$ grande, una función que oscila rápidamente, aparentemente muy distinta de la probabilidad clásica $P_{cl} = 1/a$. Mientras que la probabilidad clásica nunca se anula, ¡la probabilidad cuántica tiene muchos ceros! Aun así, sobre distancias arbitrarias mayores que $a/n$ (que se presume pequeña ya que $n$ es muy grande), el promedio de la densidad de probabilidad cuántica se aproxima a la densidad de probabilidad clásica. Recordemos que el promedio de $\sin^2$ sobre cualquier número entero de oscilaciones es $1/2$, de modo que su promedio sobre cualquier intervalo que incluya un número grande de oscilaciones (no necesariamente entero) es aproximadamente igual a $1/2$. Tenemos entonces

$$\mathrm{Promedio}_x(P_{qm}(x)) \simeq \frac{2}{a}\cdot\frac{1}{2} = \frac{1}{a} = P_{cl}(x) . \qquad \text{(2.12)}$$

![Figura 6](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig6.png)

Figura 6: Partícula en una caja unidimensional. La partícula rebota con velocidad constante.

La aproximación semiclásica es una realización explícita de lo que se llama libremente el “principio de correspondencia”, la idea de que existen límites de los estados cuánticos en los que sus propiedades pueden entenderse mediante un análisis clásico del sistema.

## 3. Esbozo del comportamiento de la función de onda en distintas regiones

Examinemos el comportamiento de un estado propio de energía para el caso de un potencial general $V(x)$. Reescribimos la ecuación de Schrödinger independiente del tiempo dividiendo por $\psi$ para obtener:

$$\frac{\psi''(x)}{\psi(x)} = -\frac{2m}{\hbar^2}(E - V(x)) , \qquad \text{(3.1)}$$

lo cual es conveniente porque no aparece la función de onda en el lado derecho. Consideraremos la ecuación en dos regiones y en algunos puntos especiales.

- $E - V(x) < 0$, **región clásicamente prohibida**, porque la energía total es menor que el potencial. En este caso el lado derecho de la ec. (3.1) es positivo. Esto significa que hay dos posibilidades: tanto $\psi$ como $\psi''$ son positivas, o tanto $\psi$ como $\psi''$ son negativas. Estas posibilidades se muestran aquí:

![Figura 7](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig7.png)

Figura 7: En la región clásicamente prohibida, o bien $\psi > 0$, $\psi'' > 0$, o bien $\psi < 0$, $\psi'' < 0$. En ambos casos la función de onda es convexa hacia el eje $x$.

Estos posibles comportamientos se resumen diciendo que la función de onda es **convexa hacia el eje**. Cuando las regiones clásicamente prohibidas se extienden hasta $x = -\infty$ o $x = \infty$, el comportamiento es del tipo mostrado a continuación:

![Figura 8](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig8.png)

Figura 8: Funciones de onda que se acercan a $x = -\infty$ o $x = \infty$ dentro de regiones clásicamente prohibidas.

- $E - V > 0$, **región clásicamente permitida**: el lado derecho de la ec. 3.1 es negativo. Así, o bien $\psi > 0$, $\psi'' < 0$, o bien $\psi < 0$, $\psi'' > 0$. Ambas opciones se muestran a continuación y se resumen diciendo que la función de onda es **cóncava hacia el eje**:

![Figura 9](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig9.png)

Figura 9: $\psi > 0$, $\psi'' < 0$, o $\psi < 0$, $\psi'' > 0$. La función de onda es cóncava hacia el eje $x$.

Una región clásicamente permitida que sea grande tendría las partes superior e inferior de la figura anterior alternándose para formar una función que se asemeja a un seno o un coseno.

- $V(x_0) = E$. **Punto de retorno**: definido como un punto $x_0$ en el cual la energía potencial $V(x_0)$ es igual a la energía total $E$. Los puntos de retorno separan regiones clásicamente permitidas de regiones clásicamente prohibidas. Un punto de retorno es un punto de inflexión en la gráfica de $\psi(x)$, un punto donde la segunda derivada se anula, ya que

$$\psi''(x_0) = -\frac{2m}{\hbar^2}\cdot 0 \cdot \psi(x_0) = 0 , \qquad \text{(3.2)}$$

No todos los puntos de inflexión son puntos de retorno. De hecho, los nodos de la función de onda son puntos de inflexión. Esto es claro a partir de $\psi'' = -\frac{2m}{\hbar^2}(E - V(x))\psi$, ya que si $\psi$ se anula, $\psi''$ también se anula.

Notemos, sin embargo, que no está permitido que $\psi$ y $\psi'$ se anulen simultáneamente en ningún punto del dominio de la función de onda. Esto se debe a que la ecuación de Schrödinger es una ecuación diferencial lineal de segundo orden. Se puede mostrar rápidamente que si $\psi = \psi' = 0$ en algún punto $x_0$, entonces todas las derivadas superiores de $\psi$ se anulan en ese punto. Suponiendo que la función de onda tiene un desarrollo de Taylor, concluimos que la función de onda debe anularse idénticamente.

![Figura 10](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig10.png)

Figura 10: Es imposible que tanto $\psi$ como $\psi'$ se anulen en algún punto $x_0$: la ecuación de Schrödinger obligaría entonces a que $\psi(x)$ se anule idénticamente.

Concluimos esta sección ilustrando la cuantización de los niveles de energía para los estados ligados de un potencial par. Como se muestra en la Figura 11, arriba, tenemos un potencial par y hemos marcado cuatro energías $E_1 < E_2 < E_3 < E_4$. No todas corresponden a estados propios de energía. Imaginamos integrar la ecuación de Schrödinger desde $x = \infty$ hacia $x = 0$. Como se muestra en la pequeña figura ligeramente a la derecha y abajo del potencial, suponemos $\psi > 0$ cuando $x \to \infty$. Dado que cualquier estado ligado es automáticamente par o impar, la imagen en $x \to -\infty$ debe ser o bien la de $\psi > 0$ (la extensión par) o bien la de $\psi < 0$ (la extensión impar).

![Figura 11](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig11.png)

Figura 11: Un potencial par (figura superior) y el resultado de integrar la ecuación desde $x = \infty$ hacia cero para varios valores de la energía. Obtenemos una solución cuando $\psi(x)$ para $x \ge 0$ puede empalmarse con $\psi$ y $\psi'$ continuas a una extensión par o impar válida para $x < 0$. No hay solución para $E_1$ y $E_3$. El estado fundamental surge para $E_2$ y el primer estado excitado surge para $E_4$.

Para tener una solución, la imagen desde la derecha debe empalmar correctamente en $x = 0$ con una de las dos posibles extensiones para $x < 0$.

Consideremos, por ejemplo, la integración de la ecuación para $E = E_1$. Llegando desde $x = \infty$, la solución tiene un punto de inflexión y se vuelve cóncava hacia el eje. Más allá de este punto, la primera derivada $\psi'$ disminuye. Aun así, como se muestra en la imagen, $\psi'$ no se anula en $x = 0$, de modo que la extensión par para $x < 0$ no empalma correctamente con la solución de $x > 0$ en $x = 0$, porque $\psi'$ no es continua. Empalmar con la extensión impar no es una posibilidad porque entonces $\psi$ no sería continua en $x = 0$. Así, $E_1$ no es una energía permitida.

Al aumentar la energía a $E = E_2$, el punto de retorno ocurre en un $x$ mayor y $\psi'$ logra llegar exactamente a cero en $x = 0$, empalmando $\psi$ y $\psi'$ con la extensión par. Esta vez tenemos una solución. Por supuesto, esto ocurre precisamente para $E = E_2$; un poco más o un poco menos de energía y la derivada no es continua en $x = 0$.

Al aumentar la energía a $E_3$, el punto de retorno se mueve a un $x$ aún mayor y $\psi'$ es negativa en el momento en que llegamos a $x = 0$, mientras que $\psi$ sigue siendo positiva. La solución no puede empalmarse con la extensión par debido a la discontinuidad de la derivada.

Si ahora aumentamos aún más la energía hasta cierto valor $E_4$, en el momento en que llegamos a $x = 0$ la derivada $\psi'$ será negativa y $\psi$ será exactamente cero. Como se puede ver en la figura, obtenemos un buen empalme con la extensión impar para $x < 0$. Este es el primer estado excitado. Es una función de onda impar con un único nodo en $x = 0$.

## 4. Método de disparo

El **método de disparo** es un método numérico para hallar la forma de la solución de estado ligado de la ecuación de Schrödinger

$$\frac{d^2\psi}{dx^2} + \frac{2m}{\hbar^2}(E - V(x))\psi = 0 . \qquad \text{(4.1)}$$

El método se implementa fácilmente para potenciales pares $V(x)$, en cuyo caso podemos buscar estados ligados pares y estados ligados impares.

Consideremos primero los estados ligados pares. Intentaremos integrar la ecuación diferencial desde $x = 0$ hasta $x = \infty$. Para comenzar en $x = 0$ necesitamos fijar $\psi$ y $\psi'$ en este punto. Dado que la normalización del estado ligado no está determinada por la ecuación, podemos elegir

$$\psi(x=0) = 1 . \qquad \text{(4.2)}$$

La derivada también debe ser cero en este punto: si la derivada no es cero, la función de onda par tendrá una derivada discontinua en $x = 0$ (¿puedes ver por qué?). Por tanto debemos fijar

$$\psi'(x=0) = 0 . \qquad \text{(4.3)}$$

Para integrar la ecuación diferencial ahora necesitamos elegir alguna energía. Elijamos algún valor arbitrario $E_0$. Ya sabemos que valores arbitrarios de la energía no producen estados ligados. Entonces, ¿qué sale mal si ahora integramos la ecuación diferencial? Lo que ocurre típicamente es que se obtiene una solución que no puede normalizarse. Al trabajar con el ordenador se observa que más allá de cierto punto a lo largo de $x$ la solución diverge, quizás con $\psi \to \infty$, es decir, $\psi$ tendiendo hacia arriba.

Debes entonces cambiar el valor de la energía hasta encontrar algún valor $E_1$ para el cual la solución también diverge, pero esta vez con $\psi \to -\infty$, o $\psi$ tendiendo hacia abajo. Esta es una señal de que existe alguna energía en el intervalo entre $E_0$ y $E_1$ para la cual existe una solución normalizable. Entonces intentas reducir el intervalo. Si $E_0 < E_1$ puedes hacerlo hallando valores mayores que $E_0$ para los cuales la divergencia sigue siendo hacia arriba, y valores menores que $E_1$ para los cuales la divergencia sigue siendo hacia abajo. A medida que reduces el intervalo seguirás encontrando estas divergencias, pero ocurrirán para valores de $x$ cada vez mayores. Al hacer esto, obtienes una aproximación cada vez mejor a la energía del estado ligado (ver Fig. 12).

Para las soluciones impares, el procedimiento es el mismo, pero las condiciones de frontera en $x = 0$ son:

$$\psi(x=0) = 0 , \qquad \psi'(x=0) = 1 . \qquad \text{(4.4)}$$

La primera es necesaria para una función impar continua. La segunda es arbitraria, salvo por la normalización.

Si un potencial no es par pero tiene una pared dura, esto proporciona un buen punto de partida para la integración de la ecuación de Schrödinger. En ese punto la función de onda se fija en cero y la derivada se fija en uno. Si el potencial tiene dos paredes duras, podemos integrar comenzando desde una pared y luego exigir que la solución llegue exactamente a cero al llegar a la segunda pared.

Una nota práctica: al trabajar con ordenadores para llevar a cabo estas integraciones numéricas, primero es necesario “eliminar” las unidades de la ecuación diferencial. El primer paso en este proceso es reemplazar $x$ por una variable adimensional $u$. La relación entre ellas es de la forma $x = bu$, donde $b$ es una cantidad con unidades de longitud construida a partir de los parámetros del problema.

![Figura 12](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig12.png)

Figura 12: La integración numérica de la ecuación de Schrödinger conduce a soluciones que divergen hacia arriba ($\psi \to \infty$) o hacia abajo ($\psi \to -\infty$) más allá de cierto valor de $x$. Los estados ligados se encuentran para los valores de energía en los cuales la divergencia cambia de hacia arriba a hacia abajo, o de hacia abajo a hacia arriba.

*Sarah Geller transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare https://ocw.mit.edu

8.04 Física Cuántica I Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

# Apéndice: Lista de problemas 5 (Problem Set 5, 2016)

*Física Cuántica I (8.04), Primavera de 2016* *Departamento de Física del MIT — Fecha de entrega: viernes 18 de marzo de 2016, 12:00 del mediodía*

**Lectura:** Griffiths: 3.2, 3.3, 3.4, 2.1 y 2.2.

## Problema 1. Gaussianas y saturación del producto de incertidumbre \[5 puntos\]

Consideremos la función de onda gaussiana

$$\psi(x) = N \exp\left(-\frac{x^2}{2a^2}\right) ,$$

donde $N \in \mathbb{R}$ y $a$ es una constante real positiva con unidades de longitud. Las integrales

$$\int_{-\infty}^{\infty} dx\, e^{-\alpha x^2 + \beta x} = \sqrt{\frac{\pi}{\alpha}}\exp\left(\frac{\beta^2}{4\alpha}\right) , \qquad \operatorname{Re}(\alpha) > 0 ,$$

$$\int_{-\infty}^{\infty} dx\, x^2 e^{-\alpha x^2} = \frac{1}{2\alpha}\int_{-\infty}^{\infty} dx\, e^{-\alpha x^2}$$

pueden ser útiles.

1.  Usa la función de onda en representación de posiciones dada arriba para calcular las incertidumbres $\Delta x$ y $\Delta p$. Confirma que tu respuesta satura el producto de incertidumbre de Heisenberg

$$\Delta x \, \Delta p \geq \frac{\hbar}{2} .$$

(Pistas: ¡estos cálculos son en realidad bastante breves si se hacen de la manera correcta! Usando la segunda de las integrales anteriores ni siquiera necesitas determinar $N$. Para evaluar $\langle \hat p^2 \rangle$ en el espacio de posiciones, traslada uno de los factores de $\hat p$ hacia $\psi^*$.)

1.  Calcula la transformada de Fourier $\phi(p)$ de $\psi(x)$. Usa el teorema de Parseval para confirmar tu respuesta y luego recalcula $\Delta p$ usando el espacio de momentos.

## Problema 2. Gaussianas complejas y el producto de incertidumbre \[10 puntos\]

Consideremos la función de onda gaussiana

$$\psi(x) = N \exp\left(-\frac{x^2}{2\Delta^2}\right) , \qquad \Delta \in \mathbb{C} , \quad \operatorname{Re}(\Delta^2) > 0 ,$$

donde $N$ es una constante de normalización real y $\Delta$ es ahora un número complejo: $\Delta^* \neq \Delta$. Las integrales del Problema 1 también son útiles aquí, así como la siguiente relación, válida para cualquier número complejo no nulo $z$,

$$\operatorname{Re}\left(\frac{1}{z}\right) = \frac{\operatorname{Re}(z)}{|z|^2} \qquad (\text{¡demuéstralo!})$$

1.  Usa la representación en el espacio de posiciones de la función de onda dada arriba para calcular las incertidumbres $\Delta x$ y $\Delta p$. Deja tu respuesta en términos de $|\Delta|$ y $\operatorname{Re}(\Delta^2)$. ($\Delta x$ dependerá de ambos[1], mientras que $\Delta p$ dependerá solo de $\operatorname{Re}(\Delta^2)$.)

2.  Calcula la transformada de Fourier $\phi(p)$ de $\psi(x)$. Usa el teorema de Parseval para confirmar tu respuesta y luego recalcula $\Delta p$ usando el espacio de momentos.

3.  Parametrizamos $\Delta$ usando una fase $\varphi_\Delta \in \mathbb{R}$ de la siguiente manera

$$\Delta = |\Delta|\, e^{i\varphi_\Delta} .$$

Calcula el producto $\Delta x \, \Delta p$ y confirma que la respuesta puede escribirse en términos de una función trigonométrica de $\varphi_\Delta$, y que $|\Delta|$ desaparece del resultado. ¿Es razonable tu respuesta para $\varphi_\Delta = 0$ y para $\varphi_\Delta = \pi/4$?

1.  Considera la evolución libre de un paquete de ondas gaussiano estudiada en el Problema 3 de la Tarea 4. ¿Cuál es $\Delta p$ en el instante $t=0$? Examina la evolución temporal de la gaussiana (¡a partir de la solución!) y lee el valor de la constante compleja dependiente del tiempo $\Delta^2$. Confirma que $\Delta p$, hallado en el apartado (a), da un resultado independiente del tiempo.

## Problema 3. Ejercicios con una partícula en una caja \[15 puntos\]

Consideremos un problema unidimensional para una partícula de masa $m$ que puede moverse libremente en el intervalo $x \in [0,a]$. El potencial $V(x)$ es nulo en este intervalo e infinito fuera de él. Para este sistema consideramos una solución de la ecuación de Schrödinger de la forma

$$\Psi_n(x,t) = N \sin\left(\frac{n\pi}{a}x\right) e^{-i\varphi_n(t)} , \qquad x \in [0,a] ,$$

y $\Psi_n(x,t) = 0$ para $x<0$ y $x>a$. Aquí $n \geq 1$ es un número entero.

1.  Encuentra la expresión de la fase (real) $\varphi_n(t)$ para que la función de onda anterior resuelva la ecuación de Schrödinger. Encuentra la constante de normalización $N$.

2.  Usa $\Psi_n(x,0)$ para calcular $\langle x \rangle$, $\langle x^2 \rangle$ y $\Delta x$.

3.  Usa $\Psi_n(x,0)$ para calcular $\langle p \rangle$, $\langle p^2 \rangle$ y $\Delta p$.

4.  ¿Se satisface la desigualdad de incertidumbre? ¿Está saturada?

5.  ¿Qué respuestas de (b) y (c) cambian para $\Psi_n(x,t)$? Explica por qué.

## Problema 4. Una pared dura \[5 puntos\]

Una partícula de masa $m$ se mueve en una dimensión, sujeta al potencial $V(x)$:

$$V(x) = \begin{cases} 0, & \text{para } x > 0, \\ \infty, & \text{para } x \leq 0 . \end{cases}$$

Encuentra los estados estacionarios y sus energías. Estos estados no pueden normalizarse.

## Problema 5. Un escalón en la recta infinita \[10 puntos\]

Una partícula de masa $m$ se mueve en una dimensión, sujeta al potencial $V(x)$:

$$V(x) = \begin{cases} V_0, & \text{para } x > 0, \\ 0, & \text{para } x \leq 0 . \end{cases}$$

Encuentra los estados estacionarios que existen para energías $0 < E < V_0$.

## Problema 6. Una pared y la mitad de un pozo finito \[10 puntos\]

Una partícula de masa $m$ se mueve en una dimensión, sujeta al potencial $V(x)$:

$$V(x) = \begin{cases} \infty, & \text{para } x < 0, \\ -V_0, & \text{para } 0 < x < a \quad (V_0 > 0), \\ 0, & \text{para } x > a . \end{cases}$$

Encuentra los estados estacionarios que corresponden a estados ligados ($E<0$ en este caso). ¿Existe siempre un estado ligado? Encuentra el valor mínimo de $z_0$

$$z_0^2 = \frac{2ma^2 V_0}{\hbar^2} ,$$

para el cual existen tres estados ligados. Explica la relación precisa de este problema con el problema del pozo cuadrado finito de anchura $2a$.

## Problema 7. Imitando el hidrógeno con un pozo cuadrado unidimensional \[5 puntos\]

El átomo de hidrógeno tiene un radio de Bohr $a_0$ y una energía del estado fundamental $E_0$ dados por

$$a_0 = \frac{\hbar^2}{me^2} \simeq 0.529 \times 10^{-10}\ \text{m} , \qquad E_0 = -\frac{e^2}{2a_0} = -13.6\ \text{eV}.$$

El estado fundamental es un estado ligado y el potencial tiende a cero en el infinito. Queremos diseñar un pozo cuadrado finito unidimensional

$$V(x) = \begin{cases} -V_0, & \text{para } |x| < a_0, \quad V_0 > 0, \\ 0, & \text{para } |x| > a_0, \end{cases}$$

que simule al átomo de hidrógeno. Calcula el valor de $V_0$ en eV para que el estado fundamental de la caja se encuentre a la profundidad correcta.

## Problema 8. No hay estados con $E < V(x)$ \[5 puntos\]

Consideremos un estado estacionario real $\psi(x)$ con energía $E$:

$$-\frac{\hbar^2}{2m}\psi''(x) + [V(x)-E]\psi(x) = 0 .$$

1.  Demuestra que $E$ debe superar el valor mínimo de $V(x)$, observando que $E = \langle H \rangle$.

2.  Explica esta afirmación intentando (y fracasando) esbozar una función de onda consistente con estar en la región clásicamente inaccesible para todos los valores de $x$.

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*

[1] De hecho, $\Delta x$ puede escribirse solamente en términos de $\operatorname{Re}(1/\Delta^2)$.


---

<!-- MIT8.04_LecNotes13_ES.md -->

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


---

<!-- MIT8.04_LecNotes14_15_ES.md -->

# Clases 14 y 15: Enfoque algebraico del oscilador armónico simple

## Vídeos de esta clase (YouTube)

**Lección 14: Simple harmonic oscillator II. Creation and annihilation operators.**

- [Recursion relation for the solution](https://www.youtube.com/watch?v=RxWfrE3o-9k)
- [Quantization of the energy](https://www.youtube.com/watch?v=Y6Ma-zn4Olk)
- [Algebraic solution of the harmonic oscillator](https://www.youtube.com/watch?v=8CCFPgd_P1w)
- [Ground state wavefunction](https://www.youtube.com/watch?v=vnyxYtj0mfE)

**Lección 15: Simple harmonic oscillator III. Scattering states and step potential.**

- [Number operator and commutators](https://www.youtube.com/watch?v=kefsxztSX74)
- [Excited states of the harmonic oscillator](https://www.youtube.com/watch?v=xmjvqbYvY9o)
- [Creation and annihilation operators acting on energy eigenstates](https://www.youtube.com/watch?v=BRFekCz4XQY)
- [Scattering states and the step potential](https://www.youtube.com/watch?v=0ABYYJSvkVk)

------------------------------------------------------------------------

*B. Zwiebach* *5 de abril de 2016*

## Contenido

1.  Solución algebraica del oscilador
2.  Manipulación de operadores y el espectro

## 1. Solución algebraica del oscilador

Ya hemos visto cómo calcular los autoestados de energía del oscilador armónico simple resolviendo una ecuación diferencial de segundo orden, la ecuación de Schrödinger independiente del tiempo.

Intentemos ahora factorizar el hamiltoniano del oscilador armónico. Con esto queremos decir, a grandes rasgos, escribir el hamiltoniano como el producto de un operador por su conjugado hermítico. Como primer paso, reescribimos el hamiltoniano como

$$\hat{H} = \tfrac{1}{2} m\omega^2 \left(\hat{x}^2 + \frac{\hat{p}^2}{m^2\omega^2}\right) \qquad \text{(1.1)}$$

Motivados por la identidad $a^2 + b^2 = (a-ib)(a+ib)$, válida para números $a$ y $b$, examinamos si la expresión entre paréntesis se puede escribir como un producto

$$\left(\hat{x} - \frac{i\hat{p}}{m\omega}\right)\left(\hat{x} + \frac{i\hat{p}}{m\omega}\right) = \hat{x}^2 + \frac{\hat{p}^2}{m^2\omega^2} + \frac{i}{m\omega}(\hat{x}\hat{p} - \hat{p}\hat{x}),$$

$$= \hat{x}^2 + \frac{\hat{p}^2}{m^2\omega^2} - \frac{\hbar}{m\omega}\mathbb{1}, \qquad \text{(1.2)}$$

donde los términos adicionales surgen porque $\hat{x}$ y $\hat{p}$, a diferencia de los números, no conmutan. Definimos ahora el factor situado más a la derecha en el producto anterior como $V$:

$$V \equiv \hat{x} + \frac{i\hat{p}}{m\omega}, \qquad \text{(1.3)}$$

Dado que $\hat{x}$ y $\hat{p}$ son operadores hermíticos, tenemos entonces

$$V^\dagger = \hat{x} - \frac{i\hat{p}}{m\omega}, \qquad \text{(1.4)}$$

¡y este es el factor situado más a la izquierda en el producto! Por lo tanto podemos reescribir (1.2) como

$$\hat{x}^2 + \frac{\hat{p}^2}{m^2\omega^2} = V^\dagger V + \frac{\hbar}{m\omega}\mathbb{1}, \qquad \text{(1.5)}$$

y por lo tanto, volviendo al hamiltoniano (1.1), encontramos

$$\hat{H} = \tfrac{1}{2}m\omega^2 V^\dagger V + \tfrac{1}{2}\hbar\omega\mathbb{1}. \qquad \text{(1.6)}$$

Esta es una forma factorizada del hamiltoniano: salvo por una constante aditiva $E_0$, $\hat{H}$ es el producto de una constante positiva por el producto de operadores $V^\dagger V$. Notamos que el conmutador de $V$ y $V^\dagger$ es simple

$$\left[V, V^\dagger\right] = \left[\hat{x} + \frac{i\hat{p}}{m\omega}, \hat{x} - \frac{i\hat{p}}{m\omega}\right] = -\frac{i}{m\omega}[\hat{x},\hat{p}] + \frac{i}{m\omega}[\hat{p},\hat{x}] = \frac{2\hbar}{m\omega}\mathbb{1}. \qquad \text{(1.7)}$$

Esto implica que

$$\left[\sqrt{\frac{m\omega}{2\hbar}}\, V,\ \sqrt{\frac{m\omega}{2\hbar}}\, V^\dagger\right] = \mathbb{1}. \qquad \text{(1.8)}$$

Esto sugiere la definición de los operadores adimensionales $\hat{a}$ y $\hat{a}^\dagger$:

$$\hat{a} \equiv \sqrt{\frac{m\omega}{2\hbar}}\, V,$$

$$\hat{a}^\dagger \equiv \sqrt{\frac{m\omega}{2\hbar}}\, V^\dagger. \qquad \text{(1.9)}$$

Debido al reescalamiento tenemos

$$\left[\hat{a}, \hat{a}^\dagger\right] = 1. \qquad \text{(1.10)}$$

El operador $\hat{a}$ se denomina operador de aniquilación y $\hat{a}^\dagger$ se denomina operador de creación. La justificación de estos nombres se verá más adelante. A partir de las definiciones anteriores leemos las relaciones entre $(\hat{a}, \hat{a}^\dagger)$ y $(\hat{x}, \hat{p})$:

$$\hat{a} = \sqrt{\frac{m\omega}{2\hbar}}\left(\hat{x} + \frac{i\hat{p}}{m\omega}\right),$$

$$\hat{a}^\dagger = \sqrt{\frac{m\omega}{2\hbar}}\left(\hat{x} - \frac{i\hat{p}}{m\omega}\right). \qquad \text{(1.11)}$$

Las relaciones inversas también son útiles muchas veces,

$$\hat{x} = \sqrt{\frac{\hbar}{2m\omega}}\left(\hat{a} + \hat{a}^\dagger\right),$$

$$\hat{p} = i\sqrt{\frac{m\omega\hbar}{2}}\left(\hat{a}^\dagger - \hat{a}\right). \qquad \text{(1.12)}$$

Aunque ni $\hat{a}$ ni $\hat{a}^\dagger$ son hermíticos (son conjugados hermíticos el uno del otro), las ecuaciones anteriores son consistentes con la hermiticidad de $\hat{x}$ y $\hat{p}$. Ahora podemos escribir el hamiltoniano en términos de los operadores $\hat{a}$ y $\hat{a}^\dagger$. Usando (1.9) tenemos

$$V^\dagger V = \frac{2\hbar}{m\omega}\hat{a}^\dagger \hat{a}, \qquad \text{(1.13)}$$

y por lo tanto, volviendo a (1.6), obtenemos

$$\hat{H} = \hbar\omega\left(\hat{a}^\dagger \hat{a} + \tfrac{1}{2}\right) = \hbar\omega\left(\hat{N} + \tfrac{1}{2}\right), \qquad \hat{N} \equiv \hat{a}^\dagger \hat{a}. \qquad \text{(1.14)}$$

La forma anterior del hamiltoniano está factorizada: salvo por una constante aditiva, $\hat{H}$ es el producto de una constante positiva por el producto de operadores $\hat{a}^\dagger \hat{a}$. Aquí hemos omitido el operador identidad, lo cual suele sobreentenderse. También hemos introducido el operador número $\hat{N}$. Este es, por construcción, un operador hermítico, y es, salvo una escala y una constante aditiva, igual al hamiltoniano. Un autoestado de $\hat{H}$ es también un autoestado de $\hat{N}$, y de la relación anterior se sigue que los correspondientes autovalores $E$ y $N$ están relacionados por

$$E = \hbar\omega\left(N + \tfrac{1}{2}\right). \qquad \text{(1.15)}$$

Mostremos ahora las poderosas conclusiones que surgen del hamiltoniano factorizado. Sobre cualquier estado $\psi$ normalizado tenemos

$$\langle \hat{H} \rangle_\psi = (\psi, \hat{H}\psi) = \hbar\omega\, (\psi, \hat{a}^\dagger \hat{a}\psi) + \tfrac{1}{2}\hbar\omega\,(\psi,\psi), \qquad \text{(1.16)}$$

y trasladando el $\hat{a}^\dagger$ a la primera entrada, obtenemos

$$\langle \hat{H} \rangle_\psi = \hbar\omega\, (\hat{a}\psi, \hat{a}\psi) + \tfrac{1}{2}\hbar\omega \geq \tfrac{1}{2}\hbar\omega. \qquad \text{(1.17)}$$

La desigualdad se sigue del hecho de que cualquier expresión de la forma $(\varphi,\varphi)$ es mayor o igual que cero. Esto muestra que para cualquier autoestado de energía con energía $E$: $\hat{H}\psi = E\psi$ tenemos

$$\text{Autoestados de energía: } E \geq \tfrac{1}{2}\hbar\omega. \qquad \text{(1.18)}$$

Este importante resultado sobre el espectro se sigue directamente de la factorización del hamiltoniano. Pero también obtenemos la información necesaria para hallar la función de onda del estado fundamental. La energía mínima $\tfrac{1}{2}\hbar\omega$ se realizará para un estado $\psi$ si el término $(\hat{a}\psi, \hat{a}\psi)$ en (1.17) se anula. Para que esto se anule, $\hat{a}\psi$ debe anularse. Por lo tanto, la función de onda del estado fundamental $\varphi_0$ debe satisfacer

$$\hat{a}\, \varphi_0 = 0. \qquad \text{(1.19)}$$

El operador $\hat{a}$ aniquila el estado fundamental, y esta es la razón por la que $\hat{a}$ se llama operador de aniquilación. Usando la definición de $\hat{a}$ en (1.11) y la representación en el espacio de posiciones de $\hat{p}$, esto se convierte en

$$\left(x + \frac{i}{m\omega}\frac{\hbar}{i}\frac{d}{dx}\right)\varphi_0(x) = 0 \ \longrightarrow\ \left(x + \frac{\hbar}{m\omega}\frac{d}{dx}\right)\varphi_0(x) = 0. \qquad \text{(1.20)}$$

Notablemente, esta es una ecuación diferencial de primer orden para el estado fundamental. No es una ecuación de segundo orden, como la ecuación de Schrödinger que determina los autoestados de energía en general. Esta es una simplificación drástica que ofrece la factorización del hamiltoniano en un producto de operadores diferenciales de primer orden. La ecuación anterior se reordena como

$$\frac{d\varphi_0}{dx} = -\frac{m\omega}{\hbar}\, x\, \varphi_0. \qquad \text{(1.21)}$$

Resolviendo esta ecuación diferencial se obtiene

$$\varphi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4} e^{-\frac{m\omega}{2\hbar}x^2}, \qquad \text{(1.22)}$$

donde hemos incluido una constante de normalización para garantizar que $(\varphi_0, \varphi_0) = 1$. Nótese que $\varphi_0$ es en efecto un autoestado de energía con energía $E_0$:

$$\hat{H}\varphi_0 = \hbar\omega\left(\hat{a}^\dagger \hat{a} + \tfrac{1}{2}\right)\varphi_0 = \tfrac{1}{2}\hbar\omega\,\varphi_0 \ \longrightarrow\ E_0 = \tfrac{1}{2}\hbar\omega. \qquad \text{(1.23)}$$

Antes de continuar con el análisis de los estados excitados, examinemos las propiedades de la factorización de manera más general. Factorizar un hamiltoniano significa hallar un operador $\hat{A}$ tal que podamos reescribir el hamiltoniano como $\hat{A}^\dagger \hat{A}$ salvo una constante aditiva. Aquí $\hat{A}^\dagger$ es el conjugado hermítico de $\hat{A}$, un operador que se define mediante

$$(\psi, \hat{A}^\dagger \varphi) = (\hat{A}\psi, \varphi). \qquad \text{(1.24)}$$

Decimos que hemos factorizado un hamiltoniano $\hat{H}$ si podemos encontrar un $\hat{A}$ para el cual

$$\hat{H} = \hat{A}^\dagger \hat{A} + E_0\, \mathbb{1}, \qquad \text{(1.25)}$$

donde $E_0$ es una constante con unidades de energía que multiplica al operador identidad. Esta constante no complica nuestra tarea de hallar los autoestados del hamiltoniano ni sus energías: cualquier autofunción de $\hat{A}^\dagger \hat{A}$ es una autofunción de $\hat{H}$. De la factorización (1.25) se siguen dos propiedades clave.

1.  Cualquier autoestado de energía debe tener una energía mayor o igual que $E_0$. Primero notemos que para un $\psi(x)$ normalizado arbitrario tenemos

$$(\psi, \hat{H}\psi) = (\psi, \hat{A}^\dagger \hat{A}\psi) + E_0 (\psi,\psi) = (\hat{A}\psi, \hat{A}\psi) + E_0, \qquad \text{(1.26)}$$

Dado que el solapamiento $(\hat{A}\psi, \hat{A}\psi)$ es mayor o igual que cero, hemos demostrado que

$$(\psi, \hat{H}\psi) \geq E_0. \qquad \text{(1.27)}$$

Si tomamos $\psi$ como un autoestado de energía con energía $E$: $\hat{H}\psi = E\psi$, la relación anterior nos da

$$E \geq E_0. \qquad \text{(1.28)}$$

Esto demuestra, como se afirmó, que todas las energías posibles son mayores o iguales que $E_0$.

1.  Una función de onda $\psi_0$ que satisface

$$\hat{A}\, \psi_0 = 0, \qquad \text{(1.29)}$$

es un autoestado de energía que satura la desigualdad (1.28). En efecto,

$$\hat{H}\psi_0 = \hat{A}^\dagger \hat{A}\, \psi_0 + E_0 \psi_0 = \hat{A}^\dagger (\hat{A}\, \psi_0) + E_0 \psi_0 = E_0 \psi_0. \qquad \text{(1.30)}$$

El estado $\psi_0$ que satisface $\hat{A}\, \psi_0 = 0$ es el estado fundamental. Para hamiltonianos convencionales esta es una ecuación diferencial de primer orden para $\psi_0$, y mucho más fácil de resolver que la ecuación de Schrödinger.

## 2. Manipulación de operadores y el espectro

Hemos visto que todos los autoestados de energía son autoestados del operador número hermítico $\hat{N} = \hat{a}^\dagger \hat{a}$. Esto se debe a que $\hat{H} = \hbar\omega\left(\hat{N} + \tfrac{1}{2}\right)$. Nótese que, como $\hat{a}\varphi_0 = 0$, también tenemos

$$\hat{N}\varphi_0 = 0. \qquad \text{(2.1)}$$

Podemos comprobar rápidamente que

$$\left[\hat{N}, \hat{a}\right] = \left[\hat{a}^\dagger \hat{a}, \hat{a}\right] = \left[\hat{a}^\dagger, \hat{a}\right]\hat{a} = -\hat{a},$$

$$\left[\hat{N}, \hat{a}^\dagger\right] = \left[\hat{a}^\dagger \hat{a}, \hat{a}^\dagger\right] = \hat{a}^\dagger \left[\hat{a}, \hat{a}^\dagger\right] = \hat{a}^\dagger, \qquad \text{(2.2)}$$

que resumimos como

$$\left[\hat{N}, \hat{a}\right] = -\hat{a},$$

$$\left[\hat{N}, \hat{a}^\dagger\right] = \hat{a}^\dagger. \qquad \text{(2.3)}$$

Usando estas identidades y por inducción se debería poder demostrar que:

$$\left[\hat{N}, (\hat{a})^k\right] = -k(\hat{a})^k,$$

$$\left[\hat{N}, (\hat{a}^\dagger)^k\right] = k(\hat{a}^\dagger)^k. \qquad \text{(2.4)}$$

Estas relaciones sugieren por qué $\hat{N}$ se llama operador número. Al actuar por conmutación sobre potencias de operadores de creación o de aniquilación, se obtiene el mismo objeto multiplicado por (más o menos) el número de operadores de creación o de aniquilación, $k$ en lo anterior. Los siguientes conmutadores relacionados también son útiles:

$$\left[\hat{a}^\dagger, (\hat{a})^k\right] = -k(\hat{a})^{k-1}$$

$$\left[\hat{a}, (\hat{a}^\dagger)^k\right] = k(\hat{a}^\dagger)^{k-1}. \qquad \text{(2.5)}$$

Estos conmutadores son análogos a $[\hat{p}, (\hat{x})^k]$ y $[\hat{x}, (\hat{p})^k]$. También haremos uso del siguiente lema, que ayuda en las evaluaciones donde tenemos un operador $\hat{A}$ que anula un estado $\psi$ y queremos simplificar la acción de $\hat{A}\hat{B}$, donde $\hat{B}$ es otro operador, actuando sobre $\psi$. Este es el resultado

$$\text{Si } \hat{A}\,\psi = 0, \text{ entonces } \hat{A}\hat{B}\,\psi = \left[\hat{A}, \hat{B}\right]\psi. \qquad \text{(2.6)}$$

Esto se demuestra fácilmente. Primero notemos que

$$\hat{A}\hat{B} = \left[\hat{A}, \hat{B}\right] + \hat{B}\hat{A}, \qquad \text{(2.7)}$$

como se puede comprobar rápidamente expandiendo el lado derecho. De ahí se sigue que

$$\hat{A}\hat{B}\,\psi = \left(\left[\hat{A}, \hat{B}\right] + \hat{B}\hat{A}\right)\psi = \left[\hat{A}, \hat{B}\right]\psi, \qquad \text{(2.8)}$$

porque $\hat{B}\hat{A}\,\psi = \hat{B}(\hat{A}\psi) = 0$. Esto es lo que queríamos demostrar. Esto es todo lo que necesitamos saber sobre conmutadores, y ahora podemos proceder a construir los estados del oscilador armónico.

Dado que $\hat{a}$ aniquila $\varphi_0$, consideremos actuar sobre el estado fundamental con $\hat{a}^\dagger$. Es claro que $\hat{a}^\dagger$ no puede también aniquilar $\varphi_0$. Si esto sucediera, actuar con ambos lados de la identidad del conmutador $\left[\hat{a}, \hat{a}^\dagger\right] = 1$ sobre $\varphi_0$ llevaría a una contradicción: el lado izquierdo se anularía pero el lado derecho no. Por lo tanto, consideremos la función de onda

$$\varphi_1 \equiv \hat{a}^\dagger \varphi_0. \qquad \text{(2.9)}$$

Vamos a demostrar que este es un autoestado de energía. Para ello actuamos sobre él con el operador número:

$$\hat{N}\varphi_1 = \hat{N}\hat{a}^\dagger \varphi_0 = \left[\hat{N}, \hat{a}^\dagger\right]\varphi_0, \qquad \text{(2.10)}$$

donde notamos que $\hat{N}\varphi_0 = 0$ y usamos el lema (2.6). Dado que $\left[\hat{N}, \hat{a}^\dagger\right] = \hat{a}^\dagger$, obtenemos

$$\hat{N}\varphi_1 = \hat{a}^\dagger \varphi_0 = \varphi_1. \qquad \text{(2.11)}$$

Por lo tanto $\varphi_1$ es un autoestado del operador $\hat{N}$ con autovalor $N=1$. Dado que $\varphi_0$ tiene autovalor de $\hat{N}$ igual a cero, el efecto de actuar sobre $\varphi_0$ con $\hat{a}^\dagger$ fue aumentar el autovalor del operador número en una unidad. El operador $\hat{a}^\dagger$ se llama operador de creación porque crea un estado a partir del estado fundamental. Alternativamente, se le llama operador de subida (o ascenso), porque sube (en una unidad) el autovalor de $\hat{N}$. Dado que $N=1$ para $\varphi_1$, se sigue que $\varphi_1$ es un autoestado de energía con energía $E_1$ dada por

$$E_1 = \hbar\omega\left(1 + \tfrac{1}{2}\right) = \tfrac{3}{2}\hbar\omega. \qquad \text{(2.12)}$$

Resulta también que $\varphi_1$ está correctamente normalizado:

$$(\varphi_1, \varphi_1) = (\hat{a}^\dagger \varphi_0, \hat{a}^\dagger \varphi_0) = (\varphi_0, \hat{a}\hat{a}^\dagger \varphi_0), \qquad \text{(2.13)}$$

donde usamos la propiedad de conjugación hermítica para trasladar el $\hat{a}^\dagger$ que actúa sobre la entrada izquierda hacia la entrada derecha, donde se convierte en $(\hat{a}^\dagger)^\dagger = \hat{a}$. Tenemos entonces

$$(\varphi_1, \varphi_1) = (\varphi_0, \hat{a}\hat{a}^\dagger \varphi_0) = (\varphi_0, \left[\hat{a}, \hat{a}^\dagger\right]\varphi_0) = (\varphi_0, \varphi_0) = 1, \qquad \text{(2.14)}$$

donde usamos (2.6) en la evaluación de $\hat{a}\hat{a}^\dagger \psi_0$. En efecto, el estado $\varphi_1$ está correctamente normalizado.

A continuación consideremos el estado

$$\varphi_2' \equiv \hat{a}^\dagger \hat{a}^\dagger \varphi_0. \qquad \text{(2.15)}$$

Este tiene

$$\hat{N}\varphi_2' = \hat{N}\hat{a}^\dagger \hat{a}^\dagger \varphi_0 = \left[\hat{N}, \hat{a}^\dagger \hat{a}^\dagger\right]\varphi_0 = 2\hat{a}^\dagger \hat{a}^\dagger \varphi_0 = 2\varphi_2', \qquad \text{(2.16)}$$

de modo que $\varphi_2$ es un estado con número $N=2$ y energía $E_2 = \tfrac{5}{2}\hbar\omega$. ¿Está correctamente normalizado? Encontramos

$$(\varphi_2', \varphi_2') = (\hat{a}^\dagger \hat{a}^\dagger \varphi_0, \hat{a}^\dagger \hat{a}^\dagger \varphi_0) = (\varphi_0, \hat{a}\hat{a}\hat{a}^\dagger \hat{a}^\dagger \varphi_0) = (\varphi_0, \hat{a}\left[\hat{a}, \hat{a}^\dagger\right]\hat{a}^\dagger \varphi_0)$$

$$= (\varphi_0, 2\hat{a}\hat{a}^\dagger \varphi_0) = 2(\varphi_0, \varphi_0) = 2. \qquad \text{(2.17)}$$

La función de onda correctamente normalizada es entonces

$$\varphi_2 \equiv \frac{1}{\sqrt{2}}\,\hat{a}^\dagger \hat{a}^\dagger \varphi_0. \qquad \text{(2.18)}$$

Afirmamos ahora que el $n$-ésimo estado excitado del oscilador armónico simple es

$$\varphi_n \equiv \frac{1}{\sqrt{n!}}\underbrace{\hat{a}^\dagger \cdots \hat{a}^\dagger}_{n}\,\varphi_0 = \frac{1}{\sqrt{n!}}\left(\hat{a}^\dagger\right)^n \varphi_0. \qquad \text{(2.19)}$$

**Ejercicio.** Verifique que este estado tiene autovalor de $\hat{N}$ igual a $n$.

**Ejercicio.** Verifique que el estado $\varphi_n$ está correctamente normalizado.

Dado que el autovalor de $\hat{N}$ de $\varphi_n$ es $n$, su energía $E_n$ está dada por

$$E_n = \hbar\omega\left(n + \tfrac{1}{2}\right). \qquad \text{(2.20)}$$

Dado que los distintos estados $\varphi_n$ son autoestados de un operador hermítico (el hamiltoniano $\hat{H}$) con autovalores diferentes, son ortonormales

$$(\varphi_n, \varphi_m) = \delta_{m,n}. \qquad \text{(2.21)}$$

Notamos ahora que $\hat{a}\varphi_n$ es un estado con $n-1$ operadores $\hat{a}^\dagger$ actuando sobre $\varphi_0$, porque el $\hat{a}$ elimina uno de los operadores de creación en $\varphi_n$. Así pues, esperamos que $\hat{a}\varphi_n \sim \varphi_{n-1}$. Podemos precisar esto

$$\hat{a}\, \varphi_n = \hat{a}\, \frac{1}{\sqrt{n!}}\left(\hat{a}^\dagger\right)^n \varphi_0 = \frac{1}{\sqrt{n!}}\left[\hat{a}, \left(\hat{a}^\dagger\right)^n\right]\varphi_0 = \frac{n}{\sqrt{n!}}\left(\hat{a}^\dagger\right)^{n-1}\varphi_0. \qquad \text{(2.22)}$$

En este punto usamos (2.19) con $n$ reemplazado por $n-1$ y así obtenemos

$$\hat{a}\,\varphi_n = \frac{n}{\sqrt{n!}}\sqrt{(n-1)!}\,\varphi_{n-1} = \sqrt{n}\,\varphi_{n-1}. \qquad \text{(2.23)}$$

Mediante la acción de $\hat{a}^\dagger$ sobre $\varphi_n$ obtenemos

$$\hat{a}^\dagger \varphi_n = \frac{1}{\sqrt{n!}}\left(\hat{a}^\dagger\right)^{n+1}\varphi_0 = \frac{1}{\sqrt{n!}}\sqrt{(n+1)!}\,\varphi_{n+1} = \sqrt{n+1}\,\varphi_{n+1}. \qquad \text{(2.24)}$$

Recopilando los resultados, tenemos

$$\hat{a}\,\varphi_n = \sqrt{n}\,\varphi_{n-1},$$

$$\hat{a}^\dagger \varphi_n = \sqrt{n+1}\,\varphi_{n+1}. \qquad \text{(2.25)}$$

Estas relaciones dejan claro que $\hat{a}$ reduce en una unidad el número de cualquier autoestado de energía, excepto el vacío $\varphi_0$, al cual aniquila. El operador de subida $\hat{a}^\dagger$ aumenta en una unidad el número de cualquier autoestado.

**Ejercicio.** Calcule la incertidumbre $\Delta x$ de la posición en el $n$-ésimo autoestado de energía.

**Solución.** Por definición,

$$(\Delta x)_n^2 = \langle \hat{x}^2 \rangle_{\varphi_n} - \langle \hat{x} \rangle_{\varphi_n}^2. \qquad \text{(2.26)}$$

El valor esperado $\langle \hat{x} \rangle$ se anula para cualquier autoestado de energía, ya que estamos integrando $x$, que es impar, frente a $|\varphi_n(x)|^2$, que siempre es par. Aun así, es instructivo ver cómo sucede esto explícitamente:

$$\langle \hat{x} \rangle_{\varphi_n} = (\varphi_n, \hat{x}\varphi_n) = \sqrt{\frac{\hbar}{2m\omega}}\,(\varphi_n, (\hat{a} + \hat{a}^\dagger)\varphi_n), \qquad \text{(2.27)}$$

usando la fórmula de $\hat{x}$ en términos de $\hat{a}$ y $\hat{a}^\dagger$. El solapamiento anterior se anula porque $\hat{a}\varphi_n \sim \varphi_{n-1}$ y $\hat{a}^\dagger \varphi_n \sim \varphi_{n+1}$, y tanto $\varphi_{n-1}$ como $\varphi_{n+1}$ son ortogonales a $\varphi_n$. Ahora calculamos el valor esperado de $\hat{x}^2$

$$\langle \hat{x}^2 \rangle_{\varphi_n} = (\varphi_n, \hat{x}^2 \varphi_n) = \frac{\hbar}{2m\omega}\,(\varphi_n, (\hat{a} + \hat{a}^\dagger)(\hat{a} + \hat{a}^\dagger)\varphi_n)$$

$$= \frac{\hbar}{2m\omega}\,(\varphi_n, (\hat{a}\hat{a} + \hat{a}\hat{a}^\dagger + \hat{a}^\dagger \hat{a} + \hat{a}^\dagger \hat{a}^\dagger)\varphi_n). \qquad \text{(2.28)}$$

Dado que $\hat{a}\hat{a}\varphi_n \sim \varphi_{n-2}$ y $\hat{a}^\dagger \hat{a}^\dagger \varphi_n \sim \varphi_{n+2}$, y tanto $\varphi_{n-2}$ como $\varphi_{n+2}$ son ortogonales a $\varphi_n$, los términos $\hat{a}\hat{a}$ y $\hat{a}^\dagger \hat{a}^\dagger$ no contribuyen. Nos queda

$$\langle \hat{x}^2 \rangle_{\varphi_n} = \frac{\hbar}{2m\omega}\,(\varphi_n, (\hat{a}\hat{a}^\dagger + \hat{a}^\dagger \hat{a})\varphi_n). \qquad \text{(2.29)}$$

En este punto reconocemos que $\hat{a}^\dagger \hat{a} = \hat{N}$ y que $\hat{a}\hat{a}^\dagger = \left[\hat{a}, \hat{a}^\dagger\right] + \hat{a}^\dagger \hat{a} = 1 + \hat{N}$. Como resultado

$$\langle \hat{x}^2 \rangle_{\varphi_n} = \frac{\hbar}{2m\omega}\,(\varphi_n, (1 + 2\hat{N})\varphi_n) = \frac{\hbar}{2m\omega}(1 + 2n). \qquad \text{(2.30)}$$

Por lo tanto tenemos

$$(\Delta x)_n^2 = \frac{\hbar}{m\omega}\left(n + \tfrac{1}{2}\right). \qquad \text{(2.31)}$$

La incertidumbre en la posición crece linealmente con el número.

------------------------------------------------------------------------

*Sarah Geller y Andrew Turner transcribieron las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare https://ocw.mit.edu

8.04 Física Cuántica I Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

# Apéndice: Lista de problemas 6 (Problem Set 6, 2016)

**Departamento de Física del MIT — Física Cuántica I (8.04), primavera de 2016**

**Fecha de publicación:** 17 de marzo de 2016. **Fecha de entrega:** viernes 1 de abril de 2016, 12:00 del mediodía.

**Lectura:** Griffiths, sección 2.6. Para la semana siguiente, secciones 2.5 y 2.3.

## Problema 1

**Partícula en un pozo cuadrado. \[10 puntos\]**

Una partícula de masa $m$ se mueve en un pozo cuadrado infinito de anchura $a$. Su función de onda en el instante $t=0$ es

$$\Psi(x,0) = \sqrt{\frac{1}{3}}\sqrt{\frac{2}{a}}\sin\left(\frac{2\pi x}{a}\right) + \sqrt{\frac{2}{3}}\sqrt{\frac{2}{a}}\sin\left(\frac{3\pi x}{a}\right).$$

1.  ¿Es $\Psi$ un autoestado de energía? Encuentre $\Psi(x,t)$.

2.  ¿Cuáles son las probabilidades de que una medida de la energía en el instante $t$ dé cada uno de los siguientes valores?

$$\frac{\hbar^2\pi^2}{2ma^2},\qquad \frac{4\hbar^2\pi^2}{2ma^2},\qquad \frac{9\hbar^2\pi^2}{2ma^2}.$$

1.  ¿Cuál es el valor esperado de $x$ en el instante $t$?

2.  ¿Cuál es el valor esperado de $p$ en el instante $t$?

## Problema 2

**No degeneración de los estados ligados en una dimensión \[10 puntos\]**

Problema 2.45 de Griffiths, p. 87.

## Problema 3

**Pozo rectangular infinito en el plano \[10 puntos\]**

Considere una partícula de masa $m$ que se mueve en el plano $x,y$ con un potencial que es nulo dentro de la caja rectangular formada por todos los puntos $(x,y)$ para los cuales

$$0 \le x \le L_x,\qquad 0 \le y \le L_y,$$

y es infinito en cualquier otro punto.

1.  Use la ecuación de Schrödinger bidimensional para hallar los autoestados de energía. Dé las energías y las autofunciones normalizadas.

2.  Considere el caso $L_x = L_y = L$. Verá que hay degeneraciones en el espectro de energía. Algunas degeneraciones tienen una explicación de simetría sencilla; identifíquelas y explique por qué ocurren. Algunas degeneraciones son accidentales; parecen aleatorias. Muestre algunos ejemplos. \[Pista: $49+1 = 25+25$\].

3.  Demuestre que siempre que $(L_x/L_y)^2$ sea irracional no hay degeneraciones.

## Problema 4

**Un pozo cuadrado infinito con un escalón \[10 puntos\]**

Una partícula de masa $m$ se mueve en una dimensión, sometida al potencial $V(x)$:

$$V(x) =
\begin{cases}
\infty, & \text{para } x < 0, \\
0, & \text{para } 0 < x < a, \\
V_0, & \text{para } a < x < 2a,\quad (V_0 > 0) \\
\infty, & \text{para } x > 2a.
\end{cases}$$

1.  Encuentre las ecuaciones que determinan los estados estacionarios con energías $0 < E < V_0$. Para ello definimos

$$k^2 \equiv \frac{2mE}{\hbar^2},\qquad \kappa^2 \equiv \frac{2m(V_0-E)}{\hbar^2},\qquad z_0^2 = \frac{2ma^2V_0}{\hbar^2},\qquad \eta \equiv ka,\qquad \xi \equiv \kappa a.$$

(Usamos $k$ para las regiones clásicamente permitidas y $\kappa$ para las regiones clásicamente prohibidas). Sus ecuaciones deberían poder escribirse en términos de $\xi$, $\eta$ y $z_0$.

1.  Como aplicación numérica, considere $z_0 = 2\pi$. ¿Cuántos estados obtiene con $E < V_0$? Halle los valores posibles de la energía $E$ en términos de $V_0$ (use al menos 4 cifras significativas).

## Problema 5

**Método de disparo (shooting method) y aplicación \[15 puntos\]**

Para una partícula en un potencial cuártico $V(x) \sim x^4$, tras reescalar $x$ en una variable adimensional $u$, la ecuación de Schrödinger toma la forma

$$-\frac{1}{2}\frac{d^2\psi}{du^2} + (u^4 - e)\psi = 0,$$

donde $e$ es una medida adimensional del autovalor de energía. A continuación se dan las instrucciones de Mathematica que permiten hallar los valores de $e$ para las soluciones pares de este potencial. Estas instrucciones producen una gráfica de la solución $\psi(u)$, para $u \in [0, 3.5]$, con unas condiciones iniciales adecuadas y para el valor elegido de la energía $e$.

    Clear[e, psi]
    v[x_]:= x^4
    e=0.65;
    psi = psi/. NDSolve[{-(1/2)psi''[u] + (v[u]-e)psi[u]==0, psi[0]==1,
      psi'[0]==0}, psi, {u, 0, 3.5}][[1]];
    Plot[psi[u], {u, 0, 3.5}]

Tras ejecutar estas instrucciones, si escribe `psi[0.5]`, por ejemplo, el programa devolverá el valor de $\psi$ en $u=0.5$.

Juegue con esto para familiarizarse. El valor inicial de $e$ fijado arriba es 0.65, pero la energía del estado fundamental, como puede averiguar por prueba y error, es un poco más alta.

Retomamos ahora el problema anterior: una partícula de masa $m$ en un pozo cuadrado infinito con un escalón. De nuevo, tomamos $z_0 = 2\pi$. Encontró dos estados ligados con $E < V_0$:

$$E_1 = 0.\#\#436\, V_0,\qquad E_2 = 0.\#\#747\, V_0.$$

1.  Use $x = au$, con $u \in [0,2]$ adimensional, y escriba $V = V_0 f(u)$ para una función $f(u)$ adecuadamente definida, con el fin de obtener una ecuación diferencial para los autoestados de energía en la que no aparezcan unidades y el autovalor de energía quede codificado por el número puro $e = E/V_0$. Ponga a prueba su ecuación diferencial con el método de disparo para recuperar los valores anteriores de $E_1$ y $E_2$. Halle los dos siguientes niveles de energía $E_3$ y $E_4$.

2.  Discutimos en clase el hecho de que, para potenciales que varían lentamente, la amplitud de la función de onda es aproximadamente proporcional a la raíz cuadrada de la longitud de onda de de Broglie “local”. Nuestro potencial, al tener un escalón, no varía realmente de forma lenta, pero aun así podemos ver numéricamente hasta qué punto se cumple esta propiedad.

Construya el autoestado de energía con 8 nodos (el octavo estado excitado) y determine su energía. Sean $A_L$ y $A_R$ las amplitudes de su función de onda en los lados izquierdo y derecho del pozo cuadrado. Lea el cociente $A_L/A_R$ de su función de onda y compárelo con la predicción para este cociente usando la longitud de onda de de Broglie.

## Problema 6

**Ion de hidrógeno usando el modelo del pozo cuadrado. \[10 puntos\]**

La última vez modelamos el tamaño del átomo de hidrógeno y la energía de su estado fundamental

$$a_0 = \frac{\hbar^2}{me^2},\qquad E_0 = -\frac{e^2}{2a_0} = -13.6\ \text{eV},$$

usando el potencial de pozo cuadrado

$$V(x) =
\begin{cases}
-V_0, & \text{para } |x| < a_0,\quad V_0 > 0, \\
0, & \text{para } |x| > a_0.
\end{cases}$$

Anteriormente encontró que este pozo tiene

$$z_0 = 1.3192,\qquad V_0 = z_0^2 |E_0| = 1.7402\, |E_0| = 23.67\ \text{eV}.$$

El potencial de pozo cuadrado imita el potencial creado por el protón, y la energía del estado fundamental es la energía del electrón en dicho potencial.

Para simular el ion de hidrógeno $H_2^+$ (2 protones, 1 electrón) construiremos un potencial par con dos modelos idénticos de pozo cuadrado de hidrógeno separados por una pequeña distancia $2\gamma a_0$, donde $\gamma$ es una constante positiva adimensional pequeña. El potencial es por tanto

$$V(x) =
\begin{cases}
0, & \text{para } |x| < \gamma a_0, \\
-V_0, & \text{para } \gamma a_0 < |x| < (2+\gamma)a_0,\quad V_0 > 0, \\
0, & \text{para } |x| > (2+\gamma)a_0.
\end{cases}$$

Para concretar, trabaje con $\gamma = 0.2$.

1.  Use el método de disparo para hallar la energía del autoestado de menor energía, es decir, la energía del estado ligado de un electrón compartido por los dos protones. Muestre la función de onda del electrón a partir de la gráfica de su solución.

2.  La energía de enlace del ion se obtiene sumando la energía positiva debida a la repulsión de los dos protones a la energía del estado fundamental anterior. ¿Qué energía de enlace obtiene? ¿Cómo se compara con el valor experimental?

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*


---

<!-- MIT8.04_LecNotes16_ES.md -->

# Clase 16: Estados de dispersión y el potencial escalón

## Vídeos de esta clase (YouTube)

**Lección 16: Step potential reflection and transmission coefficients. Phase shift, wavepackets and time delay.**

- [Step potential probability current](https://www.youtube.com/watch?v=z79v39lMR3k)
- [Reflection and transmission coefficients](https://www.youtube.com/watch?v=bX-k26w-tsU)
- [Energy below the barrier and phase shift](https://www.youtube.com/watch?v=EkpbxgEslE4)
- [Wavepackets](https://www.youtube.com/watch?v=NXPvXI603RA) (20:51)
- [Wavepackets with energy below the barrier](https://www.youtube.com/watch?v=yqrMAZkQOwI)
- [Particle on the forbidden region](https://www.youtube.com/watch?v=lA8-N_ARHTw)

------------------------------------------------------------------------

B. Zwiebach

19 de abril de 2016

## Contenido

1.  El potencial escalón
2.  Potencial escalón con $E > V_0$
3.  Potencial escalón con $E < V_0$
4.  Paquetes de onda en el potencial escalón

## 1. El potencial escalón

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes16_ES/fig1.png)

Figura 1: El potencial escalón.

Comenzamos ahora nuestro estudio detallado de los estados de dispersión. Estos son estados propios de energía no normalizables. Sencillamente no pueden normalizarse, igual que los estados propios de momento. Estos estados propios de energía no son estados de partículas; hay que superponer estados de dispersión para producir estados normalizables que puedan representar una partícula sometida a dispersión en algún potencial. Aquí examinamos el potencial escalón (Figura 1), definido por

$$V(x) = \begin{cases} 0, & x < 0, \\ V_0, & x \geq 0. \end{cases} \qquad \text{(1.1)}$$

Nuestras soluciones a la ecuación de Schrödinger con este potencial serán estados de dispersión de energía definida $E$. Podemos considerar dos casos: $E > V_0$ y $E < V_0$. En ambos casos la función de onda se extiende infinitamente hacia la izquierda y no es normalizable. Comencemos con el caso $E > V_0$.

## 2. Potencial escalón con $E > V_0$

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes16_ES/fig2.png)

Figura 2: La energía $E$ del estado estacionario es mayor que el escalón $V_0$. Todo el eje $x$ es clásicamente permitido.

El estado estacionario con energía $E$ tiene la forma

$$\Psi(x,t) = \psi(x) e^{-iEt/\hbar}, \qquad \text{(2.2)}$$

y nos centraremos primero en la función desconocida $\psi(x)$. Para escribir un ansatz adecuado para $\psi(x)$ visualizamos un proceso físico en el que tenemos una onda incidente sobre la barrera escalón desde la izquierda. Dada tal onda que viaja en la dirección de $x$ creciente, esperaríamos una onda reflejada y una onda transmitida. La onda reflejada, moviéndose en la dirección de $x$ decreciente, existiría para $x < 0$. La onda transmitida, moviéndose en la dirección de $x$ creciente, existiría para $x > 0$. El ansatz para el estado propio de energía debe contener por tanto las tres partes:

$$\psi(x) = \begin{cases} A e^{ikx} + B e^{-ikx}, & x < 0, \\ C e^{i\bar{k}x}, & x > 0. \end{cases} \qquad \text{(2.3)}$$

Recordemos que $e^{ikx}$, con $k > 0$, representa una onda que se mueve en la dirección de $x$ creciente, dada la dependencia temporal universal anterior. Por tanto $A$ es el coeficiente de la onda incidente, $B$ es el coeficiente de la onda reflejada, y $C$ es el coeficiente de la onda transmitida. Las ondas para $x < 0$ tienen número de onda $k$ y la onda para $x > 0$ tiene número de onda $\bar{k}$. Estos números de onda quedan fijados por la ecuación de Schrödinger

$$k^2 = \frac{2mE}{\hbar^2}, \qquad \bar{k}^2 = \frac{2m(E - V_0)}{\hbar^2}. \qquad \text{(2.4)}$$

Hay dos ecuaciones que restringen nuestros coeficientes $A$, $B$ y $C$: tanto la función de onda como su derivada deben ser continuas en $x = 0$. Con estas dos condiciones podemos resolver $B$ y $C$ en términos de $A$. Esto es todo lo que podríamos esperar hacer: debido a la linealidad, la escala global de estos tres coeficientes debe permanecer indeterminada. De hecho, podemos pensar en $A$ como el valor de entrada y en $B$ y $C$ como valores de salida. Comencemos:

- $\psi(x)$ debe ser continua en $x = 0$. Por tanto

$$A + B = C. \qquad \text{(2.5)}$$

- $\psi'(x)$ debe ser continua en $x = 0$. Por tanto

$$ikA - ikB = i\bar{k}C \quad \Rightarrow \quad A - B = \frac{\bar{k}}{k} C. \qquad \text{(2.6)}$$

Resolviendo $B$ y $C$ en términos de $A$, obtenemos

$$\frac{B}{A} = \frac{k - \bar{k}}{k + \bar{k}}, \qquad \frac{C}{A} = \frac{2k}{k + \bar{k}}. \qquad \text{(2.7)}$$

Si $A$ es real, $B$ y $C$ son reales. Para $E = V_0$, tenemos $\bar{k} = 0$ y las ecuaciones (2.7) dan $B = A$ y $C = 2A$. Por tanto, para $E = V_0$ el estado propio de energía es

$$E = V_0: \qquad \psi(x) = \begin{cases} 2A \cos(kx), & x < 0, \\ 2A, & x > 0, \end{cases} \qquad \text{(2.8)}$$

y tiene el siguiente aspecto:

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes16_ES/fig3.png)

Figura 3: Estado propio de energía para $E = V_0$.

Obtenemos mayor comprensión de la solución evaluando la corriente de probabilidad a la izquierda y a la derecha del escalón en $x = 0$. Recordemos la forma de la corriente de probabilidad para una función de onda $\psi$:

$$J = \operatorname{Im}\left(\psi^* \frac{\hbar}{m} \frac{\partial \psi}{\partial x}\right) \qquad \text{(2.9)}$$

Un cálculo breve muestra que la corriente $J_L$ a la izquierda del escalón es

$$J_L = \frac{\hbar k}{m}\left(|A|^2 - |B|^2\right) = J_A - J_B, \qquad J_A = \frac{\hbar k}{m}|A|^2, \qquad J_B = \frac{\hbar k}{m}|B|^2. \qquad \text{(2.10)}$$

No hay interferencia entre la onda incidente y la reflejada. La corriente total a la izquierda del escalón es simplemente la corriente $J_A$ asociada a la onda incidente menos la corriente $J_B$ asociada a la onda reflejada. La corriente $J_R$ a la derecha del escalón es

$$J_R = \frac{\hbar \bar{k}}{m}|C|^2 = J_C. \qquad \text{(2.11)}$$

En cualquier solución estacionaria no puede haber acumulación de probabilidad en ninguna región del espacio porque la densidad de probabilidad $\rho$ es manifiestamente independiente del tiempo. Aunque la probabilidad fluye continuamente en las soluciones de dispersión, debe conservarse. A partir de la ecuación de conservación $\dfrac{\partial J}{\partial x} + \dfrac{\partial \rho}{\partial t} = 0$, la independencia temporal de $\rho$ implica que la corriente $J$ debe ser independiente de $x$. En particular, nuestra solución (2.7) debe implicar que $J_L = J_R$. Verifiquémoslo:

$$\begin{aligned}
J_L &= \frac{\hbar k}{m}\left(|A|^2 - |B|^2\right) = \frac{\hbar k}{m}\left(1 - \left(\frac{k - \bar{k}}{k + \bar{k}}\right)^2\right)|A|^2\\
&= \frac{\hbar k}{m}\frac{4k\bar{k}}{(k+\bar{k})^2}|A|^2 = \frac{\hbar \bar{k}}{m}\underbrace{\frac{4k^2}{(k+\bar{k})^2}|A|^2}_{|C|^2} = \frac{\hbar \bar{k}}{m}|C|^2 = J_R, \qquad \text{(2.12)}
\end{aligned}$$

como se esperaba. La igualdad de $J_L$ y $J_R$ implica que

$$J_A - J_B = J_C \quad \Rightarrow \quad J_A = J_B + J_C \quad \Rightarrow \quad 1 = \frac{J_B}{J_A} + \frac{J_C}{J_A}. \qquad \text{(2.13)}$$

Definimos ahora el coeficiente de reflexión $R$ como el cociente entre el flujo de probabilidad en la onda reflejada y el flujo de probabilidad en la onda entrante:

$$R \equiv \frac{J_B}{J_A} = \frac{|B|^2}{|A|^2} = \left(\frac{k - \bar{k}}{k + \bar{k}}\right)^2 \leq 1. \qquad \text{(2.14)}$$

Este cociente resulta ser el módulo al cuadrado del cociente $B/A$, y es manifiestamente menor que uno, como debe ser. Definimos también el coeficiente de transmisión $T$ como el cociente entre el flujo de probabilidad en la onda transmitida y el flujo de probabilidad en la onda entrante:

$$T \equiv \frac{J_C}{J_A} = \frac{\bar{k}\,|C|^2}{k\,|A|^2} = \frac{\bar{k}}{k}\frac{4k^2}{(k+\bar{k})^2} = \frac{4k\bar{k}}{(k+\bar{k})^2}. \qquad \text{(2.15)}$$

Las definiciones anteriores son razonables porque $R$ y $T$, dados en términos de cocientes de corrientes, suman uno:

$$R + T = 1, \qquad \text{(2.16)}$$

como se deduce por inspección de (2.13). Nótese que $T \neq |C|^2/|A|^2$ porque los números de onda a la derecha y a la izquierda del escalón no son iguales.

Recordemos que para $E = V_0$ encontramos $\bar{k} = 0$. En ese caso tenemos reflexión total: $R = 1$ y $T = 0$. En efecto, la corriente de probabilidad asociada a la función de onda constante que existe para $x > 0$ (véase (2.8)) es cero. Adicionalmente podemos dar un argumento de continuidad. Los coeficientes $R$ y $T$ deben ser funciones continuas de la energía $E$. Para $E < V_0$ esperamos $T = 0$ ya que la región prohibida es todo $x > 0$ y una función de onda que decae exponencialmente no puede transportar flujo de probabilidad. Si $T = 0$ para cualquier $E < V_0$, debe seguir siendo cero para $E = V_0$, por continuidad.

## 3. Potencial escalón con $E < V_0$

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes16_ES/fig4.png)

Figura 4: La barrera del potencial escalón.

Cuando $E < V_0$ la región $x > 0$ es una región clásicamente prohibida. Intentemos resolver el estado propio de energía sin rehacer todo el trabajo involucrado en resolver $B$ y $C$ en términos de $A$. Para este propósito notamos primero que el ansatz (2.3) para $x < 0$ puede quedar sin cambios. Por otro lado, para $x > 0$ la solución anterior

$$\psi(x) = C e^{i\bar{k}x}, \qquad \bar{k}^2 = \frac{2m(E - V_0)}{\hbar^2}, \qquad \text{(3.17)}$$

debe convertirse en una exponencial decreciente

$$\psi(x) = C e^{-\kappa x}, \qquad \kappa^2 = \frac{2m(V_0 - E)}{\hbar^2}. \qquad \text{(3.18)}$$

Notamos que la primera se convierte en la segunda mediante la sustitución

$$\bar{k} \to i\kappa. \qquad \text{(3.19)}$$

Esto significa que podemos simplemente realizar esta sustitución en nuestras expresiones anteriores para $B/A$ y $C/A$ y obtenemos las nuevas expresiones. En particular, a partir de (2.7) obtenemos

$$\frac{B}{A} = \frac{k - i\kappa}{k + i\kappa} \qquad \text{(3.20)}$$

Por tanto

$$\frac{B}{A} = \frac{i(k - i\kappa)}{i(k+i\kappa)} = -\frac{\kappa + ik}{\kappa - ik} = -e^{2i\delta(E)}, \qquad \text{(3.21)}$$

con

$$\delta(E) = \tan^{-1}\left(\frac{k}{\kappa}\right) = \tan^{-1}\sqrt{\frac{E}{V_0 - E}}. \qquad \text{(3.22)}$$

Dado que el módulo de $A$ es igual al módulo de $B$, tenemos $J_A = J_B$ y $J_C = 0$. Por tanto $T = 0$ y $R = 1$. Como se señaló antes, el cociente $B/A$ es una fase pura. La fase del numerador $\kappa + ik$ es $\delta(E)$ y la fase del denominador $\kappa - ik$ es $-\delta(E)$, dando así la fase total $2\delta(E)$ para el cociente. No absorbimos el signo negativo en la fase; de esta manera $\delta(E) \to 0$ cuando $E \to 0$. Nótese que $\delta(E)$ es positiva y no excede $\pi/2$. De hecho, un esquema de $\delta(E)$ se muestra en la Figura 5.

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes16_ES/fig5.png)

Figura 5: La fase $\delta(E)$ en función de la energía $E < V_0$.

La función de onda total para $x < 0$ es interesante:

$$\begin{aligned}
\psi(x) &= A e^{ikx} + (-A e^{2i\delta(E)}) e^{-ikx} \\
&= A e^{i\delta(E)}\left(e^{-i\delta(E)} e^{ikx} - e^{i\delta(E)} e^{-ikx}\right) \\
&= 2iA e^{i\delta(E)} \sin(kx - \delta(E))
\end{aligned} \qquad \text{(3.23)}$$

Esto significa que la densidad de probabilidad es

$$|\psi|^2 = 4A^2 \sin^2(kx - \delta(E)). \qquad \text{(3.24)}$$

El punto $x_0 > 0$ determinado por la condición $kx_0 = \delta(E)$ es el punto en la región prohibida donde se anularía la extrapolación de la solución de la región permitida. Por supuesto, en la región prohibida $x > 0$, la densidad de probabilidad $|\psi|^2$ es una exponencial decreciente.

![Figura 6](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes16_ES/fig6.png)

Figura 6: Norma al cuadrado del estado propio de energía cuando $E < V_0$. Para $x > 0$ la densidad de probabilidad decae exponencialmente con $x$. El punto $x_0$ es el punto donde se anularía la extrapolación de la densidad de probabilidad de $x < 0$.

Para uso posterior registramos la derivada de la fase $\delta(E)$ respecto de la energía

$$\delta'(E) \equiv \frac{d\delta(E)}{dE} = \frac{1}{2}\sqrt{\frac{1}{E(V_0 - E)}}. \qquad \text{(3.25)}$$

Nótese que esta derivada se hace infinita tanto para $E \to 0$ como para $E \to V_0$.

![Figura 7](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes16_ES/fig7.png)

Figura 7: La derivada $\delta'(E)$ en función de la energía $E < V_0$.

## 4. Paquetes de onda en el potencial escalón

Examinamos ahora el escenario más físico. Como hemos visto con la partícula libre, los estados estacionarios no son normalizables, y las partículas físicas se representan en realidad mediante paquetes de onda construidos con una superposición infinita de estados propios de momento. Podemos hacer algo similar con nuestros estados propios de energía. Consideraremos estados propios de energía con $E > V_0$, o equivalentemente con $k^2 > \hat{k}^2$, donde

$$k^2 = \frac{2mE}{\hbar^2} > \frac{2mV_0}{\hbar^2} \equiv \hat{k}^2, \qquad \text{(4.26)}$$

y los superpondremos. Para comenzar escribimos los estados propios de energía en una forma ligeramente distinta, incluyendo la dependencia temporal. Fijando $A = 1$ y usando los valores de los cocientes $B/A$ y $C/A$, encontramos la solución

$$\Psi(x,t) = \begin{cases} \left(e^{ikx} + \dfrac{k - \bar{k}}{k + \bar{k}} e^{-ikx}\right) e^{-iE(k)t/\hbar}, & x < 0, \\[2mm] \dfrac{2k}{k + \bar{k}} e^{i\bar{k}x} e^{-iE(k)t/\hbar}, & x > 0. \end{cases} \qquad \text{(4.27)}$$

Podemos formar una superposición de estas soluciones multiplicando por una función $f(k)$ e integrando sobre $k$:

$$\Psi(x,t) = \begin{cases} \displaystyle\int_{\hat{k}}^{\infty} dk\, f(k) \left(e^{ikx} + \dfrac{k - \bar{k}}{k + \bar{k}} e^{-ikx}\right) e^{-iE(k)t/\hbar}, & x < 0, \\[3mm] \displaystyle\int_{\hat{k}}^{\infty} dk\, f(k) \dfrac{2k}{k + \bar{k}} e^{i\bar{k}x} e^{-iE(k)t/\hbar}, & x > 0. \end{cases} \qquad \text{(4.28)}$$

Aquí $f(k)$ es una función real de $k$ que es esencialmente cero excepto por un pico estrecho en $k = k_0$. Nótese que solo hemos incluido componentes de momento con energía mayor que $V_0$ fijando el límite inferior de la integral igual a $\hat{k}$. La integral solo se extiende sobre $k$ positivo porque solo en ese caso las ondas $e^{ikx}$ se mueven hacia $x$ positivo, y son por tanto ondas incidentes genuinas. Lo anterior está garantizado que sea una solución de la ecuación de Schrödinger.

Podemos dividir la solución en ondas incidente, reflejada y transmitida, como sigue.

$$\Psi(x,t) = \begin{cases} \Psi_{\text{inc}}(x,t) + \Psi_{\text{ref}}(x,t), & x < 0, \\ \Psi_{\text{trans}}(x,t), & x > 0. \end{cases} \qquad \text{(4.29)}$$

Naturalmente, tanto $\Psi_{\text{inc}}(x,t)$ como $\Psi_{\text{ref}}(x,t)$ existen para $x < 0$ y $\Psi_{\text{trans}}(x,t)$ existe para $x > 0$. Tenemos entonces, explícitamente,

$$\Psi_{\text{inc}}(x<0,t) = \int_{\hat{k}}^{\infty} dk\, f(k) e^{ikx} e^{-iE(k)t/\hbar},$$

$$\Psi_{\text{ref}}(x<0,t) = \int_{\hat{k}}^{\infty} dk\, f(k) \left(\frac{k - \bar{k}}{k + \bar{k}}\right) e^{-ikx} e^{-iE(k)t/\hbar}, \qquad \text{(4.30)}$$

$$\Psi_{\text{trans}}(x>0,t) = \int_{\hat{k}}^{\infty} dk\, f(k) \left(\frac{2k}{k + \bar{k}}\right) e^{i\bar{k}x} e^{-iE(k)t/\hbar}.$$

¿Cómo se mueve el pico de $\Psi_{\text{inc}}(x,t)$? Para esto buscamos la contribución principal a la integral asociada, que ocurre cuando la fase total en el integrando es estacionaria para $k \approx k_0$. Requerimos por tanto

$$\frac{d}{dk}\left(kx - \frac{\hbar^2 k^2}{2m}\frac{t}{\hbar}\right)\bigg|_{k_0} = 0 \quad \Rightarrow \quad x - \frac{\hbar k_0}{m} t = 0 \quad \Rightarrow \quad x = \frac{\hbar k_0}{m} t. \qquad \text{(4.31)}$$

Esta es la relación entre $t$ y $x$ que satisface el pico de $\Psi_{\text{inc}}$. Describe un pico que se mueve con velocidad constante $\hbar k_0/m > 0$. Dado que $\Psi_{\text{inc}}(x,t)$ requiere que $x < 0$, la condición anterior muestra que obtenemos el pico solo para $t < 0$. El pico del paquete llega a $x = 0$ en $t = 0$. Para $t > 0$, $\Psi_{\text{inc}}(x,t)$ no es cero, pero debe ser bastante pequeño, ya que la condición de fase estacionaria no puede satisfacerse para ningún $x$ en el dominio $x < 0$.

Consideremos ahora $\Psi_{\text{ref}}(x,t)$. Esta vez la condición de fase estacionaria es

$$\frac{d}{dk}\left(-kx - \frac{\hbar^2 k^2}{2m}\frac{t}{\hbar}\right)\bigg|_{k_0} = 0 \quad \Rightarrow \quad x + \frac{\hbar k_0}{m} t = 0 \quad \Rightarrow \quad x = -\frac{\hbar k_0}{m} t. \qquad \text{(4.32)}$$

La relación representa un pico que se mueve con velocidad constante negativa $-\hbar k_0/m$. Dado que $\Psi_{\text{ref}}(x,t)$ requiere que $x < 0$, la condición anterior muestra que obtenemos el pico solo para $t > 0$, como corresponde a una onda reflejada. Para $t > 0$, $\Psi_{\text{ref}}(x,t)$ no es cero, pero debe ser bastante pequeño, ya que la condición de fase estacionaria no puede satisfacerse para ningún $x$ en el dominio $x < 0$.

Finalmente, consideremos $\Psi_{\text{trans}}$. La condición de fase estacionaria dice:

$$\frac{d}{dk}\left(\bar{k}x - \frac{\hbar^2 k^2}{2m}\frac{t}{\hbar}\right)\bigg|_{k_0} = 0 \quad \Rightarrow \quad \frac{d\bar{k}}{dk}\bigg|_{k_0} x - \frac{\hbar k_0}{m} t = 0 \qquad \text{(4.33)}$$

Usando

$$\bar{k}^2 = k^2 - \frac{2mV_0}{\hbar^2} \quad \Rightarrow \quad \frac{d\bar{k}}{dk} = \frac{k}{\bar{k}}, \qquad \text{(4.34)}$$

y volviendo a la ecuación anterior encontramos rápidamente que

$$\text{Pico de la onda transmitida:} \qquad x = \frac{\hbar \bar{k}}{m} t, \qquad \text{(4.35)}$$

con $\bar{k}$ evaluado en $k = k_0$. Dado que $x > 0$ es el dominio de $\Psi_{\text{trans}}$, esto describe un pico que se mueve hacia la derecha con velocidad $\hbar \bar{k}/m$ para $t > 0$. Para $t < 0$, $\Psi_{\text{trans}}(x,t)$ no es cero, pero debe ser bastante pequeño, ya que la condición de fase estacionaria no puede satisfacerse para ningún $x$ en el dominio $x > 0$.

En resumen, para tiempos muy negativos $\Psi_{\text{inc}}$ domina y tanto $\Psi_{\text{ref}}$ como $\Psi_{\text{trans}}$ son muy pequeños. Para tiempos muy positivos, tanto $\Psi_{\text{ref}}$ como $\Psi_{\text{trans}}$ dominan y $\Psi_{\text{inc}}$ se hace muy pequeño. Estas situaciones se esquematizan en las figuras 8 y 9. Por supuesto, para tiempos pequeños, positivos o negativos, las tres ondas existen y juntas describen el complejo proceso de colisión con el escalón en el que se generan una onda reflejada y una onda transmitida.

![Figura 8](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes16_ES/fig8.png)

Figura 8: En tiempos muy negativos un paquete de onda entrante viaja en la dirección $+x$.

![Figura 9](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes16_ES/fig9.png)

Figura 9: En tiempos muy positivos tenemos un paquete de onda reflejado que viaja en la dirección $-\hat{x}$ y el paquete de onda transmitido que viaja en la dirección $+\hat{x}$.

Examinemos ahora un paquete de onda construido con energías $E < V_0$. Recordemos que en esta situación $B/A = -e^{2i\delta(E)}$. Por tanto, para una onda incidente, cuyas componentes de momento tienen todas energía menor que $V_0$,

$$\Psi_{\text{inc}}(x<0,t) = \int_0^{\hat{k}} dk\, f(k) e^{ikx} e^{-iEt/\hbar}, \qquad \text{(4.36)}$$

la función de onda reflejada asociada es

$$\Psi_{\text{ref}}(x<0,t) = -\int_0^{\hat{k}} dk\, f(k)\, e^{2i\delta(E)} e^{-ikx} e^{-iEt/\hbar}. \qquad \text{(4.37)}$$

Usando de nuevo el método de la fase estacionaria para encontrar la evolución del pico,

$$\frac{d}{dk}\left(2\delta(E) - kx - \frac{Et}{\hbar}\right)\bigg|_{k_0} = 0 \quad \Rightarrow \quad 2\delta'(E)\frac{\hbar^2 k_0}{m} - x - \frac{\hbar k_0 t}{m} = 0. \qquad \text{(4.38)}$$

De aquí encontramos rápidamente

$$x = -\frac{\hbar k_0}{m}\left(t - 2\hbar\, \delta'(E)\right), \qquad \text{(4.39)}$$

donde la derivada se evalúa en $E(k_0)$. El paquete de onda reflejado se mueve hacia valores más negativos de $x$ a medida que el tiempo crece positivamente. Esto es como debe ser. Pero hay un retraso temporal asociado al paquete reflejado, evidente al comparar la ecuación anterior con $x = -\dfrac{\hbar k_0}{m} t$. El retraso temporal viene dado por

$$\text{retraso temporal} = 2\hbar\, \delta'(E). \qquad \text{(4.40)}$$

La derivada $\delta'(E)$ fue evaluada en (3.25) y es positiva. Vemos que el retraso es particularmente grande para paquetes de onda de poca energía o para aquellos con energías justo por debajo de $V_0$.

Concluimos el análisis del potencial escalón discutiendo qué significa observar la partícula en la región prohibida. Sería contradictorio que el observador pudiera hacer las dos afirmaciones siguientes:

1.  La partícula está localizada en la región prohibida.
2.  La partícula tiene energía menor que $V_0$.

Ambas afirmaciones, tomadas como válidas simultáneamente, implicarían que la partícula tiene energía cinética negativa, algo inconsistente. En particular, con $E < V_0$ tendríamos una energía cinética negativa de magnitud $V_0 - E$.

![Figura 10](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes16_ES/fig10.png)

Figura 10: El potencial escalón con energía potencial $V_0$. Si pudiéramos observar una partícula en la región prohibida con energía $E$, entonces la energía cinética sería negativa.

Notemos primero que en la solución la partícula penetra en la región prohibida una distancia de aproximadamente $1/\kappa$, donde, recordemos,

$$\kappa^2 = \frac{2m(V_0 - E)}{\hbar^2}. \qquad \text{(4.41)}$$

Para asegurar que la partícula esté en la región prohibida, su incertidumbre de posición $\Delta x$ debe ser menor que la profundidad de penetración:

$$\Delta x \leq \frac{1}{\kappa}. \qquad \text{(4.42)}$$

La partícula adquiere cierto momento $p$ debido a la medición de posición:

$$p \geq \frac{\hbar}{\Delta x} \geq \hbar \kappa. \qquad \text{(4.43)}$$

Debido a este momento inducido por la medición de posición, hay alguna contribución adicional $E'$ a la energía cinética

$$E' = \frac{p^2}{2m} \geq \frac{\hbar^2 \kappa^2}{2m} = V_0 - E, \qquad \text{(4.44)}$$

donde usamos (4.41). A partir de esta desigualdad encontramos que la energía total excederá $V_0$

$$E_{\text{tot}} = E + E' \geq E + (V_0 - E) = V_0. \qquad \text{(4.45)}$$

Aunque el argumento es heurístico, aporta cierta evidencia de que no se detectará energía cinética negativa para una partícula que se encuentre en la región prohibida.

*Sarah Geller transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare https://ocw.mit.edu

8.04 Física Cuántica I Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

# Apéndice: Lista de problemas 7 (Problem Set 7, 2016)

**Física Cuántica I (8.04), Primavera de 2016**

**Tarea 7**

Departamento de Física del MIT — Entrega: viernes 8 de abril de 2016, 12:00 del mediodía

1 de abril de 2016

**Lectura:** Griffiths, secciones 2.5 y 2.3.

## Problema 1

**Dos funciones delta** \[15 puntos\]

Considere una partícula de masa $m$ moviéndose en un potencial de doble pozo unidimensional

$$V(x) = -g\,\delta(x - a) - g\,\delta(x + a), \qquad g > 0.$$

1.  Encuentre las ecuaciones trascendentes para los valores propios de energía de los estados ligados del sistema. Represente gráficamente los niveles de energía en unidades de $\hbar^2/(ma^2)$ en función del parámetro adimensional $\lambda \equiv mag/\hbar^2$. Explique las características de la gráfica.

2.  En el límite de gran separación $2a$ entre los pozos, encuentre una fórmula sencilla para el desdoblamiento (splitting) entre el estado fundamental y el primer estado excitado.

## Problema 2

**Esbozando funciones de onda.** Griffiths 2.47, p. 87. \[10 puntos\]

En este problema debe intentar averiguar intuitivamente el aspecto de las soluciones. Es buena idea comprobar después su intuición con el método de disparo (shooting method) y el planteamiento del ion H$_2^+$.

## Problema 3

**Osciladores armónicos más allá de los puntos de retorno** \[10 puntos\]

Para los estados propios de energía del oscilador armónico simple con $n = 0, 1$ y $2$, calcule la probabilidad de que la coordenada $x$ tome un valor mayor que la amplitud de un oscilador clásico de la misma energía.

## Problema 4

**Cálculos con el oscilador armónico** \[15 puntos\]

1.  Calcule el valor esperado de $x^4$ en el estado propio de energía con número $n$.

2.  Calcule $\Delta x$ y $\Delta p$ en el estado propio de energía con número $n$. ¿Cuál es el valor del producto $\Delta x \, \Delta p$?

3.  Considere los polinomios $H_n(\xi)$ definidos por la función generatriz

$$e^{-s^2 + 2s\xi} = \sum_{n=0}^{\infty} H_n(\xi) \frac{s^n}{n!}.$$

Verifique que $H_n(\xi) = (2\xi)^n + \ldots$, donde los puntos suspensivos representan términos con potencias menores de $\xi$. Demuestre que los polinomios $H_n(\xi)$ así definidos satisfacen la ecuación diferencial de Hermite:

$$H_n'' - 2\xi H_n' + 2n H_n = 0.$$

## Problema 5

**Oscilador armónico y una pared.** Problema 2.42 de Griffiths, p. 86. \[5 puntos\]

## Problema 6

**¡El oscilador armónico oscilando!** \[10 puntos\]

Una partícula de masa $m$ en un oscilador armónico de frecuencia $\omega$ tiene una función de onda inicial, en el instante cero,

$$\Psi(x,0) = \frac{1}{\sqrt{2}}\Big(\varphi_0(x) + \varphi_1(x)\Big),$$

donde $\varphi_0$ y $\varphi_1$ son los estados propios normalizados del hamiltoniano con número propio cero y uno, respectivamente.

1.  Escriba $\Psi(x,t)$ y $|\Psi(x,t)|^2$. Puede dejar sus expresiones en términos de $\varphi_0$ y $\varphi_1$.

2.  Encuentre $\langle x \rangle$ en función del tiempo. ¿Cuál es la amplitud de esta oscilación y cuál es su frecuencia?

3.  Encuentre $\langle p \rangle$ en función del tiempo.

4.  Demuestre que, para cualquier estado del oscilador armónico, la distribución de probabilidad $|\Psi(x,t)|^2$ es igual a $|\Psi(x,t+T)|^2$ para $T = \dfrac{2\pi}{\omega}$.

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*


---

<!-- MIT8.04_LecNotes17_ES.md -->

# Capítulo 17: Transmisión resonante y efecto Ramsauer–Townsend

## Vídeos de esta clase (YouTube)

**Lección 17: Ramsauer-Townsend effect. Scattering in 1D.**

- [Waves on the finite square well](https://www.youtube.com/watch?v=EdRkQmmq7vk)
- [Resonant transmission](https://www.youtube.com/watch?v=KkSr0SvXfNY)
- [Ramsauer-Townsend phenomenology](https://www.youtube.com/watch?v=5u-9lFhCl5w) (10:16)
- [Scattering in 1D. Incoming and outgoing waves](https://www.youtube.com/watch?v=twdF0EIbFds)
- [Scattered wave and phase shift](https://www.youtube.com/watch?v=w49WAat6ymk)

------------------------------------------------------------------------

*B. Zwiebach* *26 de abril de 2016*

## Contenido

1.  Transmisión resonante en un pozo cuadrado
2.  El efecto Ramsauer–Townsend

## 1. Transmisión resonante en un pozo cuadrado

Consideremos el pozo cuadrado finito

$$V(x) =
\begin{cases}
0, & \text{para } |x| > a, \\
-V_0, & \text{para } |x| < a.
\end{cases}
\qquad \text{(1.1)}$$

Aquí $V_0 > 0$ tiene unidades de energía. Consideramos un autoestado de energía, una solución de dispersión con $E > 0$ que representa una función de onda incidente que se aproxima al pozo desde la izquierda. Un ansatz para el autoestado tendrá la forma

$$\psi(x) =
\begin{cases}
Ae^{ikx} + Be^{-ikx}, & x < -a, \\
Ce^{ik_2 x} + De^{-ik_2 x}, & |x| < a, \\
Fe^{ikx}, & x > a.
\end{cases}
\qquad \text{(1.2)}$$

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes17_ES/fig1.png)

Figura 1: El pozo cuadrado con todas las ondas relevantes representadas; la onda con coeficiente $A$ incide desde la izquierda.

Aquí $A$ es el coeficiente de la onda incidente que existe para $x < -a$, y $B$ es el coeficiente de la onda reflejada (véase la Figura 1). Ambas ondas tienen número de onda $k$. En la región del pozo $|x| < a$ tenemos una onda que se mueve hacia la derecha, con coeficiente $C$, y una onda que se mueve hacia la izquierda, con coeficiente $D$. El número de onda en esta región se denomina $k_2$. A la derecha del pozo tenemos solo una onda, que se mueve hacia la derecha, con coeficiente $F$ y número de onda $k$. Nótese que, aunque el potencial es una función par de $x$, un autoestado de energía no normalizable no tiene por qué ser par ni impar. La simetría se rompe por la condición de que la onda incide desde la izquierda. Los valores de $k$ y $k_2$, ambos positivos, quedan determinados por la ecuación de Schrödinger y son

$$k^2 = \frac{2mE}{\hbar^2}, \qquad k_2^2 = \frac{2m(E + V_0)}{\hbar^2}. \qquad \text{(1.3)}$$

Hay cuatro condiciones de contorno: continuidad de $\psi$ y $\psi'$ en $x = -a$ y en $x = a$. Estas cuatro ecuaciones pueden usarse para fijar los coeficientes $B$, $C$, $D$ y $F$ en términos de $A$. Definimos los coeficientes de reflexión y transmisión $R$ y $T$ de la siguiente manera:

$$R \equiv \frac{|B|^2}{|A|^2}, \qquad T \equiv \frac{|F|^2}{|A|^2}. \qquad \text{(1.4)}$$

De la conservación de la corriente de probabilidad sabemos que las corrientes a la izquierda y a la derecha del pozo deben ser iguales, de modo que

$$|A|^2 - |B|^2 = |F|^2. \qquad \text{(1.5)}$$

Esta no es una ecuación independiente; debe deducirse de las condiciones de contorno. Implica que

$$R + T = \frac{|B|^2}{|A|^2} + \frac{|F|^2}{|A|^2} = 1, \qquad \text{(1.6)}$$

lo que muestra que nuestra definición de $R$ y $T$ tiene sentido.

Resolver para $R$ y $T$ es directo pero un poco laborioso. Citemos simplemente el resultado que se obtiene. El coeficiente de transmisión es la siguiente función de la energía $E$ del autoestado:

$$\frac{1}{T} = 1 + \frac{1}{4}\frac{V_0^2}{E(E+V_0)}\sin^2(2k_2 a). \qquad \text{(1.7)}$$

Dado que el segundo término del lado derecho es manifiestamente positivo, tenemos $T \le 1$. Cuando $E \to 0$, tenemos $\frac{1}{T} \to 1 + \infty$, lo que significa que $T \to 0$. Cuando $E \to \infty$, tenemos $T \to 1$.

Podemos eliminar todas las unidades de este resultado definiendo

$$e \equiv \frac{E}{V_0}, \qquad z_0^2 \equiv \frac{2ma^2 V_0}{\hbar^2}. \qquad \text{(1.8)}$$

Entonces,

$$(k_2 a)^2 = \frac{2ma^2(E+V_0)}{\hbar^2} = \frac{2ma^2 V_0}{\hbar^2}(1+e) \;\; \to \;\; 2k_2 a = 2z_0\sqrt{1+e}, \qquad \text{(1.9)}$$

de modo que tenemos

$$\frac{1}{T} = 1 + \frac{1}{4e(1+e)}\sin^2\!\left(2z_0\sqrt{1+e}\right). \qquad \text{(1.10)}$$

Ahora podemos ver que el pozo se vuelve transparente, haciendo $T = 1$, para ciertos valores de la energía. Todo lo que necesitamos es que el argumento de la función seno sea un múltiplo de $\pi$:

$$2z_0\sqrt{1+e} = n\pi, \quad n \in \mathbb{Z}. \qquad \text{(1.11)}$$

No todos los enteros están permitidos. Como $e > 0$, el lado izquierdo es mayor o igual que $2z_0$ y, por lo tanto,

$$n \ge \frac{2z_0}{\pi}. \qquad \text{(1.12)}$$

Llamemos $E_n = e_n V_0$ a las energías asociadas. Entonces

$$e_n + 1 = \frac{n^2\pi^2}{4z_0^2} = \frac{n^2\pi^2\hbar^2}{2m(2a)^2 V_0}, \qquad \text{(1.13)}$$

de modo que

$$E_n + V_0 = \frac{n^2\pi^2\hbar^2}{2m(2a)^2}. \qquad \text{(1.14)}$$

Nótese que $E_n + V_0$ es la energía del estado de dispersión medida respecto al fondo del pozo cuadrado. El lado derecho es la energía del $n$-ésimo estado ligado del pozo cuadrado infinito de anchura $2a$. Obtenemos así un resultado bastante sorprendente: obtenemos transmisión total para aquellas energías $E_n > 0$ que están en el espectro de la extensión de pozo cuadrado infinito de nuestro pozo cuadrado finito. La desigualdad $n \ge \frac{2z_0}{\pi}$ garantiza que $E_n > 0$. Dado que los estados ligados del pozo cuadrado infinito se caracterizan por ajustar un número entero de semilongitudes de onda, tenemos una situación de tipo resonancia en la que la transmisión perfecta ocurre cuando las ondas de dispersión encajan perfectamente dentro del pozo cuadrado finito. El fenómeno que hemos observado se denomina ¡transmisión resonante!

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes17_ES/fig2.png)

Figura 2: Obtenemos transmisión resonante a través del pozo finito en las energías de estado ligado positivas de un supuesto pozo infinito.

El ajuste de un número exacto de semilongitudes de onda también puede verse directamente a partir de la anulación de la función seno en (1.7), que da $k_2(2a) = n\pi$, lo que implica

$$\frac{2\pi}{\lambda}(2a) = n\pi \;\; \to \;\; 2a = n\,\frac{\lambda}{2}. \qquad \text{(1.15)}$$

Mostramos en la Figura 3 el coeficiente de transmisión $T$ en función de $e = E/V_0$ para un pozo cuadrado con $z_0 = 13\pi/4$. En este caso debemos tener $n \ge \frac{13}{2}$, es decir, $n \ge 7$.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes17_ES/fig3.png)

Figura 3: El coeficiente de transmisión $T$ en función de $e$ para un pozo cuadrado con $z_0 = 13\pi/4$. En las energías en las que $T = 1$ tenemos dispersión resonante. Los valores de $E_7, E_8, \ldots$ se indican en la figura. Hay tres casos de transmisión resonante para $0 < E < V_0$. Nótese que el espaciado entre los puntos donde $T = 1$ crece a medida que $e$ crece.

## 2. El efecto Ramsauer–Townsend

Carl Ramsauer y John Sealy Townsend publicaron por separado sus investigaciones en 1921. Estaban estudiando la dispersión elástica de electrones de baja energía por átomos de gases nobles. Estos gases tienen sus capas electrónicas completamente llenas y son a la vez muy poco reactivos y poseen altas energías de ionización. El potencial es creado por el núcleo y se hace visible a medida que el electrón incidente penetra en la nube electrónica. Este potencial es un potencial atractivo esféricamente simétrico para los electrones: una especie de pozo esférico finito. En el experimento, algunos electrones colisionan con los átomos y se dispersan, la mayoría rebotando hacia atrás. ¡Podemos así considerar el coeficiente de reflexión $R$ como un indicador (proxy) de la sección eficaz de dispersión!

Ramsauer y Townsend reportaron un fenómeno muy inusual. A energías muy bajas, la sección eficaz de dispersión era alta. Pero la dependencia con la energía resultaba sorprendente. A medida que la energía aumentaba, la dispersión disminuía hasta acercarse a cero, para volver a aumentar cuando la energía se incrementaba aún más. Tal comportamiento misterioso no tenía una explicación clásica razonable. Lo que está en juego es la dispersión resonante cuántica. ¡Que la sección eficaz tienda a cero significa que el coeficiente de reflexión tiende a cero, y el coeficiente de transmisión tiende a uno! La primera transmisión resonante ocurre para electrones de alrededor de un electronvoltio (tales electrones tienen una velocidad de aproximadamente 600 km/s). La Figura 4 proporciona un esquema tanto de $R$ como de $T$ en función de la energía. Nuestro potencial de pozo cuadrado unidimensional no proporciona una buena correspondencia cuantitativa con los datos, pero ilustra el fenómeno físico. Se necesita un pozo cuadrado esférico tridimensional para un análisis cuantitativo.

*Andrew Turner transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes17_ES/fig4.png)

Figura 4: Los coeficientes de reflexión y transmisión en función de la energía para el efecto Ramsauer–Townsend. Nótese que $R + T = 1$. En la flecha, tenemos $R = 0$, por lo que no hay dispersión. ¡Todos los electrones pasan directamente a través de los átomos del gas noble! Experimentan transmisión resonante. Esto ocurre por primera vez alrededor de 1 eV.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.*


---

<!-- MIT8.04_LecNotes18_ES.md -->

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


---

<!-- MIT8.04_LecNotes19_ES.md -->

# Teorema de Levinson y Resonancias

## Vídeos de esta clase (YouTube)

**Lección 19: Resonances and Breit-Wigner distribution. The complex k-plane.**

- [Time delay and resonances](https://www.youtube.com/watch?v=mnvYIEbJXlM)
- [Effects of resonance on phase shifts, wave amplitude and time delay](https://www.youtube.com/watch?v=VY-_xLxHQbA)
- [Modelling a resonance](https://www.youtube.com/watch?v=8Dxo4LPK_9w)
- [Half-width and time delay](https://www.youtube.com/watch?v=OQMczXtDnpU)
- [Resonances in the complex k plane](https://www.youtube.com/watch?v=0T83-47Vi-M)

------------------------------------------------------------------------

*B. Zwiebach* *28 de abril de 2016*

## 1. El teorema de Levinson

El teorema de Levinson relaciona el número $N_b$ de estados ligados de un potencial dado con la excursión del desfasaje $\delta(E)$ a medida que la energía va de cero a infinito:

$$N_b = \frac{1}{\pi}\left(\delta(0) - \delta(\infty)\right) . \qquad \text{(1.1)}$$

Para demostrar este resultado consideremos un potencial arbitrario $V(x)$ de alcance $R$, con una pared en $x = 0$. Este potencial, mostrado a la izquierda en la Figura 1, tiene un número de estados ligados, todos no degenerados, que pueden contarse. Existe también un conjunto de autoestados de energía positiva: los estados de dispersión que, al pertenecer a un continuo, no pueden contarse. Nuestra demostración requiere la posibilidad de contar estados, así que introduciremos una segunda pared infinita, colocada en $x = L$ para $L$ grande. Por supuesto, esto cambiará el espectro, pero a medida que $L$ se hace cada vez más grande los cambios se vuelven cada vez más pequeños. Pensamos en $L$ como un regulador del potencial que discretiza el espectro y así nos permite enumerar los estados. Lo hace porque, con dos paredes, el potencial se convierte en un pozo infinito ancho y todos los estados pasan a ser estados ligados. El potencial con la pared reguladora se muestra a la derecha en la Figura 1.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes19_ES/fig1.png)

Figura 1: Izquierda: un potencial unidimensional arbitrario $V(x)$ de alcance $R$. Derecha: el mismo potencial con una pared reguladora colocada en $x = L$.

La clave de la demostración será comparar el conteo de estados en el potencial regulado $V \neq 0$ con el conteo de estados en el potencial $V = 0$, también regulado con una segunda pared en $x = L$. Consideremos entonces el potencial regulado $V = 0$ y los autoestados de energía positiva. Estos corresponden a la función de onda $\phi(x) = \sin kx$, con la segunda pared exigiendo $\phi(x = L) = 0$. Así obtenemos

$$kL = n\pi, \quad \text{con } n = 1, 2, \ldots \qquad \text{(1.2)}$$

Los valores de $k$ están ahora cuantizados. Sea $dk$ un intervalo infinitesimal en el número de onda, con $dn$ el número de estados en $dk$ cuando $V = 0$. Así,

$$dk\, L = dn\, \pi \ \to \ dn = \frac{L}{\pi}\, dk . \qquad \text{(1.3)}$$

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes19_ES/fig2.png)

Figura 2: Con la pared reguladora el número de onda $k$ toma valores discretos. $dk$ es un intervalo infinitesimal en el espacio de $k$.

Cuando $V(x) \neq 0$, las soluciones para $x > R$, todas ellas soluciones de energía positiva, tienen la forma

$$\psi(x) = e^{i\delta} \sin(kx + \delta) . \qquad \text{(1.4)}$$

La condición de frontera $\psi(L) = 0$ implica una cuantización

$$kL + \delta(k) = n'\pi , \qquad \text{(1.5)}$$

con $n'$ entero. Podemos nuevamente diferenciar para determinar el número de estados de energía positiva $dn'$ en el intervalo $dk$, con $V \neq 0$:

$$dk\, L + \frac{d\delta}{dk}\, dk = dn'\, \pi \ \to \ dn' = \frac{L}{\pi}\, dk + \frac{1}{\pi}\frac{d\delta}{dk}\, dk . \qquad \text{(1.6)}$$

El número de soluciones de energía positiva que se pierden en el intervalo $dk$ al encender el potencial $V$ está dado por $dn - dn'$, que puede evaluarse usando (1.3) y (1.6):

$$dn - dn' = -\frac{1}{\pi}\frac{d\delta}{dk}\, dk . \qquad \text{(1.7)}$$

El número total de soluciones de energía positiva que se pierden a medida que se enciende el potencial $V$ está dado integrando la expresión anterior sobre todo el rango de $k$:

$$\begin{gathered}
\text{núm. de soluciones de energía positiva perdidas al encender } V\\
= -\int_0^{\infty} \frac{1}{\pi}\frac{d\delta}{dk}\, dk = -\frac{1}{\pi}\left(\delta(\infty) - \delta(0)\right) . \qquad \text{(1.8)}
\end{gathered}$$

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes19_ES/fig3.png)

Figura 3: Los estados de energía positiva de la configuración con V = 0 se desplazan al encender el potencial, y algunos pueden convertirse en estados ligados.

Aunque perdemos un número de soluciones de energía positiva al encender el potencial $V$, los estados no desaparecen. Al encender el potencial de manera continua desde cero hasta $V$, podemos seguir la pista de cada autoestado de energía y ¡ningún estado puede desaparecer! Si perdemos algunos estados de energía positiva, esos estados deben reaparecer ahora como estados de energía negativa, ¡es decir, estados ligados! Denotando con $N_b$ el número de estados ligados en el potencial $V \neq 0$, el resultado en (1.8) implica que

$$N_b = \frac{1}{\pi}\left(\delta(0) - \delta(\infty)\right) . \qquad \text{(1.9)}$$

¡Esto es lo que queríamos demostrar!

## 2. Resonancias

Hemos calculado el retraso temporal $\Delta t = 2\hbar\,\delta'(E)$ asociado al paquete de ondas reflejado que emerge de los potenciales de alcance $R$ que hemos considerado. Si el retraso temporal es negativo, el paquete de ondas reflejado emerge antes de tiempo. Podemos preguntar: ¿podemos obtener un retraso temporal negativo arbitrariamente grande? La respuesta es no. Un retraso temporal muy grande sería una violación de la causalidad. Significaría que el paquete entrante se refleja incluso antes de alcanzar $x = R$, lo cual es imposible. De hecho, el mayor retraso temporal negativo se realizaría (al menos clásicamente) si tuviéramos reflexión perfecta cuando el paquete entrante llega a $x = R$. Si esto ocurre, el retraso temporal sería $-\frac{2R}{v_0}$, donde $v_0$ es la velocidad del paquete. En efecto, $\frac{2R}{v_0}$ es el tiempo que se ahorra el paquete que no tuvo que entrar y salir del alcance. Así, esperamos

$$\text{retraso temporal} = 2\hbar\frac{d\delta}{dE} \ge -\frac{2R}{v_0} . \qquad \text{(2.1)}$$

Esto puede simplificarse un poco usando derivadas respecto a $k$

$$2\hbar\frac{d\delta}{dE} = 2\hbar\frac{1}{\frac{dE}{dk}}\frac{d\delta}{dk} = \frac{2}{v_0}\frac{d\delta}{dk} \ge -\frac{2R}{v_0} , \qquad \text{(2.2)}$$

lo que a su vez da la restricción

$$\frac{d\delta}{dk} \ge -R . \qquad \text{(2.3)}$$

El argumento no fue riguroso, pero el resultado es bastante preciso, recibiendo correcciones que se anulan para paquetes de energía grande.

Alternativamente, podemos preguntar: ¿podemos obtener un retraso temporal positivo arbitrariamente grande? La respuesta es sí. Esto puede ocurrir si el paquete de ondas queda temporalmente atrapado en el potencial. En ese caso esperaríamos que la amplitud de probabilidad se vuelva grande en la región $0 < x < R$. Si el paquete de ondas queda atrapado durante un tiempo largo tenemos una resonancia. El estado se parece un poco a un estado ligado en el sentido de que se localiza en el potencial, al menos por un tiempo. Para obtener una resonancia ayuda tener un potencial atractivo y una barrera de energía positiva. Podemos lograr esto con el potencial

$$V(x) =
\begin{cases}
\infty & \text{para } x \le 0 \\
-V_0 & \text{para } 0 < x < a \\
V_1 & \text{para } a < x < 2a \\
0 & \text{para } x > 2a .
\end{cases} \qquad \text{(2.4)}$$

El potencial, con $V_0, V_1 > 0$, se muestra en la Figura 4. Para tener una resonancia exploramos energías en el rango de cero a $V_1$. En ese rango de energías podemos esperar encontrar algunos valores particulares que conducen a un comportamiento resonante, es decir, gran retraso temporal y gran amplitud para la función de onda en el pozo.

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes19_ES/fig4.png)

Figura 4: Buscamos resonancias con energía $E$ en el rango $(0, V_1)$. En este rango la barrera $V_1$ produce una región clásicamente prohibida $x \in (a, 2a)$, que puede ayudar a localizar la amplitud alrededor del pozo.

Dadas las tres regiones relevantes en el potencial, definimos

$$k'^2 = \frac{2m(E + V_0)}{\hbar^2}, \qquad \kappa^2 = \frac{2m(V_1 - E)}{\hbar^2}, \qquad k^2 = \frac{2mE}{\hbar^2} . \qquad \text{(2.5)}$$

En la región $0 < x < a$ debemos usar funciones trigonométricas de $k'x$. En la región $a < x < 2a$ usamos funciones hiperbólicas de $\kappa a$ y en la región $x > 2a$ usamos la solución canónica con desfasaje y número de onda $k$. En la región intermedia $a < x < 2a$ podríamos usar una combinación de soluciones

$$\{e^{\kappa x}, e^{-\kappa x}\}, \quad \text{o} \quad \{\cosh \kappa x, \sinh \kappa x\}, \quad \text{o} \quad \{\cosh \kappa(x-a), \sinh \kappa(x-a)\} . \qquad \text{(2.6)}$$

El último par es el más adecuado para implementar directamente la continuidad de la función de onda en $x = a$. Así podemos escribir para la función de onda $\psi(x)$:

$$\psi(x) =
\begin{cases}
A \sin(k'x) & 0 < x < a \\
A \sin(k'a) \cosh\kappa(x-a) + B \sinh\kappa(x-a) & a < x < 2a \\
e^{i\delta}\sin(kx+\delta) & x > 2a
\end{cases} \qquad \text{(2.7)}$$

Tras implementar las condiciones de frontera restantes podemos resolver para el desfasaje $\delta$. Después de un trabajo moderado se obtiene:

$$\tan(2ka + \delta) = \frac{k}{\kappa} \cdot \frac{\sin k'a \cosh\kappa a + \frac{k'}{\kappa}\cos k'a \sinh\kappa a}{\sin k'a \sinh\kappa a + \frac{k'}{\kappa}\cos k'a \cosh\kappa a} . \qquad \text{(2.8)}$$

Esta expresión es bastante intrincada, por lo que es mejor hacer un trabajo numérico. Para ello definimos

$$z_0^2 = \frac{2mV_0 a^2}{\hbar^2}, \qquad z_1^2 = \frac{2mV_1 a^2}{\hbar^2}, \qquad u \equiv ka . \qquad \text{(2.9)}$$

lo que nos permite expresar tanto $k'a$ como $\kappa a$ como funciones de $u$

$$(k'a)^2 = z_0^2 + u^2, \qquad (\kappa a)^2 = z_1^2 - u^2 . \qquad \text{(2.10)}$$

En este punto (2.8) puede usarse para determinar $\delta$ en función de $u = ka$ y las constantes $z_0, z_1$. Supongamos que elegimos valores para nuestros parámetros que controlan las ecuaciones. En la Figura 5 mostramos resultados para $z_0^2 = 1$ y $z_1^2 = 5$.

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes19_ES/fig5.png)

Figura 5: Gráfico de varias cantidades en función de $u = ka$, con el potencial caracterizado por $z_0^2 = 1$ y $z_1^2 = 5$. (a) $\delta(E)$ aumenta rápidamente alrededor de $u_* = 1.85$, o equivalentemente $E = 0.69\,V_1$, cruzando $-\pi/2$ y señalando comportamiento resonante. (b) Gráfico de $|A_s|^2 = \sin^2\delta$, mostrando picos cada vez que $|\delta| = \pi/2$. (c) El coeficiente $|A|$ de la función de onda en el pozo alcanza su pico en la resonancia, mostrando alta probabilidad de encontrar la partícula en el pozo. (d) El retraso temporal es positivo y alcanza su pico en la resonancia.

Consideremos la parte (a) de la figura, que muestra $\delta(ka)$. Al comienzo $\delta$ disminuye linealmente, señal de un retraso temporal negativo, ya que las ondas de baja energía se reflejan en el borde $x = 2a$ de la barrera $V_1$. Cuando $\delta$ cruza $-\pi/2$ no hay resonancia, aunque $|A_s|^2 = \sin^2\delta$ sea igual a uno. En efecto, no vemos ningún pico en la amplitud $|A|$. A medida que aumenta la energía y $u = u_* = 1.8523$ obtenemos una resonancia. Esta vez $\delta$ está aumentando rápidamente y $\delta$ cruza $-\pi/2$ nuevamente, haciendo que $|A_s|^2 = 1$. La señal de resonancia es el muy alto $|A|$, el pico en el retraso temporal. Este retraso temporal alcanza un valor de aproximadamente 14, lo que significa que el retraso es catorce veces el tiempo de tránsito libre $4a/v_0$.

## 3. Modelando la resonancia

Nos gustaría tener más comprensión sobre la naturaleza de las resonancias. En particular, queremos apreciar las características generales del fenómeno. Además, hasta ahora podemos identificar resonancias observando el comportamiento de $\delta$, pero ¿podemos encontrar una ecuación que defina las resonancias?

Como primer paso, modelamos el comportamiento de un desfasaje cerca de la resonancia. Recordando que una resonancia requiere que $|\delta|$ cruce el valor $\pi/2$ y que $\delta$, físicamente, es lo mismo que $\delta$ aumentado o disminuido en múltiplos de $\pi$, podemos elegir que $\delta$ varíe de casi cero a casi $\pi$. Podemos lograr esto con la siguiente función simple.

$$\delta = \tan^{-1}\left(\frac{\beta}{\alpha - k}\right), \quad \text{con } \beta > 0, \ \alpha > 0 . \qquad \text{(3.1)}$$

aquí $\alpha$ y $\beta$ son constantes positivas con las mismas unidades que $k$. Para ver lo que hace esta función, primero graficamos el argumento de la arcotangente en la parte superior de la Figura 6. Nótese que el argumento varía rápidamente en la región $(\alpha - \beta, \alpha + \beta)$. La variación de la fase asociada $\delta$ se muestra en la figura de abajo. Para tener un aumento pronunciado en la fase, debemos tener $\beta$ pequeño en comparación con $\alpha$.

![Figura 6](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes19_ES/fig6.png)

Figura 6: La constante $\beta$ debe ser pequeña en comparación con $\alpha$ para obtener una variación pronunciada. Una resonancia, como se muestra aquí, requiere que $\delta$ aumente con la energía.

Dos cálculos relativamente cortos nos dan más comprensión:

$$\left.\frac{d\delta}{dk}\right|_{k=\alpha} = \frac{1}{\beta}, \qquad |A_s|^2 = \sin^2\delta = \frac{\beta^2}{\beta^2 + (\alpha - k)^2} . \qquad \text{(3.2)}$$

El primero nos informa que, en igualdad de condiciones, el retraso es grande si $\beta$ es pequeño. El segundo nos da la norma al cuadrado de la amplitud de dispersión en función de $k$, con un pico en $k = \alpha$. Esta ecuación se expresa de manera más célebre en términos de la energía. Para esto notamos que

$$E - E_\alpha = \frac{\hbar^2}{2m}(k^2 - \alpha^2) = \frac{\hbar^2}{2m}(k+\alpha)(k-\alpha) \simeq \frac{\hbar^2}{2m}(2\alpha)(k-\alpha) , \qquad \text{(3.3)}$$

cuando trabajamos con $k \approx \alpha$. De esto se sigue que

$$(k-\alpha)^2 \simeq \frac{m^2}{\hbar^4 \alpha^2}(E - E_\alpha)^2 , \qquad \text{(3.4)}$$

y por lo tanto

$$|\psi_s|^2 \simeq \frac{\beta^2}{\beta^2 + \frac{m^2}{\hbar^4\alpha^2}(E-E_\alpha)^2} = \frac{\frac{1}{4}\Gamma^2}{(E-E_\alpha)^2 + \frac{1}{4}\Gamma^2} , \qquad \text{(3.5)}$$

Donde hemos definido la constante $\Gamma$ con unidades de energía:

$$\frac{1}{4}\Gamma^2 = \frac{\hbar^4\beta^2\alpha^2}{m^2} \ \to \ \Gamma = \frac{2\alpha\beta\hbar^2}{m} . \qquad \text{(3.6)}$$

La dependencia en la energía de $|\psi_s|^2$ sigue la llamada distribución de Breit-Wigner,

$$|\psi_s|^2 \simeq \frac{\frac{1}{4}\Gamma^2}{(E-E_\alpha)^2 + \frac{1}{4}\Gamma^2} . \qquad \text{(3.7)}$$

La distribución se muestra en la Figura 8. El valor pico para $|\psi_s|^2$ se alcanza en $E = E_\alpha$ y vale uno. Llamamos a $\Gamma$ el ancho a media altura porque el valor de $|\psi_s|^2$ en $E = E_\alpha \pm \frac{1}{2}\Gamma$ es un medio. Un $\Gamma$ pequeño corresponde a un ancho estrecho, o una resonancia estrecha.

![Figura 7](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes19_ES/fig7.png)

Figura 7: La distribución de Breit-Wigner. $\Gamma$ es el ancho de la distribución a media altura.

Para comprender mejor el significado de $\Gamma$ definimos el tiempo asociado $\tau$, llamado el tiempo de vida de la resonancia:

$$\tau \equiv \frac{\hbar}{\Gamma} = \frac{m}{2\alpha\beta\hbar} . \qquad \text{(3.8)}$$

Como probablemente esperaría, el tiempo de vida está estrechamente relacionado con el retraso temporal asociado a un paquete de ondas de energía media igual a la energía resonante. En efecto, podemos evaluar el retraso temporal $\Delta t$ para $k = \alpha$ y obtener

$$\Delta t = \left.2\hbar\frac{d\delta}{dE}\right|_{k=\alpha} = 2\hbar\frac{dk}{dE}\frac{d\delta}{dk} = \frac{2\hbar}{\frac{\hbar^2}{m}k}\cdot\frac{1}{\beta} = \frac{2m}{\hbar\alpha\beta} = 4\tau . \qquad \text{(3.9)}$$

Por lo tanto, concluimos que el tiempo de vida y el retraso temporal son la misma cantidad, salvo un factor de cuatro.

$$\tau = \frac{\hbar}{\Gamma} = \frac{1}{4}\Delta t . \qquad \text{(3.10)}$$

Las partículas inestables a veces se llaman resonancias. El bosón de Higgs, descubierto en 2012, es una partícula inestable con masa de 125 GeV. Puede desintegrarse en dos fotones, o en dos leptones tau, o en un par $b\bar{b}$, entre pocas otras posibilidades. El ancho $\Gamma$ asociado a la partícula es de 4.07 MeV ($\pm 4\%$). ¡Su tiempo de vida $\tau$ es de aproximadamente $1.62 \times 10^{-22}$ segundos!

Ahora intentamos comprender las resonancias de manera más matemática. Vimos que, en la resonancia, la norma de $A_s$ alcanza un valor máximo de uno. Exploremos cuándo $A_s$ es grande. Tenemos

$$A_s = \sin\delta\, e^{i\delta} = \frac{\sin\delta}{e^{-i\delta}} = \frac{\sin\delta}{\cos\delta - i\sin\delta} = \frac{\tan\delta}{1 - i\tan\delta} . \qquad \text{(3.11)}$$

En la resonancia $\delta = \pi/2$ y $A_s = i$, usando la primera igualdad. Por otro lado, si bien normalmente pensamos en $\delta$ como un número real, la expresión final de arriba indica que $A_s$ se vuelve infinito para

$$\tan\delta = -i , \qquad \text{(3.12)}$$

¡lo que sea que eso signifique! Si recordamos que $\tan iz = i\tanh z$ deducimos que la condición anterior requiere $\delta \to -i\infty$, un resultado bastante extraño. En todo caso, $A_s$ se vuelve infinito, o tiene un polo, en $\tan\delta = -i$. Veremos que el gran valor $|A_s| = 1$ en la resonancia puede considerarse como la “sombra” del valor infinito que $A_s$ alcanza cerca en el plano complejo.

![Figura 8](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes19_ES/fig8.png)

Figura 8: En el plano complejo de $k$, las resonancias se identifican como polos de la amplitud de dispersión $A_s$ ubicados ligeramente por debajo del eje real. Los estados ligados aparecen como polos sobre el eje imaginario positivo.

En efecto, podemos ver cómo se comporta $A_s$ cerca de la resonancia insertando el comportamiento cercano a la resonancia (3.1) de $\delta$ en (3.11):

$$A_s = \frac{\frac{\beta}{\alpha-k}}{1 - i\frac{\beta}{\alpha-k}} = \frac{\beta}{(\alpha - i\beta) - k} . \qquad \text{(3.13)}$$

Cuando $k = \alpha$, es decir, en la energía resonante, obtenemos $A_s = i$, como se esperaba. Si ahora pensamos en el número de onda $k$ como una variable compleja, vemos que el polo de $A_s$ es un polo en $k = k_* = \alpha - i\beta$. La parte real de $k_*$ es la energía resonante, y la parte imaginaria $\beta$ codifica el tiempo de vida. Para $\beta$ pequeño la resonancia es un polo cercano al eje real, como se ilustra en la Figura 8. Cuanto menor es $\beta$, más aguda es la resonancia. Como podemos ver, el valor de $|A_s|$ sobre la línea real se vuelve grande para $k = \alpha$ porque en realidad es infinito un poco por debajo del eje.

La lección de todo esto es que podemos, en efecto, tomar en serio (3.12) y buscar resonancias resolviendo para los valores complejos de $k$ para los cuales

$$\text{Condición de resonancia: } \tan\delta(k) = -i . \qquad \text{(3.14)}$$

La parte real de esos valores de $k$ son las energías resonantes. Las partes imaginarias nos dan el tiempo de vida.

La idea de un plano complejo de $k$ es muy poderosa. Supongamos que consideramos valores puramente imaginarios de $k$ de la forma $k = i\kappa$, con $\kappa > 0$. Entonces la energía toma la forma

$$E = -\frac{\hbar^2\kappa^2}{2m} < 0 , \qquad \text{(3.15)}$$

que es adecuada para estados ligados. En efecto, se puede demostrar que los estados ligados aparecen como polos de $A_s$ a lo largo del eje imaginario positivo, como se muestra en la Figura 8. ¡El plano complejo de $k$ tiene espacio para acomodar estados de dispersión, resonancias, y estados ligados!

*Sarah Geller transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare https://ocw.mit.edu

8.04 Física Cuántica I Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

# Apéndice: Lista de problemas 8 (Problem Set 8, 2016)

*Departamento de Física del MIT* *13 de abril de 2016 — Fecha de entrega: viernes 22 de abril de 2016, 12:00 del mediodía*

**Lecturas recomendadas:** Griffiths, páginas 73-76, 81-82 (sobre estados de dispersión). Ohanian, Capítulo 11: Dispersión y resonancias.

## Problema 1: Estados del oscilador armónico \[15 puntos\]

Considere el estado $\psi_\alpha$ definido por

$$\psi_\alpha \equiv N \exp(\alpha \hat{a}^\dagger)\, \varphi_0 ,$$

con $\alpha \in \mathbb{C}$ un número complejo. Para las dos primeras preguntas siguientes puede ser útil simplemente expandir la exponencial anterior.

1.  Encuentre la constante $N$ necesaria para que el estado $\psi_\alpha$ esté normalizado.

2.  Demuestre que el estado $\psi_\alpha$ es un autoestado del operador de aniquilación $\hat{a}$. ¿Cuál es el autovalor?

3.  Encuentre el valor esperado del hamiltoniano en el estado $\psi_\alpha$.

4.  Encuentre la incertidumbre en la energía en el estado $\psi_\alpha$.

5.  Use la ecuación de autovalores, vista como una ecuación diferencial, para calcular la forma explícita de la función de onda normalizada $\psi_\alpha$.

## Problema 2: Dos funciones delta — otra vez \[15 puntos\]

Considere de nuevo el problema de una partícula de masa $m$ moviéndose en un potencial de doble pozo unidimensional

$$V(x) = -g\,\delta(x-a) - g\,\delta(x+a) , \qquad g > 0 .$$

En la tarea anterior encontró el valor de la energía del estado ligado $E$ para el estado par en términos de la energía $E_0 = \hbar^2/(2ma^2)$. Había definido $\xi = \kappa a$,

$$\frac{E}{E_0} = -\xi^2 \quad \text{donde} \quad \frac{\xi}{1+e^{-2\xi}} = \lambda , \qquad \lambda \equiv \frac{mag}{\hbar^2} ,$$

con $\lambda$ adimensional, y que codifica la intensidad $g$ de las funciones delta, si $a$ es constante, o bien la separación entre las funciones delta, si $g$ es constante. Podemos entonces escribir

$$\lambda = \frac{a}{a_0} , \qquad a_0 \equiv \frac{\hbar^2}{mg} ,$$

siendo $a_0$ una escala de longitud natural del problema una vez fijado $g$. Introduzcamos también la energía $E_\infty$ asociada a una única función delta:

$$E_\infty \equiv \frac{mg^2}{2\hbar^2} .$$

Suponga ahora que este es un modelo de una molécula diatómica con distancia interatómica $2a$. El electrón del estado ligado ayuda a superar la energía repulsiva entre los iones. Sea la energía potencial repulsiva $V_r(x)$, con $x$ la distancia entre los átomos, dada por

$$V_r(x) = \frac{\beta g}{x} , \qquad \beta > 0 ,$$

donde $\beta$ es un número pequeño. La energía potencial total $V_{\text{tot}}$ de la configuración es la suma de la energía negativa $E$ del estado ligado y la energía repulsiva positiva:

$$V_{\text{tot}} = E + V_r(2a) .$$

1.  Escriba $E$ como $E = -E_\infty f(\xi,\lambda)$ donde $f$ es una función que debe determinar. Grafique $E$ como función de $a/a_0 = \lambda$ para entender cómo varía la energía del estado fundamental en función de la separación entre las moléculas. ¿Cuáles son los valores de $E$ para $a \to 0$ y para $a \to \infty$?

2.  Escriba $V_r$ en términos de $E_\infty$, $\beta$ y $\lambda$.

3.  Considere ahora la energía potencial total $V_{\text{tot}}$ y grafíquela como función de $a/a_0 = \lambda$ para varios valores de $\beta$. Debería encontrar un punto crítico estable del potencial para $\beta$ suficientemente pequeño. Para $\beta = 0.31$, ¿cuál es el valor aproximado de $a/a_0$ en el punto crítico del potencial?

## Problema 3: El pozo cuadrado finito convirtiéndose en el pozo cuadrado infinito \[5 puntos\]

Considere el potencial de pozo cuadrado estándar

$$V(x) = \begin{cases} -V_0 , & \text{para } |x| \le a,\ V_0 > 0 , \\ 0 & \text{para } |x| > a , \end{cases} \qquad (1)$$

y la función de onda para un estado par

$$\psi(x) = \begin{cases} \dfrac{1}{\sqrt{a}}\cos kx , & \text{para } |x| \le a, \\[4pt] \dfrac{A}{\sqrt{a}}\, e^{-\kappa|x|} , & \text{para } |x| > a , \end{cases} \qquad (2)$$

donde incluimos el prefactor $\frac{1}{\sqrt{a}}$ para tener unidades consistentes para $\psi$.

Queremos comprender mejor el límite $V_0 \to \infty$ y entender por qué la discontinuidad en $\psi'$ del pozo infinito no genera problemas. Mantener $m$ y $a$ constantes mientras $V_0$ crece equivale a dejar que $z_0$ crezca.

Un análisis previo demostró que para el estado fundamental, en la situación de $z_0$ grande, el ansatz (2) está normalizado con precisión y

$$\eta = ka \simeq \frac{\pi}{2}\left(1 - \frac{1}{z_0}\right) , \qquad \xi = \kappa a \simeq z_0 , \qquad A \simeq \frac{\pi}{2 z_0}\, e^{z_0} .$$

Queremos ver si el valor esperado del hamiltoniano recibe una contribución singular desde la región prohibida. Dado que el potencial $V(x)$ se anula allí, solo debemos preocuparnos por la contribución del operador de energía cinética $\hat{K} = \hat{p}^2/2m$. Calcule la contribución al valor esperado de $\hat{K}$ desde la región prohibida $x > a$:

$$\langle \hat{K} \rangle_{x>a} \equiv \int_a^\infty dx\, \psi^*(x)\, \hat{K}\, \psi(x) .$$

La respuesta debe darse en términos de $z_0$. Interprete su resultado.

## Problema 4: Reflexión de un paquete de ondas contra un potencial escalón \[20 puntos\]

Considere un potencial escalón con altura $V_0$:

$$V(x) = \begin{cases} V_0 , & \text{para } x > 0 \\ 0 , & \text{para } x < 0 . \end{cases} \qquad (1)$$

Enviamos desde $x = -\infty$ un paquete de ondas cuyas componentes de momento tienen todas energías menores que la energía $V_0$ del escalón. Para esto necesitamos modos con $k$ que satisfagan

$$k \le \hat{k} , \qquad \hat{k}^2 = \frac{2mV_0}{\hbar^2} . \qquad (2)$$

Escribiremos entonces el paquete de ondas incidente como

$$\Psi_{\text{inc}}(x) = \sqrt{a} \int_0^{\hat{k}} dk\, \Phi(k)\, e^{ikx}\, e^{-iE(k)t/\hbar} , \qquad x < 0 . \qquad (3)$$

Aquí $a$ es la constante con unidades de longitud, determinada de manera única por las constantes $m$, $V_0$, $\hbar$ de este problema, y $\Phi(k)$ es una función real, adimensional, con un máximo en $k_0 < \hat{k}$:

$$a \equiv \frac{\hbar}{\sqrt{mV_0}} , \qquad \Phi(k) = e^{-\beta^2 a^2 (k-k_0)^2} . \qquad (4)$$

La constante real $\beta$, que se fijará más abajo, controla el ancho de la distribución de momento. Las unidades de $\Psi_{\text{inc}}$ son $L^{-1/2}$, y por eso incluimos el prefactor $\sqrt{a}$ en (3). Recuerde que $dk$ tiene unidades de $L^{-1}$.

1.  Escriba la función de onda reflejada (válida para $x<0$) como una integral similar a (3). Esta integral involucra el desfasaje $\delta(E)$ calculado en clase.

Introduzca una versión adimensional $K$ del número de onda $k$, una versión adimensional $u$ de la coordenada $x$, y una versión adimensional $\tau$ del tiempo $t$, de la siguiente manera:

$$k \equiv \frac{K}{a} , \qquad x \equiv au , \qquad t \equiv \frac{\hbar}{V_0}\tau . \qquad (5)$$

Naturalmente, escribiremos $k_0 = K_0/a$. Note que $kx = Ku$.

1.  Demuestre que la velocidad de grupo y la relación de incertidumbre para el paquete entrante toman la forma

$$\frac{du}{d\tau} = \#\, K_0 , \qquad \Delta u\, \Delta K \ge \# ,$$

donde $\#$ representa constantes numéricas que debe determinar (¡constantes distintas!). Use la aproximación de que se tiene la gaussiana completa $|\Phi(K)|^2$ para determinar la incertidumbre $\Delta K$ en el paquete entrante en términos de $\beta$. Suponiendo de nuevo que se tiene una gaussiana completa, ¿cuál sería (en términos de $\beta$) el valor mínimo posible de la incertidumbre $\Delta u$ para la distribución de probabilidad asociada en el espacio de coordenadas?

1.  Complete las siguientes ecuaciones fijando las constantes representadas por $\#$:

$$E(k) = \#\, V_0 K^2 , \qquad e^{2i\delta(E)} = \# + \#K^2 + iK\sqrt{\# + \#K^2} \equiv w(K) .$$

1.  Demuestre que el retraso $\Delta t = 2\hbar\,\delta'(E)$ experimentado por la onda reflejada implica un $\Delta\tau$ dado por

$$\Delta\tau = \frac{\#}{K_0\sqrt{\# + \#K_0^2}} ,$$

donde debe fijar las constantes.

1.  Demuestre que la función de onda completa $\Psi(x,t)$, válida para $x<0$ y todo tiempo, que ahora vemos como $\Psi(u,\tau)$ válida para $u<0$ y todo $\tau$, toma la forma

$$a^{\frac{1}{2}}\Psi(u,\tau) = \int_0^{\#} dK\, e^{-\beta^2 (K-K_0)^2}\, e^{-i\#K^2\tau}\left( e^{iKu} - e^{-iKu}\, w(K) \right)$$

y determine las dos constantes faltantes.

1.  Fije $\beta = 4$ y $K_0 = 1$. ¿Cuáles son los valores de $\Delta K$ y $\Delta u$? ¿Cuál es el retraso temporal $\Delta\tau$ predicho? (No se califica: ¿puede hacer una conjetura informada sobre si el paquete cambiará de forma rápidamente?)

Ahora use Mathematica para calcular y graficar la densidad de probabilidad $|a^{1/2}\Psi(u,\tau)|^2$. Dé la gráfica de la función de onda para $\tau = -20, -5$ y $0$, usando $u \in [-30,0]$. Examine la gráfica para $\tau = 20$ y determine el retraso temporal $\Delta\tau$ observando la posición del máximo del paquete. Su respuesta debería acercarse razonablemente al valor analítico determinado previamente.

## Problema 5: Dispersión en una barrera rectangular \[10 puntos\]

Basado en Griffiths 2.33, p. 83.

Resuelva solamente los casos $E < V_0$ y $E = V_0$.

¿Puede obtener $T = 1$ para $E < V_0$?

Encuentre la respuesta para $E > V_0$ en algún libro (o hágalo usted mismo). ¿Cuándo se obtiene $T=1$ para $E > V_0$?

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*


---

<!-- MIT8.04_LecNotes1_ES.md -->

*B. Zwiebach* *9 de febrero de 2016*

# Capítulo 1: Características clave de la mecánica cuántica

## Vídeos de esta clase (YouTube)

**Lección 1: An overview of quantum mechanics.**

- [Quantum mechanics as a framework. Defining linearity](https://www.youtube.com/watch?v=jANZxzetPaQ)
- [Linearity and nonlinear theories. Schrödinger’s equation](https://www.youtube.com/watch?v=kiuwtaprFjk)
- [Necessity of complex numbers](https://www.youtube.com/watch?v=f079K1f2WQk)
- [Photons and the loss of determinism](https://www.youtube.com/watch?v=8OsUQ1yXCcI)
- [The nature of superposition. Mach-Zehnder interferometer](https://www.youtube.com/watch?v=CR-eOhdxbes)

------------------------------------------------------------------------

La mecánica cuántica tiene ya casi cien años, pero todavía estamos descubriendo algunas de sus sorprendentes características y sigue siendo objeto de mucha investigación y especulación. El marco de la mecánica cuántica es una extensión rica y elegante del marco de la física clásica. También es contraintuitivo y casi paradójico.

La física cuántica ha reemplazado a la física clásica como la descripción fundamental correcta de nuestro universo físico. Se usa rutinariamente para describir la mayoría de los fenómenos que ocurren a distancias cortas. La física cuántica es el resultado de aplicar el marco de la mecánica cuántica a diferentes fenómenos físicos. Así, tenemos la Electrodinámica Cuántica, cuando la mecánica cuántica se aplica al electromagnetismo; la Óptica Cuántica, cuando se aplica a la luz y a los dispositivos ópticos; o la Gravedad Cuántica, cuando se aplica a la gravitación. La mecánica cuántica proporciona, en efecto, un marco notablemente coherente y elegante. La era de la física cuántica comienza en 1925, con los descubrimientos de Schrödinger y Heisenberg. Las semillas de estos descubrimientos fueron sembradas por Planck, Einstein, Bohr, de Broglie y otros. Es un tributo a la imaginación humana que hayamos sido capaces de descubrir el conjunto de reglas contraintuitivo y abstracto que define la mecánica cuántica. Aquí pretendemos explicar y ofrecer cierta perspectiva sobre las características principales de este marco.

Comenzaremos discutiendo la propiedad de linealidad, que la mecánica cuántica comparte con la teoría electromagnética. Esta propiedad nos dice qué tipo de teoría es la mecánica cuántica y por qué, podría argumentarse, es más simple que la mecánica clásica. A continuación pasamos a los fotones, las partículas de luz. Usamos fotones y polarizadores para explicar por qué la física cuántica no es determinista y, en contraste con la física clásica, los resultados de algunos experimentos no pueden predecirse. La mecánica cuántica es un marco en el que solo podemos predecir las probabilidades de los distintos resultados de un experimento dado. Nuestro siguiente tema son las superposiciones cuánticas, en las que un objeto cuántico de alguna manera consigue existir simultáneamente en dos estados mutuamente incompatibles. Una bombilla cuántica, por ejemplo, podría estar en un estado en el que está encendida y apagada al mismo tiempo.

## 1. Linealidad de las ecuaciones de movimiento

En física, una teoría se describe habitualmente mediante un conjunto de ecuaciones para ciertas cantidades llamadas variables dinámicas de la teoría. Tras escribir una teoría, la tarea más importante es encontrar soluciones de las ecuaciones. Una solución de las ecuaciones describe una realidad posible, según la teoría. Como un universo en expansión es una solución de las ecuaciones gravitacionales de Albert Einstein, por ejemplo, se sigue que un universo en expansión es posible, según esta teoría. Una única teoría puede tener muchas soluciones, cada una describiendo una realidad posible.

Hay teorías lineales y teorías no lineales. Las teorías no lineales son más complejas que las lineales. En una teoría lineal ocurre un hecho notable: si se tienen dos soluciones, se obtiene una tercera solución de la teoría simplemente sumando las dos soluciones. Un ejemplo de una hermosa teoría lineal es la teoría de Maxwell del electromagnetismo, una teoría que gobierna el comportamiento de los campos eléctrico y magnético. Un campo, como probablemente ya sabe, es una cantidad cuyos valores pueden depender de la posición y del tiempo. Una solución simple de esta teoría describe una onda electromagnética que se propaga en una dirección dada. Otra solución simple podría describir una onda electromagnética propagándose en una dirección distinta. Debido a que la teoría es lineal, tener las dos ondas propagándose simultáneamente, cada una en su propia dirección y sin afectarse mutuamente, es una solución nueva y consistente. La suma es una solución en el sentido de que el campo eléctrico en la nueva solución es la suma del campo eléctrico en la primera solución más el campo eléctrico en la segunda solución. Lo mismo ocurre con el campo magnético: el campo magnético en la nueva solución es la suma del campo magnético en la primera solución más el campo magnético en la segunda solución. De hecho, se puede sumar cualquier número de soluciones y seguir obteniendo una solución. Aunque esto suene esotérico, usted está totalmente familiarizado con ello. El aire a su alrededor está lleno de ondas electromagnéticas, cada una propagándose ajena a las demás. Están las ondas de miles de teléfonos móviles, las ondas que transportan cientos de mensajes de internet inalámbrico, las ondas de multitud de emisoras de radio, canales de televisión, y muchas, muchas más. Hoy en día, un único cable transatlántico puede transportar simultáneamente millones de llamadas telefónicas, junto con enormes cantidades de vídeo y datos de internet. Todo ello gracias a la linealidad.

Más concretamente, decimos que las ecuaciones de Maxwell son ecuaciones lineales. Una solución de la ecuación de Maxwell se describe mediante un campo eléctrico $E$, un campo magnético $B$, una densidad de carga $\rho$ y una densidad de corriente $J$, todos denotados colectivamente como $(E, B, \rho, J)$. Esta colección de campos y fuentes satisface las ecuaciones de Maxwell. La linealidad implica que si $(E, B, \rho, J)$ es una solución, también lo es $(\alpha E, \alpha B, \alpha \rho, \alpha J)$, donde todos los campos y fuentes han sido multiplicados por la constante $\alpha$. Dadas dos soluciones

$$(E_1, B_1, \rho_1, J_1), \quad \text{y} \quad (E_2, B_2, \rho_2, J_2), \qquad \text{(1.1)}$$

la linealidad también implica que podemos obtener una nueva solución sumándolas

$$(E_1 + E_2, B_1 + B_2, \rho_1 + \rho_2, J_1 + J_2). \qquad \text{(1.2)}$$

La nueva solución puede llamarse la superposición de las dos soluciones originales.

No es difícil explicar qué es, en general, una ecuación lineal o un conjunto lineal de ecuaciones. Consideremos la ecuación

$$Lu = 0, \qquad \text{(1.3)}$$

donde, esquemáticamente, $u$ denota la incógnita. La incógnita puede ser un número, o una función del tiempo, una función del espacio, una función del tiempo y del espacio, esencialmente cualquier cosa desconocida. De hecho, $u$ podría representar una colección de incógnitas, en cuyo caso reemplazaríamos $u$ por $u_1, u_2, \ldots$. El símbolo $L$ denota un operador lineal, un objeto que satisface las dos propiedades siguientes

$$L(u_1 + u_2) = Lu_1 + Lu_2, \qquad L(au) = aLu, \qquad \text{(1.4)}$$

donde $a$ es un número. Nótese que estas condiciones implican que

$$L(\alpha u_1 + \beta u_2) = \alpha Lu_1 + \beta Lu_2, \qquad \text{(1.5)}$$

lo que muestra que si $u_1$ es una solución ($Lu_1 = 0$) y $u_2$ es una solución ($Lu_2 = 0$), entonces $\alpha u_1 + \beta u_2$ también es una solución. Llamamos a $\alpha u_1 + \beta u_2$ la superposición general de las soluciones $u_1$ y $u_2$. Un ejemplo puede ayudar. Consideremos la ecuación

$$\frac{du}{dt} + \frac{1}{\tau} u = 0, \qquad \text{(1.6)}$$

donde $\tau$ es una constante con unidades de tiempo. Esta es, de hecho, una ecuación diferencial lineal, y toma la forma $Lu = 0$ si definimos

$$Lu \equiv \frac{du}{dt} + \frac{1}{\tau} u \qquad \text{(1.7)}$$

**Ejercicio 1.** Verifique que (1.7) satisface las condiciones para un operador lineal.

La teoría de la relatividad general de Einstein es una teoría no lineal cuya variable dinámica es un campo gravitacional, el campo que describe, por ejemplo, cómo se mueven los planetas alrededor de una estrella. Al ser una teoría no lineal, sencillamente no se pueden sumar los campos gravitacionales de distintas soluciones para hallar una nueva solución. Esto hace que la teoría de Einstein sea bastante complicada, según todos los indicios mucho más complicada que la teoría de Maxwell. De hecho, ¡la mecánica clásica, tal como fue inventada principalmente por Isaac Newton, también es una teoría no lineal! En mecánica clásica las variables dinámicas son las posiciones y velocidades de las partículas, sobre las que actúan fuerzas. No existe una forma general de usar dos soluciones para construir una tercera.

En efecto, consideremos la ecuación de movimiento para una partícula en una línea bajo la influencia de un potencial independiente del tiempo $V(x)$, que en general es una función arbitraria de $x$. La variable dinámica en este problema es $x(t)$, la posición en función del tiempo. Denotando por $V'$ la derivada de $V$ respecto a su argumento, la segunda ley de Newton toma la forma

$$m \frac{d^2 x(t)}{dt^2} = -V'(x(t)). \qquad \text{(1.8)}$$

El lado izquierdo es la masa por la aceleración y el lado derecho es la fuerza experimentada por la partícula en el potencial. Probablemente vale la pena resaltar que el lado derecho es la función $V'(x)$ evaluada en $x$ igualado a $x(t)$:

$$V'(x(t)) \equiv \left. \frac{\partial V(x)}{\partial x} \right|_{x = x(t)}. \qquad \text{(1.9)}$$

Aunque aquí podríamos haber usado una derivada ordinaria, escribimos una derivada parcial, como es habitual para el caso general de potenciales dependientes del tiempo. La razón por la que la ecuación (1.8) no es una ecuación lineal es que la función $V'(x)$ no es lineal. En general, para funciones arbitrarias $u$ y $v$ esperamos

$$V'(au) \neq aV'(u), \quad \text{y} \quad V'(u+v) \neq V'(u) + V'(v). \qquad \text{(1.10)}$$

Como resultado, dada una solución $x(t)$, no se espera que la solución escalada $\alpha x(t)$ sea también una solución. Dadas dos soluciones $x_1(t)$ y $x_2(t)$, tampoco está garantizado que $x_1(t) + x_2(t)$ sea una solución.

**Ejercicio.** ¿Cuál es el potencial $V(x)$ más general para el cual la ecuación de movimiento de $x(t)$ es lineal?

La mecánica cuántica es una teoría lineal. La ecuación distintiva de esta teoría, la llamada ecuación de Schrödinger, es una ecuación lineal para una cantidad llamada función de onda, y determina su evolución temporal. La función de onda es la variable dinámica en mecánica cuántica pero, curiosamente, su interpretación física no estaba clara para Erwin Schrödinger cuando escribió la ecuación en 1925. Fue Max Born quien, meses después, sugirió que la función de onda codifica probabilidades. Esta fue la interpretación física correcta, pero fue profundamente rechazada por muchos, incluido el propio Schrödinger, quien permaneció descontento con ella el resto de su vida. La linealidad de la mecánica cuántica implica una profunda simplicidad. En cierto sentido, la mecánica cuántica es más simple que la mecánica clásica. En mecánica cuántica las soluciones pueden sumarse para formar nuevas soluciones.

La función de onda $\Psi$ depende del tiempo y también puede depender del espacio. La ecuación de Schrödinger (ES) es una ecuación diferencial parcial que toma la forma

$$i\hbar \frac{\partial \Psi}{\partial t} = \hat{H}\Psi, \qquad \text{(1.11)}$$

donde el hamiltoniano (u operador de energía) $\hat{H}$ es un operador lineal que puede actuar sobre funciones de onda:

$$\hat{H}(a\Psi) = a\hat{H}\Psi, \qquad \hat{H}(\Psi_1 + \Psi_2) = \hat{H}(\Psi_1) + \hat{H}(\Psi_2), \qquad \text{(1.12)}$$

con $a$ una constante que, de hecho, no necesita ser real; puede ser un número complejo. Por supuesto, ¡$\hat{H}$ en sí mismo no depende de la función de onda! Para comprobar que la ecuación de Schrödinger es lineal, la escribimos en la forma $L\Psi = 0$ con $L$ definido como

$$L\Psi \equiv i\hbar \frac{\partial \Psi}{\partial t} - \hat{H}\Psi \qquad \text{(1.13)}$$

Ahora es sencillo verificar que $L$ es un operador lineal. Físicamente, esto significa que si $\Psi_1$ y $\Psi_2$ son soluciones de la ecuación de Schrödinger, entonces también lo es la superposición $\alpha\Psi_1 + \beta\Psi_2$, donde $\alpha$ y $\beta$ son ambos números complejos, es decir, $(\alpha, \beta \in \mathbb{C})$.

## 2. Los números complejos son esenciales

La mecánica cuántica es la primera teoría física que realmente hace uso de los números complejos. Los números que la mayoría usamos en la vida cotidiana (enteros, fracciones, decimales) son números reales. El conjunto de los números complejos se denota por $\mathbb{C}$ y el conjunto de los números reales se denota por $\mathbb{R}$. Los números complejos aparecen cuando combinamos números reales con la unidad imaginaria $i$, definida como igual a la raíz cuadrada de menos uno: $i \equiv \sqrt{-1}$. Al ser la raíz cuadrada de menos uno, significa que $i$ al cuadrado debe dar menos uno: $i^2 = -1$. Los números complejos son fundamentales en matemáticas. Una ecuación como $x^2 = -4$, para una incógnita $x$, no puede resolverse si $x$ ha de ser real. Ningún número real al cuadrado da menos uno. Pero si permitimos números complejos, tenemos las soluciones $x = \pm 2i$. Los matemáticos han demostrado que todas las ecuaciones polinómicas pueden resolverse en términos de números complejos.

Un número complejo $z$, en toda su generalidad, es un número de la forma

$$z = a + ib \in \mathbb{C}, \qquad a, b \in \mathbb{R}. \qquad \text{(2.1)}$$

Aquí $a$ y $b$ son números reales, e $ib$ denota el producto de $i$ con $b$. El número $a$ se llama parte real de $z$ y $b$ se llama parte imaginaria de $z$:

$$\text{Re}\, z = a, \qquad \text{Im}\, z = b. \qquad \text{(2.2)}$$

El conjugado complejo $z^*$ de $z$ se define como

$$z^* = a - ib. \qquad \text{(2.3)}$$

Puede verificar rápidamente que un número complejo $z$ es real si $z^* = z$, y que es puramente imaginario si $z^* = -z$. Para cualquier número complejo $z = a + ib$ se puede definir la norma $|z|$ del número complejo como un número real positivo dado por

$$|z| = \sqrt{a^2 + b^2}. \qquad \text{(2.4)}$$

Puede comprobar rápidamente que

$$|z|^2 = zz^*, \qquad \text{(2.5)}$$

donde $z^* \equiv a - ib$ se llama el conjugado complejo de $z = a + ib$. Los números complejos se representan como vectores en un «plano complejo» bidimensional. La parte real del número complejo es la componente $x$ del vector y la parte imaginaria del número complejo es la componente $y$. Si consideramos el vector de longitud unidad en el plano complejo que forma un ángulo $\theta$ con el eje $x$, tiene componente $x$ igual a $\cos\theta$ y componente $y$ igual a $\sin\theta$. El vector es, por tanto, el número complejo $\cos\theta + i\sin\theta$. La identidad de Euler relaciona esto con la exponencial de $i\theta$:

$$e^{i\theta} = \cos\theta + i\sin\theta. \qquad \text{(2.6)}$$

Un número complejo de la forma $e^{i\chi}$, con $\chi$ real, se llama fase pura.

Aunque los números complejos son a veces útiles en mecánica clásica o en la teoría de Maxwell, no son estrictamente necesarios. Ninguna de las variables dinámicas, que corresponden a cantidades medibles, es un número complejo. De hecho, los números complejos no pueden medirse en absoluto: todas las mediciones en física dan como resultado números reales. En mecánica cuántica, sin embargo, los números complejos son fundamentales. La ecuación de Schrödinger involucra números complejos. Más aún, la función de onda, la variable dinámica de la mecánica cuántica, es en sí misma un número complejo:

$$\Psi \in \mathbb{C}. \qquad \text{(2.7)}$$

Dado que los números complejos no se pueden medir, la relación entre la función de onda y una cantidad medible debe ser de alguna manera indirecta. La idea de Born de identificar las probabilidades, que son siempre números reales positivos, con el cuadrado de la norma de la función de onda, resultó muy natural. Si escribimos la función de onda de nuestro sistema cuántico como $\Psi$, las probabilidades de los posibles eventos se calculan a partir de $|\Psi|^2$. El marco matemático necesario para expresar las leyes de la mecánica cuántica consiste en espacios vectoriales complejos. En cualquier espacio vectorial tenemos objetos llamados vectores que pueden sumarse entre sí. En un espacio vectorial complejo, un vector multiplicado por un número complejo sigue siendo un vector. Como veremos en nuestro estudio de la mecánica cuántica, muchas veces es útil pensar en la función de onda $\Psi$ como un vector en algún espacio vectorial complejo.

## 3. Pérdida del determinismo

El mayor logro de Maxwell fue darse cuenta de que sus ecuaciones del electromagnetismo permitían la existencia de ondas propagantes. En particular, en 1865 conjeturó que la luz era una onda electromagnética, una fluctuación propagante de campos eléctrico y magnético. Los experimentos posteriores le dieron la razón. Hacia finales del siglo XIX los físicos estaban convencidos de que la luz era una onda. Sin embargo, la certeza no duró mucho. Los experimentos sobre la radiación de cuerpo negro y sobre la fotoemisión de electrones sugerían que el comportamiento de la luz debía ser más complicado que el de una simple onda. Max Planck y Albert Einstein fueron los contribuyentes más destacados a la resolución de los enigmas planteados por esos experimentos.

Para explicar las características del efecto fotoeléctrico, Einstein postuló (1905) que en un haz de luz la energía viene en cuantos: el haz está compuesto de paquetes de energía. Einstein implicaba esencialmente que la luz estaba hecha de partículas, cada una portando una cantidad fija de energía. Él mismo encontraba esta idea inquietante, convencido, como la mayoría de sus contemporáneos, de que, como había demostrado Maxwell, la luz era una onda. Anticipó que una entidad física, como la luz, que pudiera comportarse tanto como partícula como onda, podría provocar el fin de la física clásica y requeriría una teoría física completamente nueva. De hecho, tenía razón. Aunque nunca llegó a apreciar realmente la mecánica cuántica, sus ideas sobre las partículas de luz, más tarde llamadas fotones, ayudaron a construir esta teoría.

Los físicos tardaron hasta 1925 en aceptar que la luz podía comportarse como una partícula. Los experimentos de Arthur Compton (1923) terminaron por convencer a la mayoría de los escépticos. Hoy en día, las partículas de luz, o fotones, se manipulan rutinariamente en laboratorios de todo el mundo. Aunque sigan siendo misteriosos, nos hemos acostumbrado a ellos. Cada fotón de luz visible transporta muy poca energía: un pequeño pulso de láser puede contener miles de millones de fotones. Nuestro ojo, sin embargo, es un muy buen detector de fotones: en total oscuridad, somos capaces de ver luz cuando tan solo diez fotones inciden sobre nuestra retina. Cuando decimos que la luz se comporta como una partícula, nos referimos a una partícula mecánico-cuántica: un paquete de energía y momento que no está compuesto de paquetes más pequeños. No nos referimos a una partícula puntual clásica o corpúsculo newtoniano, que es un objeto de tamaño nulo con posición y velocidad definidas.

Resulta que la energía de un fotón depende únicamente del color de la luz. Como descubrió Einstein, la energía $E$ y la frecuencia $\nu$ de un fotón están relacionadas por

$$E = h\nu \qquad \text{(3.1)}$$

La frecuencia de un fotón determina la longitud de onda $\lambda$ de la luz mediante la relación $\nu\lambda = c$, donde $c$ es la velocidad de la luz. Todos los fotones verdes, por ejemplo, tienen la misma energía. Para aumentar la energía en un haz de luz manteniendo el mismo color, simplemente se necesitan más fotones.

Como explicaremos ahora, la existencia de fotones implica que la mecánica cuántica no es determinista. Con esto queremos decir que el resultado de un experimento no puede determinarse, como ocurriría en física clásica, mediante las condiciones que están bajo el control del experimentador.

Consideremos un polarizador cuya dirección preferencial está alineada a lo largo de la dirección $\hat{x}$, como se muestra en la Figura 1. La luz linealmente polarizada a lo largo de la dirección $\hat{x}$, es decir, luz cuyo campo eléctrico apunta en esa dirección, atraviesa el polarizador. Si la polarización de la luz incidente es ortogonal a la dirección $\hat{x}$, la luz no pasará en absoluto. Así, la luz polarizada linealmente en la dirección $\hat{y}$ será absorbida totalmente por el polarizador. Consideremos ahora luz polarizada a lo largo de una dirección que forma un ángulo $\alpha$ con el eje $x$, como se muestra en la Figura 2. ¿Qué ocurre?

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes1_ES/fig1.png)

Figura 1: Un polarizador que transmite luz linealmente polarizada a lo largo de la dirección $\hat{x}$.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes1_ES/fig2.png)

Figura 2: Luz linealmente polarizada a lo largo de la dirección que forma un ángulo $\alpha$ incidiendo sobre el polarizador.

Pensando en la luz como una onda propagante, el campo eléctrico incidente $E_\alpha$ forma un ángulo $\alpha$ con el eje $x$ y por lo tanto toma la forma

$$E_\alpha = E_0 \cos\alpha\, \hat{x} + E_0 \sin\alpha\, \hat{y}. \qquad \text{(3.2)}$$

Este es un campo eléctrico de magnitud $E_0$. Aquí estamos ignorando la dependencia temporal y espacial de la onda; no son relevantes para nuestra discusión. Cuando este campo eléctrico incide sobre el polarizador, la componente a lo largo de $\hat{x}$ pasa y la componente a lo largo de $\hat{y}$ es absorbida. Así,

$$\text{Más allá del polarizador:} \quad E = E_0 \cos\alpha\, \hat{x}. \qquad \text{(3.3)}$$

Probablemente recuerde que la energía de una onda electromagnética es proporcional al cuadrado de la magnitud del campo eléctrico. Esto significa que la fracción de la energía del haz que pasa a través del polarizador es $(\cos\alpha)^2$. También es bien sabido que la luz que emerge del polarizador tiene la misma frecuencia que la luz incidente.

Hasta aquí todo bien. Pero ahora, intentemos entender este resultado pensando en los fotones que componen la luz incidente. La premisa aquí es que todos los fotones del haz incidente son idénticos. Además, los fotones no interactúan entre sí. Podríamos incluso imaginar enviar toda la energía del haz de luz incidente un fotón a la vez. Puesto que toda la luz que emerge del polarizador tiene la misma frecuencia que la luz incidente, debemos concluir que cada fotón individual, o bien pasa, o bien es absorbido. Si una fracción de un fotón pasara, sería un fotón de menor energía y, por tanto, de menor frecuencia, algo que no ocurre.

Pero ahora tenemos un problema. Como sabemos por el análisis ondulatorio, aproximadamente una fracción $(\cos\alpha)^2$ de los fotones debe pasar, ya que esa es la fracción de la energía que se transmite. En consecuencia, una fracción $1 - (\cos\alpha)^2$ de los fotones debe ser absorbida. Pero si todos los fotones son idénticos, ¿por qué lo que le ocurre a un fotón no les ocurre a todos ellos?

La respuesta de la mecánica cuántica es que, en efecto, hay una pérdida de determinismo. Nadie puede predecir si un fotón pasará o será absorbido. Lo mejor que cualquiera puede hacer es predecir probabilidades. En este caso, habría una probabilidad $(\cos\alpha)^2$ de pasar y una probabilidad $1 - (\cos\alpha)^2$ de no pasar.

Se sugieren dos vías de escape. Quizás el polarizador no es realmente un objeto homogéneo y, dependiendo exactamente de dónde incide el fotón, o bien se absorbe o bien pasa. Los experimentos demuestran que no es así. Una posibilidad más intrigante fue sugerida por Einstein y otros. Una posible salida, afirmaban, era la existencia de variables ocultas. Los fotones, aunque aparentemente idénticos, tendrían otras propiedades ocultas, actualmente no comprendidas, que determinarían con certeza qué fotón pasa y cuál es absorbido. Las teorías de variables ocultas parecerían ser imposibles de comprobar, pero sorprendentemente sí pueden ponerse a prueba. Mediante el trabajo de John Bell y otros, los físicos han diseñado experimentos ingeniosos que descartan la mayoría de las versiones de las teorías de variables ocultas. Nadie ha logrado averiguar cómo restaurar el determinismo en la mecánica cuántica. Parece ser una tarea imposible.

Cuando intentamos describir fotones cuánticamente, podríamos usar funciones de onda, o de forma equivalente, el lenguaje de estados. Un fotón polarizado a lo largo de la dirección $\hat{x}$ no se representa mediante un campo eléctrico, sino que simplemente le damos un nombre a su estado:

$$|\text{fotón}; x\rangle. \qquad \text{(3.4)}$$

Aprenderemos las reglas necesarias para manipular tales objetos, pero por el momento puede pensar en ello como un vector en algún espacio todavía por definir. Otro estado de un fotón, o vector, es

$$|\text{fotón}; y\rangle, \qquad \text{(3.5)}$$

que representa un fotón polarizado a lo largo de $\hat{y}$. Estos estados son las funciones de onda que representan al fotón. Afirmamos ahora que los fotones del haz que está polarizado a lo largo de la dirección $\alpha$ están en un estado $|\text{fotón}; \alpha\rangle$ que puede escribirse como una superposición de los dos estados anteriores:

$$|\text{fotón}; \alpha\rangle = \cos\alpha\, |\text{fotón}; x\rangle + \sin\alpha\, |\text{fotón}; y\rangle. \qquad \text{(3.6)}$$

Esta ecuación debe compararse con (3.2). Aunque hay algunas similitudes —ambas son superposiciones—, una se refiere a campos eléctricos y la otra a «estados» de un único fotón. Cualquier fotón que emerja del polarizador estará necesariamente polarizado en la dirección $\hat{x}$ y, por lo tanto, estará en el estado

$$\text{Más allá del polarizador:} \quad |\text{fotón}; x\rangle. \qquad \text{(3.7)}$$

Esto puede compararse con (3.3), que con el factor $\cos\alpha$ lleva información sobre la amplitud de la onda. Aquí, para un único fotón, no hay lugar para tal factor.

En la famosa Quinta Conferencia Internacional Solvay de 1927, los físicos más notables del mundo se reunieron para discutir la teoría cuántica recién formulada. Diecisiete de los veintinueve asistentes fueron o llegaron a ser ganadores del Premio Nobel. Einstein, disgustado con la incertidumbre de la mecánica cuántica, pronunció la ahora famosa frase: «Dios no juega a los dados», a lo que Niels Bohr respondió, según se cuenta: «Einstein, deja de decirle a Dios lo que tiene que hacer». Bohr estaba dispuesto a aceptar la pérdida del determinismo; Einstein no.

## 4. Superposiciones cuánticas

Ya hemos discutido el concepto de linealidad: la idea de que la suma de dos soluciones que representan realidades físicas representa una nueva realidad física permitida. Esta superposición de soluciones tiene un significado directo en física clásica. En el caso del electromagnetismo, por ejemplo, si tenemos dos soluciones, cada una con su propio campo eléctrico y magnético, la solución «suma» se entiende de manera sencilla: su campo eléctrico es la suma de los campos eléctricos de las dos soluciones y su campo magnético es la suma de los campos magnéticos de las dos soluciones. En mecánica cuántica, como hemos explicado, la linealidad se cumple. La interpretación de una superposición, sin embargo, es muy sorprendente.

Un ejemplo interesante lo proporciona un interferómetro de Mach-Zehnder: un arreglo de divisores de haz, espejos y detectores usado por Ernst Mach y Ludwig Zehnder en la década de 1890 para estudiar la interferencia entre dos haces de luz.

Un divisor de haz, como su nombre indica, divide un haz incidente en dos haces, uno que se refleja en el divisor y otro que lo atraviesa. Nuestros divisores de haz estarán equilibrados: dividen un haz dado en dos haces de igual intensidad (Figura 3). La luz que rebota se llama haz reflejado, la luz que atraviesa se llama haz transmitido. El haz incidente puede incidir sobre el divisor desde arriba o desde abajo.

La configuración de Mach-Zehnder, mostrada en la Figura 4, tiene un divisor de haz izquierdo (BS1) y un divisor de haz derecho (BS2). En medio tenemos los dos espejos, M1 arriba y M2 abajo. Un haz entrante desde la izquierda es dividido por BS1 en dos haces, cada uno de los cuales incide sobre un espejo y luego es enviado a BS2. En BS2 los haces se recombinan y se envían a dos haces salientes que van hacia los detectores de fotones D0 y D1.

Es relativamente sencillo disponer los divisores de haz de modo que el haz entrante, tras dividirse en BS1 y recombinarse en BS2, emerja en el haz superior, que va hacia D0. En este arreglo, no llega luz en absoluto a D1. Esto requiere un efecto de interferencia preciso en BS2. Nótese que tenemos dos haces incidiendo sobre BS2; el haz superior se llama ‘a’ y el haz inferior se llama ‘b’. Dos contribuciones van hacia D0: la reflexión de ‘a’ en BS2 y la transmisión de ‘b’ en BS2. Estas dos contribuciones interfieren constructivamente para dar un haz que va hacia D0. También van dos contribuciones hacia D1: la transmisión de ‘a’ en BS2 y la reflexión de ‘b’ en BS2. Estas dos, en efecto, pueden disponerse para interferir destructivamente y así no dar ningún haz hacia D1.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes1_ES/fig3.png)

Figura 3: Un haz incidente que incide sobre un divisor de haz da como resultado un haz reflejado y un haz transmitido. Izquierda: haz incidente proveniente de arriba. Derecha: haz incidente proveniente de abajo.

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes1_ES/fig4.png)

Figura 4: Un interferómetro de Mach-Zehnder consta de dos divisores de haz BS1 y BS2, dos espejos M1 y M2, y dos detectores D0 y D1. Un haz incidente se divide en dos haces mediante BS1. Un haz recorre la rama superior, que contiene M1; el otro haz recorre la rama inferior, que contiene M2. Los haces de las dos ramas se recombinan en BS2 y luego se envían a los detectores. La configuración está preparada para producir una interferencia tal que todos los fotones incidentes terminen en el detector D0, y ninguno en D1.

Es instructivo pensar en el haz entrante como una secuencia de fotones que enviamos al interferómetro, uno a la vez. Esto muestra que, a nivel de fotones, la interferencia no es interferencia de un fotón con otro fotón. Cada fotón debe interferir consigo mismo para dar el resultado. En efecto, la interferencia entre dos fotones no es posible: la interferencia destructiva, por ejemplo, requeriría que dos fotones dieran como resultado ningún fotón, lo cual es imposible por conservación de la energía.

Por lo tanto, cada fotón hace la cosa muy extraña de atravesar ambas ramas del interferómetro. Cada fotón está en una superposición de dos estados: un estado en el que el fotón está en el haz superior o rama superior, sumado a un estado en el que el fotón está en el haz inferior o rama inferior. Así, el estado del fotón en el interferómetro es un estado curioso en el que el fotón parece estar haciendo dos cosas incompatibles al mismo tiempo.

La ecuación (3.6) es otro ejemplo de superposición cuántica. El estado del fotón tiene una componente a lo largo de un fotón polarizado en $x$ y una componente a lo largo de un fotón polarizado en $y$.

Cuando hablamos de una función de onda, también la llamamos a veces estado, porque la función de onda especifica el «estado» de nuestro sistema cuántico. También nos referimos a veces a los estados como vectores. Un estado cuántico puede no ser un vector como los vectores familiares en el espacio tridimensional, pero es un vector de todos modos, porque tiene sentido sumar estados y multiplicar estados por números. Del mismo modo que los vectores pueden sumarse, la linealidad garantiza que sumar funciones de onda o estados es algo con sentido. Al igual que cualquier vector puede escribirse como suma de otros vectores de muchas maneras distintas, haremos lo mismo con nuestros estados. Al escribir nuestro estado físico como sumas de otros estados, podemos aprender sobre las propiedades de nuestro estado.

Consideremos ahora dos estados $|A\rangle$ y $|B\rangle$. Supongamos, además, que al medir cierta propiedad $Q$ en el estado $|A\rangle$ la respuesta es siempre $a$, y que al medir la misma propiedad $Q$ en el estado $|B\rangle$ la respuesta es siempre $b$. Supongamos ahora que nuestro estado físico $|\Psi\rangle$ es la superposición

$$|\Psi\rangle = \alpha |A\rangle + \beta |B\rangle, \qquad \alpha, \beta \in \mathbb{C}. \qquad \text{(4.1)}$$

¿Qué ocurre ahora si medimos la propiedad $Q$ en el sistema descrito por el estado $|\Psi\rangle$? Podría parecer razonable que se obtuviera algún valor intermedio entre $a$ y $b$, pero eso no es lo que ocurre. Una medición de $Q$ dará como resultado $a$ o $b$. No hay una respuesta cierta, el determinismo clásico se pierde, pero la respuesta es siempre uno de estos dos valores y no uno intermedio. Los coeficientes $\alpha$ y $\beta$ en la superposición anterior afectan a las probabilidades con las que podemos obtener los dos valores posibles. De hecho, las probabilidades de obtener $a$ o $b$ son

$$\text{Probabilidad}(a) \sim |\alpha|^2, \qquad \text{Probabilidad}(b) \sim |\beta|^2. \qquad \text{(4.2)}$$

Puesto que las únicas dos posibilidades son medir $a$ o $b$, las probabilidades reales deben sumar uno y, por lo tanto, vienen dadas por

$$\text{Probabilidad}(a) = \frac{|\alpha|^2}{|\alpha|^2 + |\beta|^2}, \qquad \text{Probabilidad}(b) = \frac{|\beta|^2}{|\alpha|^2 + |\beta|^2}. \qquad \text{(4.3)}$$

Si obtenemos el valor $a$, mediciones repetidas inmediatas seguirían dando $a$, por lo que el estado tras la medición debe ser $|A\rangle$. Lo mismo ocurre para $b$, de modo que tenemos

$$\text{Tras medir } a \text{ el estado se convierte en } |\Psi\rangle = |A\rangle,$$

$$\text{Tras medir } b \text{ el estado se convierte en } |\Psi\rangle = |B\rangle. \qquad \text{(4.4)}$$

En mecánica cuántica se hace la siguiente suposición: superponer un estado consigo mismo no cambia la física, ni cambia el estado de manera no trivial. Puesto que superponer un estado consigo mismo simplemente cambia el número global que lo multiplica, tenemos que $\Psi$ y $\alpha\Psi$ representan la misma física para cualquier número complejo $\alpha$ distinto de cero. Así, dejando que $\cong$ represente equivalencia física,

$$|A\rangle \cong 2|A\rangle \cong i|A\rangle \cong -|A\rangle. \qquad \text{(4.5)}$$

Esta suposición es necesaria para verificar que el estado de polarización de un fotón tiene el número esperado de grados de libertad. La polarización de una onda plana, tal como se estudia en electromagnetismo, se describe mediante dos números reales. Para esto, consideremos una onda polarizada elípticamente, como se muestra en la Figura 5. En un punto dado, el vector de campo eléctrico traza una elipse cuya forma queda codificada por la razón $a/b$ de los semiejes (el primer parámetro real) y una inclinación codificada por el ángulo $\theta$ (el segundo parámetro real). Consideremos para ello un estado general de fotón formado por la superposición de los dos estados de polarización independientes $|\text{fotón}; x\rangle$ y $|\text{fotón}; y\rangle$:

$$\alpha|\text{fotón}; x\rangle + \beta|\text{fotón}; y\rangle, \qquad \alpha, \beta \in \mathbb{C}. \qquad \text{(4.6)}$$

A primera vista parece que tenemos dos parámetros complejos $\alpha$ y $\beta$, o de manera equivalente, cuatro parámetros reales. Pero como el factor global no importa, podemos multiplicar este estado por $1/\alpha$ para obtener el estado equivalente que codifica toda la física

$$|\text{fotón}; x\rangle + \frac{\beta}{\alpha}|\text{fotón}; y\rangle, \qquad \text{(4.7)}$$

lo que muestra que en realidad tenemos un único parámetro complejo, la razón $\beta/\alpha$. Esto equivale a dos parámetros reales, como se esperaba.

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes1_ES/fig5.png)

Figura 5: Parámetros que definen un estado polarizado elípticamente.

Hagamos otro ejemplo de superposición usando electrones. Los electrones son partículas con espín. Clásicamente, los imaginamos como pequeñas bolas girando alrededor de un eje que pasa por la propia partícula. Una vez fijado un eje, el electrón tiene dos y solo dos opciones: su rotación puede ser en sentido horario o antihorario alrededor del eje, pero en ambos casos gira a la misma velocidad fija. Estas formas opuestas de girar se llaman espín arriba y espín abajo a lo largo del eje (véase la Figura 6). El arriba y el abajo se refieren a la dirección del momento angular asociado con la rotación, y se indica mediante una flecha. Según la mecánica cuántica, y como se ha verificado en múltiples experimentos, surgen las mismas posibilidades, arriba o abajo, sea cual sea el eje que usemos para medir el espín del electrón.

Los físicos habitualmente configuran sistemas de coordenadas en el espacio eligiendo tres direcciones ortogonales, las direcciones de los ejes $x$, $y$ y $z$. Elijamos describir nuestros electrones con espín usando el eje $z$. Un posible estado de un electrón es tener espín arriba a lo largo del eje $z$. Tal estado se describe como $|\!\uparrow; z\rangle$, con una flecha apuntando hacia arriba, y la etiqueta $z$ indicando que la flecha de espín apunta a lo largo de la dirección creciente de $z$. Otro posible estado de un electrón es espín abajo a lo largo del eje $z$. Tal estado se describe como $|\!\downarrow; z\rangle$, con una flecha apuntando hacia abajo, indicando esta vez que el espín apunta a lo largo de la dirección decreciente de $z$. Si estas dos son realidades posibles, también lo sería el estado $|\Psi\rangle$ que representa la suma

$$|\Psi\rangle = |\!\uparrow; z\rangle + |\!\downarrow; z\rangle.$$

El estado $|\Psi\rangle$ está en una superposición de un estado de espín arriba y uno de espín abajo. ¿Qué tipo de física representa esta suma $|\Psi\rangle$? Representa un estado en el que una medición del espín a lo largo del eje $z$ daría como resultado dos posibles desenlaces con igual probabilidad: un electrón con espín arriba o un electrón con espín abajo. Puesto que solo podemos hablar de probabilidades, cualquier experimento debe implicar repetición hasta que las probabilidades puedan determinarse. Supongamos que tuviéramos un gran conjunto de tales electrones, todos ellos en el estado $|\Psi\rangle$ anterior. Al medir su espín a lo largo de $z$, uno a la vez, encontraríamos que aproximadamente la mitad de ellos giran hacia arriba a lo largo de $z$ y la otra mitad gira hacia abajo a lo largo de $z$. No hay manera de predecir qué opción se realizará al medir cada electrón. No es fácil imaginar la superposición, pero se puede intentar de la siguiente manera. Un electrón en el estado anterior se encuentra en un tipo de existencia diferente en la que es capaz tanto de girar hacia arriba a lo largo de $z$ como de girar hacia abajo a lo largo de $z$ simultáneamente. Se encuentra en un estado fantasmal e inquietante de este tipo, haciendo cosas incompatibles simultáneamente, hasta que se mide su espín. Una vez medido, el electrón debe elegir inmediatamente una de las dos opciones; siempre encontramos electrones girando hacia arriba o girando hacia abajo.

![Figura 6](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes1_ES/fig6.png)

Figura 6: Un electrón con espín a lo largo del eje $z$. Izquierda: se dice que el electrón tiene espín arriba a lo largo de $z$. Derecha: se dice que el electrón tiene espín abajo a lo largo de $z$. Las flechas hacia arriba y hacia abajo representan la dirección del momento angular asociado al electrón que gira.

Un crítico de la mecánica cuántica podría sugerir una explicación más simple para las observaciones anteriores. Él o ella afirmaría que el siguiente conjunto más simple produce resultados experimentales idénticos. En el conjunto del crítico tenemos un gran número de electrones, con el 50% de ellos en el estado $|\!\uparrow; z\rangle$ y el 50% de ellos en el estado $|\!\downarrow; z\rangle$. Entonces afirmaría, correctamente, que tal conjunto produciría las mismas mediciones de espín a lo largo de $z$ que el conjunto de esos esotéricos estados $|\Psi\rangle$. El nuevo conjunto podría ofrecer una explicación más simple del resultado sin tener que invocar superposiciones cuánticas.

La mecánica cuántica, sin embargo, permite otros experimentos que pueden distinguir entre el conjunto de nuestro amigable crítico y el conjunto de estados $|\Psi\rangle$. Aunque nos llevaría demasiado lejos explicarlo, si midiéramos el espín de los electrones en la dirección $x$, en lugar de la dirección $z$, los resultados serían diferentes en los dos conjuntos. En el conjunto de nuestro crítico encontraríamos el 50% de los electrones hacia arriba a lo largo de $x$ y el 50% de los electrones hacia abajo a lo largo de $x$. En nuestro conjunto de estados $|\Psi\rangle$, sin embargo, encontraríamos un resultado muy simple: todos los estados apuntando hacia arriba a lo largo de $x$. El conjunto del crítico no es equivalente a nuestro conjunto mecánico-cuántico. Así, se demuestra que el crítico está equivocado en su intento de mostrar que las superposiciones cuánticas no son necesarias.

## 5. Entrelazamiento

Cuando consideramos la superposición de estados de dos partículas podemos obtener el notable fenómeno llamado entrelazamiento mecánico-cuántico. Los estados entrelazados de dos partículas son aquellos en los que no podemos hablar por separado del estado de cada partícula. Las partículas están ligadas en un estado común en el que están entrelazadas entre sí.

Consideremos dos partículas que no interactúan. La partícula 1 podría estar en cualquiera de los estados

$$\{|u_1\rangle, |u_2\rangle, \ldots\}, \qquad \text{(5.1)}$$

mientras que la partícula 2 podría estar en cualquiera de los estados

$$\{|v_1\rangle, |v_2\rangle, \ldots\} \qquad \text{(5.2)}$$

Podría parecer razonable concluir que el estado del sistema completo, incluyendo la partícula 1 y la partícula 2, quedaría especificado indicando el estado de la partícula 1 y el estado de la partícula 2. Si ese fuera el caso, los posibles estados se escribirían como

$$|u_i\rangle \otimes |v_j\rangle, \qquad i, j \in \mathbb{N}, \qquad \text{(5.3)}$$

para alguna elección específica de $i$ y $j$ que especifican el estado de la partícula uno y de la partícula dos, respectivamente. Aquí hemos usado el símbolo $\otimes$, que significa producto tensorial, para combinar los dos estados en un único estado para todo el sistema. Estudiaremos $\otimes$ más adelante, pero por ahora podemos pensarlo como una especie de producto que se distribuye sobre la suma y obedece reglas simples, tal como sigue

$$(\alpha_1|u_1\rangle + \alpha_2|u_2\rangle) \otimes (\beta_1|v_1\rangle + \beta_2|v_2\rangle) = \alpha_1\beta_1 |u_1\rangle\otimes|v_1\rangle + \alpha_1\beta_2 |u_1\rangle\otimes|v_2\rangle$$

$$+ \alpha_2\beta_1 |u_2\rangle\otimes|v_1\rangle + \alpha_2\beta_2 |u_2\rangle\otimes|v_2\rangle. \qquad \text{(5.4)}$$

Los números pueden desplazarse a través del $\otimes$, pero el orden de los estados debe conservarse. El estado del lado izquierdo —desarrollado en el lado derecho— sigue siendo del tipo en el que combinamos un estado de la primera partícula $(\alpha_1|u_1\rangle + \alpha_2|u_2\rangle)$ con un estado de la segunda partícula $(\beta_1|v_1\rangle + \beta_2|v_2\rangle)$. Al igual que cualquiera de los estados listados en (5.3), este estado no está entrelazado.

Usando los estados en (5.3), sin embargo, podemos construir superposiciones más intrigantes. Consideremos la siguiente

$$|u_1\rangle \otimes |v_1\rangle + |u_2\rangle \otimes |v_2\rangle. \qquad \text{(5.5)}$$

Se dice que un estado de dos partículas está entrelazado si no puede escribirse en la forma factorizada $(\cdots)\otimes(\cdots)$, que nos permitiría describir el estado simplemente indicando el estado de cada partícula. Podemos ver fácilmente que el estado (5.5) no puede factorizarse. Si pudiera, tendría que ser con un producto como el indicado en (5.4). Claramente, involucrar estados como $|u_3\rangle$ o $|v_3\rangle$ que no aparecen en (5.5) no ayudaría. Para determinar las constantes $\alpha_1, \alpha_2, \beta_1, \beta_2$ comparamos el lado derecho de (5.4) con nuestro estado y concluimos que necesitamos

$$\alpha_1\beta_1 = 1, \quad \alpha_1\beta_2 = 0, \quad \alpha_2\beta_1 = 0, \quad \alpha_2\beta_2 = 1. \qquad \text{(5.6)}$$

Está claro que no hay solución aquí. La segunda ecuación, por ejemplo, requiere que $\alpha_1$ o $\beta_2$ sean cero. Tener $\alpha_1 = 0$ contradice la primera ecuación, y tener $\beta_2 = 0$ contradice la última ecuación. Esto confirma que el estado (5.5) es, en efecto, un estado entrelazado. No hay manera de describir el estado especificando un estado para cada una de las partículas.

Ilustremos la discusión anterior usando electrones y sus estados de espín. Consideremos un estado de dos electrones denotado como $|\!\uparrow\rangle \otimes |\!\downarrow\rangle$. Como indica la notación, el primer electrón, descrito por la primera flecha, está hacia arriba a lo largo de $z$, mientras que el segundo electrón, descrito por la segunda flecha, está hacia abajo a lo largo de $z$ (omitimos la etiqueta $z$ en el estado por brevedad). Este no es un estado entrelazado. Otro estado posible es aquel en el que hacen exactamente lo contrario: en $|\!\downarrow\rangle \otimes |\!\uparrow\rangle$ el primer electrón está hacia abajo y el segundo está hacia arriba. Este segundo estado tampoco está entrelazado. Se sigue entonces que, por superposición, podemos considerar el estado

$$|\!\uparrow\rangle \otimes |\!\downarrow\rangle + |\!\downarrow\rangle \otimes |\!\uparrow\rangle. \qquad \text{(5.7)}$$

Este es un estado entrelazado del par de electrones.

**Ejercicio.** Demuestre que el estado anterior no puede factorizarse y, por lo tanto, está efectivamente entrelazado.

En el estado (5.7), el primer electrón está hacia arriba a lo largo de $z$ si el segundo electrón está hacia abajo a lo largo de $z$ (primer término), o el primer electrón está hacia abajo a lo largo de $z$ si el segundo electrón está hacia arriba a lo largo de $z$ (segundo término). Hay una correlación entre los espines de las dos partículas; siempre apuntan en direcciones opuestas. Imaginemos que los dos electrones entrelazados están muy lejos el uno del otro: Alicia tiene un electrón del par en el planeta Tierra y Roberto tiene el otro electrón en la Luna. Nada de lo que conocemos conecta estas partículas, pero, sin embargo, los estados de los electrones están vinculados. Las mediciones que hacemos sobre las partículas separadas exhiben correlaciones. Supongamos que Alicia mide el espín del electrón en la Tierra. Si lo encuentra hacia arriba a lo largo de $z$, significa que se realiza el primer sumando de la superposición anterior, porque en ese sumando la primera partícula está hacia arriba. Como se discutió antes, el estado de las dos partículas se convierte inmediatamente en el del primer sumando. Esto significa que el electrón en la Luna pasará instantáneamente a la configuración de espín hacia abajo a lo largo de $z$, algo que podría confirmar Roberto, que está sentado en la Luna con esa partícula en su laboratorio. Este efecto sobre el electrón de Roberto ocurre antes de que un mensaje, transportado a la velocidad de la luz, pudiera llegar a la Luna informándole de que Alicia ha realizado una medición sobre la partícula terrestre y que el resultado fue espín hacia arriba. Por supuesto, los experimentos deben realizarse con un conjunto que contenga muchos pares de partículas, cada par en el mismo estado entrelazado anterior. La mitad de las veces el electrón en la Tierra se encontrará hacia arriba, con el electrón en la Luna hacia abajo, y la otra mitad de las veces el electrón en la Tierra se encontrará hacia abajo, con el electrón en la Luna hacia arriba.

Nuestro amigable crítico podría decir ahora, correctamente, que tales correlaciones entre las mediciones de espín a lo largo de $z$ podrían haberse producido preparando un conjunto convencional en el que el 50% de los pares están en el estado $|\!\uparrow\rangle \otimes |\!\downarrow\rangle$ y el otro 50% de los pares están en el estado $|\!\downarrow\rangle \otimes |\!\uparrow\rangle$. Tales objeciones fueron resueltas de manera concluyente en 1964 por John Bell, quien demostró que si Alicia y Roberto son capaces de medir el espín en tres direcciones arbitrarias, las correlaciones predichas por el estado cuántico entrelazado son diferentes de las correlaciones clásicas de cualquier conjunto convencional concebible. Las correlaciones cuánticas en estados entrelazados son muy sutiles y se necesitan experimentos sofisticados para mostrar que no son reproducibles como correlaciones clásicas. En efecto, los experimentos con estados entrelazados han confirmado la existencia de correlaciones cuánticas. El tipo de acción instantánea a distancia asociado con las mediciones sobre partículas entrelazadas bien separadas no conduce a paradojas ni, como podría parecer, a contradicciones con las ideas de la relatividad especial. No se pueden usar estados entrelazados mecánico-cuánticos para enviar información más rápido que la velocidad de la luz.

------------------------------------------------------------------------

*Sarah Geller transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

*Traducción al español generada con asistencia de IA a partir del original en inglés.*

------------------------------------------------------------------------

MIT OpenCourseWare

<https://ocw.mit.edu>

8.04 Física Cuántica I

Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.


---

<!-- MIT8.04_LecNotes20_21_ES.md -->

# Clases 20 y 21: Mecánica Cuántica en 3D y Potenciales Centrales

## Vídeos de esta clase (YouTube)

**Lección 20: Central potentials and angular momentum.**

- [Translation operator. Central potentials](https://www.youtube.com/watch?v=sPsDI0dICtc)
- [Angular momentum operators and their algebra](https://www.youtube.com/watch?v=xoCHe0mtxu0)
- [Commuting observables for angular momentum](https://www.youtube.com/watch?v=Mh8vUEStCQ8)
- [Simultaneous eigenstates and quantization of angular momentum](https://www.youtube.com/watch?v=lWTUcojZ_gQ)

**Lección 21: Legendre equation. Radial equation. Hydrogen atom 2-body problem.**

- [Associated Legendre functions and spherical harmonics](https://www.youtube.com/watch?v=Lt2Y6fLJ09Q)
- [Orthonormality of spherical harmonics](https://www.youtube.com/watch?v=gKSRrTik1SA)
- [Effective potential and boundary conditions at r=0](https://www.youtube.com/watch?v=_XDm2cxC-UU)
- [Hydrogen atom two-body problem](https://www.youtube.com/watch?v=7q32Wnm4dEw)

------------------------------------------------------------------------

*B. Zwiebach* *3 de mayo de 2016*

## Contenidos

1.  Ecuación de Schrödinger en 3D y momento angular
2.  El operador de momento angular
3.  Autoestados del momento angular
4.  La ecuación de onda radial

## 1. Ecuación de Schrödinger en 3D y momento angular

Hasta ahora hemos considerado varios operadores hermíticos: el operador de posición, el operador de momento y el operador de energía, o hamiltoniano. Estos operadores son observables y sus autovalores son los posibles resultados de medirlos sobre los estados. Aquí discutiremos otro operador: el momento angular. Es un operador vectorial, igual que el momento. Dará lugar a tres componentes, cada una de las cuales es un operador hermítico y por tanto una magnitud medible. La definición del operador de momento angular, como veremos, surge de su contraparte en mecánica clásica. Sin embargo, las propiedades del operador serán bastante nuevas y sorprendentes.

Habrá notado que el operador de momento tiene algo que ver con las traslaciones. En efecto, el operador de momento es una derivada en el espacio de coordenadas, y las derivadas están relacionadas con las traslaciones. La forma precisa en que esto ocurre es mediante la exponenciación. Consideremos una exponencial adecuada del operador de momento:

$$e^{\frac{i\hat{p}a}{\hbar}} , \qquad \text{(1.1)}$$

donde $a$ es una constante con unidades de longitud, lo que hace que el argumento de la exponencial sea adimensional. Consideremos ahora que este operador actúa sobre una función de onda $\psi(x)$

$$e^{\frac{i\hat{p}a}{\hbar}} \psi(x) = e^{a \frac{d}{dx}} \psi(x) , \qquad \text{(1.2)}$$

donde hemos simplificado el exponente. Expandiendo la exponencial obtenemos

$$e^{\frac{i\hat{p}a}{\hbar}} \psi(x) = \left( 1 + a\frac{d}{dx} + \frac{a^2}{2!}\frac{d^2}{dx^2} + \frac{a^3}{3!}\frac{d^3}{dx^3} + \ldots \right)\psi(x) ,$$

$$= \psi(x) + a\frac{d\psi}{dx} + \frac{a^2}{2!}\frac{d^2\psi}{dx^2} + \frac{a^3}{3!}\frac{d^3\psi}{dx^3} + \ldots = \psi(x+a) , \qquad \text{(1.3)}$$

ya que reconocemos la familiar expansión de Taylor. Este resultado significa que el operador $e^{\frac{i\hat{p}a}{\hbar}}$ desplaza la función de onda. De hecho la desplaza una distancia $-a$, ya que $\psi(x+a)$ es el desplazamiento de $\psi(x)$ por una distancia $-a$. Decimos que el operador de momento genera traslaciones. De manera similar, podremos mostrar que el operador de momento angular genera rotaciones. De nuevo, esto significa que exponenciales adecuadas del operador de momento angular actuando sobre funciones de onda las rotarán en el espacio.

El momento angular puede ser de tipo orbital, que es el caso familiar que ocurre cuando una partícula rota alrededor de algún punto fijo. Pero también puede ser momento angular de espín. Este es un tipo de momento angular bastante diferente y puede ser portado por partículas puntuales. Buena parte de la matemática del momento angular es válida tanto para el momento angular orbital como para el de espín.

Comencemos nuestro análisis del momento angular recordando que en tres dimensiones los operadores usuales $\hat{x}$ y $\hat{p}$ son operadores vectoriales:

$$\hat{p} = (\hat{p}_x, \hat{p}_y, \hat{p}_z) = \frac{\hbar}{i}\nabla = \frac{\hbar}{i}\left( \frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z} \right) .$$

$$\hat{x} = (\hat{x}, \hat{y}, \hat{z}) . \qquad \text{(1.4)}$$

Las relaciones de conmutación son las siguientes:

$$[\hat{x}, \hat{p}_x] = i\hbar ,$$

$$[\hat{y}, \hat{p}_y] = i\hbar , \qquad \text{(1.5)}$$

$$[\hat{z}, \hat{p}_z] = i\hbar .$$

¡Todos los demás conmutadores que involucran las tres coordenadas y los tres momentos son cero!

Consideremos una partícula representada por una función de onda tridimensional $\psi(x,y,z)$ que se mueve en un potencial tridimensional $V(\mathbf{r})$. La ecuación de Schrödinger toma la forma

$$-\frac{\hbar^2}{2m}\nabla^2 \psi(\mathbf{r}) + V(\mathbf{r})\psi(\mathbf{r}) = E\psi(\mathbf{r}) . \qquad \text{(1.6)}$$

Tenemos un potencial central si $V(\mathbf{r}) = V(r)$. Un potencial central no tiene dependencia angular, el valor del potencial depende únicamente de la distancia $r$ al origen. Un potencial central es esféricamente simétrico; las superficies de potencial constante son esferas centradas en el origen y por tanto es invariante bajo rotaciones. La ecuación anterior para un potencial central es

$$-\frac{\hbar^2}{2m}\nabla^2 \psi(\mathbf{r}) + V(r)\psi(\mathbf{r}) = E\psi(\mathbf{r}) . \qquad \text{(1.7)}$$

Esta ecuación será el objeto principal de nuestro estudio. Notemos que la función de onda es una función completa de $\mathbf{r}$; solo será invariante bajo rotaciones para los tipos más simples de soluciones. Dada la simetría rotacional del potencial, nos vemos llevados a expresar la ecuación de Schrödinger y las autofunciones de energía usando coordenadas esféricas.

En coordenadas esféricas, el laplaciano es

$$\nabla^2 \psi = (\nabla \cdot \nabla)\psi = \frac{1}{r}\frac{\partial^2}{\partial r^2}(r\psi) + \frac{1}{r^2}\left[ \frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left( \sin\theta \frac{\partial}{\partial\theta} \right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\varphi^2} \right]\psi . \qquad \text{(1.8)}$$

Por lo tanto la ecuación de Schrödinger para una partícula en un potencial central se convierte en

$$-\frac{\hbar^2}{2m}\left\{ \frac{1}{r}\frac{\partial^2}{\partial r^2}(r\psi) + \frac{1}{r^2}\left[ \frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left( \sin\theta \frac{\partial}{\partial\theta} \right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\varphi^2} \right] \right\}\psi + V(r)\psi = E\psi . \qquad \text{(1.9)}$$

En lo que sigue, nuestro objetivo será establecer dos hechos:

1.  La parte con dependencia angular del operador $\nabla^2$ puede identificarse como el cuadrado de la magnitud del operador de momento angular

$$\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left( \sin\theta \frac{\partial}{\partial\theta} \right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\varphi^2} = -\frac{L^2}{\hbar^2} \qquad \text{(1.10)}$$

donde

$$L^2 = \hat{L}_x \hat{L}_x + \hat{L}_y \hat{L}_y + \hat{L}_z \hat{L}_z . \qquad \text{(1.11)}$$

Esto implicará que la ecuación de Schrödinger se convierte en

$$-\frac{\hbar^2}{2m}\left[ \frac{1}{r}\frac{\partial^2}{\partial r^2}(r) - \frac{1}{r^2}\frac{L^2}{\hbar^2} \right]\psi + V(r)\psi = E\psi \qquad \text{(1.12)}$$

o desarrollando

$$-\frac{\hbar^2}{2m}\frac{1}{r}\frac{\partial^2}{\partial r^2}(r\psi) + \frac{L^2}{2mr^2}\psi + V(r)\psi = E\psi . \qquad \text{(1.13)}$$

1.  La ecuación (1.7) es la ecuación relevante para el problema de dos cuerpos cuando el potencial satisface

$$V(\mathbf{r}_1, \mathbf{r}_2) = V(|\mathbf{r}_1 - \mathbf{r}_2|) , \qquad \text{(1.14)}$$

es decir, si la energía potencial es simplemente una función de la distancia entre las partículas. Esto es cierto para la energía potencial electrostática entre el protón y el electrón que forman un átomo de hidrógeno. Por lo tanto, podremos tratar el átomo de hidrógeno como un problema de potencial central.

## 2. El operador de momento angular

Clásicamente estamos familiarizados con el momento angular, definido como el producto vectorial de $\mathbf{r}$ y $\mathbf{p}$: $\mathbf{L} = \mathbf{r} \times \mathbf{p}$. Por lo tanto tenemos

$$\mathbf{L} = (L_x, L_y, L_z) \equiv \mathbf{r} \times \mathbf{p} ,$$

$$L_x = yp_z - zp_y ,$$

$$L_y = zp_x - xp_z , \qquad \text{(2.1)}$$

$$L_z = xp_y - yp_x .$$

Usamos las relaciones anteriores para definir el operador cuántico de momento angular $\hat{\mathbf{L}}$ y sus componentes, los operadores $(\hat{L}_x, \hat{L}_y, \hat{L}_z)$:

$$\hat{\mathbf{L}} = (\hat{L}_x, \hat{L}_y, \hat{L}_z) ,$$

$$\hat{L}_x = \hat{y}\hat{p}_z - \hat{z}\hat{p}_y ,$$

$$\hat{L}_y = \hat{z}\hat{p}_x - \hat{x}\hat{p}_z , \qquad \text{(2.2)}$$

$$\hat{L}_z = \hat{x}\hat{p}_y - \hat{y}\hat{p}_x .$$

Al elaborar esta definición no encontramos ambigüedades de ordenamiento. Cada operador de momento angular es la diferencia de dos términos, cada término consistente en el producto de una coordenada y un momento. Pero notemos que en todos los casos se trata de una coordenada y un momento a lo largo de ejes distintos, por lo que conmutan. Si hubiéramos escrito $\hat{L}_x = \hat{p}_z\hat{y} - \hat{p}_y\hat{z}$, no habría importado, es lo mismo que el $\hat{L}_x$ de arriba. Es sencillo comprobar que los operadores de momento angular son hermíticos. Tomemos $\hat{L}_x$, por ejemplo. Recordando que para dos operadores cualesquiera $(AB)^\dagger = B^\dagger A^\dagger$ tenemos

$$(\hat{L}_x)^\dagger = (\hat{y}\hat{p}_z - \hat{z}\hat{p}_y)^\dagger = (\hat{y}\hat{p}_z)^\dagger - (\hat{z}\hat{p}_y)^\dagger = \hat{p}_z^\dagger \hat{y}^\dagger - \hat{p}_y^\dagger \hat{z}^\dagger . \qquad \text{(2.3)}$$

Dado que todas las coordenadas y momentos son operadores hermíticos, tenemos

$$(\hat{L}_x)^\dagger = \hat{p}_z\hat{y} - \hat{p}_y\hat{z} = \hat{y}\hat{p}_z - \hat{z}\hat{p}_y = \hat{L}_x , \qquad \text{(2.4)}$$

donde hemos movido los momentos a la derecha de las coordenadas en virtud de conmutadores nulos. Los otros dos operadores de momento angular también son hermíticos, así que tenemos

$$\hat{L}_x^\dagger = \hat{L}_x , \qquad \hat{L}_y^\dagger = \hat{L}_y , \qquad \hat{L}_z^\dagger = \hat{L}_z . \qquad \text{(2.5)}$$

Todos los operadores de momento angular son observables.

Dado un conjunto de operadores hermíticos, es natural preguntarse cuáles son sus conmutadores. Este cálculo nos permite ver si podemos medirlos simultáneamente. Calculemos el conmutador de $\hat{L}_x$ con $\hat{L}_y$:

$$[\hat{L}_x, \hat{L}_y] = [\hat{y}\hat{p}_z - \hat{z}\hat{p}_y, \hat{z}\hat{p}_x - \hat{x}\hat{p}_z] \qquad \text{(2.6)}$$

Vemos ahora que estos términos dejan de conmutar solo porque $\hat{z}$ y $\hat{p}_z$ no conmutan. De hecho, el primer término de $\hat{L}_x$ solo deja de conmutar con el primer término de $\hat{L}_y$. Igualmente, el segundo término de $\hat{L}_x$ solo deja de conmutar con el segundo término de $\hat{L}_y$. Por lo tanto

$$[\hat{L}_x, \hat{L}_y] = [\hat{y}\hat{p}_z, \hat{z}\hat{p}_x] + [\hat{z}\hat{p}_y, \hat{x}\hat{p}_z]$$

$$= [\hat{y}\hat{p}_z, \hat{z}]\hat{p}_x + \hat{x}[\hat{z}\hat{p}_y, \hat{p}_z]$$

$$= \hat{y}[\hat{p}_z, \hat{z}]\hat{p}_x + \hat{x}[\hat{z}, \hat{p}_z]\hat{p}_y \qquad \text{(2.7)}$$

$$= \hat{y}(-i\hbar)\hat{p}_x + \hat{x}(i\hbar)\hat{p}_y$$

$$= i\hbar(\hat{x}\hat{p}_y - \hat{y}\hat{p}_x) .$$

Ahora reconocemos que el operador en el lado derecho final es $\hat{L}_z$ y por tanto,

$$[\hat{L}_x, \hat{L}_y] = i\hbar \hat{L}_z . \qquad \text{(2.8)}$$

Las relaciones de conmutación básicas son completamente cíclicas, como se ilustra en la figura 1. En cualquier relación de conmutación podemos ciclar los operadores de posición como en $\hat{x} \to \hat{y} \to \hat{z} \to \hat{x}$ y los operadores de momento como en $\hat{p}_x \to \hat{p}_y \to \hat{p}_z \to \hat{p}_x$ y obtendremos otra relación de conmutación consistente. También puede verse que este ciclado lleva $\hat{L}_x \to \hat{L}_y \to \hat{L}_z \to \hat{L}_x$, observando (2.2). Por lo tanto afirmamos que no necesitamos calcular conmutadores de momento angular adicionales, y (2.8) conduce a

$$[\hat{L}_x, \hat{L}_y] = i\hbar \hat{L}_z ,$$

$$[\hat{L}_y, \hat{L}_z] = i\hbar \hat{L}_x , \qquad \text{(2.9)}$$

$$[\hat{L}_z, \hat{L}_x] = i\hbar \hat{L}_y .$$

Este es el conjunto completo de conmutadores de los operadores de momento angular. El conjunto se conoce como el álgebra del momento angular. Notemos que si bien los operadores $\hat{\mathbf{L}}$ se definieron en términos de coordenadas y momentos, la respuesta final para los conmutadores no involucra ni coordenadas ni momentos: ¡los conmutadores de momentos angulares dan momentos angulares! Los operadores $\hat{\mathbf{L}}$ a veces se denominan momento angular orbital, para distinguirlos de los operadores de momento angular de espín. Los operadores de momento angular de espín $\hat{S}_x$, $\hat{S}_y$ y $\hat{S}_z$ no pueden escribirse en términos de coordenadas y momentos. Son entidades más abstractas; de hecho su representación más simple es como ¡matrices de dos por dos! Aun así, al ser momentos angulares, satisfacen exactamente la misma álgebra que sus primos orbitales. Tenemos

$$[\hat{S}_x, \hat{S}_y] = i\hbar \hat{S}_z ,$$

$$[\hat{S}_y, \hat{S}_z] = i\hbar \hat{S}_x , \qquad \text{(2.10)}$$

$$[\hat{S}_z, \hat{S}_x] = i\hbar \hat{S}_y .$$

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes20_21_ES/fig1.png)

Figura 1: Las relaciones de conmutación del momento angular satisfacen la ciclicidad.

Hemos visto que el conmutador $[\hat{x}, \hat{p}] = i\hbar$ está asociado al hecho de que no podemos tener autoestados simultáneos de posición y de momento. Veamos ahora qué nos dicen los conmutadores de los operadores $\hat{\mathbf{L}}$. En particular: ¿podemos tener autoestados simultáneos de $\hat{L}_x$ y $\hat{L}_y$? Resulta que la respuesta es no, no podemos. Lo demostramos de la siguiente manera. Supongamos que existe una función de onda $\varphi_0$ que es simultáneamente autoestado de $\hat{L}_x$ y $\hat{L}_y$,

$$\hat{L}_x \varphi_0 = \lambda_x \varphi_0 ,$$

$$\hat{L}_y \varphi_0 = \lambda_y \varphi_0 . \qquad \text{(2.11)}$$

Haciendo actuar la primera identidad de conmutación de (2.9) sobre $\varphi_0$ tenemos

$$i\hbar \hat{L}_z \varphi_0 = [\hat{L}_x, \hat{L}_y]\varphi_0 = \hat{L}_x \hat{L}_y \varphi_0 - \hat{L}_y \hat{L}_x \varphi_0$$

$$= \hat{L}_x \lambda_y \varphi_0 - \hat{L}_y \lambda_x \varphi_0 \qquad \text{(2.12)}$$

$$= (\lambda_x \lambda_y - \lambda_y \lambda_x)\varphi_0 = 0 ,$$

lo que muestra que $\hat{L}_z \varphi_0 = 0$. Pero esto no es todo; mirando los otros conmutadores del álgebra de momento angular vemos que también se anulan al actuar sobre $\varphi_0$ y, como resultado, $\lambda_x$ y $\lambda_y$ deben ser cero:

$$[\hat{L}_y, \hat{L}_z]\varphi_0 = i\hbar \underbrace{\hat{L}_x \varphi_0}_{0} = i\hbar\, \lambda_x \varphi_0 = 0 \implies \lambda_x = 0 ,$$

$$[\hat{L}_z, \hat{L}_x]\varphi_0 = i\hbar \underbrace{\hat{L}_y \varphi_0}_{0} = i\hbar\, \lambda_y \varphi_0 = 0 \implies \lambda_y = 0 . \qquad \text{(2.13)}$$

En definitiva, suponer que $\varphi_0$ es un autoestado simultáneo de $\hat{L}_x$ y $\hat{L}_y$ ha llevado a $\hat{L}_x \varphi_0 = \hat{L}_y \varphi_0 = \hat{L}_z \varphi_0 = 0$. El estado es aniquilado por todos los operadores de momento angular. Esta situación trivial no es muy interesante. Hemos aprendido que es imposible encontrar estados que sean autoestados simultáneos no triviales de dos cualesquiera de los operadores de momento angular.

Para operadores hermíticos que conmutan, no hay problema en encontrar autoestados simultáneos. De hecho, los operadores hermíticos que conmutan siempre tienen un conjunto completo de autoestados simultáneos. Supongamos que elegimos $\hat{L}_z$ como uno de los operadores que queremos medir. ¿Podemos ahora encontrar un segundo operador hermítico que conmute con él? La respuesta es sí. Resulta que $L^2$, definido en (1.11), conmuta con $\hat{L}_z$ y es una elección interesante para un segundo operador. En efecto, comprobamos rápidamente

$$[\hat{L}_z, L^2] = [\hat{L}_z, \hat{L}_x\hat{L}_x] + [\hat{L}_z, \hat{L}_y\hat{L}_y]$$

$$= [\hat{L}_z, \hat{L}_x]\hat{L}_x + \hat{L}_x[\hat{L}_z, \hat{L}_x] + [\hat{L}_z, \hat{L}_y]\hat{L}_y + \hat{L}_y[\hat{L}_z, \hat{L}_y]$$

$$= i\hbar \hat{L}_y \hat{L}_x + i\hbar \hat{L}_x \hat{L}_y - i\hbar \hat{L}_x \hat{L}_y - i\hbar \hat{L}_x \hat{L}_y \qquad \text{(2.14)}$$

$$= 0 .$$

Así que deberíamos poder encontrar autoestados simultáneos tanto de $\hat{L}_z$ como de $L^2$. Haremos esto en breve. El operador $L^2$ es un operador de Casimir, lo que significa que conmuta con todos los operadores de momento angular. Al igual que conmuta con $\hat{L}_z$, también conmuta con $\hat{L}_x$ y $\hat{L}_y$.

Para entender mejor los operadores de momento angular, escribámoslos en coordenadas esféricas. Para esto necesitamos la relación entre $(r,\theta,\varphi)$ y las coordenadas cartesianas $(x,y,z)$:

$$x = r\sin\theta\cos\varphi , \qquad r = \sqrt{x^2+y^2+z^2} , \qquad \theta = \cos^{-1}\left(\frac{z}{r}\right) ,$$

$$y = r\sin\theta\sin\varphi , \qquad \varphi = \tan^{-1}\left(\frac{y}{x}\right) , \qquad \text{(2.15)}$$

$$z = r\cos\theta .$$

Hemos insinuado el hecho de que los operadores de momento angular generan rotaciones. En coordenadas esféricas, las rotaciones en torno al eje $z$ son las más simples: cambian $\varphi$ pero dejan invariante $\theta$. Ambas rotaciones en torno a los ejes $x$ e $y$ cambian tanto $\theta$ como $\varphi$. Por tanto podemos esperar que $\hat{L}_z$ sea simple en coordenadas esféricas. Usando la definición $\hat{L}_z = \hat{x}\hat{p}_y - \hat{y}\hat{p}_x$ tenemos

$$\hat{L}_z = \frac{\hbar}{i}\left( x\frac{\partial}{\partial y} - y\frac{\partial}{\partial x} \right) . \qquad \text{(2.16)}$$

Notemos que esto está relacionado con $\frac{\partial}{\partial\varphi}$ ya que, por la regla de la cadena,

$$\frac{\partial}{\partial\varphi} = \frac{\partial y}{\partial\varphi}\frac{\partial}{\partial y} + \frac{\partial x}{\partial\varphi}\frac{\partial}{\partial x} + \frac{\partial z}{\partial\varphi}\frac{\partial}{\partial z} = x\frac{\partial}{\partial y} - y\frac{\partial}{\partial x} , \qquad \text{(2.17)}$$

donde usamos (2.15) para evaluar las derivadas parciales. Usando las últimas dos ecuaciones podemos identificar

$$\hat{L}_z = \frac{\hbar}{i}\frac{\partial}{\partial\varphi} . \qquad \text{(2.18)}$$

Esta es una representación muy simple y útil. Confirma la interpretación de que $\hat{L}_z$ genera rotaciones alrededor del eje $z$, ya que tiene que ver con cambios en $\varphi$. Notemos que $\hat{L}_z$ es como un momento a lo largo del “círculo” definido por la coordenada $\varphi$ ($\varphi = \varphi + 2\pi$). Los demás operadores de momento angular son un poco más complicados. Un cálculo más largo muestra lo que sugerimos antes, que

$$-\frac{\hat{L}^2}{\hbar^2} = \frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left( \sin\theta \frac{\partial}{\partial\theta} \right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\varphi^2} . \qquad \text{(2.19)}$$

## 3. Autoestados del momento angular

Demostramos antes que los operadores hermíticos $\hat{L}_z$ y $L^2$ conmutan. Nuestro objetivo ahora es construir las autofunciones simultáneas de estos operadores. Serán funciones de $\theta$ y $\varphi$ y las llamaremos $\psi_{\ell m}(\theta,\varphi)$. Las condiciones para que sean autofunciones son

$$\hat{L}_z \psi_{\ell m} = \hbar m\, \psi_{\ell m} , \qquad m \in \mathbb{R}$$

$$\hat{L}^2 \psi_{\ell m} = \hbar^2 \ell(\ell+1)\, \psi_{\ell m} , \qquad \ell \in \mathbb{R} . \qquad \text{(3.1)}$$

Como corresponde a operadores hermíticos, los autovalores son reales. Tanto $m$ como $\ell$ son adimensionales; hay un $\hbar$ en el autovalor de $\hat{L}_z$ porque el momento angular tiene unidades de $\hbar$. Para el autovalor de $\hat{L}^2$ tenemos un $\hbar^2$. Notemos que hemos escrito el autovalor de $\hat{L}^2$ como $\ell(\ell+1)$ y para $\ell$ real esto siempre es mayor o igual que $-1/4$. De hecho, $\ell(\ell+1)$ va de cero a infinito conforme $\ell$ va de cero a infinito. Podemos mostrar que los autovalores de $\hat{L}^2$ no pueden ser negativos. Para esto primero afirmamos que

$$\langle \psi, \hat{L}^2 \psi \rangle \geq 0 , \qquad \text{(3.2)}$$

y tomando $\psi$ como una autofunción normalizada con autovalor $\lambda$ de $\hat{L}^2$ vemos inmediatamente que lo anterior da $\langle \psi, \lambda\psi \rangle = \lambda \geq 0$, como deseábamos. Para probar la ecuación anterior simplemente expandimos y usamos hermiticidad

$$\langle \psi, \hat{L}^2 \psi \rangle = \langle \psi, \hat{L}_x^2 \psi \rangle + \langle \psi, \hat{L}_y^2 \psi \rangle + \langle \psi, \hat{L}_z^2 \psi \rangle$$

$$= \langle \hat{L}_x \psi, \hat{L}_x \psi \rangle + \langle \hat{L}_y \psi, \hat{L}_y \psi \rangle + \langle \hat{L}_z \psi, \hat{L}_z \psi \rangle \geq 0 , \qquad \text{(3.3)}$$

porque cada uno de los tres sumandos es mayor o igual que cero.

Resolvamos ahora la primera ecuación de autovalores en (3.1) usando la representación en coordenadas (2.18) del operador $\hat{L}_z$:

$$\frac{\hbar}{i}\frac{\partial \psi_{\ell m}}{\partial \varphi} = \hbar m \psi_{\ell m} \;\; \to \;\; \frac{\partial \psi_{\ell m}}{\partial \varphi} = im\, \psi_{\ell m} . \qquad \text{(3.4)}$$

Esto determina la dependencia en $\varphi$ de la solución y escribimos

$$\psi_{\ell m}(\theta,\varphi) = e^{im\varphi}\, P_\ell^m(\theta) , \qquad \text{(3.5)}$$

donde la función $P_\ell^m(\theta)$ recoge la dependencia en $\theta$, todavía no determinada, de la autofunción $\psi_{\ell m}$. Exigiremos que $\psi_{\ell m}$ esté definida de forma única como función de los ángulos, y esto requiere que

$$\psi_{\ell m}(\theta, \varphi + 2\pi) = \psi_{\ell m}(\theta,\varphi) . \qquad \text{(3.6)}$$

*(Se podría haber intentado exigir que, tras un incremento de $2\pi$ en $\varphi$, la función de onda cambiara de signo, pero esto no conduce a un conjunto consistente de $\psi_{\ell m}$.)*

No hay una condición análoga para $\theta$. La condición anterior requiere que

$$e^{im(\varphi+2\pi)} = e^{im\varphi} \;\; \to \;\; e^{2\pi i m} = 1 . \qquad \text{(3.7)}$$

Esta ecuación implica que $m$ debe ser un entero:

$$m \in \mathbb{Z} . \qquad \text{(3.8)}$$

Esto completa nuestro análisis de la primera ecuación de autovalores. La segunda ecuación de autovalores en (3.1), usando nuestra expresión (2.19) para $\hat{L}^2$, da

$$-\hbar^2 \left[ \frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left( \sin\theta \frac{\partial}{\partial\theta} \right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\varphi^2} \right] \psi_{\ell m} = \hbar^2 \ell(\ell+1) \psi_{\ell m} . \qquad \text{(3.9)}$$

Multiplicamos por $\sin^2\theta$ y cancelamos $\hbar^2$ para obtener

$$\left[ \sin\theta \frac{\partial}{\partial\theta}\left( \sin\theta \frac{\partial}{\partial\theta} \right) + \frac{\partial^2}{\partial\varphi^2} \right]\psi_{\ell m} = -\ell(\ell+1)\sin^2\theta\, \psi_{\ell m} . \qquad \text{(3.10)}$$

Usando $\psi_{\ell m} = e^{im\varphi}P_\ell^m(\theta)$ podemos evaluar la acción de $\frac{\partial^2}{\partial\varphi^2}$ sobre $\psi_{\ell m}$ y luego cancelar el factor común $e^{im\varphi}$ para llegar a la ecuación diferencial

$$\sin\theta \frac{d}{d\theta}\left( \sin\theta \frac{dP_\ell^m}{d\theta} \right) - m^2 P_\ell^m = -\ell(\ell+1) P_\ell^m \sin^2\theta , \qquad \text{(3.11)}$$

o, equivalentemente,

$$\sin\theta \frac{d}{d\theta}\left( \sin\theta \frac{dP_\ell^m}{d\theta} \right) + \left[ \ell(\ell+1)\sin^2\theta - m^2 \right] P_\ell^m = 0 . \qquad \text{(3.12)}$$

Queremos dejar claro ahora que podemos ver a $P_\ell^m$ como una función de $\cos\theta$ escribiendo la ecuación diferencial en términos de $x = \cos\theta$. En efecto, esto da

$$\frac{d}{d\theta} = \frac{dx}{d\theta}\frac{d}{dx} = -\sin\theta \frac{d}{dx} \;\; \to \;\; \sin\theta \frac{d}{d\theta} = -(1-x^2)\frac{d}{dx} . \qquad \text{(3.13)}$$

La ecuación diferencial se convierte en

$$(1-x^2) \frac{d}{dx}\left[ (1-x^2) \frac{dP_\ell^m}{dx} \right] + \left[ \ell(\ell+1)(1-x^2) - m^2 \right] P_\ell^m(x) = 0 , \qquad \text{(3.14)}$$

y dividiendo por $1-x^2$ obtenemos la forma final:

$$\frac{d}{dx}\left[ (1-x^2) \frac{dP_\ell^m}{dx} \right] + \left[ \ell(\ell+1) - \frac{m^2}{1-x^2} \right] P_\ell^m(x) = 0 . \qquad \text{(3.15)}$$

Las $P_\ell^m(x)$ se llaman funciones asociadas de Legendre. No son polinomios. Todo lo que sabemos en este punto es que $m$ es un entero. Pronto descubriremos que $\ell$ es un entero no negativo y que, para un valor dado de $\ell$, hay un rango de valores posibles de $m$.

Para averiguar sobre $\ell$ consideramos la ecuación anterior para $m=0$. En ese caso escribimos $P_\ell(x) \equiv P_\ell^0(x)$ y las $P_\ell(x)$ deben satisfacer

$$\frac{d}{dx}\left[ (1-x^2)\frac{dP_\ell}{dx} \right] + \ell(\ell+1) P_\ell(x) = 0 . \qquad \text{(3.16)}$$

Esta es la ecuación diferencial de Legendre. Intentamos encontrar una solución en serie escribiendo

$$P_\ell(x) = \sum_{k=0}^{\infty} a_k x^k , \qquad \text{(3.17)}$$

suponiendo que $P_\ell(x)$ es regular en $x=0$, como conviene que sea. Sustituyendo esto en la ecuación diferencial obtenemos que la anulación del coeficiente de $x^k$ requiere:

$$(k+1)(k+2)a_{k+2} + \left[ \ell(\ell+1) - k(k+1) \right] a_k = 0 . \qquad \text{(3.18)}$$

Equivalentemente, tenemos

$$\frac{a_{k+2}}{a_k} = -\frac{\ell(\ell+1)-k(k+1)}{(k+1)(k+2)} . \qquad \text{(3.19)}$$

El comportamiento de los coeficientes para $k$ grande es tal que, a menos que la serie termine, $P_\ell$ diverge en $x=\pm 1$ (dado que $x=\cos\theta$, esto corresponde a $\theta = 0, \pi$). Para que la serie termine, debemos tener $\ell(\ell+1) = k(k+1)$ para algún entero $k \geq 0$. Simplemente podemos elegir $\ell = k$ de modo que $a_{k+2}=0$, haciendo de $P_k(x)$ un polinomio de grado $k$. Hemos aprendido así que los valores posibles de $\ell$ son

$$\ell = 0, 1, 2, 3, \ldots \qquad \text{(3.20)}$$

¡Esto es cuantización! Al igual que los valores de $m$ están cuantizados, también lo están los valores de $\ell$. Los polinomios de Legendre $P_\ell(x)$ están dados por la fórmula de Rodrigues:

$$P_\ell(x) = \frac{1}{2^\ell \ell!} \frac{d^\ell}{dx^\ell}\left( x^2 - 1 \right)^\ell . \qquad \text{(3.21)}$$

Los polinomios de Legendre tienen una función generatriz agradable

$$\sum_{\ell=0}^{\infty} P_\ell(x)\, s^\ell = \frac{1}{\sqrt{1-2xs+s^2}} . \qquad \text{(3.22)}$$

Algunos ejemplos son

$$P_0(x) = 1 , \qquad P_1(x) = x , \qquad P_2(x) = \frac{1}{2}\left( 3x^2 - 1 \right) . \qquad \text{(3.23)}$$

$P_\ell(x)$ es un polinomio de grado $\ell$ de paridad definida.

Habiendo resuelto la ecuación para $m=0$, debemos ahora discutir la ecuación general para $P_\ell^m(x)$. La ecuación diferencial involucra $m^2$ y no $m$, así que podemos tomar las soluciones para $m$ y $-m$ como iguales. Se puede mostrar que tomar $|m|$ derivadas de los polinomios de Legendre da una solución para $P_\ell^m(x)$:

$$P_\ell^m(x) = (1-x^2)^{|m|/2} \frac{d^{|m|}}{dx^{|m|}} P_\ell(x) . \qquad \text{(3.24)}$$

Como $P_\ell$ es un polinomio de grado $\ell$, la expresión anterior da un resultado no nulo solo para $|m| \leq \ell$. Así tenemos soluciones para

$$-\ell \leq m \leq \ell . \qquad \text{(3.25)}$$

Es posible probar que no existen otras soluciones. Se puede pensar en las autofunciones $\psi_{\ell m}$ como determinadas primero por el entero $\ell$ y, para un $\ell$ fijo, hay $2\ell+1$ elecciones de $m$: $-\ell, -\ell+1, \ldots, \ell$.

Nuestras autofunciones $\psi_{\ell m}$, con una normalización adecuada, se llaman los armónicos esféricos $Y_{\ell m}(\theta,\varphi)$. Los armónicos esféricos correctamente normalizados para $m \geq 0$ son

$$Y_{\ell,m}(\theta,\varphi) \equiv \sqrt{ \frac{2\ell+1}{4\pi} \frac{(\ell-m)!}{(\ell+m)!} } (-1)^m e^{im\varphi} P_\ell^m(\cos\theta) . \qquad \text{(3.26)}$$

Para $m<0$, usamos

$$Y_{\ell,m}(\theta,\varphi) = (-1)^m \left[ Y_{\ell,-m}(\theta,\varphi) \right]^* . \qquad \text{(3.27)}$$

Así tenemos

$$\hat{L}_z Y_{\ell m} = \hbar m\, Y_{\ell m} ,$$

$$\hat{L}^2 Y_{\ell m} = \hbar^2 \ell(\ell+1)\, Y_{\ell m} . \qquad \text{(3.28)}$$

Los primeros armónicos esféricos son

$$Y_{0,0}(\theta,\varphi) = \frac{1}{\sqrt{4\pi}} \qquad \text{(3.29)}$$

$$Y_{1,\pm 1}(\theta,\varphi) = \mp \sqrt{\frac{3}{8\pi}}\, e^{\pm i\varphi}\sin\theta = \mp \sqrt{\frac{3}{8\pi}}\, \frac{x\pm iy}{r} \qquad \text{(3.30)}$$

$$Y_{1,0}(\theta,\varphi) = \sqrt{\frac{3}{4\pi}}\cos\theta = \sqrt{\frac{3}{4\pi}}\, \frac{z}{r} . \qquad \text{(3.31)}$$

Al ser autoestados de operadores hermíticos con autovalores distintos, los armónicos esféricos con subíndices $\ell$ y $m$ diferentes son automáticamente ortogonales. El complicado factor de normalización es necesario para que tengan norma unitaria. Los armónicos esféricos forman un conjunto ortonormal con respecto a la integración sobre el ángulo sólido. Esta integración puede escribirse de varias formas:

$$\int d\Omega \cdots = \int_0^{2\pi} d\varphi \int_{\theta=0}^{\pi} d\theta \sin\theta \cdots = \int_0^{2\pi} d\varphi \int_{-1}^{1} d(\cos\theta) \cdots \qquad \text{(3.32)}$$

La afirmación de que los armónicos esféricos forman un conjunto ortonormal con respecto a esta integración significa que

$$\int d\Omega\, Y_{\ell',m'}^*(\theta,\varphi)\, Y_{\ell,m}(\theta,\varphi) = \delta_{\ell,\ell'}\, \delta_{m,m'} . \qquad \text{(3.33)}$$

## 4. La ecuación de onda radial

Escribamos ahora un ansatz para la solución de la ecuación de Schrödinger. Para esto tomamos el producto de una función puramente radial $R_{E\ell}(r)$ y un armónico esférico

$$\psi(r,\theta,\varphi) = R_{E\ell}(r)\, Y_{\ell,m}(\theta,\varphi) . \qquad \text{(4.1)}$$

Hemos puesto subíndices $E$ y $\ell$ para la función radial. No incluimos $m$, porque, como veremos, la ecuación para $R$ no depende de $m$. Podemos ahora insertar esto en la ecuación de Schrödinger (1.13)

$$-\frac{\hbar^2}{2m}\frac{1}{r}\frac{\partial^2}{\partial r^2}\left( r R_{E\ell} Y_{\ell m} \right) + \frac{\hat{L}^2}{2mr^2} R_{E\ell} Y_{\ell m} + V(r) R_{E\ell} Y_{\ell m} = E R_{E\ell} Y_{\ell m} . \qquad \text{(4.2)}$$

Dado que los armónicos esféricos son autoestados de $\hat{L}^2$ podemos simplificar la ecuación para obtener

$$-\frac{\hbar^2}{2m}\frac{1}{r}\frac{d^2(rR_{E\ell})}{dr^2} Y_{\ell m} + \frac{\hbar^2 \ell(\ell+1)}{2mr^2} R_{E\ell} Y_{\ell m} + V(r) R_{E\ell} Y_{\ell m} = E R_{E\ell} Y_{\ell m} . \qquad \text{(4.3)}$$

Cancelando el armónico esférico común y multiplicando por $r$ obtenemos una ecuación puramente radial

$$-\frac{\hbar^2}{2m}\frac{d^2(rR_{E\ell})}{dr^2} + \frac{\hbar^2 \ell(\ell+1)}{2mr^2}(rR_{E\ell}) + V(r)(rR_{E\ell}) = E(rR_{E\ell}) , \qquad \text{(4.4)}$$

Ahora es conveniente definir

$$u_{E\ell}(r) \equiv r R_{E\ell}(r) . \qquad \text{(4.5)}$$

Esto nos permite reescribir toda la ecuación diferencial como

$$-\frac{\hbar^2}{2m}\frac{d^2 u_{E\ell}}{dr^2} + \left[ V(r) + \frac{\hbar^2 \ell(\ell+1)}{2mr^2} \right] u_{E\ell} = E u_{E\ell} . \qquad \text{(4.6)}$$

Esto se llama la ecuación radial. Se parece a la familiar ecuación de Schrödinger independiente del tiempo en una dimensión, pero con un potencial efectivo

$$V_{\text{eff}}(r) = V(r) + \frac{\hbar^2 \ell(\ell+1)}{2mr^2} , \qquad \text{(4.7)}$$

que presenta el potencial original complementado por un término centrífugo, un potencial repulsivo proporcional al cuadrado del momento angular. Debido a este término, la ecuación radial es ligeramente diferente para cada valor de $\ell$. Como se anticipó, el número cuántico $m$ no aparece en la ecuación diferencial. La misma solución radial $u_{E\ell}(r)$ debe usarse para todos los valores permitidos de $m$.

Recordemos nuestra descomposición de la función de onda:

$$\psi(r,\theta,\varphi) = R_{E\ell}(r)\, Y_{\ell,m}(\theta,\varphi) = \frac{u_{E\ell}(r)}{r}\, Y_{\ell,m}(\theta,\varphi) . \qquad \text{(4.8)}$$

La condición de normalización requiere

$$1 = \int d^3x\, |\psi|^2 = \int r^2\, dr\, d\Omega\, \frac{|u_{E\ell}|^2}{r^2}\, Y_{\ell,m}^* Y_{\ell,m} . \qquad \text{(4.9)}$$

La integral angular da uno, los factores explícitos de $r$ se cancelan y obtenemos

$$\int_0^\infty dr\, |u_{E\ell}|^2 = 1 . \qquad \text{(4.10)}$$

En efecto, $u_{E\ell}(r)$ juega el papel de una función de onda unidimensional para una partícula que se mueve en el potencial efectivo a lo largo de $r$. Dado que solo se permite $r>0$, debemos considerar el posible comportamiento de la función de onda para $r=0$.

Podemos aprender sobre el comportamiento de la solución radial en el origen bajo la suposición razonable de que la barrera centrífuga domina el potencial cuando $r \to 0$. En este caso, los términos más singulares de la ecuación diferencial radial deben cancelarse entre sí, dejando términos menos singulares que podemos ignorar en este cálculo de orden principal. Así que ponemos:

$$-\frac{\hbar^2}{2m}\frac{d^2 u_{E\ell}}{dr^2} + \frac{\hbar^2 \ell(\ell+1)}{2mr^2} u_{E\ell} = 0 , \qquad \text{cuando } r \to 0 . \qquad \text{(4.11)}$$

o equivalentemente

$$\frac{d^2 u_{E\ell}}{dr^2} = \frac{\ell(\ell+1)}{r^2}\, u_{E\ell} . \qquad \text{(4.12)}$$

Las soluciones de esto pueden tomarse como $u_{E\ell} = r^s$ con $s$ una constante a determinar. Entonces encontramos

$$s(s-1) = \ell(\ell+1) \;\; \to \;\; s = \ell+1, \quad s = -\ell , \qquad \text{(4.13)}$$

lo que lleva a dos comportamientos posibles cerca de $r=0$:

$$u_{E\ell} \sim r^{\ell+1} , \qquad \text{o bien} \qquad u_{E\ell} \sim \frac{1}{r^\ell} . \qquad \text{(4.14)}$$

Para $\ell>0$, el segundo comportamiento no es consistente con la normalización, la función de onda diverge demasiado rápido cuando $r \to 0$. Para $\ell=0$, el segundo comportamiento, que lleva a $R \sim 1/r$, de hecho no es una solución de la ecuación de Schrödinger. Por lo tanto hemos establecido que para todo $\ell \geq 0$ debemos tener

$$u_{E\ell} \sim c\, r^{\ell+1} , \qquad \text{cuando } r \to 0 . \qquad \text{(4.15)}$$

Notemos que $u_{E\ell}$ se anula en $r=0$. Incluso para $\ell=0$, tenemos $u \sim r$ y $u$ se anula en $r=0$. En efecto hay una pared infinita en $r=0$, consistente con la imposibilidad de extender $r$ a valores negativos.

Recordemos que la dependencia radial completa de la función de onda se obtiene dividiendo $u_{E\ell}$ por $r$, de modo que

$$R_{E\ell} \sim c\, r^\ell . \qquad \text{(4.16)}$$

Esto permite una función de onda constante no nula en el origen solo para $\ell=0$. Solo para $\ell=0$ una partícula puede estar en el origen. Para $\ell \neq 0$ la “barrera” de momento angular impide que la partícula alcance el origen.

*Sarah Geller y Andrew Turner transcribieron las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare

https://ocw.mit.edu

8.04 Física Cuántica I

Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

# Apéndice: Lista de problemas 9 (Problem Set 9, 2016)

**Física Cuántica I (8.04) — Primavera de 2016** **Departamento de Física del MIT** **Tarea 9** *Fecha de entrega: viernes 29 de abril de 2016, 12:00 del mediodía* *21 de abril de 2016*

**Lectura:**

- Griffiths, sección 4.1.

## Problema 1

**Una comprobación numérica de la fase estacionaria. \[10 puntos\]**

Hemos utilizado la fase estacionaria para determinar la dependencia temporal de la posición de los picos en paquetes de ondas construidos a partir de representaciones integrales. De manera más general, la aproximación de fase estacionaria puede ayudarnos a obtener el valor de la propia integral.

Consideremos la integral de una gaussiana centrada en $x=2$ multiplicada por un factor de fase:

$$f(\lambda) = \int_{-\infty}^{\infty} dx\, e^{-100(x-2)^2} e^{i\varphi(\lambda,x)} , \qquad \varphi(\lambda,x) = 50\left(x-\tfrac{1}{32}\lambda x^4\right) , \quad \lambda \in \mathbb{R} .$$

Queremos confirmar que $|f(\lambda)|$ presenta un máximo en un valor $\lambda_*$ seleccionado por la fase estacionaria, y obtener el valor de $f(\lambda_*)$.

1.  ¿Cuál es la anchura $\Delta$ a media altura de la gaussiana? Es decir, ¿cuál es el mayor $\Delta$ tal que, para todo $x$ con $|x-2| \leq \tfrac{1}{2}\Delta$, la gaussiana sea mayor que la mitad de su máximo? Si tuviera que realizar la integral numéricamente, ¿sería seguro integrar entre 1 y 3? Explique su respuesta.

2.  Use la fase estacionaria para hallar el valor crítico $\lambda_*$ de $\lambda$ para el cual $f(\lambda)$ tendría la mayor magnitud. Para $\lambda_*$, escriba $\varphi(\lambda_*,x)$ como un desarrollo de Taylor alrededor de $x=2$ hasta e incluyendo los términos cuadráticos en $(x-2)$.

3.  ¿Cuál es la excursión de la fase $\varphi(\lambda_*,x)$ para $|x-2| < \tfrac{1}{2}\Delta$? Su resultado, expresado en unidades de $\pi$, debería indicar que es una buena aproximación ignorar la variación de la fase en el valor crítico. Hágalo así y realice a continuación la integral resultante de forma analítica. La respuesta es un número complejo. Escriba su resultado como una fase multiplicada por una magnitud.

4.  Realice la integral analíticamente usando la aproximación cuadrática para la fase. Escriba su resultado como una fase multiplicada por una magnitud.

5.  Realice la integral numéricamente en función de $\lambda$ para el intervalo $\lambda \in [0,1]$. Represente gráficamente el valor absoluto $|f(\lambda)|$. ¿Cuál es el valor de $f(\lambda)$ para el $\lambda$ crítico? Compárelo con sus estimaciones anteriores. ¿Cuál es el valor de $\lambda$ que produce el mayor $|f(\lambda)|$?

## Problema 2

**Comprobación del teorema de Levinson en un ejemplo \[10 puntos\]**

Para el potencial $V(x) = -V_0$ para $0<x<a$, $V(x)=0$ para $x>a$, y $V(x)=\infty$ para $x<0$, calculamos en clase el desfase $\delta(E)$, obteniendo

$$\tan\delta = \frac{1 - \dfrac{k'}{k}\cot k'a \, \tan ka}{\tan ka + \dfrac{k'}{k}\cot k'a} ,$$

con

$$k^2 = \frac{2mE}{\hbar^2} , \qquad k'^2 = \frac{2m(E+V_0)}{\hbar^2} , \qquad z_0^2 = \frac{2mV_0 a^2}{\hbar^2} .$$

1.  A medida que la energía $E$ tiende a cero, $ka \to 0$. ¿Qué ocurre con $k'a$? Demuestre que $\tan\delta$ tiende a cero, y por tanto podemos tomar $\delta \to 0$ cuando $ka \to 0$.

2.  ¿Cuál es el límite de $\tan\delta$ cuando $E \to \infty$? Explíquelo con detalle.

3.  Llame $u \equiv ka$ y escriba $\tan\delta$ como una función de $u$ y $z_0$:

$$\tan\delta = f(u; z_0) \quad \to \quad \delta = \operatorname{ArcTan}\big[f(u; z_0)\big] .$$

Escriba la función $f(u; z_0)$.

Para construir las gráficas con Mathematica, resultó difícil usar $\operatorname{ArcTan}[\ldots]$ porque utiliza el rango $(-\pi/2, \pi/2)$ y las gráficas presentan discontinuidades. Una opción (sugerida por W. Taylor) consiste en derivar la función $\operatorname{ArcTan}$ ¡y luego integrarla de nuevo! Puesto que $\delta=0$ para $u=0$, podemos escribir:

$$\delta(u; z_0) = \int_0^u du' \, \frac{d}{du'} \operatorname{ArcTan}\big[f(u'; z_0)\big] .$$

Deje que el ordenador derive e integre. Si encuentra una forma más sencilla de hacerlo, ¡háganoslo saber!

1.  Represente las fases $\delta(u,z_0)$ en función de $u$ para $z_0 = 2, 5, 9$. Para $z_0=2$ use $u \in [0,15]$, para $z_0=5$ use $u \in [0,20]$ y para $z_0=9$ use $u \in [0,30]$. En cada caso, explique cómo el resultado es consistente con el teorema de Levinson e indique cuán cerca está $\delta$ en el valor superior de $u$ del valor esperado de $\delta(E=\infty)$.

## Problema 3

**Dispersión por un escalón y una pared \[10 puntos\]**

Consideremos el potencial

$$V(x) = \begin{cases} V_0 , & 0<x<a , \quad V_0>0 , \\ 0 , & x>a , \\ \infty , & x \leq 0 . \end{cases}$$

Calcule el desfase $\delta(k)$ en función de $k$. Tendrá que considerar dos casos:

1.  $E(k) > V_0$. Llame $k'$ al número de onda para $x<a$. Puede intentar hacerlo desde el principio (a modo de práctica). También puede intentar usar el ejemplo resuelto en clase (y el problema 2 de esta lista), donde en lugar de un escalón teníamos un pozo de profundidad $V_0$, y modificar la respuesta adecuadamente. Deje su respuesta en la forma $\cot\delta = \ldots$.

2.  $E(k) < V_0$. Puede intentar hacerlo desde el principio (a modo de práctica). También puede intentar alguna continuación analítica del resultado del apartado (a). Deje su respuesta en la forma $\cot\delta = \ldots$.

3.  Represente $\delta(k)$ en función de $u = ka \in [0,\infty]$ para un potencial con $z_0 = 5$ (recuerde que $z_0^2 = \dfrac{2mV_0 a^2}{\hbar^2}$).

## Problema 4

**Dispersión por una delta de Dirac y una pared. \[15 puntos\]**

Consideremos nuestro habitual potencial unidimensional con $V(x) = \infty$ para $x \leq 0$, y con

$$V(x) = g\, \delta(x-a) , \qquad g>0 , \qquad x>0 .$$

Dispersamos partículas de masa $m$ y energía $E>0$ contra este potencial. Tenemos

$$(ka)^2 = \frac{2mEa^2}{\hbar^2} , \qquad \lambda \equiv \frac{mag}{\hbar^2} , \quad \text{sin unidades} .$$

1.  Calcule el desfase $\delta(k)$. Escriba la respuesta en la forma

$$\tan\delta = -\frac{\sin^2(ka)}{h(ka;\lambda)} ,$$

donde $h(ka;\lambda)$ es una función que debe determinar. Explique cómo, conocido $\delta$, se obtiene fácilmente la amplitud $A(k)$ que multiplica a la función ‘seno’ en la función de onda para $0<x<a$.

1.  Para comprender las características de $\tan\delta$, calcule la aproximación de orden principal para $ka \ll 1$. Discuta la dependencia del resultado en $\lambda$. Para $ka$ arbitrario, ¿en qué se convierte $\tan\delta$ cuando $\lambda \to \infty$?

2.  Represente $\delta$, el retraso temporal $\dfrac{1}{a}\dfrac{d\delta}{dk}$, y $|A|$ en función de $ka \in [0,10]$ para $\lambda=5$. ¿Observa resonancias? En caso afirmativo, identifique los valores de $ka$, el retraso temporal $\dfrac{1}{a}\dfrac{d\delta}{dk}$ y la magnitud de $|A|$. ¿Es la gráfica de $\delta$ consistente con el teorema de Levinson?

## Problema 5

**Algunos conmutadores y algunos valores esperados. \[10 puntos\]**

1.  Calcule los conmutadores

$$[L_z, x] , \qquad [L_z, y] , \qquad \text{y} \qquad [L_z, z] .$$

1.  Calcule los conmutadores

$$[L_z, p_x] , \qquad [L_z, p_y] , \qquad \text{y} \qquad [L_z, p_z] .$$

1.  Suponga que $\psi_0$ es una autofunción de $L_z$. Demuestre que $p_y$ y $p_x$ tienen valor esperado nulo en el estado $\psi_0$.

2.  Suponga que $\psi_0$ es una autofunción de $L_z$. Demuestre que $y$ y $x$ tienen valor esperado nulo en el estado $\psi_0$.

## Problema 6

**Momento angular en coordenadas esféricas. \[10 puntos\]**

1.  Calcule las nueve derivadas parciales de las coordenadas esféricas $(r,\theta,\varphi)$ respecto de las coordenadas cartesianas $(x,y,z)$, expresando sus respuestas en términos de las coordenadas esféricas.

2.  Use los resultados anteriores para escribir $L_x$, $L_y$ y $L_z$ como operadores diferenciales en coordenadas esféricas.

3.  Calcule $L_x^2$, $L_y^2$ y $L_z^2$ como operadores diferenciales en coordenadas esféricas y use sus resultados para deducir la forma esperada de $L^2$ como operador diferencial en coordenadas esféricas.

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*


---

<!-- MIT8.04_LecNotes22_ES.md -->

# Clases 21 y 22: El Átomo de Hidrógeno

## Vídeos de esta clase (YouTube)

**Lección 21: Legendre equation. Radial equation. Hydrogen atom 2-body problem.**

- [Associated Legendre functions and spherical harmonics](https://www.youtube.com/watch?v=Lt2Y6fLJ09Q)
- [Orthonormality of spherical harmonics](https://www.youtube.com/watch?v=gKSRrTik1SA)
- [Effective potential and boundary conditions at r=0](https://www.youtube.com/watch?v=_XDm2cxC-UU)
- [Hydrogen atom two-body problem](https://www.youtube.com/watch?v=7q32Wnm4dEw)

**Lección 22: Hydrogen atom (cont.). Differential equation, series solution and quantum numbers**

- [Center of mass and relative motion wavefunctions](https://www.youtube.com/watch?v=dVWKsiaAZ14)
- [Scales of the hydrogen atom](https://www.youtube.com/watch?v=GWMeYKUvj7Y)
- [Schrödinger equation for hydrogen](https://www.youtube.com/watch?v=KfbvrGt3MlI)
- [Series solution and quantization of the energy](https://www.youtube.com/watch?v=3VXLIF2DpHI)
- [Energy eigenstates of hydrogen](https://www.youtube.com/watch?v=Z4CSAWrzguY)

------------------------------------------------------------------------

*B. Zwiebach* *4 de mayo de 2016*

## Contenido

1.  El átomo de hidrógeno
2.  Espectro del átomo de hidrógeno

## 1. El átomo de hidrógeno

Nuestro objetivo aquí es mostrar que el problema cuántico de dos cuerpos del átomo de hidrógeno puede reformularse como uno en el que tenemos grados de libertad del centro de masas que se comportan como una partícula libre, y grados de libertad del movimiento relativo cuya dinámica está controlada por un potencial central.

El átomo de hidrógeno consiste en un protón y un electrón moviéndose en tres dimensiones. Denotamos los operadores de posición y momento del protón como $\hat{x}_p$, $\hat{p}_p$, y los del electrón como $\hat{x}_e$, $\hat{p}_e$. Estas son variables canónicas, es decir, satisfacen las relaciones de conmutación canónicas:

$$[(\hat{x}_p)_i, (\hat{p}_p)_j] = i\hbar \delta_{ij}, \qquad [(\hat{x}_e)_i, (\hat{p}_e)_j] = i\hbar \delta_{ij}. \qquad \text{(1.1)}$$

Aquí los subíndices $i, j = 1, 2, 3$ denotan las distintas componentes de los operadores vectoriales. Además, las variables del protón conmutan con las variables del electrón. Tenemos dos pares de variables canónicas independientes.

La función de onda del sistema es una función de las posiciones de ambas partículas:

$$\Psi(x_p, x_e), \qquad \text{(1.2)}$$

y la cantidad

$$|\Psi(x_p, x_e)|^2 \, d^3x_p \, d^3x_e, \qquad \text{(1.3)}$$

es la probabilidad de encontrar al protón dentro de una ventana $d^3x_p$ de $x_p$ y al electrón dentro de una ventana $d^3x_e$ de $x_e$. El hamiltoniano del sistema viene dado por

$$\hat{H} = \frac{\hat{p}_p^2}{2m_p} + \frac{\hat{p}_e^2}{2m_e} + V(|x_e - x_p|). \qquad \text{(1.4)}$$

Nótese que la energía cinética es simplemente la suma de la energía cinética del protón y la energía cinética del electrón. El potencial depende únicamente de la magnitud de la separación entre las dos partículas, no de sus posiciones individuales.

Para simplificar el problema, introduciremos dos nuevos pares de variables canónicas independientes. El primer par está asociado al movimiento del centro de masas (CM). Introducimos el operador de momento total $\hat{P}$ y el operador de posición del CM $\hat{X}$, dados por

$$\hat{P} = \hat{p}_p + \hat{p}_e, \qquad \hat{X} = \frac{m_e \hat{x}_e + m_p \hat{x}_p}{m_e + m_p}. \qquad \text{(1.5)}$$

El operador $\hat{X}$ viene dado por la expresión habitual del centro de masas del sistema, pero con las posiciones sustituidas por operadores de posición. Usando las relaciones de conmutación (1.1), podemos mostrar que $\hat{X}$ y $\hat{P}$ son conjugados canónicos:

$$\begin{aligned}
\left[(\hat{X})_i, (\hat{P})_j\right] &= \left[\frac{m_e (\hat{x}_e)_i + m_p (\hat{x}_p)_i}{m_e + m_p}, (\hat{p}_p)_j + (\hat{p}_e)_j\right] \\
&= \frac{m_e}{m_e + m_p}[(\hat{x}_e)_i, (\hat{p}_e)_j] + \frac{m_p}{m_e + m_p}[(\hat{x}_p)_i, (\hat{p}_p)_j] \\
&= \frac{m_e}{m_e + m_p} i\hbar \delta_{ij} + \frac{m_p}{m_e + m_p} i\hbar \delta_{ij},
\end{aligned} \qquad \text{(1.6)}$$

lo que da como resultado esperado

$$\left[(\hat{X})_i, (\hat{P})_j\right] = i\hbar \delta_{ij}. \qquad \text{(1.7)}$$

Para el segundo par de variables canónicas definiremos operadores de posición y momento relativos. El operador de posición relativa es la variable natural implicada por la forma del potencial:

$$\hat{x} = \hat{x}_e - \hat{x}_p. \qquad \text{(1.8)}$$

Puesto que el segundo par de variables canónicas debe conmutar con el primer par, debemos comprobar que $x$, definido arriba, conmuta con $X$ y con $P$. La conmutación con $X$ es automática, y la conmutación con $P$ funciona gracias al signo menos en la definición anterior. Ahora debemos construir un operador de momento relativo $\hat{p}$ que sea canónicamente conjugado a $x$. Debe construirse a partir de los operadores de momento de las dos partículas, así que escribimos

$$\hat{p} = \alpha \hat{p}_e - \beta \hat{p}_p, \qquad \text{(1.9)}$$

con $\alpha$ y $\beta$ coeficientes a determinar. Para ser canónicamente conjugados, los operadores relativos deben satisfacer

$$[(\hat{x})_i, (\hat{p})_j] = i\hbar \delta_{ij} \ \Rightarrow \ \alpha + \beta = 1, \qquad \text{(1.10)}$$

usando las definiciones anteriores de $\hat{x}$ y $\hat{p}$ y los conmutadores del protón y del electrón. Finalmente, el momento relativo debe conmutar con la coordenada del CM

$$\left[(\hat{X})_i, (\hat{p})_j\right] = 0 \ \Rightarrow \ m_e \alpha - m_p \beta = 0. \qquad \text{(1.11)}$$

Las dos ecuaciones para $\alpha$ y $\beta$ pueden resolverse para encontrar

$$\alpha = \frac{m_p}{m_e + m_p}, \qquad \beta = \frac{m_e}{m_e + m_p}. \qquad \text{(1.12)}$$

Definimos la masa total $M$ y la masa reducida $\mu$ como sigue

$$M = m_e + m_p, \qquad \mu = \frac{m_e m_p}{m_e + m_p}. \qquad \text{(1.13)}$$

La masa reducida de un par de partículas con masas muy diferentes es aproximadamente igual a la masa de la partícula de menor masa. Usando estas definiciones

$$\alpha = \frac{\mu}{m_e}, \qquad \beta = \frac{\mu}{m_p}. \qquad \text{(1.14)}$$

Así, recopilando las variables relativas tenemos

$$\hat{p} = \mu \left(\frac{\hat{p}_e}{m_e} - \frac{\hat{p}_p}{m_p}\right) = \frac{m_p}{M}\hat{p}_e - \frac{m_e}{M}\hat{p}_p, \qquad \hat{x} = \hat{x}_e - \hat{x}_p. \qquad \text{(1.15)}$$

Nótese que el momento relativo $p$ puede escribirse en términos de velocidades como $p = \mu(v_e - v_p)$. El momento relativo se anula si el movimiento es puramente movimiento del CM, en cuyo caso las velocidades de las dos partículas son iguales.

Ahora podemos reescribir el hamiltoniano en términos de las nuevas variables. Despejando los operadores de momento originales en términos de $\hat{P}$ y $\hat{p}$, encontramos

$$\hat{p}_p = \frac{m_p}{M}\hat{P} - \hat{p}, \qquad \hat{p}_e = \frac{m_e}{M}\hat{P} + \hat{p}. \qquad \text{(1.16)}$$

Podemos entonces reescribir los términos cinéticos del hamiltoniano en la forma

$$\begin{aligned}
\frac{\hat{p}_p^2}{2m_p} + \frac{\hat{p}_e^2}{2m_e} &= \frac{1}{2m_p}\left(\frac{m_p^2}{M^2}\hat{P}^2 - \frac{2m_p}{M}\hat{P}\cdot\hat{p} + \hat{p}^2\right) \\
&\quad + \frac{1}{2m_e}\left(\frac{m_e^2}{M^2}\hat{P}^2 + \frac{2m_e}{M}\hat{P}\cdot\hat{p} + \hat{p}^2\right) \\
&= \frac{\hat{P}^2}{2M} + \frac{\hat{p}^2}{2\mu}.
\end{aligned} \qquad \text{(1.17)}$$

Afortunadamente el término que acopla los dos momentos se anula. Así, los grados de libertad del centro de masas y los grados de libertad relativos dan contribuciones independientes a la energía cinética. El hamiltoniano puede entonces escribirse como

$$\hat{H} = \frac{\hat{P}^2}{2M} + \frac{\hat{p}^2}{2\mu} + V(|\hat{x}|). \qquad \text{(1.18)}$$

En el espacio de posiciones, los operadores de momento total y relativo pueden expresarse como gradientes

$$\hat{P} \to \frac{\hbar}{i}\nabla_X, \qquad \hat{p} \to \frac{\hbar}{i}\nabla_x. \qquad \text{(1.19)}$$

Cada $\nabla$ lleva un subíndice que indica el tipo de coordenada respecto a la cual tomamos las derivadas. Del mismo modo que teníamos una función de onda $\Psi(x_e, x_p)$, las nuevas variables canónicas exigen que ahora pensemos en la función de onda como una función $\Psi(X, x)$ de las nuevas coordenadas.

Resolvemos la ecuación de Schrödinger independiente del tiempo mediante separación de variables

$$\Psi(X, x) = \Psi_{CM}(X)\Psi_{rel}(x). \qquad \text{(1.20)}$$

Sustituyendo esto en la ecuación de Schrödinger independiente del tiempo $\hat{H}\Psi = E\Psi$, llegamos a

$$\left[\frac{\hat{P}^2}{2M}\Psi_{CM}(X)\right]\Psi_{rel}(x) + \left[\frac{\hat{p}^2}{2\mu}\Psi_{rel}(x) + V(|\hat{x}|)\Psi_{rel}(x)\right]\Psi_{CM}(X) = E\Psi_{CM}(X)\Psi_{rel}(x). \qquad \text{(1.21)}$$

Dividiendo por la función de onda total $\Psi_{CM}(X)\Psi_{rel}(x)$, esto se convierte en

$$\frac{1}{\Psi_{CM}(X)}\left[\frac{\hat{P}^2}{2M}\Psi_{CM}(X)\right] + \frac{1}{\Psi_{rel}(x)}\left[\frac{\hat{p}^2}{2\mu} + V(|\hat{x}|)\right]\Psi_{rel}(x) = E. \qquad \text{(1.22)}$$

El primer término del lado izquierdo es una función únicamente de $X$, y el segundo término del lado izquierdo es una función únicamente de $x$. Su suma es igual a la constante $E$, y puesto que $x$ y $X$ son variables independientes, cada término debe ser individualmente constante. Igualamos entonces el primer término a la constante $E_{CM}$ y el segundo término a la constante $E_{rel}$, obteniendo las siguientes ecuaciones:

$$\frac{\hat{P}^2}{2M}\Psi_{CM}(X) = E_{CM}\Psi_{CM}(X), \qquad \text{(1.23)}$$

$$\left[\frac{\hat{p}^2}{2\mu} + V(|x|)\right]\Psi_{rel}(x) = E_{rel}\Psi_{rel}(x), \qquad \text{(1.24)}$$

$$E = E_{CM} + E_{rel}. \qquad \text{(1.25)}$$

Obtenemos dos ecuaciones de Schrödinger. La primera ecuación nos dice que el centro de masas se mueve como una partícula libre de masa $M$. Así, la energía del CM no está cuantizada y obtenemos soluciones de onda plana. La segunda ecuación corresponde al movimiento relativo, y como queríamos mostrar, se describe como un movimiento en un potencial central. La tercera ecuación nos dice que la energía total es la suma de la energía del centro de masas y la energía del movimiento relativo.

## 2. Espectro del átomo de hidrógeno

Ahora tenemos las herramientas para estudiar el átomo de hidrógeno, que tiene un potencial central dado por

$$V(r) = -\frac{Ze^2}{r}, \qquad \text{(2.1)}$$

donde $Z$ es el número de protones en el núcleo. Para el hidrógeno tenemos $Z = 1$. Pero conviene considerar $Z > 1$, en cuyo caso estamos describiendo el movimiento de un electrón alrededor del núcleo de algún otro átomo. También definiremos las siguientes constantes físicas.

- La constante de estructura fina $\alpha$: $\alpha = \dfrac{e^2}{\hbar c} \simeq \dfrac{1}{137}$.

- El radio de Bohr $a_0$. Esta es la escala de longitud característica del problema. Puede calcularse igualando las energías cinética y potencial expresadas en términos de $a_0$ e ignorando todas las constantes numéricas:

$$\frac{\hbar^2}{m_e a_0^2} = \frac{e^2}{a_0}. \qquad \text{(2.2)}$$

Aquí la masa debería ser la masa reducida, que en este caso puede tomarse con bastante precisión como la masa del electrón. Entonces tenemos explícitamente,

$$\begin{aligned}
a_0 &= \frac{\hbar^2}{m e^2} = \frac{\hbar^2 c^2}{e^2 m c^2} = \frac{\hbar c}{\dfrac{e^2}{\hbar c} m c^2} = \frac{\hbar c}{\alpha m c^2} \\
&= \frac{197\ \text{MeV fm}}{0.51 \times 10^6\ \text{eV}} \times 137 = \frac{1970\ \text{eV Angstrom}}{0.51 \times 10^6\ \text{eV}} \times 137 \\
&= 0.529\ \text{Angstroms} \simeq 53\ \text{pm}.
\end{aligned} \qquad \text{(2.3)}$$

Para la estimación de la escala de energía tenemos

$$\frac{e^2}{a_0} = e^2 \left(\frac{m e^2}{\hbar^2}\right) = \left(\frac{e^4}{\hbar^2 c^2}\right) m c^2 = \alpha^2 m c^2 = \frac{1}{(137)^2} \times (511\,000\ \text{eV}) \simeq 27.2\ \text{eV}. \qquad \text{(2.4)}$$

Hay otras longitudes características interesantes:

$$\alpha a_0 = \text{longitud de onda Compton del electrón} = \bar\lambda_e \simeq 390\ \text{fm}, \qquad \text{(2.5)}$$

$$\alpha^2 a_0 = \text{radio clásico del electrón} \simeq 2.8\ \text{fm}.$$

¡Pasemos ahora a trabajar! La ecuación radial de Schrödinger para estados ligados $E < 0$ es

$$\left[-\frac{\hbar^2}{2m}\frac{d^2}{dr^2} + \frac{\hbar^2 \ell(\ell+1)}{2mr^2} - \frac{Ze^2}{r}\right] u = E u. \qquad \text{(2.6)}$$

Podríamos denotar la función de onda $u$ como $u_{E\ell}$, ya que las soluciones dependerán ciertamente de $\ell$ y de la energía $E$. Como es habitual, nos gusta trabajar con una coordenada adimensional. Esto podría lograrse escribiendo $r = a_0 x$, con $x$ adimensional y $a_0$ portando las unidades de longitud de $r$. Será más conveniente usar una ligera variante para eliminar $Z$ de la ecuación y algunos factores de dos. Tomaremos la nueva coordenada adimensional $x$ definida por

$$r \equiv \frac{a_0}{2Z} x. \qquad \text{(2.7)}$$

La ecuación de Schrödinger se convierte entonces en

$$\begin{aligned}
&-\frac{\hbar^2}{2m}\frac{4Z^2}{a_0^2}\frac{d^2}{dx^2} + \frac{4Z^2\hbar^2}{a_0^2}\frac{\ell(\ell+1)}{2mx^2} - \frac{2Z^2 e^2}{a_0}\frac{1}{x}\Bigg] u = Eu \\
&\Rightarrow \ \frac{2\hbar^2 Z^2}{ma_0^2}\left[-\frac{d^2}{dx^2} + \frac{\ell(\ell+1)}{x^2}\right] u - \frac{2Z^2 e^2}{a_0}\frac{1}{x}\, u = Eu.
\end{aligned} \qquad \text{(2.8)}$$

Nótese que

$$\frac{2\hbar^2 Z^2}{ma_0^2} = \left(\frac{2\hbar^2 Z}{ma_0}\right)\left(\frac{me^2}{\hbar^2}\right) = \frac{2Ze^2}{a_0}, \qquad \text{(2.9)}$$

lo que reduce nuestra ecuación diferencial a

$$\left[-\frac{d^2}{dx^2} + \frac{\ell(\ell+1)}{x^2} - \frac{1}{x}\right] u = \frac{E}{\dfrac{2Ze^2}{a_0}} u. \qquad \text{(2.10)}$$

Definimos ahora el parámetro adimensional $\kappa$ que codifica la energía:

$$\kappa^2 = -\frac{E}{\dfrac{2Ze^2}{a_0}} > 0. \qquad \text{(2.11)}$$

$\kappa$ es una versión adimensional de la energía del estado ligado. La ecuación diferencial es entonces

$$\left[-\frac{d^2}{dx^2} + \frac{\ell(\ell+1)}{x^2} - \frac{1}{x}\right] u = -\kappa^2 u. \qquad \text{(2.12)}$$

Podemos simplificar aún más esta ecuación antes de resolverla examinando los casos límite. En el límite $x \to \infty$, los términos dominantes son la segunda derivada y el término del lado derecho, lo que da

$$\frac{d^2 u}{dx^2} = \kappa^2 u \implies u \sim e^{\pm \kappa x}. \qquad \text{(2.13)}$$

Puesto que $\kappa$ es adimensional, podemos hacer que el exponente anterior sea igual a una nueva coordenada adimensional $\rho$:

$$\rho \equiv \kappa x = \frac{2\kappa Z}{a_0} r. \qquad \text{(2.14)}$$

Esta vez obtenemos

$$\left[-\frac{d^2}{d\rho^2} + \frac{\ell(\ell+1)}{\rho^2} - \frac{1}{\kappa\rho}\right] u = -u. \qquad \text{(2.15)}$$

Nótese que no logramos que $\kappa$ desaparezca de la ecuación. Esto es una buena noticia: la ecuación debería fijar los valores posibles de $\kappa$ (o las energías posibles). La ecuación anterior no está del todo lista para una solución en serie: encontraríamos una relación de recurrencia de tres términos, que es bastante complicada. Para avanzar, discutimos el comportamiento para $\rho$ pequeño y grande.

Para $\rho \to \infty$ ahora obtenemos $u \sim e^{\pm\rho}$ y, por supuesto, esperamos que $u = e^{-\rho}$ por normalizabilidad. Como discutimos antes, para $\rho \to 0$ la solución radial debe tener la forma $u \sim \rho^{(\ell+1)}$. Esta información sobre el comportamiento para $\rho$ pequeño y grande sugiere un buen ansatz para $u(\rho)$

$$u(\rho) = \rho^{\ell+1} W(\rho) e^{-\rho}. \qquad \text{(2.16)}$$

donde $W(\rho)$ es una función aún por determinar, que esperamos que satisfaga una ecuación diferencial más sencilla. Para derivar esta ecuación diferencial para $W(\rho)$, sustituimos nuestro ansatz en la Ec. (2.15). Como ayuda intermedia para el cálculo, damos un resultado intermedio:

$$-u'' + \frac{\ell(\ell+1)}{\rho^2} u + u = \left[-W'' - \frac{2(\ell+1)}{\rho}W' + \frac{2(\ell+1)}{\rho}W + 2W'\right]\rho^{\ell+1} e^{-\rho}. \qquad \text{(2.17)}$$

Con un poco más de trabajo finalmente obtenemos la ecuación diferencial para $W$:

$$\rho \frac{d^2 W}{d\rho^2} + 2(\ell+1-\rho)\frac{dW}{d\rho} + \left[\frac{1}{\kappa} - 2(\ell+1)\right] W = 0. \qquad \text{(2.18)}$$

Esto parece un poco más complicado que la ecuación diferencial con la que comenzamos, pero conduce a una relación de recurrencia de un solo paso muy agradable. Como es habitual, escribimos $W$ como una expansión en serie

$$W = \sum_{k=0}^{\infty} a_k \rho^k, \qquad \text{(2.19)}$$

y sustituyendo de nuevo en (2.18), agrupamos términos de orden $\rho^k$ para derivar una relación de recurrencia

$$a_{k+1}\left[k(k+1) + 2(\ell+1)(k+1)\right] - 2k a_k + \left[\frac{1}{\kappa} - 2(\ell+1)\right] a_k = 0,$$

$$\Rightarrow \ a_{k+1}\left(k(k+1) + 2(\ell+1)(k+1)\right) = a_k\left[2(k+\ell+1) - \frac{1}{\kappa}\right], \qquad \text{(2.20)}$$

lo que da

$$\frac{a_{k+1}}{a_k} = \frac{2(k+\ell+1) - \dfrac{1}{\kappa}}{(k+1)(k+2\ell+2)}. \qquad \text{(2.21)}$$

Un examen detallado muestra que, para funciones de onda normalizables, la serie debe terminar. Para ver esto, examinamos el comportamiento para $k$ grande de la razón anterior:

$$\frac{a_{k+1}}{a_k} \simeq \frac{2k}{k^2} = \frac{2}{k}. \qquad \text{(2.22)}$$

Nótese que $\dfrac{2}{k+1} < \dfrac{2}{k}$; así, si la razón $\dfrac{2}{k}$ conduce a una divergencia, también lo hará la razón $\dfrac{2}{k+1}$. Tomando

$$\frac{a_{k+1}}{a_k} = \frac{2}{k+1} \ \Rightarrow \ a_{k+1} = \frac{2}{k+1} a_k, \qquad \text{(2.23)}$$

y esto se resuelve mediante

$$a_k = \frac{2^k}{k!} a_0. \qquad \text{(2.24)}$$

Por lo tanto, la suma

$$W = \sum_{k=0}^{\infty} a_k \rho^k \simeq a_0 \sum_{k=0}^{\infty} \frac{2^k \rho^k}{k!} = a_0 e^{2\rho}. \qquad \text{(2.25)}$$

Esto es precisamente suficiente para hacer que el ansatz en (2.16) sea no normalizable.

Para obtener una solución normalizable, la serie para $W$ debe terminar. Supongamos que $W$ es un polinomio de grado $N$, de modo que los coeficientes satisfacen

$$a_N \neq 0 \quad \text{y} \quad a_{N+1} = 0. \qquad \text{(2.26)}$$

De la Ec. (2.21) esto implica

$$\frac{1}{\kappa} = 2(N+\ell+1). \qquad \text{(2.27)}$$

¡La cuantización ha ocurrido! El parámetro que codifica la energía, $\kappa$, está ahora relacionado con números enteros. Nótese que $\ell$ puede tomar valores $\ell = 0, 1, 2, \ldots$, como corresponde a un número cuántico de momento angular. Además, $N$ puede tomar valores $N = 0, 1, 2, \ldots$, ya que existe un polinomio de grado cero, que es igual a una constante. Definimos el número cuántico principal $n$ como sigue:

$$n \equiv N + \ell + 1 = \frac{1}{2\kappa}, \quad \text{con } \ell = 0, 1, 2, \ldots, \ N = 0, 1, 2, \ldots, \ \text{y } n = 1, 2, 3, \ldots \qquad \text{(2.28)}$$

Es importante notar que, para $n$ fijo, debemos tener

$$0 \le \ell \le n-1, \qquad \text{y} \qquad 0 \le N \le n-1. \qquad \text{(2.29)}$$

Si $n$ y $\ell$ son conocidos, $N$ queda determinado a partir de $N + \ell + 1 = n$. Así, los números cuánticos independientes hasta ahora son $n$ y $\ell$. Es interesante notar que las energías dependen únicamente de $n$, ya que $\kappa$ depende únicamente de $n$. Usando la Ec. (2.11), la dependencia de la energía respecto al número cuántico principal viene dada por

$$E = -\frac{2Z^2 e^2}{a_0}\kappa^2, \qquad \text{(2.30)}$$

y usando $\kappa = \dfrac{1}{2n}$ obtenemos

$$E = -\frac{Z^2 e^2}{2a_0}\frac{1}{n^2}. \qquad \text{(2.31)}$$

¡Estos son los niveles de energía del átomo de hidrógeno! Puesto que para cualquier valor fijo de $n > 1$ hay varios valores posibles de $\ell$, el espectro es altamente degenerado. Aún más, cada valor de $\ell$ corresponde a $2\ell+1$ estados, dados los valores posibles de $m$. Una manera de visualizar el espectro se muestra en la Figura 1. Todos los puntos enteros en el cuadrante positivo $(N, \ell)$ representan estados. Los estados con un valor común de $n$ se encuentran sobre las líneas discontinuas.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes22_ES/fig1.png)

Figura 1: Todos los puntos con $N \ge 0$ entero y $\ell \ge 0$ entero representan estados del átomo de hidrógeno. La figura nos ayuda a contar el número de estados posibles para un valor dado de $n$. Cada punto a lo largo de la línea diagonal para un $n$ dado representa un estado posible.

La Figura 1 nos ayuda a contar el número de estados ligados para un valor dado de $n$. Recordemos que para cada $n$, $\ell$ puede tomar valores desde $0, \ldots, n-1$, y para cada valor de $\ell$, $m$ toma valores desde $-\ell$ hasta $\ell$. La siguiente tabla cuenta los estados para los primeros valores del número cuántico principal $n$. Un estado dado se especifica por sus valores de $(n, \ell, m)$, todos los cuales se conocen como los números cuánticos de los estados de hidrógeno. Cada número tiene un significado físico muy importante: $n$ nos informa sobre el autovalor de energía, $\hbar^2 \ell(\ell+1)$ es el autovalor del cuadrado del momento angular, y $\hbar m$ es el autovalor de la componente $z$ del momento angular.

**Número de estados**

| Valor de $n$ | Valores de $\ell$ | Valores de $m$  | Estados totales |
|--------------|-------------------|-----------------|-----------------|
| $n=1$        | $\ell=0$          | $m=0$           | 1 estado        |
| $n=2$        | $\ell=0$          | $m=0$           | 1               |
|              | $\ell=1$          | $m=-1,0,1$      | $+3$            |
|              |                   |                 | $= 4$ estados   |
| $n=3$        | $\ell=0$          | $m=0$           | 1               |
|              | $\ell=1$          | $m=-1,0,1$      | $+3$            |
|              | $\ell=2$          | $m=-2,\ldots,2$ | $+5$            |
|              |                   |                 | $= 9$ estados   |

El número total de estados para un número cuántico principal $n$ arbitrario puede calcularse ahora:

$$\#\ \text{de estados para } n = \sum_{\ell=0}^{n-1}(2\ell+1) = \frac{2(n-1)n}{2} + n = n^2 - n + n = n^2. \qquad \text{(2.32)}$$

Esto concuerda con los resultados parciales de la tabla. Una representación más familiar de los estados del hidrógeno se muestra en la Figura 2. Las distintas columnas indican los distintos valores de $\ell$. También hemos indicado en la figura los valores de $N$, el grado del polinomio que aparece en la solución radial. Nótese que, para un $\ell$ dado, es decir, para una ecuación radial fija, el valor de $N$ aumenta a medida que subimos por la columna. El número $N$ corresponde al número de nodos de la solución.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes22_ES/fig2.png)

Figura 2: Gráfico de los niveles de energía $E \sim -1/n^2$ indicando también el número cuántico angular $\ell$ y el grado $N$ del polinomio. El espectro es altamente degenerado.

Recordemos que definimos $\rho = \dfrac{2\kappa Z}{a_0} r$. Junto con $\kappa = \dfrac{1}{2n}$ esto da

$$\rho = \frac{Zr}{na_0}. \qquad \text{(2.33)}$$

Los estados propios están etiquetados por los números cuánticos $(n, \ell, m)$ y las funciones de onda son

$$\psi_{n\ell m} = N \frac{u_{n\ell}(r)}{r} Y_{\ell m}(\theta,\phi) = N \frac{\rho^{\ell+1}}{\rho} W_{n\ell}(\rho) e^{-\rho} Y_{\ell m}(\theta,\phi) = N \rho^{\ell} \underbrace{W_{n\ell}(\rho)}_{\substack{\text{polinomio de grado} \\ N=n-(\ell+1)}} e^{-\rho} Y_{\ell m}(\theta,\phi), \qquad \text{(2.34)}$$

donde $N$ es una constante de normalización. Por lo tanto, usando la expresión para $\rho$ y absorbiendo constantes en $N$ tenemos

$$\psi_{n\ell m}(r,\theta,\phi) = N \left(\frac{r}{a_0}\right)^{\ell} \underbrace{\left[\text{polinomio en } \frac{r}{a_0}\right]}_{\text{de grado } N=n-(\ell+1)} \ e^{-\frac{Zr}{na_0}} \ Y_{\ell m}(\theta,\phi). \qquad \text{(2.35)}$$

Para el estado fundamental del hidrógeno ($Z=1$), tenemos $(n,\ell,m) = (1,0,0)$. Al tener momento angular nulo, la función de onda asociada no tiene dependencia angular. La función de onda normalizada es

$$\psi_{100}(r,\theta,\phi) = \frac{1}{\sqrt{\pi a_0^3}} e^{-r/a_0}. \qquad \text{(2.36)}$$

Para las funciones de onda normalizadas del hidrógeno en $n=2$ y $n=3$, véase http://hyperphysics.phy-astr.gsu.edu/hbase/quantum/hydwf.html

*Sarah Geller y Andrew Turner transcribieron las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare

https://ocw.mit.edu

8.04 Física Cuántica I

Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

# Apéndice: Lista de problemas 10 (Problem Set 10, 2016)

**Departamento de Física del MIT — Física Cuántica I (8.04), Primavera de 2016**

*Lectura: Griffiths, secciones 4.1, 4.2 y 4.3.*

*Publicado el 29 de abril de 2016. Fecha de entrega: viernes 6 de mayo de 2016, 12:00 del mediodía.*

## Problema 1. Estados ligados a partir de un número de onda imaginario \[5 puntos\]

Considere la solución de dispersión para un potencial unidimensional de rango finito:

$$\psi_>(x) = e^{i\delta(k)}\sin(kx+\delta(k)), \qquad x > R.$$

Muestre que tener un estado ligado significa que $A_s = e^{i\delta}\sin\delta$ tiene un polo en $k = i\kappa$ con $\kappa > 0$.

## Problema 2. Autofunciones simultáneas \[5 puntos\]

Considere dos operadores hermíticos $\hat{A}$ y $\hat{B}$ que conmutan. Suponga que al menos uno de los operadores, digamos $\hat{A}$, no tiene degeneraciones en su espectro. Muestre que las autofunciones de $\hat{A}$ son también autofunciones de $\hat{B}$.

## Problema 3. Valores esperados en una función de onda particular \[10 puntos\]

(Basado en Ohanian, Cap. 7, problema 17).

Suponga que una partícula tiene la función de onda

$$\psi(r,\theta,\phi) = \frac{1}{4}\sqrt{\frac{5}{\pi}}\,\sin^2\theta\left(1+\sqrt{14}\cos\theta\right)\cos 2\phi \; f(r),$$

con $f(r)$ una función de onda radial normalizada.

1.  Reescriba esta función de onda en términos de armónicos esféricos. ¿Cuáles son los posibles resultados de la medición de $L^2$ y $L_z$? ¿Cuáles son las probabilidades correspondientes?

2.  ¿Cuáles son los valores esperados de $L^2$ y $L_z$?

3.  Determine las incertidumbres $\Delta L^2$ y $\Delta L_z$.

## Problema 4. Pozos esféricos \[10 puntos\]

1.  Considere estados con $\ell = 0$ de una partícula que se mueve en el pozo esférico *infinito*

$$V(r) = \begin{cases} 0, & \text{si } r < a \\ \infty, & \text{si } r > a. \end{cases}$$

Resuelva la ecuación radial para la función de onda radial $u(r)$ y encuentre los niveles de energía posibles. Recuerde que $u$ debe anularse en $r=0$. Intente relacionar este espectro con $\ell=0$ con el de un potencial de pozo infinito unidimensional $V(x)$.

1.  Considere ahora estados de una partícula que se mueve en un pozo esférico *finito* con $V_0 > 0$:

$$V(r) = \begin{cases} -V_0, & \text{si } r < a \\ 0, & \text{si } r > a. \end{cases}$$

Muestre que no hay estado ligado si

$$V_0 a^2 < \frac{\pi^2 \hbar^2}{8m}.$$

## Problema 5. Átomo de hidrógeno con momento total \[10 puntos\]

Basado en Ohanian.

Cuando se tiene en cuenta el movimiento del núcleo, el estado del átomo de hidrógeno puede representarse mediante una función de onda $\psi(\mathbf{X}, \mathbf{x})$, con $\mathbf{X}$ la coordenada del centro de masas y $\mathbf{x} = \mathbf{x}_e - \mathbf{x}_p$ la coordenada relativa que apunta del protón al electrón.

Suponga que el átomo se encuentra en un estado tal que el momento *total* tiene probabilidades iguales para los valores $\mathbf{p}_0$ y $-\mathbf{p}_0$. Además, los estados internos son $\phi_{1,0,0}(\mathbf{x})$ o $\phi_{2,1,1}(\mathbf{x})$ con probabilidades $1/4$ y $3/4$ respectivamente (usamos la notación $\phi_{n\ell m}$). Estas probabilidades no están correlacionadas con el momento total.

1.  Escriba una expresión para $\psi(\mathbf{X}, \mathbf{x})$ ignorando la fase global pero incluyendo factores de fase constantes arbitrarios donde sea posible.

2.  ¿Cuál es el valor esperado de la energía total?

## Problema 6. Teorema del virial y aplicaciones \[15 puntos\]

1.  Considere cualquier operador independiente del tiempo $\Omega$ y la derivada temporal de su valor esperado, dada por

$$i\hbar \frac{d}{dt}\langle\Omega\rangle = \langle[\Omega, H]\rangle,$$

donde $H$ es el hamiltoniano. Explique cuidadosamente por qué el lado derecho se anula si el sistema se encuentra en un estado estacionario.

1.  Tome ahora $\Omega = \mathbf{r}\cdot\mathbf{p}$ y muestre que, para cualquier estado estacionario del hamiltoniano del átomo de hidrógeno, se cumple la siguiente relación

$$\langle T\rangle = -\tfrac{1}{2}\langle V\rangle.$$

Aquí $T$ es el operador de energía cinética y $V$ es el operador de energía potencial.

1.  Para cualquier autoestado del átomo de hidrógeno, escriba $\langle T\rangle = \tfrac{1}{2}m\langle v^2\rangle$, donde $m$ es, con bastante precisión, la masa del electrón. Exprese el cociente

$$\frac{\sqrt{\langle v^2\rangle}}{c}$$

en términos de la constante de estructura fina $\alpha = \dfrac{e^2}{\hbar c} \simeq \dfrac{1}{137}$ y el número cuántico principal $n$. ¿Es el electrón relativista? Dé los resultados correspondientes para el estado fundamental cuando el núcleo tiene $Z$ protones.

1.  ¿Cuánto vale $\left\langle \dfrac{1}{r} \right\rangle$ en un autoestado de energía general del átomo de hidrógeno?

## Problema 7. Ejercicios sobre el átomo de hidrógeno y algunas generalizaciones \[10 puntos\]

1.  Encuentre $\langle r\rangle$ y $\langle r^2\rangle$ en el estado fundamental del hidrógeno. ¿Cuál es el valor más probable de $r$ en el estado fundamental?

2.  Suponga que el núcleo del hidrógeno tiene un radio de un femtómetro. Calcule la probabilidad de que el electrón del estado fundamental se encuentre dentro del núcleo. ¡Haga aproximaciones para simplificar su trabajo y aun así obtener una respuesta muy precisa!

3.  El positronio es un estado ligado de un electrón y un positrón (¡partículas de igual masa!). ¿Cuáles son los niveles de energía? ¿Cómo se compara el tamaño del positronio con el tamaño de un átomo de hidrógeno?

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*


---

<!-- MIT8.04_LecNotes2_ES.md -->

# Capítulo 2: Experimentos con fotones

## Vídeos de esta clase (YouTube)

**Lección 2: Overview of quantum mechanics (cont.). Interaction-free measurements.**

- [More on superposition. General state of a photon and spin states](https://www.youtube.com/watch?v=0xNmc2tJ-YM)
- [Entanglement](https://www.youtube.com/watch?v=G3HSP3qMgKI) (13:07)
- [Mach-Zehnder interferometers and beam splitters](https://www.youtube.com/watch?v=0USje5vTIKs)
- [Interferometer and interference](https://www.youtube.com/watch?v=37-GdFJGSXs)
- [Elitzur-Vaidman bombs](https://www.youtube.com/watch?v=vFZeh8bMx58) (10:29)

------------------------------------------------------------------------

B. Zwiebach

9 de febrero de 2016

## Contenidos

1.  Interferómetro de Mach-Zehnder
2.  Bombas de Elitzur-Vaidman

## 1. Interferómetro de Mach-Zehnder

Hemos discutido antes el interferómetro de Mach-Zehnder, que mostramos de nuevo en la Figura 1. Contiene dos divisores de haz BS1 y BS2 y dos espejos. Dentro del interferómetro tenemos dos haces, uno que va por la rama superior y otro que va por la rama inferior. Esto se extiende más allá de BS2: la rama superior continúa hacia D0 mientras que la rama inferior continúa hacia D1.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes2_ES/fig1.png)

Figura 1: El interferómetro de Mach-Zehnder.

Los cortes verticales en la figura anterior intersecan los dos haces y podemos preguntarnos cuál es la probabilidad de encontrar un fotón en cada uno de los dos haces en ese corte. Para esto necesitamos dos amplitudes de probabilidad, o dos números complejos, cuyo módulo al cuadrado daría las probabilidades. Podemos codificar esta información en un vector de dos componentes como

$$\begin{pmatrix} \alpha \\ \beta \end{pmatrix}. \qquad \text{(1.1)}$$

Aquí $\alpha$ es la amplitud de probabilidad de estar en el haz superior y $\beta$ la amplitud de probabilidad de estar en el haz inferior. Por lo tanto, $|\alpha|^2$ sería la probabilidad de encontrar el fotón en el haz superior y $|\beta|^2$ la probabilidad de encontrar el fotón en el haz inferior. Dado que el fotón debe encontrarse en uno de los dos haces, debemos tener

$$|\alpha|^2 + |\beta|^2 = 1. \qquad \text{(1.2)}$$

Siguiendo esta notación, tendríamos para los casos en que el fotón está definitivamente en uno u otro haz:

$$\text{fotón en el haz superior:}\ \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \qquad \text{fotón en el haz inferior:}\ \begin{pmatrix} 0 \\ 1 \end{pmatrix}. \qquad \text{(1.3)}$$

Podemos ver el estado (1.1) como una superposición de estos dos estados más simples usando las reglas de la suma y multiplicación de vectores:

$$\begin{pmatrix} \alpha \\ \beta \end{pmatrix} = \begin{pmatrix} \alpha \\ 0 \end{pmatrix} + \begin{pmatrix} 0 \\ \beta \end{pmatrix} = \alpha \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \beta \begin{pmatrix} 0 \\ 1 \end{pmatrix}. \qquad \text{(1.4)}$$

En el interferómetro mostrado en la Figura 1 incluimos en la rama inferior un “desfasador”, una pieza de

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes2_ES/fig2.png)

Figura 2: Un desfasador de factor de fase $e^{i\delta}$. La amplitud se multiplica por la fase.

material cuyo único efecto es multiplicar la amplitud de probabilidad por una fase fija $e^{i\delta}$ con $\delta \in \mathbb{R}$. Como se muestra en la Figura 2, la amplitud de probabilidad $\alpha$ a la izquierda del dispositivo se convierte en $e^{i\delta}\alpha$ a la derecha del dispositivo. Dado que la norma de una fase es uno, el desfasador no cambia la probabilidad de encontrar el fotón. Cuando la fase $\delta$ es igual a $\pi$, el efecto del desfasador es cambiar el signo de la función de onda, ya que $e^{i\pi} = -1$.

Consideremos ahora en detalle el efecto de los divisores de haz. Si el fotón incidente golpea un divisor de haz desde arriba, consideramos que este fotón pertenece a la rama superior y lo representamos por $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$. Si el fotón incidente golpea el divisor de haz desde abajo, consideramos que este fotón pertenece a la rama inferior, y lo representamos por $\begin{pmatrix} 0 \\ 1 \end{pmatrix}$. Mostramos los dos casos en la Figura 3. El efecto del divisor de haz es dar una función de onda de salida para cada uno de los dos casos:

$$\text{BS izquierdo:}\ \begin{pmatrix} 1 \\ 0 \end{pmatrix} \to \begin{pmatrix} s \\ t \end{pmatrix}, \qquad \text{BS derecho:}\ \begin{pmatrix} 0 \\ 1 \end{pmatrix} \to \begin{pmatrix} u \\ v \end{pmatrix}. \qquad \text{(1.5)}$$

Como se puede ver en el diagrama, para el fotón que incide desde arriba, $s$ puede pensarse como una amplitud de reflexión y $t$ como un coeficiente de transmisión. De manera similar, para el fotón que incide desde abajo, $v$ puede pensarse como una amplitud de reflexión y $u$ como un coeficiente de transmisión. Los cuatro números $s, t, u, v$, por linealidad, caracterizan completamente al divisor de haz. Pueden usarse para predecir la salida dado cualquier fotón incidente, que puede tener amplitudes para golpear tanto desde arriba como desde abajo. En efecto, un estado de fotón incidente $\begin{pmatrix} \alpha \\ \beta \end{pmatrix}$ daría

$$\begin{pmatrix} \alpha \\ \beta \end{pmatrix} = \alpha \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \beta \begin{pmatrix} 0 \\ 1 \end{pmatrix} \to \alpha \begin{pmatrix} s \\ t \end{pmatrix} + \beta \begin{pmatrix} u \\ v \end{pmatrix} = \begin{pmatrix} \alpha s + \beta u \\ \alpha t + \beta v \end{pmatrix} = \begin{pmatrix} s & u \\ t & v \end{pmatrix} \begin{pmatrix} \alpha \\ \beta \end{pmatrix}. \qquad \text{(1.6)}$$

En resumen, vemos que el BS produce el siguiente efecto

$$\begin{pmatrix} \alpha \\ \beta \end{pmatrix} \to \begin{pmatrix} s & u \\ t & v \end{pmatrix} \begin{pmatrix} \alpha \\ \beta \end{pmatrix}. \qquad \text{(1.7)}$$

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes2_ES/fig3.png)

Figura 3: Izquierda: Un fotón incidente desde arriba; $s$ y $t$ son las amplitudes reflejada y transmitida, respectivamente. Derecha: Un fotón incidente desde abajo; $v$ y $u$ son las amplitudes reflejada y transmitida, respectivamente.

Podemos representar la acción del divisor de haz como una multiplicación matricial sobre la función de onda incidente, con la matriz dos por dos

$$\begin{pmatrix} s & u \\ t & v \end{pmatrix}. \qquad \text{(1.8)}$$

Debemos ahora determinar las restricciones sobre $s, t, u, v$. Debido a que las probabilidades deben sumar uno, la ecuación (1.5) implica que

$$|s|^2 + |t|^2 = 1, \qquad \text{(1.9)}$$

$$|u|^2 + |v|^2 = 1. \qquad \text{(1.10)}$$

El tipo de divisores de haz que usamos se llaman balanceados, lo que significa que las probabilidades de reflexión y transmisión son iguales. Así que las cuatro constantes deben tener el mismo módulo al cuadrado:

$$|s|^2 = |t|^2 = |u|^2 = |v|^2 = \tfrac{1}{2}. \qquad \text{(1.11)}$$

Probemos una conjetura para los valores. ¿Podríamos tener

$$\begin{pmatrix} s & u \\ t & v \end{pmatrix} = \begin{pmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{pmatrix}\ ? \qquad \text{(1.12)}$$

Esto falla si al actuar sobre funciones de onda normalizadas (o vectores columna) no se obtienen funciones de onda normalizadas. Así que probamos con un par de funciones de onda

$$\begin{pmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix}, \qquad \begin{pmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{pmatrix} \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}. \qquad \text{(1.13)}$$

Mientras que el primer ejemplo funciona, el segundo no, ya que $|1|^2 + |1|^2 = 2 \neq 1$. Una solución sencilla se logra cambiando el signo de $v$:

$$\begin{pmatrix} s & u \\ t & v \end{pmatrix} = \begin{pmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}. \qquad \text{(1.14)}$$

Comprobemos que esta matriz funciona en general. Así, al actuar sobre un estado $\begin{pmatrix} \alpha \\ \beta \end{pmatrix}$ con $|\alpha|^2 + |\beta|^2 = 1$ encontramos

$$\frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} \alpha \\ \beta \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} \alpha + \beta \\ \alpha - \beta \end{pmatrix}. \qquad \text{(1.15)}$$

En efecto, el estado resultante está bien normalizado. La probabilidad total es lo que esperamos

$$\begin{aligned}
& \tfrac{1}{2}|\alpha+\beta|^2 + \tfrac{1}{2}|\alpha-\beta|^2\\
& \quad = \tfrac{1}{2}\big(|\alpha|^2 + |\beta|^2 + \alpha\beta^* + \alpha^*\beta\big) + \tfrac{1}{2}\big(|\alpha|^2 + |\beta|^2 - \alpha\beta^* - \alpha^*\beta\big)\\
& \quad = |\alpha|^2 + |\beta|^2 = 1. \qquad \text{(1.16)}
\end{aligned}$$

El signo menos en la entrada inferior derecha de (1.14) significa que un fotón incidente desde abajo, al ser reflejado, tendrá su amplitud cambiada por un signo, o equivalentemente por un desfase de $\pi$ (¡compruébelo!). Este efecto, por supuesto, se realiza en la práctica. Un divisor de haz típico consiste en una placa de vidrio con un recubrimiento dieléctrico reflectante en un lado. El índice de refracción del recubrimiento se elige de manera que sea intermedio entre el del vidrio y el del aire. Una reflexión causa un desfase solo cuando la luz encuentra un material de mayor índice de refracción. Este es el caso en la transición de aire a recubrimiento, pero no en la transición de vidrio a recubrimiento. Por lo tanto, el divisor de haz representado por (1.14) tendría su recubrimiento en el lado inferior. Las ondas transmitidas no tienen desfase.

Otra posibilidad para una matriz de divisor de haz es

$$\frac{1}{\sqrt{2}} \begin{pmatrix} -1 & 1 \\ 1 & 1 \end{pmatrix}, \qquad \text{(1.17)}$$

que se realizaría mediante un recubrimiento dieléctrico en el lado superior. Puede comprobar rápidamente que, al igual que la matriz anterior, su acción también conserva la probabilidad. Llamaremos BS1 al divisor de haz de la izquierda y BS2 al de la derecha, y sus respectivas matrices serán

$$\text{BS1}:\ \frac{1}{\sqrt{2}} \begin{pmatrix} -1 & 1 \\ 1 & 1 \end{pmatrix}, \qquad \text{BS2}:\ \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}. \qquad \text{(1.18)}$$

Los dos divisores de haz se combinan para formar el interferómetro mostrado en la Figura 4. Si ahora suponemos una función de onda de fotón de entrada $\begin{pmatrix} \alpha \\ \beta \end{pmatrix}$ desde la izquierda, la función de onda de salida que entra a los detectores se obtiene actuando primero con la matriz BS1 y luego con la matriz BS2:

$$\begin{aligned}
\text{entrada:}\ \begin{pmatrix} \alpha \\ \beta \end{pmatrix} \quad \text{salida:}\ & \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \frac{1}{\sqrt{2}} \begin{pmatrix} -1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} \alpha \\ \beta \end{pmatrix}\\
& = \frac{1}{2}\begin{pmatrix} 0 & 2 \\ -2 & 0 \end{pmatrix}\begin{pmatrix} \alpha \\ \beta \end{pmatrix} = \begin{pmatrix} \beta \\ -\alpha \end{pmatrix}. \qquad \text{(1.19)}
\end{aligned}$$

Con la ayuda de este resultado, para cualquier estado de fotón de entrada podemos escribir inmediatamente el estado de fotón de salida que entra a los detectores.

Si el haz de fotones de entrada es $\begin{pmatrix} 0 \\ 1 \end{pmatrix}$, la salida del interferómetro es $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$, y por lo tanto se detectará un fotón en D0. Esto se muestra en la Figura 5. Podemos hacer una tabla muy sencilla con los posibles resultados y sus respectivas probabilidades $P$:

$$\begin{array}{ll}
\text{Resultado} & P \\
\text{fotón en D0} & 1 \\
\text{fotón en D1} & 0
\end{array} \qquad \text{(1.20)}$$

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes2_ES/fig4.png)

Figura 4: El interferómetro de Mach-Zehnder con las funciones de onda de entrada y salida indicadas.

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes2_ES/fig5.png)

Figura 5: Un fotón incidente desde abajo irá hacia D0.

Ahora bloqueemos el camino inferior, como se indica en la Figura 6. ¿Qué sucede entonces? Es mejor seguir el proceso sistemáticamente. El haz de entrada, actuado por BS1, da

$$\frac{1}{\sqrt{2}} \begin{pmatrix} -1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix}. \qquad \text{(1.21)}$$

Esto se indica en la figura, a la derecha de BS1. Luego se detiene la rama inferior, mientras que la rama superior continúa. La rama superior llega a BS2, y aquí la entrada es $\begin{pmatrix} \frac{1}{\sqrt{2}} \\ 0 \end{pmatrix}$, porque no llega nada de la rama inferior. Por lo tanto obtenemos una salida

$$\frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} \frac{1}{\sqrt{2}} \\ 0 \end{pmatrix} = \begin{pmatrix} \frac{1}{2} \\ \frac{1}{2} \end{pmatrix}. \qquad \text{(1.22)}$$

En este experimento hay tres resultados posibles: el fotón puede ser absorbido por el bloqueo, o puede ir hacia cualquiera de los dos detectores.

![Figura 6](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes2_ES/fig6.png)

Figura 6: La probabilidad de detectar el fotón en D1 puede cambiarse bloqueando uno de los caminos.

Como vemos en el diagrama, las probabilidades son:

$$\begin{array}{ll}
\text{Resultado} & P \\
\text{fotón en el bloqueo} & \tfrac{1}{2} \\
\text{fotón en D0} & \tfrac{1}{4} \\
\text{fotón en D1} & \tfrac{1}{4}
\end{array} \qquad \text{(1.23)}$$

Es notable que antes de bloquear el camino inferior no podíamos conseguir que un fotón llegara a D1. La probabilidad de llegar a D1 ahora es 1/4 y aumentó al bloquear un camino.

## 2. Bombas de Elitzur-Vaidman

Para ver que permitir que el fotón llegue a D1 bloqueando un camino es algo muy extraño, consideramos una situación imaginaria propuesta por los físicos Avshalom Elitzur y Lev Vaidman, de la Universidad de Tel Aviv, en Israel. Ellos imaginaron bombas con un tipo especial de disparador: un detector de fotones. Un tubo estrecho atraviesa cada bomba y en el medio del tubo hay un detector de fotones. Para detonar la bomba se envía un fotón dentro del tubo. El fotón es entonces detectado por el detector de fotones y la bomba explota. Si el detector de fotones está defectuoso, sin embargo, el fotón no es detectado en absoluto. Se propaga libremente a través del tubo y sale de la bomba. La bomba no explota.

He aquí la situación que queremos abordar. Supongamos que tenemos una cierta cantidad de bombas de Elitzur-Vaidman (EV), pero sabemos que algunas de ellas se han vuelto defectuosas. ¿Cómo podríamos saber si una bomba es operativa sin detonarla? Supongamos, a efectos del problema, que no podemos examinar el detector sin destruir la bomba.

Parece que nos enfrentamos a una situación imposible. Si enviamos un fotón al tubo del detector y no sucede nada, sabemos que la bomba está defectuosa, pero si la bomba es operativa, simplemente explotaría. Parece imposible confirmar que el detector de fotones de la bomba está funcionando sin probarlo. En efecto, es imposible en la física clásica. Sin embargo, no es imposible en la mecánica cuántica. Como veremos, ¡podemos realizar lo que puede llamarse una medición libre de interacción!

Ahora colocamos una bomba EV en el camino inferior del interferómetro, con el tubo del detector adecuadamente alineado. Supongamos que enviamos un fotón como se muestra. Si la bomba está defectuosa es como si no hubiera detector, la rama inferior del interferómetro está libre y todos los fotones que enviemos terminarán en D0,

![Figura 7](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes2_ES/fig7.png)

Figura 7: Un interferómetro de Mach-Zehnder y una bomba de Elitzur-Vaidman insertada en la rama inferior, con el tubo del detector adecuadamente alineado. Si la bomba está defectuosa, todos los fotones incidentes terminarán en D0. Si un fotón termina en D1 sabemos que la bomba es operativa, ¡aunque el fotón nunca entró en el detector de la bomba!

igual que lo hicieron en la Figura 5.

$$\begin{array}{ll}
\text{Resultado} & P \\
\text{fotón en D0, sin explosión} & 1 \\
\text{fotón en D1, sin explosión} & 0 \\
\text{la bomba explota} & 0
\end{array} \qquad \text{(2.24)}$$

Si la bomba funciona, por otro lado, tenemos la situación que teníamos en la Figura 6, donde colocamos un bloqueo en la rama inferior del interferómetro:

$$\begin{array}{ll}
\text{Resultado} & P \\
\text{la bomba explota} & \tfrac{1}{2} \\
\text{fotón en D0, sin explosión} & \tfrac{1}{4} \\
\text{fotón en D1, sin explosión} & \tfrac{1}{4}
\end{array} \qquad \text{(2.25)}$$

Supongamos que la bomba está funcionando. Entonces el 50% de las veces el fotón la golpeará y explotará, el 25% de las veces el fotón terminará en D0 y no podremos saber si está defectuosa o no. Pero el 25% de las veces el fotón terminará en D1, y dado que esto era imposible para una bomba defectuosa, ¡hemos aprendido que la bomba es operativa! Hemos aprendido esto aunque el fotón nunca haya pasado por la bomba; terminó en D1. Si piensa en esto, seguramente se dará cuenta de que es extremadamente sorprendente y contraintuitivo. Pero es cierto, y los experimentos (¡sin usar bombas!) han confirmado que este tipo de medición libre de interacción es efectivamente posible.

Sarah Geller transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.

------------------------------------------------------------------------

MIT OpenCourseWare https://ocw.mit.edu

8.04 Física Cuántica I Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.


---

<!-- MIT8.04_LecNotes3_ES.md -->

# Naturaleza corpuscular de la luz y naturaleza ondulatoria de la materia

## Vídeos de esta clase (YouTube)

**Lección 3: Photoelectric effect, Compton scattering, and de Broglie wavelength.**

- [The photoelectric effect](https://www.youtube.com/watch?v=byEaU9ILHmw)
- [Units of h and Compton wavelength of particles](https://www.youtube.com/watch?v=S9RjSQro2e0)
- [Compton Scattering](https://www.youtube.com/watch?v=WR88_Vzfcx4)
- [de Broglie’s proposal](https://www.youtube.com/watch?v=dnuZx9fZHsU)

------------------------------------------------------------------------

*B. Zwiebach* *16 de febrero de 2016*

## Contenido

1.  Efecto fotoeléctrico
2.  Dispersión de Compton
3.  Ondas de materia

## 1. Efecto fotoeléctrico

El efecto fotoeléctrico fue observado por primera vez por Heinrich Hertz en 1887. Cuando se irradian placas metálicas pulidas, observó, estas pueden emitir electrones, entonces llamados “foto-electrones”. Los electrones emitidos producen así una corriente fotoeléctrica. Las observaciones clave fueron:

- Existe una frecuencia umbral $\nu_0$. Solo para frecuencias $\nu > \nu_0$ hay corriente fotoeléctrica. La frecuencia $\nu_0$ depende del metal y de la configuración de los átomos en la superficie. También se ve afectada por las inhomogeneidades.

- La magnitud de la corriente fotoeléctrica es proporcional a la intensidad de la fuente de luz.

- La energía de los fotoelectrones es independiente de la intensidad de la fuente de luz.

Una explicación natural de las características de este efecto no llegó hasta 1905, cuando Einstein explicó las propiedades anteriores postulando que la energía de la luz es transportada por cuantos discretos (llamados posteriormente fotones) con energía $h\nu$. Aquí $h$ es la constante de Planck, la constante que Planck utilizó para ajustar la energía del cuerpo negro en función de la frecuencia.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes3_ES/fig1.png)

Figura 1: Los electrones en un metal están ligados. Si la energía del fotón es mayor que la función de trabajo $W$, un electrón puede ser expulsado.

Un material dado tiene una energía característica $W$, llamada función de trabajo, que es la energía mínima requerida para expulsar un electrón. Esta no es fácil de calcular porque es el resultado de la interacción de muchos electrones con el trasfondo de átomos. Sin embargo, es fácil de medir. Cuando se irradia la superficie del material, los electrones del material absorben la energía de los fotones incidentes. Si la energía impartida a un electrón por la absorción de un solo fotón es mayor que la función de trabajo $W$, entonces el electrón es expulsado con energía cinética $E_{e^-}$ igual a la diferencia entre la energía del fotón y la función de trabajo:

$$E_{e^-} = \frac{1}{2}mv^2 = h\nu - W = E_\gamma - W. \qquad \text{(1.1)}$$

Esta ecuación, escrita por Einstein, explica las características experimentales señaladas anteriormente, una vez que suponemos que los cuantos actúan sobre electrones individuales para expulsarlos. La frecuencia umbral se define mediante

$$h\nu_0 = W, \qquad \text{(1.2)}$$

ya que da lugar a un fotoelectrón con energía cero. Para $\nu > \nu_0$ los electrones serán expulsados. Aumentar la intensidad de la fuente de luz incrementa la tasa de llegada de fotones, lo cual incrementará la magnitud de la corriente, pero no cambiará la energía de los fotoelectrones porque no cambia la energía de cada cuanto incidente.

La ecuación (1.2) permitió a Einstein hacer una predicción: la energía cinética de los fotoelectrones aumenta linealmente con la frecuencia de la luz. La predicción de Einstein fue confirmada experimentalmente por Millikan (1915), quien midió cuidadosamente las energías de los fotoelectrones y confirmó su dependencia lineal con la energía. El cuidadoso trabajo de Millikan le permitió determinar el valor de la constante de Planck $\hbar$ con una precisión mejor que el 1%. Aun así, persistía el escepticismo y los físicos todavía no estaban convencidos de la naturaleza corpuscular de estos cuantos de luz.

**Ejemplo:** Considere luz ultravioleta con longitud de onda $\lambda = 290\,\text{nm}$ incidente sobre un metal con función de trabajo $W = 4.05\,\text{eV}$. ¿Cuál es la energía del fotoelectrón y cuál es su velocidad?

**Solución:** Es útil resolver estos problemas sin tener que buscar constantes. Para ello, conviene recordar esta relación útil

$$\hbar c = 197.33\ \text{MeV·fm}, \qquad \hbar \equiv \frac{h}{2\pi}, \qquad \text{(1.3)}$$

donde $\text{MeV} = 10^6\,\text{eV}$ y $\text{fm} = 10^{-15}\,\text{m}$. Usemos esto para calcular la energía del fotón. En este caso,

$$E_\gamma = h\nu = \frac{2\pi\hbar c}{\lambda} = \frac{2\pi \cdot 197.33\ \text{MeV·fm}}{290 \times 10^{-9}\,\text{m}} = \frac{2\pi \cdot 197.33}{290}\ \text{eV} \approx 4.28\ \text{eV}, \qquad \text{(1.4)}$$

y por tanto

$$E_{e^-} = E_\gamma - W = 0.23\ \text{eV}. \qquad \text{(1.5)}$$

Para calcular la energía escribimos

$$0.23\ \text{eV} = \frac{1}{2}m_e v^2 = \frac{1}{2}(m_e c^2)\left(\frac{v}{c}\right)^2 \qquad \text{(1.6)}$$

Recordando que $m_e c^2 \simeq 511{,}000\ \text{eV}$ se obtiene

$$\frac{0.46}{511000} = \left(\frac{v}{c}\right)^2 \quad \Rightarrow \quad \frac{v}{c} = 0.0009488. \qquad \text{(1.7)}$$

Con $c = 300{,}000\ \text{Km/s}$ finalmente obtenemos $v \simeq 284.4\ \text{Km/s}$.

Este es un buen momento para considerar las unidades, en particular las unidades de $h$. Podemos preguntarnos: ¿existe una cantidad física que tenga las unidades de $h$? La respuesta es sí, como veremos ahora. De la ecuación $E = h\nu$, tenemos

$$[h] = \frac{[E]}{[\nu]} = \frac{ML^2/T^2}{1/T} = L \cdot M\frac{L}{T}, \qquad \text{(1.8)}$$

donde $[\cdot]$ da las unidades de una cantidad, y $M$, $L$, $T$ son las unidades de masa, longitud y tiempo, respectivamente. Hemos escrito la expresión más a la derecha como un producto de unidades de longitud y momento. Por lo tanto

$$[h] = [r \times p] = [L]. \qquad \text{(1.9)}$$

¡Vemos que $h$ tiene unidades de momento angular! De hecho, para una partícula de espín un medio, la magnitud del momento angular de espín es $\frac{1}{2}\hbar$.

Con $[h] = [r][p]$ vemos también que se tiene una manera canónica de asociar una longitud a cualquier partícula de una masa dada $m$. En efecto, usando la velocidad de la luz, podemos construir el momento $p = mc$, y entonces la longitud $\ell$ se obtiene de la razón $h/p$. Esta es de hecho la longitud de onda Compton $\lambda_C$ de una partícula:

$$\lambda_C = \frac{h}{mc} \qquad \text{(1.10)}$$

que tiene unidades de longitud; esto se llama la longitud de onda Compton de una partícula de masa $m$. Nótese que esta longitud es independiente de la velocidad de la partícula. ¡La longitud de onda de de Broglie de la partícula usa el momento verdadero de la partícula, no $mc$! Por lo tanto, las longitudes de onda Compton y de de Broglie no deben confundirse.

Es posible obtener cierta intuición física para la longitud de onda Compton $\lambda_C$ de una partícula. Afirmamos que $\lambda_C$ es la longitud de onda de un fotón cuya energía es igual a la energía en reposo de la partícula. En efecto, tendríamos

$$mc^2 = h\nu = h\frac{c}{\lambda} \quad \Rightarrow \quad \lambda = \frac{h}{mc}, \qquad \text{(1.11)}$$

confirmando la afirmación. Supongamos que se intenta localizar una partícula puntual de masa $m$. Si se usa luz, la precisión posible en la posición de la partícula es aproximadamente la longitud de onda de la luz. Una vez que usamos luz con $\lambda < \lambda_C$, los fotones transportan más energía que la energía en reposo de la partícula. Es posible entonces que la energía de los fotones se convierta en la creación de más partículas de masa $m$, dificultando, si no imposibilitando, la localización de la partícula. La longitud de onda Compton es la escala de longitud en la cual necesitamos la teoría cuántica de campos relativista para tomar en cuenta los posibles procesos de creación y aniquilación de partículas.

Calculemos la longitud de onda Compton del electrón:

$$\lambda_C(e) = \frac{h}{m_e c} = \frac{2\pi\hbar c}{m_e c^2} = \frac{2\pi \cdot 197.33\ \text{MeV·fm}}{0.511\ \text{MeV}} = 2426\ \text{fm} = 2.426\ \text{pm}. \qquad \text{(1.12)}$$

Esta longitud es unas 20 veces más pequeña que el radio de Bohr (53 pm) y unas dos mil veces el tamaño de un protón (1 fm). La longitud de onda Compton del electrón aparece en la fórmula del cambio de longitud de onda del fotón en el proceso llamado dispersión de Compton.

## 2. Dispersión de Compton

Originalmente Einstein no dejó claro que el cuanto de luz significara una partícula de luz. En 1916, sin embargo, postuló que el cuanto transportaría también momento además de energía, dejando el caso mucho más claro a favor de una partícula. En relatividad, la energía, el momento y la masa en reposo de una partícula están relacionados mediante

$$E^2 - p^2 c^2 = m^2 c^4. \qquad \text{(2.13)}$$

(Compárese esto con la ecuación clásica $E = p^2/2m$.) Por supuesto, también se pueden expresar la energía y el momento de la partícula en términos de la velocidad:

$$E = \frac{mc^2}{\sqrt{1 - \frac{v^2}{c^2}}}, \qquad p = \frac{mv}{\sqrt{1 - \frac{v^2}{c^2}}}. \qquad \text{(2.14)}$$

Debería usar estas expresiones para confirmar que (2.13) se cumple (donde $|\vec{p}| = p$). Una partícula que se mueve con la velocidad de la luz, como el fotón, debe tener masa en reposo nula, ya que de lo contrario su energía y momento serían infinitos debido a los denominadores que se anulan. Con la masa en reposo fijada en cero, la ecuación (2.13) da la relación entre la energía del fotón $E_\gamma$ y el momento del fotón $p_\gamma$:

$$E_\gamma = p_\gamma c. \qquad \text{(2.15)}$$

Luego, usando $\lambda\nu = c$, llegamos a

$$p_\gamma = \frac{E_\gamma}{c} = \frac{h\nu}{c} = \frac{h}{\lambda}. \qquad \text{(2.16)}$$

Volveremos a ver esta relación más adelante cuando discutamos las ondas de materia.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes3_ES/fig2.png)

Figura 2: Luz no polarizada incidente sobre un electrón se dispersa en un ángulo $\theta$. Clásicamente, esto se describe mediante la dispersión de Thomson. La luz no cambia de frecuencia durante este proceso.

Compton llevó a cabo experimentos (1923–1924) dispersando rayos X en un blanco de carbono. Los rayos X corresponden a energías de fotón en el rango de 100 eV a 100 KeV. El objetivo era dispersar fotones de rayos X en electrones libres, y con cierta salvedad, los electrones en los átomos se comportan de esa manera.

La contraparte clásica del experimento de Compton es la dispersión de ondas electromagnéticas en electrones libres, llamada dispersión de Thomson. Aquí una onda electromagnética incide sobre un electrón. El campo eléctrico de la onda sacude al electrón, que oscila con la frecuencia del campo incidente. La oscilación del electrón produce un campo radiado, de la misma frecuencia que la radiación incidente. En la dispersión de Thomson clásica, la sección eficaz diferencial de dispersión viene dada por

$$\frac{d\sigma}{d\Omega} = \left(\frac{e^2}{mc^2}\right)^2 \frac{1}{2}\left(1 + \cos^2\theta\right), \qquad \text{(2.17)}$$

donde $\theta$ es el ángulo entre la onda incidente y la onda dispersada, con la energía radiada a la misma frecuencia que la luz incidente. Esto se muestra en la Figura 2. La sección eficaz tiene unidades de longitud al cuadrado, o área, como debe ser. Representa el área que extraería de la onda plana incidente la cantidad de energía que dispersa el electrón. En efecto, la cantidad $e^2/(mc^2)$ se llama el radio clásico del electrón y es de aproximadamente 2.8 fm, ¡no mucho más grande que un protón!

Si tratamos la luz como fotones, el proceso elemental que ocurre es una colisión entre dos partículas: un fotón incidente y un electrón aproximadamente estacionario. Se pueden demostrar rápidamente dos hechos:

- El fotón no puede ser absorbido por el electrón. Esto es inconsistente con la conservación de energía y momento (ejercicio).

- El fotón debe perder algo de energía y por lo tanto la longitud de onda final del fotón $\lambda_f$ debe ser mayor que la longitud de onda inicial del fotón $\lambda_i$. Esto es claro en el sistema de referencia del laboratorio, donde el electrón inicialmente estacionario debe retroceder y así adquirir cierta energía cinética.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes3_ES/fig3.png)

Figura 3: Los resultados del experimento de dispersión de Compton. La longitud de onda del fotón incidente es $\lambda_i$, y la longitud de onda del fotón dispersado es $\lambda_f \simeq \lambda_i + \ell_C$, correspondiente a $\theta = 90°$.

En efecto, las observaciones de Compton no concordaban con las predicciones de la dispersión de Thomson: los rayos X cambiaban de frecuencia tras la dispersión. Un cálculo usando la conservación de energía y momento muestra que el cambio de longitud de onda está correlacionado con el ángulo entre el fotón dispersado y el fotón original:

$$\lambda_f = \lambda_i + \frac{h}{m_e c}(1 - \cos\theta) = \lambda_i + \lambda_C(1 - \cos\theta). \qquad \text{(2.18)}$$

Nótese la aparición de la longitud de onda Compton del electrón, la partícula de la cual dispersa el fotón. La pérdida máxima de energía para el fotón ocurre en $\theta = \pi$, donde

$$\lambda_f(\theta = 180°) = \lambda_i + 2\lambda_C. \qquad \text{(2.19)}$$

El cambio máximo posible de longitud de onda es $2\lambda_C$. Para $\theta = \frac{\pi}{2}$ el cambio de longitud de onda es exactamente $\lambda_C$

$$\lambda_f(\theta = 90°) = \lambda_i + \lambda_C. \qquad \text{(2.20)}$$

El experimento de Compton usó rayos X de molibdeno con energía y longitud de onda

$$E_\gamma \approx 17.5\ \text{keV}, \qquad \lambda_i = 0.0709\ \text{nm}, \qquad \text{(2.21)}$$

incidiendo sobre un blanco de carbono. Colocando el detector en un ángulo $\theta = 90°$, la gráfica de la intensidad (o número de fotones dispersados) en función de la longitud de onda se muestra en la Figura 2. Se encuentra un pico para $\lambda_f = 0.0731\ \text{nm}$, pero también un segundo pico en la longitud de onda original $\lambda_i = 0.0709\ \text{nm}$.

El pico en $\lambda_f$ es el esperado: $\lambda_f - \lambda_i \simeq 2.2\ \text{pm}$, que es aproximadamente la longitud de onda Compton de 2.4 pm. Dado que los fotones tienen energías de 17 KeV y las energías de los estados ligados del carbono son de aproximadamente 300 eV, el pico esperado representa instancias en las que el átomo es ionizado por la colisión y es una buena aproximación considerar los electrones expulsados. El pico en $\lambda_i$ representa un proceso en el que un electrón recibe algo de momento del fotón pero permanece ligado. Esto no es muy improbable: el momento típico de un electrón ligado es en realidad comparable al momento del fotón. En este caso el fotón se dispersa a 90° y el momento de retroceso lo lleva todo el átomo. La longitud de onda Compton relevante es entonces la del átomo. Dado que la masa del átomo de carbono es varios miles de veces mayor que la masa del electrón, la longitud de onda Compton del átomo es mucho menor que la longitud de onda Compton del electrón y no debería haber cambio detectable en la longitud de onda del fotón.[1]

## 3. Ondas de materia

Como hemos visto, la luz se comporta tanto como partícula como onda. Este tipo de comportamiento se suele denominar dualidad: la realidad completa del objeto se captura usando tanto las características ondulatorias como las corpusculares del objeto. El fotón es una partícula de energía $E_\gamma$, pero tiene frecuencia $\nu$, que es un atributo ondulatorio, con $E = h\nu$. Es una partícula con momento $p_\gamma$ pero también tiene una longitud de onda $\lambda$, un atributo ondulatorio, dado por (2.16)

$$\lambda = \frac{h}{p_\gamma}. \qquad \text{(3.22)}$$

En 1924, Louis de Broglie propuso que la dualidad onda/partícula del fotón era universal, y por lo tanto válida también para las partículas materiales. De esta manera conjeturó la naturaleza ondulatoria de la materia. Inspirado por (3.22), de Broglie postuló que, asociada a una partícula material con momento $p$, existe una onda plana de longitud de onda $\lambda$ dada por

$$\lambda = \frac{h}{p}. \qquad \text{(3.23)}$$

Esta es una propiedad plenamente cuántica: si $h \to 0$, entonces $\lambda \to 0$, y las partículas no tienen propiedades ondulatorias. Una consecuencia interesante de esto es que las partículas materiales pueden difractarse o interferir. En el famoso experimento de Davisson-Germer (1927), los electrones inciden sobre una superficie metálica y se encuentra que a ciertos ángulos hay picos en la intensidad de los electrones dispersados. Los picos mostraban el efecto de interferencia constructiva de la dispersión en la red de átomos del metal, demostrando la naturaleza ondulatoria de los electrones. También se puede hacer interferencia de doble rendija con electrones, y el experimento se puede realizar disparando un electrón a la vez. Un experimento reciente \[arXiv:1310.8343\] de Eibenberger et al. reporta interferencia usando moléculas con 810 átomos y una masa que excede las 10 000 uma (¡eso es 20 millones de veces la masa del electrón!).

La longitud de onda de de Broglie se puede calcular para estimar si los efectos cuánticos son importantes. Considere para este propósito una partícula de masa $m$ y momento $p$ incidente sobre un objeto de tamaño $x$, como se ilustra en la Figura 3. Sea $\lambda = h/p$ la longitud de onda de de Broglie de la partícula. La naturaleza ondulatoria de la partícula no es importante si $\lambda$ es mucho menor que $x$. Así, la “aproximación clásica”, en la que los efectos ondulatorios son despreciables, requiere

$$\text{Efectos ondulatorios despreciables:} \quad \frac{\lambda}{x} \ll 1. \qquad \text{(3.24)}$$

Usando $\lambda = h/p$, esto da

$$\text{Efectos ondulatorios despreciables:} \quad xp \gg h, \qquad \text{(3.25)}$$

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes3_ES/fig4.png)

Figura 4: Una partícula de momento $p$ incidente sobre un obstáculo de tamaño $x$.

una relación en la que ambos lados tienen unidades de momento angular.

El comportamiento clásico es un límite sutil de la mecánica cuántica: un campo electromagnético clásico requiere un gran número de fotones. Sin embargo, cualquier estado con un número exacto y fijo de fotones, incluso si es grande, no es clásico. Los estados electromagnéticos clásicos son los llamados estados coherentes, en los que el número de fotones fluctúa.

------------------------------------------------------------------------

Andrew Turner transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.

------------------------------------------------------------------------

MIT OpenCourseWare https://ocw.mit.edu

8.04 Física Cuántica I Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

# Apéndice: Lista de problemas 1 (Problem Set 1, 2016)

**Física Cuántica I (8.04), Primavera de 2016** **Tarea 1**

*Instituto Tecnológico de Massachusetts* *Departamento de Física* *4 de febrero de 2016*

*Fecha de entrega: jueves, 11 de febrero de 2016, 5:00pm*

**Avisos**

- Por favor, ponga su nombre y el número de su sección en la parte superior de su lista de problemas, y colóquela en la casilla de 8.05 etiquetada con el número de su sección cerca de 8-395 antes de las 5:00pm.

- Puede resultarle entretenido leer las primeras páginas del libro de Dirac sobre Mecánica Cuántica.

## Problema 1

**Colapso radiativo de un átomo clásico.** \[10 puntos\]

En un universo clásico, podríamos intentar construir un átomo de hidrógeno colocando un electrón en una órbita circular alrededor de un protón. Sabemos, sin embargo, que un electrón no relativista y acelerado radia energía a una tasa dada por la fórmula de Larmor:

$$\frac{dE}{dt} = -\frac{2}{3}\frac{e^2 a^2}{c^3}.$$

Aquí $e$ es la carga del electrón y $a$ es la magnitud de la aceleración del electrón. Así que el átomo clásico puede tener un problema de estabilidad. Queremos averiguar cuán grande es este efecto. En las unidades con las que trabajamos, la energía potencial del electrón en presencia del protón es $V = -e^2/r$ y la magnitud de la fuerza de atracción es $e^2/r^2$.

1.  Demuestre que, para un electrón no relativista, la energía $\Delta E$ perdida por revolución es pequeña comparada con la energía cinética $K$ del electrón. Hágalo calculando el cociente $\Delta E/K$. Por lo tanto, es posible considerar la órbita como circular en cualquier instante, aunque el electrón acabe cayendo en espiral hacia el protón.

2.  Una buena estimación del tamaño del átomo de hidrógeno es 50 pm (pico-metros), y una buena estimación del tamaño del núcleo es 1 fm (femto-metro). Compare la velocidad del electrón calculada clásicamente con la velocidad de la luz para un radio orbital de 50 pm, 1 pm y 1 fm.

3.  Calcule cuánto tiempo tardaría el electrón en caer en espiral desde 50 pm hasta 1 pm. ¿Está justificado ignorar las correcciones relativistas? ¿Cambiaría mucho la respuesta usando la aproximación no relativista para una espiral desde 50 pm hasta 1 fm?

4.  A medida que el electrón se aproxima al protón, ¿qué le ocurre a su energía? ¿Existe un valor mínimo de la energía que puede tener el electrón?

## Problema 2

**Energías cuantizadas.** \[5 puntos\]

Considere un electrón en movimiento circular alrededor de un protón fijo (pesado) como modelo del átomo de hidrógeno. Sea $V = -e^2/r$ la energía potencial del electrón.

1.  Suponiendo una órbita circular, encuentre las relaciones entre la energía cinética $K$ del electrón, su energía potencial $V$ y la energía total $E$.

2.  Suponga que la magnitud $L$ del momento angular del electrón está cuantizada y es igual a $n\hbar$, donde $n$ es un entero positivo. Encuentre los valores cuantizados $E_n$ de la energía total y los radios orbitales asociados $r_n$. Exprese sus respuestas en términos de $n$, la energía en reposo $E_e = m_e c^2$ del electrón, su longitud de onda Compton $\bar\lambda = \dfrac{\hbar}{m_e c}$, y la constante de estructura fina $\alpha = \dfrac{e^2}{\hbar c}$.

## Problema 3

**Relaciones de De Broglie y la escala de los efectos cuánticos.** \[10 puntos\]

**(a) Partículas materiales como ondas**

Si se puede asociar una longitud de onda a toda partícula en movimiento, ¿por qué no somos forzosamente conscientes de esta propiedad en nuestra experiencia cotidiana? Para responder, calcule la longitud de onda de de Broglie $\lambda = h/p$ (con $h = 6.6 \times 10^{-34}\ \text{J·s}$) de cada una de las siguientes partículas:

1.  un automóvil de masa 2000 kg que viaja a una velocidad de 50 mph (22 m/s)

2.  una canica de masa 10 g que se mueve con una velocidad de 10 cm/s

3.  una partícula de humo de 100 nm de diámetro y masa 1 fg agitada por moléculas de aire a temperatura ambiente ($T = 300\,\text{K}$) (suponga que la partícula tiene la misma energía cinética de traslación que el promedio térmico de las moléculas de aire, $KE = \frac{3}{2}k_B T$, con $k_B = 1.38 \times 10^{-23}\ \text{J/K}$)

4.  un átomo de $^{87}\text{Rb}$ enfriado por láser hasta una temperatura de $T = 100\,\mu\text{K}$. De nuevo, suponga $KE = \frac{3}{2}k_B T$.

**(b) Ondas de luz como partículas**

El efecto fotoeléctrico sugiere que la luz de frecuencia $\nu$ puede considerarse formada por fotones de energía $E = h\nu$, con $h = 6.6 \times 10^{-34}\ \text{J·s}$.

1.  La luz visible tiene una longitud de onda en el rango de 400-700 nm. ¿Cuáles son la energía y la frecuencia de un fotón de luz visible?

2.  El microondas de mi cocina funciona aproximadamente a 2.5 GHz con una potencia máxima de 300 W. ¿Cuántos fotones por segundo puede emitir? ¿Y un láser de baja potencia (10 mW a 633 nm), o un teléfono móvil (0.25 W a 850 MHz)?

3.  ¿Cuántos fotones de microondas de ese tipo hacen falta para calentar 200 ml de agua en 10 °C? (La capacidad calorífica del agua es aproximadamente 4 J/g·K, y la densidad es 1 g/ml.)

4.  Para una potencia dada de una onda electromagnética, ¿espera que una descripción de onda clásica funcione mejor para frecuencias de radio, o para rayos X?

## Problema 4

**Práctica con números complejos.** \[15 puntos\]

Un número complejo puede escribirse tanto en forma cartesiana como en forma polar

$$z = a + ib = r e^{i\theta}, \qquad |z| \equiv \sqrt{a^2 + b^2}.$$

Los números reales $a$ y $b$ son, respectivamente, la parte real y la parte imaginaria de $z$. Los números reales $r$ y $\theta$ son, respectivamente, la magnitud y la fase de $z$. Llamamos a $|z|$ la norma de $z$. Use esta definición de $z$ en lo que sigue:

1.  Use desarrollos de Taylor para derivar la fórmula de Euler

$$e^{i\theta} = \cos\theta + i\sin\theta.$$

1.  Escriba $a$ y $b$ en términos de $r$ y $\theta$, y viceversa.

2.  Los números complejos se ven como vectores en un “plano complejo” bidimensional. La multiplicación de un número complejo por una fase (un número complejo de magnitud unidad) equivale a una rotación en el plano complejo.

<!-- -->

1.  Demuestre que la multiplicación por $i$ equivale a una rotación de 90°: $iz = r e^{i(\theta + \pi/2)}$.

2.  Escriba $iz$ en términos de $a$ y $b$. ¿Cuál es la parte real de $iz$?

3.  Demuestre que la multiplicación por $e^{i\phi}$ equivale a una rotación en $\phi$.

<!-- -->

1.  El conjugado complejo $z^*$ de un número complejo $z = a + ib$ es $z^* = a - ib$. Un número complejo $z$ es realmente real si $z = z^*$, lo que significa que su parte imaginaria es cero. Un número complejo $z$ es realmente imaginario si $z = -z^*$, lo que implica que su parte real es cero.

<!-- -->

1.  ¿Existe un número que sea a la vez real y puramente imaginario?

2.  ¿Qué es $(z^*)^*$? Demuestre que $z^* = r e^{-i\theta}$.

3.  Exprese la parte real y la parte imaginaria de $z$ en términos de $z$ y $z^*$.

4.  Demuestre que $zz^*$ es real y evalúelo para expresarlo en términos de $a$ y $b$, en términos de $r$, y en términos de $|z|$.

<!-- -->

1.  Usando la fórmula de Euler, derive fórmulas para $\cos 2\theta$, $\sin 2\theta$, $\cos 3\theta$ y $\sin 3\theta$, todas en términos de $\sin\theta$ y $\cos\theta$. Derive fórmulas para $\cos(A+B)$ y $\sin(A+B)$, ambas en términos de senos y cosenos de $A$ y $B$.

## Problema 5

**¿Absorción?** \[5 puntos\]

Un fotón colisiona con un electrón libre. Explique por qué el fotón no puede ser absorbido por completo.

## Problema 6

**Interferómetro de Mach-Zehnder.** \[10 puntos\]

Considere el interferómetro de Mach-Zehnder y suponga un haz de entrada de la forma $\begin{pmatrix}\alpha\\ \beta\end{pmatrix}$. Llame $P_0$ y $P_1$ a las probabilidades de detección en $D_0$ y $D_1$.

1.  Calcule $P_0$ y $P_1$ suponiendo que insertamos un desfasador con fase $\delta_l$ en el brazo inferior del interferómetro.

2.  Calcule $P_0$ y $P_1$ suponiendo que insertamos un desfasador con fase $\delta_u$ en el brazo superior del interferómetro.

3.  Calcule $P_0$ y $P_1$ suponiendo que insertamos los dos desfasadores simultáneamente.

## Problema 7

**¡Bombas de Elitzur-Vaidman!** \[10 puntos\]

1.  Suponga que decide probar bombas con un interferómetro de Mach-Zehnder repetidamente hasta que el estado de una bomba dada sea cierto más allá de toda duda razonable. ¿Qué fracción de las bombas que funcionan se certifica sin detonación?

2.  Suponga que el 80% de las bombas en su posesión son defectuosas. Elige una al azar y la prueba con un interferómetro de Mach-Zehnder enviando un fotón. Detecta el fotón en $D_0$. ¿Cuál es la probabilidad de que la bomba sea defectuosa?

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*

[1] Gracias a V. Vuletic por una aclaración sobre este punto.


---

<!-- MIT8.04_LecNotes4_ES.md -->

# Lección 4

## Vídeos de esta clase (YouTube)

**Lección 4: de Broglie matter waves. Group velocity and stationary phase. Wave for a free particle.**

- [de Broglie wavelength in different frames](https://www.youtube.com/watch?v=8x94EgM2Mpg)
- [Galilean transformation of ordinary waves](https://www.youtube.com/watch?v=YdtHAIh-kas)
- [The frequency of a matter wave](https://www.youtube.com/watch?v=3_qvO8bKGus)
- [Group velocity and stationary phase approximation](https://www.youtube.com/watch?v=-UgQEHHXTRM)
- [Motion of a wave-packet](https://www.youtube.com/watch?v=i81OpQJIH8U)
- [The wave for a free particle](https://www.youtube.com/watch?v=T6TQHNXy5Wg)

------------------------------------------------------------------------

*B. Zwiebach* *18 de febrero de 2016*

## Contenido

1.  Longitud de onda de de Broglie y transformaciones de Galileo
2.  Velocidades de fase y de grupo
3.  Elección de la función de onda para una partícula libre

## 1. Longitud de onda de de Broglie y transformaciones de Galileo

Hemos visto que a toda partícula libre con momento $p$ podemos asociarle una onda plana, o una “onda de materia”, con longitud de onda de de Broglie $\lambda = h/p$, con $p = |\vec{p}|$. La pregunta es, ¿ondas de qué? Bueno, esta onda se reconoce eventualmente como un ejemplo de lo que se llama la función de onda. La función de onda, como veremos, está gobernada por la ecuación de Schrödinger. Como hemos insinuado, la función de onda nos da información sobre probabilidades, e iremos desarrollando esta idea en detalle.

¿Tiene la onda propiedades direccionales o de polarización como los campos eléctrico y magnético en una onda electromagnética? Sí, existe un análogo de esto, aunque no profundizaremos en ello ahora. ¡El análogo de la polarización corresponde al espín! Los efectos del espín son despreciables en muchos casos (velocidades pequeñas, ausencia de campos magnéticos, por ejemplo) y por esta razón usamos simplemente una onda escalar, un número complejo

$$\Psi(x, t) \in \mathbb{C} \qquad \text{(1.1)}$$

que depende del espacio y del tiempo. Surgen de manera natural un par de preguntas obvias. ¿Es medible la función de onda? ¿Qué tipo de objeto es? ¿Qué describe? Para obtener intuición sobre esto, consideremos cómo perciben distintos observadores la longitud de onda de de Broglie de una partícula, lo cual nos ayudará a entender qué tipo de ondas estamos considerando. Recordemos que

$$p = \frac{h}{\lambda} = \frac{h}{2\pi}\frac{2\pi}{\lambda} = \hbar k, \qquad \text{(1.2)}$$

donde $k$ es el número de onda. ¿Cómo se comportaría esta onda bajo un cambio de referencial?

Consideramos entonces dos referenciales $S$ y $S'$ con los ejes $x$ y $x'$ alineados, y con $S'$ moviéndose hacia la derecha a lo largo de la dirección $+x$ de $S$ con velocidad constante $v$. En el instante $t=0$, los orígenes de ambos referenciales coinciden.

Las coordenadas de espacio y tiempo de los dos referenciales están relacionadas por una transformación de Galileo, que establece que

$$x' = x - vt, \qquad t' = t . \qquad \text{(1.3)}$$

En efecto, el tiempo transcurre a la misma velocidad en todos los referenciales galileanos, y la relación entre $x$ y $x'$ es evidente a partir del arreglo mostrado en la Fig. 1.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes4_ES/fig1.png)

Figura 1: El referencial $S'$ se mueve con velocidad $v$ a lo largo de la dirección $x$ del referencial $S$. Una partícula de masa $m$ se mueve con velocidad $\tilde v$, y por lo tanto con momento $p = m\tilde v$, en el referencial $S$.

Supongamos ahora que ambos observadores se centran en una partícula de masa $m$ que se mueve con velocidad no relativista. Llamemos a la velocidad y al momento en el referencial $S$ como $\tilde v$ y $p = m\tilde v$, respectivamente. Se sigue, derivando respecto de $t = t'$ la primera ecuación en (1.3), que

$$\frac{dx'}{dt'} = \frac{dx}{dt} - v, \qquad \text{(1.4)}$$

lo cual significa que la velocidad de la partícula $\tilde v\,'$ en el referencial $S'$ está dada por

$$\tilde v\,' = \tilde v - v . \qquad \text{(1.5)}$$

Multiplicando por la masa $m$ encontramos la relación entre los momentos en los dos referenciales

$$p' = p - mv . \qquad \text{(1.6)}$$

El momento $p'$ en el referencial $S'$ puede ser apreciablemente distinto del momento $p$ en el referencial $S$. Así, los observadores en $S'$ y en $S$ obtendrán longitudes de onda de de Broglie $\lambda'$ y $\lambda$ bastante distintas. En efecto,

$$\lambda' = \frac{h}{p'} = \frac{h}{p - mv} \neq \lambda, \qquad \text{(1.7)}$$

¡Esto es muy extraño! Como repasamos ahora, para las ondas ordinarias que se propagan en el referencial de reposo de un medio (como las ondas sonoras o las ondas en el agua) los observadores galileanos encontrarán cambios de frecuencia pero ningún cambio en la longitud de onda. Esto es intuitivamente claro: para hallar la longitud de onda basta con tomar una fotografía de la onda en un instante dado, y ambos observadores que miren la fotografía coincidirán en el valor de la longitud de onda. Por otro lado, para medir la frecuencia, cada observador debe esperar cierto tiempo para ver pasar un período completo de la onda. Esto tomará un tiempo distinto para los distintos observadores.

Demostremos estas afirmaciones cuantitativamente. Comenzamos con la afirmación de que la fase $\varphi = kx - \omega t$ de tal onda es un invariante galileano. La onda misma puede ser $\cos\varphi$ o $\sin\varphi$ o alguna combinación, pero el hecho es que el valor físico de la onda en cualquier punto y tiempo debe ser acordado por los dos observadores. La onda es un observable. Dado que todas las características de la onda (picos, ceros, etc.) están controladas por la fase, los dos observadores deben coincidir en el valor de la fase.

En el referencial $S$ la fase se puede escribir de la siguiente manera

$$\varphi = kx - \omega t = k\left(x - \frac{\omega}{k} t\right) = \frac{2\pi}{\lambda}(x - Vt) = \frac{2\pi x}{\lambda} - \frac{2\pi V}{\lambda} t, \qquad \text{(1.8)}$$

donde $V = \omega/k$ es la velocidad de la onda. Nótese que la longitud de onda se lee del coeficiente de $x$, y que $\omega$ es menos el coeficiente de $t$. Los dos observadores deben coincidir en el valor de $\varphi$. Es decir, debemos tener

$$\varphi'(x', t') = \varphi(x, t) \qquad \text{(1.9)}$$

donde las coordenadas y tiempos están relacionados por una transformación de Galileo. Por lo tanto

$$\varphi'(x', t') = \frac{2\pi}{\lambda}(x - Vt) = \frac{2\pi}{\lambda}(x' + vt' - Vt') = \frac{2\pi}{\lambda} x' - \frac{2\pi(V - v)}{\lambda} t' . \qquad \text{(1.10)}$$

Dado que el lado derecho está expresado en términos de las variables primadas, podemos leer $\lambda'$ del coeficiente de $x'$ y $\omega'$ como menos el coeficiente de $t'$:

$$\lambda' = \lambda \qquad \text{(1.11)}$$

$$\omega' = \frac{2\pi}{\lambda}(V - v) = \frac{2\pi V}{\lambda}\left(1 - \frac{v}{V}\right) = \omega\left(1 - \frac{v}{V}\right) . \qquad \text{(1.12)}$$

Esto confirma que, como afirmamos, para una onda física que se propaga en un medio, la longitud de onda es un invariante galileano y la frecuencia se transforma.

¿Qué significa entonces que la longitud de onda de las ondas de materia cambie bajo una transformación de Galileo? Significa que las ondas $\Psi$ ¡no son directamente medibles! Su valor no corresponde a una magnitud medible sobre la cual todos los observadores galileanos deban coincidir. Así, la función de onda no necesita ser invariante bajo transformaciones de Galileo:

$$\Psi(x, t) \neq \Psi'(x', t') , \qquad \text{(1.13)}$$

donde $(x, t)$ y $(x', t')$ están relacionados por transformaciones de Galileo y por lo tanto representan el mismo punto y el mismo instante. Ustedes averiguarán en la tarea la relación correcta entre $\Psi(x, t)$ y $\Psi'(x', t')$.

¿Cuál es la frecuencia $\omega$ de la onda de de Broglie para una partícula con momento $p$? Teníamos

$$p = \hbar k \qquad \text{(1.14)}$$

lo cual fija la longitud de onda en términos del momento. La frecuencia $\omega$ de la onda está determinada por la relación

$$E = \hbar \omega , \qquad \text{(1.15)}$$

que también fue postulada por de Broglie y fija $\omega$ en términos de la energía $E$ de la partícula. Nótese que, para nuestro enfoque en partículas no relativistas, la energía $E$ está determinada por el momento a través de la relación

$$E = \frac{p^2}{2m} . \qquad \text{(1.16)}$$

Podemos dar tres evidencias de que (1.15) es una relación razonable.

1.  Si superponemos ondas de materia para formar un paquete de ondas que representa a la partícula, el paquete se moverá con la llamada velocidad de grupo $v_g$, que de hecho coincide con la velocidad de la partícula. La velocidad de grupo se obtiene derivando $\omega$ respecto de $k$, como repasaremos en breve:

$$v_g = \frac{d\omega}{dk} = \frac{dE}{dp} = \frac{d}{dp}\left(\frac{p^2}{2m}\right) = \frac{p}{m} = v . \qquad \text{(1.17)}$$

1.  La relación también está sugerida por la relatividad especial. La energía y las componentes del momento de una partícula forman un cuadrivector:

$$\left(\frac{E}{c}, \vec p\right) \qquad \text{(1.18)}$$

De manera similar, para ondas cuyas fases son invariantes relativistas tenemos otro cuadrivector

$$\left(\frac{\omega}{c}, \vec k\right) \qquad \text{(1.19)}$$

Igualar dos cuadrivectores es una elección consistente: sería válida en todos los referenciales de Lorentz. Como se puede ver, ambas relaciones de de Broglie se siguen de

$$\left(\frac{E}{c}, \vec p\right) = \hbar\left(\frac{\omega}{c}, \vec k\right) . \qquad \text{(1.20)}$$

1.  Para los fotones, (1.15) es consistente con los cuantos de energía de Einstein, ya que $E = h\nu = \hbar\omega$.

En resumen, tenemos

$$p = \hbar k, \qquad E = \hbar \omega . \qquad \text{(1.21)}$$

Estas se llaman las relaciones de de Broglie, y son válidas para todas las partículas.

## 2. Velocidades de fase y de grupo

Para entender la velocidad de grupo formamos paquetes de onda e investigamos con qué rapidez se mueven. Para esto simplemente supondremos que $\omega(k)$ es alguna función arbitraria de $k$. Consideremos una superposición de ondas planas $e^{i(kx-\omega(k)t)}$ dada por

$$\psi(x, t) = \int dk\, \Phi(k) e^{i(kx-\omega(k)t)} . \qquad \text{(2.22)}$$

Suponemos que la función $\Phi(k)$ tiene un pico alrededor de cierto número de onda $k = k_0$, como se muestra en la Fig. 2.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes4_ES/fig2.png)

Figura 2: Se supone que la función $\Phi(k)$ tiene un pico alrededor de $k = k_0$.

Para motivar la siguiente discusión, consideremos el caso en que $\Phi(k)$ no solo tiene un pico alrededor de $k_0$, sino que además es real (dejaremos caer esta suposición más adelante). En este caso, la fase $\phi$ del integrando proviene únicamente de la exponencial:

$$\phi(k) = kx - \omega(k) t . \qquad \text{(2.23)}$$

Deseamos entender para qué valores de $x$ y $t$ el paquete $\psi(x,t)$ toma valores grandes. Usamos el principio de fase estacionaria: dado que solo para $k \sim k_0$ la integral sobre $k$ tiene posibilidad de dar una contribución no nula, el factor de fase debe ser estacionario en $k = k_0$. La idea es simple: si una función se multiplica por una fase que varía rápidamente, la integral se cancela en promedio. Por lo tanto, la fase debe tener derivada nula en $k_0$. Aplicando esta idea a nuestra fase, hallamos la derivada y la igualamos a cero en $k_0$:

$$\left.\frac{d\phi}{dk}\right|_{k_0} = x - \left.\frac{d\omega}{dk}\right|_{k_0} t = 0 . \qquad \text{(2.24)}$$

Esto significa que $\psi(x,t)$ es apreciable cuando $x$ y $t$ están relacionados por

$$x = \left.\frac{d\omega}{dk}\right|_{k_0} t , \qquad \text{(2.25)}$$

lo cual muestra que el paquete se mueve con velocidad de grupo

$$v_g = \left.\frac{d\omega}{dk}\right|_{k_0} . \qquad \text{(2.26)}$$

**Ejercicio.** Si $\Phi(k_0)$ no es real, escriba $\Phi(k) = |\Phi(k)| e^{i\phi(k)}$. Encuentre la nueva versión de (2.25) y muestre que la velocidad de la onda no cambia.

Hagamos ahora un cálculo más detallado que confirme el análisis anterior y aporte cierta comprensión adicional. Notemos primero que

$$\psi(x, 0) = \int dk\, \Phi(k) e^{ikx} . \qquad \text{(2.27)}$$

Expandimos $\omega(k)$ en una serie de Taylor alrededor de $k = k_0$

$$\omega(k) = \omega(k_0) + (k - k_0) \left.\frac{d\omega}{dk}\right|_{k_0} + O\!\left((k-k_0)^2\right) . \qquad \text{(2.28)}$$

Entonces encontramos, despreciando los términos $O((k-k_0)^2)$

$$\psi(x, t) = \int dk\, \Phi(k)\, e^{ikx}\, e^{-i\omega(k_0)t}\, e^{-i(k-k_0)\left.\frac{d\omega}{dk}\right|_{k_0} t} . \qquad \text{(2.29)}$$

Conviene sacar de la integral todos los factores que no dependen de $k$:

$$\psi(x, t) = e^{-i\omega(k_0)t + ik_0 \left.\frac{d\omega}{dk}\right|_{k_0} t} \int dk\, \Phi(k)\, e^{ikx}\, e^{-ik \left.\frac{d\omega}{dk}\right|_{k_0} t}$$

$$= e^{-i\omega(k_0)t + ik_0 \left.\frac{d\omega}{dk}\right|_{k_0} t} \int dk\, \Phi(k)\, e^{ik\left(x - \left.\frac{d\omega}{dk}\right|_{k_0} t\right)} . \qquad \text{(2.30)}$$

Comparando con (2.27) nos damos cuenta de que la integral en la expresión anterior puede escribirse en términos de la función de onda en el instante cero:

$$\psi(x, t) = e^{-i\omega(k_0)t + ik_0 \left.\frac{d\omega}{dk}\right|_{k_0} t}\; \psi\!\left(x - \left.\frac{d\omega}{dk}\right|_{k_0} t\right) . \qquad \text{(2.31)}$$

Los factores de fase que preceden a la expresión no son importantes para rastrear dónde está el paquete de ondas. En particular, podemos tomar la norma de ambos lados de la ecuación para hallar

$$|\psi(x, t)| = \left|\psi\!\left(x - \left.\frac{d\omega}{dk}\right|_{k_0} t,\; 0\right)\right| . \qquad \text{(2.32)}$$

Si $\psi(x, 0)$ tiene un pico en cierto valor $x_0$, resulta claro de la ecuación anterior que $|\psi(x, t)|$ tiene un pico en

$$x - \left.\frac{d\omega}{dk}\right|_{k_0} t = x_0 \quad \longrightarrow \quad x = x_0 + \left.\frac{d\omega}{dk}\right|_{k_0} t , \qquad \text{(2.33)}$$

lo cual muestra que el pico del paquete se mueve con velocidad $v_{gr} = \dfrac{d\omega}{dk}$, evaluada en $k_0$.

## 3. Elección de la función de onda para una partícula libre

¿Cuál es la forma matemática de la onda asociada con una partícula con energía $E$ y momento $p$? Sabemos que $\omega$ y $k$ están determinados a partir de $E = \hbar\omega$ y $p = \hbar k$. Supongamos que queremos que nuestra onda se propague en la dirección $+\hat x$. Todas las siguientes son ejemplos de ondas que podrían ser candidatas para la función de onda de la partícula.

1.  $\sin(kx - \omega t)$

2.  $\cos(kx - \omega t)$

3.  $e^{i(kx-\omega t)} = e^{ikx} e^{-i\omega t}$ — dependencia temporal $\propto e^{-i\omega t}$

4.  $e^{-i(kx-\omega t)} = e^{-ikx} e^{i\omega t}$ — dependencia temporal $\propto e^{+i\omega t}$

En la tercera y cuarta opciones hemos indicado que la dependencia temporal podría venir con cualquiera de los dos signos. ¡Usaremos la superposición para decidir cuál es la correcta! Estamos buscando una función de onda que sea no nula para todos los valores de $x$.

Tomémoslas una por una:

1.  Partiendo de (1), construimos una superposición en la cual la partícula tiene igual probabilidad de encontrarse moviéndose en las direcciones $+x$ y $-x$.

$$\Psi(x, t) = \sin(kx - \omega t) + \sin(kx + \omega t) \qquad \text{(3.1)}$$

Expandiendo las funciones trigonométricas, esto se puede simplificar a

$$\Psi(x, t) = 2\sin(kx)\cos(\omega t) . \qquad \text{(3.2)}$$

Pero este resultado no es razonable. La función de onda se anula idénticamente para todo $x$ en ciertos instantes especiales

$$\omega t = \frac{\pi}{2}, \frac{3\pi}{2}, \frac{5\pi}{2}, \dots \qquad \text{(3.3)}$$

Una función de onda que es cero no puede representar a una partícula.

1.  Construyendo una función de onda a partir de (2) con una superposición de ondas coseno que van hacia la izquierda y hacia la derecha,

$$\Psi(x, t) = \cos(kx - \omega t) + \cos(kx + \omega t) = 2\cos(kx)\cos(\omega t) . \qquad \text{(3.4)}$$

Esta elección no sirve, también se anula idénticamente cuando $\omega t = \dfrac{\pi}{2}, \dfrac{3\pi}{2}, \dots$

1.  Probemos una superposición similar de exponenciales a partir de (3), con ambas teniendo la misma dependencia temporal

$$\Psi(x, t) = e^{i(kx-\omega t)} + e^{i(-kx-\omega t)} \qquad \text{(3.5)}$$

$$= (e^{ikx} + e^{-ikx})\, e^{-i\omega t} \qquad \text{(3.6)}$$

$$= 2\cos(kx)\, e^{-i\omega t} . \qquad \text{(3.7)}$$

¡Esta función de onda cumple con nuestro criterio! Nunca es cero para todos los valores de $x$ porque $e^{-i\omega t}$ nunca es cero.

1.  Una superposición de exponenciales a partir de (4) también cumple con nuestro criterio

$$\Psi(x, t) = e^{-i(kx-\omega t)} + e^{-i(-kx-\omega t)} \qquad \text{(3.8)}$$

$$= (e^{ikx} + e^{-ikx})\, e^{i\omega t} \qquad \text{(3.9)}$$

$$= 2\cos(kx)\, e^{i\omega t} . \qquad \text{(3.10)}$$

Esto nunca es cero para todos los valores de $x$.

Dado que tanto la opción (3) como la (4) parecen funcionar, nos preguntamos: ¿podemos usar tanto (3) como (4) para representar a una partícula que se mueve hacia la derecha (en la dirección $+\hat x$)? Supongamos que sí podemos. Entonces, dado que sumar un estado a sí mismo no debería cambiar el estado, podríamos representar a la partícula que se mueve hacia la derecha usando la suma de (3) y (4)

$$\Psi(x, t) = e^{i(kx-\omega t)} + e^{-i(kx-\omega t)} = 2\cos(kx - \omega t) . \qquad \text{(3.11)}$$

Esto, sin embargo, es lo mismo que (2), lo cual ya mostramos que lleva a dificultades. Por lo tanto debemos elegir entre (3) y (4).

La elección es una cuestión de convención, y todos los físicos usan la misma convención. Tomamos la función de onda de la partícula libre como

$$\text{Función de onda de la partícula libre:} \qquad \Psi(x, t) = e^{i(kx-\omega t)} , \qquad \text{(3.12)}$$

que representa a una partícula con

$$p = \hbar k , \qquad \text{y} \qquad E = \hbar \omega . \qquad \text{(3.13)}$$

En tres dimensiones, la función de onda correspondiente sería

$$\text{Función de onda de la partícula libre:} \qquad \Psi(x, t) = e^{i(\vec k \cdot \vec x-\omega t)} , \qquad \text{(3.14)}$$

que representa a una partícula con

$$p = \hbar k, \qquad \text{y} \qquad E = \hbar \omega . \qquad \text{(3.15)}$$

Andrew Turner y Sarah Geller transcribieron las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.

------------------------------------------------------------------------

MIT OpenCourseWare https://ocw.mit.edu

8.04 Física Cuántica I Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.


---

<!-- MIT8.04_LecNotes5_ES.md -->

# Lección 5

## Vídeos de esta clase (YouTube)

**Lección 5: Momentum operator, Schrödinger equation, and interpretation of the wavefunction.**

- [Momentum operator, energy operator, and a differential equation](https://www.youtube.com/watch?v=ELBh60GU5yE)
- [Free Schrödinger equation](https://www.youtube.com/watch?v=7euh_iwzSGo)
- [The general Schrödinger equation. x, p commutator](https://www.youtube.com/watch?v=rwzg8iEOc8s)
- [Commutators, matrices, and 3-dimensional Schrödinger equation](https://www.youtube.com/watch?v=m7UT2Hr465o)
- [Interpretation of the wavefunction](https://www.youtube.com/watch?v=R-5hjmV-bdY)

------------------------------------------------------------------------

*B. Zwiebach*

*21 de febrero de 2016*

## Contenido

1.  Ecuaciones para una función de onda
2.  Ecuación de Schrödinger para una partícula en un potencial
3.  Interpretación de la función de onda

## 1. Ecuaciones para una función de onda

Determinamos que la función de onda o onda de de Broglie para una partícula con momento $p$ y energía $E$ está dada por

$$\Psi(x, t) = e^{i(kx-\omega t)} , \qquad \text{(1.1)}$$

donde $\omega$ y $k$ están determinados a partir de

$$p = \hbar k, \quad E = \hbar \omega , \quad E = \frac{p^2}{2m} \qquad \text{(1.2)}$$

La función de onda (1.1) representa un estado de momento definido. Resulta entonces interesante encontrar un operador que extraiga esa información de la función de onda. El operador debe ser, en términos generales, una derivada con respecto a $x$, ya que esto haría bajar un factor de $k$. De hecho, de forma más precisa, tomamos

$$\frac{\hbar}{i} \frac{\partial}{\partial x} \Psi(x, t) = \frac{\hbar}{i} (ik)\Psi(x, t)$$

$$= \hbar k \Psi(x, t) \qquad \text{(1.3)}$$

$$= p \Psi(x, t)$$

donde el factor $p$ en el último miembro derecho es justamente el momento. Identificamos así el operador $\frac{\hbar}{i}\frac{\partial}{\partial x}$ como el operador momento $\hat{p}$

$$\hat{p} \equiv \frac{\hbar}{i} \frac{\partial}{\partial x} . \qquad \text{(1.4)}$$

y hemos verificado que, al actuar sobre la función de onda $\Psi(x, t)$ de una partícula de momento $p$, da $p$ veces la función de onda:

$$\hat{p} \, \Psi = p \, \Psi . \qquad \text{(1.5)}$$

El operador momento actúa sobre funciones de onda, que son funciones del espacio y el tiempo, para dar otra función de $x$ y $t$. Puesto que $\hat{p}$ actuando sobre $\Psi$ da un número ($p$, de hecho) multiplicado por $\Psi$, decimos que $\Psi$ es un autoestado (o estado propio) de $\hat{p}$. La analogía con el álgebra de matrices es útil: las matrices son los operadores y los vectores columna son los estados. Las matrices actúan por multiplicación sobre vectores columna. Un autovector de una matriz es un vector especial. La matriz, al actuar sobre un autovector, da un número multiplicado por el autovector. Tras la acción de la matriz, la dirección del vector no cambia, pero su magnitud puede escalarse. Lo mismo ocurre con los autoestados de operadores: un operador actuando sobre un autoestado da el autoestado multiplicado por una constante. También decimos que $\Psi$ es un estado de momento definido.

Consideremos ahora la extracción de la información de energía a partir de la función de onda de la partícula libre. Esta vez debemos recurrir a la derivada temporal:

$$i\hbar \, \frac{\partial}{\partial t} \Psi(x, t) = i\hbar(-i\omega)\Psi(x, t) = \hbar \omega \, \Psi(x, t) = E \, \Psi(x, t) . \qquad \text{(1.6)}$$

Sería razonable decir que la derivada temporal $i\hbar \frac{\partial}{\partial t}$ es un operador de energía, pero, para una partícula libre, la energía está dada en términos del momento, de modo que podemos construir el operador de energía relevante trabajando sobre el miembro derecho anterior

$$E\Psi = \frac{p^2}{2m} \Psi = \frac{p}{2m} p \Psi = \frac{p}{2m} \frac{\hbar}{i}\frac{\partial}{\partial x} \Psi , \qquad \text{(1.7)}$$

donde usamos la ecuación (1.5) para escribir $p\Psi$ como el operador momento actuando sobre $\Psi$. Como $p$ es una constante, podemos mover el factor $p$ en el último miembro derecho cerca de la función de onda y luego reemplazarlo por el operador momento:

$$E\Psi = \frac{1}{2m} \frac{\hbar}{i}\frac{\partial}{\partial x} \, p\Psi = \frac{1}{2m} \frac{\hbar}{i}\frac{\partial}{\partial x} \frac{\hbar}{i}\frac{\partial}{\partial x} \Psi . \qquad \text{(1.8)}$$

Esto puede escribirse como

$$E\Psi = \frac{1}{2m} \hat{p}\,\hat{p}\, \Psi = \frac{\hat{p}^2}{2m} \Psi , \qquad \text{(1.9)}$$

lo cual sugiere la siguiente definición del operador de energía $\hat{E}$:

$$\hat{E} \equiv \frac{\hat{p}^2}{2m} = -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} . \qquad \text{(1.10)}$$

En efecto, para nuestra función de onda de partícula libre, (1.9) muestra que $E\Psi = \hat{E}\Psi$.

Nuestro trabajo también nos permite hallar una ecuación diferencial para la cual nuestra función de onda de de Broglie es solución. Consideremos (1.6) y reemplacemos el miembro derecho $E\Psi$ por $\hat{E}\Psi$, lo que nos da

$$i\hbar \, \frac{\partial}{\partial t} \Psi(x, t) = -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} \Psi(x, t) . \qquad \text{(1.11)}$$

Esta es la ecuación de Schrödinger para la partícula libre. De forma más esquemática, usando el operador de energía, puede escribirse como

$$i\hbar \, \frac{\partial}{\partial t} \Psi(x, t) = \hat{E} \, \Psi(x, t) . \qquad \text{(1.12)}$$

Vale la pena volver a comprobar que nuestra función de onda de de Broglie satisface la ecuación de Schrödinger (1.11). En efecto, para $\Psi = e^{i(kx-\omega t)}$ encontramos

$$i\hbar(-i\omega)\Psi = -\frac{\hbar^2}{2m}(ik)^2 \Psi \qquad \text{(1.13)}$$

lo cual es una solución, ya que los factores $\Psi$ se cancelan y todo lo que se necesita es la igualdad

$$\hbar \omega = \frac{\hbar^2 k^2}{2m} , \qquad \text{(1.14)}$$

que se reconoce como la familiar relación $E = \frac{p^2}{2m}$.

Nótese que la ecuación de Schrödinger admite soluciones más generales que la función de onda de de Broglie para una partícula de momento y energía definidos. Puesto que la ecuación es lineal, cualquier superposición de soluciones de ondas planas con distintos valores de $k$ es también una solución. Tomemos por ejemplo

$$\Psi(x, t) = e^{i(k_1 x - \omega_1 t)} + e^{i(k_2 x - \omega_2 t)} \qquad \text{(1.15)}$$

Esta es una solución, y nótese que, aunque cada sumando corresponde a un estado de momento definido, la solución total no es un estado de momento definido. En efecto

$$\hat{p} \, \Psi(x, t) = \hbar k_1 \, e^{i(k_1 x - \omega_1 t)} + \hbar k_2 \, e^{i(k_2 x - \omega_2 t)} , \qquad \text{(1.16)}$$

y el miembro derecho no puede escribirse como un número multiplicado por $\Psi$. El estado completo tampoco es un estado de energía definida. La solución general de la ecuación de Schrödinger libre es la superposición más general de ondas planas:

$$\Psi(x, t) = \int_{-\infty}^{\infty} dk \, \Phi(k) \, e^{i(kx - \omega(k)t)} , \qquad \text{(1.17)}$$

donde $\Phi(k)$ es una función arbitraria de $k$ que controla la superposición, y hemos escrito $\omega(k)$ para enfatizar que $\omega$ es una función del momento, como en (1.14).

**Ejercicio.** Verifique que $\Psi$ en (1.17) resuelve la ecuación de Schrödinger libre.

Ahora tenemos las herramientas para evolucionar en el tiempo cualquier función de onda inicial. Es decir, dada la función de onda inicial $\Psi(x, 0)$ de cualquier paquete en el instante cero, podemos obtener $\Psi(x, t)$. En efecto, mediante la transformación de Fourier, podemos escribir

$$\Psi(x, 0) = \int dk \, \Phi(k) \, e^{ikx} , \qquad \text{(1.18)}$$

donde $\Phi(k)$ es la transformada de Fourier de $\Psi(x, 0)$. Pero entonces, la evolución temporal consiste simplemente en añadir la exponencial $e^{-i\omega(k)t}$ a la integral, de modo que la respuesta para la evolución temporal está dada efectivamente por (1.17).

Como hemos discutido antes, la velocidad de un paquete de ondas descrito por (1.17) está dada por la velocidad de grupo evaluada para el valor dominante de $k$. Confirmamos que esto es efectivamente razonable

$$v_g \equiv \frac{\partial \omega}{\partial k} = \frac{\partial \hbar \omega}{\partial \hbar k} = \frac{\partial E}{\partial p} = \frac{\partial}{\partial p}\left(\frac{p^2}{2m}\right) = \frac{p}{m} , \qquad \text{(1.19)}$$

que es la velocidad esperada para una partícula libre no relativista con momento $p$ y masa $m$.

La ecuación de Schrödinger tiene una $i$ explícita en el miembro izquierdo. Esta $i$ muestra que es imposible encontrar una solución para $\Psi$ real. Si $\Psi$ fuera real, el miembro derecho de la ecuación sería real, pero el miembro izquierdo sería imaginario. Por lo tanto, la ecuación de Schrödinger nos obliga a trabajar con funciones de onda complejas.

Nótese también que la ecuación de Schrödinger no tiene la forma de una ecuación de onda convencional. Una ecuación de onda convencional para una variable $\phi$ toma la forma

$$\frac{\partial^2 \phi}{\partial x^2} - \frac{1}{V^2} \frac{\partial^2 \phi}{\partial t^2} = 0 . \qquad \text{(1.20)}$$

Las soluciones generales de esta ecuación lineal son $f_{\pm}(x \pm Vt)$. Esto sí permitiría soluciones reales, las cuales no son aceptables en la teoría cuántica. La ecuación de Schrödinger no tiene derivadas temporales de segundo orden. ¡Es de primer orden en el tiempo!

## 2. Ecuación de Schrödinger para una partícula en un potencial

Supongamos ahora que nuestra partícula cuántica no es libre, sino que se mueve en algún potencial externo $V(x, t)$. En este caso, la energía total de la partícula ya no es simplemente cinética, sino la suma de las energías cinética y potencial:

$$E = \frac{p^2}{2m} + V(x, t) , \qquad \text{(2.1)}$$

Esto sugiere naturalmente que el operador de energía debería tomar la forma

$$\hat{E} = \frac{\hat{p}^2}{2m} + V(x, t) . \qquad \text{(2.2)}$$

El primer término, como ya sabemos, involucra segundas derivadas con respecto a $x$. El segundo término actúa multiplicativamente: al actuar sobre cualquier función de onda $\Psi(x, t)$, simplemente la multiplica por $V(x, t)$. Postulamos ahora que la ecuación de Schrödinger para una partícula en un potencial toma la forma (1.12) con $\hat{E}$ reemplazado por el operador de energía anterior:

$$i\hbar \, \frac{\partial}{\partial t} \Psi(x, t) = \left[ -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} + V(x, t) \right] \Psi(x, t) . \qquad \text{(2.3)}$$

El operador de energía $\hat{E}$ se llama habitualmente operador hamiltoniano $\hat{H}$, de modo que se tiene

$$\hat{H} \equiv -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} + V(x, t) , \qquad \text{(2.4)}$$

y la ecuación de Schrödinger toma la forma

$$i\hbar \, \frac{\partial}{\partial t} \Psi(x, t) = \hat{H} \, \Psi(x, t) . \qquad \text{(2.5)}$$

Reconsideremos la forma en que el potencial $V(x, t)$ es un operador. Podemos hacerlo introduciendo un operador posición $\hat{x}$ que, al actuar sobre funciones de $x$, da otra función de $x$ de la siguiente manera:

$$\hat{x} f(x) \equiv x f(x) . \qquad \text{(2.6)}$$

Nótese que de esta ecuación y de aplicaciones sucesivas de la misma se sigue que

$$\hat{x}^k f(x) \equiv x^k f(x) . \qquad \text{(2.7)}$$

Si el potencial $V(x, t)$ puede escribirse como alguna expansión en serie en términos de $x$, entonces se sigue que

$$V(\hat{x}, t)\Psi(x, t) \equiv V(x, t)\Psi(x, t) . \qquad \text{(2.8)}$$

Los operadores con los que estamos tratando (momento, posición, hamiltoniano) se declaran todos operadores lineales. Un operador lineal $\hat{A}$ satisface

$$\hat{A}(a\phi) = a \, \hat{A}\phi , \qquad \hat{A}(\phi_1 + \phi_2) = \hat{A}\phi_1 + \hat{A}\phi_2 , \qquad \text{(2.9)}$$

donde $a$ es una constante. Dos operadores lineales $\hat{A}$ y $\hat{B}$ que actúan sobre el mismo conjunto de objetos siempre pueden sumarse $(\hat{A}+\hat{B})\phi \equiv \hat{A}\phi + \hat{B}\phi$. También pueden multiplicarse; el producto $\hat{A}\hat{B}$ es un operador lineal definido por $\hat{A}\hat{B}\phi \equiv \hat{A}(\hat{B}\phi)$, lo que significa que se actúa primero con $\hat{B}$, que es el más cercano a $\phi$, y luego se actúa sobre el resultado con $\hat{A}$. El orden de multiplicación importa, y por lo tanto $\hat{A}\hat{B}$ y $\hat{B}\hat{A}$ pueden no ser los mismos operadores. Para cuantificar esta posible diferencia se introduce el conmutador $[A, B]$ de dos operadores, definido como el operador lineal

$$[\, \hat{A} , \hat{B} \,] \equiv \hat{A}\hat{B} - \hat{B}\hat{A} . \qquad \text{(2.10)}$$

Si el conmutador se anula, se dice que los dos operadores conmutan. También es claro que $[\hat{A}, \hat{A}] = 0$ para cualquier operador $\hat{A}$.

Tenemos los operadores $\hat{x}$ y $\hat{p}$, que están claramente relacionados de alguna manera. Nos gustaría conocer su conmutador $[\, \hat{x}\, , \hat{p}\, ]$. Para ello dejamos que $[\, \hat{x}\, , \hat{p}\, ]$ actúe sobre alguna función arbitraria $\phi(x)$ y luego intentamos simplificar. Hagámoslo.

$$[\, \hat{x} , \hat{p} \,]\phi(x) = (\hat{x}\hat{p} - \hat{p}\hat{x})\phi(x) = \hat{x}\hat{p}\, \phi(x) - \hat{p}\hat{x}\, \phi(x)$$

$$= \hat{x}(\hat{p}\phi(x)) - \hat{p}(\hat{x}\phi(x))$$

$$= \hat{x}\left(\frac{\hbar}{i}\frac{\partial \phi(x)}{\partial x}\right) - \hat{p}(x\phi(x))$$

$$= x\,\frac{\hbar}{i}\frac{\partial \phi(x)}{\partial x} - \frac{\hbar}{i}\frac{\partial}{\partial x}(x\phi(x)) \qquad \text{(2.11)}$$

$$= x\,\frac{\hbar}{i}\frac{\partial \phi(x)}{\partial x} - x\,\frac{\hbar}{i}\frac{\partial \phi(x)}{\partial x} - \frac{\hbar}{i}\phi(x)$$

$$= -\frac{\hbar}{i}\phi(x) = i\hbar\, \phi(x) ,$$

de modo que, en definitiva, hemos mostrado que para $\phi(x)$ arbitraria se tiene

$$[\, \hat{x} , \hat{p} \,]\phi(x) = i\hbar\, \phi(x) . \qquad \text{(2.12)}$$

Puesto que esta ecuación se cumple para cualquier $\phi$, en realidad representa la igualdad de dos operadores. Siempre que tengamos $\hat{A}\phi = \hat{B}\phi$ para $\phi$ arbitraria, simplemente decimos que $\hat{A} = \hat{B}$. Los operadores son los mismos porque dan el mismo resultado al actuar sobre cualquier cosa. Hemos descubierto entonces la relación de conmutación más fundamental de la mecánica cuántica:

$$[\, \hat{x} , \hat{p} \,] = i\hbar . \qquad \text{(2.13)}$$

El miembro derecho es un número, pero debe considerarse como un operador (al actuar sobre cualquier función, la multiplica por dicho número). Esta relación de conmutación puede usarse para demostrar el principio de incertidumbre de Heisenberg, que establece que el producto de la incertidumbre en la posición y la incertidumbre en el momento debe siempre exceder $\hbar/2$.

La idea de que los operadores pueden no conmutar puede recordarnos la multiplicación de matrices, que tampoco es conmutativa. Tenemos así las siguientes correspondencias:

$$\begin{aligned}
\text{operadores} &\leftrightarrow \text{matrices} \\
\text{funciones de onda} &\leftrightarrow \text{vectores} \\
\text{autoestados} &\leftrightarrow \text{autovectores}
\end{aligned} \qquad \text{(2.14)}$$

De hecho, se puede formular la Mecánica Cuántica usando matrices, de modo que estas correspondencias son realmente concretas y funcionales.

Como ejemplo de matrices útiles que no conmutan, consideremos las matrices de Pauli, tres matrices de dos por dos dadas por

$$\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} , \quad \sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} , \quad \sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} . \qquad \text{(2.15)}$$

De hecho, estas matrices son exactamente lo que se necesita para describir partículas de espín un medio. El operador de espín $S$ tiene tres componentes $S_i = \frac{\hbar}{2}\sigma_i$. Veamos ahora si $\sigma_1$ y $\sigma_2$ conmutan.

$$\sigma_1 \sigma_2 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}$$

$$\sigma_2 \sigma_1 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix} \qquad \text{(2.16)}$$

Entonces vemos que

$$[\sigma_1, \sigma_2] = \begin{pmatrix} 2i & 0 \\ 0 & -2i \end{pmatrix} = 2i \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = 2i\sigma_3 \qquad \text{(2.17)}$$

De hecho, también se tiene $[\sigma_2, \sigma_3] = 2i\sigma_1$ y $[\sigma_3, \sigma_1] = 2i\sigma_2$.

La mecánica matricial fue desarrollada en 1925 por Werner Heisenberg y aclarada por Max Born y Pascual Jordan. Nótese que, si quisiéramos escribir los operadores $\hat{x}$ y $\hat{p}$ en forma matricial, requerirían matrices de dimensión infinita. Puede demostrarse que no existen matrices de tamaño finito que conmuten para dar un número multiplicado por la matriz identidad, como se requiere en (2.13). Esto no debería sorprendernos: en la recta real hay un número infinito de funciones de onda linealmente independientes, y en vista de las correspondencias en (2.14) esto sugeriría un número infinito de vectores de base. Las matrices relevantes deben ser, por lo tanto, de dimensión infinita.

**Dos propiedades básicas de la ecuación de Schrödinger**

1.  La ecuación diferencial es de primer orden en el tiempo. Esto significa que, para una condición inicial, basta con conocer completamente la función de onda en algún instante inicial $t_0$, y la ecuación de Schrödinger determina entonces la función de onda para todo tiempo. Esto puede entenderse de manera muy explícita. Si conocemos $\Psi(x, t_0)$ para todo $x$, entonces el miembro derecho de la ecuación de Schrödinger, que solo involucra derivadas respecto de $x$ y multiplicación, puede evaluarse en cualquier punto $x$. Esto significa que en cualquier punto $x$ conocemos la derivada temporal de la función de onda (miembro izquierdo de la ecuación de Schrödinger), y esto nos permite calcular la función de onda un poco más tarde.

2.  Linealidad y superposición. La ecuación de Schrödinger es una ecuación lineal para funciones de onda complejas. Por lo tanto, dadas dos soluciones $\Psi_1$ y $\Psi_2$, podemos formar nuevas soluciones como combinaciones lineales $\alpha\Psi_1 + \beta\Psi_2$ con coeficientes complejos $\alpha$ y $\beta$.

Hemos escrito la ecuación de Schrödinger para una partícula en un potencial unidimensional. ¿Qué ocurre en el caso de una partícula en un potencial tridimensional? Como veremos ahora, esto se logra fácilmente una vez que nos damos cuenta de que en tres dimensiones los operadores de posición y momento tienen ¡varias componentes! Recordemos que la función de onda de de Broglie

$$\Psi(\mathbf{x}, t) = e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)} = e^{i(k_x x + k_y y + k_z z - \omega t)} \qquad \text{(2.18)}$$

corresponde a una partícula que porta momento $\mathbf{p} = \hbar \mathbf{k}$, con $\mathbf{k} = (k_x, k_y, k_z)$. Tal como hicimos en (1.3), podemos intentar extraer el momento vectorial usando un operador diferencial. El operador relevante es el gradiente:

$$\nabla = \left( \frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z} \right) , \qquad \text{(2.19)}$$

con el cual intentamos

$$\frac{\hbar}{i} \nabla \Psi(\mathbf{x}, t) = \frac{\hbar}{i} \left( ik_x, ik_y, ik_z \right) \Psi(\mathbf{x}, t) = \hbar \mathbf{k} \, \Psi(\mathbf{x}, t) = \mathbf{p} \, \Psi(\mathbf{x}, t) . \qquad \text{(2.20)}$$

Definimos entonces el operador momento $\hat{\mathbf{p}}$ de la siguiente manera:

$$\hat{\mathbf{p}} = \frac{\hbar}{i} \nabla . \qquad \text{(2.21)}$$

Si llamamos a las componentes del momento $(p_1, p_2, p_3) = (p_x, p_y, p_z)$ y a las coordenadas $(x_1, x_2, x_3) = (x, y, z)$, entonces las componentes de la ecuación anterior son

$$\hat{p}_k = \frac{\hbar}{i} \frac{\partial}{\partial x_k} , \qquad k = 1, 2, 3 . \qquad \text{(2.22)}$$

Del mismo modo que definimos un operador posición $\hat{x}$, ahora tenemos tres operadores posición $(\hat{x}_1, \hat{x}_2, \hat{x}_3)$ que conforman $\hat{\mathbf{x}}$. Con tres operadores posición y tres operadores momento, debemos ahora enunciar las nueve relaciones de conmutación posibles. Si recuerdan nuestra derivación de $[\hat{x}, \hat{p}] = i\hbar$, notarán que el conmutador se anula a menos que los superíndices en $\hat{x}$ y $\hat{p}$ sean iguales. Esto significa que tenemos

$$[\, \hat{x}_i , \hat{p}_j \,] = i\hbar \, \delta_{ij} , \qquad \text{(2.23)}$$

donde la delta de Kronecker se define por

$$\delta_{ij} = \begin{cases} 1 & \text{si } i = j , \\ 0 & \text{si } i \neq j . \end{cases} \qquad \text{(2.24)}$$

Para escribir ahora la ecuación de Schrödinger general, necesitamos considerar el operador de energía cinética, o el hamiltoniano:

$$\hat{H} = \frac{\hat{p}^2}{2m} + V(\mathbf{x}, t) , \qquad \text{(2.25)}$$

En este caso

$$\hat{p}^2 = \hat{\mathbf{p}} \cdot \hat{\mathbf{p}} = \frac{\hbar}{i}\nabla \cdot \frac{\hbar}{i}\nabla = -\hbar^2 \nabla^2 \qquad \text{(2.26)}$$

donde $\nabla^2$ es el operador laplaciano

$$\nabla^2 \equiv \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2} . \qquad \text{(2.27)}$$

La ecuación de Schrödinger toma finalmente la forma

$$i\hbar \, \frac{\partial}{\partial t} \Psi(\mathbf{x}, t) = \left[ -\frac{\hbar^2}{2m} \nabla^2 + V(\mathbf{x}, t) \right] \Psi(\mathbf{x}, t) . \qquad \text{(2.28)}$$

## 3. Interpretación de la función de onda

Schrödinger pensaba que la función de onda $\Psi$ representaba una partícula que podía extenderse y desintegrarse. La fracción de la partícula que se encontraría en $x$ sería proporcional a la magnitud de $|\Psi|^2$. Esto resultaba problemático, como señaló Max Born (1882-1970). Born resolvió la ecuación de Schrödinger para la dispersión de una partícula en un potencial, hallando una función de onda que decaía como $1/r$, siendo $r$ la distancia al centro de dispersión. Pero Born también notó que en el experimento no se encuentran fracciones de partículas viajando en muchas direcciones, sino que las partículas permanecen enteras. Born propuso una interpretación probabilística. En su propuesta,

> La función de onda $\Psi(x, t)$ no nos indica cuánta cantidad de la partícula se encuentra en la posición $x$ en el instante $t$, sino más bien la probabilidad de que, al realizar una medición en el instante $t$, encontremos la partícula en la posición $x$.

Para precisar esto, usamos un elemento de volumen infinitesimal de volumen $d^3x$ centrado en algún punto arbitrario $x$. La probabilidad $dP$ de encontrar la partícula dentro del elemento de volumen $d^3x$ en el instante $t$ es

$$dP = |\Psi(x, t)|^2 \, d^3x . \qquad \text{(3.1)}$$

La consistencia exige que la probabilidad total de encontrar la partícula en algún lugar de todo el espacio sea la unidad. Por lo tanto, la integral de $dP$ sobre todo el espacio debe dar uno:

$$\int_{\text{todo el espacio}} d^3x \, |\Psi(x, t)|^2 = 1 \qquad \text{(3.2)}$$

La próxima vez exploraremos la consistencia de esta ecuación con la evolución temporal.

*Sarah Geller transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare https://ocw.mit.edu

8.04 Física Cuántica I Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

# Apéndice: Lista de problemas 2 (Problem Set 2, 2016)

*Massachusetts Institute of Technology — Departamento de Física* *8.04 Física Cuántica I, primavera de 2016* *Fecha de entrega: jueves 18 de febrero de 2016, 5:00 pm* *(Publicado el 11 de febrero de 2016)*

## Problema 1: Longitud de onda de de Broglie \[20 puntos\]

**(a)** La longitud de onda de de Broglie de un electrón no relativista (nr) con energía cinética $E_{kin}$ puede escribirse como

$$\lambda_{nr} = \frac{\delta}{\sqrt{E_{kin}}} \ \text{Å} .$$

En esta fórmula $\delta$ es una constante sin unidades, y el valor de la energía $E_{kin}$ se introduce en eV como un número puro. El resultado se obtiene en angstroms ($\text{Å} = 10^{-10}\,\text{m}$). Dé el valor de la constante adimensional $\delta$.

**(b)** La longitud de onda de de Broglie de un electrón relativista (r) con energía $E$ puede calcularse en términos del factor $\gamma$ del electrón: $E = \gamma m_e c^2$. Se obtiene

$$\lambda_r = \frac{\ell}{\sqrt{\gamma^2 - 1}} .$$

¿Cuál es el valor de $\ell$ en fm $= 10^{-15}\,\text{m}$? ¿Es esta una longitud bien conocida?

**(c)** Reescriba la expresión para $\lambda_{nr}$ del apartado (a) en términos de $\ell$ y $\gamma$, usando $E_{kin} = (\gamma - 1) m_e c^2$. Demuestre que $\lambda_r < \lambda_{nr}$ para cualquier valor de la energía.

**(d)** Algunos cálculos numéricos:

    **i.** ¿Cuál es la energía de un electrón cuya longitud de onda de de Broglie es igual a su longitud de onda Compton? ¿Es ese electrón relativista? ¿Se mueve más rápido que $0.2\,c$?

    **ii.** La longitud de onda de de Broglie de una partícula da una idea aproximada de la escala de distancias que puede explorar en un experimento de colisión. El International Linear Collider, que podría construirse en un futuro próximo, está pensado para acelerar electrones hasta $1\,\text{TeV} = 1000\,\text{GeV}$. ¿Cuál es la longitud de onda de de Broglie de tales electrones? Compárela con la longitud de onda de de Broglie de protones de $7\,\text{TeV}$ en el LHC de Ginebra.

    **iii.** ¿Cuál es la energía cinética máxima del electrón, y el correspondiente $\beta = v/c$, para la cual el valor no relativista de $\lambda$ (en (a) o en (c)) tiene un error menor o igual al 10 %?

## Problema 2: Radio de Bohr, longitud de onda Compton del electrón y radio clásico del electrón \[10 puntos\]

El radio clásico del electrón $r_0$ es el radio que se obtiene al igualar (salvo factores constantes) la energía electrostática asociada a una bola cargada de radio $r_0$ con la energía en reposo del electrón

$$\frac{e^2}{r_0} = m_e c^2 \quad \longrightarrow \quad r_0 = \frac{e^2}{m_e c^2} .$$

Aquí $e$ es la carga del electrón. La longitud de onda Compton reducida $\bar{\lambda}_C$ del electrón es

$$\bar{\lambda}_C = \frac{\hbar}{m_e c} .$$

Finalmente, la constante de estructura fina $\alpha$, que mide la intensidad del acoplamiento electromagnético, es

$$\alpha = \frac{e^2}{\hbar c} \simeq \frac{1}{137} .$$

**(a)** El radio de Bohr $a_0$ es la escala de longitud que puede construirse a partir de $e^2$, $\hbar$ y $m_e$ sin constantes numéricas adicionales. Encuentre la fórmula del radio de Bohr mediante un análisis dimensional. Evalúe esta longitud en fm.

**(b)** Muestre que las tres longitudes forman una progresión geométrica de razón $\alpha$:

$$a_0 : \bar{\lambda}_C : r_0 = 1 : \alpha : \alpha^2 .$$

Use esto para dar los valores de $\bar{\lambda}_C$ y $r_0$ en fm.

## Problema 3: Matrices de dos por dos y dispositivos lineales \[10 puntos\]

Considere el interferómetro de Mach-Zehnder de dos haces y un haz representado por el vector columna de dos componentes $u$:

$$u = \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} , \qquad \text{con } |u_1|^2 + |u_2|^2 = 1 .$$

Cualquier elemento óptico lineal del interferómetro puede representarse mediante una matriz de dos por dos $R$ tal que, para un haz de entrada $u$, el haz de salida $u'$ está dado por

$$u' = R\, u .$$

Demuestre que la conservación de la probabilidad para $u$ arbitrario exige que $R$ sea una matriz unitaria. Se dice que una matriz $R$ (de tamaño finito) es unitaria si $R^{\dagger} R = 1$, donde la daga denota la operación de transposición y conjugación compleja.

## Problema 4: Mejorando la detección de bombas \[15 puntos\]

Modificamos el interferómetro de Mach-Zehnder para aumentar el porcentaje de bombas de Elitzur-Vaidman que pueden certificarse como funcionales sin detonarlas. Para ello construimos un divisor de haz con reflectividad $R$ y transmisividad $T$. Un fotón incidente (desde cualquiera de los dos puertos) tiene una probabilidad $R$ de ser reflejado y una probabilidad $T$ de ser transmitido ($R + T = 1$). Sean $r$ y $t$ las raíces cuadradas positivas:

$$r \equiv \sqrt{R} , \qquad t \equiv \sqrt{T} .$$

**(a)** Construya la matriz de dos por dos $U$ que representa el divisor de haz. Para ello, considere lo que ocurre cuando un fotón incide sobre el divisor de haz desde el lado superior (entrada $\begin{pmatrix}1\\0\end{pmatrix}$) y cuando incide desde el lado inferior (entrada $\begin{pmatrix}0\\1\end{pmatrix}$). Para fijar convenciones, $U$ tendrá todos sus elementos positivos (y reales) excepto el elemento inferior derecho (el elemento 2,2). Confirme que $U$ es unitaria.

*(El interferómetro, con los detectores $D_0$ y $D_1$, utiliza dos copias idénticas del divisor de haz. El fotón incidente llega por el lado superior.)*

**(b)** Se inserta una bomba defectuosa en la rama inferior del interferómetro. ¿Cuáles son las probabilidades de detección $P_0$ y $P_1$ en $D_0$ y $D_1$ respectivamente? Se inserta ahora una bomba en funcionamiento en la rama inferior del interferómetro. ¿Cuál es la probabilidad de detonación $P_{boom}$ y las probabilidades de detección $P_0$ y $P_1$? Exprese sus respuestas en términos de $R$ y $T$.

**(c)** Se prueban bombas hasta estar razonablemente seguros de que fallan o de que son funcionales. ¿Qué fracción $f$ de las bombas funcionales puede certificarse como buenas sin detonarlas? Dé su respuesta en términos de $R$. ¿Cuál es el valor máximo posible de $f$?

## Problema 5: Ondas planas para partículas materiales \[10 puntos\]

Suponga que queremos representar la onda de una partícula material que se mueve en la dirección $x$ con momento $p = \hbar k$. Una propuesta razonable para dicha onda es

$$\Psi(x, t) = \cos(kx - \omega t) + \gamma \sin(kx - \omega t) ,$$

donde $\gamma$ es una constante. Un requisito físico es que un desplazamiento arbitrario de $x$ o un desplazamiento arbitrario de $t$ no debe alterar el carácter de la onda. Exigiremos por tanto que, tras el desplazamiento, cuyo efecto es cambiar la fase en una constante $\epsilon$, se tenga

$$\cos(kx - \omega t + \epsilon) + \gamma \sin(kx - \omega t + \epsilon) = a \big[ \cos(kx - \omega t) + \gamma \sin(kx - \omega t) \big]$$

para alguna constante $a$ que puede depender de $\epsilon$.

Escriba las ecuaciones que se derivan del requisito anterior. Encuentre las dos soluciones posibles para $\gamma$ y el valor de $a$ asociado a cada una. ¿Cuál es la solución que corresponde a nuestra descripción convencional de una onda material?

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*


---

<!-- MIT8.04_LecNotes6_ES.md -->

# Lección 6

## Vídeos de esta clase (YouTube)

**Lección 6: Probability density and current. Hermitian conjugation.**

- [Normalizable wavefunctions and the question of time evolution](https://www.youtube.com/watch?v=d4skxu7MpFI)
- [Is probability conserved? Hermiticity of the Hamiltonian](https://www.youtube.com/watch?v=5L4QfjbK87M)
- [Probability current and current conservation](https://www.youtube.com/watch?v=J2ltXyByPJA)
- [Three dimensional current and conservation](https://www.youtube.com/watch?v=Ex_fFlwZoM0)

------------------------------------------------------------------------

B. Zwiebach

23 de febrero de 2016

## Contenido

1.  Normalización y evolución temporal
2.  La función de onda como amplitud de probabilidad
3.  La corriente de probabilidad
4.  Corriente de probabilidad en 3D y conservación de la corriente

## 1. Normalización y evolución temporal

La función de onda $\Psi(x, t)$ que describe la mecánica cuántica de una partícula de masa $m$ moviéndose en un potencial $V(x, t)$ satisface la ecuación de Schrödinger

$$i\hbar \frac{\partial \Psi(x, t)}{\partial t} = \left( -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} + V(x, t) \right) \Psi(x, t) , \qquad \text{(1.1)}$$

o, más brevemente,

$$i\hbar \frac{\partial \Psi(x, t)}{\partial t} = \hat{H} \Psi(x, t) . \qquad \text{(1.2)}$$

La interpretación de la función de onda surge al declarar que $dP$, definido por

$$dP = |\Psi(x, t)|^2 \, dx , \qquad \text{(1.3)}$$

es la probabilidad de encontrar la partícula en el intervalo $dx$ centrado en $x$ en el instante $t$. De ahí se sigue que las probabilidades de encontrar la partícula en todos los puntos posibles deben sumar uno:

$$\int_{-\infty}^{\infty} \Psi^*(x, t) \, \Psi(x, t) \, dx = 1 . \qquad \text{(1.4)}$$

Intentaremos entender cómo esta ecuación es compatible con la evolución temporal prescrita por la ecuación de Schrödinger. Pero antes de eso, examinemos qué tipo de condiciones se requieren de las funciones de onda para satisfacer (1.4).

Supongamos que la función de onda tiene límites bien definidos cuando $x \to \pm\infty$. Si esos límites son distintos de cero, la integral en el entorno del infinito produciría un resultado infinito, lo cual es incompatible con la afirmación de que la integral total vale uno. Por lo tanto, los límites deben ser cero:

$$\lim_{x \to \pm\infty} \Psi(x, t) = 0 . \qquad \text{(1.5)}$$

En principio es posible tener una función de onda que no tenga un límite bien definido en el infinito pero que aun así sea de cuadrado integrable. Pero tales casos no parecen aparecer en la práctica, así que supondremos que (1.5) se cumple. También sería natural suponer que la derivada espacial de $\Psi$ se anula cuando $x \to \pm\infty$ pero, como veremos en breve, basta con suponer que el límite de la derivada espacial de $\Psi$ está acotado

$$\lim_{x \to \pm\infty} \frac{\partial \Psi(x, t)}{\partial x} < \infty . \qquad \text{(1.6)}$$

Hemos enfatizado antes que el factor numérico global que multiplica a la función de onda no es físico. Pero la ecuación (1.4) parece estar en conflicto con esto: ¡si una $\Psi$ dada la satisface, la presuntamente equivalente $2\Psi$ no lo hará! Para dar un sentido preciso a las probabilidades es conveniente trabajar con funciones de onda normalizadas, pero no es necesario, como mostramos ahora. Dado que el tiempo no desempeña ningún papel en el argumento, supongamos en todo lo que sigue que las ecuaciones se refieren a algún instante $t_0$ arbitrario pero fijo. Supongamos que se tiene una función de onda tal que

$$\int dx \, |\Psi|^2 = N \neq 1 . \qquad \text{(1.7)}$$

Entonces afirmo que la probabilidad $dP$ de encontrar la partícula en el intervalo $dx$ en torno a $x$ viene dada por

$$dP = \frac{1}{N} |\Psi|^2 \, dx . \qquad \text{(1.8)}$$

Esto es consistente porque

$$\int dP = \frac{1}{N} \int dx \, |\Psi|^2 = \frac{1}{N} \cdot N = 1 . \qquad \text{(1.9)}$$

Nótese que $dP$ no cambia cuando $\Psi$ se multiplica por cualquier número. Así, esta interpretación deja claro que la escala global de $\Psi$ no contiene física alguna. Mientras la integral $\int |\Psi|^2 \, dx < \infty$ la función de onda se dice normalizable, o de cuadrado integrable. Ajustando el coeficiente global de $\Psi$ podemos entonces hacerla normalizada. En efecto, suponiendo nuevamente (1.7), la nueva función de onda $\Psi'$ definida por

$$\Psi' = \frac{1}{\sqrt{N}} \Psi , \qquad \text{(1.10)}$$

está correctamente normalizada. En efecto

$$\int dx \, |\Psi'|^2 = \frac{1}{N} \int |\Psi|^2 \, dx = 1 . \qquad \text{(1.11)}$$

A veces trabajamos con funciones de onda para las cuales la integral (1.4) es infinita. Tales funciones de onda pueden ser muy útiles. De hecho, la onda plana de de Broglie $\Psi = \exp(ikx - i\omega t)$ para una partícula libre es un buen ejemplo: dado que $|\Psi|^2 = 1$, la integral es de hecho infinita. Lo que esto significa es que $\exp(ikx - i\omega t)$ no representa realmente a una sola partícula. Para construir una función de onda de cuadrado integrable podemos usar una superposición de ondas planas. Es en efecto una sorpresa agradable que ¡la superposición de infinitas ondas no normalizables sea de cuadrado integrable!

## 2. La función de onda como amplitud de probabilidad

Comencemos con una función de onda normalizada en el instante inicial $t_0$

$$\int_{-\infty}^{\infty} \Psi^*(x, t_0) \Psi(x, t_0) \, dx = 1 . \qquad \text{(2.1)}$$

Dado que $\Psi(x, t_0)$ y la ecuación de Schrödinger determinan $\Psi$ para todos los tiempos, ¿tenemos entonces

$$\int_{-\infty}^{\infty} \Psi^*(x, t) \Psi(x, t) \, dx = 1 \, ? \qquad \text{(2.2)}$$

Definamos la densidad de probabilidad $\rho(x, t)$

$$\rho(x, t) \equiv \Psi^*(x, t) \Psi(x, t) = |\Psi(x, t)|^2 . \qquad \text{(2.3)}$$

Definamos también $N(t)$ como la integral de la densidad de probabilidad en todo el espacio:

$$N(t) \equiv \int \rho(x, t) \, dx . \qquad \text{(2.4)}$$

La afirmación en (2.1) de que la función de onda comienza bien normalizada es

$$N(t_0) = 1 , \qquad \text{(2.5)}$$

y la condición de que permanezca normalizada en todos los tiempos posteriores es $N(t) = 1$. Esto quedaría garantizado si mostráramos que para todo tiempo

$$\frac{dN(t)}{dt} = 0 . \qquad \text{(2.6)}$$

A esto lo llamamos conservación de la probabilidad. Comprobemos si la ecuación de Schrödinger garantiza que esta condición se cumpla:

$$\begin{aligned}
\frac{dN(t)}{dt} &= \int_{-\infty}^{\infty} \frac{\partial \rho(x, t)}{\partial t} \, dx \\
&= \int_{-\infty}^{\infty} \left( \frac{\partial \Psi^*}{\partial t} \Psi(x, t) + \Psi^*(x, t) \frac{\partial \Psi(x, t)}{\partial t} \right) dx .
\end{aligned} \qquad \text{(2.7)}$$

A partir de la ecuación de Schrödinger, y su conjugada compleja

$$i\hbar \frac{\partial \Psi}{\partial t} = \hat{H} \Psi \implies \frac{\partial \Psi}{\partial t} = -\frac{i}{\hbar} \hat{H} \Psi , \qquad \text{(2.8)}$$

$$-i\hbar \frac{\partial \Psi^*}{\partial t} = (\hat{H} \Psi)^* \implies \frac{\partial \Psi^*}{\partial t} = \frac{i}{\hbar} (\hat{H} \Psi)^* . \qquad \text{(2.9)}$$

Al conjugar de forma compleja la ecuación de Schrödinger usamos que el conjugado complejo de la derivada temporal de $\Psi$ es simplemente la derivada temporal del conjugado complejo de $\Psi$. Para conjugar el lado derecho simplemente añadimos el asterisco a todo $\hat{H}\Psi$. Ahora usamos (2.8) y (2.9) en (2.7) para obtener

$$\begin{aligned}
\frac{dN(t)}{dt} &= \int_{-\infty}^{\infty} \left( \frac{i}{\hbar} (\hat{H}\Psi)^* \Psi - \frac{i}{\hbar} \Psi^* (\hat{H}\Psi) \right) dx \\
&= \frac{i}{\hbar} \int_{-\infty}^{\infty} (\hat{H}\Psi)^* \Psi \, dx - \frac{i}{\hbar} \int_{-\infty}^{\infty} \Psi^* (\hat{H}\Psi) \, dx .
\end{aligned} \qquad \text{(2.10)}$$

Para mostrar que la derivada temporal de $N(t)$ se anula, basta con mostrar que

$$\int_{-\infty}^{\infty} (\hat{H}\Psi)^* \Psi = \int_{-\infty}^{\infty} \Psi^* (\hat{H}\Psi) . \qquad \text{(2.11)}$$

La ecuación (2.11) es la condición sobre el operador hamiltoniano $\hat{H}$ para la conservación de la probabilidad. De hecho, si $\hat{H}$ es un operador hermítico la condición se satisfará. El operador $\hat{H}$ es un operador hermítico si satisface

$$\text{Operador hermítico:} \qquad \int_{-\infty}^{\infty} (\hat{H}\Psi_1)^* \Psi_2 = \int_{-\infty}^{\infty} \Psi_1^* (\hat{H}\Psi_2) . \qquad \text{(2.12)}$$

Aquí tenemos dos funciones de onda que son arbitrarias, pero que satisfacen las condiciones (1.5) y (1.6). Como se puede ver, un operador hermítico puede trasladarse de actuar sobre la primera función a actuar sobre la segunda función. Cuando las dos funciones son la misma, recuperamos la condición (2.11).

Vale la pena cerrar este círculo de ideas definiendo el conjugado hermítico $T^\dagger$ del operador lineal $T$. Esto se hace de la siguiente manera:

$$\int_{-\infty}^{\infty} \Psi_1^* (T \Psi_2) = \int_{-\infty}^{\infty} (T^\dagger \Psi_1)^* \Psi_2 . \qquad \text{(2.13)}$$

El operador $T^\dagger$, que también es lineal, se calcula partiendo del lado izquierdo y tratando de reescribir la expresión sin ningún operador actuando sobre la segunda función. Se dice que un operador $T$ es hermítico si es igual a su conjugado hermítico:

$$T \text{ es hermítico si } \quad T^\dagger = T . \qquad \text{(2.14)}$$

Los operadores hermíticos son muy importantes en mecánica cuántica. Tienen autovalores reales y siempre se puede encontrar una base del espacio de estados en términos de autoestados ortonormales. Resulta que los observables en mecánica cuántica están representados por operadores hermíticos, y los posibles valores medidos de esos observables vienen dados por sus autovalores. Nuestra búsqueda para mostrar que la normalización se preserva bajo la evolución temporal en mecánica cuántica se ha reducido a mostrar que el operador hamiltoniano es hermítico.

## 3. La corriente de probabilidad

Examinemos más de cerca el integrando de la ecuación (2.10). Usando la expresión explícita para el hamiltoniano tenemos

$$\begin{aligned}
\frac{\partial \rho}{\partial t} &= \frac{i}{\hbar} \left( (\hat{H}\Psi)^* \Psi - \Psi^* (\hat{H}\Psi) \right) \\
&= \frac{i}{\hbar} \left( -\frac{\hbar^2}{2m} \frac{\partial^2 \Psi^*}{\partial x^2} \Psi - \Psi^* \left( -\frac{\hbar^2}{2m} \frac{\partial^2 \Psi}{\partial x^2} \right) + V(x, t) \Psi^* \Psi - \Psi^* V(x, t) \Psi \right) .
\end{aligned} \qquad \text{(3.1)}$$

Las contribuciones del potencial se cancelan y obtenemos entonces

$$\frac{i}{\hbar} \left( (\hat{H}\Psi)^* \Psi - \Psi^* (\hat{H}\Psi) \right) = \frac{\hbar}{2im} \left( \frac{\partial^2 \Psi^*}{\partial x^2} \Psi - \Psi^* \frac{\partial^2 \Psi}{\partial x^2} \right) . \qquad \text{(3.2)}$$

La única posibilidad de mostrar que la integral del lado derecho es cero es mostrar que es una derivada total. ¡Y en efecto lo es!

$$\begin{aligned}
\frac{i}{\hbar} \left( (\hat{H}\Psi)^* \Psi - \Psi^* (\hat{H}\Psi) \right)
&= \frac{\partial}{\partial x} \left[ \frac{\hbar}{2im} \left( \frac{\partial \Psi^*}{\partial x} \Psi - \Psi^* \frac{\partial \Psi}{\partial x} \right) \right] \\
&= -\frac{\partial}{\partial x} \left[ \frac{\hbar}{2im} \left( \Psi^* \frac{\partial \Psi}{\partial x} - \frac{\partial \Psi^*}{\partial x} \Psi \right) \right] \\
&= -\frac{\partial}{\partial x} \left[ \frac{\hbar}{2im} \, 2i \, \mathrm{Im}\!\left( \Psi^* \frac{\partial \Psi}{\partial x} \right) \right] \\
&= -\frac{\partial}{\partial x} \left[ \frac{\hbar}{m} \, \mathrm{Im}\!\left( \Psi^* \frac{\partial \Psi}{\partial x} \right) \right] ,
\end{aligned} \qquad \text{(3.3)}$$

donde usamos que $z - z^* = 2i \, \mathrm{Im}(z)$. Recordemos que el lado izquierdo que hemos evaluado es en realidad $\dfrac{\partial \rho}{\partial t}$, y por lo tanto el resultado obtenido hasta ahora es

$$\frac{\partial \rho}{\partial t} + \frac{\partial}{\partial x} \left[ \frac{\hbar}{m} \, \mathrm{Im}\!\left( \Psi^* \frac{\partial \Psi}{\partial x} \right) \right] = 0 . \qquad \text{(3.4)}$$

Esta ecuación codifica la conservación de la carga y es del tipo

$$\frac{\partial \rho}{\partial t} + \frac{\partial J}{\partial x} = 0 , \qquad \text{(3.5)}$$

donde $J(x, t)$ es la corriente asociada a la densidad de carga $\rho$. Hemos identificado por lo tanto una corriente de probabilidad

$$J(x, t) \equiv \frac{\hbar}{m} \, \mathrm{Im}\!\left( \Psi^* \frac{\partial \Psi}{\partial x} \right) . \qquad \text{(3.6)}$$

Solo hay una componente para esta corriente ya que la partícula se mueve en una dimensión. Las unidades de $J$ son el inverso del tiempo, o probabilidad por unidad de tiempo, como verificamos ahora.

Para una dimensión espacial, $[\Psi] = L^{-1/2}$, lo cual se ve fácilmente a partir del requisito de que $\int dx \, |\Psi|^2$ no tenga unidades. (Cuando se trabaja con $d$ dimensiones espaciales la función de onda tendrá unidades de $L^{-d/2}$). Tenemos entonces

$$\left[ \Psi^* \frac{\partial \Psi}{\partial x} \right] = \frac{1}{L^2} , \qquad [\hbar] = \frac{ML^2}{T} , \qquad \left[ \frac{\hbar}{m} \right] = \frac{L^2}{T} , \qquad \text{(3.7)}$$

$$\implies [J] = \frac{1}{T} = \text{probabilidad por unidad de tiempo} \qquad \text{(3.8)}$$

Ahora podemos mostrar que la derivada temporal de $N$ es cero. En efecto, usando (3.5) tenemos

$$\frac{dN}{dt} = \int_{-\infty}^{\infty} \frac{\partial \rho}{\partial t} \, dx = -\int_{-\infty}^{\infty} \frac{\partial J}{\partial x} \, dx = -\big( J(\infty, t) - J(-\infty, t) \big) . \qquad \text{(3.9)}$$

La derivada se anula si la corriente de probabilidad se anula en el infinito. Recordando que

$$J = \frac{\hbar}{2im} \left( \Psi^* \frac{\partial \Psi}{\partial x} - \Psi \frac{\partial \Psi^*}{\partial x} \right) , \qquad \text{(3.10)}$$

vemos que la corriente en efecto se anula porque nos restringimos a funciones de onda para las cuales $\lim_{x \to \pm\infty} \Psi = 0$ y $\lim_{x \to \pm\infty} \dfrac{\partial \Psi}{\partial x}$ permanece acotado. Por lo tanto tenemos

$$\frac{dN}{dt} = 0 , \qquad \text{(3.11)}$$

como queríamos mostrar.

Para ilustrar cómo funciona la conservación de la probabilidad de manera más general en una dimensión, centrémonos en un segmento $x \in [a, b]$. Entonces la probabilidad $P_{ab}$ de encontrar la partícula en el segmento $[a, b]$ viene dada por

$$P_{ab} = \int_a^b \rho(x, t) \, dx . \qquad \text{(3.12)}$$

Si ahora tomamos la derivada temporal de esto y, como antes, usamos la conservación de la corriente, obtenemos

$$\frac{dP_{ab}}{dt} = -\int_a^b \frac{\partial J(x, t)}{\partial x} \, dx = -J(b, t) + J(a, t) . \qquad \text{(3.13)}$$

Este es el resultado esperado. Si la cantidad de probabilidad en la región $[a, b]$ cambia en el tiempo, debe deberse a la corriente de probabilidad que fluye hacia dentro o hacia fuera en los bordes del intervalo. Suponiendo que las corrientes en $x = b$ y en $x = a$ son positivas, notamos que la probabilidad fluye hacia afuera en $x = b$ y entra en $x = a$. Los signos en el lado derecho anterior reflejan correctamente el efecto de estos flujos sobre la tasa de cambio de la probabilidad total dentro del segmento.

## 4. Corriente de probabilidad en 3D y conservación de la corriente

La determinación de la corriente de probabilidad $J$ para una partícula que se mueve en tres dimensiones sigue la misma ruta tomada antes, pero usamos la versión 3D de la ecuación de Schrödinger. Tras algo de trabajo (tarea) la densidad de probabilidad y la corriente resultan ser

$$\rho(\mathbf{x}, t) = |\Psi(\mathbf{x}, t)|^2 , \qquad J(\mathbf{x}, t) = \frac{\hbar}{m} \, \mathrm{Im}\!\left( \Psi^* \nabla \Psi \right) , \qquad \text{(4.1)}$$

y satisfacen la ecuación de conservación

$$\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{J} = 0 . \qquad \text{(4.2)}$$

En tres dimensiones espaciales, $[\Psi] = L^{-3/2}$ y las unidades de $J$ se determinan rápidamente

$$[\Psi^* \nabla \Psi] = \frac{1}{L^4} , \qquad \left[ \frac{\hbar}{m} \right] = \frac{L^2}{T} , \qquad \text{(4.3)}$$

$$\implies [J] = \frac{1}{T L^2} = \text{probabilidad por unidad de tiempo por unidad de área} \qquad \text{(4.4)}$$

La ecuación de conservación (4.2) resulta particularmente clara en lenguaje integral. Consideremos una región fija $V$ del espacio y la probabilidad $Q_V(t)$ de encontrar la partícula dentro de la región:

$$Q_V(t) = \int_V \rho(\mathbf{x}, t) \, d^3x . \qquad \text{(4.5)}$$

La derivada temporal de la probabilidad se calcula entonces usando la ecuación de conservación

$$\frac{dQ_V}{dt} = \int_V \frac{\partial \rho}{\partial t} \, d^3x = -\int_V \nabla \cdot \mathbf{J} \, d^3x . \qquad \text{(4.6)}$$

Finalmente, usando la ley de Gauss, encontramos

$$\frac{dQ_V}{dt} = -\int_S \mathbf{J} \cdot d\mathbf{a} , \qquad \text{(4.7)}$$

donde $S$ es la frontera del volumen $V$. La interpretación aquí es clara. La probabilidad de que la partícula esté dentro de $V$ puede cambiar en el tiempo si hay un flujo de la corriente de probabilidad a través de la frontera de la región. Cuando el volumen se extiende por todo el espacio, la frontera está en el infinito, y las condiciones sobre la función de onda (que no hemos discutido en el caso 3D) implican que el flujo a través de la frontera en el infinito se anula.

Nuestra densidad de probabilidad, corriente de probabilidad y conservación de la corriente están en perfecta analogía con la densidad de carga electromagnética, la densidad de corriente y la conservación de la corriente. En electromagnetismo las cargas fluyen, en mecánica cuántica la probabilidad fluye. Los términos de la correspondencia se resumen en la siguiente tabla.

|  | Electromagnetismo | Mecánica cuántica |
|------------------------|------------------------|------------------------|
| $\rho$ | densidad de carga | densidad de probabilidad |
| $Q_V$ | carga en un volumen $V$ | probabilidad de encontrar la partícula en $V$ |
| $J$ | densidad de corriente | densidad de corriente de probabilidad |

Sarah Geller transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.

------------------------------------------------------------------------

MIT OpenCourseWare

https://ocw.mit.edu

8.04 Física Cuántica I

Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.


---

<!-- MIT8.04_LecNotes7_ES.md -->

# Lección 7

## Vídeos de esta clase (YouTube)

**Lección 7: Wavepackets and uncertainty. Time evolution and shape change time evolutions.**

- [Wavepackets and Fourier representation](https://www.youtube.com/watch?v=dzI5PddY6eE)
- [Reality condition in Fourier transforms](https://www.youtube.com/watch?v=DvFb-D1zJTA)
- [Widths and uncertainties](https://www.youtube.com/watch?v=vWGP5dogNm8)
- [Shape changes in a wave](https://www.youtube.com/watch?v=50Tla309i7o)
- [Time evolution of a free particle wavepacket](https://www.youtube.com/watch?v=ipXNYnO7yRk)

------------------------------------------------------------------------

B. Zwiebach

28 de febrero de 2016

## Contenidos

1.  Paquetes de onda e incertidumbre
2.  Cambios de forma del paquete de onda
3.  Evolución temporal de un paquete de onda libre

## 1. Paquetes de onda e incertidumbre

Un paquete de onda es una superposición de ondas planas $e^{ikx}$ con diversas longitudes de onda. Trabajemos con paquetes de onda en $t = 0$. Un paquete de onda de este tipo tiene la forma

$$\Psi(x, 0) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi(k) e^{ikx}\, dk. \qquad \text{(1.1)}$$

Si conocemos $\Psi(x, 0)$ entonces $\Phi(k)$ se puede calcular. De hecho, por el teorema de inversión de Fourier, la función $\Phi(k)$ es la transformada de Fourier de $\Psi(x, 0)$, por lo que podemos escribir

$$\Phi(k) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Psi(x, 0) e^{-ikx}\, dx. \qquad \text{(1.2)}$$

Nótese la simetría entre las dos ecuaciones anteriores. Nuestro objetivo aquí es entender cómo se relacionan las incertidumbres en $\Psi(x, 0)$ y en $\Phi(k)$. En la interpretación cuántica de las ecuaciones anteriores recordamos que una onda plana con momento $\hbar k$ tiene la forma $e^{ikx}$. Así, la representación de Fourier de la onda $\Psi(x, 0)$ nos da la manera de representar la onda como una superposición de ondas planas de diferentes momentos.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes7_ES/fig1.png)

Figura 1: Una $\Phi(k)$ centrada en $k = k_0$ y con anchura $\Delta k$.

Consideremos una $\Phi(k)$ definida positiva, real, simétrica respecto a un máximo en $k = k_0$, y con una anchura o incertidumbre $\Delta k$, como se muestra en la Fig. 1. La función de onda resultante $\Psi(x, 0)$ está centrada en $x = 0$. Esto se sigue directamente del argumento de fase estacionaria aplicado a (1.1). La función de onda tendrá cierta anchura $\Delta x$, como se muestra en la Fig. 2. Nótese que allí graficamos el valor absoluto $|\Psi(x, 0)|$ del paquete de onda. Dado que $\Psi(x, 0)$ es compleja, la otra opción habría sido graficar las partes real e imaginaria de $\Psi(x, 0)$.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes7_ES/fig2.png)

Figura 2: La $\Psi(x, 0)$ correspondiente a la $\Phi(k)$ mostrada en la Fig. 1, centrada en $x = 0$ con anchura $\Delta x$.

En efecto, en nuestro caso $\Psi(x, 0)$ ¡no es real! Podemos demostrar que

$$\Psi(x, 0) \text{ es real si y solo si } \Phi^*(-k) = \Phi(k). \qquad \text{(1.3)}$$

Comencemos tomando el complejo conjugado de la expresión (1.1) para $\Psi(x, 0)$:

$$\Psi^*(x, 0) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi^*(k) e^{-ikx}\, dk = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi^*(-k) e^{ikx}\, dk. \qquad \text{(1.4)}$$

En el segundo paso hicimos $k \to -k$ en la integral, lo cual está permitido porque integramos sobre todo $k$, y los dos cambios de signo, uno proveniente de la medida $dk$ y otro de intercambiar los límites de integración, se cancelan mutuamente. Si $\Phi^*(-k) = \Phi(k)$ entonces

$$\Psi^*(x, 0) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi(k) e^{ikx}\, dk = \Psi(x, 0), \qquad \text{(1.5)}$$

tal como queríamos comprobar. Si, por otro lado, sabemos que $\Psi(x, 0)$ es real, entonces la igualdad de $\Psi^*$ y $\Psi$ da

$$\frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi^*(-k) e^{ikx}\, dk = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi(k) e^{ikx}\, dk. \qquad \text{(1.6)}$$

Esto es equivalente a

$$\frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \underbrace{\left[\Phi^*(-k) - \Phi(k)\right]}_{} e^{ikx}\, dk = 0. \qquad \text{(1.7)}$$

Esta ecuación en realidad significa que el objeto bajo la llave debe anularse. En efecto, la integral está calculando la transformada de Fourier del objeto entre corchetes, y nos dice que es cero. Pero una función con transformada de Fourier nula debe ser ella misma nula (por el teorema de Fourier). Por lo tanto, la realidad implica $\Phi^*(-k) = \Phi(k)$, tal como queríamos mostrar.

La condición $\Phi^*(-k) = \Phi(k)$ implica que siempre que $\Phi$ sea distinta de cero para algún $k$, también debe ser distinta de cero para $-k$. Esto no es cierto para nuestra $\Phi(k)$ elegida: hay una protuberancia alrededor de $k_0$ pero no hay una protuberancia correspondiente alrededor de $-k_0$. Por lo tanto $\Psi(x, 0)$ no es real y $\Psi(x, 0)$ tendrá tanto una parte real como una imaginaria, ambas centradas en $x = 0$, como se muestra en la Fig. 3.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes7_ES/fig3.png)

Figura 3: Las partes real e imaginaria de $\Psi(x, 0)$.

Abordemos ahora la cuestión de la anchura. Consideremos la integral para $\Psi(x, 0)$

$$\Psi(x, 0) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi(k) e^{ikx}\, dk, \qquad \text{(1.8)}$$

y cambiemos la variable de integración haciendo $k = k_0 + \tilde{k}$, donde la nueva variable de integración $\tilde{k}$ parametriza la distancia al pico en la distribución de momentos. Entonces tenemos

$$\Psi(x, 0) = \frac{1}{\sqrt{2\pi}} e^{ik_0 x} \int_{-\infty}^{\infty} \Phi(k_0 + \tilde{k}) e^{i\tilde{k}x}\, d\tilde{k}. \qquad \text{(1.9)}$$

A medida que integramos sobre $\tilde{k}$, la región más relevante es

$$\tilde{k} \in \left(-\frac{\Delta k}{2}, \frac{\Delta k}{2}\right), \qquad \text{(1.10)}$$

porque es allí donde $\Phi(k)$ es grande. Al recorrer esta región, la fase $\tilde{k}x$ en la exponencial varía en el intervalo

$$\tilde{k}x \in \left(-\frac{\Delta k}{2}x, \frac{\Delta k}{2}x\right) \quad \text{(para } x > 0\text{)}, \qquad \text{(1.11)}$$

y la excursión total de fase es $\Delta k\, x$. Obtendremos una contribución sustancial a la integral para una excursión de fase total pequeña; si la excursión es grande, la integral se anulará por cancelación. Así, obtenemos una contribución significativa para $\Delta k |x| \lesssim 1$, y contribuciones que se cancelan para $\Delta k |x| \gg 1$.

De esto concluimos que $\Psi(x, 0)$ será distinta de cero para $x \in (-x_0, x_0)$ donde $x_0$ es una constante para la cual $\Delta k\, x_0 \approx 1$. Identificamos la anchura de $\Psi(x, 0)$ con $\Delta x := 2x_0$ y por lo tanto tenemos $\Delta k \cdot \tfrac{1}{2}\Delta x \approx 1$. Dado que los factores de dos son claramente poco fiables en este argumento, simplemente registramos

$$\Delta x\, \Delta k \approx 1. \qquad \text{(1.12)}$$

Esto es lo que queríamos mostrar. El producto de la incertidumbre en la distribución de momentos y la incertidumbre en la posición es una constante de orden uno. Este producto de incertidumbres no es de naturaleza cuántica; como hemos visto, se sigue de las propiedades de las transformadas de Fourier.

La contribución cuántica aparece cuando identificamos $\hbar k$ como el momento $p$. Esta identificación nos permite relacionar las incertidumbres del momento y de $k$:

$$\Delta p = \hbar \Delta k. \qquad \text{(1.13)}$$

Como resultado, podemos multiplicar la ecuación (1.12) por $\hbar$ para obtener:

$$\Delta x\, \Delta p \approx \hbar. \qquad \text{(1.14)}$$

Esta es la versión aproximada del producto de incertidumbre de Heisenberg. La versión precisa requiere definir $\Delta x$ y $\Delta p$ con precisión. Se puede demostrar entonces que

$$\text{Producto de incertidumbre de Heisenberg:} \quad \Delta x\, \Delta p \geq \frac{\hbar}{2}. \qquad \text{(1.15)}$$

El producto de las incertidumbres tiene una cota inferior.

**Ejemplo.** Consideremos el caso en que $\Phi(k)$ es un escalón finito de anchura $\Delta k$ y altura $1/\sqrt{\Delta k}$, como se muestra en la Fig. 4. Hallar $\Psi(x, t)$ y estimar el valor de $\Delta x$.

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes7_ES/fig4.png)

Figura 4: Una distribución de momentos.

Nótese que la $\Psi(x, 0)$ que buscamos calcular debe ser real porque $\Phi^*(-k) = \Phi(k)$. A partir de la representación integral,

$$\begin{aligned}
\Psi(x, 0) &= \frac{1}{\sqrt{2\pi}} \int_{-\Delta k/2}^{\Delta k/2} \frac{1}{\sqrt{\Delta k}} e^{ikx}\, dk \\
&= \frac{1}{\sqrt{2\pi \Delta k}} \left. \frac{e^{ikx}}{ix} \right|_{-\Delta k/2}^{\Delta k/2} \\
&= \frac{1}{\sqrt{2\pi \Delta k}} \frac{e^{i\Delta k x/2} - e^{-i\Delta k x/2}}{ix} \\
&= \frac{1}{\sqrt{2\pi \Delta k}} \frac{2}{x} \sin\left(\frac{\Delta k x}{2}\right) = \sqrt{\frac{\Delta k}{2\pi}} \frac{\sin(\Delta k x/2)}{\Delta k x/2}.
\end{aligned}
\qquad \text{(1.16)}$$

Mostramos $\Psi(x, 0)$ en la Fig. 5. Estimamos

$$\Delta x \approx \frac{2\pi}{\Delta k} \quad \Rightarrow \quad \Delta x\, \Delta k \approx 2\pi. \qquad \text{(1.17)}$$

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes7_ES/fig5.png)

Figura 5: La $\Psi(x, 0)$ correspondiente a la $\Phi(k)$.

## 2. Cambios de forma del paquete de onda

Para apreciar las características generales del movimiento de un paquete de onda estudiamos la solución general de la ecuación de Schrödinger

$$\Psi(x, t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi(k) e^{i(kx - \omega(k)t)}\, dk, \qquad \text{(2.18)}$$

y, bajo el supuesto de que $\Phi(k)$ presenta un pico en torno a cierto valor $k = k_0$, expandimos la frecuencia $\omega(k)$ en una serie de Taylor alrededor de $k = k_0$. Manteniendo los términos hasta e incluyendo $(k - k_0)^2$ tenemos

$$\omega(k) = \omega(k_0) + (k - k_0) \left.\frac{d\omega}{dk}\right|_{k_0} + \frac{1}{2}(k - k_0)^2 \left.\frac{d^2\omega}{dk^2}\right|_{k_0}. \qquad \text{(2.19)}$$

El segundo término desempeñó un papel en la determinación de la velocidad de grupo, y el término siguiente, con las segundas derivadas de $\omega$, es responsable de la distorsión de forma que ocurre con el paso del tiempo. Las derivadas se calculan fácilmente,

$$\frac{d\omega}{dk} = \frac{dE}{dp} = \frac{p}{m} = \frac{\hbar k}{m}, \qquad \frac{d^2\omega}{dk^2} = \frac{\hbar}{m}. \qquad \text{(2.20)}$$

Dado que todas las derivadas de orden superior se anulan, la expansión en (2.19) es en realidad exacta tal como está escrita. ¿Qué tipo de contribución de fase estamos despreciando al ignorar el último término en (2.19)? Tenemos

$$e^{-i\omega(k)t} = e^{\cdots - \frac{i}{2}(k - k_0)^2 \frac{\hbar}{m}t}. \qquad \text{(2.21)}$$

Supongamos que partimos del paquete en $t = 0$ y evolucionamos en el tiempo hasta $t > 0$. Esta fase será despreciable siempre que su magnitud sea significativamente menor que uno:

$$(k - k_0)^2 \frac{\hbar}{m} t \ll 1. \qquad \text{(2.22)}$$

Podemos estimar $(k - k_0)^2 \approx (\Delta k)^2$ ya que los valores relevantes de $k$ deben estar dentro de la anchura de la distribución de momentos. Además, dado que $\Delta p = \hbar \Delta k$ obtenemos

$$\frac{(\Delta p)^2 t}{m \hbar} \ll 1. \qquad \text{(2.23)}$$

Así, la condición para un cambio de forma mínimo es

$$t \ll \frac{m \hbar}{(\Delta p)^2}. \qquad \text{(2.24)}$$

Podemos expresar la desigualdad en términos de la incertidumbre en la posición usando $\Delta x\, \Delta p \approx \hbar$. Obtenemos entonces

$$t \ll \frac{m}{\hbar} (\Delta x)^2. \qquad \text{(2.25)}$$

También, a partir de (2.24) podemos escribir

$$\frac{\Delta p}{m} t \ll \frac{\hbar}{\Delta p}, \qquad \text{(2.26)}$$

lo cual da

$$\frac{\Delta p}{m} t \ll \Delta x. \qquad \text{(2.27)}$$

Esta desigualdad tiene una interpretación clara. Primero notemos que $\Delta p/m$ representa la incertidumbre en la velocidad del paquete. Habrá cambio de forma cuando esta incertidumbre de velocidad, a lo largo del tiempo, produzca incertidumbres de posición comparables a la anchura $\Delta x$ del paquete de onda.

En todas las desigualdades anteriores usamos $\ll$ y esto nos da la condición para un cambio de forma despreciable. Si reemplazamos $\ll$ por $\approx$ estamos dando una estimación de algún cambio de forma medible.

**Ejercicio.** Supongamos que hemos localizado un electrón dentro de $\Delta x = 10^{-10}$ m. Estimar el tiempo máximo $t$ durante el cual puede permanecer localizado a ese nivel.

Usando (2.25) tenemos

$$t \approx \frac{m(\Delta x)^2}{\hbar} = \frac{mc^2 (\Delta x)^2}{\hbar c \cdot c} = \frac{0.5\ \text{MeV} \cdot 10^{-20}\ \text{m}^2}{200\ \text{MeV}\,\text{fm} \cdot 3 \times 10^8\ \text{m/s}} \approx 10^{-16}\ \text{s}. \qquad \text{(2.28)}$$

Si originalmente tuviéramos $\Delta x = 10^{-2}$ m, ¡habríamos obtenido $t \approx 1$ s!

## 3. Evolución temporal de un paquete de onda libre

Supongamos que conocemos la función de onda $\Psi(x, 0)$ en el instante cero. Nuestro objetivo es hallar $\Psi(x, t)$. Esto se logra en unos pocos pasos sencillos.

1.  Usar $\Psi(x, 0)$ para calcular $\Phi(k)$:

$$\Phi(k) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} dx\, \Psi(x, 0) e^{-ikx}. \qquad \text{(3.1)}$$

1.  Usar $\Phi(k)$ para reescribir $\Psi(x, 0)$ como una superposición de ondas planas:

$$\Psi(x, 0) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi(k) e^{ikx}\, dk. \qquad \text{(3.2)}$$

Esto es útil porque sabemos cómo evolucionan las ondas planas en el tiempo. Lo anterior se denomina la representación de Fourier de $\Psi(x, 0)$.

1.  Una onda plana $\psi_k(x, 0) = e^{ikx}$ evoluciona en el tiempo hacia $\psi_k(x, t) = e^{i(kx - \omega(k)t)}$ con $\hbar\omega = \dfrac{\hbar^2 k^2}{2m}$. Usando la superposición tenemos que (3.2) evoluciona hacia

$$\Psi(x, t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi(k) e^{i(kx - \omega(k)t)}\, dk. \qquad \text{(3.3)}$$

Esta es, de hecho, la respuesta para $\Psi(x, t)$. Se puede confirmar fácilmente que esto es así porque: (i) resuelve la ecuación de Schrödinger (¡compruébelo!) y (ii) al fijar $t = 0$ en $\Psi(x, t)$ obtenemos la función de onda inicial (3.2) que representaba la condición inicial.

1.  Si es posible, realizar la integral sobre $k$ para hallar una expresión en forma cerrada para $\Psi(x, t)$. Si resulta demasiado difícil, la integral siempre puede realizarse numéricamente.

**Ejemplo: Evolución de un paquete de onda gaussiano libre.** Tomemos

$$\psi_a(x, 0) = \frac{1}{(2\pi)^{1/4} \sqrt{a}}\, e^{-x^2/4a^2}. \qquad \text{(3.4)}$$

Este es un paquete de onda gaussiano en $t = 0$. La constante $a$ tiene unidades de longitud y $\Delta x \approx a$. El estado $\psi_a$ está correctamente normalizado, como se puede comprobar que $\int dx\, |\psi_a(x, 0)|^2 = 1$.

No realizaremos aquí los cálculos, pero podemos imaginar que este paquete cambiará de forma a medida que evolucione el tiempo. ¿Cuál es la escala temporal $\tau$ para los cambios de forma? La ecuación (2.25) nos da una pista. El lado derecho representa una escala temporal para el cambio de forma. Así que debemos tener

$$\tau \approx \frac{m}{\hbar} a^2. \qquad \text{(3.5)}$$

Esto es, de hecho, correcto. Descubrirá, al hacer evolucionar la gaussiana, que el intervalo de tiempo relevante es en realidad el doble del tiempo anterior:

$$\tau \equiv \frac{2ma^2}{\hbar}. \qquad \text{(3.6)}$$

Si consideramos la norma al cuadrado de la función de onda

$$|\Psi_a(x, 0)|^2 = \frac{1}{\sqrt{2\pi}} \frac{1}{a} e^{-x^2/2a^2}, \qquad \text{(3.7)}$$

encontrará que, tras la evolución temporal, se tiene

$$|\Psi_a(x, t)|^2 = \frac{1}{\sqrt{2\pi}} \frac{1}{a(t)} e^{-x^2/2a(t)^2}, \qquad \text{(3.8)}$$

donde $a(t)$ es una anchura dependiente del tiempo. El objetivo de su cálculo será determinar $a(t)$ y ver cómo interviene $\tau$ en $a(t)$.

*Andrew Turner transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare

https://ocw.mit.edu

8.04 Física Cuántica I

Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

# Apéndice: Lista de problemas 3 (Problem Set 3, 2016)

**Física Cuántica I (8.04) — Primavera de 2016**

**Departamento de Física del MIT — Tarea 3**

*Fecha de entrega: jueves 25 de febrero de 2016, 5:00 pm*

*18 de febrero de 2016*

**Anuncios**

- Lectura recomendada: Griffiths, secciones 1.1, 1.2, 1.4 y 1.5.

## Problema 1: Ejercicios con conmutadores \[10 puntos\]

Sean $A$, $B$ y $C$ operadores lineales.

1.  Demuestre que $[A, BC] = [A, B]C + B[A, C]$.

2.  Demuestre que $[AB, C] = A[B, C] + [A, C]B$.

3.  Demuestre que $[A, [B, C]] + [B, [C, A]] + [C, [A, B]] = 0$.

4.  Calcule $[\hat{x}^n, \hat{p}]$ y $[\hat{x}, \hat{p}^n]$ para $n$ un número entero arbitrario mayor que cero.

5.  Calcule $[\hat{x}\hat{p}, \hat{x}^2]$ y $[\hat{x}\hat{p}, \hat{p}^2]$.

## Problema 2: Pruebas sencillas de la aproximación de fase estacionaria \[10 puntos\]

Consideremos aquí integrales de la forma

$$\Psi(x) = \int_{-\infty}^{\infty} dk\, \Phi(k) e^{ikx},$$

donde $\Phi(k)$ es una función marcadamente localizada alrededor de $k = k_0$. En cada uno de los siguientes casos, use el argumento de fase estacionaria para predecir la ubicación del pico de $|\Psi(x)|$. A continuación calcule la integral de manera exacta para hallar $\Psi(x)$, $|\Psi(x)|$, y confirmar su predicción.

1.  $\Phi(k) = e^{-L^2(k-k_0)^2}$, donde $L$ es una constante con unidades de longitud.

2.  $\Phi(k) = e^{-L^2(k-k_0)^2} e^{-ikx_0}$, donde $x_0$ y $L$ son constantes con unidades de longitud.

Integral útil: válida para constantes complejas $a$ y $b$, con la parte real de $a$ positiva:

$$\int_{-\infty}^{\infty} e^{-ax^2 + bx}\, dx = \sqrt{\frac{\pi}{a}} \exp\left(\frac{b^2}{4a}\right), \quad \text{cuando } \operatorname{Re}(a) > 0.$$

## Problema 3: Invariancia galileana de la ecuación de Schrödinger libre \[15 puntos\]

Demuestre que la ecuación de Schrödinger unidimensional de partícula libre para la función de onda $\Psi(x, t)$:

$$i\hbar \frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m} \frac{\partial^2 \Psi}{\partial x^2},$$

es invariante bajo transformaciones de Galileo

$$x' = x - vt, \qquad t' = t.$$

Con esto queremos decir que existe una $\Psi'(x', t')$ de la forma

$$\Psi'(x', t') = f(x, t)\, \Psi(x, t),$$

donde la función $f(x, t)$ involucra a $x$, $t$, $\hbar$, $m$ y $v$, y tal que $\Psi'$ satisface la ecuación de Schrödinger correspondiente en las variables primadas.

$$i\hbar \frac{\partial \Psi'}{\partial t'} = -\frac{\hbar^2}{2m} \frac{\partial^2 \Psi'}{\partial x'^2}.$$

1.  Halle la función $f(x, t)$. \[Pista: note que la función $f(x, t)$ no puede depender de ningún observable de $\Psi$; es una función universal que se usa para transformar cualquier $\Psi$. Así, si $\Psi$ es una (única) onda plana, $f$ no puede depender de su momento ni de su energía.\]

2.  Demuestre que la solución de onda plana

$$\Psi(x, t) = A\, e^{i(kx - \omega t)}$$

se transforma como se espera. Es decir, dé $\Psi'$ y muestre que representa, en el sistema de referencia primado, una partícula con el momento y la energía esperados.

## Problema 4: Repetir la conservación de la corriente en 3D \[10 puntos\]

En clase dedujimos la expresión para la corriente de probabilidad unidimensional $J(x, t)$ partiendo de $\rho(x, t) = |\Psi(x, t)|^2$ y usando la ecuación de Schrödinger unidimensional para escribir

$$\frac{\partial \rho}{\partial t} + \frac{\partial J}{\partial x} = 0.$$

Repita los mismos pasos partiendo de

$$\rho(x, t) = |\Psi(x, t)|^2,$$

y usando la ecuación de Schrödinger tridimensional para deducir la forma de la corriente de probabilidad $J(x, t)$ que debe aparecer en la ecuación de conservación

$$\frac{\partial \rho}{\partial t} + \nabla \cdot J = 0.$$

## Problema 5: Evolución temporal del solapamiento entre dos estados \[10 puntos\] (Merzbacher)

Consideremos una función de onda que en el instante $t = 0$ es la superposición de dos paquetes de onda estrechos y muy separados, $\Psi_1$ y $\Psi_2$:

$$\Psi(x, 0) = \Psi_1(x, 0) + \Psi_2(x, 0).$$

Cada paquete es normalizable por separado. Definimos la integral de solapamiento $\gamma(t)$ como

$$\gamma(t) \equiv \int_{-\infty}^{\infty} \Psi_1^*(x, t) \Psi_2(x, t)\, dx.$$

En el instante $t = 0$ el valor de $|\gamma(0)|$ es muy pequeño. A medida que los paquetes evolucionan y se ensanchan, ¿qué le sucederá al valor de $|\gamma(t)|$? ¿Aumentará a medida que los paquetes se superponen?

## Problema 6: Corriente de probabilidad en una dimensión \[10 puntos\]

Calcule la corriente de probabilidad $J(x)$ para las siguientes funciones de onda, todas ellas referidas a $t = 0$:

1.  $\Psi(x) = A\, e^{\gamma x}$. Aquí $A$ es una constante compleja y $\gamma$ es una constante real.

2.  $\Psi(x) = N(x) e^{iS(x)/\hbar}$. Aquí $N(x)$ y $S(x)$ son reales.

3.  $\Psi(x) = A e^{ikx} + B e^{-ikx}$. Aquí $A$, $B$ son constantes complejas y $k$ es real.

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*


---

<!-- MIT8.04_LecNotes8_ES.md -->

# Clase 8[1]

## Vídeos de esta clase (YouTube)

**Lección 8: Uncovering momentum space. Expectation values and their time dependence.**

- [Fourier transforms and delta functions](https://www.youtube.com/watch?v=8abBLKEZLaI)
- [Parseval identity](https://www.youtube.com/watch?v=i-bP2OkQxUI)
- [Three-dimensional Fourier transforms](https://www.youtube.com/watch?v=MJM1AzpB6Y4) (06:04)
- [Expectation values of operators](https://www.youtube.com/watch?v=XQKV-hpsurs)
- [Time dependence of expectation values](https://www.youtube.com/watch?v=AnzhigYawy8)

------------------------------------------------------------------------

B. Zwiebach

29 de febrero de 2016

## Contenido

1.  Descubriendo el espacio de momentos
2.  Valores esperados de operadores
3.  Dependencia temporal de los valores esperados

## 1. Descubriendo el espacio de momentos

Comenzamos ahora una serie de desarrollos que conducen a la idea del espacio de momentos como contrapartida o dual del espacio de posiciones. En esta sección la dependencia temporal de las funciones de onda no jugará ningún papel. Por lo tanto, simplemente suprimiremos la dependencia temporal. Se puede imaginar que todas las funciones de onda están evaluadas en el tiempo igual a cero o en algún tiempo arbitrario $t_0$.

Comenzamos recordando las identidades clave del teorema de Fourier:

$$\Psi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi(k) e^{ikx}\, dk \,,$$

$$\Phi(k) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Psi(x) e^{-ikx}\, dx \,. \qquad \text{(1.1)}$$

La transformada de Fourier $\Phi(k)$ contiene toda la información que porta la función de onda $\Psi(x)$. Esto es evidente porque conocer $\Phi(k)$ equivale a conocer $\Psi(x)$. La función $\Phi(k)$ actúa también como el peso con el que sumamos las ondas planas de momento $\hbar k$ para formar $\Psi(x)$.

Ahora veremos que la consistencia de las ecuaciones anteriores puede usarse para deducir una representación integral de la función delta. Dicha representación es una herramienta necesaria para nuestra discusión posterior. La idea es reemplazar $\Phi(k)$ en la primera ecuación por el valor dado en la segunda ecuación. Para mantener la notación clara, debemos usar $x'$ como variable muda de integración en la segunda ecuación. Tenemos

$$\Psi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} dk\, e^{ikx} \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} dx'\, e^{-ikx'}\Psi(x')$$

$$= \int_{-\infty}^{\infty} dx'\, \Psi(x') \underbrace{\frac{1}{2\pi}\int_{-\infty}^{\infty} dk\, e^{ik(x-x')}}_{} \,. \qquad \text{(1.2)}$$

Observemos el tipo de integral. El factor indicado por la llave reduce la integral en $x'$ a una evaluación en $x$. Sabemos que $\delta(x'-x)$ es la función tal que, para una $f(x)$ general,

$$\int_{-\infty}^{\infty} dx'\, f(x')\, \delta(x'-x) = f(x)\,, \qquad \text{(1.3)}$$

y por lo tanto concluimos que el factor indicado por la llave es una función delta

$$\delta(x'-x) = \frac{1}{2\pi}\int_{-\infty}^{\infty} dk\, e^{ik(x-x')}\,. \qquad \text{(1.4)}$$

En esta integral se puede hacer $k \to -k$, y como $dk$ es invariante bajo este cambio, encontramos que $\delta(x'-x) = \delta(x-x')$, o más sencillamente, $\delta(x) = \delta(-x)$. Registraremos la representación integral de la función delta usando el otro signo:

$$\delta(x-x') = \frac{1}{2\pi}\int_{-\infty}^{\infty} dk\, e^{ik(x-x')}\,. \qquad \text{(1.5)}$$

Otra propiedad útil de las funciones delta es

$$\delta(ax) = \frac{1}{|a|}\delta(x)\,. \qquad \text{(1.6)}$$

Llegados a este punto preguntamos: ¿cómo se ve la condición de normalización de $\Psi(x)$ en términos de $\Phi(k)$? Simplemente debemos calcular. Tenemos

$$\int_{-\infty}^{\infty} dx\, \Psi^*(x)\Psi(x) = \int_{-\infty}^{\infty} dx\, \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \Phi^*(k) e^{-ikx}\, dk\, \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \Phi(k') e^{ik'x}\, dk' \,. \qquad \text{(1.7)}$$

Reordenando las integrales para hacer primero la integral en $x$ escribimos

$$\int_{-\infty}^{\infty} dx\, \Psi^*(x)\Psi(x) = \int_{-\infty}^{\infty} dk \int_{-\infty}^{\infty} dk'\, \Phi^*(k)\Phi(k') \frac{1}{2\pi}\int_{-\infty}^{\infty} dx\, e^{i(k'-k)x}$$

$$= \int_{-\infty}^{\infty} dk\, dk'\, \Phi^*(k)\Phi(k') \delta(k'-k)$$

$$= \int_{-\infty}^{\infty} dk\, \Phi^*(k)\Phi(k)\,, \qquad \text{(1.8)}$$

donde reconocimos la presencia de una función delta y realizamos la integral sobre $k'$. Nuestro resultado final es entonces

$$\int_{-\infty}^{\infty} dx\, |\Psi(x)|^2 = \int_{-\infty}^{\infty} dk\, |\Phi(k)|^2\,. \qquad \text{(1.9)}$$

Esto se conoce como el teorema de Parseval, o más generalmente, el teorema de Plancherel. Esta ecuación relaciona la normalización de $\Psi(x)$ con una normalización bastante análoga para $\Phi(k)$. Esto sugiere que, al igual que para $|\Psi(x)|^2$, podríamos tener una interpretación probabilística para $|\Phi(k)|^2$.

Puesto que físicamente asociamos nuestras ondas planas con autoestados de momento, reescribamos el teorema de Parseval usando el momento $p = \hbar k$. En lugar de integrales sobre $k$ tendremos integrales sobre $p$. Definiendo $\tilde\Phi(p) = \Phi(k)$, las ecuaciones (1.1) se convierten en

$$\Psi(x) = \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^{\infty} \tilde\Phi(p)\, e^{ipx/\hbar}\, dp \,,$$

$$\tilde\Phi(p) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Psi(x) e^{-ipx/\hbar}\, dx \,. \qquad \text{(1.10)}$$

Para obtener un par de ecuaciones más simétrico podemos redefinir la función $\tilde\Phi(p)$. Haremos $\tilde\Phi(p) \to \Phi(p)\sqrt{\hbar}$ en las ecuaciones (1.10). Obtenemos entonces la forma final de las relaciones de Fourier en términos del momento:

$$\Psi(x) = \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^{\infty} \Phi(p)\, e^{ipx/\hbar}\, dp \,,$$

$$\Phi(p) = \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^{\infty} \Psi(x) e^{-ipx/\hbar}\, dx \,. \qquad \text{(1.11)}$$

Análogamente, el teorema de Parseval (1.9) se convierte en

$$\int_{-\infty}^{\infty} dx\, |\Psi(x)|^2 = \int_{-\infty}^{\infty} dp\, |\Phi(p)|^2\,. \qquad \text{(1.12)}$$

**Ejercicio.** Verifique que las redefiniciones que hicimos para llegar a (1.11) efectivamente producen (1.12) partiendo de (1.9).

Nuestra interpretación de la ecuación superior en (1.11) es que $\Phi(p)$ denota el peso con el que sumamos el estado de momento $e^{ipx/\hbar}$ en la superposición que representa a $\Psi(x)$. Este estado de momento $e^{ipx/\hbar}$ es un autoestado del operador de momento $\hat p$ con autovalor $p$. Así como decimos que $\Psi(x)$ es la función de onda en el espacio de posiciones $x$, podemos pensar en $\Phi(p)$ como la función de onda en el espacio de momentos $p$. La identidad de Parseval (1.12) sugiere que $\Phi(p)$ tiene también una interpretación probabilística. Dado que una $\Psi(x)$ correctamente normalizada conduce a una $\Phi(p)$ que satisface $\int dp\, |\Phi(p)|^2 = 1$, postulamos que:

$$\begin{gathered}
|\Phi(p)|^2\, dp \ \text{es la probabilidad de encontrar la partícula}\\
\text{con momento en el rango } (p, p+dp)\,. \qquad \text{(1.13)}
\end{gathered}$$

Esto completa bastante bien la analogía entre el espacio de posiciones y el espacio de momentos.

Consideremos la generalización a 3D. El teorema de Fourier en el lenguaje del espacio de momentos (es decir, usando $p$ en lugar de $k$) toma la forma

$$\Psi(\mathbf{x}) = \frac{1}{(2\pi\hbar)^{3/2}} \int_{-\infty}^{\infty} d^3p\, \Phi(\mathbf{p})\, e^{i\mathbf{p}\cdot\mathbf{x}/\hbar} \,,$$

$$\Phi(\mathbf{p}) = \frac{1}{(2\pi\hbar)^{3/2}} \int_{-\infty}^{\infty} d^3x\, \Psi(\mathbf{x})\, e^{-i\mathbf{p}\cdot\mathbf{x}/\hbar} \,. \qquad \text{(1.14)}$$

Tal como hicimos en el caso 1D, si insertamos la transformada de Fourier en la expresión para $\Psi(\mathbf{x})$, encontramos una representación integral de la función $\delta$ en 3D

$$\Psi(\mathbf{x}) = \frac{1}{(2\pi\hbar)^3} \int d^3p\, e^{i\mathbf{p}\cdot\mathbf{x}/\hbar} \int d^3x'\, \Psi(\mathbf{x}')\, e^{-i\mathbf{p}\cdot\mathbf{x}'/\hbar}$$

$$= \int d^3x'\, \Psi(\mathbf{x}')\, \frac{1}{(2\pi\hbar)^3} \int d^3p\, e^{i\mathbf{p}\cdot(\mathbf{x}-\mathbf{x}')/\hbar}$$

$$= \int d^3x'\, \Psi(\mathbf{x}')\, \frac{1}{(2\pi)^3} \int d^3k\, e^{i\mathbf{k}\cdot(\mathbf{x}-\mathbf{x}')} \,, \qquad \text{(1.15)}$$

lo que lleva a la identificación

$$\delta^3(\mathbf{x}-\mathbf{x}') = \frac{1}{(2\pi)^3} \int d^3k\, e^{i\mathbf{k}\cdot(\mathbf{x}-\mathbf{x}')} \,. \qquad \text{(1.16)}$$

Entonces es directo deducir la identidad de Parseval (¡ejercicio!). Encontramos

$$\int_{-\infty}^{\infty} d^3x\, |\Psi(\mathbf{x})|^2 = \int d^3p\, |\Phi(\mathbf{p})|^2\,. \qquad \text{(1.17)}$$

Usamos en el espacio de momentos 3D la misma interpretación probabilística: $|\Phi(\mathbf{p})|^2\, d^3p$ es la probabilidad de encontrar la partícula con momento en el rango $d^3p$ alrededor de $\mathbf{p}$.

## 2. Valores esperados de operadores

Consideremos una variable aleatoria $Q$ que toma valores en el conjunto $\{Q_1, \ldots, Q_n\}$ con probabilidades respectivas $\{p_1, \ldots, p_n\}$. El valor esperado $\langle Q \rangle$ (o valor esperado) de $Q$ es el valor promedio que esperamos encontrar tras una observación repetida de $Q$, y viene dado por la fórmula

$$\langle Q \rangle = \sum_{i=1}^{n} Q_i\, p_i \,. \qquad \text{(2.18)}$$

Como hemos visto, en un sistema cuántico la probabilidad de que una partícula se encuentre en $[x, x+dx]$ en el instante $t$ está dada por

$$\Psi^*(x,t)\Psi(x,t)\, dx\,. \qquad \text{(2.19)}$$

Así, el valor esperado de $x$, denotado por $\langle \hat x \rangle$, viene dado por

$$\langle \hat x \rangle \equiv \int_{-\infty}^{\infty} x\, \Psi^*(x,t)\Psi(x,t)\, dx\,. \qquad \text{(2.20)}$$

Nótese que este valor esperado depende de $t$. ¿A qué corresponde físicamente $\langle \hat x \rangle$? Si consideramos muchas copias del sistema físico, y medimos la posición $x$ en el instante $t$ en todas ellas, entonces el valor promedio registrado convergerá a $\langle \hat x \rangle$ a medida que el número de medidas se aproxime a infinito.

Discutamos ahora el valor esperado del momento. Puesto que hemos establecido que

$$\Phi^*(p,t)\Phi(p,t)\, dp \qquad \text{(2.21)}$$

es la probabilidad de encontrar la partícula con momento en el rango $[p, p+dp]$ en el instante $t$, definimos el valor esperado $\langle \hat p \rangle$ del operador de momento como

$$\langle \hat p \rangle \equiv \int_{-\infty}^{\infty} p\, \Phi^*(p,t)\Phi(p,t)\, dp\,. \qquad \text{(2.22)}$$

Ahora manipularemos esta expresión para ver qué forma toma en el espacio de configuración. Usando (1.11) y su versión compleja conjugada tenemos

$$\langle \hat p \rangle = \int_{-\infty}^{\infty} p\, \Phi^*(p,t)\Phi(p,t)\, dp$$

$$= \int_{-\infty}^{\infty} dp\, p \int_{-\infty}^{\infty} \frac{dx}{\sqrt{2\pi\hbar}}\, e^{ipx/\hbar}\Psi^*(x,t) \int_{-\infty}^{\infty} \frac{dx'}{\sqrt{2\pi\hbar}}\, e^{-ipx'/\hbar}\Psi(x',t)$$

$$= \frac{1}{2\pi\hbar} \int_{-\infty}^{\infty} dx\, \Psi^*(x,t) \int_{-\infty}^{\infty} dx'\, \Psi(x',t) \int_{-\infty}^{\infty} dp\, p\, e^{ipx/\hbar}e^{-ipx'/\hbar} \qquad \text{(2.23)}$$

$$= \frac{1}{2\pi\hbar} \int_{-\infty}^{\infty} dx\, \Psi^*(x,t) \int_{-\infty}^{\infty} dx'\, \Psi(x',t) \int_{-\infty}^{\infty} dp\, \left(\frac{\hbar}{i}\frac{\partial}{\partial x}\right) e^{ipx/\hbar}e^{-ipx'/\hbar}$$

$$= \int_{-\infty}^{\infty} dx\, \Psi^*(x,t) \int_{-\infty}^{\infty} dx'\, \Psi(x',t) \frac{\hbar}{i}\frac{\partial}{\partial x} \frac{1}{2\pi\hbar}\int_{-\infty}^{\infty} dp\, e^{ipx/\hbar}e^{-ipx'/\hbar}\,.$$

Haciendo $p = \hbar u$ en la integral final tenemos

$$\frac{1}{2\pi\hbar} \int_{-\infty}^{\infty} dp\, e^{ipx/\hbar}e^{-ipx'/\hbar} = \frac{1}{2\pi}\int_{-\infty}^{\infty} du\, e^{iu(x-x')} = \delta(x-x')\,. \qquad \text{(2.24)}$$

Como resultado, tenemos

$$\langle \hat p \rangle = \int_{-\infty}^{\infty} dx\, \Psi^*(x,t) \int_{-\infty}^{\infty} dx'\, \Psi(x',t) \frac{\hbar}{i}\frac{\partial}{\partial x} \delta(x-x')$$

$$= \int_{-\infty}^{\infty} dx\, \Psi^*(x,t) \frac{\hbar}{i}\frac{\partial}{\partial x} \int_{-\infty}^{\infty} dx'\, \Psi(x',t)\delta(x'-x)\,, \qquad \text{(2.25)}$$

donde cambiamos el orden de integración. La integral en $x'$ se realiza ahora fácilmente y encontramos

$$\langle \hat p \rangle = \int_{-\infty}^{\infty} dx\, \Psi^*(x,t) \left(\frac{\hbar}{i}\frac{\partial}{\partial x}\right) \Psi(x,t)\,, \qquad \text{(2.26)}$$

Hemos así demostrado que

$$\langle \hat p \rangle = \int_{-\infty}^{\infty} dx\, \Psi^*(x,t)\, \hat p\, \Psi(x,t)\,, \qquad \hat p = \frac{\hbar}{i}\frac{\partial}{\partial x}\,. \qquad \text{(2.27)}$$

Nótese la posición del operador $\hat p$: actúa sobre $\Psi(x)$. Esto motiva la siguiente definición para el valor esperado $\langle \hat Q \rangle$ de cualquier operador $\hat Q$:

$$\langle \hat Q \rangle = \int_{-\infty}^{\infty} dx\, \Psi^*(x,t)\, \hat Q\, \Psi(x,t)\,. \qquad \text{(2.28)}$$

**Ejemplo:** Consideremos el operador de energía cinética $\hat T$ para una partícula que se mueve en 1D:

$$\hat T = \frac{\hat p^2}{2m} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}\,. \qquad \text{(2.29)}$$

La definición da

$$\langle \hat T \rangle = -\frac{\hbar^2}{2m} \int dx\, \Psi^*(x,t)\, \frac{\partial^2}{\partial x^2}\Psi(x,t)\,. \qquad \text{(2.30)}$$

La energía cinética es un operador positivo (por ser proporcional al cuadrado del operador de momento). Por lo tanto es de interés hacer manifiesta esta positividad. Integrando por partes una de las derivadas en $x$ e ignorando los términos de frontera, que se supone que se anulan, encontramos

$$\langle \hat T \rangle = \frac{\hbar^2}{2m} \int dx\, \left| \frac{\partial \Psi(x,t)}{\partial x} \right|^2\,. \qquad \text{(2.31)}$$

¡Esto es manifiestamente positivo! El valor esperado de $\hat T$ también puede calcularse en el espacio de momentos usando la interpretación probabilística que dio lugar a (2.22):

$$\langle \hat T \rangle = \int dp\, \frac{p^2}{2m}\, |\Phi(p,t)|^2\,. \qquad \text{(2.32)}$$

Otros ejemplos de operadores cuyos valores esperados podemos ahora calcular son el operador de momento $\hat p \to \frac{\hbar}{i}\nabla$ en 3D, el operador de energía potencial $V(\hat{\mathbf{x}})$, y el operador de momento angular

$$\hat{\mathbf L} = \hat{\mathbf r} \times \hat{\mathbf p} = \left( \hat y \hat p_z - \hat z \hat p_y,\ \hat z \hat p_x - \hat x \hat p_z,\ \hat x \hat p_y - \hat y \hat p_x \right)$$

$$= \frac{\hbar}{i}\left( y\frac{\partial}{\partial z} - z\frac{\partial}{\partial y},\ z\frac{\partial}{\partial x} - x\frac{\partial}{\partial z},\ x\frac{\partial}{\partial y} - y\frac{\partial}{\partial x} \right)\,. \qquad \text{(2.33)}$$

## 3. Dependencia temporal de los valores esperados

Los valores esperados de los operadores son, en general, dependientes del tiempo porque las funciones de onda que representan los estados dependen del tiempo. Consideraremos aquí operadores que no tienen dependencia temporal explícita, es decir, operadores que no la tienen:

$$i\hbar \frac{d}{dt}\langle Q \rangle = i\hbar \frac{d}{dt} \int_{-\infty}^{\infty} d^3x\, \Psi^*(\mathbf{x},t)\, \hat Q\, \Psi(\mathbf{x},t)$$

$$= i\hbar \int_{-\infty}^{\infty} d^3x\, \left[ \frac{\partial \Psi^*}{\partial t}\, \hat Q\, \Psi + \Psi^*\, \hat Q\, \frac{\partial \Psi}{\partial t} \right]$$

$$= i\hbar \int_{-\infty}^{\infty} d^3x\, \left[ \frac{i}{\hbar}(\hat H\Psi)^*\, \hat Q\, \Psi - \frac{i}{\hbar}\Psi^*\, \hat Q\,(\hat H\Psi) \right] \qquad \text{(3.34)}$$

$$= \int_{-\infty}^{\infty} d^3x\, \left[ \Psi^*\, \hat Q\hat H\, \Psi - (\hat H\Psi^*)\, \hat Q\, \Psi \right]$$

Recordamos ahora la hermiticidad de $\hat H$, lo que implica que

$$\int_{-\infty}^{\infty} dx\, (\hat H\Psi_1)^*\, \Psi_2 = \int_{-\infty}^{\infty} dx\, \Psi_1^*\, \hat H \Psi_2\,. \qquad \text{(3.35)}$$

Esto puede aplicarse al segundo término del último lado derecho de (3.34) para trasladar $\hat H$ hacia la otra función de onda

$$i\hbar \frac{d}{dt}\langle Q \rangle = \int_{-\infty}^{\infty} d^3x\, \left[ \Psi^*\, \hat Q\hat H\, \Psi - \Psi^*\, \hat H\hat Q\, \Psi \right]$$

$$= \int_{-\infty}^{\infty} d^3x\, \Psi^*\, \left[ \hat Q, \hat H \right] \Psi\,, \qquad \text{(3.36)}$$

donde observamos la aparición del conmutador. En definitiva, hemos demostrado que para operadores $\hat Q$ que no dependen explícitamente del tiempo,

$$i\hbar \frac{d}{dt}\langle \hat Q \rangle = \left\langle \left[ \hat Q, \hat H \right] \right\rangle\,. \qquad \text{(3.37)}$$

Nótese que el conmutador satisface las siguientes propiedades (tarea):

$$[A,B] = -[B,A] \qquad \text{(3.38)}$$

$$[A,A] = 0 \qquad \text{(3.39)}$$

$$[A, B+C] = [A,B] + [A,C] \qquad \text{(3.40)}$$

$$[A, BC] = [A,B]\, C + B\, [A,C] \qquad \text{(3.41)}$$

$$[AB, C] = A\, [B,C] + [A,C]\, B \qquad \text{(3.42)}$$

$$0 = [A,[B,C]] + [B,[C,A]] + [C,[A,B]]\,. \qquad \text{(3.43)}$$

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.*

[1] Andrew Turner transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.


---

<!-- MIT8.04_LecNotes9_ES.md -->

# Observables, operadores hermíticos e incertidumbre

## Vídeos de esta clase (YouTube)

**Lección 9: Observables, Hermitian operators, measurement and uncertainty. Particle on a circle.**

- [Expectation value of Hermitian operators](https://www.youtube.com/watch?v=qP6y2edM6Ms)
- [Eigenfunctions of a Hermitian operator](https://www.youtube.com/watch?v=K3WI62VJqVo)
- [Completeness of eigenvectors and measurement postulate](https://www.youtube.com/watch?v=XF6FAEi_54I)
- [Consistency condition. Particle on a circle](https://www.youtube.com/watch?v=_jPVD45YYlk)
- [Defining uncertainty](https://www.youtube.com/watch?v=rCRH9CTThlo)

------------------------------------------------------------------------

B. Zwiebach

3 de marzo de 2016

## Contenido

1.  Observables y operadores hermíticos
2.  Incertidumbre

## 1. Observables y operadores hermíticos

Comencemos recordando la definición de un operador hermítico. El operador $\hat{Q}$ es hermítico si, para la clase de funciones de onda $\Psi$ con las que trabajamos,

$$\int dx\, \Psi_1^* \hat{Q}\Psi_2 = \int dx\, (\hat{Q}\Psi_1)^* \Psi_2 \, . \qquad \text{(1.1)}$$

A veces usaremos una notación más breve para las integrales de pares de funciones:

$$(\Psi_1, \Psi_2) \equiv \int dx\, \Psi_1^*(x)\Psi_2(x) \, . \qquad \text{(1.2)}$$

Nótese que para cualquier constante $a$

$$(a\Psi_1, \Psi_2) = a^*(\Psi_1, \Psi_2) \, , \qquad (\Psi_1, a\Psi_2) = a\,(\Psi_1, \Psi_2) \, . \qquad \text{(1.3)}$$

Con esta notación, la condición de hermiticidad se enuncia de forma más breve como

$$\hat{Q} \text{ es hermítico:} \qquad (\Psi_1, \hat{Q}\Psi_2) = (\hat{Q}\Psi_1, \Psi_2) \, . \qquad \text{(1.4)}$$

El valor esperado de $\hat{Q}$ se definió como

$$\langle Q \rangle_\Psi = \int dx\, \Psi^* \hat{Q}\Psi = (\Psi, \hat{Q}\Psi) \, . \qquad \text{(1.5)}$$

Para que esta fórmula tenga sentido, el estado $\Psi$ debe estar normalizado.

**Afirmación 1.** El valor esperado de un operador hermítico es real. Para demostrar esto, tomamos el complejo conjugado de la definición anterior. El complejo conjugado de la integral es la integral del complejo conjugado del integrando, por lo tanto

$$\langle Q \rangle_\Psi^* = \left( \int dx\, \Psi^* \hat{Q}\Psi \right)^* = \int dx\, \Psi (\hat{Q}\Psi)^* = \int dx\, (\hat{Q}\Psi)^* \Psi \, . \qquad \text{(1.6)}$$

Nótese que $\hat{Q}\Psi$ es una función de onda, así que tiene sentido tomar su complejo conjugado (nunca tenemos que pensar en conjugar $\hat{Q}$). Usando la hermiticidad del operador, lo trasladamos hacia $\Psi$ para obtener

$$\langle Q \rangle_\Psi^* = \int dx\, \Psi^* \hat{Q}\Psi = \langle Q \rangle_\Psi \, , \qquad \text{(1.7)}$$

demostrando así que el valor esperado es efectivamente real.

**Afirmación 2.** Los autovalores de un operador hermítico son reales. Supongamos que el operador $\hat{Q}$ tiene un autovalor $q_1$ asociado a una autofunción normalizada $\psi_1(x)$:

$$\hat{Q}\psi_1(x) = q_1 \psi_1(x) \, . \qquad \text{(1.8)}$$

Ahora calculemos el valor esperado de $\hat{Q}$ en el estado $\psi_1$:

$$\langle \hat{Q} \rangle_{\psi_1} = (\psi_1, \hat{Q}\psi_1) = (\psi_1, q_1 \psi_1) = q_1 (\psi_1, \psi_1) = q_1 \, . \qquad \text{(1.9)}$$

Por la afirmación 1, el valor esperado es real, y por tanto también lo es el autovalor $q_1$, como queríamos demostrar. Obsérvese el hecho interesante de que el valor esperado de $\hat{Q}$ en un autoestado está dado precisamente por el autovalor correspondiente.

Consideremos ahora el conjunto de autofunciones y autovalores del operador hermítico $\hat{Q}$:

$$\hat{Q}\, \psi_1(x) = q_1 \psi_1(x) \, , \qquad \text{(1.10)}$$

$$\hat{Q}\, \psi_2(x) = q_2 \psi_2(x) \, , \qquad \text{(1.11)}$$

$$\ldots$$

La lista puede ser finita o infinita.

**Afirmación 3.** Las autofunciones pueden organizarse de manera que satisfagan la ortonormalidad:

$$(\psi_i, \psi_j) = \int dx\, \psi_i^*(x)\psi_j(x) = \delta_{ij} \, . \qquad \text{(1.12)}$$

Para $i = j$, esto es simplemente cuestión de normalizar adecuadamente cada autofunción, lo cual podemos hacer fácilmente. La ecuación también establece que autofunciones distintas son ortogonales, es decir, tienen solapamiento nulo. Expliquemos ahora por qué esto es así para $i \neq j$ con $q_i \neq q_j$. En efecto, para ello evaluamos $(\psi_i, \hat{Q}\psi_j)$ de dos maneras distintas. Primero

$$(\psi_i, \hat{Q}\psi_j) = (\psi_i, q_j \psi_j) = q_j (\psi_i, \psi_j) \, , \qquad \text{(1.13)}$$

y segundo, usando la hermiticidad de $\hat{Q}$ y la realidad de los autovalores,

$$(\psi_i, \hat{Q}\psi_j) = (\hat{Q}\psi_i, \psi_j) = (q_i \psi_i, \psi_j) = q_i (\psi_i, \psi_j) \, . \qquad \text{(1.14)}$$

Igualando los lados derechos finales de las dos evaluaciones obtenemos

$$(q_j - q_i)(\psi_i, \psi_j) = 0 \, . \qquad \text{(1.15)}$$

Dado que los autovalores se supusieron distintos, esto demuestra que $(\psi_i, \psi_j) = 0$, como se afirmó. Esta no es aún una demostración completa de (1.12) porque es posible tener degeneraciones en el espectro, es decir, autofunciones distintas con el mismo autovalor. En ese caso, el argumento anterior no funciona. Entonces hay que demostrar que es posible elegir combinaciones lineales de las autofunciones degeneradas que sean mutuamente ortogonales (la ortogonalidad con las autofunciones fuera del espacio degenerado es automática). Esto se hace en 8.05.

**Afirmación 4.** Las autofunciones de $\hat{Q}$ forman un conjunto completo de funciones base. Cualquier $\Psi$ razonable puede escribirse como una superposición de autofunciones de $\hat{Q}$. (Este es el llamado teorema espectral, que se demuestra en 8.05 en el caso de dimensión finita.) Esto significa que

$$\Psi(x) = \alpha_1 \psi_1(x) + \alpha_2 \psi_2(x) + \cdots = \sum_i \alpha_i \psi_i(x) \, , \qquad \text{(1.16)}$$

con coeficientes calculables $\alpha_i$. En efecto, si conocemos las autofunciones tenemos que $\alpha_i$ se calcula haciendo la integral de $\psi_i^*$ contra $\Psi$:

$$\alpha_i = (\psi_i, \Psi) \, . \qquad \text{(1.17)}$$

Demostramos esto rápidamente haciendo la integral

$$\int dx\, \psi_i^*(x)\Psi(x) = \int dx\, \psi_i^*(x) \sum_j \alpha_j \psi_j(x) = \sum_j \alpha_j \int dx\, \psi_i^*(x)\psi_j(x) = \sum_j \alpha_j \delta_{ij} = \alpha_i \, . \qquad \text{(1.18)}$$

La condición de que $\Psi$ esté normalizada implica una condición sobre los coeficientes $\alpha_i$. Tenemos

$$\int dx\, \Psi^*(x)\Psi(x) = \int dx\, \sum_i \alpha_i^* \psi_i^*(x) \sum_j \alpha_j \psi_j(x)$$

$$= \sum_{i,j} \alpha_i^* \alpha_j \int dx\, \psi_i^*(x)\psi_j(x) \qquad \text{(1.19)}$$

$$= \sum_{i,j} \alpha_i^* \alpha_j \delta_{ij} = \sum_i \alpha_i^* \alpha_i \, ,$$

de modo que la normalización de $\Psi$ implica que

$$\sum_i |\alpha_i|^2 = 1 \, . \qquad \text{(1.20)}$$

Ya estamos en condiciones de enunciar el postulado de la medición. Esta es la forma en que entendemos que los operadores hermíticos representan observables y aprendemos las reglas que estos siguen.

**Postulado de la medición:** Si medimos el operador hermítico $\hat{Q}$ en el estado $\Psi$, los posibles resultados de la medición son los autovalores $q_1, q_2, \ldots$. La probabilidad $p_i$ de medir $q_i$ está dada por

$$p_i = |\alpha_i|^2 \, , \qquad \text{(1.21)}$$

donde $\Psi(x) = \sum_i \alpha_i \psi_i(x)$. Después del resultado $q_i$, el estado del sistema pasa a ser

$$\Psi(x) = \psi_i(x) \, . \qquad \text{(1.22)}$$

Esto se denomina el colapso de la función de onda.

El colapso de la función de onda implica que, inmediatamente después de la medición que arrojó $q_i$, una medición repetida de $\hat{Q}$ dará $q_i$ sin incertidumbre. Ocurre una pequeña sutileza si tenemos autoestados degenerados. Supongamos que la función de onda contiene una parte

$$\Psi = (\alpha_i \psi_i + \alpha_k \psi_k) + \ldots \qquad \text{(1.23)}$$

donde $\psi_i$ y $\psi_k$ tienen el mismo autovalor $q$, y los puntos suspensivos representan otros términos. Entonces, si medimos $q$, el estado tras la medición colapsa a la suma de esos dos términos

$$\Psi = \frac{\alpha_i \psi_i + \alpha_k \psi_k}{\sqrt{|\alpha_i|^2 + |\alpha_j|^2}} \, , \qquad \text{(1.24)}$$

con el denominador de raíz cuadrada incluido para proporcionar la normalización adecuada de $\Psi$. Como verificación de consistencia, nótese que las probabilidades $p_i$ de encontrar los diversos autovalores como resultados suman correctamente uno:

$$\sum_i p_i = \sum_i |\alpha_i|^2 = 1 \, , \qquad \text{(1.25)}$$

por la condición de normalización para $\Psi$ dada en (1.20). El postulado de la medición sigue la interpretación de Copenhague de la mecánica cuántica.

Nótese que el postulado de la medición usa la propiedad de que cualquier vector en un espacio vectorial puede escribirse como una suma de vectores distintos de un número infinito de maneras. Si vamos a medir $\hat{Q}_1$ expandimos el estado en autoestados de $\hat{Q}_1$; si vamos a medir $\hat{Q}_2$ expandimos el estado en autoestados de $\hat{Q}_2$, y así sucesivamente. Cada descomposición es adecuada para una medición particular. Cada descomposición revela las diversas probabilidades para los resultados del observable específico.

**Ejercicio.** Use la expansión $\Psi = \sum_i \alpha_i \psi_i$ para calcular el valor esperado $\langle Q \rangle$. Encontramos

$$\langle \hat{Q} \rangle = \int dx\, \sum_i \alpha_i^* \psi_i^*(x)\, \hat{Q} \sum_j \alpha_j \psi_j(x)$$

$$= \sum_{i,j} \alpha_i^* \alpha_j \int dx\, \psi_i^*(x) \hat{Q}\psi_j(x)$$

$$= \sum_{i,j} \alpha_i^* \alpha_j q_j \int dx\, \psi_i^*(x)\psi_j(x) \qquad \text{(1.26)}$$

$$= \sum_{i,j} \alpha_i^* \alpha_j q_j \delta_{ij} = \sum_i |\alpha_i|^2 q_i = \sum_i p_i q_i \, .$$

Esto concuerda con nuestras expectativas: el valor esperado de $\hat{Q}$ es la suma de los posibles resultados $q_i$ multiplicados por las probabilidades correspondientes $p_i$. Esta es una buena verificación de consistencia de nuestra definición de valores esperados.

**Ejemplo.** Partícula libre en el círculo $x \in [0, L]$.

Imaginamos que los puntos $x = 0$ y $x = L$ están identificados para formar un círculo de circunferencia $L$. Una función de onda $\Psi(x)$ en el círculo debe satisfacer la condición de periodicidad

$$\Psi(x + L) = \Psi(x) \, , \qquad \text{(1.27)}$$

Supongamos que en cierto instante fijo tenemos la función de onda

$$\Psi(x) = \sqrt{\frac{2}{L}}\, \frac{1}{\sqrt{3}} \sin\left(\frac{2\pi x}{L}\right) + \sqrt{\frac{2}{L}}\, \sqrt{\frac{2}{3}} \cos\left(\frac{6\pi x}{L}\right) \, . \qquad \text{(1.28)}$$

Esta función de onda satisface la condición de periodicidad, como debería comprobar. Queremos saber cuáles son los valores posibles del momento y sus probabilidades correspondientes.

Dada nuestra discusión, debemos encontrar el conjunto de autoestados de momento y reescribir la función de onda como una superposición de tales estados. Los autoestados de momento son exponenciales de la forma $e^{ikx}$. En el círculo ocurren dos cosas que no ocurren en el espacio libre. Primero, el momento estará cuantizado como consecuencia de la condición de periodicidad (1.27). Segundo, dado que el espacio aquí es de longitud finita, las funciones de onda de momento serán normalizables. Consideremos la condición de periodicidad aplicada a $e^{ikx}$. Necesitamos

$$e^{ikx} = e^{ik(x+L)} \;\rightarrow\; e^{ikL} = 1 \;\rightarrow\; kL = 2\pi m \, , \quad m \in \mathbb{Z} \, . \qquad \text{(1.29)}$$

Nótese que $m$ puede ser cualquier entero, positivo, negativo o cero. Escribimos entonces para los autoestados de momento, etiquetados por $m$

$$\psi_m(x) = N\, e^{\frac{2\pi i m x}{L}} \, , \qquad \text{(1.30)}$$

con $N$ una constante de normalización real. La condición de normalización da

$$1 = \int_0^L |\psi_m(x)|^2\, dx = N^2 \int_0^L dx = N^2 L \;\rightarrow\; N = \frac{1}{\sqrt{L}} \, . \qquad \text{(1.31)}$$

Por lo tanto, nuestros autoestados de momento son

$$\psi_m(x) = \frac{1}{\sqrt{L}}\, e^{\frac{2\pi i m x}{L}} \, , \qquad \text{(1.32)}$$

y estos son estados con momento $p_m$, que se calcula de la siguiente manera

$$\hat{p}\, \psi_m = \frac{\hbar}{i} \frac{\partial}{\partial x} \psi_m = \frac{2\pi m \hbar}{L} \psi_m \;\rightarrow\; p_m = \frac{2\pi m \hbar}{L} \, . \qquad \text{(1.33)}$$

Ahora que contamos con los autoestados de momento, debemos simplemente reescribir la función de onda (1.28) como una superposición de tales estados:

$$\Psi(x) = \sqrt{\frac{2}{3}}\, \frac{1}{2i}\, \frac{1}{\sqrt{L}}\left(e^{\frac{2\pi i x}{L}} - e^{-\frac{2\pi i x}{L}}\right) + \frac{2}{\sqrt{3}}\, \frac{1}{2}\, \frac{1}{\sqrt{L}}\left(e^{\frac{6\pi i x}{L}} + e^{-\frac{6\pi i x}{L}}\right) \, . \qquad \text{(1.34)}$$

Reconocemos entonces que tenemos

$$\Psi(x) = \sqrt{\frac{2}{3}}\, \frac{1}{2i}\, \psi_1(x) - \sqrt{\frac{2}{3}}\, \frac{1}{2i}\, \psi_{-1}(x) + \frac{1}{\sqrt{3}}\, \psi_3(x) + \frac{1}{\sqrt{3}}\, \psi_{-3}(x) \, . \qquad \text{(1.35)}$$

Este es nuestro resultado clave: la función de onda original escrita como una superposición de autoestados de momento $\psi_m(x)$. Ahora podemos dar los valores posibles $p$ del momento y sus probabilidades correspondientes $P$:

$$p = \frac{2\pi \hbar}{L} \, , \quad P = \left(\sqrt{\frac{2}{3}}\, \frac{1}{2i}\right)^2 = \frac{1}{6} \, ,$$

$$p = -\frac{2\pi \hbar}{L} \, , \quad P = \left(-\sqrt{\frac{2}{3}}\, \frac{1}{2i}\right)^2 = \frac{1}{6} \, ,$$

$$p = \frac{6\pi \hbar}{L} \, , \quad P = \left(\frac{1}{\sqrt{3}}\right)^2 = \frac{1}{3} \, , \qquad \text{(1.36)}$$

$$p = -\frac{6\pi \hbar}{L} \, , \quad P = \left(\frac{1}{\sqrt{3}}\right)^2 = \frac{1}{3} \, .$$

## 2. Incertidumbre

Para variables aleatorias, la incertidumbre es la desviación estándar: la raíz cuadrada del valor esperado del cuadrado de las desviaciones respecto al valor medio. Sea $Q$ una variable aleatoria que toma valores $Q_1, \ldots, Q_n$ con probabilidades $p_1, \ldots, p_n$, respectivamente. El valor esperado es

$$\overline{Q} = \sum_i p_i Q_i \, , \qquad \text{(2.37)}$$

y la varianza (el cuadrado de la desviación estándar) es

$$(\Delta Q)^2 \equiv \sum_i p_i (Q_i - \overline{Q})^2 \, . \qquad \text{(2.38)}$$

Esta definición deja claro que si $\Delta Q = 0$, entonces la variable aleatoria es constante: cada término en la suma anterior debe anularse, haciendo que $Q_i = \overline{Q}$ para todo $i$. Encontramos otra expresión útil expandiendo la definición anterior

$$(\Delta Q)^2 = \sum_i p_i Q_i^2 - 2 \sum_i p_i Q_i \overline{Q} + \sum_i p_i \overline{Q}^2$$

$$= \overline{Q^2} - 2\overline{Q}\,\overline{Q} + \overline{Q}^2 = \overline{Q^2} - \overline{Q}^2 \, , \qquad \text{(2.39)}$$

donde usamos $\sum_i p_i = 1$. Por lo tanto

$$(\Delta Q)^2 = \overline{Q^2} - \overline{Q}^2 \, . \qquad \text{(2.40)}$$

Dado que, por definición, $(\Delta Q)^2 \geq 0$, tenemos la interesante desigualdad

$$\overline{Q^2} \geq \overline{Q}^2 \, . \qquad \text{(2.41)}$$

Consideremos ahora el caso mecánico-cuántico. Ya hemos definido los valores esperados de operadores hermíticos, así que ahora podemos imitar la definición (2.40) y declarar que la incertidumbre $\Delta Q_\Psi$ de un operador en un estado $\Psi$ es un número real cuyo cuadrado está dado por

$$(\Delta Q)_\Psi^2 = \langle Q^2 \rangle_\Psi - (\langle Q \rangle_\Psi)^2 \, . \qquad \text{(2.42)}$$

A veces, por brevedad, omitimos la etiqueta del estado,

$$(\Delta Q)^2 = \langle Q^2 \rangle - \langle Q \rangle^2 \, . \qquad \text{(2.43)}$$

**Afirmación 1.** La incertidumbre también puede escribirse como el valor esperado del cuadrado de la diferencia entre el operador y su valor esperado:

$$(\Delta Q)^2 = \left\langle \left(\hat{Q} - \langle \hat{Q} \rangle\right)^2 \right\rangle \, . \qquad \text{(2.44)}$$

En efecto, expandiendo el lado derecho tenemos

$$\left\langle \hat{Q}^2 - 2\hat{Q}\langle \hat{Q} \rangle + \langle \hat{Q} \rangle^2 \right\rangle = \langle \hat{Q}^2 \rangle - 2\langle \hat{Q} \rangle \langle \hat{Q} \rangle + \langle \hat{Q} \rangle^2 = \langle \hat{Q}^2 \rangle - \langle \hat{Q} \rangle^2 \, . \qquad \text{(2.45)}$$

**Afirmación 2.** La incertidumbre puede escribirse como la integral del cuadrado de la norma de $(\hat{Q} - \langle Q \rangle)\Psi$:

$$(\Delta Q)^2 = \int_{-\infty}^{\infty} dx\, \left| \left(\hat{Q} - \langle Q \rangle\right) \Psi(x) \right|^2 \, . \qquad \text{(2.46)}$$

En efecto, para demostrar esto comenzamos con (2.44). Mediante una demostración muy similar, podemos mostrar que esto es equivalente a

$$(\Delta Q)^2 = \left\langle \left(\hat{Q} - \langle Q \rangle\right)^2 \right\rangle = \int dx\, \Psi^* \left(\hat{Q} - \langle Q \rangle\right)^2 \Psi \, . \qquad \text{(2.47)}$$

Usando la hermiticidad de $\hat{Q}$ y la realidad de $\langle \hat{Q} \rangle$, podemos trasladar uno de los dos factores para que actúe sobre $\Psi^*$:

$$(\Delta Q)^2 = \int dx\, \left[\left(\hat{Q} - \langle Q \rangle\right) \Psi\right]^* \left(\hat{Q} - \langle Q \rangle\right) \Psi = \int dx\, \left|\left(\hat{Q} - \langle Q \rangle\right)\Psi\right|^2 \, . \qquad \text{(2.48)}$$

Esto completa la demostración de la afirmación 2.

Si $\Delta Q = 0$, entonces, por la afirmación 2, debemos tener que para todo $x$:

$$(\hat{Q} - \langle Q \rangle)\Psi(x) = 0 \, , \quad \rightarrow \quad \hat{Q}\Psi(x) = \langle Q \rangle \Psi(x) \, . \qquad \text{(2.49)}$$

Vemos que $\Psi$ es un autoestado de $\hat{Q}$, lo cual efectivamente significa que no hay incertidumbre en la medición. Por supuesto, si $\Psi$ es un autoestado de $\hat{Q}$, entonces $\hat{Q}\Psi = \langle Q \rangle \Psi$ y la incertidumbre se anula. En resumen, hemos establecido la equivalencia

$$\Delta \hat{Q}_\Psi = 0 \iff \Psi \text{ es un autoestado de } \hat{Q} \, . \qquad \text{(2.50)}$$

*Andrew Turner transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare

https://ocw.mit.edu

8.04 Física Cuántica I

Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

# Apéndice: Lista de problemas 4 (Problem Set 4, 2016)

**Física Cuántica I (8.04), Primavera de 2016** **Tarea 4**

Departamento de Física del MIT — Entrega: viernes 4 de marzo de 2016, 12:00 del mediodía 25 de febrero de 2016

**Anuncios**

- Lectura recomendada: Griffiths, secciones 1.5, 1.6, 2.4.

## Problema 1. Ejercicios sobre paquetes que cambian de forma \[5 puntos\]

1.  Un protón libre está localizado dentro de $\Delta x = 10^{-10}$ m. Estime el tiempo $t_s$ que tarda el paquete en dispersarse apreciablemente. Repita el cálculo para un protón localizado dentro de 1 cm.

2.  Considere un paquete de ondas que satisface la relación $\Delta x \Delta p \sim \hbar$. Demuestre que la condición $\Delta p \ll p$ garantiza que el paquete no se dispersa apreciablemente en el tiempo que tarda en pasar por una posición fija.

## Problema 2. Corriente de probabilidad en tres dimensiones \[10 puntos\]

En la dispersión elástica de partículas en el espacio tridimensional, la función de onda toma la forma

$$\Psi(\mathbf{x}) = e^{ikz} + \frac{f(\theta)}{r} e^{ikr} \, , \quad \text{válida para } r \text{ grande} .$$

Se ha suprimido la dependencia temporal; se trata simplemente de una fase global dependiente del tiempo $e^{-iEt/\hbar}$ con $E = \hbar^2 k^2/(2m)$. No jugará ningún papel aquí.

El primer término representa las partículas incidentes, moviéndose en la dirección $+z$. El blanco se encuentra en el origen $r = 0$ y el segundo término representa la amplitud de las partículas que se mueven radialmente hacia afuera —las partículas dispersadas—. Esta amplitud depende de $\theta$ pero se supone independiente de $\varphi$; $f(\theta)$ es una función compleja de $\theta$ que contiene la información sobre la dispersión. Recuerde que $\theta$ es el ángulo polar y $z = r\cos\theta$.

Cuando se calcula la corriente de probabilidad $\mathbf{J}(\mathbf{x})$ asociada a $\Psi$, habrá una contribución $\mathbf{J}_1$ debida al primer término (la onda plana), una contribución $\mathbf{J}_2$ debida al segundo término (las ondas esféricas), y una contribución $\mathbf{J}_{12}$ debida a la interferencia entre el primer y el segundo término:

$$\mathbf{J}(\mathbf{x}) = \mathbf{J}_1(\mathbf{x}) + \mathbf{J}_2(\mathbf{x}) + \mathbf{J}_{12}(\mathbf{x}) \, .$$

1.  Calcule la corriente de probabilidad $\mathbf{J}_1$ y el flujo total de esta corriente sobre una esfera grande de radio $R$ centrada en el origen $r = 0$.

2.  Calcule la componente radial $\hat{r} \cdot \mathbf{J}_2$ de la corriente de probabilidad $\mathbf{J}_2$. Aquí $\hat{r}$ es el vector unitario en la dirección radial. Calcule el flujo de esta corriente sobre una esfera de radio $R$ centrada en el origen, en el límite $R \to \infty$. Su respuesta debe dejarse como una integral sobre el ángulo sólido $\int d\Omega$, o sobre $\int d\theta$, si lo prefiere.

3.  Calcule la componente radial del término de interferencia $\mathbf{J}_{12}$, pero quédese solo con la parte dominante en $1/r$ (es decir, ignore los términos en $1/r^2$). Demuestre que la respuesta puede escribirse en la forma

$$\hat{r} \cdot \mathbf{J}_{12} = \frac{\hbar k}{mr} \, \text{Im}\left[i (\ldots)\right] \, ,$$

donde $(\ldots)$ representa términos que su cálculo debe determinar. Estos términos dependen de $f(\theta)$, $\cos\theta$, y el producto $kr$ en exponenciales. Calcular el flujo de esta corriente sobre la esfera grande es delicado, así que lo dejaremos para más adelante (¡el resultado final es el llamado teorema óptico!).

## Problema 3. Evolución del paquete de ondas gaussiano \[15 puntos\]

Considere el paquete de ondas normalizado que representa el estado de una partícula de masa $m$ en $t = 0$:

$$\Psi_a(x, 0) = \frac{1}{(2\pi)^{1/4}\sqrt{a}} \exp\left(-\frac{x^2}{4a^2}\right) \, .$$

Aquí $a$ es un parámetro de longitud que representa la anchura del paquete en el instante inicial.

1.  Confirme que $\Psi_a(x, 0)$ está correctamente normalizada.

2.  Encuentre la representación de Fourier de $\Psi_a(x, 0)$, es decir, determine la función $\Phi_a(k)$ tal que

$$\Psi_a(x, 0) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi_a(k) e^{ikx} \, dk \, .$$

1.  Suponiendo que la partícula es libre, encuentre la función de onda $\Psi_a(x, t)$ para $t > 0$ arbitrario. La respuesta es un poco engorrosa, pero puede escribirse de manera más clara usando la constante de tiempo $\tau$ construida a partir de las constantes del problema:

$$\tau \equiv \frac{2ma^2}{\hbar} \, .$$

1.  En el instante inicial la densidad de probabilidad es

$$|\Psi_a(x, 0)|^2 = \frac{1}{\sqrt{2\pi}\, a} \exp\left(-\frac{x^2}{2a^2}\right) \equiv G(x; a) \, ,$$

donde hemos definido la gaussiana $G(x; a)$ con parámetro de anchura $a$. ¿Cuál es la densidad de probabilidad $|\Psi_a(x, t)|^2$ para $t > 0$? Exprese su respuesta en términos de la gaussiana $G$ con un parámetro de anchura dependiente del tiempo $a(t)$. Dé $a(t)$.

Integral útil: válida para constantes complejas $a$ y $b$, con parte real de $a$ positiva:

$$\int_{-\infty}^{\infty} e^{-ax^2 + bx} \, dx = \sqrt{\frac{\pi}{a}} \exp\left(\frac{b^2}{4a}\right) \, , \quad \text{cuando } \text{Re}(a) > 0 \, .$$

## Problema 4. Identidad de Parseval en 1D y 3D, y aplicación \[10 puntos\]

1.  Considere el par de Fourier $(\Psi(x), \Phi(p))$ relevante para las funciones de onda unidimensionales (1D) y el par de Fourier $(\Psi(\mathbf{x}), \Phi(\mathbf{p}))$ relevante para las funciones de onda tridimensionales (3D). Use las relaciones de Fourier y la forma integral de la función delta para demostrar las versiones 1D y 3D de la identidad de Parseval:[1]

$$\int_{-\infty}^{\infty} dx\, |\Psi(x)|^2 = \int_{-\infty}^{\infty} dp\, |\Phi(p)|^2 \, ,$$

$$\int d^3x\, |\Psi(\mathbf{x})|^2 = \int d^3p\, |\Phi(\mathbf{p})|^2 \, .$$

1.  En el átomo de hidrógeno, la función de onda del estado fundamental toma la forma $\Psi(\mathbf{x}) = N e^{-r/a_0}$, donde $r = |\mathbf{x}|$, $a_0$ es el radio de Bohr, y $N$ es una constante de normalización. Encuentre $N$. La transformada de Fourier (que no necesita derivar) toma la forma

$$\Phi(\mathbf{p}) = \frac{N'}{\left(1 + \dfrac{a_0^2 p^2}{\hbar^2}\right)^{2}} \, ,$$

para alguna constante $N'$ y con $p \equiv |\mathbf{p}|$. Encuentre $N'$ (puede usar un manipulador algebraico para hacer la integral). Calcule la probabilidad de que el electrón se encuentre con un momento cuya magnitud excede $\hbar/a_0$. (Escriba sus integrales explícitamente, pero puede evaluarlas con un ordenador). \[La distribución de momento fue medida mediante ionización de hidrógeno atómico por un haz de electrones de alta energía; véase Lohan, B. y Weigold, E. (1981) “Direct measurement of the Electron Momentum Probability Distribution in Atomic Hydrogen,” Phys. Lett. 86A, 139-141.\]

## Problema 5. Teorema de Ehrenfest \[10 puntos\]

Considere una partícula que se mueve en una dimensión con hamiltoniano $H$ dado por

$$H = \frac{p^2}{2m} + V(x) \, .$$

Demuestre que los valores esperados $\langle x \rangle$ y $\langle p \rangle$ son funciones dependientes del tiempo que satisfacen las siguientes ecuaciones diferenciales:

$$\frac{d}{dt}\langle x \rangle = \frac{1}{m}\langle p \rangle \, ,$$

$$\frac{d}{dt}\langle p \rangle = -\left\langle \frac{\partial V}{\partial x} \right\rangle \, .$$

## Problema 6. Incertidumbre del momento \[5 puntos\]

Demuestre que, en un paquete de ondas de partícula libre, la incertidumbre del momento $\Delta p$ no cambia en el tiempo.

## Problema 7. Encontrando el significado de la fase de la función de onda \[10 puntos\]

Suponga que $\psi_o(x)$ es una función de onda correctamente normalizada con $\langle x \rangle_{\psi_o} = x_o$ y $\langle p \rangle_{\psi_o} = p_o$, donde $x_o$ y $p_o$ son constantes. Defina el operador de impulso (boost) $\hat{B}_q$ como el operador que actúa sobre funciones arbitrarias de $x$ multiplicándolas por una fase dependiente de $q$:

$$\hat{B}_q f(x) = e^{iqx/\hbar} f(x) \, .$$

Aquí $q$ es un número real con las unidades apropiadas. Considere ahora una nueva función de onda obtenida aplicando el impulso a la función de onda inicial:

$$\psi_{\text{new}}(x) = \hat{B}_q \, \psi_o(x) \, .$$

1.  ¿Cuál es el valor esperado $\langle x \rangle_{\psi_{\text{new}}}$ en el estado dado por $\psi_{\text{new}}(x)$?

2.  ¿Cuál es el valor esperado $\langle p \rangle_{\psi_{\text{new}}}$ en el estado dado por $\psi_{\text{new}}(x)$?

3.  Con base en sus resultados, ¿cuál es el significado físico de añadir un factor global $e^{iqx/\hbar}$ a una función de onda?

4.  Calcule $[\hat{p}, \hat{B}_q]$ y $[\hat{x}, \hat{B}_q]$.

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*

[1] En matemáticas esto se llama teorema de Plancherel. El resultado de Parseval es el análogo para series de Fourier.
