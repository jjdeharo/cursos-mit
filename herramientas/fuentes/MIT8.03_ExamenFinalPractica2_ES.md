---
title: "Examen final de práctica 2 (con soluciones) — 8.03SC Física III: Vibraciones y Ondas"
author: "Yen-Jie Lee (traducción al español)"
lang: es
---

# Examen final de práctica 2

**Instituto Tecnológico de Massachusetts**

**Física 8.03**

**EXAMEN FINAL DE PRÁCTICA 2**

---

## Hoja de fórmulas

### Muelles y masas

$$m\frac{d^2}{dt^2}x(t) + b\frac{d}{dt}x(t) + kx(t) = F(t)$$

Ecuación diferencial más general con fuerza impulsora armónica:

$$\frac{d^2}{dt^2}x(t) + \Gamma\frac{d}{dt}x(t) + \omega_0^2 x(t) = \frac{F_0}{m}\cos(\omega_d t)$$

Soluciones estacionarias:

$$x_s(t) = A\cos(\omega_d t - \delta)$$

donde

$$A = \frac{\dfrac{F_0}{m}}{\sqrt{(\omega_0^2 - \omega_d^2)^2 + \omega_d^2\Gamma^2}} \qquad\text{y}\qquad \tan\delta = \frac{\Gamma\omega_d}{\omega_0^2 - \omega_d^2}$$

### Soluciones generales

Para $\Gamma = 0$ (sistema no amortiguado):

$$x(t) = R\cos(\omega_0 t + \theta) + x_s(t)$$

Para $\Gamma < 2\omega_0$ (sistema subamortiguado):

$$x(t) = Re^{-\frac{\Gamma}{2}t}\cos\left(\sqrt{\omega_0^2 - \frac{\Gamma^2}{4}}\,t + \theta\right) + x_s(t)$$

Para $\Gamma = 2\omega_0$ (sistema críticamente amortiguado):

$$x(t) = (R_1 + R_2 t)e^{-\frac{\Gamma}{2}t} + x_s(t)$$

Para $\Gamma > 2\omega_0$ (sistema sobreamortiguado):

$$x(t) = R_1 e^{\left(-\frac{\Gamma}{2} + \sqrt{\frac{\Gamma^2}{4} - \omega_0^2}\right)t} + R_2 e^{\left(-\frac{\Gamma}{2} - \sqrt{\frac{\Gamma^2}{4} - \omega_0^2}\right)t} + x_s(t)$$

donde $R$, $\theta$, $R_1$ y $R_2$ son coeficientes desconocidos.

### Osciladores acoplados

$$F_j = -\sum_{k=1}^{n} K_{jk}\,x_k$$

Ejemplos para $n = 2$:

$$\mathcal{X}(t) = \begin{pmatrix} x_1(t) \\ x_2(t) \end{pmatrix}
\qquad
K = \begin{pmatrix} K_{11} & K_{12} \\ K_{21} & K_{22} \end{pmatrix}
\qquad
M = \begin{pmatrix} m_1 & 0 \\ 0 & m_2 \end{pmatrix}$$

$$\frac{d^2}{dt^2}\mathcal{X}(t) = -M^{-1}K\,\mathcal{X}(t) \qquad \mathcal{Z}(t) = Ae^{-i\omega t} \qquad (M^{-1}K - \omega^2 I)A = 0$$

Para obtener las frecuencias de los modos normales, resuelva $\det(M^{-1}K - \omega^2 I) = 0$.

Para $n = 2$:

$$\det\begin{pmatrix} M_{11} & M_{12} \\ M_{21} & M_{22} \end{pmatrix} = M_{11}M_{22} - M_{12}M_{21}$$

Si el sistema está impulsado por una fuerza:

$$F(t) = F_0 e^{-i\omega_d t} \qquad W(t) = C(\omega_d)e^{-i\omega_d t} \qquad C(\omega_d) = \begin{pmatrix} c_1(\omega_d) \\ c_2(\omega_d) \end{pmatrix}$$

$$(M^{-1}K - \omega_d^2 I)\,C(\omega_d) = F_0$$

Matriz de simetría de reflexión:

$$S = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$$

### Integrales útiles con senos y cosenos

$$\frac{2}{L}\int_0^L \sin\left(\frac{n\pi x}{L}\right)\sin\left(\frac{m\pi x}{L}\right)dx = \begin{cases} 1, & \text{si } n = m \\ 0, & \text{en caso contrario} \end{cases}$$

