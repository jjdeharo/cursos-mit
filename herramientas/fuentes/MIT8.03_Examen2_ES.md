---
title: "Examen 2 (otoño de 2016) — 8.03SC Física III: Vibraciones y Ondas"
author: "Yen-Jie Lee (traducción al español)"
lang: es
---

# Examen 2 (otoño de 2016)

**Instituto Tecnológico de Massachusetts**

**Física 8.03, otoño de 2016**

**EXAMEN 2**

## Instrucciones

Escriba sus soluciones en los cuadernillos blancos. No se corregirá nada de lo escrito en la copia del examen. Este examen es a libro cerrado. No se permite ningún equipo electrónico. Todos los teléfonos, blackberries, blueberries, raspberry Pi, tabletas, ordenadores, etc. deben estar apagados.

---

## Hoja de fórmulas

### Muelles y masas

$$m\frac{d^2}{dt^2}x(t) + b\frac{d}{dt}x(t) + kx(t) = F(t)$$

Ecuación diferencial más general con fuerza impulsora armónica:

$$\frac{d^2}{dt^2}x(t) + \Gamma\frac{d}{dt}x(t) + \omega_0^2 x(t) = \frac{F_0}{m}\cos(\omega_d t)$$

Soluciones estacionarias:

$$x_s(t) = A\cos(\omega_d t - \delta)$$

donde

$$A = \frac{\dfrac{F_0}{m}}{\sqrt{(\omega_0^2 - \omega_d^2)^2 + \omega_d^2\Gamma^2}}$$

y

$$\tan\delta = \frac{\Gamma\omega_d}{\omega_0^2 - \omega_d^2}$$

### Soluciones generales

Para $\Gamma = 0$ (sistema no amortiguado):

$$x(t) = R\cos(\omega_0 t + \theta) + x_s(t)$$

donde $R$ y $\theta$ son coeficientes desconocidos.

Para $\Gamma < 2\omega_0$ (sistema subamortiguado):

$$x(t) = Re^{-\frac{\Gamma}{2}t}\cos\left(\sqrt{\omega_0^2 - \frac{\Gamma^2}{4}}\,t + \theta\right) + x_s(t)$$

donde $R$ y $\theta$ son coeficientes desconocidos.

Para $\Gamma = 2\omega_0$ (sistema críticamente amortiguado):

$$x(t) = (R_1 + R_2 t)e^{-\frac{\Gamma}{2}t} + x_s(t)$$

donde $R_1$ y $R_2$ son coeficientes desconocidos.

Para $\Gamma > 2\omega_0$ (sistema sobreamortiguado):

$$x(t) = R_1 e^{\left(-\frac{\Gamma}{2} + \sqrt{\frac{\Gamma^2}{4} - \omega_0^2}\right)t} + R_2 e^{\left(-\frac{\Gamma}{2} - \sqrt{\frac{\Gamma^2}{4} - \omega_0^2}\right)t} + x_s(t)$$

donde $R_1$ y $R_2$ son coeficientes desconocidos.

### Osciladores acoplados

$$F_j = -\sum_{k=1}^{n} K_{jk}\,x_k$$

Ejemplos para $n = 2$:

$$\mathcal{X}(t) = \begin{pmatrix} x_1(t) \\ x_2(t) \end{pmatrix}
\qquad
K = \begin{pmatrix} K_{11} & K_{12} \\ K_{21} & K_{22} \end{pmatrix}
\qquad
M = \begin{pmatrix} m_1 & 0 \\ 0 & m_2 \end{pmatrix}$$

Ecuación matricial del movimiento; las matrices $M$, $K$, $I$ son $n \times n$ y los vectores $\mathcal{X}$, $\mathcal{Z}$ son $n \times 1$:

$$\frac{d^2}{dt^2}\mathcal{X}(t) = -M^{-1}K\,\mathcal{X}(t)$$

$$\mathcal{Z}(t) = Ae^{-i\omega t}$$

$$(M^{-1}K - \omega^2 I)A = 0$$

Para obtener las frecuencias de los modos normales, resuelva:

$$\det(M^{-1}K - \omega^2 I) = 0$$

Para $n = 2$:

$$\det\begin{pmatrix} M_{11} & M_{12} \\ M_{21} & M_{22} \end{pmatrix} = M_{11}M_{22} - M_{12}M_{21}$$

