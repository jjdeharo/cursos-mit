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