$$\frac{2}{L}\int_0^L \cos\left(\frac{n\pi x}{L}\right)\cos\left(\frac{m\pi x}{L}\right)dx = \begin{cases} 1, & \text{si } n = m \\ 0, & \text{en caso contrario} \end{cases}$$

$$\int x\sin(x)\,dx = \sin(x) - x\cos(x) + C \qquad \int x\cos(x)\,dx = \cos(x) + x\sin(x) + C$$

### Ecuaciones de Maxwell en el vacío

$$\frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y} = -\frac{\partial B_z}{\partial t}\ ;\quad
\frac{\partial E_z}{\partial y} - \frac{\partial E_y}{\partial z} = -\frac{\partial B_x}{\partial t}\ ;\quad
\frac{\partial E_x}{\partial z} - \frac{\partial E_z}{\partial x} = -\frac{\partial B_y}{\partial t}$$

$$\frac{\partial E_x}{\partial x} + \frac{\partial E_y}{\partial y} + \frac{\partial E_z}{\partial z} = 0\ ;\qquad
\frac{\partial B_x}{\partial x} + \frac{\partial B_y}{\partial y} + \frac{\partial B_z}{\partial z} = 0$$

Fuerza de Lorentz:

$$\vec{F} = q(\vec{E} + \vec{v}\times\vec{B})$$

### Ecuación de ondas para los campos electromagnéticos en el vacío

$$\frac{\partial^2 E_i}{\partial x^2} + \frac{\partial^2 E_i}{\partial y^2} + \frac{\partial^2 E_i}{\partial z^2} = \frac{1}{c^2}\frac{\partial^2 E_i}{\partial t^2} \quad \text{donde } i = x, y, z$$

$$\frac{\partial^2 B_i}{\partial x^2} + \frac{\partial^2 B_i}{\partial y^2} + \frac{\partial^2 B_i}{\partial z^2} = \frac{1}{c^2}\frac{\partial^2 B_i}{\partial t^2} \quad \text{donde } i = x, y, z$$

Para ondas planas electromagnéticas en el vacío:

$$\vec{B}(\vec{r}, t) = \frac{1}{c}\,\hat{k} \times \vec{E}(\vec{r}, t) \qquad\qquad \vec{E}(\vec{r}, t) = c\,\vec{B}(\vec{r}, t) \times \hat{k}$$

### Densidad lineal de energía en una cuerda

$$\frac{dK}{dx} = \frac{1}{2}\rho_L\left(\frac{\partial y}{\partial t}\right)^2 \qquad\qquad \frac{dU}{dx} = \frac{1}{2}T\left(\frac{\partial y}{\partial x}\right)^2$$

### Transmisión, reflexión, velocidad de fase e impedancia

$$R = \frac{z_1 - z_2}{z_2 + z_1} \qquad\qquad T = \frac{2z_1}{z_2 + z_1}$$

$$v = \sqrt{\frac{T}{\rho_L}} \qquad Z = \sqrt{T\rho_L} \quad \text{(cuerda)}$$

$$v = \sqrt{\frac{1}{LC}} \qquad Z = \sqrt{\frac{L}{C}} \quad \text{(línea de transmisión)}$$

Ley de Snell: $n_1\sin\theta_1 = n_2\sin\theta_2$

### Transformada de Fourier y función delta

$$f(t) = \int_{-\infty}^{\infty} d\omega\, C(\omega)e^{-i\omega t} \qquad C(\omega) = \frac{1}{2\pi}\int_{-\infty}^{\infty} dt\, f(t)e^{i\omega t}$$

