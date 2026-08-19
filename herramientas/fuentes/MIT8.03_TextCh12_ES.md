---
title: "Capítulo 12: Polarización — 8.03SC Física III: Vibraciones y Ondas"
author: "Yen-Jie Lee (traducción al español)"
lang: es
---

# Capítulo 12: Polarización

En este capítulo volvemos a (9.46)-(9.48) y examinamos las consecuencias de las ecuaciones de Maxwell en un material homogéneo para una onda plana electromagnética viajera general. La complicación añadida es la polarización.

<h2 id="vídeos-de-esta-clase-youtube">Vídeos de esta clase (YouTube)</h2>
<ul>
<li class="video-item">
<button type="button" class="video-play" data-vid="TjxR7lAwWhI" data-title="Clase 17: Polarización, polarizador">
<span class="video-play-icon">▶</span> <strong>Clase 17: Polarización, polarizador</strong>
</button>
<a class="video-ext" href="https://www.youtube.com/watch?v=TjxR7lAwWhI" target="_blank" rel="noopener">YouTube ↗</a>
</li>
<li class="video-item">
<button type="button" class="video-play" data-vid="Dlhma3z57SA" data-title="Clase 18: Láminas de onda, radiación">
<span class="video-play-icon">▶</span> <strong>Clase 18: Láminas de onda, radiación</strong>
</button>
<a class="video-ext" href="https://www.youtube.com/watch?v=Dlhma3z57SA" target="_blank" rel="noopener">YouTube ↗</a>
</li>
</ul>

## Resumen previo

La polarización es una característica general de las ondas transversales en tres dimensiones. La onda plana electromagnética general tiene dos estados de polarización, correspondientes a las dos direcciones a las que puede apuntar el campo eléctrico transversalmente a la dirección de movimiento de la onda. De ahí surge mucha física interesante.

i. Introducimos la idea de polarización en las oscilaciones transversales de una cuerda.

ii. Discutimos la forma general de las ondas electromagnéticas y describimos el estado de polarización en términos de un vector complejo de dos componentes, $Z$. Calculamos la densidad de energía y de momento en función de $Z$ y discutimos el vector de Poynting. Describimos las variedades de estados de polarización posibles de una onda plana: lineal, circular y elíptica.

iii. Describimos la «luz no polarizada» y explicamos cómo generar y manipular luz polarizada con polarizadores y láminas de onda. Discutimos la rotación del plano de la luz polarizada linealmente por sustancias ópticamente activas.

iv. Analizamos la reflexión y la transmisión de luz polarizada con incidencia oblicua sobre un contorno entre dieléctricos.

## 12.1 La cuerda en tres dimensiones

En la mayoría de nuestras discusiones sobre fenómenos ondulatorios hasta ahora hemos supuesto que el movimiento tiene lugar en un plano, de modo que podemos dibujar el sistema en una hoja de papel. Nos hemos estado restringiendo implícitamente a ondas bidimensionales. Esto está bien para las oscilaciones longitudinales en tres dimensiones, porque toda la acción transcurre a lo largo de una única línea. Sin embargo, para las oscilaciones transversales, pasar de dos a tres dimensiones supone una diferencia enorme, porque hay dos direcciones transversales en las que el sistema puede oscilar.

Por ejemplo, considere una cuerda en tres dimensiones, tensada en la dirección $z$. Cada punto de la cuerda puede oscilar tanto en la dirección $x$ como en la dirección $y$. Si el sistema no fuera aproximadamente lineal, esto podría ser un problema horrendo. La linealidad nos permite resolver el problema de la oscilación en el plano $x$-$z$ por separado del problema de la oscilación en el plano $y$-$z$. Ya hemos resuelto estos problemas bidimensionales en el capítulo 5. Después podemos simplemente juntar los resultados para obtener el movimiento más general del sistema tridimensional. Dicho de otro modo, podemos tratar la componente $x$ de la oscilación transversal y la componente $y$ como completamente independientes.

Supongamos que hay una onda armónica viajera en la dirección $+z$ en la cuerda. El desplazamiento de la cuerda en $z$ respecto de su posición de equilibrio, $(0, 0, z)$, puede escribirse como

$$\vec{\Psi}(z, t) = \operatorname{Re}\left[(\psi_1\hat{x} + \psi_2\hat{y})\,e^{i(kz - \omega t)}\right] \tag{12.1}$$

donde $\hat{x}$ e $\hat{y}$ son vectores unitarios en las direcciones $x$ e $y$, y $\psi_1$ y $\psi_2$ son parámetros complejos que describen la amplitud y la fase de las oscilaciones en el plano $x$-$z$ y en el plano $y$-$z$,

$$\psi_j = A_j e^{i\phi_j} \quad \text{para } j = 1\text{ a }2. \tag{12.2}$$

Conviene disponer estos parámetros en un vector complejo

$$Z = \begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix}, \tag{12.3}$$

que da una descripción completa del movimiento de la cuerda.

### 12.1.1 Polarización

La «polarización» se refiere a la naturaleza del movimiento de un punto de la cuerda (o de otra oscilación transversal). Este movimiento está animado en el programa 12-1. Quizá le convenga leer la discusión que sigue con ese programa en marcha.

Si $\phi_1 = \phi_2$, o bien $A_1$ o $A_2$ es cero, entonces (12.3) representa una cuerda polarizada linealmente. La polarización lineal es fácil de entender: significa que cada punto de la cuerda oscila de un lado a otro en un plano fijo. Por ejemplo,

$$u_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \tag{12.4}$$

$$u_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \tag{12.5}$$

representan cuerdas que oscilan en el plano $x$-$z$ y en el plano $y$-$z$ respectivamente. Una cuerda que oscila en un plano que forma un ángulo $\theta$ con el eje $x$ positivo (hacia el eje $y$ positivo) se representa mediante

$$u_\theta = \begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix}. \tag{12.6}$$

Esto se muestra en el plano $x$-$y$ en la figura 12.1. Los vectores de polarización (12.4)-(12.6) pueden multiplicarse por un factor de fase, $e^{i\phi}$, sin que ello afecte al estado de polarización de ninguna manera importante. Eso corresponde simplemente a poner el reloj a cero de otro modo.

*(Figura 12.1: $u_1$, $u_2$ y $u_\theta$.)*

Más interesante es la polarización circular. Una onda polarizada circularmente en una cuerda se representa por

$$\begin{pmatrix} 1 \\ i \end{pmatrix} \tag{12.7}$$

o bien por