Si el sistema está impulsado por una fuerza, se pueden hallar las amplitudes de respuesta $C(\omega_d)$:

$$F(t) = F_0 e^{-i\omega_d t} \qquad W(t) = C(\omega_d)e^{-i\omega_d t} \qquad C(\omega_d) = \begin{pmatrix} c_1(\omega_d) \\ c_2(\omega_d) \end{pmatrix}$$

$$(M^{-1}K - \omega_d^2 I)\,C(\omega_d) = F_0$$

Resolviendo la ecuación anterior se pueden hallar las amplitudes de respuesta del primer ($c_1(\omega_d)$) y del segundo ($c_2(\omega_d)$) objeto del sistema.

### Simetría de reflexión

Matriz de simetría de reflexión:

$$S = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$$

Autovalores ($\beta$) y autovectores ($A$) de esta matriz $S$ de $2 \times 2$:

1. $\beta = -1$, $A = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$
2. $\beta = 1$, $A = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$

Sistema acoplado unidimensional infinito que satisface la simetría de traslación espacial: dado un autovalor $\beta$, el autovector correspondiente es

$$A_j = \beta^j A_0$$

donde $A_j$ ($A_0$) es la amplitud normal del objeto $j$-ésimo ($0$-ésimo) del sistema.

Considere un sistema unidimensional formado por un número infinito de masas acopladas por muelles; $\beta$ puede escribirse como $\beta = e^{ika}$, donde $k$ es el número de onda y $a$ es la distancia entre las masas.

### Leyes de Kirchhoff

(¡Tenga cuidado con los signos!)

$$\text{Nodo:}\quad \sum_{i}^{n} I_i = 0 \qquad\qquad \text{Malla:}\quad \sum_{i}^{n} \Delta V_i = 0$$

$$\text{Condensadores:}\ \Delta V = \frac{Q}{C} \qquad \text{Bobinas:}\ \Delta V = -L\frac{dI}{dt} \qquad \text{Corriente:}\ I = \frac{dQ}{dt}$$

### Identidades trigonométricas

$$\sin(a \pm b) = \sin(a)\cos(b) \pm \cos(a)\sin(b)$$

$$\cos(a \pm b) = \cos(a)\cos(b) \mp \sin(a)\sin(b)$$

$$\sin(a) + \sin(b) = 2\sin\left(\frac{a+b}{2}\right)\cos\left(\frac{a-b}{2}\right)$$

$$\sin(a) - \sin(b) = 2\cos\left(\frac{a+b}{2}\right)\sin\left(\frac{a-b}{2}\right)$$

$$\cos(a) + \cos(b) = 2\cos\left(\frac{a+b}{2}\right)\cos\left(\frac{a-b}{2}\right)$$

$$\cos(a) - \cos(b) = -2\sin\left(\frac{a+b}{2}\right)\sin\left(\frac{a-b}{2}\right)$$

### Integrales con senos y cosenos

$$\frac{2}{L}\int_0^L \sin\left(\frac{n\pi x}{L}\right)\sin\left(\frac{m\pi x}{L}\right)dx = \begin{cases} 1, & \text{si } n = m \\ 0, & \text{en caso contrario} \end{cases}$$

$$\frac{2}{L}\int_0^L \cos\left(\frac{n\pi x}{L}\right)\cos\left(\frac{m\pi x}{L}\right)dx = \begin{cases} 1, & \text{si } n = m \\ 0, & \text{en caso contrario} \end{cases}$$

$$\frac{2}{L}\int_0^L \cos\left(\frac{n\pi x}{L}\right)\sin\left(\frac{m\pi x}{L}\right)dx = 0$$

$$\int x\sin(x)\,dx = \sin(x) - x\cos(x) + C$$

$$\int x\cos(x)\,dx = \cos(x) + x\sin(x) + C$$

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

Para ondas planas electromagnéticas en el vacío:

$$\vec{B}(\vec{r}, t) = \frac{1}{c}\,\hat{k} \times \vec{E}(\vec{r}, t) \qquad\qquad \vec{E}(\vec{r}, t) = c\,\vec{B}(\vec{r}, t) \times \hat{k}$$

### Densidad lineal de energía en una cuerda

Cuerda con tensión $T$ y densidad de masa $\rho_L$:

$$\frac{dK}{dx} = \frac{1}{2}\rho_L\left(\frac{\partial y}{\partial t}\right)^2 \qquad\qquad \frac{dU}{dx} = \frac{1}{2}T\left(\frac{\partial y}{\partial x}\right)^2$$