$$\frac{1}{2\pi}\int_{-\infty}^{\infty} e^{i(\omega - \omega')t}\,dt = \delta(\omega - \omega') \qquad \int_{-\infty}^{\infty} \delta(x)\,dx = 1 \qquad \int_{-\infty}^{\infty} \delta(x - a)f(x)\,dx = f(a)$$

### Campo eléctrico y magnético de una carga acelerada

$$\vec{E}(\vec{r}, t) = -\frac{q\,\vec{a}_\perp(t - |r|/c)}{4\pi\varepsilon_0 rc^2} \qquad\qquad \vec{B}(\vec{r}, t) = \frac{\hat{k}\times\vec{E}}{c}$$

Potencia total emitida por la carga acelerada:

$$P(t) = \frac{q^2 a^2(t - r/c)}{6\pi\varepsilon_0 c^3}$$

### Interferencia y difracción

Interferencia de dos fuentes de amplitudes $A_1$ y $A_2$ con una diferencia de fase relativa $\delta$:

$$\langle I\rangle \propto \left(A_1^2 + A_2^2 + 2A_1 A_2\cos\delta\right)$$

Interferencia de $N$ campos de igual amplitud con fases $\delta_{m+1} - \delta_m = \delta$:

$$\langle I\rangle = \langle I_0\rangle\left(\frac{\sin(N\delta/2)}{\sin(\delta/2)}\right)^2$$

Difracción por una rendija, donde $\beta$ es la diferencia de fase entre los rayos procedentes de los bordes y del centro de la rendija:

$$\langle I\rangle = \langle I_0\rangle\left(\frac{\sin\beta}{\beta}\right)^2$$

Criterio de Rayleigh para la resolución: el pico de difracción de una imagen cae sobre el primer mínimo del patrón de difracción de la segunda imagen.

Razones de transmisión y reflexión del campo eléctrico, en magnitud y signo, para radiación que incide normalmente sobre una interfaz entre dieléctricos sin pérdidas de índices de refracción $n_1$ y $n_2$:

$$\frac{E_t}{E_i} = \frac{2n_1}{n_1 + n_2} \qquad\qquad \frac{E_r}{E_i} = \frac{n_1 - n_2}{n_1 + n_2}$$

### Ecuación de Schrödinger

$$i\hbar\frac{\partial}{\partial t}\psi(x, t) = \left[-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x, t)\right]\psi(x, t)$$

donde $V$ es la energía potencial, $m$ es la masa de la partícula y $\psi$ es la función de onda.

---

## Problema 1 (15 puntos)

Responda a cada pregunta corta por separado.

**1.1.** La energía potencial de una partícula de masa $m$, obligada a moverse a lo largo del eje $x$, viene dada por

$$U(x) = A\left(1 - \cos(\alpha x)\right)$$

donde $A$ y $\alpha$ son constantes, ambas $> 0$. Si la partícula se desplaza del equilibrio, ¿cuál será su periodo de oscilación de pequeña amplitud?

**1.2.** Considere el siguiente registro de la posición de un oscilador forzado en función del tiempo (figura 1). Puede suponer que la fuerza impulsora es una onda sinusoidal y que su amplitud no cambia con el tiempo. ¿Cuál o cuáles de las siguientes descripciones son verdaderas? (Seleccione todas las que correspondan.)

(a) La frecuencia impulsora es mayor que la frecuencia de resonancia natural del sistema.

(b) La frecuencia impulsora es menor que la frecuencia de resonancia natural del sistema.

(c) No hay amortiguamiento.

(d) El sistema está sobreamortiguado.

(e) El sistema está críticamente amortiguado.

(f) El sistema está subamortiguado.

**1.3.** La electrónica utilizada en el Gran Colisionador de Hadrones emplea pulsos cuadrados de 1 nanosegundo. ¿Cuál es el rango aproximado de frecuencias (ancho de banda) necesario para enviar pulsos tan cortos?

**1.4.** En la figura 2 se muestra un experimento con electrones. La fuente se calentó hasta que empezó a emitir electrones. ¿Cuál o cuáles de las siguientes descripciones son verdaderas? (Seleccione todas las que correspondan.)

(a) Cuando la temperatura de la fuente es alta, de modo que la tasa de emisión de electrones es alta, el detector registrará un patrón de interferencia.

(b) Cuando la temperatura de la fuente es alta, de modo que la tasa de emisión de electrones es alta, el detector no registrará ningún patrón de interferencia.

(c) Cuando la temperatura de la fuente es baja, de modo que la fuente emite un electrón cada vez, no habrá patrón de interferencia.

(d) Cuando la temperatura de la fuente es baja, de modo que la fuente emite un electrón cada vez, habrá patrón de interferencia.

**1.5.** Una membrana elástica está tensada sobre un marco rectangular, como se muestra en la figura 3. La velocidad de fase de propagación de las ondas en esta membrana es $v$. ¿Cuál es la frecuencia angular del modo normal más bajo que puede excitarse en la membrana?

*(Figura 1: registro de un oscilador forzado. Figura 2: experimento con electrones. Figura 3: membrana elástica, tensada sobre un marco cuadrado de lado $L$.)*

---

## Problema 2 (15 puntos)

Dos pequeñas cuentas con masa, de masas iguales $m_1 = m_2 = m$, están sobre una cuerda tensa sin masa de longitud $5L$ (véase la figura 4). La tensión de la cuerda $T$ es grande, de modo que se pueden despreciar los efectos de la gravedad. Los tramos de cuerda miden $2L$, $L$ y $2L$.