$$\begin{pmatrix} 1 \\ -i \end{pmatrix}. \tag{12.8}$$

En (12.7), la componente $y$ va retrasada respecto de la componente $x$ en $\pi/2$ ($= \phi_2$). Así, en cualquier punto fijo del espacio, el campo rota de $x$ hacia $y$, es decir, en sentido antihorario visto desde el eje $z$ positivo (con la onda viniendo hacia usted), como se muestra en la figura 12.2. Esto se llama «polarización circular a izquierdas», porque la cuerda se parece a un tornillo levógiro. Análogamente, (12.8) representa la rotación de la cuerda en sentido horario, y se llama «polarización circular a derechas».

*(Figura 12.2: polarización circular.)*

El vector

$$\begin{pmatrix} A \\ iB \end{pmatrix} \tag{12.9}$$

con $A > B > 0$ representa polarización elíptica. Un punto de la cuerda describe una elipse de semieje mayor $A$ a lo largo del eje 1 y semieje menor $B$ a lo largo del eje 2, con rotación antihoraria, como se muestra en la figura 12.3.

*(Figura 12.3: polarización elíptica con el eje largo en la dirección $x$.)*

*(Figura 12.4: polarización elíptica general.)*

Un vector completamente general puede escribirse de la forma siguiente:

$$\begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix} = e^{i\phi}\begin{pmatrix} A\cos\theta - iB\sin\theta \\ A\sin\theta + iB\cos\theta \end{pmatrix} \tag{12.10}$$

con $A \geq |B|$ y $0 \leq \theta < \pi$, donde $\phi$ es una fase real (poco relevante para la física, pero que puede estar ahí para afear las matemáticas). Esto representa polarización elíptica con semieje mayor $A$ formando un ángulo $\theta$ con el eje 1, como en

$$u_\theta = \begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix}$$

y semieje menor $B$, como se muestra en la figura 12.4. Si $B$ es positivo (negativo), la rotación es antihoraria (horaria). Los parámetros físicamente interesantes $A$, $B$ y $\theta$ pueden obtenerse a partir de $\psi_1$ y $\psi_2$ como sigue:

$$A^2 + B^2 = |\psi_1|^2 + |\psi_2|^2, \tag{12.11}$$

$$AB = -\operatorname{Im}(\psi_1\psi_2^*). \tag{12.12}$$

Así,

$$A \pm B = \sqrt{|\psi_1|^2 + |\psi_2|^2 \mp 2\operatorname{Im}(\psi_1\psi_2^*)}, \tag{12.13}$$

da $A$ y $B$. Entonces $\theta$ satisface

$$(A^2 - B^2)\cos 2\theta = |\psi_1|^2 - |\psi_2|^2,$$

$$(A^2 - B^2)\sin 2\theta = 2\operatorname{Re}(\psi_1\psi_2^*).$$

Obsérvese que el factor de fase global $e^{i\phi}$ se cancela en (12.11)-(12.13).

## 12.2 Ondas electromagnéticas

### 12.2.1 Ondas planas electromagnéticas generales

Vimos en los capítulos 8 y 9 que una onda plana electromagnética que viaja en la dirección $+z$ tiene este aspecto:

$$E_x(z, t) = \varepsilon_x e^{i(kz - \omega t)}, \qquad E_y(z, t) = \varepsilon_y e^{i(kz - \omega t)}, \tag{12.14}$$

$$B_x(z, t) = \beta_x e^{i(kz - \omega t)}, \qquad B_y(z, t) = \beta_y e^{i(kz - \omega t)}, \tag{12.15}$$

$$E_z(z, t) = B_z(z, t) = 0, \tag{12.16}$$

donde las $\beta$ vienen determinadas por las ecuaciones de Maxwell como

$$\beta_y = \frac{n}{c}\varepsilon_x, \qquad \beta_x = -\frac{n}{c}\varepsilon_y. \tag{12.17}$$

Como de costumbre, hemos escrito la onda con la dependencia temporal irreducible, $e^{-i\omega t}$. Para obtener los campos eléctrico y magnético reales, tomamos la parte real de (12.14)-(12.15). Nótese, en particular, que las constantes $\varepsilon_j$ y $\beta_j$ para $j = x$ e $y$ pueden ser complejas.

La restricción al movimiento en la dirección $z$ no es importante. Puesto que la física de las ecuaciones de Maxwell es invariante bajo rotaciones en el espacio tridimensional, podemos escribir la forma de una onda plana que se mueve con un vector $\vec{k}$ arbitrario extrayendo de (12.14)-(12.17) las características que no dependen de la dirección. Son estas:

i. $\vec{k}$, $\vec{E}$ y $\vec{B}$ son vectores mutuamente ortogonales.

ii. $\vec{B}$ queda determinado por el producto vectorial

$$\vec{B} = \frac{1}{\omega}\vec{k}\times\vec{E} = \frac{n}{c}\hat{k}\times\vec{E} \tag{12.19}$$

donde $\hat{k}$ es un vector unitario en la dirección del vector $\vec{k}$, la dirección de propagación de la onda.

Estas dos condiciones implican que una onda plana electromagnética real general puede escribirse como

$$\vec{E} = \operatorname{Re}\left(\vec{e}(\vec{k})\,e^{i\vec{k}\cdot\vec{r} - i\omega t}\right), \qquad \vec{B} = \operatorname{Re}\left(\vec{b}(\vec{k})\,e^{i\vec{k}\cdot\vec{r} - i\omega t}\right) \tag{12.20}$$

donde los vectores $\vec{e}$ y $\vec{b}$ son, en general, complejos y satisfacen

$$\vec{b}(\vec{k}) = \frac{1}{\omega}\vec{k}\times\vec{e}(\vec{k}) = \frac{n}{c}\hat{k}\times\vec{e}(\vec{k}) \qquad \text{y} \qquad \hat{k}\cdot\vec{e}(\vec{k}) = 0. \tag{12.21}$$

Hay dos cosas que señalar sobre las relaciones (12.21):

i. Basta con especificar la dirección del campo eléctrico, $\vec{e}(\vec{k})$. El campo magnético queda entonces determinado por (12.21). El vector $\vec{e}$ se llama la «polarización» de la onda electromagnética.

ii. Debido a (12.21), la polarización es perpendicular a $\vec{k}$ y, por tanto, vive en un espacio vectorial bidimensional.

En el espacio bidimensional perpendicular a $\vec{k}$ podemos elegir una base de vectores reales, $\hat{e}_1$ y $\hat{e}_2$, donde