### Energía electromagnética por unidad de volumen y vector de Poynting

$$U_E = \frac{1}{2}\varepsilon_0 \vec{E}^2 \qquad U_B = \frac{1}{2\mu_0}\vec{B}^2 \qquad \vec{S} = \frac{1}{\mu_0}\vec{E} \times \vec{B}$$

### Transmisión y reflexión

$$R = \frac{z_1 - z_2}{z_2 + z_1} \qquad\qquad T = \frac{2z_1}{z_2 + z_1}$$

### Velocidad de fase e impedancia

$$v = \sqrt{\frac{T}{\rho_L}} \qquad Z = \sqrt{T\rho_L} \quad \text{(cuerda)}$$

$$v = \sqrt{\frac{1}{LC}} \qquad Z = \sqrt{\frac{L}{C}} \quad \text{(línea de transmisión)}$$

### Ley de Snell

$$n_1\sin\theta_1 = n_2\sin\theta_2$$

### Transformada de Fourier

$$f(t) = \int_{-\infty}^{\infty} d\omega\, C(\omega)e^{-i\omega t}$$

$$C(\omega) = \frac{1}{2\pi}\int_{-\infty}^{\infty} dt\, f(t)e^{i\omega t}$$

### Función delta

$$\frac{1}{2\pi}\int_{-\infty}^{\infty} e^{i(\omega - \omega')t}\,dt = \delta(\omega - \omega')$$

$$\int_{-\infty}^{\infty} \delta(x)\,dx = 1 \qquad\qquad \int_{-\infty}^{\infty} \delta(x - a)f(x)\,dx = f(a)$$

---

## Problema 1 (30 puntos)

Resuelva las siguientes preguntas cortas. (Si observa que está dedicando mucho tiempo a un problema, probablemente no va por el buen camino.)

**A.** (6 puntos) Una onda electromagnética plana progresiva se mueve hacia un conductor perfecto, en el que las cargas pueden moverse libremente sin disipación de energía. ¿Cuál es la condición de contorno para el campo eléctrico de la onda electromagnética en la superficie del conductor (no en su interior)?

**B.** (6 puntos) Una emisora de radio AM con frecuencia de radio $f$ ha recibido recientemente malas críticas por la calidad del audio. El director de la emisora le pide consejo. Usted descubre que una posibilidad para mejorar la calidad del audio es cambiar el ancho de banda $\Delta f$ de la señal emitida por la emisora, de modo que pueda enviar señales con mejor resolución temporal. ¿Le aconsejaría aumentar o disminuir el ancho de banda $\Delta f$? ¿Por qué lo cree así?

**C.** (6 puntos) En una habitación de dimensiones $L \times L \times 16L$, ¿cuál es la frecuencia angular más baja de los modos normales de oscilación del aire de la habitación? (Puede suponer que la velocidad del sonido es $v$.)

**D.** (6 puntos) Considere una cuerda con masa y extremos fijos, de longitud $2L$, tensión $T$ y densidad lineal de masa $\rho_L$. En $t = 0$, esta cuerda tiene la forma inicial $\psi(x, 0)$ que se muestra en la figura 1. La cuerda se suelta entonces con cuidado, de modo que la velocidad inicial de la cuerda $\dot{\psi}(x, 0)$ es 0. ¿Cuánto tarda esta cuerda, un medio no dispersivo, en volver a su forma inicial después de soltarla en $t = 0$? Dé sus explicaciones sin realizar realmente la descomposición de Fourier.

*(Figura 1: cuerda «MIT». La forma inicial de la cuerda dibuja las letras MIT a lo largo de su longitud.)*

**E.** (6 puntos) Un haz de luz viaja por el vacío ($n_1 = 1$) antes de alcanzar dos láminas transparentes de índices de refracción $n_2$ y $n_3$. Llega primero a una lámina transparente de índice $n_2$ con un ángulo de incidencia $\alpha = 60^\circ$. El haz la atraviesa, alcanza otra lámina transparente de índice $n_3$, la atraviesa y entra en un cuarto material de índice $n_4$, propagándose en ese medio con un ángulo $\beta = 45^\circ$ respecto al eje normal. La configuración de este experimento óptico se muestra en la figura 2. ¿Cuál es el valor de $n_4$?

*(Figura 2: experimento con luz. El haz atraviesa sucesivamente las láminas de índices $n_2$ y $n_3$ hasta entrar en el medio de índice $n_4$, con los ángulos $\alpha$ y $\beta$ medidos respecto a la normal.)*

---

## Problema 2 (17 puntos)

Las fluctuaciones de la densidad de carga en un plasma se rigen por una ecuación de ondas que, para distorsiones unidimensionales, se reduce a

$$a^2\frac{\partial^2 \rho(x, t)}{\partial x^2} - \Omega_p^2\,\rho(x, t) = \frac{\partial^2 \rho(x, t)}{\partial t^2}$$

Aquí $\rho(x, t)$ es una pequeña desviación de la densidad de carga respecto a su valor de equilibrio y $\Omega_p$ es un parámetro constante denominado frecuencia de plasma.

**a.** (3 puntos) Escriba una solución de onda armónica progresiva que describa la desviación de la densidad de carga $\rho(x, t)$, que avanza en la dirección $-\hat{x}$. Suponemos que el número de onda de esta onda progresiva es $k$, la frecuencia angular es $\omega$ y la amplitud es $A$. En $t = 0$ y $x = 0$, la desviación de la densidad de carga $\rho(0, 0)$ es cero.

**b.** (7 puntos) Halle la relación de dispersión $\omega(k)$. Dibuje $\omega(k)$ en función de $k$. ¿Cuáles son las frecuencias angulares de las ondas armónicas progresivas que pueden existir en el plasma?

**c.** (4 puntos) ¿Cuál es la velocidad de grupo de este medio? ¿Es un medio dispersivo?

**d.** (3 puntos) ¿Cuál es la velocidad de fase límite para números de onda $k$ grandes en este medio?

---

## Problema 3 (23 puntos)

El campo eléctrico de una onda plana uniforme en el vacío, que viaja a la velocidad de la luz $c$, viene dado por

$$\vec{E}(\vec{r}, t) = E_0(3\hat{x} + a\hat{y})\cos(\omega t - 4x + 3y)$$

donde $a$ es una constante. (Este es un problema en el espacio tridimensional.)

**a.** (4 puntos) ¿Cuál es la dirección de propagación de esta onda plana? (Represente la dirección como un vector unitario.)

**b.** (6 puntos) Calcule la frecuencia angular $\omega$ y la longitud de onda de esta onda electromagnética usando los números dados.

**c.** (4 puntos) ¿Cuál es el valor de $a$?

**d.** (6 puntos) ¿Cuál es el campo magnético $\vec{B}$ asociado a esta onda?

**e.** (3 puntos) ¿Cuál es la densidad de flujo de energía direccional (la tasa de transferencia de energía por unidad de área) de esta onda electromagnética?

---

## Problema 4 (30 puntos)

Una cuerda de tensión $T$, masa por unidad de longitud $\rho_L$ y longitud $L$ adopta la forma mostrada en la figura 3. La cuerda solo puede moverse hacia arriba y hacia abajo en la dirección $\hat{y}$. El extremo izquierdo de la cuerda está fijado a una pared y el extremo derecho está unido a un anillo sin masa que puede moverse libremente en la dirección transversal sin fricción. En este problema se desprecia la gravedad, y puede suponer la aproximación de ángulos pequeños para toda la cuerda. La cuerda se suelta desde el reposo en $t = 0$.

**a.** (8 puntos) Escriba las condiciones de contorno en $x = 0$ y $x = L$. Puede escribir la condición en términos de $\psi(x, t)$, que es el desplazamiento de la cuerda con masa en la dirección $\hat{y}$ respecto a la posición de equilibrio.

**b.** (6 puntos) Esboce la forma ($\psi$ en función de $x$) de los tres modos normales más bajos (independientemente de si están excitados o no) y dé las frecuencias angulares correspondientes.

**c.** (10 puntos) Para la forma inicial mostrada en la figura 3, calcule la amplitud del $n$-ésimo modo normal en términos de $n$ y $H$.

**d.** (6 puntos) ¿Qué modos normales no se excitarán? Exprese sus resultados en términos de $n$.

*(Figura 3: forma inicial de la cuerda en el instante $t = 0$. La cuerda parte de la pared en $x = 0$ y alcanza una altura máxima $H$ antes de llegar al anillo del extremo derecho, en $x = L$.)*

---

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*