**a.** Escriba las ecuaciones del movimiento de las dos cuentas para oscilaciones de pequeña amplitud a lo largo de $y$ y escriba la matriz $M^{-1}K$ correspondiente a este sistema.

**b.** Halle las formas y las frecuencias angulares de los modos normales del sistema. Puede simplificar la tarea usando argumentos de simetría. Explique su razonamiento.

**c.** Inicialmente, en $t = 0$, ambas masas están en reposo, con $m_1$ en la posición de equilibrio y $m_2$ desplazada del equilibrio una distancia $A$. Escriba una expresión para el desplazamiento $y_1(t)$ de la masa que inicialmente está en la posición de equilibrio.

*(Figura 4: dos cuentas sobre una cuerda, con tramos de longitudes $2L$, $L$ y $2L$.)*

---

## Problema 3 (20 puntos)

La figura 5 representa un tubo lleno de gas que está abierto a un depósito de gas en $x = 0$ y cerrado en $x = L$. La velocidad del sonido en el gas es $v$. Se establece en el gas una ligera perturbación de presión que después se suelta desde el reposo en $t = 0$. La perturbación está centrada en $L/2$, abarca una anchura $L/3$ y tiene una presión $P_1$ ligeramente mayor que la presión ambiente $P_0$.

**a.** ¿Cuáles son las condiciones de contorno en $x = 0$ y en $x = L$?

**b.** Exprese la perturbación de presión $P(x, t)$ para $t > 0$ como una suma de modos normales. Dé expresiones explícitas para las variaciones espacial y temporal de cada modo normal, su número de onda y su frecuencia angular. Deje las amplitudes asociadas como parámetros por determinar.

**c.** Calcule la amplitud del $n$-ésimo modo normal.

**d.** Dibuje un esbozo (similar a la gráfica anterior) de la presión en el tubo en el instante $t = 2L/v$. [Pista: puede hacerse razonando con cuidado, en lugar de calcular explícitamente $P(x, t)$.]

*(Figura 5: onda de presión en un tubo. Sobre el tramo de $0$ a $L$ se levanta un pulso de presión de anchura $L/3$ centrado en $L/2$, que alcanza el valor $P_1$ por encima de la presión ambiente $P_0$.)*

---

## Problema 4 (15 puntos)

Una carga puntual $+q$ se ha estado moviendo con velocidad constante $w$ a lo largo de una línea recta hasta el instante $t = t_0$. En el CORTO intervalo de tiempo de $t = t_0$ a $t = t_0 + \Delta t$, una fuerza perpendicular a la trayectoria cambia la dirección sin cambiar el módulo de la velocidad. Después del instante $t = t_0 + \Delta t$, la carga vuelve a moverse con velocidad $w$ a lo largo de una línea recta que forma un pequeño ángulo $\Delta\alpha$ con la trayectoria inicial, como se muestra en la figura 6. La radiación emitida por la carga se observa desde los puntos muy lejanos $P_1$ y $P_2$. Los dos puntos de observación están situados en el plano de la trayectoria.

**a.** ¿Cuál es la aceleración media de la carga puntual en términos de las magnitudes dadas?

**b.** ¿Cuál es la dirección del campo eléctrico causado por la aceleración en el punto lejano $P_1$?

**c.** ¿En qué dirección es más intensa la radiación de la carga acelerada?

**d.** ¿Dónde es menos intensa?

**e.** El punto $P_2$ está al doble de distancia del codo de la trayectoria que $P_1$. ¿En qué fracción disminuye la amplitud de la perturbación electromagnética al pasar el pulso de radiación de $P_1$ a $P_2$?

**f.** ¿Cuál es la energía total radiada por la carga?

Haga esbozos cuidadosos al responder a los apartados b), c) y d).

*(Figura 6: carga radiante. La trayectoria se quiebra un ángulo $\Delta\alpha$; los puntos de observación $P_1$ y $P_2$ están en el plano de la trayectoria, con $P_2$ al doble de distancia que $P_1$.)*

---

## Problema 5 (15 puntos)

Considere un sistema de tres polarizadores lineales ideales dispuestos a lo largo de un banco óptico, como se muestra en la figura 7. Los dos polarizadores exteriores tienen sus ejes fáciles perpendiculares entre sí. El polarizador A transmite solo luz polarizada horizontalmente, mientras que el polarizador C transmite solo luz polarizada verticalmente. El polarizador B tiene su eje fácil formando un ángulo $\theta$ con el eje horizontal $x$. Suponga que la luz que incide sobre el polarizador A por la izquierda no está polarizada y que su intensidad es $I_0$.

