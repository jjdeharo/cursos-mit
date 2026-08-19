---
title: "Examen final de práctica 1 (con soluciones) — 8.03SC Física III: Vibraciones y Ondas"
author: "Yen-Jie Lee (traducción al español)"
lang: es
---

# Examen final de práctica 1

**INSTITUTO TECNOLÓGICO DE MASSACHUSETTS — DEPARTAMENTO DE FÍSICA**

**Física 8.03: Vibraciones y Ondas**

## Instrucciones

1. No retire ninguna página del examen, salvo la hoja de fórmulas.
2. Este es un examen a libro cerrado.
3. Realice los SEIS (6) problemas.
4. MUESTRE TODO SU TRABAJO. Escriba su nombre en cada hoja.
5. NO SE PERMITEN CALCULADORAS, LIBROS, ORDENADORES NI TELÉFONOS MÓVILES.

**Puntuación:** Problema 1: 16 · Problema 2: 16 · Problema 3: 16 · Problema 4: 16 · Problema 5: 18 · Problema 6: 18

---

## Hoja de fórmulas

La ecuación diferencial

$$\ddot{x} + \gamma\dot{x} + \omega_0^2 x = f\cos(\omega t + \varphi) \tag{1}$$

tiene las soluciones generales

$$\frac{\gamma}{2} < \omega_0: \qquad X(t) = A_1 e^{-\left(\frac{\gamma}{2}\right)t}\cos(\omega' t + \beta) + X_p(t) \tag{2}$$

$$\frac{\gamma}{2} = \omega_0: \qquad X(t) = (A_1 + A_2 t)e^{-\left(\frac{\gamma}{2}\right)t} + X_p(t) \tag{3}$$

$$\frac{\gamma}{2} > \omega_0: \qquad X(t) = A_1 e^{-\Gamma_+ t} + A_2 e^{-\Gamma_- t} + X_p(t) \tag{4}$$

con

$$X_p(t) = A(\omega)\cos(\omega t - \delta(\omega) + \varphi) \tag{5}$$

y

$$\omega' = \sqrt{\omega_0^2 - \frac{\gamma^2}{4}} \qquad\qquad \Gamma_\pm = \frac{\gamma}{2} \pm \sqrt{\frac{\gamma^2}{4} - \omega_0^2} \tag{6}$$

$$A(\omega) = f\Big/\sqrt{(\omega_0^2 - \omega^2)^2 + (\gamma\omega)^2} \qquad\qquad \tan(\delta(\omega)) = \gamma\omega/(\omega_0^2 - \omega^2) \tag{7}$$

### Relaciones idealizadas para la tensión en los elementos de un circuito

1. Condensador: $V_C = \dfrac{Q}{C}$
2. Resistencia: $V_R = IR$
3. Autoinducción: $V_L = L\dfrac{dI}{dt}$

### Ecuación de ondas escalar clásica

En 3D:

$$\frac{\partial^2\Psi}{\partial t^2} = v^2\nabla^2\Psi$$

La solución de onda plana es $\Psi(\vec{r}, t) = A\cos(\vec{k}\cdot\vec{r} \pm \omega t + \varphi)$.

La solución de onda esférica es $\Psi(\vec{r}, t) = A\dfrac{\cos(kr \pm \omega t + \varphi)}{r}$.

En 1D:

$$\frac{\partial^2\Psi}{\partial t^2} = v^2\frac{\partial^2\Psi}{\partial x^2}$$

La solución de onda estacionaria es $\Psi(x, t) = A\cos\left(\frac{\omega}{v}x + \varphi_x\right)\cos(\omega t + \varphi_t)$.

La solución de onda progresiva es $\Psi(x, t) = f\left(t \pm \frac{x}{v}\right)$.

### Velocidades e impedancias

$$\text{Cuerda:}\quad v = \sqrt{\frac{T}{\mu}} \qquad Z = \sqrt{T\mu} \qquad \langle P\rangle = \frac{1}{2}\frac{F_0^2}{Z}$$

$$\text{Sonido:}\quad v = \sqrt{\frac{\kappa}{\rho}} \qquad Z = \sqrt{\kappa\rho} \qquad \kappa = -V\frac{\partial P}{\partial V}$$

$$\text{Torsión:}\quad v = \sqrt{\frac{k}{I}} \qquad Z = \sqrt{kI}$$

$$\text{Línea de transmisión:}\quad v = \frac{1}{\sqrt{LC}} \qquad Z = \sqrt{\frac{L}{C}} \qquad \langle P\rangle = \frac{1}{2}\frac{V_0^2}{Z}$$

$$v_{\text{fase}} = \frac{\omega}{k} = \nu\lambda \qquad\qquad v_{\text{grupo}} = \frac{\partial\omega}{\partial k}$$

### Transmisión y reflexión

Para una onda de desplazamiento en una cuerda:

$$T = \frac{2Z_1}{Z_1 + Z_2} \qquad\qquad R = \frac{Z_1 - Z_2}{Z_1 + Z_2}$$

Para una onda de tensión en una línea de transmisión:

$$T = \frac{2Z_2}{Z_1 + Z_2} \qquad\qquad R = \frac{Z_2 - Z_1}{Z_1 + Z_2}$$

### Ecuaciones de Maxwell y magnitudes asociadas

$$\nabla\cdot\vec{E} = \frac{\rho}{\varepsilon_0} \qquad\qquad \vec{F} = q(\vec{E} + \vec{v}\times\vec{B})$$

$$\nabla\cdot\vec{B} = 0 \qquad\qquad U_E = \frac{1}{2}\varepsilon_0 E^2$$

$$\nabla\times\vec{E} = -\frac{\partial\vec{B}}{\partial t} \qquad\qquad U_B = \frac{1}{2\mu_0}B^2$$

$$\nabla\times\vec{B} = \varepsilon_0\mu_0\frac{\partial\vec{E}}{\partial t} + \mu_0\vec{J} \qquad\qquad \vec{S} = \frac{\vec{E}\times\vec{B}}{\mu_0}$$

Onda electromagnética en el vacío:

$$\frac{\partial^2\vec{E}}{\partial t^2} = \frac{1}{\mu_0\varepsilon_0}\nabla^2\vec{E} \qquad\qquad \text{Presión de radiación: } \frac{\vec{S}}{c}$$

Para una solución de onda progresiva en el vacío:

$$\frac{|E|}{|B|} = c = \frac{1}{\sqrt{\mu_0\varepsilon_0}}$$

### Radiación debida a la aceleración de una carga

$$\vec{E}(\vec{r}, t) = -\frac{q\vec{a}_\perp(t')}{4\pi\varepsilon_0 rc^2} \qquad \vec{B} = \frac{\hat{r}\times\vec{E}}{c} \qquad t' = t - \frac{|r|}{c}$$

Potencia total radiada por una carga acelerada (fórmula de Larmor):

$$P(t) = \frac{q^2 a^2(t')}{6\pi\varepsilon_0 c^3}$$

Condiciones de contorno en la superficie de un conductor perfecto (para campos variables en el tiempo): $E_\parallel = 0$ y $B_\perp = 0$.

Para la mayoría de los dieléctricos ($K_M \approx 1$): $n = \sqrt{K_E K_M} \approx \sqrt{K_E}$, $v_{\text{fase}} = \dfrac{c}{n}$.

Ley de Snell: $n_1\sin\theta_1 = n_2\sin\theta_2$

Reflexión y transmisión de ondas electromagnéticas con incidencia normal:

$$E_{\text{reflejada}} = E_{\text{incidente}}\frac{n_1 - n_2}{n_1 + n_2} \qquad\qquad E_{\text{transmitida}} = E_{\text{incidente}}\frac{2n_1}{n_1 + n_2}$$

### Interferencia y difracción

Para la interferencia de $N$ rendijas con separación $d$ entre dos rendijas:

$$I(\theta) = I_0\frac{\sin^2\left(\frac{N\pi}{\lambda}d\sin\theta\right)}{\sin^2\left(\frac{\pi}{\lambda}d\sin\theta\right)}$$

Intensidad de difracción de una rendija de anchura $D$:

$$I(\theta) = I_0\frac{\sin^2\left(\frac{\pi}{\lambda}D\sin\theta\right)}{\left(\frac{\pi}{\lambda}D\sin\theta\right)^2}$$

Criterio de Rayleigh para la resolución: el pico de difracción de una imagen cae sobre el primer mínimo del patrón de difracción de la segunda imagen.

### Series de Fourier

Para una función periódica de periodo $\Lambda$:

$$f(x) = \frac{A_0}{2} + \sum_{n=1}^{\infty} A_n\cos\left(n\frac{2\pi x}{\Lambda}\right) + \sum_{n=1}^{\infty} B_n\sin\left(n\frac{2\pi x}{\Lambda}\right)$$

con

$$A_0 = \frac{2}{\Lambda}\int_0^\Lambda f(x)\,dx \qquad A_n = \frac{2}{\Lambda}\int_0^\Lambda f(x)\cos\left(n\frac{2\pi x}{\Lambda}\right)dx \qquad B_n = \frac{2}{\Lambda}\int_0^\Lambda f(x)\sin\left(n\frac{2\pi x}{\Lambda}\right)dx$$

### Identidades trigonométricas

$$\sin(A + B) = \sin A\cos B + \cos A\sin B$$

$$\cos(A + B) = \cos A\cos B - \sin A\sin B$$

$$\sin A + \sin B = 2\sin\left(\frac{1}{2}(A + B)\right)\cos\left(\frac{1}{2}(A - B)\right)$$

$$\cos A + \cos B = 2\cos\left(\frac{1}{2}(A + B)\right)\cos\left(\frac{1}{2}(A - B)\right)$$

$$\sin A - \sin B = 2\cos\left(\frac{1}{2}(A + B)\right)\sin\left(\frac{1}{2}(A - B)\right)$$

$$\cos A - \cos B = -2\sin\left(\frac{1}{2}(A + B)\right)\sin\left(\frac{1}{2}(A - B)\right)$$

$$e^{j\theta} = \cos\theta + j\sin\theta$$

### Algunas integrales útiles

$$\int_0^L \sin\left(\frac{n\pi x}{L}\right)\sin\left(\frac{m\pi x}{L}\right)dx = \begin{cases} \frac{L}{2} & \text{para } m = n \\ 0 & \text{para } m \neq n \end{cases}$$

$$\int_0^L \cos\left(\frac{n\pi x}{L}\right)\cos\left(\frac{m\pi x}{L}\right)dx = \begin{cases} \frac{L}{2} & \text{para } m = n \\ 0 & \text{para } m \neq n \end{cases}$$

$$\int x\sin(ax)\,dx = \frac{\sin(ax)}{a^2} - \frac{x\cos(ax)}{a} + C$$

$$\int x\cos(ax)\,dx = \frac{\cos(ax)}{a^2} + \frac{x\sin(ax)}{a} + C$$

### Operadores vectoriales

$$\operatorname{div}\vec{A} = \nabla\cdot\vec{A} = \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z}$$

$$\operatorname{rot}\vec{A} = \nabla\times\vec{A} = \begin{vmatrix} \hat{x} & \hat{y} & \hat{z} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ A_x & A_y & A_z \end{vmatrix}$$

$$\nabla^2\vec{A} = \left(\frac{\partial^2 A_x}{\partial x^2} + \frac{\partial^2 A_x}{\partial y^2} + \frac{\partial^2 A_x}{\partial z^2}\right)\hat{x} + \left(\frac{\partial^2 A_y}{\partial x^2} + \frac{\partial^2 A_y}{\partial y^2} + \frac{\partial^2 A_y}{\partial z^2}\right)\hat{y} + \left(\frac{\partial^2 A_z}{\partial x^2} + \frac{\partial^2 A_z}{\partial y^2} + \frac{\partial^2 A_z}{\partial z^2}\right)\hat{z}$$

### Constantes físicas

$$e = 2.718 \qquad e^{-1} = 0.3679 \qquad \pi = 3.1416 \qquad c = 3.0\times10^8\ \text{m/s}$$

---

## Problema 1 (16 puntos)

El campo eléctrico de un modo TE en una guía de ondas rectangular, perfectamente conductora e infinitamente larga en la dirección $x$ (con $a < b$), viene dado por

$$\vec{E}(x, y, z, t) = E_0\cos(k_y y + \varphi_y)\cos(k_x x - \omega t)\hat{z} \tag{8}$$

**(1.a)** (4 puntos) Halle $k_y$ y $\varphi_y$ que satisfacen las condiciones de contorno.

**(1.b)** (4 puntos) Escriba la relación de dispersión de este modo de la guía de ondas.

**(1.c)** (4 puntos) ¿Cuál es la frecuencia más baja que se propagará en este modo?

**(1.d)** (4 puntos) ¿Cuál es el campo magnético $\vec{B}(x, y, z, t)$ asociado al campo eléctrico de este modo?

*(Figura 1: guía de ondas perfectamente conductora, de sección rectangular con lados $a$ y $b$.)*

---

## Problema 2 (16 puntos)

La figura muestra un sistema de masas. La masa $2m$ está conectada a una pared inmóvil mediante un muelle de constante $2k$, mientras que la masa $m$ está conectada a una pared inmóvil mediante un muelle de constante $k$. Las masas están acopladas entre sí mediante una banda elástica de longitud $L$, sometida a una tensión $T = 2kL$. Las masas están obligadas a moverse solo en la dirección $x$. En el equilibrio, las masas tienen la misma posición $x$ y los muelles no están comprimidos. No hay fricción ni gravedad. Los desplazamientos respecto del equilibrio son lo bastante pequeños ($x_1, x_2 \ll L$) como para que la tensión de la banda permanezca constante.

**(2.a)** (5 puntos) Escriba las ecuaciones diferenciales acopladas que describen el desplazamiento de las masas respecto del equilibrio $\{x_1, x_2\}$.

**(2.b)** (7 puntos) Halle las frecuencias de los modos normales del sistema.

**(2.c)** (4 puntos) Esboce los modos normales del sistema, indicando claramente tanto la magnitud como la dirección del movimiento de las masas.

*(Figura 2: sistema de osciladores acoplados.)*

---

## Problema 3 (16 puntos)

**(3.a)** (5 puntos) Una fibra óptica consiste en una varilla maciza de un material de índice de refracción $n_f$ rodeada por una envoltura cilíndrica de material de índice $n_c$. Halle el mayor ángulo $\theta$ tal que una onda que incide sobre la varilla maciza desde el aire, de índice $n_a$, permanezca dentro de la varilla (exprese su respuesta en términos de $n_f$, $n_c$ y $n_a$).

**(3.b)** (4 puntos) Luz no polarizada que se propaga en el vacío se refleja en la superficie de un líquido de índice $n$. El rayo reflejado incide sobre una pantalla situada a 25 cm, a una altura de 20 cm, y se observa que está polarizado al 100 %. ¿Cuánto vale $n$?

**(3.c)** (7 puntos) Considere un medio en el que las ondas se propagan con la relación de dispersión

$$\omega^2 = \omega_0^2 + A^2 k^2 \tag{9}$$

donde $\omega$ es la frecuencia angular de la onda, $k$ es el número de onda, y $\omega_0$ y $A$ son constantes reales.

(i) ¿Cuál es el rango de frecuencias $\omega$ para las que pueden propagarse ondas?

(ii) Calcule $v_{\text{fase}}$ y $v_{\text{grupo}}$. Haga un esbozo cuidadosamente etiquetado de cada una en función de $\omega$.

*(Figura 3: fibra óptica. Figura 4: gráficas para representar las velocidades de fase y de grupo.)*

---

## Problema 4 (16 puntos)

Un haz monocromático incide sobre $N$ rendijas, lo que da lugar a un patrón de intensidad en función del ángulo sobre una pantalla situada a cierta distancia. Cada rendija tiene una anchura $D$ y la distancia entre los centros de las rendijas es $d$. La distancia entre la pantalla y las rendijas es muy grande.

A partir del patrón, deduzca lo siguiente:

**(4.a)** (6 puntos) El número de rendijas $N$ sobre las que incide el haz. Explique su razonamiento.

**(4.b)** (6 puntos) La razón $d/D$. Explique su razonamiento.

**(4.c)** (4 puntos) Suponga ahora que la anchura de las rendijas se reduce hasta $\sim 0$, mientras que la intensidad del haz monocromático se aumenta de modo que la intensidad del máximo central no cambia. Sobre la gráfica que muestra el patrón de intensidad original (en línea discontinua), dibuje el patrón de intensidad resultante.

*(Figura 5: patrón de interferencia debido a $N$ rendijas. Figura 6: gráfica para dibujar el patrón resultante cuando $D \to 0$.)*

---

## Problema 5 (18 puntos)

Una cuerda de longitud $2L$ y densidad de masa $\mu$ se somete a una tensión $T$ y está fija por ambos extremos. En el instante $t = 0$, el desplazamiento de la cuerda es nulo en todas partes, pero se la golpea de modo que se imparte una velocidad transversal a una sección de la cuerda. Las condiciones iniciales de la cuerda son (con $a \ll L$):

$$y(x, t = 0) = 0 \tag{10}$$

$$\dot{y}(x, t = 0) = \begin{cases} v_0 & : L - a \leq x < L \\ -v_0 & : L \leq x < L + a \\ 0 & : \text{en el resto} \end{cases} \tag{11}$$

**(5.a)** (3 puntos) Esboce los tres primeros modos normales de vibración de esta cuerda, independientemente de si están excitados o no.

**(5.b)** (10 puntos) ¿Cuál es la amplitud del $n$-ésimo modo normal después de golpear la cuerda? ¿Cuál es el modo más bajo no excitado?

**(5.c)** (5 puntos) Esboce el desplazamiento de la cuerda en el instante $t = \dfrac{L}{2}\sqrt{\dfrac{\mu}{T}}$.

*(Figura 7: velocidad transversal inicial de la cuerda en $t = 0$; el desplazamiento inicial es nulo en todas partes. Figuras 8 y 9: gráficas para representar los tres primeros modos normales y el desplazamiento de la cuerda.)*

*[Nota de la traducción: el encabezado de este problema en el PDF original indica «20 Points», mientras que la tabla de puntuaciones de la portada le asigna 18. Se ha mantenido el valor de la tabla, coherente con el total de 100 puntos del examen.]*

---

## Problema 6 (18 puntos)

Una partícula cargada de masa $M$ y carga $+Q$ está unida al extremo de un muelle de constante $k$. El muelle se encuentra a lo largo del eje $x$ y el punto de equilibrio está en el origen. La partícula se desplaza del equilibrio una distancia $A$ en la dirección $x$ y se suelta en $t = 0$. Suponga que el tamaño de la partícula es mucho menor que $A$, de modo que puede tratarse como una carga puntual, y que la tasa de amortiguamiento es muy pequeña.

**(6.a)** (4 puntos) Calcule el campo eléctrico radiado por la partícula a lo largo de una dirección arbitraria del plano $x$-$z$, a una distancia $R$, donde $R \gg A$.

**(6.b)** (4 puntos) Calcule la potencia total promediada en el tiempo radiada por la partícula.

**(6.c)** (6 puntos) Suponiendo que la potencia radiada no cambia apreciablemente en función del tiempo, dé una estimación sencilla y aproximada del tiempo que tardará la partícula en reducir su amplitud de oscilación a $1/e$ de su valor inicial. ¿Es realista esta suposición?

**(6.d)** (4 puntos) Puede obtenerse una estimación más refinada usando que $dA/dt = (dA/dE)\times(dE/dt)$, y empleando la potencia media radiada en un ciclo para $dE/dt$. Úselo para calcular el tiempo que tardará la partícula en reducir su amplitud de oscilación a $1/e$ de su valor inicial.

*(Figura 10: carga oscilante.)*

---

# Soluciones

## Solución del problema 1

**(1.a)** Necesitamos que $E_\parallel \to 0$ en el contorno con el conductor. El campo eléctrico está en la dirección $\hat{z}$, así que necesitamos $E = 0$ en (i) $y = 0$ y en (ii) $y = b$. La condición (i) implica que $\varphi_y = \pm\frac{\pi}{2}$, de modo que $E \propto \sin(k_y y)$. La condición (ii) implica que $k_y = \frac{n\pi}{a}$, donde $n$ es un entero mayor que cero. Podemos, por tanto, reescribir el campo eléctrico como

$$E(x, y, z, t) = E_0\sin\left(\frac{n\pi}{a}y\right)\cos(k_x x - \omega t)\hat{z} \tag{2}$$

*[Nota de la traducción: el original sitúa la segunda pared en $y = b$, pero a partir de aquí todas sus expresiones usan $a$ como dimensión transversal (incluida la frecuencia de corte del apartado 1.c). Se han conservado tal cual; para que el desarrollo sea coherente, la pared de la condición (ii) debe entenderse en $y = a$.]*

**(1.b)** Podemos obtener la relación de dispersión a partir de la ecuación de ondas:

$$\nabla^2\vec{E} - \frac{1}{c^2}\frac{\partial^2\vec{E}}{\partial t^2} = 0 \tag{3}$$

Sustituyendo la solución de $\vec{E}$ en la ecuación de ondas encontramos

$$\frac{\omega^2}{c^2} = k_x^2 + k_y^2 \tag{4}$$

$$\frac{\omega^2}{c^2} = k_x^2 + \left(\frac{n\pi}{a}\right)^2 \tag{5}$$

$$\Rightarrow k_x = \sqrt{\frac{\omega^2}{c^2} - \left(\frac{n\pi}{a}\right)^2} \tag{6}$$

**(1.c)** La frecuencia más baja que se propaga ocurre para $n = 1$; en este caso la relación de dispersión queda

$$k_x = \sqrt{\frac{\omega^2}{c^2} - \left(\frac{\pi}{a}\right)^2} \tag{7}$$

de modo que la frecuencia más baja que da lugar a un número de onda no imaginario es

$$\omega_{\text{corte}} = \frac{\pi c}{a} \tag{8}$$

$$\Rightarrow f_{\text{corte}} = \frac{c}{2a} \tag{9}$$

**(1.d)** Podemos hallar el campo magnético asociado a este modo mediante la ley de Faraday:

$$\nabla\times\vec{E} = -\frac{\partial\vec{B}}{\partial t} \tag{10}$$

$$\begin{vmatrix} \hat{x} & \hat{y} & \hat{z} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ 0 & 0 & E_z \end{vmatrix} = -\frac{\partial\vec{B}}{\partial t} \tag{11}$$

$$E_0 k_y\cos(k_y y)\cos(k_x x - \omega t)\hat{x} + E_0\sin(k_y y)k_x\sin(k_x x - \omega t)\hat{y} = -\frac{\partial\vec{B}}{\partial t} \tag{12}$$

$$\vec{B}(x, y, z, t) = E_0\frac{k_y}{\omega}\cos(k_y y)\sin(k_x x - \omega t)\hat{x} - E_0\frac{k_x}{\omega}\sin(k_y y)\cos(k_x x - \omega t)\hat{y} \tag{13}$$

## Solución del problema 2

**(2.a)** Para $x_1$ tenemos, por la ley de Newton,

$$2m\ddot{x}_1 = -2kx_1 - T\sin\theta \tag{14}$$

donde $\sin\theta = (x_1 - x_2)/L$. Sustituyendo, encontramos

$$2m\ddot{x}_1 = -\left(2k - \frac{T}{L}\right)x_1 + \frac{T}{L}x_2 \tag{15}$$

$$\ddot{x}_1 = -\left(\frac{k}{m} - \frac{T}{2mL}\right)x_1 + \frac{T}{2mL}x_2 \tag{16}$$

$$\ddot{x}_1 = \frac{-2k}{m}x_1 + \frac{k}{m}x_2 \tag{17}$$

Mientras que para $x_2$ encontramos

$$m\ddot{x}_2 = -kx_2 + T\sin\theta \tag{18}$$

$$m\ddot{x}_2 = -\left(k - \frac{T}{L}\right)x_2 + \frac{T}{L}x_1 \tag{19}$$

$$\ddot{x}_2 = \frac{2k}{m}x_1 - \frac{3k}{m}x_2 \tag{20}$$

Llamando ahora $\omega_0^2 = k/m$, podemos reescribirlas como

$$\ddot{x}_1 = -2\omega_0^2 x_1 + \omega_0^2 x_2 \tag{21}$$

$$\ddot{x}_2 = 2\omega_0^2 x_1 - 3\omega_0^2 x_2 \tag{22}$$

**(2.b)** En forma matricial podemos reescribir las ecuaciones del movimiento (usando el ansatz $\ddot{x}_i = -\omega^2 x_i$):

$$\begin{pmatrix} -2\omega_0^2 & \omega_0^2 \\ 2\omega_0^2 & -3\omega_0^2 \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = -\omega^2\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} \tag{23}$$

Y resolviendo para los posibles valores de $\omega$ tenemos

$$\begin{pmatrix} -2\omega_0^2 + \omega^2 & \omega_0^2 \\ 2\omega_0^2 & -3\omega_0^2 + \omega^2 \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = 0 \tag{24}$$

$$\left(-2\omega_0^2 + \omega^2\right)\left(-3\omega_0^2 + \omega^2\right) - 2\omega_0^4 = 0 \tag{25}$$

$$6\omega_0^4 - 5\omega_0^2\omega^2 + \omega^4 - 2\omega_0^4 = 0 \tag{26}$$

$$\left(4\omega_0^2 - \omega^2\right)\left(\omega_0^2 - \omega^2\right) = 0 \tag{27}$$

De modo que los dos valores posibles de $\omega$ son

$$\omega_1 = \omega_0 = \sqrt{\frac{k}{m}} \tag{28}$$

y

$$\omega_2 = 2\omega_0 = 2\sqrt{\frac{k}{m}} \tag{29}$$

**(2.c)** En el modo 1 ($\omega_1$), la razón de las amplitudes del movimiento de las masas es

$$x_2/x_1 = 1 \tag{30}$$

Mientras que en el modo 2 ($\omega_2$), la razón de las amplitudes del movimiento de las masas es

$$x_2/x_1 = -2 \tag{31}$$

## Solución del problema 3

**(3.a)** Todos los rayos de la varilla maciza que inciden sobre la envoltura cilíndrica con un ángulo menor que el ángulo crítico $\theta_c = \sin^{-1}(n_c/n_f)$ quedarán atrapados en la varilla. Por tanto, el mayor ángulo $\theta$ que puede incidir sobre la varilla y permanecer dentro viene dado por

$$n_a\sin\theta = n_f\sin\theta_2 \tag{32}$$

$$\theta_2 = \frac{\pi}{2} - \theta_c \tag{33}$$

$$\Rightarrow \sin\theta = \frac{n_f}{n_a}\sin\left(\frac{\pi}{2} - \theta_c\right) \tag{34}$$

$$\Rightarrow \theta = \sin^{-1}\left(\frac{n_f}{n_a}\sin\left(\frac{\pi}{2} - \theta_c\right)\right) \tag{35}$$

O, de forma equivalente, podemos escribir

$$\frac{n_a}{n_f}\sin\theta = \sin\theta_2 = \frac{\sqrt{n_f^2 - n_c^2}}{n_f} \tag{36}$$

$$\sin\theta = \frac{n_f}{n_a}\left(\frac{\sqrt{n_f^2 - n_c^2}}{n_f}\right) \tag{37}$$

$$\theta = \sin^{-1}\left(\frac{1}{n_a}\sqrt{n_f^2 - n_c^2}\right) \tag{38}$$

**(3.b)** Si la luz reflejada está polarizada al 100 %, debe incidir con el ángulo de Brewster. Así pues,

$$\theta_B = \tan^{-1}(n_2/n_1) = \tan^{-1}(n_2) = \frac{\pi}{2} - \tan^{-1}(20/25) \tag{39}$$

$$\Rightarrow n_2 = \tan\left(\frac{\pi}{2} - \tan^{-1}(4/5)\right) \tag{40}$$

O, más sencillamente, podemos escribir

$$\tan^{-1}(n_2/n_1) = \theta_B \tag{41}$$

$$\tan\theta_B = 25/20 = 5/4 \tag{42}$$

$$\Rightarrow \tan\left(\tan^{-1}(n_2/n_1)\right) = 5/4 \tag{43}$$

$$\Rightarrow n_2 = 5/4 \tag{44}$$

**(3.c)** (i) Reordenando la relación de dispersión, encontramos que el número de onda en función de la frecuencia viene dado por

$$k = \frac{1}{A}\sqrt{\omega^2 - \omega_0^2} \tag{46}$$

*[Nota de la traducción: el PDF original escribe en esta ecuación $k = \frac{1}{A}\sqrt{\omega_0^2 + A^2k^2}$, expresión circular que no despeja $k$. Lo que se obtiene al despejar la relación de dispersión (45) es $k = \frac{1}{A}\sqrt{\omega^2 - \omega_0^2}$, que es además la que usa el propio desarrollo posterior.]*

De modo que la frecuencia más baja que da lugar a un número de onda no imaginario es $\omega = \omega_0$, así que el rango de frecuencias que pueden propagarse es $\omega_0 < \omega < \infty$.

(ii) La velocidad de fase viene dada por $\omega/k$, de modo que encontramos

$$v_p = \omega/k = \frac{\omega}{\frac{1}{A}\sqrt{\omega^2 - \omega_0^2}} = \frac{A\omega}{\sqrt{\omega^2 - \omega_0^2}} \tag{47}$$

Mientras que la velocidad de grupo viene dada por $\dfrac{d\omega}{dk}$:

$$v_g = \frac{d\omega}{dk} = \frac{A^2 k}{\omega} = A\sqrt{1 - \left(\frac{\omega_0}{\omega}\right)^2} \tag{48}$$

## Solución del problema 4

**(4.a)** Hay tres pequeños lóbulos entre picos. Por tanto, $N = 5$ (obsérvese que habrá $N - 2$ lóbulos pequeños en un patrón de interferencia de $N$ rendijas).

**(4.b)** En primer lugar, recuerde que los picos de interferencia aparecen en $\dfrac{n\lambda}{d}$, mientras que los mínimos de difracción aparecen en $\dfrac{m\lambda}{D}$, donde $n$ y $m$ son enteros. En el patrón de interferencia se aprecian los picos 0.º, 1.º, 2.º y 3.º, pero no se ve el 4.º. Esto significa que el 4.º pico queda cancelado por el mínimo de difracción. Observamos entonces que el primer mínimo de difracción y el cuarto pico de interferencia están en la misma posición. Por tanto, $\dfrac{4\lambda}{d} = \dfrac{\lambda}{D}$, y en consecuencia $d/D = 4$.

**(4.c)** Recordamos de la demostración vista en clase que, a medida que se reduce el tamaño de una rendija, el patrón de difracción se ensancha; en el límite en que la anchura de las rendijas tiende a cero, el patrón de difracción se ensancha infinitamente, de modo que ya no modula el patrón de interferencia.

## Solución del problema 5

**(5.b)** En este caso, el desplazamiento de la cuerda puede expresarse como una suma de modos normales de la forma

$$y(x, t) = \sum_n A_n\sin(k_n x)\sin(\omega_n t + \phi) \tag{51}$$

con $\omega_n = k_n v = k_n\sqrt{\dfrac{T}{\mu}}$ y $k_n = \dfrac{n\pi}{2L}$.

Así, la velocidad transversal (en términos de un desarrollo en modos normales) puede escribirse

$$\dot{y}(x, t) = \sum_n A_n\omega_n\sin(k_n x)\cos(\omega_n t) \tag{52}$$

Y la amplitud de excitación de cada modo normal $A_n$ puede hallarse mediante

$$A_n\omega_n = \frac{2}{2L}\int_0^{2L} \dot{y}(x, t = 0)\sin(k_n x)\,dx \tag{53}$$

$$A_n = \frac{1}{\omega_n L}\left[\int_{L-a}^{L} v_0\sin(k_n x)\,dx - \int_{L}^{L+a} v_0\sin(k_n x)\,dx\right] \tag{54}$$

$$A_n = -\frac{v_0}{\omega_n k_n L}\left[\cos(k_n x)\big|_{L-a}^{L} - \cos(k_n x)\big|_{L}^{L+a}\right] \tag{55}$$

$$A_n = -\frac{v_0}{\omega_n k_n L}\left[\cos(k_n L) - \cos(k_n(L - a)) - \cos(k_n(L + a)) + \cos(k_n L)\right] \tag{56}$$

$$A_n = -\frac{v_0}{\omega_n k_n L}\left[2\cos(k_n L) - 2\cos(k_n L)\cos(k_n a)\right] \tag{57}$$

$$A_n = -\frac{2v_0}{\omega_n k_n L}\left(1 - \cos(k_n a)\right)\cos(k_n L) \tag{58}$$

$$A_n = -\frac{v_0\,8L}{v\,n^2\pi^2}\left[1 - \cos\left(\frac{n\pi}{2}\frac{a}{L}\right)\right]\cos\left(\frac{n\pi}{2}\right) \tag{59}$$

$$A_n = -\frac{v_0\,8L}{\sqrt{\frac{T}{\mu}}\,n^2\pi^2}\left[1 - \cos\left(\frac{n\pi}{2}\frac{a}{L}\right)\right]\cos\left(\frac{n\pi}{2}\right) \tag{60}$$

De la última ecuación vemos que el modo $n = 1$ no está excitado. También podríamos haber visto que este modo no se excitaría por razones de simetría, ya que el modo $n = 1$ es simétrico respecto del centro de la cuerda, mientras que las condiciones iniciales son antisimétricas. Análogamente, cualquier modo que sea simétrico respecto del centro de la cuerda no estará excitado.

**(5.c)** El desplazamiento se divide en dos ondas que se propagan en sentidos opuestos, cada una con altura $h = \dfrac{a v_0}{\sqrt{T/\mu}}$.

## Solución del problema 6

**(6.a)** Suponiendo que el amortiguamiento de la carga es despreciable, el movimiento de la partícula es simplemente el de un oscilador armónico simple, cuya solución es

$$x(t) = A\cos(\omega_0 t) \tag{61}$$

$$\ddot{x}(t) = -A\omega_0^2\cos(\omega_0 t) \tag{62}$$

con $\omega_0 = \sqrt{k/m}$. Ahora bien, el campo eléctrico viene dado por

$$\vec{E}(\vec{R}, t) = -\frac{q\vec{a}_\perp(t')}{4\pi\varepsilon_0 Rc^2} = -\frac{q\left(\hat{n}\times(\hat{n}\times\vec{a}(t'))\right)}{4\pi\varepsilon_0 Rc^2} \tag{63}$$

donde $\hat{n}$ es el vector unitario que apunta de la fuente al observador. En el plano $x$-$z$ tenemos $\hat{n} = \sin\theta\,\hat{x} + \cos\theta\,\hat{z}$. Así pues, el campo eléctrico viene dado por

$$\frac{qA\omega_0^2}{4\pi\varepsilon_0 c^2 R}\cos\left(\omega_0(t - R/c)\right)\left(\cos^2\theta\,\hat{x} - \cos\theta\sin\theta\,\hat{z}\right) \tag{64}$$

**(6.b)** La potencia total radiada por la partícula viene dada directamente por la fórmula de Larmor:

$$P(t) = \frac{q^2 a^2(t')}{6\pi\varepsilon_0 c^3} = \frac{q^2 A^2\omega_0^4\cos^2\left(\omega_0(t - R/c)\right)}{6\pi\varepsilon_0 c^3} \tag{65}$$

Promediando en el tiempo se obtiene

$$\langle P\rangle = \frac{q^2 A^2\omega_0^4}{12\pi\varepsilon_0 c^3} \tag{66}$$

**(6.c)** Con la suposición de que la potencia radiada no cambia mucho con el tiempo, el tiempo $t$ que tardaría la amplitud original del movimiento en reducirse a $1/e$ de su valor puede hallarse mediante

$$\frac{1}{2}m\omega_0^2 A^2 - \langle P\rangle t = \frac{1}{2}m\omega_0^2\left(\frac{A}{e}\right)^2 \tag{67}$$

$$\Rightarrow t = \frac{m\omega_0^2 A^2}{2\langle P\rangle}\left(1 - \left(\frac{1}{e}\right)^2\right) \tag{68}$$

$$t \approx 0.86\times\frac{6\pi m\varepsilon_0 c^3}{q^2\omega_0^2} \tag{69}$$

Esta suposición no es del todo realista, ya que la potencia radiada por la carga es proporcional al cuadrado de la amplitud de su movimiento, y la amplitud del movimiento va disminuyendo a medida que se radia energía. Este método siempre subestimará el tiempo necesario para que la amplitud disminuya.

**(6.d)** La energía $E$ viene dada por

$$E = \frac{m\omega_0^2 A^2}{2} \tag{70}$$

de modo que tenemos

$$\frac{dA}{dE} = \frac{1}{m\omega_0^2 A} \tag{71}$$

mientras que la potencia media radiada por ciclo es la que hallamos en el apartado (b):

$$\frac{dE}{dt} = \langle P\rangle = \frac{q^2 A^2\omega_0^4}{12\pi\varepsilon_0 c^3} \tag{72}$$

Combinando ambas para hallar $dA/dt$ obtenemos

$$\frac{dA}{dt} = \frac{dA}{dE}\frac{dE}{dt} = \left(\frac{1}{m\omega_0^2 A}\right)\left(\frac{q^2 A^2\omega_0^4}{12\pi\varepsilon_0 c^3}\right) = \frac{q^2 A\omega_0^2}{12\pi\varepsilon_0 c^3 m} \tag{73}$$

Integrando ahora para hallar el tiempo necesario para que la amplitud disminuya de $A$ a $A/e$, tenemos

$$\int_{A/e}^{A}\frac{dA}{A} = \frac{q^2\omega_0^2}{12\pi\varepsilon_0 c^3 m}\int dt \tag{74}$$

$$\ln(A) - \ln(A/e) = \ln(e) = 1 = \left(\frac{q^2\omega_0^2}{12\pi\varepsilon_0 c^3 m}\right)t \tag{75}$$

de modo que el tiempo $t$ viene dado por

$$t = \frac{12\pi\varepsilon_0 c^3 m}{q^2\omega_0^2} \tag{76}$$

---

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*
