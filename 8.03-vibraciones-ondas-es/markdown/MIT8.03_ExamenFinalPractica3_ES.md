# Examen final de práctica 3

**Instituto Tecnológico de Massachusetts**

**Física 8.03**

**EXAMEN FINAL DE PRÁCTICA 3**

------------------------------------------------------------------------

## Hoja de fórmulas

### Ecuaciones de Maxwell en el vacío

$$\frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y} = -\frac{\partial B_z}{\partial t}\ ;\quad
\frac{\partial E_z}{\partial y} - \frac{\partial E_y}{\partial z} = -\frac{\partial B_x}{\partial t}\ ;\quad
\frac{\partial E_x}{\partial z} - \frac{\partial E_z}{\partial x} = -\frac{\partial B_y}{\partial t}$$

$$\frac{\partial B_y}{\partial x} - \frac{\partial B_x}{\partial y} = \mu_0\varepsilon_0\frac{\partial E_z}{\partial t}\ ;\quad
\frac{\partial B_z}{\partial y} - \frac{\partial B_y}{\partial z} = \mu_0\varepsilon_0\frac{\partial E_x}{\partial t}\ ;\quad
\frac{\partial B_x}{\partial z} - \frac{\partial B_z}{\partial x} = \mu_0\varepsilon_0\frac{\partial E_y}{\partial t}$$

$$\frac{\partial E_x}{\partial x} + \frac{\partial E_y}{\partial y} + \frac{\partial E_z}{\partial z} = 0\ ;\qquad
\frac{\partial B_x}{\partial x} + \frac{\partial B_y}{\partial y} + \frac{\partial B_z}{\partial z} = 0$$

### Ecuación de ondas para los campos electromagnéticos en el vacío

$$\frac{\partial^2 E_i}{\partial x^2} + \frac{\partial^2 E_i}{\partial y^2} + \frac{\partial^2 E_i}{\partial z^2} = \frac{1}{c^2}\frac{\partial^2 E_i}{\partial t^2} \quad \text{donde } i = x, y, z$$

$$\frac{\partial^2 B_i}{\partial x^2} + \frac{\partial^2 B_i}{\partial y^2} + \frac{\partial^2 B_i}{\partial z^2} = \frac{1}{c^2}\frac{\partial^2 B_i}{\partial t^2} \quad \text{donde } i = x, y, z$$

### Energía electromagnética por unidad de volumen y vector de Poynting

$$U_E = \frac{1}{2}\varepsilon_0\vec{E}^2 \qquad U_B = \frac{1}{2\mu_0}\vec{B}^2 \qquad \vec{S} = \frac{1}{\mu_0}\vec{E}\times\vec{B}$$

### Transmisión y reflexión

$$R = \frac{z_1 - z_2}{z_1 + z_2} \qquad\qquad T = \frac{2z_1}{z_1 + z_2}$$

### Velocidad de fase e impedancia

$$v = \sqrt{\frac{T}{\mu}}\ ,\qquad Z = \sqrt{T\mu} \quad \text{(cuerda)}$$

$$v = \sqrt{\frac{1}{LC}}\ ,\qquad Z = \sqrt{\frac{L}{C}} \quad \text{(línea de transmisión)}$$

### Campo eléctrico de una carga acelerada

$$\vec{E}(\vec{r}, t) = -\frac{q\,\vec{a}_\perp(t - r/c)}{4\pi\varepsilon_0 rc^2}$$

Potencia total emitida por la carga acelerada:

$$P(t) = \frac{q^2 a^2(t - r/c)}{6\pi\varepsilon_0 c^3}$$

### Transformada de Fourier

$$f(t) = \int_{-\infty}^{\infty} d\omega\, C(\omega)e^{-i\omega t} \qquad\qquad C(\omega) = \frac{1}{2\pi}\int_{-\infty}^{\infty} dt\, f(t)e^{i\omega t}$$

### Interferencia y difracción

Interferencia de dos fuentes de amplitudes $A_1$ y $A_2$ con una diferencia de fase relativa $\delta$:

$$\langle I\rangle \propto \left(A_1^2 + A_2^2 + 2A_1 A_2\cos\delta\right)$$

Interferencia de $N$ campos de igual amplitud con fases $\delta_{m+1} - \delta_m = \delta$:

$$\langle I\rangle = \langle I_0\rangle\left(\frac{\sin(N\delta/2)}{\sin(\delta/2)}\right)^2$$

Difracción por una rendija, donde $\beta$ es la diferencia de fase entre los rayos procedentes de los bordes y del centro de la rendija:

$$\langle I\rangle = \langle I_0\rangle\left(\frac{\sin\beta}{\beta}\right)^2$$

Razones de transmisión y reflexión del campo eléctrico, en magnitud y signo, para radiación que incide normalmente sobre una interfaz entre dieléctricos sin pérdidas de índices de refracción $n_1$ y $n_2$:

$$\frac{E_t}{E_i} = \frac{2n_1}{n_1 + n_2} \qquad\qquad \frac{E_r}{E_i} = \frac{n_1 - n_2}{n_1 + n_2}$$

Camino óptico entre $A$ y $B$:

$$\int_A^B n(x)\,dx$$

------------------------------------------------------------------------

## Problema 1 (30 puntos)

Responda a cada pregunta conceptual por separado. Cada una vale 5 puntos.

**a.** Luz polarizada circularmente de intensidad $I_0$ incide sobre un filtro que transmite una polarización lineal. ¿Cuál es la intensidad transmitida?

**b.** La electrónica utilizada en el acelerador LHC emplea pulsos cuadrados de 1 ns. ¿Cuál es el rango aproximado de frecuencias (ancho de banda) necesario para enviar tales pulsos?

**c.** La relación de dispersión de las ondas en aguas profundas es $\omega = \sqrt{gk}$. ¿Cuáles son las velocidades de fase y de grupo, y cuál es su magnitud relativa para un $k$ dado?

**d.** Se instala un láser verde ($\lambda = 500$ nm) en la Luna, que envía un haz de luz hacia la Tierra. ¿Cuál es el tamaño aproximado de la mancha de luz sobre la superficie terrestre si la anchura del haz láser en la Luna es de 1 metro y la distancia entre la Luna y la Tierra es de 380 000 km? El haz está limitado por difracción.

**e.** Está sentado erguido en la playa, junto a un lago, en un día soleado, con sus gafas de sol Polaroid puestas. Cuando se tumba de lado, mirando al lago, las gafas de sol no funcionan tan bien como cuando estaba sentado erguido. ¿Por qué no?

**f.** Suponga que luz monocromática incide sobre una red de difracción. ¿Qué le ocurre al patrón de máximos principales si la misma luz incide sobre una red que tiene más líneas por centímetro? ¿Qué le ocurre al patrón de máximos principales si incide luz de mayor longitud de onda sobre la misma red?

------------------------------------------------------------------------

## Problema 2 (30 puntos)

Una partícula de masa $m$ y carga $q$ está obligada a moverse sin fricción a lo largo de la dirección $\hat{x}$. La partícula es iluminada por una onda plana electromagnética viajera cuyo campo $B$ asociado es

$$\vec{B}_{\text{onda}}(\vec{r}, t) = B_0(\hat{y} + u\hat{z})\cos(kz - \omega t)$$

donde $B_0$ es constante y $u$ es un parámetro (constante) desconocido. La onda viaja por el espacio libre.

**a.** Calcule el parámetro $u$; justifique el cálculo.

**b.** Escriba el campo eléctrico de la onda incidente $\vec{E}_{\text{onda}}(\vec{r}, t)$.

**c.** Calcule la aceleración $\vec{a}(t)$ de la carga $q$. Puede despreciar cualquier pérdida de energía al calcular el movimiento de la carga.

**d.** Deduzca el campo eléctrico $\vec{E}_{\text{rad}}(\vec{r}, t)$ radiado por la carga hacia las tres posiciones siguientes. ¿Cuál es la polarización en esas tres localizaciones?

1.  $\vec{r} = r\hat{x}$

2.  $\vec{r} = r\hat{y}$

3.  $\vec{r} = r\hat{z}$

------------------------------------------------------------------------

## Problema 3 (40 puntos)

Una red sencilla que tiene 5 rendijas largas y estrechas está pegada sobre un bloque de vidrio de índice de refracción $n$. Una fuente monocromática de ondas planas ilumina la red desde el interior del vidrio. La longitud de onda de la luz en el vacío es $\lambda$. La figura 1 muestra una sección transversal de la red; la longitud de las rendijas es perpendicular al papel. La fuente está fuera del eje, con un ángulo $\theta$ respecto de la normal a la red, como se muestra (¡el signo de $\theta$ es importante!). Las rendijas son muy estrechas en comparación con su separación $d$ y con la longitud de onda de la luz que las ilumina, y la pantalla está muy lejos en comparación con $d$.