$$\hat{e}_1\cdot\hat{k} = \hat{e}_2\cdot\hat{k} = \hat{e}_1\cdot\hat{e}_2 = 0, \qquad \hat{e}_1\times\hat{e}_2 = \hat{k}. \tag{12.22}$$

Por ejemplo, para una onda plana que viaja en la dirección $z$, $\hat{k} = \hat{z}$, podríamos tomar $e_1 = \hat{x}$ y $e_2 = \hat{y}$. Entonces podemos escribir

$$\vec{e}(\vec{k}) = \psi_1\hat{e}_1 + \psi_2\hat{e}_2. \tag{12.23}$$

Las componentes $\psi_1$ y $\psi_2$ forman el vector bidimensional (12.3) que describe el estado de polarización de la onda electromagnética, igual que describe el estado de polarización de la cuerda.[^jones] Siempre podemos volver a las componentes del campo eléctrico usando (12.23) y (12.20), y hallar después el campo magnético mediante (12.21).

[^jones]: A veces se le llama vector de Jones. Véase Hecht, página 323.

Ahora toda la discusión sobre ondas transversales en una cuerda, de (12.4) a (12.13), puede trasladarse para describir la luz polarizada. La dirección de desplazamiento de la cuerda se traduce directamente en la dirección del campo eléctrico. Así, la animación del programa 12-1 se aplica igual de bien al campo eléctrico de una onda polarizada que a la polarización en una cuerda.

### 12.2.2 Energía e intensidad

La densidad de energía en un campo electromagnético es

$$\mathcal{E} = \frac{1}{2}\left(\epsilon\vec{E}^2 + \frac{1}{\mu}\vec{B}^2\right). \tag{12.24}$$

Puesto que la densidad de energía es una función no lineal de las intensidades de campo, debemos usar los campos **reales** en (12.24). La densidad de momento es

$$\vec{\mathcal{P}} = \epsilon\,\vec{E}\times\vec{B}. \tag{12.25}$$

El vector de Poynting, una medida del flujo de energía, es

$$\vec{S} = c^2\vec{\mathcal{P}}. \tag{12.26}$$

Estas magnitudes satisfacen

$$\frac{\partial}{\partial t}\mathcal{E} + \vec{\nabla}\cdot\vec{S} = 0. \tag{12.27}$$

El vector de Poynting es útil porque mide la intensidad de la onda, la energía por unidad de tiempo y de área que transporta la onda electromagnética. La relación (12.27) expresa entonces la conservación de la energía: la suma del cambio de la densidad de energía en un punto cualquiera más la energía que fluye alejándose de él es cero.

Para ver qué aspecto tienen estas magnitudes en términos del vector $Z$, calculemos explícitamente los campos eléctrico y magnético usando (12.20) y (12.21). El resultado es

$$\vec{E} = A_1\hat{e}_1\cos(\vec{k}\cdot\vec{r} - \omega t + \phi_1) + A_2\hat{e}_2\cos(\vec{k}\cdot\vec{r} - \omega t + \phi_2),$$

$$\vec{B} = \sqrt{\mu\epsilon}\left(A_1\hat{e}_2\cos(\vec{k}\cdot\vec{r} - \omega t + \phi_1) - A_2\hat{e}_1\cos(\vec{k}\cdot\vec{r} - \omega t + \phi_2)\right). \tag{12.28}$$

Sustituyendo esto en (12.24) y (12.26) se obtiene

$$\mathcal{E} = \frac{\epsilon}{4\pi}\left(A_1^2\cos^2(\vec{k}\cdot\vec{r} - \omega t + \phi_1) + A_2^2\cos^2(\vec{k}\cdot\vec{r} - \omega t + \phi_2)\right), \tag{12.29}$$

$$\vec{S} = \hat{k}\sqrt{\frac{\epsilon}{\mu}}\,\frac{c}{4\pi}\left(A_1^2\cos^2(\vec{k}\cdot\vec{r} - \omega t + \phi_1) + A_2^2\cos^2(\vec{k}\cdot\vec{r} - \omega t + \phi_2)\right). \tag{12.30}$$

*[Nota de la traducción: las expresiones (12.29) y (12.30) del original llevan un factor $1/4\pi$ que no se sigue de (12.24), donde la densidad de energía se escribe con un $\tfrac{1}{2}$ y sin $4\pi$. Sustituyendo (12.28) en (12.24) se obtiene $\mathcal{E} = \epsilon\left(A_1^2\cos^2(\cdots) + A_2^2\cos^2(\cdots)\right)$. La discrepancia viene de mezclar dos convenios de unidades, y arrastra también a (12.31) y (12.32); se han conservado las fórmulas tal como aparecen en el libro.]*

Puede comprobar explícitamente que se satisface (12.27). Como $\omega$ es muy grande para las ondas electromagnéticas de interés, casi siempre nos interesan solo los valores promediados en el tiempo de $\mathcal{E}$ y $\vec{S}$. Estos son

$$\langle\mathcal{E}\rangle = \frac{\epsilon}{8\pi}\left(A_1^2 + A_2^2\right), \tag{12.31}$$

$$\left\langle\vec{S}\right\rangle = \hat{k}\sqrt{\frac{\epsilon}{\mu}}\,\frac{c}{8\pi}\left(A_1^2 + A_2^2\right). \tag{12.32}$$

Nótese que los valores promediados en el tiempo dependen únicamente de la cantidad

$$|Z|^2 \equiv |\psi_1|^2 + |\psi_2|^2 = A_1^2 + A_2^2. \tag{12.33}$$

**La intensidad de la luz es proporcional a $|Z|^2$.**

### 12.2.3 Polarización circular y espín

Aunque la polarización lineal es más familiar y quizá más fácil de entender, hay un sentido en el que la polarización circular es más fundamental. La onda plana electromagnética en la dirección $\hat{k}$ puede rotarse alrededor del eje $\hat{k}$ sin que cambie nada salvo su estado de polarización. La simetría de rotación de la física sugiere que deberíamos ser capaces de encontrar estados que se comporten de forma sencilla bajo tal rotación y que simplemente queden multiplicados por un factor de fase. Esos estados son, de hecho, los estados de polarización circular. La acción de una rotación de ángulo $\theta$ alrededor del eje $\hat{k}$ sobre el vector de polarización $Z$ está representada por la matriz

$$R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}. \tag{12.34}$$

Por ejemplo, $R_\theta$ actuando sobre $u_1$, (12.4), da $u_\theta$, (12.6):

$$R_\theta\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix}.$$

