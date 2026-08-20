# 8.03-vibraciones-ondas-es — curso completo

Traducción no oficial de materiales de MIT OpenCourseWare, con asistencia
de IA. Licencia CC BY-NC-SA 4.0. Fórmulas en LaTeX.


---

<!-- MIT8.03_Examen1_ES.md -->

# Examen 1 (otoño de 2016)

**Instituto Tecnológico de Massachusetts**

**Física 8.03, otoño de 2016**

**EXAMEN 1**

## Instrucciones

Escriba sus soluciones en los cuadernillos blancos. No se corregirá nada de lo escrito en la copia del examen. Este examen es a libro cerrado. No se permite ningún equipo electrónico. Todos los teléfonos, blackberries, blueberries, raspberry Pi, tabletas, ordenadores, etc. deben estar apagados.

------------------------------------------------------------------------

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

$$\mathcal{X}(t) = \begin{pmatrix} x_1(t) \\ x_2(t) \end{pmatrix}$$

$$K = \begin{pmatrix} K_{11} & K_{12} \\ K_{21} & K_{22} \end{pmatrix}$$

$$M = \begin{pmatrix} m_1 & 0 \\ 0 & m_2 \end{pmatrix}$$

Ecuación matricial del movimiento; las matrices $M$, $K$, $I$ son $n \times n$ y los vectores $\mathcal{X}$, $\mathcal{Z}$ son $n \times 1$:

$$\frac{d^2}{dt^2}\mathcal{X}(t) = -M^{-1}K\,\mathcal{X}(t)$$

$$\mathcal{Z}(t) = Ae^{-i\omega t}$$

$$(M^{-1}K - \omega^2 I)A = 0$$

Para obtener las frecuencias de los modos normales, resuelva:

$$\det(M^{-1}K - \omega^2 I) = 0$$

Para $n = 2$:

$$\det\begin{pmatrix} M_{11} & M_{12} \\ M_{21} & M_{22} \end{pmatrix} = M_{11}M_{22} - M_{12}M_{21}$$

Si el sistema está impulsado por una fuerza, se pueden hallar las amplitudes de respuesta $C(\omega_d)$:

$$F(t) = F_0 e^{-i\omega_d t}$$

$$W(t) = C(\omega_d)e^{-i\omega_d t}$$

$$C(\omega_d) = \begin{pmatrix} c_1(\omega_d) \\ c_2(\omega_d) \end{pmatrix}$$

$$(M^{-1}K - \omega_d^2 I)\,C(\omega_d) = F_0$$

Resolviendo la ecuación anterior se pueden hallar las amplitudes de respuesta del primer ($c_1(\omega_d)$) y del segundo ($c_2(\omega_d)$) objeto del sistema.

### Simetría de reflexión

Matriz de simetría de reflexión:

$$S = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$$

Autovalores ($\beta$) y autovectores ($A$) de esta matriz $S$ de $2 \times 2$:

1.  $\beta = -1$, $A = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$
2.  $\beta = 1$, $A = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$

Sistema acoplado unidimensional infinito que satisface la simetría de traslación espacial: dado un autovalor $\beta$, el autovector correspondiente es

$$A_j = \beta^j A_0$$

donde $A_j$ ($A_0$) es la amplitud normal del objeto $j$-ésimo ($0$-ésimo) del sistema.

Considere un sistema unidimensional formado por un número infinito de masas acopladas por muelles; $\beta$ puede escribirse como $\beta = e^{ika}$, donde $k$ es el número de onda y $a$ es la distancia entre las masas.

### Leyes de Kirchhoff

(¡Tenga cuidado con los signos!)

$$\text{Nodo:}\quad \sum_{i}^{n} I_i = 0 \qquad\qquad \text{Malla:}\quad \sum_{i}^{n} \Delta V_i = 0$$

$$\text{Condensadores:}\ \Delta V = \frac{Q}{C} \qquad \text{Bobinas:}\ \Delta V = -L\frac{dI}{dt} \qquad \text{Corriente:}\ I = \frac{dQ}{dt}$$

------------------------------------------------------------------------

## Problema 1 (30 puntos)

Resuelva las siguientes preguntas cortas.

**A.** Un estudiante de posgrado estaba realizando un experimento con un péndulo amortiguado obligado a moverse solo en la dirección $x$. La posición del péndulo en función del tiempo se muestra en la figura 1. Basándose en los datos experimentales, ¿se trata de un oscilador subamortiguado, sobreamortiguado o críticamente amortiguado? (5 puntos)

**B.** Dos vibraciones a lo largo de la misma cuerda se describen mediante las ecuaciones $y_1(t) = A\cos(3\pi t)$ e $y_2(t) = A\cos(4\pi t)$, donde $t$ está en segundos y $A$ vale 0.01 cm. Halle el periodo de batido de la superposición de ambas. (5 puntos)

**C.** Un péndulo pesado oscilaba bajo el agua con frecuencia angular $\omega_1$ (subamortiguado). ¿La frecuencia de oscilación aumentará, disminuirá o se mantendrá igual si se saca del agua todo el sistema? Explique por qué. (5 puntos)

**D.** Considere un oscilador con tres masas dispuestas en línea y conectadas por muelles. El oscilador tiene una simetría especular $x_1 \to -x_3$, $x_3 \to -x_1$ y $x_2 \to -x_2$. Escriba la matriz de simetría $S$ de este sistema. (5 puntos)

**E.** Explique brevemente por qué un oscilador subamortiguado forzado presenta a menudo respuestas grandes y aparentemente erráticas cuando se pone en marcha el mecanismo impulsor. (5 puntos)

**F.** Considere un oscilador mecánico simple de masa $m$ unido a un muelle de constante $k$. Puede establecerse una analogía estrecha entre este sistema y un circuito de una sola malla con una bobina $L$ y un condensador $C$ conectados en serie. Ambos osciladores siguen ecuaciones matemáticamente equivalentes. ¿Cuál es el equivalente eléctrico de la masa $m$ del sistema muelle-masa y de la constante del muelle $k$? (5 puntos)

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_Examen1_ES/fig1.png)

Figura 1: desplazamiento de un péndulo respecto a la posición de equilibrio. La gráfica representa la posición, en cm, frente al tiempo, de 0 a 200 segundos. La curva parte de un valor positivo próximo a 5 cm y decae hacia cero sin llegar a cruzarlo ni oscilar en torno a él.

------------------------------------------------------------------------

## Problema 2 (30 puntos)

Muchas medidas científicas de precisión requieren mesas libres de vibraciones. En la figura 2 se muestra un ejemplo. Considere una mesa de masa $m$ sostenida por 2 muelles ideales de constante $k = \frac{1}{2}m\omega_0^2$ y amortiguada por un amortiguador con fuerza de amortiguamiento $F = -m\Gamma v$, donde $v$ es la velocidad relativa entre el suelo y la mesa (NO la velocidad de la mesa). Suponga que el sistema está subamortiguado. Tanto el muelle como el amortiguador están firmemente unidos a la mesa y al suelo. Se produce un terremoto y el suelo vibra armónicamente en dirección vertical con frecuencia $\omega_d$ y amplitud $A$:

$$y_g(t) = A\cos(\omega_d t)$$

**a.** Escriba la ecuación del movimiento de la mesa en términos de $y(t)$, suponiendo que $y = 0$ representa la posición de equilibrio de la mesa antes del terremoto. (10 puntos)

**b.** Halle la amplitud de las vibraciones estacionarias de la mesa en función de la frecuencia de vibración del suelo $\omega_d$. (10 puntos)

**c.** Haga un esbozo de la amplitud estacionaria en función de $\omega_d$, indicando el valor de la amplitud para $\omega_d \sim 0$ y para $\omega_d \to \infty$. (10 puntos)

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_Examen1_ES/fig2.png)

Figura 2: mesa libre de vibraciones. La mesa, de masa $m$, descansa sobre dos muelles y un amortiguador que la unen al suelo, el cual vibra verticalmente.

------------------------------------------------------------------------

## Problema 3 (40 puntos)

Para el sistema de tres masas mostrado en la figura 3, los muelles ideales y las varillas del péndulo carecen de masa, y $x_1$, $x_2$ y $x_3$ se miden desde la posición de equilibrio estático (es decir, el muelle está relajado y el péndulo cuelga verticalmente). Todo el montaje está preparado en la Tierra, con la fuerza de la gravedad apuntando hacia abajo. Suponemos también que las amplitudes de oscilación de las tres masas son muy pequeñas y que no hay amortiguamiento ni fricción en el sistema. Puede suponer con seguridad que las masas solo se mueven en dirección horizontal.

**a.** Al comienzo del experimento, la tercera masa (la de forma de U, de masa $2m$) está fijada en $x_3 = 0$. Deduzca las ecuaciones acopladas del movimiento para las posiciones de las dos masas ($x_1$ y $x_2$). (6 puntos)

**b.** Escriba la matriz $M^{-1}K$ de $2 \times 2$. (4 puntos)

**c.** Resuelva las dos frecuencias de los modos normales. (6 puntos)

**d.** Evalúe las razones de amplitud de cada modo normal y describa el movimiento de cada modo normal mediante un esbozo. (8 puntos)

**e.** Escriba la expresión general del movimiento de las dos masas en términos de las frecuencias de los modos normales y cuatro coeficientes desconocidos. (4 puntos)

**f.** A partir de ahora, la tercera masa (de masa $2m$) se libera y puede moverse libremente en la dirección $x$. Deduzca las ecuaciones acopladas del movimiento para las posiciones de las tres masas ($x_1$, $x_2$ y $x_3$), sin resolverlas. (8 puntos)

**g.** Describa el movimiento de los tres modos normales mediante un esbozo, sin resolver las ecuaciones acopladas del movimiento. (4 puntos)

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_Examen1_ES/fig3.png)

Figura 3: osciladores formados por un péndulo acoplado y muelles ideales. Un péndulo y dos masas adicionales, una de ellas con forma de U y masa $2m$, están conectados mediante muelles ideales y se desplazan horizontalmente.

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*


---

<!-- MIT8.03_Examen2_ES.md -->

# Examen 2 (otoño de 2016)

**Instituto Tecnológico de Massachusetts**

**Física 8.03, otoño de 2016**

**EXAMEN 2**

## Instrucciones

Escriba sus soluciones en los cuadernillos blancos. No se corregirá nada de lo escrito en la copia del examen. Este examen es a libro cerrado. No se permite ningún equipo electrónico. Todos los teléfonos, blackberries, blueberries, raspberry Pi, tabletas, ordenadores, etc. deben estar apagados.

------------------------------------------------------------------------

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

1.  $\beta = -1$, $A = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$
2.  $\beta = 1$, $A = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$

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

------------------------------------------------------------------------

## Problema 1 (30 puntos)

Resuelva las siguientes preguntas cortas. (Si observa que está dedicando mucho tiempo a un problema, probablemente no va por el buen camino.)

**A.** (6 puntos) Una onda electromagnética plana progresiva se mueve hacia un conductor perfecto, en el que las cargas pueden moverse libremente sin disipación de energía. ¿Cuál es la condición de contorno para el campo eléctrico de la onda electromagnética en la superficie del conductor (no en su interior)?

**B.** (6 puntos) Una emisora de radio AM con frecuencia de radio $f$ ha recibido recientemente malas críticas por la calidad del audio. El director de la emisora le pide consejo. Usted descubre que una posibilidad para mejorar la calidad del audio es cambiar el ancho de banda $\Delta f$ de la señal emitida por la emisora, de modo que pueda enviar señales con mejor resolución temporal. ¿Le aconsejaría aumentar o disminuir el ancho de banda $\Delta f$? ¿Por qué lo cree así?

**C.** (6 puntos) En una habitación de dimensiones $L \times L \times 16L$, ¿cuál es la frecuencia angular más baja de los modos normales de oscilación del aire de la habitación? (Puede suponer que la velocidad del sonido es $v$.)

**D.** (6 puntos) Considere una cuerda con masa y extremos fijos, de longitud $2L$, tensión $T$ y densidad lineal de masa $\rho_L$. En $t = 0$, esta cuerda tiene la forma inicial $\psi(x, 0)$ que se muestra en la figura 1. La cuerda se suelta entonces con cuidado, de modo que la velocidad inicial de la cuerda $\dot{\psi}(x, 0)$ es 0. ¿Cuánto tarda esta cuerda, un medio no dispersivo, en volver a su forma inicial después de soltarla en $t = 0$? Dé sus explicaciones sin realizar realmente la descomposición de Fourier.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_Examen2_ES/fig1.png)

Figura 1: cuerda «MIT». La forma inicial de la cuerda dibuja las letras MIT a lo largo de su longitud.

**E.** (6 puntos) Un haz de luz viaja por el vacío ($n_1 = 1$) antes de alcanzar dos láminas transparentes de índices de refracción $n_2$ y $n_3$. Llega primero a una lámina transparente de índice $n_2$ con un ángulo de incidencia $\alpha = 60^\circ$. El haz la atraviesa, alcanza otra lámina transparente de índice $n_3$, la atraviesa y entra en un cuarto material de índice $n_4$, propagándose en ese medio con un ángulo $\beta = 45^\circ$ respecto al eje normal. La configuración de este experimento óptico se muestra en la figura 2. ¿Cuál es el valor de $n_4$?

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_Examen2_ES/fig2.png)

Figura 2: experimento con luz. El haz atraviesa sucesivamente las láminas de índices $n_2$ y $n_3$ hasta entrar en el medio de índice $n_4$, con los ángulos $\alpha$ y $\beta$ medidos respecto a la normal.

------------------------------------------------------------------------

## Problema 2 (17 puntos)

Las fluctuaciones de la densidad de carga en un plasma se rigen por una ecuación de ondas que, para distorsiones unidimensionales, se reduce a

$$a^2\frac{\partial^2 \rho(x, t)}{\partial x^2} - \Omega_p^2\,\rho(x, t) = \frac{\partial^2 \rho(x, t)}{\partial t^2}$$

Aquí $\rho(x, t)$ es una pequeña desviación de la densidad de carga respecto a su valor de equilibrio y $\Omega_p$ es un parámetro constante denominado frecuencia de plasma.

**a.** (3 puntos) Escriba una solución de onda armónica progresiva que describa la desviación de la densidad de carga $\rho(x, t)$, que avanza en la dirección $-\hat{x}$. Suponemos que el número de onda de esta onda progresiva es $k$, la frecuencia angular es $\omega$ y la amplitud es $A$. En $t = 0$ y $x = 0$, la desviación de la densidad de carga $\rho(0, 0)$ es cero.

**b.** (7 puntos) Halle la relación de dispersión $\omega(k)$. Dibuje $\omega(k)$ en función de $k$. ¿Cuáles son las frecuencias angulares de las ondas armónicas progresivas que pueden existir en el plasma?

**c.** (4 puntos) ¿Cuál es la velocidad de grupo de este medio? ¿Es un medio dispersivo?

**d.** (3 puntos) ¿Cuál es la velocidad de fase límite para números de onda $k$ grandes en este medio?

------------------------------------------------------------------------

## Problema 3 (23 puntos)

El campo eléctrico de una onda plana uniforme en el vacío, que viaja a la velocidad de la luz $c$, viene dado por

$$\vec{E}(\vec{r}, t) = E_0(3\hat{x} + a\hat{y})\cos(\omega t - 4x + 3y)$$

donde $a$ es una constante. (Este es un problema en el espacio tridimensional.)

**a.** (4 puntos) ¿Cuál es la dirección de propagación de esta onda plana? (Represente la dirección como un vector unitario.)

**b.** (6 puntos) Calcule la frecuencia angular $\omega$ y la longitud de onda de esta onda electromagnética usando los números dados.

**c.** (4 puntos) ¿Cuál es el valor de $a$?

**d.** (6 puntos) ¿Cuál es el campo magnético $\vec{B}$ asociado a esta onda?

**e.** (3 puntos) ¿Cuál es la densidad de flujo de energía direccional (la tasa de transferencia de energía por unidad de área) de esta onda electromagnética?

------------------------------------------------------------------------

## Problema 4 (30 puntos)

Una cuerda de tensión $T$, masa por unidad de longitud $\rho_L$ y longitud $L$ adopta la forma mostrada en la figura 3. La cuerda solo puede moverse hacia arriba y hacia abajo en la dirección $\hat{y}$. El extremo izquierdo de la cuerda está fijado a una pared y el extremo derecho está unido a un anillo sin masa que puede moverse libremente en la dirección transversal sin fricción. En este problema se desprecia la gravedad, y puede suponer la aproximación de ángulos pequeños para toda la cuerda. La cuerda se suelta desde el reposo en $t = 0$.

**a.** (8 puntos) Escriba las condiciones de contorno en $x = 0$ y $x = L$. Puede escribir la condición en términos de $\psi(x, t)$, que es el desplazamiento de la cuerda con masa en la dirección $\hat{y}$ respecto a la posición de equilibrio.

**b.** (6 puntos) Esboce la forma ($\psi$ en función de $x$) de los tres modos normales más bajos (independientemente de si están excitados o no) y dé las frecuencias angulares correspondientes.

**c.** (10 puntos) Para la forma inicial mostrada en la figura 3, calcule la amplitud del $n$-ésimo modo normal en términos de $n$ y $H$.

**d.** (6 puntos) ¿Qué modos normales no se excitarán? Exprese sus resultados en términos de $n$.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_Examen2_ES/fig3.png)

Figura 3: forma inicial de la cuerda en el instante $t = 0$. La cuerda parte de la pared en $x = 0$ y alcanza una altura máxima $H$ antes de llegar al anillo del extremo derecho, en $x = L$.

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*


---

<!-- MIT8.03_ExamenFinalPractica1_ES.md -->

# Examen final de práctica 1

**INSTITUTO TECNOLÓGICO DE MASSACHUSETTS — DEPARTAMENTO DE FÍSICA**

**Física 8.03: Vibraciones y Ondas**

## Instrucciones

1.  No retire ninguna página del examen, salvo la hoja de fórmulas.
2.  Este es un examen a libro cerrado.
3.  Realice los SEIS (6) problemas.
4.  MUESTRE TODO SU TRABAJO. Escriba su nombre en cada hoja.
5.  NO SE PERMITEN CALCULADORAS, LIBROS, ORDENADORES NI TELÉFONOS MÓVILES.

**Puntuación:** Problema 1: 16 · Problema 2: 16 · Problema 3: 16 · Problema 4: 16 · Problema 5: 18 · Problema 6: 18

------------------------------------------------------------------------

## Hoja de fórmulas

La ecuación diferencial

$$\ddot{x} + \gamma\dot{x} + \omega_0^2 x = f\cos(\omega t + \varphi)\qquad\text{(1)}$$

tiene las soluciones generales

$$\frac{\gamma}{2} < \omega_0: \qquad X(t) = A_1 e^{-\left(\frac{\gamma}{2}\right)t}\cos(\omega' t + \beta) + X_p(t)\qquad\text{(2)}$$

$$\frac{\gamma}{2} = \omega_0: \qquad X(t) = (A_1 + A_2 t)e^{-\left(\frac{\gamma}{2}\right)t} + X_p(t)\qquad\text{(3)}$$

$$\frac{\gamma}{2} > \omega_0: \qquad X(t) = A_1 e^{-\Gamma_+ t} + A_2 e^{-\Gamma_- t} + X_p(t)\qquad\text{(4)}$$

con

$$X_p(t) = A(\omega)\cos(\omega t - \delta(\omega) + \varphi)\qquad\text{(5)}$$

y

$$\omega' = \sqrt{\omega_0^2 - \frac{\gamma^2}{4}} \qquad\qquad \Gamma_\pm = \frac{\gamma}{2} \pm \sqrt{\frac{\gamma^2}{4} - \omega_0^2}\qquad\text{(6)}$$

$$A(\omega) = f\Big/\sqrt{(\omega_0^2 - \omega^2)^2 + (\gamma\omega)^2} \qquad\qquad \tan(\delta(\omega)) = \gamma\omega/(\omega_0^2 - \omega^2)\qquad\text{(7)}$$

### Relaciones idealizadas para la tensión en los elementos de un circuito

1.  Condensador: $V_C = \dfrac{Q}{C}$
2.  Resistencia: $V_R = IR$
3.  Autoinducción: $V_L = L\dfrac{dI}{dt}$

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

------------------------------------------------------------------------

## Problema 1 (16 puntos)

El campo eléctrico de un modo TE en una guía de ondas rectangular, perfectamente conductora e infinitamente larga en la dirección $x$ (con $a < b$), viene dado por

$$\vec{E}(x, y, z, t) = E_0\cos(k_y y + \varphi_y)\cos(k_x x - \omega t)\hat{z}\qquad\text{(8)}$$

**(1.a)** (4 puntos) Halle $k_y$ y $\varphi_y$ que satisfacen las condiciones de contorno.

**(1.b)** (4 puntos) Escriba la relación de dispersión de este modo de la guía de ondas.

**(1.c)** (4 puntos) ¿Cuál es la frecuencia más baja que se propagará en este modo?

**(1.d)** (4 puntos) ¿Cuál es el campo magnético $\vec{B}(x, y, z, t)$ asociado al campo eléctrico de este modo?

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenFinalPractica1_ES/fig1.png)

Figura 1: guía de ondas perfectamente conductora, de sección rectangular con lados $a$ y $b$.

------------------------------------------------------------------------

## Problema 2 (16 puntos)

La figura muestra un sistema de masas. La masa $2m$ está conectada a una pared inmóvil mediante un muelle de constante $2k$, mientras que la masa $m$ está conectada a una pared inmóvil mediante un muelle de constante $k$. Las masas están acopladas entre sí mediante una banda elástica de longitud $L$, sometida a una tensión $T = 2kL$. Las masas están obligadas a moverse solo en la dirección $x$. En el equilibrio, las masas tienen la misma posición $x$ y los muelles no están comprimidos. No hay fricción ni gravedad. Los desplazamientos respecto del equilibrio son lo bastante pequeños ($x_1, x_2 \ll L$) como para que la tensión de la banda permanezca constante.

**(2.a)** (5 puntos) Escriba las ecuaciones diferenciales acopladas que describen el desplazamiento de las masas respecto del equilibrio $\{x_1, x_2\}$.

**(2.b)** (7 puntos) Halle las frecuencias de los modos normales del sistema.

**(2.c)** (4 puntos) Esboce los modos normales del sistema, indicando claramente tanto la magnitud como la dirección del movimiento de las masas.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenFinalPractica1_ES/fig2.png)

Figura 2: sistema de osciladores acoplados.

------------------------------------------------------------------------

## Problema 3 (16 puntos)

**(3.a)** (5 puntos) Una fibra óptica consiste en una varilla maciza de un material de índice de refracción $n_f$ rodeada por una envoltura cilíndrica de material de índice $n_c$. Halle el mayor ángulo $\theta$ tal que una onda que incide sobre la varilla maciza desde el aire, de índice $n_a$, permanezca dentro de la varilla (exprese su respuesta en términos de $n_f$, $n_c$ y $n_a$).

**(3.b)** (4 puntos) Luz no polarizada que se propaga en el vacío se refleja en la superficie de un líquido de índice $n$. El rayo reflejado incide sobre una pantalla situada a 25 cm, a una altura de 20 cm, y se observa que está polarizado al 100 %. ¿Cuánto vale $n$?

**(3.c)** (7 puntos) Considere un medio en el que las ondas se propagan con la relación de dispersión

$$\omega^2 = \omega_0^2 + A^2 k^2\qquad\text{(9)}$$

donde $\omega$ es la frecuencia angular de la onda, $k$ es el número de onda, y $\omega_0$ y $A$ son constantes reales.

1.  ¿Cuál es el rango de frecuencias $\omega$ para las que pueden propagarse ondas?

2.  Calcule $v_{\text{fase}}$ y $v_{\text{grupo}}$. Haga un esbozo cuidadosamente etiquetado de cada una en función de $\omega$.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenFinalPractica1_ES/fig3.png)

Figura 3: fibra óptica. Figura 4: gráficas para representar las velocidades de fase y de grupo.

------------------------------------------------------------------------

## Problema 4 (16 puntos)

Un haz monocromático incide sobre $N$ rendijas, lo que da lugar a un patrón de intensidad en función del ángulo sobre una pantalla situada a cierta distancia. Cada rendija tiene una anchura $D$ y la distancia entre los centros de las rendijas es $d$. La distancia entre la pantalla y las rendijas es muy grande.

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenFinalPractica1_ES/fig4.png)

Figura 4

A partir del patrón, deduzca lo siguiente:

**(4.a)** (6 puntos) El número de rendijas $N$ sobre las que incide el haz. Explique su razonamiento.

**(4.b)** (6 puntos) La razón $d/D$. Explique su razonamiento.

**(4.c)** (4 puntos) Suponga ahora que la anchura de las rendijas se reduce hasta $\sim 0$, mientras que la intensidad del haz monocromático se aumenta de modo que la intensidad del máximo central no cambia. Sobre la gráfica que muestra el patrón de intensidad original (en línea discontinua), dibuje el patrón de intensidad resultante.

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenFinalPractica1_ES/fig5.png)

Figura 5: patrón de interferencia debido a $N$ rendijas. Figura 6: gráfica para dibujar el patrón resultante cuando $D \to 0$.

------------------------------------------------------------------------

## Problema 5 (18 puntos)

Una cuerda de longitud $2L$ y densidad de masa $\mu$ se somete a una tensión $T$ y está fija por ambos extremos. En el instante $t = 0$, el desplazamiento de la cuerda es nulo en todas partes, pero se la golpea de modo que se imparte una velocidad transversal a una sección de la cuerda. Las condiciones iniciales de la cuerda son (con $a \ll L$):

![Figura 6](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenFinalPractica1_ES/fig6.png)

Figura 6

$$y(x, t = 0) = 0\qquad\text{(10)}$$

$$\dot{y}(x, t = 0) = \begin{cases} v_0 & : L - a \leq x < L \\ -v_0 & : L \leq x < L + a \\ 0 & : \text{en el resto} \end{cases}\qquad\text{(11)}$$

**(5.a)** (3 puntos) Esboce los tres primeros modos normales de vibración de esta cuerda, independientemente de si están excitados o no.

**(5.b)** (10 puntos) ¿Cuál es la amplitud del $n$-ésimo modo normal después de golpear la cuerda? ¿Cuál es el modo más bajo no excitado?

**(5.c)** (5 puntos) Esboce el desplazamiento de la cuerda en el instante $t = \dfrac{L}{2}\sqrt{\dfrac{\mu}{T}}$.

![Figura 7](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenFinalPractica1_ES/fig7.png)

Figura 7: velocidad transversal inicial de la cuerda en $t = 0$; el desplazamiento inicial es nulo en todas partes. Figuras 8 y 9: gráficas para representar los tres primeros modos normales y el desplazamiento de la cuerda.

*\[Nota de la traducción: el encabezado de este problema en el PDF original indica «20 Points», mientras que la tabla de puntuaciones de la portada le asigna 18. Se ha mantenido el valor de la tabla, coherente con el total de 100 puntos del examen.\]*

![Figura 8](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenFinalPractica1_ES/fig8.png)

Figura 8

------------------------------------------------------------------------

## Problema 6 (18 puntos)

Una partícula cargada de masa $M$ y carga $+Q$ está unida al extremo de un muelle de constante $k$. El muelle se encuentra a lo largo del eje $x$ y el punto de equilibrio está en el origen. La partícula se desplaza del equilibrio una distancia $A$ en la dirección $x$ y se suelta en $t = 0$. Suponga que el tamaño de la partícula es mucho menor que $A$, de modo que puede tratarse como una carga puntual, y que la tasa de amortiguamiento es muy pequeña.

**(6.a)** (4 puntos) Calcule el campo eléctrico radiado por la partícula a lo largo de una dirección arbitraria del plano $x$-$z$, a una distancia $R$, donde $R \gg A$.

**(6.b)** (4 puntos) Calcule la potencia total promediada en el tiempo radiada por la partícula.

**(6.c)** (6 puntos) Suponiendo que la potencia radiada no cambia apreciablemente en función del tiempo, dé una estimación sencilla y aproximada del tiempo que tardará la partícula en reducir su amplitud de oscilación a $1/e$ de su valor inicial. ¿Es realista esta suposición?

**(6.d)** (4 puntos) Puede obtenerse una estimación más refinada usando que $dA/dt = (dA/dE)\times(dE/dt)$, y empleando la potencia media radiada en un ciclo para $dE/dt$. Úselo para calcular el tiempo que tardará la partícula en reducir su amplitud de oscilación a $1/e$ de su valor inicial.

![Figura 10](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenFinalPractica1_ES/fig10.png)

Figura 10: carga oscilante.

------------------------------------------------------------------------

# Soluciones

## Solución del problema 1

**(1.a)** Necesitamos que $E_\parallel \to 0$ en el contorno con el conductor. El campo eléctrico está en la dirección $\hat{z}$, así que necesitamos $E = 0$ en (i) $y = 0$ y en (ii) $y = b$. La condición (i) implica que $\varphi_y = \pm\frac{\pi}{2}$, de modo que $E \propto \sin(k_y y)$. La condición (ii) implica que $k_y = \frac{n\pi}{a}$, donde $n$ es un entero mayor que cero. Podemos, por tanto, reescribir el campo eléctrico como

$$E(x, y, z, t) = E_0\sin\left(\frac{n\pi}{a}y\right)\cos(k_x x - \omega t)\hat{z}\qquad\text{(2)}$$

*\[Nota de la traducción: el original sitúa la segunda pared en $y = b$, pero a partir de aquí todas sus expresiones usan $a$ como dimensión transversal (incluida la frecuencia de corte del apartado 1.c). Se han conservado tal cual; para que el desarrollo sea coherente, la pared de la condición (ii) debe entenderse en $y = a$.\]*

**(1.b)** Podemos obtener la relación de dispersión a partir de la ecuación de ondas:

$$\nabla^2\vec{E} - \frac{1}{c^2}\frac{\partial^2\vec{E}}{\partial t^2} = 0\qquad\text{(3)}$$

Sustituyendo la solución de $\vec{E}$ en la ecuación de ondas encontramos

$$\frac{\omega^2}{c^2} = k_x^2 + k_y^2\qquad\text{(4)}$$

$$\frac{\omega^2}{c^2} = k_x^2 + \left(\frac{n\pi}{a}\right)^2\qquad\text{(5)}$$

$$\Rightarrow k_x = \sqrt{\frac{\omega^2}{c^2} - \left(\frac{n\pi}{a}\right)^2}\qquad\text{(6)}$$

**(1.c)** La frecuencia más baja que se propaga ocurre para $n = 1$; en este caso la relación de dispersión queda

$$k_x = \sqrt{\frac{\omega^2}{c^2} - \left(\frac{\pi}{a}\right)^2}\qquad\text{(7)}$$

de modo que la frecuencia más baja que da lugar a un número de onda no imaginario es

$$\omega_{\text{corte}} = \frac{\pi c}{a}\qquad\text{(8)}$$

$$\Rightarrow f_{\text{corte}} = \frac{c}{2a}\qquad\text{(9)}$$

**(1.d)** Podemos hallar el campo magnético asociado a este modo mediante la ley de Faraday:

$$\nabla\times\vec{E} = -\frac{\partial\vec{B}}{\partial t}\qquad\text{(10)}$$

$$\begin{vmatrix} \hat{x} & \hat{y} & \hat{z} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ 0 & 0 & E_z \end{vmatrix} = -\frac{\partial\vec{B}}{\partial t}\qquad\text{(11)}$$

$$E_0 k_y\cos(k_y y)\cos(k_x x - \omega t)\hat{x} + E_0\sin(k_y y)k_x\sin(k_x x - \omega t)\hat{y} = -\frac{\partial\vec{B}}{\partial t}\qquad\text{(12)}$$

$$\vec{B}(x, y, z, t) = E_0\frac{k_y}{\omega}\cos(k_y y)\sin(k_x x - \omega t)\hat{x} - E_0\frac{k_x}{\omega}\sin(k_y y)\cos(k_x x - \omega t)\hat{y}\qquad\text{(13)}$$

## Solución del problema 2

**(2.a)** Para $x_1$ tenemos, por la ley de Newton,

$$2m\ddot{x}_1 = -2kx_1 - T\sin\theta\qquad\text{(14)}$$

donde $\sin\theta = (x_1 - x_2)/L$. Sustituyendo, encontramos

$$2m\ddot{x}_1 = -\left(2k - \frac{T}{L}\right)x_1 + \frac{T}{L}x_2\qquad\text{(15)}$$

$$\ddot{x}_1 = -\left(\frac{k}{m} - \frac{T}{2mL}\right)x_1 + \frac{T}{2mL}x_2\qquad\text{(16)}$$

$$\ddot{x}_1 = \frac{-2k}{m}x_1 + \frac{k}{m}x_2\qquad\text{(17)}$$

Mientras que para $x_2$ encontramos

$$m\ddot{x}_2 = -kx_2 + T\sin\theta\qquad\text{(18)}$$

$$m\ddot{x}_2 = -\left(k - \frac{T}{L}\right)x_2 + \frac{T}{L}x_1\qquad\text{(19)}$$

$$\ddot{x}_2 = \frac{2k}{m}x_1 - \frac{3k}{m}x_2\qquad\text{(20)}$$

Llamando ahora $\omega_0^2 = k/m$, podemos reescribirlas como

$$\ddot{x}_1 = -2\omega_0^2 x_1 + \omega_0^2 x_2\qquad\text{(21)}$$

$$\ddot{x}_2 = 2\omega_0^2 x_1 - 3\omega_0^2 x_2\qquad\text{(22)}$$

**(2.b)** En forma matricial podemos reescribir las ecuaciones del movimiento (usando el ansatz $\ddot{x}_i = -\omega^2 x_i$):

$$\begin{pmatrix} -2\omega_0^2 & \omega_0^2 \\ 2\omega_0^2 & -3\omega_0^2 \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = -\omega^2\begin{pmatrix} x_1 \\ x_2 \end{pmatrix}\qquad\text{(23)}$$

Y resolviendo para los posibles valores de $\omega$ tenemos

$$\begin{pmatrix} -2\omega_0^2 + \omega^2 & \omega_0^2 \\ 2\omega_0^2 & -3\omega_0^2 + \omega^2 \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = 0\qquad\text{(24)}$$

$$\left(-2\omega_0^2 + \omega^2\right)\left(-3\omega_0^2 + \omega^2\right) - 2\omega_0^4 = 0\qquad\text{(25)}$$

$$6\omega_0^4 - 5\omega_0^2\omega^2 + \omega^4 - 2\omega_0^4 = 0\qquad\text{(26)}$$

$$\left(4\omega_0^2 - \omega^2\right)\left(\omega_0^2 - \omega^2\right) = 0\qquad\text{(27)}$$

De modo que los dos valores posibles de $\omega$ son

$$\omega_1 = \omega_0 = \sqrt{\frac{k}{m}}\qquad\text{(28)}$$

y

$$\omega_2 = 2\omega_0 = 2\sqrt{\frac{k}{m}}\qquad\text{(29)}$$

**(2.c)** En el modo 1 ($\omega_1$), la razón de las amplitudes del movimiento de las masas es

$$x_2/x_1 = 1\qquad\text{(30)}$$

Mientras que en el modo 2 ($\omega_2$), la razón de las amplitudes del movimiento de las masas es

$$x_2/x_1 = -2\qquad\text{(31)}$$

## Solución del problema 3

**(3.a)** Todos los rayos de la varilla maciza que inciden sobre la envoltura cilíndrica con un ángulo menor que el ángulo crítico $\theta_c = \sin^{-1}(n_c/n_f)$ quedarán atrapados en la varilla. Por tanto, el mayor ángulo $\theta$ que puede incidir sobre la varilla y permanecer dentro viene dado por

$$n_a\sin\theta = n_f\sin\theta_2\qquad\text{(32)}$$

$$\theta_2 = \frac{\pi}{2} - \theta_c\qquad\text{(33)}$$

$$\Rightarrow \sin\theta = \frac{n_f}{n_a}\sin\left(\frac{\pi}{2} - \theta_c\right)\qquad\text{(34)}$$

$$\Rightarrow \theta = \sin^{-1}\left(\frac{n_f}{n_a}\sin\left(\frac{\pi}{2} - \theta_c\right)\right)\qquad\text{(35)}$$

O, de forma equivalente, podemos escribir

$$\frac{n_a}{n_f}\sin\theta = \sin\theta_2 = \frac{\sqrt{n_f^2 - n_c^2}}{n_f}\qquad\text{(36)}$$

$$\sin\theta = \frac{n_f}{n_a}\left(\frac{\sqrt{n_f^2 - n_c^2}}{n_f}\right)\qquad\text{(37)}$$

$$\theta = \sin^{-1}\left(\frac{1}{n_a}\sqrt{n_f^2 - n_c^2}\right)\qquad\text{(38)}$$

**(3.b)** Si la luz reflejada está polarizada al 100 %, debe incidir con el ángulo de Brewster. Así pues,

$$\theta_B = \tan^{-1}(n_2/n_1) = \tan^{-1}(n_2) = \frac{\pi}{2} - \tan^{-1}(20/25)\qquad\text{(39)}$$

$$\Rightarrow n_2 = \tan\left(\frac{\pi}{2} - \tan^{-1}(4/5)\right)\qquad\text{(40)}$$

O, más sencillamente, podemos escribir

$$\tan^{-1}(n_2/n_1) = \theta_B\qquad\text{(41)}$$

$$\tan\theta_B = 25/20 = 5/4\qquad\text{(42)}$$

$$\Rightarrow \tan\left(\tan^{-1}(n_2/n_1)\right) = 5/4\qquad\text{(43)}$$

$$\Rightarrow n_2 = 5/4\qquad\text{(44)}$$

**(3.c)** (i) Reordenando la relación de dispersión, encontramos que el número de onda en función de la frecuencia viene dado por

$$k = \frac{1}{A}\sqrt{\omega^2 - \omega_0^2}\qquad\text{(46)}$$

*\[Nota de la traducción: el PDF original escribe en esta ecuación $k = \frac{1}{A}\sqrt{\omega_0^2 + A^2k^2}$, expresión circular que no despeja $k$. Lo que se obtiene al despejar la relación de dispersión (45) es $k = \frac{1}{A}\sqrt{\omega^2 - \omega_0^2}$, que es además la que usa el propio desarrollo posterior.\]*

De modo que la frecuencia más baja que da lugar a un número de onda no imaginario es $\omega = \omega_0$, así que el rango de frecuencias que pueden propagarse es $\omega_0 < \omega < \infty$.

1.  La velocidad de fase viene dada por $\omega/k$, de modo que encontramos

$$v_p = \omega/k = \frac{\omega}{\frac{1}{A}\sqrt{\omega^2 - \omega_0^2}} = \frac{A\omega}{\sqrt{\omega^2 - \omega_0^2}}\qquad\text{(47)}$$

Mientras que la velocidad de grupo viene dada por $\dfrac{d\omega}{dk}$:

$$v_g = \frac{d\omega}{dk} = \frac{A^2 k}{\omega} = A\sqrt{1 - \left(\frac{\omega_0}{\omega}\right)^2}\qquad\text{(48)}$$

## Solución del problema 4

**(4.a)** Hay tres pequeños lóbulos entre picos. Por tanto, $N = 5$ (obsérvese que habrá $N - 2$ lóbulos pequeños en un patrón de interferencia de $N$ rendijas).

**(4.b)** En primer lugar, recuerde que los picos de interferencia aparecen en $\dfrac{n\lambda}{d}$, mientras que los mínimos de difracción aparecen en $\dfrac{m\lambda}{D}$, donde $n$ y $m$ son enteros. En el patrón de interferencia se aprecian los picos 0.º, 1.º, 2.º y 3.º, pero no se ve el 4.º. Esto significa que el 4.º pico queda cancelado por el mínimo de difracción. Observamos entonces que el primer mínimo de difracción y el cuarto pico de interferencia están en la misma posición. Por tanto, $\dfrac{4\lambda}{d} = \dfrac{\lambda}{D}$, y en consecuencia $d/D = 4$.

**(4.c)** Recordamos de la demostración vista en clase que, a medida que se reduce el tamaño de una rendija, el patrón de difracción se ensancha; en el límite en que la anchura de las rendijas tiende a cero, el patrón de difracción se ensancha infinitamente, de modo que ya no modula el patrón de interferencia.

## Solución del problema 5

**(5.b)** En este caso, el desplazamiento de la cuerda puede expresarse como una suma de modos normales de la forma

$$y(x, t) = \sum_n A_n\sin(k_n x)\sin(\omega_n t + \phi)\qquad\text{(51)}$$

con $\omega_n = k_n v = k_n\sqrt{\dfrac{T}{\mu}}$ y $k_n = \dfrac{n\pi}{2L}$.

Así, la velocidad transversal (en términos de un desarrollo en modos normales) puede escribirse

$$\dot{y}(x, t) = \sum_n A_n\omega_n\sin(k_n x)\cos(\omega_n t)\qquad\text{(52)}$$

Y la amplitud de excitación de cada modo normal $A_n$ puede hallarse mediante

$$A_n\omega_n = \frac{2}{2L}\int_0^{2L} \dot{y}(x, t = 0)\sin(k_n x)\,dx\qquad\text{(53)}$$

$$A_n = \frac{1}{\omega_n L}\left[\int_{L-a}^{L} v_0\sin(k_n x)\,dx - \int_{L}^{L+a} v_0\sin(k_n x)\,dx\right]\qquad\text{(54)}$$

$$A_n = -\frac{v_0}{\omega_n k_n L}\left[\cos(k_n x)\big|_{L-a}^{L} - \cos(k_n x)\big|_{L}^{L+a}\right]\qquad\text{(55)}$$

$$A_n = -\frac{v_0}{\omega_n k_n L}\left[\cos(k_n L) - \cos(k_n(L - a)) - \cos(k_n(L + a)) + \cos(k_n L)\right]\qquad\text{(56)}$$

$$A_n = -\frac{v_0}{\omega_n k_n L}\left[2\cos(k_n L) - 2\cos(k_n L)\cos(k_n a)\right]\qquad\text{(57)}$$

$$A_n = -\frac{2v_0}{\omega_n k_n L}\left(1 - \cos(k_n a)\right)\cos(k_n L)\qquad\text{(58)}$$

$$A_n = -\frac{v_0\,8L}{v\,n^2\pi^2}\left[1 - \cos\left(\frac{n\pi}{2}\frac{a}{L}\right)\right]\cos\left(\frac{n\pi}{2}\right)\qquad\text{(59)}$$

$$A_n = -\frac{v_0\,8L}{\sqrt{\frac{T}{\mu}}\,n^2\pi^2}\left[1 - \cos\left(\frac{n\pi}{2}\frac{a}{L}\right)\right]\cos\left(\frac{n\pi}{2}\right)\qquad\text{(60)}$$

De la última ecuación vemos que el modo $n = 1$ no está excitado. También podríamos haber visto que este modo no se excitaría por razones de simetría, ya que el modo $n = 1$ es simétrico respecto del centro de la cuerda, mientras que las condiciones iniciales son antisimétricas. Análogamente, cualquier modo que sea simétrico respecto del centro de la cuerda no estará excitado.

**(5.c)** El desplazamiento se divide en dos ondas que se propagan en sentidos opuestos, cada una con altura $h = \dfrac{a v_0}{\sqrt{T/\mu}}$.

## Solución del problema 6

**(6.a)** Suponiendo que el amortiguamiento de la carga es despreciable, el movimiento de la partícula es simplemente el de un oscilador armónico simple, cuya solución es

$$x(t) = A\cos(\omega_0 t)\qquad\text{(61)}$$

$$\ddot{x}(t) = -A\omega_0^2\cos(\omega_0 t)\qquad\text{(62)}$$

con $\omega_0 = \sqrt{k/m}$. Ahora bien, el campo eléctrico viene dado por

$$\vec{E}(\vec{R}, t) = -\frac{q\vec{a}_\perp(t')}{4\pi\varepsilon_0 Rc^2} = -\frac{q\left(\hat{n}\times(\hat{n}\times\vec{a}(t'))\right)}{4\pi\varepsilon_0 Rc^2}\qquad\text{(63)}$$

donde $\hat{n}$ es el vector unitario que apunta de la fuente al observador. En el plano $x$-$z$ tenemos $\hat{n} = \sin\theta\,\hat{x} + \cos\theta\,\hat{z}$. Así pues, el campo eléctrico viene dado por

$$\frac{qA\omega_0^2}{4\pi\varepsilon_0 c^2 R}\cos\left(\omega_0(t - R/c)\right)\left(\cos^2\theta\,\hat{x} - \cos\theta\sin\theta\,\hat{z}\right)\qquad\text{(64)}$$

**(6.b)** La potencia total radiada por la partícula viene dada directamente por la fórmula de Larmor:

$$P(t) = \frac{q^2 a^2(t')}{6\pi\varepsilon_0 c^3} = \frac{q^2 A^2\omega_0^4\cos^2\left(\omega_0(t - R/c)\right)}{6\pi\varepsilon_0 c^3}\qquad\text{(65)}$$

Promediando en el tiempo se obtiene

$$\langle P\rangle = \frac{q^2 A^2\omega_0^4}{12\pi\varepsilon_0 c^3}\qquad\text{(66)}$$

**(6.c)** Con la suposición de que la potencia radiada no cambia mucho con el tiempo, el tiempo $t$ que tardaría la amplitud original del movimiento en reducirse a $1/e$ de su valor puede hallarse mediante

$$\frac{1}{2}m\omega_0^2 A^2 - \langle P\rangle t = \frac{1}{2}m\omega_0^2\left(\frac{A}{e}\right)^2\qquad\text{(67)}$$

$$\Rightarrow t = \frac{m\omega_0^2 A^2}{2\langle P\rangle}\left(1 - \left(\frac{1}{e}\right)^2\right)\qquad\text{(68)}$$

$$t \approx 0.86\times\frac{6\pi m\varepsilon_0 c^3}{q^2\omega_0^2}\qquad\text{(69)}$$

Esta suposición no es del todo realista, ya que la potencia radiada por la carga es proporcional al cuadrado de la amplitud de su movimiento, y la amplitud del movimiento va disminuyendo a medida que se radia energía. Este método siempre subestimará el tiempo necesario para que la amplitud disminuya.

**(6.d)** La energía $E$ viene dada por

$$E = \frac{m\omega_0^2 A^2}{2}\qquad\text{(70)}$$

de modo que tenemos

$$\frac{dA}{dE} = \frac{1}{m\omega_0^2 A}\qquad\text{(71)}$$

mientras que la potencia media radiada por ciclo es la que hallamos en el apartado (b):

$$\frac{dE}{dt} = \langle P\rangle = \frac{q^2 A^2\omega_0^4}{12\pi\varepsilon_0 c^3}\qquad\text{(72)}$$

Combinando ambas para hallar $dA/dt$ obtenemos

$$\frac{dA}{dt} = \frac{dA}{dE}\frac{dE}{dt} = \left(\frac{1}{m\omega_0^2 A}\right)\left(\frac{q^2 A^2\omega_0^4}{12\pi\varepsilon_0 c^3}\right) = \frac{q^2 A\omega_0^2}{12\pi\varepsilon_0 c^3 m}\qquad\text{(73)}$$

Integrando ahora para hallar el tiempo necesario para que la amplitud disminuya de $A$ a $A/e$, tenemos

$$\int_{A/e}^{A}\frac{dA}{A} = \frac{q^2\omega_0^2}{12\pi\varepsilon_0 c^3 m}\int dt\qquad\text{(74)}$$

$$\ln(A) - \ln(A/e) = \ln(e) = 1 = \left(\frac{q^2\omega_0^2}{12\pi\varepsilon_0 c^3 m}\right)t\qquad\text{(75)}$$

de modo que el tiempo $t$ viene dado por

$$t = \frac{12\pi\varepsilon_0 c^3 m}{q^2\omega_0^2}\qquad\text{(76)}$$

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*


---

<!-- MIT8.03_ExamenFinalPractica2_ES.md -->

# Examen final de práctica 2

**Instituto Tecnológico de Massachusetts**

**Física 8.03**

**EXAMEN FINAL DE PRÁCTICA 2**

------------------------------------------------------------------------

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

------------------------------------------------------------------------

## Problema 1 (15 puntos)

Responda a cada pregunta corta por separado.

**1.1.** La energía potencial de una partícula de masa $m$, obligada a moverse a lo largo del eje $x$, viene dada por

$$U(x) = A\left(1 - \cos(\alpha x)\right)$$

donde $A$ y $\alpha$ son constantes, ambas $> 0$. Si la partícula se desplaza del equilibrio, ¿cuál será su periodo de oscilación de pequeña amplitud?

**1.2.** Considere el siguiente registro de la posición de un oscilador forzado en función del tiempo (figura 1). Puede suponer que la fuerza impulsora es una onda sinusoidal y que su amplitud no cambia con el tiempo. ¿Cuál o cuáles de las siguientes descripciones son verdaderas? (Seleccione todas las que correspondan.)

1.  La frecuencia impulsora es mayor que la frecuencia de resonancia natural del sistema.

2.  La frecuencia impulsora es menor que la frecuencia de resonancia natural del sistema.

3.  No hay amortiguamiento.

4.  El sistema está sobreamortiguado.

5.  El sistema está críticamente amortiguado.

6.  El sistema está subamortiguado.

**1.3.** La electrónica utilizada en el Gran Colisionador de Hadrones emplea pulsos cuadrados de 1 nanosegundo. ¿Cuál es el rango aproximado de frecuencias (ancho de banda) necesario para enviar pulsos tan cortos?

**1.4.** En la figura 2 se muestra un experimento con electrones. La fuente se calentó hasta que empezó a emitir electrones. ¿Cuál o cuáles de las siguientes descripciones son verdaderas? (Seleccione todas las que correspondan.)

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenFinalPractica2_ES/fig2.png)

Figura 2

1.  Cuando la temperatura de la fuente es alta, de modo que la tasa de emisión de electrones es alta, el detector registrará un patrón de interferencia.

2.  Cuando la temperatura de la fuente es alta, de modo que la tasa de emisión de electrones es alta, el detector no registrará ningún patrón de interferencia.

3.  Cuando la temperatura de la fuente es baja, de modo que la fuente emite un electrón cada vez, no habrá patrón de interferencia.

4.  Cuando la temperatura de la fuente es baja, de modo que la fuente emite un electrón cada vez, habrá patrón de interferencia.

**1.5.** Una membrana elástica está tensada sobre un marco rectangular, como se muestra en la figura 3. La velocidad de fase de propagación de las ondas en esta membrana es $v$. ¿Cuál es la frecuencia angular del modo normal más bajo que puede excitarse en la membrana?

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenFinalPractica2_ES/fig1.png)

Figura 1: registro de un oscilador forzado. Figura 2: experimento con electrones. Figura 3: membrana elástica, tensada sobre un marco cuadrado de lado $L$.

------------------------------------------------------------------------

## Problema 2 (15 puntos)

Dos pequeñas cuentas con masa, de masas iguales $m_1 = m_2 = m$, están sobre una cuerda tensa sin masa de longitud $5L$ (véase la figura 4). La tensión de la cuerda $T$ es grande, de modo que se pueden despreciar los efectos de la gravedad. Los tramos de cuerda miden $2L$, $L$ y $2L$.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenFinalPractica2_ES/fig3.png)

Figura 3

**a.** Escriba las ecuaciones del movimiento de las dos cuentas para oscilaciones de pequeña amplitud a lo largo de $y$ y escriba la matriz $M^{-1}K$ correspondiente a este sistema.

**b.** Halle las formas y las frecuencias angulares de los modos normales del sistema. Puede simplificar la tarea usando argumentos de simetría. Explique su razonamiento.

**c.** Inicialmente, en $t = 0$, ambas masas están en reposo, con $m_1$ en la posición de equilibrio y $m_2$ desplazada del equilibrio una distancia $A$. Escriba una expresión para el desplazamiento $y_1(t)$ de la masa que inicialmente está en la posición de equilibrio.

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenFinalPractica2_ES/fig4.png)

Figura 4: dos cuentas sobre una cuerda, con tramos de longitudes $2L$, $L$ y $2L$.

------------------------------------------------------------------------

## Problema 3 (20 puntos)

La figura 5 representa un tubo lleno de gas que está abierto a un depósito de gas en $x = 0$ y cerrado en $x = L$. La velocidad del sonido en el gas es $v$. Se establece en el gas una ligera perturbación de presión que después se suelta desde el reposo en $t = 0$. La perturbación está centrada en $L/2$, abarca una anchura $L/3$ y tiene una presión $P_1$ ligeramente mayor que la presión ambiente $P_0$.

**a.** ¿Cuáles son las condiciones de contorno en $x = 0$ y en $x = L$?

**b.** Exprese la perturbación de presión $P(x, t)$ para $t > 0$ como una suma de modos normales. Dé expresiones explícitas para las variaciones espacial y temporal de cada modo normal, su número de onda y su frecuencia angular. Deje las amplitudes asociadas como parámetros por determinar.

**c.** Calcule la amplitud del $n$-ésimo modo normal.

**d.** Dibuje un esbozo (similar a la gráfica anterior) de la presión en el tubo en el instante $t = 2L/v$. \[Pista: puede hacerse razonando con cuidado, en lugar de calcular explícitamente $P(x, t)$.\]

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenFinalPractica2_ES/fig5.png)

Figura 5: onda de presión en un tubo. Sobre el tramo de $0$ a $L$ se levanta un pulso de presión de anchura $L/3$ centrado en $L/2$, que alcanza el valor $P_1$ por encima de la presión ambiente $P_0$.

------------------------------------------------------------------------

## Problema 4 (15 puntos)

Una carga puntual $+q$ se ha estado moviendo con velocidad constante $w$ a lo largo de una línea recta hasta el instante $t = t_0$. En el CORTO intervalo de tiempo de $t = t_0$ a $t = t_0 + \Delta t$, una fuerza perpendicular a la trayectoria cambia la dirección sin cambiar el módulo de la velocidad. Después del instante $t = t_0 + \Delta t$, la carga vuelve a moverse con velocidad $w$ a lo largo de una línea recta que forma un pequeño ángulo $\Delta\alpha$ con la trayectoria inicial, como se muestra en la figura 6. La radiación emitida por la carga se observa desde los puntos muy lejanos $P_1$ y $P_2$. Los dos puntos de observación están situados en el plano de la trayectoria.

**a.** ¿Cuál es la aceleración media de la carga puntual en términos de las magnitudes dadas?

**b.** ¿Cuál es la dirección del campo eléctrico causado por la aceleración en el punto lejano $P_1$?

**c.** ¿En qué dirección es más intensa la radiación de la carga acelerada?

**d.** ¿Dónde es menos intensa?

**e.** El punto $P_2$ está al doble de distancia del codo de la trayectoria que $P_1$. ¿En qué fracción disminuye la amplitud de la perturbación electromagnética al pasar el pulso de radiación de $P_1$ a $P_2$?

**f.** ¿Cuál es la energía total radiada por la carga?

Haga esbozos cuidadosos al responder a los apartados b), c) y d).

![Figura 6](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenFinalPractica2_ES/fig6.png)

Figura 6: carga radiante. La trayectoria se quiebra un ángulo $\Delta\alpha$; los puntos de observación $P_1$ y $P_2$ están en el plano de la trayectoria, con $P_2$ al doble de distancia que $P_1$.

------------------------------------------------------------------------

## Problema 5 (15 puntos)

Considere un sistema de tres polarizadores lineales ideales dispuestos a lo largo de un banco óptico, como se muestra en la figura 7. Los dos polarizadores exteriores tienen sus ejes fáciles perpendiculares entre sí. El polarizador A transmite solo luz polarizada horizontalmente, mientras que el polarizador C transmite solo luz polarizada verticalmente. El polarizador B tiene su eje fácil formando un ángulo $\theta$ con el eje horizontal $x$. Suponga que la luz que incide sobre el polarizador A por la izquierda no está polarizada y que su intensidad es $I_0$.

**a.** Halle la intensidad y la polarización de la luz transmitida a través del polarizador A, $I_A$.

**b.** Halle la intensidad y la polarización de la luz transmitida a través del polarizador B, $I_B$, en función de $I_0$ y $\theta$, y represéntela gráficamente en función de $\theta$.

**c.** Halle la intensidad de la luz transmitida a través del polarizador C, $I_C$, en función de $I_0$ y $\theta$, y represéntela gráficamente en función de $\theta$.

![Figura 7](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenFinalPractica2_ES/fig7.png)

Figura 7: tres polarizadores lineales A, B y C, con los ejes fáciles horizontal, a un ángulo $\theta$ y vertical, respectivamente.

------------------------------------------------------------------------

## Problema 6 (20 puntos)

Una fuente monocromática de ondas planas de longitud de onda $\lambda$ ilumina una red de cuatro rendijas. La figura 8 muestra una sección transversal de la red; la longitud de las rendijas es perpendicular al papel. La pantalla está muy lejos de las rendijas ($d \ll z$).

**a.** Escriba una expresión, en términos de $d$, $\lambda$ y $\psi$, de la intensidad $I$ que se observará en la pantalla. Suponga en principio que las rendijas son muy estrechas en comparación con su separación ($D \ll d$). Suponga que la intensidad de la luz debida a una sola rendija es $I_0$.

**b.** Haga un esbozo de la intensidad en función de $\sin\psi$ para la red de cuatro rendijas. Asegúrese de especificar las posiciones de los máximos principales y de los mínimos de interferencia.

**c.** Considere ahora la misma red con las dos rendijas INTERIORES bloqueadas. Escriba una expresión de la intensidad observada en la pantalla y haga el esbozo de la nueva intensidad frente a $\sin\psi$.

**d.** Compárelo con el esbozo obtenido para las cuatro rendijas. ¿Cuáles son las nuevas posiciones de los máximos y los mínimos? ¿Qué máximos principales están en la misma posición en las dos configuraciones? ¿Cómo ha cambiado la magnitud de los máximos principales? Suponga que las intensidades individuales de las rendijas abiertas son las mismas en ambos casos.

**e.** Considere ahora la misma red de cuatro rendijas con todas las rendijas descubiertas, pero esta vez las anchuras $D$ de las rendijas individuales no pueden despreciarse. La razón entre la distancia entre los centros de las rendijas y la anchura de la rendija es ahora $d/D = 5$. El efecto de la difracción por una sola rendija hará que algunos de los máximos principales obtenidos en el apartado a) desaparezcan ($I = 0$). ¿Cuál es el orden de interferencia más bajo para el que los efectos de difracción anulan de este modo el máximo principal?

![Figura 8](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenFinalPractica2_ES/fig8.png)

Figura 8: red de cuatro rendijas, de separación $d$ entre centros y anchura $D$, con la pantalla a una distancia $z$.

------------------------------------------------------------------------

# Soluciones

## Solución del problema 1

**1.1** (3 puntos) La energía potencial

$$U(x) = A\left(1 - \cos(\alpha x)\right)\qquad\text{(1)}$$

El mínimo está en los puntos

$$x = \frac{2n\pi}{\alpha}\ ,\qquad n \in \mathbb{Z}\qquad\text{(2)}$$

*\[Nota de la traducción: el PDF original escribe $x = 2n\pi$, omitiendo el factor $1/\alpha$; los mínimos de $U$ están donde $\cos(\alpha x) = 1$, es decir, en $\alpha x = 2n\pi$.\]*

Por ejemplo, consideramos $x = 0$:

$$\left.\frac{d^2U}{dx^2}\right|_0 = A\alpha^2\cos(\alpha x)\big|_0 = A\alpha^2\qquad\text{(3)}$$

Esto es equivalente al parámetro $k$ del movimiento armónico simple de un muelle: $U = \frac{1}{2}kx^2$. Por tanto obtenemos el periodo

$$T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{m}{k}} = 2\pi\sqrt{\frac{m}{A\alpha^2}}\qquad\text{(4)}$$

**1.2** (3 puntos) El comportamiento transitorio de un sistema de oscilación forzada se describe como la suma del movimiento estacionario y del movimiento libre que decae por el amortiguamiento.

El periodo del movimiento estacionario es mucho más largo que el periodo del movimiento libre. Además, la forma global del movimiento transitorio corresponde a un movimiento subamortiguado que decae. Por tanto, la respuesta es **b, f**.

**1.3** (3 puntos) La relación entre el ancho de banda $\Delta f$ y la resolución temporal $\Delta t$ es

$$\Delta t\,\Delta f \sim 1\qquad\text{(5)}$$

Por tanto, el ancho de banda es

$$\Delta f \sim 10^9\ \text{Hz}\qquad\text{(6)}$$

**1.4** (3 puntos) Por débil que sea la fuente de electrones, siempre aparece un patrón de interferencia en la pantalla al cabo de mucho tiempo. La respuesta es **a, d**.

**1.5** (3 puntos) La ecuación de ondas en 2D es

$$\frac{\partial^2\psi}{\partial t^2} = v^2\left(\frac{\partial^2\psi}{\partial x^2} + \frac{\partial^2\psi}{\partial y^2}\right)\qquad\text{(7)}$$

El modo más bajo que respeta la condición de contorno dada es

$$\psi_{1,1}(x, y, t) \sim \sin\left(\frac{\pi x}{L}\right)\sin\left(\frac{\pi y}{L}\right)\cos(\omega t)\qquad\text{(8)}$$

Sustituyéndolo en la ecuación de ondas, obtenemos

$$\omega = \sqrt{2}\,\frac{v\pi}{L}\qquad\text{(9)}$$

## Solución del problema 2

**a)** (5 puntos) La ecuación del movimiento de $m_1$ es

$$m\ddot{y}_1 = -\frac{T}{2L}y_1 - \frac{T}{L}(y_1 - y_2) = -\frac{3T}{2L}y_1 + \frac{T}{L}y_2\qquad\text{(10)}$$

Análogamente, la ecuación del movimiento de $m_2$ es

$$m\ddot{y}_2 = -\frac{T}{2L}y_2 - \frac{T}{L}(y_2 - y_1) = -\frac{3T}{2L}y_2 + \frac{T}{L}y_1\qquad\text{(11)}$$

Por tanto, los elementos de la matriz $K$ son

$$K_{11} = K_{22} = \frac{3T}{2L}\ ,\qquad K_{12} = K_{21} = -\frac{T}{L}\qquad\text{(12)}$$

Y la matriz $M^{-1}K$ es

$$M^{-1}K = \begin{pmatrix} \frac{3T}{2mL} & -\frac{T}{mL} \\ -\frac{T}{mL} & \frac{3T}{2mL} \end{pmatrix}\qquad\text{(13)}$$

**b)** (5 puntos) El sistema es simétrico bajo la reflexión horizontal respecto del punto central, es decir, bajo el intercambio $y_1 \leftrightarrow y_2$. Las únicas soluciones que tienen esta simetría son $y_1(t) = y_2(t)$ e $y_1(t) = -y_2(t)$. Dan lugar a los autovectores

$$V_+ = \begin{pmatrix} 1 \\ 1 \end{pmatrix}\ ,\qquad V_- = \begin{pmatrix} 1 \\ -1 \end{pmatrix}\qquad\text{(14)}$$

Sustituyendo esos autovectores en la ecuación matricial

$$M^{-1}K\,V = \omega^2 V\qquad\text{(15)}$$

obtenemos las frecuencias angulares correspondientes a $V_\pm$:

$$\omega_+ = \sqrt{\frac{T}{2mL}}\ ,\qquad \omega_- = \sqrt{\frac{5T}{2mL}}\qquad\text{(16)}$$

**c)** (5 puntos) El movimiento más general en términos de esos modos normales es

$$\begin{pmatrix} y_1 \\ y_2 \end{pmatrix} = A_+\begin{pmatrix} 1 \\ 1 \end{pmatrix}\cos(\omega_+ t + \varphi_+) + A_-\begin{pmatrix} 1 \\ -1 \end{pmatrix}\cos(\omega_- t + \varphi_-)\qquad\text{(17)}$$

donde $A_+$ y $A_-$ son dos coeficientes fijados por las condiciones iniciales. A partir de la información sobre las posiciones y velocidades iniciales, tenemos las ecuaciones

$$\begin{pmatrix} 0 \\ A \end{pmatrix} = A_+\begin{pmatrix} 1 \\ 1 \end{pmatrix}\cos\varphi_+ + A_-\begin{pmatrix} 1 \\ -1 \end{pmatrix}\cos\varphi_-\qquad\text{(18)}$$

$$\begin{pmatrix} 0 \\ 0 \end{pmatrix} = -A_+\begin{pmatrix} 1 \\ 1 \end{pmatrix}\sin\varphi_+ - A_-\begin{pmatrix} 1 \\ -1 \end{pmatrix}\sin\varphi_-\qquad\text{(19)}$$

De la segunda ecuación obtenemos $\varphi_+ = \varphi_- = 0$, y de la primera podemos despejar

$$A_+ = \frac{A}{2}\ ,\qquad A_- = -\frac{A}{2}\qquad\text{(20)}$$

El movimiento de $m_1$ es entonces

$$y_1(t) = \frac{A}{2}\left(\cos(\omega_+ t) - \cos(\omega_- t)\right)\qquad\text{(21)}$$

## Solución del problema 3

**a)** (5 puntos) En $x = 0$, la presión es la misma que la presión atmosférica $P_0$, por lo que la perturbación de presión es $P(0, t) = 0$. En $x = L$, el desplazamiento de las moléculas de aire es nulo, y entonces

$$\frac{\partial P}{\partial x}(L, t) = 0\qquad\text{(22)}$$

**b)** (5 puntos) De la condición de contorno en $x = 0$ sabemos que los modos normales tienen la forma

$$P(x, t) \sim \sin(kx)\qquad\text{(23)}$$

Y de la condición de contorno en $x = L$:

$$k\cos(kL) = 0\qquad\text{(24)}$$

deducimos

$$k = \left(n + \frac{1}{2}\right)\frac{\pi}{L}\ ,\qquad n = 0, 1, 2, \ldots\qquad\text{(25)}$$

El desarrollo de Fourier de $P(x, t)$ es entonces

$$P(x, t) = \sum_{n=0}^{\infty} A_n\sin\left(\left(n + \frac{1}{2}\right)\frac{\pi}{L}x\right)\cos\left(\left(n + \frac{1}{2}\right)\frac{v\pi}{L}t\right)\qquad\text{(26)}$$

(Las fases de cada término son todas nulas porque la «velocidad» inicial $\frac{\partial P}{\partial t} = 0$.)

**c)** (5 puntos) Los coeficientes de Fourier pueden obtenerse evaluando la integral

$$A_n = \frac{2}{L}\int_0^L f(x)\sin\left(\left(n + \frac{1}{2}\right)\frac{\pi}{L}x\right)dx\qquad\text{(27)}$$

donde $f(x)$ es la forma inicial dada en el problema.

$$\begin{aligned}
A_n &= \frac{2(P_1 - P_0)}{L}\int_{L/3}^{2L/3}\sin\left(\left(n + \frac{1}{2}\right)\frac{\pi}{L}x\right)dx \\[4pt]
&= -\frac{2(P_1 - P_0)}{\left(n + \frac{1}{2}\right)\pi}\left[\cos\left(\left(n + \frac{1}{2}\right)\frac{2\pi}{3}\right) - \cos\left(\left(n + \frac{1}{2}\right)\frac{\pi}{3}\right)\right]
\end{aligned}\qquad\text{(28)}$$

**d)** (5 puntos) En el instante $t = \dfrac{2L}{v}$, los argumentos valen

$$\left(n + \frac{1}{2}\right)\frac{v\pi}{L}t = 2\pi n + \pi\qquad\text{(29)}$$

Por tanto, todos los $\cos\left(\left(n + \frac{1}{2}\right)\frac{v\pi}{L}t\right)$ del desarrollo de $P(x, t)$ valen $-1$. La configuración (perturbación de presión) es entonces la del pulso inicial invertido, es decir, un pulso que baja hasta $P_0 - P_1$.

## Solución del problema 4

**a)** (3 puntos) La aceleración media es

$$\langle\vec{a}\rangle = \frac{\vec{v}_2 - \vec{v}_1}{\Delta t}\qquad\text{(30)}$$

donde $\vec{v}_1 = w\hat{x}$ y $\vec{v}_2 = w\cos\Delta\alpha\cdot\hat{x} - w\sin\Delta\alpha\cdot\hat{y}$ son las velocidades inicial y final. Puesto que $\Delta\alpha \ll 1$, $\cos\Delta\alpha - 1$ es un infinitésimo de segundo orden, que puede despreciarse frente a $\sin\Delta\alpha$. Entonces

$$\vec{v}_2 - \vec{v}_1 = -w\,\Delta\alpha\cdot\hat{y}\qquad\text{(31)}$$

$$\langle\vec{a}\rangle = -\frac{w\,\Delta\alpha}{\Delta t}\cdot\hat{y}\qquad\text{(32)}$$

**b)** (3 puntos) El campo eléctrico generado por esta aceleración es

$$\vec{E}(\vec{r}, t) = -\frac{q\,\vec{a}_\perp(t - |r|/c)}{4\pi\varepsilon_0 rc^2}\qquad\text{(33)}$$

donde $\vec{a}_\perp(t - |r|/c)$ es la aceleración proyectada sobre la dirección transversal a $\vec{r}$. La dirección del campo eléctrico es, por tanto, la opuesta a esa proyección transversal de la aceleración.

**c) d)** (2 puntos cada uno) La dirección perpendicular a la dirección de la aceleración es la de radiación más intensa. La dirección paralela u opuesta a la dirección de la aceleración es la de radiación mínima (nula).

**e)** (2 puntos) De (33) sabemos que el campo eléctrico escala como $\vec{E} \sim \dfrac{1}{r}$. Por tanto, la amplitud en $P_2$ será $\dfrac{1}{2}$ de la amplitud en $P_1$.

**f)** (3 puntos) La potencia total de radiación es

$$P(t) = \frac{q^2 a^2(t - |r|/c)}{6\pi\varepsilon_0 c^3}\qquad\text{(34)}$$

Por tanto, la energía total radiada por la carga es

$$E = P\,\Delta t = \Delta t\cdot\frac{q^2 w^2\Delta\alpha^2}{6\pi\varepsilon_0 c^3(\Delta t)^2} = \frac{q^2 w^2\Delta\alpha^2}{6\pi\varepsilon_0 c^3\,\Delta t}\qquad\text{(35)}$$

## Solución del problema 5

**a)** (5 puntos) Para luz no polarizada, la intensidad después de atravesar un polarizador lineal es $I_A = \frac{1}{2}I_0$. Su polarización después de atravesar A es la de la dirección $\hat{x}$.

**b)** (5 puntos) Después de que la luz atraviese B, el vector de polarización se proyecta sobre la dirección fácil de B, de modo que la intensidad final es

$$I_B = I_A\cos^2\theta = \frac{1}{2}I_0\cos^2\theta\qquad\text{(36)}$$

**c)** (5 puntos) Después de que la luz atraviese C, el vector de polarización se proyecta desde la dirección fácil de B a la dirección fácil de C (dirección $\hat{y}$), de modo que la intensidad final es

$$I_C = I_B\sin^2\theta = \frac{1}{2}I_0\cos^2\theta\sin^2\theta = \frac{1}{8}I_0\sin^2(2\theta)\qquad\text{(37)}$$

## Solución del problema 6

**a)** (4 puntos) Puesto que las rendijas son muy estrechas, la intensidad es simplemente la intensidad de interferencia de 4 rendijas:

$$I = I_0\left(\frac{\sin^2(2\delta)}{\sin^2\frac{\delta}{2}}\right)\ ,\qquad \delta = 2\pi\frac{d}{\lambda}\sin\psi\qquad\text{(38)}$$

**b)** (4 puntos) Los máximos principales están en $\delta = 2\pi n$, o bien $\sin\psi = n\dfrac{\lambda}{d}$. Los mínimos están en $\delta = \dfrac{m\pi}{2}$, donde $4 \nmid m$ (es decir, $m$ no es múltiplo de 4).

**c)** (4 puntos) Cuando se cierran las dos rendijas centrales, el sistema es simplemente una interferencia de dos rendijas con distancia entre rendijas $3d$. Por tanto,

$$I = I_0\left(\frac{\sin^2\delta'}{\sin^2\frac{\delta'}{2}}\right)\ ,\qquad \delta' = 6\pi\frac{d}{\lambda}\sin\psi\qquad\text{(39)}$$

**d)** (4 puntos) Los nuevos máximos están en

$$\sin\psi = n\frac{\lambda}{3d}\quad (n \in \mathbb{Z})\qquad\text{(40)}$$

y los nuevos mínimos están en

$$\sin\psi = \left(n + \frac{1}{2}\right)\frac{\lambda}{3d}\quad (n \in \mathbb{Z})\qquad\text{(41)}$$

Los máximos principales

$$\sin\psi = n\frac{\lambda}{d}\quad (n \in \mathbb{Z})\qquad\text{(42)}$$

están en las mismas posiciones. La intensidad de los máximos principales disminuye de $16I_0$ a $4I_0$.

**e)** (4 puntos) Cuando la anchura de una sola rendija no puede despreciarse, la intensidad es

$$I = I_0\left(\frac{\sin^2(2\delta)}{\sin^2\frac{\delta}{2}}\right)\frac{\sin^2\beta}{\beta^2}\ ,\qquad \beta = \pi\frac{D}{\lambda}\sin\psi\qquad\text{(43)}$$

Los ceros del factor de difracción $\dfrac{\sin^2\beta}{\beta^2}$ están en

$$\sin\psi = n\frac{\lambda}{D}\ ,\qquad n = 1, 2, 3, \ldots\qquad\text{(44)}$$

La condición para que un máximo principal del patrón de interferencia se solape con un cero de difracción es entonces

$$n\frac{\lambda}{D} = \frac{m\lambda}{d} = \frac{m\lambda}{5D}\qquad\text{(45)}$$

De modo que el orden de interferencia más bajo para el que esto ocurre es $m = 5$.

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*


---

<!-- MIT8.03_ExamenFinalPractica3_ES.md -->

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


---

<!-- MIT8.03_ExamenPractica1_ES.md -->

# Examen de práctica 1

**Instituto Tecnológico de Massachusetts**

**Física 8.03**

**EXAMEN DE PRÁCTICA 1**

## Instrucciones

Escriba sus soluciones en los cuadernillos blancos. No se corregirá nada de lo escrito en la copia del examen. Este examen es a libro cerrado. No se permite ningún equipo electrónico. Todos los teléfonos, tabletas, ordenadores, etc. deben estar apagados.

------------------------------------------------------------------------

## Hoja de fórmulas

### Muelles y masas

$$m\frac{d^2}{dt^2}x(t) + b\frac{d}{dt}x(t) + kx(t) = F(t)$$

Ecuación diferencial más general con fuerza impulsora armónica:

$$\frac{d^2}{dt^2}x(t) + \Gamma\frac{d}{dt}x(t) + \omega_0^2 x(t) = \frac{F_0}{m}\cos(\omega_d t)$$

### Solución estacionaria compleja

$$z_s(t) = z_0 e^{-i\omega_d t} \qquad z_0 = Ae^{i\delta} = c + id \qquad A = \sqrt{c^2 + d^2}$$

$$\delta = \arctan(d/c)\ \text{para } c > 0 \qquad \text{y} \qquad \delta = \arctan(d/c) + \pi\ \text{para } c < 0$$

El sistema físico sigue la parte real de esta solución:

$$x_s(t) = \operatorname{Re}(z_s(t)) \qquad \operatorname{Re}(z) = (z + z^*)/2$$

### Soluciones generales, incluidas las oscilaciones libres

Para $\Gamma < 2\omega_0$ (sistema subamortiguado):

$$x(t) = Re^{-\frac{\Gamma}{2}t}\cos\left(\sqrt{\omega_0^2 - \frac{\Gamma^2}{4}}\,t + \theta\right) + x_s(t)$$

Para $\Gamma = 2\omega_0$ (sistema críticamente amortiguado):

$$x(t) = (R_1 + R_2 t)e^{-\frac{\Gamma}{2}t} + x_s(t)$$

Para $\Gamma > 2\omega_0$ (sistema sobreamortiguado):

$$x(t) = R_1 e^{\left(-\frac{\Gamma}{2} + \sqrt{\frac{\Gamma^2}{4} - \omega_0^2}\right)t} + R_2 e^{\left(-\frac{\Gamma}{2} - \sqrt{\frac{\Gamma^2}{4} - \omega_0^2}\right)t} + x_s(t)$$

*\[Nota de la traducción: el PDF original escribe estas tres condiciones como $\Gamma < \omega_0/2$, $\Gamma = \omega_0/2$ y $\Gamma > \omega_0/2$. Se trata de una errata: las propias fórmulas que las acompañan, con $\sqrt{\omega_0^2 - \Gamma^2/4}$, solo tienen sentido con los umbrales $2\omega_0$, que son además los que aparecen en la hoja de fórmulas de los exámenes reales 1 y 2.\]*

### Osciladores acoplados

$$F_j = -\sum_{k=1}^{n} K_{jk}\,x_k$$

Ejemplos para $n = 2$:

$$\mathcal{X}(t) = \begin{pmatrix} x_1(t) \\ x_2(t) \end{pmatrix}
\qquad
K = \begin{pmatrix} K_{11} & K_{12} \\ K_{21} & K_{22} \end{pmatrix}
\qquad
M = \begin{pmatrix} m_1 & 0 \\ 0 & m_2 \end{pmatrix}$$

Ecuación matricial del movimiento; las matrices $M$, $K$, $I$ son $n \times n$ y los vectores $\mathcal{X}$, $\mathcal{Z}$ son $n \times 1$:

$$\frac{d^2}{dt^2}\mathcal{X}(t) = -M^{-1}K\,\mathcal{X}(t) \qquad \mathcal{Z}(t) = Ae^{-i\omega t} \qquad (M^{-1}K - \omega^2 I)A = 0$$

Para obtener las frecuencias de los modos normales, resuelva:

$$\det(M^{-1}K - \omega^2 I) = 0$$

Para $n = 2$:

$$\det\begin{pmatrix} M_{11} & M_{12} \\ M_{21} & M_{22} \end{pmatrix} = M_{11}M_{22} - M_{12}M_{21}$$

Si el sistema está impulsado por una fuerza, se pueden hallar las amplitudes de respuesta $C(\omega_d)$:

$$F(t) = F_0 e^{-i\omega_d t} \qquad W(t) = C(\omega_d)e^{-i\omega_d t} \qquad (M^{-1}K - \omega_d^2 I)\,C(\omega_d) = F_0$$

### Leyes de Kirchhoff

(¡Tenga cuidado con los signos!)

$$\text{Nodo:}\quad \sum_{i} I_i = 0 \qquad\qquad \text{Malla:}\quad \sum_{i} \Delta V_i = 0$$

$$\text{Condensadores:}\ \Delta V = \frac{Q}{C} \qquad \text{Bobinas:}\ \Delta V = -L\frac{dI}{dt} \qquad \text{Corriente:}\ I = \frac{dQ}{dt}$$

------------------------------------------------------------------------

## Problema 1 (30 puntos)

Considere una masa $M$ colgada de un muelle vertical sin masa de constante $k$ (véase la figura 1). La masa está en reposo. En $t = 0$ se desprende un trozo de la masa, quedando unida al muelle solo una fracción $\alpha$ de la masa original. La aceleración de la gravedad es $g$. Suponga que la masa se mueve a lo largo del eje vertical $y$. En $t = 0$ la masa estaba en $y = 0$.

**a.** Halle la nueva posición de equilibrio en función de los parámetros dados.

**b.** La masa oscilará. ¿Cuál es el periodo de las oscilaciones?

**c.** ¿Cuál es la dependencia temporal de la posición vertical, $y(t)$?

**d.** ¿Cuáles son la amplitud y la fase del movimiento en términos de los parámetros dados?

**e.** ¿Cuáles son la energía cinética y la energía potencial de la masa en función del tiempo?

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenPractica1_ES/fig1.png)

Figura 1: masa partida. Una masa $M$ cuelga de un muelle vertical de constante $k$; tras desprenderse un fragmento, queda colgando la masa $\alpha M$. El eje $y$ apunta hacia arriba y el origen está en la posición inicial de la masa.

------------------------------------------------------------------------

## Problema 2 (30 puntos)

Considere un oscilador simple con amortiguamiento. Una masa $m$ está unida a un muelle de constante $k$ y a un amortiguador cuya fuerza de amortiguamiento es proporcional a $-bv$. El muelle y el amortiguador están unidos a las paredes situadas en lados opuestos de la masa (véase la figura 2). El oscilador puede ser impulsado moviendo el punto de anclaje del amortiguador (A) o el extremo del muelle (B). En ambos casos, la posición del punto de anclaje en función del tiempo es $s(t) = s_0\cos(\omega_d t)$. Para AMBOS casos, A y B, responda a cada una de las preguntas siguientes.

**a.** Escriba las ecuaciones del movimiento de la masa $m$.

**b.** Halle la amplitud de la solución estacionaria en términos de los parámetros dados. Esboce la amplitud de oscilación en función de la frecuencia $\omega_d$.

**c.** ¿Para qué frecuencia $\omega_d$ es máxima la amplitud?

**d.** ¿Cuál es el comportamiento de la amplitud para $\omega_d \ll \omega_0$ y $\omega_d \gg \omega_0$?

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenPractica1_ES/fig2.png)

Figura 2: dos formas de impulsar un oscilador. En el caso A, el punto de anclaje móvil $s(t)$ está en el extremo del amortiguador $b$; en el caso B, está en el extremo del muelle $k$. En ambos casos la masa $m$ queda entre el amortiguador y el muelle, unidos a las paredes A y B.

------------------------------------------------------------------------

## Problema 3 (40 puntos)

Considere los cinco sistemas oscilantes acoplados de la figura 3, A-E. Para cada sistema, escriba un conjunto de ecuaciones del movimiento para oscilaciones armónicas de pequeña amplitud. Defina claramente las coordenadas que utiliza para describir cada sistema. Las ecuaciones deben escribirse en forma matricial: $(A - \omega^2 I)C = 0$ donde, para los sistemas habituales formados por masas y muelles, $A = M^{-1}K$. Existe también una matriz equivalente para los circuitos LC. ¡NO resuelva estas ecuaciones!

Notas sobre los sistemas:

**A.** Los extremos de los muelles que no están unidos a una masa están fijos.

**B.** Desprecie el movimiento vertical de las masas.

**C.** Desprecie los efectos debidos a la curvatura del anillo.

**D.** Escriba las ecuaciones del movimiento en términos de las corrientes que circulan por cada una de las tres bobinas.

**E.** Considere únicamente oscilaciones de ángulo pequeño.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenPractica1_ES/fig3.png)

Figura 3: cinco osciladores.

- *A: cadena horizontal fija por ambos extremos, con muelles y masas en el orden pared–$k$–$m$–$k$–$3m$–$k$–$m$–$k$–pared.*
- *B: tres péndulos de longitud $L$ y masa $m$ colgados del techo, acoplados entre sí por un muelle $k$ (entre el primero y el segundo) y otro $3k$ (entre el segundo y el tercero).*
- *C: cuatro masas $m$ sobre un anillo, unidas alternando muelles de constante $3k$ y $k$.*
- *D: circuito LC en escalera, con tres bobinas $L$ en la rama superior y cuatro condensadores $C$ en las ramas verticales.*
- *E: péndulo triple, formado por tres masas $m$ colgadas en serie mediante tres varillas de longitud $L$.*

------------------------------------------------------------------------

# Soluciones

## Solución del problema 1

**(a)** Cuando se desprende la parte inferior de la masa, la fuerza de la gravedad sobre el sistema disminuye en $(1-\alpha)Mg$, por lo que la posición de equilibrio se desplazará hacia arriba una distancia $\dfrac{(1-\alpha)Mg}{k}$. En el sistema de coordenadas centrado en la posición inicial de la masa, la nueva posición de equilibrio será

$$y = \frac{(1-\alpha)Mg}{k}\qquad\text{(1)}$$

**(b)** Como de costumbre, $\omega_0 = \sqrt{\dfrac{k}{\alpha M}}$. Recuerde, de la primera lista de problemas, que la gravedad no afecta a la frecuencia de oscilación. Por tanto, el periodo de las oscilaciones será

$$\tau = \frac{2\pi}{\omega_0} = 2\pi\sqrt{\frac{\alpha M}{k}}\qquad\text{(2)}$$

**(c)** La forma más general de las oscilaciones de este oscilador armónico no amortiguado y no forzado es

$$y(t) = A\cos(\omega_0 t + \varphi) + \frac{(1-\alpha)Mg}{k}\qquad\text{(3)}$$

donde el término $\dfrac{(1-\alpha)Mg}{k}$ proviene de que nuestro sistema de coordenadas no está centrado en la posición de equilibrio del oscilador. Por simplicidad, en el resto del problema pasaremos a un sistema de coordenadas centrado en la nueva posición de equilibrio. En este nuevo sistema de coordenadas, el movimiento del sistema vendrá dado por

$$y(t) = A\cos(\omega_0 t + \varphi)\qquad\text{(4)}$$

**(d)** Puesto que el sistema está inicialmente en reposo en la posición de equilibrio del sistema original (de masa $M$), sabemos que

$$y(0) = -\frac{(1-\alpha)Mg}{k}\qquad\text{(5)}$$

$$\dot{y}(0) = 0\qquad\text{(6)}$$

De (6) y del signo menos de (5) deducimos que $\varphi = \pi$ (obsérvese que también podríamos haber dicho que $\varphi = 0$ e incluido el signo menos en el coeficiente). De (5) vemos que la amplitud de las oscilaciones será $A = \dfrac{(1-\alpha)Mg}{k}$.

**(e)** La energía potencial almacenada en el muelle será $E_p(y) = \frac{1}{2}ky^2$, de modo que

$$E_p(t) = \frac{\big((1-\alpha)Mg\big)^2}{2k}\cos^2(\omega_0 t - \pi)\qquad\text{(7)}$$

La energía cinética de la masa es $E_c = \frac{1}{2}\alpha M\dot{y}^2$, y

$$\dot{y}(t) = -\sqrt{\frac{k}{\alpha M}}\,\frac{(1-\alpha)Mg}{k}\sin(\omega_0 t - \pi)\qquad\text{(8)}$$

de modo que

$$E_c(t) = \frac{\big((1-\alpha)Mg\big)^2}{2k}\sin^2(\omega_0 t - \pi)\qquad\text{(9)}$$

y $E = E_c + E_p = \dfrac{\big((1-\alpha)Mg\big)^2}{2k}$, una constante.

## Solución del problema 2

**(a)**

$$\text{A:}\quad \ddot{x} = -\frac{k}{m}x - \frac{b}{m}\big(\dot{x} + \omega_d s_0\sin(\omega_d t)\big)\qquad\text{(10)}$$

$$\text{B:}\quad \ddot{x} = -\frac{k}{m}\big(x - s_0\cos(\omega_d t)\big) - \frac{b}{m}\dot{x}\qquad\text{(11)}$$

Así pues, reordenando para poner el término impulsor a la derecha,

$$\text{A:}\quad \ddot{x} + \Gamma\dot{x} + \omega_0^2 x = -\Gamma\omega_d s_0\sin(\omega_d t)\qquad\text{(12)}$$

$$\text{B:}\quad \ddot{x} + \Gamma\dot{x} + \omega_0^2 x = \omega_0^2 s_0\cos(\omega_d t)\qquad\text{(13)}$$

**(b)** La solución estacionaria en notación compleja será de la forma $z(t) = Ce^{-i\omega_d t}$ en ambos casos. Primero reescribimos las ecuaciones del movimiento en notación compleja:

$$\text{A:}\quad \ddot{z} + \Gamma\dot{z} + \omega_0^2 z = -i\Gamma\omega_d s_0 e^{-i\omega_d t}\qquad\text{(14)}$$

$$\text{B:}\quad \ddot{z} + \Gamma\dot{z} + \omega_0^2 z = \omega_0^2 s_0 e^{-i\omega_d t}\qquad\text{(15)}$$

Sustituyendo nuestro ansatz en las ecuaciones del movimiento se obtiene

$$\text{A:}\quad \left(-\omega_d^2 - i\Gamma\omega_d + \omega_0^2\right)C = -i\Gamma\omega_d s_0\qquad\text{(16)}$$

$$\text{B:}\quad \left(-\omega_d^2 - i\Gamma\omega_d + \omega_0^2\right)C = \omega_0^2 s_0\qquad\text{(17)}$$

Reordenando, obtenemos

$$\text{A:}\quad C = -\frac{i\Gamma\omega_d s_0}{-\omega_d^2 - i\Gamma\omega_d + \omega_0^2}\qquad\text{(18)}$$

$$\text{B:}\quad C = \frac{\omega_0^2 s_0}{-\omega_d^2 - i\Gamma\omega_d + \omega_0^2}\qquad\text{(19)}$$

Multiplicando las expresiones por $\dfrac{-\omega_d^2 + i\Gamma\omega_d + \omega_0^2}{-\omega_d^2 + i\Gamma\omega_d + \omega_0^2}$ para que los denominadores sean reales, encontramos

$$\text{A:}\quad C = -\frac{\left[i\left(\omega_0^2 - \omega_d^2\right) - \Gamma\omega_d\right]\Gamma\omega_d s_0}{\left(\omega_0^2 - \omega_d^2\right)^2 + \Gamma^2\omega_d^2}\qquad\text{(20)}$$

$$\text{B:}\quad C = \frac{\left[\left(\omega_0^2 - \omega_d^2\right) + i\Gamma\omega_d\right]\omega_0^2 s_0}{\left(\omega_0^2 - \omega_d^2\right)^2 + \Gamma^2\omega_d^2}\qquad\text{(21)}$$

La amplitud real de oscilación es el valor absoluto de la amplitud compleja:

$$\text{A:}\quad A = \frac{\Gamma\omega_d s_0}{\sqrt{\left(\omega_0^2 - \omega_d^2\right)^2 + \Gamma^2\omega_d^2}}\qquad\text{(22)}$$

$$\text{B:}\quad A = \frac{\omega_0^2 s_0}{\sqrt{\left(\omega_0^2 - \omega_d^2\right)^2 + \Gamma^2\omega_d^2}}\qquad\text{(23)}$$

![Figura](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenPractica1_ES/figs1a.png)

Figura: amplitud en función de $\omega_d/\omega_0$ para el caso A (arriba) y el caso B (abajo), con $\Gamma = 0.3$. En el caso A la curva parte de cero, alcanza un máximo en $\omega_d/\omega_0 = 1$ y decae después; en el caso B parte de un valor no nulo, presenta un máximo pronunciado cerca de $\omega_d/\omega_0 = 1$ y decae más deprisa.

**(c)** Para hallar la frecuencia impulsora que produce la mayor amplitud debemos derivar la amplitud respecto de $\omega_d$:

$$\text{A:}\quad \frac{dA}{d\omega_d} = \frac{\Gamma s_0\left(\omega_0^4 - \omega_d^4\right)}{\left[\left(\omega_0^2 - \omega_d^2\right)^2 + \Gamma^2\omega_d^2\right]^{3/2}}\qquad\text{(24)}$$

$$\text{B:}\quad \frac{dA}{d\omega_d} = \frac{-\omega_0^2 s_0\left(2\omega_d^2 - 2\omega_0^2 + \Gamma^2\right)\omega_d}{\left[\left(\omega_0^2 - \omega_d^2\right)^2 + \Gamma^2\omega_d^2\right]^{3/2}}\qquad\text{(25)}$$

Igualando estas derivadas a cero y despejando $\omega_d$ se obtiene

$$\text{A:}\quad \omega_d = \pm\omega_0\qquad\text{(26)}$$

$$\text{B:}\quad \omega_d = 0,\ \pm\sqrt{\omega_0^2 - \frac{\Gamma^2}{2}}\qquad\text{(27)}$$

Puesto que las frecuencias negativas no son físicas y el caso de frecuencia cero es un mínimo local, encontramos que la respuesta máxima se alcanza para $\omega_d = \omega_0$ en el caso A y para $\omega_d = \sqrt{\omega_0^2 - \Gamma^2/2}$ en el caso B.

*\[Nota de la traducción: el PDF original escribe en este apartado $\sqrt{\omega_0^2 - \Gamma/2}$ en la ecuación (27) y $\sqrt{\omega_0^2 - \Gamma^2}$ en el texto que la sigue. Ambas son erratas: derivando la expresión (23) se obtiene $\omega_d = \sqrt{\omega_0^2 - \Gamma^2/2}$, que es lo que se recoge aquí.\]*

**(d)** En el caso A, la amplitud de las oscilaciones tiende a cero cuando $\omega_d/\omega_0 \to 0$ y decae a cero como $1/\omega_d$ cuando $\omega_d/\omega_0 \to \infty$. En el caso B, la amplitud tiende a $s_0$ cuando $\omega_d/\omega_0 \to 0$, y decae a cero como $1/\omega_d^2$ cuando $\omega_d/\omega_0 \to \infty$, de modo que la amplitud cae más deprisa al aumentar $\omega_d$ en el segundo caso.

*\[Nota de la traducción: el PDF original dice que en el caso B la amplitud tiende a $\omega_0^2 s_0$. Evaluando (23) en $\omega_d = 0$ se obtiene $\omega_0^2 s_0/\omega_0^2 = s_0$, que además es el resultado físicamente esperable: si el extremo del muelle se desplaza muy lentamente, la masa lo sigue con la misma amplitud.\]*

## Solución del problema 3

**(A)** Definimos las coordenadas como sigue: $x_n$ ($n = 1, 2, 3$) es el desplazamiento de la $n$-ésima masa contando desde la izquierda respecto de su posición de equilibrio, con $x_n$ positivo hacia la derecha. La matriz de masas es

$$M = \begin{pmatrix} m & 0 & 0 \\ 0 & 3m & 0 \\ 0 & 0 & m \end{pmatrix}\qquad\text{(28)}$$

y la matriz $K$ es

$$K = \omega_0^2\begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{pmatrix}\qquad\text{(29)}$$

donde $\omega_0^2 = \dfrac{k}{m}$, de modo que

$$\left[\omega_0^2\begin{pmatrix} 2 & -1 & 0 \\ -\frac{1}{3} & \frac{2}{3} & -\frac{1}{3} \\ 0 & -1 & 2 \end{pmatrix} - \omega^2 I\right]C = 0\qquad\text{(30)}$$

**(B)** De nuevo, $x_n$ ($n = 1, 2, 3$) es el desplazamiento de la $n$-ésima masa contando desde la izquierda respecto de su posición de equilibrio, con $x_n$ positivo hacia la derecha.

$$\left[\begin{pmatrix} \frac{g}{l} + \frac{k}{m} & -\frac{k}{m} & 0 \\ -\frac{k}{m} & \frac{g}{l} + \frac{4k}{m} & -\frac{3k}{m} \\ 0 & -\frac{3k}{m} & \frac{g}{l} + \frac{3k}{m} \end{pmatrix} - \omega^2 I\right]C = 0\qquad\text{(31)}$$

**(C)** Numeramos las masas empezando por la masa 1, arriba a la derecha, y avanzando en el sentido de las agujas del reloj alrededor del anillo. Definimos las coordenadas como sigue: $x_n$ ($n = 1, 2, 3, 4$) es el desplazamiento de la $n$-ésima masa respecto de su posición de equilibrio, con $x_n$ positivo en el sentido de las agujas del reloj.

$$\left[\omega_0^2\begin{pmatrix} 4 & -3 & 0 & -1 \\ -3 & 4 & -1 & 0 \\ 0 & -1 & 4 & -3 \\ -1 & 0 & -3 & 4 \end{pmatrix} - \omega^2 I\right]C = 0\qquad\text{(32)}$$

**(D)** $Q_n$ ($n = 1, 2, 3, 4$) es la carga en la placa superior del $n$-ésimo condensador contando desde la izquierda. Obsérvese, sin embargo, que estas cargas no son linealmente independientes: la carga no puede pasar de la mitad superior del circuito (la de las bobinas) a la mitad inferior, por lo que la carga total en cada mitad debe permanecer constante. Por tanto, siempre podemos despejar la carga de uno de los condensadores en función de las otras tres.

A continuación, recuerde la regla de los nodos de Kirchhoff: la suma de las corrientes en una red de conductores que se encuentran en un punto es cero. Aplicando esta ley en el punto situado entre el condensador más a la izquierda y la bobina más a la izquierda, encontramos que la corriente por la primera bobina es simplemente $\dot{Q}_1 = -I_1$, donde $I_n$ es la corriente por la $n$-ésima bobina. Aplicando la regla entre la primera y la segunda bobina se obtiene $\dot{Q}_2 = I_1 - I_2$. Análogamente, $\dot{Q}_3 = I_2 - I_3$. Por tanto,

$$I_1 = -\dot{Q}_1\qquad\text{(33)}$$

$$I_2 = -\dot{Q}_1 - \dot{Q}_2\qquad\text{(34)}$$

$$I_3 = -\dot{Q}_1 - \dot{Q}_2 - \dot{Q}_3\qquad\text{(35)}$$

$$= \dot{Q}_4\qquad\text{(36)}$$

Para deducir las ecuaciones del movimiento, recuerde que la suma de las diferencias de potencial en los elementos del circuito a lo largo de cualquier camino cerrado debe ser cero. Aplicando esta regla a las tres mallas simples del circuito se obtiene

$$\frac{1}{LC}(Q_1 - Q_2) - \dot{I}_1 = 0\qquad\text{(37)}$$

$$\frac{1}{LC}(Q_2 - Q_3) - \dot{I}_2 = 0\qquad\text{(38)}$$

$$\frac{1}{LC}(Q_3 - Q_4) + \dot{I}_3 = 0\qquad\text{(39)}$$

Si derivamos cada ecuación respecto del tiempo y sustituimos todas las derivadas de $Q$ por combinaciones lineales de las corrientes $I_n$, obtenemos las ecuaciones del movimiento en términos de las corrientes:

$$\frac{1}{LC}(2I_1 - I_2) + \ddot{I}_1 = 0\qquad\text{(40)}$$

$$\frac{1}{LC}(2I_2 - I_1 - I_3) + \ddot{I}_2 = 0\qquad\text{(41)}$$

$$\frac{1}{LC}(2I_3 - I_2) + \ddot{I}_3 = 0\qquad\text{(42)}$$

$$\implies \left[\frac{1}{LC}\begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{pmatrix} - \omega^2 I\right]C = 0\qquad\text{(43)}$$

**(E)** Definiendo $x_n$ como la distancia horizontal respecto del equilibrio de la $n$-ésima masa contando desde arriba,

$$\ddot{x}_1 + \frac{5g}{L}x_1 - \frac{2g}{L}x_2 = 0\qquad\text{(44)}$$

$$\ddot{x}_2 + \frac{3g}{L}x_2 - \frac{2g}{L}x_1 - \frac{g}{L}x_3 = 0\qquad\text{(45)}$$

$$\ddot{x}_3 + \frac{g}{L}(x_3 - x_2) = 0\qquad\text{(46)}$$

de modo que

$$\left[\frac{g}{L}\begin{pmatrix} 5 & -2 & 0 \\ -2 & 3 & -1 \\ 0 & -1 & 1 \end{pmatrix} - \omega^2 I\right]C = 0\qquad\text{(47)}$$

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*


---

<!-- MIT8.03_ExamenPractica2_ES.md -->

# Examen de práctica 2

**Instituto Tecnológico de Massachusetts**

**Física 8.03**

**EXAMEN DE PRÁCTICA 2**

------------------------------------------------------------------------

## Problema 1

Las fluctuaciones de la densidad de carga en un plasma satisfacen la ecuación de ondas que, para distorsiones unidimensionales, se reduce a

$$\frac{\partial^2\rho}{\partial t^2} = c^2\frac{\partial^2\rho}{\partial x^2} - \omega_p^2\rho$$

donde $\rho(x, t)$ es la fluctuación de la densidad de carga, $c$ es la velocidad de la luz y el parámetro fijo $\omega_p$ se conoce como frecuencia de plasma.

**a.** Halle la relación de dispersión $\omega(k)$ para soluciones de onda viajera de la forma $\rho(x, t) = a\sin(kx - \omega t)$.

**b.** Halle $k(\omega)$. Represente gráficamente el vector de ondas $k$ en función de la frecuencia de onda $\omega$. Halle y esboce las velocidades de fase y de grupo.

**c.** Demuestre que la ecuación de ondas también puede satisfacerse mediante una solución exponencialmente decreciente de la forma

$$\rho(x, t) = a\cos(\omega t)e^{-\kappa x}$$

Halle $\kappa(\omega)$ y represéntela gráficamente (puede usar la misma gráfica de la pregunta anterior, pero asegúrese de etiquetarla claramente).

------------------------------------------------------------------------

## Problema 2

Considere una cuerda muy larga unida a un pequeño anillo sin masa en $x = 0$. La cuerda tiene densidad de masa $\mu$ y se mantiene a una tensión $T$. El anillo puede moverse verticalmente sin fricción. Se aplica al anillo una fuerza externa $F(t) = F_0\sin(\omega t)$ que lo mueve arriba y abajo, dando lugar a una onda armónica estacionaria en régimen permanente que viaja hacia $x$ positiva. Suponga que la cuerda es tan larga que no hay que preocuparse por los pulsos reflejados.

**a.** Halle las condiciones de contorno que debe satisfacer una solución de onda $y(x, t)$ en $x = 0$ en términos de los parámetros dados.

**b.** Halle la frecuencia y la longitud de onda de la onda armónica en régimen permanente resultante en función de los parámetros dados.

**c.** Halle la amplitud de la onda armónica en régimen permanente resultante.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenPractica2_ES/fig1.png)

Figura 1: fuerza que crea una onda. La fuerza $F(t) = F_0\sin(\omega t)$ se aplica al anillo situado en el extremo izquierdo de la cuerda, en $x = 0$.

------------------------------------------------------------------------

## Problema 3

Considere una cuerda de longitud $L$ unida a un anillo sin masa en $x = 0$ y a un punto fijo en $x = L$. El anillo puede moverse libremente en dirección perpendicular a la cuerda a lo largo de una varilla sin fricción. La tensión de la cuerda es $T$ y la densidad de masa es $\mu$. La fuerza de la gravedad puede despreciarse frente a las demás fuerzas. En $t = 0$ la cuerda está deformada de modo que presenta un pulso rectangular estrecho de altura $H$, como se muestra en la figura 2. La anchura del pulso $D$ es mucho menor que la longitud de la cuerda $L$, pero es finita. El centro del pulso está en $x_0 = L/4$. La cuerda está inicialmente en reposo, con $\dfrac{\partial y}{\partial t}(x, 0) = 0$.

**a.** Halle la forma funcional, los números de onda $k_m$, las frecuencias $\omega_m$ y los periodos de oscilación $\tau_m$ de todos los modos normales posibles de esta cuerda en función de $L$, $T$, $\mu$ y el entero $m$.

**b.** Halle la expresión de los coeficientes $A_m$ del desarrollo de $y(x, 0)$ en modos normales. Evalúe todas las integrales y simplifique los resultados. Exprese los resultados en función de $L$, $H$, $D$ y $m$. Puede encontrar útiles las expresiones trigonométricas de la hoja de fórmulas.

**c.** Halle cuáles de los coeficientes son iguales a cero, si es que hay alguno.

**d.** Escriba la expresión completa de la descomposición de Fourier dependiente del tiempo del pulso $y(x, t)$ en forma de serie infinita de coeficientes multiplicados por los términos dependientes del tiempo apropiados.

**e.** Halle la forma de la cuerda en $t = \tau_1/2$, donde $\tau_1$ es el periodo de oscilación del modo normal más bajo. No es necesario que utilice el desarrollo de Fourier: cualquier argumento lógico será aceptable.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenPractica2_ES/fig2.png)

Figura 2: cuerda deformada. Sobre una cuerda que va de $x = 0$ a $x = L$ se levanta un pulso rectangular de altura $H$ y anchura $D$, centrado en $x = L/4$.

------------------------------------------------------------------------

## Problema 4

Considere dos cuerdas con densidades de masa $\mu_1 = \mu$ y $\mu_2 = \mu/2$ y tensiones $T_1 = T$ y $T_2 = T/2$, unidas por un anillo sin masa en $x = 0$. El anillo puede moverse a lo largo de una varilla sin fricción. La cuerda 1 se extiende hacia la izquierda, mucho más allá de $x = -L$, y la cuerda 2 está unida a un punto fijo de la pared en $x = L$. Inicialmente, un pulso triangular de anchura $L/4$ se mueve por la cuerda 1 de izquierda a derecha. En $t = 0$ el borde delantero del triángulo está en $x = -7L/8$, como se muestra en la figura 3.

**a.** Escriba las ecuaciones de ondas a ambos lados del anillo y especifique las condiciones de contorno en $x = 0$.

**b.** ¿Espera ondas reflejadas en $x = 0$ y en $x = L$? ¿Tendrá la onda reflejada el mismo signo que la onda incidente o el opuesto, en $x = 0$ y en $x = L$?

**c.** Suponga que el pulso incidente es de la forma $f_1(x, t) = f_1(x/v_1 - t)$. Halle la forma funcional de los pulsos transmitido $g(x, t)$ y reflejado $f_2(x, t)$ en $x = 0$ y $x = L$. Considere únicamente tiempos $t \leq 2L\sqrt{\dfrac{\mu}{T}}$.

**d.** Haga un esbozo de las deformaciones de la cuerda en $t = L\sqrt{\dfrac{\mu}{T}}$ y en $t = 2L\sqrt{\dfrac{\mu}{T}}$.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenPractica2_ES/fig3.png)

Figura 3: triángulo viajero. El pulso triangular de anchura $L/4$ avanza por la cuerda 1, de parámetros $T_1$ y $\mu_1$, hacia el anillo situado en $x = 0$; a la derecha, la cuerda 2, de parámetros $T_2$ y $\mu_2$, llega hasta la pared en $x = L$.

------------------------------------------------------------------------

## Problema 5

Una cuerda de longitud $L$, masa $M$ y tensión $T$ está fija por ambos extremos.

**a.** ¿Cuál es la longitud de onda $\lambda_1$ del modo normal más bajo posible, y cuál es la frecuencia asociada $\omega_1$?

**b.** ¿Cuál es la longitud de onda $\lambda_n$ del $n$-ésimo modo normal, y cuál es la frecuencia asociada $\omega_n$?

Deformamos la cuerda como se muestra en la figura 5 (el triángulo es equilátero). El desplazamiento vertical está muy exagerado en la figura. En el intervalo $0 < x < L$ la forma de la cuerda viene dada por $y = f(x)$. Según Fourier:

$$y(x) = \sum_{n=1}^{\infty} B_n\sin\frac{n\pi x}{L}\qquad\text{(1)}$$

con

$$B_n = \frac{2}{L}\int_0^L f(x)\sin\frac{n\pi x}{L}\,dx\qquad\text{(2)}$$

**c.** ¿Qué valores de $B_n$ serán cero? Razone su respuesta. ¡NO intente realizar ninguna integración!

Soltamos la cuerda pulsada con velocidad cero.

**d.** ¿Cuál es el tiempo mínimo que hay que esperar para que la cuerda tenga el aspecto de la figura 4 ($y(x) = 0$), y cuál es el tiempo mínimo para que la cuerda vuelva a tener el aspecto de la figura 5? Razone su respuesta.

**e.** Haga un esbozo de la cuerda $\dfrac{1}{4}\sqrt{\dfrac{ML}{T}}$ segundos después de soltarla.

**f.** Sea $t = 0$ el instante en que la cuerda tiene por primera vez (tras soltarla) el aspecto de la figura 4 ($y(x) = 0$). Sea $B_5$ el valor de $B$ del quinto modo normal ($n = 5$). ¡No intente calcular $B_5$! ¿Cuál es la evolución temporal de este quinto modo? Es decir, ¿cuánto vale $y_5(x, t)$? El índice 5 indica el quinto modo. Exprese su respuesta en términos de $T$, $M$, $L$ y $B_5$.

Suponga ahora que alguien (¡NO usted!) ha calculado todos los valores de $B_n$. Esa persona le muestra orgullosa, en su portátil, que sumando los 20 modos permitidos más bajos la coincidencia con la forma mostrada en la figura 5 es casi perfecta. Por curiosidad, usted quiere ver la forma de la cuerda para valores de $x$ desde $L$ hasta $3L$. La cuerda no existe ahí, pero la ecuación (1) no lo sabe.

**g.** Esboce $f(x)$ en el intervalo de $0$ a $3L$.

Dejamos ahora que el extremo de la cuerda ($x = L$) se mueva libremente sin fricción. Mantenemos la misma tensión mediante un anillo «sin masa» que desliza sin fricción a lo largo de una barra vertical.

**h.** Responda a la pregunta **a** en esta nueva configuración.

**i.** Responda a la pregunta **b** en esta configuración.

Deformamos ahora la cuerda como se muestra en la figura 5. Su amiga le muestra de nuevo, orgullosa, los resultados de su análisis de Fourier en la nueva configuración. De nuevo siente curiosidad por el intervalo de $L$ a $3L$.

**j.** Esboce $f(x)$ en el intervalo de $0$ a $3L$.

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenPractica2_ES/fig4.png)

Figura 4: cuerda fija por ambos extremos, de tensión $T$, masa $M$ y longitud $L$.

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenPractica2_ES/fig5.png)

Figura 5: triángulo sobre la cuerda. La cuerda se deforma en un triángulo de altura $A$ con el vértice en $x = L/2$.

![Figura 6](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenPractica2_ES/fig6.png)

Figura 6: cuerda con un extremo libre. Igual que la figura 4, pero el extremo en $x = L$ termina en un anillo que desliza por una barra vertical.

------------------------------------------------------------------------

## Problema 6

Considere dos planos perfectamente conductores en $z = 0$ y $z = L$. Entre los planos hay una onda electromagnética estacionaria con el campo $E$ siempre a lo largo del eje $y$. La onda se describe mediante un campo eléctrico $\vec{E}(z, t) = E_y(z, t)\hat{y}$ y un campo magnético $\vec{B}(z, t) = B_x(z, t)\hat{x}$.

**a.** Usando las condiciones de contorno del campo eléctrico en los planos conductores, escriba la expresión de $E_y(z, t)$ en el $n$-ésimo modo normal.

**b.** Usando las ecuaciones de Maxwell, o de otro modo, halle el campo magnético correspondiente $B_x(z, t)$ en el $n$-ésimo modo normal. (Pista: puede considerar una onda estacionaria como la superposición de dos ondas progresivas.)

**c.** Deduzca las expresiones del vector de Poynting $\vec{S}$ y de las densidades $U_E$ del campo eléctrico y $U_B$ del campo magnético, así como los promedios temporales de las tres magnitudes.

**d.** Para el segundo modo ($n = 2$), esboce la variación espacial de $\vec{E}$, $\vec{B}$, $U_E$ y $U_B$ entre los dos planos en $t = 0$.

------------------------------------------------------------------------

# Soluciones

## Solución del problema 1

**a.**

$$\frac{\partial^2\rho}{\partial t^2} = c^2\frac{\partial^2\rho}{\partial x^2} - \omega_p^2\rho\qquad\text{(1)}$$

Sustituyendo $\rho(x, t) = a\sin(kx - \omega t)$, obtenemos

$$-\omega^2 = -c^2k^2 - \omega_p^2\qquad\text{(2)}$$

Por tanto,

$$\omega = \sqrt{c^2k^2 + \omega_p^2}\qquad\text{(3)}$$

**b.**

$$k(\omega) = \frac{1}{c}\sqrt{\omega^2 - \omega_p^2}\qquad\text{(4)}$$

La velocidad de fase:

$$v = \frac{\omega}{k} = \frac{c}{\sqrt{1 - \dfrac{\omega_p^2}{\omega^2}}}\qquad\text{(5)}$$

La velocidad de grupo:

$$v = \left(\frac{dk}{d\omega}\right)^{-1} = c\sqrt{1 - \frac{\omega_p^2}{\omega^2}}\qquad\text{(6)}$$

**c.** Sustituyendo $\rho(x, t) = a\cos(\omega t)e^{-\kappa x}$ en la ecuación de ondas, obtenemos

$$-\omega^2 = c^2\kappa^2 - \omega_p^2\qquad\text{(7)}$$

Por tanto,

$$\kappa = \frac{1}{c}\sqrt{\omega_p^2 - \omega^2}\qquad\text{(8)}$$

## Solución del problema 2

**a.** La fuerza de tensión de la cuerda en la dirección vertical

$$T_y = T\left.\frac{dy}{dx}\right|_{x=0}\qquad\text{(9)}$$

equilibra la fuerza externa $F(t)$. Por tanto, la condición de contorno es

$$F_0\sin(\omega t) + T\left.\frac{dy}{dx}\right|_{x=0} = 0\qquad\text{(10)}$$

**b.** La onda debe satisfacer la ecuación de ondas:

$$\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2 y}{\partial t^2}\qquad\text{(11)}$$

donde $v^2 = \dfrac{T}{\mu}$. La solución compleja general con una sola frecuencia es

$$y = f\cos\left(\omega'\left(t - \frac{x}{v}\right) + \phi_1\right) + g\cos\left(\omega'\left(t + \frac{x}{v}\right) + \phi_2\right)\qquad\text{(12)}$$

Para que la solución en régimen permanente satisfaga la condición de contorno para $t$ arbitrario, esta $\omega'$ debe ser igual a $\omega$. Por tanto, la solución en régimen permanente tiene frecuencia angular $\omega$ y longitud de onda

$$\lambda = \frac{2\pi v}{\omega}\qquad\text{(13)}$$

**c.** No necesitamos conservar el término del pulso reflejado, así que basta con sustituir

$$y = f\cos\left(\omega\left(t - \frac{x}{v}\right) + \phi_1\right)\qquad\text{(14)}$$

en la condición de contorno

$$F_0\sin(\omega t) + T\frac{\partial y}{\partial x} = 0\qquad\text{(15)}$$

con lo que tenemos

$$F_0\sin(\omega t) + \frac{Tf\omega}{v}\sin(\omega t + \phi_1) = 0\qquad\text{(16)}$$

Podemos tomar $\phi_1 = \pi$, $f = \dfrac{F_0 v}{T\omega}$, de modo que la onda armónica resultante en régimen permanente tiene la forma

$$y = \frac{F_0 v}{T\omega}\cos\left(\omega\left(t - \frac{x}{v}\right) + \pi\right)\qquad\text{(17)}$$

con amplitud

$$A = \frac{F_0 v}{T\omega}\qquad\text{(18)}$$

## Solución del problema 3

**a.** La condición de contorno es

$$\left.\frac{\partial y}{\partial x}\right|_{x=0} = 0\qquad\text{(19)}$$

$$y(L, t) = 0\qquad\text{(20)}$$

Los modos normales tienen entonces la forma

$$y(x) = \cos(kx)\qquad\text{(21)}$$

con la condición

$$\cos(kL) = 0\qquad\text{(22)}$$

Por tanto, el modo normal $m$ es

$$y_m = \cos(k_m x)\ ,\qquad k_m = \left(m - \frac{1}{2}\right)\frac{\pi}{L} \quad (m = 1, 2, \ldots)\qquad\text{(23)}$$

La frecuencia de un modo normal está relacionada con $k$ mediante

$$\omega = kv = k\sqrt{\frac{T}{\mu}}\qquad\text{(24)}$$

Por tanto,

$$\omega_m = \left(m - \frac{1}{2}\right)\frac{\pi}{L}\sqrt{\frac{T}{\mu}}\qquad\text{(25)}$$

$$\tau_m = \frac{2\pi}{\omega_m} = \frac{2L}{m - \frac{1}{2}}\sqrt{\frac{\mu}{T}}\qquad\text{(26)}$$

**b.**

$$\begin{aligned}
A_m &= \frac{2}{L}\int_0^L y(x, 0)\cos\left(\left(m - \frac{1}{2}\right)\frac{\pi x}{L}\right)dx \\[4pt]
&= \frac{2}{L}\int_{L/4 - D/2}^{L/4 + D/2} H\cos\left(\left(m - \frac{1}{2}\right)\frac{\pi x}{L}\right)dx \\[4pt]
&= \frac{2H}{\pi\left(m - \frac{1}{2}\right)}\left[\sin\left(\left(m - \frac{1}{2}\right)\pi\left(\frac{1}{4} + \frac{D}{2L}\right)\right) - \sin\left(\left(m - \frac{1}{2}\right)\pi\left(\frac{1}{4} - \frac{D}{2L}\right)\right)\right] \\[4pt]
&= \frac{4H}{\pi\left(m - \frac{1}{2}\right)}\cos\frac{\left(m - \frac{1}{2}\right)\pi}{4}\,\sin\frac{\left(m - \frac{1}{2}\right)\pi D}{2L}
\end{aligned}\qquad\text{(27)}$$

**c.** $A_m = 0$ cuando

$$\cos\frac{\left(m - \frac{1}{2}\right)\pi}{4} = 0\qquad\text{(28)}$$

o bien

$$\sin\frac{\left(m - \frac{1}{2}\right)\pi D}{2L} = 0\qquad\text{(29)}$$

La primera condición no puede darse nunca para $m$ entero. Esto se debe a que ningún modo normal tiene $y_m(L/4) = 0$.

La segunda condición puede darse si existe algún $m$ tal que

$$\frac{\left(m - \frac{1}{2}\right)D}{2L} = p\qquad\text{(30)}$$

sea un número entero.

**d.**

$$\begin{aligned}
y(x, t) = \sum_{m=1}^{\infty} & \frac{4H}{\pi\left(m - \frac{1}{2}\right)}\cos\frac{\left(m - \frac{1}{2}\right)\pi}{4}\,\sin\frac{\left(m - \frac{1}{2}\right)\pi D}{2L}\\
& \cos\left(\left(m - \frac{1}{2}\right)\frac{\pi x}{L}\right)\cos\left(\left(m - \frac{1}{2}\right)\frac{v\pi}{L}t\right)\qquad\text{(31)}
\end{aligned}$$

Los factores temporales de cada componente se eligen como $\cos(\omega_m t)$, de modo que la derivada temporal $\dfrac{\partial y}{\partial t}(x, 0) = 0$.

**e.**

$$\tau_1 = \frac{4L}{v}\ ,\qquad t = \frac{\tau_1}{2} = \frac{2L}{v}\qquad\text{(32)}$$

La configuración inicial de la cuerda estática puede descomponerse en dos pulsos cuadrados que viajan en direcciones opuestas, cada uno con velocidad $v$, anchura $D$ y altura $\dfrac{H}{2}$. Al cabo del tiempo $t$, cada uno de ellos ha viajado de vuelta a la posición original, habiendo chocado una vez con la pared. Puesto que chocar con la pared añade un desfase de $\pi$, es decir, invierte el pulso, mientras que chocar con el anillo sin masa no cambia la forma del pulso, cada uno de los dos pulsos viajeros queda invertido al cabo del tiempo $t$.

Por tanto, la forma de la cuerda en el instante $t = \dfrac{\tau_1}{2}$ es la del pulso original invertido.

## Solución del problema 4

**a.** La ecuación de ondas a la izquierda:

$$\frac{\partial^2 y_L}{\partial x^2} = \frac{\mu}{T}\frac{\partial^2 y_L}{\partial t^2}\qquad\text{(33)}$$

La ecuación de ondas a la derecha:

$$\frac{\partial^2 y_R}{\partial x^2} = \frac{\mu}{T}\frac{\partial^2 y_R}{\partial t^2}\qquad\text{(34)}$$

La condición de contorno en $x = 0$: la componente vertical de la tensión de la cuerda a izquierda y derecha debe equilibrarse, por lo que

$$T\left.\frac{\partial y_L}{\partial x}\right|_{x=0^-} = \frac{T}{2}\left.\frac{\partial y_R}{\partial x}\right|_{x=0^+}\qquad\text{(35)}$$

Tenemos además la condición de continuidad:

$$y_L\big|_{x=0^-} = y_R\big|_{x=0^+}\qquad\text{(36)}$$

**b.** Hay ondas reflejadas en $x = 0$ y en $x = L$. La onda reflejada en $x = 0$ no cambia de signo, ya que la impedancia $\sqrt{T\mu}$ de la izquierda es mayor que la impedancia de la derecha. La onda reflejada en $x = L$ sí cambia de signo, porque en $x = L$ la condición de contorno es de extremo fijo. Por tanto, estas ondas reflejadas tienen signos opuestos.

**c.** Denotamos

$$v = v_1 = \sqrt{\frac{T}{\mu}}\qquad\text{(37)}$$

Por tanto, la onda a la izquierda de $x = 0$:

$$y_L = f_1(x/v - t) + f_2(x, t)\qquad\text{(38)}$$

donde la onda reflejada es

$$f_2(x, t) = r\,f_1(-x/v - t)\qquad\text{(39)}$$

La onda a la derecha de $x = 0$:

$$y_R = g(x, t) + g_2(x, t)\qquad\text{(40)}$$

Aquí $g(x, t)$ es la onda transmitida a través de $x = 0$:

$$g(x, t) = \mathrm{t}\,f_1(x/v - t)\qquad\text{(41)}$$

y $g_2(x, t)$ es la onda reflejada desde $x = L$:

$$g_2(x, t) = r_2\,f_1((2L - x)/v - t)\qquad\text{(42)}$$

Entonces la condición de contorno en $x = 0$ da:

$$\frac{T}{v}f_1'(-t) - \frac{rT}{v}f_1'(-t) = \frac{\mathrm{t}T}{2v}f_1'(-t) - \frac{r_2 T}{2v}f_1'(2L/v - t)\qquad\text{(43)}$$

Puesto que

$$f_1(t \geq 0) \equiv 0\qquad\text{(44)}$$

y solo consideramos tiempos $t \leq 2L/v$, el último término de (43) se anula, con lo que tenemos

$$1 - r = \frac{\mathrm{t}}{2}\qquad\text{(45)}$$

y

$$1 + r = \mathrm{t}\qquad\text{(46)}$$

Por tanto,

$$r = \frac{1}{3}\ ,\qquad \mathrm{t} = \frac{4}{3}\qquad\text{(47)}$$

En el contorno $x = L$ tenemos

$$g(L, t) + g_2(L, t) = 0\qquad\text{(48)}$$

de donde

$$r_2 = -\mathrm{t} = -\frac{4}{3}\qquad\text{(49)}$$

**d.** En el instante $t = \dfrac{L}{v}$, la mitad derecha del pulso ha pasado $x = 0$ y también se ha reflejado hacia la izquierda. La mitad izquierda del pulso sigue propagándose hacia la derecha. Denotando por 1 la altura del borde derecho del pulso inicial, la forma de la cuerda en $t = \dfrac{L}{v}$ presenta escalones de alturas $\frac{1}{3}$, $\frac{2}{3}$ y $\frac{4}{3}$ en torno a $x = 0$.

En el instante $t = \dfrac{2L}{v}$, el pulso reflejado $f_2$ ha viajado de vuelta hasta $x = -L$ y el pulso transmitido $g$ ha alcanzado $x = L$. La mitad derecha de $g$ ya se ha reflejado, mientras que la mitad izquierda sigue propagándose hacia la derecha. La forma de la cuerda en $t = \dfrac{2L}{v}$ muestra el pulso de altura $\frac{1}{3}$ a la izquierda y el pulso invertido de altura $-\frac{4}{3}$ junto a $x = L$.

## Solución del problema 5

**a.** El modo más bajo tiene la forma

$$y_1 = \sin(k_1 x)\ ,\qquad k_1 = \frac{\pi}{L}\qquad\text{(50)}$$

La longitud de onda

$$\lambda_1 = 2L\qquad\text{(51)}$$

y la frecuencia

$$\omega_1 = vk_1 = k_1\sqrt{\frac{TL}{M}} = \frac{\pi}{L}\sqrt{\frac{TL}{M}}\qquad\text{(52)}$$

**b.** El $n$-ésimo modo tiene la forma

$$y_n = \sin(k_n x)\ ,\qquad k_n = \frac{n\pi}{L}\qquad\text{(53)}$$

La longitud de onda

$$\lambda_n = \frac{2L}{n}\qquad\text{(54)}$$

y la frecuencia

$$\omega_n = vk_n = k_n\sqrt{\frac{TL}{M}} = \frac{n\pi}{L}\sqrt{\frac{TL}{M}}\qquad\text{(55)}$$

**c.** Los modos con $y_n(L/2) = 0$ serán cero, porque son antisimétricos respecto de $x = L/2$:

$$y_n(L/2 - x) = -y_n(L/2 + x)\qquad\text{(56)}$$

No debería haber ninguna contribución de estos modos. Por tanto, se anulan los modos $n = 2m$.

**d.** En $t = 0$ la cuerda tiene velocidad nula. La función completa $y(x, t)$:

$$y(x, t) = \sum_{n=1}^{\infty} B_n\sin\frac{n\pi x}{L}\cos\frac{n\pi vt}{L}\qquad\text{(57)}$$

Al cabo del tiempo $T = \dfrac{2L}{v}$, todos los factores dependientes del tiempo $\cos\dfrac{n\pi vt}{L}$ vuelven a valer 1. Este es el tiempo mínimo, ya que $B_1 \neq 0$.

**e.** La configuración inicial puede descomponerse en dos pulsos que viajan en direcciones opuestas con velocidad $v$, altura $A/2$ y la misma anchura que la configuración inicial. Al chocar con el contorno izquierdo o derecho, cambian de signo tras reflejarse. Por tanto, en el instante $t = \dfrac{L}{4v}$ la configuración de la cuerda es una línea recta.

**f.** Este instante es $t = \dfrac{L}{4v}$ en la expresión (57). Desplazando el origen de tiempos a este instante, tenemos la expresión del quinto modo:

$$y_5(x, t) = B_5\sin\frac{5\pi x}{L}\cos\frac{5\pi v(t + L/4v)}{L} = B_5\sin\frac{5\pi x}{L}\cos\left(5\pi t\sqrt{\frac{T}{ML}} + \frac{5\pi}{4}\right)\qquad\text{(58)}$$

**g.** Puesto que todos los modos no nulos corresponden a $n$ impar, la función $f(x)$ en el intervalo de $L$ a $2L$ debe ser la opuesta de la función $f(x)$ en el intervalo de $0$ a $L$:

$$f(x + L) = \sum_{m=1}^{20} B_m\sin\frac{(2m-1)\pi(x + L)}{L} = -\sum_{m=1}^{20} B_m\sin\frac{(2m-1)\pi x}{L} = -f(x)\qquad\text{(59)}$$

mientras que la función $f(x)$ en el intervalo de $2L$ a $3L$ debe ser igual a la función $f(x)$ en el intervalo de $0$ a $L$:

$$f(x + 2L) = \sum_{m=1}^{20} B_m\sin\frac{(2m-1)\pi(x + 2L)}{L} = \sum_{m=1}^{20} B_m\sin\frac{(2m-1)\pi x}{L} = f(x)\qquad\text{(60)}$$

*\[Nota de la traducción: el PDF original cierra la ecuación (60) con $= -f(x)$, en contradicción con el propio desarrollo que la precede y con el texto que la introduce («debe ser igual a»). Como $\sin\frac{(2m-1)\pi(x+2L)}{L} = \sin\left(\frac{(2m-1)\pi x}{L} + 2(2m-1)\pi\right) = \sin\frac{(2m-1)\pi x}{L}$, el resultado correcto es $f(x + 2L) = f(x)$.\]*

**h.** En esta nueva configuración, el modo más bajo tiene la forma

$$y_1 = \sin(k_1 x)\ ,\qquad k_1 = \frac{\pi}{2L}\qquad\text{(61)}$$

La longitud de onda

$$\lambda_1 = 4L\qquad\text{(62)}$$

y la frecuencia

$$\omega_1 = vk_1 = k_1\sqrt{\frac{TL}{M}} = \frac{\pi}{2L}\sqrt{\frac{TL}{M}}\qquad\text{(63)}$$

**i.** El $n$-ésimo modo tiene la forma

$$y_n = \sin(k_n x)\ ,\qquad k_n = \frac{(2n-1)\pi}{2L}\qquad\text{(64)}$$

La longitud de onda

$$\lambda_n = \frac{4L}{2n-1}\qquad\text{(65)}$$

y la frecuencia

$$\omega_n = vk_n = k_n\sqrt{\frac{TL}{M}} = \frac{(2n-1)\pi}{2L}\sqrt{\frac{TL}{M}}\qquad\text{(66)}$$

**j.** En este caso, la función $f(x)$ en el intervalo de $L$ a $2L$ debe ser igual a la función $f(x)$ en el intervalo de $0$ a $L$:

$$f(2L - x) = \sum_{m=1}^{20} B_m\sin\frac{(2m-1)\pi(2L - x)}{2L} = \sum_{m=1}^{20} B_m\sin\frac{(2m-1)\pi x}{2L} = f(x)\qquad\text{(67)}$$

mientras que la función $f(x)$ en el intervalo de $2L$ a $3L$ debe ser la opuesta de la función $f(x)$ en el intervalo de $0$ a $L$:

$$f(x + 2L) = \sum_{m=1}^{20} B_m\sin\frac{(2m-1)\pi(x + 2L)}{2L} = -\sum_{m=1}^{20} B_m\sin\frac{(2m-1)\pi x}{2L} = -f(x)\qquad\text{(68)}$$

## Solución del problema 6

**a.** Las condiciones de contorno del campo eléctrico son

$$\vec{E}(0, t) = \vec{E}(L, t) = 0\qquad\text{(69)}$$

Por tanto, el $n$-ésimo modo normal es

$$E_y^{(n)}(z) = \sin\frac{n\pi z}{L}\qquad\text{(70)}$$

$$E_y^{(n)}(z, t) = \sin\frac{n\pi z}{L}\cos\frac{n\pi ct}{L}\qquad\text{(71)}$$

**b.** La onda estacionaria puede descomponerse en

$$E_y^{(n)}(z, t) = \sin\frac{n\pi z}{L}\cos\frac{n\pi ct}{L} = \operatorname{Re}\left[\frac{1}{2}e^{i\frac{n\pi}{L}(z - ct) - \frac{i\pi}{2}} + \frac{1}{2}e^{i\frac{n\pi}{L}(z + ct) - \frac{i\pi}{2}}\right]\qquad\text{(72)}$$

Para una componente de onda viajera con vector de ondas unitario $\hat{k}$,

$$\vec{B} = \frac{1}{c}\hat{k} \times \vec{E}\qquad\text{(73)}$$

Por tanto,

$$\vec{B} = \operatorname{Re}\left[\hat{z} \times \hat{y}\,\frac{1}{2}e^{i\frac{n\pi}{L}(z - ct) - \frac{i\pi}{2}} - \hat{z} \times \hat{y}\,\frac{1}{2}e^{i\frac{n\pi}{L}(z + ct) - \frac{i\pi}{2}}\right] = \frac{\hat{x}}{c}\cos\frac{n\pi z}{L}\sin\frac{n\pi ct}{L}\qquad\text{(74)}$$

**c.**

$$\vec{S} = \frac{1}{\mu_0}\vec{E} \times \vec{B} = -\frac{\hat{z}}{\mu_0 c}\sin\frac{n\pi z}{L}\cos\frac{n\pi z}{L}\cos\frac{n\pi ct}{L}\sin\frac{n\pi ct}{L}\qquad\text{(75)}$$

$$\langle\vec{S}\rangle = 0\qquad\text{(76)}$$

$$U_E = \frac{1}{2}\varepsilon_0\vec{E}^2 = \frac{1}{2}\varepsilon_0\sin^2\frac{n\pi z}{L}\cos^2\frac{n\pi ct}{L}\qquad\text{(77)}$$

$$\langle U_E\rangle = \frac{1}{4}\varepsilon_0\sin^2\frac{n\pi z}{L}\qquad\text{(78)}$$

$$U_B = \frac{1}{2\mu_0}\vec{B}^2 = \frac{1}{2\mu_0 c^2}\cos^2\frac{n\pi z}{L}\sin^2\frac{n\pi ct}{L} = \frac{1}{2}\varepsilon_0\cos^2\frac{n\pi z}{L}\sin^2\frac{n\pi ct}{L}\qquad\text{(79)}$$

$$\langle U_B\rangle = \frac{1}{4}\varepsilon_0\cos^2\frac{n\pi z}{L}\qquad\text{(80)}$$

*\[Nota de la traducción: el PDF original etiqueta la ecuación (80) como $\langle U_E\rangle$; por el contexto y por la expresión (79) que la precede, se trata de $\langle U_B\rangle$.\]*

Obsérvese que

$$\langle U_E + U_B\rangle = \frac{1}{4}\varepsilon_0\qquad\text{(81)}$$

que está distribuida uniformemente. La amplitud del modo normal se ha fijado en 1 (sin unidades).

**d.** En el instante $t = 0$ elegido, $\vec{B}$ y $U_B$ se anulan idénticamente: $E_y$ presenta la variación espacial $\sin\frac{2\pi z}{L}$, con un nodo en $z = L/2$, y $U_E$ es proporcional a $\sin^2\frac{2\pi z}{L}$, con máximos en $z = L/4$ y $z = 3L/4$. En otro instante en el que $\vec{B}$ y $U_B$ no se anulen, $B_x$ varía como $\cos\frac{2\pi z}{L}$ y $U_B$ como $\cos^2\frac{2\pi z}{L}$, con máximos en $z = 0$, $z = L/2$ y $z = L$.

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*


---

<!-- MIT8.03_ProblemSet10_ES.md -->

*Massachusetts Institute of Technology*

**Física 8.03SC — Otoño de 2016**

**Tarea 10**

## Problemas

**Problema 10.1 (20 pts)**

Una fuente de luz puntual, $S$, de frecuencia $\nu$, se coloca en el aire ($n=1$) a una distancia $L$ de un conductor perfecto, como se muestra en la figura 1.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet10_ES/fig1.png)

Figura 1: fuente puntual $S$ situada a una distancia $L$ de un espejo conductor perfecto, con un observador lejano en la dirección perpendicular al conductor.

1.  ¿Para qué valores de $L$ verá el observador un máximo en el patrón de interferencia, a gran distancia de $S$, en una dirección perpendicular al conductor perfecto? (Puede ignorar cualquier absorción de la luz reflejada por parte de $S$.)
2.  ¿Para qué valores de $L$ verá el observador un mínimo en el patrón de interferencia, en las mismas condiciones?
3.  ¿Cuál es el grosor mínimo de vidrio, de índice de refracción $n$, que debe colocarse entre la fuente de luz y el espejo, de modo que, para un $L$ dado, un mínimo pase a ser un máximo y viceversa? (Puede suponer que no hay reflexión en la superficie del vidrio.)

**Problema 10.2 (20 pts)**

Tres rendijas largas y estrechas, mostradas en la figura 2, se iluminan con una fuente de luz monocromática de longitud de onda $\lambda = 500$ nanómetros ($1\ \text{nm}=10^{-9}\ \text{m}$). La distancia entre los centros de las rendijas es $d=1$ milímetro. La luz transmitida se proyecta sobre una pantalla a $L=5$ metros. Suponga que las rendijas son tan estrechas que puede ignorarse la difracción de una sola rendija.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet10_ES/fig2.png)

Figura 2: tres rendijas horizontales separadas 1 mm entre sí, iluminadas y proyectadas sobre una pantalla a 5 m de distancia.

Considere primero el caso en que la rendija superior está completamente bloqueada.

1.  ¿Cuál es la distancia, en milímetros, entre el máximo central de intensidad (franja) y el primer mínimo en la pantalla?
2.  Esboce la distribución de intensidad cerca de la franja central, incluyendo un total de 5 máximos de intensidad vecinos (el central y dos a cada lado). Etiquete cuidadosamente los ejes. ¿Cuál es la intensidad máxima de cada una de las 5 franjas si la intensidad de una sola rendija es $I_0$?

Ahora se destapa la rendija superior.

1.  ¿Cuál es ahora la distancia, en milímetros, entre el máximo central (franja) y el primer mínimo en la pantalla?
2.  Esboce la nueva distribución de intensidad cerca de la franja central, incluyendo un total de 5 máximos vecinos (el central y dos a cada lado), en función de la distancia al centro del pico central, $x$. Etiquete cuidadosamente los ejes.
3.  ¿Cuál es la intensidad máxima de cada una de las 5 franjas?

Ahora la rendija superior se cubre con un material mágico que transmite solo la mitad de la intensidad incidente, sin afectar a la fase, la polarización ni ninguna otra propiedad de la luz.

1.  ¿Cuál es la intensidad máxima que puede tener una franja en esta configuración? ¿Cuál de las 5 franjas vecinas tendrá esa intensidad?
2.  Escriba una ecuación, en términos de la posición de la franja $x$, que pueda resolverse para hallar la posición del mínimo de intensidad más cercano al pico central. No la resuelva.
3.  Esboce ahora la nueva distribución de intensidad cerca de la franja central, incluyendo un total de 5 máximos vecinos (el central y dos a cada lado).

**Problema 10.3 (20 pts)**

Dos radiadores dipolares están separados una distancia $\lambda/2$ a lo largo del eje $x$. Los dipolos están orientados según $z$. Suponga $r \gg \lambda$. Véase la figura 3.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet10_ES/fig3.png)

Figura 3: dos dipolos orientados en $z$, separados $\lambda/2$ en el eje $x$, con un punto de observación a distancia $r$ y ángulo $\theta$ en el plano $x$-$y$.

1.  Encuentre las intensidades relativas de la radiación en el plano $x$-$y$ para $\theta = 0, \pi/3, \pi/2$ y $\pi$, si las oscilaciones de los dipolos están en fase.
2.  Repita el apartado a si los osciladores están desfasados $\pi$.
3.  Los osciladores están separados una distancia $\lambda/4$ y desfasados $\pi/2$. Encuentre las intensidades relativas para $\theta = 0, \pi/2, 3\pi/2$.

**Problema 10.4 (20 pts)**

Una pequeña cantidad de aceite ($n=1.45$) cae sobre la superficie lisa de un lago ($n=1.33$). Forma una película de espesor continuamente decreciente a medida que se extiende sobre la superficie. Un observador contempla el aspecto cambiante de la luz del cielo (blanca) reflejada con incidencia casi normal. Véanse las longitudes de onda en la tabla 1.

| Color  | Longitud de onda \[nm\]               |
|--------|---------------------------------------|
| blanco | todas las longitudes de onda visibles |
| azul   | 480                                   |
| verde  | 530                                   |
| rojo   | 650                                   |
| negro  | ninguna longitud de onda visible      |

*Tabla 1: longitudes de onda de la luz visible.*

1.  Inicialmente, cuando la película es gruesa, la luz reflejada parece blanca a simple vista. Vista a través de un filtro de banda estrecha centrado en el rojo, la intensidad reflejada cambia con el tiempo. A través del filtro se observa que la reflexión empieza siendo brillante, pasa por 10 mínimos y vuelve a un máximo. ¿Cuánto ha cambiado el espesor de la película durante ese tiempo?
2.  Solo cuando la película se ha adelgazado lo suficiente aparece coloreada a simple vista. ¿En qué orden de interferencia $m$ el espesor para interferencia constructiva en el rojo supera al espesor para interferencia constructiva en el azul del siguiente orden superior? (Para espesores mayores que este, distintas porciones del espectro visible se solapan en la luz reflejada.)
3.  Justo cuando la película en la superficie plana parece verde, una onda superficial generada por el viento cruza el campo de visión. Como resultado, el color oscila con el tiempo. ¿Hacia qué extremo del espectro cambia el color? (Recuerde que, en la interferencia de películas delgadas, la diferencia de camino óptico es proporcional al coseno del ángulo que forma el rayo con la normal dentro de la película.)

**Problema 10.5 (20 pts)**

Considere una pantalla con dos rendijas paralelas largas. La anchura de cada rendija es $a$ y la distancia entre las dos rendijas es $b$. Se iluminan con un haz paralelo de luz de longitud de onda $\lambda$, como se muestra en la figura 4.

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet10_ES/fig4.png)

Figura 4: pantalla con dos rendijas de anchura $a$ separadas una distancia $b$ entre centros, iluminadas por un haz de longitud de onda $\lambda$; el ángulo de observación se mide como $\psi$.

El patrón de difracción se proyecta sobre una pantalla lejos de las rendijas. La distribución de luz sobre la pantalla en función de $\sin\psi$ se muestra en la figura 5.

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet10_ES/fig5.png)

Figura 5: patrón de interferencia y difracción — intensidad frente a $\sin\psi$ entre −0.8 y 0.8, mostrando una envolvente de difracción de anchura moderada modulada por franjas de interferencia más finas, con máximo de intensidad ≈4 en el centro.

1.  Estime los valores de $a$ y $b$ en unidades de $\lambda$.
2.  Ahora las rendijas se ensanchan de modo que la distancia entre ellas se duplica a $2b$, manteniendo la misma anchura $a$. Esboce la intensidad de la luz en función de $\sin\psi$. Etiquete cuidadosamente el eje horizontal y use la misma escala que en la figura 5. El eje vertical es arbitrario; solo se pregunta por la forma del patrón, no por su magnitud absoluta.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.


---

<!-- MIT8.03_ProblemSet1_ES.md -->

*Massachusetts Institute of Technology*

**Física 8.03SC — Otoño de 2016**

**Tarea 1**

## Problemas

**Problema 1.1 (20 pts)**

Para el sistema de masa y muelle discutido en clase (las notas de Howard Georgi, Ecs. (1.1)-(1.8)), suponga que el sistema cuelga verticalmente en el campo gravitatorio terrestre, con el extremo superior del muelle fijo. Demuestre que la frecuencia de las oscilaciones verticales viene dada por la Ec. (1.5). Explique por qué la gravedad no afecta a la frecuencia angular.

**Problema 1.2 (20 pts)**

En cada uno de los tres casos siguientes, el movimiento de una partícula se especifica mediante una representación compleja de su desplazamiento, velocidad o aceleración. Para cada caso, encuentre una representación real para las tres cantidades —desplazamiento, velocidad y aceleración— en la forma:

$$\eta(t) = c \cos \omega t + d \sin \omega t$$

donde $c$ y $d$ son cantidades reales independientes del tiempo. $A$, $B$, $C$ y $\tau$ son cantidades reales. Si necesita integrar, suponga que las constantes de integración son iguales a cero.

1.  $X(t) = A e^{-i(\omega t - \pi/2)}$
2.  $\dot X(t) = Bi\omega\tau\, e^{-i(\omega t + \pi/6)}$
3.  $\ddot X(t) = C \dfrac{1}{1+i\omega\tau}\, e^{-i\omega t}$

En cada uno de los siguientes casos, el movimiento de una partícula se especifica mediante una representación real de su desplazamiento, velocidad o aceleración. Para cada caso, encuentre la representación compleja de las tres cantidades —desplazamiento, velocidad y aceleración— en la forma

$$Q(t) = Q e^{-i(\omega t + \varphi)}$$

donde $Q$ y $\varphi$ son cantidades reales independientes del tiempo. $\alpha$, $\beta$, $\gamma$ y $\delta$ son cantidades reales y positivas.

1.  $x(t) = \alpha \cos \omega t - \beta \sin \omega t$
2.  $\dot x(t) = -\gamma \sin(\omega t + \pi/3)$
3.  $\ddot x(t) = \delta \cos(\omega t + \pi/6)$

**Problema 1.3 (20 pts)**

Un bloque de masa $M$ desliza sin fricción entre dos muelles de constantes $K$ y $2K$, como se muestra en la figura 1. El sistema está obligado a moverse solo a lo largo del eje de los muelles.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet1_ES/fig1.png)

Figura 1: bloque de masa $M$ conectado por la izquierda a un muelle de constante $K$ y por la derecha a un muelle de constante $2K$, ambos anclados a paredes fijas.

1.  Calcule la frecuencia angular de las oscilaciones.
2.  Si la velocidad del bloque en la posición de equilibrio es $v$, calcule la amplitud de las oscilaciones.
3.  Escriba una expresión para la posición de la masa como función real, $x(t)$ (con la condición inicial del apartado b).
4.  Escriba una expresión para la posición de la masa como función compleja, $z(t)$, en forma irreducible (con la condición inicial del apartado b).

**Problema 1.4 (20 pts)**

Una partícula de masa $m$ se mueve en el eje $x$ con energía potencial

$$V(x) = \frac{E_0}{a^4}\left(x^4 + 4a x^3 - 8a^2 x^2\right)$$

1.  Encuentre las posiciones en las que la partícula está en equilibrio estable.
2.  Encuentre la frecuencia angular de las pequeñas oscilaciones en torno a cada posición de equilibrio estable.
3.  ¿Qué entiende por pequeñas oscilaciones? Sea cuantitativo y dé una respuesta distinta para cada punto de equilibrio estable.

**Problema 1.5 (20 pts)**

Considere un péndulo simple formado por una masa puntual $m$ unida a una cuerda sin masa de longitud $L$ que cuelga de un soporte fijo y está obligada a moverse en un plano vertical (véase la figura 2). Suponga que la aceleración gravitatoria es $g$.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet1_ES/fig2.png)

Figura 2: péndulo de longitud $L$ colgando de un soporte fijo, con ángulo $\theta$ respecto a la vertical y ejes cartesianos $x$ horizontal e $y$ vertical con origen en el punto de equilibrio.

1.  Parametrice el movimiento del péndulo en términos del ángulo $\theta$, su desviación respecto a la vertical. Encuentre la ecuación de movimiento exacta ($\tau = I\alpha$) del péndulo en función de $\theta$.
2.  Suponga que el ángulo $\theta$ es pequeño y encuentre la ecuación de movimiento armónico simple aproximada.
3.  Justifique sus aproximaciones. Encuentre el intervalo de $\theta$ para el que el péndulo puede considerarse un MAS. ¿Cuál es el periodo de oscilación de este MAS?
4.  Calcule la energía potencial exacta del péndulo en función de $\theta$. A continuación, demuestre que el desarrollo de Taylor conduce al mismo resultado que en el apartado b.
5.  Parametrice el movimiento del péndulo en términos de la coordenada cartesiana $x$, en el sistema de coordenadas con origen en la posición de equilibrio del péndulo y eje $x$ horizontal en el plano del péndulo. Encuentre la ecuación de movimiento exacta ($F = ma$) del péndulo en función de $x$.
6.  Suponga que $x$ es pequeño y encuentre la ecuación de movimiento armónico simple aproximada.
7.  Justifique sus aproximaciones. Encuentre el intervalo de $x$ para el que el péndulo puede considerarse un MAS.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.


---

<!-- MIT8.03_ProblemSet2_ES.md -->

*Massachusetts Institute of Technology*

**Física 8.03SC — Otoño de 2016**

**Tarea 2**

## Problemas

**Problema 2.1 (20 pts)**

En el circuito de la figura 1, $C = 2\ \mu\text{F}$, $L = 2\ \text{mH}$ y $R = 20\ \Omega$. Inicialmente, en el instante $t=0$, tenemos $V_C(t=0) = 5\ \text{V}$ y corriente $i(t=0) = 0.5\ \text{A}$.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet2_ES/fig1.png)

Figura 1: circuito RLC con un condensador $C$, una bobina $L$ y una resistencia $R$ en serie, recorridos por la corriente $i(t)$.

1.  Traduzcamos ahora esta situación física a matemáticas. Escriba la ecuación de movimiento en términos de $Q(t)$, la carga almacenada en el condensador.
2.  ¿Qué tipo de oscilador estamos considerando aquí? (¿No amortiguado, subamortiguado, con amortiguamiento crítico o sobreamortiguado?) Explique por qué lo cree así.
3.  Encuentre una expresión analítica para $V_C(t)$ para todo $t>0$.

**Problema 2.2 (20 pts)**

En un laboratorio cercano al Gran Colisionador de Hadrones, un delicado cristal de masa $M$ está sostenido por cuatro muelles sin masa en paralelo, cada uno con constante $k$. Todo el montaje se coloca sobre una mesa. Cuando los estudiantes de posgrado del laboratorio mueven la mesa por el suelo, el tablero vibra, produciendo una fuerza vertical efectiva $F = MA_0\cos(\omega_d t)$ sobre la masa $M$ en el sistema de referencia del tablero.

1.  Sea $x$ el desplazamiento vertical del cristal respecto a su posición de equilibrio. Escriba la ecuación de movimiento del instrumento. (Puede suponer que no hay fuerza de rozamiento en esta parte del problema.)
2.  Encuentre la amplitud de vibración del cristal (la masa $M$) en el estado estacionario. (Suponiendo que hay pérdidas de energía muy pequeñas en este sistema, de modo que la solución homogénea se extingue cuando $t \to \infty$.)
3.  Para reducir en un factor diez la amplitud de vibración del cristal obtenida en (a), ¿cómo propondría modificar los cuatro muelles?, es decir, ¿cuánto más largos (o cortos) deberían ser los nuevos muelles? Suponga $k/M \gg \omega_d^2$. (Pista: la constante de un muelle es proporcional a su área e inversamente proporcional a su longitud.)
4.  Una forma mejor de reducir esta amplitud de vibración en un factor diez respecto a la original es insertar una especie de amortiguador blando y sin masa entre el cristal y la mesa, en paralelo con los muelles. Suponiendo que el amortiguador produce una fuerza resistiva igual a $-b$ veces la velocidad de $M$, deduzca una ecuación que le permita determinar el valor de $b$ en términos de $k$, $M$, $\omega_d$, y resuelva para $b$, suponiendo $k/M \gg \omega_d^2$.

**Problema 2.3 (20 pts)**

Durante un huracán reciente, una física esperaba en un cruce. Observó el semáforo, suspendido sobre la calle por cables, oscilar verticalmente con el viento. Como había cursado 8.03 cuando era estudiante de grado en el MIT, notó de inmediato que el sistema se comportaba como un oscilador masa-muelle amortiguado, con la suspensión de cables desempeñando el papel del muelle. Observó que las perturbaciones de la amplitud tardaban 4 segundos (el tiempo $e^{-1}$) en amortiguarse (es decir, la amplitud pasa de $A$ a $e^{-1}A$ en 4 segundos). De repente, la mitad inferior del semáforo se desprendió y cayó al pavimento. La nueva posición de equilibrio de la mitad restante quedó 0.1 metros más alta que antes.

1.  ¿Cuál es la frecuencia natural no amortiguada (en hercios) del semáforo tras la separación?
2.  Suponga que toda la disipación ocurre en el sistema de suspensión. ¿Cuál es el tiempo de decaimiento (el tiempo $e^{-1}$) de las oscilaciones de amplitud del semáforo tras la separación?
3.  Escriba una expresión analítica para el desplazamiento vertical, $y(t)$, del semáforo respecto a su nueva posición de equilibrio tras la separación. Suponga que el semáforo estaba en reposo ($\dot y = 0$) en la posición de equilibrio anterior en el instante de la separación, $t=0$. Dé valores numéricos, con unidades, para cualquier constante que aparezca en la expresión.

**Problema 2.4 (20 pts)**

Considere una masa $m$ que se mueve sobre un carril de aire horizontal. La masa está unida por ambos lados a dos muelles idénticos, cada uno con constante $k$ y longitud relajada $\ell_0$ (véase la figura 2). El extremo del primer muelle está fijo. El extremo del segundo muelle está conectado a un motor eléctrico que le hace realizar un movimiento armónico con amplitud $\Delta$ y frecuencia angular $\omega$. En $t=0$ los muelles están relajados, con $\ell = \ell_0$, y la masa está en reposo, $\dot x(0) = 0$. Defina el origen del sistema de coordenadas en la posición de la masa en $t=0$, de modo que $x(0)=0$.

En $t=0$ se enciende el motor, de forma que el extremo del muelle empieza a moverse según la ecuación

$$x_{\text{ext}} = \Delta \sin(\omega t) + \ell_0$$

Suponga que el movimiento de la masa está afectado por una pequeña fricción del aire dependiente de la velocidad, $-b\dot x$.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet2_ES/fig2.png)

Figura 2: masa $m$ sobre un carril de aire, unida a la izquierda a un muelle fijo de constantes $k, \ell_0$ y a la derecha a otro muelle idéntico cuyo extremo se mueve como $\Delta\sin(\omega t)$.

1.  Plantee cuidadosamente la ecuación de movimiento unidimensional para la masa $m$, incluyendo todas las fuerzas. Organice la ecuación de forma que se distingan claramente los términos del oscilador y los términos relacionados con la fuerza externa.
2.  Postule, sin resolver, la solución completa para el movimiento de la masa $x(t) = x_{\text{libre}}(t) + x_{\text{forzada}}(t)$. Indique qué constantes de la solución dependen solo de las propiedades del oscilador, cuáles de las propiedades de la fuerza externa y cuáles deben determinarse a partir de las condiciones iniciales.
3.  Encuentre la amplitud y la fase del movimiento estacionario de la masa. Esboce su dependencia con la frecuencia de la fuerza impulsora $\omega$ y con los parámetros dados.
4.  Encuentre la frecuencia $\omega_{\text{máx}}$ para la que la amplitud es máxima.
5.  Use las condiciones iniciales para encontrar la solución específica, incluyendo tanto el oscilador libre como la solución estacionaria, con la elección adecuada de todos los parámetros.

**Problema 2.5 (20 pts)**

Considere un sistema de tres muelles y dos masas como se muestra en la figura 3, donde las masas están obligadas a moverse solo en la dirección vertical. El sistema se prepara en un laboratorio en la Tierra, con la fuerza gravitatoria apuntando hacia abajo. Las constantes de los muelles son $K_A = 78$, $K_B = 60$ y $K_C = 24$, medidas en N/m. Las dos masas son $m_1 = 4$ y $m_2 = 12$, medidas en kg. Las longitudes naturales de los muelles A y B son iguales a la longitud natural de C.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet2_ES/fig3.png)

Figura 3: dos masas colgando verticalmente; el muelle $K_A$ conecta un soporte fijo con $m_2$, el muelle $K_C$ conecta $m_2$ con otro soporte fijo lateral, y el muelle $K_B$ conecta $m_2$ con $m_1$, colgando esta última en el extremo inferior.

1.  Defina el/los sistema(s) de coordenadas y escriba las ecuaciones de movimiento de las dos masas.
2.  Escriba la ecuación de movimiento en forma matricial. Muestre claramente la matriz $M^{-1}K$ tal como se define en el libro de texto.
3.  Encuentre los modos normales de oscilación y sus frecuencias angulares asociadas.
4.  Si la masa $m_1$ se desplaza 1 cm hacia arriba desde su posición de equilibrio y $m_2$ se mantiene en su posición de equilibrio original, y ambos bloques se sueltan desde el reposo en $t=0$, escriba las expresiones para el movimiento posterior de ambos bloques.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.


---

<!-- MIT8.03_ProblemSet3_ES.md -->

*Massachusetts Institute of Technology*

**Física 8.03SC — Otoño de 2016**

**Tarea 3**

## Problemas

**Problema 3.1 (20 pts)**

Consideramos aquí un péndulo doble, cada masa con un grado de libertad, como se muestra en la figura 1. La masa $M_1$ está unida a un origen fijo mediante una varilla rígida sin masa de longitud $L$. Su coordenada $x$ es $X_1$ y forma un ángulo $\theta_1$ respecto a la vertical (eje $y$). La masa $M_2$ está unida a la masa $M_1$ mediante una varilla rígida sin masa de longitud $L$. Su coordenada $x$ es $X_2$ y forma un ángulo $\theta_2$ respecto a la vertical.

Puede suponer que las «bisagras» en el origen y en la masa $M_1$ no tienen fricción. La gravedad apunta hacia abajo en la dirección $y$. Puede suponer que todas las oscilaciones son pequeñas, es decir, que $\theta_1$ y $\theta_2$ son pequeños y los términos de orden $O(\theta^2)$ son despreciables.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet3_ES/fig1.png)

Figura 1: péndulo doble; $M_1$ cuelga de un punto fijo mediante una varilla de longitud $L$ formando un ángulo $\theta_1$ con la vertical, y $M_2$ cuelga de $M_1$ mediante otra varilla idéntica formando un ángulo $\theta_2$ con la vertical.

1.  Escriba las ecuaciones de movimiento de las dos masas oscilantes.
2.  Determine las dos frecuencias de modo normal de oscilación en el límite de pequeña amplitud, en función de $\omega_0$ y $\alpha$, donde $\omega_0^2 = g/L$ y $\alpha = M_2/M_1$. (No es necesario resolver las razones de amplitud correspondientes.)
3.  ¿Cuáles son las dos frecuencias de modo normal si $\alpha \to \infty$? ¿Tienen sentido sus resultados?
4.  ¿Cuáles son las dos frecuencias de modo normal si $\alpha \to 0$? ¿Tienen sentido sus resultados?

**Problema 3.2 (20 pts)**

Considere dos circuitos LC idénticos, como se muestra en la figura 2. Las dos bobinas se acercan de modo que su inductancia mutua $M$ produce un acoplamiento entre las corrientes que circulan por los dos circuitos.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet3_ES/fig2.png)

Figura 2: dos circuitos LC idénticos, cada uno con un condensador $C$ y una bobina $L$; las dos bobinas están próximas y acopladas mediante la inductancia mutua $M$.

1.  Encuentre las frecuencias de los modos normales en función de los parámetros dados.
2.  ¿Qué patrones de corriente corresponden a estos modos normales? ¿Podría usar argumentos de simetría para descubrir estos modos?

**Problema 3.3 (20 pts)**

Considere tres masas idénticas obligadas a moverse sobre un círculo sin fricción. Las masas están conectadas mediante muelles idénticos, cada uno con constante $k$ (véase la figura 3). El círculo es grande, de modo que puede ignorar cualquier efecto relacionado con su curvatura. El círculo es horizontal, de modo que se puede ignorar la gravedad.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet3_ES/fig3.png)

Figura 3: tres masas idénticas $m$ dispuestas sobre un círculo, conectadas entre sí por tres muelles idénticos de constante $k$.

1.  Encuentre las ecuaciones de movimiento de las tres masas en función de los pequeños desplazamientos respecto a la posición de equilibrio de cada una.
2.  Determine las frecuencias y las amplitudes relativas de cada uno de los modos normales. Haga un esquema simple del movimiento de las masas para cada modo normal. ¿Cuántas frecuencias distintas hay en este sistema?
3.  Debido a que las masas están conectadas en círculo, algunos de los resultados del cálculo de modos normales no corresponden a un movimiento oscilatorio. Explique por qué.

**Problema 3.4 (20 pts)**

Considere dos masas idénticas $m$ conectadas entre sí por un muelle y unidas mediante otro muelle a un soporte móvil (véase la figura 4). El soporte oscila verticalmente y su posición viene dada por $h(t) = A\cos(\omega t)$. La constante de Hooke de los dos muelles idénticos es $k$. Ignore los efectos de amortiguamiento.

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet3_ES/fig4.png)

Figura 4: soporte oscilante $h(t)$ conectado mediante un muelle $k$ a una masa $m$ con posición $y_1(t)$, y esta a su vez conectada mediante otro muelle $k$ a una segunda masa $m$ con posición $y_2(t)$.

1.  Encuentre las ecuaciones diferenciales acopladas que gobiernan los desplazamientos respecto al equilibrio de las masas, $y_1(t)$ e $y_2(t)$. Exprese sus resultados en términos de $\omega_0^2 = k/m$. Note que el efecto de la gravedad produce un desplazamiento de la posición de equilibrio, pero no afecta al movimiento armónico.
2.  Encuentre la respuesta estacionaria de las posiciones de las dos masas, $y_1(t)$ e $y_2(t)$. Haga un esquema cuidadoso de la amplitud en función de la frecuencia impulsora $\omega$ para cada una de las masas.
3.  Examinando los resultados del apartado b, dé las frecuencias y las razones de amplitud para los modos normales del sistema no forzado.

**Problema 3.5 (20 pts)**

Dos cuentas idénticas, cada una de masa $m$, están igualmente espaciadas a lo largo de una cuerda sin masa de longitud $3a$ (véase la figura 5). Considere que el sistema está sobre una superficie horizontal sin fricción. Inicialmente ambos extremos de la cuerda están fijos ($\Delta = 0$). Suponga que la cuerda está bajo tensión $T$ en todo momento. Las cuentas pueden realizar pequeñas oscilaciones perpendiculares a la cuerda (los desplazamientos están exagerados en la figura).

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet3_ES/fig5.png)

Figura 5: cuerda de longitud total $3a$ con dos cuentas de masa $m$ en posiciones $y_1(t)$ e $y_2(t)$, separadas por tramos de longitud $a$; el extremo derecho se mueve como $Y(t) = \Delta\cos(\omega_d t)$.

1.  Encuentre las ecuaciones de movimiento de las dos cuentas en función del desplazamiento respecto al equilibrio, $y_1(t)$, $y_2(t)$.
2.  Encuentre y esquematice el movimiento de los modos normales y calcule las frecuencias de modo normal del sistema.

Suponga ahora que el punto de anclaje del extremo derecho realiza una oscilación armónica $y(t) = \Delta \cos(\omega_d t)$.

1.  Encuentre la amplitud estacionaria del movimiento de las dos masas en función de la frecuencia impulsora $\omega_d$ y de la amplitud $\Delta$.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.


---

<!-- MIT8.03_ProblemSet4_ES.md -->

*Massachusetts Institute of Technology*

**Física 8.03SC — Otoño de 2016**

**Tarea 4**

## Problemas

**Problema 4.1 (25 pts)**

En la cuerda con cuentas de la figura 1, el intervalo entre cuentas vecinas es $a$, y la distancia entre las cuentas de los extremos y la pared es $a/2$. Todas las cuentas tienen masa $m$ y están obligadas a moverse solo verticalmente en el plano del papel. Las cuerdas no tienen masa y tienen tensión constante $T$.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet4_ES/fig1.png)

Figura 1: cuentas numeradas de 1 a N sobre una cuerda, separadas una distancia $a$ entre sí y a $a/2$ de las paredes en ambos extremos.

1.  Demuestre que la física de la pared izquierda puede incorporarse pasando a un sistema infinito y exigiendo la condición de contorno $A_1 = -A_0$.
2.  Encuentre la condición de contorno análoga para la pared derecha.
3.  Encuentre los modos normales y las frecuencias correspondientes para el sistema finito.

**Problema 4.2 (25 pts)**

Una física trataba de entender un sistema con dos péndulos de torsión acoplados. Primero, intentó escribir las ecuaciones de movimiento de los péndulos en términos de $\theta_1$ y $\theta_2$, los ángulos respecto a las posiciones de equilibrio de los péndulos. Encontró que la matriz de interacción $M^{-1}K$ conmuta con la matriz de simetría de reflexión $2\times 2$

$$S = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$$

(es decir, satisface $[S, M^{-1}K] = 0$).

1.  ¿Cuántos modos normales tiene este sistema?
2.  ¿Cuál será la razón de amplitudes ($A_1/A_2$, donde $A_1$ y $A_2$ son las componentes del autovector) de los péndulos de torsión en cada modo normal?

**Problema 4.3 (25 pts)**

Considere una cuerda uniforme y delgada de longitud $L$ y densidad de masa $\mu$. La cuerda está unida en ambos extremos a varillas verticales sin fricción mediante anillos sin masa, como se muestra en la figura 2. La tensión en la cuerda es $T$.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet4_ES/fig2.png)

Figura 2: cuerda uniforme de longitud $L$ con sus dos extremos unidos, mediante anillos sin masa, a sendas varillas verticales sin fricción.

1.  Encuentre los modos normales y sus frecuencias para pequeñas oscilaciones transversales.
2.  Esquematice las formas de los tres primeros modos normales.
3.  Haga una gráfica de la frecuencia angular $\omega$ en función del número de onda angular $k$.

**Problema 4.4 (25 pts)**

Una cuerda de densidad de masa $\mu$, sometida a tensión $T$, se deforma como se muestra en la figura 3 (la amplitud $A$ es muy pequeña; la deformación mostrada en la figura está muy exagerada). La cuerda se suelta en $t=0$ con velocidad inicial nula ($\partial y(x,t)/\partial t = 0$ en $t=0$ para todo $x$).

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet4_ES/fig3.png)

Figura 3: perfil triangular simétrico de la cuerda entre $x=-L$ y $x=L$, con amplitud máxima $A$ en $x=0$ y amplitud $-A$ en los extremos, formando una forma de “M” invertida — un triángulo que sube desde $-A$ en $x=-L$ hasta $A$ en $x=0$ y vuelve a bajar hasta $-A$ en $x=L$.

1.  ¿Cuántos modos normales tiene este sistema?
2.  Encuentre expresiones para los coeficientes de Fourier $A_m$ del desarrollo en modos normales de la forma inicial de la cuerda, y úselos para escribir una serie completa dependiente del tiempo que describa el movimiento de la cuerda para $t>0$: $y(x,t)$.
3.  Haga un esquema de las amplitudes $A_m$ de los modos en función del número de modo $m$. Asegúrese de indicar las amplitudes de todos los modos normales posibles de la cuerda.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.


---

<!-- MIT8.03_ProblemSet5_ES.md -->

*Massachusetts Institute of Technology*

**Física 8.03SC — Otoño de 2016**

**Tarea 5**

## Problemas

**Problema 5.1 (20 pts)**

En un laboratorio, un estudiante de posgrado estudiaba una cuerda de longitud $L$, fija en ambos extremos.

1.  Encuentre la energía total de una vibración de la cuerda oscilando en su $n$-ésimo modo normal con amplitud $A$. La tensión en la cuerda es $T$ y su masa total es $M$. (Pista: considere la energía cinética integrada en el instante en que la cuerda está recta, de modo que la energía potencial debida a la vibración es cero.)
2.  Calcule la energía total de vibración de la misma cuerda si vibra en la siguiente superposición de modos normales. Suponga que es la suma de las energías de los dos modos tomados por separado.

$$\psi(x,t) = A_1 \sin\!\left(\frac{\pi x}{L}\right)\cos(\omega_1 t) + A_3 \sin\!\left(\frac{3\pi x}{L}\right)\cos(\omega_3 t - \pi/4)$$

**Problema 5.2 (20 pts)**

Una cuerda de longitud $L$, tensión $T$ y masa por unidad de longitud $\rho_L$, fija en ambos extremos, se deforma como se muestra en la figura 1. La altura del pulso cuadrado es $h$. La cuerda está obligada a vibrar solo en la dirección vertical. En $t=0$, la cuerda se suelta cuidadosamente de modo que su velocidad inicial es 0.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet5_ES/fig1.png)

Figura 1: pulso cuadrado de altura $h$ en el centro de una cuerda de longitud $L$ fija en ambos extremos.

1.  ¿Cuál es la velocidad de una onda progresiva en esta cuerda?
2.  Dibuje a escala la forma de la cuerda en $t = \dfrac{L}{4}\sqrt{\rho_L/T}$.
3.  Dibuje a escala la forma de la cuerda en $t = L\sqrt{\rho_L/T}$.

**Problema 5.3 (20 pts)**

Considere una cuerda de densidad de masa $\rho$ bajo tensión $T$. Un pulso viaja por la cuerda, produciendo un desplazamiento vertical dado por:

$$y(x,t) = y_0\, e^{-\frac{1}{2}\left(\frac{x-vt}{\sigma}\right)^2}$$

La energía de la onda es la suma de la energía cinética de la cuerda en movimiento y la energía potencial de la deformación de la cuerda, integradas a lo largo de toda su longitud.

1.  Para el desplazamiento dado arriba, encuentre una expresión para la densidad de energía cinética de la cuerda en un instante $t$ y esboce el resultado en función de $x$.
2.  Encuentre una expresión para la densidad de energía potencial de la cuerda. Compárela con la densidad de energía cinética.
3.  Encuentre una expresión para la energía total del pulso en términos de $T$, $y_0$ y $\sigma$. Compruebe las unidades. Recuerde que la energía debe variar como el cuadrado de la amplitud. (Pista: puede necesitar la integral gaussiana $\int_{-\infty}^{\infty} x^2 e^{-ax^2}\,dx = \dfrac{1}{2a}\sqrt{\pi/a}$.)
4.  Encuentre una expresión para la potencia (en vatios) que atraviesa el punto $x=x_0$ en función del tiempo. Esboce el resultado.

**Problema 5.4 (20 pts)**

Considere una cuerda con densidad lineal $\rho_L$ dividida en dos tramos. Las dos mitades están unidas a un anillo sin masa que desliza verticalmente sin fricción por una varilla en $x=0$, como se muestra en la figura 2. Una de las dos mitades está estirada en la dirección $x$ negativa con tensión $T_L$, y la otra en la dirección $x$ positiva con tensión $T_R$. Note que la varilla vertical es necesaria para equilibrar las fuerzas horizontales sobre la cuerda sin masa que surgen de los dos tramos con tensiones distintas.

Suponga que hay una onda viajera de amplitud $A$ que llega desde la dirección $x$ negativa.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet5_ES/fig2.png)

Figura 2: cuerda dividida en $x=0$ mediante un anillo sin masa que desliza por una varilla vertical; el tramo izquierdo tiene tensión $T_L$ y el derecho tensión $T_R$.

1.  Suponiendo que la onda incidente tiene la forma funcional $\psi(x,t) = \alpha\cos(kx-\omega t)$, escriba la expresión general para el desplazamiento de la cuerda $\psi(x,t)$ a ambos lados del anillo.
2.  Escriba las expresiones para las condiciones de contorno en $x=0$. (Pista: como el anillo no tiene masa, la fuerza total sobre él es 0.)
3.  Encuentre los coeficientes de reflexión ($R$) y transmisión ($T$) para este sistema.
4.  Demuestre que la energía se conserva en la unión.
5.  ¿Cuáles son los coeficientes de reflexión y transmisión en los siguientes tres casos: $T_R = T_L$, $T_R \gg T_L$ y $T_R \ll T_L$? ¿Tiene sentido su resultado?

**Problema 5.5 (20 pts)**

Una cuerda de densidad de masa $\rho_L$ bajo tensión $T$ está unida mediante un anillo sin masa a un alambre cubierto de grasa viscosa. El anillo experimenta una fuerza de arrastre vertical $F_y = -b\,\partial y/\partial t$ cuando el extremo de la cuerda se mueve.

![Figura](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet5_ES/figs1.png)

Figura: cuerda de tensión $T$ unida a un anillo sin masa que desliza por un alambre vertical cubierto de grasa.

1.  Aplique la segunda ley de Newton al anillo para encontrar la condición de contorno en el extremo de la cuerda, como una relación entre las derivadas parciales de $y(x,t)$ en ese punto. (Pista: hay tres fuerzas actuando sobre el anillo: la tensión de la cuerda, la fuerza normal del alambre y la fuerza de arrastre vertical.)
2.  Demuestre que la condición de contorno se satisface con un pulso incidente $f(t-x/v)$ y un pulso reflejado $g(t+x/v)$. Encuentre $g$ en términos de $f$.
3.  Demuestre que su resultado tiene el comportamiento adecuado en los límites $b\to 0$ (deslizamiento libre) y $b\to\infty$ (cuerda fija).

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.


---

<!-- MIT8.03_ProblemSet6_ES.md -->

*Massachusetts Institute of Technology*

**Física 8.03SC — Otoño de 2016**

**Tarea 6**

## Problemas

**Problema 6.1 (25 pts)**

Considere ondas sonoras propagándose a lo largo del eje $x$ en un tubo de órgano, descritas por la ecuación de ondas para el desplazamiento longitudinal, $\psi$, de un elemento de volumen de aire,

$$\frac{\partial^2 \psi}{\partial t^2} = A\, \frac{\partial^2 \psi}{\partial x^2}$$

donde la constante $A = 90000\ \text{m}^2/\text{s}^2$. El tubo de órgano está cerrado en un extremo, $x=0$, y abierto en el otro, $x=L=1.5\ \text{m}$.

1.  Dibuje los tres primeros modos normales en el intervalo $0 \le x \le L$ (es decir, esboce $\psi$ en función de $x$ en el instante de máximo desplazamiento), y escriba las frecuencias de modo normal para cada uno. Este problema no requiere cálculos elaborados ni resolver la ecuación anterior; solo necesita comprensión física de cómo se determinan los modos normales y algo de aritmética muy sencilla.
2.  Para los tres primeros modos normales, esboce la presión en función de $x$ en su amplitud máxima.
3.  Si el tubo se cambia para que esté abierto por ambos extremos, ¿qué longitud debe tener para conservar la frecuencia del modo fundamental?

**Problema 6.2 (25 pts)**

Durante la clase discutimos la solución de onda de las ecuaciones de Maxwell, pero no terminamos la deducción de la ecuación de ondas para el campo magnético.

1.  Demuestre que $\vec\nabla \times (\vec\nabla \times \vec A) = \vec\nabla(\vec\nabla \cdot \vec A) - (\vec\nabla \cdot \vec\nabla)\vec A$, donde $\vec A$ es un vector.
2.  Demuestre que, en el vacío, $\nabla^2 \vec B = \mu_0 \epsilon_0 \dfrac{\partial^2 \vec B}{\partial t^2}$, usando las ecuaciones de Maxwell.

**Problema 6.3 (25 pts)**

El objetivo de este problema es demostrar que un pulso plano —un pulso que viaja en cierta dirección sin variación (en un instante dado) perpendicular a esa dirección— es solución de las ecuaciones de Maxwell. Elegiremos la dirección de propagación a lo largo del eje $x$:

$$\vec E(\vec r, t) = E_0\, \hat y\, f(x - ct)$$

donde $f(\xi)$ es una función arbitraria, suficientemente regular.

1.  Demuestre que este campo satisface la ecuación de ondas electromagnética.
2.  Demuestre que el campo satisface $\vec\nabla \cdot \vec E = 0$. ¿Qué otras direcciones del vector $\vec E$ son compatibles con esta ecuación de Maxwell (ley de Gauss)?
3.  Encuentre una expresión para el campo magnético asociado a este pulso.

**Problema 6.4 (25 pts)**

En un lugar muy alejado de la Tierra, dos ondas planas EM sinusoidales, ambas de frecuencia $\nu$ y amplitud de campo eléctrico $E_0$ a lo largo de $\hat y$, viajan en direcciones opuestas en este espacio vacío a lo largo de la dirección $\hat x$. En $t=0$, se observa que el campo eléctrico es 0 en $x=0$.

1.  Escriba el campo eléctrico de una onda viajera sinusoidal que se propaga en la dirección $x$ positiva. (Pista: véanse los apuntes de la clase 12, página 6, y el ejemplo discutido en clase. En general, el campo eléctrico de una onda EM sinusoidal progresiva puede escribirse como $\vec E(\vec r, t) = \text{Re}(\vec E_0\, e^{j(\vec k \cdot \vec r - \omega t)})$, donde $\vec r = x\hat x + y\hat y + z\hat z$ y $\hat k = \vec k/|\vec k|$ es la dirección de propagación.)
2.  Encuentre el campo total $\vec E(\vec r,t)$ de las dos ondas planas y el promedio temporal de $E^2(\vec r, t)$ (promediado en un periodo).
3.  Encuentre el campo $\vec B(\vec r, t)$ correspondiente de las dos ondas planas y el promedio temporal de $B^2(\vec r,t)$ (promediado en un periodo).
4.  Encuentre la densidad de energía $U(\vec r, t)$ y su promedio temporal (promediado en un periodo).
5.  Encuentre el vector de Poynting $\vec S(\vec r, t)$ y su promedio temporal (promediado en un periodo).

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.


---

<!-- MIT8.03_ProblemSet7_ES.md -->

*Massachusetts Institute of Technology*

**Física 8.03SC — Otoño de 2016**

**Tarea 7**

## Problemas

**Problema 7.1 (40 pts)**

En sus *Lectures on Physics*, Richard Feynman escribe: «las ondas de agua, que todo el mundo ve fácilmente y que se suelen usar como ejemplo de ondas en cursos elementales, son el peor ejemplo posible; tienen todas las complicaciones que las ondas pueden tener». Este problema explora la complicación principal: las propiedades dispersivas de las ondas de agua.

Considere ondas en la superficie del agua (también llamadas ondas de gravedad superficiales). Suponga que las deformaciones de la superficie están influidas por la gravedad $g$ (en la Tierra) y por la tensión superficial $T$ del agua (expresada en newtons por metro). Si la densidad del agua es $\rho$ y la profundidad no perturbada es $h$, puede demostrarse que la velocidad de fase de las ondas superficiales viene dada por

$$v_p^2(k) = \left(\frac{g}{k} + \frac{Tk}{\rho}\right)\tanh(kh)$$

donde $k = 2\pi/\lambda$ es el número de onda, $\tanh(kh)$ es la tangente hiperbólica, y se desprecia la viscosidad. Para el agua, $\rho = 1\ \text{g}\,\text{cm}^{-3}$.

1.  En términos de las cantidades dadas, ¿a qué longitud de onda aproximada $\lambda_{\text{crítica}}$ el efecto de la tensión superficial se vuelve comparable al de la gravedad? Para agua a 20 °C, la longitud de onda crítica es $\lambda_{\text{crítica}} = 2\ \text{cm}$. ¿Cuál es la tensión superficial $T$ del agua?
2.  Suponga que $\lambda \gg \lambda_{\text{crítica}}$, de modo que la tensión superficial es despreciable. ¿Cuáles son la velocidad de fase y la velocidad de grupo para ondas de agua en aguas poco profundas ($\lambda \gg h$)? ¿Son dispersivas las ondas en esta condición?
3.  Suponga que $\lambda \gg \lambda_{\text{crítica}}$, de modo que la tensión superficial es despreciable. ¿Cuáles son la velocidad de fase y la velocidad de grupo para ondas en aguas profundas ($\lambda \ll h$)? ¿Son dispersivas las ondas en esta condición?
4.  Suponga que el agua es profunda, $\lambda \ll h$, y que las longitudes de onda son tan cortas que $\lambda \ll \lambda_{\text{crítica}}$, de modo que domina la tensión superficial y la gravedad es despreciable. Estas ondas se llaman ondas capilares. ¿Cuáles son su velocidad de fase y de grupo? ¿Son dispersivas las ondas capilares?

**Problema 7.2 (30 pts)**

La figura 1 muestra la curva de dispersión de cierto medio. (No haga ninguna suposición sobre la forma matemática de esta curva.)

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet7_ES/fig1.png)

Figura 1: relación de dispersión $\omega$ frente a $k$ de un medio genérico, con una forma curva no especificada.

1.  ¿Para qué frecuencia(s) angular(es) $\omega$, aproximadamente, son iguales la velocidad de fase y la velocidad de grupo ($v_p$ y $v_g$)?
2.  ¿Qué frecuencia angular media elegiría para transmitir un pulso a la mayor velocidad posible? ¿Cuánto vale esa velocidad?
3.  ¿Cuál será la respuesta del medio si lo excita en $\omega = \omega_0 = 1\times10^4\ \text{s}^{-1}$? (Pista: para $\omega \to \omega_0$, ¿cuáles son los valores de $v_p$ y $v_g$?)

**Problema 7.3 (30 pts)**

Considere una cuerda infinita de densidad lineal $\rho_L$ bajo tensión $T$. Un pulso de forma gaussiana viaja por la cuerda, produciendo un desplazamiento vertical dado por:

$$y(x,t) = \exp\!\left[-\frac{1}{2}\left(\frac{x-vt}{\sigma}\right)^2\right]$$

1.  Encuentre la distribución de frecuencias $C(\omega)$ que contribuyen a este pulso calculando la «transformada inversa de Fourier» (ec. 10.37 de Georgi). Esta es una integral muy conocida; $C(\omega)$ es también una gaussiana de anchura $\sigma_\omega$, puede usar herramientas en línea para encontrarla. Asegúrese de que todas las constantes sean correctas.
2.  Calcule el producto de las anchuras de las dos gaussianas, $\sigma \cdot \sigma_\omega$.
3.  Esboce la forma del pulso $y(x,0)$ en $t=0$ para $\sigma=1$ y $\sigma=5$.
4.  Esboce la forma de $C(\omega)$ en $x=0$ para $\sigma=1$ y $\sigma=5$ (no para $\sigma_\omega=1$ y $\sigma_\omega=5$).
5.  Compare las formas obtenidas de $y(x,0)$ y $C(\omega)$ para distintos valores de $\sigma$. ¿Observa alguna tendencia interesante?

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.


---

<!-- MIT8.03_ProblemSet8_ES.md -->

*Massachusetts Institute of Technology*

**Física 8.03SC — Otoño de 2016**

**Tarea 8**

## Problemas

**Problema 8.1 (25 pts)**

Considere las oscilaciones transversales libres de la cuerda bidimensional con cuentas de la figura 1. El sistema está formado por 9 cuentas dispuestas en una rejilla 3×3. Todas las cuerdas horizontales tienen tensión $T_h$, todas las verticales tienen tensión $T_v$, y todos los círculos rellenos son cuentas de masa $m$. Los extremos de las cuerdas que no están unidos a una cuenta están fijos. El marco cuadrado está fijo en el plano $z=0$.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet8_ES/fig1.png)

Figura 1: rejilla 2D de 9 masas dispuestas en 3 filas ($j=1,2,3$) y 3 columnas ($k=1,2,3$), unidas por cuerdas horizontales de tensión $T_h$ y verticales de tensión $T_v$, dentro de un marco fijo cuadrado de lado $L$.

1.  Encuentre los modos normales y las frecuencias correspondientes.
2.  Suponga que $T_v = 1000\, T_h$. Dibuje nueve diagramas, uno por cada modo normal, en orden de frecuencia creciente, indicando qué cuentas se mueven hacia arriba (con un signo +), cuáles hacia abajo (con un signo −) y cuáles no se mueven (con un 0). Puede intercambiar + y − y seguir teniendo la respuesta correcta, cambiando el instante de referencia o multiplicando el vector de modo normal por −1. Por ejemplo, el modo de menor frecuencia se ve así:

<!-- -->

    + + +
    + + +
    + + +

mientras que el quinto modo en frecuencia se ve así:

    - 0 +
    0 0 0
    + 0 -

**Problema 8.2 (25 pts)**

Un rayo de luz viaja por el vacío ($n_1=1$) antes de llegar a una placa transparente con índice de refracción $n_2$, con un ángulo $\alpha = 60°$. Atraviesa esta placa y entra en un nuevo material con índice de refracción $n_3$ con un ángulo $\beta = 30°$. La configuración de este experimento óptico se muestra en la figura 2.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet8_ES/fig2.png)

Figura 2: rayo de luz que incide desde el vacío sobre una placa transparente de índice $n_2$ con ángulo $\alpha=60°$, y sale hacia un material de índice $n_3$ con ángulo $\beta=30°$.

1.  ¿Cuál es el posible rango de valores de $n_2$?
2.  ¿Cuál es el valor de $n_3$?

**Problema 8.3 (25 pts)**

La luz solar entra en las gotas de agua de las nubes oscuras de forma casi horizontal, produciendo un arcoíris en un ángulo $\alpha$, que ronda entre 40 y 42 grados, como se muestra en la figura 3.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet8_ES/fig3.png)

Figura 3: rayo de luz solar entrando casi horizontalmente en una gota de agua esférica, reflejándose internamente y saliendo con un ángulo $\alpha$ respecto a la dirección original.

1.  Encuentre $\alpha$ en función del ángulo de incidencia $\theta$ y de $n$, el índice de refracción del agua. Represente y encuentre el valor extremo (máximo) de $\alpha$ en función del ángulo de incidencia $\theta$, que varía entre 0 y 90 grados. (Use $n=1.33$ para hallar el $\alpha$ máximo y haga la gráfica con Mathematica o cualquier herramienta de representación que prefiera.)
2.  ¿Por qué aparece el arcoíris en el valor extremo de $\alpha$?
3.  ¿Qué color aparece en un ángulo mayor cuando se mira el arcoíris? (Pista: el índice de refracción de la luz roja es ligeramente menor que el de la azul.)
4.  ¿Cómo se explican los arcoíris dobles? ¿Qué color queda más alto en el cielo en el segundo arcoíris? Basta con una discusión cualitativa para este apartado.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.


---

<!-- MIT8.03_ProblemSet9_ES.md -->

*Massachusetts Institute of Technology*

**Física 8.03SC — Otoño de 2016**

**Tarea 9**

## Problemas

**Problema 9.1 (20 pts)**

La ionosfera puede verse como un medio dieléctrico con índice de refracción

$$n = \sqrt{1 - \frac{\omega_p^2}{\omega^2}}$$

donde $\omega$ es la frecuencia y $\omega_p$ es la frecuencia de plasma, que se supone constante.

1.  Haga una gráfica de la magnitud del vector de propagación $k$ en función de la frecuencia $\omega$ para una onda electromagnética que se propaga por la ionosfera.
2.  Calcule la velocidad de fase y la velocidad de grupo de una onda de radio que se propaga con frecuencia $\omega = \sqrt{2}\,\omega_p$.
3.  ¿Qué le ocurre a una perturbación electromagnética dentro de la ionosfera cuando $\omega < \omega_p$?

**Problema 9.2 (20 pts)**

Considere dos polarizadores y una lámina de cuarto de onda como se muestra en la figura 1.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet9_ES/fig1.png)

Figura 1: haz de luz atravesando, en orden, el polarizador A, el polarizador B y una lámina de cuarto de onda, cada uno con su eje “fácil” o “rápido/lento” orientado con un ángulo distinto.

Primero se insertan los dos polarizadores A y B en la trayectoria de un haz de luz, como se muestra en la figura 2. El haz incidente viaja a lo largo del eje $z$ y está polarizado linealmente en la dirección $y$. La intensidad inicial de la luz es $I_0$. En este problema se le pide determinar la intensidad de la luz relativa a $I_0$ a lo largo de la trayectoria del haz. Los polarizadores son perfectos: transmiten el 100 % de la luz polarizada a lo largo de su eje «fácil» y detienen toda la luz perpendicular a ese eje. Los ángulos de los ejes fáciles de los dos polarizadores ($\theta_A$, $\theta_B$) se miden respecto a la dirección $y$. Nota: la intensidad de la luz es proporcional al promedio temporal de $E^2$: $I \propto \langle E^2 \rangle_t$.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet9_ES/fig2.png)

Figura 2: haz de intensidad $I_0$ propagándose en $z$, atravesando el polarizador A en el punto a y el polarizador B en el punto b.

1.  Encuentre la intensidad $I_a$ del haz después de pasar por el polarizador A, en función de $I_0$ y $\theta_A$.
2.  Encuentre la intensidad $I_b$ del haz después de pasar por ambos polarizadores, en función de $I_0$, $\theta_A$ y $\theta_B$.

Ahora el polarizador A se sustituye por una lámina de cuarto de onda C (véase la figura 3). La lámina de cuarto de onda afecta solo a la fase de la luz transmitida. Tiene dos ejes perpendiculares, «lento» y «rápido». La fase de la luz polarizada a lo largo del eje «lento» se retrasa $\pi/2$ respecto a la fase de la luz polarizada a lo largo del eje «rápido». La lámina se coloca de modo que el ángulo del eje «rápido» respecto al eje $y$ es $\theta_C$.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet9_ES/fig3.png)

Figura 3: haz atravesando la lámina de cuarto de onda C en el punto c y luego el polarizador B en el punto b.

1.  Encuentre la intensidad $I_c$ del haz después de pasar por la lámina de cuarto de onda C, en función de los parámetros dados.
2.  La intensidad de la luz que pasa por el polarizador B se verá afectada, en general, por la presencia de la lámina de cuarto de onda. Suponga que el eje fácil del polarizador B está orientado a lo largo del eje $y$ ($\theta_B=0$). Encuentre la intensidad $I_b$ del haz después de pasar por el polarizador B, en función de $I_0$ y $\theta_C$.

**Problema 9.3 (20 pts)**

Una onda electromagnética plana y monocromática viaja en la dirección $+z$ dentro de un medio dieléctrico. La onda está polarizada linealmente, con el campo $\vec E$ formando 30° con el eje $x$. La frecuencia angular de la onda es $\omega$ y la constante dieléctrica del medio es $\kappa_e$.

1.  Escriba las expresiones para $E_x(z,t)$, $E_y(z,t)$, $B_x(z,t)$, $B_y(z,t)$, en términos de $\omega$, $c$, $\kappa_e$, $E_0$, donde $E_0$ es la amplitud del campo eléctrico.
2.  ¿Cuál es la tasa de flujo de energía por unidad de área y por unidad de tiempo que se transporta a través de una superficie perpendicular a la dirección de propagación?
3.  ¿Cuál es la ecuación de ondas para las ondas electromagnéticas que viajan dentro del medio?

**Problema 9.4 (20 pts)**

Un electrón realiza un movimiento en espiral en un campo magnético, como se muestra en la figura 4. Su velocidad no es relativista. La posición del electrón viene dada por:

$$\vec r(t) = \hat x\, \alpha\cos(\beta t) + \hat y\, \alpha\sin(\beta t) + \hat z\, \gamma t$$

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet9_ES/fig4.png)

Figura 4: electrón describiendo una trayectoria helicoidal a lo largo del eje $z$, con radio $\alpha$ y avance $\gamma t$.

1.  Dé la frecuencia $\nu$, el vector de onda $\vec k$ y el estado de polarización de la radiación observada por un radioastrónomo situado lejos, en las siguientes direcciones $(x,y,z)$ ($R \gg \alpha$):
    1.  $(0,0,R)$
    2.  $(R/\sqrt2,\,0,\,R/\sqrt2)$
    3.  $(R,0,0)$
2.  Dé la expresión completa de los vectores de campo eléctrico y magnético de las ondas observadas en el punto B sobre el eje $z$, con coordenadas $(x,y,z)=(0,0,R)$, donde $R \gg \alpha$.
3.  Dé una expresión para la energía total radiada por segundo por el electrón, en términos de las constantes dadas. (Pista: puede usar la fórmula de Larmor, potencia $P = \dfrac{q^2|a|^2}{6\pi\epsilon_0 c^3}$.)
4.  En una esfera de radio $R$ alrededor de la fuente, ¿cuál es la razón entre el valor máximo y el mínimo del vector de Poynting promediado en el tiempo?

**Problema 9.5 (20 pts)**

Un rayo de luz con componentes del campo eléctrico paralela ($E_\parallel$) y perpendicular ($E_\perp$) al plano de incidencia de una interfaz vidrio-aire se muestra en la figura 5.

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet9_ES/fig5.png)

Figura 5: rayo de luz incidiendo sobre una interfaz vidrio-aire, con las componentes paralela y perpendicular del campo eléctrico indicadas mediante flechas y puntos.

1.  Si el rayo incide sobre el vidrio con el ángulo de Brewster, muestre mediante esquemas (como se hace para el rayo incidente en la figura 5) las componentes de polarización de los rayos reflejado y refractado.
2.  Dé la ecuación que define el ángulo de Brewster $\theta_B$. (Pista: use la ley de Snell.)
3.  Explique, a partir de la aceleración de las cargas en el vidrio, la dirección de polarización de la luz reflejada. ¿Por qué la luz reflejada está polarizada paralelamente a la interfaz?

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.


---

<!-- MIT8.03_TextCh10_ES.md -->

# Capítulo 10: Señales y análisis de Fourier

Las ondas viajeras de frecuencia definida transportan energía, pero no información. Sencillamente están ahí, siempre han estado y siempre estarán. Para enviar información hay que enviar una señal no armónica.

## Vídeos de esta clase (YouTube)

- [Clase 14: Transformada de Fourier, radio AM](https://www.youtube.com/watch?v=VGAlyJ7e0IQ)
- [Clase 15: Principio de incertidumbre, ondas en 2D](https://www.youtube.com/watch?v=In0E5_JrPpo)

## Resumen previo

En este capítulo veremos cómo funciona esto en el contexto de un problema de oscilación forzada. Por el camino encontraremos una sutileza en la noción de la velocidad con la que se mueve una onda viajera: la velocidad de fase puede no coincidir con la velocidad de propagación de la señal.

1.  Empezamos estudiando la propagación de un pulso transversal en una cuerda tensada. Resolvemos el problema de dos maneras: con un truco que funciona en este caso especial, y con la técnica más potente de la transformación de Fourier. Introducimos el concepto de «velocidad de grupo», la velocidad a la que realmente pueden enviarse señales en un sistema real.

2.  Discutimos, primero con un ejemplo y después en general, el contrapunto entre una función y su transformada de Fourier. Establecemos la conexión con los conceptos físicos de ancho de banda y fidelidad en la transmisión de señales, y con la relación de incertidumbre de Heisenberg en mecánica cuántica.

3.  Desarrollamos con cierto detalle un ejemplo de dispersión de un paquete de ondas.

4.  Discutimos con más detalle la relación de dispersión de las ondas electromagnéticas y exploramos la cuestión de si la luz viaja realmente a la velocidad de la luz.

## 10.1 Señales en oscilación forzada

### 10.1.1 Un pulso en una cuerda

Empezamos con el siguiente problema ilustrativo: las oscilaciones transversales de una cuerda semiinfinita tensada de $x = 0$ a $\infty$, forzada en $x = 0$ con una señal transversal arbitraria $f(t)$, y con la condición de contorno en el infinito de que no hay ondas viajeras entrantes. Este sistema sencillo se muestra en la figura 10.1.

![Figura 10.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.1.png)

Figura 10.1: una cuerda semiinfinita.

Hay una manera elegante de obtener la respuesta a este problema, que solo funciona para un sistema con la relación de dispersión sencilla

$$\omega^2 = v^2 k^2.\qquad\text{(10.1)}$$

El truco consiste en notar que la relación de dispersión (10.1) implica que el sistema satisface la ecuación de ondas, (6.4), o sea

$$\frac{\partial^2}{\partial t^2}\psi(x, t) = v^2\frac{\partial^2}{\partial x^2}\psi(x, t).\qquad\text{(10.2)}$$

Es un hecho matemático (discutiremos su física más abajo) que la solución general de la ecuación de ondas unidimensional, (10.2), es una suma de ondas que se mueven hacia la derecha y hacia la izquierda con formas arbitrarias,

$$\psi(x, t) = g(x - vt) + h(x + vt),\qquad\text{(10.3)}$$

donde $g$ y $h$ son funciones arbitrarias. Puede comprobar, usando la regla de la cadena, que (10.3) satisface (10.2):

$$\frac{\partial^2}{\partial t^2}\left(g(x - vt) + h(x + vt)\right) = v^2\left(g''(x - vt) + h''(x + vt)\right) = v^2\frac{\partial^2}{\partial x^2}\left(g(x - vt) + h(x + vt)\right).$$

Dado este hecho matemático, podemos hallar las funciones $g$ y $h$ que resuelven nuestro problema concreto imponiendo las condiciones de contorno. La condición de contorno en el infinito implica

$$h = 0,$$

porque la función $h$ describe una onda que se mueve en la dirección $-x$. La condición de contorno en $x = 0$ implica

$$g(-vt) = f(t),$$

lo que da

$$\psi(x, t) = f(t - x/v).\qquad\text{(10.7)}$$

Esto describe la señal $f(t)$ propagándose por la cuerda a la velocidad de fase $v$ sin cambio de forma.

Para la función sencilla

$$f(t) = \begin{cases} 1 - |t| & \text{para } |t| \leq 1 \\ 0 & \text{para } |t| > 1 \end{cases}\qquad\text{(10.8)}$$

la forma de la cuerda en una sucesión de instantes se muestra en la figura 10.2 y está animada en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-10-1" rel="noopener" target="_blank" title="Animación original de Howard Georgi">10-1</a>.

![Figura 10.2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.2.png)

Figura 10.2: un pulso triangular propagándose por una cuerda tensada.

### 10.1.2 Integrales de Fourier

Pensemos en este problema de una manera más física. Por el camino entenderemos la física de la solución general, (10.3). Puede parecer extraño decir esto en una sección titulada «Integrales de Fourier». Sin embargo, veremos que las matemáticas de las integrales de Fourier tienen una interpretación física directa y sencilla.

La idea es usar la linealidad de forma astuta para resolver este problema. Podemos descomponer $f(t)$ en sus frecuencias angulares componentes. Ya sabemos resolver el problema de la oscilación forzada para cada frecuencia angular. Después podemos tomar las soluciones individuales y volver a sumarlas para reconstruir la solución del problema completo. La ventaja de este procedimiento es que funciona para cualquier relación de dispersión, no solo para (10.1).

Como puede haber una distribución continua de frecuencias en una señal arbitraria, no podemos escribir $f(t)$ simplemente como una suma sobre componentes: necesitamos una integral de Fourier,

$$f(t) = \int_{-\infty}^{\infty} d\omega\, C(\omega)\,e^{-i\omega t}.\qquad\text{(10.9)}$$

La física de (10.9) es simplemente la linealidad y la invariancia bajo traslación temporal. Sabemos que podemos elegir los modos normales del sistema libre con una dependencia temporal exponencial irreducible, gracias a la invariancia bajo traslación temporal. Puesto que los modos normales describen todos los movimientos posibles del sistema, sabemos que, tomando una combinación lineal adecuada de modos normales, podemos encontrar una solución en la que el movimiento del extremo del sistema esté descrito por la función $f(t)$. La única sutileza de (10.9) es que hemos supuesto que todos los valores de $\omega$ que aparecen en la integral son reales. Esto es apropiado porque una parte imaginaria no nula de $\omega$ en $e^{-i\omega t}$ describe una función que va exponencialmente a infinito cuando $t \to \pm\infty$. Físicamente, esas cosas nunca nos interesan. De hecho, lo que realmente nos interesa son funciones que van a cero cuando $t \to \pm\infty$, y esas quedan bien descritas por la integral sobre $\omega$ real, (10.9).

Nótese que si $f(t)$ es real en (10.9), entonces

$$f(t)^* = \int d\omega\, C(\omega)^*\,e^{i\omega t} = \int d\omega\, C(-\omega)^*\,e^{-i\omega t},$$

y por tanto

$$C(-\omega)^* = C(\omega).\qquad\text{(10.12)}$$

En realidad es más fácil trabajar con la integral de Fourier compleja, (10.9), con la dependencia temporal exponencial compleja irreducible, que con desarrollos reales en términos de $\cos\omega t$ y $\sin\omega t$. Pero también puede encontrar las formas reales en otros libros. Siempre se puede traducir de (10.9) usando la identidad de Euler

$$e^{i\theta} = \cos\theta + i\sin\theta.$$

Para cada valor de $\omega$ podemos escribir la solución del problema de oscilación forzada incorporando la condición de contorno en $\infty$. Cada componente de frecuencia de la fuerza produce una onda que viaja en la dirección $+x$:

$$e^{-i\omega t} \to e^{-i\omega t + ikx}.\qquad\text{(10.13)}$$

Entonces podemos usar la linealidad para construir la solución sumando las ondas viajeras individuales de (10.13) con los coeficientes $C(\omega)$ de (10.9). Así,

$$\psi(x, t) = \int d\omega\, C(\omega)\,e^{-i\omega t + ikx},\qquad\text{(10.14)}$$

donde $\omega$ y $k$ están relacionados por la relación de dispersión.

La ecuación (10.14) es cierta con bastante generalidad para cualquier sistema unidimensional y cualquier relación de dispersión, pero el resultado es particularmente sencillo para un sistema no dispersivo, como la cuerda continua con una relación de dispersión de la forma (10.1). Podemos usar (10.1) en (10.14) sustituyendo

$$k = \omega/v.\qquad\text{(10.15)}$$

Nótese que, mientras que $k^2$ queda determinado por la relación de dispersión, el signo de $k$, para un $\omega$ dado, lo determina la condición de contorno en el infinito. $k$ y $\omega$ deben tener el mismo signo, como en (10.15), para describir una onda que viaja en la dirección $+x$. Poniendo (10.15) en (10.14) se obtiene

$$\psi(x, t) = \int d\omega\, C(\omega)\,e^{-i\omega t + i\omega x/v} = \int d\omega\, C(\omega)\,e^{-i\omega(t - x/v)}.$$

Comparando esto con (10.9) se obtiene (10.7).

Intentemos entender en palabras lo que está ocurriendo. La integral de Fourier, (10.9), expresa la señal como una combinación lineal de ondas viajeras armónicas. La relación (10.15), que se sigue de la relación de dispersión (10.1) y de la condición de contorno en $\infty$, implica que cada una de las infinitas ondas viajeras armónicas se mueve con la misma velocidad de fase. Por tanto, las ondas se mantienen exactamente en la misma relación unas con otras conforme se mueven, y la señal nunca se distorsiona: simplemente se desplaza con las ondas.

La señal no armónica se llama «paquete de ondas». Como hemos visto, puede descomponerse en ondas armónicas por medio de la integral de Fourier, (10.9).

## 10.2 Medios dispersivos y velocidad de grupo

Para cualquier otra relación de dispersión, la señal cambia de forma al propagarse, porque las distintas componentes armónicas viajan a velocidades diferentes. Con el tiempo, las distintas partes de la señal se desfasan y la señal se dispersa. Por eso a un medio así se le llama «dispersivo». Este es el origen del nombre «relación de dispersión».

### 10.2.1 Velocidad de grupo

Si es astuto, puede enviar señales en un medio dispersivo. El truco consiste en enviar la señal no directamente como la función $f(t)$, sino como una modulación de una señal armónica, de la forma

$$f(t) = f_s(t)\cos\omega_0 t,\qquad\text{(10.17)}$$

donde $f_s(t)$ es la señal. Muy a menudo querrá hacer esto de todos modos, porque puede que las frecuencias importantes de su señal no coincidan con las frecuencias de las ondas con las que quiere enviarla. Un ejemplo es la transmisión de radio AM, en la que la señal procede del sonido, con una frecuencia típica de unos cientos de ciclos por segundo (Hz), pero se transporta como una modulación de la amplitud de una onda de radio electromagnética, con una frecuencia de unos millones de ciclos por segundo.[1]

Puede hacerse una idea de lo que va a ocurrir en este caso considerando la suma de dos ondas viajeras con frecuencias y números de onda distintos,

$$\cos(k_+x - \omega_+t) + \cos(k_-x - \omega_-t)\qquad\text{(10.18)}$$

donde

$$k_\pm = k_0 \pm k_s, \qquad \omega_\pm = \omega_0 \pm \omega_s,\qquad\text{(10.19)}$$

para

$$k_s \ll k_0, \qquad \omega_s \ll \omega_0.\qquad\text{(10.20)}$$

La suma puede escribirse como un producto de cosenos:

$$2\cos(k_sx - \omega_st)\cdot\cos(k_0x - \omega_0t).\qquad\text{(10.21)}$$

Debido a (10.20), el primer factor varía lentamente en $x$ y $t$ comparado con el segundo. El resultado puede pensarse como una onda armónica de frecuencia $\omega_0$ con una amplitud que varía lentamente, proporcional al primer factor. La dependencia espacial de (10.21) se muestra en la figura 10.3.

![Figura 10.3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.3.png)

Figura 10.3: la función (10.21) para $t = 0$ y $k_0/k_s = 10$.

Debe pensar en el primer factor de (10.21) como la señal. El segundo factor se llama «onda portadora». Entonces (10.21) describe una señal que se mueve con velocidad

$$v_s = \frac{\omega_s}{k_s}\qquad\text{(10.22)}$$

mientras que las ondas más pequeñas asociadas al segundo factor se mueven con velocidad

$$v_0 = \frac{\omega_0}{k_0}.\qquad\text{(10.23)}$$

Estas dos velocidades no serán, en general, la misma. Si se satisface (10.20), entonces (como mostraremos con más detalle abajo) $v_0$ será aproximadamente la velocidad de fase. En el límite en que $k_+ - k_- = 2k_s$ se hace muy pequeño, (10.22) se convierte en una derivada:

$$v_s = \left.\frac{\partial\omega}{\partial k}\right|_{k = k_0}.\qquad\text{(10.24)}$$

A esto se le llama «velocidad de grupo». Mide la velocidad a la que puede enviarse realmente la señal.

La dependencia temporal de (10.21) está animada en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-10-2" rel="noopener" target="_blank" title="Animación original de Howard Georgi">10-2</a>. Fíjese en cómo las ondas portadoras se desplazan a través de la señal. En esta animación, la velocidad de grupo es menor que la velocidad de fase, así que las ondas portadoras aparecen en la parte trasera de cada pulso de la señal y avanzan hacia el frente.

Veamos cómo funciona esto en general para señales $f(t)$ interesantes. Supongamos que, para cierto rango de frecuencias cercanas a una frecuencia $\omega_0$, la relación de dispersión varía lentamente. Entonces podemos tomarla como aproximadamente lineal desarrollando $\omega(k)$ en serie de Taylor alrededor de $k_0$ y quedándonos solo con los dos primeros términos. Es decir,

$$\omega = \omega(k) = \omega_0 + (k - k_0)\left.\frac{\partial\omega}{\partial k}\right|_{k = k_0}, \qquad \omega_0 \equiv \omega(k_0),\qquad\text{(10.25)}$$

y los términos de orden superior son despreciables para un rango de frecuencias

$$\omega_0 - \Delta\omega < \omega < \omega_0 + \Delta\omega,\qquad\text{(10.26)}$$

donde $\Delta\omega$ es una constante que depende de $\omega_0$ y de los detalles de los términos de orden superior. Entonces puede enviar una señal de la forma

$$f(t)\cdot e^{-i\omega_0 t}\qquad\text{(10.28)}$$

(una forma compleja de (10.17)), donde $f(t)$ satisface (10.9) con

$$C(\omega) \approx 0 \quad \text{para } |\omega - \omega_0| > \Delta\omega.$$

Esto describe una señal que tiene una onda portadora de frecuencia $\omega_0$, modulada por la parte interesante de la señal, $f(t)$, que actúa como una amplitud variable en el tiempo para la portadora $e^{-i\omega_0 t}$. La estrategia de enviar una señal como una amplitud variable sobre una onda portadora se llama modulación de amplitud.

Normalmente, los términos de orden superior de (10.25) solo son despreciables si $\Delta\omega \ll \omega_0$. Si los despreciamos, podemos escribir (10.25) como

$$\omega = vk + a, \qquad k = \omega/v + b,\qquad\text{(10.29)}$$

donde $a$ y $b$ son constantes que podemos determinar a partir de (10.25),

$$a = \omega_0 - vk_0, \qquad b = k_0 - \omega_0/v,\qquad\text{(10.30)}$$

y $v$ es la velocidad de grupo

$$v = \left.\frac{\partial\omega}{\partial k}\right|_{k = k_0}.\qquad\text{(10.32)}$$

Para la señal (10.28),

$$f(t)\,e^{-i\omega_0 t} = \int d\omega\, C(\omega)\,e^{-i(\omega + \omega_0)t} = \int d\omega\, C(\omega - \omega_0)\,e^{-i\omega t}.$$

Así, (10.14) queda

$$\psi(x, t) = \int d\omega\, C(\omega - \omega_0)\,e^{-i\omega t}e^{ikx},$$

pero entonces (10.29) da

$$\begin{aligned}
\psi(x, t) &= \int d\omega\, C(\omega - \omega_0)\,e^{-i\omega t + i(\omega/v + b)x} \\
&= \int d\omega\, C(\omega - \omega_0)\,e^{-i\omega(t - x/v) + ibx} \\
&= \int d\omega\, C(\omega)\,e^{-i(\omega + \omega_0)(t - x/v) + ibx} \\
&= f(t - x/v)\,e^{-i\omega_0(t - x/v) + ibx}.
\end{aligned}\qquad\text{(10.35)}$$

La modulación $f(t)$ viaja sin cambio de forma a la velocidad de grupo $v$ dada por (10.32), mientras podamos ignorar el término de orden superior de la relación de dispersión. La velocidad de fase

$$v_\phi = \frac{\omega}{k}\qquad\text{(10.36)}$$

no tiene nada que ver con la transmisión de información, pero obsérvese que, debido al $e^{ibx}$ adicional de (10.35), la onda portadora viaja a la velocidad de fase.

Puede ver la diferencia entre velocidad de fase y velocidad de grupo en su piscina o su bañera creando un paquete de ondas formado por varias ondas más cortas.

## 10.3 Ancho de banda, fidelidad e incertidumbre

La relación (10.9) puede invertirse para dar $C(\omega)$ en términos de $f(t)$ como sigue:

$$C(\omega) = \frac{1}{2\pi}\int_{-\infty}^{\infty} dt\, f(t)\,e^{i\omega t}.\qquad\text{(10.37)}$$

Esta es la «transformada de Fourier inversa». Es muy importante, porque nos permite ir y venir entre la señal y la distribución de frecuencias que contiene. Obtendremos este resultado de dos maneras: primero, con un argumento elegante que volveremos a usar y explicaremos con más detalle en el capítulo 13; después, volviendo a la serie de Fourier discutida en el capítulo 6 para ondas en una cuerda finita, y tomando el límite en que la longitud de la cuerda tiende a infinito.

El argumento elegante es este. Es muy razonable que la integral de (10.37) sea proporcional a $C(\omega)$, porque si insertamos (10.9) y reordenamos el orden de integración obtenemos

$$\int d\omega'\, C(\omega')\int dt\, e^{i(\omega - \omega')t}.$$

La integral en $t$ promedia a cero salvo que $\omega = \omega'$. Así, la integral en $\omega'$ es simplemente proporcional a $C(\omega)$ multiplicada por un factor constante. El factor $1/2\pi$ puede obtenerse haciendo algunas integrales explícitamente. Por ejemplo, si

$$f(t) = e^{-\Gamma|t|},\qquad\text{(10.39)}$$

para $\Gamma > 0$, entonces, como mostraremos explícitamente en (10.49)-(10.56), (10.37) da

$$2\pi C(\omega) = \frac{2\Gamma}{\Gamma^2 + \omega^2},\qquad\text{(10.40)}$$

que a su vez puede llevarse de vuelta a (10.9) para dar (10.39). Para $t = 0$, la integral puede hacerse mediante la sustitución trigonométrica $\omega \to \Gamma\tan\theta$:

$$1 = f(0) = \int d\omega\, C(\omega)\,e^{-i\omega\cdot 0} = \frac{1}{\pi}\int_{-\infty}^{\infty} d\omega\,\frac{\Gamma}{\Gamma^2 + \omega^2} = \frac{1}{\pi}\int_{-\pi/2}^{\pi/2} d\theta = 1.\qquad\text{(10.41)}$$

Para obtener la transformada de Fourier inversa, (10.37), como límite de una serie de Fourier, conviene usar una condición de contorno ligeramente distinta de las que discutimos en el capítulo 6 (extremos fijos y extremos libres). En su lugar, consideremos una cuerda tensada de $x = -\pi\ell$ a $x = \pi\ell$, en la que suponemos que el desplazamiento de la cuerda respecto del equilibrio en $x = \pi\ell$ es el mismo que el desplazamiento en $x = -\pi\ell$:[2]

$$\psi(-\pi\ell, t) = \psi(\pi\ell, t).\qquad\text{(10.42)}$$

El requisito (10.42) se llama «condiciones de contorno periódicas», porque implica que la función $\psi$ que describe el desplazamiento de la cuerda es periódica en $x$ con periodo $2\pi\ell$. Los modos normales del sistema infinito que satisfacen (10.42) son

$$e^{inx/\ell},\qquad\text{(10.43)}$$

para $n$ entero, porque cambiar $x$ en $2\pi\ell$ en (10.43) solo cambia la fase de la exponencial en $2\pi$. Así, si $\psi(x)$ es una función arbitraria que satisface $\psi(-\pi\ell) = \psi(\pi\ell)$, deberíamos poder desarrollarla en los modos normales de (10.43),

$$\psi(x) = \sum_{n = -\infty}^{\infty} c_n\,e^{-inx/\ell}.\qquad\text{(10.44)}$$

Análogamente, para una función $f(t)$ que satisfaga $f(-\pi T) = f(\pi T)$ para algún tiempo $T$ grande, esperamos poder desarrollarla como sigue:

$$f(t) = \sum_{n = -\infty}^{\infty} c_n\,e^{-int/T},\qquad\text{(10.45)}$$

donde hemos cambiado el signo del exponente para concordar con (10.9). Mostraremos que, cuando $T \to \infty$, esto se vuelve equivalente a (10.9).

La ecuación (10.44) es el análogo de (6.8) para la condición de contorno (10.42). La suma va de $-\infty$ a $\infty$ en vez de de $0$ a $\infty$ porque los modos de (10.43) son distintos para $n$ y $-n$. Para esta serie de Fourier, la inversa es

$$c_m = \frac{1}{2\pi T}\int_{-\pi T}^{\pi T} dt\, e^{imt/T} f(t),\qquad\text{(10.46)}$$

donde hemos usado la identidad

$$\frac{1}{2\pi T}\int_{-\pi T}^{\pi T} dt\, e^{imt/T}e^{-int/T} = \begin{cases} 1 & \text{para } m = n, \\ 0 & \text{para } m \neq n. \end{cases}\qquad\text{(10.47)}$$

Supongamos ahora que $f(t)$ tiende a 0 para $|t|$ grande (nótese que esto es coherente con la condición de contorno periódica (10.42)) lo bastante deprisa como para que la integral de (10.46) esté bien definida cuando $T \to \infty$ para todo $m$. Entonces, por el factor $1/T$ de (10.46), todos los $c_n$ tienden a cero como $1/T$. Así pues, deberíamos multiplicar $c_n$ por $T$ para obtener algo finito en el límite. Comparando (10.45) con (10.9), vemos que deberíamos tomar $\omega$ igual a $n/T$.

Así, la relación (10.45) es un análogo de la integral de Fourier (10.9), donde la correspondencia es

$$\frac{1}{T} \to d\omega, \qquad \frac{n}{T} \to \omega, \qquad c_n T \to C(\omega).\qquad\text{(10.48)}$$

En el límite $T \to \infty$, la suma se convierte en una integral sobre $\omega$. Multiplicando ambos miembros de (10.46) por $T$ y haciendo la sustitución de (10.48) se obtiene (10.37).

### 10.3.1 Un ejemplo resoluble

Como práctica en el manejo de integrales de funciones complejas, haremos con todo detalle la integración que lleva a (10.40), con todos los pasos:

$$2\pi C(\omega) = \int_{-\infty}^{\infty} dt\, e^{-\Gamma|t|}e^{i\omega t}.\qquad\text{(10.49)}$$

Primero nos deshacemos del valor absoluto:

$$= \int_0^{\infty} dt\, e^{-\Gamma t}e^{i\omega t} + \int_{-\infty}^{0} dt\, e^{\Gamma t}e^{i\omega t}$$

y escribimos la segunda integral como una integral de 0 a $\infty$:

$$= \int_0^{\infty} dt\, e^{-\Gamma t}e^{i\omega t} + \int_0^{\infty} dt\, e^{-\Gamma t}e^{-i\omega t} = \int_0^{\infty} dt\, e^{-\Gamma t}e^{i\omega t} + \text{complejo conjugado},$$

pero sabemos derivar exponenciales, incluso complejas (véase la discusión de (3.108)), así que podemos escribir

$$\frac{\partial}{\partial t}\left(e^{-\Gamma t}e^{i\omega t}\right) = (-\Gamma + i\omega)\,e^{-\Gamma t}e^{i\omega t}.$$

Por tanto,

$$\int_0^{\infty} dt\, e^{-\Gamma t}e^{i\omega t} = \frac{1}{-\Gamma + i\omega}\int_0^{\infty} dt\,\frac{\partial}{\partial t}\left(e^{-\Gamma t}e^{i\omega t}\right)$$

o, usando el teorema fundamental del cálculo integral,

$$= \frac{1}{-\Gamma + i\omega}\left.e^{-\Gamma t}e^{i\omega t}\right|_0^{\infty} = \frac{1}{\Gamma - i\omega}.$$

Esta función de $\omega$ se llama un «polo». Aunque la función se comporta perfectamente bien para $\omega$ real, se dispara para $\omega = -i\Gamma$, que es la posición del polo en el plano complejo. Ahora solo tenemos que añadir el complejo conjugado para obtener

$$2\pi C(\omega) = \frac{1}{\Gamma - i\omega} + \frac{1}{\Gamma + i\omega} = \frac{\Gamma + i\omega}{\Gamma^2 + \omega^2} + \frac{\Gamma - i\omega}{\Gamma^2 + \omega^2} = \frac{2\Gamma}{\Gamma^2 + \omega^2},\qquad\text{(10.56)}$$

que es (10.40). Ya comprobamos, en (10.41), que el factor $1/2\pi$ tiene sentido.

El par (10.39)-(10.40) ilustra un hecho muy general sobre las señales y sus espectros de frecuencia asociados. En la figura 10.4 representamos $f(t)$ para $\Gamma = 0.5$ y $\Gamma = 2$, y en la figura 10.5 representamos $C(\omega)$ para los mismos valores de $\Gamma$. Nótese que, conforme $\Gamma$ aumenta, la señal se vuelve más aguda cerca de $t = 0$, pero el espectro de frecuencias se ensancha. Y, recíprocamente, si $\Gamma$ es pequeño, de modo que $C(\omega)$ está muy concentrada cerca de $\omega = 0$, entonces $f(t)$ está extendida en el tiempo. Este comportamiento complementario es general: para resolver tiempos cortos hace falta un espectro amplio de frecuencias.

![Figura 10.4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.4.png)

Figura 10.4: $f(t) = e^{-\Gamma|t|}$ para $\Gamma = 0.5$ y $\Gamma = 2$.

![Figura 10.5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.5.png)

Figura 10.5: $C(\omega)$ para los mismos valores de $\Gamma$.

### 10.3.2 Generalidades amplias

Podemos enunciar este hecho de forma muy general usando una definición matemática precisa de la anchura de la señal en el tiempo y de la anchura del espectro en frecuencia.

Definiremos la intensidad de la señal como proporcional a $|f(t)|^2$. Entonces podemos definir el valor medio de cualquier función $g(t)$ pesado con la intensidad de la señal como sigue:

$$\langle g(t)\rangle = \frac{\int_{-\infty}^{\infty} dt\, g(t)\,|f(t)|^2}{\int_{-\infty}^{\infty} dt\,|f(t)|^2}.\qquad\text{(10.57)}$$

Esto pesa más $g(t)$ allí donde la señal es más intensa.

Por ejemplo, $\langle t\rangle$ es el tiempo medio, es decir, el valor del tiempo alrededor del cual la señal es más intensa. Entonces

$$\left\langle[t - \langle t\rangle]^2\right\rangle \equiv \Delta t^2\qquad\text{(10.58)}$$

mide la desviación cuadrática media respecto del tiempo medio, así que es una medida de la anchura de la señal.

Podemos definir el valor medio de una función de $\omega$ de manera análoga, integrando sobre la intensidad del espectro de frecuencias. Pero aquí está el truco: gracias a (10.9) y (10.37) podemos ir y venir entre $f(t)$ y $C(\omega)$ a voluntad. Ambas llevan la misma información. Deberíamos poder calcular promedios de funciones de $\omega$ mediante una integral sobre $t$. Y, en efecto, podemos. Considere la integral

$$\int d\omega\,\omega\,C(\omega)\,e^{-i\omega t} = i\frac{\partial}{\partial t}\int d\omega\, C(\omega)\,e^{-i\omega t} = i\frac{\partial}{\partial t}f(t).$$

Esto muestra que multiplicar $C(\omega)$ por $\omega$ equivale a derivar la $f(t)$ correspondiente y multiplicar por $i$.

Así, podemos calcular $\langle\omega\rangle$ como

$$\langle\omega\rangle = \frac{\int_{-\infty}^{\infty} dt\, f(t)^*\,i\frac{\partial}{\partial t}f(t)}{\int_{-\infty}^{\infty} dt\,|f(t)|^2}\qquad\text{(10.60)}$$

y

$$\Delta\omega^2 \equiv \left\langle[\omega - \langle\omega\rangle]^2\right\rangle = \frac{\int_{-\infty}^{\infty} dt\,\left|\left(i\frac{\partial}{\partial t} - \langle\omega\rangle\right)f(t)\right|^2}{\int_{-\infty}^{\infty} dt\,|f(t)|^2}.\qquad\text{(10.61)}$$

$\Delta\omega$ es una medida de la anchura del espectro de frecuencias, o «ancho de banda».

Ahora podemos enunciar y demostrar el resultado siguiente:

$$\Delta t\,\Delta\omega \geq \frac{1}{2}.\qquad\text{(10.62)}$$

Una consecuencia importante de este teorema es que, para un ancho de banda $\Delta\omega$ dado, la anchura temporal de la señal no puede ser arbitrariamente pequeña, sino que está acotada por

$$\Delta t \geq \frac{1}{2\Delta\omega}.\qquad\text{(10.63)}$$

Cuanto menor sea el valor mínimo posible de $\Delta t$ que puede enviar, mayor será la «fidelidad» que puede alcanzar. Un $\Delta t$ menor significa que puede enviar señales con detalles más finos. Pero (10.63) significa que, cuanto menor es el ancho de banda, mayor es el $\Delta t$ mínimo y menor la fidelidad.

Para demostrar (10.62), considere la función[3]

$$\left([t - \langle t\rangle] - i\kappa\left(i\frac{\partial}{\partial t} - \langle\omega\rangle\right)\right)f(t) = r(t),\qquad\text{(10.64)}$$

que depende del parámetro enteramente libre $\kappa$.

Ahora fíjese en el cociente

$$\frac{\int_{-\infty}^{\infty} dt\,|r(t)|^2}{\int_{-\infty}^{\infty} dt\,|f(t)|^2}.\qquad\text{(10.65)}$$

Este cociente es obviamente positivo, porque los integrandos del numerador y del denominador son ambos positivos. Lo que haremos será elegir $\kappa$ de forma astuta, de modo que el hecho de que el cociente sea positivo nos diga algo interesante.

Primero simplificaremos (10.65). En los términos de (10.65) que involucran derivadas de $f(t)^*$, podemos integrar por partes (y desechar los términos de contorno, porque suponemos que $f(t)$ tiende a cero en el infinito) para que las derivadas actúen sobre $f(t)$. Entonces (10.65) queda

$$\Delta t^2 + \kappa^2\Delta\omega^2 + \kappa\,\frac{\int_{-\infty}^{\infty} dt\, f(t)^*\left(t\frac{\partial}{\partial t} - \frac{\partial}{\partial t}t\right)f(t)}{\int_{-\infty}^{\infty} dt\,|f(t)|^2}.\qquad\text{(10.66)}$$

Todos los demás términos se cancelan. Pero

$$\frac{\partial}{\partial t}\left[t f(t)\right] = f(t) + t\frac{\partial}{\partial t}f(t).\qquad\text{(10.67)}$$

Así, el último término de (10.66) es simplemente $-\kappa$, y (10.65) queda

$$\Delta t^2 + \kappa^2\Delta\omega^2 - \kappa.\qquad\text{(10.68)}$$

(10.68) es claramente mayor o igual que cero para cualquier valor de $\kappa$, porque es un cociente de integrales positivas. Para sacar la máxima información del hecho de que es positivo, deberíamos elegir $\kappa$ de modo que (10.65) (= (10.68)) sea lo más pequeño posible. Dicho de otro modo, deberíamos hallar el valor de $\kappa$ que minimiza (10.68). Si derivamos (10.68) e igualamos el resultado a cero, encontramos

$$\kappa_{\min} = \frac{1}{2\Delta\omega^2}.$$

Ahora podemos llevar esto de vuelta a (10.68) para hallar el mínimo, que sigue siendo mayor o igual que cero. Es

$$\Delta t^2 - \frac{1}{4\Delta\omega^2} \geq 0,$$

lo que da inmediatamente (10.62).

La ecuación (10.62) aparece en muchos lugares de la física. Un ejemplo sencillo es el ancho de banda en las transmisiones de radio AM. Una emisora comercial de AM típica emite en una banda de frecuencia de unos 5000 ciclos/s (5 kc) a cada lado de la frecuencia de la portadora. Así,

$$\Delta\omega = 2\pi\Delta\nu \approx 3\times10^4\ \text{s}^{-1},\qquad\text{(10.71)}$$

y no pueden enviar señales que separen tiempos menores que unos pocos $\times10^{-5}$ segundos. Esto es suficiente para la palabra y aceptable para algo de música.

Un ejemplo famoso de (10.62) viene de la mecánica cuántica. Hay una relación completamente análoga entre la anchura espacial de un paquete de ondas, $\Delta x$, y la anchura de los valores de $k$ necesarios para producirlo, $\Delta k$:

$$\Delta x\,\Delta k \geq \frac{1}{2}.\qquad\text{(10.72)}$$

En mecánica cuántica, el momento de una partícula está relacionado con el valor de $k$ de la onda que la describe por

$$p = \hbar k,\qquad\text{(10.73)}$$

donde $\hbar$ es la constante de Planck $h$ dividida por $2\pi$. Así, (10.72) implica

$$\Delta x\,\Delta p \geq \frac{\hbar}{2}.\qquad\text{(10.74)}$$

Este es el enunciado matemático del hecho de que la posición y el momento de una partícula no pueden especificarse simultáneamente. Es la relación de incertidumbre de Heisenberg.

## 10.4 Dispersión de paquetes de ondas

En un experimento real de dispersión no nos interesa una onda armónica entrante que haya existido siempre y vaya a existir siempre. Lo que nos interesa es un paquete de ondas entrante limitado en el tiempo. En esta sección discutimos dos ejemplos de dispersión de paquetes de ondas.

### 10.4.1 Dispersión en una frontera

Empezamos con el más fácil de los dos ejemplos. Considere la dispersión de un paquete de ondas en la frontera entre dos cuerdas semiinfinitas sin dispersión, ambas con tensión $T$ y densidades distintas, $\rho_I$ y $\rho_{II}$, como se muestra en la figura 9.1. Las relaciones de dispersión son:

$$\omega = \begin{cases} v_I k = \sqrt{\dfrac{T}{\rho_I}}\,k & \text{en la región I} \\[8pt] v_{II} k = \sqrt{\dfrac{T}{\rho_{II}}}\,k & \text{en la región II} \end{cases}\qquad\text{(10.75)}$$

donde $v_I$ y $v_{II}$ son las velocidades de fase en las dos regiones.

Concretamente, suponemos que la condición de contorno en $-\infty$ es que hay una onda entrante,

$$f(x - vt)$$

en la región I, pero ninguna onda entrante en la región II, y queremos hallar las ondas salientes: la onda reflejada en la región I y la transmitida en la región II.

Podemos resolver este problema sin descomponer el paquete de ondas en sus componentes armónicas, con un truco análogo al usado al principio de este capítulo para resolver el problema de oscilación forzada de la figura 10.1. La solución más general de las condiciones de contorno en $\pm\infty$ es

$$\psi(x, t) = \begin{cases} f(t - x/v_I) + g(t + x/v_I) & \text{en la región I} \\[4pt] h(t - x/v_{II}) & \text{en la región II} \end{cases}\qquad\text{(10.77)}$$

donde $g$ y $h$ son funciones arbitrarias. Para determinar realmente las ondas reflejada y transmitida debemos imponer las condiciones de contorno en $x = 0$: que el desplazamiento sea continuo (porque la cuerda no se rompe) y que su derivada respecto de $x$ sea continua (porque el nudo que une las dos cuerdas no tiene masa):

$$f(t) + g(t) = h(t),\qquad\text{(10.78)}$$

y

$$\left.\frac{\partial}{\partial x}\left[f(t - x/v_I) + g(t + x/v_I)\right]\right|_{x=0} = \left.\frac{\partial}{\partial x}h(t - x/v_{II})\right|_{x=0}.\qquad\text{(10.79)}$$

Usando la regla de la cadena en (10.79), podemos relacionar las derivadas parciales respecto de $x$ con las derivadas de las funciones,

$$\frac{1}{v_I}\left(-f'(t - x/v_I) + g'(t + x/v_I)\right)\bigg|_{x=0} = -\frac{1}{v_{II}}h'(t - x/v_{II})\bigg|_{x=0},$$

o sea,

$$-f'(t) + g'(t) = -\frac{v_I}{v_{II}}h'(t).\qquad\text{(10.81)}$$

Derivando (10.78), obtenemos

$$f'(t) + g'(t) = h'(t).\qquad\text{(10.82)}$$

Ahora, para cada valor de $t$, (10.81) y (10.82) forman un par de ecuaciones lineales simultáneas que pueden resolverse para $g'(t)$ y $h'(t)$ en términos de $f'(t)$:

$$g'(t) = \frac{1 - v_I/v_{II}}{1 + v_I/v_{II}}f'(t), \qquad h'(t) = \frac{2}{1 + v_I/v_{II}}f'(t).$$

Deshaciendo las derivadas, podemos escribir

$$g(t) = \frac{1 - v_I/v_{II}}{1 + v_I/v_{II}}f(t) + k_1, \qquad h(t) = \frac{2}{1 + v_I/v_{II}}f(t) + k_2,$$

donde $k_1$ y $k_2$ son constantes independientes de $t$. De hecho, debemos tener $k_1 = k_2$ para satisfacer (10.78), y sumar la misma constante en ambas regiones es irrelevante, porque corresponde simplemente a nuestra libertad de desplazar toda la cuerda hacia arriba o hacia abajo en la dirección transversal. Concluimos, por tanto, que

$$g(t) = \frac{1 - v_I/v_{II}}{1 + v_I/v_{II}}f(t), \qquad h(t) = \frac{2}{1 + v_I/v_{II}}f(t)$$

y la solución (10.77) queda

$$\psi(x, t) = \begin{cases} f(t - x/v_I) + \dfrac{1 - v_I/v_{II}}{1 + v_I/v_{II}}f(t + x/v_I) & \text{en la región I,} \\[10pt] \dfrac{2}{1 + v_I/v_{II}}f(t - x/v_{II}) & \text{en la región II.} \end{cases}\qquad\text{(10.86)}$$

El mismo resultado surge si descomponemos el paquete de ondas entrante en sus componentes armónicas. Para cada componente armónica, los coeficientes de reflexión y transmisión son los mismos (de (9.16)):

$$\tau = \frac{2Z_I}{Z_I + Z_{II}} = \frac{2}{1 + v_I/v_{II}}, \qquad R = \frac{Z_I - Z_{II}}{Z_I + Z_{II}} = \frac{1 - v_I/v_{II}}{1 + v_I/v_{II}}.$$

Cuando ahora volvemos a juntar las componentes armónicas para obtener los paquetes de ondas dispersado y transmitido, los coeficientes $\rho$ y $\tau$ aparecen simplemente como constantes globales delante del pulso original, como en (10.86).

Este proceso de dispersión está animado en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-10-3" rel="noopener" target="_blank" title="Animación original de Howard Georgi">10-3</a>. Ahí puede introducir distintos valores de $v_{II}/v_I$ para ver cómo se ven afectadas la reflexión y la transmisión. Nótese que un $v_{II}/v_I$ muy pequeño corresponde a un cociente de impedancias $Z_{II}/Z_I$ grande, lo que significa que la cuerda de la región II apenas se mueve. Entonces obtenemos un pulso reflejado que es simplemente el pulso entrante volcado por debajo de la cuerda. En el límite extremo $v_{II}/v_I \to \infty$, el contorno en $x = 0$ actúa como un extremo fijo. Un $v_{II}/v_I$ muy grande corresponde a un cociente de impedancias $Z_{II}/Z_I$ pequeño, en cuyo caso la cuerda de la región I apenas nota la cuerda de la región II. En el límite $v_{II}/v_I \to 0$, el contorno en $x = 0$ actúa como un extremo libre.

### 10.4.2 Una masa sobre una cuerda

Un ejemplo más interesante de dispersión de paquetes de ondas, que puede resolverse con las matemáticas que ya hemos hecho, es la dispersión de un paquete de ondas entrante con la forma de (10.39) que se encuentra con una masa sobre una cuerda. Aquí la relación de dispersión es trivial, así que el paquete se propaga sin cambio de forma hasta que «choca» con la masa. Pero entonces ocurren cosas interesantes. Esta vez, cuando descomponemos el paquete en sus componentes armónicas, los coeficientes de reflexión y transmisión dependen de $\omega$. Cuando los volvemos a sumar para obtener los paquetes reflejado y transmitido, encontraremos que la forma ha cambiado. Lo desarrollaremos en detalle. El montaje, ya familiar, se muestra en la figura 10.6.

![Figura 10.6](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.6.png)

Figura 10.6: una masa sobre una cuerda.

Para una onda armónica entrante de amplitud $A$, el desplazamiento es

$$\psi(x, t) = A e^{ikx}e^{-i\omega t} + R\,A e^{-ikx}e^{-i\omega t} \quad \text{para } x \leq 0$$

$$\psi(x, t) = \tau\,A e^{ikx}e^{-i\omega t} \quad \text{para } x \geq 0$$

La solución para $R$ y $\tau$ se obtuvo en el capítulo anterior en (9.39)-(9.45). Sin embargo, el parámetro $\epsilon$ de (9.38) depende de $\omega$. Para desenredar la dependencia en frecuencia de los paquetes dispersados, escribimos $R$ y $\tau$ como

$$\tau = \frac{2\Omega}{2\Omega - i\omega}, \qquad R = \frac{i\omega}{2\Omega - i\omega}\qquad\text{(10.90)}$$

donde

$$\Omega = \frac{T}{mv} = \frac{\sqrt{\rho T}}{m}$$

es independiente de $\omega$: depende solo de los parámetros fijos de la cuerda y de la masa. Nótese que, en la notación de (9.38), $\epsilon = \Omega/\omega$.

Supongamos que no tenemos una onda armónica entrante, sino un pulso entrante:

$$\psi_{\text{in}}(x - vt) = A e^{-\Gamma|t - x/v|}.\qquad\text{(10.92)}$$

Ahora la situación es más interesante. Esperamos una solución de la forma

$$\psi(x, t) = \psi_{\text{in}}(x - vt) + \psi_R(x + vt) \quad \text{para } x \leq 0$$

$$\psi(x, t) = \psi_\tau(x - vt) \quad \text{para } x \geq 0$$

donde $\psi_\tau(x - vt)$ es la onda transmitida, que viaja en la dirección $+x$, y $\psi_R(x + vt)$ es la onda reflejada, que viaja en la dirección $-x$. Para obtener las ondas reflejada y transmitida usaremos la superposición y descompondremos $\psi_{\text{in}}$ en componentes armónicas. Podemos entonces usar (10.90) para determinar la dispersión de cada una de las componentes, y después volver a juntar las piezas para obtener la solución. Así pues, empezamos transformando por Fourier $\psi_{\text{in}}$:

$$\psi_{\text{in}}(x, t) = \int d\omega\, e^{-i\omega(t - x/v)}\,C_{\text{in}}(\omega).$$

Sabemos, de nuestra discusión sobre señales, que

$$C_{\text{in}}(\omega) = \frac{1}{2\pi}\int dt\, e^{i\omega t}\,\psi_{\text{in}}(0, t) = \frac{A}{2\pi}\left(\frac{1}{\Gamma - i\omega} + \frac{1}{\Gamma + i\omega}\right).$$

Ahora, para obtener los pulsos reflejado y transmitido, multiplicamos las componentes de $\psi_{\text{in}}$ por las amplitudes de reflexión y transmisión $R$ y $\tau$ para $\psi_{\text{in}}$ unidad:

$$C_\tau(\omega) = \frac{A}{2\pi}\left(\frac{1}{\Gamma - i\omega} + \frac{1}{\Gamma + i\omega}\right)\frac{2\Omega}{2\Omega - i\omega}\qquad\text{(10.98)}$$

$$C_R(\omega) = \frac{A}{2\pi}\left(\frac{1}{\Gamma - i\omega} + \frac{1}{\Gamma + i\omega}\right)\frac{i\omega}{2\Omega - i\omega}\qquad\text{(10.99)}$$

Ahora tenemos que invertir el proceso y hallar las transformadas de Fourier de estas para obtener los pulsos reflejado y transmitido. Esto es directo, porque podemos reescribir (10.98) y (10.99) en términos de polos simples en $\omega$. Después podemos trabajar hacia atrás para obtener las transformadas de Fourier: sabemos de (10.55) que cada término es la transformada de Fourier de una exponencial. Es directo, aunque tedioso, volver a juntarlos. El resultado se reproduce abajo (nótese que hemos combinado los dos términos de cada expresión proporcionales a $1/(2\Omega - i\omega)$):

$$C_\tau(\omega) = A\,\frac{1}{2\pi}\frac{2\Omega}{2\Omega - \Gamma}\left(\frac{1}{\Gamma - i\omega} - \frac{1}{2\Omega - i\omega}\right) + \frac{1}{2\pi}\frac{2\Omega}{2\Omega + \Gamma}\left(\frac{1}{\Gamma + i\omega} + \frac{1}{2\Omega - i\omega}\right);\qquad\text{(10.100)}$$

$$C_R(\omega) = A\,\frac{1}{2\pi}\frac{1}{2\Omega - \Gamma}\left(\frac{\Gamma}{\Gamma - i\omega} - \frac{2\Omega}{2\Omega - i\omega}\right) + \frac{1}{2\pi}\frac{1}{2\Omega + \Gamma}\left(-\frac{\Gamma}{\Gamma + i\omega} + \frac{2\Omega}{2\Omega - i\omega}\right).\qquad\text{(10.101)}$$

Ahora podemos trabajar hacia atrás en (10.100) y (10.101) para obtener las transformadas de Fourier. Sabemos de (10.55) que cada término es la transformada de Fourier de una exponencial. Es directo, aunque tedioso, volver a juntarlos. El resultado se reproduce abajo (nótese que hemos combinado los dos términos de cada expresión proporcionales a $1/(2\Omega - i\omega)$):

$$\begin{aligned}
\psi_\tau(x, t) = {} & \frac{2\Omega}{2\Omega - \Gamma}\,\theta(t - x/v)\,A e^{-\Gamma(t - x/v)}\\
& - \frac{4\Omega\Gamma}{4\Omega^2 - \Gamma^2}\,\theta(t - x/v)\,A e^{-2\Omega(t - x/v)}\\
& + \frac{2\Omega}{2\Omega + \Gamma}\,\theta(-t + x/v)\,A e^{\Gamma(t - x/v)}\qquad\text{(10.102)}
\end{aligned}$$

y

$$\begin{aligned}
\psi_r(x, t) = {} & \frac{2\Gamma}{2\Omega - \Gamma}\,\theta(t + x/v)\,A e^{-\Gamma(t + x/v)}\\
& - \frac{4\Omega\Gamma}{4\Omega^2 - \Gamma^2}\,\theta(t + x/v)\,A e^{-2\Omega(t + x/v)}\\
& - \frac{2\Gamma}{2\Omega + \Gamma}\,\theta(-t - x/v)\,A e^{\Gamma(t + x/v)}\qquad\text{(10.103)}
\end{aligned}$$

donde

$$\theta(t) = \begin{cases} 1 & \text{para } t \geq 0, \\ 0 & \text{para } t < 0. \end{cases}\qquad\text{(10.104)}$$

![Figura 10.7](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.7.png)

Figura 10.7: un paquete de ondas en una cuerda tensada, en $t = -2$.

![Figura 10.8](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.8.png)

Figura 10.8: $t = -1$.

Estas fórmulas no son muy transparentes ni informativas, pero podemos meterlas en un ordenador y mirar el resultado. Representaremos el resultado en el límite $2\Omega \to \Gamma$. Los resultados (10.102) y (10.103) parecen singulares en este límite pero, en realidad, el límite existe y es perfectamente suave.[4] En las figuras 10.7-10.12 mostramos $\psi(x, t)$ para $\Gamma = v = 1$ en unidades arbitrarias, para valores de $t$ desde $-2$ hasta 3.

![Figura 10.9](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.9.png)

Figura 10.9: $t = 0$.

![Figura 10.10](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.10.png)

Figura 10.10: $t = 1$.

![Figura 10.11](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.11.png)

Figura 10.11: $t = 2$.

En $t = -2$ se ve el pulso acercándose a la masa para $t$ negativo. En $t = -1$ empieza a apreciarse el efecto de la masa sobre la cuerda. Para $t = 0$, la cuerda a la izquierda de $x = 0$ se mueve rápidamente hacia abajo. En $t = 1$, el movimiento descendente de la cuerda para $x < 0$ ha continuado y ha empezado a formar el pulso reflejado. Para $t = 2$ se ve cómo las ondas transmitida y reflejada empiezan a separarse. Para $t = 3$ se ve que los pulsos reflejado y transmitido se han separado casi por completo y que la masa ha vuelto casi a su posición de equilibrio. Para $t$ positivo grande, el pulso se ha dividido en una onda reflejada y otra transmitida.

![Figura 10.12](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.12.png)

Figura 10.12: $t = 3$.

Lo realmente interesante ocurre entre $t = 0$ y $t = 1$, así que lo miraremos en una escala temporal más fina en las figuras 10.13-10.16. Para apreciarlo de verdad, debería verlo en movimiento: está animado en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-10-4" rel="noopener" target="_blank" title="Animación original de Howard Georgi">10-4</a>.

![Figura 10.13](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.13.png)

Figura 10.13: $t = 0.2$.

![Figura 10.14](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.14.png)

Figura 10.14: $t = 0.4$.

![Figura 10.15](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.15.png)

Figura 10.15: $t = 0.6$.

![Figura 10.16](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh10_ES/fig10.16.png)

Figura 10.16: $t = 0.8$.

## 10.5 ¿Es $c$ la velocidad de la luz?

Hemos visto que una onda electromagnética en la dirección $z$ que satisface las ecuaciones de Maxwell en el espacio libre tiene la relación de dispersión (8.47), de modo que la luz, al menos en el vacío, viaja a la velocidad de la luz. Pero ¿es correcta la teoría? ¿Cómo comprobamos la relación de dispersión? De hecho, las pruebas más sensibles de las ecuaciones de Maxwell no involucran ondas viajeras: provienen de observaciones de campos magnéticos que se extienden a distancias astrofísicas (¡como la galaxia!). Sin embargo, hay una manera interesante, aunque no muy sensible, de buscar correcciones a (8.47) que involucra directamente la velocidad de la luz. Antes de discutirla, hagamos una breve digresión para hablar con más detalle de los fotones, las partículas de luz que describimos brevemente en el capítulo 8.

La luz es un fenómeno ondulatorio, como hemos visto. De hecho, las propiedades ondulatorias de la luz son evidentes en nuestra experiencia cotidiana. Es menos evidente a partir de esa experiencia, pero igualmente cierto, que la luz también consta de fotones. Esto se hace obvio cuando se trabaja con luz a intensidades muy bajas o a energías muy altas. Que ambas afirmaciones puedan ser ciertas simultáneamente es uno de los (muchos) milagros de la mecánica cuántica.

La mecánica cuántica nos dice que todas las partículas tienen propiedades ondulatorias. Una partícula con momento $p$ y energía $E$ tiene asociadas una frecuencia angular y un número de onda angular relacionados por

$$E = \hbar\omega, \qquad p = \hbar k,\qquad\text{(10.105)}$$

donde $\hbar$ es la constante de Planck dividida por $2\pi$. Esta combinación aparece de forma tan ubicua en mecánica cuántica que tiene su propio símbolo, y los físicos casi siempre usamos $\hbar$ en vez de $h$. La razón es simplemente que $h$ está relacionada con la frecuencia $\nu$, en vez de con la frecuencia angular $\omega$, y hemos visto que $\omega$ es la medida más conveniente para la mayoría de los propósitos. Además, la energía y el momento de la partícula están relacionados así:

$$E^2 = p^2c^2 + m^2c^4, \qquad v = c\,\frac{pc}{E}\qquad\text{(10.106)}$$

donde $m$ es la masa en reposo y $v$ es la velocidad clásica.

Si ponemos (10.105) en (10.106), obtenemos una relación de dispersión para la onda mecanocuántica asociada a la partícula,

$$\omega^2 = c^2k^2 + \omega_0^2, \qquad \omega_0 = \frac{mc^2}{\hbar}.\qquad\text{(10.107)}$$

¡La velocidad clásica es la velocidad de grupo de la onda mecanocuántica!

$$v = \frac{pc^2}{E} = \frac{c^2 k}{\omega} = \frac{\partial\omega}{\partial k}.$$

De hecho, las partículas, en una imagen mecanocuántica, corresponden a paquetes de ondas que se mueven con la velocidad de grupo.

La relación de dispersión mecanocuántica, (10.107), concuerda con (8.47) solo si $m = 0$. Así pues, podemos reformular la pregunta de si (8.47) es correcta preguntando: «¿es realmente nula la masa del fotón?».

Parecería que deberíamos poder comprobar esta idea observando dos fotones de frecuencias distintas emitidos al mismo tiempo desde un objeto lejano y comprobando si llegan al mismo tiempo. Hay un fallo evidente en este plan: si el objeto está tan lejos que no podemos llegar hasta él, ¿cómo sabemos que los dos fotones fueron emitidos al mismo tiempo? De hecho, la astrofísica nos ha proporcionado una manera de sortear esta dificultad: podemos mirar los púlsares. Los púlsares son (presumiblemente) restos de estrellas de neutrones en rotación procedentes de explosiones de supernova, que emiten luz hacia la Tierra a intervalos regulares. Por ejemplo, el púlsar 1937+21 es tan regular que el instante de salida de los fotones puede determinarse con una precisión de unos pocos microsegundos (µs).[5] Además está a unos 16 000 años luz, así que los fotones de mayor frecuencia (los más rápidos) tienen tiempo de sobra para adelantarse. Cuando se hace este experimento, se encuentra un $\omega_0$ no nulo, de unos $1.7\times10^4\ \text{s}^{-1}$, que corresponde a una masa de unos $1.26\times10^{-49}$ g. Puede parecer una masa bastante pequeña, pero de hecho es ridículamente grande para un fotón: por estudios del campo magnético galáctico sospechamos que es menor que $4\times10^{-65}$ g.[6] Así que está ocurriendo alguna otra cosa.

El problema de esta medida como prueba de la relación de dispersión es que ahí fuera hay electrones: electrones libres en el espacio interestelar ($10^{-1}$ a $10^{-2}$ cm$^{-3}$). Esos electrones del espacio se agitarán en el campo $E$; eso producirá una densidad de corriente que afectará a las ecuaciones de Maxwell y eso, a su vez, afectará a la relación de dispersión. Analicemos el efecto de este plasma diluido suponiendo que la densidad de electrones es constante. Entonces (al menos para las ondas de radio de longitud de onda larga que interesan en estos experimentos) todavía podemos usar la invariancia bajo traslación para entender lo que ocurre. Considere una onda plana en la dirección $z$ y suponga que el campo eléctrico de la onda plana está en la dirección $x$. Entonces sigue siendo cierto que, a un $\omega$ dado,

$$E_x(\vec{r}, t) = E_0 e^{i(kz - \omega t)}, \qquad B_y(\vec{r}, t) = B_0 e^{i(kz - \omega t)},\qquad\text{(10.108)}$$

para algún $k$. Para hallar $k$ debemos mirar el efecto de los campos eléctricos sobre los electrones y volver después a las ecuaciones de Maxwell. Los campos son muy pequeños y, para campos pequeños, las velocidades inducidas de los electrones, $v$, son pequeñas. Así, podemos despreciar $B$. Entonces la fuerza sobre un electrón en el punto $(\vec{r}, t)$ es

$$F_x(\vec{r}, t) = e\,E_x(\vec{r}, t) = e\,E_0 e^{i(kz - \omega t)} = m\,a_x(\vec{r}, t).\qquad\text{(10.110)}$$

El desplazamiento del electrón tiene la misma forma:

$$d_x(\vec{r}, t) = d_0 e^{i(kz - \omega t)}$$

lo que implica

$$a_x(\vec{r}, t) = -\omega^2 d_0 e^{i(kz - \omega t)}.\qquad\text{(10.112)}$$

Comparando (10.110) y (10.112) se obtiene

$$d_0 = -\frac{e\,E_0}{m\,\omega^2}.$$

Así, los electrones se desplazan $180°$ desfasados respecto del campo eléctrico y en la misma dirección. Entonces la velocidad del electrón es

$$v_x = \frac{i\,e\,E_0}{m\,\omega}e^{i(kz - \omega t)}.$$

El movimiento de los electrones da lugar a una densidad de corriente:[7]

$$J_x = \frac{i\,e^2 N\,E_0}{m\,\omega}e^{i(kz - \omega t)},$$

donde $N$ es la densidad numérica de electrones.

Poniendo esto en las ecuaciones de Maxwell relevantes, encontramos

$$k\,E_0 = \omega\,B_0, \qquad -k\,B_0 = -\omega\mu_0\varepsilon_0 E_0 + \mu_0\frac{i\,e^2 N E_0}{m\,\omega}\cdot\frac{1}{i},$$

o, usando $c = 1/\sqrt{\mu_0\varepsilon_0}$, (8.47),

$$\frac{k^2}{\omega} = \frac{\omega}{c^2} - \frac{e^2 N}{c^2 m\,\varepsilon_0\,\omega},$$

o, despejando $\omega^2$,

$$\omega^2 = c^2k^2 + \omega_0^2, \qquad \text{con } \omega_0^2 = \frac{e^2 N}{m\,\varepsilon_0}.\qquad\text{(10.118)}$$

La constante $\omega_0$ de (10.118) se llama «frecuencia de plasma». Lo asombroso es que se comporta exactamente igual que una masa del fotón. Para $N \approx 10^{-2}$ cm$^{-3}$, esto es coherente con la observación del púlsar.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Resolver un problema de oscilación forzada para una cuerda tensada con un desplazamiento arbitrario dependiente del tiempo en el extremo;

2.  Descomponer una señal arbitraria en componentes armónicas mediante la transformación de Fourier;

3.  Calcular la velocidad de grupo de un sistema dispersivo;

4.  Comprender las relaciones entre una función y su transformada de Fourier que llevan a la relación entre ancho de banda y fidelidad;

5.  Ser capaz de describir la dispersión de un paquete de ondas;

6.  Comprender el efecto de las cargas libres sobre la relación de dispersión de las ondas electromagnéticas.

## Problemas

**10.1.** ¿Es posible que un medio que soporta ondas electromagnéticas tenga la relación de dispersión $\omega^2 = c^2k^2 - \omega_0^2$ para $\omega_0$ real? ¿Por qué sí o por qué no?

**10.2.** Una cuerda con cuentas tiene las cuentas vecinas separadas una distancia $a$. Si la velocidad de grupo máxima posible para las ondas en la cuerda es $v$, halle $T/m$.

**10.3.** En el próximo capítulo deduciremos la relación de dispersión de las ondas en el agua (o, al menos, en una imagen idealizada del agua). Si el agua es profunda, la relación de dispersión es

$$\omega^2 = gk + \frac{T k^3}{\rho}$$

donde $g$ es la aceleración de la gravedad, 980 en unidades cgs, $T$ es la tensión superficial, 72, y $\rho$ es la densidad, 1.0. Halle la velocidad de grupo y la velocidad de fase en función de la longitud de onda. ¿Cuándo son iguales?

**10.4.** Considere las oscilaciones longitudinales del sistema de bloques y muelles sin masa que se muestra abajo. Cada bloque tiene masa $m$. Cada muelle tiene constante $K$. La separación de equilibrio entre los bloques es $a$. El anillo de la izquierda se mueve adelante y atrás con desplazamiento $B\cos\omega t$. Esto produce una onda viajera en el sistema que se mueve hacia la derecha para $\omega < 2\sqrt{K/m}$. No hay onda viajera moviéndose hacia la izquierda.

La relación de dispersión del sistema es

$$\omega^2 = \frac{4K}{m}\sin^2\frac{ka}{2}.$$

**a.** Suponga que $\omega = \sqrt{K/m}$. Halle la velocidad de fase de las ondas viajeras a esta frecuencia.

**b.** Para $\omega = \sqrt{K/m}$, halle el desplazamiento del primer bloque en el instante $t = \pi/2\omega$. Exprese la respuesta como $B$ multiplicada por un número puro.

**c.** Halle la velocidad de grupo en el límite $\omega \to 2\sqrt{K/m}$.

**d.** Halle el promedio temporal de la potencia suministrada por la fuerza sobre el anillo en el límite $\omega \to 2\sqrt{K/m}$.

**e.** Explique la relación entre las respuestas de los apartados c y d. Puede que sea capaz de hacer este apartado incluso si se ha liado con el álgebra: piense en la física e intente entender qué debe estar ocurriendo.

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*

[1] Véase (10.71), más abajo.

[2] Un ejemplo de sistema físico con este tipo de condición de contorno sería una cuerda tensada alrededor de un cilindro sin fricción de radio $\ell$ y, por tanto, de circunferencia $2\pi\ell$. Entonces (10.42) sería cierta porque $x = -\pi\ell$ describe el mismo punto de la cuerda que $x = \pi\ell$.

[3] Este es un truco tomado de un análisis similar que conduce al principio de incertidumbre de Heisenberg en mecánica cuántica. No se preocupe si no le resulta obvio de dónde sale. Lo importante es el resultado.

[4] La aparente singularidad es similar a una que aparece al aproximarse al amortiguamiento crítico, discutido en (2.12).

[5] Véase G. Barbiellini y G. Cocconi, *Nature* **329** (1987) 21.

[6] Chibisov, *Soviet Physics - Uspekhi*, **19** (1986) 624.

[7] Nótese que el resultado es inversamente proporcional a la masa del electrón. Por eso nos concentramos en los electrones y no en los protones: ¡los protones no se mueven tan deprisa!


---

<!-- MIT8.03_TextCh11_ES.md -->

# Capítulo 11: Dos y tres dimensiones

Los conceptos de invariancia bajo traslación espacial e interacciones locales pueden extenderse de forma directa a sistemas con más de una dimensión espacial. Pero en dos y tres dimensiones estas ideas por sí solas no bastan para determinar los modos normales de un sistema arbitrario. Hacen falta trucos adicionales, o trabajo duro y llano.

## Vídeos de esta clase (YouTube)

- [Clase 16: Ondas en 2D y 3D, ley de Snell](https://www.youtube.com/watch?v=_kKIQ1h9UuA)

## Resumen previo

Aquí solo podremos discutir los trucos más sencillos, pero al menos podremos entender por qué los problemas son más difíciles.

1.  Empezamos explicando por qué el número de onda angular, $k$, se convierte en un vector en dos o tres dimensiones. Hallamos los modos normales de sistemas con condiciones de contorno sencillas.

2.  Discutimos después la dispersión en planos en el espacio de dos y tres dimensiones. Deducimos la ley de refracción de Snell y discutimos la reflexión total interna y el efecto túnel.

3.  Discutimos el ejemplo de las placas de Chladni.

4.  Damos un ejemplo bidimensional de guía de ondas, en la que las ondas están obligadas a propagarse solo en una dirección.

5.  Estudiamos las ondas en el agua (en una versión simplificada del agua).

6.  Introducimos el tema más avanzado de las ondas esféricas.

## 11.1 El vector $\vec{k}$

Considere la malla bidimensional de cuentas, un análogo bidimensional de la cuerda con cuentas, mostrada en la figura 11.1. Todas las cuentas tienen masa $m$. La tensión de las cuerdas horizontales (verticales) es $T_H$ ($T_V$) y la distancia entre cuentas es $a_H$ ($a_V$). No hay amortiguamiento. Podemos etiquetar las cuentas mediante un par de enteros $(j, k)$ que indican sus posiciones horizontal y vertical, como se muestra. Alternativamente, podemos etiquetarlas por sus posiciones en el plano $x$, $y$ según

$$(x, y) = (j a_H, k a_V).\qquad\text{(11.1)}$$

![Figura 11.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.1.png)

Figura 11.1: una malla bidimensional de cuentas.

Así pues, podemos describir sus pequeñas oscilaciones transversales (fuera del plano del papel, en la dirección $z$) o bien mediante una matriz $\psi_{jk}(t)$, o bien mediante una función

$$\psi(x, y, t); \qquad 0 \leq x \leq 5a_H,\ 0 \leq y \leq 4a_V.\qquad\text{(11.2)}$$

Usaremos (11.2) porque así podremos extender la discusión a sistemas continuos con más facilidad. Solo nos interesan las oscilaciones transversales de este sistema, en las que los bloques se mueven arriba y abajo fuera del plano del papel, porque esas oscilaciones no estiran mucho las cuerdas (solo a segundo orden en los desplazamientos pequeños). Las demás oscilaciones de un sistema así tienen frecuencias mucho más altas y están fuertemente amortiguadas, de modo que no son muy interesantes.

Como en el caso unidimensional, el primer paso es quitar las paredes y considerar el sistema infinito que se obtiene extendiendo el interior en todas las direcciones. Las oscilaciones del sistema resultante pueden describirse mediante una función $\psi(x, y, t)$, donde $x$ e $y$ no están restringidas.

Este sistema infinito tiene el mismo aspecto si se traslada $a_V$ verticalmente o $a_H$ horizontalmente. Podemos escribir soluciones para el sistema infinito usando dos veces nuestra discusión del caso unidimensional. Como el sistema tiene invariancia bajo traslación en la dirección $x$, esperamos poder hallar autoestados de la matriz $M^{-1}K$ proporcionales a

$$e^{ik_x x}\qquad\text{(11.3)}$$

para cualquier constante $k_x$. Como el sistema tiene invariancia bajo traslación en la dirección $y$, esperamos poder hallar autoestados de $M^{-1}K$ proporcionales a

$$e^{ik_y y}\qquad\text{(11.4)}$$

para cualquier constante $k_y$. Juntando (11.3) y (11.4), esperamos poder hallar autoestados de $M^{-1}K$ que tengan la forma

$$\psi(x, y) = A\,e^{ik_x x}e^{ik_y y} = A\,e^{i\vec{k}\cdot\vec{r}}\qquad\text{(11.5)}$$

donde $\vec{k}\cdot\vec{r}$ es el producto escalar bidimensional

$$\vec{k}\cdot\vec{r} = k_x x + k_y y.\qquad\text{(11.6)}$$

Dicho de otro modo, el número de onda se ha convertido en un vector.

Igual que con el sistema unidimensional, podemos usar (11.5) para determinar la relación de dispersión del sistema infinito. Incluyendo la dependencia en $t$, tenemos un desplazamiento de la forma

$$\psi(x, y, t) = A\,e^{i\vec{k}\cdot\vec{r}}\,e^{-i\omega t}.\qquad\text{(11.7)}$$

El análisis es exactamente análogo al de la cuerda unidimensional con cuentas, con el resultado de que $\omega^2$ es simplemente una suma de contribuciones vertical y horizontal, cada una de las cuales tiene el aspecto de la relación de dispersión del caso unidimensional:

$$\omega^2 = \frac{4T_H}{m a_H}\sin^2\frac{k_x a_H}{2} + \frac{4T_V}{m a_V}\sin^2\frac{k_y a_V}{2}.\qquad\text{(11.8)}$$

Las ecuaciones (11.7) y (11.8) son la solución completa de las ecuaciones del movimiento de la malla infinita de cuentas.

### 11.1.1 La diferencia entre una y dos dimensiones

Hasta aquí, nuestro análisis ha sido esencialmente el mismo en dos dimensiones que en una. El paso siguiente, sin embargo, es muy distinto. En el caso unidimensional, donde los modos normales son $e^{\pm ikx}$, solo hay dos modos con un valor dado de $\omega^2$. Así, sean cuales sean las condiciones de contorno, solo tenemos que preocuparnos de superponer dos modos a la vez. Pero en el caso bidimensional hay un número continuamente infinito de soluciones de (11.8) para cualquier $\omega$, porque se puede bajar $k_x$ y compensar subiendo $k_y$. Así, un modo normal del sistema bidimensional finito sin amortiguamiento (que no es más que alguna solución en la que todas las cuentas oscilan en fase con la misma $\omega$) puede ser una combinación lineal de un número infinito de los bonitos y sencillos modos del sistema infinito invariantes bajo traslación.

En efecto, en general el caso bidimensional es infinitamente más difícil. Si la figura 11.1 fuera un sistema con una forma más complicada, no seríamos capaces de encontrar una solución analítica. Pero para el caso especial de un marco rectangular alineado con las cuentas, las condiciones de contorno no son tan malas, porque tanto los modos (11.5) como las condiciones de contorno pueden expresarse de forma sencilla en términos de productos de modos normales unidimensionales.

Las condiciones de contorno del sistema de la figura 11.1 son

$$\psi(0, y, t) = \psi(L_H, y, t) = \psi(x, 0, t) = \psi(x, L_V, t) = 0,\qquad\text{(11.9)}$$

donde

$$L_H = 5a_H, \qquad L_V = 4a_V.\qquad\text{(11.10)}$$

En el sistema infinito correspondiente, del que se muestra un fragmento en la figura 11.2, (11.9) implica que las cuentas a lo largo del rectángulo punteado están todas en reposo. Comparando la figura 11.1 y la figura 11.2, puede verse que esta condición de contorno recoge la física de las paredes de la figura 11.1.

![Figura 11.2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.2.png)

Figura 11.2: un fragmento de una malla bidimensional infinita de cuentas.

Ahora, para hallar los modos normales del sistema finito de la figura 11.1, debemos encontrar combinaciones lineales de modos del sistema infinito que satisfagan las condiciones de contorno (11.9). Podemos satisfacer (11.9) formando combinaciones lineales de solo cuatro modos del sistema infinito,[1]

$$A\,e^{\pm ik_x x}e^{\pm ik_y y}\qquad\text{(11.11)}$$

donde

$$k_x = n\pi/L_H, \qquad k_y = n'\pi/L_V.\qquad\text{(11.12)}$$

Entonces podemos tomar las soluciones como un producto de senos,

$$\psi(x, y) = A\sin(n\pi x/L_H)\sin(n'\pi y/L_V)\qquad\text{(11.13)}$$

para $n = 1$ a 4 y $n' = 1$ a 3.

La frecuencia de cada modo viene dada por la relación de dispersión (11.8):

$$\omega^2 = \frac{4T_H}{m a_H}\sin^2\frac{n\pi a_H}{2L_H} + \frac{4T_V}{m a_V}\sin^2\frac{n'\pi a_V}{2L_V}.\qquad\text{(11.14)}$$

Estos modos están animados en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-11-1" rel="noopener" target="_blank" title="Animación original de Howard Georgi">11-1</a>.

La solución de este problema es un ejemplo de una técnica llamada «separación de variables». En las variables adecuadas —en este caso, $x$ e $y$— el problema se descompone en problemas unidimensionales. Este truco funciona igual de bien en el caso continuo, siempre que la superficie de contorno sea rectangular. Si tomamos el límite en el que $a_V$ y $a_H$ son muy pequeñas comparadas con las longitudes de onda de interés, podemos expresar (11.8) en términos de cantidades que tengan sentido en el límite continuo, igual que en el análisis de la cuerda unidimensional continua como límite de la cuerda con cuentas, en el capítulo 6. Supongamos, por simplicidad, que

$$a_V = a_H = a \qquad \text{y} \qquad T_V = T_H = T\qquad\text{(11.15)}$$

(de modo que las direcciones $x$ e $y$ tengan las mismas propiedades). Las cantidades que caracterizan la superficie en este caso son la densidad superficial de masa,

$$\rho_s = \frac{m}{a^2}\qquad\text{(11.16)}$$

y la tensión superficial,

$$T_s = \frac{T}{a}.\qquad\text{(11.17)}$$

La tensión superficial es la fuerza por unidad de distancia transversal que ejerce la membrana. Cuando estas cantidades permanecen finitas al hacer tender a cero la separación $a$, (11.8) se convierte en

$$\omega^2 = \frac{T_s}{\rho_s}\left(k_x^2 + k_y^2\right) = \frac{T_s}{\rho_s}\vec{k}^2.\qquad\text{(11.18)}$$

Un argumento precisamente análogo al del caso unidimensional muestra que, en este límite, $\psi(x, y, t)$ satisface la ecuación de ondas bidimensional,

$$\frac{\partial^2}{\partial t^2}\psi(x, y, t) = v^2\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}\right)\psi(x, y, t) = v^2\,\vec{\nabla}^2\psi(x, y, t).\qquad\text{(11.19)}$$

Nótese que, en este límite, las propiedades especiales de los ejes $x$ e $y$ que se manifestaban en el sistema finito han desaparecido por completo de la ecuación del movimiento. Los números de onda $k_x$ y $k_y$ forman un vector bidimensional $\vec{k}$. El número infinito de soluciones de la relación de dispersión (11.18) son simplemente las que se obtienen rotando $\vec{k}$ de todas las formas posibles sin cambiar su longitud. Esto hace posible resolver los modos normales en regiones circulares, por ejemplo. Pero no discutiremos ahora esas condiciones de contorno más complicadas. Está claro, sin embargo, que (11.13) es la solución para la región rectangular en el caso continuo, y que la frecuencia correspondiente es

$$\omega^2 = \frac{T_s}{\rho_s}\left[\left(\frac{n\pi}{L_H}\right)^2 + \left(\frac{n'\pi}{L_V}\right)^2\right].\qquad\text{(11.20)}$$

Ahora, como el sistema es continuo, los enteros $n$ y $n'$ van de cero a infinito (aunque $n = n' = 0$ no es interesante), o hasta que la aproximación continua deja de valer.

### 11.1.2 Tres dimensiones

La malla de cuentas no puede extenderse a tres dimensiones porque no hay dirección transversal. Pero un sistema de masas conectadas por varillas elásticas sí puede ser tridimensional y, de hecho, ese tipo de sistema es un buen modelo de un sólido elástico. Este sistema es bastante más complicado porque cada masa puede moverse en las tres direcciones. En la figura 11.3 se ilustra una versión bidimensional. Este sistema es igual que el de la figura 11.1, salvo que las cuerdas se han sustituido por varillas elásticas ligeras, de modo que el sistema está en equilibrio incluso sin el marco. Ahora nos interesan las oscilaciones de este sistema en el plano del papel. Comparado con la figura 11.1, este sistema tiene el doble de grados de libertad, porque cada bloque puede moverse tanto en la dirección $x$ como en la $y$, mientras que en la figura 11.1 los bloques solo se movían en la dirección $z$. Esto significa que no podemos usar la invariancia bajo traslación espacial por sí sola ni siquiera para determinar los modos del sistema infinito.

![Figura 11.3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.3.png)

Figura 11.3: un sólido bidimensional, con masas conectadas por varillas elásticas.

Para cada valor de $\vec{k}$ habrá cuatro modos en vez de los dos habituales. Tendríamos que hacer algún análisis matricial para ver qué combinaciones de movimiento en $x$ y en $y$ son realmente los modos normales. No lo haremos en general, pero lo discutiremos brevemente en el límite continuo, para recordarle algo de física que es importante en campos como la geología.

Considere el sistema continuo e infinito que se obtiene haciendo muy pequeñas las $a$ de la figura 11.3, escalando adecuadamente las demás cantidades. Considere una onda con número de onda $\vec{k}$. Los modos normales tendrán la forma

$$\vec{A}\,e^{i\vec{k}\cdot\vec{r} - i\omega t}\qquad\text{(11.21)}$$

para algún vector $\vec{A}$ (en el caso tridimensional, $\vec{A}$ es un 3-vector; en nuestro ejemplo bidimensional, es un 2-vector). Si el sistema es invariante bajo rotaciones, entonces la física no destaca ninguna dirección salvo la de $\vec{k}$. Entonces los modos normales deben ser un modo longitudinal o «de compresión»,

$$\vec{A} \propto \vec{k},\qquad\text{(11.22)}$$

y un modo transversal o «de cizalla»,

$$\vec{A}\cdot\vec{k} = 0.\qquad\text{(11.23)}$$

Cada modo tendrá su propia relación de dispersión característica. En tres dimensiones habrá dos modos de cizalla, porque hay dos direcciones perpendiculares, y tendrán la misma relación de dispersión, porque uno puede rotarse hasta convertirse en el otro.

![Figura 11.4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.4.png)

Figura 11.4: un sistema bidimensional de cuentas y muelles.

### 11.1.3 Ondas sonoras

En un líquido o un gas no hay ondas de cizalla, porque no hay ninguna fuerza restauradora que mantenga al sistema en una forma determinada. Los modos de cizalla tienen frecuencia cero. Si sustituyéramos las varillas de la figura 11.3 por muelles sin estirar, obtendríamos un sistema con esa misma propiedad, mostrado en la figura 11.4. Sin el marco, este sistema no sería rígido. Sin embargo, los modos de compresión siguen ahí. Son análogos a las ondas sonoras. Para un sistema aproximadamente continuo, como el aire, esperamos una relación de dispersión de la forma

$$\omega^2 = v^2\vec{k}^2\qquad\text{(11.24)}$$

donde $v$ es constante mientras $k$ no sea demasiado grande. Ya hemos calculado $v$, en (7.43), considerando oscilaciones unidimensionales. Se llama velocidad del sonido porque es la velocidad de las ondas sonoras en un sistema infinito o semiinfinito.

Podemos describir los modos normales de una caja rectangular llena de aire en términos de una función $P(x, y, z)$ que describe la presión del gas en el punto $(x, y, z)$. La presión o la densidad de la onda de compresión está relacionada con el desplazamiento $\vec{\psi}$ por

$$P \propto -\vec{\nabla}\cdot\vec{\psi}.\qquad\text{(11.25)}$$

Como en el sistema bidimensional descrito arriba, podemos usar separación de variables y hallar una solución que sea un producto de funciones de una sola variable. La única diferencia aquí es que las condiciones de contorno son distintas. Debido a (11.25), que es el enunciado matemático del hecho de que el gas es empujado de las regiones de presión alta a las de presión baja, el gradiente de presión perpendicular al contorno debe anularse: el gas del contorno no tiene a dónde ir. Así, los modos normales en una caja rectangular, $0 \leq x \leq X$, $0 \leq y \leq Y$, $0 \leq z \leq Z$, tienen la forma

$$P(x, y, z) = A\cos(n_x\pi x/X)\cos(n_y\pi y/Y)\cos(n_z\pi z/Z)\qquad\text{(11.26)}$$

con frecuencia

$$\omega = v\sqrt{\left(\frac{n_x\pi}{X}\right)^2 + \left(\frac{n_y\pi}{Y}\right)^2 + \left(\frac{n_z\pi}{Z}\right)^2}.\qquad\text{(11.27)}$$

La solución trivial $n_x = n_y = n_z = 0$ representa aire estacionario. Si alguna de las $n$ es no nula, el modo es no trivial.

## 11.2 Contornos planos

Las ondas viajeras más fáciles de discutir en dos y tres dimensiones son las «ondas planas», soluciones del sistema infinito de la forma

$$\psi(\vec{r}, t) = A\,e^{i(\vec{k}\cdot\vec{r} - \omega t)}.\qquad\text{(11.28)}$$

Esto describe una onda que viaja en la dirección del vector de número de onda $\vec{k}$, con la velocidad de fase del medio. El desplazamiento (o lo que sea) es constante sobre planos de $\vec{k}\cdot\vec{r}$ constante, que son perpendiculares a la dirección de movimiento, $\vec{k}$. Estudiaremos ondas viajeras más complicadas pronto, cuando discutamos la difracción. Entonces aprenderemos a describir «haces» de luz, de sonido o de otras ondas, que son las ondas viajeras con las que solemos trabajar, y veremos cómo describirlos como superposiciones de ondas planas. Por ahora, puede pensar en una onda plana como algo parecido a la onda viajera que encontraría dentro de un haz ancho y coherente, o muy lejos de una fuente pequeña de luz casi monocromática, luz de frecuencia definida. Con eso basta para hacerse una imagen física de los fenómenos que discutimos en esta sección.

Lo que más nos interesa son ondas como la luz y el sonido. Sin embargo, es mucho más fácil discutir las oscilaciones transversales de una membrana bidimensional, y muchos de nuestros ejemplos serán de ese sistema. Hay dos razones. Una es que una membrana bidimensional es más fácil de dibujar en un papel bidimensional. La otra es que la física es muy sencilla, así que podemos concentrarnos en las propiedades ondulatorias. Intentaremos señalar dónde se complican las cosas para otros tipos de fenómenos ondulatorios.

Considere dos membranas bidimensionales tensadas en el plano $z = 0$, como se muestra en la figura 11.5. Para $x < 0$, suponga que la densidad superficial de masa es $\rho_s$ y la tensión superficial $T_s$. Para $x > 0$, suponga que la densidad superficial de masa es $\rho_s'$ y la tensión superficial $T_s'$. Este es un análogo bidimensional del sistema de cuerdas que discutimos largamente en el capítulo 9. El contorno entre las dos membranas debe suministrar una fuerza (en este caso, una fuerza constante por unidad de longitud) en la dirección $x$ para sostener la diferencia de tensiones, como en el sistema de la figura 9.2. Sin embargo, supondremos que el mecanismo que suministra esa fuerza, sea cual sea, no tiene masa, no tiene fricción y es infinitamente flexible.

![Figura 11.5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.5.png)

Figura 11.5: una línea de fase constante en una onda plana que se acerca a un contorno.

Ahora, de nuevo, podemos considerar la reflexión de ondas viajeras. Supongamos que hay, en esta membrana, una onda plana de amplitud $A$ y número de onda $\vec{k}$ para $x < 0$, que viaja hacia el contorno en $x = 0$. La condición de que la onda viaje hacia el contorno puede escribirse en términos de las componentes de $\vec{k}$ como

$$k_x > 0.\qquad\text{(11.29)}$$

Nos gustaría saber qué ondas produce esta onda incidente por reflexión y transmisión en el contorno $x = 0$. Por razones generales de invariancia bajo traslación espacial, esperamos que la solución tenga la forma

$$\psi(\vec{r}, t) = A\,e^{i(\vec{k}\cdot\vec{r} - \omega t)} + \sum_\alpha R_\alpha A\,e^{i(\vec{k}_\alpha\cdot\vec{r} - \omega t)} \quad \text{para } x \leq 0$$

$$\psi(\vec{r}, t) = \sum_\beta \tau_\beta A\,e^{i(\vec{k}_\beta\cdot\vec{r} - \omega t)} \quad \text{para } x \geq 0\qquad\text{(11.30)}$$

con

$$\vec{k}_\alpha^2 = \frac{\omega^2\rho_s}{T_s}, \qquad \vec{k}_\beta^2 = \frac{\omega^2\rho_s'}{T_s'}\qquad\text{(11.31)}$$

y

$$k_{\alpha x} < 0 \quad \text{y} \quad k_{\beta x} > 0 \quad \text{para todo } \alpha \text{ y } \beta.\qquad\text{(11.32)}$$

Los índices $\alpha$ y $\beta$ de (11.30) recorren todas las ondas transmitidas y reflejadas. Mostraremos en breve que solo una de cada contribuye para una condición de contorno plana en $x = 0$, pero (11.30) es completamente general y se sigue únicamente de la invariancia bajo traslación espacial. Nótese que hemos incluido las condiciones de contorno en $\pm\infty$ exigiendo (11.29) y (11.32). Salvo la onda incidente de amplitud $A$, todas las demás ondas se alejan del contorno. Pero todavía no hemos impuesto la condición de contorno en $x = 0$.

### 11.2.1 La ley de Snell: el contorno invariante bajo traslación

Por lo que sabemos de la física en $\pm\infty$, las ondas reflejada y transmitida podrían ser una superposición complicada de un número infinito de ondas planas que se alejan del contorno en distintas direcciones. De hecho, si el contorno tuviera una forma irregular, eso es exactamente lo que esperaríamos. Es el hecho de que el contorno, $x = 0$, sea él mismo invariante bajo traslaciones espaciales en la dirección $y$ lo que nos permite reducir el número infinito de parámetros de (11.30) a solo dos. Como las traslaciones en la dirección $y$ dejan invariante todo el sistema, incluido el contorno, podemos hallar soluciones en las que todas las componentes tengan la misma dependencia irreducible en $y$. Si la onda incidente es proporcional a

$$e^{ik_y y},\qquad\text{(11.33)}$$

entonces todas las componentes de (11.30) deben ser también proporcionales a $e^{ik_y y}$. De lo contrario, no hay manera de satisfacer la condición de contorno en $x = 0$ para todo $y$. Eso significa que

$$k_{\alpha y} = k_y, \qquad k_{\beta y} = k_y.\qquad\text{(11.34)}$$

Pero (11.34), junto con (11.31) y (11.32), determina completamente los vectores de onda $\vec{k}_\alpha$ y $\vec{k}_\beta$. Entonces (11.30) se convierte en[2]

$$\psi(\vec{r}, t) = A\,e^{i\vec{k}\cdot\vec{r} - i\omega t} + R\,A\,e^{i\tilde{\vec{k}}\cdot\vec{r} - i\omega t} \equiv \psi_-(\vec{r}, t) \quad \text{para } x \leq 0$$

$$\psi(\vec{r}, t) = \tau\,A\,e^{i\vec{k}'\cdot\vec{r} - i\omega t} \equiv \psi_+(\vec{r}, t) \quad \text{para } x \geq 0\qquad\text{(11.35)}$$

donde

$$\tilde{k}_y = k_y, \qquad k'_y = k_y,\qquad\text{(11.36)}$$

y

$$\tilde{k}_x = -\sqrt{\omega^2/v^2 - k_y^2} = -k_x, \qquad k'_x = \sqrt{\omega^2/v'^2 - k_y^2},\qquad\text{(11.37)}$$

con

$$v = \sqrt{\frac{T_s}{\rho_s}}, \qquad v' = \sqrt{\frac{T_s'}{\rho_s'}}.$$

Lo entretenido de (11.35)-(11.37) es que sabemos todo sobre las direcciones de las ondas reflejada y transmitida sin haber mencionado siquiera los detalles de la física del contorno. Para obtener las direcciones solo hemos necesitado la invariancia bajo traslaciones en la dirección $y$. Los detalles de la física del contorno solo entran cuando queremos calcular $R$ y $\tau$. Las direcciones de las ondas reflejada y transmitida son las mismas para cualquier sistema con un contorno invariante bajo traslación. Evidentemente, este argumento funciona también en tres dimensiones. De hecho, si simplemente elegimos las coordenadas de modo que el contorno sea el plano $x = 0$ y la onda viaje en el plano $x$-$y$, entonces nada depende de la coordenada $z$ y el análisis es exactamente el mismo que arriba. Podemos, por ejemplo, aplicar estos argumentos directamente a las ondas electromagnéticas. Para las ondas electromagnéticas en un medio transparente, como la velocidad de fase es $v_\varphi = \omega/k$, el índice de refracción, $n$, es proporcional a $k$:

$$n = \frac{c}{v_\varphi} = \frac{ck}{\omega}.\qquad\text{(11.39)}$$

(11.36)-(11.37) muestran que la onda reflejada sale con el mismo ángulo que la incidente, porque la única diferencia entre los vectores $\vec{k}$ de la onda incidente y la reflejada es un cambio de signo de la componente $x$. Así, el ángulo de incidencia es igual al ángulo de reflexión: es la regla de la «reflexión especular». De (11.36) podemos deducir también la ley de refracción de Snell para el ángulo de la onda refractada. Si $\theta$ es el ángulo que forma la onda incidente con la perpendicular al contorno, y $\theta'$ es el ángulo correspondiente de la onda transmitida, entonces (11.36) implica

$$k\sin\theta = k'\sin\theta'.\qquad\text{(11.40)}$$

Para ondas electromagnéticas, podemos reescribir esto como

$$n\sin\theta = n'\sin\theta'.\qquad\text{(11.41)}$$

Por ejemplo, cuando una onda electromagnética que viaja por el aire encuentra una superficie plana de vidrio con un ángulo $\theta$, se cumple $n' > n$ en (11.41): la onda se refracta acercándose a la perpendicular a la superficie. Esto se ilustra en la figura 11.6 para $n' > n$.

![Figura 11.6](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.6.png)

Figura 11.6: reflexión y transmisión en un contorno.

Terminemos ahora la solución del problema de la membrana resolviendo para $R$ y $\tau$ en (11.35). Para ello debemos discutir por fin las condiciones de contorno con más detalle. Una es que la membrana es continua, lo que, dada la forma (11.35), implica

$$\psi_-(\vec{r}, t)\big|_{x=0} = \psi_+(\vec{r}, t)\big|_{x=0},\qquad\text{(11.42)}$$

o sea,

$$1 + R = \tau.\qquad\text{(11.43)}$$

La otra es que la fuerza vertical sobre cualquier trocito de la membrana es nula. La fuerza sobre un trocito de longitud $d\ell$ del contorno en el punto $(0, y, 0)$, ejercida por la membrana con $x < 0$, viene dada por

$$-T_s\,d\ell\left.\frac{\partial\psi_-(\vec{r}, t)}{\partial x}\right|_{x=0}.\qquad\text{(11.44)}$$

Esto es análogo al ejemplo unidimensional ilustrado en la figura 8.6. La fuerza de tensión superficial es perpendicular al contorno, así que, para desplazamientos pequeños, solo importa la pendiente del desplazamiento en la dirección $x$. La pendiente en la dirección $y$ no contribuye a la fuerza vertical a primer orden en el desplazamiento. Análogamente, la fuerza sobre un trocito de longitud $d\ell$ del contorno en el punto $(0, y, 0)$, ejercida por la membrana con $x > 0$, viene dada por

$$T_s'\,d\ell\left.\frac{\partial\psi_+(\vec{r}, t)}{\partial x}\right|_{x=0}.\qquad\text{(11.45)}$$

Así, la otra condición de contorno es

$$T_s'\left.\frac{\partial\psi_+(\vec{r}, t)}{\partial x}\right|_{x=0} = T_s\left.\frac{\partial\psi_-(\vec{r}, t)}{\partial x}\right|_{x=0},\qquad\text{(11.46)}$$

o sea,

$$T_s'\,k'_x\,\tau = T_s\,k_x\,(1 - R).\qquad\text{(11.47)}$$

Así, la solución es

$$\tau = \frac{2}{1 + r}, \qquad R = \frac{1 - r}{1 + r}\qquad\text{(11.48)}$$

donde

$$r = \frac{T_s'\,k'_x}{T_s\,k_x}.\qquad\text{(11.49)}$$

De (11.48) y (11.49) puede verse que podemos ajustar la tensión superficial para que la onda reflejada desaparezca, incluso cuando hay un cambio en la longitud del vector $\vec{k}$ de un lado a otro del contorno. Conviene pensar en la refracción en este límite, porque permite visualizarla de forma sencilla. Si $r = 1$ en (11.48), entonces $R = 0$ y $\tau = 1$: no hay onda reflejada y la transmitida tiene la misma amplitud que la incidente. Así, en cada región hay una única onda plana. Recuerde que una onda plana consiste en líneas infinitas de fase constante perpendiculares al vector $\vec{k}$, que se mueven en la dirección de $\vec{k}$ con la velocidad de fase $v_\varphi = \omega/|\vec{k}|$. En particular, fijémonos en las líneas donde la fase es cero, de modo que $\psi = A$. La distancia perpendicular entre dos de esas líneas es la longitud de onda, $2\pi/|\vec{k}|$, porque la diferencia de fase entre líneas vecinas es $2\pi$. Pero he aquí la clave: las líneas de las dos regiones deben encontrarse en el contorno, $x = 0$, para satisfacer la condición de contorno (11.43). Si la amplitud de la onda incidente es 1 en $x = 0$, la de la onda saliente también es 1. Las líneas donde $\psi = A$ son continuas a través del contorno $x = 0$. Esta situación se ilustra en la figura 11.7, donde se muestran los vectores $\vec{k}$ de las dos regiones. Nótese que el ángulo de las líneas debe cambiar cuando cambia la distancia entre ellas, para mantener la continuidad en el contorno. En el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-11-2" rel="noopener" target="_blank" title="Animación original de Howard Georgi">11-2</a> se muestra el mismo sistema en movimiento.

![Figura 11.7](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.7.png)

Figura 11.7: líneas de $\psi = 1$ constante para un sistema con refracción pero sin reflexión.

### 11.2.2 Prismas

El índice de refracción no trivial del vidrio es el ladrillo con que se construyen muchos elementos ópticos. Discutamos el prisma. En realidad, resolver del todo correctamente el problema de la dispersión de ondas luminosas por prismas requeriría técnicas mucho más sofisticadas de las que tenemos ahora a nuestra disposición. La razón es que el prisma no es una superficie plana e infinita con invariancia bajo traslación espacial; en general, tendríamos que preocuparnos del contorno. Sin embargo, podemos decir cosas interesantes incluso ignorando esta complicación. La idea es pensar no en una onda plana infinita, sino en un haz ancho de luz que incide sobre una cara del prisma. Un haz ancho se comporta de forma muy parecida a una onda plana, e ignoraremos la diferencia en este capítulo. Veremos cuáles son las diferencias en el capítulo 13, cuando discutamos la difracción.

Consideremos, pues, la siguiente situación, en la que un haz ancho de luz entra por una cara de un prisma de índice de refracción $n$ y sale por la otra. La geometría se muestra en la figura 11.8 (las direcciones de los haces se indican con las líneas gruesas). La cantidad interesante es $\delta$, que describe cuánto ha desviado el prisma la dirección del haz saliente respecto de la del incidente. Podemos calcularla con geometría sencilla y la ley de Snell, (11.40). De la ley de Snell,

$$\sin\theta_{in} = n\sin\theta_1, \qquad \sin\theta_{out} = n\sin\theta_2.\qquad\text{(11.50)}$$

![Figura 11.8](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.8.png)

Figura 11.8: la geometría de un prisma.

Y ahora, algo de geometría:

$$\theta_2 + \theta_1 = \phi'\qquad\text{(11.52)}$$

—porque el complemento de $\phi'$, es decir $\pi - \phi'$, junto con $\theta_1$ y $\theta_2$ son los ángulos de un triángulo y, por tanto, suman $\pi$—, y

$$\phi = \phi'\qquad\text{(11.53)}$$

—porque $\phi$ y $\phi'$ son ángulos correspondientes de los dos triángulos rectángulos semejantes cuyo otro ángulo agudo es $\gamma$. Así,

$$\delta = \xi_1 + \xi_2 = \theta_{in} + \theta_{out} - \theta_1 - \theta_2 = \theta_{in} + \theta_{out} - \phi\qquad\text{(11.54)}$$

donde hemos usado (11.52) y (11.53). Pero, para ángulos pequeños, de (11.50) y (11.51),

$$\theta_{in} \approx n\,\theta_1, \qquad \theta_{out} \approx n\,\theta_2.\qquad\text{(11.55)}$$

Así,

$$\delta \approx n(\theta_1 + \theta_2) - \phi \approx (n - 1)\,\phi.\qquad\text{(11.56)}$$

El resultado (11.56) es sin duda razonable. Debe anularse cuando $n \to 1$, porque para $n = 1$ no hay contorno. Y si las cosas son pequeñas y la respuesta es lineal, debe ser proporcional a $\phi$.

Una de las características más familiares de un prisma es consecuencia de la dependencia del índice de refracción, $n$, con la frecuencia. Eso hace que un haz de luz blanca se descomponga en colores. Para la mayoría de los materiales, el índice de refracción aumenta con la frecuencia, de modo que la luz azul se desvía más que la roja. La física de la dependencia de $n$ con la frecuencia es la de la oscilación forzada. El índice de refracción de un material está relacionado con la constante dieléctrica (véase (9.53)), que a su vez está relacionada con la distorsión de la estructura electrónica del material causada por el campo eléctrico. Para un campo variable, esto depende de la amplitud del movimiento de las cargas ligadas dentro del material en un campo eléctrico. Como esas cargas están ligadas, responden a los campos oscilantes de una onda electromagnética como una masa en un muelle sometida a una fuerza oscilante. Sabemos, de nuestro estudio de la oscilación forzada, que esa amplitud tiene la forma

$$\sum_{\text{resonancias }\alpha}\frac{C_\alpha}{\omega_\alpha^2 - \omega^2},\qquad\text{(11.57)}$$

donde $\omega_\alpha$ son las frecuencias de resonancia del sistema y las $C_\alpha$ son constantes que dependen de los detalles de cómo actúa la fuerza sobre los grados de libertad.

Podemos estimar el orden de magnitud de estas frecuencias de resonancia por análisis dimensional, recordando que cualquier material consta de electrones y núcleos unidos por fuerzas eléctricas (y por la mecánica cuántica, claro, aunque $\hbar$ no entrará en nuestra estimación salvo implícitamente, en la distancia atómica típica). Las cantidades relevantes son:[3]

| Magnitud                 | Valor                               |
|--------------------------|-------------------------------------|
| Carga del protón         | $e \approx 1.6\times10^{-19}$ C     |
| Masa del electrón        | $m_e \approx 9.11\times10^{-31}$ kg |
| Distancia atómica típica | $a \approx 10^{-10}$ m = 1 Å        |
| Velocidad de la luz      | $c = 299\,792\,458$ m/s             |

En términos de estos parámetros, cabe suponer que la fuerza típica dentro de los materiales es del orden de $\dfrac{e^2}{4\pi\varepsilon_0 a^2}$ (por la ley de Coulomb) y, por tanto, que la constante del muelle es del orden de $\dfrac{e^2}{4\pi\varepsilon_0 a^3}$ (la fuerza típica dividida por la distancia típica). Así, esperamos

$$\omega_\alpha \approx \sqrt{\frac{e^2}{4\pi\varepsilon_0 a^3 m_e}}\qquad\text{(11.58)}$$

y

$$\lambda_\alpha \approx \frac{2\pi c}{\omega_\alpha} \approx 2\pi c\sqrt{\frac{4\pi\varepsilon_0 a^3 m_e}{e^2}} \approx 10^{-7}\ \text{m} = 1000\ \text{Å}.\qquad\text{(11.59)}$$

Esta es una longitud de onda en la región ultravioleta del espectro electromagnético, más corta que la de la luz visible. Eso significa que, para la luz visible, $\omega < \omega_\alpha$ y, por tanto, el desplazamiento (11.57) aumenta al aumentar $\omega$ dentro del visible. La distorsión de la estructura electrónica del material causada por un campo eléctrico variable aumenta con la frecuencia en el espectro visible. Así, la constante dieléctrica del material aumenta con la frecuencia y, en consecuencia, la luz azul se desvía más.

Dicho sea de paso, esta es la misma razón por la que el cielo es azul: la luz azul se dispersa más que la roja porque su frecuencia está más cerca de las resonancias importantes de las moléculas del aire.

### 11.2.3 Reflexión total interna

La situación en la que la onda viene de una región de $|\vec{k}|$ grande a una región de $|\vec{k}|$ menor tiene otra característica sorprendente y muy útil. Esta situación se representa en la figura 11.9 para un sistema sin reflexión. Para $\theta$ pequeña, como se muestra en la figura 11.9, esto se parece bastante a la figura 11.7, salvo que la onda se refracta alejándose de la perpendicular a la superficie en vez de acercarse a ella. Pero suponga que el ángulo $\theta$ es grande y satisface

$$n\sin\theta/n' > 1.\qquad\text{(11.60)}$$

![Figura 11.9](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.9.png)

Figura 11.9: líneas de $\psi = 1$ constante para $n' < n$.

Entonces no hay solución con $\theta'$ real en (11.41). Así pues, no puede haber onda viajera transmitida: la onda incidente debe ser totalmente reflejada por el contorno. Esto es la reflexión total interna. Ocurre cuando una onda plana intenta escapar de una región de $|\vec{k}|$ alto a una región de $|\vec{k}|$ menor con un ángulo rasante. Se usa mucho en equipos ópticos y en muchas otras cosas. Investiguemos este curioso fenómeno con más detalle.

Suponga que partimos de $\theta = 0$ y aumentamos $\theta$. Al aumentar $\theta$, $k_y$ aumenta y $k_x$ disminuye. Esto continúa hasta llegar a la frontera de la reflexión total interna, llamada ángulo crítico,

$$\sin\theta = \sin\theta_c \equiv \frac{n'}{n}.\qquad\text{(11.61)}$$

Las amplitudes de las ondas reflejada y transmitida de (11.48) también aumentan. En el ángulo crítico, $k'_x$ se anula: la amplitud de la onda reflejada es 1 y la de la transmitida es 2. Sin embargo, aunque la onda transmitida es no nula, no se lleva energía del contorno, porque el vector $\vec{k}$ apunta en la dirección $y$.

Al aumentar $\theta$ más allá del ángulo crítico, $k_y$ sigue creciendo. Para satisfacer la relación de dispersión,

$$\frac{\omega^2}{v'^2} = k_x'^2 + k_y^2,\qquad\text{(11.62)}$$

¡$k'_x$ debe ser imaginario puro! La dependencia en $x$ es entonces proporcional a

$$e^{-\kappa x} \qquad \text{donde } \kappa = \operatorname{Im}k'_x.\qquad\text{(11.63)}$$

Ahora cambia la naturaleza de la condición de contorno en el infinito. Ya no podemos exigir simplemente que $k'_x > 0$. En su lugar, debemos exigir

$$\operatorname{Im}k'_x > 0.\qquad\text{(11.64)}$$

El signo es importante. Si $\operatorname{Im}k'_x$ fuera negativa, la amplitud de la onda para $x > 0$ crecería con $x$, yendo exponencialmente a infinito cuando $x \to \infty$. Eso no tiene mucho sentido físico, porque corresponde a una causa finita (la onda incidente para $x < 0$) produciendo un efecto infinito. Como veremos más abajo, también podemos llegar a esta conclusión tomando este sistema infinito como límite de un sistema finito.

En realidad tenemos tres condiciones de contorno distintas en el infinito para esta situación:

$$\operatorname{Re}k'_x > 0 \ \text{para } \theta < \theta_c, \qquad k'_x = 0 \ \text{para } \theta = \theta_c, \qquad \operatorname{Im}k'_x > 0 \ \text{para } \theta > \theta_c.\qquad\text{(11.66)}$$

Estas tres pueden combinarse en una condición compuesta válida en todos los regímenes:

$$\operatorname{Re}k'_x \geq 0, \qquad \operatorname{Im}k'_x \geq 0.\qquad\text{(11.67)}$$

La condición (11.67) es en realidad el enunciado más general de la condición de contorno de onda viajera saliente en el infinito. Es correcta también en situaciones en las que hay amortiguamiento y tanto la parte real como la imaginaria de $k'_x$ son no nulas. Es el enunciado matemático del hecho físico de que la onda para $x > 0$, sea cual sea su forma, la produce en el contorno la onda incidente.

De (11.48) y (11.49) se ve que, para $\theta > \theta_c$, la amplitud de la onda reflejada se vuelve compleja. Sin embargo, su valor absoluto sigue siendo 1: toda la energía de la onda incidente se refleja.

Hemos visto que, en la reflexión total interna, la onda sí penetra en la región prohibida, pero la dependencia en $x$ tiene la forma de una onda estacionaria exponencial, no de una onda viajera. La dependencia en $y$ es la de una onda viajera. Esta es una de las muchas situaciones en las que la física obliga a que la solución bidimensional o tridimensional tenga propiedades distintas en direcciones distintas.

Es fácil ver la reflexión total interna en un acuario, un bloque de vidrio u otro objeto transparente rectangular con índice de refracción bastante mayor que 1. Puede mirar a través de una cara del rectángulo y ver el reflejo plateado desde una cara adyacente, como se ilustra en la figura 11.10.

![Figura 11.10](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.10.png)

Figura 11.10: reflexión total interna en vidrio de índice de refracción 2.

### 11.2.4 Efecto túnel

Considere la dispersión de una onda plana en el sistema ilustrado en la figura 11.11. Es el mismo montaje que en la figura 11.10, salvo que se ha añadido otro bloque de vidrio a una distancia pequeña, $d$, por debajo del contorno en el que había reflexión total interna. Hemos definido la dirección $x$ positiva hacia abajo por coherencia con la discusión de la ley de Snell de más arriba. ¿Llega ahora algo de luz al observador de abajo, o la luz sigue reflejándose totalmente en el contorno, como en la figura 11.10? La respuesta es que algo de luz pasa. Como veremos en detalle en un ejemplo más abajo, la presencia del otro bloque de vidrio significa que, en vez de una condición de contorno en el infinito, tenemos una condición de contorno a la distancia finita $d$.

![Figura 11.11](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.11.png)

Figura 11.11: un experimento sencillo para demostrar el efecto túnel.

Los detalles de este fenómeno para ondas electromagnéticas se complican algo por la polarización, que discutiremos en detalle en el capítulo siguiente. Sin embargo, hay un proceso precisamente análogo en la oscilación transversal de membranas que podemos analizar con facilidad. De hecho, veremos que ya lo hemos analizado en el capítulo 9.

Considere el problema de dispersión ilustrado en la figura 11.12. La región sin sombrear es una membrana de densidad menor. Las flechas indican las direcciones de los vectores $\vec{k}$ de las ondas planas. Las regiones sombreadas tienen densidad superficial de masa $\rho_s$ y tensión superficial $T_s$. La región sin sombrear, que va de $x = 0$ a $x = d$, tiene la misma tensión superficial pero densidad superficial de masa $\rho_s/4$. Así, la razón entre las velocidades de fase de las dos regiones es dos, la misma que la razón entre el aire y el vidrio en la figura 11.11. Las líneas discontinuas son contornos sin masa entre las distintas membranas.

![Figura 11.12](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.12.png)

Figura 11.12: efecto túnel en una membrana infinita.

Podemos preguntarnos ahora cuáles son los coeficientes $R$ y $\tau$ de reflexión y transmisión. Hemos hecho este problema para un solo contorno antes en este capítulo, en (11.42)-(11.49). Podríamos resolver este juntando dos de esas soluciones con las técnicas de matriz de transferencia del capítulo 9. De hecho, ni siquiera tenemos que hacer eso, porque podemos leer el resultado de (9.97) y (9.98), en la discusión de las películas delgadas del capítulo 9. La cuestión es que todos los términos de nuestra solución deben tener la misma dependencia irreducible en $y$, $e^{ik_y y}$, por la invariancia bajo traslación espacial de todo el sistema, incluido el contorno, en la dirección $y$. Ese factor común no juega ningún papel en las condiciones de contorno. Si lo sacamos factor común, lo que queda parece un problema de dispersión unidimensional. Comparando (11.47) para $T_s = T_s'$ con (9.10), se ve que los análisis coinciden si hacemos los reemplazos

$$k_1 \to k_x, \qquad k_2 \to k'_x, \qquad L \to d\qquad\text{(11.68)}$$

donde $k_x$ es la componente $x$ del vector $\vec{k}$ de la onda incidente en la región sombreada y $k'_x$ es la componente $x$ del vector $\vec{k}$ de la onda transmitida en la región sin sombrear. El resultado es

$$\tau = \left(\cos k'_x d - i\,\frac{k_x^2 + k_x'^2}{2k_x k'_x}\sin k'_x d\right)^{-1}e^{-ik_x d}\qquad\text{(11.69)}$$

y

$$R = \left(i\,\frac{k_x'^2 - k_x^2}{2k_x k'_x}\sin k'_x d\right)\left(\cos k'_x d - i\,\frac{k_x^2 + k_x'^2}{2k_x k'_x}\sin k'_x d\right)^{-1}.\qquad\text{(11.70)}$$

Puede ser un poco más fácil mirar la intensidad de la onda transmitida, que es proporcional a

$$|\tau|^2 = \frac{4k_x^2 k_x'^2}{\left(k_x^4 + k_x'^4\right)\sin^2 k'_x d + 2k_x^2 k_x'^2}.\qquad\text{(11.71)}$$

Nótese que no hemos mencionado el ángulo crítico, ni la reflexión total interna, ni nada por el estilo. La razón es que nuestro análisis del capítulo 9 era perfectamente general. Sigue siendo correcto incluso si el número de onda angular de la región intermedia se vuelve imaginario. Todo lo que ocurre para $\theta$ mayor que el ángulo crítico, $\theta_c$, es que $k'_x$ se vuelve imaginario. Pero eso tiene un efecto espectacular en (11.71). Si $k'_x \to i\kappa$, con $\kappa$ real, se sigue de la identidad de Euler, (1.57) y (1.62), que

$$\sin k'_x d \to i\sinh\kappa d,\qquad\text{(11.72)}$$

donde $\sinh$ es el «seno hiperbólico», definido por

$$\sinh x \equiv \frac{e^x - e^{-x}}{2}.\qquad\text{(11.73)}$$

Así, para ángulos por encima del crítico, el denominador de (11.71) es una función exponencialmente creciente de $d$ (el término $e^{\kappa d}$ de (11.73) domina para $\kappa d$ grande). La intensidad de la onda transmitida decrece, por tanto, exponencialmente con $d$. En el límite de $d$ grande recuperamos rápidamente la reflexión total interna.

Podemos entender algo mejor lo que ocurre mirando las condiciones de contorno en $x = d$ para ángulos por encima del crítico. Para $x > d$, la onda tiene la forma (suprimiendo los factores comunes $e^{ik_y y}$ y $A e^{-i\omega t}$)

$$\tau\,e^{ik_x x}.\qquad\text{(11.74)}$$

Para $0 \leq x \leq d$, la onda tiene la forma

$$T_{II}\,e^{-\kappa x} + R_{II}\,e^{\kappa x},\qquad\text{(11.75)}$$

donde he llamado a los coeficientes $T_{II}$ y $R_{II}$ por analogía con las ondas transmitida y reflejada, aunque no son ondas viajeras. Las condiciones de contorno en $x = d$ son

$$\tau\,e^{ik_x d} = T_{II}\,e^{-\kappa d} + R_{II}\,e^{\kappa d}, \qquad ik_x\,\tau\,e^{ik_x d} = \kappa\left(-T_{II}\,e^{-\kappa d} + R_{II}\,e^{\kappa d}\right).\qquad\text{(11.76)}$$

Esto parece más complicado de lo que es. Si despejamos $T_{II}e^{-\kappa d}$ y $R_{II}e^{\kappa d}$ en términos de $\tau e^{ik_x d}$, el resultado es

$$T_{II}\,e^{-\kappa d} = \frac{\kappa - ik_x}{2\kappa}\,\tau\,e^{ik_x d}, \qquad R_{II}\,e^{\kappa d} = \frac{\kappa + ik_x}{2\kappa}\,\tau\,e^{ik_x d}.$$

Lo importante es que los valores de las dos componentes de la onda (11.75) en $x = d$, es decir, $T_{II}e^{-\kappa d}$ y $R_{II}e^{\kappa d}$, son más o menos del mismo tamaño. Estas dos cantidades no tienen ninguna dependencia exponencial en $d$. Este hecho cualitativo no depende de los detalles de (11.76): será cierto para cualquier condición de contorno razonable en $x = d$.

Así pues, el coeficiente $R_{II}$ de la onda «reflejada» (entre comillas, porque es una onda exponencial real, no una onda viajera) debe ser menor que la «transmitida» en un factor de aproximadamente $e^{2\kappa d}$. Nótese que esto justifica el enunciado (11.67) de la condición de contorno en el infinito. Cuando $d \to \infty$, para cualquier física razonable en $d$, la onda se convierte en una exponencial negativa pura.

En $x = 0$, para $\kappa d$ grande, el término $R_{II}$ de la onda será completamente despreciable, y el término $T_{II}$ se producirá con algún coeficiente del orden de 1, igual que en el límite de reflexión total interna.

Así, lo que ocurre en las condiciones de contorno del efecto túnel puede describirse cualitativamente así: la onda incidente para $x < 0$ produce el término $e^{-\kappa x}$ en la región $0 \leq x \leq d$, con una mezcla exponencialmente pequeña de $e^{\kappa x}$. Pero en $x = d$ las dos partes de la onda exponencial son del mismo tamaño (ambas exponencialmente pequeñas), y pueden producir la onda transmitida.

La rápida dependencia exponencial de la onda transmitida con $d$ tiene consecuencias interesantes. Implica, por ejemplo, que la onda reflejada es también muy sensible al valor de $d$ para $d$ pequeña (la conservación de la energía implica $|R|^2 + |\tau|^2 = 1$). Puede ver esta rápida dependencia en el ejemplo de la figura 11.10 poniendo el dedo sobre la superficie inferior del bloque de vidrio o del acuario, donde la onda se está reflejando. ¡Verá una huella dactilar fantasmal! La razón es que las minúsculas hendiduras de su dedo están lo bastante lejos del vidrio como para que $\kappa d$ sea grande y la onda se refleje casi por completo. Pero donde la carne se aprieta firmemente contra el vidrio, la onda se absorbe. Es una versión sencilla de un microscopio de efecto túnel.

Por último, antes de dejar el tema del efecto túnel, consideremos qué ocurre cuando bajamos la intensidad de la onda luminosa de la figura 11.11 hasta ver la dispersión de fotones individuales. Lo primero que hay que notar es que cada fotón o bien se transmite o bien se refleja. El significado de $R$ y $\tau$ en este caso es que $|R|^2$ y $|\tau|^2$ son las probabilidades de reflexión y transmisión. No se puede predecir si un fotón concreto pasará. En el mundo mecanocuántico solo se pueden predecir probabilidades.

Lo segundo que hay que notar es que, en la descripción de partículas, todo el fenómeno del efecto túnel es muy peculiar. Un fotón clásico que llegara al contorno de la placa de vidrio con más del ángulo crítico no podría entrar en absoluto en el aire: se lo impedirían la conservación de la energía y la conservación de la componente $y$ del momento.[4] ¿Cómo puede la partícula llegar al lado $x > d$ si no puede existir para $0 < x < d$? Evidentemente, en física clásica no puede. El efecto túnel es, por tanto, un fenómeno genuinamente mecanocuántico. La onda consigue penetrar en la región prohibida, pero solo en forma de onda exponencial real, no de onda viajera. Solo para $x < 0$ y $x > d$, donde las ondas son viajeras, pueden interpretarse como partículas en algo parecido al sentido clásico.

## 11.3 Placas de Chladni

Las placas de Chladni son un ejemplo muy bonito e instructivo de sistema oscilante bidimensional. Una placa de Chladni no es más que una placa metálica cuadrada que se excita transversalmente en su centro. Se ilustra en la figura 11.13. El punto del centro muestra dónde se excita la placa en la dirección transversal (fuera del plano del papel). El centro, cuya posición de equilibrio tomaremos como $\vec{r} = 0$, se mueve arriba y abajo fuera del plano del papel con frecuencia $\omega$. Supongamos que el cuadrado está en el plano $x$-$y$ y tiene lado $2L$, y llamemos al desplazamiento transversal (en la dirección $z$)

$$\psi(x, y, t) \qquad \text{para } |x|, |y| \leq L.\qquad\text{(11.78)}$$

![Figura 11.13](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.13.png)

Figura 11.13: una placa de Chladni.

En principio, este es un problema de oscilación forzada. Podríamos tomar como condición de contorno en el origen

$$\psi(0, 0, t) = A\cos\omega t\qquad\text{(11.79)}$$

e intentar hallar $\psi$ en todas partes.

Para hallar $\psi$ debemos conocer la condición de contorno en los bordes de la placa. Eso depende de los detalles de la física de la placa, porque hay varias maneras en que la placa puede deformarse en respuesta a la fuerza impulsora. Por simplicidad, supondremos que la deformación dominante es la cizalla, ilustrada en la figura 11.14. Para este tipo de desplazamiento, y para evitar una aceleración infinita, la pendiente de la placa debe anularse en el contorno en la dirección perpendicular al contorno, o sea, en lenguaje matemático,

$$\hat{n}\cdot\vec{\nabla}\psi = 0\qquad\text{(11.80)}$$

en el borde, donde $\hat{n}$ es un vector unitario en el plano perpendicular al borde. En este caso,

$$\left.\frac{\partial}{\partial x}\psi(x, y, t)\right|_{x=|L|} = \left.\frac{\partial}{\partial y}\psi(x, y, t)\right|_{y=|L|} = 0.\qquad\text{(11.81)}$$

![Figura 11.14](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.14.png)

Figura 11.14: cizalla.

Aunque el caso general es más complicado que esto, usaremos (11.81) como ilustración. Lo instructivo de las placas de Chladni, como veremos, no es lo que ocurre en los bordes, ¡sino lo que ocurre en el medio!

No es fácil escribir la solución general de este problema de oscilación forzada. Sin embargo, nos interesan sobre todo las resonancias. Son los modos de oscilación libre de la placa (sujetos a la condición de contorno (11.81)) que pueden ser excitados por la fuerza impulsora, es decir, los modos que tienen valores no nulos del desplazamiento en el origen.

Los modos de oscilación libre relevantes de la placa tienen la forma[5]

$$\psi_{(n_x, n_y)}(x, y, t) = A\cos\frac{n_x\pi x}{L}\cos\frac{n_y\pi y}{L}\cos\omega t\qquad\text{(11.82)}$$

con

$$\omega^2 = \omega_0^2(\vec{k}^2) \implies \omega^2 = f(n_x^2 + n_y^2).\qquad\text{(11.83)}$$

Si las frecuencias de estos modos fueran únicas, (11.82) sería toda la historia. Pero lo interesante de este sistema es que la simetría garantiza que hay degeneración: si $n_x \neq n_y$, hay dos modos con la misma frecuencia. Obtenemos un modo físicamente equivalente intercambiando $n_x \leftrightarrow n_y$, porque eso corresponde simplemente a una rotación de 90° de la placa, ¡que no cambia la física en absoluto! Cuando hay modos degenerados, las combinaciones lineales de ellos son también modos, como se muestra en (3.117). Así que tenemos que preguntarnos qué combinaciones lineales excita la fuerza impulsora. Otra forma de decir esto se resume en (11.83): la invariancia bajo rotaciones asegura que $\omega^2$ depende solo de $n_x^2 + n_y^2$. En particular, está claro que la diferencia

$$\psi^-_{(n_x, n_y)}(x, y, t) = A\left(\cos\frac{n_x\pi x}{L}\cos\frac{n_y\pi y}{L} - \cos\frac{n_y\pi x}{L}\cos\frac{n_x\pi y}{L}\right)\cos\omega t\qquad\text{(11.84)}$$

se anula en el origen. ¡Solo la suma se acopla a la fuerza impulsora!

$$\psi^+_{(n_x, n_y)}(x, y, t) = A\left(\cos\frac{n_x\pi x}{L}\cos\frac{n_y\pi y}{L} + \cos\frac{n_y\pi x}{L}\cos\frac{n_x\pi y}{L}\right)\cos\omega t\qquad\text{(11.85)}$$

Estos son los modos resonantes de una placa de Chladni.

Una razón por la que esto resulta divertido es que es fácil de ver. Si se excita la placa y se espolvorea arena sobre ella, la arena se acumula en las regiones donde la placa no se mueve, a lo largo de los nodos de desplazamiento donde $\psi = 0$. Así obtenemos una imagen visual de los ceros de $\psi$.

Miremos algunos de estos modos (en orden de frecuencia creciente) para ver qué esperar. El modo $\psi^+_{(0,0)}$ no es interesante: corresponde a toda la placa subiendo y bajando en bloque. Obviamente, la frecuencia correspondiente es 0, porque no hay fuerza restauradora.

El primer modo interesante es

$$\psi^+_{(1,0)}(x, y, t) = A\left(\cos\frac{\pi x}{L} + \cos\frac{\pi y}{L}\right)\cos\omega t.$$

Este se anula para $y = \pm L \pm x$, de modo que el patrón de arena de Chladni tiene el aspecto del diagrama de la figura 11.15.

![Figura 11.15](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.15.png)

Figura 11.15: el patrón de Chladni del modo $(n_x, n_y) = (1, 0)$.

El modo siguiente es

$$\psi^+_{(1,1)}(x, y, t) = 2A\cos\frac{\pi x}{L}\cos\frac{\pi y}{L}\cos\omega t.$$

Como este modo no es degenerado, no da lugar a un patrón muy interesante. Se anula en $x = \pm L/2$ e $y = \pm L/2$, lo que da el patrón mostrado en la figura 11.16. No consideraremos más de estos modos aburridos con $n_x = n_y$.

![Figura 11.16](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.16.png)

Figura 11.16: el patrón de Chladni del modo (1,1).

El siguiente modo es

$$\psi^+_{(2,0)}(x, y, t) = A\left(\cos\frac{2\pi x}{L} + \cos\frac{2\pi y}{L}\right)\cos\omega t,$$

que se anula para $y = \pm L/2 \pm x$ o $y = \pm 3L/2 \pm x$, de modo que el patrón tiene el aspecto de la figura 11.17.

![Figura 11.17](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.17.png)

Figura 11.17: el patrón de Chladni del modo (2,0).

A continuación viene

$$\psi^+_{(2,1)}(x, y, t) = A\left(\cos\frac{\pi x}{L}\cos\frac{2\pi y}{L} + \cos\frac{2\pi x}{L}\cos\frac{\pi y}{L}\right)\cos\omega t.$$

Este se anula para

$$c_x(2c_y^2 - 1) + c_y(2c_x^2 - 1) = (c_x + c_y)(2c_xc_y - 1) = 0$$

con $c_x \equiv \cos(\pi x/L)$ y $c_y \equiv \cos(\pi y/L)$. El patrón se muestra en la figura 11.18.

![Figura 11.18](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.18.png)

Figura 11.18: el patrón de Chladni del modo (2,1).

Podríamos seguir, pero a estas alturas ya debería tener la idea. Veamos un último modo:

$$\psi^+_{(3,1)}(x, y, t) = A\left(\cos\frac{\pi x}{L}\cos\frac{3\pi y}{L} + \cos\frac{3\pi x}{L}\cos\frac{\pi y}{L}\right)\cos\omega t,$$

que se anula para

$$c_x(4c_y^3 - 3c_y) + c_y(4c_x^3 - 3c_x) = c_xc_y(4c_x^2 + 4c_y^2 - 6) = 0$$

con el patrón mostrado en la figura 11.19.

![Figura 11.19](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.19.png)

Figura 11.19: el patrón de Chladni del modo (3,1).

**Moraleja:** cuando hay más de un modo con la misma frecuencia, ¡mire las combinaciones lineales para determinar cuáles se excitan!

## 11.4 Guías de onda

En general, una «guía de ondas» es un dispositivo que obliga a una onda viajera a propagarse solo por donde uno quiere. Típicamente, una guía de ondas es algún tipo de tubo que permite a la perturbación ondulatoria propagarse en una dirección mientras la confina en las otras. En esta sección discutiremos el caso de guías de onda rectas con secciones transversales uniformes sencillas. La física realmente interesante ocurre cuando la anchura de la guía no es mucho mayor que la longitud de onda. Entonces, como veremos, la física de la guía tiene un efecto espectacular sobre la propagación de la onda.

La situación más sencilla de discutir es la de las oscilaciones transversales de una membrana en forma de banda infinita, como se muestra en la figura 11.20. Considere una membrana con densidad superficial de masa $\rho_s$ y tensión superficial $T_s$, tensada en una banda infinita en el plano $x$-$y$ entre $y = 0$ e $y = \ell$, y desde $x = -\infty$ hasta $\infty$. Los bordes, en $y = 0$ e $y = \ell$, se mantienen fijos en el plano. Nos interesan las oscilaciones del interior de la banda hacia arriba y hacia abajo, fuera del plano.

![Figura 11.20](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.20.png)

Figura 11.20: una sección de una banda infinita de membrana tensada que actúa como guía de ondas.

Este es un trabajo para la separación de variables. Podemos buscar modos de este sistema que sean productos de una función de $x$ por una función de $y$. En particular, podemos satisfacer la condición de contorno en $y = 0$ combinando dos modos del sistema infinito,

$$e^{ik_x x}e^{ik_y y} \quad \text{y} \quad e^{ik_x x}e^{-ik_y y},\qquad\text{(11.96)}$$

para formar

$$\sin(k_y y)\,e^{ik_x x}.\qquad\text{(11.97)}$$

Esto satisface la condición de contorno en $y = \ell$ si

$$k_y = \frac{n\pi}{\ell} \qquad \text{para } n = 1\text{ a }\infty.\qquad\text{(11.98)}$$

Así, los modos tienen este aspecto:

$$\psi_n^+(x, y, t) = A\sin\frac{n\pi y}{\ell}\,e^{i(k_x x - \omega t)}\qquad\text{(11.99)}$$

y

$$\psi_n^-(x, y, t) = A\sin\frac{n\pi y}{\ell}\,e^{i(-k_x x - \omega t)}.\qquad\text{(11.100)}$$

Para cada valor de $n$, ¡estos parecen ondas que viajan en la dirección $\pm x$!

La relación de dispersión de la membrana viene dada por (11.18). Pero los modos $\psi_n^\pm$ tienen $|k_y| = n\pi/\ell$. Así, la relación de dispersión de las ondas viajeras (11.99) y (11.100) es

$$\omega^2 = v^2 k_x^2 + \omega_n^2,\qquad\text{(11.101)}$$

donde

$$v = \sqrt{\frac{T_s}{\rho_s}}\qquad\text{(11.102)}$$

y

$$\omega_n = \frac{n\pi v}{\ell}.\qquad\text{(11.103)}$$

Algo interesante de (11.101) es que la relación de dispersión tiene una frecuencia de corte inferior que depende de $n$. Para un $\omega$ dado, los únicos modos que se propagan realmente son el número finito de modos con

$$n < \frac{\omega\ell}{\pi v}.\qquad\text{(11.104)}$$

Por ejemplo, para $\omega \leq \pi v/\ell$ no hay ondas viajeras. Para $\pi v/\ell < \omega \leq 2\pi v/\ell$ solo hay una, la correspondiente a $n = 1$, etc.

Los modos que satisfacen (11.104) tienen una interpretación física sencilla. Pueden pensarse como las ondas planas (11.96) del sistema infinito rebotando de un lado a otro entre los bordes fijos, $y = 0$ e $y = \ell$. El requisito (11.98) sobre los valores permitidos de $k_y$ surge porque, para otros valores de $k_y$, las ondas reflejadas se desfasan y dan interferencia destructiva. Cabría esperar que una onda en zigzag de este tipo se propagara en la dirección $x$ con una velocidad menor que la velocidad de fase, $v$, de las ondas del sistema infinito, en un factor de

$$\frac{k_x}{\sqrt{k_x^2 + k_y^2}} = \frac{k_x}{\sqrt{k_x^2 + (\omega_n/v)^2}},\qquad\text{(11.105)}$$

porque tiene que recorrer esa distancia de más al rebotar para avanzar una distancia dada en $x$, como se ilustra en la figura 11.21. De hecho, la velocidad de fase de las ondas en zigzag para $n$ fijo, $\omega/k_x$, es en realidad **mayor** que $v$ por el factor (11.105), en vez de menor:

$$v_{n\varphi} = \frac{\omega}{k_x} = v\,\frac{\sqrt{k_x^2 + (\omega_n/v)^2}}{k_x}.\qquad\text{(11.106)}$$

![Figura 11.21](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.21.png)

Figura 11.21: una onda en zigzag en la guía de ondas.

Sin embargo, la velocidad de grupo, $\partial\omega/\partial k_x$, de las ondas en zigzag —la velocidad a la que realmente se pueden enviar señales— es menor justamente por el factor esperado:

$$v_{gn} = \frac{\partial\omega}{\partial k_x} = v\,\frac{k_x}{\sqrt{k_x^2 + (\omega_n/v)^2}}.\qquad\text{(11.107)}$$

Para ondas luminosas podemos hacer una guía de ondas construyendo un tubo de algún material conductor, de modo que el campo eléctrico sea no nulo solo dentro del tubo. Sin embargo, en ese caso los detalles de las condiciones de contorno en los bordes dependen de la dirección del campo eléctrico. Volveremos a una cuestión relacionada en el capítulo siguiente.

## 11.5 Agua

El agua es una sustancia bastante complicada. Moja las cosas. Tiene viscosidad. Forma remolinos y torbellinos y tiene movimientos turbulentos no lineales que no podemos aspirar a entender con las técnicas de que disponemos. En esta sección consideramos un fluido algo idealizado, que llamaremos «agua seca» (siguiendo a Feynman), que no tiene nada de esa estructura complicada. Tiene tres características que mantendremos en común con la de verdad: tiene densidad de masa, tiene tensión superficial y es casi incompresible. Veamos cómo ondula.

Imagine un universo infinito lleno de un líquido incompresible y sin fricción. Esto nos permitirá ver las consecuencias de la incompresibilidad de forma sencilla y cualitativa. Considere el análogo de una onda sonora plana en un sistema así. Es decir, por ejemplo, una onda plana que viaja en la dirección $x$ (con $k_y = k_z = 0$) con desplazamientos longitudinales en la dirección $x$. Si el líquido es verdaderamente incompresible, $k_x$ debe ser cero para esta onda, porque cualquier desplazamiento longitudinal debe ir acompañado de compresiones y enrarecimientos del medio. Así, para una onda plana así, $\vec{k} = 0$: ¡no hay ondas planas no triviales en el sistema infinito!

En general, no esperamos que todas las componentes del vector $\vec{k}$ tengan que anularse, porque incluso en un líquido incompresible el desplazamiento en una dirección está permitido si va acompañado del movimiento adecuado en otras direcciones. Pero lo que hemos visto es que no podemos tener un modo con un vector $\vec{k}$ real. Eso sería una onda plana, que hemos visto que no es compatible con la incompresibilidad. En su lugar, esperamos que la restricción $k_x = 0$ se sustituya por una restricción sobre la longitud, invariante bajo rotaciones, del vector $k$: que $\vec{k}\cdot\vec{k} = 0$. Si algunas de las componentes del vector $\vec{k}$ son imaginarias, esto puede satisfacerse con $\vec{k}$ no nulo.

Nótese que la condición $\vec{k}\cdot\vec{k} = 0$ no es exactamente una relación de dispersión, porque no hace referencia alguna a la frecuencia. Pero es toda la historia para un sistema infinito de fluido incompresible. De hecho, está claro que no hay ondas armónicas en el sistema infinito, porque no hay nada que produzca una fuerza restauradora. Incluso si hay un campo gravitatorio, la presión del líquido se ajusta para cancelar el efecto de la gravedad. Solo podemos obtener una relación de dispersión no trivial cuando hay una superficie. La relación de dispersión depende entonces de la física de la superficie. Esto parecería violar nuestro principio general de que la relación de dispersión es una propiedad del sistema infinito. Lo que ocurre es esto: la relación $\vec{k}\cdot\vec{k} = 0$ es realmente la única relación de dispersión que tiene algún sentido para el sistema infinito tridimensional. Cuando introducimos una superficie, hemos roto la invariancia bajo traslación en la dirección normal a la superficie. Eso nos permite obtener una relación de dispersión no trivial para el sistema bidimensional paralelo a la superficie.

### 11.5.1 Matemáticas de las ondas en el agua

Intentemos ahora hacer cuantitativas estas consideraciones. Como de costumbre, etiquetaremos nuestro fluido por las posiciones de equilibrio de sus partes. Llamemos entonces al desplazamiento respecto del equilibrio del fluido que está en el punto $\vec{r}$ en equilibrio

$$\varepsilon\,\vec{\psi}(\vec{r}, t)$$

para algún $\varepsilon$ pequeño. Esto significa que la posición real del agua es[6]

$$\vec{R}(\vec{r}, t) = \vec{r} + \varepsilon\,\vec{\psi}(\vec{r}, t).\qquad\text{(11.109)}$$

Podemos considerar (11.109) como una especie de cambio de coordenadas. Nos lleva de las coordenadas de equilibrio (una etiqueta más bien arbitraria, porque el agua es libre de fluir) a las coordenadas físicas, que nos dicen dónde está realmente el agua. Si el agua es incompresible, lo cual es una aproximación bastante buena, un elemento de volumen pequeño debe tener el mismo volumen en equilibrio y en las coordenadas físicas:

$$dR_x\,dR_y\,dR_z = dx\,dy\,dz.\qquad\text{(11.110)}$$

Esto se cumplirá si el determinante de la matriz jacobiana vale 1:

$$\det\begin{pmatrix} \frac{\partial R_x}{\partial x} & \frac{\partial R_x}{\partial y} & \frac{\partial R_x}{\partial z} \\ \frac{\partial R_y}{\partial x} & \frac{\partial R_y}{\partial y} & \frac{\partial R_y}{\partial z} \\ \frac{\partial R_z}{\partial x} & \frac{\partial R_z}{\partial y} & \frac{\partial R_z}{\partial z} \end{pmatrix} = 1.\qquad\text{(11.111)}$$

Como $\varepsilon$ es pequeño, podemos desarrollar (11.111) a orden más bajo en $\varepsilon$, con el resultado

$$1 + \varepsilon\,\vec{\nabla}\cdot\vec{\psi} + O(\varepsilon^2) = 1.\qquad\text{(11.112)}$$

Así,

$$\vec{\nabla}\cdot\vec{\psi} = 0.\qquad\text{(11.113)}$$

(11.113) es muy razonable: es el enunciado de que el flujo de desplazamiento hacia dentro o hacia fuera de cualquier región se anula.[7] Esto es lo que esperábamos de nuestra discusión cualitativa.

Para ver qué significa esto para las ondas, supongamos además que no hay remolinos. El enunciado matemático de esto es

$$\vec{\nabla}\times\vec{\psi} = 0.\qquad\text{(11.114)}$$

Si no suponemos (11.114), la conservación del momento angular se vuelve importante y la vida se complica muchísimo. Tendrá que esperar a cursos de dinámica de fluidos para aprender más sobre ello. Con la simplificación (11.114), el desplazamiento puede escribirse como el gradiente de una función escalar, $\chi$:

$$\varepsilon\,\vec{\psi} = \vec{\nabla}\chi.\qquad\text{(11.115)}$$

Esto simplifica enormemente la vida, porque ahora podemos trabajar con la cantidad escalar $\chi$. La invariancia bajo traslación espacial nos dice que podemos hallar modos de la forma

$$\chi = e^{i\vec{k}\cdot\vec{r} - i\omega t},\qquad\text{(11.116)}$$

lo que da un desplazamiento de la forma

$$\varepsilon\,\vec{\psi} = i\,\vec{k}\,e^{i\vec{k}\cdot\vec{r} - i\omega t}.\qquad\text{(11.117)}$$

La condición (11.113) se convierte entonces en

$$\vec{k}\cdot\vec{k} = 0,\qquad\text{(11.118)}$$

como anticipamos en la discusión cualitativa del principio de la sección.

### 11.5.2 Profundidad

Consideremos ahora ondas en un «océano» de profundidad $L$, ignorando las fuerzas de fricción, los remolinos y las no linealidades. Restringiremos además nuestra atención a una situación bidimensional. Sea $y$ la dirección vertical y consideremos ondas en el agua en la dirección $x$. Es decir, tomaremos $k_x$ real, porque nos interesa la propagación de ondas en la dirección $x$, y $k_y$ imaginario puro con la misma magnitud, de modo que se satisfaga (11.118). Suponemos entonces que nada depende de la otra coordenada, $z$. Habiendo simplificado tanto las cosas, podemos suponer también que nuestro océano es una caja rectangular. Entonces los modos de interés del sistema infinito tienen el aspecto

$$\chi_\infty(x, y, t) = e^{\pm ikx \pm ky - i\omega t}.\qquad\text{(11.119)}$$

Si el océano tiene un fondo en $y = 0$, entonces el desplazamiento vertical debe anularse en $y = 0$. Entonces (11.115) implica que debemos combinar modos del sistema infinito para obtener una $\chi$ cuya derivada respecto de $y$ se anule en $y = 0$:

$$\chi(x, y, t) \propto e^{\pm ikx - i\omega t}\cosh ky,\qquad\text{(11.120)}$$

donde $\cosh$ es el «coseno hiperbólico», definido por

$$\cosh x \equiv \frac{e^x + e^{-x}}{2}.\qquad\text{(11.121)}$$

Entonces, de (11.115), obtenemos

$$\psi_x(x, y, t) = \frac{\partial}{\partial x}\chi(x, y, t) = \pm i\,e^{\pm ikx - i\omega t}\cosh ky,$$

$$\psi_y(x, y, t) = \frac{\partial}{\partial y}\chi(x, y, t) = e^{\pm ikx - i\omega t}\sinh ky.\qquad\text{(11.122)}$$

Antes de seguir, nótese que podríamos extender estas consideraciones añadiendo una coordenada $z$. Entonces (11.120) se convertiría en

$$\chi(x, y, z, t) \propto e^{(\pm ik_x x \pm ik_z z) - i\omega t}\cosh ky$$

donde

$$k = \sqrt{k_x^2 + k_z^2}.$$

Estos son los modos ondulatorios bidimensionales del océano infinito de profundidad $L$. La dependencia en $y$ queda completamente fijada por la condición de contorno en el fondo y por la condición $\vec{k}\cdot\vec{k} = 0$. Lo único interesante, desde el punto de vista de la invariancia bajo traslación espacial, es la dependencia en $x$ y $z$.

Volvamos ahora al océano rectangular y a los modos independientes de $z$, (11.122). Si nuestro océano tiene lados en $x = 0$ y $x = X$, debemos elegir combinaciones lineales de los modos (11.122) tales que el desplazamiento en $x$ se anule en los lados. Podemos hacerlo para $x = 0$ formando las combinaciones

$$\psi_x(x, y, t) = -\sin kx\,\cosh ky\,\cos\omega t, \qquad \psi_y(x, y, t) = \cos kx\,\sinh ky\,\cos\omega t.\qquad\text{(11.125)}$$

Entonces, si

$$k = \frac{n\pi}{X},\qquad\text{(11.126)}$$

la condición de contorno en $x = X$ también se satisface.

![Figura 11.22](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.22.png)

Figura 11.22: el movimiento de un fluido incompresible en una onda.

Ya conocemos las matemáticas del desplazamiento del agua seca. Antes de pasar a discutir la relación de dispersión, detengámonos a considerar qué aspecto tiene esto realmente. Imagine que colocamos en el agua una cuadrícula rectangular regular de puntos en equilibrio. Entonces, en la figura 11.22 mostramos qué aspecto tiene la cuadrícula en el modo (11.125) con $n = 1$. Cada uno de los pequeños rectángulos de la figura 11.22 era un cuadrado en la posición de equilibrio (cuando $\psi = 0$). Nótese cómo funciona la incompresibilidad: cuando el agua se comprime en una dirección, se estira en la otra. Puede verlo en movimiento en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-11-3" rel="noopener" target="_blank" title="Animación original de Howard Georgi">11-3</a>.

Habiendo mirado esto, podemos olvidarlo un rato y concentrarnos solo en la superficie: eso es lo que importa para la relación de dispersión. Para facilitar la presentación en los diagramas siguientes, exageraremos el desplazamiento en la dirección vertical $y$ y olvidaremos el desplazamiento de la superficie en la dirección $x$ (que de todos modos no importará). Entonces la onda tiene el aspecto de la figura 11.23.

![Figura 11.23](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.23.png)

Figura 11.23: la superficie de una onda en el agua, con el desplazamiento horizontal suprimido.

Usaremos argumentos energéticos para obtener la relación de dispersión. Hay tres contribuciones a la energía total de la onda estacionaria (11.125): la energía potencial gravitatoria, la energía almacenada en la tensión superficial y la energía cinética. Consideremos cada una por turno.

#### Potencial gravitatorio

En el diagrama de la figura 11.24 puede verse que el efecto global de los desplazamientos en el modo (11.125) es tomar un trozo de agua de $X - x$, elevarlo $\varepsilon\psi_y(x, L, t)$ (el desplazamiento vertical de la superficie) y llevarlo a $x$. El volumen de ese trozo es $W\,dx\,\varepsilon\psi_y(x, L, t)$, donde $dx$ es la longitud del trozo y $W$ es la anchura en la dirección $z$ (hacia dentro del papel). Así, el potencial gravitatorio total es

$$V_{\text{grav}} = \rho g\int dV\,\Delta h = \rho g W\int_0^{\pi/2k} dx\,|\varepsilon\psi_y(x, L, t)|^2 + O(\varepsilon^3)$$

$$= \rho g W\int_0^{\pi/2k} dx\,\varepsilon^2\cos^2 kx\,\sinh^2 kL\,\cos^2\omega t + \cdots = \frac{\pi}{4k}\rho g W\varepsilon^2\sinh^2 kL\,\cos^2\omega t + \cdots.\qquad\text{(11.127)}$$

![Figura 11.24](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.24.png)

Figura 11.24: se retira agua del rectángulo en $X - x$ y se eleva hasta el rectángulo en $x$.

#### Tensión superficial

La energía almacenada en la tensión superficial es $W$ multiplicada por la diferencia entre la longitud de la superficie y la longitud de equilibrio ($X$). Esto exige que tengamos algo de cuidado con la posición de la superficie, volviendo a (11.109). La posición de la superficie es

$$R_x(x, t) = x + \varepsilon\psi_x(x, L, t), \qquad R_y(x, t) = \varepsilon\psi_y(x, L, t).\qquad\text{(11.128)}$$

La longitud es entonces

$$\int_0^X dx\sqrt{\left(\frac{\partial R_x}{\partial x}\right)^2 + \left(\frac{\partial R_y}{\partial x}\right)^2}.\qquad\text{(11.129)}$$

Pero

$$\frac{\partial R_x}{\partial x} = 1 + \varepsilon\frac{\partial\psi_x}{\partial x}, \qquad \frac{\partial R_y}{\partial x} = \varepsilon\frac{\partial\psi_y}{\partial x}.\qquad\text{(11.130)}$$

Así,

$$V_{\text{sup}} = T\times(\text{Área} - \text{Área}_0) = T W\int_0^{\pi/k} dx\left(\sqrt{(1 + \varepsilon\partial\psi_x/\partial x)^2 + (\varepsilon\partial\psi_y/\partial x)^2} - 1\right)$$

$$= T W\int_0^{\pi/k} dx\left(\varepsilon\frac{\partial\psi_x}{\partial x} + \frac{1}{2}\left(\varepsilon\frac{\partial\psi_y}{\partial x}\right)^2 + O(\varepsilon^3)\right).\qquad\text{(11.131)}$$

El término de orden $\varepsilon$ de (11.131) se cancela al integrar en $x$, de modo que

$$V_{\text{sup}} = \frac{1}{2}T W\varepsilon^2 k^2\int_0^{\pi/k} dx\,\sin^2 kx\,\sinh^2 kL\,\cos^2\omega t + \cdots = \frac{\pi}{4k}T W\varepsilon^2 k^2\sinh^2 kL\,\cos^2\omega t + \cdots.\qquad\text{(11.132)}$$

#### Energía cinética

La energía cinética se obtiene integrando $\frac{1}{2}mv^2$ sobre todo el volumen del líquido:

$$KE = \frac{\rho}{2}\int dV\,\vec{v}^2 = \frac{\rho W}{2}\int_0^{\pi/k} dx\int_0^L dy\left[(\varepsilon\partial\psi_x/\partial t)^2 + (\varepsilon\partial\psi_y/\partial t)^2\right]$$

$$= \frac{\rho W\varepsilon^2}{2}\int_0^{\pi/k} dx\int_0^L dy\,\omega^2\sin^2\omega t\left[\cos^2 kx\,\sinh^2 ky + \sin^2 kx\,\cosh^2 ky\right]$$

$$= \frac{\pi}{4k}\rho W\varepsilon^2\int_0^L dy\,\omega^2\sin^2\omega t\,\cosh 2ky = \frac{\pi}{8k^2}\rho W\varepsilon^2\omega^2\sinh 2kL\,\sin^2\omega t.\qquad\text{(11.135)}$$

#### Relación de dispersión

El total de (11.127)-(11.135) es

$$\begin{aligned}
V_{\text{grav}} + V_{\text{sup}} + KE = {} & \frac{\pi}{4k}\rho g W\varepsilon^2\sinh^2 kL\,\cos^2\omega t\\
& + \frac{\pi}{4k}T W\varepsilon^2 k^2\sinh^2 kL\,\cos^2\omega t\\
& + \frac{\pi}{8k^2}\rho W\omega^2\varepsilon^2\sinh 2kL\,\sin^2\omega t + \cdots.\qquad\text{(11.136)}
\end{aligned}$$

Esto debe ser constante en el tiempo, lo que implica

$$\omega^2 = \frac{2\sinh^2 kL\left(gk + \frac{T}{\rho}k^3\right)}{\sinh 2kL} = \left(gk + \frac{T}{\rho}k^3\right)\tanh kL,\qquad\text{(11.137)}$$

donde $\tanh$ es la «tangente hiperbólica», definida por

$$\tanh x \equiv \frac{\sinh x}{\cosh x} = \frac{e^x - e^{-x}}{e^x + e^{-x}}.\qquad\text{(11.138)}$$

Nótese que, en el doble límite de longitud de onda larga y agua poco profunda, las ondas en el agua se vuelven no dispersivas: para $kL \ll 1$ y $\rho g k \gg T k^3$, $\tanh kL \to kL$ y

$$\omega^2 \approx gL\,k^2.\qquad\text{(11.139)}$$

#### Gravedad frente a tensión superficial

La relación de dispersión (11.137) implica una competición entre la gravedad y la tensión superficial. Para longitudes de onda largas domina la gravedad y el término $gk$ es el más importante. Para longitudes de onda cortas domina la tensión superficial y el término $Tk^3/\rho$ es el más importante. El cruce ocurre para números de onda del orden de

$$k_0 = \sqrt{\frac{\rho g}{T}}.\qquad\text{(11.140)}$$

La longitud de onda de cruce es en realidad una distancia familiar. Hay un proceso mucho más familiar que implica una competición similar entre gravedad y tensión superficial. Considere una gota de agua sobre una superficie de baja fricción, como una sartén de teflón. Una gota muy pequeña es casi esférica. Pero al aumentar el tamaño de la gota, empieza a aplanarse. Y cuando la gota crece por encima de un tamaño crítico, la altura de la gota deja de aumentar: se extiende con una altura fija, $h$, como se muestra en sección en la figura 11.25.

![Figura 11.25](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.25.png)

Figura 11.25: sección de una gota de agua sobre una superficie sin fricción.

Como con la relación de dispersión, podemos entender lo que ocurre considerando la energía. La energía total de la gota es la suma de la energía potencial gravitatoria y la energía debida a la tensión superficial:

$$V_{\text{grav}} \approx \rho\,g\,h\,v,\qquad\text{(11.141)}$$

donde $v$ es el volumen de la gota, y

$$V_{\text{sup}} \approx \frac{T v}{h}.\qquad\text{(11.142)}$$

El volumen es fijo, así que el valor de equilibrio de $h$ minimiza la suma

$$V_{\text{grav}} + V_{\text{sup}} \approx \rho g h v + \frac{T v}{h}.\qquad\text{(11.143)}$$

El mínimo ocurre para

$$T \approx \rho\,g\,h^2.\qquad\text{(11.144)}$$

La tensión superficial medida del agua es $T \approx 72$ dinas/cm. Esto da la altura familiar de una gota de agua, $h \approx 0.4$ cm. Esta altura está relacionada con $k_0$ por

$$h \approx \sqrt{\frac{T}{\rho g}} = \frac{1}{k_0}.\qquad\text{(11.145)}$$

## 11.6 Lentes y óptica geométrica

### Óptica geométrica

La idea de la óptica geométrica es entender los efectos de la refracción y la reflexión sobre haces de luz, ignorando los efectos de la difracción. En realidad, esto es solo la ley de Snell y geometría. Una aplicación de estas ideas será la discusión del arcoíris en la sección siguiente. Allí usaremos lo que se llama «trazado de rayos», que, como su nombre indica, consiste simplemente en seguir la pista de lo que hace cada rayo de luz al atravesar la gota. Una gota esférica es una «lente gruesa»: evidentemente, no tiene sentido considerar «delgada» una esfera. En esta sección vamos a ver cómo dar una descripción aproximada más sencilla de lo que hace una «lente delgada». De hecho, si estuviéramos diseñando un instrumento óptico de mucha precisión, seguiríamos usando el trazado de rayos para afinar los detalles. Pero el análisis de lente delgada es un buen punto de partida aproximado y nos ayudará a entender lo que ocurre en algunas situaciones importantes.

Técnicamente, lo que significa «delgada» en este contexto es que, si un haz estrecho de luz aproximadamente perpendicular al plano de la lente entra en la lente por algún punto de un lado, sale más o menos por el mismo punto del otro lado. Si ignoramos el pequeño cambio de posición, esto simplifica el análisis y nos da la fórmula de la lente delgada.

### Lentes esféricas delgadas

Antes en este capítulo dedujimos la fórmula del cambio angular de un haz estrecho de luz (estamos ignorando la difracción) debido a un prisma. El análisis usa la construcción geométrica de la figura 11.26 y da

$$\delta = \theta_{in} + \theta_{out} - \theta_1 - \theta_2 \approx n(\theta_1 + \theta_2) - \phi \approx (n - 1)\phi\qquad\text{(11.146)}$$

donde la primera igualdad es exacta y la segunda se sigue en el límite en que los ángulos $\theta$ son pequeños. En ese límite, la desviación angular es independiente del ángulo de entrada.

![Figura 11.26](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.26.png)

Figura 11.26: la geometría del prisma, de nuevo.

### Lentes delgadas y ángulos pequeños

Podemos usar este resultado para entender cómo enfoca la luz una lente. Una lente es un dispositivo en el que el cambio angular que se da al haz es proporcional a la distancia al eje, para ángulos y distancias pequeños:

$$\delta \approx h/f\qquad\text{(11.147)}$$

donde $f$ es una longitud. Esto es aproximadamente cierto para un trozo de vidrio con superficies que son partes de esferas. En la figura 11.27 hay un diagrama que muestra cómo funciona esto para una lente que es plana por un lado y una porción de esfera de radio $r_1$ por el otro. En el diagrama, $\theta_1$ es el ángulo del «prisma efectivo» que ve la parte del haz que está a distancia $h$ del eje. Debería quedar claro por la figura que, si $\theta_1$ es pequeño, es proporcional a $h$:

$$\theta_1 \approx \sin\theta_1 = \frac{h}{r_1}.\qquad\text{(11.148)}$$

![Figura 11.27](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.27.png)

Figura 11.27: lente plana por un lado y esférica de radio $r_1$ por el otro.

Más a menudo, la lente es curva por ambos lados. Si los radios son $r_1$ y $r_2$, el resultado tiene el aspecto de la figura 11.28. La figura 11.28 muestra el haz justo en la punta de la lente por comodidad pero, como debería dejar claro el diagrama anterior, $\theta_1 + \theta_2$ es el ángulo del «prisma efectivo» para cualquier $h$. La figura exagera también la curvatura de los dos lados, de modo que la lente dibujada no es realmente «delgada»: una lente delgada de verdad tiene las caras mucho menos curvadas. Esto es importante porque, si la lente es gruesa, la altura $h$ no está muy bien definida: si la luz dentro de la lente no es horizontal, podríamos tener una $h$ donde la luz entra en la lente y una $h$ muy distinta donde sale. Pero si la lente es delgada y los rayos no están muy lejos de la perpendicular, esta ambigüedad en $h$ puede ignorarse igual que las demás correcciones a las relaciones de ángulos pequeños (como $\sin\theta \approx \theta$).

![Figura 11.28](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.28.png)

Figura 11.28: lente curva por ambos lados, con radios $r_1$ y $r_2$.

Juntando la geometría de la figura 11.28 con la fórmula de $\delta$ para un prisma, obtenemos la constante $f$ para una lente esférica delgada:

$$\delta = (n - 1)(\theta_1 + \theta_2) = (n - 1)\left(\frac{h}{r_1} + \frac{h}{r_2}\right) = \frac{h}{f}\qquad\text{(11.149)}$$

y, por tanto,

$$\frac{1}{f} = (n - 1)\left(\frac{1}{r_1} + \frac{1}{r_2}\right).\qquad\text{(11.150)}$$

Esta es la llamada «fórmula del fabricante de lentes».

Una lente de este tipo enfoca los rayos paralelos de luz, como se muestra en la figura 11.30. Esto funciona porque $\delta \approx h/f$, como se muestra en la figura 11.31. Los rayos paralelos con cualquier ángulo se enfocan sobre un «plano focal» a una distancia $f$ de la lente, como se muestra en la figura 11.32. La manera analítica de explicar cómo funciona esto es notar que la diferencia entre las pendientes de los rayos a ambos lados de la lente es proporcional a la altura. Así, en este caso, como las pendientes de un lado son las mismas, la diferencia de pendientes del otro lado es proporcional a la diferencia de alturas, y eso significa que todos convergen en la misma $x$.

![Figura 11.30](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.30.png)

Figura 11.30: una lente enfoca rayos paralelos.

![Figura 11.31](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.31.png)

Figura 11.31: la desviación es proporcional a la altura.

![Figura 11.32](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.32.png)

Figura 11.32: rayos paralelos con cualquier ángulo se enfocan sobre el plano focal.

Otra forma de ver que este enfoque debe funcionar se ilustra en las figuras 11.33 y 11.34. Nótese que, si los rayos paralelos llegan con un ángulo $\delta_i$, el rayo que está a una distancia $h_i = \delta_i f$ por encima del centro de la lente se desvía hasta la horizontal, como se muestra en la figura 11.33 con la línea continua. Entonces, para los rayos a ambos lados de ese (mostrados con líneas discontinuas), como la dependencia de la desviación con la altura en la lente es lineal, la desviación angular total, $\delta_i + \delta_o$, es $1/f$ multiplicada por la distancia total al centro, $h_i + h_o$; pero entonces $h_o = \delta_o f$, que es la condición de enfoque. Esto se ilustra en la figura 11.34.

![Figura 11.33](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.33.png)

Figura 11.33: el rayo a la altura $h_i = \delta_i f$ se desvía hasta la horizontal.

![Figura 11.34](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.34.png)

Figura 11.34: la condición de enfoque.

Para un haz de rayos paralelos con cualquier ángulo, puede determinar dónde inciden en el plano focal trazando cualquier rayo; el más fácil es el que pasa por el centro de la lente, que no se desvía en absoluto, como se muestra en la figura 11.35. Los rayos paralelos (una parte de una onda plana; sabemos que eso es imposible, pero estamos ignorando la difracción) pueden pensarse como procedentes de una fuente puntual en el infinito. Si hay una fuente puntual más cerca de la lente, esta enfoca más lejos. Ahora juegue con la animación LENS.EXE.

![Figura 11.35](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.35.png)

Figura 11.35: el rayo que pasa por el centro de la lente no se desvía.

![Figura 11.36](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.36.png)

Figura 11.36: una fuente puntual a distancia $d_1$ se enfoca a distancia $d_2$.

Para hallar la relación entre $d_1$ y $d_2$, considere el diagrama de la figura 11.37: la suma de los ángulos de desviación a ambos lados es igual a $\delta$:

$$\delta_1 + \delta_2 = \delta,$$

lo que, para ángulos pequeños, equivale a

$$\frac{h}{d_1} + \frac{h}{d_2} = \frac{h}{f}$$

o

$$\frac{1}{d_1} + \frac{1}{d_2} = \frac{1}{f}.\qquad\text{(11.153)}$$

Esta es la llamada «fórmula de la lente delgada».

![Figura 11.37](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.37.png)

Figura 11.37: la suma de las desviaciones a ambos lados es $\delta$.

Hasta ahora hemos discutido lentes «convergentes» o «convexas», para las que $f$ es positiva, pero también hay lentes «divergentes» o «cóncavas», para las que $f$ es negativa. En ese caso, los rayos paralelos no se enfocan, sino que se desenfocan, y parecen divergir de un plano situado a una distancia $-f$ (que es un número positivo) más allá de la lente, como se muestra en la figura 11.38. El punto del que divergen los rayos salientes se llama «imagen virtual». En este caso es una imagen virtual del punto en el infinito. En la figura 11.39 se muestra el efecto de una lente cóncava sobre una fuente puntual. De nuevo hay una imagen virtual. Aquí la fórmula de la lente delgada se sigue satisfaciendo, pero tanto $f$ como $d_2$ son negativas.

![Figura 11.38](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.38.png)

Figura 11.38: una lente divergente y su imagen virtual del punto en el infinito.

![Figura 11.39](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.39.png)

Figura 11.39: efecto de una lente cóncava sobre una fuente puntual.

### Imágenes

La propiedad de enfoque de una lente puede usarse para proyectar la imagen de un objeto sobre una superficie, como se muestra en la figura 11.40. Lo que ocurre es que la luz que se abre desde cada punto del objeto se vuelve a enfocar en un único punto de la pantalla. Como en las figuras 11.36 y 11.37, las distancias satisfacen la fórmula de la lente delgada,

$$\frac{1}{d_1} + \frac{1}{d_2} = \frac{1}{f}.\qquad\text{(11.153)}$$

Esto le dice dónde poner la pantalla. Nótese además que es fácil ver en qué punto de la pantalla aparece la imagen de un punto concreto del objeto, porque el rayo de luz que pasa justo por el centro de la lente no se desvía en absoluto (esto lo usamos también para los rayos paralelos, arriba de la figura 11.35). Esto, más geometría sencilla, implica que la razón entre el tamaño de la imagen y el del objeto es $d_2/d_1$:

$$\frac{\text{tamaño de la imagen}}{\text{tamaño del objeto}} = \frac{d_2}{d_1}.\qquad\text{(11.154)}$$

![Figura 11.40](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.40.png)

Figura 11.40: proyección de la imagen de un objeto sobre una pantalla.

Si se retira la pantalla de la figura 11.40, puede verse que la luz a la derecha de donde estaba la pantalla es una copia de la luz que viene del objeto, pero al revés y con el tamaño cambiado en $d_2/d_1$. Si ha jugado con lentes, ya lo sabe.

Nótese que (11.153) implica que ni $d_1$ ni $d_2$ pueden ser menores que $f$. Si acerca demasiado el objeto a la lente, no obtiene una imagen real al otro lado. En su lugar, $d_2$ se hace negativa y se obtiene una «imagen virtual» al mismo lado de la lente que el objeto, y la luz a la derecha de la lente diverge como si viniera de la imagen virtual. Esta situación se ilustra en la figura 11.41. Como discutiremos más abajo, así es como funciona una lupa.

![Figura 11.41](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.41.png)

Figura 11.41: imagen virtual cuando el objeto está más cerca que la distancia focal.

La formación de imágenes ilustrada en la figura 11.40 es lo que ocurre en una cámara y en su propio globo ocular. La lente enfoca la luz de puntos exteriores sobre puntos de la película, o de su retina. Por supuesto, la retina no es realmente un plano. Por la misma razón, el cristalino de su ojo no es una lente esférica, sino de una forma más complicada. El trazado de rayos lo ha hecho la evolución, sin embargo, de modo que los objetos en un plano se enfocan correctamente sobre la retina.

Como la distancia del cristalino a la retina está fijada por la geometría de su ojo, usted debe poder ajustar la forma del cristalino. Al hacerlo, puede cambiar la distancia focal de su cristalino y, con ella, la distancia a la que los puntos están perfectamente enfocados (esto se llama «acomodación»).

La formación de una imagen en la retina se ilustra en el diagrama de la figura 11.42. De nuevo, como en la figura 11.40, la imagen está invertida. No puede enfocar objetos demasiado cercanos al cristalino porque la cantidad de acomodación que puede hacer es limitada. Si acerca el objeto más de la distancia focal más pequeña que su cristalino puede producir, la imagen real queda más allá de la retina y el objeto se verá borroso, como se muestra en la figura 11.43.

![Figura 11.42](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.42.png)

Figura 11.42: formación de una imagen en la retina.

![Figura 11.43](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.43.png)

Figura 11.43: objeto demasiado cercano: la imagen queda más allá de la retina.

Una lupa funciona permitiéndole producir una imagen mayor del objeto sobre su retina. Lo hace de dos maneras, ambas ilustradas en el diagrama de la figura 11.44 (con menos rayos dibujados ahora, porque los diagramas se están volviendo demasiado recargados).

Obviamente, la imagen es mayor. Pero nótese además que la lupa cambia la cantidad de acomodación que su cristalino necesita. Su ojo está enfocando en realidad la imagen virtual, que está mucho más lejos, y eso es más fácil. Así, cuando mira un objeto con una lupa puede acercárselo mucho más al ojo de lo que podría sin ella. Esto aumenta aún más el efecto de aumento, porque los objetos más cercanos se ven más grandes. En este diagrama puede verse también un tercer efecto beneficioso de la lupa: llega más luz del objeto a su ojo.

![Figura 11.44](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.44.png)

Figura 11.44: cómo funciona una lupa.

Uno de los efectos de aumento de una lente puede obtenerse sin lente de una manera muy sencilla: con un agujero de alfiler. Si mira un objeto cercano a través de un agujero de alfiler, puede acercárselo mucho más al ojo. La razón es que solo pasa un haz estrecho de luz por el agujero desde cada punto del objeto que mira, así que no hace falta mucho enfoque. El tamaño de la imagen en su retina no aumenta cuando mira el objeto a través de un agujero de alfiler a la misma distancia que sin él pero, con el agujero, puede acercárselo mucho más al ojo sin que se vea borroso y, por tanto, hacer que parezca más grande.

Puede que también haya jugado con cámaras estenopeicas, en las que se forma una imagen sobre una pantalla dentro de una caja oscura sin lente, como se muestra en la figura 11.45.

![Figura 11.45](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.45.png)

Figura 11.45: una cámara estenopeica.

Una desventaja de la cámara estenopeica es que hace falta un objeto muy brillante: se desecha la mayor parte de la luz que viene del objeto. Puede conseguir más luz haciendo el agujero más grande, pero eso hace la imagen más borrosa. En realidad, sin embargo, tampoco puede hacer el agujero demasiado pequeño. En última instancia, como veremos en el capítulo 13, la difracción limita la resolución de una cámara estenopeica. Si intenta hacer la imagen muy nítida haciendo el agujero muy diminuto, el haz que obtiene dentro de la cámara se ensancha por difracción. Lo mejor que puede hacer es elegir el tamaño del agujero de modo que el ensanchamiento en la pantalla por difracción iguale justo el tamaño del agujero.

Ya que estamos, nótese que la difracción y el tamaño finito de su pupila limitan la resolución angular de su ojo. Como entenderemos en detalle en el capítulo 13, el tamaño finito $s$ de su pupila introduce una dispersión angular del orden de $\lambda/s$ para luz de longitud de onda $\lambda$. A menos que tenga ojos enormes, $s$ es menor que 0.25 cm, así que para luz verde de longitud de onda 500 nanómetros (550 está aproximadamente en mitad del espectro visible), la resolución angular es mayor que unos $2\times10^{-4}$. A una distancia de 10 metros, por ejemplo, incluso si sus ojos son perfectos, no será capaz de resolver dos objetos separados menos de unos pocos milímetros.

Puede usar un agujero de alfiler para estudiar sus ojos de maneras bastante interesantes. Ponga el agujero cerca del ojo y mire una fuente de luz difusa y brillante. Lo haremos en clase, pero puede fabricarse su propio agujero perforando un pequeño orificio en una lámina de papel de aluminio con un alfiler y probarlo. Si lleva gafas, quíteselas: no las necesitará. Debería ver una mancha circular de luz. Es la imagen de su pupila sobre la retina, como se muestra en la figura 11.46.

![Figura 11.46](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.46.png)

Figura 11.46: la imagen de su pupila sobre la retina.

Puede ver cómo cambia el tamaño de su pupila con este montaje. Basta con que tape o cierre el otro ojo: como ahora recibe menos luz, ambas pupilas se dilatarán. Destape el otro ojo, mire de nuevo la luz brillante y las pupilas se contraerán. ¿Nota un pequeño retardo temporal?

Ahora acerque con cuidado la punta de un bolígrafo o un lápiz desde abajo, entre el agujero y su ojo, hasta que justo empiece a tapar la vista. ¿Qué ve? Esto debería convencerle, si no estaba seguro, de que la imagen en su retina está invertida, como se muestra en la figura 11.47. Falta la mitad inferior de la imagen en su retina. Su cerebro, acostumbrado a ver las imágenes de la retina invertidas, ¡lo interpreta como un objeto que baja desde arriba!

![Figura 11.47](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.47.png)

Figura 11.47: la mitad inferior de la imagen retiniana queda tapada.

### Aumento, telescopios, microscopios y todo eso

Combinando lentes de diversas maneras se pueden construir todo tipo de instrumentos ópticos interesantes. La manera más sencilla de pensar en el aumento es considerar el tamaño angular de la imagen observada, comparado con el tamaño angular que se vería sin el instrumento.

En la figura 11.48 se ilustra un telescopio sencillo. Las distancias están algo distorsionadas: en un telescopio real, el objeto estaría mucho más lejos y los tamaños de las lentes serían mucho menores. Cuando mira un objeto lejano (con $L$ grande) con su telescopio, la luz llega a la primera lente (el «objetivo») como un haz de rayos casi paralelos. Sabemos, por la fórmula de la lente delgada,

$$\frac{1}{d_1} + \frac{1}{d_2} = \frac{1}{f},$$

con $d_1 = L \gg f$, que se forma una imagen real a una distancia del objetivo $d_2$ apenas mayor que su distancia focal $f_1$. El «ocular» se coloca entonces a una distancia apenas mayor que su distancia focal, $f_2$, de la imagen real, para convertir de nuevo la luz de la imagen en un haz casi paralelo. Esencialmente, lo que hace con el ocular es mirar la luz de la imagen real con una lupa.

![Figura 11.48](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.48.png)

Figura 11.48: un telescopio sencillo.

Podemos entender cómo (y cuánto) aumenta un telescopio los objetos lejanos mirando los ángulos implicados. Si el objeto tiene tamaño $h_o$, su tamaño angular sin el telescopio es

$$\frac{h_o}{L}.$$

Por triángulos semejantes, el tamaño de la imagen real es

$$\frac{h_o f_1}{L},$$

y por tanto el tamaño angular de la imagen real en el ocular (y en su ojo) es

$$\frac{h_o f_1}{L f_2}.$$

Así, el aumento es aproximadamente

$$\frac{f_1}{f_2}.$$

Nótese que la imagen del telescopio aparece invertida, porque lo que está viendo en realidad es la imagen real.

Un microscopio tiene un aspecto parecido al de la figura 11.49 (con aún menos rayos dibujados, porque a estas alturas ya debería estar acostumbrado a ellos).

![Figura 11.49](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.49.png)

Figura 11.49: un microscopio.

La muestra se coloca un poco más allá de la distancia focal, $f_1$, del objetivo, de modo que se forma una imagen real mucho mayor que la muestra. Después se mira la imagen real con el ocular como si fuera una lupa, colocado de nuevo un poco más allá de su distancia focal, $f_2$, para poder ver la imagen cómodamente con los ojos relajados. Si la muestra tiene tamaño $h_o$, el tamaño de la imagen real es

$$\frac{L}{f_1}h_o$$

y el tamaño angular de la imagen en el ocular (y en su ojo) es

$$\frac{L}{f_1}\frac{h_o}{f_2}.$$

Esto debe compararse con el tamaño angular del objeto a alguna distancia de referencia, $L_0 \approx 25$ cm, a la que puede ver el objeto cómodamente a simple vista, que es

$$\frac{h_o}{L_0}.$$

Así, el aumento es

$$\frac{L\,L_0}{f_1 f_2}.$$

## 11.7 Arcoíris

La mayoría de los libros de física elemental o no explican el arcoíris, o lo explican incorrectamente (a veces de forma embarazosa). Obviamente, tiene algo que ver con la refracción de la luz por las gotas de lluvia. Deberíamos poder explicarlo solo con la ley de Snell y la óptica geométrica —trazado de rayos—. Pero es un poco sutil, como verá.

Para empezar, considere la refracción de un rayo estrecho de luz por una gota esférica de agua, ilustrada en la figura 11.50. El índice de refracción del agua, $n$, varía de unos 1.332 para la luz roja a unos 1.343 para la violeta. El rayo entra en algún punto de la gota, que podemos parametrizar por el ángulo $\theta$ entre la dirección de la luz incidente y el radio que va del centro de la gota al punto por donde entra la luz. El ángulo $\theta$ es también el ángulo entre el rayo de luz y la perpendicular a la superficie de la gota, así que es el apropiado para usar en la ley de Snell. Por tanto, el ángulo $\phi$ del rayo refractado dentro de la gota viene dado por

$$\sin\phi = \frac{\sin\theta}{n} \qquad \text{o} \qquad \phi = \sin^{-1}\left(\frac{\sin\theta}{n}\right).\qquad\text{(11.164)}$$

![Figura 11.50](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.50.png)

Figura 11.50: refracción de un rayo en una gota esférica.

Parte de la luz también se refleja en la gota. Nótese que la luz reflejada se refleja especularmente. Para $\theta = 0$, la luz se refleja directamente hacia atrás. Al aumentar $\theta$ desde 0, el rayo reflejado gira en sentido antihorario respecto del rayo incidente un ángulo $\pi - 2\theta$, hasta que en $\theta = \pi/2$ apenas roza la esfera y no gira nada.

El hecho geométrico importante que hace el problema bastante sencillo es que el ángulo entre el rayo y la perpendicular a la superficie es el mismo cuando sale de la gota que cuando entra. La ley de Snell funciona a la inversa, y el rayo que sale de la gota forma un ángulo $\theta$ con la perpendicular. Como puede verse en la figura 11.51, esto significa que el rayo refractado que sale de la gota es simplemente una versión del rayo reflejado de la figura 11.50 girada $\pi - 2\phi$. Eso significa que está girado

$$\theta_1 = (\pi - 2\phi) - (\pi - 2\theta) = 2\theta - 2\phi\qquad\text{(11.165)}$$

respecto de la dirección original de la luz incidente.

![Figura 11.51](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.51.png)

Figura 11.51: el rayo refractado que sale de la gota.

El problema con esto es que no tiene nada que ver con el arcoíris. El problema es que la dirección del rayo refractado es básicamente hacia delante y depende de $\theta$, de modo que no se destaca ningún valor concreto de $\theta$. Hay tres cosas misteriosas del arcoíris que este efecto no puede explicar:

1.  el arcoíris primario ocurre a un ángulo definido;

2.  el ángulo es en la dirección hacia atrás —a un ángulo de unos 41° (unos 0.7 radianes) del rayo de luz incidente, es decir, girado unos 2.4 radianes respecto de la dirección original—; y

3.  hay un segundo arcoíris fuera del primero, ¡en el que los colores van en orden opuesto!

![Figura 11.52](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.52.png)

Figura 11.52: gráfica de $\theta_1$ frente a $\theta$ para luz roja y azul.

Entonces, ¿qué hace esta refracción? La respuesta es: ¡casi nada! El rayo refractado se reparte sobre un amplio rango de ángulos, como se muestra en la gráfica de la figura 11.52. A un ángulo de salida cualquiera, la luz de este efecto es muy tenue y apenas se nota. No solo los colores no se separan mucho, sino que además todos se reparten de forma más o menos uniforme sobre el ángulo de salida, de modo que no se ve ningún arcoíris por esta refracción.

Entonces, ¿de dónde viene el arcoíris? La respuesta es que, además de refractarse en la superficie interior de la gota, el rayo también puede reflejarse y salir después a un ángulo todavía mayor. El resultado tiene el aspecto de la figura 11.53.

![Figura 11.53](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.53.png)

Figura 11.53: el rayo que se refleja una vez dentro de la gota.

Comparando la figura 11.51, la figura 11.53 y la ecuación (11.165), está claro que en este camino la luz gira

$$\theta_2 = 2(\pi - 2\phi) - (\pi - 2\theta) = 2\theta + \pi - 4\phi.\qquad\text{(11.166)}$$

Y aquí está el punto crítico. Si representamos este $\theta_2$ frente a $\theta$, ¡la gráfica tiene un mínimo! Esto se muestra en la figura 11.54.

![Figura 11.54](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.54.png)

Figura 11.54: gráfica de $\theta_2$ frente a $\theta$ para luz roja y azul.

Ahora el ángulo de salida tiene un mínimo para $\theta \approx 1.05$ (que es el valor de $\theta$ ilustrado en los diagramas). El ángulo de salida $\theta_2 \equiv \theta_{out}$ correspondiente a ese $\theta$ da la posición angular del arcoíris. Aquí, como $\theta_2$ no cambia mucho ante un cambio pequeño de $\theta$, se ve la suma de la luz refractada procedente de un rango de $\theta$ alrededor del mínimo. El ángulo es aproximadamente el que esperamos: $\theta_{out} \approx \pi - 0.7$, donde 0.7 radianes ≈ 41° es el ángulo entre el vector que va de la gota al Sol y el que va de esa misma gota a su ojo, como se muestra en la figura 11.55. El signo negativo de $\pi - 0.7$ significa que la luz no ha girado 180° completos, así que la luz que llega a su ojo entró en la gota refractante por el lado más alejado de usted.

![Figura 11.55](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.55.png)

Figura 11.55: geometría del Sol, la gota y el ojo.

También puede verse en la gráfica de la figura 11.54 que los colores están separados. La luz roja está en el exterior (más lejos de $2\pi$) y la azul en el interior.

Matemáticamente, ¿por qué se acumula la luz en el borde? La energía de la luz solar que cae sobre una parte pequeña de la superficie de la gota entre $\theta$ y $\theta + d\theta$ es proporcional a $I\,d\theta$ (hay otros factores, como $\cos\theta$, pero varían lentamente, así que olvidémoslos). El ángulo del rayo saliente, $\theta_{out}$, es una función de $\theta$, y la energía $\propto I_i\,d\theta$ se reparte sobre una región angular entre $\theta_{out}$ y $\theta_{out} + d\theta_{out}$. Así, la intensidad saliente es proporcional a

$$I_o \propto \frac{I_i\,d\theta}{d\theta_{out}} = \frac{I_i}{\dfrac{d\theta_{out}}{d\theta}}.\qquad\text{(11.167)}$$

¡Cuando $d\theta_{out}/d\theta = 0$, la intensidad se va a infinito! El borde es infinitamente más brillante que el interior. ¡Por eso lo vemos!

Podemos comprobar ahora esta imagen viendo cómo explica el segundo arcoíris. Como cabe suponer, procede de una reflexión más, como se muestra en la figura 11.56.

![Figura 11.56](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.56.png)

Figura 11.56: el rayo que se refleja dos veces dentro de la gota.

Ahora el rayo de luz gira

$$\theta_3 = 3(\pi - 2\phi) - (\pi - 2\theta) = 2\theta + 2\pi - 6\phi.\qquad\text{(11.168)}$$

Esto se muestra, junto con $\theta_2$, en la gráfica de la figura 11.57. El mínimo de $\theta_3$ es la posición del segundo arcoíris. Pero ahora, como el ángulo es mayor que $\pi$, la luz llega a su ojo por el lado de la gota que está más cerca de usted, y está doblándose completamente alrededor.

![Figura 11.57](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.57.png)

Figura 11.57: gráfica de $\theta_2$ y $\theta_3$ frente a $\theta$ para luz roja y azul.

Por eso los colores están invertidos. De nuevo, el azul se refracta más, pero esta vez eso significa que el azul queda en el exterior, mientras que el rojo queda en el interior.

Por casualidad, los mínimos de $\theta_2$ y $\theta_3$ están desplazados de $\pi$ casi lo mismo (dentro de unos 0.13 radianes), aunque en lados opuestos. Por eso los dos arcoíris están bastante juntos en el cielo.

Otra predicción de esta imagen que puede verse a menudo es la «banda oscura de Alejandro», que aparece entre los arcoíris. La luz que no se concentra en el valor mínimo de $\theta$ se reparte dentro del primer arcoíris pero fuera del segundo; así, la región entre los dos arcoíris (o fuera del primero, si el segundo no se ve) es más oscura. Si representamos la distancia angular respecto de $\pi$ en función del ángulo con el que la luz solar entra en la gota, el primer y el segundo arcoíris tienen el aspecto de la figura 11.58 (como de costumbre, he exagerado la diferencia de índice de refracción entre el rojo y el azul). Aquí se ve claramente que el ángulo del primer arcoíris es menor, y la banda oscura entre los dos.

![Figura 11.58](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.58.png)

Figura 11.58: los dos arcoíris.

## 11.8 Ondas esféricas

Considere ondas sonoras en una sala muy grande con paredes absorbentes. En el centro de la sala (tomaremos el centro como origen de nuestro sistema de coordenadas, $\vec{r} = 0$) hay un altavoz esférico, una esfera que produce en su superficie (de radio $R$) una presión oscilante de la forma $p_0\cos\omega t$. ¿Qué tipo de ondas sonoras se producen? Parece bastante tonto usar nuestras soluciones de onda plana con invariancia bajo traslación espacial para este problema, porque el sistema tiene simetría bajo rotaciones alrededor del origen. En su lugar, miremos directamente la ecuación de ondas y aprovechemos la naturaleza esférica del problema. Es decir, supongamos que la solución tiene la forma $\psi(\vec{r}, t) = \chi(|\vec{r}|, t)$. Sustituyendo esto en la ecuación de ondas se obtiene

$$\vec{\nabla}^2\chi(r, t) = \frac{\partial^2}{\partial r^2}\chi(r, t) + \frac{2}{r}\frac{\partial}{\partial r}\chi(r, t).\qquad\text{(11.172)}$$

Podemos reescribir esto de la siguiente forma útil:

$$\vec{\nabla}^2\chi(r, t) = \frac{1}{r}\frac{\partial^2}{\partial r^2}\left[r\,\chi(r, t)\right].\qquad\text{(11.173)}$$

Así, $r\chi(r, t)$ satisface la ecuación de ondas unidimensional.

Ahora podemos resolver el problema que planteamos arriba. Las soluciones para $r\chi$ tienen la forma $\sin(kr \pm \omega t)$ y $\cos(kr \pm \omega t)$, donde $k = \omega/v$. Como la presión en $r = R$ es $p_0\cos\omega t$, nos interesan las combinaciones $\cos(kr - kR - \omega t)$ y $\cos(kr - kR + \omega t)$. Estas describen ondas que salen del origen y que van hacia él, respectivamente. La condición de contorno apropiada en el infinito es tomar la onda saliente, de modo que la perturbación la produzca enteramente el altavoz. Así,

$$\chi(r, t) = \frac{p_0 R}{r}\cos(kr - kR - \omega t).\qquad\text{(11.174)}$$

Las características generales de la solución (11.174) son fáciles de entender. Los frentes de onda, a lo largo de los cuales la fase de oscilación es constante, son esferas centradas en el origen, como debe ser por la simetría rotacional. Las ondas se alejan del origen con velocidad $v$. Al alejarse, su intensidad local debe disminuir, porque la misma cantidad de energía se reparte sobre un área mayor. Esa es la razón del $1/r$ de (11.174). Si la amplitud cae como $1/r$, la intensidad de la onda cae como $1/r^2$, como debe ser. Aunque la física está clara, la forma precisa de esta solución es engañosamente sencilla. En dos dimensiones, por ejemplo, no es posible hallar una solución de un problema análogo usando las funciones que conoce del instituto. En dos dimensiones, la amplitud de la onda debe decrecer aproximadamente como $1/\sqrt{r}$. Las soluciones de la ecuación de ondas bidimensional con esa propiedad se llaman funciones de Bessel. Aprenderá sobre ellas en cursos más avanzados.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Interpretar las ondas planas en el espacio de dos y tres dimensiones en términos de un vector $\vec{k}$, el número de onda angular;

2.  Analizar la dispersión de una onda plana en un contorno plano entre regiones con relaciones de dispersión distintas;

3.  Deducir y usar la ley de Snell;

4.  Comprender el fenómeno de la reflexión total interna, junto con el enunciado general de la condición de contorno en el infinito para $\vec{k}$ complejo;

5.  Comprender la física y las matemáticas de los fenómenos de efecto túnel;

6.  Comprender cómo afecta la degeneración de las frecuencias de los modos normales al problema de la oscilación forzada, y hallar los patrones de arena en placas de Chladni cuadradas;

7.  Comprender la propagación de ondas en guías de onda, usando la separación de variables para construir los modos e interpretar el resultado en términos de ondas en zigzag;

8.  Ser capaz de analizar las ondas en el agua, ignorando la viscosidad y el momento angular;

9.  Resolver problemas con ondas esféricas donde el desplazamiento solo depende de $r$ y $t$.

## Problemas

**11.1.** Considere las oscilaciones transversales libres de la cuerda bidimensional con cuentas mostrada en la figura 11.59. Todas las cuerdas horizontales tienen tensión $T_h$, todas las verticales tienen tensión $T_v$, y todos los círculos macizos son cuentas de masa $m$. El marco cuadrado está fijo en el plano $z = 0$.

**a.** Halle los modos normales y sus frecuencias correspondientes.

**b.** Suponga que $T_v = 100\,T_h$. Dibuje nueve diagramas, uno para cada modo normal, en orden de frecuencia creciente, indicando qué cuentas se mueven hacia arriba (con un signo $+$), cuáles hacia abajo (con un signo $-$) y cuáles no se mueven (con un 0). Puede intercambiar $+$ y $-$ y seguir teniendo la respuesta correcta, cambiando el origen de tiempos o multiplicando su vector de modo normal por $-1$. Haga el resto y ponga el orden correcto. Debería poder hacerlo incluso si se lió con los detalles del apartado a.

![Figura 11.59](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.59.png)

Figura 11.59: una cuerda bidimensional con cuentas.

**11.2.** Considere las oscilaciones transversales forzadas de la cuerda bidimensional con cuentas mostrada en la figura 11.60. Todas las cuerdas tienen tensión $T$ y todos los círculos macizos son cuentas de masa $m$. El marco se mantiene fijo en el plano $z = 0$. Los círculos huecos se mueven arriba y abajo fuera del plano del papel con el mismo desplazamiento transversal,

$$z_1(t) = z_2(t) = z_3(t) = d\cos\omega t$$

donde

$$\omega = \sqrt{\frac{T}{ma}}.$$

Halle el desplazamiento de cada una de las cuentas. Puede hacerlo resolviendo para el desplazamiento $z_{jk}(t)$ de la cuenta cuya posición horizontal es $x = kL/4$, $y = jL/4$, para todos los $j$ y $k$ relevantes. Todos los desplazamientos serán proporcionales a $d\cos\omega t$, así que escriba su respuesta en forma de tabla de los coeficientes de $d\cos\omega t$ para cada $j$ y $k$.

![Figura 11.60](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.60.png)

Figura 11.60: una cuerda bidimensional con cuentas, forzada.

**11.3.** Considere las oscilaciones transversales forzadas de la cuerda bidimensional semiinfinita con cuentas mostrada en la figura 11.61. Todas las cuerdas tienen tensión $T$, todos los círculos macizos son cuentas de masa $m$ y las separaciones de equilibrio de los bloques son todas $a$. El marco en $y = 0$ e $y = 4a$ se mantiene fijo en el plano $z = 0$. Los círculos huecos en $x = 0$ se mueven arriba y abajo fuera del plano del papel con desplazamiento transversal

$$z_1(t) = z_3(t) = \frac{d}{\sqrt{2}}\cos\omega t, \qquad z_2(t) = -d\cos\omega t,$$

para los valores de $\omega$ dados abajo. Para cada $\omega$, halle el desplazamiento de cada cuenta en función de su posición de equilibrio. Es decir, determine $\psi(x, y, t)$. Suponga que todo el sistema oscila con frecuencia $\omega$ y que el desplazamiento se comporta bien en $x = +\infty$.

![Figura 11.61](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.61.png)

Figura 11.61: una cuerda bidimensional semiinfinita con cuentas.

**a.** Halle $\psi(x, y, t)$ para $\omega = \sqrt{2 + \epsilon}\sqrt{T/am}$.

**b.** Halle $\psi(x, y, t)$ para $\omega = \sqrt{2 - \epsilon}\sqrt{T/am}$.

En ambos casos suponga que $\epsilon$ es un número real pequeño, lo bastante pequeño como para poder aproximar $\sinh\epsilon \approx \epsilon$.

**11.4.** Una membrana flexible con tensión superficial $\tau_S$ y densidad superficial de masa $\rho_S$ está tensada de modo que su posición de equilibrio es el plano $z = 0$. Unida a la superficie de la membrana en $x = 0$ hay una cuerda con tensión $\tau_L$ y densidad lineal de masa $\rho_L$. Considere una onda viajera en la membrana con desplazamiento transversal

$$\psi(x, y, t) = \psi_-(x, y, t) = A e^{-i\omega t + ik_x x + ik_y y} + R\,A e^{-i\omega t - ik_x x + ik_y y}$$

para $x \leq 0$, y

$$\psi(x, y, t) = \psi_+(x, y, t) = T\,A e^{-i\omega t + ik_x x + ik_y y}$$

para $x \geq 0$.

¿En qué dirección viaja la onda reflejada (para $x < 0$)? ¡Fácil!

La ley de Newton para un elemento pequeño de la cuerda de longitud $dy$ con posición de equilibrio $(0, y, 0)$ es

$$\tau_S\,dy\left(\frac{\partial}{\partial x}\psi_+(0, y, t) - \frac{\partial}{\partial x}\psi_-(0, y, t)\right) + \tau_L\,dy\,\frac{\partial^2}{\partial y^2}\psi_\pm(0, y, t) = \rho_L\,dy\,\frac{\partial^2}{\partial t^2}\psi_\pm(0, y, t).$$

Explique el significado físico del término proporcional a $\tau_S$. ¿Qué tira de qué? ¿Por qué tiene la forma mostrada?

**11.5.** Considere las oscilaciones transversales de una membrana flexible infinita tensada en el plano $z = 0$ con tensión superficial $T_s$ y densidad superficial de masa $D_s$. A lo largo de la línea $z = 0$, $x = 0$, hay una cuerda de densidad lineal de masa $D_L$, pero sin tensión propia, unida a la membrana.

Considere una onda de la forma

$$A e^{i(kx\cos\theta + ky\sin\theta - \omega t)} + R\,A e^{i(-kx\cos\theta + ky\sin\theta - \omega t)} \quad \text{para } x < 0$$

$$T\,A e^{i(k'x\cos\theta' + k'y\sin\theta' - \omega t)} \quad \text{para } x > 0$$

donde $\cos\theta > 0$ y $\cos\theta' > 0$.

Halle $\sin\theta'$ en términos de $\sin\theta$ (¡TRIVIAL!).

Halle $R$ y $T$. *Pista: considere $F = ma$ para un trozo infinitesimal de la cuerda cargada, recordando que no tiene tensión propia.*

**11.6.** Dos membranas flexibles semiinfinitas están tensadas en el plano $z = 0$. La primera tiene tensión superficial 1 dina/cm y densidad de masa 169 g/cm². Está fijada a lo largo de los ejes $z = 0$, $y = 0$ y $z = 0$, $y = a$, y se extiende de $x = 0$ a $\infty$ en la dirección $+x$. La segunda tiene la misma tensión superficial pero densidad de masa 180 g/cm². También está fijada a lo largo de los ejes $z = 0$, $y = 0$ y $z = 0$, $y = a$, y se extiende de $x = 0$ a $-\infty$ en la dirección $-x$. Las dos membranas están unidas con cinta adhesiva sin masa en $x = 0$. Considere las oscilaciones transversales de este sistema de la forma

$$\psi(x, y, t) = A\sin(k_y y)\left(e^{-i(\omega t - k_x x)} + R\,e^{-i(\omega t + k_x x)}\right) \quad \text{para } x \leq 0;$$

$$\psi(x, y, t) = A\sin(k_y y)\,T\,e^{-i(\omega t - k'_x x)} \quad \text{para } x \geq 0$$

donde $k_y = 12\pi$ cm$^{-1}$ y $\omega = \pi$ s$^{-1}$.

Halle $k_x$ y $k'_x$. Halle $R$ y $T$.

**11.7.** Una membrana uniforme está tensada en el plano $z = 0$, como se muestra en la figura 11.62. Está unida a varillas fijas a lo largo de $y = 0$, $z = 0$ e $y = a$, $z = 0$, desde $x = 0$ hasta $\infty$. $\psi(x, y, t)$ es el desplazamiento $z$ del punto de la membrana cuya posición de equilibrio es $(x, y, 0)$. Para oscilaciones pequeñas, $\psi$ satisface la ecuación de ondas bidimensional,

$$\frac{\partial^2}{\partial t^2}\psi = v^2\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}\right)\psi.$$

![Figura 11.62](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.62.png)

Figura 11.62: un problema de oscilación forzada en una membrana elástica.

Si este sistema se extiende a un sistema infinito continuándolo a $x$ negativa, muestre que los modos normales del sistema infinito toman la forma

$$\psi(x, y) = A\sin(nk_0 y)\,e^{ikx}.$$

Halle $k_0$. Suponga que el extremo de la membrana en $x = 0$ se excita como sigue:

$$\psi(0, y, t) = \cos(5vk_0 t)\left[B\sin(3k_0 y) + C\sin(13k_0 y)\right].$$

La condición de contorno en $\infty$ es tal que no hay onda viajando en la dirección $-x$ a lo largo de la membrana. Halle $\psi(x, y, t)$.

Explique la siguiente afirmación: para $\omega < 2vk_0$, el sistema actúa como un portador de ondas unidimensional con la relación de dispersión $\omega^2 = v^2k^2 + \omega_0^2$. ¿Cuánto vale $\omega_0$?

**11.8.** Considere una cáscara esférica rígida de radio interior $L$ llena de gas en el que la velocidad del sonido es $v$. En esta esfera hay modos normales de onda estacionaria de muchos tipos. Nos interesarán aquellos en los que la presión depende solo de la distancia $r$ al centro de la esfera. Suponga que $\psi(\vec{r}, t) = \chi(r, t)$ es la diferencia entre la presión del gas en tal modo y la presión de equilibrio. Sabemos de (11.173) que $\xi(r, t) \equiv r\chi(r, t)$ satisface la ecuación de ondas unidimensional.

Explique la física de la condición de contorno en $r = 0$.

En términos de un número de onda desconocido $k$, halle una forma de $\chi(r, t)$ que satisfaga la condición de contorno en $r = 0$.

Explique la física de la condición de contorno en $r = L$.

Escriba el enunciado matemático de la condición de contorno en $r = L$, cuyas soluciones dan los valores permitidos de $k$ para los modos normales.

*Pistas: recuerde que es $\chi$, y no $\xi$, la diferencia física de presión. El modo no trivial más bajo tiene un valor de $k$ que satisface $kL \approx 4.4934$.*

![Figura 11.63](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.63.png)

Figura 11.63: amplitud de la oscilación de presión frente a $r$.

**11.9.** Considere un contorno entre dos membranas semiinfinitas tensadas en el plano $x$-$y$. La membrana para $x < 0$ tiene tensión superficial $\tau_s$ y densidad superficial de masa $\rho_s$. La membrana para $x > 0$ tiene la misma tensión superficial $\tau_s$ pero densidad superficial de masa distinta, $\rho_s'$. A lo largo del contorno hay un dispositivo (no sé exactamente cómo funciona) que produce una fuerza de fricción vertical proporcional a menos la velocidad vertical de la membrana en el contorno. Dicho de otro modo, si $\psi(x, y, t)$ es el desplazamiento $z$ de la membrana en función de $(x, y)$, la fuerza (en la dirección $z$) sobre un trocito del contorno que va del punto $(0, y)$ al $(0, y + dy)$ es

$$dF = -dy\,\gamma\,\frac{\partial}{\partial t}\psi(0, y, t).$$

En la membrana hay una onda plana de la forma siguiente:

$$\psi(x, y, t) = A e^{i(kx\cos\theta + ky\sin\theta - \omega t)}$$

para $x < 0$, y

$$\psi(x, y, t) = A e^{i(k'x\cos\theta' + k'y\sin\theta' - \omega t)}$$

para $x > 0$. El montaje se muestra en la figura 11.64.

![Figura 11.64](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.64.png)

Figura 11.64: dispersión en un contorno de una membrana elástica.

Halle $k'$. Halle $\theta'$. Halle $\gamma$. Debería obtener $\gamma \to 0$ para $\rho_s \to \rho_s'$; explique por qué.

**11.10.** En vez de un océano abierto, considere un sistema con un fondo en $y = 0$ y una tapa fija en $y = 2L$, medio lleno de agua y medio lleno de disolvente de pintura, otro fluido casi incompresible más ligero que el agua, que flota en la mitad superior sin mezclarse con ella.

Muestre que las ondas de este sistema tienen la forma de (11.122) para $y \leq L$ (en el agua) y

$$\psi_x(x, y, t) = \mp i\,e^{\pm ikx - i\omega t}\cosh[k(2L - y)], \qquad \psi_y(x, y, t) = e^{\pm ikx - i\omega t}\sinh[k(2L - y)]\qquad\text{(11.175)}$$

para $L \leq y \leq 2L$ (en el disolvente), argumentando que (11.175) y (11.122) satisfacen las condiciones de contorno apropiadas en $y = 0$ y $y = 2L$ y (para desplazamientos pequeños) en $y = L$, y muestre que (11.175), como (11.125), es coherente con la incompresibilidad ($\vec{\nabla}\cdot\vec{\psi} = 0$).

Muestre que $\psi_x$ es discontinua en $y = L$ y explique físicamente qué está ocurriendo en ese contorno y por qué. Cuando lo haya hecho, mire el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-11-4" rel="noopener" target="_blank" title="Animación original de Howard Georgi">11-4</a>, en el que se anima este sistema. Si mira con atención, notará el efecto de la ruptura de la linealidad para desplazamientos grandes.

Suponga ahora que los líquidos están contenidos entre paredes verticales en $x = 0$ y $x = X$. ¿Qué condiciones de contorno se satisfacen en los contornos verticales?

Halle la forma de los desplazamientos de los modos normales de este sistema.

Muestre que la relación de dispersión de este sistema es

$$\omega^2 = \left(\frac{\rho_W - \rho_P}{\rho_W + \rho_P}\,gk + \frac{k^3\tau_S}{\rho_W + \rho_P}\right)\tanh kL,\qquad\text{(11.176)}$$

donde $\rho_P$ es la densidad del disolvente, $\rho_W$ la del agua y $\tau_S$ la tensión superficial del contorno entre el agua y el disolvente. *Pista: use un argumento energético análogo a (11.127)-(11.137) y discuta simplemente cómo cambian las distintas contribuciones al pasar de (11.137) a (11.176).*

**11.11.** Considere la reflexión de ondas sonoras en una membrana sin masa e infinitamente flexible que separa dos gases con la misma presión de equilibrio, $p_0$, pero densidades distintas. La membrana está en el plano $x = 0$. El gas de la región 1, para $x < 0$, tiene densidad de equilibrio $\rho_1$, razón entre el calor específico a presión constante y a volumen constante $\gamma_1$, y velocidad del sonido $\sqrt{\gamma_1 p_0/\rho_1}$; el gas de la región 2, para $x > 0$, tiene densidad $\rho_2$, razón de calores específicos $\gamma_2$ y velocidad del sonido $\sqrt{\gamma_2 p_0/\rho_2}$. Una onda de presión en el sistema tiene la forma

$$P(\vec{r}, t)/\delta p = A e^{i\vec{k}_1\cdot\vec{r} - i\omega t} + R\,A e^{i\vec{k}_R\cdot\vec{r} - i\omega t}$$

en la región 1, para $x < 0$, y

$$P(\vec{r}, t)/\delta p = T\,A e^{i\vec{k}_2\cdot\vec{r} - i\omega t}$$

en la región 2, para $x > 0$, donde $P(\vec{r}, t) + p_0$ es la presión del gas cuya posición de equilibrio es $\vec{r}$. La presión pequeña $\delta p$ describe la amplitud de la onda de presión. $R$ y $T$ son los coeficientes de reflexión y transmisión. Los vectores $k$ son

$$\vec{k}_1 = (k\cos\theta, k\sin\theta, 0), \quad \vec{k}_R = (-k_R\cos\theta_R, k_R\sin\theta_R, 0), \quad \vec{k}_2 = (k_2\cos\theta_2, k_2\sin\theta_2, 0)$$

donde $k$, $k_R$, $k_2$, $\cos\theta$, $\cos\theta_R$ y $\cos\theta_2$ son todos positivos.

Halle $k_R$ y $\cos\theta_R$ en términos de $k$ y $\theta$.

Halle $k_2$ y $\cos\theta_2$ en términos de $k$ y $\theta$.

Muestre que si $\rho_1/\gamma_1 > \rho_2/\gamma_2$ hay un valor crítico de $\theta$ por encima del cual la onda se refleja totalmente, y halle el ángulo crítico.

Para hallar $R$ y $T$ necesitamos las condiciones de contorno en $x = 0$. Una se sigue del hecho de que la membrana no tiene masa y es infinitamente flexible: eso implica que no puede haber fuerza sobre ella transversal a su superficie. Halle esta condición de contorno. *Pista: ¿de dónde viene la fuerza transversal a la superficie?*

La otra condición implica el desplazamiento transversal de la membrana. El desplazamiento puede obtenerse de la presión:

$$\vec{\psi}(\vec{r}, t) = \frac{1}{\rho_j\omega^2}\vec{\nabla}P(\vec{r}, t),$$

donde $\vec{\psi}(\vec{r}, t)$ es el desplazamiento del gas cuya posición de equilibrio es $\vec{r}$ y $j$ es la etiqueta de la región. Halle la otra condición de contorno. *Pista: suponga que la amplitud $\delta p$ es pequeña.* Halle $R$ y $T$.

**11.12.** Considere un universo lleno de un material con conductividad no nula, $\sigma$. Es decir, en ese material hay una corriente proporcional al campo eléctrico (ley de Ohm),

$$\vec{J}(\vec{r}, t) = \sigma\vec{E}(\vec{r}, t).\qquad\text{(11.177)}$$

Supondremos que el material no tiene ninguna otra propiedad eléctrica —en particular, que no hay polarización ni magnetización— y que no se acumula carga en ningún sitio, de modo que $\rho = 0$. Considere la propagación de una onda plana electromagnética en este universo. Como este universo es perfectamente invariante bajo traslación espacial y bajo rotaciones, y como (11.177) es lineal, cabría esperar que hubiera soluciones de onda plana en las que los campos eléctrico y magnético fueran proporcionales a $e^{i(\vec{k}\cdot\vec{r} - \omega t)}$ para $\vec{k}^2$ y $\omega$ relacionados por alguna relación de dispersión. En particular, considere la propagación en la dirección $+z$ con el campo eléctrico en la dirección $x$ y el magnético en la $y$.

**a.** Muestre, a partir de las ecuaciones de Maxwell relevantes, que tal onda plana puede existir si

$$k^2 = \mu_0\varepsilon_0\omega^2 + i\mu_0\sigma\omega.$$

**b.** Suponga que $\omega$ es real y positiva y que la parte real de $k$ es positiva. Halle el signo de la parte imaginaria de $k$ e interprete físicamente su resultado. Es decir, explique por qué el signo tenía que salir como salió.

**11.13.** Considere una onda sonora esférica que llega desde muy lejos y es absorbida completamente por un amortiguador de sonido esférico de radio $r = \ell$, como se muestra en la figura 11.65. La presión en este sistema se describe mediante la parte real de la onda viajera compleja siguiente, que depende solo del radio y del tiempo:

$$p(r, t) - p_0 = \frac{\varepsilon}{r}e^{-i(kr + \omega t)}$$

![Figura 11.65](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.65.png)

Figura 11.65: un amortiguador esférico de sonido.

**a.** Halle la potencia promediada en el tiempo absorbida por el amortiguador esférico en $r = \ell$.

**b.** Explique cualitativamente el factor $1/r$ de la presión.

Suponga ahora que hay un contorno esférico sin masa y flexible entre dos gases distintos, de radio $r = r_b$, mostrado como el círculo discontinuo del diagrama de la figura 11.66. La presión de equilibrio, $p_0$, es la misma a ambos lados del contorno. Suponga también que $\gamma$ es el mismo para los dos gases y que la única diferencia son las densidades: dentro la densidad es $\rho$ y fuera es $\rho'$. Ahora, para $\ell < r < r_b$, la presión sigue viniendo dada como antes, pero en la región exterior al círculo discontinuo hay una onda reflejada además de la incidente.

![Figura 11.66](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh11_ES/fig11.66.png)

Figura 11.66: un amortiguador esférico de sonido con un contorno reflectante.

**c.** ¿Cuáles son las condiciones de contorno en $r = r_b$ y por qué?

**d.** Halle $B/A$ y $\varepsilon/A$ en el límite $k, k' \gg 1/r_b$, en el que se pueden despreciar los términos proporcionales a $1/r_b$ frente a $k$ o $k'$.

**11.14.** Uno de los problemas de las lentes de vidrio es que el índice de refracción del vidrio depende de la frecuencia. Así, según la fórmula del fabricante de lentes, la distancia focal de una lente de vidrio dependerá de la frecuencia, y eso no es bueno, porque si un color queda bien enfocado, los demás quedarán borrosos. Esto se llama «aberración cromática». Afortunadamente, distintos tipos de vidrio se comportan de manera distinta a este respecto, y eso hace posible eliminar la aberración cromática. Suponga que fabrica una lente pegando lentes de dos tipos de vidrio, con radios $r_1$ y $r_2$. Suponga que los índices de refracción de los dos vidrios son

$$n_1(\lambda) = n_{01} + \alpha_1\lambda, \qquad n_2(\lambda) = n_{02} + \alpha_2\lambda.$$

¿Qué relación debe satisfacerse para que la lente compuesta tenga una distancia focal independiente de $\lambda$?

**11.15.** También se puede hacer un telescopio con una lente convergente (el objetivo) y una divergente (el ocular). La distancia focal de la lente convexa es $f_1$ y la de la cóncava es $-f_2$.

**a.** Si el trazado de rayos funciona como se muestra, es decir, si los rayos paralelos que entran en el objetivo salen paralelos del ocular, halle la distancia $d$ entre las dos lentes.

**b.** Calcule el aumento suponiendo que mira un objeto lejano que subtiende un tamaño angular $\theta$. Considere después un rayo con ángulo $\theta$ que pasa por el centro de la lente convexa. Calculando por dónde pasa por la lente cóncava, debería poder determinar su ángulo, $\theta_o$, cuando llega al ojo del observador. El aumento es entonces $\theta_o/\theta$. ¿Cuánto vale en términos de las distancias focales?

**c.** En este caso la imagen sale derecha. Dibuje un diagrama cuidadoso para explicar por qué.

**11.16.** El aspecto de los arcoíris depende de forma espectacular del índice de refracción del agua. Describa en detalle qué aspecto tendrían los arcoíris si $n$ disminuyera en 0.03 para cada frecuencia de la luz. Discuta el primer y el segundo arcoíris y la banda oscura de Alejandro.

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*

[1] ¡Aquí hay una simetría en juego! Los modos en los que el vector $\vec{k}$ está alineado con los ejes $x$ o $y$ son los que se comportan de forma sencilla bajo reflexiones a través del centro del rectángulo.

[2] Hemos definido aquí $\psi_\pm$ para facilitar la discusión de las condiciones de contorno, más abajo.

[3] Nótese que es la masa del electrón, y no la del protón, la relevante, porque los electrones se mueven mucho más en los campos eléctricos.

[4] El contorno no cambia $p_y$ del fotón, por la invariancia bajo traslación en la dirección $y$. Sin embargo, no hay ninguna razón por la que el contorno no pueda ejercer una fuerza en la dirección $x$ y cambiar $p_x$ del fotón.

[5] Hay también modos proporcionales a $\sin\left((n_x + 1/2)\pi x/L\right)$ y/o $\sin\left((n_y + 1/2)\pi y/L\right)$, pero se anulan en el origen y no son excitados por la fuerza impulsora.

[6] Aquí podemos tomar $\psi$ adimensional y dejar que el parámetro $\varepsilon$ sea un desplazamiento pequeño.

[7] Nótese, sin embargo, que para $\varepsilon$ grande la incompresibilidad es la restricción no lineal (11.111).


---

<!-- MIT8.03_TextCh12_ES.md -->

# Capítulo 12: Polarización

En este capítulo volvemos a (9.46)-(9.48) y examinamos las consecuencias de las ecuaciones de Maxwell en un material homogéneo para una onda plana electromagnética viajera general. La complicación añadida es la polarización.

## Vídeos de esta clase (YouTube)

- [Clase 17: Polarización, polarizador](https://www.youtube.com/watch?v=TjxR7lAwWhI)
- [Clase 18: Láminas de onda, radiación](https://www.youtube.com/watch?v=Dlhma3z57SA)

## Resumen previo

La polarización es una característica general de las ondas transversales en tres dimensiones. La onda plana electromagnética general tiene dos estados de polarización, correspondientes a las dos direcciones a las que puede apuntar el campo eléctrico transversalmente a la dirección de movimiento de la onda. De ahí surge mucha física interesante.

1.  Introducimos la idea de polarización en las oscilaciones transversales de una cuerda.

2.  Discutimos la forma general de las ondas electromagnéticas y describimos el estado de polarización en términos de un vector complejo de dos componentes, $Z$. Calculamos la densidad de energía y de momento en función de $Z$ y discutimos el vector de Poynting. Describimos las variedades de estados de polarización posibles de una onda plana: lineal, circular y elíptica.

3.  Describimos la «luz no polarizada» y explicamos cómo generar y manipular luz polarizada con polarizadores y láminas de onda. Discutimos la rotación del plano de la luz polarizada linealmente por sustancias ópticamente activas.

4.  Analizamos la reflexión y la transmisión de luz polarizada con incidencia oblicua sobre un contorno entre dieléctricos.

## 12.1 La cuerda en tres dimensiones

En la mayoría de nuestras discusiones sobre fenómenos ondulatorios hasta ahora hemos supuesto que el movimiento tiene lugar en un plano, de modo que podemos dibujar el sistema en una hoja de papel. Nos hemos estado restringiendo implícitamente a ondas bidimensionales. Esto está bien para las oscilaciones longitudinales en tres dimensiones, porque toda la acción transcurre a lo largo de una única línea. Sin embargo, para las oscilaciones transversales, pasar de dos a tres dimensiones supone una diferencia enorme, porque hay dos direcciones transversales en las que el sistema puede oscilar.

Por ejemplo, considere una cuerda en tres dimensiones, tensada en la dirección $z$. Cada punto de la cuerda puede oscilar tanto en la dirección $x$ como en la dirección $y$. Si el sistema no fuera aproximadamente lineal, esto podría ser un problema horrendo. La linealidad nos permite resolver el problema de la oscilación en el plano $x$-$z$ por separado del problema de la oscilación en el plano $y$-$z$. Ya hemos resuelto estos problemas bidimensionales en el capítulo 5. Después podemos simplemente juntar los resultados para obtener el movimiento más general del sistema tridimensional. Dicho de otro modo, podemos tratar la componente $x$ de la oscilación transversal y la componente $y$ como completamente independientes.

Supongamos que hay una onda armónica viajera en la dirección $+z$ en la cuerda. El desplazamiento de la cuerda en $z$ respecto de su posición de equilibrio, $(0, 0, z)$, puede escribirse como

$$\vec{\Psi}(z, t) = \operatorname{Re}\left[(\psi_1\hat{x} + \psi_2\hat{y})\,e^{i(kz - \omega t)}\right]\qquad\text{(12.1)}$$

donde $\hat{x}$ e $\hat{y}$ son vectores unitarios en las direcciones $x$ e $y$, y $\psi_1$ y $\psi_2$ son parámetros complejos que describen la amplitud y la fase de las oscilaciones en el plano $x$-$z$ y en el plano $y$-$z$,

$$\psi_j = A_j e^{i\phi_j} \quad \text{para } j = 1\text{ a }2.\qquad\text{(12.2)}$$

Conviene disponer estos parámetros en un vector complejo

$$Z = \begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix},\qquad\text{(12.3)}$$

que da una descripción completa del movimiento de la cuerda.

### 12.1.1 Polarización

La «polarización» se refiere a la naturaleza del movimiento de un punto de la cuerda (o de otra oscilación transversal). Este movimiento está animado en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-12-1" rel="noopener" target="_blank" title="Animación original de Howard Georgi">12-1</a>. Quizá le convenga leer la discusión que sigue con ese programa en marcha.

Si $\phi_1 = \phi_2$, o bien $A_1$ o $A_2$ es cero, entonces (12.3) representa una cuerda polarizada linealmente. La polarización lineal es fácil de entender: significa que cada punto de la cuerda oscila de un lado a otro en un plano fijo. Por ejemplo,

$$u_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}\qquad\text{(12.4)}$$

$$u_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}\qquad\text{(12.5)}$$

representan cuerdas que oscilan en el plano $x$-$z$ y en el plano $y$-$z$ respectivamente. Una cuerda que oscila en un plano que forma un ángulo $\theta$ con el eje $x$ positivo (hacia el eje $y$ positivo) se representa mediante

$$u_\theta = \begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix}.\qquad\text{(12.6)}$$

Esto se muestra en el plano $x$-$y$ en la figura 12.1. Los vectores de polarización (12.4)-(12.6) pueden multiplicarse por un factor de fase, $e^{i\phi}$, sin que ello afecte al estado de polarización de ninguna manera importante. Eso corresponde simplemente a poner el reloj a cero de otro modo.

![Figura 12.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh12_ES/fig12.1.png)

Figura 12.1: $u_1$, $u_2$ y $u_\theta$.

Más interesante es la polarización circular. Una onda polarizada circularmente en una cuerda se representa por

$$\begin{pmatrix} 1 \\ i \end{pmatrix}\qquad\text{(12.7)}$$

o bien por

$$\begin{pmatrix} 1 \\ -i \end{pmatrix}.\qquad\text{(12.8)}$$

En (12.7), la componente $y$ va retrasada respecto de la componente $x$ en $\pi/2$ ($= \phi_2$). Así, en cualquier punto fijo del espacio, el campo rota de $x$ hacia $y$, es decir, en sentido antihorario visto desde el eje $z$ positivo (con la onda viniendo hacia usted), como se muestra en la figura 12.2. Esto se llama «polarización circular a izquierdas», porque la cuerda se parece a un tornillo levógiro. Análogamente, (12.8) representa la rotación de la cuerda en sentido horario, y se llama «polarización circular a derechas».

![Figura 12.2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh12_ES/fig12.2.png)

Figura 12.2: polarización circular.

El vector

$$\begin{pmatrix} A \\ iB \end{pmatrix}\qquad\text{(12.9)}$$

con $A > B > 0$ representa polarización elíptica. Un punto de la cuerda describe una elipse de semieje mayor $A$ a lo largo del eje 1 y semieje menor $B$ a lo largo del eje 2, con rotación antihoraria, como se muestra en la figura 12.3.

![Figura 12.3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh12_ES/fig12.3.png)

Figura 12.3: polarización elíptica con el eje largo en la dirección $x$.

![Figura 12.4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh12_ES/fig12.4.png)

Figura 12.4: polarización elíptica general.

Un vector completamente general puede escribirse de la forma siguiente:

$$\begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix} = e^{i\phi}\begin{pmatrix} A\cos\theta - iB\sin\theta \\ A\sin\theta + iB\cos\theta \end{pmatrix}\qquad\text{(12.10)}$$

con $A \geq |B|$ y $0 \leq \theta < \pi$, donde $\phi$ es una fase real (poco relevante para la física, pero que puede estar ahí para afear las matemáticas). Esto representa polarización elíptica con semieje mayor $A$ formando un ángulo $\theta$ con el eje 1, como en

$$u_\theta = \begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix}$$

y semieje menor $B$, como se muestra en la figura 12.4. Si $B$ es positivo (negativo), la rotación es antihoraria (horaria). Los parámetros físicamente interesantes $A$, $B$ y $\theta$ pueden obtenerse a partir de $\psi_1$ y $\psi_2$ como sigue:

$$A^2 + B^2 = |\psi_1|^2 + |\psi_2|^2,\qquad\text{(12.11)}$$

$$AB = -\operatorname{Im}(\psi_1\psi_2^*).\qquad\text{(12.12)}$$

Así,

$$A \pm B = \sqrt{|\psi_1|^2 + |\psi_2|^2 \mp 2\operatorname{Im}(\psi_1\psi_2^*)},\qquad\text{(12.13)}$$

da $A$ y $B$. Entonces $\theta$ satisface

$$(A^2 - B^2)\cos 2\theta = |\psi_1|^2 - |\psi_2|^2,$$

$$(A^2 - B^2)\sin 2\theta = 2\operatorname{Re}(\psi_1\psi_2^*).$$

Obsérvese que el factor de fase global $e^{i\phi}$ se cancela en (12.11)-(12.13).

## 12.2 Ondas electromagnéticas

### 12.2.1 Ondas planas electromagnéticas generales

Vimos en los capítulos 8 y 9 que una onda plana electromagnética que viaja en la dirección $+z$ tiene este aspecto:

$$E_x(z, t) = \varepsilon_x e^{i(kz - \omega t)}, \qquad E_y(z, t) = \varepsilon_y e^{i(kz - \omega t)},\qquad\text{(12.14)}$$

$$B_x(z, t) = \beta_x e^{i(kz - \omega t)}, \qquad B_y(z, t) = \beta_y e^{i(kz - \omega t)},\qquad\text{(12.15)}$$

$$E_z(z, t) = B_z(z, t) = 0,\qquad\text{(12.16)}$$

donde las $\beta$ vienen determinadas por las ecuaciones de Maxwell como

$$\beta_y = \frac{n}{c}\varepsilon_x, \qquad \beta_x = -\frac{n}{c}\varepsilon_y.\qquad\text{(12.17)}$$

Como de costumbre, hemos escrito la onda con la dependencia temporal irreducible, $e^{-i\omega t}$. Para obtener los campos eléctrico y magnético reales, tomamos la parte real de (12.14)-(12.15). Nótese, en particular, que las constantes $\varepsilon_j$ y $\beta_j$ para $j = x$ e $y$ pueden ser complejas.

La restricción al movimiento en la dirección $z$ no es importante. Puesto que la física de las ecuaciones de Maxwell es invariante bajo rotaciones en el espacio tridimensional, podemos escribir la forma de una onda plana que se mueve con un vector $\vec{k}$ arbitrario extrayendo de (12.14)-(12.17) las características que no dependen de la dirección. Son estas:

1.  $\vec{k}$, $\vec{E}$ y $\vec{B}$ son vectores mutuamente ortogonales.

2.  $\vec{B}$ queda determinado por el producto vectorial

$$\vec{B} = \frac{1}{\omega}\vec{k}\times\vec{E} = \frac{n}{c}\hat{k}\times\vec{E}\qquad\text{(12.19)}$$

donde $\hat{k}$ es un vector unitario en la dirección del vector $\vec{k}$, la dirección de propagación de la onda.

Estas dos condiciones implican que una onda plana electromagnética real general puede escribirse como

$$\vec{E} = \operatorname{Re}\left(\vec{e}(\vec{k})\,e^{i\vec{k}\cdot\vec{r} - i\omega t}\right), \qquad \vec{B} = \operatorname{Re}\left(\vec{b}(\vec{k})\,e^{i\vec{k}\cdot\vec{r} - i\omega t}\right)\qquad\text{(12.20)}$$

donde los vectores $\vec{e}$ y $\vec{b}$ son, en general, complejos y satisfacen

$$\vec{b}(\vec{k}) = \frac{1}{\omega}\vec{k}\times\vec{e}(\vec{k}) = \frac{n}{c}\hat{k}\times\vec{e}(\vec{k}) \qquad \text{y} \qquad \hat{k}\cdot\vec{e}(\vec{k}) = 0.\qquad\text{(12.21)}$$

Hay dos cosas que señalar sobre las relaciones (12.21):

1.  Basta con especificar la dirección del campo eléctrico, $\vec{e}(\vec{k})$. El campo magnético queda entonces determinado por (12.21). El vector $\vec{e}$ se llama la «polarización» de la onda electromagnética.

2.  Debido a (12.21), la polarización es perpendicular a $\vec{k}$ y, por tanto, vive en un espacio vectorial bidimensional.

En el espacio bidimensional perpendicular a $\vec{k}$ podemos elegir una base de vectores reales, $\hat{e}_1$ y $\hat{e}_2$, donde

$$\hat{e}_1\cdot\hat{k} = \hat{e}_2\cdot\hat{k} = \hat{e}_1\cdot\hat{e}_2 = 0, \qquad \hat{e}_1\times\hat{e}_2 = \hat{k}.\qquad\text{(12.22)}$$

Por ejemplo, para una onda plana que viaja en la dirección $z$, $\hat{k} = \hat{z}$, podríamos tomar $e_1 = \hat{x}$ y $e_2 = \hat{y}$. Entonces podemos escribir

$$\vec{e}(\vec{k}) = \psi_1\hat{e}_1 + \psi_2\hat{e}_2.\qquad\text{(12.23)}$$

Las componentes $\psi_1$ y $\psi_2$ forman el vector bidimensional (12.3) que describe el estado de polarización de la onda electromagnética, igual que describe el estado de polarización de la cuerda.[1] Siempre podemos volver a las componentes del campo eléctrico usando (12.23) y (12.20), y hallar después el campo magnético mediante (12.21).

Ahora toda la discusión sobre ondas transversales en una cuerda, de (12.4) a (12.13), puede trasladarse para describir la luz polarizada. La dirección de desplazamiento de la cuerda se traduce directamente en la dirección del campo eléctrico. Así, la animación del programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-12-1" rel="noopener" target="_blank" title="Animación original de Howard Georgi">12-1</a> se aplica igual de bien al campo eléctrico de una onda polarizada que a la polarización en una cuerda.

### 12.2.2 Energía e intensidad

La densidad de energía en un campo electromagnético es

$$\mathcal{E} = \frac{1}{2}\left(\epsilon\vec{E}^2 + \frac{1}{\mu}\vec{B}^2\right).\qquad\text{(12.24)}$$

Puesto que la densidad de energía es una función no lineal de las intensidades de campo, debemos usar los campos **reales** en (12.24). La densidad de momento es

$$\vec{\mathcal{P}} = \epsilon\,\vec{E}\times\vec{B}.\qquad\text{(12.25)}$$

El vector de Poynting, una medida del flujo de energía, es

$$\vec{S} = c^2\vec{\mathcal{P}}.\qquad\text{(12.26)}$$

Estas magnitudes satisfacen

$$\frac{\partial}{\partial t}\mathcal{E} + \vec{\nabla}\cdot\vec{S} = 0.\qquad\text{(12.27)}$$

El vector de Poynting es útil porque mide la intensidad de la onda, la energía por unidad de tiempo y de área que transporta la onda electromagnética. La relación (12.27) expresa entonces la conservación de la energía: la suma del cambio de la densidad de energía en un punto cualquiera más la energía que fluye alejándose de él es cero.

Para ver qué aspecto tienen estas magnitudes en términos del vector $Z$, calculemos explícitamente los campos eléctrico y magnético usando (12.20) y (12.21). El resultado es

$$\vec{E} = A_1\hat{e}_1\cos(\vec{k}\cdot\vec{r} - \omega t + \phi_1) + A_2\hat{e}_2\cos(\vec{k}\cdot\vec{r} - \omega t + \phi_2),$$

$$\vec{B} = \sqrt{\mu\epsilon}\left(A_1\hat{e}_2\cos(\vec{k}\cdot\vec{r} - \omega t + \phi_1) - A_2\hat{e}_1\cos(\vec{k}\cdot\vec{r} - \omega t + \phi_2)\right).\qquad\text{(12.28)}$$

Sustituyendo esto en (12.24) y (12.26) se obtiene

$$\mathcal{E} = \frac{\epsilon}{4\pi}\left(A_1^2\cos^2(\vec{k}\cdot\vec{r} - \omega t + \phi_1) + A_2^2\cos^2(\vec{k}\cdot\vec{r} - \omega t + \phi_2)\right),\qquad\text{(12.29)}$$

$$\vec{S} = \hat{k}\sqrt{\frac{\epsilon}{\mu}}\,\frac{c}{4\pi}\left(A_1^2\cos^2(\vec{k}\cdot\vec{r} - \omega t + \phi_1) + A_2^2\cos^2(\vec{k}\cdot\vec{r} - \omega t + \phi_2)\right).\qquad\text{(12.30)}$$

*\[Nota de la traducción: las expresiones (12.29) y (12.30) del original llevan un factor $1/4\pi$ que no se sigue de (12.24), donde la densidad de energía se escribe con un $\tfrac{1}{2}$ y sin $4\pi$. Sustituyendo (12.28) en (12.24) se obtiene $\mathcal{E} = \epsilon\left(A_1^2\cos^2(\cdots) + A_2^2\cos^2(\cdots)\right)$. La discrepancia viene de mezclar dos convenios de unidades, y arrastra también a (12.31) y (12.32); se han conservado las fórmulas tal como aparecen en el libro.\]*

Puede comprobar explícitamente que se satisface (12.27). Como $\omega$ es muy grande para las ondas electromagnéticas de interés, casi siempre nos interesan solo los valores promediados en el tiempo de $\mathcal{E}$ y $\vec{S}$. Estos son

$$\langle\mathcal{E}\rangle = \frac{\epsilon}{8\pi}\left(A_1^2 + A_2^2\right),\qquad\text{(12.31)}$$

$$\left\langle\vec{S}\right\rangle = \hat{k}\sqrt{\frac{\epsilon}{\mu}}\,\frac{c}{8\pi}\left(A_1^2 + A_2^2\right).\qquad\text{(12.32)}$$

Nótese que los valores promediados en el tiempo dependen únicamente de la cantidad

$$|Z|^2 \equiv |\psi_1|^2 + |\psi_2|^2 = A_1^2 + A_2^2.\qquad\text{(12.33)}$$

**La intensidad de la luz es proporcional a $|Z|^2$.**

### 12.2.3 Polarización circular y espín

Aunque la polarización lineal es más familiar y quizá más fácil de entender, hay un sentido en el que la polarización circular es más fundamental. La onda plana electromagnética en la dirección $\hat{k}$ puede rotarse alrededor del eje $\hat{k}$ sin que cambie nada salvo su estado de polarización. La simetría de rotación de la física sugiere que deberíamos ser capaces de encontrar estados que se comporten de forma sencilla bajo tal rotación y que simplemente queden multiplicados por un factor de fase. Esos estados son, de hecho, los estados de polarización circular. La acción de una rotación de ángulo $\theta$ alrededor del eje $\hat{k}$ sobre el vector de polarización $Z$ está representada por la matriz

$$R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}.\qquad\text{(12.34)}$$

Por ejemplo, $R_\theta$ actuando sobre $u_1$, (12.4), da $u_\theta$, (12.6):

$$R_\theta\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix}.$$

Pero sobre los estados de polarización circular a izquierdas y a derechas,

$$R_\theta\begin{pmatrix} 1 \\ i \end{pmatrix} = e^{-i\theta}\begin{pmatrix} 1 \\ i \end{pmatrix},$$

$$R_\theta\begin{pmatrix} 1 \\ -i \end{pmatrix} = e^{i\theta}\begin{pmatrix} 1 \\ -i \end{pmatrix}.$$

Esto está relacionado con el hecho de que los estados de polarización circular transportan el máximo momento angular posible, lo que a su vez está relacionado con la propiedad mecanocuántica del espín del fotón.

## 12.3 Láminas de onda y polarizadores

Una razón por la que la polarización es importante es que el estado de polarización de una onda electromagnética puede manipularse con facilidad. Dos de los dispositivos más importantes para tal manipulación son los polarizadores y las láminas de onda.

### 12.3.1 Luz no polarizada

En cualquier haz de luz, en un punto y un instante dados, el campo eléctrico apunta en una dirección determinada. Además, como cualquier onda plana electromagnética de frecuencia angular definida puede describirse mediante (12.20) y (12.21), toda onda plana está polarizada. Sin embargo, en un haz «no polarizado» la onda luminosa consta de un rango de frecuencias angulares con polarizaciones distintas. Como resultado de la interferencia de las distintas componentes armónicas de la onda, la polarización deambula de forma más o menos aleatoria en función del tiempo y del espacio y, en promedio, no se destaca ninguna polarización particular. Un ejemplo sencillo de este aspecto está animado en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-12-2" rel="noopener" target="_blank" title="Animación original de Howard Georgi">12-2</a>, donde representamos un campo eléctrico de la forma

$$E_x(t) = \cos(\omega_1 t + \phi_1) + \cos(\omega_2 t + \phi_2),$$

$$E_y(t) = \cos(\omega_3 t + \phi_3) + \cos(\omega_4 t + \phi_4),$$

donde las fases son aleatorias y las frecuencias se eligen al azar en un rango pequeño alrededor de una frecuencia central. Puede observar cómo el campo $\vec{E}$ deambula por el plano $x$-$y$ hasta acabar llenándolo. Cuanto más estrecho es el rango de frecuencias de la onda, más lentamente deambula la polarización. En el ejemplo del programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-12-2" rel="noopener" target="_blank" title="Animación original de Howard Georgi">12-2</a>, el rango de frecuencias es del orden del 10 % de la frecuencia central, así que la polarización deambula rápidamente. Pero para un haz con una frecuencia bastante bien definida, la polarización será casi constante durante muchos ciclos de la onda. El tiempo durante el cual la polarización es aproximadamente constante se llama tiempo de coherencia de la onda. Para una onda plana de frecuencia definida, el tiempo de coherencia es infinito.

### 12.3.2 Polarizadores

Un «polarizador» es un dispositivo que deja pasar con muy poca absorción la luz polarizada en una dirección determinada (el «eje fácil de transmisión» del polarizador), pero absorbe la mayor parte de la luz polarizada en la dirección perpendicular. Así, un haz de luz no polarizada, al atravesar el polarizador, emerge polarizado a lo largo del eje fácil.

Para las oscilaciones transversales de una cuerda, un polarizador es sencillamente una ranura que permite a la cuerda oscilar en una dirección transversal pero no en la perpendicular.

Para las ondas electromagnéticas, el ejemplo más familiar de polarizador, el Polaroid, fue inventado por Edwin Land hace más de 50 años, en parte en experimentos realizados en el ático del Jefferson Physical Laboratory, donde trabajaba siendo estudiante de grado en Harvard. La idea del polaroid es fabricar un material que conduzca la electricidad (mal) en una dirección, pero no en la otra. Entonces el campo eléctrico en la dirección conductora será absorbido (con la energía yendo a pérdidas resistivas), mientras que el campo eléctrico en la dirección no conductora no se verá afectado. Una manera de conseguirlo es hacer láminas de polímero (alcohol polivinílico) estiradas (para alinear las moléculas del polímero a lo largo de un eje preferente) y dopadas con yodo (para permitir la conducción a lo largo de las moléculas del polímero).[2]

### 12.3.3 Láminas de onda

Las «láminas de onda» son elementos ópticos que cambian la fase relativa de las dos componentes de $Z$. Las láminas de onda son posibles porque existen materiales en los que el índice de refracción depende de la polarización. Esta propiedad se llama «birrefringencia», y puede darse de varias maneras.

Por ejemplo, el celofán, un material polimérico transparente, se convierte en láminas delgadas mediante estirado. A causa del estirado, las cadenas del polímero tienden a orientarse a lo largo de la dirección de estiramiento. La constante dieléctrica de este material depende de la dirección del campo eléctrico: a las cargas les resulta más fácil moverse a lo largo de las cadenas del polímero que atravesarlas. Así, la constante dieléctrica es mayor para campos eléctricos en la dirección de estirado.

El mismo efecto puede surgir por la estructura inherente de un cristal transparente. Un ejemplo es el mineral natural calcita, una forma cristalina del carbonato de calcio, CaCO₃. Los cristales de calcita tienen la fascinante propiedad de desdoblar un haz de luz no polarizada en sus dos estados de polarización. La birrefringencia puede incluso producirse mecánicamente, tensionando un material transparente, es decir, comprimiendo la estructura electrónica en una dirección.

Sea cual sea la forma en que se produzca la birrefringencia, podemos fabricar una lámina de onda orientando el material de modo que las direcciones $x$ e $y$ correspondan a índices de refracción distintos, $n_x$ y $n_y$, y cortando después una rebanada del material en forma de lámina en el plano $x$-$y$, con cierto espesor $\ell$ en la dirección $z$. Entonces una onda electromagnética que viaja en la dirección $z$ a través de la lámina tiene valores de $k$ distintos según su polarización:

$$k = \begin{cases} \dfrac{n_x\omega}{c} & \text{para polarización en la dirección } x \\[6pt] \dfrac{n_y\omega}{c} & \text{para polarización en la dirección } y \end{cases}\qquad\text{(12.38)}$$

En particular, la diferencia de fase entre la luz polarizada en $x$ y en $y$ al atravesar la lámina es

$$\Delta\phi = \frac{(n_x - n_y)\,\omega\,\ell}{c}.\qquad\text{(12.39)}$$

Nótese que, en general, la diferencia de fase $\Delta\phi$ depende de la frecuencia de la luz. Incluso si $n_x$ y $n_y$ dependen de la frecuencia, sería una casualidad extravagante que esa dependencia cancelara la dependencia en $\omega$ del factor explícito de $\omega$ en (12.39).

![Figura 12.5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh12_ES/fig12.5.png)

Figura 12.5: luz inicialmente no polarizada atravesando un par de polarizadores cruzados con una lámina de onda entre ellos.

Consideremos ahora la colocación de una lámina de onda así entre dos polarizadores cruzados, orientados a $\pm 45°$, como se muestra en la figura 12.5. Sin la lámina de onda no pasaría nada de luz, porque el primer polarizador solo transmite luz polarizada a $45°$, descrita por el vector $Z$

$$Z = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}\qquad\text{(12.40)}$$

y el segundo polarizador la absorbe.

Al salir del primer polarizador, el vector $Z$ tiene el aspecto de (12.40) para todas las componentes de frecuencia de la luz blanca. Pero cuando se inserta la lámina de onda en medio, se añade una diferencia de fase dependiente de la frecuencia, de modo que el vector $Z$ que sale de la lámina de onda (salvo una fase global irrelevante) tiene el aspecto

$$Z = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ e^{-i\Delta\phi} \end{pmatrix}.$$

Para las frecuencias tales que $e^{-i\Delta\phi}$ vale $-1$, la luz queda polarizada en la dirección $-45°$ y atraviesa el segundo polarizador sin más atenuación. Pero para las frecuencias tales que $e^{-i\Delta\phi}$ vale $1$, la luz sigue siendo absorbida por el segundo polarizador. Las frecuencias intermedias se absorben parcialmente.

Es esta dependencia con la frecuencia la que produce los interesantes patrones de color que se ven al poner celofán, o un trozo de plástico tensionado, entre polarizadores.

### 12.3.4 Matrices

Los efectos de las láminas de onda, los polarizadores y demás pueden resumirse mediante la multiplicación del vector $Z$ por matrices $2\times2$. Por ejemplo, un polarizador perfecto con el eje formando un ángulo $\theta$ con el eje 1 puede representarse por

$$P_\theta = \begin{pmatrix} \cos^2\theta & \cos\theta\sin\theta \\ \cos\theta\sin\theta & \sin^2\theta \end{pmatrix}.\qquad\text{(12.42)}$$

El objeto $P_\theta$ se denomina «operador de proyección», porque proyecta el vector sobre la dirección paralela a $u_\theta$. Satisface

$$P_\theta P_\theta = P_\theta,\qquad\text{(12.43)}$$

como debe ser, ya que el primer polarizador produce luz polarizada y el segundo la transmite perfectamente. $P_\theta$ actuando sobre un vector transmite la componente en la dirección $\theta$. Esto es más fácil de visualizar si $\theta = 0$ o $\pi/2$. Las matrices

$$P_0 = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \qquad P_{\pi/2} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}\qquad\text{(12.44)}$$

representan polarizadores a lo largo de los ejes 1 y 2 respectivamente.

Una lámina de onda en la que la diferencia de fase es $\pi/2$ se llama «lámina de cuarto de onda». Para una lámina de onda en la que la diferencia de fase está entre $0$ y $\pi$, se acostumbra a llamar «eje rápido» al eje con la fase menor. Una lámina de cuarto de onda con el eje rápido a lo largo del eje 1 se representa por

$$Q_0 = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}.\qquad\text{(12.45)}$$

Obsérvese que podemos escribir

$$Q_0 = P_0 + iP_{\pi/2}.\qquad\text{(12.46)}$$

Esto debería convencerle de que, en general, si el eje rápido está en la dirección $\theta$, la lámina de cuarto de onda tiene el aspecto

$$Q_\theta = P_\theta + iP_{\theta + \pi/2}.\qquad\text{(12.47)}$$

La discusión de (12.39) muestra que, en general, una lámina de onda solo será una lámina de cuarto de onda para luz de una frecuencia definida.

Una lámina de onda en la que la diferencia de fase es $\pi$ se llama «lámina de media onda». Se obtiene una lámina de media onda sustituyendo la $i$ de (12.45)-(12.47) por $-1$. Así,

$$H_\theta = P_\theta - P_{\theta + \pi/2}.\qquad\text{(12.48)}$$

Obsérvese que

$$H_\theta = Q_\theta Q_\theta;\qquad\text{(12.49)}$$

dos láminas de cuarto de onda hacen una lámina de media onda.

![Figura 12.6](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh12_ES/fig12.6.png)

Figura 12.6: producción de luz polarizada circularmente.

He aquí dos dispositivos divertidos que puede construir con estos elementos ópticos (o matrices). Considere la combinación de, primero, un polarizador a $45°$ y después una lámina de cuarto de onda, como se muestra en la figura 12.6. Formando el producto matricial $Q_0 P_{\pi/4}$ puede ver que esto produce luz polarizada circularmente en sentido antihorario a partir de cualquier cosa que tenga una componente de polarización en la dirección $\pi/4$. El argumento es el siguiente. El producto es

$$Q_0 P_{\pi/4} = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}\frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 1 & 1 \\ i & i \end{pmatrix}.\qquad\text{(12.50)}$$

Cuando esto actúa sobre un vector arbitrario se obtiene polarización circular, salvo que el vector sea aniquilado por $P_{\pi/4}$:

$$Q_0 P_{\pi/4}\begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix} = \frac{\psi_1 + \psi_2}{2}\begin{pmatrix} 1 \\ i \end{pmatrix}.\qquad\text{(12.51)}$$

En el orden opuesto, $P_{\pi/4}Q_0$ es un analizador de luz polarizada circularmente: aniquila la luz antihoraria y convierte la luz polarizada en sentido horario en luz polarizada linealmente en la dirección $\pi/4$.

### 12.3.5 Actividad óptica

La «actividad óptica» es una propiedad de muchos compuestos orgánicos y de algunos inorgánicos. Un material ópticamente activo rota la polarización de la luz sin absorber ninguna de las dos componentes de la polarización. Un ejemplo familiar de tal material es el jarabe de maíz, una disolución acuosa espesa de azúcar que probablemente tenga en la cocina. Si pone un recipiente rectangular de jarabe de maíz entre polarizadores, como se muestra en la figura 12.7, y rota el segundo polarizador hasta que la intensidad de la luz que pasa sea máxima, encontrará que la dirección del segundo polarizador no es la misma que la del primero. El plano de la polarización ha sido rotado un cierto ángulo $\theta$. El ángulo de rotación $\theta$ es proporcional al espesor del recipiente, es decir, a la longitud de la región de jarabe que atraviesa la luz.

![Figura 12.7](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh12_ES/fig12.7.png)

Figura 12.7: un recipiente rectangular de jarabe de maíz entre polarizadores.

Está claro que la actividad óptica del jarabe de maíz no puede depender de la estructura cristalina, porque el material es un líquido perfectamente uniforme, completamente invariante bajo rotaciones en el espacio tridimensional. No puede tener ejes especiales ni nada por el estilo. La actividad óptica debe funcionar de manera muy distinta a la birrefringencia.

Puede encontrar una pista sobre la naturaleza de la actividad óptica considerando qué aspecto tiene vista en un espejo. Si refleja el sistema ilustrado en la figura 12.7 en el plano $x$-$z$, cambiando el signo de todas las coordenadas $y$, el ángulo $\theta$ cambia a $-\theta$. Así pues, el jarabe de maíz que ve en un espejo debe ser fundamentalmente distinto del jarabe de maíz de su cocina. Esto no es tan extraño: al fin y al cabo, su mano derecha parece una mano izquierda cuando la mira en un espejo. El jarabe de maíz debe tener la misma propiedad y poseer una «lateralidad» definida. De hecho, a causa de los enlaces tetraédricos de los átomos de carbono con que están construidas, las moléculas de azúcar del jarabe de maíz pueden tener, y tienen, tal lateralidad.

Debido a la lateralidad de las moléculas de azúcar, el índice de refracción del jarabe de maíz depende en realidad de la lateralidad de la luz: es ligeramente distinto para la luz polarizada circularmente a izquierdas y a derechas. Esto ocurre porque el campo $\vec{E}$ de un haz polarizado circularmente gira ligeramente al recorrer cada molécula de azúcar y ve una estructura electrónica algo distinta según el sentido del giro. Entonces, como los índices de refracción son ligeramente distintos, las componentes polarizadas circularmente a izquierdas y a derechas adquieren factores de fase distintos ($k\ell$) al atravesar un espesor $\ell$ del jarabe.

Podemos usar ahora nuestro lenguaje matricial para ver cómo lleva esto a la actividad óptica. Salvo una fase global irrelevante, podemos elegir que la fase producida sobre la luz polarizada circularmente a izquierdas sea $-\theta$ y la producida sobre la polarizada a derechas sea $\theta$. Entonces podemos representar la acción del jarabe sobre una onda arbitraria mediante la matriz

$$e^{-i\theta}P_+ + e^{i\theta}P_-,\qquad\text{(12.52)}$$

donde $P_\pm$ son matrices que seleccionan las componentes polarizadas circularmente a izquierdas y a derechas, respectivamente. Satisfacen

$$P_\pm\begin{pmatrix} 1 \\ \pm i \end{pmatrix} = \begin{pmatrix} 1 \\ \pm i \end{pmatrix}, \qquad P_\pm\begin{pmatrix} 1 \\ \mp i \end{pmatrix} = 0.$$

Puede comprobar que las matrices son

$$P_\pm = \frac{1}{2}\begin{pmatrix} 1 & \mp i \\ \pm i & 1 \end{pmatrix}.\qquad\text{(12.53)}$$

Entonces (12.52) se convierte en

$$e^{-i\theta}\frac{1}{2}\begin{pmatrix} 1 & -i \\ i & 1 \end{pmatrix} + e^{i\theta}\frac{1}{2}\begin{pmatrix} 1 & i \\ -i & 1 \end{pmatrix} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}.\qquad\text{(12.54)}$$

¡Esta es precisamente la matriz de rotación $R_\theta$ de (12.34)! $R_\theta$ rota ambas componentes de cualquier luz un ángulo $\theta$.

Cabe preguntarse por la razón de la lateralidad de las moléculas de azúcar. De hecho, existen procesos físicos —las interacciones débiles, que dan lugar a la radiactividad $\beta$— que se ven distintos al reflejarse en un espejo[3] y que, por tanto, podrían en principio distinguir entre moléculas levógiras y dextrógiras. Sin embargo, lo más probable es que esas interacciones sean irrelevantes para la lateralidad del jarabe de maíz. Probablemente la razón sea biológica, no física. Hace mucho tiempo, cuando los comienzos de la vida emergieron del caldo primordial, por puro accidente se emplearon los azúcares dextrógiros. Desde entonces, la lateralidad se ha mantenido por los procesos de reproducción.

![Figura 12.8](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh12_ES/fig12.8.png)

Figura 12.8: luz inicialmente no polarizada atravesando un par de polarizadores cruzados.

### 12.3.6 Polarizadores cruzados y mecánica cuántica

La polarización ofrece muchas oportunidades de confundirse cuando se piensa en la onda luminosa en términos de fotones. Imaginemos que bajamos la intensidad de la luz hasta el punto de que pasa un fotón cada vez por los polarizadores, y consideremos primero la situación engañosamente simple de luz que se mueve en la dirección $z$ a través de polarizadores cruzados en el plano $x$-$y$. Supongamos que el primer polarizador transmite luz polarizada en la dirección $x$ y el segundo transmite luz polarizada en la dirección $y$. Esto es engañosamente simple porque parece que podemos interpretar lo que ocurre sencillamente en términos de fotones. La situación se representa en la figura 12.8. Parece bastante sencillo de interpretar en términos de fotones: la luz no polarizada de la región I está compuesta a partes iguales por fotones polarizados en la dirección $x$ y en la dirección $y$ (así reza el argumento «clásico», que es erróneo). Los polarizados en la dirección $x$ atraviesan el primer polarizador, de modo que la mitad de los fotones siguen presentes en la región II, donde la intensidad se reduce a la mitad. Después, ninguno de estos atraviesa el segundo polarizador, así que la intensidad en la región III es cero.

Pero compare esto con la situación aparentemente similar en la que el segundo polarizador transmite luz polarizada a $45°$ en el plano $x$-$y$, como se muestra en la figura 12.9. Ahora la descripción ondulatoria nos dice que la intensidad en la región III se reduce en otro factor de 2 respecto de la de la región II. Esto es imposible de interpretar en términos de partículas clásicas. Para verlo, basta con bajar la intensidad de modo que solo pase un fotón cada vez. Entonces el primer polarizador no da problemas: como antes, si el fotón está polarizado en la dirección $x$, pasa. Pero ¿qué ocurre ahora en el segundo polarizador? El fotón no puede partirse: o pasa o no pasa. Para ser coherente con la descripción ondulatoria, en la que la intensidad se reduce en otro factor de dos, la transmisión en el segundo polarizador debe ser un suceso probabilístico. La mitad de las veces el fotón pasa; la mitad de las veces es absorbido. No hay manera de que el fotón de la región II sepa si va a lograrlo. Es aleatorio. Dios juega a los dados.

![Figura 12.9](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh12_ES/fig12.9.png)

Figura 12.9: luz inicialmente no polarizada atravesando un par de polarizadores con los ejes a $45°$.

## 12.4 Contorno entre dieléctricos

Volvamos al contorno plano infinito entre dos dieléctricos que discutimos en el capítulo 9, pero considerando ahora una onda electromagnética que llega con un ángulo arbitrario. Como en el capítulo 5, supondremos que el contorno es el plano $z = 0$ y que para $z < 0$ tenemos constante dieléctrica $\epsilon$, mientras que para $z > 0$ la constante dieléctrica es $\epsilon'$. Suponemos $\mu = 1$ en todas partes.

Por los argumentos generales de invariancia bajo traslación e interacciones locales discutidos en el capítulo anterior, todas las componentes de los campos eléctrico y magnético tendrán la forma general

$$\psi(r, t) \propto e^{i\vec{k}\cdot\vec{r}} + R\,e^{i\tilde{\vec{k}}\cdot\vec{r}} \quad \text{para } z \leq 0$$

$$\psi(r, t) \propto \tau\,e^{i\vec{k}'\cdot\vec{r}} \quad \text{para } z \geq 0$$

donde

$$\tilde{k}_x = k_x, \qquad k'_x = k_x,$$

y

$$\tilde{k}_z = -\sqrt{\omega^2/v^2 - k_x^2} = -k_z, \qquad k'_z = \sqrt{\omega^2/v'^2 - k_x^2}.$$

Así se satisface la ley de Snell, con $\theta$ y $\theta'$ definidos como se muestra en la figura 12.10:

$$k\sin\theta = k'\sin\theta'.$$

Como

$$|\vec{k}| = \sqrt{\mu\epsilon}\,\frac{\omega}{c} = \frac{n\omega}{c},$$

se obtiene

$$n\sin\theta = n'\sin\theta'.$$

![Figura 12.10](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh12_ES/fig12.10.png)

Figura 12.10: dispersión de ondas planas en un contorno plano.

Los detalles de la dispersión dependerán de la polarización. Está claro (por simetría, como de costumbre) que los dos casos serán la polarización en el plano $x$-$z$ y la polarización perpendicular al plano $x$-$z$. Por supuesto, no perdemos nada considerándolos por separado, gracias a la linealidad: cualquier polarización de la onda incidente puede tratarse formando una combinación lineal de las soluciones paralela y perpendicular.

### 12.4.1 Polarización perpendicular al plano de dispersión

Consideremos primero la polarización perpendicular. Esto significa que el campo eléctrico está en la dirección $y$ (saliendo del plano del papel), mientras que el campo magnético está en el plano $x$-$z$:[4]

$$E_y(r, t) = A e^{i(\vec{k}\cdot\vec{r} - \omega t)} + R_\perp A e^{i(\tilde{\vec{k}}\cdot\vec{r} - \omega t)} \quad \text{para } z \leq 0$$

$$E_y(r, t) = \tau_\perp A e^{i(\vec{k}'\cdot\vec{r} - \omega t)} \quad \text{para } z \geq 0$$

$$E_z = E_x = 0$$

Usando (12.19),

$$\vec{B} = \frac{1}{\omega}\vec{k}\times\vec{E} = \frac{n}{c}\hat{k}\times\vec{E},$$

podemos escribir

$$B_x(r, t) = -\frac{n}{c}\cos\theta\,A e^{i(\vec{k}\cdot\vec{r} - \omega t)} + \frac{n}{c}\cos\theta\,R_\perp A e^{i(\tilde{\vec{k}}\cdot\vec{r} - \omega t)} \quad \text{para } z \leq 0$$

$$B_x(r, t) = -\frac{n'}{c}\cos\theta'\,\tau_\perp A e^{i(\vec{k}'\cdot\vec{r} - \omega t)} \quad \text{para } z \geq 0$$

$$B_z(r, t) = \frac{n}{c}\sin\theta\,A e^{i(\vec{k}\cdot\vec{r} - \omega t)} + \frac{n}{c}\sin\theta\,R_\perp A e^{i(\tilde{\vec{k}}\cdot\vec{r} - \omega t)} \quad \text{para } z \leq 0$$

$$B_z(r, t) = \frac{n'}{c}\sin\theta'\,\tau_\perp A e^{i(\vec{k}'\cdot\vec{r} - \omega t)} \quad \text{para } z \geq 0$$

El sistema se muestra en la figura 12.11. Esa figura muestra las direcciones de los campos magnéticos de las ondas componentes incidente ($\vec{B}_i$), reflejada ($\vec{B}_r$) y transmitida ($\vec{B}_t$) en la dispersión de una onda plana electromagnética polarizada paralelamente a un contorno dieléctrico plano. Los vectores $\vec{k}$ se muestran justo debajo de los campos magnéticos. Las condiciones de contorno no triviales son que $E_y$ y $B_x$ sean continuos (esto último porque hemos supuesto $\mu = 1$, así que no hay una lámina de corriente ligada en el contorno). $B_z$ también es continuo, pero eso no aporta información nueva. Así,

$$1 + R_\perp = \tau_\perp$$

![Figura 12.11](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh12_ES/fig12.11.png)

Figura 12.11: dispersión de una onda plana electromagnética polarizada paralelamente a un contorno dieléctrico.

y, como $n \propto |\vec{k}|$,

$$n\cos\theta\,(1 - R_\perp) = n'\cos\theta'\,\tau_\perp,$$

es decir,

$$k_z(1 - R_\perp) = k'_z\,\tau_\perp.$$

Así,

$$\tau_\perp = \frac{2}{1 + \xi_\perp}, \qquad R_\perp = \frac{1 - \xi_\perp}{1 + \xi_\perp}$$

donde

$$\xi_\perp = \frac{k'_z}{k_z}.$$

### 12.4.2 Polarización en el plano de dispersión

La polarización en el plano $x$-$z$ tiene el aspecto

$$B_y(r, t) = A e^{i(\vec{k}\cdot\vec{r} - \omega t)} + R_\parallel A e^{i(\tilde{\vec{k}}\cdot\vec{r} - \omega t)} \quad \text{para } z \leq 0$$

$$B_y(r, t) = \tau_\parallel A e^{i(\vec{k}'\cdot\vec{r} - \omega t)} \quad \text{para } z \geq 0$$

$$B_z = B_x = 0,$$

donde, por comodidad, hemos definido los coeficientes de reflexión y transmisión en términos de los campos magnéticos, y

$$E_x(r, t) = \frac{c}{n}\cos\theta\,A e^{i(\vec{k}\cdot\vec{r} - \omega t)} - \frac{c}{n}\cos\theta\,R_\parallel A e^{i(\tilde{\vec{k}}\cdot\vec{r} - \omega t)} \quad \text{para } z \leq 0$$

$$E_x(r, t) = \frac{c}{n'}\cos\theta'\,\tau_\parallel A e^{i(\vec{k}'\cdot\vec{r} - \omega t)} \quad \text{para } z \geq 0$$

$$E_z(r, t) = -\frac{c}{n}\sin\theta\,A e^{i(\vec{k}\cdot\vec{r} - \omega t)} - \frac{c}{n}\sin\theta\,R_\parallel A e^{i(\tilde{\vec{k}}\cdot\vec{r} - \omega t)} \quad \text{para } z \leq 0$$

$$E_z(r, t) = -\frac{c}{n'}\sin\theta'\,\tau_\parallel A e^{i(\vec{k}'\cdot\vec{r} - \omega t)} \quad \text{para } z \geq 0$$

Ahora las condiciones de contorno no triviales son la continuidad de $B_y$ y de $E_x$. $E_z$ no es continua porque en el contorno dieléctrico se acumula una densidad superficial de carga ligada. Las condiciones de contorno dan

$$1 + R_\parallel = \tau_\parallel$$

$$\frac{\cos\theta}{n}\left(1 - R_\parallel\right) = \frac{\cos\theta'}{n'}\,\tau_\parallel$$

es decir,

$$\tau_\parallel = \frac{2}{1 + \xi_\parallel}, \qquad R_\parallel = \frac{1 - \xi_\parallel}{1 + \xi_\parallel}\qquad\text{(12.74)}$$

donde

$$\xi_\parallel = \frac{\cos\theta'/n'}{\cos\theta/n} = \frac{n\,k'_z}{n'\,k_z}.$$

Una de las cosas interesantes de (12.74) es que cuando

$$\frac{n^2 k'_z}{n'^2 k_z} = 1$$

no hay reflexión. Esta condición se satisface para un ángulo de incidencia especial llamado ángulo de Brewster. Podemos entender el significado del ángulo de Brewster como sigue. De la ley de Snell,

$$\frac{n^2}{n'^2} = \frac{\sin^2\theta'}{\sin^2\theta},$$

y como

$$\frac{k'_z}{k_z} = \frac{k_x/\tan\theta'}{k_x/\tan\theta} = \frac{\tan\theta}{\tan\theta'},$$

la condición se convierte en

$$\frac{n^2 k'_z}{n'^2 k_z} = \frac{\sin\theta'\cos\theta'}{\sin\theta\cos\theta} = 1.$$

Así, $\sin 2\theta = \sin 2\theta'$. Como $\theta \neq \theta'$ (eso sería la situación trivial sin contorno), esto significa que

$$\theta = \pi/2 - \theta'.$$

Dicho de otro modo, el ángulo de Brewster se define por la condición de que las ondas planas reflejada y transmitida sean perpendiculares, como se muestra en el diagrama de la figura 12.12. La relevancia de esta condición está en que la onda reflejada puede pensarse como producida por el movimiento de las cargas del contorno. Pero si estas se mueven en una dirección perpendicular al campo eléctrico de la onda reflejada que habría de producirse, entonces esa onda no puede producirse.

![Figura 12.12](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh12_ES/fig12.12.png)

Figura 12.12: ángulo de Brewster.

## 12.5 Radiación

En esta sección escribimos los campos eléctrico y magnético asociados a densidades de carga y de corriente variables.

### 12.5.1 Campos de cargas en movimiento

Como las ecuaciones de Maxwell son ecuaciones en derivadas parciales, hay que especificar muchas condiciones iniciales o de contorno para determinar las soluciones. Por ejemplo, un campo eléctrico constante en todas partes es solución de las ecuaciones de Maxwell en el espacio libre y, por tanto, se puede sumar un campo constante a cualquier solución y seguirá siendo solución. Tales cosas deben determinarse mediante condiciones físicas iniciales o de contorno. Un conjunto de condiciones que resulta interesante con frecuencia es un análogo de la condición de contorno en el infinito que discutimos para las ondas unidimensionales. Suponga que tiene un universo inicialmente estacionario, sin corrientes eléctricas, sin campos magnéticos y con campos eléctricos debidos solo a cargas estacionarias (que sabe calcular de Física 15b). En cierto instante empieza a mover cargas en alguna región finita del espacio. ¿Cuáles son los campos eléctrico y magnético producidos de este modo? Esta pregunta tiene una respuesta relativamente sencilla, que es una bonita generalización intuitiva de las relaciones que aprendió en 15b para los potenciales eléctrico y vectorial de distribuciones estacionarias de carga y corriente. Aquellas relaciones eran

$$\phi(\vec{r}) = \int d^3r'\,\frac{\rho(\vec{r}')}{|\vec{r} - \vec{r}'|}, \qquad \vec{A}(\vec{r}) = \frac{1}{c}\int d^3r'\,\frac{\vec{J}(\vec{r}')}{|\vec{r} - \vec{r}'|}.$$

Las generalizaciones son

$$\phi(\vec{r}, t) = \int d^3r'\,\frac{\rho(\vec{r}', t - |\vec{r} - \vec{r}'|/c)}{|\vec{r} - \vec{r}'|},\qquad\text{(12.82)}$$

$$\vec{A}(\vec{r}, t) = \frac{1}{c}\int d^3r'\,\frac{\vec{J}(\vec{r}', t - |\vec{r} - \vec{r}'|/c)}{|\vec{r} - \vec{r}'|}.\qquad\text{(12.83)}$$

Es un ejercicio directo, aunque tedioso, de cálculo vectorial demostrar que estas satisfacen las ecuaciones de Maxwell. No voy a hablar de ello (escribiré la deducción en un apéndice para quienes tengan interés), pero merece la pena intentar entender qué significan físicamente estas relaciones. El punto físico importante que implican es que, si las distribuciones de carga y de corriente dependen del tiempo y son ellas las que producen los campos, entonces lo que determina cuál es el campo en un punto $\vec{r}$ son los valores de las distribuciones de carga y corriente en instantes anteriores. Cuanto más lejos está la carga, más anterior tiene que ser el instante. Eso es lo que nos dice el factor $t - |\vec{r} - \vec{r}'|/c$. La aparición de este factor es una especie de condición de contorno en el infinito, coherente con la versión relativista del principio de causalidad. Como la información no puede transferirse más deprisa que la luz, una distribución de carga en un punto del espacio-tiempo $(\vec{r}', t')$ puede afectar a los campos en el punto del espacio-tiempo $(\vec{r}, t)$ solo si $t \geq t'$ y

$$\frac{|\vec{r} - \vec{r}'|}{t - t'} \leq c.$$

Sin embargo, en estas relaciones, (12.82) y (12.83), la condición es todavía más fuerte: una distribución de carga en un punto del espacio-tiempo $(\vec{r}', t')$ puede afectar a los campos en el punto del espacio-tiempo $(\vec{r}, t)$ solo si la luz puede viajar directamente de $(\vec{r}', t')$ a $(\vec{r}, t)$, es decir, si $t \geq t'$ y

$$\frac{|\vec{r} - \vec{r}'|}{t - t'} = c,$$

o bien

$$t - t' = |\vec{r} - \vec{r}'|/c,$$

o bien

$$t' = t - |\vec{r} - \vec{r}'|/c.$$

Esto son solo palabras: ¡no lo hemos deducido! La justificación real de esta discusión llega cuando se comprueba que las relaciones satisfacen efectivamente las ecuaciones de Maxwell. Eso puede esperar a Física 153 o 232 (o al apéndice, si tiene prisa). Con todo, espero que esta discusión haga al menos razonable el resultado. De hecho, ya ha visto el resultado en acción en 15b, en la discusión de Purcell sobre el campo eléctrico de una carga que arranca y se para. Mire las ANIMACIONES — PURCELL: el campo de una carga que se acelera súbitamente. Es una animación de una famosa figura del libro de Purcell. Lo interesante de la animación es el pliegue del campo eléctrico que se propaga hacia fuera desde el suceso de aceleración a la velocidad de la luz — porque es luz. Dentro del pliegue, los campos son los de la carga en movimiento. Fuera del pliegue, los campos son los de la carga estacionaria. El pliegue —la onda electromagnética— es lo que conecta ambas regiones asintóticas. También es divertido compararlo con PURCELL2, que ilustra lo que ocurre si una carga inicialmente en movimiento se detiene súbitamente.

Veamos ahora qué aspecto tienen los campos eléctrico y magnético en un límite importante. La conexión entre los potenciales y los campos es la siguiente:

$$\vec{E} = -\vec{\nabla}\phi - \frac{1}{c}\frac{\partial\vec{A}}{\partial t}, \qquad \vec{B} = \vec{\nabla}\times\vec{A}.$$

Estas relaciones son completamente generales. El límite especial que quiero considerar es aquel en el que las cargas y las corrientes están confinadas en una región pequeña alrededor de $\vec{r} = 0$. Miraremos entonces los campos eléctrico y magnético producidos por las cargas en movimiento lejos de ellas, para $|\vec{r}|$ grande. En realidad es más fácil mirar el campo magnético:

$$\vec{B} = \vec{\nabla}\times\vec{A} = \frac{1}{c}\vec{\nabla}\times\int d^3r'\,\frac{\vec{J}(\vec{r}', t - |\vec{r} - \vec{r}'|/c)}{|\vec{r} - \vec{r}'|}.$$

La cuestión es que el rotacional ($\vec{\nabla}\times$) puede operar en dos sitios distintos: sobre el $1/|\vec{r} - \vec{r}'|$ o sobre el $-|\vec{r} - \vec{r}'|/c$ de la dependencia temporal de $\vec{J}$. El primero da una contribución que decae como $1/r^2$ para $r$ grande, igual que el campo magnético de una distribución de corrientes independiente del tiempo. Pero el segundo da una contribución que solo decae como $1/r$. Así pues, esta contribución domina para $r$ grande. Explícitamente (usando la regla de la cadena), es

$$\begin{aligned}
\vec{B} &\approx -\frac{1}{c^2}\int d^3r'\,\frac{\vec{r} - \vec{r}'}{|\vec{r} - \vec{r}'|^2}\times\frac{d}{dt}\vec{J}(\vec{r}', t - |\vec{r} - \vec{r}'|/c)\\
&\approx -\frac{1}{c^2}\frac{\hat{r}}{r}\times\int d^3r'\,\frac{d}{dt}\vec{J}(\vec{r}', t - |\vec{r} - \vec{r}'|/c),\qquad\text{(12.92)}
\end{aligned}$$

donde en (12.92) hemos despreciado un $\vec{r}'$ en el numerador porque ese término decae como $1/r^2$ para $r$ grande.

Este es el campo magnético de una onda electromagnética. Nótese que es perpendicular a la dirección de movimiento ($\hat{r}$). El decaimiento como $1/r$ es lo que esperamos para una onda electromagnética, porque la densidad de energía va como el cuadrado del campo y decae como $1/r^2$ conforme la onda se extiende.

El campo eléctrico puede calcularse de manera similar, aunque también hace falta usar la conservación de la carga eléctrica,

$$\frac{\partial}{\partial t}\rho + \vec{\nabla}\cdot\vec{J} = 0.$$

Como cabe esperar, el resultado es que el campo eléctrico tiene la misma magnitud que el campo magnético y es perpendicular tanto a la dirección de movimiento como al campo magnético. La parte que corresponde a una onda electromagnética viajera puede escribirse como

$$\vec{E} \approx \frac{1}{c^2}\frac{1}{r}\int d^3r'\;\hat{r}\times\left(\hat{r}\times\frac{d}{dt}\vec{J}(\vec{r}', t - |\vec{r} - \vec{r}'|/c)\right).\qquad\text{(12.95)}$$

Al orden más bajo en $1/r$, para cargas que se mueven con velocidades mucho menores que $c$, podemos simplificar el campo eléctrico de (12.95) sustituyendo

$$|\vec{r} - \vec{r}'| \to r$$

y escribir el resultado como

$$\vec{E}(\vec{r}, t) \approx \frac{1}{c^2}\frac{1}{r}\int d^3r'\;\hat{r}\times\left(\hat{r}\times\frac{d}{dt}\vec{J}(\vec{r}', t - r/c)\right).\qquad\text{(12.97)}$$

La razón de la restricción al movimiento no relativista de las cargas es que, si una partícula cargada se mueve a una velocidad próxima a la de la luz, entonces no podemos despreciar su posición $\vec{r}'$ cuando se mueve hacia $\vec{r}$. Para verlo, considere el límite imposible en el que la carga se mueve hacia el punto $\vec{r}$ a la velocidad de la luz. Entonces, si la carga contribuye al campo eléctrico en $\vec{r}$ en un instante, también contribuye en instantes posteriores, porque la partícula acompaña a la onda luminosa. Aunque $v = c$ es imposible, para $v \approx c$ la dependencia en $\vec{r}'$ no puede ignorarse, porque lleva a una dependencia temporal muy rápida de los potenciales y, por tanto, a campos grandes. Lo que ocurre es que la contribución de las cargas que se mueven relativistamente a los campos eléctricos que tienen delante se ve amplificada por factores de $\frac{c}{c - v}$. Este efecto se usa hoy ampliamente para producir «luz» intensa a partir de aceleradores de partículas: la llamada radiación de sincrotrón. Puede ver este efecto en las ANIMACIONES si hace $v$ próxima a 1.

Un caso particularmente importante e instructivo de (12.97) es el movimiento no relativista de una sola carga $Q$ que se desplaza a lo largo de una trayectoria $\vec{R}(t)$. Para este sistema,[5]

$$\vec{J}(\vec{r}, t) = Q\,\vec{v}(t)\,\delta^3(\vec{r} - \vec{R}(t)) = Q\,\frac{d\vec{R}(t)}{dt}\,\delta^3(\vec{r} - \vec{R}(t)).$$

Entonces la integración sobre $d^3r'$ elimina la función $\delta$, y el campo eléctrico de la onda electromagnética saliente es proporcional a la aceleración:

$$\vec{E}(\vec{r}, t) \approx \frac{1}{c^2}\frac{1}{r}\,Q\;\hat{r}\times\left(\hat{r}\times\vec{a}(t - r/c)\right)\qquad\text{(12.102)}$$

donde

$$\vec{a} = \frac{d^2\vec{R}}{dt^2}.$$

Todo lo que hacen los productos vectoriales con $\hat{r}$ es seleccionar, cambiada de signo, la componente de $\vec{a}(t - r/c)$ perpendicular a $\vec{r}$. Se sigue de la famosa identidad «bac-cab»,

$$\vec{a}\times(\vec{b}\times\vec{c}) = \vec{b}\,(\vec{a}\cdot\vec{c}) - \vec{c}\,(\vec{a}\cdot\vec{b}),$$

que

$$\vec{E}(\vec{r}, t) \approx -\frac{1}{c^2}\frac{1}{r}\,Q\left(\vec{a}(t - r/c) - \hat{r}\,\left(\hat{r}\cdot\vec{a}(t - r/c)\right)\right).$$

Esto tenía que ocurrir, porque el campo eléctrico de una onda electromagnética es perpendicular a su dirección de movimiento. En este caso, para $r$ grande, la onda es casi una onda plana que se mueve en la dirección $\vec{r}$.

### 12.5.2 El diagrama de antena

Hagamos un ejemplo aún más explícito considerando una carga que oscila armónicamente a lo largo del eje $z$,

$$\vec{R}(t) = \ell\,\hat{z}\cos\omega t,$$

de modo que

$$\vec{a}(t) = -\ell\omega^2\,\hat{z}\cos\omega t.$$

Entonces

$$\vec{E}(\vec{r}, t) \approx \frac{\ell\omega^2}{c^2}\frac{1}{r}\,Q\left(\hat{z} - \hat{r}(\hat{r}\cdot\hat{z})\right)\cos[\omega(t - r/c)].$$

El vector $\hat{z} - \hat{r}(\hat{r}\cdot\hat{z})$ es la componente de $\hat{z}$ perpendicular a $\vec{r}$, como se ilustra en la figura 12.13.

![Figura 12.13](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh12_ES/fig12.13.png)

Figura 12.13: la componente de $\hat{z}$ perpendicular a $\vec{r}$.

Evidentemente, la magnitud de $\hat{z} - \hat{r}(\hat{r}\cdot\hat{z})$ es $\sin\theta$. Esto significa que la intensidad de la onda electromagnética a un ángulo $\theta$ del eje $z$ es proporcional a $\sin^2\theta$. El patrón de intensidad puede representarse cómodamente en coordenadas polares, dibujando la intensidad en función de $\theta$. El resultado es el «diagrama de antena» del dipolo oscilante en la dirección $z$, y se muestra en la figura 12.14. Los dos lóbulos del diagrama surgen porque el campo es máximo en el plano $x$-$y$, para $\theta = \pi/2$, y cae a cero conforme nos acercamos al eje $z$, $\theta = 0$ o $\theta = \pi$.

![Figura 12.14](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh12_ES/fig12.14.png)

Figura 12.14: diagrama de antena de un dipolo oscilante.

### 12.5.3 \* Comprobación de las ecuaciones de Maxwell

A estas expresiones se las llama potenciales retardados. Es un nombre confuso, porque en realidad los potenciales no tienen nada de especial. Lo especial es la suposición de una relación concreta entre los potenciales y las cargas y corrientes: que los campos están producidos enteramente por las cargas y las corrientes. Aquí muestro que satisfacen las ecuaciones de Maxwell. Llamo a esto un apéndice porque usted NO es responsable de conocer los detalles. Lo incluyo para su cultura general.

Algunas cuestiones matemáticas que conviene notar sobre la solución: la conservación de la carga,

$$\frac{\partial}{\partial t}\rho + \vec{\nabla}\cdot\vec{J} = 0,$$

implica

$$\frac{1}{c}\frac{\partial\phi}{\partial t} + \vec{\nabla}\cdot\vec{A} = 0.$$

Esto se llama la condición de gauge de Lorentz. Con ella,

$$\vec{\nabla}\cdot\vec{E} = -\nabla^2\phi - \frac{1}{c}\frac{\partial}{\partial t}\vec{\nabla}\cdot\vec{A} = -\nabla^2\phi + \frac{1}{c^2}\frac{\partial^2\phi}{\partial t^2}.$$

Desarrollando el laplaciano sobre la expresión integral de $\phi$ aparecen tres términos: el primero es el que queremos,

$$\int d^3r'\,\rho(\vec{r}', t - |\vec{r} - \vec{r}'|/c)\,4\pi\,\delta^3(\vec{r} - \vec{r}') = 4\pi\,\rho(\vec{r}, t),$$

y los otros dos se cancelan gracias a la forma especial de la variable $t - |\vec{r} - \vec{r}'|/c$. Un cálculo análogo, usando de nuevo la condición de gauge de Lorentz, da la ecuación correspondiente para $\vec{B}$. QED.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Describir la polarización en una cuerda con cuentas o continua;

2.  Escribir la forma general de una onda plana electromagnética y relacionarla con el vector bidimensional $Z$;

3.  Hallar la densidad de energía y de momento de una onda plana electromagnética;

4.  Comprender los estados de polarización posibles de una onda plana;

5.  Analizar sistemas de polarizadores y láminas de onda mediante multiplicación de matrices;

6.  Comprender la conexión entre la actividad óptica y la lateralidad;

7.  Calcular la reflexión y la transmisión de una onda plana electromagnética en un contorno plano entre dieléctricos para cualquier ángulo, y hallar y explicar el ángulo de Brewster.

## Problemas

**12.1.** Una lámina de vidrio de índice de refracción $n = 2$ se sitúa en el plano $x$-$y$, desde $z = 0$ hasta $z = \ell$. Una onda plana de número de onda $k$ (fuera del vidrio) incide sobre la lámina con un ángulo $\theta$ respecto de la perpendicular en el plano $x$-$y$, con $k_z = k\cos\theta$ y $k_x = k\sin\theta$.

Para cada uno de los dos estados de polarización (en la dirección $y$ y en el plano $x$-$z$), alguna fracción de la intensidad se refleja en función de $\theta$ y $k$. En este problema usaremos el método de las matrices de transferencia, discutido en el capítulo 9, para hallarla. Desarrollaremos en detalle el caso de la polarización perpendicular al plano de dispersión $x$-$z$; su tarea será repetir el cálculo para la polarización en el plano $x$-$z$. Para hacerlo, debemos generalizar el análisis de (12.62)-(12.63) y (12.70)-(12.71) a una situación con ondas entrantes y salientes arbitrarias a ambos lados y a un contorno situado en un $z$ arbitrario. Para el estado de polarización perpendicular, las condiciones de contorno son:

$$e^{ik_z z}T_{\perp 1} + e^{-ik_z z}R_{\perp 1} = e^{ik'_z z}T_{\perp 2} + e^{-ik'_z z}R_{\perp 2}$$

$$n\cos\theta\left(e^{ik_z z}T_{\perp 1} - e^{-ik_z z}R_{\perp 1}\right) = n'\cos\theta'\left(e^{ik'_z z}T_{\perp 2} - e^{-ik'_z z}R_{\perp 2}\right)$$

lo que da

$$\begin{pmatrix} T_{\perp 1} \\ R_{\perp 1} \end{pmatrix} = d(z)\begin{pmatrix} T_{\perp 2} \\ R_{\perp 2} \end{pmatrix}$$

donde la matriz de transferencia $d(z)$ es

$$d(z) = \frac{1}{2}\begin{pmatrix} e^{-ik_z z} & 0 \\ 0 & e^{ik_z z} \end{pmatrix}\begin{pmatrix} 1 + h_\perp & 1 - h_\perp \\ 1 - h_\perp & 1 + h_\perp \end{pmatrix}\begin{pmatrix} e^{ik'_z z} & 0 \\ 0 & e^{-ik'_z z} \end{pmatrix}$$

con

$$h_\perp = \frac{n'\cos\theta'}{n\cos\theta}.$$

Pasar del índice $n'$ al índice $n$ en $z$ da una matriz de transferencia que es la inversa de $d(z)$. Aplicando esto al presente problema, si $R_\perp$ y $\tau_\perp$ son los coeficientes de reflexión y transmisión de la lámina de vidrio, tenemos

$$\begin{pmatrix} 1 \\ R_\perp \end{pmatrix} = d(0)\,d(\ell)^{-1}\begin{pmatrix} \tau_\perp \\ 0 \end{pmatrix}$$

lo que implica

$$\tau_\perp = \frac{2h_\perp e^{ik_z\ell}}{2h_\perp\cos k'_z\ell - i(1 + h_\perp^2)\sin k'_z\ell},$$

$$R_\perp = \frac{-i(1 - h_\perp^2)\sin k'_z\ell}{2h_\perp\cos k'_z\ell - i(1 + h_\perp^2)\sin k'_z\ell}.$$

La fracción de la intensidad reflejada es

$$|R_\perp|^2 = \frac{(1 - h_\perp^2)^2\sin^2 k'_z\ell}{4h_\perp^2\cos^2 k'_z\ell + (1 + h_\perp^2)^2\sin^2 k'_z\ell}.$$

Haga ahora el mismo análisis para la polarización en el plano $x$-$z$. Halle $\left|R_\parallel\right|^2$. ¿Qué ocurre en el ángulo de Brewster?

**12.2.** Considere un contorno en $x = 0$ entre dos regiones de espacio vacío. Sobre la superficie de contorno en $x = 0$ hay una capa delgada de material con conductividad superficial $\sigma$. Eso significa que un campo eléctrico $\vec{E}$ con una componente paralela a la superficie (en el plano $y$-$z$) produce una densidad superficial de corriente en la capa de contorno:

$$\vec{J}(y, z) = \left(0,\ \sigma E_y(0, y, z),\ \sigma E_z(0, y, z)\right).$$

En este sistema hay un campo eléctrico de la forma siguiente:

$$E_z(x, y, t) = A e^{i(kx\cos\theta + ky\sin\theta - \omega t)} + R\,A e^{i(-k'x\cos\theta' + k'y\sin\theta' - \omega t)}$$

para $x < 0$, y

$$E_z(x, y, t) = T\,A e^{i(k''x\cos\theta'' + k''y\sin\theta'' - \omega t)}$$

para $x > 0$. $E_x$ y $E_y$ se anulan en todas partes.

Halle $k'$, $k''$, $\theta'$ y $\theta''$. Halle $T$ en términos de $R$. Halle la densidad de corriente en el contorno, $\vec{J}(y, z)$. Halle el campo magnético en todas partes. Halle $R$.

Compruebe su resultado para $R$ explicando el límite $\sigma \to \infty$, una superficie superconductora. ¿Qué le ocurre a $R$ en este límite y por qué?

*Pista: use las ecuaciones de Maxwell para hallar $\vec{B}$ y observe después la discontinuidad del campo magnético a través de la corriente superficial.*

**12.3.** Suponga que en los planos $z = 0$ y $z = a$, para $x \geq 0$, hay dos planos conductores planos semiinfinitos. Suponga además que la oscilación del sistema está forzada por algún dispositivo que produce un campo eléctrico en el plano $x = 0$ para $0 \leq z \leq a$ con las propiedades siguientes: $\vec{E}$ apunta en la dirección $y$, pero su componente $y$ es independiente de $y$ e igual a $E_0\sin(3\pi z/a)\cos(\omega t)$, donde $\omega > 3\pi c/a$ y $c$ es la velocidad de la luz en el vacío. Si esto produce una onda viajera en la dirección $+x$, halle la forma del campo eléctrico en todas partes entre las placas. Si esta onda viajera se usa como onda portadora para señales moduladas en amplitud, ¿con qué velocidad viaja la señal?

**12.4.** Considere las ondas electromagnéticas estacionarias en una caja cúbica evacuada con lados perfectamente conductores en $x = 0$, $x = L$, $y = 0$, $y = L$, $z = 0$ y $z = L$. Existen modos en los que los campos eléctrico y magnético se anulan fuera de la caja y dentro toman la forma siguiente:

$$E_z(x, y, z, t) = A\,\omega\sin k_x x\,\sin k_y y\,\cos\omega t$$

$$B_x(x, y, z, t) = -A\,k_y\sin k_x x\,\cos k_y y\,\sin\omega t$$

$$B_y(x, y, z, t) = A\,k_x\cos k_x x\,\sin k_y y\,\sin\omega t$$

$$E_x = E_y = B_z = 0.$$

Puede comprobar que dentro de la caja, y para una $\omega$ elegida adecuadamente, estos satisfacen las ecuaciones de Maxwell. Halle $\omega$ en función de $k_x$ y $k_y$.

No hay cargas ni corrientes dentro de la caja, pero se acumularán cargas y corrientes en el contorno para confinar los campos eléctrico y magnético dentro de ella. Por ejemplo, aparece una densidad superficial de carga no nula en la parte superior ($z = L$) y en la inferior ($z = 0$). Las cargas oscilan de arriba abajo, mientras que aparecen densidades superficiales de corriente no nulas en todos los lados. La forma anterior está construida para satisfacer las condiciones de contorno apropiadas en los cuatro lados $x = 0$, $y = 0$, $z = 0$ y $z = L$.

Explique la física de las condiciones de contorno para el campo $\vec{E}$ en los lados $x = L$ e $y = L$ y halle los valores permitidos de $k_x$ y $k_y$. Explique después la física de las condiciones de contorno para el campo $\vec{B}$ en los lados $x = L$ e $y = L$ y dibuje un diagrama que explique lo que ocurre para los valores más bajos posibles de $k_x$ y $k_y$. *Pista: recuerde que el campo magnético se anula fuera de la caja.*

**12.5.** Una onda plana de luz que viaja en la dirección $+z$ está polarizada formando un ángulo $\theta$ con el eje $x$ en el plano $x$-$y$. Cuando encuentra una lámina de polaroid en el plano $z = L$ que solo transmite luz polarizada a un ángulo $\theta + \frac{\pi}{2}$, la onda es completamente absorbida. Sin embargo, si la onda plana pasa primero por una lámina de celofán situada en el plano $z = 0$ con el «eje rápido» a lo largo del eje $x$, algo de luz consigue pasar. Suponga que el celofán introduce una diferencia de fase $\phi$ entre la componente de la onda luminosa polarizada a lo largo del eje rápido ($x$) y la componente polarizada a lo largo del eje lento ($y$). Halle la razón entre la intensidad de la onda transmitida más allá del polaroid y la intensidad de la onda incidente, en función de $\theta$ y $\phi$. *Pista: ¿tiende su respuesta a cero cuando $\phi \to 0$? ¿Qué ocurre cuando $\theta \to 0$?*

**12.6.** Una onda plana de luz que viaja en la dirección $+z$ está polarizada en la dirección $x$. Cuando encuentra una lámina de polaroid en el plano $z = L$ que solo transmite luz polarizada en $y$, la onda es completamente absorbida. Sin embargo, si la onda plana pasa primero por una lámina de celofán situada en el plano $z = 0$ con el «eje rápido» formando un ángulo $\theta$ con el eje $x$, algo de luz consigue pasar. Suponga que el celofán introduce una diferencia de fase $\phi$ entre una onda polarizada a lo largo del eje rápido y otra polarizada a lo largo del eje lento. Halle la razón entre la intensidad de la onda transmitida más allá del polaroid y la intensidad de la onda incidente, en función de $\theta$ y $\phi$.

Compare el resultado con el del problema anterior y explique qué está ocurriendo.

**12.7.** Suponga que una carga $Q$ está en reposo en el origen hasta $t = 0$. Desde $t = 0$ hasta $t = \Delta t$, la carga experimenta una aceleración uniforme $a\,\hat{x}$.

**a.** Use (12.102) para hallar una expresión aproximada del campo eléctrico a una distancia grande $r \gg a\,\Delta t^2$ del origen.

**b.** ¿Cómo se compara esto con lo que ve en la animación PURCELL?

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*

[1] A veces se le llama vector de Jones. Véase Hecht, página 323.

[2] Véase Sears, Zemansky y Young, página 813.

[3] Violan lo que se llama la simetría de «paridad».

[4] Las magnitudes $R_\perp$ y $\tau_\perp$ de esta sección, y $R_\parallel$ y $\tau_\parallel$ de la siguiente, se llaman convencionalmente «coeficientes de Fresnel». Véase Hecht, página 97.

[5] Esta ecuación emplea la notación de la función $\delta$. Para un físico, una función $\delta(x)$ es simplemente una función de área 1 tan puntiaguda alrededor de $x = 0$ que no nos importa exactamente qué aspecto tiene. Lo único que importa es el área y dónde está el pico. La $\delta^3(\vec{r} - \vec{R}(t))$ de la ecuación es en realidad el producto de tres funciones delta, para las componentes $x$, $y$ y $z$, y solo dice que $\vec{r} = (x, y, z) = \vec{R}(t) = (X(t), Y(t), Z(t))$, es decir, que la partícula se mueve a lo largo de la trayectoria $\vec{R}(t)$. Para una discusión matemática de la función $\delta$ puede consultar <http://mathworld.wolfram.com/DeltaFunction.html>. Pero no se asuste: es solo un recurso sencillo para ignorar detalles pequeños que no nos importan. Si traduce la integral a palabras o a dibujos, puede que ayude.


---

<!-- MIT8.03_TextCh13_ES.md -->

# Capítulo 13: Interferencia y difracción

Un «haz» de luz nos resulta muy familiar. Un puntero láser, por ejemplo, produce un patrón de luz que se parece bastante a una sección transversal de una onda plana. Pero no del todo: el haz láser se ensancha al viajar. Podría pensar que eso se debe simplemente a las imperfecciones del láser pero, de hecho, por mucho que se esfuerce en perfeccionarlo, no puede evitar cierto ensanchamiento. El problema es la «difracción».

La interferencia es una parte crucial de la física de la difracción. Ya la hemos visto en situaciones unidimensionales, como los interferómetros y la reflexión en películas delgadas. Aquí empezamos a ver las cosas asombrosas que hace en más de una dimensión.

## Vídeos de esta clase (YouTube)

- [Clase 20: Interferencia, pompa de jabón](https://www.youtube.com/watch?v=VkbtIDSHfSc)
- [Clase 21: Radar en fase, interferencia de un solo electrón](https://www.youtube.com/watch?v=mqhO9GT8hD4)
- [Clase 22: Difracción, resolución](https://www.youtube.com/watch?v=FY6iXM9X5Fo)

## Resumen previo

En este capítulo mostramos cómo los fenómenos de interferencia y difracción surgen de la física del problema de oscilación forzada y de las matemáticas de la transformación de Fourier.

1.  Empezamos discutiendo la interferencia de una doble rendija. Este es el ejemplo clásico de interferencia. Damos una discusión heurística de la física y la generalizamos para obtener el resultado fundamental de la óptica de Fourier.

2.  Continuamos después nuestro análisis cuantitativo de la interferencia y la difracción discutiendo de nuevo el problema general como un problema de oscilación forzada. Mostramos la conexión con la formación de un haz. Hallamos la condición de contorno relevante en el infinito y expresamos la solución en forma de integral.

3.  Mostramos cómo la integral se simplifica en dos regiones extremas: muy cerca de la fuente del haz, donde de verdad parece un haz, y muy lejos, donde la difracción se impone y la intensidad de la onda está relacionada con una transformada de Fourier del patrón de onda en la fuente, el mismo resultado que encontramos en nuestra discusión heurística de la interferencia.

4.  Aplicamos estas técnicas a ejemplos con haces formados por una o más rendijas y por regiones rectangulares.

5.  Demostramos un resultado útil, el teorema de convolución, para combinar transformadas de Fourier.

6.  Mostramos cómo los patrones periódicos dan lugar a patrones de difracción nítidos, y discutimos en detalle el ejemplo de la red de difracción.

7.  Aplicamos las mismas ideas al ejemplo tridimensional de la difracción de rayos X en cristales.

8.  Describimos un holograma como un patrón de difracción bastante complicado.

9.  Discutimos las franjas de interferencia y las placas zonales.

## 13.1 Interferencia

### 13.1.1 La doble rendija

La disposición clásica del experimento de la doble rendija se ilustra en la figura 13.1. Hay una pantalla opaca con dos rendijas estrechas en el plano $z = 0$ (mostrada en sección en el plano $x$-$z$; las rendijas salen del papel en la dirección $y$), separadas una pequeña distancia $s$. La pantalla opaca está iluminada por una fuente de luz «puntual». Podría ser, por ejemplo, una bombilla de vidrio transparente con un filtro de color para seleccionar un rango estrecho de frecuencias, muy lejos en la dirección $-z$. Un haz láser expandido con una lente serviría igual de bien. Lo importante es producir en la pantalla opaca una iluminación cuya frecuencia esté en un rango estrecho y en la que la fase de la luz que llega a las dos rendijas esté correlacionada. Eso será ciertamente así si la iluminación para $z < 0$ es casi una onda plana.

![Figura 13.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.1.png)

Figura 13.1: el experimento de la doble rendija.

Ahora ocurre algo interesante en la segunda pantalla, en $z = Z$. Esa «pantalla» podría ser una placa fotográfica, una pantalla translúcida o incluso su retina. Lo que aparece en ella es una serie de líneas brillantes paralelas en la dirección $y$ (paralelas a las rendijas). Si se tapa una de las rendijas, las líneas desaparecen.

Lo que está ocurriendo es interferencia entre los dos caminos rectilíneos posibles por los que la luz puede llegar a la pantalla. En esta sección daremos una discusión heurística y física de la interferencia. Después, en la sección siguiente, deduciremos el mismo resultado usando los argumentos de oscilación forzada y condiciones de contorno que ya conoce de nuestro estudio de las ondas unidimensionales.

La imagen física es esta. El campo eléctrico en $z = Z$ es la suma de los campos que vienen de las dos rendijas. En $x = 0$, en la disposición simétrica de la figura 13.1, los dos caminos posibles de la luz tienen la misma longitud. Por tanto, las dos componentes del campo tienen la misma fase y, en consecuencia, interfieren «constructivamente»: hay una línea brillante en $x = 0$. Al variar $x$, en $z = Z$, cambia la longitud relativa de los dos caminos. Obtenemos entonces posiciones alternas de interferencia constructiva y destructiva, lo que da lugar a las líneas brillantes.

Podemos entender el efecto cuantitativamente calculando explícitamente la longitud de camino. Considere un punto de la pantalla en $x = X$, como se muestra en la figura 13.2. La longitud de la línea de puntos de la figura 13.2 es

$$\sqrt{X^2 + Z^2}.\qquad\text{(13.1)}$$

Para la rendija superior y la inferior, las longitudes de camino son ligeramente menor y mayor, respectivamente. La diferencia total de longitud de camino es

$$\Delta\ell = \sqrt{(X + s/2)^2 + Z^2} - \sqrt{(X - s/2)^2 + Z^2}.\qquad\text{(13.2)}$$

Para $Z \gg s$, podemos desarrollar $\Delta\ell$ de (13.2) en serie de Taylor,

$$\Delta\ell \approx \frac{sX}{Z}.\qquad\text{(13.3)}$$

![Figura 13.2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.2.png)

Figura 13.2: longitudes de camino.

Por tanto, si el número de onda angular de la luz es $k$, la diferencia de fase entre los dos caminos es

$$\frac{ksX}{Z}.\qquad\text{(13.4)}$$

Obtenemos un máximo de intensidad cada vez que la fase es un múltiplo de $2\pi$, es decir, cuando

$$\frac{ksX}{Z} = 2n\pi.\qquad\text{(13.5)}$$

En términos de la longitud de onda, $\lambda = 2\pi/k$, esto es

$$\frac{X}{Z} = \frac{n\lambda}{s}.\qquad\text{(13.6)}$$

### 13.1.2 Óptica de Fourier

Supongamos que, en vez de un simple patrón de dos rendijas, hay en la pantalla opaca algún patrón más complicado. En general, podemos describir la perturbación ondulatoria en el plano $z = 0$ mediante alguna función de $x$ e $y$:[1]

$$f(x, y)\,e^{-i\omega t}.\qquad\text{(13.7)}$$

Nuestra estrategia consistirá en pensar en la onda producida para $z > 0$ por esta función general como una suma de los efectos de agujeros diminutos en todos los valores de $x$ e $y$ para los que $f(x, y)$ es no nula. Para cada trocito de la función podemos calcular la longitud de camino hasta un punto de la pantalla en $z = Z$. Después podemos sumar todos los trozos.

Supongamos, por simplicidad, que $f(x, y)$ solo es no nula en una región pequeña alrededor del origen, de modo que $x$ e $y$ serán pequeños,

$$|x|, |y| \ll |X|, |Y|, Z\qquad\text{(13.8)}$$

para todos los valores relevantes de $x$ e $y$. Ahora bien, la longitud de camino desde el punto $(x, y, 0)$ de la pantalla en $z = 0$ hasta el punto $(X, Y, Z)$ de la pantalla en $z = Z$ es

$$\sqrt{(X - x)^2 + (Y - y)^2 + Z^2}.\qquad\text{(13.9)}$$

Usando (13.8), podemos desarrollar esto como

$$R + \Delta\ell(x, y) + \cdots,\qquad\text{(13.10)}$$

donde

$$R = \sqrt{X^2 + Y^2 + Z^2}\qquad\text{(13.11)}$$

y

$$\Delta\ell(x, y) = -\frac{xX + yY}{R}.\qquad\text{(13.12)}$$

Así, la onda en el camino de $(x, y, 0)$ a $(X, Y, Z)$ adquiere una fase de aproximadamente

$$e^{ik(R + \Delta\ell)}.\qquad\text{(13.13)}$$

Ahora podemos volver a juntar las piezas de la onda para ver cómo funciona la interferencia en el punto $(X, Y, Z)$. Simplemente sumamos sobre todos los valores de $x$ e $y$, con un factor que es la fase por la función $f(x, y)$. Como $x$ e $y$ son variables continuas, la suma es en realidad una integral:

$$\int dx\int dy\, f(x, y)\,e^{ik(R + \Delta\ell)} = e^{ikR}\int dx\int dy\, f(x, y)\,e^{-i(xX + yY)k/R}.\qquad\text{(13.14)}$$

Como veremos con más detalle abajo, esto es una transformada de Fourier bidimensional de la función $f(x, y)$.

La ecuación (13.14) es el resultado fundamental de la óptica de Fourier. Contiene buena parte de la física de la difracción. Hemos hecho al deducirla una serie de suposiciones que merecen más discusión. En la sección siguiente la deduciremos de otra manera, tratando la onda para $z > 0$ como el resultado de una oscilación forzada, producida por la onda en el plano $z = 0$. Eso nos dará una descripción física alternativa de la difracción. Pero será útil tener presente la imagen sencilla de sumar todos los caminos posibles conforme nos adentremos en los fenómenos de interferencia y difracción.

## 13.2 Haces

### 13.2.1 Formando un haz

Considere un sistema con una barrera opaca en el plano $z = 0$. Si se ilumina con una onda plana que viaja en la dirección $+z$, la barrera absorbe la onda por completo. Practique ahora un agujero en la barrera. Podría pensar que eso produciría un haz de luz viajando en la dirección de la onda plana inicial. Pero no es tan sencillo. Este es en realidad el mismo problema que consideramos en la sección anterior, (13.7)-(13.14), con la función $f(x, y)$ dada por

$$f(x, y) = \begin{cases} 1 & \text{dentro de la abertura} \\ 0 & \text{fuera de la abertura.} \end{cases}\qquad\text{(13.16)}$$

De hecho, será útil pensar en el problema más general, porque la función (13.16) es discontinua. Como veremos más adelante, eso lleva a fenómenos de difracción más complicados que los que vemos con una función suave. En particular, supondremos que $f(x, y)$ es significativamente distinta de cero solo para $x$ e $y$ pequeños y tiende a cero para $x$ e $y$ grandes. Entonces podemos hablar de la posición de la «abertura» que produce el haz, cerca de $x = y = 0$.

Podemos pensar en este problema como un problema de oscilación forzada. Es mucho más fácil analizar la física si ignoramos la polarización, así que discutiremos ondas escalares. Podríamos considerar, por ejemplo, las ondas transversales de una membrana flexible o las ondas de presión en un gas. Equivalentemente, podríamos considerar ondas luminosas que dependen solo de dos dimensiones, $x$ y $z$, y polarizadas en la dirección $y$. No nos preocuparemos demasiado por estas sutilezas porque, como de costumbre, las propiedades básicas de los fenómenos ondulatorios están determinadas por propiedades de invariancia bajo traslación que son independientes de qué es lo que está ondulando.

### 13.2.2 Advertencias

Conviene señalar que hay otros enfoques del problema de la difracción además del que discutimos aquí. El montaje físico que estamos considerando es ligeramente distinto del planteamiento estándar de la difracción de Huygens-Fresnel-Kirchhoff, porque estamos estudiando un problema diferente. En la difracción de Huygens-Fresnel-Kirchhoff[2] se considera la difracción de una onda plana por un objeto finito, mientras que nuestra pantalla opaca es infinita en el plano $x$-$y$. En el caso de Huygens-Fresnel, la condición de contorno apropiada es que no hay ondas esféricas entrantes que regresen desde el infinito hacia el objeto que difracta. La difracción produce únicamente ondas esféricas salientes. No discutiremos en detalle este montaje físico alternativo porque lleva más adentro de las funciones de Bessel de lo que nosotros (y probablemente también el lector) estamos dispuestos a ir. La ventaja de nuestra formulación es que podemos plantearla enteramente con las soluciones de onda plana que ya hemos discutido. Simplemente indicaremos las diferencias entre nuestro tratamiento y la difracción de Huygens-Fresnel. Para la difracción en la región frontal, a $z$ grande y no muy lejos del eje $z$, la difracción es la misma en ambos casos.

El lector debería notar también que no hemos explicado exactamente cómo se produce la oscilación $f(x, y)\,e^{-i\omega t}$ en el plano $z = 0$. No es un problema trivial en absoluto, pero no lo discutiremos en detalle. Nos concentramos en la física para $z > 0$, que ya resultará bastante interesante.

### 13.2.3 El contorno en el infinito

Para determinar la forma de las ondas en la región $z > 0$ (más allá de la barrera) necesitamos condiciones de contorno tanto en $z = 0$ como en $z = \infty$. En $z = 0$ hay una amplitud oscilante dada por (13.15).[3] En $z = \infty$ debemos imponer la condición de que no hay ondas viajando en la dirección $-z$ (de vuelta hacia la barrera) y de que las soluciones se comportan bien en $\infty$. Los modos normales tienen la forma

$$e^{i\vec{k}\cdot\vec{r} - i\omega t}$$

donde $\vec{k}$ satisface la relación de dispersión

$$\omega^2 = v^2\vec{k}^2.\qquad\text{(13.18)}$$

Así pues, dadas dos componentes de $\vec{k}$, podemos hallar la tercera usando (13.18). Por tanto, podemos escribir la solución como

$$\psi(\vec{r}, t) = \int dk_x\,dk_y\; C(k_x, k_y)\,e^{i\vec{k}\cdot\vec{r} - i\omega t} \qquad \text{para } z > 0\qquad\text{(13.19)}$$

donde

$$k_z = \sqrt{\omega^2/v^2 - k_x^2 - k_y^2}.\qquad\text{(13.20)}$$

Nótese que (13.20) no determina el signo de $k_z$. Pero la condición de contorno en $\infty$ sí lo hace. Si $k_z$ es real, debe ser positivo para describir una onda que viaja hacia la derecha, alejándose de la barrera. Si $k_z$ es complejo, su parte imaginaria debe ser positiva; de lo contrario, $e^{i\vec{k}\cdot\vec{r}}$ se dispararía cuando $z$ tiende a $\infty$. Así,

$$\text{si } \operatorname{Im}k_z = 0,\ \text{entonces } \operatorname{Re}k_z > 0;\ \text{en caso contrario } \operatorname{Im}k_z > 0.\qquad\text{(13.21)}$$

Discutimos el significado físico de la condición de contorno (13.21) en nuestra discusión del efecto túnel. Hay física real en la condición de contorno en el infinito. Considere, por ejemplo, la relación entre este análisis y la discusión de longitudes de camino de la sección anterior. En el lenguaje del último capítulo, no podemos describir los efectos de las ondas con $k_z$ imaginario. Sin embargo, la condición de contorno (13.21) garantiza que esas componentes de la onda tenderán a cero rápidamente para $z$ grande.

### 13.2.4 El contorno en $z = 0$

Todo lo que necesitamos para determinar la forma de la onda para $z > 0$ es hallar $C(k_x, k_y)$. Para ello implementamos la condición de contorno en $z = 0$ usando (13.19) y poniendo

$$\psi(\vec{r}, t)\big|_{z=0} = f(x, y)\,e^{-i\omega t}\qquad\text{(13.22)}$$

para obtener (13.15). Sacando el factor común $e^{-i\omega t}$, esta condición es

$$f(x, y) = \int dk_x\,dk_y\; C(k_x, k_y)\,e^{i(k_x x + k_y y)}.\qquad\text{(13.23)}$$

Si $f(x, y)$ se comporta bien en el infinito (como ciertamente ocurre si, como hemos supuesto, tiende a cero para $x$ e $y$ grandes), entonces solo pueden contribuir $k_x$ y $k_y$ reales en (13.23). Un $k_x$ complejo produciría una contribución que se dispararía o bien para $x \to +\infty$ o bien para $x \to -\infty$. Así, las integrales de (13.23) recorren $k$ real de $-\infty$ a $\infty$.

(13.23) es sencillamente una transformada de Fourier bidimensional. Usando argumentos análogos a los de nuestra discusión sobre señales, podemos invertirla para hallar $C$:

$$C(k_x, k_y) = \frac{1}{4\pi^2}\int dx\,dy\; f(x, y)\,e^{-i(k_x x + k_y y)}.\qquad\text{(13.24)}$$

Insertar (13.24) en (13.19), con (13.20) y (13.21), da el resultado para la onda $\psi(\vec{r}, t)$ para $z > 0$. Este resultado es realmente muy general: vale para cualquier $f(x, y)$ razonable.

## 13.3 $z$ pequeña y $z$ grande

Pero ¿qué hacemos con él? La integral de (13.19) es demasiado complicada para hacerla analíticamente. Más abajo daremos algunos ejemplos de cómo funciona haciendo la integral numéricamente. Sin embargo, para $z$ pequeña y para $z$ grande, la integral se simplifica de maneras distintas.

### 13.3.1 $z$ pequeña

Para $z$ suficientemente pequeña esperaríamos, por razones físicas, haber producido realmente un haz y proyectado una imagen de la función $f(x, y)$. Para verlo explícitamente, usaremos el hecho de que, para una $f(x, y)$ concreta (y bien comportada), la transformada de Fourier $C(k_x, k_y)$ es una función que tiende a cero para

$$k \equiv \sqrt{k_x^2 + k_y^2} \gg 1/L\qquad\text{(13.25)}$$

para algún $L$ mucho mayor que la longitud de onda. La distancia $L$ está determinada por la suavidad de $f(x, y)$. Típicamente, $L$ es el tamaño del detalle importante más pequeño de $f(x, y)$, la distancia más corta en la que $f(x, y)$ cambia apreciablemente. Vimos esto en nuestra discusión de las transformadas de Fourier en relación con las señales, en el capítulo 10. Veremos más ejemplos abajo. Podemos desarrollar $k_z z$ en el exponente en serie de Taylor:

$$k_z z = z\sqrt{\frac{\omega^2}{v^2} - k_x^2 - k_y^2} = \frac{z\omega}{v}\sqrt{1 - \frac{v^2(k_x^2 + k_y^2)}{\omega^2}} \approx \frac{z\omega}{v} - \frac{zv(k_x^2 + k_y^2)}{2\omega}.\qquad\text{(13.26)}$$

Debido a (13.25), el mayor valor de $\sqrt{k_x^2 + k_y^2}$ que necesitamos en la integral (13.19) es del orden de $1/L$. Para valores mucho mayores, el integrando es cero. Así, el mayor valor posible del segundo término del desarrollo (13.26) que importa en la integral (13.19) es del orden de

$$\frac{zv}{2\omega L^2}.\qquad\text{(13.27)}$$

Por tanto, si $L$ es finito y $z$ es pequeña ($\ll \omega L^2/v$), el segundo término es pequeño y podemos quedarnos solo con el primero, $z\omega/v$. Llevando esto de vuelta a la integral (13.19), tenemos

$$\psi(\vec{r}, t) \approx \int dk_x\,dk_y\, C(k_x, k_y)\,e^{i(k_x x + k_y y)}\,e^{i(z\omega/v - \omega t)} \approx f(x, y)\,e^{i\omega(z - vt)/v}.\qquad\text{(13.28)}$$

Esto es justo lo que esperamos: un haz con la forma de la función original, propagándose en la dirección $z$ con velocidad $v$.

El resultado (13.28) empieza a fallar cuando el siguiente término de la serie de Taylor (13.26) se vuelve importante. Eso ocurre cuando

$$\frac{z\,v\,(k_x^2 + k_y^2)}{\omega} \approx 1.$$

Así,

$$z \approx \frac{\omega L^2}{v} = \frac{2\pi L^2}{\lambda}\qquad\text{(13.29)}$$

marca la transición de un simple haz al comienzo de efectos de difracción importantes.

Si $L = 0$, que es la situación en el ejemplo de una rendija sencilla de anchura $2a$ que analizaremos en detalle más adelante, los efectos de difracción importantes empiezan de inmediato, porque la rendija tiene bordes afilados. Sin embargo, el haz mantiene cierta apariencia de su tamaño original hasta

$$z \approx \frac{\omega a^2}{v}.$$

Para $z$ mayor que $\omega L^2/v$, la dependencia en $k_x$ y $k_y$ del factor $e^{ik_z z}$ no puede ignorarse. En general, evaluar la integral (13.19) es muy difícil. Sin embargo, para $z$ muy grande, $z \gg L$, podemos usar un argumento físico para hallar el resultado de la integral.

### 13.3.2 $z$ grande

Supongamos que está muy lejos, en un punto $\vec{R} = (X, Y, Z)$, con

$$Z \gg \frac{\omega L^2}{v}.\qquad\text{(13.31)}$$

Entonces no puede ver los detalles de la forma de la abertura, ni otros detalles de $f(x, y)$, sino solo su posición. La onda que detecta en algún punto lejano tiene que haber venido de la abertura y, si está suficientemente lejos, es casi una onda plana. A esto se le llama difracción de «Fraunhofer» o de «campo lejano». Si no se satisface esta condición, el problema se llama difracción de «Fresnel» o de «campo cercano». Para que la luz llegue efectivamente a su ojo en la situación de campo lejano, el vector de propagación debe apuntar de la abertura hacia usted. La situación se representa en el diagrama de la figura 13.3. En la región de campo cercano, el ensanchamiento debido a la difracción es del mismo orden que el tamaño de la abertura. Para $Z$ mucho mayor, en la región de campo lejano, el vector $\vec{k}$ debe apuntar de vuelta a la abertura.

![Figura 13.3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.3.png)

Figura 13.3: el problema básico de la difracción — formar un haz.

Así pues, la única contribución a la integral (13.19) que cuenta es la proporcional a $e^{i\vec{k}\cdot\vec{R}}$, donde $\vec{k}$ apunta de la abertura a su ojo. Como el integrando de (13.19) tiene un factor $C(k_x, k_y)$, la amplitud de la onda es proporcional a $C(k_x, k_y)$, donde

$$(k_x, k_y, k_z) = \left(k_x, k_y, \sqrt{\omega^2/v^2 - k^2}\right) \propto (X, Y, Z).\qquad\text{(13.32)}$$

La amplitud es además inversamente proporcional a

$$R = \sqrt{X^2 + Y^2 + Z^2},\qquad\text{(13.33)}$$

porque la intensidad debe decaer como $R^{-2}$, como en una onda esférica, por conservación de la energía. Hay otros factores que contribuyen a la variación de la amplitud además de $C(k_x, k_y)$ (veremos uno más abajo). Sin embargo, típicamente todos esos otros factores varían muy despacio y pueden ignorarse. Así, esperamos que la intensidad para $Z$ grande sea aproximadamente

$$I \propto \frac{|C(k_x, k_y)|^2}{R^2},\qquad\text{(13.34)}$$

donde $\vec{k}$ y $\vec{R}$ están relacionados por (13.32), lo que implica

$$\frac{k_x}{X} = \frac{k_y}{Y} = \frac{k_z}{Z} = \frac{k}{R} = \frac{\omega/v}{R}\qquad\text{(13.35)}$$

o

$$k_x = \frac{kX}{R}, \qquad k_y = \frac{kY}{R}.\qquad\text{(13.36)}$$

¡Y aquí está la clave! Insertando (13.36) en (13.24) se obtiene la integral de (13.14), la que salió de nuestro argumento físico sobre la interferencia. Así pues, nuestra descripción de la onda para $z > 0$ como un problema de oscilación forzada contiene el mismo factor que describe la interferencia de todos los caminos que la onda puede tomar desde la abertura hasta $\vec{R}$. La ventaja de nuestro enfoque actual es que es una deducción de verdad.

También podemos escribir este resultado en términos de ángulos:

$$\sin\theta_x = \frac{X}{R} = \frac{k_x v}{\omega}, \qquad \sin\theta_y = \frac{Y}{R} = \frac{k_y v}{\omega}\qquad\text{(13.37)}$$

donde $\theta_x$ y $\theta_y$ son los ángulos del vector $\vec{r}$ respecto de la línea $X = Y = 0$ en las direcciones $x$ e $y$. O, equivalentemente,

$$X = \frac{Z\,k_x}{\sqrt{\omega^2/v^2 - k_x^2 - k_y^2}}, \qquad Y = \frac{Z\,k_y}{\sqrt{\omega^2/v^2 - k_x^2 - k_y^2}}.\qquad\text{(13.38)}$$

Esto se ilustra en el diagrama de la figura 13.4.

![Figura 13.4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.4.png)

Figura 13.4: relación entre el vector $\vec{k}$ y los ángulos.

### 13.3.3 \* Fase estacionaria

Matemáticamente, (13.32) surge para $Z$ grande porque la fase de la exponencial de (13.19) varía muy rápidamente en función de $k_x$ y $k_y$, salvo para valores especiales de $k_x$ y $k_y$ en los que se anulan las derivadas de la fase respecto de $k_x$ y $k_y$. Si la función está centrada en $x = y = 0$ y es suave, las derivadas de $C(k_x, k_y)$ respecto de $k$ son del orden de $L$ y son irrelevantes. Así, la contribución viene de los $k_x$, $k_y$ tales que

$$\frac{\partial}{\partial k_x}\left(X k_x + Y k_y + Z\sqrt{\omega^2/v^2 - k_x^2 - k_y^2}\right) = X - \frac{Z\,k_x}{\sqrt{\omega^2/v^2 - k_x^2 - k_y^2}} = 0$$

$$\frac{\partial}{\partial k_y}\left(X k_x + Y k_y + Z\sqrt{\omega^2/v^2 - k_x^2 - k_y^2}\right) = Y - \frac{Z\,k_y}{\sqrt{\omega^2/v^2 - k_x^2 - k_y^2}} = 0$$

lo que equivale a (13.38). Una evaluación cuidadosa de la integral, teniendo en cuenta la dependencia en $k_x$ y $k_y$ en el entorno del valor crítico determinado por (13.38), da un factor adicional en la amplitud de la onda de

$$\frac{\cos\theta}{r}$$

donde $\theta$ es el ángulo del vector $\vec{r}$ con el eje $z$. Esperábamos el factor $1/r$ por el ensanchamiento de la onda difractada con la distancia. El factor $\cos\theta$ es en realidad el único sitio donde los detalles de la condición de contorno en el infinito, (13.21), entran en nuestra expresión para la onda difractada. Este factor garantiza que la onda difractada se anula al acercarnos a la superficie de la pantalla opaca lejos de la abertura. Es análogo al factor de «oblicuidad» $(1 + \cos\theta)/2$ de la teoría de difracción de Fresnel-Kirchhoff. La diferencia entre ambos se debe a las distintas condiciones de contorno (nuestra barrera plana infinita frente a la ausencia de ondas esféricas entrantes). Normalmente ignoraremos este factor y, de hecho, no suele suponer mucha diferencia allí donde la difracción es importante en la dirección frontal. Lo importante es que todo lo demás sobre la difracción en la región de campo lejano queda determinado únicamente por la linealidad, la invariancia bajo traslación y las interacciones locales.

### 13.3.4 Tamaño de la mancha

Una manera útil de pensar en la transición de la difracción de campo cercano (Fresnel) a la de campo lejano (Fraunhofer) es considerar el tamaño de la mancha formada por el haz de la figura 13.3 en función de $z$. Es una competición entre dos efectos. Aumentar el tamaño de la abertura hace la mancha más grande a $z$ pequeña. Sin embargo, disminuir el tamaño de la abertura aumenta la anchura en $k_x$, con lo que aumenta la difracción y la mancha se hace más grande a $z$ grande. Para un $z$ dado, lo mejor que puede hacer es elegir el tamaño de la abertura de modo que ambos efectos sean del mismo orden de magnitud. Suponga que el tamaño de su abertura es $\ell$. Entonces la anchura en $k_x$ es del orden de $2\pi/\ell$. A $z$ grande, el haz se abre en un cono con un ángulo de abertura del orden de

$$\theta \approx \frac{\lambda}{\ell}.\qquad\text{(13.40)}$$

Así, cuando

$$\ell \approx \frac{\lambda z}{\ell}, \qquad \text{es decir} \qquad \ell \approx \sqrt{\lambda z},\qquad\text{(13.41)}$$

el ensanchamiento de la mancha por difracción es del mismo orden de magnitud que el tamaño de la abertura. Concluimos que, para minimizar el tamaño de la mancha a un $z$ dado, debe elegir una abertura de tamaño $\ell \approx \sqrt{\lambda z}$.

La relación (13.41), salvo factores de $\pi$, es lo que define la región de difracción de Fresnel en la figura 13.3. Otra manera de resumir el resultado de esta discusión es que, para

$$z \gg \frac{\ell^2}{\lambda},$$

el ensanchamiento debido a la difracción es mucho mayor que el debido al tamaño de la abertura. Esto define la región de campo lejano, o difracción de Fraunhofer.

### 13.3.5 Ángulos

¿Qué ocurre si la onda plana de (13.15) llega a la barrera opaca con un ángulo, en vez de de frente? Concretamente, suponga que el vector $\vec{k}$ de la onda forma un ángulo $\theta$ con la perpendicular en el plano $x$-$z$, de modo que

$$k_z = k\cos\theta, \qquad k_x = k\sin\theta.$$

Entonces es razonable suponer que el análogo de (13.15), la amplitud de la onda en el plano $z = 0$, es[4]

$$f_\theta(x, y) = f(x, y)\,e^{ixk\sin\theta}\qquad\text{(13.46)}$$

donde la dependencia adicional en $x$ se ha heredado simplemente de la dependencia en $x$ de la onda incidente.

Podemos escribir la transformada de Fourier de $f_\theta$ en términos de la de $f$ como sigue:

$$f_\theta(x, y) = \int dk_x\,dk_y\, C(k_x, k_y)\,e^{i(k_x x + k_y y)}e^{ixk\sin\theta} = \int dk_x\,dk_y\, C(k_x - k\sin\theta, k_y)\,e^{i(k_x x + k_y y)},$$

lo que implica

$$C_\theta(k_x, k_y) = C(k_x - k\sin\theta, k_y).\qquad\text{(13.48)}$$

Esto es enteramente razonable. Si el máximo de $C(k_x, k_y)$ ocurre en $k_x \approx 0$, el máximo de $C_\theta(k_x, k_y)$ ocurre en $k_x = k\sin\theta$. Así, el patrón de difracción aparece donde una línea que pasa por la abertura en la dirección de la onda plana incidente cruza la pantalla, justo como esperaríamos de un haz oblicuo.

## 13.4 Ejemplos

### 13.4.1 La rendija sencilla

Suponga

$$f(x, y) = \begin{cases} 1 & \text{para } -a \leq x \leq a \\ 0 & \text{para } |x| > a \end{cases}\qquad\text{(13.49)}$$

independientemente de $y$. Este es en realidad un problema bidimensional, porque podemos mantener $k_y = 0$ e ignorarlo (salvo por un factor $2\pi$, del que no nos preocuparemos) eliminando la integral en $k_y$ de (13.19). Entonces (13.24) queda (con el $2\pi$ corregido para hacerlo unidimensional)[5]

$$C(k_x) = \frac{1}{2\pi}\int dx\, f(x)\,e^{-ik_x x} = \frac{1}{2\pi}\int_{-a}^{a} dx\, e^{-ik_x x} = \left.\frac{e^{-ik_x x}}{-2i\pi k_x}\right|_{-a}^{a} = \frac{\sin k_x a}{\pi k_x}.\qquad\text{(13.51)}$$

Así, esperamos que la intensidad de la onda a $z$ grande sea proporcional a $|C(k_x)|^2$, es decir,

$$I \propto \frac{\sin^2(k_x a)}{k_x^2},\qquad\text{(13.52)}$$

donde

$$\frac{k_x}{k} = \frac{x}{r} = \frac{k_x}{\omega/v} \qquad \text{o} \qquad k_x = \frac{\omega}{v}\frac{x}{r}.\qquad\text{(13.53)}$$

Así, si medimos la intensidad del haz difractado a una distancia $r$ de la abertura, la intensidad va como sigue:[6]

$$I \propto \frac{\sin^2(2\pi a x/r\lambda)}{x^2}\qquad\text{(13.54)}$$

donde $\lambda$ es la longitud de onda de la luz. En la figura 13.5 se muestra $I$ en función de $x$.

Esto se llama un patrón de difracción. En el caso importante de la luz que pasa por una abertura pequeña, el patrón de difracción puede observarse fácilmente proyectando el haz difractado sobre una pantalla. Las características de este patrón que merece la pena señalar son el gran máximo en $x = 0$, con el doble de anchura que todos los demás máximos, y los ceros periódicos en $x = nr\lambda/2a$. Nótese también que, conforme la anchura $a$ de la rendija disminuye, el tamaño del patrón de difracción aumenta.

![Figura 13.5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.5.png)

Figura 13.5: la intensidad del patrón de difracción en función de $x$.

**Moraleja:** esta relación inversa entre el tamaño de la rendija y el tamaño del patrón de difracción es otra ilustración de la propiedad general de las transformadas de Fourier discutida en el capítulo 10.

### 13.4.2 Difracción de campo cercano

Nos detendremos aquí para discutir la región de $z$ intermedia, la difracción de Fresnel, donde el problema de la difracción es complicado. Todo lo que podemos hacer es evaluar la integral (13.19) numéricamente, por ordenador, y hallar aproximadamente la intensidad a distintos valores de $z$. Suponga, por ejemplo, que tomamos

$$\frac{\omega a}{c} = \frac{2\pi a}{\lambda} = 200,$$

que corresponde a una rendija bastante pequeña, con una anchura de solo $100/\pi \approx 32$ veces la longitud de onda de la onda. Usaremos entonces (13.19) para calcular la intensidad de la onda a distintos valores de $z$, en unidades de $a$. Para $z$ pequeña, el resultado se muestra en la figura 13.6. Puede verse que la forma básica del haz se mantiene durante un tiempo, como esperábamos de (13.28). Sin embargo, aparecen ondulaciones de inmediato. La difracción ondulante bastante grande se debe a los bordes afilados. Más abajo daremos otro ejemplo en el que la difracción es mucho más suave. Para $z$ intermedia, mostrada en la figura 13.7, las ondulaciones empiezan a fundirse y a cambiar drásticamente la forma global del haz. Al mismo tiempo, el haz empieza a ensancharse.

![Figura 13.6](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.6.png)

Figura 13.6: la intensidad de una onda que pasa por una rendija, para $z$ pequeña.

![Figura 13.7](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.7.png)

Figura 13.7: la intensidad de una onda que pasa por una rendija, para $z$ intermedia.

Por último, en la figura 13.8 mostramos la aproximación a la región de $z$ grande, donde la difracción se impone por completo y aparece el patrón de difracción de campo lejano, (13.54).

![Figura 13.8](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.8.png)

Figura 13.8: la intensidad de una onda que pasa por una rendija, conforme $z$ se hace grande.

Puede resultar interesante un ejemplo más. Suponga que, en vez de ser un simple agujero en la pantalla opaca, la abertura está sombreada de tal manera que la perturbación ondulatoria en $z = 0$ tiene la forma

$$f(x, y) = e^{-|x|/a}.\qquad\text{(13.56)}$$

La transformada de Fourier se hizo en el capítulo 10, en (10.49)-(10.56). Sustituyendo $\omega \to k_x$ y $\Gamma \to 1/a$ en (10.56) se obtiene

$$C(k_x) = \frac{1}{\pi}\frac{a}{1 + a^2 k_x^2}.\qquad\text{(13.57)}$$

Esto determina la distribución de intensidad a $z$ grande. Sin embargo, a diferencia del ejemplo anterior, este patrón da una difracción muy suave. Para $z$ pequeña, el patrón de intensidad se muestra en la figura 13.9. El pico agudo de (13.56) desaparece, pero por lo demás el cambio es muy gradual, porque el patrón inicial es muy suave excepto en $x = 0$. Para $z$ intermedia y grande, los patrones de intensidad se muestran en las figuras 13.10 y 13.11.

![Figura 13.9](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.9.png)

Figura 13.9: la distribución de intensidad de (13.56) para $z$ pequeña.

![Figura 13.10](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.10.png)

Figura 13.10: la distribución de intensidad de (13.56) para $z$ intermedia.

![Figura 13.11](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.11.png)

Figura 13.11: la distribución de intensidad de (13.56) para $z$ grande.

### 13.4.3 El rectángulo

Suponga

$$f(x, y) = \begin{cases} 1 & \text{para } -a_x \leq x \leq a_x \text{ y } -a_y \leq y \leq a_y, \\ 0 & \text{en caso contrario.} \end{cases}\qquad\text{(13.58)}$$

Este es el producto de un patrón de rendija sencilla en $x$ por un patrón de rendija sencilla en $y$. La transformada de Fourier es el producto de las transformadas de Fourier unidimensionales:

$$C(k_x, k_y) = \frac{1}{4\pi^2}\int_{-a_x}^{a_x} dx\, e^{-ik_x x}\int_{-a_y}^{a_y} dy\, e^{-ik_y y} = \frac{\sin(k_x a_x)}{\pi k_x}\frac{\sin(k_y a_y)}{\pi k_y}.\qquad\text{(13.59)}$$

Así, la intensidad se parece aproximadamente a

$$I \propto \frac{\sin^2(2\pi a_x x/r\lambda)}{x^2}\frac{\sin^2(2\pi a_y y/r\lambda)}{y^2}.\qquad\text{(13.60)}$$

Por supuesto, una vez más, por las propiedades generales de la transformada de Fourier, si el rectángulo es estrecho en $x$, el patrón de difracción se ensancha en $k_x$, y análogamente para $y$.

### 13.4.4 «Funciones» $\delta$

Conforme la rendija de (13.49) se estrecha, el patrón de difracción se ensancha. Por supuesto, la intensidad también disminuye. La intensidad en $k_x = 0$ está relacionada con la transformada de Fourier de $f$ en cero, que es simplemente la integral de $f$ sobre todo $x$. Conforme la rendija se estrecha, esa integral disminuye. Pero suponga que aumentamos la intensidad del haz incidente, conforme $a$ disminuye, para mantener fija la intensidad del máximo del patrón de difracción. Ignorando la dependencia en $y$, exigimos

$$f_a(x) = \begin{cases} \dfrac{1}{2a} & \text{para } -a \leq x \leq a, \\[6pt] 0 & \text{para } |x| > a. \end{cases}\qquad\text{(13.61)}$$

El límite de $f_a$ cuando $a \to 0$ no existe realmente como función. Es cero en todas partes salvo en $x = 0$. Pero tiende a $\infty$ muy deprisa en $x = 0$, de modo que

$$\lim_{a \to 0}\int dx\, f_a(x) = 1.\qquad\text{(13.62)}$$

Resulta extraordinariamente cómodo inventar un objeto con estas propiedades, llamado «función $\delta$». Es decir, $\delta(x)$ tiene la propiedad de ser cero salvo en $x = 0$, y de que

$$\int dx\,\delta(x) = 1.\qquad\text{(13.63)}$$

De hecho, este objeto tiene una especie de sentido matemático, siempre que no se eleve al cuadrado. Las funciones $\delta$ pueden manipularse como funciones ordinarias, sumarse, multiplicarse por constantes o por funciones suaves —incluso pueden multiplicarse funciones $\delta$ de variables distintas—; ¡solo hay que evitar elevarlas al cuadrado! Por ejemplo, una función delta puede multiplicarse por una función continua ordinaria:

$$f(x)\,\delta(x) = f(0)\,\delta(x)\qquad\text{(13.64)}$$

donde la igualdad se sigue de que la función delta se anula salvo en $x = 0$, de modo que solo importa el valor de $f$ en 0.

Ahora debería estar claro, de (13.63) y (13.64), que la transformada de Fourier de $\delta(x)$ es simplemente una constante:

$$\frac{1}{2\pi}\int dx\, e^{-ikx}\,\delta(x) = \frac{1}{2\pi}.\qquad\text{(13.65)}$$

El patrón de difracción de esta cosa es, por tanto, muy aburrido: hay iluminación uniforme en todos los ángulos.

Por supuesto, en física no podemos fabricar funciones $\delta$. Sin embargo, si $a$, en (13.61), es mucho menor que la longitud de onda de la onda, entonces bien podría ser una función $\delta$, porque solo importa cuánto vale $C(k_x)$ para $k_x < k = 2\pi/\lambda$. Los $k_x$ mayores corresponden a ondas exponenciales que se extinguen rápidamente con $z$. Pero para tales $k_x$, el producto $k_x a$ es muy pequeño, así que

$$C(k_x) = \frac{1}{2\pi}\frac{\sin k_x a}{k_x a} \approx \frac{1}{2\pi}\left(1 - \frac{(k_x a)^2}{6} + \cdots\right) \approx \frac{1}{2\pi}\qquad\text{(13.66)}$$

y seguimos obteniendo difracción uniforme en todos los ángulos.

**Moraleja:** las funciones $\delta$ son simplemente una comodidad. Cuando los físicos hablan de una función $\delta$, quieren decir (o al menos deberían querer decir) una función como $f_a(x)$, donde $a$ es menor que cualquier distancia física que importe en el problema. Una vez que $a$ se hace así de pequeña, a menudo es más fácil seguir la pista de las matemáticas si se va hasta el límite no físico, $a = 0$.

### 13.4.5 Algunas propiedades de las funciones $\delta$

La transformada de Fourier de una función $\delta$ es una exponencial compleja:

$$\text{si } f(x) = \delta(x - a), \text{ entonces } C(k) = \frac{1}{2\pi}e^{-ika}.\qquad\text{(13.67)}$$

La transformada de Fourier de una exponencial compleja es una función $\delta$:

$$\text{si } f(x) = e^{-i\ell x}, \text{ entonces } C(k) = \delta(k - \ell).\qquad\text{(13.68)}$$

Se puede llegar a una función $\delta$ como límite de diversas maneras. Por ejemplo, de (13.68) esperaríamos que, cuando $a \to \infty$, la transformada de Fourier de (13.49) se aproximara a una función $\delta$:

$$\lim_{a \to \infty}\frac{\sin k_x a}{\pi k_x} = \delta(k_x).\qquad\text{(13.69)}$$

### 13.4.6 Una dimensión a partir de dos

Usando funciones $\delta$ podemos decir con más elegancia qué se quiere decir con la afirmación que hicimos antes de que, si $f(x, y)$ no depende de $y$, el problema es unidimensional. Si miramos el límite de (13.58) cuando $a_y \to \infty$, pasa a (13.49). Dicho de otro modo, cuando un rectángulo es infinitamente largo, es una rendija. En este límite, la transformada de Fourier (13.59) pasa a

$$C(k_x, k_y) = \frac{\sin(k_x a_x)}{\pi k_x}\,\delta(k_y).\qquad\text{(13.70)}$$

Este es el significado real de (13.50). Es unidimensional en el sentido de que $k_y$ está fijado en 0. No hay difracción en la dirección $y$.

### 13.4.7 Muchas rendijas estrechas

Una aplicación interesante de las funciones $\delta$ es el patrón de difracción de varias rendijas estrechas. Lo usaremos después de varias maneras. Considere una función $f(x, y)$ de la forma

$$f(x, y) = \sum_{j=0}^{n-1}\delta(x - jb).\qquad\text{(13.71)}$$

Esto describe una serie de $n$ rendijas estrechas[7] en $x = 0$, $x = b$, $x = 2b$, etc., hasta $x = (n-1)b$.

La transformada de Fourier de (13.71) es una suma de contribuciones de las funciones $\delta$ individuales; de (13.67) y (13.68),

$$C(k_x, k_y) = \delta(k_y)\sum_{j=0}^{n-1} e^{-ijbk_x}.\qquad\text{(13.72)}$$

Pero la suma es una serie geométrica que puede hacerse explícitamente:

$$\sum_{j=0}^{n-1} e^{-ijbk_x} = \frac{1 - e^{-inbk_x}}{1 - e^{-ibk_x}} = \frac{e^{-inbk_x/2}\left(e^{inbk_x/2} - e^{-inbk_x/2}\right)}{e^{-ibk_x/2}\left(e^{ibk_x/2} - e^{-ibk_x/2}\right)} = e^{-i(n-1)bk_x/2}\,\frac{\sin nbk_x/2}{\sin bk_x/2}.\qquad\text{(13.73)}$$

Así, la intensidad del patrón de difracción es proporcional a

$$\frac{\sin^2 nbk_x/2}{\sin^2 bk_x/2}.\qquad\text{(13.74)}$$

Para $n = 2$, (13.74) es simplemente

$$4\cos^2\frac{bk_x}{2} = 2(1 + \cos bk_x).\qquad\text{(13.75)}$$

Este es el problema con el que empezamos el capítulo. Cuando $bk_x = 2m\pi$ para $m$ entero, la onda de una rendija recorre más camino que la de la otra en $m\lambda$, donde $\lambda = 2\pi/k$ es la longitud de onda. Así, para $bk_x = 2m\pi$ la interferencia es constructiva, como se ilustra en la figura 13.12.

![Figura 13.12](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.12.png)

Figura 13.12: si $bk_x/k = n\lambda$, la interferencia es constructiva.

Para $n$ mayor seguimos obteniendo interferencia constructiva para $bk_x = 2m\pi$, pero los máximos son más agudos, porque con más rendijas hay más posibilidades de interferencia destructiva en otros ángulos. En las figuras 13.13 y 13.14 representamos (13.74) frente a $bk_x$ (de $-\pi$ a $3\pi$, para que pueda ver dos periodos completos) para $n = 3$ y 6. Nótese la aparición de $n - 2$ máximos secundarios entre los máximos principales de la intensidad. Volveremos a estas relaciones cuando discutamos las redes de difracción.

![Figura 13.13](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.13.png)

Figura 13.13: el patrón de difracción de tres rendijas estrechas.

![Figura 13.14](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.14.png)

Figura 13.14: el patrón de difracción de 6 rendijas estrechas.

## 13.5 Convolución

Hay un teorema bastante sencillo, conocido como teorema de convolución, que resulta extremadamente útil al tratar con transformadas de Fourier. Suponga que tenemos dos funciones, $f_1(x)$ y $f_2(x)$. Definimos la función $f_1 \circ f_2$ como sigue:

$$f_1 \circ f_2(x) = \int dy\, f_1(x - y)\,f_2(y).\qquad\text{(13.76)}$$

Esta integral estará bien definida si $f_1(x)$ y $f_2(x)$ decaen suficientemente deprisa en el infinito (y desde luego si son no nulas solo en una región finita de $x$). Nótese que $f_1 \circ f_2$ es una función de una sola variable. Es además simétrica bajo el intercambio de las dos funciones, porque mediante un simple cambio de variables ($y \to x - y$)

$$f_1 \circ f_2(x) = \int dy\, f_1(x - y)\,f_2(y) = \int dy\, f_1(y)\,f_2(x - y) = f_2 \circ f_1(x).\qquad\text{(13.77)}$$

Ahora el teorema dice que la transformada de Fourier de la convolución es $2\pi$ veces el producto de las transformadas de Fourier de las dos funciones. La demostración es inmediata (todas las integrales van de $-\infty$ a $\infty$):

$$C_{f_1 \circ f_2}(k) = \frac{1}{2\pi}\int dx\, e^{ikx}\, f_1 \circ f_2(x) = \frac{1}{2\pi}\int dx\, e^{ikx}\int dy\, f_1(x - y)\,f_2(y).\qquad\text{(13.78)}$$

Ahora sustituimos $x \to y + z$ y escribimos la integral sobre $y$ y $z$:

$$= \frac{1}{2\pi}\int dz\int dy\, e^{ik(y+z)} f_1(z)\,f_2(y) = 2\pi\,C_{f_1}(k)\,C_{f_2}(k).\qquad\text{(13.79)}$$

La versión bidimensional de (13.79) es una extensión directa. La convolución bidimensional es

$$f_1 \circ f_2(x, y) = \int dx'\,dy'\, f_1(x - x', y - y')\,f_2(x', y')\qquad\text{(13.80)}$$

y

$$C_{f_1 \circ f_2}(k_x, k_y) = 4\pi^2\,C_{f_1}(k_x, k_y)\,C_{f_2}(k_x, k_y).\qquad\text{(13.81)}$$

### 13.5.1 Patrones repetidos

El teorema de convolución puede usarse para entender muchas situaciones interesantes. Considere el siguiente patrón, muy instructivo, de dos rendijas anchas:

$$f(x, y) = \begin{cases} 1 & \text{para } -a \leq x \leq a \\ 1 & \text{para } -a \leq x - b \leq a \\ 0 & \text{en caso contrario} \end{cases}\qquad\text{(13.82)}$$

para $b > 2a$. En la figura 13.15 se muestra un fragmento del patrón para $b = 3.5a$.

![Figura 13.15](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.15.png)

Figura 13.15: un fragmento de la barrera opaca con dos rendijas anchas.

Esto puede considerarse la convolución de dos funciones, $f = f_1 \circ f_2$, donde

$$f_1(x, y) = \begin{cases} 1 & \text{para } -a \leq x \leq a \\ 0 & \text{en caso contrario} \end{cases}\qquad\text{(13.84)}$$

y

$$f_2(x, y) = \delta(x)\,\delta(y) + \delta(x - b)\,\delta(y).\qquad\text{(13.85)}$$

Las transformadas de Fourier correspondientes son, de (13.70),

$$C_{f_1}(k_x, k_y) = \frac{\sin(k_x a)}{\pi k_x}\,\delta(k_y)\qquad\text{(13.86)}$$

y, de (13.73),

$$C_{f_2}(k_x, k_y) = \frac{1}{4\pi^2}\,e^{-ibk_x/2}\,\cos\frac{bk_x}{2}\cdot 2.\qquad\text{(13.87)}$$

Aplicando ahora el teorema de convolución se obtiene

$$C_{f_1 \circ f_2}(k_x, k_y) = \cos\frac{bk_x}{2}\;e^{-ibk_x/2}\;\frac{\sin(k_x a)}{\pi k_x}\;\delta(k_y).\qquad\text{(13.88)}$$

Como $b > 2a$, esto describe un patrón que oscila rápidamente en la escala fijada por $1/b$, con una amplitud que varía siguiendo el patrón de difracción de una sola rendija caracterizado por el tamaño $1/a$. El patrón de intensidad sobre una pantalla lejana se muestra en la figura 13.16, para $b = 3.5a$. La línea de puntos es el patrón de una sola rendija ancha (compárese con (13.5)).

![Figura 13.16](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.16.png)

Figura 13.16: el patrón de difracción de dos rendijas anchas.

## 13.6 $f(x, y)$ periódica

Suponga que $f(x, y)$ es periódica en $x$ con periodo $a$, es decir,

$$f(x + a, y) = f(x, y).\qquad\text{(13.89)}$$

Entonces $C(k_x, k_y)$ solo puede ser no nula si

$$k_x = \frac{2\pi n}{a}.\qquad\text{(13.90)}$$

Para verlo, inserte (13.89) en (13.24):

$$C(k_x, k_y) = \frac{1}{4\pi^2}\int dx\,dy\, f(x + a, y)\,e^{i(k_x x + k_y y)}.\qquad\text{(13.91)}$$

Si cambiamos de variable $x \to x - a$, (13.91) es

$$C(k_x, k_y) = \frac{1}{4\pi^2}\int dx\,dy\, f(x, y)\,e^{i(k_x x - k_x a + k_y y)} = e^{-ik_x a}\,C(k_x, k_y)\qquad\text{(13.92)}$$

porque el factor de fase constante puede sacarse fuera de la integral. (13.90) se sigue porque (13.92) implica que, o bien $C(k_x, k_y) = 0$, o bien $e^{-ik_x a} = 1$.

Un ejemplo de este principio general es (13.74). En el límite $n \to \infty$, (13.74) tiende a 0 salvo para $k_x = 2\pi m/b$ con $m$ entero (donde es infinita). Este ejemplo es sencillo porque las rendijas son estrechas, de modo que la intensidad es independiente de $m$. Sin embargo, con rendijas anchas repetidas, o con algún patrón más complicado, podríamos usar el teorema de convolución y (13.74) para ver que (13.90) emerge cuando $n \to \infty$. Los detalles del patrón de cada rendija determinan entonces la intensidad relativa del patrón de difracción para los distintos $m$.

Así, cualquier patrón regular infinito produce una sucesión discreta de $k$. Por ejemplo, una red de difracción por transmisión, que consiste en muchas líneas igualmente espaciadas en la dirección $y$ con separación $a$ en $x$ sobre un sustrato transparente, produce un $C(k_x, k_y)$ que solo es no nulo para $k_y = 0$ (porque no hay dependencia alguna en $y$) y $k_x = 2n\pi/a$. Entonces (13.19) queda

$$\psi \propto \sum_n C_n\, e^{i\left(2n\pi x/a + z\sqrt{\omega^2/v^2 - (2n\pi/a)^2} - \omega t\right)}.\qquad\text{(13.93)}$$

Esto describe una superposición lineal de ondas planas que se abren en abanico con ángulos en la dirección $x$ dados por

$$\sin\theta_n = \frac{2\pi n v}{a\omega} = \frac{n\lambda}{a}\qquad\text{(13.94)}$$

como se muestra en la figura 13.17.

![Figura 13.17](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.17.png)

Figura 13.17: una red de difracción por transmisión desdobla un haz de una sola frecuencia.

Típicamente, en una red de transmisión la mayor parte de la luz va a la línea central, lo que equivale a decir que se puede ver a través de la red. Nótese que el espaciado uniforme en $\sin\theta_n$ de (13.94) corresponde a un espaciado creciente de las líneas proyectadas sobre una pantalla a $z$ grande fijo (por ejemplo, ¡una pantalla como su retina!), porque la distancia a lo largo de la pantalla está determinada por

$$\tan\theta_n = \frac{n\lambda/a}{\sqrt{1 - n^2\lambda^2/a^2}}.\qquad\text{(13.95)}$$

Hay un valor máximo de $n$ por encima del cual no se produce onda propagante (porque corresponde a $\sin\theta > 1$ y, por tanto, a $k_z$ imaginario).

Nótese también la dependencia de (13.94) con la longitud de onda. Cuanto mayor es la longitud de onda de la luz, mayores son los ángulos del patrón de la red de difracción. Esto es, por supuesto, lo que hace útil a la red de difracción: puede separar luz de frecuencias distintas. Los distintos colores del arcoíris se despliegan a lo largo de una línea, para cada valor de $n$. Esto se ilustra en la figura 13.18 para tres frecuencias: luz azul de longitud de onda 4300 Å, luz verde de 5200 Å y luz roja de 6300 Å, incidiendo sobre una red de difracción de 10 000 líneas por pulgada. Hemos representado (13.95) para $n = -3$ a 3 y etiquetado los colores del máximo secundario $n = 1$. Como puede ver, en una red realista los ángulos de difracción pueden ser grandes, y es muy mala idea usar una aproximación de ángulos pequeños.

![Figura 13.18](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.18.png)

Figura 13.18: el patrón de tres frecuencias de luz producido por una red.

### 13.6.1 Girando la red

Algunos ejemplos interesantes de los efectos discutidos en (13.48) se dan cuando la onda luminosa incidente llega a la red formando un ángulo con la perpendicular. Partiendo de las líneas de la red en la dirección $y$ y de la red en el plano $x$-$y$, hay dos efectos distintos.

**1: giro alrededor del eje $y$.** Suponga que la luz llega con un ángulo $\theta_{in}$ respecto de la perpendicular en el plano $x$-$z$. Entonces, de (13.48),

$$C_{\theta_{in}}(k_x, k_y) = C(k_x - k\sin\theta_{in}, k_y)$$

donde $C$ es la transformada de Fourier de la red perpendicular,

$$C(k_x, k_y) \neq 0 \quad \text{para } k_y = 0,\ k_x = \frac{2\pi n}{a}.$$

Así,

$$C_{\theta_{in}}(k_x, k_y) \neq 0 \quad \text{para } k_y = 0,\ k_x = k\sin\theta_{in} + \frac{2\pi n}{a}$$

o

$$\sin\theta = \frac{k_x}{k} = \sin\theta_{in} + \frac{n\lambda}{a}.\qquad\text{(13.99)}$$

Dicho de otro modo, $\sin\theta$ simplemente se desplaza en $\sin\theta_{in}$. Esto significa, por ejemplo, que si $\sin\theta_{in} = \lambda/a$, el patrón es exactamente el mismo, pero el máximo central se ha desplazado, como se muestra en la figura 13.19.

![Figura 13.19](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.19.png)

Figura 13.19: el patrón para un haz que llega con un ángulo $\theta_{in} = \arcsin\lambda/a$.

**2: giro alrededor del eje $x$.** Suponga que la luz llega con un ángulo $\theta_{in}$ respecto de la perpendicular en el plano $y$-$z$. Entonces, de (13.48),

$$C_{\theta_{in}}(k_x, k_y) = C(k_x, k_y - k\sin\theta_{in}).$$

Ahora, en vez de ser 0, $k_y$ está fijado en $k\sin\theta_{in}$:

$$k_y = k\sin\theta_{in}, \qquad k_x = \frac{2\pi n}{a}.$$

Ahora las ondas difractadas forman ángulos no triviales con la perpendicular tanto en $x$ como en $y$:

$$\sin\theta_y = \frac{k_y}{\sqrt{k_y^2 + k_z^2}} = \frac{\sin\theta_{in}}{\sqrt{1 - n^2\lambda^2/a^2}}\qquad\text{(13.101)}$$

y

$$\sin\theta_x = \frac{k_x}{\sqrt{k_x^2 + k_z^2}} = \frac{n\lambda}{a\cos\theta_{in}}.\qquad\text{(13.102)}$$

De nuevo, como en (13.95), lo que vemos si proyectamos el patrón sobre una pantalla perpendicular a $z$ fijo son las tangentes,

$$(x, y)_{\text{pantalla}} = z\,(\tan\theta_x, \tan\theta_y),\qquad\text{(13.103)}$$

donde

$$\tan\theta_x = \frac{k_x}{k_z}, \qquad \tan\theta_y = \frac{k_y}{k_z}.$$

Así, el patrón de difracción aparece curvado. Lo que se ve en una pantalla o en la retina son los colores del arcoíris desplegados a lo largo de una línea curva. Esto se muestra en la figura 13.20, donde representamos $\tan\theta_x$ frente a $\tan\theta_y$ para una fuente de luz y una red como las de la figura 13.18, pero con $\sin\theta_{in} = 0.5$. Nótese que el patrón no solo se ha curvado: también se ha ensanchado respecto del de la figura 13.18. Aquí se ve realmente el vector $\vec{k}$ tridimensional en acción. Conforme $\tan\theta_y$ aumenta, para $k_x$ fijo, $\tan\theta_x$ aumenta también, porque $k_z$ disminuye.

![Figura 13.20](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.20.png)

Figura 13.20: el patrón de difracción de una red girada.

### 13.6.2 Poder de resolución

La discusión hasta aquí ha supuesto que la red de difracción es verdaderamente periódica. Pero eso solo es posible si la red es infinita. En una red finita, solo la parte central es periódica: los bordes rompen la periodicidad. En una red que consta solo de un número finito de surcos, $n$, los picos de difracción no son infinitamente agudos: no son funciones delta. Sin embargo, como se discutió al principio de esta sección, en realidad ya sabemos qué aspecto tienen en el caso finito, porque hemos resuelto el problema de la difracción por $n$ rendijas estrechas igualmente espaciadas, en (13.74). En la situación general de $n$ surcos idénticos, la intensidad se parece a (13.74) multiplicada por alguna función que varía lentamente y que depende de la forma de los surcos (por el teorema de convolución, (13.79)). La consecuencia importante de esto es que la forma de un pico de difracción para una red de $n$ rendijas viene dada aproximadamente por (13.74).

La forma del pico de difracción es importante por la siguiente cuestión práctica. Suponga que tiene un haz de luz que consta de una superposición de luz de dos frecuencias distintas. ¿Cómo de próximas tienen que estar las frecuencias para que sus picos de difracción no triviales se fundan, de modo que no pueda usar su red de difracción para distinguirlas? Cuanto mayor es el número de surcos de la red, más agudos son los picos de difracción y más fácil resulta distinguir frecuencias distintas.

El criterio de Rayleigh es una manera históricamente importante de responder a esta pregunta. Rayleigh supuso que sería posible distinguir los máximos de difracción de ondas igualmente intensas de longitudes de onda ligeramente distintas si el máximo de una frecuencia coincide con el primer mínimo de la otra. Para una red de 6 líneas, este criterio se ilustra en la figura 13.21. La línea continua es la intensidad total de una onda formada por dos frecuencias ligeramente distintas. Las contribuciones de las componentes de frecuencia separadas se indican con las líneas de puntos y de trazos.

![Figura 13.21](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.21.png)

Figura 13.21: el criterio de Rayleigh para una red de 6 líneas.

Cualquier criterio fijo de este tipo para el poder de resolución no debería considerarse un hecho sobre la naturaleza, sino una definición convencional que facilita la comunicación entre experimentadores. Siempre es posible hacerlo mejor que cualquier definición dada acumulando datos precisos sobre la forma de la línea y modelando los detalles.

### 13.6.3 Redes «blazed» (con surcos inclinados)

Como espectroscopio, la red de difracción por transmisión tiene una desventaja frente a un prisma. La dificultad está en que, como señalamos antes, la mayor parte de la luz que incide sobre la red la atraviesa directamente y no se separa en sus frecuencias componentes. Es un problema muy serio en dispositivos en los que la cantidad total de luz es limitada. A menudo es importante que el grueso de la luz vaya a un único valor no nulo de $n$ en (13.94). Entonces casi todos los fotones pueden aprovecharse para la medida, en vez de desperdiciarse en el máximo $n = 0$ (que no lleva información sobre la frecuencia). Como argumentamos antes, no hay ninguna razón teórica por la que no pueda hacerse tal cosa: los principios generales de invariancia bajo traslación e interacciones locales determinan los ángulos de difracción posibles, pero no cuánta luz va a cada ángulo.

De hecho, existe un método práctico y muy usado en las redes de reflexión. Una superficie reflectante con una serie de líneas paralelas igualmente espaciadas grabadas en ella actúa como una red de reflexión, como se ilustra en la figura 13.22. Ahí se muestra una red de reflexión en la que la reflexión predominante de un haz que llega perpendicular al plano de la red es también perpendicular. Lo que queremos, en cambio, es lo que se muestra en la figura 13.23. Para construir una red así, se puede dar forma a los surcos de la red de modo que la reflexión especular en cada surco dirija el haz hacia el máximo de difracción no trivial, como se muestra en la figura 13.24.

![Figura 13.22](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.22.png)

Figura 13.22: una red de difracción por reflexión desdobla un haz de una sola frecuencia.

![Figura 13.23](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.23.png)

Figura 13.23: una red «blazed» dirige el haz hacia un máximo de difracción no trivial.

![Figura 13.24](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.24.png)

Figura 13.24: los surcos de una red «blazed».

Para hacer esto, se puede elegir el ángulo del «blaze» como la mitad del ángulo del primer máximo, $\theta_1 = 2\pi v/a\omega$, en (13.94), como se muestra en la ampliación de un surco de la figura 13.25.

![Figura 13.25](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.25.png)

Figura 13.25: $\theta \approx \theta_1/2$.

## 13.7 \* Difracción de rayos X

Un hermoso ejemplo tridimensional de difracción por una función periódica es la difracción de rayos X en cristales. Un cristal es una disposición regular de átomos cuyas posiciones pueden describirse mediante una función periódica

$$f(\vec{r}) = f(\vec{r} + \vec{a})\qquad\text{(13.106)}$$

donde $\vec{a}$ es cualquier vector que va de un punto de la red a otro. Matemáticamente, podemos definir la red como el conjunto de todos esos vectores. Nótese que la red incluye siempre el vector cero, el punto en el origen. La transformada de Fourier tridimensional de $f(\vec{r})$ es no nula solo para vectores de número de onda de la forma

$$2\pi\sum_j n_j\,\vec{\ell}_j\qquad\text{(13.107)}$$

donde $\vec{\ell}_j$ son los vectores base de la red «dual» o «recíproca», que satisface

$$\vec{a}\cdot\vec{\ell}_j = \text{entero, para todo } \vec{a}.\qquad\text{(13.108)}$$

La idea aquí es la misma que en la discusión unidimensional de la red de difracción, $k_x = 2\pi n/a$, (13.90). La deducción de (13.107) es precisamente análoga a la de (13.90).

Podemos visualizar la relación entre la red y la red dual más fácilmente para «cristales» bidimensionales. Considere, por ejemplo, una red de la forma

$$\vec{a} = n_x a_x\,\hat{x} + n_y a_y\,\hat{y}\qquad\text{(13.109)}$$

mostrada en la figura 13.26 (para $a_x = 2a_y$).

![Figura 13.26](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.26.png)

Figura 13.26: una red cristalina.

Está claro que los vectores de la forma

$$\vec{\ell}_1 = \frac{1}{a_x}\hat{x}, \qquad \vec{\ell}_2 = \frac{1}{a_y}\hat{y}\qquad\text{(13.110)}$$

satisfacen (13.108). Además, pensándolo un poco se convencerá de que son el par más corto de vectores linealmente independientes con esa propiedad. Así, podemos tomar (13.110) como los vectores base de la red dual, de modo que la red dual tiene el aspecto

$$\vec{d}_m = \frac{m_x}{a_x}\hat{x} + \frac{m_y}{a_y}\hat{y}\qquad\text{(13.111)}$$

como se muestra en la figura 13.27. Nótese que los ejes largo y corto se intercambian, como es habitual en un proceso de difracción.

![Figura 13.27](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.27.png)

Figura 13.27: la red dual.

Suponga ahora que una onda plana atraviesa la red infinita,

$$e^{i\vec{k}\cdot\vec{r} - i\omega t}.$$

La onda que resulta de la interacción de la onda plana con la red tiene entonces la forma

$$e^{i\vec{k}\cdot\vec{r} - i\omega t}\,g(\vec{r}),\qquad\text{(13.113)}$$

donde $g(\vec{r})$ es una función periódica, como $f(\vec{r})$ en (13.106). Para hallar las ondas refractadas posibles, debemos escribir esto en la forma

$$e^{i\vec{k}\cdot\vec{r} - i\omega t}\,g(\vec{r}) = \sum_{\text{ondas difractadas},\,\alpha} C_\alpha\, e^{i\vec{k}_\alpha\cdot\vec{r} - i\omega t}.\qquad\text{(13.114)}$$

Pero también sabemos, por la discusión anterior, que la transformada de Fourier de $g$ es no nula solo para valores de $\vec{k}$ de la forma (13.107). Así, (13.114) toma la forma

$$e^{i\vec{k}\cdot\vec{r} - i\omega t}\int d^3k'\, e^{i\vec{k}'\cdot\vec{r}}\,C_g(\vec{k}') = e^{i\vec{k}\cdot\vec{r} - i\omega t}\sum_{n_j} C_{n_j}\, e^{2\pi i\sum_j n_j\vec{\ell}_j\cdot\vec{r}}.\qquad\text{(13.115)}$$

Por tanto, los $\vec{k}_\alpha$ de (13.114) deben tener la forma

$$\vec{k}_\alpha = \vec{k} + 2\pi\sum_j n_j\,\vec{\ell}_j.\qquad\text{(13.116)}$$

Pero esto solo es posible si $\vec{k}_\alpha$ satisface la relación de dispersión en el material, lo que significa, si el material es invariante bajo rotaciones de modo que $\omega^2$ depende solo de $|\vec{k}|^2$, que

$$|\vec{k}_\alpha|^2 = |\vec{k}|^2.\qquad\text{(13.117)}$$

Así, obtenemos una onda difractada solo para los $n_j$ tales que se satisface (13.117). La difracción de rayos X en un cristal puede, por tanto, dar información directa sobre la red dual y, con ella, sobre la propia red cristalina.

Hay una manera más física de pensar en la red dual. Considere cualquier vector de la red dual que no sea múltiplo de otro,

$$\vec{d} = \sum_j n_j\,\vec{\ell}_j.$$

Ahora mire el subconjunto de vectores de la red que satisfacen

$$\vec{d}\cdot\vec{a} = 0.\qquad\text{(13.119)}$$

Este subconjunto es el conjunto de puntos de la red que están en el plano $\vec{d}\cdot\vec{r} = 0$, es decir, el plano perpendicular a $\vec{d}$ que pasa por el origen. Considere ahora el subconjunto

$$\vec{d}\cdot\vec{a} = 1.\qquad\text{(13.120)}$$

Este subconjunto es el conjunto de puntos de la red que están en el plano $\vec{d}\cdot\vec{r} = 1$, paralelo al plano $\vec{d}\cdot\vec{r} = 0$ en la red. Ese plano también es perpendicular a $\vec{d}$ y pasa por el punto (que puede no ser un punto de la red)

$$\frac{\vec{d}}{|\vec{d}|^2}.$$

Por tanto, la distancia perpendicular (es decir, en la dirección de $\vec{d}$) entre los dos planos es $1/|\vec{d}|$.

Podemos continuar esta discusión para concluir que el subconjunto de puntos de la red que satisfacen

$$\vec{d}\cdot\vec{a} = m \quad \text{para } m \text{ entero, de } -\infty \text{ a } \infty\qquad\text{(13.123)}$$

es el conjunto de puntos de la red que están en planos paralelos perpendiculares a $\vec{d}$, con planos adyacentes separados por $1/|\vec{d}|$. ¡Pero ese conjunto debe ser el de todos los puntos de la red! Esto es así porque $\vec{d}\cdot\vec{a}$ es un entero para todos los puntos de la red, por la definición de red dual. Así, todos los puntos de la red están en uno de los planos de (13.123).

Estas consideraciones se ilustran en el cristal bidimensional de las figuras siguientes. Si el vector $\vec{d}$ de la red dual es el mostrado en la figura 13.28, entonces los planos perpendiculares de la red son los de la figura 13.29.

![Figura 13.28](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.28.png)

Figura 13.28: un vector de la red dual.

![Figura 13.29](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.29.png)

Figura 13.29: los planos correspondientes de la red.

Suponga ahora que $\vec{d}$ es uno de los puntos especiales de la red dual que dan lugar a una onda refractada, de modo que

$$|\vec{k} + 2\pi\vec{d}|^2 = |\vec{k}|^2 \implies \vec{d}\cdot\left(\vec{k} + \pi\vec{d}\right) = 0.\qquad\text{(13.124)}$$

Esta relación se muestra en la figura 13.30. Muestra que el vector $k$ de la onda refractada, $\vec{k} + 2\pi\vec{d}$, es simplemente $\vec{k}$ reflejado en un plano perpendicular a $\vec{d}$. Hemos visto que hay un número infinito de tales planos en la red, separados por $1/|\vec{d}|$. La contribución a la onda dispersada de cada uno de esos planos se suma constructivamente a la onda refractada. Para verlo, considere la diferencia de fase entre la onda incidente, $e^{i\vec{k}\cdot\vec{r} - i\omega t}$, y la onda difractada $e^{i\vec{k}_\alpha\cdot\vec{r} - i\omega t}$ para $\vec{k}_\alpha = \vec{k} + 2\pi\vec{d}$. Evidentemente, la diferencia de fase en cualquier punto $\vec{r}$ es

$$2\pi\,\vec{d}\cdot\vec{r}.\qquad\text{(13.125)}$$

![Figura 13.30](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.30.png)

Figura 13.30: la condición de dispersión de Bragg.

Esta diferencia de fase es un múltiplo entero de $2\pi$ en todos los planos

$$\vec{d}\cdot\vec{r} = m \quad \text{para } m \text{ entero, de } -\infty \text{ a } \infty.\qquad\text{(13.126)}$$

Así, la contribución a la dispersión de todos los planos de puntos de la red se suma constructivamente, porque la relación de fase entre la onda incidente y la difractada es la misma en todos ellos. Recíprocamente, si $\vec{k}_\alpha \neq \vec{k} + 2\pi\vec{d}$, las contribuciones de los distintos planos interferirán destructivamente y no resultará ninguna onda difractada.

Esta interpretación física va asociada al nombre de «dispersión de Bragg». Los planos de (13.123) (o (13.126)) son los planos de Bragg del cristal. Nótese que, conforme el vector $\vec{d}$ de la red dual se alarga, los planos de Bragg correspondientes se acercan entre sí, pero son también menos densos, con menos centros dispersores por unidad de área. Generalmente, la dispersión es más débil para $|\vec{d}|$ grande.

## 13.8 Holografía

Nada nos impide analizar el patrón de difracción de una función $f(x, y)$ más complicada que la discutida en (13.16). Un holograma es precisamente uno de esos patrones de difracción. Una de las versiones más sencillas de holograma es aquella en la que un objeto se ilumina con un láser, que proporciona esencialmente una onda plana. La luz reflejada, y una parte del haz láser (extraída mediante alguna técnica de división de haz), inciden sobre una placa fotográfica con ángulos ligeramente distintos, como se muestra esquemáticamente en la figura 13.31. La onda incidente sobre la placa fotográfica tiene la forma

$$e^{-i\omega t}\left(e^{ikz} + \int dk_x\,dk_y\, C(k_x, k_y)\,e^{i\vec{k}\cdot\vec{r}}\right)\qquad\text{(13.127)}$$

donde

$$k = |\vec{k}| = \omega/v.\qquad\text{(13.128)}$$

![Figura 13.31](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.31.png)

Figura 13.31: cómo se hace un holograma.

(13.127) describe las dos partes coherentes de la onda luminosa incidente sobre la placa fotográfica. Por simplicidad, supondremos que la señal que realmente nos interesa, la onda reflejada con transformada de Fourier $C(k_x, k_y)$, es pequeña comparada con la onda de referencia $e^{ikz}$. Esta señal es lo que veríamos si se retirara la placa fotográfica y pusiéramos los ojos en el camino de la onda reflejada, pero fuera del camino del haz láser, como se muestra en la figura 13.32.

![Figura 13.32](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.32.png)

Figura 13.32: viendo el objeto.

La placa fotográfica (supondremos que está en $z = 0$) registra solo la intensidad de la onda total, proporcional a

$$1 + 2\operatorname{Re}\int dk_x\,dk_y\, C(k_x, k_y)\,e^{i(k_x x + k_y y)} + O(C^2).\qquad\text{(13.129)}$$

Descartaremos los términos de orden $C^2$, suponiendo que $C$ es pequeña, aunque más adelante podremos ver que en realidad no supondrán ninguna diferencia aunque $C$ sea grande. Si ahora hacemos una diapositiva positiva a partir de la placa y la iluminamos con un haz láser de la misma frecuencia $\omega$, la onda «pasa» donde la intensidad luminosa sobre la placa era grande y se absorbe donde la intensidad era pequeña. Así, tenemos un problema de oscilación forzada exactamente del tipo que hemos discutido antes, con (13.129) haciendo el papel de $f(x, y)$. La solución para $z > 0$ (de (13.19)-(13.24)) es

$$e^{-i\omega t}\left(e^{ikz} + \int dk_x\,dk_y\, C(k_x, k_y)\,e^{i\vec{k}\cdot\vec{r}} + \text{c.c.}\right)\qquad\text{(13.130)}$$

donde c.c. es la onda compleja conjugada, obtenida tomando el complejo conjugado de la señal y cambiando el signo de la dependencia en $z$ para obtener una onda que viaja en la dirección $+z$.

Lo importante que hay que notar sobre la onda compleja conjugada es que **representa un haz que viaja en una dirección distinta tanto de la señal como del haz de referencia**, porque la conjugación compleja ha cambiado el signo de $k_x$ y $k_y$.

El sistema resultante se muestra esquemáticamente en la figura 13.33. Su ojo ve una versión reconstruida de la onda reflejada que habría visto sin la placa fotográfica, como en la figura 13.32. Nótese que ni el haz de referencia ni el haz complejo conjugado se interponen en su visión, porque salen con ángulos ligeramente distintos. Esto es un holograma. Como no es una fotografía, sino una reconstrucción de la onda real que usted habría visto en la figura 13.32, tiene esa sorprendente propiedad de tridimensionalidad que hace llamativo a un holograma.

![Figura 13.33](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.33.png)

Figura 13.33: viendo la imagen holográfica.

Cabe preguntarse por qué elegimos que el ángulo entre el haz de referencia y la señal sea pequeño. Un ángulo grande tendría la ventaja de apartar más el haz de referencia, pero tendría una desventaja importante. Considere el patrón de intensidad sobre la placa fotográfica que registra el holograma. Es un patrón oscilante con un número de onda típico dado por el valor típico de $k_x$ o $k_y$, que son del orden de $k\sin\theta$, donde $\theta$ es el ángulo entre el haz de referencia y la señal. Pero entonces la distancia entre máximos vecinos sobre la placa fotográfica es del orden de

$$\frac{2\pi}{k\sin\theta} = \frac{\lambda}{\sin\theta}$$

donde $\lambda$ es la longitud de onda de la luz. Como $\lambda$ es una distancia muy pequeña, conviene tomar $\theta$ pequeño para desplegar el patrón sobre la placa fotográfica.

Nótese, además, que los términos de orden $C^2$ que descartamos realmente no hacen ningún daño aunque $C$ no sea pequeña. Como su dependencia en $x$ e $y$ es proporcional a la de la señal por su complejo conjugado, los $k_x$ y $k_y$ típicos de esos términos son cero y viajan aproximadamente en la dirección del haz de referencia. No llegan a su ojo en la figura 13.33.

## 13.9 Franjas y placas zonales

### 13.9.1 La imagen holográfica de un punto

Una de las imágenes holográficas más sencillas es la imagen de un solo punto. Si una onda plana encuentra en su camino un objeto muy pequeño, el objeto producirá una onda esférica. Si la onda plana y la onda esférica son absorbidas después por una placa fotográfica, como se muestra en la figura 13.34, se produce un patrón de interferencia en forma de círculos concéntricos, o franjas.

Concretamente, suponga que la onda plana se propaga en la dirección $z$, que la placa fotográfica está en el plano $x$-$y$ en $z = z_0$ y que ponemos el origen de nuestro sistema de coordenadas en la posición de la fuente de la onda esférica, como se muestra en la figura 13.34. Entonces la combinación lineal de onda plana más onda esférica tiene la forma (ignorando la polarización)

$$A e^{ikz} + \frac{B}{r}e^{ikr}\qquad\text{(13.132)}$$

donde $r = \sqrt{x^2 + y^2 + z^2}$. Supondremos, por simplicidad, que $A$ y $B$ son reales, lo que significa que las dos ondas están en fase en el objeto. La intensidad de la onda en $z = z_0$, sobre la placa fotográfica, es por tanto

$$A^2 + \frac{B^2}{r_0^2} + \frac{2AB}{r_0}\cos\left[k(r_0 - z_0)\right]\qquad\text{(13.133)}$$

donde $r_0$ es la distancia al objeto para un punto del plano $z = z_0$,

$$r_0 = \sqrt{R^2 + z_0^2}\qquad\text{(13.134)}$$

y

$$R = \sqrt{x^2 + y^2}\qquad\text{(13.135)}$$

es la distancia al eje $z$ en el plano $x$-$y$. La intensidad depende solo de $R$, como debe ser por la simetría del sistema bajo rotaciones alrededor del eje $z$.

![Figura 13.34](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.34.png)

Figura 13.34: franjas.

Normalmente nos interesa la región $z_0 \gg R$ porque, como veremos, el patrón de intensidad es más interesante para $R$ pequeña. En esa región, la distancia $r_0$ es muy próxima a $z_0$. Podemos ignorar la variación de $r_0$ en la amplitud $B/r_0$. Sin embargo, hay una dependencia interesante en el término del coseno de (13.133). En ese término podemos desarrollar $r_0$ en serie de Taylor,

$$r_0 = z_0\sqrt{1 + R^2/z_0^2} \approx z_0 + \frac{R^2}{2z_0}.\qquad\text{(13.136)}$$

Poniendo todo junto, la intensidad viene dada aproximadamente, para $z_0 \gg R$, por

$$A^2 + \frac{B^2}{z_0^2} + \frac{2AB}{z_0}\cos\frac{kR^2}{2z_0}.\qquad\text{(13.137)}$$

El patrón de intensidad (13.137) describe «zonas» circulares concéntricas de variación de intensidad. Las zonas pueden etiquetarse por los máximos y mínimos del coseno, en

$$\frac{kR^2}{2z_0} = n\pi\qquad\text{(13.138)}$$

o

$$R^2 = n\lambda z_0\qquad\text{(13.139)}$$

donde $\lambda$ es la longitud de onda de la onda. Para $n$ par, el coseno tiene un máximo y, para $n$ impar, un mínimo. La variación de intensidad es máxima si la onda plana y la onda esférica tienen aproximadamente la misma amplitud en la placa,

$$A \approx \frac{B}{z_0}.\qquad\text{(13.140)}$$

Entonces la amplitud llega efectivamente a cero en los mínimos. La distribución de intensidad en función de $R$ se muestra en la figura 13.35. Las posiciones de los máximos y mínimos, o «zonas», se muestran en el eje $R$. Sobre la placa fotográfica, esta distribución de intensidad da lugar a franjas circulares.

![Figura 13.35](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.35.png)

Figura 13.35: la distribución de intensidad.

Si la placa se revela y se ilumina con una onda plana, se reproduce la onda esférica original junto con otra onda esférica que se mueve hacia dentro, hacia un punto del eje $z$ a una distancia $z_0$ más allá de la placa, como se muestra en la figura 13.36. Esta onda es la imagen real de la figura 13.33. Cuando una onda plana (líneas de puntos) ilumina la placa fotográfica producida en la figura 13.34, se producen ondas esféricas divergentes (líneas de puntos) y convergentes (líneas continuas).

![Figura 13.36](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.36.png)

Figura 13.36: una onda plana iluminando la placa fotográfica.

### 13.9.2 Placas zonales

El holograma de la figura 13.34 puede usarse para enfocar parte de una onda plana. La onda esférica convergente mostrada en la figura 13.36 es mucho más intensa que el resto de la perturbación ondulatoria en el foco, $z = 2z_0$, $x = y = 0$, porque la amplitud de esa parte de la onda aumenta al acercarse al foco. Tiene la forma

$$\frac{1}{r'}e^{ikr'}\qquad\text{(13.141)}$$

donde

$$r' = \sqrt{(z - 2z_0)^2 + x^2 + y^2}.\qquad\text{(13.142)}$$

El mismo efecto puede producirse con una versión caricaturesca de la placa fotográfica, hecha tomando una placa transparente y ennegreciendo las zonas correspondientes a los $n$ negativos de (13.138), donde la distribución de intensidad es menor que la mitad del máximo. Por ejemplo, la primera zona negativa es la región $\lambda z_0/2 < R^2 < 3\lambda z_0/2$; la segunda es la región $5\lambda z_0/2 < R^2 < 7\lambda z_0/2$, etc. El resultado es una «placa zonal». En la figura 13.37 se muestra un ejemplo, producido ennegreciendo las primeras 4 zonas negativas. Estas cosas son bastante útiles, porque pueden producirse fácilmente y adaptarse a cualquier longitud de onda.

![Figura 13.37](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.37.png)

Figura 13.37: una placa zonal.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Plantear un problema de difracción como un problema de oscilación forzada y escribir la onda difractada como una integral de Fourier;

2.  Interpretar la integral de Fourier en la región de campo lejano y hallar el patrón de difracción;

3.  Analizar los patrones de difracción de haces formados con una o más rendijas y con rectángulos;

4.  Usar el teorema de convolución para simplificar el cálculo de transformadas de Fourier;

5.  Analizar la dispersión por una red de difracción y la difracción de rayos X en cristales;

6.  Interpretar un holograma como un patrón de difracción;

7.  Entender cómo una placa zonal puede enfocar una onda plana.

## Problemas

**13.1.** Considere las oscilaciones transversales de una membrana flexible semiinfinita con tensión superficial $T_S$ y densidad superficial de masa $\rho_S$. La membrana está tensada en el plano $z = 0$ desde $y = -\infty$ a $\infty$ y desde $x = 0$ a $\infty$. La membrana se mantiene fija a lo largo de las semirrectas $x = z = 0$, $a \leq y \leq \infty$ y $x = z = 0$, $-\infty \leq y \leq -a$. Para $y$ entre $a$ y $-a$, la membrana se fuerza con frecuencia $\omega$ de modo que el extremo en $x = 0$ se mueve con desplazamiento transversal

$$\psi(0, y, t) = f(y)\,e^{-i\omega t}$$

donde

$$f(y) = \begin{cases} b\left(1 - \dfrac{y}{a}\right) & \text{para } 0 \leq y \leq a \\[6pt] b\left(1 + \dfrac{y}{a}\right) & \text{para } -a \leq y \leq 0 \\[6pt] 0 & \text{para } |y| \geq a. \end{cases}$$

El desplazamiento transversal viene dado por

$$\psi(x, y, t) = \int dk_y\, C(k_y)\,e^{i(yk_y + xk(k_y) - \omega t)}$$

donde $k(k_y)$ es alguna función de $k_y$ y

$$C(k_y) = \frac{1}{2\pi}\int dy\, f(y)\,e^{-ik_y y} = \frac{b}{\pi k_y^2 a}\left(1 - \cos k_y a\right).$$

Halle la función $k(k_y)$.

Si la intensidad de la onda en $x = L$, $y = 0$ para $L$ grande es $I_0$, halle la intensidad para $x = L$ y cualquier valor de $y$. *Pista: suponga que está en la región de campo lejano y tenga en cuenta todos los factores relevantes que contribuyen a la razón entre la intensidad e $I_0$.*

**13.2.** Considere una barrera opaca en el plano $x$-$y$ en $z = 0$, con una sola rendija a lo largo del eje $x$ de anchura $2a$, pero con regiones a cada lado de la rendija, cada una de anchura $2a$, que son parcialmente transparentes y están diseñadas para reducir la intensidad en un factor de 2. Cuando esta barrera se ilumina con una onda plana en la dirección $z$, la amplitud del campo oscilante en $z = 0$ es $f(x, y)\,e^{-i\omega t}$ con

$$f(x, y) = \begin{cases} 1 & \text{para } |y| < a \\[4pt] 1/\sqrt{2} & \text{para } a < |y| < 3a \\[4pt] 0 & \text{para } |y| > 3a. \end{cases}$$

Cerca de la rendija, esto produce simplemente un haz cuya intensidad es la mitad en los bordes. Lejos, sin embargo, el patrón de difracción es bastante distinto del de la rendija sencilla. A una distancia grande fija $R = \sqrt{y^2 + z^2}$ de la rendija, la intensidad en función de

$$\xi = k_y a = \frac{\omega y a}{cR}$$

se muestra en la gráfica de la figura 13.38 para $\xi$ positiva. El valor del pico en $\xi = 0$ está normalizado a 1, pero se ha suprimido en la gráfica para mostrar los detalles de los máximos secundarios.

Halle el menor valor positivo de $\xi$ para el que la intensidad se anula.

Halle la razón entre la intensidad en $\xi = \pi/2$ y la que hay en $\xi = 0$.

Hasta ahora no hemos mencionado la polarización de la luz, suponiendo que es irrelevante. De hecho, obtenemos el patrón mostrado arriba para cualquier polarización, siempre que el sombreado no afecte a la polarización (y $\xi$ sea pequeña). Sin embargo, si la luz está inicialmente polarizada en la dirección $45°$ respecto del eje $x$, podríamos reducir la intensidad a la mitad haciéndola pasar por un polarizador perfecto alineado con el eje $y$. Suponga que nuestra rendija entre $-a$ y $a$ está completamente vacía, pero que entre $-3a$ y $-a$ y entre $a$ y $3a$ ponemos tal polarizador. Ahora, como antes, el haz cerca de la rendija tiene simplemente la intensidad reducida a la mitad en los bordes. Sin embargo, el patrón de difracción es ahora bastante distinto. En función de $\xi$, la intensidad a $R$ grande fija es

$$\left(\frac{\sin 3\xi}{\xi}\right)^2 \ \text{combinada con}\ \left(\frac{\sin\xi}{\xi}\right)^2$$

que no se parece en nada al patrón anterior. Explique la diferencia.

![Figura 13.38](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.38.png)

Figura 13.38: problema 13.2.

**13.3.** Considere una barrera opaca en el plano $x$-$y$ en $z = 0$, con agujeros idénticos centrados en $(x, y) = (n_x a, n_y a)$ para todos los enteros $n_x$ y $n_y$. Suponga que la barrera se ilumina desde $z < 0$ por una onda plana que viaja en la dirección $z$ con longitud de onda $\lambda = a\sqrt{3}/2$. Para $z > 0$, la onda tiene la forma

$$\sum_{m_x, m_y} C_{m_x, m_y}\, e^{i\left(m_x\rho x + m_y\rho y + k_z(m_x, m_y)z - \omega t\right)}$$

donde $m_x$ y $m_y$ recorren todos los enteros.

Halle $\rho$.

Para $z$ grande, solo un número finito de términos de la suma son importantes. ¿Cuántos y cómo lo sabe?

Suponga ahora que, en vez de venir en la dirección $z$, una onda plana con la misma longitud de onda se mueve para $z < 0$ a $45°$ del eje $z$, tanto en el plano $x$-$z$ como en el plano $y$-$z$. Es decir,

$$\frac{k_x}{k_z} = \frac{k_y}{k_z} = \tan 45° = 1.$$

Ahora, para $z > 0$, la onda tiene la forma

$$\sum_{m_x, m_y} C_{m_x, m_y}\, e^{i\left[(m_x\rho + \xi_x)x + (m_y\rho + \xi_y)y + k_z(m_x, m_y)z - \omega t\right]}$$

donde $m_x$ y $m_y$ recorren todos los enteros.

Halle $\xi_x$ y $\xi_y$.

De nuevo, para $z$ grande solo un número finito de términos de la suma son importantes. ¿Cuáles, es decir, qué valores de $m_x$ y $m_y$?

**13.4.** Describa el patrón de difracción que resulta cuando una red de difracción por transmisión con distancia de separación entre líneas $S$ se ilumina con una onda plana de luz monocromática de longitud de onda $L$ que viaja en una dirección perpendicular a las líneas de la red y con un ángulo $\theta$ respecto de la perpendicular a la superficie de la red.

**13.5.** Una pantalla opaca con cuatro rendijas estrechas en $x = \pm 0.6$ mm y $x = \pm 0.4$ mm bloquea un haz de luz coherente de longitud de onda $4\times10^{-5}$ cm. Describa el patrón de difracción que aparece en una pantalla situada a 5 metros.

**13.6.** Una membrana flexible semiinfinita está tensada en el plano $z = 0$ para $x \geq 0$, con tensión superficial $T_s$ y densidad superficial de masa $\rho_s$. La membrana está sujeta en $z = 0$ a lo largo de las dos semirrectas $z = 0$, $x = 0$, $y \geq a$ y $z = 0$, $x = 0$, $y \leq -a$. Para $-a \leq y \leq a$ y $x = 0$, la membrana se ve forzada a oscilar con una amplitud de la forma

$$z = B\,e^{i\omega t}\cos\frac{\pi y}{2a}.$$

Dibuje un diagrama del semiplano $z = 0$ para $x \geq 0$ e indique dónde es grande el promedio del cuadrado del valor absoluto del desplazamiento transversal de la membrana (es decir, no mucho menor que $B^2 a/r$, donde $r$ es la distancia al origen). Para su diagrama, suponga que la distancia $a$ es unas 5 veces la longitud de onda de las ondas.

Halle la intensidad de la perturbación en la membrana producida por esta oscilación forzada en función de $\theta = \tan^{-1}(y/x)$ sobre un semicírculo grande, $x^2 + y^2 = R^2$, para $R^2 \gg a^4\omega^2\rho_s/T_s$.

*Pista: esto es similar a un problema de difracción por una rendija sencilla. Nótese que, aunque la perturbación es un coseno, tendrá que hacer una integral de Fourier (aunque no difícil) para hacer el apartado b, porque la perturbación está confinada a $-a \leq y \leq a$ en $x = 0$.*

**13.7.** Suponga que una red de difracción con separación entre líneas $d$ está grabada sobre la cara superior de una pieza gruesa de vidrio de índice de refracción $n$. Si luz de frecuencia $\omega$ incide sobre la cara superior, llegando con un ángulo $\theta$ respecto de la perpendicular a la cara y perpendicular a las líneas de la red, halle los ángulos de las componentes de la onda dentro del vidrio.

**13.8.** En la figura 13.39 se muestran 4 patrones de difracción como los que podrían producirse haciendo pasar luz láser (casi una onda plana) por una rendija o unas rendijas, y proyectando el patrón sobre una placa fotográfica lejana. Cada patrón está producido por unos 500 fotones individuales que golpean la placa con una densidad de probabilidad proporcional a la intensidad de la onda difractada.

![Figura 13.39](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh13_ES/fig13.39.png)

Figura 13.39: cuatro patrones de difracción.

Los cuatro objetos que produjeron estos patrones fueron, en orden aleatorio:

1.  Una rendija sencilla de 1 mm de anchura;

2.  Una rendija sencilla de 0.6 mm de anchura;

3.  Dos rendijas, cada una de 0.6 mm de anchura, con los centros separados 1.5 mm;

4.  Seis rendijas, cada una de 0.6 mm de anchura, con centros adyacentes separados 1.5 mm.

**a.** ¿Cuál es cuál?

**b.** ¿Cómo lo sabe?

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*

[1] Estamos ignorando la polarización.

[2] Véase, por ejemplo, Hecht, capítulo 10.

[3] Nótese que, en una situación física real, las condiciones de contorno son a menudo mucho más complicadas que (13.16), porque la física del contorno importa. Sin embargo, eso suele significar que la difracción en una situación real es incluso mayor.

[4] De nuevo, esto es simplista: ignora las complicaciones de los contornos igual que (13.15).

[5] Nótese que $\sin ka/k$ está bien definida ($= a$) en $k = 0$.

[6] Aquí estamos suponiendo ángulos pequeños, de modo que $\sin\theta \approx \tan\theta$. En nuestra discusión de las redes de difracción, más abajo, veremos qué ocurre cuando la diferencia es importante.

[7] «Estrechas» significa aquí estrechas comparadas con la longitud de onda de la luz; véase la moraleja anterior.


---

<!-- MIT8.03_TextCh1_ES.md -->

# Capítulo 1: Oscilación armónica

Los osciladores son los componentes básicos de las ondas. Empezamos analizando el oscilador armónico. Identificaremos los principios generales que hacen que el oscilador armónico sea tan especial e importante. Para aprovechar estos principios, debemos introducir la herramienta matemática de los números complejos. Pero la ventaja de introducir estas matemáticas es que podemos entender la solución del problema del oscilador armónico de una forma nueva. Mostraremos que las propiedades de linealidad e invariancia bajo traslación temporal conducen a soluciones que son funciones exponenciales complejas del tiempo.

## Vídeos de esta clase (YouTube)

- [Clase 1: Oscilaciones periódicas, osciladores armónicos](https://www.youtube.com/watch?v=4ysFC9vd3GE)

## Resumen previo

En este capítulo discutimos la oscilación armónica en sistemas con un único grado de libertad.

1.  Empezamos con un repaso del oscilador armónico simple, señalando que la ecuación de movimiento de un oscilador libre es lineal e invariante bajo traslación temporal;
2.  Discutimos la linealidad con más detalle, argumentando que es la situación genérica para pequeñas oscilaciones en torno a un punto de equilibrio estable;
3.  Discutimos la invariancia bajo traslación temporal del oscilador armónico, y la conexión entre la oscilación armónica y el movimiento circular uniforme;
4.  Introducimos los números complejos y discutimos su aritmética;
5.  Usando números complejos, encontramos soluciones de la ecuación de movimiento del oscilador armónico que se comportan de la forma más simple posible bajo traslaciones temporales. Llamamos a estas soluciones «irreducibles». Mostramos que son en realidad exponenciales complejas.
6.  Discutimos un circuito LC y trazamos una analogía entre él y un sistema de una masa y muelles.
7.  Discutimos las unidades.
8.  Damos un ejemplo simple de oscilador no lineal.

## 1.1 El oscilador armónico

Cuando estudió mecánica, probablemente aprendió sobre el oscilador armónico. Empezaremos nuestro estudio de los fenómenos ondulatorios repasando este sistema físico simple pero importante. Considere un bloque de masa $m$, libre para deslizar sobre un carril de aire sin fricción, pero unido a un muelle ligero que obedece la ley de Hooke, con su otro extremo unido a una pared fija. Una representación esquemática de este sistema físico se muestra en la figura 1.1.

![Figura 1.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.1.png)

Figura 1.1: bloque de masa $m$ sobre un carril de aire horizontal, unido mediante un muelle a una pared fija a su izquierda.

Este sistema tiene un único grado de libertad relevante. En general, el número de grados de libertad de un sistema es el número de coordenadas que deben especificarse para determinar completamente su configuración. En este caso, como el muelle es ligero, podemos suponer que está estirado uniformemente desde la pared fija hasta el bloque. Entonces la única coordenada importante es la posición del bloque.

En esta situación, la gravedad no desempeña ningún papel en el movimiento del bloque. La fuerza gravitatoria queda cancelada por una fuerza vertical del carril de aire. La única fuerza relevante que actúa sobre el bloque proviene del estiramiento o compresión del muelle. Cuando el muelle está relajado, no hay fuerza sobre el bloque y el sistema está en equilibrio. La ley de Hooke nos dice que la fuerza del muelle viene dada por una constante negativa, $-K$, multiplicada por el desplazamiento del bloque respecto a su posición de equilibrio. Así, si la posición del bloque en cierto instante es $x$ y su posición de equilibrio es $x_0$, la fuerza sobre el bloque en ese instante es

$$F = -K(x - x_0)\,. \qquad \text{(1.1)}$$

La constante $K$ se llama «constante del muelle». Tiene unidades de fuerza por unidad de distancia, o $MT^{-2}$ en términos de $M$ (la unidad de masa), $L$ (la unidad de longitud) y $T$ (la unidad de tiempo). Siempre podemos elegir medir la posición $x$ del bloque con nuestro origen en la posición de equilibrio. Si hacemos esto, entonces $x_0 = 0$ en (1.1) y la fuerza sobre el bloque toma la forma más simple

$$F = -Kx\,. \qquad \text{(1.2)}$$

La oscilación armónica resulta de la interacción entre la fuerza de la ley de Hooke y la ley de Newton, $F=ma$. Sea $x(t)$ el desplazamiento del bloque en función del tiempo, $t$. Entonces la ley de Newton implica

$$m\,\frac{d^2}{dt^2}x(t) = -K\,x(t)\,. \qquad \text{(1.3)}$$

Una ecuación de esta forma, que involucra no solo la función $x(t)$ sino también sus derivadas, se llama «ecuación diferencial». La ecuación diferencial (1.3) es la «ecuación de movimiento» del sistema de la figura 1.1. Como el sistema tiene un único grado de libertad, hay una única ecuación de movimiento. En general, debe haber una ecuación de movimiento por cada coordenada independiente necesaria para especificar la configuración del sistema.

La solución más general de la ecuación diferencial de movimiento (1.3) es una suma de una constante por $\cos\omega t$ más una constante por $\sin\omega t$,

$$x(t) = a\cos\omega t + b\sin\omega t\,, \qquad \text{(1.4)}$$

donde

$$\omega \equiv \sqrt{\frac{K}{m}} \qquad \text{(1.5)}$$

es una constante con unidades de $T^{-1}$ llamada «frecuencia angular». La frecuencia angular será una cantidad muy importante en nuestro estudio de los fenómenos ondulatorios. Casi siempre la denotaremos con la letra griega minúscula $\omega$ (omega).

Como la ecuación involucra una segunda derivada temporal pero ninguna derivada de orden superior, la solución más general contiene dos constantes. Esto es justo lo que esperamos de la física, porque podemos obtener una solución distinta para cada valor de la posición y la velocidad del bloque en el instante inicial. Generalmente, pensaremos en determinar la solución en términos de la posición y la velocidad del bloque cuando ponemos en marcha el movimiento, en un instante que convencionalmente tomamos como $t=0$. Por esta razón, el proceso de determinar la solución en términos de la posición y la velocidad en un instante dado se llama «problema de valores iniciales». Los valores de la posición y la velocidad en $t=0$ se llaman condiciones iniciales. Por ejemplo, podemos escribir la solución más general (1.4) en términos de $x(0)$ y $x'(0)$, el desplazamiento y la velocidad del bloque en el instante $t=0$. Poniendo $t=0$ en (1.4) da $a = x(0)$. Derivando y poniendo luego $t=0$ da $b = \omega^{-1}x'(0)$. Así

$$x(t) = x(0)\cos\omega t + \frac{1}{\omega}x'(0)\sin\omega t\,. \qquad \text{(1.6)}$$

Por ejemplo, supongamos que el bloque tiene una masa de 1 kilogramo y que el muelle mide 0.5 metros, con una constante de muelle $K$ de 100 newtons por metro. Para hacerse una idea de lo que significa esta constante, considere colgar el muelle verticalmente (véase el problema 1.1). La fuerza gravitatoria sobre el bloque es

$$mg \approx 9.8\ \text{newtons}\,. \qquad \text{(1.7)}$$

En equilibrio, la fuerza gravitatoria cancela la fuerza del muelle, así que el muelle se estira

$$\frac{mg}{K} \approx 0.098\ \text{metros} = 9.8\ \text{centímetros}\,. \qquad \text{(1.8)}$$

Para esta masa y esta constante de muelle, la frecuencia angular $\omega$ del sistema de la figura 1.1 es

$$\omega = \sqrt{\frac{K}{M}} = \sqrt{\frac{100\ \text{N/m}}{1\ \text{kg}}} = 10\ \frac{1}{\text{s}}\,. \qquad \text{(1.9)}$$

Si, por ejemplo, el bloque se desplaza 0.01 m (1 cm) de su posición de equilibrio y se suelta desde el reposo en $t=0$, la posición en cualquier instante posterior $t$ viene dada (en metros) por

$$x(t) = 0.01 \times \cos 10t\,. \qquad \text{(1.10)}$$

La velocidad (en metros por segundo) es

$$x'(t) = -0.1 \times \sin 10t\,. \qquad \text{(1.11)}$$

El movimiento es periódico, en el sentido de que el sistema oscila —repite el mismo movimiento una y otra vez indefinidamente. Tras un tiempo

$$\tau = \frac{2\pi}{\omega} \approx 0.628\ \text{s} \qquad \text{(1.12)}$$

el sistema vuelve exactamente a donde estaba en $t=0$, con el bloque instantáneamente en reposo con desplazamiento 0.01 metros. El tiempo $\tau$ (letra griega tau) se llama el «periodo» de la oscilación. Sin embargo, la solución (1.6) es más que simplemente periódica: es un movimiento «armónico simple», lo que significa que en el movimiento aparece una única frecuencia.

La frecuencia angular, $\omega$, es la inversa del tiempo requerido para que la fase de la onda cambie en un radián. La «frecuencia», usualmente denotada por la letra griega $\nu$ (nu), es la inversa del tiempo requerido para que la fase cambie un ciclo completo, o $2\pi$ radianes, y así vuelva a su estado original. La frecuencia se mide en hercios, o ciclos por segundo. Así, la frecuencia angular es mayor que la frecuencia por un factor de $2\pi$,

$$\omega\ (\text{en radianes/segundo}) = 2\pi\ (\text{radianes/ciclo}) \cdot \nu\ (\text{ciclos/segundo})\,. \qquad \text{(1.13)}$$

La frecuencia, $\nu$, es la inversa del periodo, $\tau$, de (1.12),

$$\nu = \frac{1}{\tau}\,. \qquad \text{(1.14)}$$

El movimiento armónico simple como (1.6) ocurre en una amplísima variedad de sistemas físicos. La pregunta con la que comenzaremos nuestro estudio de los fenómenos ondulatorios es la siguiente: ¿por qué aparecen soluciones de la forma (1.6) de manera tan ubicua en física? ¿Qué tienen en común los sistemas que oscilan armónicamente? Por supuesto, la respuesta matemática a esta pregunta es que todos estos sistemas tienen ecuaciones de movimiento esencialmente de la misma forma que (1.3). Encontraremos una respuesta más profunda y física que después podremos generalizar a sistemas más complicados. Las características clave que todos estos sistemas comparten con la masa en el muelle son la linealidad y la invariancia bajo traslación temporal de las ecuaciones de movimiento (al menos de forma aproximada). Son estas dos propiedades las que determinan el comportamiento oscilatorio en sistemas que van desde muelles hasta bobinas y condensadores.

Cada una de estas dos propiedades es interesante por sí sola, pero juntas son mucho más poderosas. Determinan casi por completo la forma de las soluciones. Veremos que si el sistema es lineal e invariante bajo traslación temporal, siempre podemos escribir su movimiento como una suma de movimientos simples en los que la dependencia temporal es o bien oscilación armónica o bien decaimiento (o crecimiento) exponencial.

## 1.2 Pequeñas oscilaciones y linealidad

Un sistema con un grado de libertad es lineal si su ecuación de movimiento es una función lineal de la coordenada $x$ que especifica la configuración del sistema. Dicho de otro modo, la ecuación de movimiento debe ser una suma de términos, cada uno de los cuales contiene como máximo una potencia de $x$. La ecuación de movimiento involucra una segunda derivada, pero ninguna derivada de orden superior, así que una ecuación de movimiento lineal tiene la forma general:

$$\alpha\,\frac{d^2}{dt^2}x(t) + \beta\,\frac{d}{dt}x(t) + \gamma\,x(t) = f(t)\,. \qquad \text{(1.15)}$$

Si todos los términos involucran exactamente una potencia de $x$, la ecuación de movimiento es «homogénea». La ecuación (1.15) no es homogénea debido al término del lado derecho. El término «inhomogéneo», $f(t)$, representa una fuerza externa. La ecuación homogénea correspondiente sería:

$$\alpha\,\frac{d^2}{dt^2}x(t) + \beta\,\frac{d}{dt}x(t) + \gamma\,x(t) = 0\,. \qquad \text{(1.16)}$$

En general, $\alpha$, $\beta$ y $\gamma$, así como $f$, podrían ser funciones de $t$. Sin embargo, eso rompería la invariancia bajo traslación temporal que discutiremos con más detalle más abajo y haría el sistema mucho más complicado. Casi siempre supondremos que $\alpha$, $\beta$ y $\gamma$ son constantes. La ecuación de movimiento para la masa sobre un muelle, (1.3), es de esta forma general, pero con $\beta$ y $f$ iguales a cero. Como veremos en el capítulo 2, podemos incluir el efecto de las fuerzas de fricción permitiendo un $\beta$ no nulo, y el efecto de fuerzas externas permitiendo un $f$ no nulo.

La linealidad de la ecuación de movimiento (1.15) implica que si $x_1(t)$ es una solución para la fuerza externa $f_1(t)$,

$$\alpha\,\frac{d^2}{dt^2}x_1(t) + \beta\,\frac{d}{dt}x_1(t) + \gamma\,x_1(t) = f_1(t)\,, \qquad \text{(1.17)}$$

y $x_2(t)$ es una solución para la fuerza externa $f_2(t)$,

$$\alpha\,\frac{d^2}{dt^2}x_2(t) + \beta\,\frac{d}{dt}x_2(t) + \gamma\,x_2(t) = f_2(t)\,, \qquad \text{(1.18)}$$

entonces la suma,

$$x_{12}(t) = A\,x_1(t) + B\,x_2(t)\,, \qquad \text{(1.19)}$$

para constantes $A$ y $B$, es una solución para la fuerza externa $Af_1 + Bf_2$,

$$\alpha\,\frac{d^2}{dt^2}x_{12}(t) + \beta\,\frac{d}{dt}x_{12}(t) + \gamma\,x_{12}(t) = Af_1(t) + Bf_2(t)\,. \qquad \text{(1.20)}$$

La suma $x_{12}(t)$ se llama «combinación lineal» de las dos soluciones $x_1(t)$ y $x_2(t)$. En el caso del movimiento «libre», es decir, sin fuerza externa, si $x_1(t)$ y $x_2(t)$ son soluciones, entonces la suma $Ax_1(t) + Bx_2(t)$ también es una solución.

La solución más general de cualquiera de estas ecuaciones involucra dos constantes que deben fijarse mediante las condiciones iniciales, por ejemplo la posición y velocidad iniciales de la partícula, como en (1.6). Se sigue de (1.20) que siempre podemos escribir la solución más general para cualquier fuerza externa $f(t)$ como una suma de la «solución general» de la ecuación homogénea (1.16) y cualquier solución «particular» de (1.15).

Ningún sistema es exactamente lineal. La «linealidad» nunca es exactamente «cierta». Sin embargo, la idea de linealidad es extremadamente importante, porque es una aproximación útil en un número muy grande de sistemas, por una muy buena razón física. En casi cualquier sistema en el que las propiedades sean funciones suaves de las posiciones de sus partes, los pequeños desplazamientos respecto al equilibrio producen fuerzas restauradoras aproximadamente lineales. La diferencia entre algo que es «cierto» y algo que es una aproximación útil es la diferencia esencial entre las matemáticas y la física. En el mundo real, las preguntas son demasiado interesantes para tener respuestas exactas. Si consigue entender la respuesta dentro de una aproximación bien definida, ha aprendido algo importante.

Para ver la naturaleza genérica de la linealidad, considere una partícula que se mueve en el eje $x$ con energía potencial $V(x)$. La fuerza sobre la partícula en el punto $x$ es menos la derivada de la energía potencial,

$$F = -\frac{d}{dx}V(x)\,. \qquad \text{(1.21)}$$

Una fuerza que puede derivarse de una energía potencial de esta forma se llama fuerza «conservativa».

En un punto de equilibrio, $x_0$, la fuerza se anula, y por tanto la derivada de la energía potencial se anula:

$$F = -\left.\frac{d}{dx}V(x)\right|_{x=x_0} = -V'(x_0) = 0\,. \qquad \text{(1.22)}$$

Podemos describir las pequeñas oscilaciones del sistema en torno al equilibrio de la forma más simple si redefinimos el origen de modo que $x_0=0$. Entonces el desplazamiento respecto al equilibrio es la coordenada $x$. Podemos expandir la fuerza en serie de Taylor:

$$F(x) = -V'(x) = -V'(0) - x\,V''(0) - \frac{1}{2}x^2\,V'''(0) + \cdots \qquad \text{(1.23)}$$

El primer término en (1.23) se anula porque este sistema está en equilibrio en $x=0$, de acuerdo con (1.22). El segundo término tiene la forma de la ley de Hooke, con

$$K = V''(0)\,. \qquad \text{(1.24)}$$

El equilibrio es estable si la segunda derivada de la energía potencial es positiva, de modo que $x=0$ es un mínimo local de la energía potencial.

El punto importante es que, para $x$ suficientemente pequeño, el tercer término de (1.23), y todos los siguientes, serán mucho menores que el segundo. El tercer término es despreciable si

$$\left|x\,V'''(0)\right| \ll V''(0)\,. \qquad \text{(1.25)}$$

Típicamente, cada derivada adicional trae consigo un factor $1/L$, donde $L$ es la distancia sobre la cual la energía potencial cambia una fracción apreciable. Entonces (1.25) se convierte en

$$x \ll L\,. \qquad \text{(1.26)}$$

Solo hay dos formas en que una fuerza derivada de una energía potencial puede dejar de ser aproximadamente lineal para oscilaciones suficientemente pequeñas en torno al equilibrio estable:

1.  Si el potencial no es suave, de modo que la primera o la segunda derivada del potencial no está bien definida en el punto de equilibrio, entonces no podemos hacer un desarrollo de Taylor y el argumento de (1.23) no funciona. Daremos un ejemplo de este tipo al final de este capítulo.

2.  Aunque las derivadas existan en el punto de equilibrio $x=0$, puede ocurrir que $V''(0)=0$. En este caso, para tener un equilibrio estable, también debemos tener $V'''(0)=0$; de lo contrario, un pequeño desplazamiento en una dirección u otra crecería con el tiempo. Entonces el siguiente término del desarrollo de Taylor domina para $x$ pequeño, dando una fuerza proporcional a $x^3$.

![Figura 1.2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.2.png)

Figura 1.2: energía potencial de la ecuación (1.27), $V(x) = E(L/x + x/L)$, mostrada para $x$ entre 0 y $5L$; presenta un mínimo en $x=L$.

Ambos casos excepcionales son muy raros en la naturaleza. Habitualmente, la energía potencial es una función suave del desplazamiento y no hay razón para que $V''(0)$ se anule. La situación genérica es que las pequeñas oscilaciones en torno al equilibrio estable son lineales.

Puede ser útil un ejemplo. Casi cualquier función de energía potencial con un punto de equilibrio estable sirve, siempre que sea suave. Por ejemplo, considere la energía potencial

$$V(x) = E\left(\frac{L}{x} + \frac{x}{L}\right)\,. \qquad \text{(1.27)}$$

Esto se muestra en la figura 1.2. El mínimo (al menos para $x$ positivo) ocurre en $x=L$, así que primero redefinimos $x = X+L$, de modo que

$$V(X) = E\left(\frac{L}{X+L} + \frac{X+L}{L}\right)\,. \qquad \text{(1.28)}$$

La fuerza correspondiente es

$$F(X) = E\left(\frac{L}{(X+L)^2} - \frac{1}{L}\right)\,. \qquad \text{(1.29)}$$

Podemos mirar cerca de $X=0$ y expandir en serie de Taylor:

$$F(X) = -2\frac{E}{L}\left(\frac{X}{L}\right) + 3\frac{E}{L}\left(\frac{X}{L}\right)^2 + \cdots \qquad \text{(1.30)}$$

Ahora, el cociente entre el primer término no lineal y el término lineal es

$$\frac{3X}{2L}\,, \qquad \text{(1.31)}$$

que es pequeño si $X \ll L$.

En otras palabras, cuanto más cerca esté del punto de equilibrio, más se parece la energía potencial real a la parábola que esperaríamos de la energía potencial de una fuerza lineal tipo ley de Hooke. Puede verlo gráficamente ampliando una pequeña región en torno al punto de equilibrio. En la figura 1.3, el rectángulo punteado de la figura 1.2 se ha ampliado hasta convertirse en un cuadrado. Note que se parece mucho más a una parábola que la figura 1.2. Si repitiéramos el procedimiento y volviéramos a ampliar una pequeña región en torno al punto de equilibrio, no podría detectar a simple vista el término cúbico.

![Figura 1.3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.3.png)

Figura 1.3: ampliación del pequeño rectángulo punteado de la figura 1.2, entre $0.9L$ y $1.1L$, mostrando una forma mucho más parabólica.

A menudo, la aproximación lineal es incluso mejor, porque el término de orden $x^2$ se anula por simetría. Por ejemplo, cuando el sistema es simétrico respecto a $x=0$, de modo que $V(x)=V(-x)$, el término de orden $x^3$ (y todos los $x^n$ con $n$ impar) en la energía potencial se anula, y entonces no hay término de orden $x^2$ en la fuerza.

Para un muelle típico, la linealidad (la ley de Hooke) es una excelente aproximación para desplazamientos pequeños. Sin embargo, siempre hay términos no lineales que se vuelven importantes si los desplazamientos son suficientemente grandes. Habitualmente, en este libro nos limitaremos a las pequeñas oscilaciones y supondremos que nuestros sistemas son lineales. Sin embargo, no debe concluir que el tema de los sistemas no lineales carece de interés. De hecho, es un área muy activa de la investigación actual en física.

## 1.3 Invariancia bajo traslación temporal

### 1.3.1 Movimiento circular uniforme

*(Referencia al programa interactivo 1-1 del disco de programas del curso original.)*

Cuando $\alpha$, $\beta$ y $\gamma$ en (1.15) no dependen del tiempo $t$, y en ausencia de fuerza externa, es decir, para el movimiento libre, el tiempo entra en (1.15) solo a través de las derivadas. Entonces la ecuación de movimiento tiene la forma

$$\alpha\,\frac{d^2}{dt^2}x(t) + \beta\,\frac{d}{dt}x(t) + \gamma\,x(t) = 0\,. \qquad \text{(1.32)}$$

La ecuación de movimiento del oscilador armónico no amortiguado, (1.3), tiene esta forma con $\alpha=m$, $\beta=0$ y $\gamma=K$. Las soluciones de (1.32) tienen la propiedad de que

$$\text{si } x(t) \text{ es una solución, } x(t+a) \text{ también lo será.} \qquad \text{(1.33)}$$

Matemáticamente, esto es cierto porque las operaciones de derivar respecto al tiempo y sustituir $t \to t+a$ pueden hacerse en cualquier orden gracias a la regla de la cadena

$$\frac{d}{dt}x(t+a) = \left[\frac{d}{dt}(t+a)\right]\left[\frac{d}{dt'}x(t')\right]_{t'=t+a} = \left[\frac{d}{dt'}x(t')\right]_{t'=t+a}\,. \qquad \text{(1.34)}$$

La razón física de (1.33) es que podemos cambiar el ajuste inicial de nuestro reloj y la física se verá igual. La solución $x(t+a)$ puede obtenerse a partir de la solución $x(t)$ cambiando el ajuste del reloj en $a$. La etiqueta temporal ha sido «trasladada» en $a$. Nos referiremos a la propiedad (1.33) como invariancia bajo traslación temporal.

La mayoría de los sistemas físicos en los que pueda pensar son invariantes bajo traslación temporal en ausencia de fuerza externa. Para obtener un oscilador sin invariancia bajo traslación temporal, tendría que hacer algo bastante extraño, como hacer que la constante del muelle dependiera del tiempo.

Para el movimiento libre del oscilador armónico, aunque la ecuación de movimiento es ciertamente invariante bajo traslación temporal, la manifestación de esta invariancia en la solución (1.6) no es tan simple como podría ser. Las dos partes de la solución, una proporcional a $\cos\omega t$ y la otra a $\sin\omega t$, se mezclan al reajustar el reloj. Por ejemplo,

$$\cos[\omega(t+a)] = \cos\omega a\cos\omega t - \sin\omega a\sin\omega t\,. \qquad \text{(1.35)}$$

Será muy útil encontrar otra forma de escribir la solución que se comporte de manera más simple al reajustar los relojes. Para ello, tendremos que trabajar con números complejos.

Para motivar la introducción de los números complejos, comenzaremos mostrando la relación entre el movimiento armónico simple y el movimiento circular uniforme. Considere el movimiento circular uniforme en el plano $x$-$y$ alrededor de un círculo centrado en el origen, $x=y=0$, con radio $R$ y velocidad en sentido horario $v=R\omega$. Las coordenadas $x$ e $y$ del movimiento son

$$x(t) = R\cos(\omega t - \varphi)\,,\qquad y(t) = -R\sin(\omega t - \varphi)\,, \qquad \text{(1.36)}$$

donde $\varphi$ es el ángulo en radianes, medido en sentido antihorario, de la posición en $t=0$ respecto al eje $x$ positivo. La $x(t)$ de (1.36) es idéntica a la $x(t)$ de (1.6) con

$$x(0) = R\cos\varphi\,,\qquad x'(0) = \omega R\sin\varphi\,. \qquad \text{(1.37)}$$

El movimiento armónico simple es equivalente a una componente del movimiento circular uniforme. Esta relación se ilustra en la figura 1.4. A medida que el punto se mueve alrededor del círculo con velocidad constante $R\omega$, la coordenada $x$ ejecuta un movimiento armónico simple con velocidad angular $\omega$. Si lo deseamos, podemos elegir las dos constantes necesarias para fijar la solución de (1.3) como $R$ y $\varphi$, en lugar de $x(0)$ y $x'(0)$. En este lenguaje, la acción de reajustar el reloj es más transparente: reajustar el reloj cambia el valor de $\varphi$ sin cambiar nada más.

![Figura 1.4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.4.png)

Figura 1.4: circunferencia de radio $R$ recorrida con velocidad angular $\omega$ en sentido horario; la proyección sobre el eje $x$ ejecuta movimiento armónico simple.

Pero nos gustaría aún más. La idea clave es que la linealidad nos otorga una libertad considerable. Podemos sumar soluciones de las ecuaciones de movimiento y multiplicarlas por constantes, y el resultado sigue siendo una solución. Nos gustaría usar esta libertad para elegir soluciones que se comporten de la forma más simple posible bajo traslaciones temporales.

El comportamiento más simple posible para una solución $z(t)$ bajo traslación temporal es

$$z(t+a) = h(a)\,z(t)\,. \qquad \text{(1.38)}$$

Es decir, nos gustaría encontrar una solución que se reproduzca a sí misma salvo una constante global, $h(a)$, cuando reajustamos nuestros relojes en $a$. Como siempre somos libres de multiplicar una solución de una ecuación de movimiento lineal homogénea por una constante, el cambio de $z(t)$ a $h(a)z(t)$ no supone gran cosa. Llamaremos a una solución que satisface (1.38) una «solución irreducible» respecto a las traslaciones temporales, porque su comportamiento bajo traslaciones temporales (reajustes del reloj) es lo más simple que puede ser.

Resulta que, para sistemas cuyas ecuaciones de movimiento son lineales e invariantes bajo traslación temporal, como veremos con más detalle más abajo, siempre podemos encontrar soluciones irreducibles que tienen la propiedad (1.38). Sin embargo, para el movimiento armónico simple, esto requiere números complejos. Puede verlo notando que cambiar el ajuste del reloj en $\pi/\omega$ simplemente cambia el signo de la solución con frecuencia angular $\omega$, porque tanto el término coseno como el seno cambian de signo:

$$\cos(\omega t+\pi) = -\cos\omega t\,,\qquad \sin(\omega t+\pi) = -\sin\omega t\,. \qquad \text{(1.39)}$$

Pero entonces, de (1.38) y (1.39), podemos escribir

$$-z(t) = z(t+\pi/\omega) = z(t+\pi/2\omega+\pi/2\omega) = h(\pi/2\omega)\,z(t+\pi/2\omega) = h(\pi/2\omega)^2\,z(t)\,. \qquad \text{(1.40)}$$

Así, no podemos encontrar tal solución a menos que $h(\pi/2\omega)$ tenga la propiedad

$$[h(\pi/2\omega)]^2 = -1\,. \qquad \text{(1.41)}$$

¡El cuadrado de $h(\pi/2\omega)$ es $-1$! Por tanto, nos vemos obligados a considerar los números complejos. Cuando terminemos de introducirlos, volveremos a (1.38) y mostraremos que siempre podemos encontrar soluciones de esta forma para sistemas lineales e invariantes bajo traslación temporal.

## 1.4 Números complejos

La raíz cuadrada de $-1$, llamada $i$, es importante en física y matemáticas por muchas razones. Las cantidades físicas medibles siempre pueden describirse con números reales: nunca obtendrá una lectura de $i$ metros en su regla. Sin embargo, veremos que cuando $i$ se incluye junto con los números reales y las operaciones aritméticas habituales (suma, resta, multiplicación y división), el álgebra, la trigonometría y el cálculo se simplifican. Aunque los números complejos no son necesarios para describir los fenómenos ondulatorios, nos permitirán discutirlos de forma más simple y esclarecedora.

### 1.4.1 Algunas definiciones

Un número imaginario es un número de la forma $i$ por un número real.

Un número complejo, $z$, es una suma de un número real y un número imaginario: $z=a+ib$.

Las partes real e «imaginaria», $\text{Re}(z)$ y $\text{Im}(z)$, del número complejo $z=a+ib$:

$$\text{Re}(z) = a\,,\qquad \text{Im}(z) = b\,. \qquad \text{(1.42)}$$

Note que la parte imaginaria es en realidad un número real: el coeficiente real de $i$ en $z=a+ib$.

El conjugado complejo, $z^*$, del número complejo $z$, se obtiene cambiando el signo de $i$:

$$z^* = a - ib\,. \qquad \text{(1.43)}$$

Note que $\text{Re}(z) = (z+z^*)/2$ y $\text{Im}(z) = (z-z^*)/2i$.

El plano complejo: como un número complejo $z$ queda especificado por dos números reales, puede pensarse como un vector bidimensional, con componentes $(a,b)$. La parte real de $z$, $a=\text{Re}(z)$, es la componente $x$, y la parte imaginaria de $z$, $b=\text{Im}(z)$, es la componente $y$.

![Figura 1.5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.5.png)

Figura 1.5 y 1.6: dos vectores en el plano complejo. La figura 1.5 muestra $2+i \leftrightarrow (2,1)$, con ángulo $\theta = \arg(2+i) = \arctan(1/2)$ medido desde el eje $x$ positivo. La figura 1.6 muestra $-1.5-2i \leftrightarrow (-1.5,-2)$, con $\theta = \arg(-1.5-2i) = \arctan(4/3)+\pi$.

El valor absoluto, $|z|$, de $z$, es la longitud del vector $(a,b)$:

$$|z| = \sqrt{a^2+b^2} = \sqrt{z^*z}\,. \qquad \text{(1.44)}$$

El valor absoluto $|z|$ es siempre un número real no negativo.

El argumento o fase, $\arg(z)$, de un número complejo $z$ no nulo, es el ángulo, en radianes, del vector $(a,b)$ en sentido antihorario desde el eje $x$:

$$\arg(z) = \begin{cases} \arctan(b/a) & \text{para } a \ge 0\,, \\ \arctan(b/a) + \pi & \text{para } a < 0\,. \end{cases} \qquad \text{(1.45)}$$

Como cualquier ángulo, $\arg(z)$ puede redefinirse sumando un múltiplo de $2\pi$ radianes o $360°$ (véanse las figuras 1.5 y 1.6).

### 1.4.2 Aritmética

*(Referencia al programa interactivo 1-2 del disco de programas del curso original.)*

Las operaciones aritméticas de suma, resta y multiplicación de números complejos se definen tratando $i$ como una variable algebraica, usando la propiedad distributiva y la relación $i^2=-1$. Así, si $z=a+ib$ y $z'=a'+ib'$, entonces

$$\begin{aligned}
z+z' &= (a+a') + i(b+b')\,,\\
z-z' &= (a-a') + i(b-b')\,,\\
zz' &= (aa'-bb') + i(ab'+ba')\,.
\end{aligned} \qquad \text{(1.46)}$$

Por ejemplo:

$$(3+4i)+(-2+7i) = (3-2)+(4+7)i = 1+11i\,, \qquad \text{(1.47)}$$

$$(3+4i)\cdot(5+7i) = (3\cdot5-4\cdot7) + (3\cdot7+4\cdot5)i = -13+41i\,. \qquad \text{(1.48)}$$

Vale la pena jugar con la multiplicación compleja y familiarizarse con el plano complejo.

La división es más complicada. Dividir un número complejo $z$ por un número real $r$ es fácil: basta dividir tanto la parte real como la imaginaria por $r$, obteniendo $z/r = a/r + ib/r$. Para dividir por un número complejo $z'$, podemos usar el hecho de que $z'^*z'=|z'|^2$ es real. Si multiplicamos el numerador y el denominador de $z/z'$ por $z'^*$, podemos escribir:

$$z/z' = z'^*z/|z'|^2 = \frac{aa'+bb'}{a'^2+b'^2} + i\,\frac{ba'-ab'}{a'^2+b'^2}\,. \qquad \text{(1.49)}$$

Por ejemplo:

$$(3+4i)/(2+i) = (3+4i)\cdot(2-i)/5 = (10+5i)/5 = 2+i\,. \qquad \text{(1.50)}$$

Con estas definiciones para las operaciones aritméticas, el valor absoluto se comporta de forma muy simple bajo multiplicación y división. Bajo multiplicación, el valor absoluto del producto de dos números complejos es el producto de los valores absolutos:

$$|zz'| = |z|\,|z'|\,. \qquad \text{(1.51)}$$

La división funciona igual, siempre que no divida por cero:

$$|z/z'| = |z|/|z'| \quad \text{si } z' \neq 0\,. \qquad \text{(1.52)}$$

Los matemáticos llaman «álgebra de división» a un conjunto de objetos sobre el que se definen la suma y la multiplicación y para el cual existe un valor absoluto que satisface (1.51) y (1.52). Es un hecho matemático curioso (aunque irrelevante para nosotros) que los números complejos son una de solo cuatro álgebras de división, siendo las otras los números reales y objetos más exóticos llamados cuaterniones y octoniones, obtenidos relajando los requisitos de conmutatividad y asociatividad (respectivamente) de las leyes de multiplicación.

Lo maravilloso de los números complejos desde el punto de vista del álgebra es que todas las ecuaciones polinómicas tienen solución. Por ejemplo, la ecuación $x^2-2x+5=0$ no tiene soluciones reales, pero tiene dos soluciones complejas, $x=1\pm 2i$. En general, una ecuación de la forma $p(x)=0$, donde $p(x)$ es un polinomio de grado $n$ con coeficientes complejos (o reales), tiene $n$ soluciones si se permiten números complejos, pero puede no tener ninguna si $x$ se restringe a ser real.

Note que el conjugado complejo de cualquier suma, producto, etc. de números complejos puede obtenerse simplemente cambiando el signo de $i$ dondequiera que aparezca. Esto implica que si el polinomio $p(z)$ tiene coeficientes reales, las soluciones de $p(z)=0$ aparecen en pares conjugados complejos. Es decir, si $p(z)=0$, entonces $p(z^*)=0$ también.

### 1.4.3 Exponenciales complejas

Considere un número complejo $z=a+ib$ con valor absoluto 1. Como $|z|=1$ implica $a^2+b^2=1$, podemos escribir $a$ y $b$ como el coseno y el seno de un ángulo $\theta$.

$$z = \cos\theta + i\sin\theta \quad \text{para } |z|=1\,. \qquad \text{(1.53)}$$

Como

$$\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{b}{a} \qquad \text{(1.54)}$$

el ángulo $\theta$ es el argumento de $z$:

$$\arg(\cos\theta+i\sin\theta) = \theta\,. \qquad \text{(1.55)}$$

Pensemos en $z$ como función de $\theta$ y consideremos el cálculo. La derivada respecto a $\theta$ es:

$$\frac{\partial}{\partial\theta}(\cos\theta+i\sin\theta) = -\sin\theta+i\cos\theta = i(\cos\theta+i\sin\theta) \qquad \text{(1.56)}$$

Una función que, al derivarla, se reproduce a sí misma salvo una constante es una exponencial. En particular, si tuviéramos una función de $\theta$, $f(\theta)$, que satisficiera $\partial f(\theta)/\partial\theta = kf(\theta)$ para $k$ real, concluiríamos que $f(\theta)=e^{k\theta}$. Así, si queremos que el cálculo funcione de la misma manera para los números complejos que para los reales, debemos concluir que

$$e^{i\theta} = \cos\theta + i\sin\theta\,. \qquad \text{(1.57)}$$

Podemos comprobar esta relación notando que los desarrollos de Taylor de ambos lados son iguales. Los desarrollos de Taylor de las funciones exponencial, coseno y seno son:

$$\begin{aligned}
e^x &= 1 + x + \frac{x^2}{2} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots\\
\cos(x) &= 1 - \frac{x^2}{2} + \frac{x^4}{4!} - \cdots\\
\sin(x) &= x - \frac{x^3}{3!} + \cdots
\end{aligned} \qquad \text{(1.58)}$$

Así, el desarrollo de Taylor del lado izquierdo de (1.57) es

$$1 + i\theta + (i\theta)^2/2 + (i\theta)^3/3! + \cdots \qquad \text{(1.59)}$$

mientras que el desarrollo del lado derecho es

$$(1-\theta^2/2+\cdots) + i(\theta-\theta^3/6+\cdots) \qquad \text{(1.60)}$$

Las potencias de $i$ en (1.59) funcionan justo de la manera adecuada para reproducir el patrón de signos menos en (1.60).

Además, la ley de multiplicación funciona correctamente:

$$e^{i\theta}e^{i\theta'} = (\cos\theta+i\sin\theta)(\cos\theta'+i\sin\theta') = \cos(\theta+\theta') + i\sin(\theta+\theta') = e^{i(\theta+\theta')}\,. \qquad \text{(1.61)}$$

Así, (1.57) tiene sentido en todos los aspectos. Esta conexión entre las exponenciales complejas y las funciones trigonométricas se llama identidad de Euler. Es extremadamente útil. Entre otras cosas, la lógica puede invertirse y las funciones trigonométricas pueden «definirse» algebraicamente en términos de exponenciales complejas:

$$\cos\theta = \frac{e^{i\theta}+e^{-i\theta}}{2}\,,\qquad \sin\theta = \frac{e^{i\theta}-e^{-i\theta}}{2i} = -i\,\frac{e^{i\theta}-e^{-i\theta}}{2}\,. \qquad \text{(1.62)}$$

Usando (1.62), las identidades trigonométricas pueden deducirse muy fácilmente. Por ejemplo:

$$\cos 3\theta = \text{Re}(e^{3i\theta}) = \text{Re}((e^{i\theta})^3) = \cos^3\theta - 3\cos\theta\sin^2\theta\,. \qquad \text{(1.63)}$$

Otro ejemplo que nos será útil más adelante es:

$$\begin{aligned}
\cos(\theta+\theta') + \cos(\theta-\theta') &= \frac{e^{i(\theta+\theta')}+e^{-i(\theta+\theta')}+e^{i(\theta-\theta')}+e^{-i(\theta-\theta')}}{2}\\
&= \frac{(e^{i\theta}+e^{-i\theta})(e^{i\theta'}+e^{-i\theta'})}{2} = 2\cos\theta\cos\theta'\,. \qquad \text{(1.64)}
\end{aligned}$$

Todo número complejo no nulo puede escribirse como el producto de un número real positivo (su valor absoluto) y un número complejo de valor absoluto 1. Así,

$$z = x+iy = R\,e^{i\theta} \quad \text{donde } R=|z|\,,\ \theta = \arg(z)\,. \qquad \text{(1.65)}$$

En el plano complejo, (1.65) expresa el hecho de que un vector bidimensional puede escribirse en coordenadas cartesianas, $(x,y)$, o en coordenadas polares, $(R,\theta)$. Por ejemplo, $\sqrt3+i = 2e^{i\pi/6}$; $1+i = \sqrt2\,e^{i\pi/4}$; $-8i = 8e^{3i\pi/2}=8e^{-i\pi/2}$. La figura 1.7 muestra el número complejo $1+i=\sqrt2\,e^{i\pi/4}$.

![Figura 1.7](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.7.png)

Figura 1.7: el número complejo $1+i$ representado como un vector de módulo $\sqrt2$ y ángulo $\pi/4$ respecto al eje real.

La relación (1.65) da otra forma útil de pensar en la multiplicación de números complejos. Si

$$z_1 = R_1 e^{i\theta_1}\quad\text{y}\quad z_2 = R_2 e^{i\theta_2}\,, \qquad \text{(1.66)}$$

entonces

$$z_1 z_2 = R_1 R_2\, e^{i(\theta_1+\theta_2)}\,. \qquad \text{(1.67)}$$

En palabras: para multiplicar dos números complejos, se multiplican los valores absolutos y se suman los argumentos.

La ecuación (1.57) da lugar a varias relaciones que pueden parecer sorprendentes hasta que se acostumbre a ellas. Por ejemplo: $e^{i\pi}=-1$; $e^{i\pi/2}=i$; $e^{2i\pi}=1$. Estas tienen una interpretación en el plano complejo, donde $e^{i\theta}$ es el vector unitario $(\cos\theta,\sin\theta)$, en un ángulo $\theta$ medido en sentido antihorario desde el eje $x$. Entonces $-1$ está a $180°$ o $\pi$ radianes en sentido antihorario desde el eje $x$, mientras que $i$ está sobre el eje $y$, a $90°$ o $\pi/2$ radianes del eje $x$. $2\pi$ radianes son $360°$, y por tanto nos hacen volver completamente al eje $x$. Estas relaciones se muestran en la figura 1.8.

![Figura 1.8](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.8.png)

Figura 1.8: círculo unidad en el plano complejo mostrando los puntos $1=e^{2i\pi}$, $i=e^{i\pi/2}$, $-1=e^{i\pi}$ y $-i=e^{-i\pi/2}=e^{3i\pi/2}$.

### 1.4.4 Notación

No es estrictamente necesario tener una notación que distinga entre números reales y complejos. La razón es que, como hemos visto, las reglas de la aritmética, el álgebra y el cálculo se aplican a los números reales y complejos exactamente de la misma manera. Sin embargo, a algunos lectores les puede resultar útil que se les recuerde cuándo una cantidad es compleja. Esto es probablemente particularmente útil para cantidades como $x$, que representan coordenadas físicas. Por ello, al menos durante los primeros capítulos, hasta que el lector esté completamente «complejizado», distinguiremos entre «coordenadas» reales y complejas. Si son reales, usaremos las letras $x$ e $y$. Si son complejas, usaremos $z$ y $w$.

## 1.5 Soluciones exponenciales

Ya estamos listos para traducir las condiciones de linealidad e invariancia bajo traslación temporal a matemáticas. Lo que veremos es que estas dos propiedades conducen automáticamente a soluciones irreducibles que satisfacen (1.38), y además que estas soluciones irreducibles son simplemente exponenciales. No necesitamos usar ningún otro detalle sobre la ecuación de movimiento para obtener este resultado. Por tanto, nuestros argumentos se aplicarán a situaciones mucho más complicadas, en las que haya amortiguamiento, más grados de libertad, o ambas cosas. Mientras el sistema tenga invariancia bajo traslación temporal y linealidad, las soluciones serán sumas de soluciones exponenciales irreducibles.

Hemos visto que las soluciones de ecuaciones diferenciales lineales homogéneas con coeficientes constantes, de la forma

$$M\,\frac{d^2}{dt^2}x(t) + K\,x(t) = 0\,, \qquad \text{(1.68)}$$

tienen las propiedades de linealidad e invariancia bajo traslación temporal. La ecuación del movimiento armónico simple es de esta forma. Las coordenadas son reales, y las constantes $M$ y $K$ son reales porque son cosas físicas como masas y constantes de muelle. Sin embargo, queremos permitirnos el lujo de considerar también soluciones complejas, así que consideramos la misma ecuación con variables complejas:

$$M\,\frac{d^2}{dt^2}z(t) + K\,z(t) = 0\,. \qquad \text{(1.69)}$$

Note la relación entre las soluciones de (1.68) y (1.69). Como los coeficientes $M$ y $K$ son reales, para cada solución $z(t)$ de (1.69), el conjugado complejo, $z(t)^*$, también es una solución. La ecuación diferencial sigue siendo cierta al cambiar el signo de todas las $i$.

A partir de estas dos soluciones, podemos construir dos soluciones reales:

$$x_1(t) = \text{Re}(z(t)) = (z(t)+z(t)^*)/2\,;\qquad x_2(t) = \text{Im}(z(t)) = (z(t)-z(t)^*)/2i\,. \qquad \text{(1.70)}$$

Todo esto es posible gracias a la linealidad, que nos permite ir y venir entre soluciones reales y complejas formando combinaciones lineales, como en (1.70). Estas son soluciones de (1.68). Note que $x_1(t)$ y $x_2(t)$ son justamente las partes real e imaginaria de $z(t)$. El punto importante es que siempre puede reconstruir las soluciones físicas reales de la ecuación de movimiento a partir de la solución compleja. Puede hacer toda la matemática usando variables complejas, lo que la hace mucho más fácil. Luego, al final, puede obtener la solución física de interés simplemente tomando la parte real de su solución compleja.

Volvamos ahora a la solución de (1.69). Lo que queremos mostrar es que llegamos a soluciones irreducibles y exponenciales para cualquier sistema con invariancia bajo traslación temporal y linealidad. Así entenderemos por qué siempre podemos encontrar soluciones irreducibles, no solo en (1.69), sino en situaciones mucho más complicadas, con amortiguamiento o más grados de libertad.

Hay dos elementos cruciales:

1.  La invariancia bajo traslación temporal, (1.33), que exige que $x(t+a)$ sea una solución si $x(t)$ es una solución;
2.  La linealidad, que nos permite formar combinaciones lineales de soluciones para obtener nuevas soluciones.

Resolveremos (1.68) usando únicamente estos dos elementos. Esto nos permitirá generalizar inmediatamente nuestra solución a cualquier sistema en el que estén presentes las propiedades anteriores.

Una forma de usar la linealidad es elegir un conjunto «base» de soluciones, $x_j(t)$ para $j=1$ hasta $n$, que sea «completo» y «linealmente independiente». Para el oscilador armónico, bastan dos soluciones, así que $n=2$. Pero nuestro análisis será mucho más general y se aplicará, por ejemplo, a sistemas lineales con más grados de libertad, así que dejaremos $n$ libre. Que el conjunto sea «completo» significa que cualquier solución $z(t)$ (que puede ser compleja) puede expresarse como una combinación lineal de las $x_j(t)$,

$$z(t) = \sum_{j=1}^n c_j\,x_j(t)\,. \qquad \text{(1.72)}$$

Que sean «linealmente independientes» significa que ninguna de las $x_j(t)$ puede expresarse como combinación lineal de las demás, de modo que la única combinación lineal de las $x_j(t)$ que se anula es la combinación trivial, con todos los coeficientes nulos,

$$\sum_{j=1}^n c_j\,x_j(t) = 0 \implies c_j = 0\,. \qquad \text{(1.73)}$$

Veamos ahora si podemos encontrar una solución irreducible que se comporte de forma simple ante un cambio en el ajuste inicial del reloj, como en (1.38),

$$z(t+a) = h(a)\,z(t) \qquad \text{(1.74)}$$

para alguna función (posiblemente compleja) $h(a)$. En términos de las soluciones base, esto es

$$z(t+a) = h(a)\sum_{k=1}^n c_k\,x_k(t)\,. \qquad \text{(1.75)}$$

Pero cada una de las soluciones base también se transforma en una solución bajo una traslación temporal, y cada nueva solución puede a su vez escribirse como una combinación lineal de las soluciones base, así:

$$x_j(t+a) = \sum_{k=1}^n R_{jk}(a)\,x_k(t)\,. \qquad \text{(1.76)}$$

Así,

$$z(t+a) = \sum_{j=1}^n c_j\,x_j(t+a) = \sum_{j,k=1}^n c_j\,R_{jk}(a)\,x_k(t)\,. \qquad \text{(1.77)}$$

Comparando (1.75) y (1.77), y usando (1.73), vemos que podemos encontrar una solución irreducible si y solo si

$$\sum_{j=1}^n c_j\,R_{jk}(a) = h(a)\,c_k \quad\text{para todo } k\,. \qquad \text{(1.78)}$$

Esto se llama una «ecuación de autovalores». Tendremos mucho más que decir sobre las ecuaciones de autovalores en el capítulo 3, cuando discutamos la notación matricial. Por ahora, note que (1.78) es un sistema de $n$ ecuaciones simultáneas homogéneas en las $n$ incógnitas $c_j$. Podemos reescribirlo como

$$\sum_{j=1}^n c_j\,S_{jk}(a) = 0 \quad\text{para todo } k\,, \qquad \text{(1.79)}$$

donde

$$S_{jk}(a) = \begin{cases} R_{jk}(a) & \text{para } j\neq k\,, \\ R_{jk}(a) - h(a) & \text{para } j=k\,. \end{cases} \qquad \text{(1.80)}$$

Podemos encontrar una solución de (1.78) si y solo si existe una solución de la ecuación de determinante

$$\det S_{jk}(a) = 0\,. \qquad \text{(1.81)}$$

(Discutiremos el determinante en detalle en el capítulo 3, así que si ha olvidado este resultado del álgebra, no se preocupe por ahora.)

(1.81) es una ecuación de grado $n$ en la variable $h(a)$. Puede no tener soluciones reales, pero siempre tiene $n$ soluciones complejas para $h(a)$ (aunque algunos de los valores de $h(a)$ pueden repetirse). Para cada solución de $h(a)$, podemos encontrar un conjunto de $c_j$ que satisfaga (1.78). Las distintas combinaciones lineales $z(t)$ construidas de esta forma constituirán un conjunto linealmente independiente de soluciones irreducibles, cada una satisfaciendo (1.74) para algún $h(a)$. Si hay $n$ valores distintos de $h(a)$, la situación habitual, formarán un conjunto completo de soluciones irreducibles de las ecuaciones de movimiento. Entonces podemos tomar directamente nuestras soluciones como irreducibles, satisfaciendo (1.74). Más adelante veremos qué ocurre cuando algunos de los $h(a)$ se repiten, de modo que hay menos de $n$ valores distintos.

Ahora, para cada solución irreducible, podemos ver cuáles deben ser las funciones $h(a)$ y $z(a)$. Si derivamos ambos lados de (1.74) respecto a $a$, obtenemos

$$z'(t+a) = h'(a)\,z(t)\,. \qquad \text{(1.82)}$$

Poniendo $a=0$ da

$$z'(t) = H\,z(t) \qquad \text{(1.83)}$$

donde

$$H \equiv h'(0)\,. \qquad \text{(1.84)}$$

Esto implica

$$z(t) \propto e^{Ht}\,. \qquad \text{(1.85)}$$

¡Así, la solución irreducible es una exponencial! Hemos mostrado que (1.71) conduce a soluciones irreducibles y exponenciales, sin usar ningún detalle de la dinámica.

### 1.5.1 \* Construyendo la exponencial

Hay otra forma de ver lo que (1.74) implica para la forma de la solución irreducible, que ni siquiera involucra resolver la sencilla ecuación diferencial (1.83). Empecemos poniendo $t=0$ en (1.74). Esto da

$$h(a) = z(a)/z(0)\,. \qquad \text{(1.86)}$$

$h(a)$ es proporcional a $z(a)$. Esto es particularmente simple si elegimos multiplicar nuestra solución irreducible por una constante de modo que $z(0)=1$. Entonces (1.86) da

$$h(a) = z(a) \qquad \text{(1.87)}$$

y por tanto

$$z(t+a) = z(t)\,z(a)\,. \qquad \text{(1.88)}$$

Consideremos qué ocurre para $t=\epsilon \ll 1$ muy pequeño. Haciendo un desarrollo de Taylor, podemos escribir

$$z(\epsilon) = 1 + H\epsilon + O(\epsilon^2) \qquad \text{(1.89)}$$

donde $H=z'(0)$, de (1.84) y (1.87). Usando (1.88), podemos mostrar que

$$z(N\epsilon) = [z(\epsilon)]^N\,. \qquad \text{(1.90)}$$

Entonces, para cualquier $t$, podemos escribir (tomando $t=N\epsilon$)

$$z(t) = \lim_{N\to\infty}[z(t/N)]^N = \lim_{N\to\infty}[1+H(t/N)]^N = e^{Ht}\,. \qquad \text{(1.91)}$$

Así, de nuevo vemos que la solución irreducible respecto a la invariancia bajo traslación temporal es simplemente una exponencial:

$$z(t) = e^{Ht}\,. \qquad \text{(1.92)}$$

### 1.5.2 ¿Qué es $H$?

Cuando sustituimos la solución irreducible, $e^{Ht}$, en (1.69), las derivadas simplemente bajan potencias de $H$, así que la ecuación se convierte en una ecuación puramente algebraica (eliminando un factor global $e^{Ht}$)

$$M H^2 + K = 0\,. \qquad \text{(1.93)}$$

Ahora, por fin, podemos ver la relevancia de los números complejos en la discusión anterior sobre la invariancia bajo traslación temporal. Para $M$ y $K$ positivos, la ecuación (1.93) no tiene ninguna solución si restringimos $H$ a ser real. No podemos encontrar ninguna solución irreducible real. Pero siempre hay dos soluciones para $H$ entre los números complejos. En este caso, la solución es

$$H = \pm i\omega \quad\text{donde } \omega = \sqrt{\frac{K}{M}}\,. \qquad \text{(1.94)}$$

Es solo en este último paso, donde efectivamente calculamos $H$, que entran los detalles de (1.69). Hasta (1.93), todo se seguía simplemente de los principios generales, (1.71).

Ahora, como antes, a partir de estas dos soluciones podemos construir dos soluciones reales tomando las partes real e imaginaria de $z(t)=e^{\pm i\omega t}$.

$$x_1(t) = \text{Re}(z(t)) = \cos\omega t\,,\qquad x_2(t) = \text{Im}(z(t)) = \pm\sin\omega t\,. \qquad \text{(1.95)}$$

Las traslaciones temporales mezclan estas dos soluciones reales. Por eso las soluciones exponenciales complejas irreducibles son más fáciles de manejar. La cantidad $\omega$ es la frecuencia angular que vimos en (1.5), en la solución de la ecuación de movimiento del oscilador armónico. Cualquier combinación lineal de tales soluciones puede escribirse en términos de una «amplitud» y una «fase», de la siguiente manera: para $c$ y $d$ reales,

$$\begin{aligned}
c\cos(\omega t)+d\sin(\omega t) &= c\,\frac{e^{i\omega t}+e^{-i\omega t}}{2} - id\,\frac{e^{i\omega t}-e^{-i\omega t}}{2} = \text{Re}\left[(c+id)e^{-i\omega t}\right]\\
&= \text{Re}\left[A e^{i\theta}e^{-i\omega t}\right] = \text{Re}\left[A e^{-i(\omega t-\theta)}\right] = A\cos(\omega t-\theta)\,. \qquad \text{(1.96)}
\end{aligned}$$

donde $A$ es un número real positivo llamado la amplitud,

$$A = \sqrt{c^2+d^2}\,, \qquad \text{(1.97)}$$

y $\theta$ es un ángulo llamado la fase,

$$\theta = \arg(c+id)\,. \qquad \text{(1.98)}$$

Estas relaciones son otro ejemplo de la equivalencia entre coordenadas cartesianas y polares, discutida tras (1.65). El par $c$ y $d$ son las coordenadas cartesianas en el plano complejo del número complejo $c+id$. La amplitud, $A$, y la fase, $\theta$, son la representación en coordenadas polares del mismo número complejo. (1.96) muestra que $c$ y $d$ son también los coeficientes de $\cos\omega t$ y $\sin\omega t$ en la parte real del producto de este número complejo con $e^{-i\omega t}$. Esta relación se ilustra en la figura 1.9 (note la relación con la figura 1.4). Mientras $z$ se mueve en sentido horario con velocidad angular constante, $\omega$, alrededor del círculo $|z|=A$ en el plano complejo, la parte real de $z$ realiza un movimiento armónico simple, $A\cos(\omega t-\theta)$.

![Figura 1.9](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.9.png)

Figura 1.9: representación en el plano complejo del número $A e^{-i(\omega t - \theta)}$, con coordenadas cartesianas $c,d$ y fase $\theta$; la proyección real ejecuta $A\cos(\omega t - \theta)$.

Ahora que conoce los números complejos y las exponenciales complejas, debería volver a la relación entre el movimiento armónico simple y el movimiento circular uniforme ilustrada en la figura 1.4. El movimiento circular uniforme puede interpretarse como un movimiento en el plano complejo de

$$z(t) = e^{-i\omega t}\,. \qquad \text{(1.99)}$$

A medida que $t$ cambia, $z(t)$ se mueve con velocidad constante en sentido horario alrededor del círculo unidad en el plano complejo. La parte real, $\cos\omega t$, ejecuta un movimiento armónico simple.

Note que igual de fácilmente podríamos haber tomado nuestra solución compleja como $e^{+i\omega t}$. Esto correspondería a un movimiento antihorario en el plano complejo, pero la parte real, que es lo único que importa físicamente, no cambiaría. Es convencional en física tomar soluciones complejas proporcionales a $e^{-i\omega t}$. Esto es puramente una convención; no hay física en ello. Sin embargo, es suficientemente universal en la literatura de física como para que intentemos hacerlo así de manera consistente aquí.

## 1.6 Circuitos LC

Uno de los ejemplos más importantes de un sistema oscilante es un circuito LC. Probablemente estudió estos circuitos en su curso de electricidad y magnetismo. Al igual que un muelle que obedece la ley de Hooke, este sistema es lineal, porque las relaciones entre carga, corriente, voltaje, etc., para inductores, condensadores y resistencias ideales, son lineales. Aquí queremos hacer explícita la analogía entre un circuito LC particular y un sistema de una masa sobre un muelle. El circuito LC, con un inductor sin resistencia de inductancia $L$ y un condensador de capacitancia $C$, se muestra en la figura 1.10. Normalmente no pensaríamos en esto como un circuito en absoluto, porque no hay batería ni otra fuente de energía eléctrica. Sin embargo, podríamos imaginar, por ejemplo, que el condensador se cargó inicialmente al montar el circuito. Entonces circularía corriente al cerrar el circuito. De hecho, en ausencia de resistencia, la corriente seguiría oscilando para siempre. Veremos que este circuito es análogo a la combinación de muelles y una masa mostrada en la figura 1.11. La frecuencia de oscilación del sistema mecánico es

$$\omega = \sqrt{\frac{K}{m}}\,. \qquad \text{(1.100)}$$

![Figura 1.10](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.10.png)

Figura 1.10: circuito LC formado por un inductor $L$ y un condensador $C$ en un lazo cerrado. Figura 1.11: sistema mecánico análogo, una masa $m$ unida a un muelle de constante $K$ y a una pared fija.

Podemos describir la configuración del sistema mecánico de la figura 1.10 en términos de $x$, el desplazamiento del bloque hacia la derecha. Podemos describir la configuración del circuito LC de la figura 1.10 en términos de $Q$, la carga que ha «pasado» a través del inductor desde la situación de equilibrio con el condensador descargado. En este caso, la carga desplazada a través del inductor va enteramente al condensador, porque no tiene otro sitio adonde ir, como se muestra en la figura 1.12. La corriente a través del inductor es la derivada temporal de la carga que ha pasado,

![Figura 1.11](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.11.png)

Figura 1.11

$$I = \frac{dQ}{dt}\,. \qquad \text{(1.101)}$$

![Figura 1.12](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.12.png)

Figura 1.12: carga $Q$ desplazada a través del inductor, acumulándose como $+Q$ en una placa del condensador y $-Q$ en la otra.

Para ver cómo funciona el circuito LC, podemos examinar los voltajes en distintos puntos del sistema, como se muestra en la figura 1.13. Para un inductor, la caída de voltaje a través de él es la tasa de cambio de la corriente que lo atraviesa, o

$$-L\,\frac{dI}{dt} = V\,. \qquad \text{(1.102)}$$

![Figura 1.13](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.13.png)

Figura 1.13: voltaje y corriente en el circuito LC; el voltaje es $0$ en los extremos del inductor salvo por la caída debida a él, y $V=Q/C$ en el condensador.

Para el condensador, la carga almacenada es el voltaje por la capacitancia, o

$$V = Q/C\,. \qquad \text{(1.103)}$$

Juntando (1.101), (1.102) y (1.103) obtenemos

$$L\,\frac{dI}{dt} = L\,\frac{d^2Q}{dt^2} = -\frac{1}{C}Q\,. \qquad \text{(1.104)}$$

La correspondencia entre los dos sistemas es la siguiente:

$$m \leftrightarrow L\,,\qquad K \leftrightarrow 1/C\,,\qquad x \leftrightarrow Q\,. \qquad \text{(1.105)}$$

Al hacer las sustituciones de (1.105), la ecuación de movimiento de la masa sobre el muelle, (1.3), se convierte en (1.104). Así, conociendo la solución (1.6) para la masa sobre el muelle, podemos concluir inmediatamente que la carga desplazada en este circuito LC oscila con frecuencia

$$\omega = \sqrt{\frac{1}{LC}}\,. \qquad \text{(1.106)}$$

## 1.7 Unidades — desplazamiento y energía

Hemos visto ya dos tipos de sistemas físicos muy diferentes que presentan oscilación armónica simple. Hay otros posibles, y daremos otro ejemplo a continuación. Este es un buen momento para discutir las unidades de las ecuaciones de movimiento. La ecuación de movimiento «genérica» para el movimiento armónico simple sin amortiguamiento tiene esta forma:

$$M\,\frac{d^2\mathcal{X}}{dt^2} = -K\,\mathcal{X} \qquad \text{(1.107)}$$

donde

$$\begin{aligned}
&\mathcal{X}\ \text{es la coordenada generalizada,}\\
&M\ \text{es la masa generalizada,}\\
&K\ \text{es la constante de muelle generalizada.}
\end{aligned} \qquad \text{(1.108)}$$

En el movimiento armónico simple de una masa puntual, $\mathcal{X}$ es justamente el desplazamiento respecto al equilibrio, $x$; $M$ es la masa, $m$; y $K$ es la constante del muelle, $K$.

Las unidades apropiadas para $M$ y $K$ dependen de las unidades de $\mathcal{X}$. Se determinan convencionalmente exigiendo que

$$\frac{1}{2}M\left(\frac{d\mathcal{X}}{dt}\right)^2 \qquad \text{(1.109)}$$

sea la energía «cinética» del sistema debida al cambio de la coordenada con el tiempo, y que

$$\frac{1}{2}K\mathcal{X}^2 \qquad \text{(1.110)}$$

sea la energía «potencial» del sistema, almacenada en el muelle generalizado.

Tiene buen sentido físico conceder a la energía un estatus especial en estos problemas, porque, en ausencia de fricción y fuerzas externas, la energía total —la suma de la energía cinética (1.109) y la energía potencial (1.110)— es constante. En la oscilación, la energía se almacena alternadamente en energía cinética y potencial. Cuando el sistema está en su configuración de equilibrio pero moviéndose con su velocidad máxima, toda la energía es cinética. Cuando el sistema se detiene instantáneamente en su desplazamiento máximo, toda la energía es potencial. De hecho, a veces es más fácil identificar $M$ y $K$ calculando las energías cinética y potencial que encontrando directamente la ecuación de movimiento. Usaremos este truco en el capítulo 11 para discutir las ondas de agua.

Por ejemplo, en un circuito LC en unidades del SI, tomamos nuestra coordenada generalizada como una carga, $Q$, en culombios. La energía se mide en julios, o voltios por culombios. La constante de muelle generalizada tiene unidades de

$$\frac{\text{julios}}{\text{culombios}^2} = \frac{\text{voltios}}{\text{culombios}} \qquad \text{(1.111)}$$

que es la inversa de la unidad de capacitancia, culombios por voltio, o faradios. La masa generalizada tiene unidades de

$$\frac{\text{julios}\times\text{segundos}^2}{\text{culombios}^2} = \frac{\text{voltios}\times\text{segundos}}{\text{amperios}} \qquad \text{(1.112)}$$

que es una unidad de inductancia (henrios). Esto es lo que usamos en nuestra correspondencia entre el circuito LC y el oscilador mecánico, (1.105).

También podemos añadir una fuerza generalizada al lado derecho de (1.107). La fuerza generalizada tiene unidades de energía sobre desplazamiento generalizado. Esto es correcto porque, cuando la ecuación de movimiento se multiplica por el desplazamiento, (1.109) y (1.110) implican que cada uno de los términos tiene unidades de energía. Así, por ejemplo, en el circuito LC, la fuerza generalizada es un voltaje.

### 1.7.1 Energía constante

La energía total es la suma de la energía cinética más la potencial, de (1.109) y (1.110),

$$E = \frac{1}{2}M\left(\frac{d\mathcal{X}}{dt}\right)^2 + \frac{1}{2}K\mathcal{X}^2\,. \qquad \text{(1.113)}$$

Si no actúan fuerzas externas sobre el sistema, la energía total debe ser constante. Puede verse de (1.113) que la energía puede ser constante para una solución oscilante solo si la frecuencia angular, $\omega$, es $\sqrt{K/M}$. Suponga, por ejemplo, que el desplazamiento generalizado del sistema tiene la forma

$$\mathcal{X}(t) = A\sin\omega t\,, \qquad \text{(1.114)}$$

donde $A$ es una amplitud con las unidades de $\mathcal{X}$. Entonces la velocidad generalizada es

$$\frac{d}{dt}\mathcal{X}(t) = A\omega\cos\omega t\,. \qquad \text{(1.115)}$$

Para que la energía sea constante, debemos tener

$$K = \omega^2 M\,. \qquad \text{(1.116)}$$

Entonces, la energía total, de (1.109) y (1.110), es

$$\frac{1}{2}M\omega^2 A^2\cos^2\omega t + \frac{1}{2}KA^2\sin^2\omega t = \frac{1}{2}KA^2\,. \qquad \text{(1.117)}$$

### 1.7.2 El péndulo de torsión

Puede ser útil otro ejemplo más. Consideremos el péndulo de torsión, mostrado en la figura 1.14.

![Figura 1.14](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.14.png)

Figura 1.14: dos vistas de un péndulo de torsión —una barra o mancuerna suspendida por su centro mediante un hilo o fibra desde un soporte superior; la vista superior muestra el ángulo de torsión $\theta$.

Un péndulo de torsión es un oscilador simple pero muy útil, formado por una mancuerna o varilla sostenida por su centro mediante un hilo o fibra, colgada de un soporte superior. Cuando la mancuerna se tuerce un ángulo $\theta$, como se muestra en la vista superior de la figura 1.14, el hilo se retuerce y proporciona un par restaurador sobre la mancuerna. Para un hilo o fibra adecuados, este par restaurador es casi lineal incluso para ángulos de desplazamiento bastante grandes. En este sistema, la variable natural para el desplazamiento es el ángulo $\theta$. Entonces la ecuación de movimiento es

$$I\,\frac{d^2\theta}{dt^2} = -\alpha\theta\,, \qquad \text{(1.118)}$$

donde $I$ es el momento de inercia de la mancuerna respecto a su centro y $-\alpha\theta$ es la fuerza restauradora. Así, la masa generalizada es el momento de inercia, $I$, con unidades de longitud al cuadrado por masa, y la constante de muelle generalizada es la constante $\alpha$, con unidades de par. Como es de esperar, de (1.109) y (1.110), la energía cinética y potencial son (respectivamente)

$$\frac{1}{2}I\left(\frac{d\theta}{dt}\right)^2 \quad\text{y}\quad \frac{1}{2}\alpha\theta^2\,. \qquad \text{(1.119)}$$

## 1.8 Un oscilador no lineal simple

Para ilustrar algunas de las diferencias entre osciladores lineales y no lineales, daremos un ejemplo muy simple de oscilador no lineal. Considere la siguiente ecuación de movimiento no lineal:

$$m\,\frac{d^2}{dt^2}x = \begin{cases} -F_0 & \text{para } x>0\,,\\ F_0 & \text{para } x<0\,,\\ 0 & \text{para } x=0\,. \end{cases} \qquad \text{(1.120)}$$

Esto describe una partícula de masa $m$ sometida a una fuerza hacia la izquierda, $-F_0$, cuando la partícula está a la derecha del origen ($x(t)>0$), una fuerza hacia la derecha, $F_0$, cuando la partícula está a la izquierda del origen ($x(t)<0$), y ninguna fuerza cuando la partícula está justo en el origen.

La energía potencial de este sistema crece linealmente a ambos lados de $x=0$. No puede derivarse en $x=0$, porque la derivada no es continua allí. Así, no podemos desarrollar en serie de Taylor la energía potencial (ni la fuerza) en torno al punto $x=0$, y los argumentos de (1.21)-(1.24) no se aplican.

Es fácil encontrar una solución de (1.120). Suponga que en el instante $t=0$ la partícula está en el origen pero moviéndose con velocidad positiva $v$. La partícula se mueve inmediatamente a la derecha del origen y desacelera con aceleración constante, $-F_0/m$, de modo que

$$x(t) = vt - \frac{F_0}{2m}t^2 \quad\text{para } t\le\tau\,, \qquad \text{(1.121)}$$

donde

$$\tau = \frac{2mv}{F_0} \qquad \text{(1.122)}$$

es el tiempo requerido para que la partícula dé la vuelta y regrese al origen. En el instante $t=\tau$, la partícula pasa a la izquierda del origen. En ese punto se mueve con velocidad $-v$, y el proceso se repite para $x$ negativo y aceleración positiva $F_0/m$. Entonces la solución continúa en la forma

$$x(t) = -v(t-\tau) + \frac{F_0}{2m}(t-\tau)^2 \quad\text{para } \tau\le t\le 2\tau\,. \qquad \text{(1.123)}$$

Luego todo el proceso se repite. El movimiento de la partícula, mostrado en la figura 1.15, se parece superficialmente a una oscilación armónica, pero la curva es en realidad una secuencia de parábolas empalmadas, en lugar de una onda senoidal.

![Figura 1.15](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.15.png)

Figura 1.15: posición $x(t)$, en unidades de $mv^2/(2F_0)$ en el eje vertical y $\tau$ en el horizontal, formada por arcos de parábola alternos entre $0$ y $\pm mv^2/(2F_0)$, con periodo $2\tau$.

La ecuación de movimiento, (1.120), es invariante bajo traslación temporal. Claramente, podemos hacer arrancar la partícula desde el origen con velocidad $v$ en cualquier instante $t_0$. La solución entonces se ve como la mostrada en la figura 1.15, pero trasladada en el tiempo por $t_0$. La solución tiene la forma

$$x_{t_0}(t) = x(t-t_0) \qquad \text{(1.124)}$$

donde $x(t)$ es la función descrita por (1.121), (1.123), etc. Esto se muestra en la figura 1.16 para $t_0=3\tau/4$. La curva punteada corresponde a $t_0=0$.

![Figura 1.16](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.16.png)

Figura 1.16: la misma trayectoria en zigzag parabólico que la figura 1.15, pero desplazada en el tiempo un valor $t_0 = 3\tau/4$; la curva punteada muestra la trayectoria original sin desplazar.

Al igual que el oscilador armónico, este sistema oscila de forma regular e indefinida. Sin embargo, en este caso, el periodo de la oscilación, el tiempo que tarda en repetirse, $2\tau$, depende de la amplitud de la oscilación, o equivalentemente, de la velocidad inicial, $v$. El periodo es proporcional a $v$, según (1.122). El movimiento de la partícula, arrancando desde el origen en $t=t_0$, para una velocidad inicial $v/2$, se muestra en la figura 1.17. La curva punteada corresponde a una velocidad inicial $v$.

![Figura 1.17](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/fig1.17.png)

Figura 1.17: la misma familia de trayectorias parabólicas, pero con una velocidad inicial $v/2$, de modo que el periodo se duplica respecto al caso de velocidad $v$, mostrado en trazo punteado para comparar.

Aunque la ecuación de movimiento no lineal, (1.120), es invariante bajo traslación temporal, la simetría es mucho menos útil porque el sistema carece de linealidad. Desde nuestro punto de vista, lo importante de la linealidad (aparte del hecho de que es una buena aproximación en tantos sistemas físicos importantes) es que nos permite elegir una base conveniente para las soluciones de la ecuación de movimiento. Las elegimos de modo que se comporten de forma simple bajo traslaciones temporales. Entonces, gracias a la linealidad, podemos construir cualquier solución como una combinación lineal de las soluciones base. En una situación como (1.120), no tenemos esta opción.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Analizar la física de un oscilador armónico, incluyendo encontrar la constante del muelle, plantear la ecuación de movimiento, resolverla e imponer las condiciones iniciales;
2.  Encontrar la «constante de muelle» aproximada para pequeñas oscilaciones en torno a un punto de equilibrio y estimar el desplazamiento a partir del cual la linealidad deja de ser válida;
3.  Entender la conexión entre la oscilación armónica y el movimiento circular uniforme;
4.  Usar la aritmética compleja y las exponenciales complejas;
5.  Resolver ecuaciones de movimiento lineales homogéneas usando soluciones irreducibles que son exponenciales complejas;
6.  Entender y explicar la diferencia entre frecuencia y frecuencia angular;
7.  Analizar las oscilaciones de circuitos LC;
8.  Calcular cantidades físicas para sistemas oscilantes en unidades del SI;
9.  Entender la invariancia bajo traslación temporal en sistemas no lineales.

## Problemas

**1.1.** Para la masa y el muelle discutidos en (1.1)-(1.8), suponga que el sistema cuelga verticalmente en el campo gravitatorio terrestre, con el extremo superior del muelle fijo. Demuestre que la frecuencia de las oscilaciones verticales viene dada por (1.5). Explique por qué la gravedad no afecta a la frecuencia angular.

**1.2.**

1.  Encuentre una expresión para $\cos 7\theta$ en términos de $\cos\theta$ y $\sin\theta$, usando exponenciales complejas y el desarrollo del binomio.

2.  Haga lo mismo para $\sin 5\theta$.

3.  Use exponenciales complejas para encontrar una expresión para $\sin(\theta_1+\theta_2+\theta_3)$ en términos de los senos y cosenos de los ángulos individuales.

4.  ¿Recuerda la «fórmula del ángulo mitad»,

$$\cos^2\frac{\theta}{2} = \frac{1}{2}(1+\cos\theta)\ ?$$

Use exponenciales complejas para demostrar la «fórmula del quinto ángulo»,

$$\cos^5\frac{\theta}{5} = \frac{10}{16}\cos\frac{\theta}{5} + \frac{5}{16}\cos\frac{3\theta}{5} + \frac{1}{16}\cos\theta\,.$$

1.  Use exponenciales complejas para demostrar la identidad

$$\sin 6x = \sin x\left(32\cos^5x - 32\cos^3x + 6\cos x\right)\,.$$

**1.3.**

1.  Escriba $i+\sqrt3$ en la forma $Re^{i\theta}$. Escriba $\theta$ como un número racional multiplicado por $\pi$.

2.  Haga lo mismo para $i-\sqrt3$.

3.  Demuestre que las dos raíces cuadradas de $Re^{i\theta}$ son $\pm\sqrt{R}\,e^{i\theta/2}$. (Pista: esto es fácil, no se esfuerce demasiado.)

4.  Use el resultado de c. para encontrar las raíces cuadradas de $2i$ y de $2+2i\sqrt3$.

**1.4.** Encuentre las seis soluciones de la ecuación $z^6=1$ y escriba cada una en la forma $A+iB$, representándolas en el plano complejo. (Pista: escriba $z=Re^{i\theta}$ con $R$ real y positivo, y encuentre $R$ y $\theta$.)

**1.5.** Encuentre tres soluciones independientes de la ecuación diferencial

$$\frac{d^3}{dt^3}f(t) + f(t) = 0\,.$$

Debe usar exponenciales complejas para deducir las soluciones, pero exprese los resultados en forma real.

**1.6.** Un bloque de masa $M$ desliza sin fricción entre dos muelles de constantes $K$ y $2K$, como se muestra en la figura. El bloque está obligado a moverse solo hacia la izquierda y hacia la derecha en el papel, así que el sistema tiene un único grado de libertad.

![Figura](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh1_ES/figs1.png)

Figura: bloque $M$ entre un muelle de constante $K$ a su izquierda y otro de constante $2K$ a su derecha, ambos anclados a paredes fijas.

Calcule la frecuencia angular de la oscilación. Si la velocidad del bloque en su posición de equilibrio es $v$, calcule la amplitud de la oscilación.

**1.7.** Una partícula de masa $m$ se mueve en el eje $x$ con energía potencial

$$V(x) = \frac{E_0}{a^4}\left(x^4+4ax^3-8a^2x^2\right)\,.$$

Encuentre las posiciones en las que la partícula está en equilibrio estable. Encuentre la frecuencia angular de las pequeñas oscilaciones en torno a cada posición de equilibrio. ¿Qué entiende por pequeñas oscilaciones? Sea cuantitativo y dé una respuesta separada para cada punto de equilibrio estable.

**1.8.** Para el péndulo de torsión de la figura 1.14, suponga que el péndulo consiste en dos masas de 0.01 kg sobre una varilla ligera de longitud total 0.1 m. Si la constante de muelle generalizada, $\alpha$, es $5\times10^{-7}\ \text{N}\,\text{m}$, encuentre la frecuencia angular del oscilador.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.


---

<!-- MIT8.03_TextCh2_ES.md -->

# Capítulo 2: Oscilación forzada y resonancia

El problema de la oscilación forzada será crucial para nuestra comprensión de los fenómenos ondulatorios. Las exponenciales complejas son aún más útiles para discutir el amortiguamiento y las oscilaciones forzadas. Nos ayudarán a discutir las oscilaciones forzadas sin perdernos en el álgebra.

## Vídeos de esta clase (YouTube)

- [Clase 2: Osciladores libres amortiguados](https://www.youtube.com/watch?v=T2n6fVybLcU)
- [Clase 3: Osciladores forzados, fenómenos transitorios, resonancia](https://www.youtube.com/watch?v=FCFpaKcpuXQ)

## Resumen previo

En este capítulo aplicamos las herramientas de las exponenciales complejas y la invariancia bajo traslación temporal para tratar la oscilación amortiguada y el importante fenómeno físico de la resonancia en osciladores individuales.

1.  Planteamos y resolvemos (usando exponenciales complejas) la ecuación de movimiento de un oscilador armónico amortiguado en los regímenes sobreamortiguado, subamortiguado y con amortiguamiento crítico.
2.  Planteamos la ecuación de movimiento del oscilador armónico amortiguado y forzado.
3.  Estudiamos la solución, que presenta una resonancia cuando la frecuencia impulsora coincide con la frecuencia de oscilación libre del oscilador no amortiguado correspondiente.
4.  Estudiamos en detalle un sistema concreto: una masa sobre un muelle en un fluido viscoso. Damos una explicación física de la relación de fase entre el término impulsor y el amortiguamiento.

## 2.1 Osciladores amortiguados

Consideremos primero la oscilación libre de un oscilador amortiguado. Podría ser, por ejemplo, un sistema de un bloque unido a un muelle, como el de la figura 1.1, pero con todo el sistema sumergido en un fluido viscoso. Entonces, además de la fuerza restauradora del muelle, el bloque experimenta una fuerza de fricción. Para velocidades pequeñas, la fuerza de fricción puede tomarse de la forma

$$-m\gamma v\,, \qquad \text{(2.1)}$$

donde $\gamma$ es una constante. Note que, como hemos extraído el factor de la masa del bloque en (2.1), $1/\gamma$ tiene dimensiones de tiempo. Podemos escribir la ecuación de movimiento del sistema como

$$\frac{d^2}{dt^2}x(t) + \gamma\,\frac{d}{dt}x(t) + \omega_0^2\,x(t) = 0\,, \qquad \text{(2.2)}$$

donde $\omega_0=\sqrt{K/m}$. Esta ecuación es lineal e invariante bajo traslación temporal, como la ecuación de movimiento no amortiguada. De hecho, es justamente la forma que analizamos en el capítulo anterior, en (1.16). Como antes, permitimos la posibilidad de soluciones complejas de la misma ecuación,

$$\frac{d^2}{dt^2}z(t) + \gamma\,\frac{d}{dt}z(t) + \omega_0^2\,z(t) = 0\,. \qquad \text{(2.3)}$$

Como se satisface (1.71), sabemos, por los argumentos del capítulo 1, que podemos encontrar soluciones irreducibles de la forma

$$z(t) = e^{\alpha t}\,, \qquad \text{(2.4)}$$

donde $\alpha$ (letra griega alfa) es una constante. Sustituyendo (2.4) en (2.2), encontramos

$$(\alpha^2+\gamma\alpha+\omega_0^2)\,e^{\alpha t} = 0\,. \qquad \text{(2.5)}$$

Como la exponencial nunca se anula, la cantidad entre paréntesis debe ser cero, así

$$\alpha = -\frac{\gamma}{2} \pm \sqrt{\frac{\gamma^2}{4}-\omega_0^2}\,. \qquad \text{(2.6)}$$

De (2.6) vemos que hay tres regímenes, según la comparación entre $\gamma$ y $\omega_0$, que conducen a físicas distintas.

### 2.1.1 Osciladores sobreamortiguados

Si $\gamma/2 > \omega_0$, ambas soluciones para $\alpha$ son reales y negativas. La solución de (2.2) es una suma de exponenciales decrecientes. Cualquier desplazamiento inicial del sistema se extingue sin oscilación. Este es un oscilador sobreamortiguado.

La solución general en el caso sobreamortiguado tiene la forma

$$x(t) = z(t) = A_+\,e^{-\gamma_+ t} + A_-\,e^{-\gamma_- t}\,, \qquad \text{(2.7)}$$

donde

$$\gamma_\pm = \frac{\gamma}{2} \pm \sqrt{\frac{\gamma^2}{4}-\omega_0^2}\,. \qquad \text{(2.8)}$$

![Figura 2.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh2_ES/fig2.1.png)

Figura 2.1: soluciones de la ecuación de movimiento para un oscilador sobreamortiguado, con $\gamma=1\ \text{s}^{-1}$ y $\omega_0=0.4\ \text{s}^{-1}$; la línea punteada es $e^{-\gamma_+t}$, la discontinua es $e^{-\gamma_-t}$, y la línea continua es la combinación lineal $e^{-\gamma_+t}-\tfrac12 e^{-\gamma_-t}$, entre $t=0$ y $t=10\ \text{s}$.

En la situación sobreamortiguada, en realidad no hay oscilación. Si la masa se mueve inicialmente muy rápido hacia la posición de equilibrio, puede sobrepasarla, como se muestra en la figura 2.1. Sin embargo, luego regresa exponencialmente hacia la posición de equilibrio, sin volver a cruzar nunca el valor de equilibrio del desplazamiento por segunda vez. Así, en el movimiento libre de un oscilador sobreamortiguado, la posición de equilibrio se cruza cero o una vez.

### 2.1.2 Osciladores subamortiguados

Si $\gamma/2 < \omega_0$, la expresión dentro de la raíz cuadrada es negativa, y las soluciones para $\alpha$ son un par complejo conjugado, con parte real negativa. Así, las soluciones son productos de una exponencial decreciente, $e^{-\gamma t/2}$, por exponenciales complejas (o senos y cosenos), $e^{\pm i\omega t}$, donde

$$\omega^2 = \omega_0^2 - \gamma^2/4\,. \qquad \text{(2.9)}$$

Este es un oscilador subamortiguado.

La mayoría de los sistemas que consideramos osciladores están subamortiguados. Por ejemplo, un niño sentado quieto en un columpio de parque es un péndulo subamortiguado que puede oscilar muchas veces antes de que las fuerzas de fricción lo detengan.

La exponencial decreciente $e^{-\gamma t/2}e^{-i(\omega t-\theta)}$ describe una espiral hacia el origen en el plano complejo. Su parte real, $e^{-\gamma t/2}\cos(\omega t-\theta)$, describe una función que oscila con amplitud decreciente. En forma real, la solución general para el caso subamortiguado tiene la forma

$$x(t) = A\,e^{-\gamma t/2}\cos(\omega t-\theta)\,, \qquad \text{(2.10)}$$

o bien

$$x(t) = e^{-\gamma t/2}\left(c\cos(\omega t)+d\sin(\omega t)\right)\,, \qquad \text{(2.11)}$$

donde $A$ y $\theta$ están relacionados con $c$ y $d$ por (1.97) y (1.98). Esto se muestra en la figura 2.2 (compárese con la figura 1.9). La figura superior muestra el plano complejo con $e^{-\gamma t/2}e^{-i(\omega t-\theta)}$ representado para valores de $t$ igualmente espaciados. La figura inferior es la parte real, $\cos(\omega t-\theta)$, para los mismos valores de $t$, representada frente a $t$. En el caso subamortiguado, ¡la posición de equilibrio se cruza un número infinito de veces, aunque con amplitud decreciente exponencialmente!

![Figura 2.2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh2_ES/fig2.2.png)

Figura 2.2: exponencial compleja amortiguada — en el plano complejo, una espiral que converge al origen, $e^{-\gamma t/2}e^{-i(\omega t-\theta)}$; debajo, su parte real, $\cos(\omega t-\theta)$, mostrada como una senoide de amplitud decreciente frente a $t$.

### 2.1.3 Osciladores con amortiguamiento crítico

Si $\gamma/2=\omega_0$, entonces (2.4) da una única solución, $e^{-\gamma t/2}$. Sabemos que debe haber dos soluciones de la ecuación diferencial de segundo orden (2.2). Una forma de encontrar la otra solución es abordar esta situación como un límite del caso subamortiguado. Si escribimos las soluciones del caso subamortiguado en forma real, son $e^{-\gamma t/2}\cos\omega t$ y $e^{-\gamma t/2}\sin\omega t$. Tomando el límite de la primera cuando $\omega\to0$ da $e^{-\gamma t/2}$, la solución que ya conocemos. Tomando el límite de la segunda da 0. Sin embargo, si primero dividimos la segunda solución por $\omega$, sigue siendo una solución, porque $\omega$ no depende de $t$. Ahora podemos obtener un límite no nulo:

$$\lim_{\omega\to0}\frac{1}{\omega}e^{-\gamma t/2}\sin\omega t = t\,e^{-\gamma t/2}\,. \qquad \text{(2.12)}$$

Así, $t\,e^{-\gamma t/2}$ es también una solución. También puede comprobarlo explícitamente sustituyéndola de nuevo en (2.2). Este caso se llama amortiguamiento crítico porque es la frontera entre el sobreamortiguamiento y el subamortiguamiento.

Un sistema familiar cercano al amortiguamiento crítico es la combinación de muelles y amortiguadores de un automóvil. Aquí el amortiguamiento debe ser lo bastante grande como para evitar que el coche rebote. Pero si el amortiguamiento de los amortiguadores es demasiado alto, el coche no podrá responder rápidamente a los baches y la marcha será incómoda.

La solución general en el caso de amortiguamiento crítico es, por tanto,

$$c\,e^{-\gamma t/2} + d\,t\,e^{-\gamma t/2}\,. \qquad \text{(2.13)}$$

Esto se ilustra en la figura 2.3. La línea punteada es $e^{-\gamma t}$ para $\gamma=1\ \text{s}^{-1}$. La línea discontinua es $t\,e^{-\gamma t}$. La línea continua es una combinación lineal, $(1-t)\,e^{-\gamma t}$.

![Figura 2.3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh2_ES/fig2.3.png)

Figura 2.3: soluciones de la ecuación de movimiento para un oscilador con amortiguamiento crítico, entre $t=0$ y $t=10\ \text{s}$, análoga a la figura 2.1 pero para el caso crítico.

Como en la situación sobreamortiguada, no hay oscilación real en el amortiguamiento crítico. Sin embargo, de nuevo, la masa puede sobrepasar el equilibrio y luego regresar suavemente hacia la posición de equilibrio, sin cruzar nunca el valor de equilibrio del desplazamiento por segunda vez. Al igual que en el sobreamortiguamiento, la posición de equilibrio se cruza una vez o ninguna.

## 2.2 Oscilaciones forzadas

El oscilador amortiguado con una fuerza impulsora armónica tiene la ecuación de movimiento

$$\frac{d^2}{dt^2}x(t) + \gamma\,\frac{d}{dt}x(t) + \omega_0^2\,x(t) = F(t)/m\,, \qquad \text{(2.14)}$$

donde la fuerza es

$$F(t) = F_0\cos\omega_d t\,. \qquad \text{(2.15)}$$

A $\omega_d/2\pi$ se le llama la frecuencia impulsora. Note que no es necesariamente la misma que la frecuencia natural, $\omega_0/2\pi$, ni la frecuencia de oscilación del sistema libre, (2.9). Es simplemente la frecuencia de la fuerza externa. Puede ajustarse de forma completamente independiente de los demás parámetros del sistema. Sería correcto, aunque incómodo, referirse a $\omega_d$ como la frecuencia angular impulsora; simplemente la llamaremos frecuencia impulsora, ignorando su carácter angular.

Las frecuencias angulares, $\omega_d$ y $\omega_0$, aparecen en la ecuación de movimiento, (2.15), de formas completamente distintas. Debe tener presente esta distinción para entender la oscilación forzada. La frecuencia angular natural del sistema, $\omega_0$, es cierta combinación de las masas y las constantes de muelle (o las cantidades físicas relevantes que determinan las oscilaciones libres). La frecuencia angular $\omega_d$ entra solo a través de la dependencia temporal de la fuerza impulsora. Este es el aspecto nuevo de la oscilación forzada. Para explotar plenamente este aspecto nuevo, buscaremos una solución de la ecuación de movimiento que oscile con la misma frecuencia angular, $\omega_d$, que la fuerza impulsora.

Podemos relacionar (2.14) con una ecuación de movimiento con una fuerza impulsora compleja

$$\frac{d^2}{dt^2}z(t) + \gamma\,\frac{d}{dt}z(t) + \omega_0^2\,z(t) = \mathcal{F}(t)/m\,, \qquad \text{(2.16)}$$

donde

$$\mathcal{F}(t) = F_0\,e^{-i\omega_d t}\,. \qquad \text{(2.17)}$$

Esto funciona porque la ecuación de movimiento, (2.14), no involucra $i$ explícitamente y porque

$$\text{Re}\,\mathcal{F}(t) = F(t)\,. \qquad \text{(2.18)}$$

Si $z(t)$ es una solución de (2.16), entonces puede demostrar que $x(t)=\text{Re}\,z(t)$ es una solución de (2.14), tomando la parte real de ambos lados de (2.16).

La ventaja de la fuerza exponencial compleja en (2.16) es que es irreducible: se comporta de forma simple bajo traslaciones temporales. En particular, podemos encontrar una solución estacionaria proporcional a la fuerza impulsora, $e^{-i\omega_d t}$, mientras que para la fuerza impulsora real, las formas $\cos\omega_d t$ y $\sin\omega_d t$ se mezclan. Es decir, buscamos una solución estacionaria de la forma

$$z(t) = A\,e^{-i\omega_d t}\,. \qquad \text{(2.19)}$$

La solución estacionaria, (2.19), es una solución particular, no la solución más general de (2.16). Como se discutió en el capítulo 1, la solución más general de (2.16) se obtiene sumando a la solución particular la solución más general para el movimiento libre del mismo oscilador (soluciones de (2.3)). En general, tendremos que incluir estas contribuciones más generales para satisfacer las condiciones iniciales. Sin embargo, como hemos visto arriba, todas estas soluciones se extinguen exponencialmente con el tiempo. Se llaman soluciones «transitorias». Solo la solución estacionaria sobrevive durante mucho tiempo en presencia de amortiguamiento. A diferencia de las soluciones de la ecuación de movimiento libre, la solución estacionaria no tiene nada que ver con los valores iniciales del desplazamiento y la velocidad. Está determinada enteramente por la fuerza impulsora, (2.17). Explorará las soluciones transitorias en el problema 2.4.

Sustituyendo (2.19) y (2.17) en (2.16), y cancelando un factor $e^{-i\omega_d t}$ en cada lado de la ecuación resultante, obtenemos

$$(-\omega_d^2 - i\gamma\omega_d + \omega_0^2)\,A = \frac{F_0}{m}\,, \qquad \text{(2.20)}$$

o bien

$$A = \frac{F_0/m}{\omega_0^2 - i\gamma\omega_d - \omega_d^2}\,. \qquad \text{(2.21)}$$

Note que obtuvimos la solución usando solo álgebra. Esta es la ventaja de partir de la solución irreducible, (2.19).

La amplitud, (2.21), del desplazamiento es proporcional a la amplitud de la fuerza impulsora. Esto es justamente lo que esperamos de la linealidad (véase el problema 2.2). Pero el coeficiente de proporcionalidad es complejo. Para ver explícitamente su forma, multiplicamos el numerador y el denominador del lado derecho de (2.21) por $\omega_0^2+i\gamma\omega_d-\omega_d^2$, para llevar los números complejos al numerador:

$$A = \frac{\left(\omega_0^2+i\gamma\omega_d-\omega_d^2\right)F_0/m}{\left(\omega_0^2-\omega_d^2\right)^2+\gamma^2\omega_d^2}\,. \qquad \text{(2.22)}$$

El número complejo $A$ puede escribirse como $\mathcal{A}+i\mathcal{B}$, con $\mathcal{A}$ y $\mathcal{B}$ reales:

$$\mathcal{A} = \frac{\left(\omega_0^2-\omega_d^2\right)F_0/m}{\left(\omega_0^2-\omega_d^2\right)^2+\gamma^2\omega_d^2}\,; \qquad \text{(2.23)}$$

$$\mathcal{B} = \frac{\gamma\omega_d\,F_0/m}{\left(\omega_0^2-\omega_d^2\right)^2+\gamma^2\omega_d^2}\,. \qquad \text{(2.24)}$$

Entonces la solución de la ecuación de movimiento para la fuerza impulsora real, (2.14), es

$$x(t) = \text{Re}\,z(t) = \text{Re}\left(A\,e^{-i\omega_d t}\right) = \mathcal{A}\cos\omega_d t + \mathcal{B}\sin\omega_d t\,. \qquad \text{(2.25)}$$

Así, la solución para la fuerza real es una suma de dos términos. El término proporcional a $\mathcal{A}$ está en fase con la fuerza impulsora (o desfasado $180°$), mientras que el término proporcional a $\mathcal{B}$ está desfasado $90°$. La ventaja de pasar a la fuerza impulsora compleja es que nos permite obtener ambos a la vez. Los coeficientes $\mathcal{A}$ y $\mathcal{B}$ se muestran en la gráfica de la figura 2.4 para $\gamma=\omega_0/2$.

![Figura 2.4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh2_ES/fig2.4.png)

Figura 2.4: amplitudes elástica $\mathcal{A}$ (línea continua) y absortiva $\mathcal{B}$ (línea punteada), en unidades de $F_0/m\omega_0^2$, en función de $\omega_d$ entre 0 y $2\omega_0$; $\mathcal{A}$ pasa de positiva a negativa cruzando cero cerca de $\omega_d=\omega_0$, mientras $\mathcal{B}$ alcanza su máximo cerca de la resonancia.

La parte real de $A$, $\mathcal{A}=\text{Re}\,A$, se llama la amplitud elástica, y la parte imaginaria de $A$, $\mathcal{B}=\text{Im}\,A$, se llama la amplitud absortiva. La razón de estos nombres se hará evidente más abajo, cuando consideremos el trabajo realizado por la fuerza impulsora.

## 2.3 Resonancia

El término $\left(\omega_0^2-\omega_d^2\right)^2$ del denominador de (2.22) se anula para $\omega_d=\omega_0$. Si el amortiguamiento es pequeño, este comportamiento del denominador produce un enorme aumento en la respuesta del sistema a la fuerza impulsora en $\omega_d=\omega_0$. El fenómeno se llama resonancia. La frecuencia angular $\omega_0$ es la frecuencia angular de resonancia. Cuando $\omega_d=\omega_0$, se dice que el sistema está «en resonancia».

El fenómeno de la resonancia es a la vez familiar y espectacularmente importante. Es familiar en situaciones tan sencillas como aumentar la amplitud de un columpio infantil aplicando una pequeña fuerza en el mismo instante de cada ciclo. Aun siendo tan simple, es crucial en muchos dispositivos y en muchos experimentos delicados de física. Los fenómenos de resonancia se usan por doquier para generar una respuesta grande y medible a partir de una perturbación muy pequeña.

Muy a menudo ignoraremos el amortiguamiento en las oscilaciones forzadas. Cerca de una resonancia, esto no es buena idea, porque la amplitud, (2.22), tiende a infinito cuando $\gamma\to0$ para $\omega_d=\omega_0$. Los infinitos no son físicos. Este infinito nunca ocurre en la práctica: antes de que la amplitud «explote», sucede una de dos cosas. O bien el amortiguamiento deja de ser despreciable, de modo que la respuesta se parece a (2.22) con $\gamma$ no nulo, o bien la amplitud se hace tan grande que las no linealidades del sistema dejan de ser despreciables, de modo que la ecuación de movimiento deja de parecerse a (2.16).

### 2.3.1 Trabajo

Es instructivo considerar el trabajo realizado por la fuerza externa en (2.16). Para ello debemos usar la fuerza real, (2.14), y el desplazamiento real, (2.25), en lugar de sus extensiones complejas, porque, a diferencia de casi todo lo demás de lo que hablamos, el trabajo es una función no lineal de la fuerza. La potencia entregada por la fuerza es el producto de la fuerza impulsora y la velocidad,

$$P(t) = F(t)\,\frac{\partial}{\partial t}x(t) = -F_0\omega_d\,\mathcal{A}\cos\omega_d t\sin\omega_d t + F_0\omega_d\,\mathcal{B}\cos^2\omega_d t\,. \qquad \text{(2.26)}$$

El primer término de (2.26) es proporcional a $\sin2\omega_d t$. Así, a veces es positivo y a veces negativo. Se promedia a cero sobre cualquier semiperiodo completo de oscilación, un tiempo $\pi/\omega_d$, porque

$$\int_{t_0}^{t_0+\pi/\omega_d} dt\,\sin2\omega_d t = -\frac{1}{2}\cos2\omega_d t\Big|_{t_0}^{t_0+\pi/\omega_d} = 0\,. \qquad \text{(2.27)}$$

Por eso $\mathcal{A}$ se llama la amplitud elástica. Si $\mathcal{A}$ domina, entonces la energía introducida en el sistema en un momento dado se devuelve más tarde, como en una colisión elástica en mecánica.

El segundo término de (2.26), en cambio, siempre es positivo. Se promedia a

$$P_{\text{prom}} = \frac{1}{2}F_0\omega_d\,\mathcal{B}\,. \qquad \text{(2.28)}$$

Por eso $\mathcal{B}$ se llama la amplitud absortiva: mide la rapidez con la que el sistema absorbe energía. La potencia absorbida, $P_{\text{prom}}$, alcanza su máximo en resonancia, en $\omega_0=\omega_d$. Este es un criterio diagnóstico usado a menudo para encontrar resonancias en situaciones experimentales. Note que la dependencia de $\mathcal{B}$ con $\omega_d$ se parece cualitativamente a la de $P_{\text{prom}}$, mostrada en la figura 2.5 para $\gamma=\omega_0/2$. Sin embargo, difieren en un factor de $\omega_d$. En particular, el máximo de $\mathcal{B}$ ocurre ligeramente por debajo de la resonancia.

![Figura 2.5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh2_ES/fig2.5.png)

Figura 2.5: potencia media disipada por la fuerza de fricción en función de $\omega_d$, para $\gamma=\omega_0/2$; una curva con pico en $\omega_d=\omega_0$ de altura $F_0^2/2m\gamma$.

### 2.3.2 Anchura de la resonancia y vida media

Tanto la altura como la anchura de la curva de resonancia de la figura 2.5 están determinadas por el término friccional, $\gamma$, en la ecuación de movimiento. La potencia media máxima es inversamente proporcional a $\gamma$,

$$\frac{F_0^2}{2m\gamma}\,. \qquad \text{(2.29)}$$

La anchura (para una altura fija) está determinada por el cociente entre $\gamma$ y $\omega_0$. De hecho, puede comprobar que los valores de $\omega_d$ para los cuales la pérdida media de potencia es la mitad de su valor máximo son

$$\omega_{1/2} = \sqrt{\omega_0^2+\frac{\gamma^2}{4}} \pm \frac{\gamma}{2}\,. \qquad \text{(2.30)}$$

$\gamma$ es la «anchura total a media altura» de la curva de potencia. En las figuras 2.6 y 2.7 mostramos la potencia media en función de $\omega_d$ para $\gamma=\omega_0/4$ y $\gamma=\omega_0$. La dependencia lineal de la anchura con $\gamma$ se aprecia claramente. Las líneas punteadas muestran la posición de media altura.

![Figura 2.6](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh2_ES/fig2.6.png)

Figura 2.6 y 2.7: la misma curva de potencia media disipada frente a $\omega_d$ que en la figura 2.5, pero para $\gamma=\omega_0/4$ (pico estrecho) y $\gamma=\omega_0$ (pico ancho), respectivamente, mostrando cómo la anchura de la resonancia crece linealmente con $\gamma$.

Esta relación es aún más interesante en vista de la relación entre $\gamma$ y la dependencia temporal de la oscilación libre. La vida media del estado en oscilación libre es del orden de $1/\gamma$. En otras palabras, la anchura del pico de resonancia en la oscilación forzada es inversamente proporcional a la vida media del modo normal correspondiente de oscilación libre. Esta relación inversa es importante en muchos campos de la física. Un ejemplo extremo es la física de partículas, donde partículas de vida muy corta pueden describirse como resonancias. Las ondas cuánticas asociadas a estas partículas tienen frecuencias angulares proporcionales a sus energías,

$$E = \hbar\omega \qquad \text{(2.31)}$$

donde $\hbar$ es la constante de Planck dividida entre $2\pi$,

$$\hbar \approx 6.626\times10^{-34}\ \text{J}\,\text{s}\,. \qquad \text{(2.32)}$$

Las vidas medias de estas partículas, algunas tan cortas como $10^{-24}$ segundos, son demasiado breves para medirse directamente. Sin embargo, la vida corta se manifiesta en la gran anchura de la distribución de energías de estos estados. Así es como en realidad se infieren las vidas medias.

### 2.3.3 Retraso de fase

También podemos escribir (2.25) como

$$x(t) = R\cos(\omega_d t-\theta) \qquad \text{(2.33)}$$

para

$$R = \sqrt{\mathcal{A}^2+\mathcal{B}^2}\,,\qquad \theta = \arg(\mathcal{A}+i\mathcal{B})\,. \qquad \text{(2.34)}$$

El ángulo de fase, $\theta$, mide el retraso de fase entre la fuerza externa y la respuesta del sistema. El retraso temporal real es $\theta/\omega_d$. El desplazamiento alcanza su máximo un tiempo $\theta/\omega_d$ después de que la fuerza alcance el suyo.

Note que a medida que la frecuencia aumenta, $\theta$ aumenta y el movimiento queda cada vez más rezagado respecto a la fuerza externa. El ángulo de fase, $\theta$, está determinado por la importancia relativa de la fuerza restauradora y la inercia del oscilador. A frecuencias bajas (comparadas con $\omega_0$), la inercia (una palabra imprecisa para el término $ma$ de la ecuación de movimiento) es casi irrelevante, porque las cosas se mueven muy lentamente, y el movimiento está casi en fase con la fuerza. Muy por encima de la resonancia, la inercia domina. La masa ya no puede seguir el ritmo de la fuerza restauradora, y el movimiento está casi $180°$ desfasado respecto a la fuerza. Desarrollaremos un ejemplo detallado de esto en la siguiente sección.

El retraso de fase pasa por $\pi/2$ en la resonancia, como se muestra en la gráfica de la figura 2.8 para $\gamma=\omega_0/2$. Un retraso de fase de $\pi/2$ es otro criterio diagnóstico frecuentemente usado para la resonancia.

![Figura 2.8](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh2_ES/fig2.8.png)

Figura 2.8: retraso de fase $\theta$ frente a la frecuencia $\omega_d$ en un oscilador forzado amortiguado; $\theta$ crece de forma monótona desde 0 hasta $\pi$, pasando por $\pi/2$ exactamente en $\omega_d=\omega_0$.

## 2.4 Un ejemplo

### 2.4.1 Sintiéndolo en los huesos

*(Referencia al programa interactivo 2-1 del disco de programas del curso original.)*

Discutiremos más a fondo la física de las oscilaciones forzadas en el contexto del sistema simple mostrado en la figura 2.9. El bloque tiene masa $m$. El bloque se mueve en un fluido viscoso que proporciona una fuerza de fricción. Imaginaremos que el fluido es algo así como un aceite de silicona espeso, de modo que la solución estacionaria se alcanza muy rápidamente. El bloque está unido a una cuerda que pasa por una polea y se conecta a un muelle, como se muestra. El muelle tiene constante $K$. Usted sostiene el otro extremo del muelle y lo mueve hacia adelante y hacia atrás con desplazamiento

$$d_0\cos\omega_d t\,. \qquad \text{(2.35)}$$

![Figura 2.9](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh2_ES/fig2.9.png)

Figura 2.9: bloque en un recipiente con fluido viscoso, unido mediante una cuerda que pasa por una polea a un muelle cuyo extremo libre se mueve como $d_0\cos\omega_d t$.

En este montaje, no hace falta que usted esté dentro del fluido viscoso junto al bloque —lo que facilita mucho la respiración.

La pregunta es: ¿cómo se mueve el bloque? Este sistema tiene exactamente la ecuación de movimiento del oscilador amortiguado y forzado. Para verlo, note que el cambio en la longitud del muelle respecto a su longitud de equilibrio es la diferencia

$$x(t) - d_0\cos\omega_d t\,. \qquad \text{(2.36)}$$

Así, la ecuación de movimiento se ve así:

$$m\,\frac{d^2}{dt^2}x(t) + m\gamma\,\frac{d}{dt}x(t) = -K\left[x(t)-d_0\cos\omega_d t\right]\,. \qquad \text{(2.37)}$$

Dividiendo por $m$ y reordenando términos, puede ver que esto es idéntico a (2.14) con

$$F_0/m = K d_0/m = \omega_0^2 d_0\,. \qquad \text{(2.38)}$$

Mover el otro extremo del muelle sinusoidalmente produce, en efecto, una fuerza sinusoidal variable sobre la masa.

Ahora repasaremos de nuevo la solución, resaltando la física de este sistema a medida que avanzamos. ¡Intente imaginarse realmente haciendo el experimento! Le ayudará tratar de sentir las fuerzas involucradas en sus propios huesos.

El primer paso es pasar a la fuerza compleja, como en (2.16). El resultado se ve así:

$$\underbrace{\frac{d^2}{dt^2}z(t)}_{\text{inercial}} + \underbrace{\gamma\,\frac{d}{dt}z(t)}_{\text{friccional}} + \underbrace{\omega_0^2\,z(t)}_{\text{muelle}} = \underbrace{\omega_0^2\,d_0\,e^{-i\omega_d t}}_{\text{impulsor}}\,. \qquad \text{(2.39)}$$

Hemos etiquetado los términos de (2.39) para recordarle sus distintos orígenes físicos.

El siguiente paso es buscar soluciones estacionarias irreducibles de la forma de (2.19):

$$z(t) = A\,e^{-i\omega_d t}\,. \qquad \text{(2.40)}$$

Sustituyendo (2.40) en (2.39), obtenemos

$$\left[-\omega_d^2 - i\gamma\omega_d + \omega_0^2\right]A\,e^{-i\omega_d t} = \omega_0^2\,d_0\,e^{-i\omega_d t}\,. \qquad \text{(2.41)}$$

Lo que discutiremos en detalle es la fase de la cantidad entre corchetes del lado izquierdo de (2.41). Cada uno de los tres términos —inercial, friccional y de muelle— tiene una fase distinta. Cada término también depende de la frecuencia angular $\omega_d$ de una forma diferente. La fase de $A$ depende de cuál término domina.

Para $\omega_d$ muy pequeño, en particular para

$$\omega_d \ll \omega_0,\ \gamma\,, \qquad \text{(2.42)}$$

el término de muelle domina la suma. Entonces $A$ está en fase con la fuerza impulsora. Esto tiene una interpretación física simple. Si mueve el extremo del muelle suficientemente despacio, tanto la fricción como la inercia son irrelevantes. Cuando el bloque se mueve muy lentamente, se requiere una fuerza casi nula. El bloque simplemente sigue el desplazamiento del extremo del muelle, $A\approx d_0$. Debería poder sentir esta dependencia en sus huesos: si mueve la mano muy despacio, la masa no tiene ninguna dificultad para seguirle el ritmo.

Para $\omega_d$ muy grande, es decir, para

$$\omega_d \gg \omega_0,\ \gamma\,, \qquad \text{(2.43)}$$

el término inercial domina la suma. El desplazamiento queda entonces desfasado $180°$ respecto a la fuerza impulsora. También se hace cada vez más pequeño a medida que $\omega_d$ aumenta, comportándose como

$$A \approx -\frac{\omega_0^2}{\omega_d^2}\,d_0\,. \qquad \text{(2.44)}$$

De nuevo, esto tiene sentido físicamente. Cuando la frecuencia angular de la fuerza impulsora se hace muy grande, la masa simplemente no tiene tiempo de moverse.

En un régimen intermedio, al menos dos de los tres términos del lado izquierdo de (2.41) contribuyen significativamente a la suma. En resonancia, el término inercial cancela exactamente al término de muelle, dejando solo el término friccional, de modo que el desplazamiento queda desfasado $90°$ respecto a la fuerza impulsora. El tamaño de la fuerza de amortiguamiento determina cuán aguda es la resonancia. Si $\gamma$ es mucho menor que $\omega_0$, entonces la cancelación entre los términos inercial y de muelle en (2.39) debe ser muy precisa para que el término friccional domine. En este caso, la resonancia es muy aguda. Por otro lado, si $\gamma \gg \omega_0$, la resonancia es muy amplia, y el realce en la resonancia no es muy grande, porque el término friccional domina en un amplio rango de $\omega_d$ alrededor del punto de resonancia, $\omega_d=\omega_0$.

¡Inténtelo! No hay sustituto para hacer realmente este experimento. Le dará una verdadera sensación de en qué consiste la resonancia. Empiece moviendo la mano a una frecuencia muy baja, de modo que el bloque se mantenga en fase con el movimiento de su mano. Luego aumente muy gradualmente la frecuencia. Si cambia la frecuencia lo bastante despacio, las contribuciones de la oscilación libre transitoria serán pequeñas, y usted permanecerá cerca de la solución estacionaria. A medida que la frecuencia aumenta, verá primero que, debido a la fricción, el bloque empieza a retrasarse respecto a su mano. Al atravesar la resonancia, este retraso aumentará y pasará por $90°$. Finalmente, a frecuencia muy alta, el bloque estará desfasado $180°$ respecto a su mano y su desplazamiento (la amplitud de su movimiento) será muy pequeño.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Resolver el movimiento libre del oscilador armónico amortiguado buscando las soluciones exponenciales complejas irreducibles;
2.  Encontrar la solución estacionaria del oscilador armónico amortiguado con un término impulsor armónico, estudiando el problema correspondiente con una fuerza exponencial compleja y encontrando la solución exponencial compleja irreducible;
3.  Calcular la potencia perdida por fuerzas de fricción y el retraso de fase en el oscilador armónico forzado;
4.  ¡Sentirlo en los huesos!

## Problemas

**2.1.** Demuestre que un oscilador sobreamortiguado puede cruzar su posición de equilibrio como máximo una vez.

**2.2.** Demuestre, usando solamente la linealidad, sin usar la solución explícita, que la solución estacionaria de (2.16) debe ser proporcional a $F_0$.

**2.3.** Para el sistema con ecuación de movimiento (2.14), suponga que la fuerza impulsora tiene la forma

$$f_0\cos\omega_0 t\cos\delta t$$

donde

$$\delta \ll \omega_0 \quad\text{y}\quad \gamma=0\,.$$

Cuando $\delta\to0$, esto entra en resonancia. ¿Cuál es el desplazamiento para $\delta$ no nulo, a orden principal en $\delta/\omega_0$? Escriba el resultado en la forma

$$\alpha(t)\cos\omega_0 t + \beta(t)\sin\omega_0 t$$

y encuentre $\alpha(t)$ y $\beta(t)$. Discuta la física de este resultado. Pista: primero demuestre que

$$\cos\omega_0 t\cos\delta t = \frac{1}{2}\text{Re}\left(e^{-i(\omega_0+\delta)t}+e^{-i(\omega_0-\delta)t}\right)\,.$$

**2.4.** Para el sistema mostrado en la figura 2.9, suponga que el desplazamiento del extremo del alambre se anula para $t<0$, y tiene la forma

$$d_0\sin\omega_d t \quad\text{para } t\ge0\,.$$

1.  Encuentre el desplazamiento del bloque para $t>0$. Escriba la solución como la parte real de una solución compleja, usando una fuerza compleja y soluciones exponenciales. No intente simplificar los números complejos. Pista: use (2.23), (2.24) y (2.6). Si se confunde, pase al apartado b.

2.  Encuentre la solución cuando $\gamma\to0$ y simplifique el resultado. Incluso si se confundió con los números complejos en el apartado a, debería poder encontrar la solución en este límite. ¡Cuando no hay amortiguamiento, las soluciones «transitorias» no se extinguen con el tiempo!

**2.5.** Para el circuito LC mostrado en la figura 1.10, suponga que el inductor tiene resistencia no nula, $R$. Escriba la ecuación de movimiento de este sistema y encuentre la relación entre el término friccional, $m\gamma$, del oscilador armónico amortiguado y la resistencia, $R$, que completa la correspondencia de (1.105). Suponga que el condensador tiene capacitancia $C\approx0.00667\ \mu\text{F}$, el inductor tiene inductancia $L\approx150\ \mu\text{H}$ y la resistencia es $R\approx15\ \Omega$. Resuelva la ecuación de movimiento y evalúe las constantes que aparecen en su solución en unidades de segundos.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.


---

<!-- MIT8.03_TextCh3_ES.md -->

# Capítulo 3: Modos normales

Los sistemas con varios grados de libertad parecen mucho más complicados que el oscilador armónico simple. Lo que veremos en este capítulo es que esto es una ilusión. Cuando lo miramos de la manera adecuada, podemos ver los osciladores simples dentro del sistema más complicado.

## Vídeos de esta clase (YouTube)

- [Clase 4: Osciladores acoplados, modos normales](https://www.youtube.com/watch?v=BX4QPdP7fT8)
- [Clase 5: Modos normales (continuación)](https://www.youtube.com/watch?v=I0YACDaY-ww)

## Resumen previo

En este capítulo discutimos la oscilación armónica en sistemas con más de un grado de libertad.

1.  Escribiremos las ecuaciones de movimiento de un sistema de partículas sometidas a fuerzas restauradoras lineales generales, sin amortiguamiento.
2.  A continuación, introducimos las matrices y la multiplicación de matrices, y mostramos cómo pueden usarse para simplificar la descripción de las ecuaciones de movimiento deducidas en la sección anterior.
3.  Después usaremos la invariancia bajo traslación temporal para encontrar las soluciones irreducibles de las ecuaciones de movimiento en forma matricial. Esto conducirá a la idea de «modos normales». Luego mostraremos cómo combinar los modos normales para construir la solución general de las ecuaciones de movimiento.
4.  - Introduciremos la idea de «coordenadas normales» y mostraremos cómo pueden usarse para automatizar la solución del problema de valores iniciales.
5.  - Discutiremos la oscilación forzada amortiguada en sistemas con muchos grados de libertad.

## 3.1 Más de un grado de libertad

En general, el número de grados de libertad de un sistema es el número de coordenadas independientes necesarias para especificar la configuración del sistema. Cuantos más grados de libertad tenga el sistema, mayor será el número de formas independientes en que puede moverse. Cabría pensar que, cuantos más movimientos posibles, más complicado será analizar el sistema. Sin embargo, usando las herramientas del álgebra lineal, veremos que podemos tratar sistemas con muchos grados de libertad de forma directa.

### 3.1.1 Dos osciladores acoplados

![Figura 3.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh3_ES/fig3.1.png)

Figura 3.1: dos péndulos de longitud $\ell$ colgando de soportes fijos, con sus masas conectadas entre sí por un muelle horizontal.

Considere el sistema de dos péndulos mostrado en la figura 3.1. Los péndulos consisten en varillas rígidas pivotadas en su extremo superior, de modo que oscilan sin fricción en el plano del papel. Las masas en los extremos de las varillas están acopladas por un muelle. Consideraremos el movimiento libre del sistema, sin más fuerzas externas que la gravedad. Este es un ejemplo clásico de dos «osciladores acoplados». El muelle que conecta los dos osciladores es el acoplamiento. Supondremos que el muelle de la figura 3.1 no está estirado cuando los dos péndulos cuelgan verticalmente, como se muestra. Entonces la configuración de equilibrio es la mostrada en la figura 3.1. Este es un ejemplo de un sistema con dos grados de libertad, porque se necesitan dos cantidades —los desplazamientos de cada uno de los dos bloques respecto al equilibrio— para especificar la configuración del sistema. Por ejemplo, si las oscilaciones son pequeñas, podemos especificar la configuración dando el desplazamiento horizontal de cada uno de los dos bloques respecto a la posición de equilibrio.

Suponga que el bloque 1 tiene masa $m_1$, el bloque 2 tiene masa $m_2$, ambos péndulos tienen longitud $\ell$ y la constante del muelle es $\kappa$ (letra griega kappa). Denote los (pequeños) desplazamientos horizontales de los bloques hacia la derecha como $x_1$ y $x_2$, como se muestra en la figura 3.2. Podríamos haber llamado a estas masas y desplazamientos de cualquier otra forma, pero es muy conveniente usar el mismo símbolo, $x$, con subíndices distintos. Entonces podemos escribir la ley de Newton, $F=ma$, en una forma compacta y útil,

$$m_j\,\frac{d^2}{dt^2}x_j = F_j\,, \qquad \text{(3.1)}$$

para $j=1$ a $2$, donde $F_1$ es la fuerza horizontal sobre el bloque 1 y $F_2$ es la fuerza horizontal sobre el bloque 2. Como hay dos valores de $j$, (3.1) representa dos ecuaciones: una para $j=1$ y otra para $j=2$. Estas son las dos ecuaciones de movimiento del sistema con dos grados de libertad. A menudo nos referiremos a todas las masas, desplazamientos o fuerzas a la vez como $m_j$, $x_j$ o $F_j$, respectivamente. Por ejemplo, diremos que $F_j$ es la fuerza horizontal sobre el $j$-ésimo bloque. Este es un ejemplo del uso de «índices» ($j$ es un índice) para simplificar la descripción de un sistema con más de un grado de libertad.

![Figura 3.2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh3_ES/fig3.2.png)

Figura 3.2: los mismos dos péndulos, ahora desplazados de su posición de equilibrio en las cantidades horizontales $x_1$ y $x_2$.

Cuando los bloques se mueven horizontalmente, también se mueven verticalmente, porque la longitud de los péndulos permanece fija. Como el desplazamiento vertical es de segundo orden en las $x_j$,

$$y_j \approx \frac{x_j^2}{2}\,, \qquad \text{(3.2)}$$

podemos ignorarlo al pensar en el muelle. El muelle permanece aproximadamente horizontal para oscilaciones pequeñas.

Para encontrar la ecuación de movimiento de este sistema, debemos encontrar las fuerzas, $F_j$, en función de los desplazamientos, $x_j$. Es la linealidad aproximada del sistema la que nos permite hacer esto de forma útil. Las fuerzas producidas por el muelle (ley de Hooke) y las fuerzas horizontales sobre los péndulos debidas a la tensión de la cuerda (que a su vez se debe a la gravedad) son ambas funciones aproximadamente lineales de los desplazamientos, para desplazamientos pequeños. Además, las fuerzas se anulan cuando ambos desplazamientos son nulos, porque el sistema está en equilibrio.

![Figura 3.3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh3_ES/fig3.3.png)

Figura 3.3: los dos péndulos con el bloque 2 desplazado una cantidad $x_2$ y el bloque 1 mantenido en su posición de equilibrio.

Así, cada una de las fuerzas es cierta constante (distinta para cada bloque) multiplicada por $x_1$, más otra constante multiplicada por $x_2$. Conviene escribir esto así:

$$F_1 = -K_{11}x_1 - K_{12}x_2\,,\qquad F_2 = -K_{21}x_1 - K_{22}x_2\,, \qquad \text{(3.3)}$$

o, más compactamente,

$$F_j = -\sum_{k=1}^{2}K_{jk}\,x_k \qquad \text{(3.4)}$$

para $j=1$ a $2$. Hemos escrito las cuatro constantes como $K_{11}$, $K_{12}$, $K_{21}$ y $K_{22}$ para escribir la fuerza de esta forma compacta. Más adelante llamaremos a estas constantes los elementos de la matriz $K$. Con esta notación, las ecuaciones de movimiento son

$$m_j\,\frac{d^2}{dt^2}x_j = -\sum_{k=1}^{2}K_{jk}\,x_k \qquad \text{(3.5)}$$

para $j=1$ a $2$.

![Figura 3.4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh3_ES/fig3.4.png)

Figura 3.4: fuerzas sobre los dos bloques del sistema de la figura 3.3 — las tensiones $T_1$ y $T_2$ de las cuerdas, las fuerzas del muelle $\kappa x_2$ sobre el bloque 1 y $-\kappa x_2$ sobre el bloque 2, y los pesos $m_1g$ y $m_2g$.

Debido a la linealidad del sistema, podemos encontrar las constantes $K_{jk}$ considerando los desplazamientos de los bloques uno a la vez. Luego encontramos la fuerza total usando (3.4). Por ejemplo, supongamos que desplazamos el bloque 2 manteniendo el bloque 1 fijo en su posición de equilibrio, y observamos las fuerzas sobre ambos bloques. Esto nos permitirá calcular $K_{12}$ y $K_{22}$. El sistema con el bloque 2 desplazado se muestra en la figura 3.3. Las fuerzas sobre los bloques se muestran en la figura 3.4, donde $T_j$ es la tensión de la cuerda del $j$-ésimo péndulo. $F_{12}$ es la fuerza sobre el bloque 1 debida al desplazamiento del bloque 2. $F_{22}$ es la fuerza sobre el bloque 2 debida a su propio desplazamiento. Para desplazamientos pequeños, la fuerza restauradora del muelle es casi horizontal e igual a $\kappa x_2$ sobre el bloque 1 y $-\kappa x_2$ sobre el bloque 2. Asimismo, en el límite de desplazamiento pequeño, la componente vertical de la fuerza de la tensión $T_2$ casi cancela la fuerza gravitatoria sobre el bloque 2, $m_2g$, de modo que la componente horizontal de la tensión da una fuerza restauradora $-x_2m_2g/\ell$ sobre el bloque 2. Para el bloque 1, la fuerza de la tensión $T_1$ simplemente cancela la fuerza gravitatoria $m_1g$. Así,

$$F_{12} \approx \kappa x_2\,,\qquad F_{22} \approx -\frac{m_2g\,x_2}{\ell} - \kappa x_2\,, \qquad \text{(3.6)}$$

y

$$K_{12} \approx -\kappa\,,\qquad K_{22} \approx \frac{m_2g}{\ell}+\kappa\,. \qquad \text{(3.7)}$$

Un argumento análogo muestra que

$$K_{21} \approx -\kappa\,,\qquad K_{11} \approx \frac{m_1g}{\ell}+\kappa\,. \qquad \text{(3.8)}$$

Note que

$$K_{12} = K_{21}\,. \qquad \text{(3.9)}$$

Veremos más abajo que este es un ejemplo de una relación muy general.

### 3.1.2 Linealidad y modos normales

*(Referencia al programa interactivo 3-1 del disco de programas del curso original.)*

Veremos en este capítulo que el movimiento más general posible de este sistema, y de cualquier sistema así de osciladores, puede descomponerse en soluciones particularmente simples, en las que todos los grados de libertad oscilan con la misma frecuencia. Estas soluciones simples se llaman «modos normales». Los desplazamientos del movimiento más general pueden escribirse como sumas de las soluciones simples. Estudiaremos esto en detalle más adelante, pero puede ser útil verlo primero. Para este sistema, el modo normal de frecuencia menor es aquel en el que los desplazamientos de los dos bloques son iguales:

$$x_1(t) = x_2(t) = b_1\cos(\omega_1t-\theta_1)\,. \qquad \text{(3.10)}$$

El otro modo normal es aquel en el que los desplazamientos de los dos bloques son opuestos:

$$x_1(t) = -x_2(t) = b_2\cos(\omega_2t-\theta_2)\,. \qquad \text{(3.11)}$$

La suma de estos dos movimientos simples da el movimiento mucho más complicado que se muestra en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-3-1" rel="noopener" target="_blank" title="Animación original de Howard Georgi">3-1</a>.

### 3.1.3 $n$ osciladores acoplados

Antes de intentar resolver las ecuaciones de movimiento, (3.5), generalicemos la discusión a sistemas con más grados de libertad. Considere la oscilación de un sistema de $n$ partículas conectadas por diversos muelles, sin amortiguamiento. Nuestro análisis será completamente general, pero, por simplicidad, hablaremos de las partículas como si estuvieran obligadas a moverse en la dirección $x$, de modo que podamos medir el desplazamiento de la $j$-ésima partícula respecto al equilibrio con la coordenada $x_j$. Entonces la configuración de equilibrio es aquella en la que todas las $x_j$ son cero.

La ley de Newton, $F=ma$, para el movimiento del sistema da

$$m_j\,\frac{d^2x_j}{dt^2} = F_j \qquad \text{(3.12)}$$

donde $m_j$ es la masa de la $j$-ésima partícula y $F_j$ es la fuerza sobre ella. Como el sistema es lineal, esperamos poder escribir la fuerza de la siguiente forma (como en (3.4)):

$$F_j = -\sum_{k=1}^{n}K_{jk}\,x_k \qquad \text{(3.13)}$$

para $j=1$ a $n$. La constante, $-K_{jk}$, es la fuerza por unidad de desplazamiento de la $j$-ésima partícula debida a un desplazamiento $x_k$ de la $k$-ésima partícula. Note que todas las $F_j$ se anulan en el equilibrio, cuando todas las $x_j$ son cero. Así, las ecuaciones de movimiento son

$$m_j\,\frac{d^2x_j}{dt^2} = -\sum_k K_{jk}\,x_k \qquad \text{(3.14)}$$

para $j=1$ a $n$.

Para medir $K_{jk}$, haga un pequeño desplazamiento $x_k$ de la $k$-ésima partícula, manteniendo fijas en cero a todas las demás partículas (posición supuesta de equilibrio). Luego mida la fuerza, $F_{jk}$, sobre la $j$-ésima partícula, con solo la $k$-ésima partícula desplazada. Como el sistema es lineal (porque está hecho de muelles, o en general, mientras el desplazamiento sea suficientemente pequeño), la fuerza es proporcional al desplazamiento $x_k$. El cociente entre $F_{jk}$ y $x_k$ es $-K_{jk}$:

$$K_{jk} = -F_{jk}/x_k \quad\text{cuando } x_\ell=0 \text{ para } \ell\neq k\,. \qquad \text{(3.15)}$$

Note que $K_{jk}$ se define con un signo $-$, de modo que un $K$ positivo es una fuerza opuesta al desplazamiento, y por tanto tiende a devolver el sistema al equilibrio.

Como el sistema es lineal, la fuerza total debida a un desplazamiento arbitrario es la suma de las contribuciones de cada desplazamiento. Así,

$$F_j = \sum_k F_{jk} = -\sum_k K_{jk}\,x_k\,. \qquad \text{(3.16)}$$

Tratemos ahora de entender (3.9). Si consideramos sistemas sin amortiguamiento, las fuerzas pueden derivarse de una energía potencial,

$$F_j = -\frac{\partial V}{\partial x_j}\,. \qquad \text{(3.17)}$$

Pero entonces, derivando la ecuación (3.16), encontramos que

$$K_{jk} = \frac{\partial^2V}{\partial x_j\partial x_k}\,. \qquad \text{(3.18)}$$

Las derivadas parciales conmutan entre sí, así que la ecuación (3.18) implica

$$K_{jk} = K_{kj}\,. \qquad \text{(3.19)}$$

En palabras: la fuerza sobre la partícula $j$ debida al desplazamiento de la partícula $k$ es igual a la fuerza sobre la partícula $k$ debida al desplazamiento de la partícula $j$.

## 3.2 Matrices

Es muy útil reescribir la ecuación (3.14) en notación matricial. Debido a la linealidad de las ecuaciones de movimiento del movimiento armónico, será muy útil tener a mano las herramientas del álgebra lineal para nuestro estudio de los fenómenos ondulatorios. Si no ha estudiado álgebra lineal (o no entendió gran parte de ella en sus cursos de matemáticas), NO SE ALARME. Empezaremos desde cero, describiendo las propiedades de las matrices y la multiplicación de matrices. Lo importante que debe tener presente es que las matrices no son nada profundo ni mágico: son simplemente herramientas de contabilidad diseñadas para facilitarle la vida cuando trata con más de una ecuación a la vez.

Una matriz es un arreglo rectangular de números. Una matriz $N\times M$ tiene $N$ filas y $M$ columnas. Las matrices pueden sumarse y restarse simplemente sumando y restando cada una de sus componentes. La diferencia surge en la multiplicación. Es muy conveniente definir una ley de multiplicación que defina el producto de una matriz $N\times M$ por la izquierda con una matriz $M\times L$ por la derecha (¡el orden importa!) como una matriz $N\times L$ de la siguiente forma:

Llame $A$ a la matriz $N\times M$, y sea $A_{jk}$ el número en la fila $j$ y columna $k$, para $1\le j\le N$ y $1\le k\le M$. Estas componentes individuales de la matriz se llaman elementos de matriz. En términos de sus elementos, la matriz $A$ se ve así:

$$A = \begin{pmatrix} A_{11} & A_{12} & \cdots & A_{1M}\\ A_{21} & A_{22} & \cdots & A_{2M}\\ \vdots & \vdots & \ddots & \vdots\\ A_{N1} & A_{N2} & \cdots & A_{NM} \end{pmatrix}\,. \qquad \text{(3.20)}$$

Llame $B$ a la matriz $M\times L$, con elementos $B_{kl}$ para $1\le k\le M$ y $1\le l\le L$:

$$B = \begin{pmatrix} B_{11} & B_{12} & \cdots & B_{1L}\\ B_{21} & B_{22} & \cdots & B_{2L}\\ \vdots & \vdots & \ddots & \vdots\\ B_{M1} & B_{M2} & \cdots & B_{ML} \end{pmatrix}\,. \qquad \text{(3.21)}$$

Llame $C$ a la matriz $N\times L$, con elementos $C_{jl}$ para $1\le j\le N$ y $1\le l\le L$:

$$C = \begin{pmatrix} C_{11} & C_{12} & \cdots & C_{1L}\\ C_{21} & C_{22} & \cdots & C_{2L}\\ \vdots & \vdots & \ddots & \vdots\\ C_{N1} & C_{N2} & \cdots & C_{NL} \end{pmatrix}\,. \qquad \text{(3.22)}$$

Entonces la matriz $C$ se define como el producto de matrices $AB$ si

$$C_{jl} = \sum_{k=1}^{M}A_{jk}\cdot B_{kl}\,. \qquad \text{(3.23)}$$

La ecuación (3.23) es el enunciado algebraico de la «regla fila-columna». Para calcular el elemento $j\ell$ de la matriz producto, $AB$, tome la fila $j$ de la matriz $A$ y la columna $\ell$ de la matriz $B$, y forme su producto escalar (correspondiente a la suma sobre $k$ en (3.23)).

Por ejemplo,

$$\begin{pmatrix} 2 & 3\\ 0 & 1\\ 2 & -1 \end{pmatrix} \cdot \begin{pmatrix} 1 & 0 & 2\\ 0 & 1 & 3 \end{pmatrix} = \begin{pmatrix} 2 & 3 & 13\\ 0 & 1 & 3\\ 2 & -1 & 1 \end{pmatrix}\,. \qquad \text{(3.25)}$$

Es fácil comprobar que el producto matricial así definido es asociativo, $(AB)C=A(BC)$. Sin embargo, en general no es conmutativo, $AB\neq BA$. De hecho, si las matrices no son cuadradas, ¡el producto en el orden opuesto puede ni siquiera tener sentido! El producto matricial $AB$ solo tiene sentido si el número de columnas de $A$ coincide con el número de filas de $B$. ¡Cuidado!

Salvo por el hecho de que no es conmutativa, la multiplicación de matrices se comporta de forma muy parecida a la multiplicación ordinaria. Por ejemplo, existen matrices «identidad». La matriz identidad $N\times N$, llamada $I$, tiene ceros en todas partes salvo unos en la diagonal. Por ejemplo, la matriz identidad $3\times 3$ es

$$I = \begin{pmatrix} 1&0&0\\0&1&0\\0&0&1 \end{pmatrix}\,. \qquad \text{(3.26)}$$

La matriz identidad $N\times N$ satisface

$$\begin{aligned}
& IA=AI=A \text{ para cualquier matriz } N\times N,\ A;\\
& IB=B \text{ para cualquier matriz } N\times M,\ B;\\
& CI=C \text{ para cualquier matriz } M\times N,\ C. \qquad \text{(3.27)}
\end{aligned}$$

Nos concentraremos principalmente en matrices «cuadradas» (es decir, $N\times N$).

Las matrices nos permiten manejar muchas ecuaciones lineales a la vez.

Un vector columna de dimensión $N$ puede verse como una matriz $N\times1$. Llamaremos a este objeto un «$N$-vector». No debe confundirse con un vector de coordenadas en el espacio tridimensional. Del mismo modo, podemos pensar en un vector fila de dimensión $N$ como una matriz $1\times N$. La multiplicación matricial también puede describir el producto de una matriz por un vector, dando otro vector. El caso particularmente importante que necesitaremos para analizar los fenómenos ondulatorios involucra matrices cuadradas. Considere una matriz $N\times N$, $A$, que multiplica a un $N$-vector $X$, dando otro $N$-vector $F$. La matriz cuadrada $A$ tiene $N^2$ elementos, $A_{jk}$, para $j$ y $k=1$ a $N$. Los vectores $X$ y $F$ tienen cada uno $N$ componentes, $X_j$ y $F_j$, para $j=1$ a $N$. Entonces la ecuación matricial

$$AX=F \qquad \text{(3.28)}$$

representa en realidad $N$ ecuaciones:

$$\sum_{k=1}^{N}A_{jk}\cdot X_k = F_j \qquad \text{(3.29)}$$

para $j=1$ a $N$. En otras palabras, estas son $N$ ecuaciones lineales simultáneas para las $N$ incógnitas $X_j$. Ya sabe, por sus estudios de álgebra, cómo resolver las $X_j$ en función de las $F_j$ y las $A_{jk}$, pero es muy útil hacerlo en notación matricial. A veces podemos encontrar la «inversa» de la matriz $A$, $A^{-1}$, que tiene la propiedad

$$A\,A^{-1} = A^{-1}A = I\,, \qquad \text{(3.30)}$$

donde $I$ es la matriz identidad discutida en (3.26) y (3.27). Si podemos encontrar tal matriz, entonces las $N$ ecuaciones lineales simultáneas, (3.29), tienen una solución única que podemos escribir de forma muy compacta. Multiplicando ambos lados de (3.29) por $A^{-1}$, y usando (3.30) y (3.27) en el lado izquierdo para eliminar $A^{-1}A$, podemos escribir la solución así:

$$X = A^{-1}F\,. \qquad \text{(3.31)}$$

### 3.2.1 \* Inversa y determinante

Podemos calcular $A^{-1}$ en términos del «determinante» de $A$. El determinante de la matriz $A$ es una suma de productos de los elementos de $A$ con las siguientes propiedades:

- Hay $N!$ términos en la suma;
- Cada término de la suma es un producto de $N$ elementos de matriz distintos;
- En cada producto, cada número de fila y cada número de columna aparece exactamente una vez;
- Cada uno de esos productos puede obtenerse a partir del producto de los elementos diagonales, $A_{11}A_{22}\cdots A_{NN}$, mediante una secuencia de intercambios de las etiquetas de columna. Por ejemplo, $A_{12}A_{21}A_{33}\cdots A_{NN}$ involucra un intercambio, mientras que $A_{12}A_{23}A_{31}A_{44}\cdots A_{NN}$ requiere dos.
- El coeficiente de un producto en el determinante es $+1$ si involucra un número par de intercambios, y $-1$ si involucra un número impar de intercambios.

Así, el determinante de una matriz $2\times2$, $A$, es

$$\det A = A_{11}A_{22} - A_{12}A_{21}\,. \qquad \text{(3.32)}$$

El determinante de una matriz $3\times3$, $A$, es

$$\det A = A_{11}A_{22}A_{33} + A_{12}A_{23}A_{31} + A_{13}A_{21}A_{32} - A_{11}A_{23}A_{32} - A_{13}A_{22}A_{31} - A_{12}A_{21}A_{33}\,. \qquad \text{(3.33)}$$

A menos que tenga muy mala suerte, nunca tendrá que calcular a mano el determinante de una matriz mayor que $3\times3$. Si tiene esa mala suerte, lo mejor es usar un procedimiento inductivo que lo construya a partir de los determinantes de submatrices menores, que discutiremos más abajo.

Si $\det A=0$, la matriz no tiene inversa: no es «invertible». En ese caso, las ecuaciones lineales simultáneas no tienen ninguna solución, o tienen infinitas. Si $\det A\neq0$, la matriz inversa existe y viene dada de forma única por

$$A^{-1} = \frac{\tilde A}{\det A} \qquad \text{(3.34)}$$

donde $\tilde A$ es la matriz de cofactores, definida por sus elementos como sigue:

$$(\tilde A)_{jk} = \det A^{(jk)} \qquad \text{(3.35)}$$

con

$$\begin{aligned}
A^{(jk)}_{\ell m} &= 1 \text{ si } m=j \text{ y } \ell=k;\\
A^{(jk)}_{\ell m} &= 0 \text{ si } m=j \text{ y } \ell\neq k;\\
A^{(jk)}_{\ell m} &= 0 \text{ si } m\neq j \text{ y } \ell=k;\\
A^{(jk)}_{\ell m} &= A_{\ell m} \text{ si } m\neq j \text{ y } \ell\neq k\,.
\end{aligned}$$

En otras palabras, $A^{(jk)}$ se obtiene de la matriz $A$ reemplazando el elemento $kj$ por 1 y todos los demás elementos de la fila $k$ o la columna $j$ por 0.

Por ejemplo, si

$$A = \begin{pmatrix} 4&3\\5&2 \end{pmatrix} \qquad \text{(3.38)}$$

entonces

$$A^{(11)} = \begin{pmatrix} 1&0\\0&2 \end{pmatrix}\,,\qquad A^{(12)} = \begin{pmatrix} 0&3\\1&0 \end{pmatrix}\,,\qquad A^{(21)} = \begin{pmatrix} 0&1\\5&0 \end{pmatrix}\,,\qquad A^{(22)} = \begin{pmatrix} 4&0\\0&1 \end{pmatrix}\,. \qquad \text{(3.39)}$$

Así,

$$\tilde A = \begin{pmatrix} 2&-3\\-5&4 \end{pmatrix} \qquad \text{(3.40)}$$

y como $\det A = 4\cdot2-5\cdot3=-7$,

$$A^{-1} = \begin{pmatrix} -2/7 & 3/7\\ 5/7 & -4/7 \end{pmatrix}\,. \qquad \text{(3.41)}$$

$A^{-1}$ satisface $AA^{-1}=A^{-1}A=I$, donde $I$ es la matriz identidad:

$$I = \begin{pmatrix} 1&0\\0&1 \end{pmatrix}\,. \qquad \text{(3.42)}$$

En términos de las submatrices $A^{(jk)}$, podemos definir el determinante inductivamente, como prometimos. De hecho, la razón por la que (3.30) funciona es que el determinante puede escribirse como

$$\det A = \sum_{k=1}^{N}A_{1k}\,\det A^{(k1)}\,. \qquad \text{(3.43)}$$

De hecho, esto es cierto para cualquier fila, no solo $j=1$. La relación (3.30) puede reescribirse como

$$\sum_{k=1}^{N}A_{jk}\,\det A^{(kj')} = \begin{cases} \det A & \text{para } j=j'\\ 0 & \text{para } j\neq j' \end{cases} \qquad \text{(3.44)}$$

Los determinantes de las submatrices, $\det A^{(k1)}$, en (3.43), pueden a su vez calcularse mediante el mismo procedimiento. El resultado es una definición del determinante que se refiere a sí misma. Sin embargo, el proceso eventualmente termina, porque las matrices se hacen cada vez más pequeñas, y el determinante siempre puede calcularse de esta manera. El único problema de este procedimiento es que es muy tedioso para una matriz grande: para una matriz $n\times n$, hay que calcular y sumar $n!$ términos. Para $n$ grande, esto es impracticable. Una de las ventajas de las técnicas que discutiremos en los próximos capítulos es que podremos evitar tales cálculos.

### 3.2.2 Más hechos útiles sobre matrices

Suponga que $A$ y $B$ son matrices $N\times N$ y $v$ es un $N$-vector.

1.  Si conoce las inversas de $A$ y $B$, puede encontrar la inversa del producto, $AB$, multiplicando las inversas en orden inverso:

$$(AB)^{-1} = B^{-1}A^{-1}\,. \qquad \text{(3.45)}$$

1.  El determinante del producto, $AB$, es el producto de los determinantes:

$$\det(AB) = \det A\,\det B\,, \qquad \text{(3.46)}$$

así que si $\det(AB)=0$, entonces $A$ o $B$ tiene determinante nulo.

1.  Una matriz multiplicada por un vector no nulo solo puede dar cero si el determinante de la matriz se anula:

$$Av=0 \implies \det A=0 \text{ o } v=0\,. \qquad \text{(3.47)}$$

Este es el enunciado, en lenguaje matricial, de que $N$ ecuaciones lineales homogéneas en $N$ incógnitas pueden tener una solución no trivial, $v\neq0$, solo si el determinante de los coeficientes se anula.

1.  De igual modo, si $\det A=0$, existe un vector no nulo, $v$, que es aniquilado por $A$:

$$\det A=0 \implies \exists\, v\neq0 \text{ tal que } Av=0\,. \qquad \text{(3.48)}$$

Este es el enunciado, en lenguaje matricial, de que $N$ ecuaciones lineales homogéneas en $N$ incógnitas sí tienen una solución no trivial, $v\neq0$, si el determinante de los coeficientes se anula.

1.  La transpuesta de una matriz $N\times M$, $A$, denotada $A^T$, es la matriz $M\times N$ obtenida reflejando la matriz respecto a una diagonal que pasa por la esquina superior izquierda. Note que si $N\neq M$, la transposición cambia la forma de la matriz. Solo para matrices cuadradas la transpuesta devuelve una matriz del mismo tipo. Una matriz cuadrada igual a su transpuesta se llama matriz «simétrica».

### 3.2.3 Ecuaciones de autovalores

Haremos un uso extenso del concepto de «ecuación de autovalores». Para una matriz $N\times N$, $R$, la ecuación de autovalores tiene la forma:

$$Rc = hc\,, \qquad \text{(3.51)}$$

donde $c$ es un $N$-vector no nulo, y $h$ es un número. La idea es encontrar tanto el número $h$, llamado el autovalor, como el vector $c$, llamado el autovector. Este es el problema que discutimos en el capítulo 1, en (1.78), en relación con la invariancia bajo traslación temporal, pero ahora escrito en forma matricial.

Un par de ejemplos pueden ser útiles. Suponga que $R$ es una matriz diagonal, como

$$R = \begin{pmatrix} 2&0\\0&1 \end{pmatrix}\,. \qquad \text{(3.52)}$$

Entonces los autovalores son justamente los elementos diagonales, 2 y 1, y los autovectores son los vectores en las direcciones coordenadas,

$$R\begin{pmatrix}1\\0\end{pmatrix} = 2\begin{pmatrix}1\\0\end{pmatrix}\,,\qquad R\begin{pmatrix}0\\1\end{pmatrix} = 1\begin{pmatrix}0\\1\end{pmatrix}\,. \qquad \text{(3.53)}$$

Un ejemplo menos obvio es

$$R = \begin{pmatrix}2&1\\1&2\end{pmatrix}\,. \qquad \text{(3.54)}$$

Esta vez los autovalores son 3 y 1, y los autovectores son los siguientes:

$$R\begin{pmatrix}1\\1\end{pmatrix} = 3\begin{pmatrix}1\\1\end{pmatrix}\,,\qquad R\begin{pmatrix}1\\-1\end{pmatrix} = 1\begin{pmatrix}1\\-1\end{pmatrix}\,. \qquad \text{(3.55)}$$

Puede parecer extraño que, en la ecuación de autovalores, tanto el autovalor como el autovector sean incógnitas. La razón de que esto funcione es que, para la mayoría de los valores de $h$, la ecuación (3.51) no tiene solución. Para verlo, escribimos (3.51) como un conjunto de ecuaciones lineales homogéneas para las componentes del autovector $c$,

$$(R-hI)c = 0\,. \qquad \text{(3.56)}$$

El conjunto de ecuaciones (3.56) tiene soluciones no nulas para $c$ solo si el determinante de la matriz de coeficientes, $R-hI$, se anula. Pero esto solo ocurrirá para $N$ valores de $h$, porque la condición

$$\det(R-hI) = 0 \qquad \text{(3.57)}$$

es una ecuación de grado $N$ en $h$. Para cada $h$ que resuelva (3.57), podemos encontrar una solución para $c$. Daremos algunos ejemplos de este procedimiento más abajo.

### 3.2.4 La ecuación matricial de movimiento

Es muy útil reescribir la ecuación de movimiento, (3.14), en notación matricial. Defina un vector columna $X$, cuya fila $j$ (desde arriba) es la coordenada $x_j$:

$$X = \begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix}\,. \qquad \text{(3.58)}$$

Defina la «matriz $K$», una matriz $n\times n$ que tiene el coeficiente $K_{jk}$ en su fila $j$, columna $k$:

$$K = \begin{pmatrix} K_{11}&K_{12}&\cdots&K_{1n}\\ K_{21}&K_{22}&\cdots&K_{2n}\\ \vdots&\vdots&\ddots&\vdots\\ K_{n1}&K_{n2}&\cdots&K_{nn} \end{pmatrix}\,. \qquad \text{(3.59)}$$

Se dice que $K_{jk}$ es el «elemento $jk$» de la matriz $K$. Debido a la ecuación (3.19), la matriz $K$ es simétrica, $K=K^T$.

Defina la matriz diagonal $M$, con $m_j$ en la fila $j$, columna $j$, y ceros en el resto:

$$M = \begin{pmatrix} m_1&0&\cdots&0\\ 0&m_2&\cdots&0\\ \vdots&\vdots&\ddots&\vdots\\ 0&0&\cdots&m_n \end{pmatrix}\,. \qquad \text{(3.60)}$$

$M$ se llama la «matriz de masas».

Usando estas definiciones, podemos reescribir (3.14) en notación matricial así:

$$M\,\frac{d^2X}{dt^2} = -KX\,. \qquad \text{(3.61)}$$

No hay nada muy sofisticado en esto. Simplemente hemos usado la notación matricial para eliminar el signo de sumatoria de (3.14). La suma ahora está implícita en la multiplicación matricial de (3.61). Esto es útil porque ahora podemos usar las propiedades de las matrices y su multiplicación, discutidas arriba, para manipular (3.61). Por ejemplo, podemos simplificar un poco (3.61) multiplicando por la izquierda por $M^{-1}$, para obtener

$$\frac{d^2X}{dt^2} = -M^{-1}K\,X\,. \qquad \text{(3.62)}$$

## 3.3 Modos normales

Si solo hay un grado de libertad, entonces tanto $X$ como $M^{-1}$ son simples números, y las soluciones de la ecuación de movimiento, (3.62), tienen la forma de una amplitud constante multiplicada por un factor exponencial. De hecho, vimos que esta forma está relacionada con un hecho muy general de la física: la invariancia bajo traslación temporal, (1.33). Los argumentos del capítulo 1, (1.71)-(1.85), no dependían del número de grados de libertad. Así, muestran que, también aquí, podemos encontrar soluciones irreducibles que se reproducen a sí mismas salvo una constante global al reajustar los relojes. Como en el capítulo 1, el primer paso es permitir que las soluciones sean complejas. Es decir, reemplazamos (3.62) por

$$\frac{d^2Z}{dt^2} = -M^{-1}K\,Z\,, \qquad \text{(3.63)}$$

donde $Z$ es un $n$-vector complejo, con componentes $z_j$. Las partes reales de las componentes de $Z$ son las componentes de una solución real que satisface (3.62),

$$x_j = \text{Re}\,z_j\,. \qquad \text{(3.64)}$$

Diremos que el vector real $X$ es la parte real del vector complejo $Z$,

$$X = \text{Re}\,Z\,, \qquad \text{(3.65)}$$

si se satisface (3.64).

Igual que en el capítulo 1, sabemos que podemos encontrar soluciones irreducibles que tienen la misma forma, salvo una constante global, al reajustar los relojes. Sabemos, por (1.85), que estas tienen la forma

$$Z(t) = A\,e^{-i\omega t} \qquad \text{(3.66)}$$

donde $A$ es cierto $n$-vector constante y la frecuencia angular, $\omega$, sigue siendo simplemente un número. Ahora, si $t\to t+a$,

$$Z(t) \to Z(t+a) = e^{-i\omega a}\,Z(t)\,. \qquad \text{(3.67)}$$

Aunque la forma irreducible, (3.66), proviene solo de la invariancia bajo traslación temporal, aún debemos examinar las ecuaciones de movimiento para determinar el vector $A$ y la frecuencia angular $\omega$. Sustituyendo (3.66) en (3.63), derivando y cancelando los factores exponenciales de ambos lados, encontramos que (3.66) es una solución si

$$\omega^2A = M^{-1}K\,A\,. \qquad \text{(3.68)}$$

Esta ecuación matricial es una ecuación de autovalores de la forma que discutimos en (3.51)-(3.57). $\omega^2$ es el autovalor de la matriz $M^{-1}K$, y $A$ es el autovector correspondiente. Veamos qué significa físicamente.

La parte real del vector columna $Z$ especifica el desplazamiento de cada uno de los grados de libertad del sistema. La ecuación de autovalores, (3.68), no involucra números complejos (porque no hemos incluido amortiguamiento). Por tanto (como veremos explícitamente más abajo), podemos elegir las soluciones de modo que todas las componentes de $A$ sean reales. Entonces la parte real de las soluciones complejas que buscamos en (3.66) es

$$X(t) = A\cos\omega t\,, \qquad \text{(3.69)}$$

o, en términos de las componentes de $A$,

$$A = \begin{pmatrix}a_1\\a_2\\\vdots\end{pmatrix}\,,\qquad x_1(t)=a_1\cos\omega t\,,\ x_2(t)=a_2\cos\omega t\,,\ \text{etc.} \qquad \text{(3.70)–(3.71)}$$

No solo todo se mueve con la misma frecuencia, sino que las razones entre los desplazamientos de los distintos grados de libertad quedan fijas. Todo oscila en fase. La única diferencia entre el movimiento de los distintos grados de libertad son sus distintas amplitudes, dadas por las distintas componentes de $A$.

Vale la pena repetir el punto: la invariancia bajo traslación temporal y la linealidad implican que siempre podemos encontrar soluciones irreducibles, (3.67), en las que todos los grados de libertad oscilan con la misma frecuencia. La información adicional que conduce a (3.69) es dinámica. Si no hay amortiguamiento, todas las componentes de $A$ pueden elegirse reales, y todos los grados de libertad oscilan no solo con la misma frecuencia, sino también con la misma fase.

Si tal solución ha de satisfacer las ecuaciones de movimiento, la aceleración también debe ser proporcional a $A$, para que los desplazamientos individuales no se desincronicen. Pero eso es justo lo que nos dice (3.68): $-M^{-1}K$ es la matriz que, actuando sobre el desplazamiento, da la aceleración. La ecuación de autovalores (3.68) significa que la aceleración vuelve a ser proporcional a $A$. La constante de proporcionalidad, $\omega^2$, es la fuerza restauradora por unidad de desplazamiento y por unidad de masa, para el desplazamiento particular especificado por $A$.

Ya hemos discutido la estructura matemática de la ecuación de autovalores en (3.51)-(3.57). Lo haremos de nuevo, para enfatizar, en el caso de interés físico, (3.68). Debería quedar claro que no todo valor de $A$ y $\omega^2$ da una solución de (3.68). Resolveremos para los valores permitidos encontrando primero los posibles valores de $\omega^2$ y luego los correspondientes valores de $A$. Para encontrar los autovalores, note que (3.68) puede reescribirse como

$$\left[M^{-1}K-\omega^2I\right]A = 0\,, \qquad \text{(3.72)}$$

donde $I$ es la matriz identidad $n\times n$. (3.72) es simplemente una forma compacta de representar $n$ ecuaciones lineales homogéneas en las $n$ componentes de $A$, cuyos coeficientes dependen de $\omega^2$. Vimos en (3.47) y (3.48) que, para sistemas de $n$ ecuaciones lineales homogéneas en $n$ incógnitas, existe una solución no nula si y solo si el determinante de la matriz de coeficientes se anula. La razón es que, si el determinante fuera no nulo, la matriz $M^{-1}K-\omega^2I$ tendría inversa, y podríamos usar (3.31) para concluir que la única solución para el vector $A$ es $A=0$. Así, para tener una amplitud $A$ no nula, debemos tener

$$\det\left[M^{-1}K-\omega^2I\right] = 0\,. \qquad \text{(3.73)}$$

(3.73) es una ecuación polinómica para $\omega^2$, de grado $n$ en $\omega^2$, porque el término del determinante proveniente del producto de todos los elementos diagonales de la matriz contiene una pieza que se comporta como $[\omega^2]^n$. Todos los coeficientes del polinomio son reales. Físicamente, esperamos que todas las soluciones para $\omega^2$ sean reales y positivas siempre que el sistema esté en equilibrio estable, porque esperamos que tales sistemas oscilen. Matemáticamente, podemos mostrar que $\omega^2$ es siempre real, mientras todas las masas sean positivas. Haremos esto más abajo, en (3.127)-(3.130).

Los $\omega^2$ negativos están asociados al equilibrio inestable. Por ejemplo, considere una masa en el extremo de una varilla rígida, libre para oscilar en el campo gravitatorio terrestre en un plano vertical alrededor de un pivote sin fricción, como se muestra en la figura 3.5. La masa puede moverse a lo largo de la línea punteada. La posición de equilibrio estable se indica con la línea continua. La posición de equilibrio inestable se indica con la línea discontinua.

![Figura 3.5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh3_ES/fig3.5.png)

Figura 3.5: masa sobre una varilla rígida, libre para oscilar en el campo gravitatorio terrestre en un plano vertical; el punto más bajo es el equilibrio estable y el punto más alto es el equilibrio inestable.

Cuando la masa está en el punto de equilibrio inestable, la más mínima perturbación hará que caiga. Una vez alejada del equilibrio, el desplazamiento crece exponencialmente hasta que el ángulo respecto a la vertical se vuelve tan grande que las no linealidades de la ecuación de movimiento de este sistema toman el control.

Una vez que hemos encontrado los posibles valores de $\omega^2$, podemos sustituir cada uno de nuevo en (3.72) para obtener el $A$ correspondiente. Como (3.72) es homogénea, la escala global de $A$ no queda determinada, pero todas las razones $a_j/a_k$ sí quedan fijas para cada $\omega^2$.

### 3.3.1 Modos normales y frecuencias

El vector $A$ se llama el «modo normal» del sistema asociado a la frecuencia $\omega$. Como $A$ es real (en ausencia de fricción), las soluciones complejas, (3.66), pueden combinarse en soluciones reales, como (3.69). La solución real general tiene la forma

$$X(t) = \text{Re}\left[(b+ic)Z(t)\right] = bA\cos\omega t + cA\sin\omega t = dA\cos(\omega t-\theta) \qquad \text{(3.74)}$$

donde $b$ y $c$ (o $d$ y $\theta$) son números reales.

Ahora podemos construir la solución completa de la ecuación de movimiento. Debido a la linealidad, la obtenemos sumando todas las soluciones de modo normal, con coeficientes arbitrarios que deben fijarse mediante las condiciones iniciales.

Ahora podemos ver que el número de modos normales distintos es siempre igual a $n$, el número de grados de libertad. Etiquete los modos normales como $A^\alpha$, donde $\alpha$ es una etiqueta que (como argumentaremos más abajo) va de 1 a $n$. Etiquete las frecuencias correspondientes como $\omega_\alpha$. Entonces el movimiento más general posible del sistema es una suma de todos los modos normales,

$$Z(t) = \sum_{\alpha=1}^{n}w_\alpha\,A^\alpha\,e^{-i\omega_\alpha t} \qquad \text{(3.75)}$$

o, en forma real (con $w=b+ic$),

$$X(t) = \sum_{\alpha=1}^{n}\left[b_\alpha A^\alpha\cos(\omega_\alpha t)+c_\alpha A^\alpha\sin(\omega_\alpha t)\right] = \sum_{\alpha=1}^{n}d_\alpha A^\alpha\cos(\omega_\alpha t-\theta_\alpha) \qquad \text{(3.76)}$$

donde $b_\alpha$ y $c_\alpha$ (o $d_\alpha$ y $\theta_\alpha$) son números reales que deben determinarse a partir de las condiciones iniciales del sistema. Note que el conjunto de todos los vectores de modo normal debe ser «completo», en el sentido matemático de que cualquier configuración posible de este sistema puede describirse como una combinación lineal de modos normales. De lo contrario, no podríamos satisfacer condiciones iniciales arbitrarias con la solución (3.76). Esto puede demostrarse matemáticamente (porque la matriz $K$ es simétrica y las masas son positivas), pero el argumento físico nos bastará aquí. Del mismo modo, ningún modo normal puede ser una combinación lineal de los demás, porque cada uno corresponde a un movimiento posible independiente del sistema físico, con su propia frecuencia. La forma matemática de decir esto es que el conjunto de todos los modos normales es «linealmente independiente».

Como el conjunto de modos normales debe ser tanto completo como linealmente independiente, debe haber exactamente $n$ modos normales, donde, de nuevo, $n$ es el número de grados de libertad. $\qquad \text{(3.77)}$

Si hubiera menos de $n$ modos normales, no podrían describir todas las configuraciones posibles de los $n$ grados de libertad. Si hubiera más de $n$, no podrían ser $n$ vectores linealmente independientes: al menos uno de ellos podría escribirse como combinación lineal de los demás. Como veremos más adelante, (3.77) es el principio físico detrás del análisis de Fourier.

Vale la pena notar que resolver la ecuación de autovalores, (3.68), se vuelve difícil muy rápidamente a medida que aumenta el número de grados de libertad. Primero hay que calcular el determinante de una matriz $n\times n$; si todos los elementos son no nulos, esto requiere sumar $n!$ términos. Una vez hecho esto, aún hay que resolver una ecuación polinómica de grado $n$. Para $n>3$, esto no puede hacerse analíticamente salvo en casos especiales.

Por otro lado, siempre es sencillo comprobar si un vector dado es un autovector de una matriz dada y, si lo es, calcular el autovalor. Usaremos este hecho en los problemas al final del capítulo.

### 3.3.2 De vuelta al ejemplo $2\times2$

Volvamos al ejemplo del principio de este capítulo, en el caso especial en que los dos bloques del péndulo tienen la misma masa, $m_1=m_2=m$. Aunque simple, este será un sistema muy importante para nuestra comprensión de los fenómenos ondulatorios. Veamos cómo las técnicas que hemos desarrollado nos permiten resolver las frecuencias permitidas y los vectores $A$ correspondientes, los modos normales. De (3.7) y (3.8), la matriz $K$ tiene la forma

$$K = \begin{pmatrix} mg/\ell+\kappa & -\kappa\\ -\kappa & mg/\ell+\kappa \end{pmatrix}\,. \qquad \text{(3.78)}$$

La matriz $M$ es

$$M = \begin{pmatrix} m&0\\0&m \end{pmatrix}\,. \qquad \text{(3.79)}$$

Así, de (3.78) y (3.79),

$$M^{-1}K = \begin{pmatrix} g/\ell+\kappa/m & -\kappa/m\\ -\kappa/m & g/\ell+\kappa/m \end{pmatrix}\,. \qquad \text{(3.80)}$$

La matriz $M^{-1}K-\omega^2I$ es

$$M^{-1}K-\omega^2I = \begin{pmatrix} g/\ell+\kappa/m-\omega^2 & -\kappa/m\\ -\kappa/m & g/\ell+\kappa/m-\omega^2 \end{pmatrix}\,. \qquad \text{(3.81)}$$

Para encontrar los autovalores de $M^{-1}K$, formamos el determinante

$$\det\left[M^{-1}K-\omega^2I\right] = (g/\ell+\kappa/m-\omega^2)^2 - (\kappa/m)^2 = (\omega^2-g/\ell)(\omega^2-g/\ell-2\kappa/m) = 0\,. \qquad \text{(3.82)}$$

Así, las frecuencias angulares de los modos normales son

$$\omega_1^2 = g/\ell\,,\qquad \omega_2^2 = g/\ell+2\kappa/m\,. \qquad \text{(3.83)}$$

Para encontrar los modos normales correspondientes, sustituimos estas frecuencias de vuelta en la ecuación de autovalores. Para $\omega_1^2$, el vector de modo normal, $A^1$,

$$A^1 = \begin{pmatrix} a_1^1\\a_2^1 \end{pmatrix}\,, \qquad \text{(3.84)}$$

satisface la ecuación matricial

$$[M^{-1}K-\omega_1^2I]A^1 = 0\,. \qquad \text{(3.85)}$$

De (3.81) y (3.83),

$$M^{-1}K-\omega_1^2I = \begin{pmatrix} \kappa/m & -\kappa/m\\ -\kappa/m & \kappa/m \end{pmatrix}\,. \qquad \text{(3.86)}$$

Así, (3.85) se convierte en

$$\begin{pmatrix} \kappa/m & -\kappa/m\\ -\kappa/m & \kappa/m \end{pmatrix}\begin{pmatrix} a_1^1\\a_2^1 \end{pmatrix}=0 \implies \frac{\kappa}{m}\begin{pmatrix} a_1^1-a_2^1\\ -a_1^1+a_2^1 \end{pmatrix}=0 \implies a_1^1=a_2^1\,. \qquad \text{(3.87)}$$

Podemos tomar $a_1^1=1$, porque podemos multiplicar el vector de modo normal por el número que queramos: solo importa la razón $a_1^1/a_2^1$. Así, por ejemplo, podemos tomar

$$A^1 = \begin{pmatrix}1\\1\end{pmatrix}\,. \qquad \text{(3.88)}$$

Esto da (3.10). El desplazamiento en este modo normal se muestra en la figura 3.6.

![Figura 3.6](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh3_ES/fig3.6.png)

Figura 3.6: los dos péndulos moviéndose en la misma dirección, con el muelle sin estirar — el modo normal $A^1$.

Para $\omega_2^2$, el vector de modo normal, $A^2$,

$$A^2 = \begin{pmatrix} a_1^2\\a_2^2 \end{pmatrix}\,, \qquad \text{(3.89)}$$

satisface la ecuación matricial (donde se sobreentiende la matriz identidad que multiplica a $\omega_2^2$)

$$[M^{-1}K-\omega_2^2]A^2 = 0\,. \qquad \text{(3.90)}$$

Esta vez, (3.81) y (3.83) dan

$$M^{-1}K-\omega_2^2 = \begin{pmatrix} -\kappa/m & -\kappa/m\\ -\kappa/m & -\kappa/m \end{pmatrix}\,. \qquad \text{(3.91)}$$

Así, (3.90) se convierte en

$$\begin{pmatrix} -\kappa/m & -\kappa/m\\ -\kappa/m & -\kappa/m \end{pmatrix}\begin{pmatrix} a_1^2\\a_2^2 \end{pmatrix}=0 \implies -\frac{\kappa}{m}\begin{pmatrix} a_1^2+a_2^2\\ a_1^2+a_2^2 \end{pmatrix}=0 \implies a_1^2=-a_2^2\,. \qquad \text{(3.92)}$$

De nuevo, solo importa la razón $a_1^2/a_2^2$, así que podemos tomar

$$A^2 = \begin{pmatrix}1\\-1\end{pmatrix}\,. \qquad \text{(3.93)}$$

Esto da (3.11). El desplazamiento en este modo normal se muestra en la figura 3.7.

![Figura 3.7](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh3_ES/fig3.7.png)

Figura 3.7: los dos péndulos moviéndose en direcciones opuestas, estirando y comprimiendo el muelle alternadamente — el modo normal $A^2$.

La física de estos modos es fácil de entender. En el modo 1, los bloques se mueven juntos y el muelle nunca se estira respecto a su posición de equilibrio. Así, la frecuencia es simplemente $g/\ell$, la misma que la de un péndulo no acoplado. En el modo 2, los bloques se mueven en direcciones opuestas, de modo que el muelle se estira el doble del desplazamiento de cada bloque. Por tanto hay una fuerza restauradora adicional de $2\kappa$, y el cuadrado de la frecuencia angular es correspondientemente mayor.

### 3.3.3 $n=2$ — el caso general

Trabajemos explícitamente el caso $n=2$ para una matriz $K$ arbitraria,

$$M^{-1}K = \begin{pmatrix} K_{11}/m_1 & K_{12}/m_1\\ K_{12}/m_2 & K_{22}/m_2 \end{pmatrix}\,, \qquad \text{(3.94)}$$

donde hemos usado $K_{21}=K_{12}$. Entonces (3.73) se convierte en

$$\left(\frac{K_{11}K_{22}-K_{12}^2}{m_1m_2}\right) - \left(\frac{K_{11}}{m_1}+\frac{K_{22}}{m_2}\right)\omega^2 + \omega^4 = 0\,, \qquad \text{(3.95)}$$

con soluciones

$$\omega^2 = \frac12\left(\frac{K_{11}}{m_1}+\frac{K_{22}}{m_2}\right) \pm \sqrt{\frac14\left(\frac{K_{11}}{m_1}-\frac{K_{22}}{m_2}\right)^2 + \frac{K_{12}^2}{m_1m_2}}\,. \qquad \text{(3.96)}$$

Para cada $\omega^2$, podemos tomar $a_1=1$. Entonces

$$a_2 = \frac{m_1\omega^2-K_{11}}{K_{12}}\,. \qquad \text{(3.97)}$$

Como anticipamos, los autovectores resultaron ser reales. Esta es una consecuencia general de la realidad de $M^{-1}K$ y $\omega^2$. Vale la pena repetir el argumento. Cuando todos los elementos de la matriz $M^{-1}K-\omega^2I$ son reales, las razones $a_j/a_k$ son reales (porque se obtienen resolviendo un sistema de ecuaciones lineales simultáneas con coeficientes reales). Así, si elegimos una componente del vector $A$ para que sea real (multiplicando, si es necesario, por un número complejo), todas las componentes serán reales. Físicamente, esto significa que, para la solución (3.66), las distintas partes del sistema oscilan no solo con la misma frecuencia, sino con la misma fase, salvo un posible signo. Esto es cierto solo porque hemos ignorado el amortiguamiento. Volveremos a esta cuestión en la última sección (una sección opcional no apta para los débiles de corazón).

### 3.3.4 El problema de valores iniciales

Una vez que ha resuelto los modos normales y las frecuencias correspondientes, es sencillo combinarlos en la solución más general de las ecuaciones de movimiento para el conjunto de $N$ osciladores acoplados, (3.76):

$$X(t) = \sum_\alpha \left(b_\alpha A^\alpha\cos\omega_\alpha t + c_\alpha A^\alpha\sin\omega_\alpha t\right)\,. \qquad \text{(3.98)}$$

Las $2N$ constantes $b_\alpha$ y $c_\alpha$ están determinadas por las condiciones iniciales. Las $b_\alpha$ están relacionadas con los desplazamientos iniciales, $X(0)$:

$$X(0) = \sum_\alpha b_\alpha A^\alpha\,. \qquad \text{(3.99)}$$

En palabras: $b_\alpha$ es el coeficiente del modo normal $A^\alpha$ en el desplazamiento inicial $X(0)$. Las $c_\alpha$ están relacionadas con las velocidades iniciales, $dX(t)/dt|_{t=0}$:

$$\left.\frac{dX(t)}{dt}\right|_{t=0} = \sum_\alpha c_\alpha\,\omega_\alpha\,A^\alpha\,. \qquad \text{(3.100)}$$

Las ecuaciones (3.99) y (3.100) son dos conjuntos de ecuaciones lineales simultáneas para las $b_\alpha$ y $c_\alpha$. Pueden resolverse a mano; esto es bastante fácil para un número pequeño de grados de libertad. Veremos en la siguiente sección que también podemos obtener las soluciones directamente, con muy poco trabajo adicional, manipulando los modos normales.

Mientras tanto, deberíamos detenernos de nuevo a considerar la física de (3.98). Esto muestra explícitamente cómo el movimiento más general del sistema puede descomponerse en los movimientos simples asociados a los modos normales. Vale la pena contemplar un ejemplo (real, animado, o preferiblemente ambos) en este punto. Intente construir el sistema de la figura 3.1; cualquier par de osciladores idénticos conectados por un muelle relativamente débil servirá. Convénzase de que existen los modos normales. Si pone el sistema a oscilar con los bloques moviéndose de la misma manera y con la misma amplitud, permanecerán así. Si los pone a moverse en direcciones opuestas con la misma amplitud, seguirán haciéndolo. Ahora provoque un movimiento aleatorio; vea si puede entender cómo descomponerlo en modos normales.

## 3.4 \* Coordenadas normales y valores iniciales

Hay otra forma de ver las soluciones de (3.14). Podemos encontrar combinaciones lineales de las coordenadas originales que oscilan con una sola frecuencia, sin importar qué más esté pasando. Esta construcción también es útil: nos permite usar la forma de los modos normales para simplificar la solución del problema de valores iniciales.

Para ver cómo funciona esto, volvamos al ejemplo simple de los dos péndulos idénticos, (3.78)-(3.93). El movimiento más general posible de este sistema se ve así:

$$X(t) = bA^1\cos(\omega_1t-\theta_1) + cA^2\cos(\omega_2t-\theta_2)\,, \qquad \text{(3.101)}$$

o, usando (3.88) y (3.93),

$$x_1(t) = b\cos(\omega_1t-\theta_1)+c\cos(\omega_2t-\theta_2)\,,\qquad x_2(t) = b\cos(\omega_1t-\theta_1)-c\cos(\omega_2t-\theta_2)\,. \qquad \text{(3.102)}$$

El movimiento de cada bloque no es armónico, pues involucra dos frecuencias distintas y cuatro constantes que deben determinarse resolviendo el problema de valores iniciales para ambos bloques.

Pero considere la combinación lineal

$$X^1(t) \equiv x_1(t)+x_2(t)\,. \qquad \text{(3.103)}$$

En esta combinación, toda dependencia de $c$ y $\theta_2$ desaparece,

$$X^1(t) = 2b\cos(\omega_1t-\theta_1)\,. \qquad \text{(3.104)}$$

Esta combinación oscila con una única frecuencia, $\omega_1$, y depende solo de dos constantes, $b$ y $\theta_1$, sin importar cuáles sean las condiciones iniciales. Del mismo modo,

$$X^2(t) \equiv x_1(t)-x_2(t) \qquad \text{(3.105)}$$

oscila con la frecuencia $\omega_2$,

$$X^2(t) = 2c\cos(\omega_2t-\theta_2)\,. \qquad \text{(3.106)}$$

$X^1$ y $X^2$ se llaman «coordenadas normales». Podemos describir el movimiento del sistema tanto en términos de $X^1$ y $X^2$ como en términos de $x_1$ y $x_2$. Podemos ir y venir entre ambas usando las definiciones (3.103) y (3.105). Aunque $x_1$ y $x_2$ son más naturales desde el punto de vista de la configuración física del sistema, figura 3.1, $X^1$ y $X^2$ son más convenientes para entender la solución. Como veremos más abajo, yendo y viniendo entre coordenadas físicas y coordenadas normales, podemos simplificar el análisis del problema de valores iniciales.

Resulta que es posible construir coordenadas normales para cualquier sistema de modos normales. Considere un modo normal $A^\alpha$ correspondiente a una frecuencia $\omega_\alpha$. Construya el vector fila

$$B^\alpha = A^{\alpha T}M \qquad \text{(3.107)}$$

donde $A^{\alpha T}$ es la transpuesta de $A^\alpha$, un vector fila con $a_j^\alpha$ en la columna $j$.

El vector fila $B^\alpha$ es también un autovector de la matriz $M^{-1}K$, pero esta vez por la izquierda. Es decir,

$$B^\alpha\,M^{-1}K = \omega_\alpha^2\,B^\alpha\,. \qquad \text{(3.108)}$$

Para deducir (3.108), note que (3.68) puede transponerse para dar

$$A^{\alpha T}KM^{-1} = \omega_\alpha^2\,A^{\alpha T} \qquad \text{(3.109)}$$

porque $M^{-1}$ y $K$ son ambas simétricas (véase (3.18), y note que el orden de $M^{-1}$ y $K$ se invierte al transponer). Entonces

$$B^\alpha M^{-1}K = A^{\alpha T}MM^{-1}K = A^{\alpha T}KM^{-1}M = \omega_\alpha^2\,A^{\alpha T}M = \omega_\alpha^2\,B^\alpha\,. \qquad \text{(3.110)–(3.111)}$$

Dado un vector fila que satisface (3.108), podemos formar la combinación lineal de coordenadas

$$X^\alpha = B^\alpha\cdot X = \sum_j b_j^\alpha\,x_j\,. \qquad \text{(3.112)}$$

Entonces $X^\alpha$ es la coordenada normal que oscila con frecuencia angular $\omega_\alpha$, porque

$$\frac{d^2X^\alpha}{dt^2} = B^\alpha\cdot\frac{d^2X}{dt^2} = -B^\alpha M^{-1}KX = -\omega_\alpha^2\,B^\alpha\cdot X = -\omega_\alpha^2\,X^\alpha\,. \qquad \text{(3.113)}$$

Así, cada coordenada normal se comporta exactamente como la coordenada de un sistema con un único grado de libertad. Los vectores $B^\alpha$ a partir de los cuales se construyen las coordenadas normales llevan la misma cantidad de información que los modos normales; de hecho, podemos ir y venir entre ambos usando (3.107).

### 3.4.1 Más sobre el problema de valores iniciales

Mostramos aquí cómo usar los modos normales y las coordenadas normales para simplificar la solución del problema de valores iniciales de sistemas de osciladores acoplados. Al mismo tiempo, podemos usar nuestra intuición física para aprender algo sobre las matemáticas del problema de autovalores. Nos gustaría encontrar las constantes $b_\alpha$ y $c_\alpha$ determinadas por (3.99) y (3.100) sin resolver realmente estas ecuaciones lineales. En efecto, hay una forma fácil: podemos aprovechar las propiedades especiales de las coordenadas normales. Considere la combinación

$$B^\beta A^\alpha\,. \qquad \text{(3.114)}$$

Esta combinación es simplemente un número, porque es un vector fila multiplicado por un vector columna a la derecha. Sabemos, por (3.112), que $X^\beta=B^\beta X$ es la coordenada normal que oscila con frecuencia $\omega_\beta$, es decir,

$$B^\beta X(t) \propto e^{\pm i\omega_\beta t}\,. \qquad \text{(3.115)}$$

Por otro lado, los únicos términos de (3.98) que oscilan con esta frecuencia son aquellos para los que $\omega_\alpha=\omega_\beta$. Así, si $\omega_\beta$ no es igual a $\omega_\alpha$, entonces $B^\beta A^\alpha$ debe anularse, para ser consistentes con (3.115).

Si el sistema tiene dos o más modos normales con distintos vectores $A$, pero la misma frecuencia, no podemos usar (3.115) para distinguirlos. En esta situación, decimos que los modos son «degenerados». Suponga que $A^1$ y $A^2$ son dos modos distintos con la misma frecuencia,

$$M^{-1}KA^1 = \omega^2A^1\,,\qquad M^{-1}KA^2 = \omega^2A^2\,. \qquad \text{(3.116)}$$

Como los autovalores son iguales, cualquier combinación lineal de los dos vectores de modo sigue siendo un modo normal con la misma frecuencia,

$$M^{-1}K\left(\beta_1A^1+\beta_2A^2\right) = \omega^2\left(\beta_1A^1+\beta_2A^2\right)\,, \qquad \text{(3.117)}$$

para cualesquiera constantes $\beta_1$ y $\beta_2$.

Ahora, si $A^{1T}MA^2\neq0$, podemos usar (3.117) para elegir un nuevo $A^2$ así:

$$A^2 \to A^2 - \frac{A^{1T}MA^2}{A^{1T}MA^1}\,A^1\,. \qquad \text{(3.118)}$$

Este nuevo modo normal satisface

$$A^{1T}MA^2 = 0\,. \qquad \text{(3.119)}$$

La construcción de (3.118) puede extenderse a cualquier número de modos normales de la misma frecuencia. Así, incluso si tenemos varios modos normales con la misma frecuencia, podemos usar la linealidad del sistema para elegir los modos normales de modo que satisfagan

$$B^\beta A^\alpha = A^{\beta T}MA^\alpha = 0 \quad\text{para } \beta\neq\alpha\,. \qquad \text{(3.120)}$$

Casi siempre supondremos que hemos hecho esto.

Podemos usar (3.120) para simplificar el problema de valores iniciales. Considere (3.99). Si multiplicamos esta ecuación vectorial por ambos lados por el vector fila $B^\beta$, obtenemos

$$B^\beta X(0) = B^\beta\sum_\alpha b_\alpha A^\alpha = \sum_\alpha b_\alpha\,B^\beta A^\alpha = b_\beta\,B^\beta A^\beta\,, \qquad \text{(3.121)}$$

donde el último paso se sigue de (3.120), que implica que la suma sobre $\alpha$ solo contribuye para $\alpha=\beta$. Así, podemos calcular $b_\alpha$ directamente a partir de los modos normales y $X(0)$,

$$b_\alpha = \frac{B^\alpha X(0)}{B^\alpha A^\alpha}\,. \qquad \text{(3.122)}$$

De forma similar,

$$\omega_\alpha c_\alpha = \frac{1}{B^\alpha A^\alpha}\,B^\alpha\left.\frac{dX(t)}{dt}\right|_{t=0}\,. \qquad \text{(3.123)}$$

El punto es que ya hemos resuelto ecuaciones lineales simultáneas como (3.99) al encontrar los autovectores de $M^{-1}K$, así que no es necesario volver a hacerlo para hallar $b_\alpha$ y $c_\alpha$. Físicamente, sabemos que la coordenada normal $X^\alpha$ debe ser proporcional al coeficiente del modo normal $A^\alpha$ en el movimiento. La expresión precisa de esto es (3.122).

### 3.4.2 \* Matrices a partir de vectores

También podemos usar (3.120) y el requisito físico de independencia lineal de los modos normales para escribir $M^{-1}K$ y la matriz identidad en términos de los modos normales.

Consideremos primero la matriz identidad. Podemos pensar en la matriz identidad como una «máquina» que toma cualquier vector y devuelve el mismo vector. Pero, usando (3.120), podemos construir tal máquina a partir de los modos normales. Considere la matriz $H$, definida como sigue:

$$H = \sum_\alpha \frac{A^\alpha B^\alpha}{B^\alpha A^\alpha}\,. \qquad \text{(3.124)}$$

Note que $H$ es una matriz porque $A^\alpha B^\alpha$ en el numerador es el producto de un vector columna por un vector fila a la derecha, en lugar de a la izquierda. Si hacemos actuar $H$ sobre uno de los vectores de modo normal, $A^\beta$, y usamos (3.120), es fácil ver que solo el término $\alpha=\beta$ de la suma contribuye, y $H\cdot A^\beta=A^\beta$. Pero como los modos normales son un conjunto completo de $N$ vectores linealmente independientes, esto implica que $H\cdot V=V$ para cualquier vector $V$. Así, $H$ es la matriz identidad,

$$H = I\,. \qquad \text{(3.125)}$$

Podemos usar esta forma de $I$ para obtener una expresión de $M^{-1}K$ como suma sobre los modos normales. Considere el producto $M^{-1}K\cdot H=M^{-1}K$, y use la condición de autovalores $M^{-1}KA^\alpha=\omega_\alpha^2A^\alpha$ para obtener

$$M^{-1}K = \sum_\alpha \frac{\omega_\alpha^2\,A^\alpha B^\alpha}{B^\alpha A^\alpha}\,. \qquad \text{(3.126)}$$

En lenguaje matemático, lo que ocurre en (3.124) y (3.126) es un cambio de la base en la que describimos las matrices que actúan sobre nuestro espacio vectorial: pasamos de la base original, formada por un conjunto obvio de desplazamientos independientes de los grados de libertad, a la base menos obvia pero más útil de los modos normales.

### 3.4.3 \* $\omega^2$ es real

Podemos usar (3.120) para mostrar que todos los autovalores de $M^{-1}K$ son reales. Este es un ejemplo particular de un importante teorema matemático general que usará con frecuencia cuando estudie mecánica cuántica. Para demostrarlo, supongamos lo contrario y deduzcamos una contradicción. Si $\omega^2$ es un autovalor complejo con autovector $A$, entonces el conjugado complejo, $\omega^{2*}$, también es un autovalor, con autovector $A^*$. Esto debe ser así porque la matriz $M^{-1}K$ es real, lo que implica que podemos tomar el conjugado complejo de la ecuación de autovalores,

$$M^{-1}KA = \omega^2A\,, \qquad \text{(3.127)}$$

para obtener

$$M^{-1}KA^* = \omega^{2*}A^*\,. \qquad \text{(3.128)}$$

Entonces, si $\omega^2$ es complejo, $\omega^2$ y $\omega^{2*}$ son distintos, y (3.120) implica

$$A^{*T}MA = 0\,. \qquad \text{(3.129)}$$

Pero (3.129) es imposible a menos que $A=0$ o al menos una de las masas de $M$ sea negativa. Para verlo, expandámosla en las componentes de $A$:

$$A^{*T}MA = \sum_{j=1}^{n}a_j^*\,m_j\,a_j = \sum_{j=1}^{n}m_j\,|a_j|^2\,. \qquad \text{(3.130)}$$

Cada uno de los términos de (3.130) es positivo o nulo. Así, las únicas soluciones de la ecuación de autovalores, (3.127), para $\omega^2$ complejo, son las triviales, en las que $A=0$ en ambos lados. Todos los modos normales tienen $\omega^2$ real.

Así, solo hay tres posibilidades. $\omega^2>0$ corresponde a equilibrio estable y oscilación armónica. $\omega^2<0$, en cuyo caso $\omega$ es puramente imaginario, ocurre cuando el equilibrio es inestable. $\omega^2=0$ es la situación en la que el equilibrio es neutro y podemos deformar el sistema sin fuerza restauradora.

## 3.5 \* Oscilaciones forzadas y resonancia

Una de las ventajas del formalismo matricial que hemos introducido es que, en lenguaje matricial, podemos trasladar casi sin cambios la discusión anterior sobre la oscilación forzada y la resonancia del capítulo 2 a sistemas con más de un grado de libertad. Simplemente tenemos que reemplazar números por los vectores y matrices apropiados. En particular, la fuerza $F(t)$ en la ecuación de movimiento, (2.2), se convierte en un vector que describe la fuerza sobre cada uno de los grados de libertad del sistema. La única restricción aquí es que la frecuencia de oscilación sea la misma para cada componente de la fuerza. El $\omega_0^2$ de la ecuación de movimiento, (2.2), se convierte en la matriz $M^{-1}K$. El término friccional $\gamma$ se convierte en una matriz. En términos de la matriz $\gamma$, el vector de fuerza friccional es $M\gamma\,dZ/dt$ (compárese con (2.1)). Entonces podemos buscar una solución estacionaria irreducible de la ecuación de movimiento, de la forma

$$Z(t) = W\,e^{-i\omega t} \qquad \text{(3.131)}$$

donde $W$ es un vector constante, lo que da la ecuación matricial

$$\left[-\omega^2-i\gamma\omega+M^{-1}K\right]W = M^{-1}F_0\,. \qquad \text{(3.132)}$$

Formalmente, podemos resolver esto multiplicando por la matriz inversa:

$$W = \left[M^{-1}K-\omega^2-i\gamma\omega\right]^{-1}M^{-1}F_0\,. \qquad \text{(3.133)}$$

Si $\gamma$ fuera cero en la matriz

$$\left[-\omega^2-i\gamma\omega+M^{-1}K\right]\,, \qquad \text{(3.134)}$$

entonces sabemos que la matriz inversa no existiría para ningún valor de $\omega$ correspondiente a una frecuencia de oscilación libre del sistema, $\omega_0$, porque el determinante de la matriz $M^{-1}K-\omega_0^2$ es cero. La amplitud $W$ tendería a $\infty$ en este límite, en la dirección del modo normal asociado a la frecuencia impulsora, siempre que la fuerza impulsora tenga una componente en la dirección del modo normal. Para $\omega$ cercano a $\omega_0$, si no hay amortiguamiento, la amplitud de la respuesta es muy grande, proporcional a $1/(\omega_0^2-\omega^2)$, casi en la dirección del modo normal. Sin embargo, en presencia de amortiguamiento, la amplitud de la respuesta no diverge, ni siquiera para $\omega=\omega_0$, porque el término $i\gamma\omega$ sigue siendo no nulo.

Podemos ver todo esto explícitamente si la matriz de amortiguamiento $\gamma$ es proporcional a la matriz identidad,

$$\gamma = \gamma I\,. \qquad \text{(3.135)}$$

Entonces podemos usar (3.124)-(3.126) para escribir $M^{-1}K-\omega^2-i\gamma\omega$ como una suma sobre los modos normales, así:

$$\left[M^{-1}K-\omega^2-i\gamma\omega\right] = \sum_\alpha\left(\omega_\alpha^2-\omega^2-i\gamma\omega\right)\frac{A^\alpha B^\alpha}{B^\alpha A^\alpha}\,. \qquad \text{(3.136)}$$

Entonces la matriz inversa puede construirse de forma similar, simplemente invirtiendo el factor del numerador:

$$\left[M^{-1}K-\omega^2-i\gamma\omega\right]^{-1} = \sum_\alpha\left(\omega_\alpha^2-\omega^2-i\gamma\omega\right)^{-1}\frac{A^\alpha B^\alpha}{B^\alpha A^\alpha}\,. \qquad \text{(3.137)}$$

Usando (3.137), podemos reescribir (3.133) como

$$W = \sum_\alpha \frac{A^\alpha}{\omega_\alpha^2-\omega^2-i\gamma\omega}\,\frac{B^\alpha M^{-1}F_0}{B^\alpha A^\alpha}\,. \qquad \text{(3.138)}$$

Esto tiene una interpretación simple. El segundo factor del lado derecho de (3.138) es el coeficiente del modo normal $A^\alpha$ en el término impulsor, $M^{-1}F_0$. Este coeficiente se multiplica por el número complejo

$$\left[\frac{1}{\omega_\alpha^2-\omega^2-i\gamma\omega}\right]\,, \qquad \text{(3.139)}$$

que es exactamente análogo al factor de (2.21) en el caso unidimensional. Así, si $\gamma\propto I$, entonces, para cada modo normal, la oscilación forzada funciona exactamente igual que para un grado de libertad. Si $\gamma$ no es proporcional a la identidad, las fórmulas son un poco más complicadas, pero la física es cualitativamente la misma.

### 3.5.1 Ejemplo

Ilustraremos estas consideraciones con nuestro ejemplo favorito, el sistema de dos osciladores acoplados idénticos, con matriz $M^{-1}K$ dada por (3.80). Imaginaremos que el sistema está sumergido en un fluido viscoso que da un amortiguamiento uniforme $\gamma=\gamma I$, y que hay una fuerza periódica que actúa el doble de fuerte sobre el bloque 1 que sobre el bloque 2 (por ejemplo, podríamos dar a los bloques cargas eléctricas $2q$ y $q$ y someterlos a un campo eléctrico periódico), de modo que la fuerza es

$$F(t) = \begin{pmatrix}2\\1\end{pmatrix}f_0\cos\omega t = \text{Re}\left[\begin{pmatrix}2\\1\end{pmatrix}f_0e^{-i\omega t}\right]\,. \qquad \text{(3.140)}$$

Así,

$$M^{-1}F_0 = \begin{pmatrix}2\\1\end{pmatrix}\frac{f_0}{m}\,. \qquad \text{(3.141)}$$

Ahora, para usar (3.133), solo necesitamos invertir la matriz

$$[M^{-1}K-\omega^2-i\gamma\omega] = \begin{pmatrix} g/\ell+\kappa/m-\omega^2-i\gamma\omega & -\kappa/m\\ -\kappa/m & g/\ell+\kappa/m-\omega^2-i\gamma\omega \end{pmatrix}\,. \qquad \text{(3.142)}$$

Esto es bastante sencillo de hacer a mano. Lo haremos primero, y luego compararemos el resultado con (3.137). El determinante es

$$\left(\frac{g}{\ell}+\frac{\kappa}{m}-\omega^2-i\gamma\omega\right)^2 - \left(\frac{\kappa}{m}\right)^2 = \left(\frac{g}{\ell}+\frac{2\kappa}{m}-\omega^2-i\gamma\omega\right)\cdot\left(\frac{g}{\ell}-\omega^2-i\gamma\omega\right)\,. \qquad \text{(3.143)}$$

Aplicando (3.34), encontramos

$$\begin{aligned}
[M^{-1}K-\omega^2-i\gamma\omega]^{-1} = {} & \frac{1}{\left(\frac{g}{\ell}+\frac{2\kappa}{m}-\omega^2-i\gamma\omega\right)\left(\frac{g}{\ell}-\omega^2-i\gamma\omega\right)}\\
& \begin{pmatrix} g/\ell+\kappa/m-\omega^2-i\gamma\omega & \kappa/m\\ \kappa/m & g/\ell+\kappa/m-\omega^2-i\gamma\omega \end{pmatrix}\,. \qquad \text{(3.144)}
\end{aligned}$$

Si aislamos la contribución de los dos ceros del denominador de (3.144), podemos escribir

$$\begin{aligned}
[M^{-1}K-\omega^2-i\gamma\omega]^{-1} = {} & \frac{1}{2\left(\frac{g}{\ell}-\omega^2-i\gamma\omega\right)}\begin{pmatrix}1&1\\1&1\end{pmatrix}\\
& + \frac{1}{2\left(\frac{g}{\ell}+\frac{2\kappa}{m}-\omega^2-i\gamma\omega\right)}\begin{pmatrix}1&-1\\-1&1\end{pmatrix} \qquad \text{(3.145)}
\end{aligned}$$

que es justamente (3.137), como prometimos. Sustituyendo ahora en (3.133), encontramos

$$W = \frac{1}{2\left(\frac{g}{\ell}-\omega^2-i\gamma\omega\right)}\begin{pmatrix}3\\3\end{pmatrix}\frac{f_0}{m} + \frac{1}{2\left(\frac{g}{\ell}+\frac{2\kappa}{m}-\omega^2-i\gamma\omega\right)}\begin{pmatrix}1\\-1\end{pmatrix}\frac{f_0}{m}$$

$$= \frac{1}{2}\,\frac{\left(\frac{g}{\ell}-\omega^2\right)+i\gamma\omega}{\left(\frac{g}{\ell}-\omega^2\right)^2+(\gamma\omega)^2}\begin{pmatrix}3\\3\end{pmatrix}\frac{f_0}{m} + \frac12\,\frac{\left(\frac{g}{\ell}+\frac{2\kappa}{m}-\omega^2\right)+i\gamma\omega}{\left(\frac{g}{\ell}+\frac{2\kappa}{m}-\omega^2\right)^2+(\gamma\omega)^2}\begin{pmatrix}1\\-1\end{pmatrix}\frac{f_0}{m}\,, \qquad \text{(3.146)}$$

de donde podemos leer el resultado final:

$$X(t) = \text{Re}\left(We^{-i\omega t}\right) = \begin{pmatrix} \alpha_1\cos\omega t+\beta_1\sin\omega t\\ \alpha_2\cos\omega t+\beta_2\sin\omega t \end{pmatrix} \qquad \text{(3.147)}$$

donde

$$\alpha_{1(2)} = \frac{3\left(\frac{g}{\ell}-\omega^2\right)}{\left(\frac{g}{\ell}-\omega^2\right)^2+(\gamma\omega)^2}\,\frac{f_0}{2m} \pm \frac{\left(\frac{g}{\ell}+\frac{2\kappa}{m}-\omega^2\right)}{\left(\frac{g}{\ell}+\frac{2\kappa}{m}-\omega^2\right)^2+(\gamma\omega)^2}\,\frac{f_0}{2m} \qquad \text{(3.148)}$$

y

$$\beta_{1(2)} = \frac{3\gamma\omega}{\left(\frac{g}{\ell}-\omega^2\right)^2+(\gamma\omega)^2}\,\frac{f_0}{2m} \pm \frac{\gamma\omega}{\left(\frac{g}{\ell}+\frac{2\kappa}{m}-\omega^2\right)^2+(\gamma\omega)^2}\,\frac{f_0}{2m} \qquad \text{(3.149)}$$

(donde el signo superior corresponde al subíndice 1 y el inferior al subíndice 2).

La potencia entregada por la fuerza externa es la suma, sobre todos los grados de libertad, de la fuerza por la velocidad. En lenguaje matricial, esto puede escribirse como

$$P(t) = F(t)^T\cdot\frac{dX(t)}{dt}\,. \qquad \text{(3.150)}$$

La potencia media perdida por la fuerza de fricción proviene del término en $\cos^2\omega t$ de (3.150), y es

$$\frac{1}{\left(\frac{g}{\ell}-\omega^2\right)^2+(\gamma\omega)^2}\,\frac{9\gamma\omega^2f_0^2}{4m} + \frac{1}{\left(\frac{g}{\ell}+\frac{2\kappa}{m}-\omega^2\right)^2+(\gamma\omega)^2}\,\frac{\gamma\omega^2f_0^2}{4m}\,. \qquad \text{(3.151)}$$

La figura 3.8 muestra una gráfica de esto (para $\kappa/m=3g/2\ell$ y $\gamma^2=g/4\ell$). Hay dos cosas que observar en la figura 3.8. Primero, note los dos picos de resonancia, en $\omega^2=g/\ell$ y $\omega^2=g/\ell+2\kappa/m=4g/\ell$. Segundo, note que el primer pico es mucho más pronunciado que el segundo. Esto se debe a que la fuerza está más alineada con la dirección del modo normal de frecuencia menor, por lo que es más eficiente excitando ese modo.

![Figura 3.8](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh3_ES/fig3.8.png)

Figura 3.8: potencia media disipada por fricción en función de $\omega$, mostrando dos picos de resonancia en $\omega=\sqrt{g/\ell}$ y $\omega=2\sqrt{g/\ell}$, el primero mucho más alto que el segundo.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Escribir las ecuaciones de movimiento de un sistema con más de un grado de libertad en forma matricial;
2.  Encontrar las matrices $M$ y $K$ a partir de la física del sistema;
3.  Sumar, restar y multiplicar matrices;
4.  Encontrar el determinante y la inversa de matrices $2\times2$ y $3\times3$;
5.  Encontrar los modos normales y las frecuencias correspondientes de un sistema con dos grados de libertad, lo que significa encontrar los autovectores y autovalores de una matriz $2\times2$;
6.  Comprobar si un vector dado es un modo normal de un sistema con más de dos grados de libertad, y, si lo es, encontrar la frecuencia angular correspondiente;
7.  Dados los modos normales y las frecuencias correspondientes, junto con las posiciones y velocidades iniciales de todas las partes de cualquier sistema, encontrar el movimiento de todas las partes en cualquier instante posterior;
8.  - Ir y venir entre modos normales y coordenadas normales;
9.  - Reconstruir la matriz $M^{-1}K$ a partir de los modos normales y las coordenadas normales;
10. - Resolver explícitamente las oscilaciones libres de un sistema con dos grados de libertad con amortiguamiento, y poder analizar sistemas con tres o más grados de libertad si se le dan los autovectores;
11. - Resolver explícitamente problemas de oscilación forzada, con o sin amortiguamiento, para sistemas con tres o menos grados de libertad.

## Problemas

**3.1.** El vector columna de 3 componentes $A$, el vector fila de 3 componentes $B$ y la matriz $3\times3$ $C$ se definen así:

$$A = \begin{pmatrix}0\\2\\1\end{pmatrix}\,,\qquad B = \begin{pmatrix}3&-2&1\end{pmatrix}\,,\qquad C = \begin{pmatrix}1&1&1\\0&-2&1\\2&2&0\end{pmatrix}\,.$$

Calcule los siguientes objetos:

$$BA\,,\qquad BC\,,\qquad AB\,.$$

**3.2.** Considere la oscilación vertical del sistema de muelles y masas mostrado a continuación, con constantes $K_A=78$, $K_B=15$ y $K_C=6$ (todas en dinas/cm).

![Figura](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh3_ES/figs1.png)

Figura: dos masas colgando verticalmente; el muelle $K_A$ une un soporte fijo con la masa de 3 g, el muelle $K_B$ une la masa de 3 g con la masa de 1 g, y el muelle $K_C$ une la masa de 1 g con otro soporte fijo.

Encuentre los modos normales, las coordenadas normales y las frecuencias angulares asociadas. Si el bloque de 1 g se desplaza 1 cm hacia arriba desde su posición de equilibrio, con el bloque de 3 g mantenido en su posición de equilibrio, y ambos bloques se sueltan desde el reposo, describa el movimiento posterior de ambos bloques.

**3.3.** Considere el sistema de muelles y masas mostrado a continuación, con constantes de muelle (en N/m) $2110$, $90$, $81$ y $1701$ (de izquierda a derecha), $m_1=100$ kg, $m_2=9$ kg y $m_3=81$ kg.

![Figura](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh3_ES/figs2.png)

Figura: tres masas en línea horizontal, conectadas por cuatro muelles: uno a la pared izquierda ($K=2110$), uno entre $m_1$ y $m_2$ ($K=90$), uno entre $m_2$ y $m_3$ ($K=81$) y uno a la pared derecha ($K=1701$).

1.  ¿Cuáles de los siguientes vectores son modos normales del sistema, y cuáles son las frecuencias angulares correspondientes? Note que la matriz $M^{-1}K$ puede parecer un poco complicada.

$$\begin{pmatrix}\psi_1\\\psi_2\\\psi_3\end{pmatrix} = \begin{pmatrix}9\\0\\10\end{pmatrix},\ \begin{pmatrix}9\\60\\10\end{pmatrix},\ \begin{pmatrix}9\\-30\\10\end{pmatrix},\ \begin{pmatrix}9\\30\\10\end{pmatrix},\ \begin{pmatrix}9\\0\\-10\end{pmatrix}$$

1.  Si el sistema se suelta desde el reposo con un desplazamiento inicial (medido en mm)

$$\begin{pmatrix}\psi_1\\\psi_2\\\psi_3\end{pmatrix} = \begin{pmatrix}9\\0\\10\end{pmatrix}\,,$$

¿cuánto tiempo tarda en volver por primera vez a su configuración inicial?

\*\*3.4 \*.\*\* Un sistema de cuatro masas conectadas por muelles se describe mediante una matriz de masas

$$M = \begin{pmatrix}1&0&0&0\\0&2&0&0\\0&0&1&0\\0&0&0&2\end{pmatrix}$$

y una matriz $K$

$$K = \begin{pmatrix}29&-10&-4&-2\\-10&58&-14&-2\\-4&-14&31&-26\\-2&-2&-26&74\end{pmatrix}$$

1.  ¿Cuáles de los siguientes vectores son modos normales?

$$\begin{pmatrix}1\\2\\1\\1\end{pmatrix},\ \begin{pmatrix}1\\1\\2\\1\end{pmatrix},\ \begin{pmatrix}2\\1\\1\\1\end{pmatrix},\ \begin{pmatrix}2\\1\\-1\\-1\end{pmatrix},\ \begin{pmatrix}4\\-3\\0\\1\end{pmatrix},\ \begin{pmatrix}0\\1\\-4\\3\end{pmatrix}$$

1.  Para cada modo normal, encuentre la frecuencia angular correspondiente. Pista: esto requiere algo de aritmética. Si es perezoso, puede usar una calculadora programable o escribir un pequeño programa de ordenador para comprobarlo. Pero el objetivo de este problema es mostrarle que la cantidad de trabajo necesaria para comprobar si los vectores son modos normales es realmente pequeña comparada con el trabajo de encontrar los modos desde cero.

2.  Si los bloques se sueltan desde el reposo con un desplazamiento inicial proporcional a

$$\begin{pmatrix}1\\1\\-1\\1\end{pmatrix}\,,$$

¿qué modo normal está ausente del movimiento posterior?

1.  Encuentre las coordenadas normales correspondientes a cada uno de los modos normales del sistema.

**3.5.** Considere las oscilaciones longitudinales del sistema mostrado a continuación: dos bloques que pueden deslizar horizontalmente sin fricción, conectados por muelles de $15$, $90$ y $10$ dinas/cm (de izquierda a derecha, el primero y el último anclados a paredes fijas). El bloque 1 tiene una masa de 15 gramos y el bloque 2 una masa de 10 gramos. Los desplazamientos de los bloques respecto al equilibrio se miden ambos hacia la derecha.

1.  Demuestre que la matriz $M^{-1}K$ de este sistema es

$$M^{-1}K = \begin{pmatrix}7&-6\\-9&10\end{pmatrix}\,.$$

1.  Demuestre que los modos normales son

$$A^1 = \begin{pmatrix}1\\1\end{pmatrix}\,,\qquad A^2 = \begin{pmatrix}2\\-3\end{pmatrix}\,.$$

Encuentre las frecuencias angulares correspondientes, $\omega_1$ y $\omega_2$.

**3.6.** Considere las oscilaciones longitudinales del sistema mostrado a continuación: dos bloques que pueden deslizar horizontalmente sin fricción, conectados por tres muelles de constantes $K_1$, $K_2$ y $K_3$ (el primero y el último anclados a paredes fijas). Los desplazamientos de los bloques respecto al equilibrio se miden ambos hacia la derecha. El bloque 1 tiene una masa de 15 gramos y el bloque 2 una masa de 10 gramos. Los modos normales de este sistema son

$$A^1 = \begin{pmatrix}1\\3\end{pmatrix}\,,\qquad A^2 = \begin{pmatrix}2\\-1\end{pmatrix}\,,$$

con frecuencias correspondientes

$$\omega_1 = 1\ \text{s}^{-1}\,,\qquad \omega_2 = 2\ \text{s}^{-1}\,.$$

1.  Si el sistema está en reposo en $t=0$, con desplazamientos $x_1(0)=5$ cm, $x_2(0)=0$, es decir,

$$X(0) = \begin{pmatrix}x_1(0)\\x_2(0)\end{pmatrix} = \begin{pmatrix}5\\0\end{pmatrix}\,\text{cm}\,,$$

encuentre el desplazamiento del bloque 2 en el instante $t=\pi$ s.

1.  Encuentre $K_1$, $K_2$ y $K_3$.

\*\*3.7 \*.\*\* En el sistema del problema (3.5), suponga que sumergimos el sistema en un fluido amortiguador de modo que

$$\gamma = \begin{pmatrix}\gamma&0\\0&\gamma\end{pmatrix}$$

con $\gamma=1\ \text{s}^{-1}$, y que se aplica una fuerza externa de la siguiente forma (en dinas):

$$F(t) = f\cos\omega t = \begin{pmatrix}1\\0\end{pmatrix}\cos\omega t\,.$$

Encuentre y grafique la potencia media perdida por la fuerza de fricción en función de $\omega$, desde $\omega=0$ hasta $10\ \text{s}^{-1}$.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.


---

<!-- MIT8.03_TextCh4_ES.md -->

# Capítulo 4: Simetrías

La simetría es un concepto importante en física y matemáticas (¡y en arte!). En este capítulo mostramos cómo las matemáticas de la simetría pueden usarse para simplificar el análisis de los modos normales de sistemas simétricos.

## Vídeos de esta clase (YouTube)

- [Clase 6: Osciladores forzados, resonancia](https://www.youtube.com/watch?v=Ahv7Akj2xs4)
- [Clase 7: Simetría, número infinito de osciladores acoplados](https://www.youtube.com/watch?v=b1eKhyC9TTo)

## Resumen previo

En este capítulo introducimos el concepto formal de simetría o invariancia.

1.  Trabajaremos algunos ejemplos del uso de argumentos de simetría para simplificar el análisis de sistemas oscilantes.

## 4.1 Simetrías

Volvamos al sistema de dos péndulos idénticos acoplados por un muelle, discutido en el capítulo 3, en (3.78)-(3.93). Este sistema simple todavía tiene más que enseñarnos. Se muestra en la figura 4.1. Como en (3.78)-(3.93), ambos bloques tienen masa $m$, ambos péndulos tienen longitud $\ell$ y la constante del muelle es $\kappa$. De nuevo denotamos los pequeños desplazamientos de los bloques hacia la derecha como $x_1$ y $x_2$.

![Figura 4.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh4_ES/fig4.1.png)

Figura 4.1: los dos péndulos acoplados, con los desplazamientos $x_1$ y $x_2$ medidos hacia la derecha.

Encontramos los modos normales de este sistema en el capítulo anterior. Pero, de hecho, podríamos haberlos encontrado aún más fácilmente aprovechando la simetría de este sistema. Si reflejamos este sistema en un plano situado a medio camino entre los dos bloques, obtenemos un sistema completamente equivalente. Decimos que el sistema es «invariante» bajo reflexiones en el plano entre los bloques. Sin embargo, aunque la física no cambia con la reflexión, nuestra descripción del sistema sí se ve afectada: las coordenadas se intercambian. El sistema reflejado se muestra en la figura 4.2. Comparando ambas figuras, podemos describir la reflexión por su efecto sobre los desplazamientos,

$$x_1 \to -x_2\,,\qquad x_2\to -x_1\,. \qquad \text{(4.1)}$$

![Figura 4.2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh4_ES/fig4.2.png)

Figura 4.2: el sistema de péndulos acoplados tras la reflexión en el plano entre ambos; las posiciones 1 y 2 quedan intercambiadas, con los desplazamientos $x_2$ y $x_1$ respectivamente, ambos con signo cambiado.

En particular, si

$$X(t) = \begin{pmatrix}x_1(t)\\x_2(t)\end{pmatrix} \qquad \text{(4.2)}$$

es una solución de las ecuaciones de movimiento del sistema, entonces el vector reflejado,

$$\tilde X(t) \equiv \begin{pmatrix}-x_2(t)\\-x_1(t)\end{pmatrix}\,, \qquad \text{(4.3)}$$

también debe ser una solución, porque el sistema reflejado es en realidad idéntico al original. Aunque esto debe ser así por la física, es útil entender cómo funciona la matemática. Para ver matemáticamente que (4.3) es una solución, definimos la matriz de simetría, $S$,

$$S \equiv \begin{pmatrix}0&-1\\-1&0\end{pmatrix}\,, \qquad \text{(4.4)}$$

de modo que $\tilde X(t)$ se relaciona con $X(t)$ mediante multiplicación matricial:

$$\tilde X(t) = \begin{pmatrix}0&-1\\-1&0\end{pmatrix}\begin{pmatrix}x_1(t)\\x_2(t)\end{pmatrix} = SX(t)\,. \qquad \text{(4.5)}$$

El enunciado matemático de la simetría es la siguiente condición sobre las matrices $M$ y $K$ (dos matrices $A$ y $B$ que satisfacen $AB=BA$ se dice que «conmutan»):

$$MS = SM\,, \qquad \text{(4.6)}$$

y

$$KS = SK\,. \qquad \text{(4.7)}$$

Puede comprobar explícitamente que (4.6) y (4.7) son ciertas. De estas ecuaciones se sigue que, si $X(t)$ es una solución de la ecuación de movimiento,

$$M\,\frac{d^2}{dt^2}X(t) = -K\,X(t)\,, \qquad \text{(4.8)}$$

entonces $\tilde X(t)$ también lo es. Para verlo explícitamente, multiplique ambos lados de (4.8) por $S$:

$$SM\,\frac{d^2}{dt^2}X(t) = -SK\,X(t)\,. \qquad \text{(4.9)}$$

Usando (4.6) y (4.7) en (4.9), obtenemos

$$MS\,\frac{d^2}{dt^2}X(t) = -KS\,X(t)\,. \qquad \text{(4.10)}$$

La matriz $S$ es constante, independiente del tiempo, así que podemos pasarla a través de las derivadas temporales en (4.10), obteniendo

$$M\,\frac{d^2}{dt^2}SX(t) = -K\,SX(t)\,. \qquad \text{(4.11)}$$

Pero ahora, usando (4.5), esta es la ecuación de movimiento para $\tilde X(t)$,

$$M\,\frac{d^2}{dt^2}\tilde X(t) = -K\,\tilde X(t)\,. \qquad \text{(4.12)}$$

Así, como prometimos, (4.6) y (4.7) son los enunciados matemáticos de la simetría de reflexión, porque implican, como acabamos de ver explícitamente, que si $X(t)$ es una solución, $\tilde X(t)$ también lo es.

Note que de (4.6) puede demostrar que

$$M^{-1}S = SM^{-1} \qquad \text{(4.13)}$$

multiplicando ambos lados por $M^{-1}$. Entonces (4.13) puede combinarse con (4.7) para dar

$$M^{-1}KS = SM^{-1}K\,. \qquad \text{(4.14)}$$

Usaremos esto más adelante.

Ahora supongamos que el sistema está en un modo normal, por ejemplo

$$X(t) = A^1\cos\omega_1t\,. \qquad \text{(4.15)}$$

Entonces $\tilde X(t)$ es otra solución. Pero tiene la misma dependencia temporal y, por tanto, la misma frecuencia angular. Por ello debe ser proporcional al mismo vector de modo normal, porque ya sabemos, de nuestro análisis anterior, que las dos frecuencias angulares de los modos normales del sistema son distintas, $\omega_1\neq\omega_2$. Cualquier cosa que oscile con frecuencia angular $\omega_1$ debe ser proporcional al modo normal $A^1$:

$$\tilde X(t) \propto A^1\cos\omega_1t\,. \qquad \text{(4.16)}$$

Así, la simetría implica

$$SA^1 \propto A^1\,. \qquad \text{(4.17)}$$

Es decir, esperamos, por la simetría, que los modos normales sean también autovectores de $S$. Esto debe ser cierto siempre que las frecuencias angulares sean distintas. De hecho, podemos comprobar, examinando las soluciones, que esto es cierto. La constante de proporcionalidad es justamente $-1$,

$$SA^1 = \begin{pmatrix}0&-1\\-1&0\end{pmatrix}A^1 = -A^1\,, \qquad \text{(4.18)}$$

y de forma similar

$$SA^2 = \begin{pmatrix}0&-1\\-1&0\end{pmatrix}A^2 = A^2\,. \qquad \text{(4.19)}$$

Además, podemos invertir el argumento. Si $A$ es un autovector de la matriz de simetría $S$, y si todos los autovalores de $S$ son distintos, entonces, gracias a la simetría (4.13), $A$ es un modo normal. Para verlo, considere el vector $M^{-1}KA$ y hágalo actuar con la matriz $S$. Usando (4.14), vemos que si

$$SA = \beta A \qquad \text{(4.20)}$$

entonces

$$S\,M^{-1}KA = M^{-1}K\,SA = \beta\,M^{-1}KA\,. \qquad \text{(4.21)}$$

En palabras, (4.21) significa que $M^{-1}KA$ es un autovector de $S$ con el mismo autovalor que $A$. Pero si los autovalores de $S$ son todos distintos, entonces $M^{-1}KA$ debe ser proporcional a $A$, lo que significa que $A$ es un modo normal. Matemáticamente, podríamos decirlo así: si los autovectores de $S$ son $A^n$ con autovalores $\beta_n$, entonces

$$SA^n = \beta_nA^n\,,\ \text{y}\ \beta_n\neq\beta_m\ \text{para}\ n\neq m \implies A^n\ \text{son modos normales.} \qquad \text{(4.22)}$$

Resulta que, para las simetrías que nos interesan, los autovalores de $S$ son siempre todos distintos.

Así, incluso si no hubiéramos conocido la solución, podríamos haber usado (4.20) para determinar los modos normales ¡sin molestarnos en resolver el problema de autovalores de la matriz $M^{-1}K$! En lugar de resolver el problema de autovalores

$$M^{-1}K\,A^n = \omega_n^2\,A^n\,, \qquad \text{(4.23)}$$

podemos en cambio resolver el problema de autovalores

$$S\,A^n = \beta_n\,A^n\,. \qquad \text{(4.24)}$$

Podría parecer que simplemente hemos cambiado un problema de autovalores por otro. Pero, de hecho, (4.24) es más fácil de resolver, porque podemos usar la simetría para determinar los autovalores, $\beta_n$, sin necesidad de calcular nunca un determinante. La simetría de reflexión tiene la agradable propiedad de que, si la aplica dos veces, vuelve a donde empezó. Esto se refleja en la propiedad de la matriz $S$,

$$S^2 = I\,. \qquad \text{(4.25)}$$

En palabras, esto significa que aplicar la matriz $S$ dos veces le devuelve exactamente el vector con el que empezó. Multiplicando ambos lados de la ecuación de autovalores, (4.24), por $S$, obtenemos

$$A^n = IA^n = S^2A^n = S\beta_nA^n = \beta_n\,SA^n = \beta_n^2A^n\,, \qquad \text{(4.26)}$$

lo que implica

$$\beta_n^2=1 \quad\text{o}\quad \beta_n=\pm1\,. \qquad \text{(4.27)}$$

Esto ahorra trabajo. Una vez conocidos los autovalores de $S$, es más fácil encontrar los autovectores de $S$. Pero, gracias a la simetría, sabemos que los autovectores de $S$ serán también los modos normales, los autovectores de $M^{-1}K$. Y una vez conocidos los modos normales, es directo encontrar la frecuencia angular haciendo actuar $M^{-1}K$ sobre los autovectores de modo normal.

Lo que hemos visto aquí, en un ejemplo simple, es cómo usar la simetría de un sistema oscilante para determinar los modos normales. En el resto de este capítulo generalizaremos esta técnica a una situación mucho más interesante. La idea siempre es la misma:

Podemos encontrar los modos normales resolviendo el problema de autovalores de la matriz de simetría, $S$, en lugar de $M^{-1}K$. Y podemos usar la simetría para determinar los autovalores. $\qquad \text{(4.28)}$

### 4.1.1 Pulsaciones

*(Referencia al programa interactivo 4-1 del disco de programas del curso original.)*

Los inicios de los fenómenos ondulatorios ya pueden verse en este simple ejemplo. Suponga que ponemos a oscilar el sistema desplazando el bloque 1 una cantidad $d$, manteniendo el bloque 2 fijo en su posición de equilibrio, y luego soltando ambos bloques desde el reposo en $t=0$. La solución general tiene la forma

$$X(t) = A^1(b_1\cos\omega_1t+c_1\sin\omega_1t) + A^2(b_2\cos\omega_2t+c_2\sin\omega_2t)\,. \qquad \text{(4.29)}$$

Las posiciones de los bloques en $t=0$ dan la ecuación matricial:

$$X(0) = \begin{pmatrix}d\\0\end{pmatrix} = A^1b_1+A^2b_2\,, \qquad \text{(4.30)}$$

o

$$\begin{aligned} d&=b_1+b_2\\ 0&=-b_1+b_2 \end{aligned} \implies b_1=b_2=\frac{d}{2}\,. \qquad \text{(4.31)}$$

Como ambos bloques se sueltan desde el reposo, sabemos que $c_1=c_2=0$. Podemos verlo de la misma forma examinando las velocidades iniciales de los bloques:

$$\dot X(0) = \begin{pmatrix}0\\0\end{pmatrix} = \omega_1A^1c_1+\omega_2A^2c_2\,, \qquad \text{(4.32)}$$

o

$$\begin{aligned} 0&=c_1+c_2\\ 0&=-c_1+c_2 \end{aligned} \implies c_1=c_2=0\,. \qquad \text{(4.33)}$$

Así,

$$x_1(t) = \frac{d}{2}(\cos\omega_1t+\cos\omega_2t)\,,\qquad x_2(t) = \frac{d}{2}(\cos\omega_1t-\cos\omega_2t)\,. \qquad \text{(4.34)}$$

Lo notable de esta solución es la forma en que la energía se transfiere por completo del bloque 1 al bloque 2 y de vuelta. Para verlo, podemos reescribir (4.34) como (usando (1.64) y otra identidad similar)

$$x_1(t) = d\cos\bar\omega t\cos\delta\omega t\,,\qquad x_2(t) = d\sin\bar\omega t\sin\delta\omega t \qquad \text{(4.35)}$$

donde

$$\bar\omega = \frac{\omega_1+\omega_2}{2}\,,\qquad \delta\omega = \frac{\omega_2-\omega_1}{2}\,. \qquad \text{(4.36)}$$

Cada uno de los bloques presenta «pulsaciones» (*beats*): oscilan con la frecuencia angular promedio, $\bar\omega$, pero la amplitud de la oscilación cambia con la frecuencia angular $\delta\omega$. Tras un tiempo $\pi/2\delta\omega$, la energía se ha transferido casi por completo del bloque 1 al bloque 2. Este comportamiento se muestra en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-4-1" rel="noopener" target="_blank" title="Animación original de Howard Georgi">4-1</a> de su disco de programas. Note cómo las pulsaciones se producen por la interacción entre los dos modos normales. Cuando los dos modos están en fase para uno de los bloques, de modo que ese bloque se mueve con amplitud máxima, los modos están desfasados $180°$ para el otro bloque, de modo que este último está casi quieto.

La transferencia completa de energía, hacia adelante y hacia atrás, del bloque 1 al bloque 2 es una característica tanto de nuestra condición inicial especial —con el bloque 2 en reposo y en su posición de equilibrio— como de la forma especial de los modos normales que se sigue de la simetría de reflexión. Como veremos con más detalle más adelante, este es el mismo tipo de transferencia de energía que ocurre en los fenómenos ondulatorios.

### 4.1.2 Un ejemplo menos trivial

*(Referencia al programa interactivo 4-2 del disco de programas del curso original.)*

Tome una hoja de sierra para metales, fije un extremo y sujete una masa al otro. Esto forma un buen oscilador con esencialmente un solo grado de libertad (porque la hoja de sierra solo se dobla fácilmente hacia adelante y hacia atrás de una manera). Ahora tome seis hojas idénticas y fije un extremo de cada una en un mismo punto, de modo que las hojas se abran en abanico formando ángulos de $60°$ entre sí desde el centro, orientadas de forma que puedan doblarse hacia adelante y hacia atrás en el plano formado por las hojas. Si coloca una masa en el extremo de cada una, en un patrón hexagonal, tendrá seis osciladores desacoplados. Pero si en su lugar coloca imanes idénticos en los extremos, los osciladores quedarán acoplados entre sí de una forma complicada. Puede ver cómo son las oscilaciones de este sistema en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-4-2" rel="noopener" target="_blank" title="Animación original de Howard Georgi">4-2</a> del disco de programas.

![Figura 4.3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh4_ES/fig4.3.png)

Figura 4.3: sistema de seis osciladores de hoja de sierra acoplados, dispuestos en abanico hexagonal alrededor de un centro común; las flechas indican las direcciones en que se miden los desplazamientos $x_1$ a $x_6$, en sentido antihorario alrededor del hexágono.

Si los desplazamientos respecto a las posiciones de equilibrio simétricas son pequeños, el sistema es aproximadamente lineal. A pesar de la aparente complejidad de este sistema, ¡podemos escribir los modos normales y las frecuencias angulares correspondientes con casi ningún esfuerzo! El truco consiste en aprovechar inteligentemente la simetría de este sistema.

Este sistema se ve exactamente igual si lo rotamos $60°$ alrededor de su centro. Por tanto, deberíamos esforzarnos en analizarlo de una manera manifiestamente simétrica. Etiquetemos las masas de 1 a 6, empezando en cualquier lugar y recorriendo el sistema en sentido antihorario. Sea $x_j$ el desplazamiento en sentido antihorario del $j$-ésimo bloque respecto a su posición de equilibrio. Como de costumbre, dispondremos estas coordenadas en un vector (a partir de aquí, supondremos que el lector está suficientemente acostumbrado a los números complejos como para que no sea necesario distinguir entre una coordenada real y una compleja):

$$X = \begin{pmatrix}x_1\\x_2\\x_3\\x_4\\x_5\\x_6\end{pmatrix}\,. \qquad \text{(4.37)}$$

La operación de simetría de rotación se implementa mediante la sustitución cíclica

$$x_1 \to x_2 \to x_3 \to x_4 \to x_5 \to x_6 \to x_1\,. \qquad \text{(4.38)}$$

Esto puede representarse en notación matricial como

$$X \to SX\,, \qquad \text{(4.39)}$$

donde la matriz de simetría, $S$, es

$$S = \begin{pmatrix} 0&1&0&0&0&0\\ 0&0&1&0&0&0\\ 0&0&0&1&0&0\\ 0&0&0&0&1&0\\ 0&0&0&0&0&1\\ 1&0&0&0&0&0 \end{pmatrix}\,. \qquad \text{(4.40)}$$

Note que los unos en la subdiagonal de la matriz $S$, en (4.40), implementan las sustituciones

$$x_1\to x_2\to x_3\to x_4\to x_5\to x_6\,, \qquad \text{(4.41)}$$

mientras que el 1 de la esquina inferior izquierda cierra el círculo con la sustitución

$$x_6\to x_1\,. \qquad \text{(4.42)}$$

La simetría exige que la matriz $K$ de este sistema tenga la siguiente forma:

$$K = \begin{pmatrix} E&-B&-C&-D&-C&-B\\ -B&E&-B&-C&-D&-C\\ -C&-B&E&-B&-C&-D\\ -D&-C&-B&E&-B&-C\\ -C&-D&-C&-B&E&-B\\ -B&-C&-D&-C&-B&E \end{pmatrix}\,. \qquad \text{(4.43)}$$

Note que todos los elementos diagonales son iguales ($E$), como debe ser por la simetría. El $j$-ésimo elemento diagonal de la matriz $K$ es menos la fuerza por unidad de desplazamiento sobre la $j$-ésima masa debida a su propio desplazamiento. Debido a la simetría, cada una de las masas se comporta exactamente igual cuando se desplaza manteniendo fijas todas las demás. Así, todos los elementos diagonales de la matriz $K$, $K_{jj}$, son iguales. Del mismo modo, la simetría garantiza que el efecto del desplazamiento de cada bloque $j$ sobre su vecino $j\pm1$ (con $j+1\to1$ si $j=6$, y $j-1\to6$ si $j=1$ —véase (4.42)) es exactamente el mismo. Así, los elementos de matriz en la subdiagonal ($B$) son todos iguales, junto con las $B$ de las esquinas. Y así sucesivamente. La matriz $K$ satisface entonces (4.7),

$$SK = KS \qquad \text{(4.44)}$$

que, como vimos en (4.13)-(4.12), es el enunciado matemático de la simetría. De hecho, podemos ir hacia atrás y deducir la matriz simétrica más general consistente con (4.44), y comprobar que debe tener la forma (4.43). Esto lo hará en el problema 4.4.

Debido a la simetría, sabemos que si un vector $A$ es un modo normal, entonces el vector $SA$ también es un modo normal con la misma frecuencia. Esto es físicamente obvio: si el sistema oscila con todas sus partes moviéndose al mismo ritmo de cierta manera, también puede oscilar con las partes rotadas $60°$, pero moviéndose por lo demás de la misma forma, y la frecuencia será la misma. Esto sugiere que busquemos modos normales que se comporten de forma simple bajo la transformación de simetría $S$. En particular, si encontramos los autovectores de $S$ y descubrimos que los autovalores de $S$ son todos distintos, entonces sabemos, por (4.22), que todos los autovectores son modos normales. En el ejemplo anterior, encontramos modos que se reproducían a sí mismos multiplicados por $\pm1$ bajo la simetría. En general, sin embargo, no debemos esperar que los autovalores sean reales, porque los modos pueden involucrar exponenciales complejas. En este caso, debemos buscar modos correspondientes a autovalores complejos de $S$ (aunque incluso esto no es la posibilidad más general —en general, podríamos tener que considerar conjuntos de modos que se transforman unos en otros bajo la multiplicación matricial; esto no es necesario aquí porque las transformaciones de simetría conmutan todas entre sí),

$$SA = \beta A\,. \qquad \text{(4.45)}$$

Como arriba, en (4.25)-(4.27), podemos encontrar los posibles autovalores usando la simetría. Note que, como seis rotaciones de $60°$ nos devuelven al punto de partida, la matriz $S$ satisface

$$S^6 = I\,. \qquad \text{(4.46)}$$

De (4.46) se sigue que $\beta^6=1$. Así, $\beta$ es una raíz sexta de la unidad,

$$\beta=\beta_k=e^{2ik\pi/6} \quad\text{para } k=0\text{ a }5\,. \qquad \text{(4.47)}$$

Entonces, para cada $k$, hay un modo normal

$$S\,A^k = \beta_k\,A^k\,. \qquad \text{(4.48)}$$

Explícitamente,

$$SA^k = \begin{pmatrix}A_2^k\\A_3^k\\A_4^k\\A_5^k\\A_6^k\\A_1^k\end{pmatrix} = \beta_k\cdot\begin{pmatrix}A_1^k\\A_2^k\\A_3^k\\A_4^k\\A_5^k\\A_6^k\end{pmatrix}\,. \qquad \text{(4.49)}$$

Si tomamos $A_1^k=1$, podemos resolver todas las demás componentes,

$$A_j^k = (\beta_k)^{j-1}\,. \qquad \text{(4.50)}$$

Así,

$$\begin{pmatrix}A_1^k\\A_2^k\\A_3^k\\A_4^k\\A_5^k\\A_6^k\end{pmatrix} = \begin{pmatrix}1\\e^{2ik\pi/6}\\e^{4ik\pi/6}\\e^{6ik\pi/6}\\e^{8ik\pi/6}\\e^{10ik\pi/6}\end{pmatrix}\,. \qquad \text{(4.51)}$$

Ahora, para determinar las frecuencias angulares correspondientes a los modos normales, debemos evaluar

$$M^{-1}K\,A^k = \omega_k^2\,A^k\,. \qquad \text{(4.52)}$$

Como ya conocemos la forma de los modos normales, esto es directo. Por ejemplo, podemos comparar las primeras componentes de estos dos vectores:

$$\begin{aligned}
\omega_k^2 &= \left(E-Be^{2ik\pi/6}-Ce^{4ik\pi/6}-De^{6ik\pi/6}-Ce^{8ik\pi/6}-Be^{10ik\pi/6}\right)/m\\
&= \frac{E}{m}-\frac{2B}{m}\cos\frac{k\pi}{3}-\frac{2C}{m}\cos\frac{2k\pi}{3}-(-1)^k\frac{D}{m}\,. \qquad \text{(4.53)}
\end{aligned}$$

Note que $\omega_1^2=\omega_5^2$ y $\omega_2^2=\omega_4^2$. Esto tenía que ser así, porque los modos normales correspondientes son pares complejos conjugados,

$$A^5 = A^{1*}\,,\qquad A^4=A^{2*}\,. \qquad \text{(4.54)}$$

Cualquier modo normal complejo debe formar parte de un par junto con su modo normal complejo conjugado, a la misma frecuencia, de modo que podamos construir modos normales reales a partir de ellos. Esto debe ser así porque los modos normales describen un sistema físico real, cuyos desplazamientos son reales. Los modos reales son combinaciones lineales (véase (1.19)) de los modos complejos,

$$A^k+A^{k*} \quad\text{y}\quad (A^k-A^{k*})/i \quad\text{para } k=1\text{ o }2\,. \qquad \text{(4.55)}$$

Estos modos pueden verse en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-4-2" rel="noopener" target="_blank" title="Animación original de Howard Georgi">4-2</a> del disco de programas.

Note que las soluciones reales, (4.55), no son autovectores de la matriz de simetría $S$. Esto es posible porque las frecuencias angulares no son todas distintas. Sin embargo, los autovalores de $S$ sí son todos distintos, de (4.47). Así, aunque podamos construir modos normales que no sean autovectores de $S$, sigue siendo cierto que todos los autovectores de $S$ son modos normales. Esto es lo que usamos en (4.48)-(4.50) para determinar los $A^n$.

Observamos que (4.55) es otro ejemplo de un principio muy importante, (3.117), que usaremos muchas veces en lo que sigue:

Si $A$ y $A'$ son modos normales de un sistema con la misma frecuencia angular, $\omega$, entonces cualquier combinación lineal, $bA+cA'$, también es un modo normal con la misma frecuencia angular. $\qquad \text{(4.56)}$

Los modos normales con la misma frecuencia pueden combinarse linealmente para dar nuevos modos normales (véase el problema 4.3). Por otro lado, una combinación lineal de dos modos normales con frecuencias distintas no da nada muy simple.

Las técnicas usadas aquí podrían haberse usado para cualquier número de masas en una disposición simétrica similar. Con $N$ masas y simetría bajo rotación de $2\pi/N$ radianes, las $N$-ésimas raíces de la unidad reemplazarían a las raíces sextas de la unidad de nuestro ejemplo. Los argumentos de simetría también pueden usarse para determinar los modos normales en situaciones más interesantes, por ejemplo cuando las masas están en los vértices de un cubo. Pero ese caso es más complicado que el que hemos analizado, porque el orden de las transformaciones de simetría importa —las transformaciones no conmutan entre sí—. Puede que quiera volver a este tema después de haber estudiado algo de teoría de grupos.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Aplicar argumentos de simetría para encontrar los modos normales de sistemas de osciladores acoplados, hallando los autovalores y autovectores de la matriz de simetría.

## Problemas

**4.1.** Demuestre explícitamente que (4.7) se cumple para la matriz $K$, (4.43), del sistema de la figura 4.3, calculando $SK$ y $KS$.

**4.2.** Considere un sistema de seis masas idénticas que pueden deslizar sin fricción sobre un anillo circular de radio $R$, cada una conectada a sus dos vecinas más cercanas mediante muelles idénticos, mostrado en equilibrio en la figura.

![Figura](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh4_ES/figs1.png)

Figura: seis masas idénticas dispuestas simétricamente sobre un anillo circular, conectadas entre sí por muelles idénticos a lo largo del anillo, con los desplazamientos $y_j$ medidos tangencialmente al anillo.

1.  Analice los posibles movimientos de este sistema en la región en la que es lineal (note que esto no es exactamente lo mismo que pequeñas oscilaciones). Para ello, defina variables de desplazamiento adecuadas (de modo que pueda usar un argumento de simetría), encuentre la forma de la matriz $K$ y luego siga el análisis de (4.37)-(4.55). Si lo ha hecho correctamente, debería encontrar que uno de los modos tiene frecuencia cero. Explique el significado físico de este modo. Pista: no intente encontrar la forma de la matriz $K$ directamente a partir de las constantes de los muelles y la geometría —esto es un lío—; en su lugar, deduzca cómo debe ser a partir de argumentos de simetría.

2.  Si en $t=0$ las masas están distribuidas uniformemente alrededor del círculo, pero cada dos masas se mueve con velocidad $v$ (en sentido antihorario) mientras las demás están en reposo, encuentre y describa en palabras el movimiento posterior del sistema.

**4.3.**

1.  Demuestre (4.56).

2.  Demuestre que si $A$ y $A'$ son modos normales correspondientes a frecuencias angulares distintas, $\omega$ y $\omega'$ respectivamente, con $\omega^2\neq\omega'^2$, entonces $bA+cA'$ no es un modo normal a menos que $b$ o $c$ sean cero. Pista: necesitará usar el hecho de que tanto $A$ como $A'$ son vectores no nulos.

**4.4.** Demuestre que (4.43) es la matriz simétrica $6\times6$ más general que satisface (4.44).

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.


---

<!-- MIT8.03_TextCh5_ES.md -->

# Capítulo 5: Ondas

El clímax de este libro llega pronto. Aquí identificamos las características cruciales de un sistema que admite ondas: la invariancia bajo traslación espacial y las interacciones locales.

## Vídeos de esta clase (YouTube)

- [Clase 6: Osciladores forzados, resonancia](https://www.youtube.com/watch?v=Ahv7Akj2xs4)
- [Clase 7: Simetría, número infinito de osciladores acoplados](https://www.youtube.com/watch?v=b1eKhyC9TTo)
- [Clase 8: Simetría de traslación](https://www.youtube.com/watch?v=J1uHGy1tRmM)
- [Clase 9: Ecuación de ondas, ondas estacionarias, series de Fourier](https://www.youtube.com/watch?v=1JeBWHzrRD4)

## Resumen previo

Identificamos la invariancia bajo traslación espacial de la clase de sistemas infinitos en los que ocurren los fenómenos ondulatorios.

1.  Los argumentos de simetría no pueden aplicarse directamente a sistemas finitos que admiten ondas, como una serie de péndulos acoplados. Sin embargo, mostramos que, si los acoplamientos son solo entre bloques vecinos, el concepto de simetría todavía puede usarse para entender las oscilaciones. En este caso decimos que las interacciones son «locales». La idea es separar la física en dos componentes distintos: la física del interior y la física de las fronteras, que se incorpora en forma de condiciones de contorno. El interior puede considerarse parte de un sistema infinito con invariancia bajo traslación espacial, una simetría bajo traslaciones en cierta distancia $a$. En este caso, los modos normales se llaman ondas estacionarias.
2.  Después introducimos una notación diseñada para aprovechar al máximo la invariancia bajo traslación espacial del sistema infinito. Introducimos el número de onda angular, $k$, que desempeña para la dependencia espacial de la onda el mismo papel que la frecuencia angular, $\omega$, desempeña para su dependencia temporal.
3.  Describimos los modos normales de oscilación transversal de una cuerda con cuentas. Los modos son «ondulados».
4.  Estudiamos los modos normales de una cuerda con cuentas finita con extremos libres, como otro ejemplo de condiciones de contorno.
5.  Estudiamos un tipo de problema de oscilación forzada particularmente importante para sistemas invariantes bajo traslación con interacciones locales. Si la fuerza impulsora actúa solo en los extremos del sistema, la solución puede encontrarse simplemente usando condiciones de contorno.
6.  Aplicamos la idea de invariancia bajo traslación espacial a un sistema de circuitos LC acoplados.

## 5.1 Invariancia bajo traslación espacial

![Figura 5.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.1.png)

Figura 5.1: sistema finito de $N$ péndulos acoplados idénticos, en línea, cada uno conectado a sus vecinos mediante un muelle, con los dos extremos anclados a paredes fijas.

El sistema típico de osciladores acoplados que admite ondas es como el sistema de $N$ péndulos acoplados idénticos mostrado en la figura 5.1. Este sistema es una generalización del sistema de dos péndulos acoplados que estudiamos en los capítulos 3 y 4. Suponga que cada masa de péndulo tiene masa $m$, cada péndulo tiene longitud $\ell$, cada muelle tiene constante $\kappa$ y la separación de equilibrio entre masas es $a$. Suponga además que no hay fricción y que los péndulos están obligados a oscilar solo en la dirección en la que se estiran los muelles. Nos interesa la oscilación libre de este sistema, sin fuerza externa. Tal oscilación, cuando el movimiento es paralelo a la dirección en la que el sistema se extiende en el espacio, se llama «oscilación longitudinal». Llame $\psi_j$ al desplazamiento longitudinal de la $j$-ésima masa respecto al equilibrio. Podemos organizar los desplazamientos en un vector $\Psi$ (por razones que quedarán claras más abajo, sería confuso usar $X$, así que elegimos otra letra, la griega psi, que se escribe $\psi$ en minúscula y $\Psi$ en mayúscula):

$$\Psi = \begin{pmatrix}\psi_1\\\psi_2\\\psi_3\\\vdots\\\psi_N\end{pmatrix}\,. \qquad \text{(5.1)}$$

Entonces las ecuaciones de movimiento (para pequeñas oscilaciones longitudinales) son

$$\frac{d^2\Psi}{dt^2} = -M^{-1}K\,\Psi \qquad \text{(5.2)}$$

donde $M$ es la matriz diagonal con $m$ en la diagonal,

$$M = \begin{pmatrix} m&0&0&\cdots&0\\ 0&m&0&\cdots&0\\ 0&0&m&\cdots&0\\ \vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&m \end{pmatrix}\,, \qquad \text{(5.3)}$$

y $K$ tiene elementos diagonales $(mg/\ell+2\kappa)$, elementos en la subdiagonal $-\kappa$, y ceros en el resto,

$$K = \begin{pmatrix} mg/\ell+2\kappa & -\kappa & 0 & \cdots & 0\\ -\kappa & mg/\ell+2\kappa & -\kappa & \cdots & 0\\ 0 & -\kappa & mg/\ell+2\kappa & \cdots & 0\\ \vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&mg/\ell+2\kappa \end{pmatrix}\,. \qquad \text{(5.4)}$$

El $-\kappa$ de la subdiagonal tiene exactamente el mismo origen que el $-\kappa$ de la matriz $K$ $2\times2$ de (3.78): describe el acoplamiento de dos bloques vecinos por el muelle. El $(mg/\ell+2\kappa)$ de la diagonal es análogo al $(mg/\ell+\kappa)$ de la diagonal de (3.78). La diferencia en el factor 2 del coeficiente de $\kappa$ surge porque hay dos muelles, uno a cada lado, que contribuyen a la fuerza restauradora sobre cada bloque en el sistema de la figura 5.1, mientras que solo había uno en el sistema de la figura 3.1. Así, $M^{-1}K$ tiene la forma

$$M^{-1}K = \begin{pmatrix} 2B&-C&0&\cdots&0\\ -C&2B&-C&\cdots&0\\ 0&-C&2B&\cdots&0\\ \vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&2B \end{pmatrix} \qquad \text{(5.5)}$$

donde

$$2B = g/\ell+2\kappa/m\,,\qquad C=\kappa/m\,. \qquad \text{(5.6)}$$

Es interesante comparar la matriz (5.5) con la matriz (4.43) del capítulo anterior. En ambos casos, los elementos diagonales son todos iguales, por la simetría; lo mismo ocurre con los elementos de la subdiagonal. Sin embargo, en (5.5), todos los demás elementos son cero, porque las interacciones son solo entre bloques vecinos más cercanos. Llamamos «locales» a tales interacciones. En (4.43), en cambio, cada masa interactúa con todas las demás. Usaremos la naturaleza local de las interacciones más abajo.

Podríamos intentar encontrar los modos normales de este sistema directamente, hallando los autovectores de $M^{-1}K$, pero hay una técnica mucho más fácil y de utilidad más general. Podemos dividir la física del sistema en dos partes: la física de los péndulos acoplados, y la física de las paredes. Para ello, primero consideramos un sistema infinito sin paredes en absoluto.

### 5.1.1 El sistema infinito

![Figura 5.2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.2.png)

Figura 5.2: fragmento de un sistema infinito de péndulos acoplados, extendiéndose indefinidamente a ambos lados del bloque 1 al N, con los mismos muelles de acoplamiento.

Note que en la figura 5.2 no hemos cambiado en absoluto el interior del sistema de la figura 5.1: simplemente hemos reemplazado las paredes por una continuación del interior.

Ahora podemos encontrar todos los modos del sistema infinito de la figura 5.2 muy fácilmente, aprovechando un argumento de simetría. El sistema infinito de la figura 5.2 se ve igual si se traslada, moviéndolo a la izquierda o a la derecha en un múltiplo de la separación de equilibrio, $a$. Tiene la propiedad de «invariancia bajo traslación espacial». La invariancia bajo traslación espacial es la simetría del sistema infinito bajo traslaciones en múltiplos de $a$. En este ejemplo, debido a los bloques discretos y a la longitud finita de los muelles, la invariancia bajo traslación espacial es «discreta»: solo las traslaciones por múltiplos enteros de $a$ dan la misma física. Más adelante discutiremos sistemas continuos que tienen invariancia bajo traslación espacial continua; sin embargo, veremos que tales sistemas pueden analizarse con las mismas técnicas que introducimos en este capítulo.

Podemos usar la simetría de la invariancia bajo traslación espacial, igual que usamos las simetrías de reflexión y rotación discutidas en el capítulo anterior, para encontrar los modos normales del sistema infinito. La invariancia discreta bajo traslación espacial del sistema infinito (la simetría bajo traslaciones en múltiplos de $a$) nos permite encontrar los modos normales del sistema infinito de forma simple.

La mayoría de los modos que encontremos usando la invariancia bajo traslación espacial del sistema infinito de la figura 5.2 no tendrán nada que ver con el sistema finito de la figura 5.1. Pero si podemos encontrar combinaciones lineales de los modos normales del sistema infinito de la figura 5.2 en las que los bloques $0$ y $N+1$ permanezcan fijos, entonces deben ser soluciones de las ecuaciones de movimiento del sistema de la figura 5.1. La razón es que las interacciones entre los bloques son «locales» —ocurren solo entre bloques vecinos más cercanos—. Así, el bloque 1 «sabe» qué hace el bloque 0, pero no qué hace el bloque $-1$. Si el bloque 0 está inmóvil, bien podría ser una pared, porque los bloques del otro lado no afectan en absoluto al bloque 1 (ni a ninguno de los bloques 1 a $N$). La naturaleza local de la interacción nos permite incorporar la física de las paredes como una condición de contorno, después de resolver el problema infinito. Este mismo truco también nos permitirá resolver muchos otros problemas.

Veamos cómo funciona esto para el sistema de la figura 5.1. Primero, usamos la simetría bajo traslaciones para encontrar los modos normales del sistema infinito de la figura 5.2. Como en los dos capítulos anteriores, describimos las soluciones en términos de un vector, $A$. Pero ahora $A$ tiene un número infinito de componentes, $A_j$, donde el entero $j$ va de $-\infty$ a $+\infty$. Es un poco incómodo escribir este vector infinito, pero podemos representar un fragmento de él:

$$A = \begin{pmatrix}\vdots\\A_0\\A_1\\A_2\\A_3\\\vdots\\A_N\\A_{N+1}\\\vdots\end{pmatrix}\,. \qquad \text{(5.7)}$$

Del mismo modo, la matriz $M^{-1}K$ del sistema es una matriz infinita, no fácil de escribir en su totalidad, pero cualquier fragmento de ella (a lo largo de la diagonal) se ve como el interior de (5.5):

$$\begin{pmatrix}\ddots&\ddots&\ddots&\ddots&\ddots&\ddots\\ \cdots&2B&-C&0&0&\cdots\\ \cdots&-C&2B&-C&0&\cdots\\ \cdots&0&-C&2B&-C&\cdots\\ \cdots&0&0&-C&2B&\cdots\\ \ddots&\ddots&\ddots&\ddots&\ddots&\ddots \end{pmatrix}\,. \qquad \text{(5.8)}$$

Este sistema es «invariante bajo traslación espacial» porque se ve igual si se desplaza una distancia $a$ hacia la izquierda. Esto mueve el bloque $j+1$ a donde estaba el bloque $j$, así que, si hay un modo con componentes $A_j$, debe haber otro modo con la misma frecuencia, representado por un vector $A'=SA$, con componentes

$$A'_j = A_{j+1}\,. \qquad \text{(5.9)}$$

La matriz de simetría, $S$, es una matriz infinita con unos en la subdiagonal. Estos son análogos a los unos de la subdiagonal en (4.40). Sin embargo, ahora la transformación nunca se cierra sobre sí misma: no hay análogo del 1 de la esquina inferior izquierda de (4.40), porque la matriz infinita no tiene esquina. Queremos encontrar los autovalores y autovectores de la matriz $S$, que satisfacen

$$A' = SA = \beta A \qquad \text{(5.10)}$$

o, equivalentemente (de (5.9)), los modos en los que $A_j$ y $A'_j$ son proporcionales:

$$A'_j = \beta A_j = A_{j+1} \qquad \text{(5.11)}$$

donde $\beta$ es alguna constante no nula (el cero no sirve para $\beta$, porque la ecuación de autovalores no tendría solución).

La ecuación (5.11) puede resolverse así: elija $A_0=1$. Entonces $A_1=\beta$, $A_2=\beta^2$, etc., de modo que $A_j=(\beta)^j$ para todo $j$ no negativo. También podemos reescribir (5.11) como $A_{j-1}=\beta^{-1}A_j$, de modo que $A_{-1}=\beta^{-1}$, $A_{-2}=\beta^{-2}$, etc. Así, la solución es

$$A_j = (\beta)^j \qquad \text{(5.12)}$$

para todo $j$. Note que esta solución funciona para cualquier valor no nulo de $\beta$, a diferencia de los ejemplos que discutimos en el capítulo anterior. La razón es que una traslación en $a$, a diferencia de las simetrías de reflexión y rotación de $60°$ discutidas en el capítulo 4, nunca lo devuelve a donde empezó, sin importar cuántas veces la repita. Además, el sistema infinito, con un número infinito de grados de libertad, tiene un número infinito de modos normales distintos, correspondientes a distintos valores de $\beta$.

Para cada valor de $\beta$, hay un autovector único (salvo multiplicación por una constante global), $A$. Sabemos que es único porque lo hemos construido explícitamente en (5.12). Por tanto, todos los autovalores de $S$ son distintos. Así, de (4.22), sabemos que cada uno de los autovectores es un modo normal del sistema infinito. Como hay una correspondencia biunívoca entre números no nulos, $\beta$, y modos normales, podemos (al menos por ahora —encontraremos una notación mejor más adelante) etiquetar los modos normales por el autovalor, $\beta$, de la matriz de simetría $S$. Llamaremos al autovector correspondiente $A^\beta$, de modo que (5.12) puede escribirse

$$A_j^\beta = \beta^j\,. \qquad \text{(5.13)}$$

Ahora que conocemos la forma de los modos normales, es fácil obtener las frecuencias correspondientes haciendo actuar la matriz $M^{-1}K$, (5.8), sobre (5.12). Esto da

$$\omega^2A_j^\beta = 2BA_j^\beta - CA_{j+1}^\beta - CA_{j-1}^\beta\,, \qquad \text{(5.14)}$$

o, sustituyendo (5.13),

$$\omega^2\beta^j = 2B\beta^j - C\beta^{j+1} - C\beta^{j-1} = (2B-C\beta-C\beta^{-1})\beta^j\,. \qquad \text{(5.15)}$$

Esto es cierto para todo $j$, lo que muestra que (5.13) es en efecto un autovector (ya lo sabíamos por el argumento de simetría, (4.22), pero está bien comprobarlo cuando es posible), y el autovalor es

$$\omega^2 = 2B - C\beta - C\beta^{-1}\,. \qquad \text{(5.16)}$$

Note que, para casi cualquier valor de $\omega^2$, hay dos modos normales, porque podemos intercambiar $\beta$ y $\beta^{-1}$ sin cambiar (5.16). Las únicas excepciones son

$$\omega^2 = 2B \pm 2C\,, \qquad \text{(5.17)}$$

correspondientes a $\beta=\pm1$. El hecho de que haya como máximo dos modos normales para cada valor de $\omega^2$ tendrá una consecuencia dramática: significa que solo tenemos que tratar con dos modos normales a la vez para implementar la física de la frontera. Esta es una característica especial del sistema unidimensional que no comparten los sistemas bidimensionales y tridimensionales. Como veremos, esto hace que el sistema unidimensional sea muy fácil de manejar.

### 5.1.2 Condiciones de contorno

*(Referencia al programa interactivo 5-1 del disco de programas del curso original.)*

Ya hemos resuelto el problema de la oscilación del sistema infinito. Armados con este resultado, podemos reincorporar la física de las paredes. Cualquier $\beta$ (salvo $\beta=\pm1$) da un par de modos normales para el sistema infinito de la figura 5.2. Pero solo valores especiales de $\beta$ funcionarán para el sistema finito de la figura 5.1. Para encontrar los modos normales del sistema de la figura 5.1, usamos (4.56), el hecho de que cualquier combinación lineal de los dos modos normales con la misma frecuencia angular, $\omega$, también es un modo normal. Si podemos encontrar una combinación lineal que se anule en $j=0$ y en $j=N+1$, será un modo normal del sistema de la figura 5.1. Es la anulación del modo normal en $j=0$ y $j=N+1$ lo que constituye las «condiciones de contorno» de este sistema finito en particular.

Empecemos tratando de satisfacer la condición de contorno en $j=0$. Para cada posible valor de $\omega^2$, solo tenemos que preocuparnos por dos modos normales, las dos soluciones de (5.16) para $\beta$. Mientras $\beta\neq\pm1$, podemos encontrar una combinación que se anule en $j=0$; basta restar los dos modos $A^\beta$ y $A^{\beta^{-1}}$ para obtener un vector

$$A = A^\beta - A^{\beta^{-1}}\,, \qquad \text{(5.18)}$$

o, en componentes,

$$A_j \propto A_j^\beta - A_j^{\beta^{-1}} = \beta^j-\beta^{-j}\,. \qquad \text{(5.19)}$$

Lo primero que hay que notar sobre (5.19) es que $A_j$ no puede anularse para ningún $j\neq0$ a menos que $|\beta|=1$. Así, si vamos a tener alguna posibilidad de satisfacer la condición de contorno en $j=N+1$, debemos suponer que

$$\beta = e^{i\theta}\,. \qquad \text{(5.20)}$$

Entonces, de (5.19),

$$A_j \propto \sin j\theta\,. \qquad \text{(5.21)}$$

Ahora podemos satisfacer la condición de contorno en $j=N+1$ imponiendo $A_{N+1}=0$. Esto implica $\sin[(N+1)\theta]=0$, o

$$\theta = n\pi/(N+1)\,,\quad\text{para } n\text{ entero}\,. \qquad \text{(5.22)}$$

Así, los modos normales del sistema de la figura 5.1 son

$$A_j^n = \sin\left(\frac{jn\pi}{N+1}\right)\,,\quad\text{para } n=1,2,\ldots,N\,. \qquad \text{(5.23)}$$

Otros valores de $n$ no dan modos nuevos: simplemente repiten los $N$ modos ya mostrados en (5.23). Las frecuencias correspondientes se obtienen sustituyendo (5.20)-(5.21) en (5.16), dando

$$\omega^2 = 2B - 2C\cos\theta = 2B - 2C\cos\left(\frac{n\pi}{N+1}\right)\,. \qquad \text{(5.24)}$$

A partir de aquí, el análisis del movimiento del sistema es igual que para cualquier otro sistema de osciladores acoplados. Como se discutió en el capítulo 3, podemos descomponer un movimiento general y expresarlo como suma de los modos normales. Esto se ilustra para el sistema de péndulos acoplados en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-5-1" rel="noopener" target="_blank" title="Animación original de Howard Georgi">5-1</a> del disco de programas. Lo nuevo de este sistema es la manera en que obtuvimos los modos normales, y su forma peculiarmente simple, en términos de funciones trigonométricas. Obtendremos más intuición sobre el significado de estos modos en la siguiente sección. Mientras tanto, note la forma en que los modos simples pueden combinarse para dar el movimiento muy complicado del sistema completo.

## 5.2 $k$ y relaciones de dispersión

Hasta ahora, la separación de equilibrio entre los bloques, $a$, no ha aparecido en el análisis. Todo lo que hemos dicho hasta ahora sería cierto incluso si los muelles tuvieran longitudes aleatorias, siempre que todas las constantes de muelle fueran iguales. En tal caso, la «invariancia bajo traslación espacial» que usamos para resolver el problema sería un artificio puramente matemático, que transforma el sistema original en un sistema distinto con el mismo tipo de pequeñas oscilaciones. Sin embargo, habitualmente, en aplicaciones físicas, la invariancia bajo traslación espacial es real y todas las distancias entre bloques son iguales. Entonces es muy útil etiquetar los bloques por su posición de equilibrio. Tomemos $x=0$ como la posición de la pared izquierda (o del bloque 0). Entonces el primer bloque está en $x=a$, el segundo en $x=2a$, etc., como se muestra en la figura 5.3. Podemos describir el desplazamiento de todos los bloques mediante una función $\psi(x,t)$, donde $\psi(ja,t)$ es el desplazamiento del $j$-ésimo bloque (el que tiene posición de equilibrio $ja$). Por supuesto, esta función no está muy bien definida, porque solo nos importan sus valores en un conjunto discreto de puntos. Sin embargo, como veremos más abajo al discutir la cuerda con cuentas, nos ayudará a entender lo que ocurre si dibujamos una curva suave que pase por estos puntos.

![Figura 5.3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.3.png)

Figura 5.3: los péndulos acoplados etiquetados por su posición de equilibrio, $x=0, a, 2a, \ldots, (N+1)a$.

Del mismo modo, podemos describir un modo normal del sistema de la figura 5.1 (o del sistema infinito de la figura 5.2) como una función $A(x)$, donde

$$A(ja) = A_j\,. \qquad \text{(5.25)}$$

En este lenguaje, la invariancia bajo traslación espacial, (5.11), se convierte en

$$A(x+a) = \beta A(x)\,. \qquad \text{(5.26)}$$

Es convencional escribir la constante $\beta$ como una exponencial

$$\beta = e^{ika}\,. \qquad \text{(5.27)}$$

Cualquier número complejo no nulo puede escribirse como una exponencial de esta forma. De hecho, podemos cambiar $k$ por un múltiplo de $2\pi/a$ sin cambiar $\beta$, así que podemos elegir la parte real de $k$ entre $-\pi/a$ y $\pi/a$:

$$-\frac{\pi}{a} < \text{Re}\,k \le \frac{\pi}{a}\,. \qquad \text{(5.28)}$$

Si sustituimos (5.13) y (5.27) en (5.25), obtenemos

$$A^\beta(ja) = e^{ikja}\,. \qquad \text{(5.29)}$$

Esto sugiere que tomemos la función que describe el modo normal correspondiente a (5.27) como

$$A(x) = e^{ikx}\,. \qquad \text{(5.30)}$$

El modo queda determinado por el número $k$ que satisface (5.28).

El parámetro $k$ (cuando es real) se llama el número de onda angular del modo. Mide la «ondulación» del modo normal, en radianes por unidad de distancia. La «longitud de onda» del modo es la longitud más pequeña, $\lambda$ (letra griega lambda), tal que un cambio de $x$ en $\lambda$ deja el modo sin cambiar,

$$A(x+\lambda) = A(x)\,. \qquad \text{(5.31)}$$

En otras palabras, la longitud de onda es la longitud de un ciclo completo de la onda, $2\pi$ radianes. Así, la longitud de onda, $\lambda$, y el número de onda angular, $k$, son inversamente proporcionales, con un factor de $2\pi$,

$$\lambda = \frac{2\pi}{k}\,. \qquad \text{(5.32)}$$

En este lenguaje, los modos normales del sistema de la figura 5.1 se describen mediante las funciones

$$A^n(x) = \sin kx\,, \qquad \text{(5.33)}$$

con

$$k = \frac{n\pi}{L}\,, \qquad \text{(5.34)}$$

donde $L=(N+1)a$ es la longitud total del sistema. Lo importante de (5.33) y (5.34) es que no dependen de los detalles del sistema; ni siquiera dependen de $N$. Los modos normales siempre tienen la misma forma, cuando el sistema tiene longitud $L$. Por supuesto, a medida que $N$ aumenta, aumenta el número de modos. Para $L$ fija, esto ocurre porque $a=L/(N+1)$ disminuye cuando $N$ aumenta, y por tanto el rango permitido de $k$ (recuerde (5.28)) aumenta.

Las formas (5.33) de los modos normales del sistema invariante bajo traslación espacial se llaman «ondas estacionarias». Veremos con más detalle más abajo por qué la palabra «onda» es apropiada. La palabra «estacionaria» se refiere al hecho de que, aunque las ondas cambian con el tiempo, no parecen moverse en la dirección $x$, a diferencia de las «ondas viajeras» que discutiremos en el capítulo 8 y más adelante.

### 5.2.1 La relación de dispersión

En términos del número de onda angular $k$, la frecuencia del modo es (de (5.16) y (5.27))

$$\omega^2 = 2B - 2C\cos ka\,. \qquad \text{(5.35)}$$

Tal relación entre $k$ (en realidad $k^2$, porque $\cos ka$ es una función par de $k$) y $\omega^2$ se llama «relación de dispersión» (más adelante aprenderemos por qué el nombre es apropiado). La forma específica (5.35) es una característica del sistema infinito particular de la figura 5.2: depende de las masas, las constantes de los muelles, las longitudes de los péndulos y las separaciones.

Pero no depende de las condiciones de contorno. De hecho, veremos más abajo que (5.35) será útil para condiciones de contorno muy distintas de las del sistema de la figura 5.1.

La relación de dispersión depende únicamente de la física del sistema infinito. $\qquad \text{(5.36)}$

De hecho, es solo a través de la relación de dispersión que los detalles de la física del sistema infinito entran en el problema. La forma de los modos, $e^{\pm ikx}$, ya está determinada por las propiedades generales de linealidad e invariancia bajo traslación espacial.

Llamaremos a (5.35) la relación de dispersión de los péndulos acoplados. Le hemos dado un nombre especial porque volveremos a ella muchas veces en lo que sigue. La física esencial es que hay dos fuentes de fuerza restauradora: la gravedad, que tiende a mantener todas las masas en equilibrio; y los muelles de acoplamiento, que tienden a mantener fijas las separaciones entre las masas, pero no se ven afectados si todas las masas se desplazan la misma distancia. En (5.35), las constantes siempre satisfacen $B\ge C$, como se ve en (5.6).

El límite $B=C$ es especialmente interesante: ocurre cuando no hay gravedad (o $\ell\to\infty$). La relación de dispersión es entonces

$$\omega^2 = 2B(1-\cos ka) = 4B\sin^2\frac{ka}{2}\,. \qquad \text{(5.37)}$$

Note que el modo con $k=0$ tiene ahora frecuencia cero, porque todas las masas pueden desplazarse a la vez sin fuerza restauradora.

## 5.3 Ondas

### 5.3.1 La cuerda con cuentas

![Figura 5.4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.4.png)

Figura 5.4: cuerda con cuentas en equilibrio, mostrando varias cuentas espaciadas regularmente sobre una cuerda tensa y recta.

Otro sistema instructivo es la cuerda con cuentas, sometida a oscilaciones transversales. Las oscilaciones se llaman «transversales» si el movimiento es perpendicular a la dirección en la que se extiende el sistema. Considere una cuerda sin masa, con tensión $T$, a la que se atan cuentas idénticas de masa $m$ a intervalos regulares, $a$. Una parte de tal sistema, en su configuración de equilibrio, se muestra en la figura 5.4. Las cuentas no pueden oscilar longitudinalmente, porque la cuerda se rompería (más precisamente, la cuerda tiene una constante de fuerza muy grande y no lineal para el estiramiento longitudinal; las oscilaciones longitudinales tienen una frecuencia mucho mayor y están mucho más fuertemente amortiguadas que las transversales, así que podemos ignorarlas en el rango de frecuencias de los modos transversales; véase la discusión del muelle masivo «ligero» en el capítulo 7). Sin embargo, para pequeñas oscilaciones transversales, el estiramiento de la cuerda es despreciable, y la tensión y la componente horizontal de la fuerza de la cuerda son aproximadamente constantes. La componente horizontal de la fuerza sobre cada bloque, debida a la cuerda de su derecha, se cancela con la componente horizontal debida a la cuerda de su izquierda. La fuerza horizontal total sobre cada bloque es cero (debe serlo, porque los bloques no se mueven horizontalmente). Pero las cuerdas producen una fuerza restauradora transversal cuando las cuentas vecinas no tienen el mismo desplazamiento transversal, como se ilustra en la figura 5.5. Se muestra la fuerza de la cuerda sobre la cuenta 1, junto con su componente transversal. Las líneas punteadas completan triángulos semejantes, de modo que $F/T=(\psi_2-\psi_1)/a$. Puede ver en la figura 5.5 que la fuerza restauradora, $F$ en la figura, es lineal para pequeñas oscilaciones transversales, y corresponde a una constante de muelle $T/a$.

![Figura 5.5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.5.png)

Figura 5.5: dos cuentas vecinas, 1 y 2, en una cuerda con cuentas, mostrando la fuerza de tensión $T$ a lo largo de la cuerda entre ambas y su componente transversal $F \approx (T/a)(\psi_2-\psi_1)$ sobre la cuenta 1.

Así, (5.37) es también la relación de dispersión para las pequeñas oscilaciones transversales de la cuerda con cuentas, con

$$B = \frac{T}{ma}\,, \qquad \text{(5.38)}$$

donde $T$ es la tensión de la cuerda, $m$ es la masa de la cuenta y $a$ es la separación entre cuentas. La relación de dispersión para la cuerda con cuentas puede escribirse entonces como

$$\omega^2 = \frac{4T}{ma}\sin^2\frac{ka}{2}\,. \qquad \text{(5.39)}$$

Esta relación de dispersión, (5.39), tiene la propiedad interesante de que $\omega\to0$ cuando $k\to0$. Esto se discute desde el punto de vista de la simetría en el apéndice C, donde se discute la conexión de esta relación de dispersión con lo que se llaman «bosones de Goldstone». Aquí deberíamos discutir las propiedades especiales del modo $k=0$, con frecuencia angular exactamente nula, $\omega=0$. Este caso es distinto de todos los demás valores de frecuencia angular, porque no obtenemos una dependencia temporal distinta al conjugar la exponencial compleja irreducible, $e^{-i\omega t}$. Pero necesitamos dos soluciones para describir las posibles condiciones iniciales del sistema, porque podemos especificar tanto un desplazamiento como una velocidad para cada cuenta. La resolución de este dilema es similar a la discutida para el amortiguamiento crítico en el capítulo 2 (véase (2.12)). Si nos acercamos a $\omega=0$ desde $\omega$ no nulo, podemos formar dos soluciones independientes así (puede evaluar estos límites fácilmente, usando el desarrollo de Taylor de $e^x=1+x+\cdots$):

$$\lim_{\omega\to0}\frac{e^{-i\omega t}+e^{i\omega t}}{2}=1\,,\qquad \lim_{\omega\to0}\frac{e^{-i\omega t}-e^{i\omega t}}{-2i\omega}=t\,. \qquad \text{(5.40)}$$

La primera, para $k=0$, describe una situación en la que todas las cuentas están en una posición fija. La segunda describe una situación en la que todas las cuentas se mueven juntas con velocidad constante en la dirección transversal.

Se pueden decir cosas precisamente análogas sobre la dependencia en $x$ del modo $k=0$. De nuevo, acercándonos a $k=0$ desde $k$ no nulo, podemos formar dos modos,

$$\lim_{k\to0}\frac{e^{ikx}+e^{-ikx}}{2}=1\,,\qquad \lim_{k\to0}\frac{e^{ikx}-e^{-ikx}}{2ik}=x\,. \qquad \text{(5.41)}$$

El segundo modo aquí describe una situación en la que cada cuenta sucesiva está más desplazada que la anterior. La fuerza transversal sobre cada cuenta, debida a la cuerda de la izquierda, se cancela con la fuerza de la cuerda de la derecha.

### 5.3.2 Extremos fijos

*(Referencia al programa interactivo 5-2 del disco de programas del curso original.)*

![Figura 5.6](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.6.png)

Figura 5.6: cuerda con cuentas de cuatro cuentas numeradas 1 a 4, con ambos extremos fijos a paredes.

Supongamos ahora que consideramos una cuerda con cuentas finita, con sus extremos fijos en $x=0$ y $x=L=(N+1)a$, como se muestra en la figura 5.6. El análisis de los modos normales de este sistema es exactamente el mismo que el del problema de los péndulos acoplados al principio del capítulo. De nuevo, imaginamos que el sistema finito es parte de un sistema infinito con invariancia bajo traslación espacial, y buscamos combinaciones lineales de modos tales que las cuentas en $x=0$ y $x=L$ estén fijas. De nuevo esto conduce a (5.33). Las únicas diferencias son:

1.  Las frecuencias de los modos son distintas, porque la relación de dispersión ahora viene dada por (5.39);
2.  (5.33) describe los desplazamientos transversales de las cuentas.

Este es un ejemplo muy bonito de los modos normales de onda estacionaria, (5.33), porque las formas se ven más fácilmente que para las oscilaciones longitudinales. Para cuatro cuentas ($N=4$), los cuatro modos normales independientes se ilustran en las figuras 5.7-5.10, donde hemos hecho invisibles las cuerdas de acoplamiento por claridad. Las cuentas imaginarias fijas que hacen el papel de las paredes se muestran (discontinuas) en $x=0$ y $x=L$. Superpuesta a las posiciones de las cuentas está la función continua $\sin kx$, para cada valor de $k$, representada con una línea punteada. Note que esta función no describe las posiciones de las cuerdas de acoplamiento, que están estiradas en línea recta entre cuentas vecinas.

![Figura 5.7](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.7.png)

Figura 5.7:-5.10: los cuatro modos normales de la cuerda con cuentas de 4 cuentas y extremos fijos, para $n=1,2,3,4$; cada figura muestra la curva $\sin(n\pi x/L)$ pasando por las cuentas, con un número creciente de nodos y “ondulaciones” a medida que $n$ aumenta.

Son imágenes como las figuras 5.7-5.10 las que justifican la palabra «onda» para estas soluciones de onda estacionaria: son, francamente, onduladas, y exhiben la dependencia espacial senoidal que es la característica esencial de los fenómenos ondulatorios.

La oscilación transversal de una cuerda con cuentas con ambos extremos fijos se ilustra en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-5-2" rel="noopener" target="_blank" title="Animación original de Howard Georgi">5-2</a>, donde se muestra una oscilación general junto con los modos normales de los que está formada. Note las distintas frecuencias de los distintos modos normales, con la frecuencia aumentando a medida que los modos se vuelven más ondulados. A menudo usaremos la cuerda con cuentas como ejemplo ilustrativo, porque los modos son muy fáciles de visualizar.

## 5.4 Extremos libres

Trabajemos un ejemplo de oscilación forzada con un tipo distinto de condición de contorno. Considere las oscilaciones transversales de una cuerda con cuentas. Para concretar, tomaremos cuatro cuentas, de modo que este es un sistema de cuatro osciladores acoplados. Sin embargo, en lugar de acoplar las cuerdas de los extremos a paredes fijas, las uniremos a anillos sin masa que pueden deslizar libremente en la dirección transversal sobre varillas sin fricción. Se dice entonces que la cuerda tiene sus extremos libres (al menos para el movimiento transversal). Entonces el sistema se ve como el diagrama de la figura 5.11, donde los osciladores se mueven hacia arriba y hacia abajo en el plano del papel. Encontremos sus modos normales.

![Figura 5.11](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.11.png)

Figura 5.11: cuerda con cuentas de cuatro cuentas, con ambos extremos unidos a anillos sin masa que deslizan libremente sobre varillas verticales sin fricción, en lugar de a paredes fijas.

### 5.4.1 Modos normales para extremos libres

*(Referencia al programa interactivo 5-3 del disco de programas del curso original.)*

Como antes, imaginamos que esto es parte de un sistema infinito de cuentas con invariancia bajo traslación espacial. Esto se muestra en la figura 5.12. Aquí, los anillos sin masa que deslizan sobre varillas sin fricción se han reemplazado por las cuentas imaginarias (discontinuas) 0 y 5. La relación de dispersión es exactamente la misma que para cualquier otra cuerda con cuentas infinita, (5.39). La pregunta entonces es: ¿qué tipo de condición de contorno en el sistema infinito corresponde a la condición de contorno física de que las cuentas de los extremos son libres por un lado? La respuesta es que la primera cuenta imaginaria de cada lado debe moverse hacia arriba y hacia abajo junto con la última cuenta real, de modo que la cuerda de acoplamiento de la cuenta 0 sea horizontal y no ejerza fuerza restauradora transversal sobre la cuenta 1, y la cuerda de acoplamiento de la cuenta 5 sea horizontal y no ejerza fuerza restauradora transversal sobre la cuenta 4:

$$A_0=A_1\,, \qquad \text{(5.42)}$$

$$A_4=A_5\,; \qquad \text{(5.43)}$$

![Figura 5.12](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.12.png)

Figura 5.12: satisfaciendo las condiciones de contorno en el sistema finito, con las cuentas imaginarias 0 y 5 unidas rígidamente a las cuentas reales 1 y 4, respectivamente.

Trabajaremos en la notación en la que las cuentas se etiquetan por su posición de equilibrio. Los modos normales del sistema infinito son entonces $e^{\pm ikx}$. Pero todavía no hemos tenido que decidir dónde pondremos el origen. ¿Cómo formamos una combinación lineal de los modos exponenciales complejos, $e^{\pm ikx}$, y elegimos $k$ de modo que sea consistente con esta condición de contorno? Empecemos con (5.42). Podemos escribir la combinación lineal, sea cual sea, en la forma

$$\cos(kx-\theta)\,. \qquad \text{(5.44)}$$

Cualquier combinación lineal real de $e^{\pm ikx}$ puede escribirse así, salvo una constante multiplicativa global (véase (1.96)). Ahora bien, si

$$\cos(kx_0-\theta) = \cos(kx_1-\theta)\,, \qquad \text{(5.45)}$$

donde $x_j$ es la posición del $j$-ésimo bloque, entonces o bien

1.  $\cos(kx-\theta)$ tiene un máximo o un mínimo en $(x_0+x_1)/2$, o
2.  $kx_1-kx_0$ es un múltiplo de $2\pi$.

Consideremos el caso 1 (veremos que el caso 2 no da modos adicionales). Elegiremos nuestras coordenadas de modo que el punto $(x_0+x_1)/2$, a medio camino entre $x_0$ y $x_1$, sea $x=0$. No nos importa la normalización global, así que, si la función tiene un mínimo ahí, la multiplicaremos por $-1$, para convertirlo en un máximo. Así, en el caso 1, la función $\cos(kx-\theta)$ tiene un máximo en $x=0$, lo que implica que podemos tomar $\theta=0$. Así, la función es simplemente $\cos kx$. El sistema con este etiquetado se muestra en la figura 5.13. El desplazamiento de la $j$-ésima cuenta es entonces

$$A_j = \cos[ka(j-1/2)]\,. \qquad \text{(5.46)}$$

![Figura 5.13](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.13.png)

Figura 5.13: el mismo sistema de osciladores, etiquetado de forma más conveniente, con el origen $x=0$ situado a medio camino entre las cuentas imaginarias 0 y la cuenta 1, de modo que las cuentas reales quedan en $x=a/2, 3a/2, 5a/2, 7a/2$.

Ahora debería quedar claro cómo imponer la condición de contorno, (5.43), en el otro extremo. Queremos tener un máximo o un mínimo a medio camino entre la cuenta 4 y la cuenta 5, en $x=4a$. Obtenemos un máximo o un mínimo cada vez que el argumento del coseno es un múltiplo entero de $\pi$. El argumento del coseno en $x=4a$ es $4ka$, donde $k$ es el número de onda angular. Así, la condición de contorno se satisfará si el modo tiene $4ka=n\pi$ para $n$ entero. Entonces

$$\cos[ka(4-1/2)] = \cos[ka(5-1/2)] \implies ka=\frac{n\pi}{4}\,. \qquad \text{(5.47)}$$

Así, los modos son

$$A_j = \cos[ka(j-1/2)] \quad\text{con } k=\frac{n\pi}{4a}\,,\ \text{para } n=0\text{ a }3\,. \qquad \text{(5.48)}$$

Para $n>3$, los modos simplemente se repiten, porque $k\ge\pi/a$.

En (5.48), $n=0$ es el modo trivial en el que todas las cuentas se mueven juntas hacia arriba y hacia abajo. Esto es posible porque no hay ninguna fuerza restauradora cuando todas las cuentas se mueven juntas. Como se discutió arriba (véase (5.40)), las cuentas pueden moverse todas con velocidad constante, porque $\omega=0$ para este modo. Note que el caso 2 anterior da el mismo modo, y nada más, porque si $kx_1-kx_0=2n\pi$, entonces (5.44) tiene el mismo valor para todas las $x_j$. Los modos restantes se muestran en las figuras 5.14-5.16. Este sistema se ilustra en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-5-3" rel="noopener" target="_blank" title="Animación original de Howard Georgi">5-3</a> del disco de programas.

![Figura 5.14](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.14.png)

Figura 5.14:-5.16: los modos $n=1,2,3$ de la cuerda con cuentas de extremos libres, mostrando $A_j = \cos[(j-1/2)n\pi/4]$ para cada valor de $n$, con ondulación creciente.

## 5.5 Oscilaciones forzadas y condiciones de contorno

Las oscilaciones forzadas pueden analizarse con los métodos del capítulo 3. Esto siempre funciona, incluso para una fuerza que actúa sobre cada parte del sistema de forma independiente. Sin embargo, muy a menudo, para un sistema invariante bajo traslación espacial, nos interesa un tipo distinto de problema de oscilación forzada: uno en el que la fuerza externa actúa solo en un extremo (o en ambos). En este caso, podemos resolver el problema de una forma mucho más simple, usando condiciones de contorno. Un ejemplo de este tipo se muestra en la figura 5.17.

![Figura 5.17](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.17.png)

Figura 5.17: sistema de péndulos acoplados igual al de la figura 5.1, pero con la pared derecha reemplazada por un agente externo que mueve el extremo del último muelle.

Este es el sistema de (5.1), salvo que se ha eliminado una pared y el extremo del muelle está obligado, por algún agente externo, a moverse hacia adelante y hacia atrás con un desplazamiento

$$z\cos\omega_dt\,. \qquad \text{(5.49)}$$

Como de costumbre, en un problema de oscilación forzada, primero consideramos el término impulsor, en este caso el desplazamiento fijo del bloque $N+1$, (5.49), como la parte real de un término impulsor exponencial complejo,

$$z\,e^{-i\omega_dt}\,. \qquad \text{(5.50)}$$

Luego buscamos una solución estacionaria en la que todo el sistema oscila con la frecuencia impulsora $\omega_d$, con la dependencia temporal irreducible $e^{-i\omega_dt}$.

Si hay amortiguamiento debido a una fuerza de fricción, por pequeña que sea, esta será la solución estacionaria que sobrevive después de que todas las oscilaciones libres se hayan extinguido. Podemos encontrar tales soluciones con el mismo tipo de truco que usamos para encontrar los modos de oscilación libre del sistema: buscamos modos del sistema infinito y los combinamos para satisfacer las condiciones de contorno.

Esta situación es distinta del problema de oscilación libre. En un problema típico de oscilación libre, las condiciones de contorno fijan $k$; luego determinamos $\omega$ a partir de la relación de dispersión. En este caso, las condiciones de contorno determinan $\omega_d$ en su lugar. Ahora debemos usar la relación de dispersión, (5.35), para encontrar el número de onda $k$.

Resolviendo (5.35) obtenemos

$$k = \frac{1}{a}\cos^{-1}\left(\frac{2B-\omega_d^2}{2C}\right)\,. \qquad \text{(5.51)}$$

Debemos combinar los modos del sistema infinito, $e^{\pm ikx}$, para satisfacer las condiciones de contorno en $x=0$ y $x=(N+1)a=L$. Como en el sistema (5.1), la condición de que el sistema esté inmóvil en $x=0$ conduce a un modo de la forma

$$\psi(x,t) = y\sin kx\,e^{-i\omega_dt} \qquad \text{(5.52)}$$

para cierta amplitud $y$. Pero ahora la condición en $x=L=(N+1)a$ determina, no el número de onda (que ya está fijado por la relación de dispersión), sino la amplitud $y$.

$$\psi(L,t) = y\sin kL\,e^{-i\omega_dt} = z\,e^{-i\omega_dt}\,. \qquad \text{(5.53)}$$

Así,

$$y = \frac{z}{\sin kL}\,. \qquad \text{(5.54)}$$

Note que si $\omega_d$ es una frecuencia de modo normal del sistema (5.1) sin amortiguamiento, entonces (5.54) no tiene sentido, porque $\sin kL$ se anula. Así debe ser: corresponde a la amplitud infinita producida por una fuerza impulsora en resonancia con una frecuencia normal de un sistema sin fricción. En presencia de amortiguamiento, sin embargo, como discutiremos en el capítulo 8, el número de onda $k$ es complejo, porque la relación de dispersión es compleja. Veremos más adelante que, si $k$ es complejo, $\sin kL$ no puede anularse. Incluso si el amortiguamiento es muy pequeño, por supuesto, no obtenemos un infinito real en la amplitud al acercarnos a la resonancia: eventualmente, los efectos no lineales toman el control. Si es la no linealidad o el amortiguamiento lo más importante cerca de una resonancia dada depende de los detalles del sistema físico (note también que, cuando $\sin kL$ es complejo, las partes del sistema no oscilan todas en fase, aunque todas oscilan a la misma frecuencia).

### 5.5.1 Oscilaciones forzadas con un extremo libre

![Figura 5.18](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.18.png)

Figura 5.18: masa sobre un muelle, con el otro extremo del muelle movido externamente de forma oscilante.

Como otro ejemplo, discutiremos de nuevo las oscilaciones longitudinales forzadas del sistema simple de una masa sobre un muelle, mostrado en la figura 5.18. La física aquí es la misma que la del sistema de la figura 2.9, salvo que, para empezar, ignoraremos el amortiguamiento. El bloque tiene masa $m$. El muelle tiene constante $K$ y longitud de equilibrio $a$. Para concretar, imagine que este bloque está sobre una mesa casi sin fricción, y que usted sostiene el otro extremo del muelle, moviéndolo hacia adelante y hacia atrás sobre la mesa, paralelamente a la dirección del muelle, con desplazamiento

$$d_0\cos\omega_dt\,. \qquad \text{(5.55)}$$

La pregunta es: ¿cómo se mueve el bloque? Ya sabemos resolver este problema desde el capítulo 2. Ahora lo haremos de una forma distinta, usando la invariancia bajo traslación espacial, las interacciones locales y las condiciones de contorno. Puede parecer sorprendente que podamos tratar este problema con las técnicas que hemos desarrollado para sistemas invariantes bajo traslación espacial, porque solo hay un bloque. Sin embargo, eso es lo que vamos a hacer. Ciertamente nada nos impide extender este sistema a un sistema infinito, repitiendo la combinación bloque-muelle. El sistema infinito tiene entonces la relación de dispersión de la cuerda con cuentas (o de los péndulos acoplados con $\ell\to\infty$):

$$\omega_d^2 = \frac{4K}{m}\sin^2\frac{ka}{2}\,. \qquad \text{(5.56)}$$

La parte relevante del sistema infinito se muestra en la figura 5.19. La idea es que podemos imponer condiciones de contorno sobre el sistema infinito, figura 5.19, que lo hagan equivalente a la figura 5.18.

![Figura 5.19](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.19.png)

Figura 5.19: fragmento del sistema infinito de masas y muelles, mostrando las masas 0, 1 y 2.

Empezamos imaginando que el desplazamiento es complejo, $d_0e^{-i\omega_dt}$, de modo que al final tomaremos la parte real para recuperar el resultado real de (5.55). Así, tomamos

$$\psi_2(t) = d_0\,e^{-i\omega_dt}\,. \qquad \text{(5.57)}$$

Entonces, para garantizar que no haya fuerza sobre el bloque 1 debida al muelle imaginario de la izquierda, debemos tomar

$$\psi_0(t) = \psi_1(t)\,. \qquad \text{(5.58)}$$

Para satisfacer (5.58), podemos argumentar, como en la figura 5.13, que

$$\psi(x,t) = z(t)\cos kx \qquad \text{(5.59)}$$

donde $x$ se define como en la figura 5.20.

![Figura 5.20](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.20.png)

Figura 5.20: una mejor definición del origen de $x$, con el origen a medio camino entre las masas 0 y 1.

Ahora, como la posición de equilibrio del bloque 2 es $3a/2$, sustituimos

$$\psi_2(t) = z(t)\cos\frac{3ka}{2} \qquad \text{(5.60)}$$

en (5.57), para obtener

$$z(t) = \frac{d_0}{\cos\frac{3ka}{2}}\,e^{-i\omega_dt}\,. \qquad \text{(5.61)}$$

Entonces el resultado final es

$$\psi_1(t) = \frac{\cos\frac{ka}{2}}{\cos\frac{3ka}{2}}\,d_0\,e^{-i\omega_dt} \qquad \text{(5.62)}$$

o, en forma real,

$$\psi_1(t) = \frac{\cos\frac{ka}{2}}{\cos\frac{3ka}{2}}\,d_0\cos\omega_dt\,. \qquad \text{(5.63)}$$

Ahora podemos usar la relación de dispersión. Primero usamos trigonometría,

$$\cos3y = \cos^3y-3\cos y\sin^2y = \cos y\left(1-4\sin^2y\right) \qquad \text{(5.64)}$$

para escribir

$$\psi_1(t) = \frac{1}{1-4\sin^2\frac{ka}{2}}\,d_0\cos\omega_dt \qquad \text{(5.65)}$$

o, sustituyendo (5.56),

$$\psi_1(t) = \frac{\omega_0^2}{\omega_0^2-\omega_d^2}\,d_0\cos\omega_dt\,, \qquad \text{(5.66)}$$

donde $\omega_0$ es la frecuencia de oscilación libre del sistema,

$$\omega_0^2 = \frac{K}{m}\,. \qquad \text{(5.67)}$$

Esta es exactamente la misma fórmula de resonancia que obtuvimos en el capítulo 2.

### 5.5.2 Generalización

La verdadera ventaja del procedimiento que usamos para resolver este problema es que es fácil de generalizar. Por ejemplo, supongamos que consideramos el sistema mostrado en la figura 5.21.

![Figura 5.21](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.21.png)

Figura 5.21: sistema con dos bloques en línea, unidos por muelles, con el extremo derecho movido externamente.

Aquí podemos pasar al mismo sistema infinito y argumentar que la solución es proporcional a $\cos kx$, donde $x$ se define como en la figura 5.22. Entonces el mismo argumento conduce al resultado para los desplazamientos de los bloques 1 y 2:

$$\psi_1(t) = \frac{\cos\frac{ka}{2}}{\cos\frac{5ka}{2}}\,d_0\cos\omega_dt\,,\qquad \psi_2(t) = \frac{\cos\frac{3ka}{2}}{\cos\frac{5ka}{2}}\,d_0\cos\omega_dt\,. \qquad \text{(5.68)}$$

![Figura 5.22](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.22.png)

Figura 5.22: el sistema infinito correspondiente, con el origen definido a medio camino entre las masas 0 y 1.

Debería poder generalizar esto a un número arbitrario de bloques.

## 5.6 Circuitos LC acoplados

Vimos en el capítulo 1 la analogía entre el circuito LC de la figura 1.10 y el sistema correspondiente de una masa y muelles de la figura 1.11. En esta sección discutimos qué ocurre cuando combinamos circuitos LC en un sistema invariante bajo traslación espacial.

Por ejemplo, considere un circuito infinito invariante bajo traslación espacial, del que se muestra un fragmento en la figura 5.23. Podría suponerse, basándose en la discusión del capítulo 1, que el circuito de la figura 5.23 es análogo a la combinación de muelles y masas mostrada en la figura 5.24, con la correspondencia entre ambos sistemas:

![Figura 5.24](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.24.png)

Figura 5.24

$$m \leftrightarrow L\,,\qquad K \leftrightarrow 1/C\,,\qquad x_j \leftrightarrow Q_j \qquad \text{(5.69)}$$

donde $x_j$ es el desplazamiento del $j$-ésimo bloque hacia la derecha, y $Q_j$ es la carga que ha «pasado» a través del $j$-ésimo inductor desde la situación de equilibrio con los condensadores descargados.

![Figura 5.23](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.23.png)

Figura 5.23: circuito infinito de inductores $L$ y condensadores $C$ conectados alternativamente, con separación $a$ entre elementos idénticos. Figura 5.24: sistema mecánico análogo — cadena infinita de masas $m$ conectadas por muelles $K$.

De hecho, esto es correcto, y podríamos usar (5.69) para escribir la relación de dispersión de la figura 5.23. Sin embargo, con nuestras potentes herramientas de linealidad e invariancia bajo traslación espacial, podemos resolver el problema desde cero sin demasiado esfuerzo. La estrategia será escribir lo que sabemos que debe parecer la solución, por la invariancia bajo traslación espacial, y luego trabajar hacia atrás para encontrar la relación de dispersión.

El punto de partida debería resultarle familiar a estas alturas. Como el sistema es lineal e invariante bajo traslación espacial, los modos del sistema infinito son proporcionales a $e^{\pm ikx}$. Por tanto, todas las cantidades físicas de un modo —voltajes, cargas, corrientes, lo que sea— también deben ser proporcionales a $e^{\pm ikx}$. En este caso, la variable $x$ es realmente solo una etiqueta: las propiedades eléctricas del circuito no dependen mucho de la disposición de los elementos en el espacio (esto no es exactamente cierto, sin embargo: la relatividad impone restricciones; véase el capítulo 11). La relación de dispersión dependerá solo de $ka$, donde $a$ es la separación entre las partes idénticas del sistema (véase (5.35)). Sin embargo, es más fácil pensar en el sistema si se dispone físicamente en una configuración invariante bajo traslación espacial, como en la figura 5.23.

![Figura 5.25](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.25.png)

Figura 5.25: etiquetado del sistema infinito de circuitos LC acoplados, con los inductores numerados $-2,-1,0,1$ y los condensadores en las posiciones intermedias.

En particular, etiquetemos los inductores y condensadores como se muestra en la figura 5.25. Entonces la carga desplazada a través del $j$-ésimo inductor, en el modo con número de onda angular $k$, es

$$Q_j(t) = q\,e^{ijka}\,e^{-i\omega t} \qquad \text{(5.70)}$$

para alguna carga constante $q$. Note que igualmente podríamos haber tomado la dependencia temporal como $\cos\omega t$, $\sin\omega t$, o $e^{i\omega t}$; no importa para el argumento siguiente. Lo que importa es que, al derivar $Q_j(t)$ dos veces respecto al tiempo, obtenemos $-\omega^2Q_j(t)$. La corriente a través del $j$-ésimo inductor es

$$I_j = \frac{d}{dt}Q_j(t) = -i\omega q\,e^{ijka}\,e^{-i\omega t}\,. \qquad \text{(5.71)}$$

La carga en el $j$-ésimo condensador, que llamaremos $q_j$, también es proporcional a $e^{ijka}e^{-i\omega t}$, pero de hecho podemos calcularla directamente. La carga, $q_j$, es simplemente

$$q_j = Q_j - Q_{j+1} \qquad \text{(5.72)}$$

porque la carga desplazada a través del $j$-ésimo inductor debe fluir hacia el $j$-ésimo condensador, o pasar a través del inductor $j+1$, de modo que $Q_j=q_j+Q_{j+1}$. Ahora podemos calcular el voltaje, $V_j$, de cada condensador,

$$V_j = \frac{1}{C}(Q_j-Q_{j+1}) = \frac{q}{C}\left(1-e^{ika}\right)e^{ijka}\,e^{-i\omega t}\,, \qquad \text{(5.73)}$$

y luego calcular la caída de voltaje a través de los inductores,

$$L\,\frac{dI_j}{dt} = V_{j-1}-V_j\,, \qquad \text{(5.74)}$$

sustituyendo (5.71) y (5.73) en (5.74), y dividiendo ambos lados por el factor común $-qL\,e^{ijka}e^{-i\omega t}$, obtenemos la relación de dispersión,

$$\omega^2 = -\frac{1}{LC}\left(1-e^{ika}\right)\left(e^{-ika}-1\right) = \frac{4}{LC}\sin^2\frac{ka}{2}\,. \qquad \text{(5.75)}$$

Esto corresponde a (5.37) con $B=1/LC$. Esto es justamente lo que esperamos de (5.69). Llamaremos a (5.75) la relación de dispersión de los circuitos LC acoplados.

### 5.6.1 Un ejemplo de circuitos LC acoplados

![Figura 5.26](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.26.png)

Figura 5.26: circuito con tres inductores en serie, cada uno conectado a un condensador a tierra, formando un sistema finito. Figura 5.27: sistema mecánico análogo, tres masas conectadas por cuatro muelles entre dos paredes fijas.

Usemos los resultados de esta sección para estudiar un ejemplo finito, con condiciones de contorno. Considere el circuito mostrado en la figura 5.26. Este circuito es análogo a la combinación de muelles y masas mostrada en la figura 5.27.

![Figura 5.27](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.27.png)

Figura 5.27

Ya sabemos que esto es cierto para el interior. Solo queda entender las condiciones de contorno en los extremos. Si etiquetamos los inductores como se muestra en la figura 5.28, podemos imaginar que este sistema es parte del sistema infinito mostrado en la figura 5.23, con las cargas obligadas a satisfacer

$$Q_0=Q_4=0\,. \qquad \text{(5.76)}$$

![Figura 5.28](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.28.png)

Figura 5.28: etiquetado de los inductores del circuito de la figura 5.26, numerados 1, 2 y 3.

Esto debe ser correcto: no puede desplazarse carga a través de los inductores 0 y 4, porque en la figura 5.26 estos no existen. Esto es justamente lo que esperamos de la analogía con el sistema de (5.27), donde el desplazamiento de los bloques 0 y 4 debe anularse, porque ocupan el lugar de las paredes fijas.

Ahora podemos escribir inmediatamente la solución para los modos normales, en analogía con (5.21) y (5.22),

$$Q_j \propto \sin\frac{jn\pi}{4} \qquad \text{(5.77)}$$

para $n=1$ a $3$.

### 5.6.2 Un problema de oscilación forzada para circuitos LC acoplados

![Figura 5.29](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.29.png)

Figura 5.29: circuito con tres inductores, con una fuente de voltaje oscilante conectada en un extremo. Figura 5.30: los voltajes $V_0$ a $V_3$ en los distintos nodos del sistema de la figura 5.29.

Un ejemplo algo más práctico puede ser instructivo. Considere el circuito mostrado en la figura 5.29. El símbolo de fuente en la figura representa una fuente de voltaje que varía armónicamente. Supondremos que el voltaje en este punto del circuito está fijado por la fuente, de modo que

![Figura 5.30](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/fig5.30.png)

Figura 5.30

$$V\cos\omega t\,. \qquad \text{(5.78)}$$

Nos gustaría encontrar los voltajes en los otros nodos del sistema, como se muestra en la figura 5.30, con

$$V_3 = V\cos\omega t\,. \qquad \text{(5.79)}$$

Podríamos resolver este problema usando las cargas desplazadas; sin embargo, es un poco más fácil usar el hecho de que todas las cantidades físicas del sistema infinito de la figura 5.23 son proporcionales a $e^{ikx}$ en un modo con número de onda angular $k$. Como este es un problema de oscilación forzada (y, como de costumbre, ignoramos las posibles oscilaciones libres del sistema y buscamos la solución estacionaria), $k$ queda determinado por $\omega$ mediante la relación de dispersión del sistema infinito de circuitos LC acoplados, (5.75).

Lo otro que necesitamos es que

$$V_0=0\,, \qquad \text{(5.80)}$$

porque el circuito está cortocircuitado en ese extremo. Así, debemos combinar los dos modos del sistema infinito, $e^{\pm ikx}$, en $\sin kx$, y la solución tiene la forma

$$V_j \propto \sin jka\,. \qquad \text{(5.81)}$$

Podemos satisfacer la condición de contorno en el otro extremo tomando

$$V_j = \frac{V}{\sin3ka}\sin jka\,\cos\omega t\,. \qquad \text{(5.82)}$$

Esta es la solución.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Reconocer un sistema finito como parte de un sistema infinito invariante bajo traslación espacial;
2.  Encontrar los modos normales del sistema finito como combinaciones lineales de modos normales del sistema infinito invariante bajo traslación espacial, consistentes con la física de las fronteras, imponiendo condiciones de contorno;
3.  Describir los modos normales de un sistema invariante bajo traslación espacial en términos de un número de onda angular, $k$;
4.  Encontrar la relación de dispersión que relaciona la frecuencia angular, $\omega$, con el número de onda angular, $k$;
5.  Resolver problemas de oscilación forzada usando condiciones de contorno;
6.  Analizar sistemas invariantes bajo traslación espacial de circuitos LC acoplados.

## Problemas

**5.1.** Considere las pequeñas oscilaciones longitudinales del sistema mostrado a continuación: cuatro péndulos acoplados idénticos en línea, entre dos paredes fijas, cada masa de masa $m$, cada péndulo de longitud $\ell$, cada muelle de constante $\kappa$, con separación de equilibrio $a$ entre las masas.

1.  Encuentre la matriz $M^{-1}K$ de este sistema en la base en la que los desplazamientos de los bloques respecto al equilibrio se miden todos hacia la derecha y se organizan en un vector de la forma obvia,

$$X(t) = \begin{pmatrix}x_1(t)\\x_2(t)\\x_3(t)\\x_4(t)\end{pmatrix}\,.$$

1.  Clasifique como VERDADERO o FALSO cada una de las siguientes afirmaciones sobre los modos normales de este sistema. Si es posible, explique sus respuestas cualitativamente, es decir, en palabras en lugar de sustituir en una fórmula, y discuta la generalidad de sus resultados.

    1.  En el modo normal de frecuencia más baja, todos los bloques se mueven en la misma dirección cuando se mueven.
    2.  En el modo normal de segunda frecuencia más baja, el primer y el segundo bloque tienen el mismo desplazamiento.
    3.  En el modo normal de frecuencia más alta, los bloques vecinos se mueven en direcciones opuestas cuando se mueven.

2.  Encuentre las frecuencias angulares de cada uno de los modos normales. Pista: puede querer usar la relación de dispersión de los péndulos acoplados,

$$\omega^2 = 2B-2C\cos ka$$

donde

$$B = \frac{g}{2\ell}+\frac{\kappa}{m}\,,\qquad C=\frac{\kappa}{m}\,.$$

**5.2.** Considere el sistema de cinco bloques mostrado en la figura, todos de masa $m$, obligados a moverse solo horizontalmente. Los muelles largos, con seis espiras, tienen constante $K$. Los muelles más cortos, con tres espiras, tienen constante $2K$. Los muelles más cortos aún, con dos espiras, tienen constante $3K$ (como verá en el capítulo 7, esto es lo esperado si todos los muelles están hechos del mismo material).

![Figura](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/figs1.png)

Figura: cinco bloques en línea entre dos paredes fijas, conectados por una alternancia de muelles largos (constante $K$), medianos (constante $2K$) y cortos (constante $3K$), en un patrón simétrico.

Encuentre los modos normales del sistema y las frecuencias correspondientes. Asegúrese de justificar cualquier suposición que haga sobre los modos normales. Pista: intente encontrar un sistema infinito con invariancia bajo traslación espacial que contenga a este de tal forma que pueda incorporar la física de las paredes como condición de contorno. Otra pista: esto solo funciona de forma simple si los muelles de tres espiras tienen exactamente el doble de la constante de los muelles largos. Su respuesta debería explicar por qué.

**5.3.** En la cuerda con cuentas mostrada a continuación, el intervalo entre cuentas vecinas es $a$, y la distancia entre las cuentas de los extremos y las paredes es $a/2$. Todas las cuentas tienen masa $m$ y están obligadas a moverse solo verticalmente, en el plano del papel.

![Figura](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh5_ES/figs2.png)

Figura: cinco cuentas numeradas 1 a 5 sobre una cuerda, separadas una distancia $a$ entre sí y $a/2$ de las paredes en ambos extremos.

Demuestre que la física de la pared izquierda puede incorporarse pasando a un sistema infinito y exigiendo la condición de contorno $A_0=-A_1$.

1.  Fácil: encuentre la condición de contorno análoga para la pared derecha.

2.  Encuentre los modos normales y las frecuencias correspondientes.

**5.4.** Considere el siguiente circuito: seis nodos con voltajes $V_0$ a $V_6$, conectados en cadena por inductores idénticos, con condensadores idénticos a tierra en cada nodo intermedio, y el nodo central conectado a tierra.

Todos los condensadores tienen la misma capacitancia, $C\approx0.00667\ \mu\text{F}$, y todos los inductores tienen la misma inductancia, $L\approx150\ \mu\text{H}$, y ninguna resistencia. El hilo central está conectado a tierra. Este circuito es un análogo eléctrico de los sistemas invariantes bajo traslación espacial de osciladores mecánicos acoplados que hemos discutido en este capítulo.

Cuando aplica una señal oscilante armónicamente desde un generador de señales, a través de un cable coaxial, a $V_6$, se inducen distintos voltajes oscilantes a lo largo de la línea. Es decir, si

$$V_6(t) = V\cos\omega t\,,$$

entonces $V_j(t)$ tiene la forma

$$V_j(t) = A_j\cos\omega t + B_j\sin\omega t\,.$$

Encuentre $A_j$ y $B_j$.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.


---

<!-- MIT8.03_TextCh6_ES.md -->

# Capítulo 6: Límite continuo y series de Fourier

«Continuo» está en el ojo del observador. La mayoría de los sistemas que consideramos continuos están en realidad formados por partes discretas. En este capítulo mostramos que un sistema discreto puede parecer continuo a escalas de distancia mucho mayores que la separación entre sus partes. También exploraremos la física y las matemáticas de las series de Fourier.

## Vídeos de esta clase (YouTube)

- [Clase 8: Simetría de traslación](https://www.youtube.com/watch?v=J1uHGy1tRmM)
- [Clase 9: Ecuación de ondas, ondas estacionarias, series de Fourier](https://www.youtube.com/watch?v=1JeBWHzrRD4)
- [Clase 10: Ondas viajeras](https://www.youtube.com/watch?v=SnNmbVH5DAM)
- [Clase 11: Ondas sonoras](https://www.youtube.com/watch?v=RhIh1zw0-BM)

## Resumen previo

En este capítulo discutimos la ecuación de ondas, el punto de partida de otros tratamientos de las ondas. La obtendremos como resultado natural de nuestros principios generales de invariancia bajo traslación espacial e interacciones locales, aplicados a sistemas continuos.

1.  Estudiaremos los sistemas discretos invariantes bajo traslación espacial discutidos en el capítulo anterior, en el límite en que la separación entre partes tiende a cero. Argumentaremos que el resultado genérico es un sistema continuo que obedece la ecuación de ondas.

2.  El límite continuo de la cuerda con cuentas es una cuerda continua con oscilaciones transversales. Discutiremos sus modos normales para diversas condiciones de contorno. Veremos que los modos normales de un sistema continuo invariante bajo traslación espacial son los mismos que los de un sistema finito; la única diferencia es que hay un número infinito de ellos. La suma sobre el número infinito de modos normales necesaria para resolver el problema de valores iniciales de tal sistema continuo se llama serie de Fourier.

## 6.1 El límite continuo

Considere un sistema discreto invariante bajo traslación espacial en el que la separación entre masas vecinas es $a$. Si $a$ es muy pequeño, el sistema discreto parece continuo. Para entender esta afirmación, considere la acción de la matriz $M^{-1}K$, (5.8), en la notación del capítulo anterior, en la que los grados de libertad se etiquetan por su posición de equilibrio. La matriz $M^{-1}K$ actúa sobre un vector para producir otro vector. Hemos reemplazado nuestros vectores por funciones de $x$, así que $M^{-1}K$ es algo que actúa sobre una función $A(x)$ para dar otra función. Llamémosla $M^{-1}KA(x)$. Es más fácil ver qué ocurre para la cuerda con cuentas, para la cual $B=C=T/ma$. Entonces

$$M^{-1}KA(x) = \left(\frac{T}{ma}\right)\left(2A(x)-A(x+a)-A(x-a)\right)\,. \qquad \text{(6.1)}$$

Hasta aquí, (6.1) es correcta para cualquier $a$, grande o pequeño.

Siempre que diga que una cantidad dimensional, como la longitud $a$, es grande o pequeña, debe especificar una cantidad de comparación: debe decir grande o pequeña *comparada con qué* (una cantidad adimensional no requiere este paso: un número adimensional es grande si es mucho mayor que uno, y pequeño si es mucho menor que uno). En este caso, la otra cantidad dimensional del problema con dimensiones de longitud es la longitud de onda del modo que nos interesa. Aquí es donde entra el que $a$ sea pequeño. Si solo nos interesan modos con longitud de onda $\lambda=2\pi/k$ muy grande comparada con $a$, entonces $ka$ es un número adimensional muy pequeño, y $A(x+a)$ está muy cerca de $A(x)$. Podemos expandirla en una serie de Taylor rápidamente convergente. Expandiendo (6.1) en serie de Taylor obtenemos

$$M^{-1}KA(x) = -\frac{Ta}{m}\,\frac{\partial^2A(x)}{\partial x^2} + \cdots \qquad \text{(6.2)}$$

donde los puntos suspensivos representan términos de derivadas superiores, más pequeños por potencias del número pequeño $ka$ que el primer término de (6.2). En el límite en que tomamos $a$ realmente diminuto (siempre en comparación con las longitudes de onda que queremos estudiar), podemos reemplazar $m/a$ por la densidad de masa lineal $\rho_L$, o masa por unidad de longitud de la cuerda ahora casi continua, e ignorar los términos de orden superior. En este límite, podemos reemplazar la matriz $M^{-1}K$ por la combinación de derivadas que aparece en el primer término superviviente de la serie de Taylor, (6.2),

$$M^{-1}K \to -\frac{T}{\rho_L}\,\frac{\partial^2}{\partial x^2}\,. \qquad \text{(6.3)}$$

Entonces la ecuación de movimiento para $\psi(x,t)$ se convierte en la ecuación de ondas:

$$\frac{\partial^2}{\partial t^2}\psi(x,t) = \frac{T}{\rho_L}\,\frac{\partial^2}{\partial x^2}\psi(x,t)\,. \qquad \text{(6.4)}$$

La relación de dispersión es

$$\omega^2 = \frac{T}{\rho_L}\,k^2\,. \qquad \text{(6.5)}$$

Esto puede verse directamente sustituyendo el modo normal $e^{ikx}$ en (6.4), o tomando el límite de (5.37)-(5.38) cuando $a\to0$. La ecuación (6.5) es la relación de dispersión de la cuerda continua ideal. La cantidad $\sqrt{T/\rho_L}$ tiene dimensiones de velocidad; se llama la «velocidad de fase», $v_\varphi$. Como discutiremos con mucho más detalle en el capítulo 8 y siguientes, esta es la velocidad con la que las ondas viajeras se mueven por la cuerda.

Llamaremos «aproximación del continuo» a la aproximación de reemplazar un sistema discreto por un sistema continuo que se ve aproximadamente igual para $k\gg1/a$. En realidad, todos los sistemas mecánicos que consideraremos son discretos, al menos a nivel atómico. Sin embargo, si solo nos preocupan las ondas con longitudes de onda macroscópicas, la aproximación del continuo es muy buena.

### 6.1.1 Filosofía y especulación

Nuestro tratamiento de la ecuación de ondas en (6.4) es un poco inusual. En muchos tratamientos de los fenómenos ondulatorios, se le da a la ecuación de ondas un lugar de honor. De hecho, la ecuación de ondas es solo una reformulación de la relación de dispersión, (6.5), que habitualmente es solo una aproximación a lo que realmente está ocurriendo. Casi todos los sistemas que habitualmente tratamos con la ecuación de ondas son en realidad discretos a distancias muy pequeñas. En realidad no podemos llegar del todo al límite continuo que da (6.5). Las ondas de luz, que estudiaremos en los próximos capítulos, hasta donde sabemos, podrían ser una excepción a esta regla, y ser completamente continuas. Sin embargo, en realidad no tenemos derecho a suponer ni siquiera eso. Podría ser que, a distancias muy cortas, muy por debajo de todo lo que podemos observar hoy, la naturaleza de la luz e incluso del espacio y el tiempo cambie de alguna manera, de modo que el espacio y el tiempo mismos tengan cierta escala de longitud característica diminuta, $a$. El análisis anterior muestra que ¡esto no importa! Mientras solo podamos observar el espacio y el tiempo a distancias mucho mayores que $a$, nos parecerán continuos. Entonces, como somos científicos, preocupados por cómo se ve el mundo en nuestros experimentos, y no por cómo se comporta en algún régimen ideal muy más allá de lo que podemos sondear experimentalmente, bien podemos tratarlos como continuos.

## 6.2 Series de Fourier

### 6.2.1 La cuerda con extremos fijos

*(Referencia al programa interactivo 6-1 del disco de programas del curso original.)*

Si estiramos nuestra cuerda continua entre paredes fijas, de modo que $\psi(0)=\psi(\ell)=0$, los modos vienen dados por (5.33) y (5.34), igual que para el sistema discreto. La única diferencia es que ahora $n$ va de 1 a $\infty$, o al menos hasta un $n$ tan grande que la longitud de onda $2\pi/k=2\ell/n$ sea tan pequeña que la aproximación del continuo deje de valer. Esto se sigue de (5.28), que, como aquí $k$ es real, se convierte en

$$-\frac{\pi}{a} < k \le \frac{\pi}{a}\,. \qquad \text{(6.6)}$$

A medida que $a\to0$, el rango permitido de $k$ crece hasta el infinito.

Estos modos de onda estacionaria se animan en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-6-1" rel="noopener" target="_blank" title="Animación original de Howard Georgi">6-1</a> del disco de programas, suponiendo la relación de dispersión (6.5).

Ahora podemos discutir la base física de la serie de Fourier. En (3.77), en el capítulo 3, mostramos que los modos normales de un sistema discreto son linealmente independientes y completos. Eso significa que cualquier desplazamiento del sistema discreto puede escribirse como una única combinación lineal de los modos normales. Físicamente, esto debe ser así para poder resolver el problema de valores iniciales. Nuestra imagen de la cuerda continua es un límite de la cuerda con cuentas en el que el número de cuentas, $N$, tiende a infinito y las cuentas se acercan infinitamente entre sí. Para cada $N$, el desplazamiento más general del sistema puede desarrollarse como una combinación lineal de los $N$ modos normales. Si el límite $N\to\infty$ se comporta razonablemente bien, cabría esperar que el desplazamiento más general de la cuerda continua límite pudiera desarrollarse en términos del número infinito de modos normales del sistema continuo. Este desarrollo es una serie de Fourier. El desplazamiento del sistema continuo se describe mediante una función de la posición a lo largo de la cuerda. Si la función no es demasiado discontinua, el desarrollo en modos normales funciona bien.

Considere la cuerda continua, estirada entre paredes fijas en $x=0$ y $x=\ell$. El desplazamiento transversal de este sistema en cualquier instante se describe mediante una función continua de $x$, $\psi(x)$, con

$$\psi(0) = \psi(\ell) = 0\,. \qquad \text{(6.7)}$$

Así, esperamos, por el argumento anterior, poder expresar cualquier función que no sea demasiado discontinua y que satisfaga (6.7) como una suma de los modos normales dados por (5.33) y (5.34),

$$\psi(x) = \sum_{n=1}^{\infty}c_n\sin\frac{n\pi x}{\ell}\,. \qquad \text{(6.8)}$$

Las constantes $c_n$ se llaman los «coeficientes de Fourier». Pueden encontrarse usando la siguiente identidad:

$$\int_0^\ell dx\,\sin\frac{n\pi x}{\ell}\sin\frac{n'\pi x}{\ell} = \begin{cases}\ell/2 & \text{si } n=n'\\ 0 & \text{si } n\neq n'\end{cases} \qquad \text{(6.9)}$$

de modo que

$$c_n = \frac{2}{\ell}\int_0^\ell dx\,\sin\frac{n\pi x}{\ell}\,\psi(x)\,. \qquad \text{(6.10)}$$

Este es simplemente el método de las coordenadas normales adaptado a la situación continua.

### 6.2.2 Extremos libres

*(Referencia al programa interactivo 6-2 del disco de programas del curso original.)*

La ecuación (6.8) se llama la serie de Fourier de una función que satisface (6.7). Otras condiciones de contorno dan series distintas. Por ejemplo, considere una cuerda con el extremo $x=0$ fijo en $z=0$. Suponga que el otro extremo, en $x=\ell$, está unido a un anillo sin masa que puede deslizar libremente a lo largo de una varilla sin fricción en la dirección $z$, como se muestra en la figura 6.1. Decimos que este sistema tiene un «extremo libre», porque el extremo en $x=\ell$ es libre de deslizar en la dirección transversal, aunque está fijo en la dirección $x$.

![Figura 6.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh6_ES/fig6.1.png)

Figura 6.1: cuerda continua con el extremo $x=0$ fijo y el extremo $x=\ell$ unido a un anillo sin masa que desliza libremente sobre una varilla sin fricción, perpendicular a la cuerda.

Como la varilla no tiene fricción, la fuerza sobre el anillo debida a la varilla no puede tener componente en la dirección $z$. Pero, como el anillo no tiene masa, la fuerza total sobre él debe anularse. Por tanto, la fuerza sobre el anillo debida a la cuerda tampoco puede tener componente en la dirección $z$. Esto implica que la cuerda es horizontal en $x=\ell$. Pero la forma de la cuerda en un instante dado viene dada por la gráfica del desplazamiento transversal, $\psi(x,t)$, frente a $x$ (esta es la razón por la que las oscilaciones transversales son más fáciles de visualizar que las longitudinales; compárese con (7.5)). Así, la pendiente de $\psi(x,t)$ en $x=\ell$ debe anularse. Por tanto, las condiciones de contorno apropiadas para el desplazamiento son

$$\psi(0,t) = 0\,,\qquad \left.\frac{\partial}{\partial x}\psi(x,t)\right|_{x=\ell} = 0\,. \qquad \text{(6.11)}$$

Esto implica que los modos normales también satisfacen condiciones de contorno similares:

$$A_n(0)=0\,,\qquad A_n'(\ell)=0\,. \qquad \text{(6.12)}$$

La primera condición implica que la solución debe tener la forma

$$A_n(x) \propto \sin k_nx \qquad \text{(6.13)}$$

para cierto $k_n$. La segunda condición determina los posibles valores de $k_n$: implica que $\sin k_nx$ debe tener un máximo o un mínimo en $x=\ell$, lo que a su vez implica que

$$k_n\ell = \frac{\pi}{2}+n\pi \qquad \text{(6.14)}$$

donde $n$ es un entero no negativo (no negativo porque podemos elegir todos los $k_n>0$ en (6.13); los valores negativos solo cambian el signo de $A_n(x)$ y no dan lugar a soluciones nuevas). Las soluciones tienen la forma

$$\sin\left(\frac{(2n+1)\pi x}{2\ell}\right) \quad\text{para } n=0\text{ a }\infty\,. \qquad \text{(6.15)}$$

Estos modos normales se animan en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-6-2" rel="noopener" target="_blank" title="Animación original de Howard Georgi">6-2</a>. Con estos modos normales, podemos describir una función arbitraria, $\psi(x)$, que satisfaga las condiciones de contorno de este sistema, (6.11),

$$\psi(0)=0\,,\qquad \psi'(\ell)=0\,. \qquad \text{(6.16)}$$

Así, para tal función, podemos escribir

$$\psi(x) = \sum_{n=1}^{\infty}c_n\sin\left(\frac{(2n+1)\pi x}{2\ell}\right) \qquad \text{(6.17)}$$

donde

$$c_n = \frac{2}{\ell}\int_0^\ell dx\,\sin\left(\frac{(2n+1)\pi x}{2\ell}\right)\psi(x)\,. \qquad \text{(6.18)}$$

### 6.2.3 Ejemplos de series de Fourier

*(Referencia al programa interactivo 6-3 del disco de programas del curso original.)*

Encontremos los coeficientes de Fourier de la siguiente función, definida en el intervalo $[0,1]$:

$$\psi(x) = \begin{cases} x & \text{para } x\le w\,,\\ \dfrac{w(1-x)}{1-w} & \text{para } x>w\,. \end{cases} \qquad \text{(6.19)}$$

Para concretar, tomaremos $w=0.75$, de modo que la función $\psi(x)$ tiene la forma mostrada en la figura 6.2.

![Figura 6.2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh6_ES/fig6.2.png)

Figura 6.2: la función $\psi(x)$ para $w=0.75$ — un triángulo asimétrico que sube linealmente desde $(0,0)$ hasta $(0.75,0.75)$ y baja linealmente hasta $(1,0)$.

Calculamos los coeficientes de Fourier usando (6.10). Como $\ell=1$, esto toma la siguiente forma (véase el problema 6.2):

$$c_n = \int_0^1 dx\,\sin n\pi x\,\psi(x) = \int_0^w dx\,x\sin n\pi x + \int_w^1 dx\,\frac{w(1-x)}{1-w}\sin n\pi x = \frac{\sin n\pi w}{(1-w)n^2\pi^2}\,. \qquad \text{(6.20)}$$

Podemos reconstruir la función, $\psi(x)$, como una suma sobre los modos normales de la cuerda. Veamos los primeros términos de la serie para hacernos una idea de cómo funciona esto. El primer término de la suma, para $w=0.75$, se muestra en la figura 6.3. Esta es necesariamente una mala aproximación, porque la función no es simétrica respecto a $x=1/2$, mientras que el primer término de la suma sí lo es. Los dos primeros términos se muestran en la figura 6.4; esto se ve mucho mejor.

![Figura 6.4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh6_ES/fig6.4.png)

Figura 6.4

![Figura 6.3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh6_ES/fig6.3.png)

Figura 6.3:-6.5: aproximaciones sucesivas de $\psi(x)$ mediante 1, 2 y 6 términos de la serie de Fourier, respectivamente, comparadas con la función triangular original mostrada con línea punteada; la aproximación mejora progresivamente salvo cerca del pico angular.

Los primeros seis términos se muestran en la figura 6.5. Esta es ya una muy buena aproximación, salvo donde la función tiene un pico angular.

Lo que ocurre aquí es que, si incluimos términos de la serie de Fourier solo hasta $n=N$, podemos ver cómo funciona esto con más detalle estudiando la figura 6.6. La curva de trazos largos es el primer término de la serie de Fourier. Evidentemente, es menor que la función $\psi(x)$ (el triángulo punteado) para $x$ grande, y mayor que $\psi(x)$ para $x$ pequeño. El signo y la magnitud del segundo término de la serie de Fourier, la curva de trazos cortos en la figura 6.6, se eligen para compensar esta discrepancia, de modo que la suma (la curva continua) queda mucho más cerca de la función real. El mismo proceso se repite una y otra vez a medida que se avanza a órdenes superiores en la serie de Fourier truncada.

![Figura 6.6](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh6_ES/fig6.6.png)

Figura 6.6: los dos primeros términos de la serie de Fourier de $\psi(x)$ y su suma, mostrando cómo el primer término sobreestima la función para $x$ pequeño y la subestima para $x$ grande, y cómo el segundo término corrige esta discrepancia.

Puede jugar con la serie de Fourier truncada de la función $\psi(x)$ en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-6-3" rel="noopener" target="_blank" title="Animación original de Howard Georgi">6-3</a>. Este programa le permite variar el parámetro $w$, y también el número de términos de la serie de Fourier. Debería observar qué ocurre cerca de $w=1$. Podría pensar que esto causaría problemas para la serie de Fourier, porque el $(1-w)$ del denominador de (6.20) tiende a cero. Sin embargo, el límite en realidad se comporta bien, porque $\sin n\pi w$ también tiende a cero cuando $w\to1$. Sin embargo, la serie de Fourier tiene que «trabajar duro» para $w=1$, para reproducir una función que no se anula en $x=1$ como suma de funciones seno, cada una de las cuales sí se anula en $x=1$. Esta dificultad se refleja en las oscilaciones cerca de $x=1$ para cualquier número razonable de términos en la serie de Fourier.

### 6.2.4 Pulsar una cuerda

*(Referencia a los programas interactivos 6-4 y 6-5 del disco de programas del curso original.)*

Usemos ahora estas matemáticas para resolver un problema de física. Resolveremos el problema de valores iniciales para la cuerda con extremo fijo, para una forma inicial concreta. El problema de valores iniciales aquí es casi exactamente igual al discutido en el capítulo 3, (3.98)-(3.100), para un sistema con un número finito de grados de libertad. La única diferencia es que ahora, como el número de grados de libertad es infinito, la suma sobre modos llega hasta el infinito. No debería preocuparse por el hecho de que el número de modos sea infinito: lo que ese «infinito» realmente significa es «más grande que cualquier número que nos vaya a importar». En la práctica, como vimos en los ejemplos anteriores, los modos superiores eventualmente no marcan mucha diferencia; están asociados a rasgos cada vez más pequeños de la forma. Cuando decimos que el sistema es continuo y que tiene un número infinito de grados de libertad, en realidad estamos suponiendo que los rasgos más pequeños que nos importan en las ondas siguen siendo mucho mayores que la distancia entre las partes del sistema, de modo que podemos truncar nuestra serie de Fourier muy por debajo del límite y aun así tener una buena descripción aproximada del movimiento.

Supongamos que pulsamos la cuerda. Concretamente, supongamos que la cuerda tiene densidad de masa lineal $\rho_L$, tensión $T$, y extremos fijos en $x=0$ y $\ell$. Supongamos además que en $t=0$ la cuerda está en reposo, pero desplazada de su posición de equilibrio hacia la forma $\psi(x)$ dada por (6.19). Si la cuerda se suelta entonces en $t=0$, podemos encontrar el movimiento posterior sumando sobre todos los modos normales con coeficientes fijos multiplicados por $\cos\omega_nt$ y/o $\sin\omega_nt$, donde $\omega_n$ es la frecuencia del modo $\sin(n\pi x/\ell)$, con $k=n\pi/\ell$ (la frecuencia viene dada por (6.5)):

$$\omega_n = \sqrt{\frac{T}{\rho_L}}\,k_n = \sqrt{\frac{T}{\rho_L}}\,\frac{n\pi}{\ell}\,. \qquad \text{(6.22)}$$

En este caso, solo aparecen los términos en $\cos\omega_nt$, porque la velocidad es cero en $t=0$. Así, podemos escribir

$$\psi(x,t) = \sum_{n=1}^{\infty}c_n\sin\frac{n\pi x}{\ell}\cos\omega_nt\,. \qquad \text{(6.23)}$$

Esto satisface las condiciones de contorno en $t=0$, en virtud de la serie de Fourier, (6.8). La desventaja de (6.23) es que nos queda una suma infinita. Para la relación de dispersión simple, (6.5), hay otras formas de resolver este problema, que discutiremos más adelante cuando estudiemos las ondas viajeras. Sin embargo, la ventaja de la solución (6.23) es que no depende de la relación de dispersión.

Podemos resolver el problema aproximadamente usando (6.23), sumando solo los primeros términos de la serie. El ordenador puede hacer esto rápidamente. En el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-6-4" rel="noopener" target="_blank" title="Animación original de Howard Georgi">6-4</a> se muestran los primeros veinte términos de la serie, para $w=1/2$ (y con la relación de dispersión todavía dada por (6.5)). El resultado es sorprendentemente simple; ¡compruébelo! El programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-6-5" rel="noopener" target="_blank" title="Animación original de Howard Georgi">6-5</a> sigue la misma idea, pero le permite variar $w$ y el número de términos de la serie de Fourier. Pruebe con $w=0.75$ y compare con las figuras 6.3-6.5.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Tomar el límite de un sistema discreto invariante bajo traslación espacial cuando la distancia entre las partes tiende a cero, interpretar la física del sistema continuo resultante, y encontrar su relación de dispersión;

2.  Usar la serie de Fourier para plantear y resolver el problema de valores iniciales de una cuerda masiva con diversas condiciones de contorno.

## Problemas

**6.1.** Considere la cuerda continua de (6.7)-(6.10) como el límite continuo de una cuerda con cuentas de $W$ cuentas, cuando $W\to\infty$. Escriba el análogo de (6.8) y (6.10) para $W$ finito. Demuestre que el límite cuando $W\to\infty$ da (6.10). Pista: esto es un ejercicio sobre la definición de una integral como límite de una suma. Pero para hacer la primera parte, necesitará usar coordenadas normales, o demostrar la identidad

$$\sum_{k=1}^{W}\sin\frac{nk\pi}{W+1}\sin\frac{n'k\pi}{W+1} = \begin{cases} b & \text{si } n=n'\neq0\\ 0 & \text{si } n\neq n' \text{ y } n,n'>0 \end{cases}$$

para una constante $b$, y encuentre $b$.

**6.2.** Haga las integrales de (6.20). Pista: use integración por partes y esté atento a cancelaciones milagrosas.

**6.3.** Encuentre los modos normales de la cuerda con dos extremos libres, mostrada en la figura 6.7.

![Figura 6.7](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh6_ES/fig6.7.png)

Figura 6.7: cuerda continua con ambos extremos, en $x=0$ y $x=\ell$, unidos a anillos sin masa que deslizan libremente sobre varillas sin fricción perpendiculares a la cuerda.

**6.4.** Diversión con series de Fourier y fractales

En este problema explorará la serie de Fourier de un conjunto interesante de funciones. Considere una función de la siguiente forma, definida en el intervalo $[0,1]$:

$$f(t) = \sum_{j=0}^{\infty}h^j\,g(\text{frac}(2^jt))\,.$$

donde

$$g(t) = \begin{cases} 1 & \text{para } 0\le t\le w\\ 0 & \text{para } w<t<1-w\\ 1 & \text{para } 1-w\le t\le1 \end{cases}$$

y $\text{frac}(x)$ denota la parte fraccionaria, es decir, $\text{frac}(4.39)=0.39$. Así, $f(t)$ depende de los dos parámetros $h$ y $w$, donde $0<h<1$ y $0<w<1/2$. Por ejemplo, para $h=1/2$ y $w=1/4$, el término $h^0$ se muestra en la figura 6.8.

![Figura 6.8](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh6_ES/fig6.8.png)

Figura 6.8: el término $h^0$ de $f(t)$ para $h=1/2$, $w=1/4$ — una onda cuadrada de altura 2 con “mesetas” de anchura $w$ en cada extremo del intervalo $[0,1]$, unidas por rampas lineales.

Si añadimos el término $h^1$ obtenemos la figura 6.9, y añadiendo el término $h^2$ obtenemos la figura 6.10, y así sucesivamente.

![Figura 6.9](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh6_ES/fig6.9.png)

Figura 6.9 y 6.10: sumas parciales de $f(t)$ incluyendo los términos $h^0+h^1$ y $h^0+h^1+h^2$ respectivamente, mostrando una estructura cada vez más fina y autosimilar, típica de un fractal.

El resultado final es una función muy accidentada, llamada «fractal». No se puede calcular esta función exactamente, pero se pueden incluir suficientes términos para alcanzar cualquier precisión deseada. Como la función es simétrica respecto a $t=1/2$, en realidad solo es necesario graficarla de 0 a 1/2. También, debido a la simetría, puede expresarse mediante una serie de Fourier de cosenos,

$$f(t) = \sum_{k=0}^{\infty}b_k\cos2\pi kt\,.$$

Demuestre que los coeficientes de Fourier vienen dados por

$$b_k = \frac{2}{\pi k}\sum_{j=0}^{\xi(k)}(2h)^j\sin(2\pi kw/2^j)$$

para $k\neq0$, y

$$b_0 = \frac{2w}{1-h}$$

donde la función $\xi(k)$ es el número de veces que el 2 aparece como factor de $k$. Así, $\xi(0)=\xi(1)=\xi(3)=0$, $\xi(2)=1$, $\xi(4)=2$, etc.

Escriba un programa que muestre e imprima el fractal para cierto conjunto de parámetros $h$ y $w$. Muestre también la serie de Fourier truncada,

$$f_m(t) = \sum_{k=0}^{m-1}b_k\cos2\pi kt$$

con $m$ términos, para $m=5$, 10 y 20 (o más, si dispone de un ordenador rápido).

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.


---

<!-- MIT8.03_TextCh7_ES.md -->

# Capítulo 7: Oscilaciones longitudinales y sonido

Las oscilaciones transversales de un sistema continuo son fáciles de visualizar, porque se puede ver directamente la función que describe el desplazamiento. Las matemáticas de las oscilaciones longitudinales de un sistema continuo, lineal e invariante bajo traslación espacial son las mismas. Deben serlo, porque quedan completamente determinadas por la invariancia bajo traslación espacial. Pero la física es distinta.

## Vídeos de esta clase (YouTube)

- [Clase 10: Ondas viajeras](https://www.youtube.com/watch?v=SnNmbVH5DAM)
- [Clase 11: Ondas sonoras](https://www.youtube.com/watch?v=RhIh1zw0-BM)

## Resumen previo

En este capítulo introducimos dos sistemas físicos con oscilaciones longitudinales: muelles masivos y tubos de órgano.

1.  Describimos el muelle masivo como el límite continuo de un sistema de masas conectadas por muelles sin masa, y estudiamos sus modos normales para diversas condiciones de contorno.

2.  Discutimos con cierto detalle el sistema de una masa en el extremo de un muelle masivo. Cuando el muelle es «ligero», este es un ejemplo importante de física con dos «escalas» distintas.

3.  Discutimos la física de las ondas sonoras en un tubo, por analogía con las oscilaciones del muelle masivo. También introducimos la aproximación de «Helmholtz» para el modo más bajo de una botella.

## 7.1 Modos longitudinales en un muelle masivo

Hasta ahora, en nuestras extensas discusiones sobre ondas en sistemas de muelles y bloques, hemos supuesto que los únicos grados de libertad son los asociados al movimiento de los bloques. Esta es una suposición razonable a bajas frecuencias, cuando los bloques son muy pesados comparados con los muelles, porque los bloques se mueven tan lentamente que los muelles tienen tiempo de reajustarse y son siempre casi uniformes (lo formalizaremos más abajo). En este caso, la relación de dispersión de las oscilaciones longitudinales de los bloques es justamente la relación de dispersión de los péndulos acoplados, (5.35), en el límite en que ignoramos la gravedad y conservamos solo el acoplamiento entre las masas producido por la constante del muelle, $K$. En otras palabras, tomamos el límite de (5.35) cuando $g/\ell\to0$. El resultado puede escribirse como

$$\omega^2 = \frac{4K_a}{m}\sin^2\frac{ka}{2} \qquad \text{(7.1)}$$

donde $K_a$ es la constante de los muelles, $m$ es la masa de los bloques, y $a$ es la separación de equilibrio. Hemos puesto un subíndice $a$ en $K_a$ porque querremos variar la constante del muelle a medida que variamos la separación entre los bloques en la discusión que sigue.

Ahora bien, ¿qué ocurre cuando los bloques desaparecen, pero el muelle es masivo? Podemos averiguarlo considerando el límite de (7.1) cuando $a\to0$. En este límite, los bloques masivos y el muelle sin masa se funden entre sí, de modo que el resultado se parece a un muelle uniforme y masivo. Para tomar el límite, sin embargo, debemos entender qué variables describen el muelle masivo y tienen un límite finito cuando $a\to0$. Una de esas variables es la densidad de masa lineal,

$$\rho_L = \lim_{a\to0}\frac{m}{a}\,. \qquad \text{(7.2)}$$

Debemos hacer que las masas de los bloques tiendan a cero cuando $a\to0$, para mantener $\rho_L$ finita.

Para entender qué le ocurre a $K_a$ cuando $a\to0$, considere qué pasa cuando corta un muelle por la mitad. Cuando un muelle se estira, cada mitad contribuye la mitad del desplazamiento. Pero la tensión es uniforme a lo largo de todo el muelle estirado. Así, la constante de media muelle es el doble de la del muelle completo, porque la mitad del desplazamiento da la misma fuerza. Esta relación se ilustra en la figura 7.1. El muelle central no está estirado. El muelle de arriba está estirado una cantidad $x$ hacia la derecha. Abajo se muestra el mismo muelle estirado, todavía estirado $x$, pero ahora simétricamente. Comparando arriba y abajo, puede ver que la fuerza de retorno de estirar el muelle una cantidad $x$ es la misma que la de estirar media muelle una cantidad $x/2$.

![Figura 7.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh7_ES/fig7.1.png)

Figura 7.1: arriba, un muelle completo estirado una cantidad $x$ hacia la derecha; abajo, el mismo muelle dividido en dos mitades, cada una estirada simétricamente una cantidad $x/2$, mostrando que la fuerza de retorno es la misma.

El diagrama de la figura 7.1 es un ejemplo del siguiente resultado. En general, la constante de muelle, $K_a$, no depende solo de qué está hecho el muelle, sino de cuán largo es. Pero la cantidad $K_aa$, donde $a$ es la longitud del muelle, es en realidad independiente de $a$, para un muelle hecho de material uniforme. Así, deberíamos tomar el límite $a\to0$ manteniendo $K_aa$ fijo.

Esto implica que la relación de dispersión del muelle masivo es

$$\omega^2 = \frac{K_aa}{\rho_L}\,k^2\,, \qquad \text{(7.3)}$$

donde hemos usado el desarrollo en serie de Taylor de $\sin x$, (1.58), y conservado solo el primer término. Según la discusión anterior, podemos reescribir esto como

$$\omega^2 = \frac{K\ell}{\rho_L}\,k^2 \qquad \text{(7.4)}$$

donde $\ell$ es la longitud del muelle y $K$ es la constante del muelle completo.

Note que, en las oscilaciones longitudinales de un material continuo en la dirección $x$, la posición de equilibrio, $x$, en realidad no describe la posición $x$ del material. Como el desplazamiento es longitudinal, la posición $x$ real del punto del muelle con posición de equilibrio $x$ es

$$x+\psi(x,t)\,, \qquad \text{(7.5)}$$

donde $\psi$ es el desplazamiento. Necesitará esto para el problema 7.1.

### 7.1.1 Extremos fijos

*(Referencia al programa interactivo 7-1 del disco de programas del curso original.)*

Suponga que tenemos un muelle masivo de longitud $\ell$, con sus extremos fijos en $x=0$ y $x=\ell$. Entonces el desplazamiento, $\psi(x,t)$, debe anularse en los extremos,

$$\psi(0,t)=0\,,\qquad \psi(\ell,t)=0\,. \qquad \text{(7.6)}$$

Los modos del sistema son los mismos que para cualquier otro sistema invariante bajo traslación espacial. Las combinaciones lineales de los modos exponenciales complejos del sistema infinito que satisfacen (7.6) son

$$A_n(x) = \sin\frac{n\pi x}{\ell}\,, \qquad \text{(7.7)}$$

con número de onda angular

$$k_n = \frac{n\pi}{\ell} \qquad \text{(7.8)}$$

y frecuencia (a partir de la relación de dispersión, (7.4))

$$\omega_n = \sqrt{\frac{K\ell}{\rho_L}}\,k_n = \sqrt{\frac{K\ell}{\rho_L}}\,\frac{n\pi}{\ell}\,. \qquad \text{(7.9)}$$

Sin embargo, como las oscilaciones son longitudinales, los modos se ven muy distintos de los modos transversales de la cuerda que estudiamos en el capítulo anterior. La posición del punto de la cuerda cuya posición de equilibrio es $x$, en el $n$-ésimo modo normal, tiene la forma general (de (7.5))

$$x + \epsilon\sin\frac{n\pi x}{\ell}\cos(\omega_nt+\varphi) \qquad \text{(7.10)}$$

donde $\epsilon$ y $\varphi$ son la amplitud y la fase de la oscilación.

Los nueve modos más bajos de (7.10) se animan en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-7-1" rel="noopener" target="_blank" title="Animación original de Howard Georgi">7-1</a>. Compárelos con los modos animados en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-6-1" rel="noopener" target="_blank" title="Animación original de Howard Georgi">6-1</a>. Las matemáticas son las mismas, pero la física es muy distinta, debido a (7.5). Observe con atención estas dos animaciones hasta que pueda visualizar la relación entre ambas: entonces habrá entendido (7.5).

### 7.1.2 Extremos libres

*(Referencia al programa interactivo 7-2 del disco de programas del curso original.)*

Consideremos ahora la situación en la que el extremo del muelle en $x=0$ está fijo, pero el extremo en $x=\ell$ es libre. Las condiciones de contorno en este caso son análogas a las de los modos normales de la cuerda con un extremo fijo. El desplazamiento en $x=0$ debe anularse porque ese extremo está fijo. Además, la derivada del desplazamiento en $x=\ell$ debe anularse. Puede verlo considerando el muelle continuo como el límite de masas discretas acopladas por muelles. Como vimos en (5.43), la última masa real debe tener el mismo desplazamiento que la primera masa «imaginaria»,

$$\psi(\ell,t) = \psi(\ell+a,t)\,. \qquad \text{(7.11)}$$

Por tanto, para el sistema finito con un extremo libre en $\ell$, tenemos la relación

$$\frac{\psi(\ell,t)-\psi(\ell+a,t)}{a} = 0 \quad\text{para todo } a\,. \qquad \text{(7.12)}$$

En el límite en que la distancia entre masas tiende a cero, esto se convierte en la condición de que la derivada del desplazamiento, $\psi$, respecto a $x$ se anule en $x=\ell$,

$$\left.\frac{\partial}{\partial x}\psi(x,t)\right|_{x=\ell} = 0\,. \qquad \text{(7.13)}$$

Así, las condiciones de contorno para el desplazamiento son las mismas que en (6.11), para la oscilación transversal de una cuerda continua con $x=0$ fijo y $x=\ell$ libre,

$$\psi(0,t)=0\,,\qquad \left.\frac{\partial}{\partial x}\psi(x,t)\right|_{x=\ell}=0\,. \qquad \text{(7.14)}$$

Esto, a su vez, implica que los modos normales son los mismos que para la cuerda oscilando transversalmente, (6.15),

$$A_n(x) = \sin\left(\frac{(2n+1)\pi x}{2\ell}\right) \quad\text{para } n=0\text{ a }\infty\,. \qquad \text{(7.15)}$$

Sin embargo, de nuevo debido a (7.5), estos modos se ven muy distintos de los de la cuerda. Los primeros nueve se animan en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-7-2" rel="noopener" target="_blank" title="Animación original de Howard Georgi">7-2</a> (compárese con el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-6-2" rel="noopener" target="_blank" title="Animación original de Howard Georgi">6-2</a>).

## 7.2 Una masa sobre un muelle ligero

Volvamos al sistema que estudiamos al principio mismo del libro, el oscilador armónico construido colocando una masa en el extremo de un muelle ligero. Ahora estamos en posición de entender con precisión qué significa «ligero» para este sistema, porque ahora podemos permitir que el muelle tenga una densidad de masa lineal no nula, $\rho_L$, y encontrar los modos normales de este sistema. Después podremos ver qué ocurre cuando $\rho_L\to0$.

Para concretar, considere un muelle con longitud de equilibrio $\ell$ y constante $K$, fijo en $x=0$ y obligado a oscilar solo en la dirección $x$ (es decir, longitudinalmente). Ahora una una masa, $m$, al extremo libre (con posición de equilibrio $x=\ell$). El muelle, para $0<x<\ell$, puede considerarse parte de un sistema invariante bajo traslación espacial. Para encontrar los modos normales de este sistema, buscamos una combinación lineal de los modos del muelle infinito (para un $\omega$ dado) que reproduzca la física en $x=0$ y $x=\ell$. El extremo fijo en $x=0$ es fácil: fija la forma de los modos para que sean proporcionales a

$$\sin k_nx \qquad \text{(7.16)}$$

con frecuencia

$$\omega_n = \sqrt{\frac{K\ell}{\rho_L}}\,k_n\,. \qquad \text{(7.17)}$$

Como siempre, $k_n$ y $\omega_n$ están relacionados por la relación de dispersión, (7.4). Ahora, para determinar los posibles valores de $k_n$, exigimos que se satisfaga $F=ma$ para la masa. Suponga, por ejemplo, que la amplitud de la oscilación es $A$ (una longitud). Entonces el desplazamiento del punto del muelle con posición de equilibrio $x$ es

$$\psi(x,t) = A\sin k_nx\cos\omega_nt\,, \qquad \text{(7.18)}$$

y el desplazamiento de la masa queda determinado por el desplazamiento del extremo del muelle,

$$x(t) \equiv \psi(\ell,t) = A\sin k_n\ell\cos\omega_nt\,. \qquad \text{(7.19)}$$

La aceleración es

$$a(t) = \frac{\partial^2}{\partial t^2}\psi(\ell,t) = -\omega_n^2A\sin k_n\ell\cos\omega_nt \qquad \text{(7.20)}$$

![Figura 7.2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh7_ES/fig7.2.png)

Figura 7.2: el estiramiento del último tramo de muelle es $\psi(\ell,t)-\psi(\ell-a,t)$, mostrando el muelle en equilibrio y estirado, con la masa $m$ en el extremo derecho.

Para encontrar la fuerza sobre la masa, considere el muelle masivo como el límite continuo, cuando $a\to0$, de masas conectadas por muelles sin masa de longitud de equilibrio $a$, como al principio del capítulo. Entonces la fuerza sobre la masa del extremo está determinada por el estiramiento del último muelle de la serie. Esto, a su vez, es la diferencia entre el desplazamiento del sistema en $x=\ell$ y en $x=\ell-a$, como se ilustra en la figura 7.2. Así, la fuerza es

$$F = -K_a\left[\psi(\ell,t)-\psi(\ell-a,t)\right]\,. \qquad \text{(7.21)}$$

Para tomar el límite $a\to0$, reescribimos esto como

$$F = -K_aa\,\frac{\psi(\ell,t)-\psi(\ell-a,t)}{a}\,. \qquad \text{(7.22)}$$

Ahora, en el límite continuo, $K_aa$ es $K\ell$, y el último factor tiende a una derivada, $\partial\psi(x,t)/\partial x|_{x=\ell}$. El resultado final para la fuerza es, por tanto (note que esto también da una deducción alternativa de la condición de contorno para un extremo libre, (7.14)):

$$F = -K\ell\,\left.\frac{\partial}{\partial x}\psi(x,t)\right|_{x=\ell} = -K\ell\,k_nA\cos k_n\ell\cos\omega_nt\,. \qquad \text{(7.23)}$$

Note que las unidades cuadran: $K\ell$ es una fuerza, y $\partial\psi/\partial x$ es adimensional.

Sustituyendo (7.20) y (7.23) en $F=ma$, y cancelando un factor $-A\cos\omega_nt$ en ambos lados, obtenemos

$$K\ell\,k_n\cos k_n\ell = m\omega_n^2\sin k_n\ell\,. \qquad \text{(7.24)}$$

Usando la relación de dispersión para eliminar $\omega_n^2$, obtenemos

$$k_n\ell\tan k_n\ell = \frac{\rho_L\ell}{m}\,. \qquad \text{(7.25)}$$

Hemos multiplicado ambos lados de (7.25) por $\ell$ para trabajar con la variable adimensional $k_n\ell$ (que es $2\pi$ veces el número de longitudes de onda que caben en el muelle) y el número adimensional

$$\epsilon \equiv \frac{\rho_L\ell}{m} \qquad \text{(7.26)}$$

(que es el cociente entre la masa del muelle, $\rho_L\ell$, y la masa $m$). El muelle es ligero si $\epsilon$ es mucho menor que uno.

El punto importante es que (7.25) tiene una única solución para $k_n\ell$ que tiende a cero cuando $\epsilon\to0$. Como $\tan k\ell\approx k\ell$ para $k\ell$ pequeño, es

$$k_0\ell \approx \sqrt\epsilon\,. \qquad \text{(7.27)}$$

Para todas las demás soluciones, la pequeñez del lado izquierdo de (7.25) debe provenir de que $\tan k_n\ell$ sea muy pequeño,

$$k_n\ell \approx n\pi \quad\text{para } n=1\text{ a }\infty\,. \qquad \text{(7.28)}$$

Pero (7.28) implica

$$x(t) \equiv \psi(\ell,t) = A\sin k_n\ell\cos\omega_nt \approx 0 \quad\text{para } n=1\text{ a }\infty\,. \qquad \text{(7.29)}$$

En otras palabras, en todas las soluciones excepto $k_0$, la masa apenas se mueve, y es el muelle el que hace casi toda la oscilación, pareciéndose mucho a un sistema con dos extremos fijos. Además, las frecuencias de todos los modos, salvo el modo $k_0$, son grandes,

$$\omega_n \approx n\pi\sqrt{\frac{K}{\rho_L\ell}} \quad\text{para } n=1\text{ a }\infty\,, \qquad \text{(7.30)}$$

mientras que la frecuencia del modo $k_0$ es

$$\omega_0 \approx \sqrt{\frac{K}{m}}\,. \qquad \text{(7.31)}$$

Para $\epsilon$ pequeño (masa grande), el modo $k_0$ está asociado principalmente a la oscilación de la masa, y tiene aproximadamente la frecuencia que encontramos para el caso del muelle sin masa. Los demás modos están en un rango de frecuencias completamente distinto: están asociados a las oscilaciones del muelle. Este es un ejemplo importante de cómo un único sistema puede comportarse de formas muy distintas en diferentes regímenes de frecuencia.

## 7.3 La velocidad del sonido

![Figura 7.3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh7_ES/fig7.3.png)

Figura 7.3: tubo de órgano vertical, de longitud $z=0$ a $z=\ell$.

La física de las ondas sonoras es obviamente un problema tridimensional. Sin embargo, podemos aprender mucho sobre el sonido considerando el movimiento del aire en una sola dimensión. Considere, por ejemplo, ondas estacionarias en el aire de un tubo largo y estrecho, como un tubo de órgano, mostrado esquemáticamente en la figura 7.3. Aquí ignoraremos el movimiento del aire perpendicular a la longitud del tubo, y consideraremos solo el movimiento unidimensional a lo largo del tubo. Como veremos más adelante, cuando podamos tratar problemas tridimensionales, esto es razonable a bajas frecuencias, para las que no pueden excitarse los modos transversales de oscilación. Si consideramos solo el movimiento unidimensional, podemos trazar una analogía entre las oscilaciones del aire en el tubo y las ondas longitudinales en un muelle masivo.

Está claro cuál es el análogo de $\rho_L$: la densidad de masa lineal del aire en el tubo es

$$\rho_L = \rho A \qquad \text{(7.32)}$$

donde $A$ es el área de la sección transversal del tubo. La pregunta entonces es: ¿cuál es $K\ell$ para un tubo de aire?

Considere colocar un pistón en la parte superior del tubo, como se muestra en la figura 7.4. Con el pistón en la parte superior, no hay fuerza sobre él, porque la presión del aire en el tubo es igual a la presión del aire de la habitación exterior. Sin embargo, si el pistón se empuja hacia adentro una distancia $dz$, como se muestra en la figura 7.5, el volumen del aire en el tubo disminuye en

$$-dV = A\,dz\,. \qquad \text{(7.33)}$$

![Figura 7.4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh7_ES/fig7.4.png)

Figura 7.4 y 7.5: el tubo de órgano con un pistón en la parte superior; el aire del tubo actúa como un muelle; al empujar el pistón hacia adentro una distancia $dz$, cambia el volumen del aire encerrado.

Si el pistón se moviera lo bastante despacio como para que la temperatura del gas se mantuviera constante, entonces la presión sería simplemente inversamente proporcional al volumen. Sin embargo, en una onda sonora, el movimiento del aire es tan rápido que casi no hay tiempo para que fluya calor dentro o fuera del sistema. Tal cambio de volumen se llama «adiabático». Cuando el volumen disminuye adiabáticamente, la temperatura sube (porque la fuerza sobre el pistón realiza trabajo) y la presión aumenta más rápido que $1/V$, como

$$p \propto V^{-\gamma} \qquad \text{(7.34)}$$

donde $\gamma$ es una constante positiva que depende de las propiedades termodinámicas del gas. Más precisamente, $\gamma$ es el cociente entre el calor específico a presión constante y el calor específico a volumen constante (véase, por ejemplo, Halliday y Resnick):

$$\gamma = C_P/C_V \qquad \text{(7.35)}$$

En el aire, en condiciones normales de temperatura y presión,

$$\gamma_{\text{aire}} \approx 1.40\,. \qquad \text{(7.36)}$$

Ahora podemos escribir, a partir de (7.34),

$$\frac{dp}{p} = -\gamma\,\frac{dV}{V} \qquad \text{(7.37)}$$

o

$$dp = -\gamma p\,\frac{dV}{V} \approx \frac{\gamma A\,p_0}{V}\,dz = \frac{\gamma p_0}{\ell}\,dz \qquad \text{(7.38)}$$

donde $p_0$ es la presión de equilibrio (ambiente). Entonces la fuerza sobre el pistón es

$$dF = A\,dp = \frac{\gamma A^2p_0}{V}\,dz = \frac{\gamma A p_0}{\ell}\,dz \qquad \text{(7.39)}$$

de modo que

$$K = \frac{dF}{dz} = \frac{\gamma A p_0}{\ell} \qquad \text{(7.40)}$$

y $K\ell$ es

$$K\ell = \gamma A p_0\,. \qquad \text{(7.41)}$$

Así, esperamos que la relación de dispersión sea

$$\omega^2 = v_{\text{sonido}}^2k^2 = \frac{K\ell}{\rho_L}\,k^2 = \frac{\gamma p_0}{\rho}\,k^2 \qquad \text{(7.42)}$$

donde hemos definido la «velocidad del sonido», $v_{\text{sonido}}$, como

$$v_{\text{sonido}}^2 = \frac{\gamma p_0}{\rho}\,. \qquad \text{(7.43)}$$

Para el aire en condiciones normales de temperatura y presión,

$$v_{\text{sonido}} \approx 332\ \frac{\text{m}}{\text{s}}\,. \qquad \text{(7.44)}$$

Como veremos en el próximo capítulo, esta es en realidad la velocidad a la que viajan las ondas sonoras. Por ahora, es simplemente un parámetro en nuestro cálculo de los modos normales.

En el tubo mostrado en la figura 7.3, el desplazamiento del aire, que llamaremos $\psi(z,t)$, debe anularse en $z=0$, porque el fondo del tubo está cerrado y no hay adónde ir para el gas.

La derivada en $z$ de $\psi$ debe anularse en $z=\ell$, porque el exceso de presión es proporcional a $-\partial\psi/\partial z$. La presión es proporcional a la fuerza en nuestra analogía con las ondas longitudinales en el muelle masivo. Usando (7.41) y (7.23), esperamos que la fuerza longitudinal sea

$$\pm\gamma A p_0\,\frac{\partial\psi}{\partial z} \qquad \text{(7.45)}$$

o que el exceso de presión sea

$$p - p_0 = -\gamma p_0\,\frac{\partial\psi}{\partial z}\,. \qquad \text{(7.46)}$$

Queremos el signo negativo porque, para $\partial\psi/\partial z>0$, el aire se está expandiendo y tiene menor presión.

Así, para una onda estacionaria en el tubo de la figura 7.3, esperamos las condiciones de contorno

$$\psi(0,t)=0\,,\qquad \left.\frac{\partial}{\partial z}\psi(z,t)\right|_{z=\ell}=0\,, \qquad \text{(7.47)}$$

para las cuales la solución es

$$\psi(z,t) = \sin kz\cos\omega t \qquad \text{(7.48)}$$

$$k = \frac{(n+1/2)\pi}{\ell}\,,\qquad \omega=vk\,, \qquad \text{(7.49)}$$

donde $v=v_{\text{sonido}}$, para $n$ entero no negativo. En particular, el modo de frecuencia más baja del tubo corresponde a $n=0$,

$$\omega = \frac{v\pi}{2\ell}\,,\qquad \nu = \frac{\omega}{2\pi} = \frac{v}{4\ell}\,. \qquad \text{(7.50)}$$

### 7.3.1 La aproximación de Helmholtz

Consideremos un problema ligeramente distinto. ¿Cuál es el modo de frecuencia más baja de una botella de refresco de un litro, mostrada en la figura 7.6? Un conjunto típico de parámetros es:

$$\begin{aligned}
A &\approx 2.85\ \text{cm}^2\ \text{: área del cuello}\\
\ell &\approx 5.7\ \text{cm}\ \text{: longitud del cuello}\\
L &\approx 25\ \text{cm}\ \text{: longitud de la botella}\\
V_0 &\approx 1000\ \text{cm}^3\ \text{: volumen del cuerpo}
\end{aligned} \qquad \text{(7.51)}$$

![Figura 7.6](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh7_ES/fig7.6.png)

Figura 7.6: botella de refresco de un litro, mostrando el cuello de longitud $\ell$ y el cuerpo de longitud $L$ y volumen $V_0$.

Sustituyendo la longitud, $L$, de la botella en (7.50), da $\nu\approx332$ hercios. En la afinación estándar americana (véase la tabla 7.1), esto es un Mi por encima del Do central.

Esto es obviamente incorrecto. Si alguna vez ha soplado en su botella de refresco, sabe que la frecuencia del modo más bajo es mucho menor que esa. El problema, por supuesto, es que la botella de refresco no tiene ni remotamente la forma de un tubo. Determinar los modos es un complicado problema tridimensional. Resulta, sin embargo, que podemos encontrar el modo más bajo con una aproximación bastante decente, de forma bastante fácil.

La idea es que, en el modo más bajo, el aire del cuello de la botella se mueve rápidamente, pero en el cuerpo de la botella, el aire se dispersa rápidamente, de modo que apenas se mueve. La idea de la aproximación de Helmholtz es tratar el aire del cuello como un único bloque, de masa

$$\rho A\ell\,, \qquad \text{(7.52)}$$

y tratar el cuerpo como un muelle que contribuye fuerza restauradora, pero no inercia (porque el aire apenas se mueve). Entonces todo lo que tenemos que hacer es calcular la $K$ del «muelle». Esto es fácil, usando (7.38). En este caso,

$$dV = A\,dz\,, \qquad \text{(7.53)}$$

así que

$$dp = -\gamma p\,\frac{A\,dz}{V} \approx -\gamma p_0\,\frac{A\,dz}{V_0} \qquad \text{(7.54)}$$

y

$$F \approx -\gamma p_0\,\frac{A^2\,dz}{V_0} \qquad \text{(7.55)}$$

o

$$\text{«}K\text{»} = \gamma p_0\,\frac{A^2}{V_0}\,. \qquad \text{(7.56)}$$

Entonces, usando $\omega^2=K/m$, esperamos

$$\omega = \sqrt{\frac{\gamma A^2p_0/V_0}{\rho A\ell}} = v\sqrt{\frac{A}{\ell V_0}}\,. \qquad \text{(7.57)}$$

Para la botella de refresco, (7.51), esto da

$$\nu \approx 118\ \text{hercios} \qquad \text{(7.58)}$$

o aproximadamente un Si♭ por debajo del Do grave. Esto es bastante correcto (véase el problema 7.5).

### 7.3.2 Correcciones a Helmholtz

Hay muchas correcciones posibles a (7.57) que podrían considerarse. Una es incluir el llamado «efecto de extremo». El punto es que la velocidad del aire en el modo más bajo no cae a cero inmediatamente al pasar los extremos del cuello. Así, la masa real es algo mayor que $\rho A\ell$. Según la experiencia acumulada, se obtiene un mejor resultado reemplazando

$$\ell \to \ell + 0.6\,r \qquad \text{(7.59)}$$

donde $r$ es el radio del cuello.

Aquí discutiremos otra corrección que puede tratarse sistemáticamente usando los métodos de la invariancia bajo traslación espacial y las interacciones locales. Si la botella tiene un cuello largo, probablemente no sea buena idea tratar el aire del cuello como una masa sólida. Además, hay una alternativa simple: una analogía mejor para el cuello es un muelle masivo con $K\ell=\gamma Ap_0$. Como el cuello es un sistema esencialmente unidimensional e invariante bajo traslación espacial, esperamos un desplazamiento de la forma

$$y\cos\frac{\omega z}{v} \qquad \text{(7.60)}$$

en el cuello, donde $z=0$ es el extremo abierto e $y$ es el desplazamiento del aire en $z=0$. Así, donde el cuello se une al cuerpo, el desplazamiento es

$$y\cos\frac{\omega\ell}{v}\,. \qquad \text{(7.61)}$$

La fuerza en este punto, debida a la compresión del aire en el cuello, es (de (7.45))

$$F_{\text{cuello}} = -\gamma Ap_0\,\frac{\partial\psi}{\partial z} = \frac{\gamma Ap_0\,\omega}{v}\,y\sin\frac{\omega\ell}{v}\,. \qquad \text{(7.62)}$$

Esta debe ser el negativo de la fuerza del aire en el cuerpo, a partir de (7.39),

$$-F_{\text{cuerpo}} = \frac{\gamma A^2p_0}{V_0}\,y\cos\frac{\omega\ell}{v}\,, \qquad \text{(7.63)}$$

o

$$\frac{\omega V_0}{Av}\tan\frac{\omega\ell}{v} = 1\,. \qquad \text{(7.64)}$$

Explorará las consecuencias de esto en el problema 7.5.

Este análisis no distingue entre el área de la parte superior y la inferior del cuello. Quizá el área en la parte inferior sea más apropiada: lo que importa es el área en el punto donde la onda del cuello se empalma con el cuerpo, que determina la fuerza por unidad de área en ese punto.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Encontrar el movimiento de un punto de un muelle continuo que oscila longitudinalmente en uno de sus modos normales, para diversas condiciones de contorno;

2.  Resolver los modos normales de un sistema formado por una masa unida a un muelle masivo;

3.  Deducir la relación de dispersión de las ondas sonoras y encontrar los modos normales de las oscilaciones del aire en un tubo;

4.  Usar la aproximación de Helmholtz para estimar la frecuencia del modo más bajo de una botella.

## Problemas

**7.1.** Deduzca (7.45) directamente, considerando el volumen del elemento de aire en el tubo entre $z$ y $z+dz$, y usando (7.38).

**7.2.** Use una analogía con (7.16)-(7.31) para encontrar (¡aproximadamente!) los modos normales y las frecuencias correspondientes del sistema mostrado en la figura 6.1, pero con un anillo masivo, de masa $m$, deslizando sobre la varilla sin fricción.

**7.3.** Un muelle continuo masivo, de masa $m$, longitud $L$ y constante $K$, cuelga verticalmente. El sistema se muestra en reposo, en su configuración de equilibrio, en la figura 7.7. La constante del muelle es grande, satisfaciendo $KL\gg mg$, de modo que la gravedad no desempeña ningún papel importante aquí, salvo mantener el muelle vertical. Suponga ahora que el soporte del que cuelga el muelle se hace subir y bajar, de modo que la parte superior del muelle se mueve verticalmente con desplazamiento $\epsilon\cos\omega t$, como se muestra en la figura 7.8. Encuentre la posición $z$ del extremo inferior del muelle en función del tiempo. Ignore el amortiguamiento.

![Figura 7.7](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh7_ES/fig7.7.png)

Figura 7.7: muelle masivo colgando verticalmente en equilibrio, de $z=0$ a $z=L$. Figura 7.8: el mismo muelle, con el soporte superior moviéndose como $z(t)=L+\epsilon\cos\omega t$ y se pregunta por la posición del extremo inferior.

**7.4.** Un sistema análogo al del problema 7.3 es un tubo de aire con un pistón en la parte superior y el fondo abierto, como se muestra en la figura 7.9. Si el área de la sección transversal del tubo es $A$, ¿cuál es, en este sistema, el análogo de la constante de muelle, $K$, del problema 7.3? Asegúrese de que su respuesta tenga unidades de fuerza por unidad de distancia.

![Figura 7.8](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh7_ES/fig7.8.png)

Figura 7.8

![Figura 7.9](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh7_ES/fig7.9.png)

Figura 7.9: tubo de aire vertical, de $z=0$ (abierto) a $z=L$ (pistón en la parte superior).

**7.5.** EXPERIMENTO PERSONAL — Demuestre que, cuando $\omega\ell/v$ es pequeño, (7.64) se reduce a la aproximación de Helmholtz, (7.57), mientras que para $V_0\approx0$, cuando la botella es todo cuello, se reduce al resultado de los modos de un tubo uniforme con un extremo abierto y otro cerrado, (7.50).

¡Haga el experimento! Busque una selección de al menos cuatro botellas, al menos una de las cuales tenga un cuello muy largo. Mida la frecuencia del modo más bajo de cada una, y describa cómo lo hizo. Para cada botella, tabule lo siguiente (en unidades cgs):

1.  Una descripción (por ejemplo, botella de refresco, 1000 ml)
2.  $A_t$ (el área de la parte superior del cuello)
3.  $A_b$ (el área de la parte inferior del cuello)
4.  $r$ (el radio del cuello)
5.  $\ell$ (la longitud del cuello)
6.  $V_{\text{cuerpo}}$ (el volumen del cuerpo)
7.  $\nu$ (la frecuencia del modo más bajo)
8.  $\omega$ (la frecuencia angular del modo más bajo)
9.  $\omega^2V_0\ell/Av^2$ (=1 en la aproximación de Helmholtz)
10. $(\omega V_0/Av)\tan(\omega\ell/v)$ (=1 en la aproximación (7.64))

Vea si puede apreciar el efecto de extremo, (7.59), o distinguir el área de la parte superior del cuello de la inferior —es decir, vea cuál funciona mejor en (7.57)—. Comente, de la forma más cuantitativa posible, los errores de su experimento y los méritos relativos de las expresiones aproximadas que ha puesto a prueba.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.


---

<!-- MIT8.03_TextCh8_ES.md -->

# Capítulo 8: Ondas viajeras

En este capítulo mostramos cómo la misma física que da lugar a las oscilaciones de onda estacionaria también origina ondas que se mueven tanto en el espacio como en el tiempo. Después pasamos a introducir el importante ejemplo físico de las ondas de luz.

## Vídeos de esta clase (YouTube)

- [Clase 12: Ecuaciones de Maxwell, ondas electromagnéticas](https://www.youtube.com/watch?v=8kcvyoHsXrw)
- [Clase 13: Medio dispersivo, velocidad de fase, velocidad de grupo](https://www.youtube.com/watch?v=QxemLb8-5AA)

## Resumen previo

En un sistema infinito invariante bajo traslación, las ondas viajeras surgen de forma natural a partir del comportamiento exponencial complejo de las soluciones en el espacio y el tiempo.

1.  Empezamos mostrando la conexión entre las ondas estacionarias y las ondas viajeras en sistemas infinitos. Una onda viajera en un sistema lineal es un par de ondas estacionarias combinadas con una relación de fase especial. Mostramos cómo pueden producirse ondas viajeras en sistemas finitos mediante oscilaciones forzadas apropiadas.

2.  A continuación discutimos la fuerza y la potencia necesarias para producir una onda viajera en una cuerda, e introducimos la útil idea de «impedancia».

3.  Introducimos y discutimos el ejemplo clásico más importante de fenómeno ondulatorio: las ondas electromagnéticas y la luz.

4.  Reexaminamos los sistemas invariantes bajo traslación de circuitos LC acoplados discutidos en el capítulo 5, y mostramos cómo se relacionan con las ondas electromagnéticas.

5.  Discutimos los efectos del amortiguamiento en sistemas invariantes bajo traslación, dando una interpretación física simple del efecto en las ondas viajeras.

6.  Discutimos las ondas viajeras en sistemas con amortiguamiento y en sistemas con cortes de frecuencia altos y/o bajos.

## 8.1 Ondas estacionarias y viajeras

### 8.1.1 ¿Qué es lo que se mueve?

*(Referencia al programa interactivo 8-1 del disco de programas del curso original.)*

Hemos visto que un sistema infinito con invariancia bajo traslación tiene soluciones complejas de la forma

$$e^{\pm ikx}e^{\pm i\omega t}\,, \qquad \text{(8.1)}$$

donde $k$ y $\omega$ están relacionados por la relación de dispersión característica del sistema. Hasta ahora hemos considerado soluciones de onda estacionaria en las que los factores espacial y temporal son cada uno real por separado, es decir,

$$\sin kx\cdot\cos\omega t \propto (e^{ikx}-e^{-ikx})\cdot(e^{i\omega t}+e^{-i\omega t})\,. \qquad \text{(8.2)}$$

Pero podemos combinar las mismas soluciones de otra manera,

$$\psi(x,t) = \cos(kx-\omega t) \propto (e^{ikx}e^{-i\omega t}+e^{-ikx}e^{i\omega t})\,. \qquad \text{(8.3)}$$

Esto se llama una «onda viajera». El sistema subyacente que sostiene la onda no se está moviendo en realidad; lo que se mueve es la onda misma. Si seguimos el punto $x$ para el cual $\psi(x,t)$ tiene cierto valor constante, ese punto se mueve en la dirección $x$ positiva con velocidad constante, llamada la «velocidad de fase»,

$$v_\varphi = \omega(k)/k\,. \qquad \text{(8.4)}$$

En (8.3), por ejemplo, $\psi(x,t)$ vale uno para $x=t=0$, porque el argumento del coseno es cero (también vale uno para $x=2n\pi/k$, para cualquier entero $n$, pero nos centraremos en el único punto $x=0$). A medida que $t$ aumenta, este punto se mueve en la dirección $x$ positiva, porque el argumento del coseno, $kx-\omega t$, se anula para $x=\omega t/k=v_\varphi t$. Esto se ilustra en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-1" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-1</a>.

Seguiremos definiendo todos los modos reales como las partes reales de modos complejos proporcionales a $e^{-i\omega t}$. Así, (8.3) es

$$\cos(kx-\omega t) = \text{Re}\left[e^{ikx}e^{-i\omega t}\right]\,. \qquad \text{(8.5)}$$

En esta notación, una onda que viaja hacia la izquierda es

$$\cos(kx+\omega t) = \text{Re}\left[e^{-ikx}e^{-i\omega t}\right]\,, \qquad \text{(8.6)}$$

mientras que una onda estacionaria es

$$\cos kx\cos\omega t = \frac{1}{2}\text{Re}\left[e^{ikx}e^{-i\omega t}+e^{-ikx}e^{-i\omega t}\right] = \frac{1}{2}\left[\cos(kx-\omega t)+\cos(kx+\omega t)\right]\,. \qquad \text{(8.7)}$$

¡Una onda estacionaria es una combinación de ondas viajeras en direcciones opuestas! Del mismo modo, una onda viajera es una combinación de ondas estacionarias. Por ejemplo,

$$\cos(kx-\omega t) = \cos kx\cos\omega t + \sin kx\sin\omega t\,. \qquad \text{(8.8)}$$

Estas relaciones son importantes porque muestran que la relación entre $k$ y $\omega$, la relación de dispersión, ¡es exactamente la misma para las ondas viajeras que para las ondas estacionarias! Una onda es una onda, viaje o esté estacionaria. De hecho, podemos ir y venir usando (8.7) y (8.8). La relación de dispersión que vincula $k$ y $\omega$ es una propiedad del sistema en el que existen las ondas, no de la onda particular.

El reverso de esta moneda es que las ondas viajeras existen para sistemas con cualquier relación de dispersión. Conocer la velocidad de fase, (8.4), para todo $k$, es equivalente a conocer la relación de dispersión, porque hay que conocer $\omega(k)$. En particular, solo para sistemas continuos simples, como la cuerda estirada (véase (6.5)), $\omega(k)$ es proporcional a $k$ y la velocidad de fase es una constante, independiente de $k$.

### 8.1.2 Condiciones de contorno

*(Referencia al programa interactivo 8-2 del disco de programas del curso original.)*

Las ondas viajeras pueden producirse en sistemas finitos mediante oscilación forzada con una fase apropiada de las oscilaciones en los dos extremos. Un ejemplo simple involucra una cuerda estirada con tensión $T$ y densidad de masa lineal $\rho$. Dadas condiciones de contorno sobre el sistema tales que

$$\psi(0,t)=A\cos\omega t\,,\qquad \psi(L,t)=A\sin\omega t\,, \qquad \text{(8.9)}$$

donde $L$ es la longitud de la cuerda, la frecuencia angular $\omega$ se elige de modo que

$$k = \frac{5\pi}{2L} = \omega\sqrt{\frac{\rho}{T}} = \frac{\omega}{v_\varphi}\,. \qquad \text{(8.10)}$$

Como de costumbre en un problema de oscilación forzada, nos interesa la solución estacionaria en la que el sistema se mueve con la frecuencia angular, $\omega$, de los términos impulsores. Podemos resolver este problema fácilmente descomponiéndolo en dos problemas.

Primero considere la condición de contorno:

$$\psi_1(0,t)=0\,,\qquad \psi_1(L,t)=A\sin\omega t\,. \qquad \text{(8.11)}$$

Esto se resuelve fácilmente con los métodos del capítulo 5. A partir de la condición en $x=0$, sabemos que la solución de $\psi_1(x,t)$ es proporcional a $\sin kx$. Entonces la condición de contorno en $x=L$ da la solución de onda estacionaria:

$$\psi_1(x,t) = A\sin kx\sin\omega t\,. \qquad \text{(8.12)}$$

Considere ahora la condición de contorno

$$\psi_2(0,t)=A\cos\omega t\,,\qquad \psi_2(L,t)=0\,. \qquad \text{(8.13)}$$

Argumentos análogos (empezando en $x=L$) muestran que la solución es la onda estacionaria

$$\psi_2(x,t) = A\cos kx\cos\omega t\,. \qquad \text{(8.14)}$$

Ahora podemos obtener la solución para la condición de contorno (8.9) simplemente sumando estas:

$$\psi(x,t) = \psi_1(x,t)+\psi_2(x,t) = A\cos kx\cos\omega t+A\sin kx\sin\omega t = A\cos(kx-\omega t)\,, \qquad \text{(8.15)}$$

que es una onda que viaja de $x=0$ a $x=L$. El punto crucial es que las dos ondas estacionarias con las que se construye la onda viajera están desfasadas $90°$ entre sí, tanto en el tiempo como en el espacio: se hacen grandes en puntos distintos del espacio y también en instantes distintos, y la interacción entre ambas produce la onda viajera. Esto se ilustra en las figuras 8.1-8.4 para $\omega t=0,\pi/4,\pi/2$ y $3\pi/4$. En cada una de estas figuras, la curva superior es la onda viajera; la curva del medio es (8.14); la curva inferior es (8.12).

![Figura 8.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh8_ES/fig8.1.png)

Figuras 8.1-8.4: instantáneas de la construcción de la onda viajera en $\omega t=0,\pi/4,\pi/2,3\pi/4$; en cada una, la curva superior es la suma de las dos ondas estacionarias mostradas debajo, que se desplaza progresivamente hacia la derecha a medida que avanza el tiempo.

Este sistema se anima en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-2" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-2</a>. Esta animación es importante: vale la pena observarla un rato para hacerse una idea de cómo funciona (8.15), mejor de lo que permiten las imágenes fijas de las figuras 8.1-8.4. Si se concentra en un punto particular de la cuerda, verá que la onda viajera se hace grande cuando una de las ondas estacionarias es máxima mientras la otra está cerca de cero, o (según dónde mire) cuando ambas ondas estacionarias son positivas.

## 8.2 Fuerza, potencia e impedancia

![Figura 8.5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh8_ES/fig8.5.png)

Figura 8.5 y 8.6: fuerza que ejerce una cuerda sobre un agente externo en $x=0$ y en $x=L$, mostrando la componente de la tensión perpendicular a la cuerda, con $\theta\approx\psi'$ para pequeños desplazamientos.

Para producir la onda viajera de (8.15), necesitamos calcular la fuerza requerida en cada extremo. En $x=0$, la fuerza aplicada por el agente externo debe igualar a la componente transversal de la tensión de la cuerda que tira hacia la derecha (dirección $+x$), como se muestra en la figura 8.5:

$$F_0 = -T\sin\theta \approx -T\,\left.\frac{\partial}{\partial x}\psi(x,t)\right|_{x=0}\,. \qquad \text{(8.16)}$$

En $x=L$, como la cuerda llega desde la dirección $-x$, es

$$F_L = T\,\left.\frac{\partial}{\partial x}\psi(x,t)\right|_{x=L}\,, \qquad \text{(8.17)}$$

como se ilustra en la figura 8.6.

En la oscilación forzada, el extremo de la cuerda se mueve solo en la dirección transversal. Así, la potencia suministrada por la fuerza externa en $x=0$, que es $\vec F\cdot\vec v$, es

$$P(t) = -T\,\left.\frac{\partial}{\partial x}\psi(x,t)\right|_{x=0}\,\frac{\partial}{\partial t}\psi(0,t) \qquad \text{(8.18)}$$

donde, como en (2.26), $\psi(x,t)$ es el desplazamiento real respecto al equilibrio del trozo de cuerda en la posición horizontal $x$. Debemos tomar primero la parte real, porque la potencia es una función no lineal del desplazamiento.

Para una onda estacionaria en la cuerda (o cualquier sistema sin fuerzas de fricción), la fuerza y la velocidad están desfasadas $90°$. Por ejemplo, si el desplazamiento es proporcional a $\sin\omega t$, entonces la fuerza transversal en cada extremo también es proporcional a $\sin\omega t$. La velocidad, sin embargo, es proporcional a $\cos\omega t$. Así, la potencia gastada por la fuerza externa es

$$\propto \sin\omega t\cos\omega t = \frac{1}{2}\sin2\omega t\,. \qquad \text{(8.19)}$$

Esto se promedia a cero en medio ciclo. En promedio, no se requiere potencia para mantener la onda estacionaria (en ausencia de amortiguamiento).

En una onda viajera, en cambio, la fuerza y la velocidad son proporcionales. De (8.15) puede ver que

$$\frac{\partial}{\partial x}\psi(x,t) = -\frac{k}{\omega}\,\frac{\partial}{\partial t}\psi(x,t)\,. \qquad \text{(8.20)}$$

Así,

$$F_0 = Z\,\frac{\partial}{\partial t}\psi(0,t)\,,\qquad F_L = -Z\,\frac{\partial}{\partial t}\psi(L,t)\,, \qquad \text{(8.21)}$$

donde la constante $Z$,

$$Z = \frac{Tk}{\omega} = \sqrt{\rho T}\,, \qquad \text{(8.22)}$$

se llama la «impedancia» del sistema de la cuerda. Mide la potencia necesaria para producir la onda viajera. La potencia necesaria en $x=0$ es

$$P_0 = Z\left(\frac{\partial}{\partial t}\psi(0,t)\right)^2 = ZA^2\omega^2\sin^2\omega t\,. \qquad \text{(8.23)}$$

La potencia media gastada es, por tanto,

$$\langle P_0\rangle = ZA^2\omega^2/2\,. \qquad \text{(8.24)}$$

La potencia gastada en $x=0$ para producir la onda viajera es entregada por la cuerda en $x=L$, porque la potencia requerida en $L$ es

$$P_L = -Z\left(\frac{\partial}{\partial t}\psi(L,t)\right)^2 = -ZA^2\omega^2\cos^2\omega t\,. \qquad \text{(8.25)}$$

Si las condiciones de contorno fueran tales que las ondas viajeras fueran en la dirección opuesta, la fuerza en las deducciones anteriores tendría el signo opuesto al de (8.20). Así, siempre se necesita potencia positiva para producir la onda, y se necesita potencia negativa para absorberla. Puede parecer extraño que la potencia entregada a la onda en (8.23) y la potencia entregada por la onda en (8.25) no sean exactamente iguales y opuestas. La suma se anula en promedio, pero oscila con el tiempo. La razón es que la longitud del sistema no es un número entero de longitudes de onda, lo que permite que la energía almacenada en el sistema, la suma de la cinética y la potencial, oscile en función del tiempo.

Note que la fuerza necesaria para absorber una onda viajera, en (8.21), es negativa y proporcional a la velocidad: esta es una fuerza friccional típica. Así, una onda viajera puede ser absorbida completamente por una fuerza friccional (o una resistencia) con exactamente el cociente correcto entre fuerza y velocidad. Si la impedancia del «amortiguador» (así se llama tal resistencia) no es exactamente igual a la de la cuerda, habrá algo de reflexión; volveremos a esto en el próximo capítulo.

### 8.2.1 \* Impedancia compleja

Para la cuerda estirada, un sistema cuya relación de dispersión es equivalente a la ecuación de ondas, (6.4), la fuerza sobre el sistema y la velocidad del desplazamiento, $\partial\psi/\partial t$, son proporcionales para cualquier onda viajera (lo veremos en detalle en el capítulo 10). En general, esto no es cierto. Por ejemplo, considere la cuerda con cuentas de la figura 5.4, estirada de $x=0$ a algún $x$ grande. Suponga además que hay una onda viajera en el sistema de la forma

$$\psi(x,t) = A\cos(kx-\omega t)\,, \qquad \text{(8.26)}$$

ilustrada en la figura 8.7 (para una animación de una onda viajera en un sistema similar, véase el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-6" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-6</a>; el sistema mostrado en ese programa tiene las cuentas sobre muelles, además de sobre una cuerda, pero la forma de la onda viajera es la misma; solo la relación de dispersión es distinta). La línea punteada es la posición de equilibrio de la cuerda.

![Figura 8.7](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh8_ES/fig8.7.png)

Figura 8.7: instantánea de una onda viajera en una cuerda con cuentas, mostrando las cuentas desplazadas siguiendo la envolvente $A\cos(kx-\omega t)$.

Mientras $k$ y $\omega$ estén relacionados por la relación de dispersión, (5.39), (8.26) es una solución de la ecuación de movimiento. La fuerza transversal externa en $x=0$ necesaria para producir la onda viajera está relacionada con la diferencia entre el desplazamiento del primer bloque y el desplazamiento del extremo en $x=0$ (véase la figura 5.5). Es

$$F_0 = \frac{TA}{a}\left(\cos(\omega t-ka)-\cos\omega t\right)\,. \qquad \text{(8.27)}$$

Esto es aproximadamente proporcional a la velocidad solo si $ka$ es muy pequeño, de modo que el lado derecho de (8.27) pueda expandirse en serie de Taylor. Así, en este caso, y en general para un sistema discreto, no podemos definir la impedancia simplemente como en (8.21).

Sin embargo, supongamos que, en lugar de la onda viajera real, (8.26), consideramos una onda viajera armónica compleja con dependencia irreducible en el tiempo y el espacio, de la forma

$$\psi(x,t) = A\,e^{-i(\omega t-kx)}\,. \qquad \text{(8.28)}$$

Entonces, debido a la irreducibilidad en $t$ y $x$ (que proviene de la invariancia bajo traslación), sabemos inmediatamente que tanto la fuerza como la derivada temporal de $\psi$ son proporcionales a $\psi$. Para una solución irreducible, todo es proporcional a $e^{-i(\omega t-kx)}$; así, son también proporcionales entre sí, y podemos definir la impedancia,

$$F = -Z(k)\,\frac{\partial}{\partial t}\psi(x,t) = i\omega A\,Z(k)\,e^{-i(\omega t-kx)}\,. \qquad \text{(8.29)}$$

Por ejemplo, para la cuerda con cuentas, si reemplazamos la solución real, (8.26), por la solución compleja irreducible, (8.28), la fuerza se convierte en

$$F_0 = \frac{TA}{a}\left(e^{-i(\omega t-ka)}-e^{-i\omega t}\right) = \frac{TA}{a}\left(e^{ika}-1\right)e^{-i\omega t}\,. \qquad \text{(8.30)}$$

Así, de (8.29), la impedancia, $Z(k)$, es

$$Z(k) = \frac{T}{\omega a}\,\frac{e^{ika}-1}{i} = \frac{2T}{a\omega}\,e^{ika/2}\sin\frac{ka}{2}\,. \qquad \text{(8.31)}$$

Usando la relación de dispersión, (5.39), podemos escribir esto como

$$Z(k) = e^{ika/2}\sqrt{\frac{mT}{a}}\,. \qquad \text{(8.32)}$$

La impedancia, $Z(k)$, definida por (8.29), es en general compleja y depende de $k$. Sin embargo, podemos encontrar la potencia media necesaria para producir la onda. Como la potencia es una función no lineal del desplazamiento, debemos tomar primero las partes reales de la velocidad y la fuerza complejas antes de calcular la potencia, como en (2.26). Para $A=|A|e^{i\varphi}$ compleja arbitraria,

$$v = \omega|A|\sin(\omega t-kx-\varphi)\,, \qquad \text{(8.33)}$$

$$F = (\text{Im}\,Z(k))\,\omega|A|\cos(\omega t-kx-\varphi) + (\text{Re}\,Z(k))\,\omega|A|\sin(\omega t-kx-\varphi)\,,$$

donde hemos puesto la fase de $A$ dentro de las funciones seno y coseno (véase (1.96)-(1.98)), para dejar claro que solo el valor absoluto de $A$ importa para la potencia media. Entonces, como en (2.26), solo el término en $\sin^2$ contribuye a la potencia promediada en el tiempo, que es

$$\frac{1}{2}(\text{Re}\,Z)\,\omega^2|A|^2\,. \qquad \text{(8.34)}$$

## 8.3 La luz

Las ondas de luz, como las ondas sonoras que discutimos en el capítulo anterior, son intrínsecamente tridimensionales. Sin embargo, como con el sonido, podemos decir mucho sobre la luz que es más o menos independiente de los detalles tridimensionales.

### 8.3.1 Ondas planas

Hay una forma simple de concentrarse en una sola dimensión: buscar soluciones en las que las otras dos dimensiones no intervengan en absoluto. Considere las ecuaciones de Maxwell en el vacío, en términos de los campos vectoriales $\vec E$ y $\vec B$ que describen los campos eléctrico y magnético:

$$\begin{aligned}
\frac{\partial E_y}{\partial x}-\frac{\partial E_x}{\partial y} &= -\frac{\partial B_z}{\partial t}\\
\frac{\partial E_z}{\partial y}-\frac{\partial E_y}{\partial z} &= -\frac{\partial B_x}{\partial t}\\
\frac{\partial E_x}{\partial z}-\frac{\partial E_z}{\partial x} &= -\frac{\partial B_y}{\partial t}
\end{aligned} \qquad \text{(8.35)}$$

$$\begin{aligned}
\frac{\partial B_y}{\partial x}-\frac{\partial B_x}{\partial y} &= \mu_0\epsilon_0\,\frac{\partial E_z}{\partial t}\\
\frac{\partial B_z}{\partial y}-\frac{\partial B_y}{\partial z} &= \mu_0\epsilon_0\,\frac{\partial E_x}{\partial t}\\
\frac{\partial B_x}{\partial z}-\frac{\partial B_z}{\partial x} &= \mu_0\epsilon_0\,\frac{\partial E_y}{\partial t}
\end{aligned} \qquad \text{(8.36)}$$

$$\frac{\partial E_x}{\partial x}+\frac{\partial E_y}{\partial y}+\frac{\partial E_z}{\partial z}=0\,,\qquad \frac{\partial B_x}{\partial x}+\frac{\partial B_y}{\partial y}+\frac{\partial B_z}{\partial z}=0 \qquad \text{(8.37)}$$

donde $\epsilon_0$ y $\mu_0$ son dos constantes llamadas la permitividad y la permeabilidad del espacio vacío (véase, por ejemplo, Purcell, capítulo 9). Busquemos soluciones de estas ecuaciones diferenciales parciales que involucren solo funciones de $z$ y $t$. En este caso, las cosas se simplifican a:

$$0=-\frac{\partial B_z}{\partial t}\,,\qquad -\frac{\partial E_y}{\partial z}=-\frac{\partial B_x}{\partial t}\,,\qquad \frac{\partial E_x}{\partial z}=-\frac{\partial B_y}{\partial t}\,, \qquad \text{(8.38)}$$

$$0=\mu_0\epsilon_0\,\frac{\partial E_z}{\partial t}\,,\qquad -\frac{\partial B_y}{\partial z}=\mu_0\epsilon_0\,\frac{\partial E_x}{\partial t}\,,\qquad \frac{\partial B_x}{\partial z}=\mu_0\epsilon_0\,\frac{\partial E_y}{\partial t}\,, \qquad \text{(8.39)}$$

$$\frac{\partial E_z}{\partial z}=0\,,\qquad \frac{\partial B_z}{\partial z}=0\,. \qquad \text{(8.40)}$$

Estas ecuaciones implican que $E_z$ y $B_z$ son independientes de $z$ y $t$. Como ya hemos supuesto que dependen solo de $z$ y $t$, esto significa que son constantes; las ignoraremos, porque nos interesan las soluciones con dependencia no trivial en $z$ y $t$. Eso deja las componentes $x$ e $y$, que satisfacen (8.38) y (8.39).

Entonces, como (8.38) y (8.39) son invariantes bajo traslaciones en $z$ y $t$, esperamos soluciones exponenciales complejas, en las que todas las componentes son proporcionales a

$$e^{i(\pm kz-\omega t)}\,, \qquad \text{(8.41)}$$

$$E_x(z,t) = \varepsilon_x^\pm\,e^{i(\pm kz-\omega t)}\,,\qquad E_y(z,t) = \varepsilon_y^\pm\,e^{i(\pm kz-\omega t)}\,, \qquad \text{(8.42)}$$

$$B_x(z,t) = \beta_x^\pm\,e^{i(\pm kz-\omega t)}\,,\qquad B_y(z,t) = \beta_y^\pm\,e^{i(\pm kz-\omega t)}\,. \qquad \text{(8.43)}$$

Sustituyendo directamente (8.42) y (8.43) en (8.38) y (8.39), obtenemos

$$\pm k\varepsilon_y^\pm = \omega\beta_x^\pm\,,\qquad \pm k\varepsilon_x^\pm = \omega\beta_y^\pm\,, \qquad \text{(8.44)}$$

$$\pm k\beta_y^\pm = -\mu_0\epsilon_0\omega\varepsilon_x^\pm\,,\qquad \pm k\beta_x^\pm = -\mu_0\epsilon_0\omega\varepsilon_y^\pm\,. \qquad \text{(8.45)}$$

Como de costumbre, hemos escrito la onda con la dependencia temporal irreducible, $e^{-i\omega t}$. Para obtener los campos eléctrico y magnético reales, tomamos la parte real de (8.42) y (8.43). Esto funciona porque las ecuaciones de Maxwell son lineales en los campos eléctrico y magnético. Las amplitudes, $\varepsilon_x^\pm$, etc., pueden ser complejas.

De (8.44) y (8.45), verá que $\varepsilon_y^\pm$ está relacionada con $\beta_x^\pm$, y $\varepsilon_x^\pm$ está relacionada con $\beta_y^\pm$. Para cada relación, hay dos ecuaciones lineales simultáneas homogéneas en las dos incógnitas. Son consistentes solo si el cociente de los coeficientes es el mismo, lo que implica una relación entre $k$ y $\omega$,

$$k^2 = \mu_0\epsilon_0\,\omega^2\,. \qquad \text{(8.46)}$$

Esta es una relación de dispersión,

$$\omega^2 = c^2k^2 = \frac{1}{\mu_0\epsilon_0}\,k^2\,. \qquad \text{(8.47)}$$

La velocidad de fase, $c$, es la velocidad de la luz en el vacío (tendremos más que decir sobre esto en los capítulos 10 y 11). Una vez satisfecha (8.47), podemos resolver para las $\beta^\pm$ en términos de las $\varepsilon^\pm$:

$$\beta_y^\pm = \pm\frac{1}{c}\varepsilon_x^\pm\,,\qquad \beta_x^\pm = \mp\frac{1}{c}\varepsilon_y^\pm\,. \qquad \text{(8.48)}$$

Estas soluciones de las ecuaciones de Maxwell en el vacío son ondas electromagnéticas, u ondas de luz. Estas soluciones simples, que dependen solo de $z$ y $t$, son un ejemplo de soluciones de onda plana. El nombre es apropiado porque los campos eléctrico y magnético de la onda tienen el mismo valor en todos los puntos de cada plano de $z$ constante, para cualquier instante $t$ fijo. Estos planos se propagan en la dirección $\pm z$ con la velocidad de fase $c$.

En general, las ondas electromagnéticas pueden propagarse en cualquier dirección del espacio tridimensional. Sin embargo, los campos eléctrico y magnético que forman la onda son siempre perpendiculares a la dirección en la que viaja la onda, y perpendiculares entre sí.

El tratamiento de las ondas planas electromagnéticas que viajan en la dirección $z$ es análogo a nuestro tratamiento del sonido en el capítulo 7. Allí también la onda dependía solo de $z$. Sin embargo, las ondas electromagnéticas son un poco más complicadas, porque el fenómeno ondulatorio depende tanto del campo eléctrico como del magnético. La razón por la que hemos pospuesto hasta ahora la discusión de las ondas electromagnéticas, a pesar de que son uno de los ejemplos más importantes de fenómenos ondulatorios, es que las relaciones (8.48) entre los campos eléctrico y magnético dependen de la dirección en la que viaja la onda (¡el signo $\pm$!). Es mucho más fácil escribir las soluciones de las ondas viajeras que las de las ondas estacionarias. Incluso para las simples ondas planas viajeras que hemos descrito, que dependen solo de $z$ y $t$, esta relación entre $\vec E$ y $\vec B$, y la dirección de la onda, depende de las propiedades tridimensionales de las ecuaciones de Maxwell. Discutiremos estos temas con mucho más detalle en los capítulos 11 y 12.

### 8.3.2 Interferómetros

Una de las maravillosas características de las ondas de luz es que es relativamente fácil dividirlas y recombinarlas. Esta característica se usa en muchos dispositivos ópticos, uno de los más simples de los cuales es un «interferómetro», una versión del cual (el interferómetro de Michelson) se muestra esquemáticamente en la figura 8.8. Una fuente produce una onda plana (como discutiremos en el capítulo 13, no puede ser exactamente una onda plana, pero no importa por ahora). El espejo semiplateado sirve como «divisor de haz», dejando pasar parte de la luz mientras refleja el resto. Luego los espejos de arriba y de la derecha reflejan los haces de vuelta. Entonces el espejo semiplateado sirve como «recombinador de haz», combinando los haces de arriba y de la derecha en un único haz que continúa hacia la pantalla detectora, donde se mide la intensidad del haz (proporcional al cuadrado del campo eléctrico). Lo importante es que la onda de luz que llega a la pantalla detectora es la suma de dos componentes que son coherentes y que sin embargo han recorrido caminos distintos. Lo que significa «coherente» en este contexto no es solo que la frecuencia sea la misma, sino que la fase de las ondas esté correlacionada. En este caso, eso ocurre simplemente porque las dos componentes que llegan a la pantalla provienen de la misma onda plana incidente.

![Figura 8.8](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh8_ES/fig8.8.png)

Figura 8.8: diagrama esquemático de un interferómetro de Michelson, con una fuente, un espejo semiplateado que divide el haz hacia dos espejos perpendiculares, y una pantalla detectora donde se recombinan los dos haces reflejados.

Ahora bien, la intensidad de la luz que llega a la pantalla depende de la longitud relativa de los dos caminos. Longitudes de camino distintas producirán fases distintas. Si las dos componentes están en fase, las amplitudes se suman y la pantalla se ve brillante: esto se llama «interferencia constructiva». Si las dos componentes están desfasadas $180°$, las amplitudes se restan y la pantalla se ve oscura: hay lo que se llama «interferencia destructiva».

Esto suena bastante trivial, y de hecho lo es (al menos para las ondas electromagnéticas clásicas), pero también es extremadamente útil, porque proporciona una medida muy sensible de los cambios en la longitud de los caminos. En particular, si uno de los espejos se mueve una distancia $d$ (podría ser parte de un montaje experimental diseñado para detectar pequeños movimientos, por ejemplo), la fase relativa de las dos componentes que llegan a la pantalla cambia en $2kd$, donde $k$ es el número de onda angular de la onda plana, porque la longitud del camino de la onda reflejada ha cambiado en $2d$. Así, cada vez que $d$ cambia en un cuarto de la longitud de onda de la luz, la pantalla pasa de brillante a oscura, o viceversa.

Esta es una manera muy útil de medir pequeños cambios de distancia. En la práctica, el haz incidente no es exactamente una onda plana (eso, como veremos en detalle más adelante, ¡requeriría un experimento infinito!), así que la intensidad de la luz no es uniforme sobre la pantalla. En su lugar, hay zonas claras y oscuras conocidas como «franjas». A medida que se mueve el espejo, las franjas se desplazan, y se pueden contar las franjas que pasan por un punto dado para llevar la cuenta del número de cambios de brillante a oscuro.

### 8.3.3 Interferencia cuántica

Hay otra forma de pensar en el interferómetro que lo hace parecer mucho menos trivial. Como discutiremos varias veces en este libro, y aprenderá con más detalle cuando estudie mecánica cuántica, la luz no es solo una onda: también está formada por partículas individuales de luz llamadas fotones. No lo nota a menos que baje mucho la intensidad de la onda de luz. Pero, de hecho, puede bajar tanto la intensidad que puede detectar fotones individuales llegando a la pantalla. Ahora ya no está tan claro qué está ocurriendo. Un fotón individual no puede dividirse en dos partes en el divisor y el recombinador de haz. Como veremos más adelante, la energía del fotón está determinada por la frecuencia de la luz; no puede dividirse. Podría pensar, por tanto, que el fotón individual tendría que ir por un camino o por el otro. Pero entonces, ¿cómo puede haber interferencia entre los dos caminos? No hay respuesta a esta pregunta que tenga «sentido» en la física clásica de partículas. Sin embargo, cuando se hace el experimento, el número de fotones que llegan a la pantalla depende de la diferencia de longitudes entre los dos caminos exactamente como se esperaría por la descripción ondulatoria. La probabilidad de que un fotón golpee un punto dado de la pantalla es proporcional a la intensidad de la onda clásica correspondiente. Si las longitudes de los caminos producen interferencia destructiva, no pasan fotones. Y no solo eso: experimentos similares pueden hacerse con otras partículas, ¡como los neutrones! Quizá la interferencia no sea tan trivial después de todo.

## 8.4 Líneas de transmisión

Hemos visto que un sistema invariante bajo traslación de inductores y condensadores puede transportar ondas. Preguntémonos qué ocurre cuando tomamos el límite continuo de tal sistema; esto dará una visión interesante de las ondas electromagnéticas. La relación de dispersión del sistema de la figura 5.23 viene dada por (5.75),

$$\omega^2 = \frac{4}{L_aC_a}\sin^2\frac{ka}{2}\,. \qquad \text{(8.49)}$$

donde $L_a$ y $C_a$ son la inductancia y la capacitancia de los inductores y condensadores del sistema, con separación $a$ entre partes vecinas. Para tomar el límite continuo, debemos reemplazar la inductancia y la capacitancia, $L_a$ y $C_a$, por cantidades que esperamos tengan límites finitos cuando $a\to0$. Esperamos, por la analogía (5.69) entre circuitos LC y sistemas de muelles y masas, y por la discusión al principio del capítulo 7 sobre el límite continuo del sistema de masas y muelles, que las cantidades relevantes sean:

$$\begin{aligned}
&\frac{L_a}{a} \to \text{inductancia por unidad de longitud}\\
&K_aa \to \frac{a}{C_a} \to \text{recíproco de la capacitancia por unidad de longitud}
\end{aligned} \qquad \text{(8.50)}$$

Estas dos cantidades pueden calcularse directamente a partir de la inductancia y la capacitancia de una longitud finita, $\ell$, del sistema que contiene muchas unidades individuales. Los inductores están conectados en serie, así que las inductancias individuales se suman para dar la inductancia total. Así, si la longitud $\ell$ es $na$, de modo que el sistema finito contiene $n$ inductores, la inductancia total es $L=nL_a$. Entonces

$$\frac{L}{\ell} = \frac{L_a}{a}\,. \qquad \text{(8.51)}$$

Las capacitancias funcionan de la misma manera porque están conectadas en paralelo, y las capacitancias en paralelo se suman. Así,

$$\frac{C}{\ell} = \frac{C_a}{a}\,. \qquad \text{(8.52)}$$

Por tanto, al tomar el límite $a\to0$ de (8.49), podemos escribir

$$L_a = a\,\frac{L}{\ell}\,,\qquad C_a = a\,\frac{C}{\ell}\,. \qquad \text{(8.53)}$$

Esto da la siguiente relación de dispersión:

$$\omega^2 = \frac{\ell^2}{LC}\,\frac{4\sin^2\frac{ka}{2}}{a^2} \to \frac{\ell^2}{LC}\,k^2\,. \qquad \text{(8.54)}$$

Un sistema continuo como este, con inductancia y capacitancia fijas por unidad de longitud, se llama línea de transmisión. Llamaremos a (8.54) la relación de dispersión de una línea de transmisión sin resistencia. Una línea de transmisión puede usarse para enviar ondas eléctricas, igual que una cuerda continua transmite ondas mecánicas. En el sistema continuo, la variable de desplazamiento, la carga desplazada, se convierte en una función de la posición a lo largo de la línea de transmisión. Si la línea de transmisión se extiende en la dirección $z$, podemos describir las cargas de la línea mediante una función $Q(z,t)$, que es la carga que se ha desplazado a través del punto $z$ de la línea en el instante $t$. La derivada temporal de $Q(z,t)$ es la corriente en el punto $z$ e instante $t$:

$$I(z,t) = \frac{\partial Q(z,t)}{\partial t}\,. \qquad \text{(8.55)}$$

### 8.4.1 Línea de transmisión de placas paralelas

Vale la pena trabajar un ejemplo concreto de línea de transmisión. El ejemplo que usaremos es el de dos largas tiras conductoras paralelas. Imagine un sistema infinito en el que las tiras se extienden paralelas entre sí en planos de $y$ constante, hacia el infinito en la dirección $z$. Suponga que las tiras son suficientemente delgadas como para despreciar su grosor. Suponga además que la anchura de las tiras, $w$, es mucho mayor que la separación, $s$. Una sección transversal de esta línea de transmisión en el plano $x$-$y$ se muestra en la figura 8.9. En la figura, la dirección $z$ sale del plano del papel, hacia usted. Seguiremos el movimiento de las cargas en el conductor superior, y supondremos que el conductor inferior está conectado a tierra (con voltaje fijo en $V=0$).

![Figura 8.9](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh8_ES/fig8.9.png)

Figura 8.9: sección transversal de la línea de transmisión de placas paralelas, mostrando dos tiras conductoras de anchura $w$ separadas verticalmente una distancia $s$.

Encontraremos la relación de dispersión de la línea de transmisión calculando la capacitancia y la inductancia de un tramo de la línea de longitud $\ell$. Será útil hacerlo usando consideraciones de energía. Suponga que hay una carga, $Q$, distribuida uniformemente sobre la placa superior del condensador, y una corriente, $I$, fluyendo uniformemente hacia afuera del plano $x$-$y$, en la dirección $z$, a lo largo del conductor superior (y de vuelta hacia el plano a lo largo del conductor inferior). La energía almacenada en la longitud $\ell$ de la línea de transmisión es entonces

$$\frac{1}{2C}Q^2 + \frac{1}{2}LI^2\,, \qquad \text{(8.56)}$$

donde $C$ y $L$ son la capacitancia y la inductancia (véase, por ejemplo, Halliday y Resnick, parte 2).

La energía en realidad se almacena en los campos eléctrico y magnético producidos por la carga y la corriente. En esta configuración, los campos eléctrico y magnético están casi enteramente entre las dos placas del tramo de línea de transmisión. Si $Q$ e $I$ son positivos, los campos eléctrico y magnético son como se muestra en las figuras 8.10 y 8.11. En la figura 8.10, la línea punteada es la sección transversal de una región en forma de caja que puede usarse para calcular el campo eléctrico, usando la ley de Gauss. En la figura 8.11, el camino punteado puede usarse para calcular el campo magnético, usando la ley de Ampère. Los campos eléctrico y magnético son aproximadamente constantes entre las tiras, pero caen rápidamente a casi cero fuera de ellas.

![Figura 8.11](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh8_ES/fig8.11.png)

Figura 8.11

![Figura 8.10](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh8_ES/fig8.10.png)

Figura 8.10: el campo eléctrico producido por la carga en la línea de transmisión, apuntando de la placa superior a la inferior, con una región gaussiana en forma de caja para aplicar la ley de Gauss. Figura 8.11: el campo magnético producido por la corriente, apuntando horizontalmente entre las placas, con un camino amperiano rectangular para aplicar la ley de Ampère.

La densidad de carga en la placa superior es aproximadamente uniforme y viene dada por la carga total dividida entre el área, $w\ell$,

$$\sigma \approx \frac{Q}{w\ell}\,. \qquad \text{(8.57)}$$

Entonces podemos aplicar la ley de Gauss a una pequeña región en forma de caja, cuya sección transversal se muestra en la figura 8.10, y concluir que el campo eléctrico en el interior viene dado por

$$E_y \approx -\frac{Q}{\epsilon_0w\ell} \qquad \text{(8.58)}$$

La densidad de energía almacenada en el campo eléctrico entre las placas es, por tanto,

$$u_E = \frac{\epsilon_0}{2}E^2 \approx \frac{Q^2}{2\epsilon_0w^2\ell^2}\,. \qquad \text{(8.59)}$$

La energía total almacenada en el campo eléctrico se obtiene entonces multiplicando $u_E$ por el volumen entre las placas, dando

$$\frac{1}{2}\,\frac{s}{\epsilon_0w\ell}\,Q^2 \qquad \text{(8.60)}$$

así, comparando con (8.56),

$$C = \frac{\epsilon_0w\ell}{s}\,. \qquad \text{(8.61)}$$

Podemos calcular la inductancia de forma similar. La ley de Ampère, aplicada a un camino que rodea el conductor superior (como se muestra en la figura 8.11), da

$$B_x \approx \frac{\mu_0I}{w}\,. \qquad \text{(8.62)}$$

La densidad de energía almacenada en el campo magnético entre las placas es, por tanto,

$$u_B = \frac{1}{2\mu_0}B^2 \approx \frac{\mu_0I^2}{2w^2}\,. \qquad \text{(8.63)}$$

La energía total almacenada en el campo magnético se obtiene entonces multiplicando $u_B$ por el volumen entre las placas, dando

$$\frac{1}{2}\,\frac{\mu_0s\ell}{w}\,I^2 \qquad \text{(8.64)}$$

así, comparando con (8.56),

$$L = \frac{\mu_0s\ell}{w}\,. \qquad \text{(8.65)}$$

Ahora podemos sustituir (8.61) y (8.65) en (8.54), para obtener la relación de dispersión de esta línea de transmisión:

$$\omega^2 = \frac{1}{\mu_0\epsilon_0}\,k^2 = c^2k^2\,, \qquad \text{(8.66)}$$

¡donde $c$ es la velocidad de la luz!

### 8.4.2 Ondas en la línea de transmisión

La relación de dispersión, (8.66), se parece sospechosamente a la relación de dispersión de las ondas electromagnéticas. De hecho, los campos eléctrico y magnético entre las tiras de la línea de transmisión tienen exactamente la forma de una onda electromagnética. Para verlo explícitamente, consideremos una onda viajera en la línea de transmisión, y la carga, $Q(z,t)$, desplazada a través de $z$, con la dependencia exponencial compleja irreducible en $z$ y $t$,

$$Q(z,t) = q\,e^{i(kz-\omega t)}\,. \qquad \text{(8.67)}$$

Esta onda viaja en la dirección $z$ positiva, alejándose hacia usted en el diagrama de la figura 8.9.

En cualquier instante fijo $t$ y posición $z$, los campos eléctrico y magnético dentro de la línea de transmisión se ven como en las figuras 8.10 y 8.11 (o ambos pueden apuntar en la dirección opuesta). Podemos encontrar el campo magnético igual que hicimos arriba, porque la corriente en cualquier punto de la línea viene dada por (8.55), así que

$$B_x(z,t) \approx \frac{\mu_0I(z,t)}{w} = \frac{\mu_0}{w}\,\frac{\partial}{\partial t}Q(z,t) = -i\,\frac{\mu_0\omega q}{w}\,e^{i(kz-\omega t)}\,. \qquad \text{(8.68)}$$

Para encontrar el campo eléctrico como función de $z$ y $t$, necesitamos la densidad de carga a lo largo de la línea. Una vez que la tenemos, podemos encontrar el campo eléctrico usando la ley de Gauss, como arriba. Resulta una densidad de carga no nula si la cantidad de carga desplazada cambia en función de $z$. Es más fácil encontrar la densidad de carga volviendo al sistema discreto discutido en el capítulo 5, y a (5.72). En el lenguaje en el que etiquetamos las partes del sistema por sus posiciones, la carga $q_j$ del sistema discreto se convierte en $q(z,t)$, donde $z=ja$. Cuando $a\to0$, esto corresponde a una densidad de carga lineal a lo largo de la línea de transmisión de

$$\rho(z,t) = \frac{q(z,t)}{a}\,. \qquad \text{(8.69)}$$

En este lenguaje, (5.72) se convierte en

$$q(z,t) = Q(z,t) - Q(z+a,t)\,, \qquad \text{(8.70)}$$

donde $Q(z,t)$ es la carga desplazada a través del inductor en la posición $z$ en el instante $t$. Combinando (8.69) y (8.70) da

$$\rho(z,t) = \frac{Q(z,t)-Q(z+a,t)}{a}\,. \qquad \text{(8.71)}$$

Tomando el límite cuando $a\to0$, da

$$\rho(z,t) = -\frac{\partial}{\partial z}Q(z,t) = -ikq\,e^{i(kz-\omega t)}\,. \qquad \text{(8.72)}$$

Esta densidad de carga lineal se distribuye sobre la anchura de la tira superior de la línea de transmisión, dando una densidad de carga superficial de

$$\sigma(z,t) = \frac{\rho(z,t)}{w} = -i\,\frac{kq}{w}\,e^{i(kz-\omega t)}\,. \qquad \text{(8.73)}$$

Ahora el campo eléctrico, por la ley de Gauss, es

$$E_y = -\frac{\sigma(z,t)}{\epsilon_0} = i\,\frac{kq}{\epsilon_0w}\,e^{i(kz-\omega t)}\,. \qquad \text{(8.74)}$$

Comparando (8.68) con (8.74), puede ver que se satisface (8.45), de modo que este par de campos eléctrico y magnético forma parte de una onda plana electromagnética viajera.

Lo que ocurre aquí es que el papel de las cargas y corrientes en las tiras de la línea de transmisión es confinar las ondas electromagnéticas. Sin los conductores, sería imposible producir un fragmento de onda plana, como veremos con mucho más detalle en el capítulo 13.

Mientras tanto, note que el modo con $\omega=0$ y $k=0$ debe tratarse con cuidado, igual que el modo $\omega=k=0$ de la cuerda con cuentas discutido en el capítulo 5. El modo en el que la carga desplazada es proporcional a $z$ (véase (5.41)) describe una situación en la que toda la línea de transmisión infinita está cargada; esto no es muy interesante en el caso finito. Sin embargo, el modo independiente de $z$ pero creciente con el tiempo, proporcional a $t$, sí es importante: describe la situación en la que fluye una corriente constante por los conductores. Dentro de la línea de transmisión, en este caso, hay un campo magnético constante.

## 8.5 Amortiguamiento

Es instructivo, llegados a este punto, considerar las ondas en sistemas con fuerzas de fricción. Hemos pospuesto esto hasta ahora porque será más fácil entender qué ocurre en sistemas con amortiguamiento ahora que hemos discutido las ondas viajeras.

La observación clave es que, en un sistema invariante bajo traslación, incluso en presencia de amortiguamiento, los modos normales del sistema infinito son exactamente los mismos que sin amortiguamiento, porque siguen estando determinados por la invariancia bajo traslación. Los modos normales siguen siendo de la forma $e^{\pm ikx}$, caracterizados por el número de onda angular $k$. Solo la relación de dispersión es distinta. Para ver esto en detalle, recapitulemos los argumentos del capítulo 5.

La relación de dispersión de un sistema sin amortiguamiento se determina por la solución de la ecuación de autovalores

$$\left[-\omega^2+M^{-1}K\right]A^k = 0\,, \qquad \text{(8.75)}$$

donde $A^k$ es el modo normal con número de onda $k$,

$$A_j^k \propto e^{ijka}\,, \qquad \text{(8.76)}$$

con dependencia temporal $e^{-i\omega t}$ (en presencia de amortiguamiento, el signo de $i$ importa: las relaciones de abajo tendrían otro aspecto si hubiéramos usado $e^{i\omega t}$, y no podríamos usar $\cos\omega t$ o $\sin\omega t$). Ya sabemos que $A^k$ es un modo normal, por la invariancia bajo traslación; esto implica que es un autovector de $M^{-1}K$. El autovalor es cierta función de $k$; la llamaremos $\omega_0^2(k)$, de modo que

$$M^{-1}K\,A^k = \omega_0^2(k)\,A^k\,. \qquad \text{(8.77)}$$

Esta función $\omega_0^2(k)$ determina la relación de dispersión del sistema sin amortiguamiento, porque la ecuación de autovalores, (8.75), implica ahora

$$\omega^2 = \omega_0^2(k)\,. \qquad \text{(8.78)}$$

Ahora podemos modificar la discusión anterior para incluir el amortiguamiento en el sistema infinito invariante bajo traslación. En presencia de amortiguamiento, la ecuación de movimiento tiene la forma

$$M\,\frac{d^2}{dt^2}\psi(t) = -M\gamma\,\frac{d}{dt}\psi(t) - K\psi(t)\,, \qquad \text{(8.79)}$$

donde $M\gamma$ es la matriz que describe el amortiguamiento dependiente de la velocidad. Entonces, para un modo normal,

$$\psi(t) = A^k\,e^{-i\omega t}\,, \qquad \text{(8.80)}$$

la ecuación de autovalores ahora se ve así:

$$\left[-\omega^2-i\gamma\omega+M^{-1}K\right]A^k = 0\,. \qquad \text{(8.81)}$$

Ahora, igual que en (8.77) arriba, por la invariancia bajo traslación sabemos que $A^k$ es un autovector tanto de $M^{-1}K$ como de $\gamma$,

$$M^{-1}K\,A^k = \omega_0^2(k)\,A^k\,,\qquad \gamma\,A^k = \gamma(k)\,A^k\,. \qquad \text{(8.82)}$$

Entonces, como arriba, la ecuación de autovalores se convierte en la relación de dispersión

$$\omega^2 = \omega_0^2(k) - i\gamma(k)\omega\,. \qquad \text{(8.83)}$$

Para todo $k$, $\gamma(k)\ge0$, porque, como veremos en (8.84) más abajo, la fuerza es una fuerza de fricción. Si $\gamma(k)$ fuera negativo para algún $k$, la fuerza «friccional» estaría inyectando energía al sistema en vez de amortiguarlo. Note también que si $\gamma=\gamma I$, entonces $\gamma(k)=\gamma$, independiente de $k$. Sin embargo, en general, el amortiguamiento dependerá de $k$: modos con distinto $k$ pueden amortiguarse de forma diferente.

En (8.83) vemos la característica nueva de los sistemas invariantes bajo traslación con amortiguamiento: la única diferencia es que la relación de dispersión se vuelve compleja. Tanto $\omega_0^2(k)$ como $\gamma(k)$ son reales para $k$ real. Debido a la $i$ explícita en (8.83), o bien $\omega$ o bien $k$ (o ambos) deben ser complejos para satisfacer la ecuación de movimiento.

### 8.5.1 Oscilaciones libres

Para las oscilaciones libres, los números de onda angulares, $k$, de los modos permitidos quedan determinados por las condiciones de contorno. Típicamente, los valores permitidos de $k$ son reales y $\omega_0^2(k)$ es positivo (correspondiendo a un equilibrio estable en ausencia de amortiguamiento). Entonces los modos de oscilación libre son análogos a las oscilaciones libres de un oscilador amortiguado discutidas en el capítulo 2. De hecho, si sustituimos $\alpha\to-i\omega$ y $\gamma\to\gamma(k)$ en (2.5), obtenemos precisamente (8.83). Así, podemos retomar la solución de (2.6),

$$-i\omega = -\frac{\gamma(k)}{2} \pm \sqrt{\frac{\gamma(k)^2}{4}-\omega_0^2(k)}\,. \qquad \text{(8.84)}$$

Esto describe una solución que se extingue exponencialmente con el tiempo. Que oscile o se extinga suavemente depende del cociente entre $\gamma(k)$ y $\omega_0(k)$, como se discutió en el capítulo 2.

### 8.5.2 Oscilación forzada

*(Referencia a los programas interactivos 8-3 a 8-5 del disco de programas del curso original.)*

Consideremos ahora una oscilación forzada, en la que impulsamos un extremo de un sistema invariante bajo traslación con frecuencia angular $\omega$. Después de que las oscilaciones libres se hayan extinguido, quedamos con una oscilación a la única frecuencia angular real, $\omega$. Como siempre, en los problemas de oscilación forzada, pensamos en el desplazamiento real del extremo del sistema como la parte real de un desplazamiento complejo proporcional a $e^{-i\omega t}$. Entonces se aplica la relación de dispersión, (8.83). Ahora la relación de dispersión determina $k$, y $k$ debe ser complejo.

Puede haber notado que ninguna de las relaciones de dispersión que hemos estudiado hasta ahora dependen del signo de $k$. Esto no es casualidad. La razón es que todos los sistemas que hemos estudiado tienen la propiedad de simetría de reflexión: podríamos cambiar $x\to-x$ sin afectar la física. De hecho, un sistema invariante bajo traslación que no tuviera esta simetría sería un poco peculiar. Mientras el sistema sea invariante bajo reflexiones, $x\to-x$, la relación de dispersión no puede depender del signo de $k$. La razón es que, cuando $x\to-x$, el modo $e^{ikx}$ se convierte en $e^{-ikx}$. Si $x\to-x$ es una simetría, estos dos modos con números de onda angulares $k$ y $-k$ deben ser físicamente equivalentes, y por tanto deben tener la misma frecuencia. Así, las dos soluciones para $\omega$ fijo deben tener la forma:

$$k = \pm(k_r+ik_i) \qquad \text{(8.85)}$$

Debido al signo $\pm$, podemos elegir $k_r>0$ en (8.85).

En sistemas con fuerzas de fricción, siempre encontramos

$$k_i \ge 0 \quad\text{para } k_r>0\,. \qquad \text{(8.86)}$$

La razón de esto es fácil de ver si considera las ondas viajeras, que tienen la forma

$$e^{-i\omega t}e^{\pm i(k_r+ik_i)x} \qquad \text{(8.87)}$$

o

$$e^{i(\pm k_rx-\omega t)}e^{\mp k_ix}\,. \qquad \text{(8.88)}$$

De (8.88) debería ser evidente qué ocurre. Cuando el signo $\pm$ es $+$, la onda va en la dirección $+x$, así que el signo de la exponencial real es tal que la amplitud de la onda disminuye a medida que $x$ aumenta: ¡la onda se va apagando a medida que viaja! Esto es lo que debe ocurrir con una fuerza friccional. El otro signo requeriría una fuente de energía en el medio, de modo que la amplitud de la onda crecería exponencialmente al viajar. Un fragmento de una onda viajera amortiguada infinita se anima en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-3" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-3</a>.

La forma (8.88) tiene algunas consecuencias interesantes para los problemas de oscilación forzada en presencia de amortiguamiento. En sistemas discretos amortiguados, incluso en un modo normal, las partes del sistema no oscilan todas en fase. En sistemas continuos amortiguados, la distinción entre ondas viajeras y ondas estacionarias se difumina.

Considere un problema de oscilación forzada para la oscilación transversal de una cuerda con un extremo, en $x=0$, fijo, y el otro extremo, $x=L$, impulsado a frecuencia $\omega$. No importará hasta el final de nuestro análisis si la cuerda es continua o tiene cuentas con separación $a$ tal que $na=L$ para $n$ entero. Las condiciones de contorno son

$$\psi(L,t)=A\cos\omega t\,,\qquad \psi(0,t)=0\,. \qquad \text{(8.89)}$$

Como de costumbre, consideramos $\psi(x,t)$ como la parte real de un desplazamiento complejo, $\tilde\psi(x,t)$, que satisface

$$\tilde\psi(L,t)=Ae^{-i\omega t}\,,\qquad \tilde\psi(0,t)=0\,. \qquad \text{(8.90)}$$

Si $k$, para la frecuencia angular dada $\omega$, viene dado por (8.85), entonces los modos relevantes del sistema infinito son los de (8.87), y debemos encontrar una combinación lineal de estos dos que satisfaga (8.89). La respuesta es

$$\tilde\psi(x,t) = A\left[\frac{e^{i(k_r+ik_i)x}-e^{-i(k_r+ik_i)x}}{e^{i(k_r+ik_i)L}-e^{-i(k_r+ik_i)L}}\right]e^{-i\omega t}\,. \qquad \text{(8.91)}$$

El factor entre corchetes está construido para anularse en $x=0$ y valer 1 en $x=L$.

Para una cuerda continua, la solución (8.91) se anima en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-4" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-4</a>. Lo interesante de esto es que, cerca del extremo $x=L$, la solución se parece a una onda viajera. La razón es que ahí los factores exponenciales reales de (8.91) refuerzan la onda que se mueve hacia la izquierda y suprimen la que se mueve hacia la derecha, de modo que la solución es casi exactamente una onda viajera moviéndose hacia la izquierda. Por otro lado, cerca de $x=0$, los factores exponenciales reales son comparables, y la solución es casi exactamente una onda estacionaria. Discutiremos el comportamiento más complicado del medio en el próximo capítulo.

La misma solución funciona para una cuerda con cuentas (aunque la relación de dispersión será distinta). Un ejemplo se muestra en la animación del programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-5" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-5</a>. Ahí puede ver muy claramente que las partes del sistema no están todas en fase.

## 8.6 Cortes de frecuencia altos y bajos

### 8.6.1 Más sobre péndulos acoplados

*(Referencia al programa interactivo 8-6 del disco de programas del curso original.)*

En la sección anterior, vimos cómo el número de onda angular, $k$, puede volverse complejo en un sistema con fricción. Hay otra forma importante en la que $k$ puede volverse complejo. Considere la relación de dispersión del sistema de péndulos acoplados, (5.35), que podemos reescribir así:

$$\omega^2 = \omega_\ell^2 + \omega_c^2\sin^2\frac{ka}{2}\,. \qquad \text{(8.92)}$$

Aquí $a$ es la distancia entre bloques, $\omega_\ell$ es la frecuencia de un único péndulo no acoplado, y $\omega_c^2$ es una frecuencia asociada al acoplamiento entre bloques vecinos,

$$\omega_c^2 = \frac{4K}{m} \qquad \text{(8.93)}$$

donde $m$ es la masa de un bloque y $K$ es la constante de los muelles de acoplamiento.

Las ondas viajeras en un sistema con una relación de dispersión como (8.92) se animan en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-6" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-6</a>. Para hacer la física más fácil de ver, este sistema es una cuerda con cuentas con oscilaciones transversales. Sin embargo, para producir el término $\omega_\ell^2$ de (8.92), también hemos unido cada cuenta mediante un muelle a una posición de equilibrio a lo largo de la línea punteada. En este caso, el acoplamiento entre cuentas proviene de la cuerda, así que el análogo de (8.93) es

$$\omega_c^2 = \frac{4T}{ma}\,. \qquad \text{(8.94)}$$

Los parámetros del sistema se eligen de modo que, en términos de una frecuencia de referencia, $\omega_0$,

$$\omega_\ell^2 = 25\omega_0^2\,,\qquad \omega_c^2 = 24\omega_0^2\,. \qquad \text{(8.95)}$$

Las propiedades de las ondas en este sistema difieren dramáticamente en función de $\omega$. Una forma de verlo es ir hacia atrás y notar que, para $k$ real, como $\sin^2(ka/2)$ debe estar entre 0 y 1, $\omega$ está restringida,

$$\omega_\ell \le \omega \le \sqrt{\omega_\ell^2+\omega_c^2} \equiv \omega_h\,. \qquad \text{(8.96)}$$

Para $k$ en esta región «permitida»,

$$\sin^2\frac{ka}{2} = \frac{\omega^2-\omega_\ell^2}{\omega_c^2} \qquad \text{(8.97)}$$

está entre 0 y 1, al igual que

$$\cos^2\frac{ka}{2} = \frac{\omega_h^2-\omega^2}{\omega_c^2}\,. \qquad \text{(8.98)}$$

Las dos frecuencias, $\omega_\ell$ y $\omega_h$, se llaman cortes de frecuencia baja y alta. El sistema de péndulos acoplados solo admite ondas viajeras para frecuencias $\omega$ entre los cortes de frecuencia alta y baja. Es solo en esta región donde la relación de dispersión puede satisfacerse con $\omega$ y $k$ reales. Para $\omega<\omega_\ell$ o $\omega>\omega_h$, el sistema oscila, pero no hay nada parecido a una onda viajera. Puede verlo en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-6" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-6</a>, cambiando la frecuencia hacia arriba y hacia abajo con las teclas de flecha.

Para cualquier $\omega$, siempre podemos resolver la relación de dispersión. Sin embargo, en algunas regiones de frecuencia, el resultado será complejo, como en (8.85). Esperamos $k_i=0$ en la región permitida, (8.96). La solución de (8.92) para $k_r$ y $k_i$ en función de $\omega$ se muestra en las gráficas de la figura 8.12. Aquí, $k_r$ y $k_i$ se representan frente a $\omega$ para la relación de dispersión, (8.92), con $\omega_\ell=5\omega_0$ y $\omega_h=7\omega_0$. $k_i$ es la línea punteada. Note la dependencia muy rápida de $k_i$ cerca de los cortes de frecuencia alta y baja.

![Figura 8.12](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh8_ES/fig8.12.png)

Figura 8.12: $k_ra$ y $k_ia$ en función de $\omega$; en la región permitida entre $\omega_\ell$ y $\omega_h$, $k_r$ crece suavemente de $0$ a $\pi/a$ mientras $k_i=0$; fuera de esa región, $k_i$ crece rápidamente desde cero mientras $k_r$ permanece en $0$ o $\pi/a$.

A medida que $\omega$ disminuye, en la región permitida (8.96), $\sin(ka/2)$ disminuye. En el corte de frecuencia baja, $\omega=\omega_\ell$, $\sin(ka/2)$, y por tanto $k$, tiende a cero. Esto significa que, a medida que la frecuencia disminuye, la longitud de onda de las ondas viajeras se hace cada vez más larga, hasta que, en la frecuencia de corte, se vuelve infinita. En el corte de frecuencia baja, cada péndulo de la cadena infinita oscila en fase. Los muelles que los acoplan son entonces irrelevantes, porque siempre mantienen sus longitudes de equilibrio. Esto es posible precisamente porque $\omega_\ell$ es la frecuencia de oscilación del péndulo no acoplado, así que no se necesita acoplamiento para que un péndulo individual oscile a frecuencia $\omega_\ell$.

Si $\omega$ está por debajo del corte de frecuencia baja, $\omega_\ell$, $\sin^2(ka/2)$ debe volverse negativo para satisfacer la relación de dispersión, (8.92). Por tanto, $\sin(ka/2)$ debe ser un número puramente imaginario,

$$k = \pm ik_i\,. \qquad \text{(8.99)}$$

La solución general para la onda es entonces

$$\psi(x,t) = A\,e^{-k_ix}e^{-i\omega t} + B\,e^{k_ix}e^{-i\omega t}\,. \qquad \text{(8.100)}$$

En un sistema finito de péndulos acoplados, ambos términos pueden estar presentes. En un sistema semiinfinito impulsado en $x=0$ y que se extiende hasta $x\to\infty$, la constante $B$ debe anularse, para evitar un crecimiento exponencial de la onda en el infinito. Así, la onda cae exponencialmente para $x$ grande. Además, la solución es un producto de una función real de $x$ y una función exponencial compleja de $t$: esto es una onda estacionaria. No hay onda viajera. Puede verlo en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-6" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-6</a> a bajas frecuencias.

La física de esta oscilación por debajo del corte de frecuencia baja es particularmente clara en el límite extremo, $\omega\to0$. A frecuencia cero, no hay movimiento. El análogo de un problema de oscilación forzada es simplemente desplazar un péndulo respecto al equilibrio y observar qué le ocurre al resto. Claramente, lo que ocurre es que el desplazamiento del primer péndulo produce una fuerza sobre el siguiente, debida al muelle de acoplamiento, que lo aleja del equilibrio, pero no tanto como al primero. Su desplazamiento es menor que el del primero por cierto factor $\epsilon=e^{-k_ia}$. Entonces el segundo péndulo tira del tercero, pero de nuevo el desplazamiento es menor por el mismo factor. ¡Y así sucesivamente! En un sistema infinito, esto da lugar al desplazamiento exponencialmente decreciente de (8.100), con $B=0$. A medida que la frecuencia aumenta, el efecto de la inercia (más precisamente, el término $ma$ en $F=ma$) aumenta el desplazamiento del segundo bloque (y de cada uno de los siguientes), hasta que, por encima del corte de frecuencia baja, el efecto de la inercia es lo bastante grande como para competir en pie de igualdad con el efecto de la fuerza restauradora, y puede producirse una verdadera onda viajera.

El corte de frecuencia baja no es peculiar del sistema discreto: ocurre siempre que hay una fuerza restauradora para $k=0$ en el sistema infinito. Más adelante, en el capítulo 11, veremos que un fenómeno similar puede ocurrir en sistemas bidimensionales y tridimensionales, incluso cuando no hay fuerza restauradora en $k=0$.

El corte de frecuencia alta, en cambio, depende de la separación finita entre bloques. A medida que $\omega$ aumenta, en la región permitida (8.96), $\sin(ka/2)$ aumenta, $k$ aumenta, y por tanto $\cos(ka/2)$ disminuye. En el corte de frecuencia alta, $\omega=\omega_h$, $\sin(ka/2)=1$ y $\cos(ka/2)=0$. Pero

$$\sin\frac{ka}{2}=1 \implies k=\frac{\pi}{a} \qquad \text{(8.101)}$$

lo que a su vez significa

$$e^{ika}=e^{-ika}=-1\,. \qquad \text{(8.102)}$$

Así, el desplazamiento de los bloques simplemente alterna, porque

$$\psi_j = \psi(ja,t) \propto e^{ij\pi} = (-1)^j\,. \qquad \text{(8.103)}$$

Esto es lo más ondulado que puede llegar a ser el sistema discreto. En un sistema discreto con separación entre bloques $a$, la máxima parte real posible de $k$ es $\pi/a$ (porque $k$ puede redefinirse en un múltiplo de $2\pi/a$ sin cambiar los desplazamientos de ninguno de los bloques —véase (5.28)). Esta cota es el origen del corte de frecuencia alta.

Puede verlo en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-6" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-6</a>. La frecuencia empieza en $6\omega_0$; en este punto, $k_ra$ es bastante pequeño (y $k_i=0$), y la onda se ve suave. A medida que la frecuencia aumenta hacia $\omega_h$, la onda se ve cada vez más dentada, hasta que, en $\omega=\omega_h$, las cuentas vecinas se mueven en direcciones opuestas.

Para $\omega>\omega_h$, $\sin(ka/2)$ es mayor que 1, y $\cos(ka/2)$ es negativo. Esto implica que $k$ tiene la forma

$$k = \frac{\pi}{a} \pm ik_i\,. \qquad \text{(8.104)}$$

Entonces la solución general para el desplazamiento es

$$\psi(x,t) = A\,e^{-k_ix}e^{i\pi x/a}e^{-i\omega t} + B\,e^{k_ix}e^{i\pi x/a}e^{-i\omega t}\,. \qquad \text{(8.105)}$$

Como en (8.100), hay un término que decae exponencialmente y otro que crece exponencialmente. Aquí, sin embargo, hay también un factor de fase, $e^{i\pi x/a}$, que parece que pudiera dar lugar a una onda viajera. Pero, de hecho, esto no es realmente una fase: simplemente produce la alternancia del desplazamiento de un bloque al siguiente. Vemos esto si solo miramos los desplazamientos de los bloques (como en (8.103)):

$$\psi_j = \psi(ja,t) = A(-1)^je^{-k_ix}e^{-i\omega t} + B(-1)^je^{k_ix}e^{-i\omega t}\,. \qquad \text{(8.106)}$$

Como en (8.100), en un sistema semiinfinito que se extiende hasta $x\to\infty$, debemos tener $B=0$, y no hay onda viajera.

Una de las cosas llamativas del programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-8-6" rel="noopener" target="_blank" title="Animación original de Howard Georgi">8-6</a> es el cambio muy rápido de una solución de onda viajera en la región permitida a una solución de onda estacionaria con decaimiento exponencial rápido de la amplitud en las regiones de frecuencia alta y baja. Esto también se ve en la figura 8.12, en el cambio rápido de $k_i$ cerca de los cortes. La razón es que $k$ tiene una dependencia en raíz cuadrada de la frecuencia cerca de los cortes.

En el sistema infinito, la solución fuera de la región permitida es una onda estacionaria pura. En ausencia de amortiguamiento, el trabajo realizado por la fuerza que produce la onda se promedia a cero con el tiempo. En un sistema finito, sin embargo, es posible transferir energía de un extremo del sistema al otro, incluso por debajo del corte de frecuencia baja o por encima del corte de frecuencia alta. La razón es que, en un sistema finito, tanto el término $A$ como el $B$ de (8.100) (o (8.106)) pueden ser no nulos. Si $A$ y $B$ son ambos reales (o «relativamente reales», es decir, tienen la misma fase), no hay transferencia de energía: la solución es el producto de una función real de $x$ (o $j$) y una función exponencial oscilante de $t$, así que se ve como una onda estacionaria. Sin embargo, si $A$ y $B$ tienen fases distintas, la oscilación se parece a una onda viajera y puede transferirse energía. Este proceso se vuelve exponencialmente menos eficiente a medida que aumenta la longitud del sistema. Discutiremos esto con más detalle en el capítulo 11.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Construir modos de onda viajera de un sistema infinito invariante bajo traslación;

2.  Descomponer una onda viajera en un par de ondas estacionarias, y una onda estacionaria en un par de ondas viajeras «moviéndose» en direcciones opuestas;

3.  Resolver problemas de oscilación forzada con soluciones de onda viajera y calcular las fuerzas que actúan sobre el sistema;

4.  Calcular la potencia y la potencia media necesarias para producir una onda, y definir y calcular la impedancia;

5.  Analizar sistemas invariantes bajo traslación con amortiguamiento;

6.  Entender los orígenes físicos de los cortes de frecuencia alta y baja, y poder analizar el comportamiento de sistemas impulsados por encima y por debajo de las frecuencias de corte.

## Problemas

**8.1.** Una cuerda infinita con tensión $T$ y densidad de masa lineal $\rho$ está estirada a lo largo del eje $x$. Se aplica una fuerza en la dirección $y$ en $x=0$, de modo que la cuerda en $x=0$ oscila en la dirección $y$ con desplazamiento

$$A(t) = D\cos\omega t\,.$$

Esto produce dos ondas viajeras que se alejan de $x=0$ en las direcciones $\pm x$.

1.  Encuentre la fuerza aplicada en $x=0$.

2.  Encuentre la potencia media suministrada por la fuerza.

**8.2.** Para el aire en condiciones normales de temperatura y presión, la presión es $1.01\times10^6\ \text{dyn/cm}^2$, la densidad es $1.29\times10^{-3}\ \text{g/cm}^3$. Use estos valores para encontrar la amplitud de desplazamiento de las ondas sonoras con una frecuencia de 440 ciclos/s (hercios), que transportan una potencia por unidad de área de $10^{-3}\ \text{W/cm}^2$.

**8.3.** Considere el siguiente circuito: seis nodos con voltajes $V_0$ a $V_6$, conectados en cadena por inductores idénticos, con condensadores idénticos a tierra y una resistencia en cada tramo.

Todos los condensadores tienen la misma capacitancia, $C\approx0.00667\ \mu\text{F}$, y todos los inductores tienen la misma inductancia, $L\approx150\ \mu\text{H}$, y la misma resistencia, $R\approx15\ \Omega$ (este es el mismo problema que (5.4), pero con resistencia no nula). El hilo de abajo está conectado a tierra, de modo que $V_0=0$. Este circuito es un análogo eléctrico de los sistemas invariantes bajo traslación de osciladores mecánicos acoplados que hemos discutido en este capítulo.

1.  Demuestre que la relación de dispersión de este sistema es

$$\omega^2 + i\omega\frac{R}{L} = \frac{2}{LC}(1-\cos ka)\,.$$

Cuando aplica una señal oscilante armónicamente desde un generador de señales, a través de un cable coaxial, a $V_6$, se inducen distintos voltajes oscilantes a lo largo de la línea. Es decir, si

$$V_6(t) = V\cos\omega t\,,$$

entonces $V_j(t)$ tiene la forma

$$V_j(t) = A_j\cos\omega t + B_j\sin\omega t\,.$$

1.  Encuentre $A_1$, $B_1$ y $|A_1+iB_1|$, y grafique cada uno en función de $\omega$, desde $\omega=0$ hasta $2/\sqrt{LC}$. No se preocupe por simplificar expresiones complicadas, siempre que pueda graficarlas. ¿Cuántas de las resonancias puede identificar en cada una de las gráficas? Pista: use la identidad trigonométrica del problema 1.2e,

$$\sin6x = \sin x\left(32\cos^5x-32\cos^3x+6\cos x\right)$$

para expresar $A_1+iB_1$ en términos de $\cos ka$. Note que esta identidad es cierta incluso si $x$ es un número complejo. Luego use la relación de dispersión para expresar $\cos ka$ en términos de $\omega$. Encuentre $A_1$ y $B_1$ tomando las partes real e imaginaria de $A_1+iB_1$. Finalmente, programe un ordenador para construir las gráficas.

1.  Encuentre las posiciones de las resonancias directamente, usando los argumentos del capítulo 5, y demuestre que están donde se esperaría.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.


---

<!-- MIT8.03_TextCh9_ES.md -->

# Capítulo 9: La frontera en el infinito

Aunque los fenómenos ondulatorios que podemos observar en el laboratorio viven en regiones finitas del espacio, a menudo es conveniente analizarlos como si las ondas viajeras vinieran del infinito y se fueran hacia el infinito. Hemos descrito ondas viajeras en sistemas infinitos invariantes bajo traslación. Pero las ondas viajeras son más complicadas y más interesantes en sistemas que tienen fronteras que rompen la simetría de traslación.

## Vídeos de esta clase (YouTube)

- [Clase 12: Ecuaciones de Maxwell, ondas electromagnéticas](https://www.youtube.com/watch?v=8kcvyoHsXrw)
- [Clase 13: Medio dispersivo, velocidad de fase, velocidad de grupo](https://www.youtube.com/watch?v=QxemLb8-5AA)

## Resumen previo

En este capítulo introducimos un nuevo tipo de «condición de contorno» en sistemas que carecen de frontera. Nos permitirá discutir la reflexión y la transmisión, y en general, el fenómeno de la dispersión (*scattering*).

1.  Discutimos problemas de oscilación forzada en sistemas semiinfinitos, que se extienden hasta el infinito en una dirección. Mostramos que podemos imponer una «condición de contorno» aunque no haya frontera, especificando la amplitud de una onda que viaja en una dirección. Después discutimos problemas de dispersión en sistemas infinitos, describiendo las amplitudes de transmisión y reflexión. Estudiamos el movimiento de una onda general con frecuencia definida.

2.  Discutimos ondas planas electromagnéticas en un dieléctrico.

3.  Discutimos la reflexión y transmisión de una masa sobre una cuerda y de dos masas sobre una cuerda, mostrando cómo usar una «matriz de transferencia» para simplificar la solución del problema de dispersión. Analizamos la reflexión en la frontera entre regiones con distinto número de onda, y mostramos cómo eliminar la reflexión con un «recubrimiento antirreflectante» adecuado.

## 9.1 Reflexión y transmisión

### 9.1.1 Oscilación forzada

Considere el problema de oscilación forzada en una cuerda estirada semiinfinita que va de $x=0$ a $x=\infty$. Suponga que

$$\psi(0,t) = A\cos\omega t\,. \qquad \text{(9.1)}$$

¿Cuál es entonces $\psi(x,t)$? Este no es un problema bien planteado, porque solo tenemos una condición de contorno en un lado. Además, $\psi(\infty,t)$ no tiene un valor definido: solo podemos hablar del valor de una función en el infinito si la función tiende a un valor constante. Aquí esperamos que $\psi(x,t)$ siga oscilando cuando $x\to\infty$, así que no podemos especificarlo. En su lugar, podemos especificar la onda viajera entrante (que viaja hacia la frontera en $x=0$, en la dirección $-x$) o la saliente (que viaja alejándose de $x=0$, en la dirección $+x$) del sistema. Esto se llama una «condición de contorno en el infinito».

Por ejemplo, podríamos tomar como condición de contorno en el infinito que no aparezcan ondas viajeras entrantes en la cuerda. Físicamente, esto corresponde a la situación en la que el movimiento de la cuerda en $x=0$ es lo que produce las ondas. En general, podemos escribir una solución con frecuencia angular $\omega$ como una suma de cuatro ondas viajeras reales:

$$\psi(x,t) = a\cos(kx-\omega t) + b\sin(kx-\omega t) + c\cos(kx+\omega t) + d\sin(kx+\omega t)\,. \qquad \text{(9.2)}$$

Entonces (9.1) implica

$$a+c=A\,,\qquad b-d=0\,, \qquad \text{(9.3)}$$

y la condición de contorno en el infinito implica

$$c=d=0\,. \qquad \text{(9.4)}$$

Así,

$$\psi(x,t) = A\cos(kx-\omega t)\,. \qquad \text{(9.5)}$$

### 9.1.2 Sistemas infinitos

Considere ahora dos cuerdas semiinfinitas con la misma tensión pero distintas densidades, unidas entre sí en $x=0$, como se muestra en la figura 9.1. Suponga que en la región $x\le0$ (Región I) hay una onda viajera entrante con amplitud $A$ y frecuencia angular $\omega$, y que en la región $x\ge0$ (Región II) no hay onda entrante. Esto describe una situación física en la que la onda entrante en I se dispersa en la frontera, de modo que las demás ondas son una onda transmitida en II y una onda reflejada en I, ambas salientes.

![Figura 9.1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh9_ES/fig9.1.png)

Figura 9.1: dos cuerdas semiinfinitas unidas en $x=0$; en la región I, a la izquierda, hay una onda entrante hacia la derecha y una reflejada hacia la izquierda; en la región II, a la derecha, hay una onda transmitida hacia la derecha.

La clave de este problema es pensarlo como un problema de oscilación forzada. La onda viajera entrante en la región I es lo que «causa» todas las oscilaciones (ponemos la palabra entre comillas, porque la forma armónica, $e^{-i\omega t}$, de la oscilación implica que ha estado ocurriendo desde siempre, así que un filósofo podría cuestionar este uso de causa y efecto; sin embargo, nos ayudará pensarlo así). Si las ondas reflejada y transmitida son producidas por la onda entrante, sus amplitudes también serán proporcionales a $e^{-i\omega t}$. Como en un problema de oscilación forzada convencional, podríamos añadir cualquier oscilación libre del sistema; sin embargo, si hay algo de fricción, estas se extinguirán con el tiempo, y nos quedará solo la oscilación producida por la onda viajera entrante, proporcional a $e^{-i\omega t}$. Lo importante es que la frecuencia es la misma en ambas regiones, porque, como en un problema de oscilación forzada, la frecuencia la impone al sistema un agente externo, en este caso, lo que sea que haya producido la onda viajera entrante.

En nuestra notación exponencial compleja, en la que todo tiene la dependencia temporal irreducible $e^{-i\omega t}$, las ondas que se mueven hacia la derecha son $\propto e^{ikx}e^{-i\omega t}$ y las que se mueven hacia la izquierda son $\propto e^{-ikx}e^{-i\omega t}$. En este caso, las condiciones de contorno en $\pm\infty$ exigen que

$$\psi(x,t) = e^{ikx}Ae^{-i\omega t} + R\,Ae^{-ikx}e^{-i\omega t} \qquad \text{(9.6)}$$

para $x\le0$ en la Región I, y

$$\psi(x,t) = \tau\,Ae^{ik'x}e^{-i\omega t} \qquad \text{(9.7)}$$

para $x\ge0$ en la Región II. $k$ y $k'$ son

$$k = \omega\sqrt{\rho_I/T}\,,\qquad k' = \omega\sqrt{\rho_{II}/T}\,, \qquad \text{(9.8)}$$

y $R$ y $\tau$ son (en general) números complejos que determinan las ondas reflejada y transmitida. A veces se llaman el «coeficiente de reflexión» y el «coeficiente de transmisión», o las «amplitudes» de transmisión y reflexión. Note que hemos definido los coeficientes de reflexión y transmisión extrayendo un factor de la amplitud, $A$, de la onda entrante. La amplitud, $A$, desaparece entonces de todas las condiciones de contorno, y los coeficientes adimensionales $R$ y $\tau$ son independientes de $A$. Esto debe ser así por la linealidad del sistema. Sabemos que, una vez encontrada la solución, $\psi(x,t)$, para una amplitud entrante $A$, podemos encontrar la solución para una amplitud entrante $B$ multiplicando nuestra solución por $B/A$. Mantendremos el parámetro $A$ en nuestras expresiones de $\psi(x,t)$, sobre todo para que las unidades cuadren correctamente. $A$ tiene unidades de longitud en este ejemplo, pero en general la amplitud de la onda entrante tendrá unidades de desplazamiento generalizado (como en (1.107) y (1.108)).

Para determinar $R$ y $\tau$, necesitamos una condición de contorno en $x=0$, donde se encuentran (9.6) y (9.7). Claramente $\psi(x,t)$ debe ser continua en $x=0$, así,

$$1+R=\tau\,. \qquad \text{(9.9)}$$

Hemos cancelado el factor común $Ae^{-i\omega t}$ en ambos lados. La derivada en $x$ también debe ser continua (para un nudo sin masa), porque las fuerzas verticales sobre el nudo deben equilibrarse, así,

$$ik(1-R) = ik'\tau\,. \qquad \text{(9.10)}$$

Resolviendo para $R$ y $\tau$, obtenemos

$$\tau = \frac{2}{1+k'/k}\,,\qquad R = \frac{1-k'/k}{1+k'/k}\,. \qquad \text{(9.11)}$$

### 9.1.3 Acoplamiento de impedancias

Note que podríamos reemplazar la cuerda de la Región II por un amortiguador con la misma impedancia, $Z_{II}$. Esto debe ser cierto por la naturaleza local de las interacciones: lo único que «sabe» la cuerda para $x<0$ sobre la cuerda para $x>0$ es que esta ejerce una fuerza en $x=0$ igual a

$$-Z_{II}\,\frac{\partial}{\partial t}\psi(0,t)\,. \qquad \text{(9.12)}$$

Así, también hemos aprendido qué ocurre cuando una onda entrante encuentra un amortiguador con la impedancia incorrecta: la amplitud de la onda reflejada viene dada por $R$ en (9.11).

La onda reflejada de (9.11) se anula si $k=k'$. Si $k=k'$, entonces $\rho_I=\rho_{II}$ (de (9.8)), y la impedancia en la región I es igual a la de la región II. Este es un ejemplo simple del importante principio del «acoplamiento de impedancias»: no hay reflexión si la impedancia del sistema en la región II es igual a la del sistema en la región I. El argumento es el mismo que el del amortiguador del párrafo anterior. Lo que importa en el cálculo del coeficiente de reflexión son las fuerzas que actúan sobre la cuerda en $x=0$; esas fuerzas están determinadas por las impedancias en las dos regiones, y nada más importa. Considere, por ejemplo, el sistema mostrado en la figura 9.2, de dos cuerdas semiinfinitas conectadas en $x=0$ a un anillo sin masa que puede deslizar en la dirección vertical sobre una varilla sin fricción. La varilla puede ejercer una fuerza horizontal sobre el anillo, así que las tensiones de las dos cuerdas no tienen por qué ser iguales. En tal sistema, podemos cambiar tanto la densidad como la tensión de la cuerda de la región I a la región II. No habrá reflexión mientras el producto de la densidad de masa lineal y la tensión (y por tanto la impedancia, de (8.22)) sea el mismo en ambas regiones,

$$Z_I = \sqrt{\rho_IT_I} = \sqrt{\rho_{II}T_{II}} = Z_{II}\,. \qquad \text{(9.13)}$$

![Figura 9.2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh9_ES/fig9.2.png)

Figura 9.2: dos cuerdas semiinfinitas unidas en $x=0$ a un anillo sin masa que desliza verticalmente sobre una varilla sin fricción, permitiendo que las tensiones de ambas cuerdas sean distintas.

Es instructivo resolver completamente el problema de dispersión para el caso más general de la figura 9.2. Esto nos dará una idea del significado de la impedancia. La forma de la solución, (9.6) y (9.7), no cambia, pero ahora los números de onda angulares satisfacen

$$k = \omega\sqrt{\rho_I/T_I}\,,\qquad k' = \omega\sqrt{\rho_{II}/T_{II}}\,. \qquad \text{(9.14)}$$

La condición de contorno en $x=0$ que surge de la continuidad de la cuerda, (9.9), permanece sin cambios. Sin embargo, (9.10) surgió del hecho de que las fuerzas sobre el nudo sin masa deben sumar cero, para que la aceleración no sea infinita. En este caso, de (8.21), la contribución de cada componente de la onda a la fuerza total es proporcional a más o menos la impedancia en la región correspondiente, según se mueva en la dirección $+x$ o $-x$. Así, la condición de contorno es

$$Z_I(1-R) = Z_{II}\tau\,. \qquad \text{(9.15)}$$

Entonces los coeficientes de reflexión y transmisión son

$$\tau = \frac{2Z_I}{Z_I+Z_{II}}\,,\qquad R = \frac{Z_I-Z_{II}}{Z_I+Z_{II}}\,. \qquad \text{(9.16)}$$

Ya hemos discutido el caso en que las impedancias coinciden y el coeficiente de reflexión se anula. También es interesante examinar los límites en los que $R=\pm1$. Considere primero el límite en el que la impedancia de la región II tiende a infinito,

$$\lim_{Z_{II}\to\infty}R = -1\,. \qquad \text{(9.17)}$$

Esta es la situación en la que se necesitaría una fuerza infinita para producir una onda en la región II. Así, la cuerda de la región II no se mueve en absoluto, y en particular el punto $x=0$ bien podría ser un extremo fijo. La solución, (9.17), garantiza que la cuerda no se mueve en $x=0$, y por tanto que la solución en la región I es $\psi(x,t)\propto\sin kx$. Esta solución es una onda estacionaria infinita con condición de contorno de extremo fijo.

En el límite opuesto, en el que la impedancia de la región II es cero, obtenemos

$$\lim_{Z_{II}\to0}R = 1\,. \qquad \text{(9.18)}$$

Esta vez, no se necesita ninguna fuerza para producir una onda en la región II. Así, el extremo de la región I en $x=0$ no siente ninguna fuerza transversal: actúa como un extremo libre. La solución, (9.18), garantiza que $\psi(x,t)\propto\cos kx$ en la región I, de modo que la pendiente de la cuerda se anula en $x=0$. Esta solución es una onda estacionaria infinita con condición de contorno de extremo libre.

### 9.1.4 Observando las ondas reflejadas

*(Referencia al programa interactivo 9-1 del disco de programas del curso original.)*

En esta sección discutimos qué aspecto tiene el desplazamiento en la Región I. Encontraremos un diagnóstico útil para la presencia de reflexión, y concluiremos también que las ondas estacionarias son muy especiales.

Considere una onda de la forma

$$A\cos(kx-\omega t) + R\,A\cos(kx+\omega t)\,. \qquad \text{(9.19)}$$

Esto describe una onda viajera entrante con cierta onda reflejada de amplitud $R$ (podríamos añadir una fase arbitraria para la onda reflejada, pero eso complicaría el álgebra sin cambiar la física).

Para $R=\pm1$, esto es una onda estacionaria. Para $R=0$, es una onda viajera. Para ver cómo el sistema interpola entre estos dos extremos, considere el movimiento de la cresta de la onda, un máximo de (9.19).

Para encontrar el máximo, derivamos respecto a $x$ e igualamos el resultado a cero. Eliminando el factor irrelevante de $A$, obtenemos

$$\sin(kx-\omega t) + R\sin(kx+\omega t) = 0\,, \qquad \text{(9.20)}$$

o

$$(1+R)\sin kx\cos\omega t = (1-R)\cos kx\sin\omega t\,, \qquad \text{(9.21)}$$

o

$$\tan kx = \frac{1-R}{1+R}\tan\omega t\,. \qquad \text{(9.22)}$$

(9.22) describe (implícitamente —podríamos resolver para $x$ en función de $t$ si quisiéramos) el movimiento del máximo en función del tiempo. Podemos derivarla para obtener la velocidad:

$$k\left(1+\tan^2kx\right)\frac{\partial x}{\partial t} = \frac{1-R}{1+R}\,\frac{\omega}{\cos^2\omega t}\,. \qquad \text{(9.23)}$$

Hemos dejado $(1+\tan^2kx)$ en (9.23) para poder eliminarlo usando (9.22). Así,

$$\begin{aligned}
\frac{\partial x}{\partial t} &= \frac{1-R}{1+R}\,\frac{\omega}{k}\,\frac{1}{\left(1+\tan^2kx\right)\cos^2\omega t}\\
&= \frac{1-R}{1+R}\,\frac{\omega}{k}\,\frac{1}{\left(1+\left(\frac{1-R}{1+R}\right)^2\tan^2\omega t\right)\cos^2\omega t}\\
&= v\,\frac{(1+R)(1-R)}{(1+R)^2\cos^2\omega t+(1-R)^2\sin^2\omega t} \qquad \text{(9.24)}
\end{aligned}$$

donde $v=\omega/k$ es la velocidad de fase. Cuando $\sin\omega t$ se anula, la velocidad del máximo es menor que la velocidad de fase por un factor

$$\frac{1-R}{1+R}\,, \qquad \text{(9.25)}$$

mientras que, cuando $\cos\omega t$ se anula, la velocidad es mayor que $v$ por el factor inverso,

$$\frac{1+R}{1-R}\,. \qquad \text{(9.26)}$$

Así, la onda parece moverse a trompicones. Puede ver este efecto fácilmente si observa un sistema con mucha reflexión. El efecto se ilustra en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-9-1" rel="noopener" target="_blank" title="Animación original de Howard Georgi">9-1</a>.

Podemos extraer una lección más general de esta discusión. El caso general de movimiento ondulatorio se parece mucho más a una onda viajera que a una onda estacionaria. Genéricamente, salvo para $R=\pm1$, las crestas de la onda se mueven con el tiempo. A medida que nos acercamos a $R=\pm1$, una de las dos velocidades de (9.25) y (9.26) tiende a cero y la otra a infinito. Lo que ocurre cuando estamos cerca de $R=\pm1$ es entonces que la onda permanece casi quieta la mayor parte del tiempo, y luego se mueve muy rápidamente a la siguiente posición casi estacionaria. Una onda estacionaria es así un caso especial degenerado de una onda viajera, en el que este movimiento es inobservable porque, en cierto sentido, es infinitamente rápido.

### 9.1.5 Potencia y reflexión

Es instructivo considerar la potencia necesaria para producir una onda viajera que se refleja parcialmente. Es decir, consideramos la potencia que requiere una fuerza transversal actuando en $x=0$ para producir una onda en la región $x>0$ que es una combinación lineal de una onda saliente moviéndose en la dirección $+x$ y una onda entrante moviéndose en la dirección $-x$, como podría producirse por una reflexión en algún valor grande de $x$. Consideremos el caso unidimensional más general, en un medio con impedancia $Z$:

$$\begin{aligned}
\psi(x,t) &= \text{Re}\left(A_+e^{i(kx-\omega t)}+A_-e^{i(-kx-\omega t)}\right)\\
&= R_+\cos(kx-\omega t+\varphi_+) + R_-\cos(-kx-\omega t+\varphi_-) \qquad \text{(9.27)}
\end{aligned}$$

donde $R_\pm$ y $\varphi_\pm$ son el valor absoluto y la fase de la amplitud $A_\pm$. La velocidad es

$$\frac{\partial}{\partial t}\psi(x,t) = \omega R_+\sin(kx-\omega t+\varphi_+) + \omega R_-\sin(-kx-\omega t+\varphi_-)\,. \qquad \text{(9.28)}$$

Ahora bien, como (9.27) involucra ondas que viajan tanto en la dirección $+x$ como en la $-x$, no podemos encontrar la fuerza necesaria para producir la onda en el punto $x$ simplemente multiplicando (9.28) por la impedancia, $Z$. Sin embargo, podemos usar la linealidad. Podemos escribir $\psi(x,t)=\psi_+(x,t)+\psi_-(x,t)$, donde $\psi_\pm(x,t)$ es la onda que se mueve en la dirección $\pm x$. Entonces, de (8.21), la fuerza necesaria para producir $\psi_+$ es

$$F_+(t) = Z\,\frac{\partial}{\partial t}\psi_+(0,t) \qquad \text{(9.29)}$$

mientras que la fuerza necesaria para producir $\psi_-$ es

$$F_-(t) = -Z\,\frac{\partial}{\partial t}\psi_-(0,t)\,. \qquad \text{(9.30)}$$

Entonces la fuerza total necesaria para producir $\psi$ es

$$F(t) = F_+(t)+F_-(t) = Z\omega R_+\sin(-\omega t+\varphi_+) - Z\omega R_-\sin(-\omega t+\varphi_-)\,. \qquad \text{(9.31)}$$

Así, la potencia necesaria es

$$P(t) = F(t)\,\left.\frac{\partial}{\partial t}\psi(x,t)\right|_{x=0} = Z\omega^2R_+^2\sin^2(-\omega t+\varphi_+) - Z\omega^2R_-^2\sin^2(-\omega t+\varphi_-)\,. \qquad \text{(9.32)}$$

La potencia media viene entonces dada por

$$P_{\text{prom}} = \frac{1}{2}Z\omega^2(R_+^2-R_-^2) = \frac{1}{2}Z\omega^2\left(|A_+|^2-|A_-|^2\right)\,. \qquad \text{(9.33)}$$

El resultado, (9.32), tiene una interpretación física obvia e importante. Se necesita potencia positiva para producir la onda saliente, mientras que la onda entrante devuelve energía al sistema, y por tanto requiere potencia negativa. La potencia necesaria para producir una onda viajera general es, por tanto, proporcional a la diferencia de los cuadrados de los valores absolutos de las amplitudes de las ondas saliente y entrante.

Note también que podemos aplicar esta discusión al ejemplo de la reflexión en una frontera, discutido arriba: podemos comprobar que la energía se conserva en esta dispersión. La potencia media necesaria para producir la onda en la región I es, de (9.33),

$$ZI\omega^2 - ZI\omega^2R^2\,. \qquad \text{(9.34)}$$

La potencia media necesaria para producir la onda en la región II es

$$Z_{II}\omega^2\tau^2\,. \qquad \text{(9.35)}$$

Usando (9.16), puede comprobar que estas son iguales.

### 9.1.6 Una masa sobre una cuerda

*(Referencia al programa interactivo 9-2 del disco de programas del curso original.)*

![Figura 9.3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh9_ES/fig9.3.png)

Figura 9.3: una masa $m$ en $x=0$ sobre una cuerda infinita, con una onda entrante de amplitud 1 desde la izquierda, una onda reflejada $R$ hacia la izquierda y una onda transmitida $\tau$ hacia la derecha.

Considere la transmisión y reflexión de ondas debidas a una masa, $m$, en $x=0$, sobre una cuerda con densidad de masa lineal $\rho$ y tensión $T$, estirada de $x=-\infty$ a $x=\infty$, mostrada en la figura 9.3. Antes de calcular los coeficientes de reflexión y transmisión, adivinemos el resultado en dos límites extremos.

**$m$ pequeña** — Aquí esperamos que la reflexión sea pequeña y la transmisión cercana a uno, porque en el límite

$$m\to0 \implies \tau\to1 \text{ y } R\to0\,. \qquad \text{(9.36)}$$

**$m$ grande** — Aquí esperamos que la transmisión sea pequeña y la reflexión cercana a $-1$, porque en el límite

$$m\to\infty \implies \tau\to0 \text{ y } R\to-1\,. \qquad \text{(9.37)}$$

¡«Grande o pequeña comparada con qué», pregunta usted! Podemos responder eso por análisis dimensional. Los parámetros dimensionales relevantes son $m$, $\omega$, $k$, $\rho$ y $T$. Sin embargo, uno de ellos no es independiente, por la relación de dispersión, (6.5). Si usamos (6.5) para eliminar $T$, entonces $\omega$ no puede ser relevante para la pregunta, porque es lo único que queda que involucra la unidad de tiempo. La única cantidad adimensional que podemos construir es

$$\epsilon = \frac{mk}{\rho} = \frac{m\omega^2}{kT}\,. \qquad \text{(9.38)}$$

Ahora que hemos adivinado, podemos hacer el cálculo. Se sigue de la invariancia bajo traslación y de la condición de contorno en $x=\infty$ que

$$\psi(x,t) = Ae^{ikx}e^{-i\omega t} + R\,Ae^{-ikx}e^{-i\omega t} \quad\text{para } x\le0 \qquad \text{(9.39)}$$

$$\psi(x,t) = \tau\,Ae^{ikx}e^{-i\omega t} \quad\text{para } x\ge0 \qquad \text{(9.40)}$$

donde, como de costumbre, $R$ y $\tau$ son las «amplitudes» de las ondas reflejada y transmitida. Las condiciones de contorno son:

**continuidad** — El hecho de que la cuerda no se rompe implica que es continua, así que $\psi(0,t)$ puede calcularse con (9.39) o con (9.40). Esto implica

$$1+R=\tau\,. \qquad \text{(9.41)}$$

**$F=ma$** — La componente horizontal de la tensión de la cuerda debe ser igual en ambos lados; ambas son aproximadamente iguales a $T$, para pequeños desplazamientos. Sin embargo, si hay un doblez en la cuerda, las componentes verticales no coinciden, como se muestra en la figura 9.4 (véase también (8.16)-(8.17)). La fuerza sobre la masa es entonces la tensión por la pendiente para $x\ge0$ menos la tensión por la pendiente para $x\le0$, así que $F=ma$ se convierte en

$$T\left(\left.\frac{\partial}{\partial x}\psi(x,t)\right|_{x=0^+} - \left.\frac{\partial}{\partial x}\psi(x,t)\right|_{x=0^-}\right) = m\,\frac{\partial^2}{\partial t^2}\psi(0,t) \qquad \text{(9.42)}$$

o

$$ikT(R-1+\tau) = -m\omega^2\tau\,. \qquad \text{(9.43)}$$

Así,

$$1+R=\tau\,,\qquad 1-R = (1-i\epsilon)\tau\,, \qquad \text{(9.44)}$$

de modo que

$$\tau = \frac{2}{2-i\epsilon}\,,\qquad R = \frac{i\epsilon}{2-i\epsilon}\,. \qquad \text{(9.45)}$$

Claramente, esto concuerda con nuestra conjetura.

![Figura 9.4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh9_ES/fig9.4.png)

Figura 9.4: la fuerza sobre la masa debida al doblez de la cuerda, con la pendiente $\theta\approx\psi'$ a cada lado.

Note que estas amplitudes, a diferencia de las de (9.11), son números complejos. Las ondas transmitida y reflejada no tienen la misma fase que la onda entrante en la frontera. La diferencia de fase entre la onda transmitida (o reflejada) se llama un «desfase» (*phase shift*). Una característica interesante de la solución, (9.45), que no adivinamos, es que, para $\epsilon$ grande, la pequeña onda transmitida está desfasada $90°$ respecto a la onda entrante.

Esta dispersión se anima en el programa <a href="https://sites.harvard.edu/hgeorgi/wave-programs-9-2" rel="noopener" target="_blank" title="Animación original de Howard Georgi">9-2</a>. La solución también se descompone en ondas entrante, transmitida y reflejada. Observe la masa y vea si puede entender cómo se relaciona el doblez de la cuerda con su aceleración. También puede hacer la masa más grande o más pequeña para acercarse a los límites (9.36) y (9.37).

## 9.2 Índice de refracción

La materia está compuesta de cargas eléctricas. Esto es, en cierto modo, un milagro: no podemos entenderlo sin la mecánica cuántica. En un mundo puramente clásico, no habría átomos ni moléculas estables. Gracias a la mecánica cuántica, el mundo no colapsa y podemos construir trozos estables de materia compuestos por números iguales de cargas positivas y negativas. En un trozo de materia en equilibrio, la carga y la corriente son muy cercanas a cero cuando se promedian sobre cualquier región grande y suave. Sin embargo, en presencia de campos eléctricos y magnéticos externos, como los producidos por una onda electromagnética, las cargas de las que está hecha la materia pueden moverse. Esto da lugar a lo que se llaman cargas y corrientes «ligadas», distinguibles de las cargas «libres» que no forman parte de la materia misma. Estas cargas y corrientes ligadas afectan a la relación entre los campos eléctrico y magnético. En un material homogéneo e isótropo, que es una forma elegante de describir un material que no tiene ningún eje preferente, los efectos de la materia (promediados sobre regiones grandes) pueden incorporarse reemplazando las constantes $\epsilon_0$ y $\mu_0$ por la permitividad y la permeabilidad, $\epsilon$ y $\mu$. Entonces las ecuaciones de Maxwell para las ondas electromagnéticas, (8.35)-(8.37), se modifican así (véase, por ejemplo, Purcell, capítulo 10):

$$\begin{aligned}
\frac{\partial E_y}{\partial x}-\frac{\partial E_x}{\partial y} &= -\frac{\partial B_z}{\partial t}\,,\qquad \frac{\partial E_z}{\partial y}-\frac{\partial E_y}{\partial z} = -\frac{\partial B_x}{\partial t}\,,\\
\frac{\partial E_x}{\partial z}-\frac{\partial E_z}{\partial x} &= -\frac{\partial B_y}{\partial t}\,,
\end{aligned} \qquad \text{(9.46)}$$

$$\begin{aligned}
\frac{\partial B_y}{\partial x}-\frac{\partial B_x}{\partial y} &= \mu\epsilon\,\frac{\partial E_z}{\partial t}\,,\qquad \frac{\partial B_z}{\partial y}-\frac{\partial B_y}{\partial z} = \mu\epsilon\,\frac{\partial E_x}{\partial t}\,,\\
\frac{\partial B_x}{\partial z}-\frac{\partial B_z}{\partial x} &= \mu\epsilon\,\frac{\partial E_y}{\partial t}\,,
\end{aligned} \qquad \text{(9.47)}$$

$$\frac{\partial E_x}{\partial x}+\frac{\partial E_y}{\partial y}+\frac{\partial E_z}{\partial z}=0\,,\qquad \frac{\partial B_x}{\partial x}+\frac{\partial B_y}{\partial y}+\frac{\partial B_z}{\partial z}=0\,. \qquad \text{(9.48)}$$

Ahora (8.41)-(8.47) se satisfacen con las sustituciones apropiadas,

$$\epsilon_0\to\epsilon\,,\qquad \mu_0\to\mu\,. \qquad \text{(9.49)}$$

En particular, la relación de dispersión, (8.47), se convierte en

$$\omega^2 = \frac{1}{\mu\epsilon}\,k^2 = \frac{\mu_0\epsilon_0}{\mu\epsilon}\,c^2k^2\,. \qquad \text{(9.50)}$$

así que las ondas electromagnéticas se propagan con velocidad

$$v = \frac{\omega}{k} = c\sqrt{\frac{\mu_0\epsilon_0}{\mu\epsilon}}\,, \qquad \text{(9.51)}$$

y (8.48) se convierte en

$$\beta_y^\pm = \pm\sqrt{\mu\epsilon}\,\varepsilon_x^\pm\,,\qquad \beta_x^\pm = \mp\sqrt{\mu\epsilon}\,\varepsilon_y^\pm\,. \qquad \text{(9.52)}$$

El factor

$$n = \sqrt{\frac{\mu\epsilon}{\mu_0\epsilon_0}} \qquad \text{(9.53)}$$

se llama el índice de refracción del material. $1/n$ es el cociente entre la velocidad de la luz en el material y la velocidad de la luz en el vacío. En términos de $n$, podemos escribir (9.52) como

$$\beta_y^\pm = \pm\frac{n}{c}\,\varepsilon_x^\pm\,,\qquad \beta_x^\pm = \mp\frac{n}{c}\,\varepsilon_y^\pm\,. \qquad \text{(9.54)}$$

Note también que podemos reescribir (9.50) en la siguiente forma útil:

$$k = n\,\frac{\omega}{c}\,. \qquad \text{(9.55)}$$

Para frecuencia fija, el número de onda es proporcional al índice de refracción. Para la mayoría de los materiales transparentes, $\mu$ es muy cercano a 1 y puede ignorarse; pero $\epsilon$ puede ser muy distinto de 1, y a menudo es bastante importante. Por ejemplo, el índice de refracción del vidrio ordinario es aproximadamente 1.5 (varía ligeramente con la frecuencia, pero discutiremos las consecuencias interesantes y familiares de esto más adelante, cuando tratemos las ondas en tres dimensiones).

### 9.2.1 Reflexión en una frontera dieléctrica

Consideremos ahora una onda plana en la dirección $+z$, en un universo que está lleno de un material dieléctrico con índice de refracción $n=\sqrt{\epsilon/\epsilon_0}$ para $z<0$, y lleno de otro material dieléctrico con índice de refracción $n'=\sqrt{\epsilon'/\epsilon_0}$ para $z>0$. La frontera entre los dos dieléctricos, el plano $z=0$, es análoga a la frontera entre las dos regiones de la cuerda de la figura 9.1. Por tanto, esperaríamos algo de reflexión en esta superficie.

Como el campo eléctrico de una onda electromagnética plana es perpendicular a su dirección de movimiento, sabemos que en este caso está en el plano $x$-$y$. No importa en qué dirección apunte el campo eléctrico de nuestra onda plana incidente dentro del plano $x$-$y$; esto es claro por simetría. El sistema se ve igual si lo rotamos alrededor del eje $z$, así que siempre podemos rotar hasta que nuestro vector $\vec e_+$ apunte en alguna dirección conveniente, digamos la dirección $x$. Entonces es bastante obvio que las ondas reflejada y transmitida también tendrán sus campos eléctricos en la dirección $\pm x$. En realidad, también podemos convertir esto en un argumento de simetría: si reflejamos el sistema en el plano $x$-$z$, tanto la onda entrante como el dieléctrico quedan sin cambios, pero cualquier componente $y$ de las ondas transmitida o reflejada cambiaría de signo. Así, estas componentes deben anularse por simetría. Los campos magnéticos funcionan al revés, debido al producto vectorial en su definición. Así, podemos escribir

$$E_x(z,t) = Ae^{i(kz-\omega t)} + R\,Ae^{i(-kz-\omega t)} \quad\text{para } z<0\,, \qquad \text{(9.56)}$$

$$B_y(z,t) = \frac{n}{c}Ae^{i(kz-\omega t)} - R\,\frac{n}{c}Ae^{i(-kz-\omega t)}$$

y

$$E_x(z,t) = \tau\,Ae^{i(kz-\omega t)} \quad\text{para } z>0\,, \qquad \text{(9.57)}$$

$$B_y(z,t) = \tau\,\frac{n'}{c}Ae^{i(kz-\omega t)}$$

donde hemos seguido nuestra convención de llamar $A$ a la amplitud de la onda entrante. Aquí, $A$ tiene unidades de campo eléctrico. En (9.56) y (9.57), hemos usado (9.54) para obtener el campo $B$ a partir del campo $E$.

Para calcular $R$ y $\tau$, necesitamos las condiciones de contorno en $z=0$. Para ello volvemos a Maxwell. La única forma de tener una discontinuidad en el campo eléctrico es tener una lámina de carga. En un dieléctrico, se acumula carga en la frontera solo si hay una polarización perpendicular a la frontera. En este caso, los campos eléctricos, y por tanto las polarizaciones, son paralelos a la frontera, así que el campo $E$ es continuo en $z=0$. La única forma de tener una discontinuidad del campo magnético, $B$, es tener una lámina de corriente. Si $\mu$ no fuera igual a 1 en alguno de los materiales, tendríamos una magnetización no nula, y tendríamos que preocuparnos por láminas de corriente en la frontera. Sin embargo, como estos son solo dieléctricos, y $\mu=1$ en ambos, no hay magnetización, y el campo $B$ también es continuo en $z=0$. Así, podemos leer inmediatamente las condiciones de contorno:

$$1+R=\tau\,,\qquad n(1-R)=n'\tau\,. \qquad \text{(9.58)}$$

Debido a (9.55), la condición de contorno (9.58) es equivalente a

$$1+R=\tau\,,\qquad k(1-R)=k'\tau\,, \qquad \text{(9.59)}$$

que se parece exactamente a (9.9) y (9.10). Podemos simplemente reutilizar los resultados de (9.11),

$$\tau = \frac{2}{1+k'/k}\,,\qquad R = \frac{1-k'/k}{1+k'/k}\,. \qquad \text{(9.60)}$$

## 9.3 \* Matrices de transferencia

### 9.3.1 Dos masas sobre una cuerda

Consideremos a continuación la reflexión y transmisión debidas a dos masas sobre una cuerda, como en la figura 9.5. Ahora la invariancia bajo traslación y la condición de contorno en $x=\infty$ implican que

$$\psi(x,t) = Ae^{ikx}e^{-i\omega t} + R\,Ae^{-ikx}e^{-i\omega t} \quad\text{para } x\le0\,, \qquad \text{(9.61)}$$

![Figura 9.5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh9_ES/fig9.5.png)

Figura 9.5: dos masas sobre una cuerda infinita, en $x=0$ y $x=L$, con onda entrante 1, onda intermedia $T_I,R_I$ entre las masas, y onda transmitida $\tau$.

$$\psi(x,t) = T_IAe^{ikx}e^{-i\omega t} + R_IAe^{-ikx}e^{-i\omega t} \quad\text{para } 0\le x\le L\,, \qquad \text{(9.62)}$$

$$\psi(x,t) = \tau Ae^{ikx}e^{-i\omega t} \quad\text{para } x\ge L\,. \qquad \text{(9.63)}$$

![Figura 9.6](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh9_ES/fig9.6.png)

Figura 9.6: el problema general de dispersión debido a una única masa en $x=\ell$, con ondas entrante y saliente a ambos lados, $T_I,R_I$ a la izquierda y $T_{II},R_{II}$ a la derecha.

Podríamos resolver este problema de la misma manera, imponiendo condiciones de contorno dos veces, en $x=0$ y $x=L$, pero hay una forma sistemática de hacerlo que es muy útil. Considere primero el problema general de dispersión debido a una única masa en $x=\ell$, con ondas tanto entrantes como salientes a ambos lados, como se muestra en la figura 9.6. Esto es lo más general que puede ocurrir en la dispersión debida a una única masa, y podremos usar el resultado para resolver problemas mucho más complicados sin trabajo adicional. La solución general tiene la forma

$$\psi(x,t) = T_IAe^{ikx}e^{-i\omega t} + R_IAe^{-ikx}e^{-i\omega t} \quad\text{para } x\le\ell\,, \qquad \text{(9.64)}$$

$$\psi(x,t) = T_{II}Ae^{ikx}e^{-i\omega t} + R_{II}Ae^{-ikx}e^{-i\omega t} \quad\text{para } x\ge\ell\,. \qquad \text{(9.65)}$$

Las condiciones de contorno son la continuidad —

$$T_Ie^{ik\ell}+R_Ie^{-ik\ell} = T_{II}e^{ik\ell}+R_{II}e^{-ik\ell} \qquad \text{(9.66)}$$

y $F=ma$ —

$$T\left(\left.\frac{\partial}{\partial x}\psi(x,t)\right|_{x=\ell^+}-\left.\frac{\partial}{\partial x}\psi(x,t)\right|_{x=\ell^-}\right) = m\,\frac{\partial^2}{\partial t^2}\psi(\ell,t) \qquad \text{(9.67)}$$

o

$$ikT\left[(T_{II}-T_I)e^{ik\ell}+(R_I-R_{II})e^{-ik\ell}\right] = -m\omega^2\left(T_{II}e^{ik\ell}+R_{II}e^{-ik\ell}\right)\,. \qquad \text{(9.68)}$$

Resolviendo para $T_I$ y $R_I$, obtenemos

$$T_I = \frac{1}{2}\left[(2-i\epsilon)T_{II}-i\epsilon R_{II}e^{-2ik\ell}\right]\,,\qquad R_I = \frac{1}{2}\left[(2+i\epsilon)R_{II}+i\epsilon T_{II}e^{2ik\ell}\right]\,. \qquad \text{(9.69)}$$

El punto importante es que, por la linealidad, el resultado (9.69) puede escribirse en forma matricial:

$$\begin{pmatrix}T_I\\R_I\end{pmatrix} = d(\ell)\begin{pmatrix}T_{II}\\R_{II}\end{pmatrix} \qquad \text{(9.70)}$$

donde la matriz $d(\ell)$ es

$$d(\ell) = \frac{1}{2}\begin{pmatrix} (2-i\epsilon) & -i\epsilon\,e^{-2ik\ell}\\ i\epsilon\,e^{2ik\ell} & (2+i\epsilon) \end{pmatrix}\,. \qquad \text{(9.71)}$$

La matriz, $d(\ell)$, es una «matriz de transferencia». Nos permite pasar de las amplitudes de una región a las de la siguiente con una simple multiplicación matricial. Podemos usar esto para resolver el problema de las dos masas sin más cálculo que una multiplicación de matrices. Comparando el resultado general, (9.70), con el problema de las dos masas, figura 9.5, vemos inmediatamente que

$$\begin{pmatrix}1\\R\end{pmatrix} = d(0)\begin{pmatrix}T_I\\R_I\end{pmatrix}\,, \qquad \text{(9.72)}$$

y

$$\begin{pmatrix}T_I\\R_I\end{pmatrix} = d(L)\begin{pmatrix}\tau\\0\end{pmatrix}\,. \qquad \text{(9.73)}$$

Así,

$$\begin{pmatrix}1\\R\end{pmatrix} = d(0)\,d(L)\begin{pmatrix}\tau\\0\end{pmatrix}\,. \qquad \text{(9.74)}$$

Haciendo la multiplicación matricial,

$$d(0)\,d(L) = \frac{1}{4}\begin{pmatrix} (2-i\epsilon)^2+\epsilon^2e^{2ikL} & -i\epsilon\left[(2-i\epsilon)e^{-2ikL}+(2+i\epsilon)\right]\\ i\epsilon\left[(2-i\epsilon)+(2+i\epsilon)e^{2ikL}\right] & (2+i\epsilon)^2+\epsilon^2e^{-2ikL} \end{pmatrix}\,. \qquad \text{(9.75)}$$

Así,

$$\tau = \frac{4}{(2-i\epsilon)^2+\epsilon^2e^{2ikL}}\,,\qquad R = i\epsilon\left[(2-i\epsilon)+(2+i\epsilon)e^{2ikL}\right]\frac{\tau}{4}\,. \qquad \text{(9.76)}$$

Note que la reflexión y la transmisión muestran una estructura de resonancia interesante. Por ejemplo, la reflexión se anula para

$$e^{2ikL} = -\frac{2-i\epsilon}{2+i\epsilon}\,. \qquad \text{(9.77)}$$

![Figura 9.7](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh9_ES/fig9.7.png)

Figura 9.7: $|\tau|$ y $|R|$ en función de $\epsilon$, para $kL=0.5$, mostrando oscilaciones amortiguadas de $|\tau|$ y $|R|$ entre 0 y 1 que se estabilizan a valores intermedios para $\epsilon$ grande.

### 9.3.2 Cambios en $k$

![Figura 9.8](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh9_ES/fig9.8.png)

Figura 9.8: el problema general de dispersión para un cambio de $k$, con las regiones I y II separadas en $x=\ell$, ondas $T_I,R_{II}$ a la izquierda y $T_{II},R_I$ a la derecha.

Volvamos al ejemplo simple del principio del capítulo: una frontera entre dos regiones de una cuerda con distintos valores de $k$. Este es un ejemplo muy importante, porque sus características generales son propias de muchos sistemas físicos importantes. Por ejemplo, cuando una onda de luz encuentra un medio transparente, el valor de $k$ cambia. Esa situación es algo más complicada por la naturaleza tridimensional de las ondas de luz y por la polarización; sin embargo, la analogía entre (9.59) y (9.9)-(9.10) significa que podemos trasladar directamente la discusión de la cuerda a las ondas electromagnéticas reflejándose en una frontera dieléctrica perpendicular a la dirección de la onda. En esta sección aplicamos el método general de las matrices de transferencia, discutido en la sección anterior, a este importante ejemplo. Consideramos así la situación mostrada en la figura 9.8, donde las ondas tienen la forma

$$\psi(x,t) = Ae^{-i\omega t}\left(T_Ie^{ik_1x}+R_Ie^{-ik_1x}\right) \quad\text{en I}\,, \qquad \text{(9.78)}$$

$$\psi(x,t) = Ae^{-i\omega t}\left(T_{II}e^{ik_2x}+R_{II}e^{-ik_2x}\right) \quad\text{en II}\,. \qquad \text{(9.79)}$$

Entonces, como en (9.9) y (9.10), las condiciones de contorno son que $\psi$ es continua en $x=\ell$, lo que implica

$$T_Ie^{ik_1\ell}+R_Ie^{-ik_1\ell} = T_{II}e^{ik_2\ell}+R_{II}e^{-ik_2\ell}\,, \qquad \text{(9.80)}$$

y que la pendiente, $\partial\psi/\partial x$, es continua en $x=\ell$, lo que implica

$$ik_1\left(T_Ie^{ik_1\ell}-R_Ie^{-ik_1\ell}\right) = ik_2\left(T_{II}e^{ik_2\ell}-R_{II}e^{-ik_2\ell}\right)\,. \qquad \text{(9.81)}$$

Resolviendo las ecuaciones lineales simultáneas, (9.80) y (9.81), para $T_I$ y $R_I$, y expresando el resultado en forma matricial, encontramos

$$\begin{pmatrix}T_I\\R_I\end{pmatrix} = d(k_1,k_2,\ell)\begin{pmatrix}T_{II}\\R_{II}\end{pmatrix}\,, \qquad \text{(9.82)}$$

donde

$$d(k_1,k_2,\ell) = \frac{1}{2}\begin{pmatrix} \left(1+\frac{k_2}{k_1}\right)e^{ik_2\ell-ik_1\ell} & \left(1-\frac{k_2}{k_1}\right)e^{-ik_2\ell-ik_1\ell}\\ \left(1-\frac{k_2}{k_1}\right)e^{ik_2\ell+ik_1\ell} & \left(1+\frac{k_2}{k_1}\right)e^{-ik_2\ell+ik_1\ell} \end{pmatrix}\,. \qquad \text{(9.83)}$$

(9.82) es un resultado muy general, porque $k_1$, $k_2$ y $\ell$ pueden ser cualquier cosa. Note que la relación es simétrica:

$$\begin{pmatrix}T_{II}\\R_{II}\end{pmatrix} = d(k_2,k_1,\ell)\begin{pmatrix}T_I\\R_I\end{pmatrix}\,. \qquad \text{(9.84)}$$

En lenguaje matricial, esto implica que

$$d(k_2,k_1,\ell)\,d(k_1,k_2,\ell) = I\,. \qquad \text{(9.85)}$$

También es útil usar las propiedades de la multiplicación matricial para reescribir (9.83) de la siguiente forma:

$$d(k_1,k_2,\ell) = b(k_1,\ell)^{-1}\,\tau(k_1,k_2)\,b(k_2,\ell)\,, \qquad \text{(9.86)}$$

donde

$$b(k,\ell) = \begin{pmatrix}e^{ik\ell}&0\\0&e^{-ik\ell}\end{pmatrix}\,, \qquad \text{(9.87)}$$

y

$$\tau(k_1,k_2) = d(k_1,k_2,0) = \frac{1}{2}\begin{pmatrix} \left(1+\frac{k_2}{k_1}\right) & \left(1-\frac{k_2}{k_1}\right)\\ \left(1-\frac{k_2}{k_1}\right) & \left(1+\frac{k_2}{k_1}\right) \end{pmatrix}\,. \qquad \text{(9.88)}$$

Verá la utilidad de esto en el problema de ordenador, (9.6).

### 9.3.3 Reflexión en una película delgada

![Figura 9.9](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh9_ES/fig9.9.png)

Figura 9.9: reflexión en una película delgada, con tres regiones: I ($x\le0$, con onda entrante 1 y reflejada $R$), II ($0\le x\le L$, con $T_{II},R_{II}$) y III ($x\ge L$, con onda transmitida $\tau$).

Considere la situación mostrada en la figura 9.9, donde los números de onda son $k_1$ para $x\le0$, $k_2$ para $0\le x\le L$ y $k_3$ para $x\ge L$. Como de costumbre, la invariancia bajo traslación más la condición de contorno en el infinito (que la onda entrante en I tiene amplitud $A$, y que solo hay una onda saliente en III) implica

$$\psi(x,t) = Ae^{-i\omega t}\left(e^{ik_1x}+Re^{-ik_1x}\right) \quad\text{para } x\le0\,,$$

$$\psi(x,t) = Ae^{-i\omega t}\left(T_{II}e^{ik_2x}+R_{II}e^{-ik_2x}\right) \quad\text{para } 0\le x\le L\,, \qquad \text{(9.89)}$$

$$\psi(x,t) = \tau Ae^{-i\omega t}e^{ik_3x} \quad\text{para } L\le x\,.$$

Entonces sabemos, por los resultados de la sección anterior, que

$$\begin{pmatrix}1\\R\end{pmatrix} = d(k_1,k_2,0)\begin{pmatrix}T_{II}\\R_{II}\end{pmatrix} \qquad \text{(9.90)}$$

y

$$\begin{pmatrix}T_{II}\\R_{II}\end{pmatrix} = d(k_2,k_3,L)\begin{pmatrix}\tau\\0\end{pmatrix} \qquad \text{(9.91)}$$

y por tanto

$$\begin{pmatrix}1\\R\end{pmatrix} = d(k_1,k_2,0)\,d(k_2,k_3,L)\begin{pmatrix}\tau\\0\end{pmatrix}\,. \qquad \text{(9.92)}$$

$$d(k_1,k_2,0)\,d(k_2,k_3,L) = b(k_1,0)^{-1}\,\tau(k_1,k_2)\,b(k_2,0)\,b(k_2,L)^{-1}\,\tau(k_2,k_3)\,b(k_3,L) \qquad \text{(9.93)}$$

A menudo nos interesa la situación $k_3=k_1$, que describe una película (en una dimensión, una película es simplemente una región en $x$) dentro de un medio por lo demás homogéneo. Este es entonces un análogo unidimensional de la reflexión de la luz en una pompa de jabón. Entonces la matriz de transferencia se ve así:

$$\begin{aligned}
\frac{1}{4} & \begin{pmatrix} \left(1+\frac{k_1}{k_2}\right) & \left(1-\frac{k_1}{k_2}\right)\\ \left(1-\frac{k_1}{k_2}\right) & \left(1+\frac{k_1}{k_2}\right) \end{pmatrix}\begin{pmatrix}e^{-ik_2L}&0\\0&e^{ik_2L}\end{pmatrix}\\
& \begin{pmatrix} \left(1+\frac{k_2}{k_1}\right) & \left(1-\frac{k_2}{k_1}\right)\\ \left(1-\frac{k_2}{k_1}\right) & \left(1+\frac{k_2}{k_1}\right) \end{pmatrix}\begin{pmatrix}e^{ik_1L}&0\\0&e^{-ik_1L}\end{pmatrix} \qquad \text{(9.94)}
\end{aligned}$$

Así,

$$1 = \left(\cos k_2L - i\,\frac{k_1^2+k_2^2}{2k_1k_2}\sin k_2L\right)e^{ik_1L}\tau \qquad \text{(9.95)}$$

y

$$R = -i\,\frac{k_1^2-k_2^2}{2k_1k_2}\sin k_2L\,e^{ik_1L}\tau \qquad \text{(9.96)}$$

o

$$\tau = \left(\cos k_2L - i\,\frac{k_1^2+k_2^2}{2k_1k_2}\sin k_2L\right)^{-1}e^{-ik_1L} \qquad \text{(9.97)}$$

y

$$R = -i\,\frac{k_1^2-k_2^2}{2k_1k_2}\sin k_2L\left(\cos k_2L - i\,\frac{k_1^2+k_2^2}{2k_1k_2}\sin k_2L\right)^{-1}\,. \qquad \text{(9.98)}$$

Aquí vemos el fenómeno de la transmisión resonante. La onda no se refleja en absoluto si el grosor de la película es un número entero o semientero de longitudes de onda. Note también que, cuando $k_2\to k_1$, $\tau\to1$ y $R\to0$, como debe ser, porque en este límite no hay frontera.

La reflexión de (9.98) varía rápidamente con $k_2$, como se muestra en la figura 9.10, donde graficamos la intensidad de la onda reflejada frente a $k_2$, para un cociente fijo $k_1/k_2=3$. Es esta variación rápida de la intensidad de la luz reflejada en función de la longitud de onda la responsable de los familiares patrones de color en películas delgadas como pompas de jabón y manchas de aceite.

![Figura 9.10](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh9_ES/fig9.10.png)

Figura 9.10: gráfica de $|R|^2$ en función de $k_2$ para $k_1/k_2=3$, mostrando oscilaciones periódicas entre 0 y un valor máximo, con la envolvente moduladas por el cociente de números de onda.

### 9.3.4 Recubrimiento antirreflectante

No trabajaremos el caso general $k_1\neq k_3$, simplemente porque el álgebra es un lío. Sin embargo, vale la pena señalar un caso especial importante. Suponga que tiene una frontera entre medios en los que el número de onda de su onda viajera es $k_1$ y $k_3$. Normalmente, encuentra reflexión en la frontera. La pregunta es: ¿puede añadir una capa intermedia de película con número de onda $k_2$ que elimine toda la reflexión? La respuesta es sí. Primero debe ajustar el número de onda de la película para que sea la media geométrica de $k_1$ y $k_3$, de modo que

$$\frac{k_2}{k_1} = \frac{k_3}{k_2}\,. \qquad \text{(9.99)}$$

Entonces la matriz de transferencia se convierte en

$$\begin{aligned}
\frac{1}{4} & \begin{pmatrix} \left(1+\frac{k_2}{k_1}\right) & \left(1-\frac{k_2}{k_1}\right)\\ \left(1-\frac{k_2}{k_1}\right) & \left(1+\frac{k_2}{k_1}\right) \end{pmatrix}\begin{pmatrix}e^{-ik_2L}&0\\0&e^{ik_2L}\end{pmatrix}\\
& \begin{pmatrix} \left(1+\frac{k_2}{k_1}\right) & \left(1-\frac{k_2}{k_1}\right)\\ \left(1-\frac{k_2}{k_1}\right) & \left(1+\frac{k_2}{k_1}\right) \end{pmatrix}\begin{pmatrix}e^{ik_3L}&0\\0&e^{-ik_3L}\end{pmatrix}\,. \qquad \text{(9.100)}
\end{aligned}$$

Es fácil comprobar que la reflexión se anula cuando hay un número semientero impar de longitudes de onda en la región intermedia,

$$k_2L = (2n+1)\frac{\pi}{2}\,. \qquad \text{(9.101)}$$

En términos cualitativos, la reflexión se anula debido a una interferencia destructiva entre las ondas reflejadas en las dos fronteras. Esto tiene aplicaciones prácticas en recubrimientos antirreflectantes para componentes ópticos.

## Repaso del capítulo

Ahora debería ser capaz de:

1.  Analizar problemas de dispersión imponiendo condiciones de contorno y calculando los coeficientes de reflexión y transmisión;

2.  Identificar una onda con algo de reflexión, y distinguirla de una onda puramente viajera o estacionaria;

3.  Comprobar la conservación de la energía en problemas de dispersión;

4.  Analizar ondas planas electromagnéticas en un dieléctrico, y la reflexión en una frontera dieléctrica;

5.  - Usar matrices de transferencia para simplificar el análisis de la dispersión debida a más de una frontera.

## Problemas

**9.1.** Se muestra la frontera entre dos sistemas semiinfinitos. A la izquierda hay bloques idénticos de masa $m$. A la derecha hay bloques idénticos de masa $M$. Están conectados, como se muestra, por muelles idénticos sin masa, de constante $K$, tales que la separación de equilibrio entre bloques vecinos es $a$.

![Figura](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh9_ES/figs1.png)

Figura: cadena infinita de masas $m$ a la izquierda de $x=0$ y masas $M$ a la derecha de $x=0$, todas conectadas por muelles idénticos de constante $K$ y separación $a$.

Considere la reflexión de una onda longitudinal viajera en la frontera entre estas dos regiones; es decir, suponga que en la región I hay una onda incidente de amplitud $A$ viajando hacia la derecha y una onda reflejada viajando hacia la izquierda. En notación compleja, el desplazamiento de la masa con posición de equilibrio $x$ es

$$\psi(x,t) = Ae^{-i(\omega t-kx)} + R\,Ae^{-i(\omega t+kx)}$$

para $x\le a$. ¿Cuál es la relación entre $\omega$ y $k$?

En la región II, solo hay onda transmitida:

$$\psi(x,t) = T\,Ae^{-i(\omega t-k'x)}$$

para $x\ge0$. ¿Cuál es la relación entre $\omega$ y $k'$? Encuentre las condiciones de contorno apropiadas que le permitan relacionar $\psi(x,t)$ en las dos regiones, y resuelva para $R$ (no se moleste en simplificar el número complejo). Compruebe su resultado tomando el límite de $a$, $m$ y $M$ tendiendo a cero, con $m/a$ y $M/a$ fijos, y comparando con un sistema continuo apropiado.

**9.2.** Una línea infinita de péndulos acoplados admite ondas viajeras, pero no tiene modos normales de onda estacionaria en los que el desplazamiento de los péndulos tienda a cero en el infinito. Considere, sin embargo, el sistema mostrado a continuación:

![Figura](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh9_ES/figs2.png)

Figura: cadena infinita de péndulos acoplados numerados $\ldots,-3,-2,-1,0,1,2,3,\ldots$; el péndulo 0 puede deslizar longitudinalmente sin fuerza restauradora gravitatoria, solo con el acoplamiento de los muelles.

Aquí el bloque 0 es libre de deslizar longitudinalmente sin fuerza restauradora gravitatoria, solo con el acoplamiento debido a los muelles. Si los bloques tienen masa $M$, la constante de los muelles es $K$, la separación entre bloques vecinos es $a$, y los péndulos tienen longitud $\ell$, encuentre la frecuencia del modo normal de onda estacionaria del sistema en el que los desplazamientos son $Ae^{-\kappa x}$ para $x\ge0$ y $Ae^{\kappa x}$ para $x\le0$. Pista: considere el subsistema $-a\le x\le a$ como parte de un sistema infinito con las condiciones de contorno apropiadas. Entonces puede obtener la respuesta directamente de la relación de dispersión.

**9.3.** Considere una cuerda con densidad de masa lineal $\rho$, dividida en dos partes. Las dos mitades están unidas a un anillo sin masa que desliza verticalmente sin fricción por una varilla en $x=0$. Una de las dos mitades está estirada en la dirección $x$ negativa con tensión $T$. La otra está estirada en la dirección $x$ positiva con tensión $T'$. Note que la varilla vertical es necesaria para equilibrar las fuerzas horizontales sobre el anillo sin masa debidas a las dos cuerdas con tensiones distintas.

Suponga que llega una onda viajera desde la dirección $x$ negativa. Entonces el desplazamiento de las cuerdas en las dos regiones es

$$\psi(x,t) = Ae^{ikx}e^{-i\omega t} + R\,Ae^{-ik'x}e^{-i\omega't} \quad\text{para } x\le0$$

$$\psi(x,t) = \tau\,Ae^{ik''x}e^{-i\omega''t} \quad\text{para } x\ge0\,.$$

1.  Encuentre $k$, $k'$, $\omega'$, $k''$ y $\omega''$ en términos de $\omega$, $T$, $T'$ y $\rho$. Pista: ¡esto es fácil!

2.  Escriba las dos condiciones de contorno en $x=0$ y encuentre $R$ y $\tau$.

**9.4.** Considere ondas viajeras en un sistema infinito, parte del cual se muestra a continuación, para el movimiento longitudinal (horizontal) de los bloques.

![Figura](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh9_ES/figs3.png)

Figura: cadena infinita de masas numeradas $\ldots,-3,-2,-1,0,1,2,3,\ldots$, con separación $a$, todas de masa $m$ excepto el bloque 0, que no tiene masa; muelles idénticos de constante $K$.

Todos los bloques tienen masa $m$, excepto el bloque 0, que no tiene masa. Los muelles no tienen masa y tienen constante $K$. La separación entre bloques vecinos es $a$. A la izquierda del bloque 0, que tomaremos en $x=0$, hay una onda entrante y una reflejada, de modo que el desplazamiento longitudinal de los bloques para $x\le0$ tiene la forma

$$Ae^{ikx-i\omega t} + R\,Ae^{-ikx-i\omega t}\,.$$

A la derecha del bloque sin masa hay una onda transmitida, de modo que el desplazamiento longitudinal de los bloques para $x\ge0$ tiene la forma

$$T\,Ae^{ikx-i\omega t}\,.$$

$\omega$ y $k$ están relacionados por la relación de dispersión

$$\omega^2 = \frac{4K}{m}\sin^2\frac{ka}{2}\,.$$

1.  Explique la física de las condiciones de contorno en $x=0$.

2.  Encuentre $R$ y $T$.

**9.5.** Considere un sistema semiinfinito de dos tipos de cuerda masiva con distintas densidades, mostrado a continuación: la densidad de la cuerda en la región I es $\rho$, y en la región II es $\rho'$. La tensión en ambas cuerdas es $T$. Suponga que el extremo en $x=-L$ oscila en la dirección transversal con desplazamiento $\chi\sin\omega t$. Esto produce una onda saliente (moviéndose hacia la derecha) en la región II sin onda entrante. Suponga que $\omega = \dfrac{\pi}{2L}\sqrt{T/\rho}$. Encuentre el desplazamiento en el punto $x=0$ en función del tiempo.

![Figura](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh9_ES/figs4.png)

Figura: cuerda de densidad $\rho$ entre $x=-L$ y $x=0$ (región I), y cuerda de densidad $\rho'$ para $x\ge0$ (región II).

**9.6.** Si está resolviendo un problema de reflexión y transmisión que involucra varias regiones distintas, y por tanto requiere varias condiciones de contorno, la matriz de transferencia es muy útil, como vio en el análisis de la dispersión en una película delgada.

Su tarea de ordenador es extender este análisis para incorporar $2n$ condiciones de contorno de este tipo, donde $n$ es un entero grande. En particular, considere una cuerda continua con número de onda $k_2$ para $L\le x\le2L$, $3L\le x\le4L$, …, y $(2n-1)L\le x\le2nL$, y $k_1$ en el resto.

Tome $k_1=k$ y $k_2=2k$. Calcule la amplitud de transmisión de una onda entrante en este sistema, en función de $L$, haciendo la multiplicación apropiada de $2n$ matrices. Para ello, debe programar su ordenador para multiplicar matrices complejas. Organice su programa de forma iterativa, de modo que pueda cambiar $n$ fácilmente. Esto le permitirá empezar con $n$ pequeño y avanzar a $n$ más grande solo cuando esté seguro de que el programa funciona.

Si es posible, presente los resultados en forma de gráfica del valor absoluto del coeficiente de transmisión frente a $kL$, para $0\le L\le\pi/2k$. A medida que aumenta $n$, ocurre algo interesante: el coeficiente de transmisión cae casi a cero en una región de valores de $L$. Incluso si no puede producir una gráfica, debería poder encontrar el rango de $L$ para el que la transmisión tiende a cero cuando $n$ se hace grande.

Pista: para $n=3$, el resultado debería parecerse a la gráfica de la figura 9.11.

![Figura 9.11](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_TextCh9_ES/fig9.11.png)

Figura 9.11: coeficiente de transmisión frente a $kL$ para $n=3$, mostrando una banda central donde la transmisión cae casi a cero, flanqueada por oscilaciones de alta transmisión.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.
