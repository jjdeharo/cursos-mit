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