**a.** Halle la intensidad y la polarización de la luz transmitida a través del polarizador A, $I_A$.

**b.** Halle la intensidad y la polarización de la luz transmitida a través del polarizador B, $I_B$, en función de $I_0$ y $\theta$, y represéntela gráficamente en función de $\theta$.

**c.** Halle la intensidad de la luz transmitida a través del polarizador C, $I_C$, en función de $I_0$ y $\theta$, y represéntela gráficamente en función de $\theta$.

*(Figura 7: tres polarizadores lineales A, B y C, con los ejes fáciles horizontal, a un ángulo $\theta$ y vertical, respectivamente.)*

---

## Problema 6 (20 puntos)

Una fuente monocromática de ondas planas de longitud de onda $\lambda$ ilumina una red de cuatro rendijas. La figura 8 muestra una sección transversal de la red; la longitud de las rendijas es perpendicular al papel. La pantalla está muy lejos de las rendijas ($d \ll z$).

**a.** Escriba una expresión, en términos de $d$, $\lambda$ y $\psi$, de la intensidad $I$ que se observará en la pantalla. Suponga en principio que las rendijas son muy estrechas en comparación con su separación ($D \ll d$). Suponga que la intensidad de la luz debida a una sola rendija es $I_0$.

**b.** Haga un esbozo de la intensidad en función de $\sin\psi$ para la red de cuatro rendijas. Asegúrese de especificar las posiciones de los máximos principales y de los mínimos de interferencia.

**c.** Considere ahora la misma red con las dos rendijas INTERIORES bloqueadas. Escriba una expresión de la intensidad observada en la pantalla y haga el esbozo de la nueva intensidad frente a $\sin\psi$.

**d.** Compárelo con el esbozo obtenido para las cuatro rendijas. ¿Cuáles son las nuevas posiciones de los máximos y los mínimos? ¿Qué máximos principales están en la misma posición en las dos configuraciones? ¿Cómo ha cambiado la magnitud de los máximos principales? Suponga que las intensidades individuales de las rendijas abiertas son las mismas en ambos casos.

**e.** Considere ahora la misma red de cuatro rendijas con todas las rendijas descubiertas, pero esta vez las anchuras $D$ de las rendijas individuales no pueden despreciarse. La razón entre la distancia entre los centros de las rendijas y la anchura de la rendija es ahora $d/D = 5$. El efecto de la difracción por una sola rendija hará que algunos de los máximos principales obtenidos en el apartado a) desaparezcan ($I = 0$). ¿Cuál es el orden de interferencia más bajo para el que los efectos de difracción anulan de este modo el máximo principal?

*(Figura 8: red de cuatro rendijas, de separación $d$ entre centros y anchura $D$, con la pantalla a una distancia $z$.)*

---

# Soluciones

## Solución del problema 1

**1.1** (3 puntos) La energía potencial

$$U(x) = A\left(1 - \cos(\alpha x)\right) \tag{1}$$

El mínimo está en los puntos

$$x = \frac{2n\pi}{\alpha}\ ,\qquad n \in \mathbb{Z} \tag{2}$$

*[Nota de la traducción: el PDF original escribe $x = 2n\pi$, omitiendo el factor $1/\alpha$; los mínimos de $U$ están donde $\cos(\alpha x) = 1$, es decir, en $\alpha x = 2n\pi$.]*

Por ejemplo, consideramos $x = 0$:

$$\left.\frac{d^2U}{dx^2}\right|_0 = A\alpha^2\cos(\alpha x)\big|_0 = A\alpha^2 \tag{3}$$

Esto es equivalente al parámetro $k$ del movimiento armónico simple de un muelle: $U = \frac{1}{2}kx^2$. Por tanto obtenemos el periodo

$$T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{m}{k}} = 2\pi\sqrt{\frac{m}{A\alpha^2}} \tag{4}$$

**1.2** (3 puntos) El comportamiento transitorio de un sistema de oscilación forzada se describe como la suma del movimiento estacionario y del movimiento libre que decae por el amortiguamiento.

El periodo del movimiento estacionario es mucho más largo que el periodo del movimiento libre. Además, la forma global del movimiento transitorio corresponde a un movimiento subamortiguado que decae. Por tanto, la respuesta es **b, f**.

**1.3** (3 puntos) La relación entre el ancho de banda $\Delta f$ y la resolución temporal $\Delta t$ es

$$\Delta t\,\Delta f \sim 1 \tag{5}$$