Pero sobre los estados de polarización circular a izquierdas y a derechas,

$$R_\theta\begin{pmatrix} 1 \\ i \end{pmatrix} = e^{-i\theta}\begin{pmatrix} 1 \\ i \end{pmatrix},$$

$$R_\theta\begin{pmatrix} 1 \\ -i \end{pmatrix} = e^{i\theta}\begin{pmatrix} 1 \\ -i \end{pmatrix}.$$

Esto está relacionado con el hecho de que los estados de polarización circular transportan el máximo momento angular posible, lo que a su vez está relacionado con la propiedad mecanocuántica del espín del fotón.

## 12.3 Láminas de onda y polarizadores

Una razón por la que la polarización es importante es que el estado de polarización de una onda electromagnética puede manipularse con facilidad. Dos de los dispositivos más importantes para tal manipulación son los polarizadores y las láminas de onda.

### 12.3.1 Luz no polarizada

En cualquier haz de luz, en un punto y un instante dados, el campo eléctrico apunta en una dirección determinada. Además, como cualquier onda plana electromagnética de frecuencia angular definida puede describirse mediante (12.20) y (12.21), toda onda plana está polarizada. Sin embargo, en un haz «no polarizado» la onda luminosa consta de un rango de frecuencias angulares con polarizaciones distintas. Como resultado de la interferencia de las distintas componentes armónicas de la onda, la polarización deambula de forma más o menos aleatoria en función del tiempo y del espacio y, en promedio, no se destaca ninguna polarización particular. Un ejemplo sencillo de este aspecto está animado en el programa 12-2, donde representamos un campo eléctrico de la forma

$$E_x(t) = \cos(\omega_1 t + \phi_1) + \cos(\omega_2 t + \phi_2),$$

$$E_y(t) = \cos(\omega_3 t + \phi_3) + \cos(\omega_4 t + \phi_4),$$

donde las fases son aleatorias y las frecuencias se eligen al azar en un rango pequeño alrededor de una frecuencia central. Puede observar cómo el campo $\vec{E}$ deambula por el plano $x$-$y$ hasta acabar llenándolo. Cuanto más estrecho es el rango de frecuencias de la onda, más lentamente deambula la polarización. En el ejemplo del programa 12-2, el rango de frecuencias es del orden del 10 % de la frecuencia central, así que la polarización deambula rápidamente. Pero para un haz con una frecuencia bastante bien definida, la polarización será casi constante durante muchos ciclos de la onda. El tiempo durante el cual la polarización es aproximadamente constante se llama tiempo de coherencia de la onda. Para una onda plana de frecuencia definida, el tiempo de coherencia es infinito.

### 12.3.2 Polarizadores

Un «polarizador» es un dispositivo que deja pasar con muy poca absorción la luz polarizada en una dirección determinada (el «eje fácil de transmisión» del polarizador), pero absorbe la mayor parte de la luz polarizada en la dirección perpendicular. Así, un haz de luz no polarizada, al atravesar el polarizador, emerge polarizado a lo largo del eje fácil.

Para las oscilaciones transversales de una cuerda, un polarizador es sencillamente una ranura que permite a la cuerda oscilar en una dirección transversal pero no en la perpendicular.

Para las ondas electromagnéticas, el ejemplo más familiar de polarizador, el Polaroid, fue inventado por Edwin Land hace más de 50 años, en parte en experimentos realizados en el ático del Jefferson Physical Laboratory, donde trabajaba siendo estudiante de grado en Harvard. La idea del polaroid es fabricar un material que conduzca la electricidad (mal) en una dirección, pero no en la otra. Entonces el campo eléctrico en la dirección conductora será absorbido (con la energía yendo a pérdidas resistivas), mientras que el campo eléctrico en la dirección no conductora no se verá afectado. Una manera de conseguirlo es hacer láminas de polímero (alcohol polivinílico) estiradas (para alinear las moléculas del polímero a lo largo de un eje preferente) y dopadas con yodo (para permitir la conducción a lo largo de las moléculas del polímero).[^land]

[^land]: Véase Sears, Zemansky y Young, página 813.

### 12.3.3 Láminas de onda

Las «láminas de onda» son elementos ópticos que cambian la fase relativa de las dos componentes de $Z$. Las láminas de onda son posibles porque existen materiales en los que el índice de refracción depende de la polarización. Esta propiedad se llama «birrefringencia», y puede darse de varias maneras.

Por ejemplo, el celofán, un material polimérico transparente, se convierte en láminas delgadas mediante estirado. A causa del estirado, las cadenas del polímero tienden a orientarse a lo largo de la dirección de estiramiento. La constante dieléctrica de este material depende de la dirección del campo eléctrico: a las cargas les resulta más fácil moverse a lo largo de las cadenas del polímero que atravesarlas. Así, la constante dieléctrica es mayor para campos eléctricos en la dirección de estirado.

El mismo efecto puede surgir por la estructura inherente de un cristal transparente. Un ejemplo es el mineral natural calcita, una forma cristalina del carbonato de calcio, CaCO₃. Los cristales de calcita tienen la fascinante propiedad de desdoblar un haz de luz no polarizada en sus dos estados de polarización. La birrefringencia puede incluso producirse mecánicamente, tensionando un material transparente, es decir, comprimiendo la estructura electrónica en una dirección.

Sea cual sea la forma en que se produzca la birrefringencia, podemos fabricar una lámina de onda orientando el material de modo que las direcciones $x$ e $y$ correspondan a índices de refracción distintos, $n_x$ y $n_y$, y cortando después una rebanada del material en forma de lámina en el plano $x$-$y$, con cierto espesor $\ell$ en la dirección $z$. Entonces una onda electromagnética que viaja en la dirección $z$ a través de la lámina tiene valores de $k$ distintos según su polarización:

$$k = \begin{cases} \dfrac{n_x\omega}{c} & \text{para polarización en la dirección } x \\[6pt] \dfrac{n_y\omega}{c} & \text{para polarización en la dirección } y \end{cases} \tag{12.38}$$

En particular, la diferencia de fase entre la luz polarizada en $x$ y en $y$ al atravesar la lámina es

$$\Delta\phi = \frac{(n_x - n_y)\,\omega\,\ell}{c}. \tag{12.39}$$

Nótese que, en general, la diferencia de fase $\Delta\phi$ depende de la frecuencia de la luz. Incluso si $n_x$ y $n_y$ dependen de la frecuencia, sería una casualidad extravagante que esa dependencia cancelara la dependencia en $\omega$ del factor explícito de $\omega$ en (12.39).

