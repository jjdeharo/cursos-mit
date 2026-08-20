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