Por tanto, el ancho de banda es

$$\Delta f \sim 10^9\ \text{Hz} \tag{6}$$

**1.4** (3 puntos) Por débil que sea la fuente de electrones, siempre aparece un patrón de interferencia en la pantalla al cabo de mucho tiempo. La respuesta es **a, d**.

**1.5** (3 puntos) La ecuación de ondas en 2D es

$$\frac{\partial^2\psi}{\partial t^2} = v^2\left(\frac{\partial^2\psi}{\partial x^2} + \frac{\partial^2\psi}{\partial y^2}\right) \tag{7}$$

El modo más bajo que respeta la condición de contorno dada es

$$\psi_{1,1}(x, y, t) \sim \sin\left(\frac{\pi x}{L}\right)\sin\left(\frac{\pi y}{L}\right)\cos(\omega t) \tag{8}$$

Sustituyéndolo en la ecuación de ondas, obtenemos

$$\omega = \sqrt{2}\,\frac{v\pi}{L} \tag{9}$$

## Solución del problema 2

**a)** (5 puntos) La ecuación del movimiento de $m_1$ es

$$m\ddot{y}_1 = -\frac{T}{2L}y_1 - \frac{T}{L}(y_1 - y_2) = -\frac{3T}{2L}y_1 + \frac{T}{L}y_2 \tag{10}$$

Análogamente, la ecuación del movimiento de $m_2$ es

$$m\ddot{y}_2 = -\frac{T}{2L}y_2 - \frac{T}{L}(y_2 - y_1) = -\frac{3T}{2L}y_2 + \frac{T}{L}y_1 \tag{11}$$

Por tanto, los elementos de la matriz $K$ son

$$K_{11} = K_{22} = \frac{3T}{2L}\ ,\qquad K_{12} = K_{21} = -\frac{T}{L} \tag{12}$$

Y la matriz $M^{-1}K$ es

$$M^{-1}K = \begin{pmatrix} \frac{3T}{2mL} & -\frac{T}{mL} \\ -\frac{T}{mL} & \frac{3T}{2mL} \end{pmatrix} \tag{13}$$

**b)** (5 puntos) El sistema es simétrico bajo la reflexión horizontal respecto del punto central, es decir, bajo el intercambio $y_1 \leftrightarrow y_2$. Las únicas soluciones que tienen esta simetría son $y_1(t) = y_2(t)$ e $y_1(t) = -y_2(t)$. Dan lugar a los autovectores

$$V_+ = \begin{pmatrix} 1 \\ 1 \end{pmatrix}\ ,\qquad V_- = \begin{pmatrix} 1 \\ -1 \end{pmatrix} \tag{14}$$

Sustituyendo esos autovectores en la ecuación matricial

$$M^{-1}K\,V = \omega^2 V \tag{15}$$

obtenemos las frecuencias angulares correspondientes a $V_\pm$:

$$\omega_+ = \sqrt{\frac{T}{2mL}}\ ,\qquad \omega_- = \sqrt{\frac{5T}{2mL}} \tag{16}$$

**c)** (5 puntos) El movimiento más general en términos de esos modos normales es

$$\begin{pmatrix} y_1 \\ y_2 \end{pmatrix} = A_+\begin{pmatrix} 1 \\ 1 \end{pmatrix}\cos(\omega_+ t + \varphi_+) + A_-\begin{pmatrix} 1 \\ -1 \end{pmatrix}\cos(\omega_- t + \varphi_-) \tag{17}$$

donde $A_+$ y $A_-$ son dos coeficientes fijados por las condiciones iniciales. A partir de la información sobre las posiciones y velocidades iniciales, tenemos las ecuaciones

$$\begin{pmatrix} 0 \\ A \end{pmatrix} = A_+\begin{pmatrix} 1 \\ 1 \end{pmatrix}\cos\varphi_+ + A_-\begin{pmatrix} 1 \\ -1 \end{pmatrix}\cos\varphi_- \tag{18}$$

$$\begin{pmatrix} 0 \\ 0 \end{pmatrix} = -A_+\begin{pmatrix} 1 \\ 1 \end{pmatrix}\sin\varphi_+ - A_-\begin{pmatrix} 1 \\ -1 \end{pmatrix}\sin\varphi_- \tag{19}$$

De la segunda ecuación obtenemos $\varphi_+ = \varphi_- = 0$, y de la primera podemos despejar

$$A_+ = \frac{A}{2}\ ,\qquad A_- = -\frac{A}{2} \tag{20}$$

El movimiento de $m_1$ es entonces