*(Figura 12.5: luz inicialmente no polarizada atravesando un par de polarizadores cruzados con una lámina de onda entre ellos.)*

Consideremos ahora la colocación de una lámina de onda así entre dos polarizadores cruzados, orientados a $\pm 45°$, como se muestra en la figura 12.5. Sin la lámina de onda no pasaría nada de luz, porque el primer polarizador solo transmite luz polarizada a $45°$, descrita por el vector $Z$

$$Z = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix} \tag{12.40}$$

y el segundo polarizador la absorbe.

Al salir del primer polarizador, el vector $Z$ tiene el aspecto de (12.40) para todas las componentes de frecuencia de la luz blanca. Pero cuando se inserta la lámina de onda en medio, se añade una diferencia de fase dependiente de la frecuencia, de modo que el vector $Z$ que sale de la lámina de onda (salvo una fase global irrelevante) tiene el aspecto

$$Z = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ e^{-i\Delta\phi} \end{pmatrix}.$$

Para las frecuencias tales que $e^{-i\Delta\phi}$ vale $-1$, la luz queda polarizada en la dirección $-45°$ y atraviesa el segundo polarizador sin más atenuación. Pero para las frecuencias tales que $e^{-i\Delta\phi}$ vale $1$, la luz sigue siendo absorbida por el segundo polarizador. Las frecuencias intermedias se absorben parcialmente.

Es esta dependencia con la frecuencia la que produce los interesantes patrones de color que se ven al poner celofán, o un trozo de plástico tensionado, entre polarizadores.

### 12.3.4 Matrices

Los efectos de las láminas de onda, los polarizadores y demás pueden resumirse mediante la multiplicación del vector $Z$ por matrices $2\times2$. Por ejemplo, un polarizador perfecto con el eje formando un ángulo $\theta$ con el eje 1 puede representarse por

$$P_\theta = \begin{pmatrix} \cos^2\theta & \cos\theta\sin\theta \\ \cos\theta\sin\theta & \sin^2\theta \end{pmatrix}. \tag{12.42}$$

El objeto $P_\theta$ se denomina «operador de proyección», porque proyecta el vector sobre la dirección paralela a $u_\theta$. Satisface

$$P_\theta P_\theta = P_\theta, \tag{12.43}$$

como debe ser, ya que el primer polarizador produce luz polarizada y el segundo la transmite perfectamente. $P_\theta$ actuando sobre un vector transmite la componente en la dirección $\theta$. Esto es más fácil de visualizar si $\theta = 0$ o $\pi/2$. Las matrices

$$P_0 = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \qquad P_{\pi/2} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \tag{12.44}$$

representan polarizadores a lo largo de los ejes 1 y 2 respectivamente.

Una lámina de onda en la que la diferencia de fase es $\pi/2$ se llama «lámina de cuarto de onda». Para una lámina de onda en la que la diferencia de fase está entre $0$ y $\pi$, se acostumbra a llamar «eje rápido» al eje con la fase menor. Una lámina de cuarto de onda con el eje rápido a lo largo del eje 1 se representa por

$$Q_0 = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}. \tag{12.45}$$

Obsérvese que podemos escribir

$$Q_0 = P_0 + iP_{\pi/2}. \tag{12.46}$$

Esto debería convencerle de que, en general, si el eje rápido está en la dirección $\theta$, la lámina de cuarto de onda tiene el aspecto

$$Q_\theta = P_\theta + iP_{\theta + \pi/2}. \tag{12.47}$$

La discusión de (12.39) muestra que, en general, una lámina de onda solo será una lámina de cuarto de onda para luz de una frecuencia definida.

Una lámina de onda en la que la diferencia de fase es $\pi$ se llama «lámina de media onda». Se obtiene una lámina de media onda sustituyendo la $i$ de (12.45)-(12.47) por $-1$. Así,

$$H_\theta = P_\theta - P_{\theta + \pi/2}. \tag{12.48}$$

Obsérvese que

$$H_\theta = Q_\theta Q_\theta; \tag{12.49}$$

dos láminas de cuarto de onda hacen una lámina de media onda.

*(Figura 12.6: producción de luz polarizada circularmente.)*

He aquí dos dispositivos divertidos que puede construir con estos elementos ópticos (o matrices). Considere la combinación de, primero, un polarizador a $45°$ y después una lámina de cuarto de onda, como se muestra en la figura 12.6. Formando el producto matricial $Q_0 P_{\pi/4}$ puede ver que esto produce luz polarizada circularmente en sentido antihorario a partir de cualquier cosa que tenga una componente de polarización en la dirección $\pi/4$. El argumento es el siguiente. El producto es

$$Q_0 P_{\pi/4} = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}\frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 1 & 1 \\ i & i \end{pmatrix}. \tag{12.50}$$

Cuando esto actúa sobre un vector arbitrario se obtiene polarización circular, salvo que el vector sea aniquilado por $P_{\pi/4}$:

$$Q_0 P_{\pi/4}\begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix} = \frac{\psi_1 + \psi_2}{2}\begin{pmatrix} 1 \\ i \end{pmatrix}. \tag{12.51}$$

En el orden opuesto, $P_{\pi/4}Q_0$ es un analizador de luz polarizada circularmente: aniquila la luz antihoraria y convierte la luz polarizada en sentido horario en luz polarizada linealmente en la dirección $\pi/4$.

### 12.3.5 Actividad óptica

La «actividad óptica» es una propiedad de muchos compuestos orgánicos y de algunos inorgánicos. Un material ópticamente activo rota la polarización de la luz sin absorber ninguna de las dos componentes de la polarización. Un ejemplo familiar de tal material es el jarabe de maíz, una disolución acuosa espesa de azúcar que probablemente tenga en la cocina. Si pone un recipiente rectangular de jarabe de maíz entre polarizadores, como se muestra en la figura 12.7, y rota el segundo polarizador hasta que la intensidad de la luz que pasa sea máxima, encontrará que la dirección del segundo polarizador no es la misma que la del primero. El plano de la polarización ha sido rotado un cierto ángulo $\theta$. El ángulo de rotación $\theta$ es proporcional al espesor del recipiente, es decir, a la longitud de la región de jarabe que atraviesa la luz.

*(Figura 12.7: un recipiente rectangular de jarabe de maíz entre polarizadores.)*

Está claro que la actividad óptica del jarabe de maíz no puede depender de la estructura cristalina, porque el material es un líquido perfectamente uniforme, completamente invariante bajo rotaciones en el espacio tridimensional. No puede tener ejes especiales ni nada por el estilo. La actividad óptica debe funcionar de manera muy distinta a la birrefringencia.