**a.** Considere primero el caso $\theta = 0$. Demuestre, mediante un diagrama sencillo, que la diferencia de fase $\delta$ entre los rayos procedentes de rendijas adyacentes, observados a gran distancia con un ángulo $\psi$ respecto del eje $z$, es $\delta = \dfrac{2\pi d}{\lambda}\sin\psi$.

**b.** Considere ahora un $\theta$ arbitrario. ¿Cuánto vale $\delta$?

**c.** Escriba una expresión, en términos de $d$, $\theta$, $\lambda$ y $\psi$, de la intensidad $I$ que se observará en la pantalla.

**d.** Esboce la intensidad $I$ en función de $\sin\psi$. Asegúrese de especificar la posición de los primeros máximos y mínimos de interferencia.

**e.** Considere ahora la misma red con las dos rendijas exteriores bloqueadas (rendijas 1 y 5). Escriba una expresión para la intensidad observada en la pantalla.

**f.** Haga el esbozo de la nueva intensidad frente a $\sin\psi$ y compárelo con el esbozo obtenido para las 5 rendijas. ¿Cuáles son las nuevas posiciones de los primeros máximos y mínimos? ¿Cómo ha cambiado la magnitud de los máximos?

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenFinalPractica3_ES/fig1.png)

Figura 1: red de difracción. Las 5 rendijas, numeradas de 1 a 5 y separadas una distancia $d$, están sobre la cara del bloque de vidrio; la luz llega desde el vidrio con un ángulo $\theta$ respecto de la normal y se observa en el vacío con un ángulo $\psi$ respecto del eje $z$.

------------------------------------------------------------------------

# Soluciones

*\[Nota de la traducción: las soluciones de este examen están manuscritas en el original y encabezadas «Solutions to Exam \#3, 8.03 Spring 2014». Se han transcrito y traducido íntegramente; los esbozos de los apartados 3.d y 3.f se describen con palabras.\]*

## Solución del problema 1

**a)**

$$I = \frac{I_0}{2}$$

$$\vec{E} = E_0\sin(kz - \omega t)\hat{x} + E_0\cos(kz - \omega t)\hat{y}$$

Después del polarizador solo permanece una componente, por ejemplo $E_0\sin(kz - \omega t)\hat{x}$.

**b)**

$$\Delta t\,\Delta\nu \simeq 1 \qquad \Rightarrow \qquad \Delta\nu = 10^9\ \text{Hz} \sim 1\ \text{GHz}$$

**c)**

$$v_p = \frac{\omega}{k} = \sqrt{\frac{g}{k}} \qquad v_g = \frac{d\omega}{dk} = \frac{\sqrt{g}}{2\sqrt{k}} \qquad \Rightarrow \qquad v_p = 2v_g$$

**d)** La anchura del pico de difracción es

$$\frac{\pi D}{\lambda}\sin\psi = \pi \qquad \Rightarrow \qquad \sin\psi = \frac{R}{L} = \frac{\lambda}{D}$$

$$R = \frac{\lambda}{D}\cdot L = \frac{5\cdot10^{-7}}{1}\cdot 3.8\cdot10^{8} = 200\ \text{m}$$

Se obtiene un radio más preciso analizando fuentes circulares:

$$r = \frac{1.22\,\lambda}{D}\cdot L \qquad \Rightarrow \qquad R = 230\ \text{m}$$

**e)** La luz reflejada en la superficie del agua está predominantemente polarizada con $\vec{E}$ paralelo a la superficie del agua. Las gafas Polaroid filtran esa polarización. Al girarlas 90°, dejamos pasar esa luz, anulando el efecto de bloqueo del sol.

**f)** Usando

$$\frac{\sin^2\left(\frac{N\delta}{2}\right)}{\sin^2\left(\frac{\delta}{2}\right)}$$

Si $N\cdot d = \text{constante}$ y $d$ es menor, la distancia entre máximos principales aumenta, y estos se vuelven más estrechos y más altos.

Si $\lambda$ es mayor, la distancia entre máximos principales aumenta.

## Solución del problema 2

**a)** Como $\vec{B} \perp \vec{k}$ y $\nabla\cdot\vec{B} = 0$:

$$\frac{\partial B_x}{\partial x} + \frac{\partial B_y}{\partial y} + \frac{\partial B_z}{\partial z} = 0$$

$$0 + \underbrace{\frac{\partial}{\partial y}\left(B_0\cos(kz - \omega t)\right)}_{=\,0} + u\underbrace{\frac{\partial}{\partial z}\left(B_0\cos(kz - \omega t)\right)}_{\neq\,0} = 0$$

$$\Rightarrow \quad u = 0$$