$$y_1(t) = \frac{A}{2}\left(\cos(\omega_+ t) - \cos(\omega_- t)\right) \tag{21}$$

## Solución del problema 3

**a)** (5 puntos) En $x = 0$, la presión es la misma que la presión atmosférica $P_0$, por lo que la perturbación de presión es $P(0, t) = 0$. En $x = L$, el desplazamiento de las moléculas de aire es nulo, y entonces

$$\frac{\partial P}{\partial x}(L, t) = 0 \tag{22}$$

**b)** (5 puntos) De la condición de contorno en $x = 0$ sabemos que los modos normales tienen la forma

$$P(x, t) \sim \sin(kx) \tag{23}$$

Y de la condición de contorno en $x = L$:

$$k\cos(kL) = 0 \tag{24}$$

deducimos

$$k = \left(n + \frac{1}{2}\right)\frac{\pi}{L}\ ,\qquad n = 0, 1, 2, \ldots \tag{25}$$

El desarrollo de Fourier de $P(x, t)$ es entonces

$$P(x, t) = \sum_{n=0}^{\infty} A_n\sin\left(\left(n + \frac{1}{2}\right)\frac{\pi}{L}x\right)\cos\left(\left(n + \frac{1}{2}\right)\frac{v\pi}{L}t\right) \tag{26}$$

(Las fases de cada término son todas nulas porque la «velocidad» inicial $\frac{\partial P}{\partial t} = 0$.)

**c)** (5 puntos) Los coeficientes de Fourier pueden obtenerse evaluando la integral

$$A_n = \frac{2}{L}\int_0^L f(x)\sin\left(\left(n + \frac{1}{2}\right)\frac{\pi}{L}x\right)dx \tag{27}$$

donde $f(x)$ es la forma inicial dada en el problema.

$$\begin{aligned}
A_n &= \frac{2(P_1 - P_0)}{L}\int_{L/3}^{2L/3}\sin\left(\left(n + \frac{1}{2}\right)\frac{\pi}{L}x\right)dx \\[4pt]
&= -\frac{2(P_1 - P_0)}{\left(n + \frac{1}{2}\right)\pi}\left[\cos\left(\left(n + \frac{1}{2}\right)\frac{2\pi}{3}\right) - \cos\left(\left(n + \frac{1}{2}\right)\frac{\pi}{3}\right)\right]
\end{aligned} \tag{28}$$

**d)** (5 puntos) En el instante $t = \dfrac{2L}{v}$, los argumentos valen

$$\left(n + \frac{1}{2}\right)\frac{v\pi}{L}t = 2\pi n + \pi \tag{29}$$

Por tanto, todos los $\cos\left(\left(n + \frac{1}{2}\right)\frac{v\pi}{L}t\right)$ del desarrollo de $P(x, t)$ valen $-1$. La configuración (perturbación de presión) es entonces la del pulso inicial invertido, es decir, un pulso que baja hasta $P_0 - P_1$.

## Solución del problema 4

**a)** (3 puntos) La aceleración media es

$$\langle\vec{a}\rangle = \frac{\vec{v}_2 - \vec{v}_1}{\Delta t} \tag{30}$$

donde $\vec{v}_1 = w\hat{x}$ y $\vec{v}_2 = w\cos\Delta\alpha\cdot\hat{x} - w\sin\Delta\alpha\cdot\hat{y}$ son las velocidades inicial y final. Puesto que $\Delta\alpha \ll 1$, $\cos\Delta\alpha - 1$ es un infinitésimo de segundo orden, que puede despreciarse frente a $\sin\Delta\alpha$. Entonces

$$\vec{v}_2 - \vec{v}_1 = -w\,\Delta\alpha\cdot\hat{y} \tag{31}$$

$$\langle\vec{a}\rangle = -\frac{w\,\Delta\alpha}{\Delta t}\cdot\hat{y} \tag{32}$$

**b)** (3 puntos) El campo eléctrico generado por esta aceleración es

$$\vec{E}(\vec{r}, t) = -\frac{q\,\vec{a}_\perp(t - |r|/c)}{4\pi\varepsilon_0 rc^2} \tag{33}$$

donde $\vec{a}_\perp(t - |r|/c)$ es la aceleración proyectada sobre la dirección transversal a $\vec{r}$. La dirección del campo eléctrico es, por tanto, la opuesta a esa proyección transversal de la aceleración.

**c) d)** (2 puntos cada uno) La dirección perpendicular a la dirección de la aceleración es la de radiación más intensa. La dirección paralela u opuesta a la dirección de la aceleración es la de radiación mínima (nula).