Puede encontrar una pista sobre la naturaleza de la actividad óptica considerando qué aspecto tiene vista en un espejo. Si refleja el sistema ilustrado en la figura 12.7 en el plano $x$-$z$, cambiando el signo de todas las coordenadas $y$, el ángulo $\theta$ cambia a $-\theta$. Así pues, el jarabe de maíz que ve en un espejo debe ser fundamentalmente distinto del jarabe de maíz de su cocina. Esto no es tan extraño: al fin y al cabo, su mano derecha parece una mano izquierda cuando la mira en un espejo. El jarabe de maíz debe tener la misma propiedad y poseer una «lateralidad» definida. De hecho, a causa de los enlaces tetraédricos de los átomos de carbono con que están construidas, las moléculas de azúcar del jarabe de maíz pueden tener, y tienen, tal lateralidad.

Debido a la lateralidad de las moléculas de azúcar, el índice de refracción del jarabe de maíz depende en realidad de la lateralidad de la luz: es ligeramente distinto para la luz polarizada circularmente a izquierdas y a derechas. Esto ocurre porque el campo $\vec{E}$ de un haz polarizado circularmente gira ligeramente al recorrer cada molécula de azúcar y ve una estructura electrónica algo distinta según el sentido del giro. Entonces, como los índices de refracción son ligeramente distintos, las componentes polarizadas circularmente a izquierdas y a derechas adquieren factores de fase distintos ($k\ell$) al atravesar un espesor $\ell$ del jarabe.

Podemos usar ahora nuestro lenguaje matricial para ver cómo lleva esto a la actividad óptica. Salvo una fase global irrelevante, podemos elegir que la fase producida sobre la luz polarizada circularmente a izquierdas sea $-\theta$ y la producida sobre la polarizada a derechas sea $\theta$. Entonces podemos representar la acción del jarabe sobre una onda arbitraria mediante la matriz

$$e^{-i\theta}P_+ + e^{i\theta}P_-, \tag{12.52}$$

donde $P_\pm$ son matrices que seleccionan las componentes polarizadas circularmente a izquierdas y a derechas, respectivamente. Satisfacen

$$P_\pm\begin{pmatrix} 1 \\ \pm i \end{pmatrix} = \begin{pmatrix} 1 \\ \pm i \end{pmatrix}, \qquad P_\pm\begin{pmatrix} 1 \\ \mp i \end{pmatrix} = 0.$$

Puede comprobar que las matrices son

$$P_\pm = \frac{1}{2}\begin{pmatrix} 1 & \mp i \\ \pm i & 1 \end{pmatrix}. \tag{12.53}$$

Entonces (12.52) se convierte en

$$e^{-i\theta}\frac{1}{2}\begin{pmatrix} 1 & -i \\ i & 1 \end{pmatrix} + e^{i\theta}\frac{1}{2}\begin{pmatrix} 1 & i \\ -i & 1 \end{pmatrix} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}. \tag{12.54}$$

¡Esta es precisamente la matriz de rotación $R_\theta$ de (12.34)! $R_\theta$ rota ambas componentes de cualquier luz un ángulo $\theta$.

Cabe preguntarse por la razón de la lateralidad de las moléculas de azúcar. De hecho, existen procesos físicos —las interacciones débiles, que dan lugar a la radiactividad $\beta$— que se ven distintos al reflejarse en un espejo[^paridad] y que, por tanto, podrían en principio distinguir entre moléculas levógiras y dextrógiras. Sin embargo, lo más probable es que esas interacciones sean irrelevantes para la lateralidad del jarabe de maíz. Probablemente la razón sea biológica, no física. Hace mucho tiempo, cuando los comienzos de la vida emergieron del caldo primordial, por puro accidente se emplearon los azúcares dextrógiros. Desde entonces, la lateralidad se ha mantenido por los procesos de reproducción.

[^paridad]: Violan lo que se llama la simetría de «paridad».

*(Figura 12.8: luz inicialmente no polarizada atravesando un par de polarizadores cruzados.)*

### 12.3.6 Polarizadores cruzados y mecánica cuántica

La polarización ofrece muchas oportunidades de confundirse cuando se piensa en la onda luminosa en términos de fotones. Imaginemos que bajamos la intensidad de la luz hasta el punto de que pasa un fotón cada vez por los polarizadores, y consideremos primero la situación engañosamente simple de luz que se mueve en la dirección $z$ a través de polarizadores cruzados en el plano $x$-$y$. Supongamos que el primer polarizador transmite luz polarizada en la dirección $x$ y el segundo transmite luz polarizada en la dirección $y$. Esto es engañosamente simple porque parece que podemos interpretar lo que ocurre sencillamente en términos de fotones. La situación se representa en la figura 12.8. Parece bastante sencillo de interpretar en términos de fotones: la luz no polarizada de la región I está compuesta a partes iguales por fotones polarizados en la dirección $x$ y en la dirección $y$ (así reza el argumento «clásico», que es erróneo). Los polarizados en la dirección $x$ atraviesan el primer polarizador, de modo que la mitad de los fotones siguen presentes en la región II, donde la intensidad se reduce a la mitad. Después, ninguno de estos atraviesa el segundo polarizador, así que la intensidad en la región III es cero.

Pero compare esto con la situación aparentemente similar en la que el segundo polarizador transmite luz polarizada a $45°$ en el plano $x$-$y$, como se muestra en la figura 12.9. Ahora la descripción ondulatoria nos dice que la intensidad en la región III se reduce en otro factor de 2 respecto de la de la región II. Esto es imposible de interpretar en términos de partículas clásicas. Para verlo, basta con bajar la intensidad de modo que solo pase un fotón cada vez. Entonces el primer polarizador no da problemas: como antes, si el fotón está polarizado en la dirección $x$, pasa. Pero ¿qué ocurre ahora en el segundo polarizador? El fotón no puede partirse: o pasa o no pasa. Para ser coherente con la descripción ondulatoria, en la que la intensidad se reduce en otro factor de dos, la transmisión en el segundo polarizador debe ser un suceso probabilístico. La mitad de las veces el fotón pasa; la mitad de las veces es absorbido. No hay manera de que el fotón de la región II sepa si va a lograrlo. Es aleatorio. Dios juega a los dados.

*(Figura 12.9: luz inicialmente no polarizada atravesando un par de polarizadores con los ejes a $45°$.)*

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

