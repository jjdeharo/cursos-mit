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