**e)** (2 puntos) De (33) sabemos que el campo eléctrico escala como $\vec{E} \sim \dfrac{1}{r}$. Por tanto, la amplitud en $P_2$ será $\dfrac{1}{2}$ de la amplitud en $P_1$.

**f)** (3 puntos) La potencia total de radiación es

$$P(t) = \frac{q^2 a^2(t - |r|/c)}{6\pi\varepsilon_0 c^3} \tag{34}$$

Por tanto, la energía total radiada por la carga es

$$E = P\,\Delta t = \Delta t\cdot\frac{q^2 w^2\Delta\alpha^2}{6\pi\varepsilon_0 c^3(\Delta t)^2} = \frac{q^2 w^2\Delta\alpha^2}{6\pi\varepsilon_0 c^3\,\Delta t} \tag{35}$$

## Solución del problema 5

**a)** (5 puntos) Para luz no polarizada, la intensidad después de atravesar un polarizador lineal es $I_A = \frac{1}{2}I_0$. Su polarización después de atravesar A es la de la dirección $\hat{x}$.

**b)** (5 puntos) Después de que la luz atraviese B, el vector de polarización se proyecta sobre la dirección fácil de B, de modo que la intensidad final es

$$I_B = I_A\cos^2\theta = \frac{1}{2}I_0\cos^2\theta \tag{36}$$

**c)** (5 puntos) Después de que la luz atraviese C, el vector de polarización se proyecta desde la dirección fácil de B a la dirección fácil de C (dirección $\hat{y}$), de modo que la intensidad final es

$$I_C = I_B\sin^2\theta = \frac{1}{2}I_0\cos^2\theta\sin^2\theta = \frac{1}{8}I_0\sin^2(2\theta) \tag{37}$$

## Solución del problema 6

**a)** (4 puntos) Puesto que las rendijas son muy estrechas, la intensidad es simplemente la intensidad de interferencia de 4 rendijas:

$$I = I_0\left(\frac{\sin^2(2\delta)}{\sin^2\frac{\delta}{2}}\right)\ ,\qquad \delta = 2\pi\frac{d}{\lambda}\sin\psi \tag{38}$$

**b)** (4 puntos) Los máximos principales están en $\delta = 2\pi n$, o bien $\sin\psi = n\dfrac{\lambda}{d}$. Los mínimos están en $\delta = \dfrac{m\pi}{2}$, donde $4 \nmid m$ (es decir, $m$ no es múltiplo de 4).

**c)** (4 puntos) Cuando se cierran las dos rendijas centrales, el sistema es simplemente una interferencia de dos rendijas con distancia entre rendijas $3d$. Por tanto,

$$I = I_0\left(\frac{\sin^2\delta'}{\sin^2\frac{\delta'}{2}}\right)\ ,\qquad \delta' = 6\pi\frac{d}{\lambda}\sin\psi \tag{39}$$

**d)** (4 puntos) Los nuevos máximos están en

$$\sin\psi = n\frac{\lambda}{3d}\quad (n \in \mathbb{Z}) \tag{40}$$

y los nuevos mínimos están en

$$\sin\psi = \left(n + \frac{1}{2}\right)\frac{\lambda}{3d}\quad (n \in \mathbb{Z}) \tag{41}$$

Los máximos principales

$$\sin\psi = n\frac{\lambda}{d}\quad (n \in \mathbb{Z}) \tag{42}$$

están en las mismas posiciones. La intensidad de los máximos principales disminuye de $16I_0$ a $4I_0$.

**e)** (4 puntos) Cuando la anchura de una sola rendija no puede despreciarse, la intensidad es

$$I = I_0\left(\frac{\sin^2(2\delta)}{\sin^2\frac{\delta}{2}}\right)\frac{\sin^2\beta}{\beta^2}\ ,\qquad \beta = \pi\frac{D}{\lambda}\sin\psi \tag{43}$$

Los ceros del factor de difracción $\dfrac{\sin^2\beta}{\beta^2}$ están en

$$\sin\psi = n\frac{\lambda}{D}\ ,\qquad n = 1, 2, 3, \ldots \tag{44}$$

La condición para que un máximo principal del patrón de interferencia se solape con un cero de difracción es entonces

$$n\frac{\lambda}{D} = \frac{m\lambda}{d} = \frac{m\lambda}{5D} \tag{45}$$

De modo que el orden de interferencia más bajo para el que esto ocurre es $m = 5$.

---

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*