*(Figura 12.10: dispersión de ondas planas en un contorno plano.)*

Los detalles de la dispersión dependerán de la polarización. Está claro (por simetría, como de costumbre) que los dos casos serán la polarización en el plano $x$-$z$ y la polarización perpendicular al plano $x$-$z$. Por supuesto, no perdemos nada considerándolos por separado, gracias a la linealidad: cualquier polarización de la onda incidente puede tratarse formando una combinación lineal de las soluciones paralela y perpendicular.

### 12.4.1 Polarización perpendicular al plano de dispersión

Consideremos primero la polarización perpendicular. Esto significa que el campo eléctrico está en la dirección $y$ (saliendo del plano del papel), mientras que el campo magnético está en el plano $x$-$z$:[^fresnel]

$$E_y(r, t) = A e^{i(\vec{k}\cdot\vec{r} - \omega t)} + R_\perp A e^{i(\tilde{\vec{k}}\cdot\vec{r} - \omega t)} \quad \text{para } z \leq 0$$

$$E_y(r, t) = \tau_\perp A e^{i(\vec{k}'\cdot\vec{r} - \omega t)} \quad \text{para } z \geq 0$$

$$E_z = E_x = 0$$

[^fresnel]: Las magnitudes $R_\perp$ y $\tau_\perp$ de esta sección, y $R_\parallel$ y $\tau_\parallel$ de la siguiente, se llaman convencionalmente «coeficientes de Fresnel». Véase Hecht, página 97.

Usando (12.19),

$$\vec{B} = \frac{1}{\omega}\vec{k}\times\vec{E} = \frac{n}{c}\hat{k}\times\vec{E},$$

podemos escribir

$$B_x(r, t) = -\frac{n}{c}\cos\theta\,A e^{i(\vec{k}\cdot\vec{r} - \omega t)} + \frac{n}{c}\cos\theta\,R_\perp A e^{i(\tilde{\vec{k}}\cdot\vec{r} - \omega t)} \quad \text{para } z \leq 0$$

$$B_x(r, t) = -\frac{n'}{c}\cos\theta'\,\tau_\perp A e^{i(\vec{k}'\cdot\vec{r} - \omega t)} \quad \text{para } z \geq 0$$

$$B_z(r, t) = \frac{n}{c}\sin\theta\,A e^{i(\vec{k}\cdot\vec{r} - \omega t)} + \frac{n}{c}\sin\theta\,R_\perp A e^{i(\tilde{\vec{k}}\cdot\vec{r} - \omega t)} \quad \text{para } z \leq 0$$

$$B_z(r, t) = \frac{n'}{c}\sin\theta'\,\tau_\perp A e^{i(\vec{k}'\cdot\vec{r} - \omega t)} \quad \text{para } z \geq 0$$

El sistema se muestra en la figura 12.11. Esa figura muestra las direcciones de los campos magnéticos de las ondas componentes incidente ($\vec{B}_i$), reflejada ($\vec{B}_r$) y transmitida ($\vec{B}_t$) en la dispersión de una onda plana electromagnética polarizada paralelamente a un contorno dieléctrico plano. Los vectores $\vec{k}$ se muestran justo debajo de los campos magnéticos. Las condiciones de contorno no triviales son que $E_y$ y $B_x$ sean continuos (esto último porque hemos supuesto $\mu = 1$, así que no hay una lámina de corriente ligada en el contorno). $B_z$ también es continuo, pero eso no aporta información nueva. Así,

$$1 + R_\perp = \tau_\perp$$

*(Figura 12.11: dispersión de una onda plana electromagnética polarizada paralelamente a un contorno dieléctrico.)*

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

$$\tau_\parallel = \frac{2}{1 + \xi_\parallel}, \qquad R_\parallel = \frac{1 - \xi_\parallel}{1 + \xi_\parallel} \tag{12.74}$$

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

*(Figura 12.12: ángulo de Brewster.)*

## 12.5 Radiación

En esta sección escribimos los campos eléctrico y magnético asociados a densidades de carga y de corriente variables.

### 12.5.1 Campos de cargas en movimiento

Como las ecuaciones de Maxwell son ecuaciones en derivadas parciales, hay que especificar muchas condiciones iniciales o de contorno para determinar las soluciones. Por ejemplo, un campo eléctrico constante en todas partes es solución de las ecuaciones de Maxwell en el espacio libre y, por tanto, se puede sumar un campo constante a cualquier solución y seguirá siendo solución. Tales cosas deben determinarse mediante condiciones físicas iniciales o de contorno. Un conjunto de condiciones que resulta interesante con frecuencia es un análogo de la condición de contorno en el infinito que discutimos para las ondas unidimensionales. Suponga que tiene un universo inicialmente estacionario, sin corrientes eléctricas, sin campos magnéticos y con campos eléctricos debidos solo a cargas estacionarias (que sabe calcular de Física 15b). En cierto instante empieza a mover cargas en alguna región finita del espacio. ¿Cuáles son los campos eléctrico y magnético producidos de este modo? Esta pregunta tiene una respuesta relativamente sencilla, que es una bonita generalización intuitiva de las relaciones que aprendió en 15b para los potenciales eléctrico y vectorial de distribuciones estacionarias de carga y corriente. Aquellas relaciones eran

$$\phi(\vec{r}) = \int d^3r'\,\frac{\rho(\vec{r}')}{|\vec{r} - \vec{r}'|}, \qquad \vec{A}(\vec{r}) = \frac{1}{c}\int d^3r'\,\frac{\vec{J}(\vec{r}')}{|\vec{r} - \vec{r}'|}.$$

Las generalizaciones son

$$\phi(\vec{r}, t) = \int d^3r'\,\frac{\rho(\vec{r}', t - |\vec{r} - \vec{r}'|/c)}{|\vec{r} - \vec{r}'|}, \tag{12.82}$$

$$\vec{A}(\vec{r}, t) = \frac{1}{c}\int d^3r'\,\frac{\vec{J}(\vec{r}', t - |\vec{r} - \vec{r}'|/c)}{|\vec{r} - \vec{r}'|}. \tag{12.83}$$

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

$$\vec{B} \approx -\frac{1}{c^2}\int d^3r'\,\frac{\vec{r} - \vec{r}'}{|\vec{r} - \vec{r}'|^2}\times\frac{d}{dt}\vec{J}(\vec{r}', t - |\vec{r} - \vec{r}'|/c) \approx -\frac{1}{c^2}\frac{\hat{r}}{r}\times\int d^3r'\,\frac{d}{dt}\vec{J}(\vec{r}', t - |\vec{r} - \vec{r}'|/c), \tag{12.92}$$

donde en (12.92) hemos despreciado un $\vec{r}'$ en el numerador porque ese término decae como $1/r^2$ para $r$ grande.

Este es el campo magnético de una onda electromagnética. Nótese que es perpendicular a la dirección de movimiento ($\hat{r}$). El decaimiento como $1/r$ es lo que esperamos para una onda electromagnética, porque la densidad de energía va como el cuadrado del campo y decae como $1/r^2$ conforme la onda se extiende.

El campo eléctrico puede calcularse de manera similar, aunque también hace falta usar la conservación de la carga eléctrica,

$$\frac{\partial}{\partial t}\rho + \vec{\nabla}\cdot\vec{J} = 0.$$

Como cabe esperar, el resultado es que el campo eléctrico tiene la misma magnitud que el campo magnético y es perpendicular tanto a la dirección de movimiento como al campo magnético. La parte que corresponde a una onda electromagnética viajera puede escribirse como

$$\vec{E} \approx \frac{1}{c^2}\frac{1}{r}\int d^3r'\;\hat{r}\times\left(\hat{r}\times\frac{d}{dt}\vec{J}(\vec{r}', t - |\vec{r} - \vec{r}'|/c)\right). \tag{12.95}$$

Al orden más bajo en $1/r$, para cargas que se mueven con velocidades mucho menores que $c$, podemos simplificar el campo eléctrico de (12.95) sustituyendo

$$|\vec{r} - \vec{r}'| \to r$$

y escribir el resultado como

$$\vec{E}(\vec{r}, t) \approx \frac{1}{c^2}\frac{1}{r}\int d^3r'\;\hat{r}\times\left(\hat{r}\times\frac{d}{dt}\vec{J}(\vec{r}', t - r/c)\right). \tag{12.97}$$

La razón de la restricción al movimiento no relativista de las cargas es que, si una partícula cargada se mueve a una velocidad próxima a la de la luz, entonces no podemos despreciar su posición $\vec{r}'$ cuando se mueve hacia $\vec{r}$. Para verlo, considere el límite imposible en el que la carga se mueve hacia el punto $\vec{r}$ a la velocidad de la luz. Entonces, si la carga contribuye al campo eléctrico en $\vec{r}$ en un instante, también contribuye en instantes posteriores, porque la partícula acompaña a la onda luminosa. Aunque $v = c$ es imposible, para $v \approx c$ la dependencia en $\vec{r}'$ no puede ignorarse, porque lleva a una dependencia temporal muy rápida de los potenciales y, por tanto, a campos grandes. Lo que ocurre es que la contribución de las cargas que se mueven relativistamente a los campos eléctricos que tienen delante se ve amplificada por factores de $\frac{c}{c - v}$. Este efecto se usa hoy ampliamente para producir «luz» intensa a partir de aceleradores de partículas: la llamada radiación de sincrotrón. Puede ver este efecto en las ANIMACIONES si hace $v$ próxima a 1.

Un caso particularmente importante e instructivo de (12.97) es el movimiento no relativista de una sola carga $Q$ que se desplaza a lo largo de una trayectoria $\vec{R}(t)$. Para este sistema,[^delta]

$$\vec{J}(\vec{r}, t) = Q\,\vec{v}(t)\,\delta^3(\vec{r} - \vec{R}(t)) = Q\,\frac{d\vec{R}(t)}{dt}\,\delta^3(\vec{r} - \vec{R}(t)).$$

[^delta]: Esta ecuación emplea la notación de la función $\delta$. Para un físico, una función $\delta(x)$ es simplemente una función de área 1 tan puntiaguda alrededor de $x = 0$ que no nos importa exactamente qué aspecto tiene. Lo único que importa es el área y dónde está el pico. La $\delta^3(\vec{r} - \vec{R}(t))$ de la ecuación es en realidad el producto de tres funciones delta, para las componentes $x$, $y$ y $z$, y solo dice que $\vec{r} = (x, y, z) = \vec{R}(t) = (X(t), Y(t), Z(t))$, es decir, que la partícula se mueve a lo largo de la trayectoria $\vec{R}(t)$. Para una discusión matemática de la función $\delta$ puede consultar <http://mathworld.wolfram.com/DeltaFunction.html>. Pero no se asuste: es solo un recurso sencillo para ignorar detalles pequeños que no nos importan. Si traduce la integral a palabras o a dibujos, puede que ayude.

Entonces la integración sobre $d^3r'$ elimina la función $\delta$, y el campo eléctrico de la onda electromagnética saliente es proporcional a la aceleración:

$$\vec{E}(\vec{r}, t) \approx \frac{1}{c^2}\frac{1}{r}\,Q\;\hat{r}\times\left(\hat{r}\times\vec{a}(t - r/c)\right) \tag{12.102}$$

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

*(Figura 12.13: la componente de $\hat{z}$ perpendicular a $\vec{r}$.)*

Evidentemente, la magnitud de $\hat{z} - \hat{r}(\hat{r}\cdot\hat{z})$ es $\sin\theta$. Esto significa que la intensidad de la onda electromagnética a un ángulo $\theta$ del eje $z$ es proporcional a $\sin^2\theta$. El patrón de intensidad puede representarse cómodamente en coordenadas polares, dibujando la intensidad en función de $\theta$. El resultado es el «diagrama de antena» del dipolo oscilante en la dirección $z$, y se muestra en la figura 12.14. Los dos lóbulos del diagrama surgen porque el campo es máximo en el plano $x$-$y$, para $\theta = \pi/2$, y cae a cero conforme nos acercamos al eje $z$, $\theta = 0$ o $\theta = \pi$.

*(Figura 12.14: diagrama de antena de un dipolo oscilante.)*

### 12.5.3 * Comprobación de las ecuaciones de Maxwell

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

i. Describir la polarización en una cuerda con cuentas o continua;

ii. Escribir la forma general de una onda plana electromagnética y relacionarla con el vector bidimensional $Z$;

iii. Hallar la densidad de energía y de momento de una onda plana electromagnética;

iv. Comprender los estados de polarización posibles de una onda plana;

v. Analizar sistemas de polarizadores y láminas de onda mediante multiplicación de matrices;

vi. Comprender la conexión entre la actividad óptica y la lateralidad;

vii. Calcular la reflexión y la transmisión de una onda plana electromagnética en un contorno plano entre dieléctricos para cualquier ángulo, y hallar y explicar el ángulo de Brewster.

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

---

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*