$$\vec{B}(\vec{r}, t) = B_0\,\hat{y}\cos(kz - \omega t)$$

**b)**

$$\vec{E}(\vec{r}, t) = B_0\,c\,\hat{x}\cos(kz - \omega t)$$

**c)**

$$\vec{F} = q\left(\vec{E} + \vec{v}\times\vec{B}\right) \qquad \vec{a} = \frac{\vec{F}}{m}$$

La fuerza debida al campo $\vec{B}$ puede despreciarse, puesto que $q$ está obligada a moverse a lo largo de $\hat{x}$. Entonces

$$\vec{a} = \frac{q\vec{E}}{m} = \frac{qB_0 c}{m}\,\hat{x}\cos(\omega t) \qquad \text{ya que } z = 0$$

**d)**

$$\vec{E}_{\text{rad}} = -\frac{q\,\vec{a}_\perp(t - r/c)}{4\pi\varepsilon_0 rc^2}$$

**(1)** $\vec{r} = r\hat{x}$ $\Rightarrow$ $\vec{E}_{\text{rad}} = 0$, ya que $\vec{a}$ es paralela a $\hat{x}$ y no tiene componente transversal a $\vec{r}$.

**(2)** $\vec{r} = r\hat{y}$ $\Rightarrow$

$$\vec{E}_{\text{rad}} = -\frac{q^2 B_0 c\cos\left(\omega\left(t - \frac{r}{c}\right)\right)}{4\pi\varepsilon_0 rc^2 m}\,\hat{x}$$

Polarización lineal.

**(3)** $\vec{r} = r\hat{z}$: igual que en (2).

## Solución del problema 3

**a)** La diferencia de camino entre rayos de rendijas adyacentes es $\Delta\ell = d\sin\psi$, de modo que

$$\delta_{\text{después}} = \Delta\ell\cdot k = \frac{2\pi}{\lambda}\,d\sin\psi$$

**b)** La onda incidente introduce un desfase adicional. Hemos definido $\theta$ y $\psi$ de modo que ambos desfases se cancelan. Además, la presencia del vidrio cambia la magnitud del desfase:

$$\Delta\delta_{\text{antes}} = -\frac{2\pi d}{\lambda'}\sin\theta = -\frac{2\pi d\,n}{\lambda_0}\sin\theta \qquad \text{con } \lambda' = \frac{1}{n}\lambda_0$$

$$\delta_{\text{total}} = \frac{2\pi d}{\lambda_0}\left(\sin\psi - n\sin\theta\right)$$

**c)**

$$I = I_0\,\frac{\sin^2\left(\frac{5\pi d}{\lambda_0}\left(\sin\psi - n\sin\theta\right)\right)}{\sin^2\left(\frac{\pi d}{\lambda_0}\left(\sin\psi - n\sin\theta\right)\right)}$$

donde $I_0$ es la intensidad de una sola rendija.

**d)** El máximo principal está en $\delta = 0$, es decir, en $\sin\psi = n\sin\theta$, y alcanza el valor $25I_0$.

El primer mínimo está en $\dfrac{5\delta}{2} = \pi$, es decir, en

$$\sin\psi = n\sin\theta + \frac{\lambda}{5d}$$

*(Esbozo: máximos principales altos y estrechos de altura $25I_0$, centrados en $\sin\psi = n\sin\theta$ y repetidos periódicamente, con tres lóbulos secundarios pequeños entre cada par de máximos principales.)*

**e)** Con las rendijas exteriores bloqueadas, $N \to 3$:

$$I = I_0\,\frac{\sin^2\left(\frac{3\pi d}{\lambda_0}\left(\sin\psi - n\sin\theta\right)\right)}{\sin^2\left(\frac{\pi d}{\lambda_0}\left(\sin\psi - n\sin\theta\right)\right)}$$

con un máximo de $9I_0$.

**f)** El máximo principal sigue estando en $\delta = 0$ y el primer mínimo pasa a estar en $\dfrac{3\delta}{2} = \pi$, es decir, en

$$\sin\psi = n\sin\theta + \frac{\lambda}{3d}$$

Comparación:

- Valor máximo: $25I_0$ frente a $9I_0$.
- Posición de los máximos principales: la misma.
- Primer mínimo: $+\dfrac{\lambda}{5d}$ frente a $+\dfrac{\lambda}{3d}$; queda más lejos con 3 rendijas.
- Los máximos principales son más anchos con 3 rendijas.

*(Esbozo: el patrón de 3 rendijas presenta máximos principales más bajos y más anchos, con un solo lóbulo secundario entre cada par de máximos principales.)*

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*
