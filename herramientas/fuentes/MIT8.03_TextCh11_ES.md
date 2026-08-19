---
title: "Capítulo 11: Dos y tres dimensiones — 8.03SC Física III: Vibraciones y Ondas"
author: "Yen-Jie Lee (traducción al español)"
lang: es
---

# Capítulo 11: Dos y tres dimensiones

Los conceptos de invariancia bajo traslación espacial e interacciones locales pueden extenderse de forma directa a sistemas con más de una dimensión espacial. Pero en dos y tres dimensiones estas ideas por sí solas no bastan para determinar los modos normales de un sistema arbitrario. Hacen falta trucos adicionales, o trabajo duro y llano.

<h2 id="vídeos-de-esta-clase-youtube">Vídeos de esta clase (YouTube)</h2>
<ul>
<li class="video-item">
<button type="button" class="video-play" data-vid="_kKIQ1h9UuA" data-title="Clase 16: Ondas en 2D y 3D, ley de Snell">
<span class="video-play-icon">▶</span> <strong>Clase 16: Ondas en 2D y 3D, ley de Snell</strong>
</button>
<a class="video-ext" href="https://www.youtube.com/watch?v=_kKIQ1h9UuA" target="_blank" rel="noopener">YouTube ↗</a>
</li>
</ul>

## Resumen previo

Aquí solo podremos discutir los trucos más sencillos, pero al menos podremos entender por qué los problemas son más difíciles.

i. Empezamos explicando por qué el número de onda angular, $k$, se convierte en un vector en dos o tres dimensiones. Hallamos los modos normales de sistemas con condiciones de contorno sencillas.

ii. Discutimos después la dispersión en planos en el espacio de dos y tres dimensiones. Deducimos la ley de refracción de Snell y discutimos la reflexión total interna y el efecto túnel.

iii. Discutimos el ejemplo de las placas de Chladni.

iv. Damos un ejemplo bidimensional de guía de ondas, en la que las ondas están obligadas a propagarse solo en una dirección.

v. Estudiamos las ondas en el agua (en una versión simplificada del agua).

vi. Introducimos el tema más avanzado de las ondas esféricas.

## 11.1 El vector $\vec{k}$

Considere la malla bidimensional de cuentas, un análogo bidimensional de la cuerda con cuentas, mostrada en la figura 11.1. Todas las cuentas tienen masa $m$. La tensión de las cuerdas horizontales (verticales) es $T_H$ ($T_V$) y la distancia entre cuentas es $a_H$ ($a_V$). No hay amortiguamiento. Podemos etiquetar las cuentas mediante un par de enteros $(j, k)$ que indican sus posiciones horizontal y vertical, como se muestra. Alternativamente, podemos etiquetarlas por sus posiciones en el plano $x$, $y$ según

$$(x, y) = (j a_H, k a_V). \tag{11.1}$$

*(Figura 11.1: una malla bidimensional de cuentas.)*

Así pues, podemos describir sus pequeñas oscilaciones transversales (fuera del plano del papel, en la dirección $z$) o bien mediante una matriz $\psi_{jk}(t)$, o bien mediante una función

$$\psi(x, y, t); \qquad 0 \leq x \leq 5a_H,\ 0 \leq y \leq 4a_V. \tag{11.2}$$

Usaremos (11.2) porque así podremos extender la discusión a sistemas continuos con más facilidad. Solo nos interesan las oscilaciones transversales de este sistema, en las que los bloques se mueven arriba y abajo fuera del plano del papel, porque esas oscilaciones no estiran mucho las cuerdas (solo a segundo orden en los desplazamientos pequeños). Las demás oscilaciones de un sistema así tienen frecuencias mucho más altas y están fuertemente amortiguadas, de modo que no son muy interesantes.

Como en el caso unidimensional, el primer paso es quitar las paredes y considerar el sistema infinito que se obtiene extendiendo el interior en todas las direcciones. Las oscilaciones del sistema resultante pueden describirse mediante una función $\psi(x, y, t)$, donde $x$ e $y$ no están restringidas.

Este sistema infinito tiene el mismo aspecto si se traslada $a_V$ verticalmente o $a_H$ horizontalmente. Podemos escribir soluciones para el sistema infinito usando dos veces nuestra discusión del caso unidimensional. Como el sistema tiene invariancia bajo traslación en la dirección $x$, esperamos poder hallar autoestados de la matriz $M^{-1}K$ proporcionales a

$$e^{ik_x x} \tag{11.3}$$

para cualquier constante $k_x$. Como el sistema tiene invariancia bajo traslación en la dirección $y$, esperamos poder hallar autoestados de $M^{-1}K$ proporcionales a

$$e^{ik_y y} \tag{11.4}$$

para cualquier constante $k_y$. Juntando (11.3) y (11.4), esperamos poder hallar autoestados de $M^{-1}K$ que tengan la forma

$$\psi(x, y) = A\,e^{ik_x x}e^{ik_y y} = A\,e^{i\vec{k}\cdot\vec{r}} \tag{11.5}$$

donde $\vec{k}\cdot\vec{r}$ es el producto escalar bidimensional

$$\vec{k}\cdot\vec{r} = k_x x + k_y y. \tag{11.6}$$

Dicho de otro modo, el número de onda se ha convertido en un vector.

Igual que con el sistema unidimensional, podemos usar (11.5) para determinar la relación de dispersión del sistema infinito. Incluyendo la dependencia en $t$, tenemos un desplazamiento de la forma

$$\psi(x, y, t) = A\,e^{i\vec{k}\cdot\vec{r}}\,e^{-i\omega t}. \tag{11.7}$$

El análisis es exactamente análogo al de la cuerda unidimensional con cuentas, con el resultado de que $\omega^2$ es simplemente una suma de contribuciones vertical y horizontal, cada una de las cuales tiene el aspecto de la relación de dispersión del caso unidimensional:

$$\omega^2 = \frac{4T_H}{m a_H}\sin^2\frac{k_x a_H}{2} + \frac{4T_V}{m a_V}\sin^2\frac{k_y a_V}{2}. \tag{11.8}$$

Las ecuaciones (11.7) y (11.8) son la solución completa de las ecuaciones del movimiento de la malla infinita de cuentas.

### 11.1.1 La diferencia entre una y dos dimensiones

Hasta aquí, nuestro análisis ha sido esencialmente el mismo en dos dimensiones que en una. El paso siguiente, sin embargo, es muy distinto. En el caso unidimensional, donde los modos normales son $e^{\pm ikx}$, solo hay dos modos con un valor dado de $\omega^2$. Así, sean cuales sean las condiciones de contorno, solo tenemos que preocuparnos de superponer dos modos a la vez. Pero en el caso bidimensional hay un número continuamente infinito de soluciones de (11.8) para cualquier $\omega$, porque se puede bajar $k_x$ y compensar subiendo $k_y$. Así, un modo normal del sistema bidimensional finito sin amortiguamiento (que no es más que alguna solución en la que todas las cuentas oscilan en fase con la misma $\omega$) puede ser una combinación lineal de un número infinito de los bonitos y sencillos modos del sistema infinito invariantes bajo traslación.

En efecto, en general el caso bidimensional es infinitamente más difícil. Si la figura 11.1 fuera un sistema con una forma más complicada, no seríamos capaces de encontrar una solución analítica. Pero para el caso especial de un marco rectangular alineado con las cuentas, las condiciones de contorno no son tan malas, porque tanto los modos (11.5) como las condiciones de contorno pueden expresarse de forma sencilla en términos de productos de modos normales unidimensionales.

Las condiciones de contorno del sistema de la figura 11.1 son

$$\psi(0, y, t) = \psi(L_H, y, t) = \psi(x, 0, t) = \psi(x, L_V, t) = 0, \tag{11.9}$$

donde

$$L_H = 5a_H, \qquad L_V = 4a_V. \tag{11.10}$$

En el sistema infinito correspondiente, del que se muestra un fragmento en la figura 11.2, (11.9) implica que las cuentas a lo largo del rectángulo punteado están todas en reposo. Comparando la figura 11.1 y la figura 11.2, puede verse que esta condición de contorno recoge la física de las paredes de la figura 11.1.

*(Figura 11.2: un fragmento de una malla bidimensional infinita de cuentas.)*

Ahora, para hallar los modos normales del sistema finito de la figura 11.1, debemos encontrar combinaciones lineales de modos del sistema infinito que satisfagan las condiciones de contorno (11.9). Podemos satisfacer (11.9) formando combinaciones lineales de solo cuatro modos del sistema infinito,[^simetria]

$$A\,e^{\pm ik_x x}e^{\pm ik_y y} \tag{11.11}$$

donde

$$k_x = n\pi/L_H, \qquad k_y = n'\pi/L_V. \tag{11.12}$$

[^simetria]: ¡Aquí hay una simetría en juego! Los modos en los que el vector $\vec{k}$ está alineado con los ejes $x$ o $y$ son los que se comportan de forma sencilla bajo reflexiones a través del centro del rectángulo.

Entonces podemos tomar las soluciones como un producto de senos,

$$\psi(x, y) = A\sin(n\pi x/L_H)\sin(n'\pi y/L_V) \tag{11.13}$$

para $n = 1$ a 4 y $n' = 1$ a 3.

La frecuencia de cada modo viene dada por la relación de dispersión (11.8):

$$\omega^2 = \frac{4T_H}{m a_H}\sin^2\frac{n\pi a_H}{2L_H} + \frac{4T_V}{m a_V}\sin^2\frac{n'\pi a_V}{2L_V}. \tag{11.14}$$

Estos modos están animados en el programa 11-1.

La solución de este problema es un ejemplo de una técnica llamada «separación de variables». En las variables adecuadas —en este caso, $x$ e $y$— el problema se descompone en problemas unidimensionales. Este truco funciona igual de bien en el caso continuo, siempre que la superficie de contorno sea rectangular. Si tomamos el límite en el que $a_V$ y $a_H$ son muy pequeñas comparadas con las longitudes de onda de interés, podemos expresar (11.8) en términos de cantidades que tengan sentido en el límite continuo, igual que en el análisis de la cuerda unidimensional continua como límite de la cuerda con cuentas, en el capítulo 6. Supongamos, por simplicidad, que

$$a_V = a_H = a \qquad \text{y} \qquad T_V = T_H = T \tag{11.15}$$

(de modo que las direcciones $x$ e $y$ tengan las mismas propiedades). Las cantidades que caracterizan la superficie en este caso son la densidad superficial de masa,

$$\rho_s = \frac{m}{a^2} \tag{11.16}$$

y la tensión superficial,

$$T_s = \frac{T}{a}. \tag{11.17}$$

La tensión superficial es la fuerza por unidad de distancia transversal que ejerce la membrana. Cuando estas cantidades permanecen finitas al hacer tender a cero la separación $a$, (11.8) se convierte en

$$\omega^2 = \frac{T_s}{\rho_s}\left(k_x^2 + k_y^2\right) = \frac{T_s}{\rho_s}\vec{k}^2. \tag{11.18}$$

Un argumento precisamente análogo al del caso unidimensional muestra que, en este límite, $\psi(x, y, t)$ satisface la ecuación de ondas bidimensional,

$$\frac{\partial^2}{\partial t^2}\psi(x, y, t) = v^2\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}\right)\psi(x, y, t) = v^2\,\vec{\nabla}^2\psi(x, y, t). \tag{11.19}$$

Nótese que, en este límite, las propiedades especiales de los ejes $x$ e $y$ que se manifestaban en el sistema finito han desaparecido por completo de la ecuación del movimiento. Los números de onda $k_x$ y $k_y$ forman un vector bidimensional $\vec{k}$. El número infinito de soluciones de la relación de dispersión (11.18) son simplemente las que se obtienen rotando $\vec{k}$ de todas las formas posibles sin cambiar su longitud. Esto hace posible resolver los modos normales en regiones circulares, por ejemplo. Pero no discutiremos ahora esas condiciones de contorno más complicadas. Está claro, sin embargo, que (11.13) es la solución para la región rectangular en el caso continuo, y que la frecuencia correspondiente es

$$\omega^2 = \frac{T_s}{\rho_s}\left[\left(\frac{n\pi}{L_H}\right)^2 + \left(\frac{n'\pi}{L_V}\right)^2\right]. \tag{11.20}$$

Ahora, como el sistema es continuo, los enteros $n$ y $n'$ van de cero a infinito (aunque $n = n' = 0$ no es interesante), o hasta que la aproximación continua deja de valer.

### 11.1.2 Tres dimensiones

La malla de cuentas no puede extenderse a tres dimensiones porque no hay dirección transversal. Pero un sistema de masas conectadas por varillas elásticas sí puede ser tridimensional y, de hecho, ese tipo de sistema es un buen modelo de un sólido elástico. Este sistema es bastante más complicado porque cada masa puede moverse en las tres direcciones. En la figura 11.3 se ilustra una versión bidimensional. Este sistema es igual que el de la figura 11.1, salvo que las cuerdas se han sustituido por varillas elásticas ligeras, de modo que el sistema está en equilibrio incluso sin el marco. Ahora nos interesan las oscilaciones de este sistema en el plano del papel. Comparado con la figura 11.1, este sistema tiene el doble de grados de libertad, porque cada bloque puede moverse tanto en la dirección $x$ como en la $y$, mientras que en la figura 11.1 los bloques solo se movían en la dirección $z$. Esto significa que no podemos usar la invariancia bajo traslación espacial por sí sola ni siquiera para determinar los modos del sistema infinito.

*(Figura 11.3: un sólido bidimensional, con masas conectadas por varillas elásticas.)*

Para cada valor de $\vec{k}$ habrá cuatro modos en vez de los dos habituales. Tendríamos que hacer algún análisis matricial para ver qué combinaciones de movimiento en $x$ y en $y$ son realmente los modos normales. No lo haremos en general, pero lo discutiremos brevemente en el límite continuo, para recordarle algo de física que es importante en campos como la geología.

Considere el sistema continuo e infinito que se obtiene haciendo muy pequeñas las $a$ de la figura 11.3, escalando adecuadamente las demás cantidades. Considere una onda con número de onda $\vec{k}$. Los modos normales tendrán la forma

$$\vec{A}\,e^{i\vec{k}\cdot\vec{r} - i\omega t} \tag{11.21}$$

para algún vector $\vec{A}$ (en el caso tridimensional, $\vec{A}$ es un 3-vector; en nuestro ejemplo bidimensional, es un 2-vector). Si el sistema es invariante bajo rotaciones, entonces la física no destaca ninguna dirección salvo la de $\vec{k}$. Entonces los modos normales deben ser un modo longitudinal o «de compresión»,

$$\vec{A} \propto \vec{k}, \tag{11.22}$$

y un modo transversal o «de cizalla»,

$$\vec{A}\cdot\vec{k} = 0. \tag{11.23}$$

Cada modo tendrá su propia relación de dispersión característica. En tres dimensiones habrá dos modos de cizalla, porque hay dos direcciones perpendiculares, y tendrán la misma relación de dispersión, porque uno puede rotarse hasta convertirse en el otro.

*(Figura 11.4: un sistema bidimensional de cuentas y muelles.)*

### 11.1.3 Ondas sonoras

En un líquido o un gas no hay ondas de cizalla, porque no hay ninguna fuerza restauradora que mantenga al sistema en una forma determinada. Los modos de cizalla tienen frecuencia cero. Si sustituyéramos las varillas de la figura 11.3 por muelles sin estirar, obtendríamos un sistema con esa misma propiedad, mostrado en la figura 11.4. Sin el marco, este sistema no sería rígido. Sin embargo, los modos de compresión siguen ahí. Son análogos a las ondas sonoras. Para un sistema aproximadamente continuo, como el aire, esperamos una relación de dispersión de la forma

$$\omega^2 = v^2\vec{k}^2 \tag{11.24}$$

donde $v$ es constante mientras $k$ no sea demasiado grande. Ya hemos calculado $v$, en (7.43), considerando oscilaciones unidimensionales. Se llama velocidad del sonido porque es la velocidad de las ondas sonoras en un sistema infinito o semiinfinito.

Podemos describir los modos normales de una caja rectangular llena de aire en términos de una función $P(x, y, z)$ que describe la presión del gas en el punto $(x, y, z)$. La presión o la densidad de la onda de compresión está relacionada con el desplazamiento $\vec{\psi}$ por

$$P \propto -\vec{\nabla}\cdot\vec{\psi}. \tag{11.25}$$

Como en el sistema bidimensional descrito arriba, podemos usar separación de variables y hallar una solución que sea un producto de funciones de una sola variable. La única diferencia aquí es que las condiciones de contorno son distintas. Debido a (11.25), que es el enunciado matemático del hecho de que el gas es empujado de las regiones de presión alta a las de presión baja, el gradiente de presión perpendicular al contorno debe anularse: el gas del contorno no tiene a dónde ir. Así, los modos normales en una caja rectangular, $0 \leq x \leq X$, $0 \leq y \leq Y$, $0 \leq z \leq Z$, tienen la forma

$$P(x, y, z) = A\cos(n_x\pi x/X)\cos(n_y\pi y/Y)\cos(n_z\pi z/Z) \tag{11.26}$$

con frecuencia

$$\omega = v\sqrt{\left(\frac{n_x\pi}{X}\right)^2 + \left(\frac{n_y\pi}{Y}\right)^2 + \left(\frac{n_z\pi}{Z}\right)^2}. \tag{11.27}$$

La solución trivial $n_x = n_y = n_z = 0$ representa aire estacionario. Si alguna de las $n$ es no nula, el modo es no trivial.

## 11.2 Contornos planos

Las ondas viajeras más fáciles de discutir en dos y tres dimensiones son las «ondas planas», soluciones del sistema infinito de la forma

$$\psi(\vec{r}, t) = A\,e^{i(\vec{k}\cdot\vec{r} - \omega t)}. \tag{11.28}$$

Esto describe una onda que viaja en la dirección del vector de número de onda $\vec{k}$, con la velocidad de fase del medio. El desplazamiento (o lo que sea) es constante sobre planos de $\vec{k}\cdot\vec{r}$ constante, que son perpendiculares a la dirección de movimiento, $\vec{k}$. Estudiaremos ondas viajeras más complicadas pronto, cuando discutamos la difracción. Entonces aprenderemos a describir «haces» de luz, de sonido o de otras ondas, que son las ondas viajeras con las que solemos trabajar, y veremos cómo describirlos como superposiciones de ondas planas. Por ahora, puede pensar en una onda plana como algo parecido a la onda viajera que encontraría dentro de un haz ancho y coherente, o muy lejos de una fuente pequeña de luz casi monocromática, luz de frecuencia definida. Con eso basta para hacerse una imagen física de los fenómenos que discutimos en esta sección.

Lo que más nos interesa son ondas como la luz y el sonido. Sin embargo, es mucho más fácil discutir las oscilaciones transversales de una membrana bidimensional, y muchos de nuestros ejemplos serán de ese sistema. Hay dos razones. Una es que una membrana bidimensional es más fácil de dibujar en un papel bidimensional. La otra es que la física es muy sencilla, así que podemos concentrarnos en las propiedades ondulatorias. Intentaremos señalar dónde se complican las cosas para otros tipos de fenómenos ondulatorios.

Considere dos membranas bidimensionales tensadas en el plano $z = 0$, como se muestra en la figura 11.5. Para $x < 0$, suponga que la densidad superficial de masa es $\rho_s$ y la tensión superficial $T_s$. Para $x > 0$, suponga que la densidad superficial de masa es $\rho_s'$ y la tensión superficial $T_s'$. Este es un análogo bidimensional del sistema de cuerdas que discutimos largamente en el capítulo 9. El contorno entre las dos membranas debe suministrar una fuerza (en este caso, una fuerza constante por unidad de longitud) en la dirección $x$ para sostener la diferencia de tensiones, como en el sistema de la figura 9.2. Sin embargo, supondremos que el mecanismo que suministra esa fuerza, sea cual sea, no tiene masa, no tiene fricción y es infinitamente flexible.

*(Figura 11.5: una línea de fase constante en una onda plana que se acerca a un contorno.)*

Ahora, de nuevo, podemos considerar la reflexión de ondas viajeras. Supongamos que hay, en esta membrana, una onda plana de amplitud $A$ y número de onda $\vec{k}$ para $x < 0$, que viaja hacia el contorno en $x = 0$. La condición de que la onda viaje hacia el contorno puede escribirse en términos de las componentes de $\vec{k}$ como

$$k_x > 0. \tag{11.29}$$

Nos gustaría saber qué ondas produce esta onda incidente por reflexión y transmisión en el contorno $x = 0$. Por razones generales de invariancia bajo traslación espacial, esperamos que la solución tenga la forma

$$\psi(\vec{r}, t) = A\,e^{i(\vec{k}\cdot\vec{r} - \omega t)} + \sum_\alpha R_\alpha A\,e^{i(\vec{k}_\alpha\cdot\vec{r} - \omega t)} \quad \text{para } x \leq 0$$

$$\psi(\vec{r}, t) = \sum_\beta \tau_\beta A\,e^{i(\vec{k}_\beta\cdot\vec{r} - \omega t)} \quad \text{para } x \geq 0 \tag{11.30}$$

con

$$\vec{k}_\alpha^2 = \frac{\omega^2\rho_s}{T_s}, \qquad \vec{k}_\beta^2 = \frac{\omega^2\rho_s'}{T_s'} \tag{11.31}$$

y

$$k_{\alpha x} < 0 \quad \text{y} \quad k_{\beta x} > 0 \quad \text{para todo } \alpha \text{ y } \beta. \tag{11.32}$$

Los índices $\alpha$ y $\beta$ de (11.30) recorren todas las ondas transmitidas y reflejadas. Mostraremos en breve que solo una de cada contribuye para una condición de contorno plana en $x = 0$, pero (11.30) es completamente general y se sigue únicamente de la invariancia bajo traslación espacial. Nótese que hemos incluido las condiciones de contorno en $\pm\infty$ exigiendo (11.29) y (11.32). Salvo la onda incidente de amplitud $A$, todas las demás ondas se alejan del contorno. Pero todavía no hemos impuesto la condición de contorno en $x = 0$.

### 11.2.1 La ley de Snell: el contorno invariante bajo traslación

Por lo que sabemos de la física en $\pm\infty$, las ondas reflejada y transmitida podrían ser una superposición complicada de un número infinito de ondas planas que se alejan del contorno en distintas direcciones. De hecho, si el contorno tuviera una forma irregular, eso es exactamente lo que esperaríamos. Es el hecho de que el contorno, $x = 0$, sea él mismo invariante bajo traslaciones espaciales en la dirección $y$ lo que nos permite reducir el número infinito de parámetros de (11.30) a solo dos. Como las traslaciones en la dirección $y$ dejan invariante todo el sistema, incluido el contorno, podemos hallar soluciones en las que todas las componentes tengan la misma dependencia irreducible en $y$. Si la onda incidente es proporcional a

$$e^{ik_y y}, \tag{11.33}$$

entonces todas las componentes de (11.30) deben ser también proporcionales a $e^{ik_y y}$. De lo contrario, no hay manera de satisfacer la condición de contorno en $x = 0$ para todo $y$. Eso significa que

$$k_{\alpha y} = k_y, \qquad k_{\beta y} = k_y. \tag{11.34}$$

Pero (11.34), junto con (11.31) y (11.32), determina completamente los vectores de onda $\vec{k}_\alpha$ y $\vec{k}_\beta$. Entonces (11.30) se convierte en[^psi]

$$\psi(\vec{r}, t) = A\,e^{i\vec{k}\cdot\vec{r} - i\omega t} + R\,A\,e^{i\tilde{\vec{k}}\cdot\vec{r} - i\omega t} \equiv \psi_-(\vec{r}, t) \quad \text{para } x \leq 0$$

$$\psi(\vec{r}, t) = \tau\,A\,e^{i\vec{k}'\cdot\vec{r} - i\omega t} \equiv \psi_+(\vec{r}, t) \quad \text{para } x \geq 0 \tag{11.35}$$

donde

$$\tilde{k}_y = k_y, \qquad k'_y = k_y, \tag{11.36}$$

y

$$\tilde{k}_x = -\sqrt{\omega^2/v^2 - k_y^2} = -k_x, \qquad k'_x = \sqrt{\omega^2/v'^2 - k_y^2}, \tag{11.37}$$

con

$$v = \sqrt{\frac{T_s}{\rho_s}}, \qquad v' = \sqrt{\frac{T_s'}{\rho_s'}}.$$

[^psi]: Hemos definido aquí $\psi_\pm$ para facilitar la discusión de las condiciones de contorno, más abajo.

Lo entretenido de (11.35)-(11.37) es que sabemos todo sobre las direcciones de las ondas reflejada y transmitida sin haber mencionado siquiera los detalles de la física del contorno. Para obtener las direcciones solo hemos necesitado la invariancia bajo traslaciones en la dirección $y$. Los detalles de la física del contorno solo entran cuando queremos calcular $R$ y $\tau$. Las direcciones de las ondas reflejada y transmitida son las mismas para cualquier sistema con un contorno invariante bajo traslación. Evidentemente, este argumento funciona también en tres dimensiones. De hecho, si simplemente elegimos las coordenadas de modo que el contorno sea el plano $x = 0$ y la onda viaje en el plano $x$-$y$, entonces nada depende de la coordenada $z$ y el análisis es exactamente el mismo que arriba. Podemos, por ejemplo, aplicar estos argumentos directamente a las ondas electromagnéticas. Para las ondas electromagnéticas en un medio transparente, como la velocidad de fase es $v_\varphi = \omega/k$, el índice de refracción, $n$, es proporcional a $k$:

$$n = \frac{c}{v_\varphi} = \frac{ck}{\omega}. \tag{11.39}$$

(11.36)-(11.37) muestran que la onda reflejada sale con el mismo ángulo que la incidente, porque la única diferencia entre los vectores $\vec{k}$ de la onda incidente y la reflejada es un cambio de signo de la componente $x$. Así, el ángulo de incidencia es igual al ángulo de reflexión: es la regla de la «reflexión especular». De (11.36) podemos deducir también la ley de refracción de Snell para el ángulo de la onda refractada. Si $\theta$ es el ángulo que forma la onda incidente con la perpendicular al contorno, y $\theta'$ es el ángulo correspondiente de la onda transmitida, entonces (11.36) implica

$$k\sin\theta = k'\sin\theta'. \tag{11.40}$$

Para ondas electromagnéticas, podemos reescribir esto como

$$n\sin\theta = n'\sin\theta'. \tag{11.41}$$

Por ejemplo, cuando una onda electromagnética que viaja por el aire encuentra una superficie plana de vidrio con un ángulo $\theta$, se cumple $n' > n$ en (11.41): la onda se refracta acercándose a la perpendicular a la superficie. Esto se ilustra en la figura 11.6 para $n' > n$.

*(Figura 11.6: reflexión y transmisión en un contorno.)*

Terminemos ahora la solución del problema de la membrana resolviendo para $R$ y $\tau$ en (11.35). Para ello debemos discutir por fin las condiciones de contorno con más detalle. Una es que la membrana es continua, lo que, dada la forma (11.35), implica

$$\psi_-(\vec{r}, t)\big|_{x=0} = \psi_+(\vec{r}, t)\big|_{x=0}, \tag{11.42}$$

o sea,

$$1 + R = \tau. \tag{11.43}$$

La otra es que la fuerza vertical sobre cualquier trocito de la membrana es nula. La fuerza sobre un trocito de longitud $d\ell$ del contorno en el punto $(0, y, 0)$, ejercida por la membrana con $x < 0$, viene dada por

$$-T_s\,d\ell\left.\frac{\partial\psi_-(\vec{r}, t)}{\partial x}\right|_{x=0}. \tag{11.44}$$

Esto es análogo al ejemplo unidimensional ilustrado en la figura 8.6. La fuerza de tensión superficial es perpendicular al contorno, así que, para desplazamientos pequeños, solo importa la pendiente del desplazamiento en la dirección $x$. La pendiente en la dirección $y$ no contribuye a la fuerza vertical a primer orden en el desplazamiento. Análogamente, la fuerza sobre un trocito de longitud $d\ell$ del contorno en el punto $(0, y, 0)$, ejercida por la membrana con $x > 0$, viene dada por

$$T_s'\,d\ell\left.\frac{\partial\psi_+(\vec{r}, t)}{\partial x}\right|_{x=0}. \tag{11.45}$$

Así, la otra condición de contorno es

$$T_s'\left.\frac{\partial\psi_+(\vec{r}, t)}{\partial x}\right|_{x=0} = T_s\left.\frac{\partial\psi_-(\vec{r}, t)}{\partial x}\right|_{x=0}, \tag{11.46}$$

o sea,

$$T_s'\,k'_x\,\tau = T_s\,k_x\,(1 - R). \tag{11.47}$$

Así, la solución es

$$\tau = \frac{2}{1 + r}, \qquad R = \frac{1 - r}{1 + r} \tag{11.48}$$

donde

$$r = \frac{T_s'\,k'_x}{T_s\,k_x}. \tag{11.49}$$

De (11.48) y (11.49) puede verse que podemos ajustar la tensión superficial para que la onda reflejada desaparezca, incluso cuando hay un cambio en la longitud del vector $\vec{k}$ de un lado a otro del contorno. Conviene pensar en la refracción en este límite, porque permite visualizarla de forma sencilla. Si $r = 1$ en (11.48), entonces $R = 0$ y $\tau = 1$: no hay onda reflejada y la transmitida tiene la misma amplitud que la incidente. Así, en cada región hay una única onda plana. Recuerde que una onda plana consiste en líneas infinitas de fase constante perpendiculares al vector $\vec{k}$, que se mueven en la dirección de $\vec{k}$ con la velocidad de fase $v_\varphi = \omega/|\vec{k}|$. En particular, fijémonos en las líneas donde la fase es cero, de modo que $\psi = A$. La distancia perpendicular entre dos de esas líneas es la longitud de onda, $2\pi/|\vec{k}|$, porque la diferencia de fase entre líneas vecinas es $2\pi$. Pero he aquí la clave: las líneas de las dos regiones deben encontrarse en el contorno, $x = 0$, para satisfacer la condición de contorno (11.43). Si la amplitud de la onda incidente es 1 en $x = 0$, la de la onda saliente también es 1. Las líneas donde $\psi = A$ son continuas a través del contorno $x = 0$. Esta situación se ilustra en la figura 11.7, donde se muestran los vectores $\vec{k}$ de las dos regiones. Nótese que el ángulo de las líneas debe cambiar cuando cambia la distancia entre ellas, para mantener la continuidad en el contorno. En el programa 11-2 se muestra el mismo sistema en movimiento.

*(Figura 11.7: líneas de $\psi = 1$ constante para un sistema con refracción pero sin reflexión.)*

### 11.2.2 Prismas

El índice de refracción no trivial del vidrio es el ladrillo con que se construyen muchos elementos ópticos. Discutamos el prisma. En realidad, resolver del todo correctamente el problema de la dispersión de ondas luminosas por prismas requeriría técnicas mucho más sofisticadas de las que tenemos ahora a nuestra disposición. La razón es que el prisma no es una superficie plana e infinita con invariancia bajo traslación espacial; en general, tendríamos que preocuparnos del contorno. Sin embargo, podemos decir cosas interesantes incluso ignorando esta complicación. La idea es pensar no en una onda plana infinita, sino en un haz ancho de luz que incide sobre una cara del prisma. Un haz ancho se comporta de forma muy parecida a una onda plana, e ignoraremos la diferencia en este capítulo. Veremos cuáles son las diferencias en el capítulo 13, cuando discutamos la difracción.

Consideremos, pues, la siguiente situación, en la que un haz ancho de luz entra por una cara de un prisma de índice de refracción $n$ y sale por la otra. La geometría se muestra en la figura 11.8 (las direcciones de los haces se indican con las líneas gruesas). La cantidad interesante es $\delta$, que describe cuánto ha desviado el prisma la dirección del haz saliente respecto de la del incidente. Podemos calcularla con geometría sencilla y la ley de Snell, (11.40). De la ley de Snell,

$$\sin\theta_{in} = n\sin\theta_1, \qquad \sin\theta_{out} = n\sin\theta_2. \tag{11.50}$$

*(Figura 11.8: la geometría de un prisma.)*

Y ahora, algo de geometría:

$$\theta_2 + \theta_1 = \phi' \tag{11.52}$$

—porque el complemento de $\phi'$, es decir $\pi - \phi'$, junto con $\theta_1$ y $\theta_2$ son los ángulos de un triángulo y, por tanto, suman $\pi$—, y

$$\phi = \phi' \tag{11.53}$$

—porque $\phi$ y $\phi'$ son ángulos correspondientes de los dos triángulos rectángulos semejantes cuyo otro ángulo agudo es $\gamma$. Así,

$$\delta = \xi_1 + \xi_2 = \theta_{in} + \theta_{out} - \theta_1 - \theta_2 = \theta_{in} + \theta_{out} - \phi \tag{11.54}$$

donde hemos usado (11.52) y (11.53). Pero, para ángulos pequeños, de (11.50) y (11.51),

$$\theta_{in} \approx n\,\theta_1, \qquad \theta_{out} \approx n\,\theta_2. \tag{11.55}$$

Así,

$$\delta \approx n(\theta_1 + \theta_2) - \phi \approx (n - 1)\,\phi. \tag{11.56}$$

El resultado (11.56) es sin duda razonable. Debe anularse cuando $n \to 1$, porque para $n = 1$ no hay contorno. Y si las cosas son pequeñas y la respuesta es lineal, debe ser proporcional a $\phi$.

Una de las características más familiares de un prisma es consecuencia de la dependencia del índice de refracción, $n$, con la frecuencia. Eso hace que un haz de luz blanca se descomponga en colores. Para la mayoría de los materiales, el índice de refracción aumenta con la frecuencia, de modo que la luz azul se desvía más que la roja. La física de la dependencia de $n$ con la frecuencia es la de la oscilación forzada. El índice de refracción de un material está relacionado con la constante dieléctrica (véase (9.53)), que a su vez está relacionada con la distorsión de la estructura electrónica del material causada por el campo eléctrico. Para un campo variable, esto depende de la amplitud del movimiento de las cargas ligadas dentro del material en un campo eléctrico. Como esas cargas están ligadas, responden a los campos oscilantes de una onda electromagnética como una masa en un muelle sometida a una fuerza oscilante. Sabemos, de nuestro estudio de la oscilación forzada, que esa amplitud tiene la forma

$$\sum_{\text{resonancias }\alpha}\frac{C_\alpha}{\omega_\alpha^2 - \omega^2}, \tag{11.57}$$

donde $\omega_\alpha$ son las frecuencias de resonancia del sistema y las $C_\alpha$ son constantes que dependen de los detalles de cómo actúa la fuerza sobre los grados de libertad.

Podemos estimar el orden de magnitud de estas frecuencias de resonancia por análisis dimensional, recordando que cualquier material consta de electrones y núcleos unidos por fuerzas eléctricas (y por la mecánica cuántica, claro, aunque $\hbar$ no entrará en nuestra estimación salvo implícitamente, en la distancia atómica típica). Las cantidades relevantes son:[^electron]

| Magnitud | Valor |
|---|---|
| Carga del protón | $e \approx 1.6\times10^{-19}$ C |
| Masa del electrón | $m_e \approx 9.11\times10^{-31}$ kg |
| Distancia atómica típica | $a \approx 10^{-10}$ m = 1 Å |
| Velocidad de la luz | $c = 299\,792\,458$ m/s |

[^electron]: Nótese que es la masa del electrón, y no la del protón, la relevante, porque los electrones se mueven mucho más en los campos eléctricos.

En términos de estos parámetros, cabe suponer que la fuerza típica dentro de los materiales es del orden de $\dfrac{e^2}{4\pi\varepsilon_0 a^2}$ (por la ley de Coulomb) y, por tanto, que la constante del muelle es del orden de $\dfrac{e^2}{4\pi\varepsilon_0 a^3}$ (la fuerza típica dividida por la distancia típica). Así, esperamos

$$\omega_\alpha \approx \sqrt{\frac{e^2}{4\pi\varepsilon_0 a^3 m_e}} \tag{11.58}$$

y

$$\lambda_\alpha \approx \frac{2\pi c}{\omega_\alpha} \approx 2\pi c\sqrt{\frac{4\pi\varepsilon_0 a^3 m_e}{e^2}} \approx 10^{-7}\ \text{m} = 1000\ \text{Å}. \tag{11.59}$$

Esta es una longitud de onda en la región ultravioleta del espectro electromagnético, más corta que la de la luz visible. Eso significa que, para la luz visible, $\omega < \omega_\alpha$ y, por tanto, el desplazamiento (11.57) aumenta al aumentar $\omega$ dentro del visible. La distorsión de la estructura electrónica del material causada por un campo eléctrico variable aumenta con la frecuencia en el espectro visible. Así, la constante dieléctrica del material aumenta con la frecuencia y, en consecuencia, la luz azul se desvía más.

Dicho sea de paso, esta es la misma razón por la que el cielo es azul: la luz azul se dispersa más que la roja porque su frecuencia está más cerca de las resonancias importantes de las moléculas del aire.

### 11.2.3 Reflexión total interna

La situación en la que la onda viene de una región de $|\vec{k}|$ grande a una región de $|\vec{k}|$ menor tiene otra característica sorprendente y muy útil. Esta situación se representa en la figura 11.9 para un sistema sin reflexión. Para $\theta$ pequeña, como se muestra en la figura 11.9, esto se parece bastante a la figura 11.7, salvo que la onda se refracta alejándose de la perpendicular a la superficie en vez de acercarse a ella. Pero suponga que el ángulo $\theta$ es grande y satisface

$$n\sin\theta/n' > 1. \tag{11.60}$$

*(Figura 11.9: líneas de $\psi = 1$ constante para $n' < n$.)*

Entonces no hay solución con $\theta'$ real en (11.41). Así pues, no puede haber onda viajera transmitida: la onda incidente debe ser totalmente reflejada por el contorno. Esto es la reflexión total interna. Ocurre cuando una onda plana intenta escapar de una región de $|\vec{k}|$ alto a una región de $|\vec{k}|$ menor con un ángulo rasante. Se usa mucho en equipos ópticos y en muchas otras cosas. Investiguemos este curioso fenómeno con más detalle.

Suponga que partimos de $\theta = 0$ y aumentamos $\theta$. Al aumentar $\theta$, $k_y$ aumenta y $k_x$ disminuye. Esto continúa hasta llegar a la frontera de la reflexión total interna, llamada ángulo crítico,

$$\sin\theta = \sin\theta_c \equiv \frac{n'}{n}. \tag{11.61}$$

Las amplitudes de las ondas reflejada y transmitida de (11.48) también aumentan. En el ángulo crítico, $k'_x$ se anula: la amplitud de la onda reflejada es 1 y la de la transmitida es 2. Sin embargo, aunque la onda transmitida es no nula, no se lleva energía del contorno, porque el vector $\vec{k}$ apunta en la dirección $y$.

Al aumentar $\theta$ más allá del ángulo crítico, $k_y$ sigue creciendo. Para satisfacer la relación de dispersión,

$$\frac{\omega^2}{v'^2} = k_x'^2 + k_y^2, \tag{11.62}$$

¡$k'_x$ debe ser imaginario puro! La dependencia en $x$ es entonces proporcional a

$$e^{-\kappa x} \qquad \text{donde } \kappa = \operatorname{Im}k'_x. \tag{11.63}$$

Ahora cambia la naturaleza de la condición de contorno en el infinito. Ya no podemos exigir simplemente que $k'_x > 0$. En su lugar, debemos exigir

$$\operatorname{Im}k'_x > 0. \tag{11.64}$$

El signo es importante. Si $\operatorname{Im}k'_x$ fuera negativa, la amplitud de la onda para $x > 0$ crecería con $x$, yendo exponencialmente a infinito cuando $x \to \infty$. Eso no tiene mucho sentido físico, porque corresponde a una causa finita (la onda incidente para $x < 0$) produciendo un efecto infinito. Como veremos más abajo, también podemos llegar a esta conclusión tomando este sistema infinito como límite de un sistema finito.

En realidad tenemos tres condiciones de contorno distintas en el infinito para esta situación:

$$\operatorname{Re}k'_x > 0 \ \text{para } \theta < \theta_c, \qquad k'_x = 0 \ \text{para } \theta = \theta_c, \qquad \operatorname{Im}k'_x > 0 \ \text{para } \theta > \theta_c. \tag{11.66}$$

Estas tres pueden combinarse en una condición compuesta válida en todos los regímenes:

$$\operatorname{Re}k'_x \geq 0, \qquad \operatorname{Im}k'_x \geq 0. \tag{11.67}$$

La condición (11.67) es en realidad el enunciado más general de la condición de contorno de onda viajera saliente en el infinito. Es correcta también en situaciones en las que hay amortiguamiento y tanto la parte real como la imaginaria de $k'_x$ son no nulas. Es el enunciado matemático del hecho físico de que la onda para $x > 0$, sea cual sea su forma, la produce en el contorno la onda incidente.

De (11.48) y (11.49) se ve que, para $\theta > \theta_c$, la amplitud de la onda reflejada se vuelve compleja. Sin embargo, su valor absoluto sigue siendo 1: toda la energía de la onda incidente se refleja.

Hemos visto que, en la reflexión total interna, la onda sí penetra en la región prohibida, pero la dependencia en $x$ tiene la forma de una onda estacionaria exponencial, no de una onda viajera. La dependencia en $y$ es la de una onda viajera. Esta es una de las muchas situaciones en las que la física obliga a que la solución bidimensional o tridimensional tenga propiedades distintas en direcciones distintas.

Es fácil ver la reflexión total interna en un acuario, un bloque de vidrio u otro objeto transparente rectangular con índice de refracción bastante mayor que 1. Puede mirar a través de una cara del rectángulo y ver el reflejo plateado desde una cara adyacente, como se ilustra en la figura 11.10.

*(Figura 11.10: reflexión total interna en vidrio de índice de refracción 2.)*

### 11.2.4 Efecto túnel

Considere la dispersión de una onda plana en el sistema ilustrado en la figura 11.11. Es el mismo montaje que en la figura 11.10, salvo que se ha añadido otro bloque de vidrio a una distancia pequeña, $d$, por debajo del contorno en el que había reflexión total interna. Hemos definido la dirección $x$ positiva hacia abajo por coherencia con la discusión de la ley de Snell de más arriba. ¿Llega ahora algo de luz al observador de abajo, o la luz sigue reflejándose totalmente en el contorno, como en la figura 11.10? La respuesta es que algo de luz pasa. Como veremos en detalle en un ejemplo más abajo, la presencia del otro bloque de vidrio significa que, en vez de una condición de contorno en el infinito, tenemos una condición de contorno a la distancia finita $d$.

*(Figura 11.11: un experimento sencillo para demostrar el efecto túnel.)*

Los detalles de este fenómeno para ondas electromagnéticas se complican algo por la polarización, que discutiremos en detalle en el capítulo siguiente. Sin embargo, hay un proceso precisamente análogo en la oscilación transversal de membranas que podemos analizar con facilidad. De hecho, veremos que ya lo hemos analizado en el capítulo 9.

Considere el problema de dispersión ilustrado en la figura 11.12. La región sin sombrear es una membrana de densidad menor. Las flechas indican las direcciones de los vectores $\vec{k}$ de las ondas planas. Las regiones sombreadas tienen densidad superficial de masa $\rho_s$ y tensión superficial $T_s$. La región sin sombrear, que va de $x = 0$ a $x = d$, tiene la misma tensión superficial pero densidad superficial de masa $\rho_s/4$. Así, la razón entre las velocidades de fase de las dos regiones es dos, la misma que la razón entre el aire y el vidrio en la figura 11.11. Las líneas discontinuas son contornos sin masa entre las distintas membranas.

*(Figura 11.12: efecto túnel en una membrana infinita.)*

Podemos preguntarnos ahora cuáles son los coeficientes $R$ y $\tau$ de reflexión y transmisión. Hemos hecho este problema para un solo contorno antes en este capítulo, en (11.42)-(11.49). Podríamos resolver este juntando dos de esas soluciones con las técnicas de matriz de transferencia del capítulo 9. De hecho, ni siquiera tenemos que hacer eso, porque podemos leer el resultado de (9.97) y (9.98), en la discusión de las películas delgadas del capítulo 9. La cuestión es que todos los términos de nuestra solución deben tener la misma dependencia irreducible en $y$, $e^{ik_y y}$, por la invariancia bajo traslación espacial de todo el sistema, incluido el contorno, en la dirección $y$. Ese factor común no juega ningún papel en las condiciones de contorno. Si lo sacamos factor común, lo que queda parece un problema de dispersión unidimensional. Comparando (11.47) para $T_s = T_s'$ con (9.10), se ve que los análisis coinciden si hacemos los reemplazos

$$k_1 \to k_x, \qquad k_2 \to k'_x, \qquad L \to d \tag{11.68}$$

donde $k_x$ es la componente $x$ del vector $\vec{k}$ de la onda incidente en la región sombreada y $k'_x$ es la componente $x$ del vector $\vec{k}$ de la onda transmitida en la región sin sombrear. El resultado es

$$\tau = \left(\cos k'_x d - i\,\frac{k_x^2 + k_x'^2}{2k_x k'_x}\sin k'_x d\right)^{-1}e^{-ik_x d} \tag{11.69}$$

y

$$R = \left(i\,\frac{k_x'^2 - k_x^2}{2k_x k'_x}\sin k'_x d\right)\left(\cos k'_x d - i\,\frac{k_x^2 + k_x'^2}{2k_x k'_x}\sin k'_x d\right)^{-1}. \tag{11.70}$$

Puede ser un poco más fácil mirar la intensidad de la onda transmitida, que es proporcional a

$$|\tau|^2 = \frac{4k_x^2 k_x'^2}{\left(k_x^4 + k_x'^4\right)\sin^2 k'_x d + 2k_x^2 k_x'^2}. \tag{11.71}$$

Nótese que no hemos mencionado el ángulo crítico, ni la reflexión total interna, ni nada por el estilo. La razón es que nuestro análisis del capítulo 9 era perfectamente general. Sigue siendo correcto incluso si el número de onda angular de la región intermedia se vuelve imaginario. Todo lo que ocurre para $\theta$ mayor que el ángulo crítico, $\theta_c$, es que $k'_x$ se vuelve imaginario. Pero eso tiene un efecto espectacular en (11.71). Si $k'_x \to i\kappa$, con $\kappa$ real, se sigue de la identidad de Euler, (1.57) y (1.62), que

$$\sin k'_x d \to i\sinh\kappa d, \tag{11.72}$$

donde $\sinh$ es el «seno hiperbólico», definido por

$$\sinh x \equiv \frac{e^x - e^{-x}}{2}. \tag{11.73}$$

Así, para ángulos por encima del crítico, el denominador de (11.71) es una función exponencialmente creciente de $d$ (el término $e^{\kappa d}$ de (11.73) domina para $\kappa d$ grande). La intensidad de la onda transmitida decrece, por tanto, exponencialmente con $d$. En el límite de $d$ grande recuperamos rápidamente la reflexión total interna.

Podemos entender algo mejor lo que ocurre mirando las condiciones de contorno en $x = d$ para ángulos por encima del crítico. Para $x > d$, la onda tiene la forma (suprimiendo los factores comunes $e^{ik_y y}$ y $A e^{-i\omega t}$)

$$\tau\,e^{ik_x x}. \tag{11.74}$$

Para $0 \leq x \leq d$, la onda tiene la forma

$$T_{II}\,e^{-\kappa x} + R_{II}\,e^{\kappa x}, \tag{11.75}$$

donde he llamado a los coeficientes $T_{II}$ y $R_{II}$ por analogía con las ondas transmitida y reflejada, aunque no son ondas viajeras. Las condiciones de contorno en $x = d$ son

$$\tau\,e^{ik_x d} = T_{II}\,e^{-\kappa d} + R_{II}\,e^{\kappa d}, \qquad ik_x\,\tau\,e^{ik_x d} = \kappa\left(-T_{II}\,e^{-\kappa d} + R_{II}\,e^{\kappa d}\right). \tag{11.76}$$

Esto parece más complicado de lo que es. Si despejamos $T_{II}e^{-\kappa d}$ y $R_{II}e^{\kappa d}$ en términos de $\tau e^{ik_x d}$, el resultado es

$$T_{II}\,e^{-\kappa d} = \frac{\kappa - ik_x}{2\kappa}\,\tau\,e^{ik_x d}, \qquad R_{II}\,e^{\kappa d} = \frac{\kappa + ik_x}{2\kappa}\,\tau\,e^{ik_x d}.$$

Lo importante es que los valores de las dos componentes de la onda (11.75) en $x = d$, es decir, $T_{II}e^{-\kappa d}$ y $R_{II}e^{\kappa d}$, son más o menos del mismo tamaño. Estas dos cantidades no tienen ninguna dependencia exponencial en $d$. Este hecho cualitativo no depende de los detalles de (11.76): será cierto para cualquier condición de contorno razonable en $x = d$.

Así pues, el coeficiente $R_{II}$ de la onda «reflejada» (entre comillas, porque es una onda exponencial real, no una onda viajera) debe ser menor que la «transmitida» en un factor de aproximadamente $e^{2\kappa d}$. Nótese que esto justifica el enunciado (11.67) de la condición de contorno en el infinito. Cuando $d \to \infty$, para cualquier física razonable en $d$, la onda se convierte en una exponencial negativa pura.

En $x = 0$, para $\kappa d$ grande, el término $R_{II}$ de la onda será completamente despreciable, y el término $T_{II}$ se producirá con algún coeficiente del orden de 1, igual que en el límite de reflexión total interna.

Así, lo que ocurre en las condiciones de contorno del efecto túnel puede describirse cualitativamente así: la onda incidente para $x < 0$ produce el término $e^{-\kappa x}$ en la región $0 \leq x \leq d$, con una mezcla exponencialmente pequeña de $e^{\kappa x}$. Pero en $x = d$ las dos partes de la onda exponencial son del mismo tamaño (ambas exponencialmente pequeñas), y pueden producir la onda transmitida.

La rápida dependencia exponencial de la onda transmitida con $d$ tiene consecuencias interesantes. Implica, por ejemplo, que la onda reflejada es también muy sensible al valor de $d$ para $d$ pequeña (la conservación de la energía implica $|R|^2 + |\tau|^2 = 1$). Puede ver esta rápida dependencia en el ejemplo de la figura 11.10 poniendo el dedo sobre la superficie inferior del bloque de vidrio o del acuario, donde la onda se está reflejando. ¡Verá una huella dactilar fantasmal! La razón es que las minúsculas hendiduras de su dedo están lo bastante lejos del vidrio como para que $\kappa d$ sea grande y la onda se refleje casi por completo. Pero donde la carne se aprieta firmemente contra el vidrio, la onda se absorbe. Es una versión sencilla de un microscopio de efecto túnel.

Por último, antes de dejar el tema del efecto túnel, consideremos qué ocurre cuando bajamos la intensidad de la onda luminosa de la figura 11.11 hasta ver la dispersión de fotones individuales. Lo primero que hay que notar es que cada fotón o bien se transmite o bien se refleja. El significado de $R$ y $\tau$ en este caso es que $|R|^2$ y $|\tau|^2$ son las probabilidades de reflexión y transmisión. No se puede predecir si un fotón concreto pasará. En el mundo mecanocuántico solo se pueden predecir probabilidades.

Lo segundo que hay que notar es que, en la descripción de partículas, todo el fenómeno del efecto túnel es muy peculiar. Un fotón clásico que llegara al contorno de la placa de vidrio con más del ángulo crítico no podría entrar en absoluto en el aire: se lo impedirían la conservación de la energía y la conservación de la componente $y$ del momento.[^momento] ¿Cómo puede la partícula llegar al lado $x > d$ si no puede existir para $0 < x < d$? Evidentemente, en física clásica no puede. El efecto túnel es, por tanto, un fenómeno genuinamente mecanocuántico. La onda consigue penetrar en la región prohibida, pero solo en forma de onda exponencial real, no de onda viajera. Solo para $x < 0$ y $x > d$, donde las ondas son viajeras, pueden interpretarse como partículas en algo parecido al sentido clásico.

[^momento]: El contorno no cambia $p_y$ del fotón, por la invariancia bajo traslación en la dirección $y$. Sin embargo, no hay ninguna razón por la que el contorno no pueda ejercer una fuerza en la dirección $x$ y cambiar $p_x$ del fotón.

## 11.3 Placas de Chladni

Las placas de Chladni son un ejemplo muy bonito e instructivo de sistema oscilante bidimensional. Una placa de Chladni no es más que una placa metálica cuadrada que se excita transversalmente en su centro. Se ilustra en la figura 11.13. El punto del centro muestra dónde se excita la placa en la dirección transversal (fuera del plano del papel). El centro, cuya posición de equilibrio tomaremos como $\vec{r} = 0$, se mueve arriba y abajo fuera del plano del papel con frecuencia $\omega$. Supongamos que el cuadrado está en el plano $x$-$y$ y tiene lado $2L$, y llamemos al desplazamiento transversal (en la dirección $z$)

$$\psi(x, y, t) \qquad \text{para } |x|, |y| \leq L. \tag{11.78}$$

*(Figura 11.13: una placa de Chladni.)*

En principio, este es un problema de oscilación forzada. Podríamos tomar como condición de contorno en el origen

$$\psi(0, 0, t) = A\cos\omega t \tag{11.79}$$

e intentar hallar $\psi$ en todas partes.

Para hallar $\psi$ debemos conocer la condición de contorno en los bordes de la placa. Eso depende de los detalles de la física de la placa, porque hay varias maneras en que la placa puede deformarse en respuesta a la fuerza impulsora. Por simplicidad, supondremos que la deformación dominante es la cizalla, ilustrada en la figura 11.14. Para este tipo de desplazamiento, y para evitar una aceleración infinita, la pendiente de la placa debe anularse en el contorno en la dirección perpendicular al contorno, o sea, en lenguaje matemático,

$$\hat{n}\cdot\vec{\nabla}\psi = 0 \tag{11.80}$$

en el borde, donde $\hat{n}$ es un vector unitario en el plano perpendicular al borde. En este caso,

$$\left.\frac{\partial}{\partial x}\psi(x, y, t)\right|_{x=|L|} = \left.\frac{\partial}{\partial y}\psi(x, y, t)\right|_{y=|L|} = 0. \tag{11.81}$$

*(Figura 11.14: cizalla.)*

Aunque el caso general es más complicado que esto, usaremos (11.81) como ilustración. Lo instructivo de las placas de Chladni, como veremos, no es lo que ocurre en los bordes, ¡sino lo que ocurre en el medio!

No es fácil escribir la solución general de este problema de oscilación forzada. Sin embargo, nos interesan sobre todo las resonancias. Son los modos de oscilación libre de la placa (sujetos a la condición de contorno (11.81)) que pueden ser excitados por la fuerza impulsora, es decir, los modos que tienen valores no nulos del desplazamiento en el origen.

Los modos de oscilación libre relevantes de la placa tienen la forma[^senos]

$$\psi_{(n_x, n_y)}(x, y, t) = A\cos\frac{n_x\pi x}{L}\cos\frac{n_y\pi y}{L}\cos\omega t \tag{11.82}$$

con

$$\omega^2 = \omega_0^2(\vec{k}^2) \implies \omega^2 = f(n_x^2 + n_y^2). \tag{11.83}$$

[^senos]: Hay también modos proporcionales a $\sin\left((n_x + 1/2)\pi x/L\right)$ y/o $\sin\left((n_y + 1/2)\pi y/L\right)$, pero se anulan en el origen y no son excitados por la fuerza impulsora.

Si las frecuencias de estos modos fueran únicas, (11.82) sería toda la historia. Pero lo interesante de este sistema es que la simetría garantiza que hay degeneración: si $n_x \neq n_y$, hay dos modos con la misma frecuencia. Obtenemos un modo físicamente equivalente intercambiando $n_x \leftrightarrow n_y$, porque eso corresponde simplemente a una rotación de 90° de la placa, ¡que no cambia la física en absoluto! Cuando hay modos degenerados, las combinaciones lineales de ellos son también modos, como se muestra en (3.117). Así que tenemos que preguntarnos qué combinaciones lineales excita la fuerza impulsora. Otra forma de decir esto se resume en (11.83): la invariancia bajo rotaciones asegura que $\omega^2$ depende solo de $n_x^2 + n_y^2$. En particular, está claro que la diferencia

$$\psi^-_{(n_x, n_y)}(x, y, t) = A\left(\cos\frac{n_x\pi x}{L}\cos\frac{n_y\pi y}{L} - \cos\frac{n_y\pi x}{L}\cos\frac{n_x\pi y}{L}\right)\cos\omega t \tag{11.84}$$

se anula en el origen. ¡Solo la suma se acopla a la fuerza impulsora!

$$\psi^+_{(n_x, n_y)}(x, y, t) = A\left(\cos\frac{n_x\pi x}{L}\cos\frac{n_y\pi y}{L} + \cos\frac{n_y\pi x}{L}\cos\frac{n_x\pi y}{L}\right)\cos\omega t \tag{11.85}$$

Estos son los modos resonantes de una placa de Chladni.

Una razón por la que esto resulta divertido es que es fácil de ver. Si se excita la placa y se espolvorea arena sobre ella, la arena se acumula en las regiones donde la placa no se mueve, a lo largo de los nodos de desplazamiento donde $\psi = 0$. Así obtenemos una imagen visual de los ceros de $\psi$.

Miremos algunos de estos modos (en orden de frecuencia creciente) para ver qué esperar. El modo $\psi^+_{(0,0)}$ no es interesante: corresponde a toda la placa subiendo y bajando en bloque. Obviamente, la frecuencia correspondiente es 0, porque no hay fuerza restauradora.

El primer modo interesante es

$$\psi^+_{(1,0)}(x, y, t) = A\left(\cos\frac{\pi x}{L} + \cos\frac{\pi y}{L}\right)\cos\omega t.$$

Este se anula para $y = \pm L \pm x$, de modo que el patrón de arena de Chladni tiene el aspecto del diagrama de la figura 11.15.

*(Figura 11.15: el patrón de Chladni del modo $(n_x, n_y) = (1, 0)$.)*

El modo siguiente es

$$\psi^+_{(1,1)}(x, y, t) = 2A\cos\frac{\pi x}{L}\cos\frac{\pi y}{L}\cos\omega t.$$

Como este modo no es degenerado, no da lugar a un patrón muy interesante. Se anula en $x = \pm L/2$ e $y = \pm L/2$, lo que da el patrón mostrado en la figura 11.16. No consideraremos más de estos modos aburridos con $n_x = n_y$.

*(Figura 11.16: el patrón de Chladni del modo (1,1).)*

El siguiente modo es

$$\psi^+_{(2,0)}(x, y, t) = A\left(\cos\frac{2\pi x}{L} + \cos\frac{2\pi y}{L}\right)\cos\omega t,$$

que se anula para $y = \pm L/2 \pm x$ o $y = \pm 3L/2 \pm x$, de modo que el patrón tiene el aspecto de la figura 11.17.

*(Figura 11.17: el patrón de Chladni del modo (2,0).)*

A continuación viene

$$\psi^+_{(2,1)}(x, y, t) = A\left(\cos\frac{\pi x}{L}\cos\frac{2\pi y}{L} + \cos\frac{2\pi x}{L}\cos\frac{\pi y}{L}\right)\cos\omega t.$$

Este se anula para

$$c_x(2c_y^2 - 1) + c_y(2c_x^2 - 1) = (c_x + c_y)(2c_xc_y - 1) = 0$$

con $c_x \equiv \cos(\pi x/L)$ y $c_y \equiv \cos(\pi y/L)$. El patrón se muestra en la figura 11.18.

*(Figura 11.18: el patrón de Chladni del modo (2,1).)*

Podríamos seguir, pero a estas alturas ya debería tener la idea. Veamos un último modo:

$$\psi^+_{(3,1)}(x, y, t) = A\left(\cos\frac{\pi x}{L}\cos\frac{3\pi y}{L} + \cos\frac{3\pi x}{L}\cos\frac{\pi y}{L}\right)\cos\omega t,$$

que se anula para

$$c_x(4c_y^3 - 3c_y) + c_y(4c_x^3 - 3c_x) = c_xc_y(4c_x^2 + 4c_y^2 - 6) = 0$$

con el patrón mostrado en la figura 11.19.

*(Figura 11.19: el patrón de Chladni del modo (3,1).)*

**Moraleja:** cuando hay más de un modo con la misma frecuencia, ¡mire las combinaciones lineales para determinar cuáles se excitan!

## 11.4 Guías de onda

En general, una «guía de ondas» es un dispositivo que obliga a una onda viajera a propagarse solo por donde uno quiere. Típicamente, una guía de ondas es algún tipo de tubo que permite a la perturbación ondulatoria propagarse en una dirección mientras la confina en las otras. En esta sección discutiremos el caso de guías de onda rectas con secciones transversales uniformes sencillas. La física realmente interesante ocurre cuando la anchura de la guía no es mucho mayor que la longitud de onda. Entonces, como veremos, la física de la guía tiene un efecto espectacular sobre la propagación de la onda.

La situación más sencilla de discutir es la de las oscilaciones transversales de una membrana en forma de banda infinita, como se muestra en la figura 11.20. Considere una membrana con densidad superficial de masa $\rho_s$ y tensión superficial $T_s$, tensada en una banda infinita en el plano $x$-$y$ entre $y = 0$ e $y = \ell$, y desde $x = -\infty$ hasta $\infty$. Los bordes, en $y = 0$ e $y = \ell$, se mantienen fijos en el plano. Nos interesan las oscilaciones del interior de la banda hacia arriba y hacia abajo, fuera del plano.

*(Figura 11.20: una sección de una banda infinita de membrana tensada que actúa como guía de ondas.)*

Este es un trabajo para la separación de variables. Podemos buscar modos de este sistema que sean productos de una función de $x$ por una función de $y$. En particular, podemos satisfacer la condición de contorno en $y = 0$ combinando dos modos del sistema infinito,

$$e^{ik_x x}e^{ik_y y} \quad \text{y} \quad e^{ik_x x}e^{-ik_y y}, \tag{11.96}$$

para formar

$$\sin(k_y y)\,e^{ik_x x}. \tag{11.97}$$

Esto satisface la condición de contorno en $y = \ell$ si

$$k_y = \frac{n\pi}{\ell} \qquad \text{para } n = 1\text{ a }\infty. \tag{11.98}$$

Así, los modos tienen este aspecto:

$$\psi_n^+(x, y, t) = A\sin\frac{n\pi y}{\ell}\,e^{i(k_x x - \omega t)} \tag{11.99}$$

y

$$\psi_n^-(x, y, t) = A\sin\frac{n\pi y}{\ell}\,e^{i(-k_x x - \omega t)}. \tag{11.100}$$

Para cada valor de $n$, ¡estos parecen ondas que viajan en la dirección $\pm x$!

La relación de dispersión de la membrana viene dada por (11.18). Pero los modos $\psi_n^\pm$ tienen $|k_y| = n\pi/\ell$. Así, la relación de dispersión de las ondas viajeras (11.99) y (11.100) es

$$\omega^2 = v^2 k_x^2 + \omega_n^2, \tag{11.101}$$

donde

$$v = \sqrt{\frac{T_s}{\rho_s}} \tag{11.102}$$

y

$$\omega_n = \frac{n\pi v}{\ell}. \tag{11.103}$$

Algo interesante de (11.101) es que la relación de dispersión tiene una frecuencia de corte inferior que depende de $n$. Para un $\omega$ dado, los únicos modos que se propagan realmente son el número finito de modos con

$$n < \frac{\omega\ell}{\pi v}. \tag{11.104}$$

Por ejemplo, para $\omega \leq \pi v/\ell$ no hay ondas viajeras. Para $\pi v/\ell < \omega \leq 2\pi v/\ell$ solo hay una, la correspondiente a $n = 1$, etc.

Los modos que satisfacen (11.104) tienen una interpretación física sencilla. Pueden pensarse como las ondas planas (11.96) del sistema infinito rebotando de un lado a otro entre los bordes fijos, $y = 0$ e $y = \ell$. El requisito (11.98) sobre los valores permitidos de $k_y$ surge porque, para otros valores de $k_y$, las ondas reflejadas se desfasan y dan interferencia destructiva. Cabría esperar que una onda en zigzag de este tipo se propagara en la dirección $x$ con una velocidad menor que la velocidad de fase, $v$, de las ondas del sistema infinito, en un factor de

$$\frac{k_x}{\sqrt{k_x^2 + k_y^2}} = \frac{k_x}{\sqrt{k_x^2 + (\omega_n/v)^2}}, \tag{11.105}$$

porque tiene que recorrer esa distancia de más al rebotar para avanzar una distancia dada en $x$, como se ilustra en la figura 11.21. De hecho, la velocidad de fase de las ondas en zigzag para $n$ fijo, $\omega/k_x$, es en realidad **mayor** que $v$ por el factor (11.105), en vez de menor:

$$v_{n\varphi} = \frac{\omega}{k_x} = v\,\frac{\sqrt{k_x^2 + (\omega_n/v)^2}}{k_x}. \tag{11.106}$$

*(Figura 11.21: una onda en zigzag en la guía de ondas.)*

Sin embargo, la velocidad de grupo, $\partial\omega/\partial k_x$, de las ondas en zigzag —la velocidad a la que realmente se pueden enviar señales— es menor justamente por el factor esperado:

$$v_{gn} = \frac{\partial\omega}{\partial k_x} = v\,\frac{k_x}{\sqrt{k_x^2 + (\omega_n/v)^2}}. \tag{11.107}$$

Para ondas luminosas podemos hacer una guía de ondas construyendo un tubo de algún material conductor, de modo que el campo eléctrico sea no nulo solo dentro del tubo. Sin embargo, en ese caso los detalles de las condiciones de contorno en los bordes dependen de la dirección del campo eléctrico. Volveremos a una cuestión relacionada en el capítulo siguiente.

## 11.5 Agua

El agua es una sustancia bastante complicada. Moja las cosas. Tiene viscosidad. Forma remolinos y torbellinos y tiene movimientos turbulentos no lineales que no podemos aspirar a entender con las técnicas de que disponemos. En esta sección consideramos un fluido algo idealizado, que llamaremos «agua seca» (siguiendo a Feynman), que no tiene nada de esa estructura complicada. Tiene tres características que mantendremos en común con la de verdad: tiene densidad de masa, tiene tensión superficial y es casi incompresible. Veamos cómo ondula.

Imagine un universo infinito lleno de un líquido incompresible y sin fricción. Esto nos permitirá ver las consecuencias de la incompresibilidad de forma sencilla y cualitativa. Considere el análogo de una onda sonora plana en un sistema así. Es decir, por ejemplo, una onda plana que viaja en la dirección $x$ (con $k_y = k_z = 0$) con desplazamientos longitudinales en la dirección $x$. Si el líquido es verdaderamente incompresible, $k_x$ debe ser cero para esta onda, porque cualquier desplazamiento longitudinal debe ir acompañado de compresiones y enrarecimientos del medio. Así, para una onda plana así, $\vec{k} = 0$: ¡no hay ondas planas no triviales en el sistema infinito!

En general, no esperamos que todas las componentes del vector $\vec{k}$ tengan que anularse, porque incluso en un líquido incompresible el desplazamiento en una dirección está permitido si va acompañado del movimiento adecuado en otras direcciones. Pero lo que hemos visto es que no podemos tener un modo con un vector $\vec{k}$ real. Eso sería una onda plana, que hemos visto que no es compatible con la incompresibilidad. En su lugar, esperamos que la restricción $k_x = 0$ se sustituya por una restricción sobre la longitud, invariante bajo rotaciones, del vector $k$: que $\vec{k}\cdot\vec{k} = 0$. Si algunas de las componentes del vector $\vec{k}$ son imaginarias, esto puede satisfacerse con $\vec{k}$ no nulo.

Nótese que la condición $\vec{k}\cdot\vec{k} = 0$ no es exactamente una relación de dispersión, porque no hace referencia alguna a la frecuencia. Pero es toda la historia para un sistema infinito de fluido incompresible. De hecho, está claro que no hay ondas armónicas en el sistema infinito, porque no hay nada que produzca una fuerza restauradora. Incluso si hay un campo gravitatorio, la presión del líquido se ajusta para cancelar el efecto de la gravedad. Solo podemos obtener una relación de dispersión no trivial cuando hay una superficie. La relación de dispersión depende entonces de la física de la superficie. Esto parecería violar nuestro principio general de que la relación de dispersión es una propiedad del sistema infinito. Lo que ocurre es esto: la relación $\vec{k}\cdot\vec{k} = 0$ es realmente la única relación de dispersión que tiene algún sentido para el sistema infinito tridimensional. Cuando introducimos una superficie, hemos roto la invariancia bajo traslación en la dirección normal a la superficie. Eso nos permite obtener una relación de dispersión no trivial para el sistema bidimensional paralelo a la superficie.

### 11.5.1 Matemáticas de las ondas en el agua

Intentemos ahora hacer cuantitativas estas consideraciones. Como de costumbre, etiquetaremos nuestro fluido por las posiciones de equilibrio de sus partes. Llamemos entonces al desplazamiento respecto del equilibrio del fluido que está en el punto $\vec{r}$ en equilibrio

$$\varepsilon\,\vec{\psi}(\vec{r}, t)$$

para algún $\varepsilon$ pequeño. Esto significa que la posición real del agua es[^epsilon]

$$\vec{R}(\vec{r}, t) = \vec{r} + \varepsilon\,\vec{\psi}(\vec{r}, t). \tag{11.109}$$

[^epsilon]: Aquí podemos tomar $\psi$ adimensional y dejar que el parámetro $\varepsilon$ sea un desplazamiento pequeño.

Podemos considerar (11.109) como una especie de cambio de coordenadas. Nos lleva de las coordenadas de equilibrio (una etiqueta más bien arbitraria, porque el agua es libre de fluir) a las coordenadas físicas, que nos dicen dónde está realmente el agua. Si el agua es incompresible, lo cual es una aproximación bastante buena, un elemento de volumen pequeño debe tener el mismo volumen en equilibrio y en las coordenadas físicas:

$$dR_x\,dR_y\,dR_z = dx\,dy\,dz. \tag{11.110}$$

Esto se cumplirá si el determinante de la matriz jacobiana vale 1:

$$\det\begin{pmatrix} \frac{\partial R_x}{\partial x} & \frac{\partial R_x}{\partial y} & \frac{\partial R_x}{\partial z} \\ \frac{\partial R_y}{\partial x} & \frac{\partial R_y}{\partial y} & \frac{\partial R_y}{\partial z} \\ \frac{\partial R_z}{\partial x} & \frac{\partial R_z}{\partial y} & \frac{\partial R_z}{\partial z} \end{pmatrix} = 1. \tag{11.111}$$

Como $\varepsilon$ es pequeño, podemos desarrollar (11.111) a orden más bajo en $\varepsilon$, con el resultado

$$1 + \varepsilon\,\vec{\nabla}\cdot\vec{\psi} + O(\varepsilon^2) = 1. \tag{11.112}$$

Así,

$$\vec{\nabla}\cdot\vec{\psi} = 0. \tag{11.113}$$

(11.113) es muy razonable: es el enunciado de que el flujo de desplazamiento hacia dentro o hacia fuera de cualquier región se anula.[^nolineal] Esto es lo que esperábamos de nuestra discusión cualitativa.

[^nolineal]: Nótese, sin embargo, que para $\varepsilon$ grande la incompresibilidad es la restricción no lineal (11.111).

Para ver qué significa esto para las ondas, supongamos además que no hay remolinos. El enunciado matemático de esto es

$$\vec{\nabla}\times\vec{\psi} = 0. \tag{11.114}$$

Si no suponemos (11.114), la conservación del momento angular se vuelve importante y la vida se complica muchísimo. Tendrá que esperar a cursos de dinámica de fluidos para aprender más sobre ello. Con la simplificación (11.114), el desplazamiento puede escribirse como el gradiente de una función escalar, $\chi$:

$$\varepsilon\,\vec{\psi} = \vec{\nabla}\chi. \tag{11.115}$$

Esto simplifica enormemente la vida, porque ahora podemos trabajar con la cantidad escalar $\chi$. La invariancia bajo traslación espacial nos dice que podemos hallar modos de la forma

$$\chi = e^{i\vec{k}\cdot\vec{r} - i\omega t}, \tag{11.116}$$

lo que da un desplazamiento de la forma

$$\varepsilon\,\vec{\psi} = i\,\vec{k}\,e^{i\vec{k}\cdot\vec{r} - i\omega t}. \tag{11.117}$$

La condición (11.113) se convierte entonces en

$$\vec{k}\cdot\vec{k} = 0, \tag{11.118}$$

como anticipamos en la discusión cualitativa del principio de la sección.

### 11.5.2 Profundidad

Consideremos ahora ondas en un «océano» de profundidad $L$, ignorando las fuerzas de fricción, los remolinos y las no linealidades. Restringiremos además nuestra atención a una situación bidimensional. Sea $y$ la dirección vertical y consideremos ondas en el agua en la dirección $x$. Es decir, tomaremos $k_x$ real, porque nos interesa la propagación de ondas en la dirección $x$, y $k_y$ imaginario puro con la misma magnitud, de modo que se satisfaga (11.118). Suponemos entonces que nada depende de la otra coordenada, $z$. Habiendo simplificado tanto las cosas, podemos suponer también que nuestro océano es una caja rectangular. Entonces los modos de interés del sistema infinito tienen el aspecto

$$\chi_\infty(x, y, t) = e^{\pm ikx \pm ky - i\omega t}. \tag{11.119}$$

Si el océano tiene un fondo en $y = 0$, entonces el desplazamiento vertical debe anularse en $y = 0$. Entonces (11.115) implica que debemos combinar modos del sistema infinito para obtener una $\chi$ cuya derivada respecto de $y$ se anule en $y = 0$:

$$\chi(x, y, t) \propto e^{\pm ikx - i\omega t}\cosh ky, \tag{11.120}$$

donde $\cosh$ es el «coseno hiperbólico», definido por

$$\cosh x \equiv \frac{e^x + e^{-x}}{2}. \tag{11.121}$$

Entonces, de (11.115), obtenemos

$$\psi_x(x, y, t) = \frac{\partial}{\partial x}\chi(x, y, t) = \pm i\,e^{\pm ikx - i\omega t}\cosh ky,$$

$$\psi_y(x, y, t) = \frac{\partial}{\partial y}\chi(x, y, t) = e^{\pm ikx - i\omega t}\sinh ky. \tag{11.122}$$

Antes de seguir, nótese que podríamos extender estas consideraciones añadiendo una coordenada $z$. Entonces (11.120) se convertiría en

$$\chi(x, y, z, t) \propto e^{(\pm ik_x x \pm ik_z z) - i\omega t}\cosh ky$$

donde

$$k = \sqrt{k_x^2 + k_z^2}.$$

Estos son los modos ondulatorios bidimensionales del océano infinito de profundidad $L$. La dependencia en $y$ queda completamente fijada por la condición de contorno en el fondo y por la condición $\vec{k}\cdot\vec{k} = 0$. Lo único interesante, desde el punto de vista de la invariancia bajo traslación espacial, es la dependencia en $x$ y $z$.

Volvamos ahora al océano rectangular y a los modos independientes de $z$, (11.122). Si nuestro océano tiene lados en $x = 0$ y $x = X$, debemos elegir combinaciones lineales de los modos (11.122) tales que el desplazamiento en $x$ se anule en los lados. Podemos hacerlo para $x = 0$ formando las combinaciones

$$\psi_x(x, y, t) = -\sin kx\,\cosh ky\,\cos\omega t, \qquad \psi_y(x, y, t) = \cos kx\,\sinh ky\,\cos\omega t. \tag{11.125}$$

Entonces, si

$$k = \frac{n\pi}{X}, \tag{11.126}$$

la condición de contorno en $x = X$ también se satisface.

*(Figura 11.22: el movimiento de un fluido incompresible en una onda.)*

Ya conocemos las matemáticas del desplazamiento del agua seca. Antes de pasar a discutir la relación de dispersión, detengámonos a considerar qué aspecto tiene esto realmente. Imagine que colocamos en el agua una cuadrícula rectangular regular de puntos en equilibrio. Entonces, en la figura 11.22 mostramos qué aspecto tiene la cuadrícula en el modo (11.125) con $n = 1$. Cada uno de los pequeños rectángulos de la figura 11.22 era un cuadrado en la posición de equilibrio (cuando $\psi = 0$). Nótese cómo funciona la incompresibilidad: cuando el agua se comprime en una dirección, se estira en la otra. Puede verlo en movimiento en el programa 11-3.

Habiendo mirado esto, podemos olvidarlo un rato y concentrarnos solo en la superficie: eso es lo que importa para la relación de dispersión. Para facilitar la presentación en los diagramas siguientes, exageraremos el desplazamiento en la dirección vertical $y$ y olvidaremos el desplazamiento de la superficie en la dirección $x$ (que de todos modos no importará). Entonces la onda tiene el aspecto de la figura 11.23.

*(Figura 11.23: la superficie de una onda en el agua, con el desplazamiento horizontal suprimido.)*

Usaremos argumentos energéticos para obtener la relación de dispersión. Hay tres contribuciones a la energía total de la onda estacionaria (11.125): la energía potencial gravitatoria, la energía almacenada en la tensión superficial y la energía cinética. Consideremos cada una por turno.

#### Potencial gravitatorio

En el diagrama de la figura 11.24 puede verse que el efecto global de los desplazamientos en el modo (11.125) es tomar un trozo de agua de $X - x$, elevarlo $\varepsilon\psi_y(x, L, t)$ (el desplazamiento vertical de la superficie) y llevarlo a $x$. El volumen de ese trozo es $W\,dx\,\varepsilon\psi_y(x, L, t)$, donde $dx$ es la longitud del trozo y $W$ es la anchura en la dirección $z$ (hacia dentro del papel). Así, el potencial gravitatorio total es

$$V_{\text{grav}} = \rho g\int dV\,\Delta h = \rho g W\int_0^{\pi/2k} dx\,|\varepsilon\psi_y(x, L, t)|^2 + O(\varepsilon^3)$$

$$= \rho g W\int_0^{\pi/2k} dx\,\varepsilon^2\cos^2 kx\,\sinh^2 kL\,\cos^2\omega t + \cdots = \frac{\pi}{4k}\rho g W\varepsilon^2\sinh^2 kL\,\cos^2\omega t + \cdots. \tag{11.127}$$

*(Figura 11.24: se retira agua del rectángulo en $X - x$ y se eleva hasta el rectángulo en $x$.)*

#### Tensión superficial

La energía almacenada en la tensión superficial es $W$ multiplicada por la diferencia entre la longitud de la superficie y la longitud de equilibrio ($X$). Esto exige que tengamos algo de cuidado con la posición de la superficie, volviendo a (11.109). La posición de la superficie es

$$R_x(x, t) = x + \varepsilon\psi_x(x, L, t), \qquad R_y(x, t) = \varepsilon\psi_y(x, L, t). \tag{11.128}$$

La longitud es entonces

$$\int_0^X dx\sqrt{\left(\frac{\partial R_x}{\partial x}\right)^2 + \left(\frac{\partial R_y}{\partial x}\right)^2}. \tag{11.129}$$

Pero

$$\frac{\partial R_x}{\partial x} = 1 + \varepsilon\frac{\partial\psi_x}{\partial x}, \qquad \frac{\partial R_y}{\partial x} = \varepsilon\frac{\partial\psi_y}{\partial x}. \tag{11.130}$$

Así,

$$V_{\text{sup}} = T\times(\text{Área} - \text{Área}_0) = T W\int_0^{\pi/k} dx\left(\sqrt{(1 + \varepsilon\partial\psi_x/\partial x)^2 + (\varepsilon\partial\psi_y/\partial x)^2} - 1\right)$$

$$= T W\int_0^{\pi/k} dx\left(\varepsilon\frac{\partial\psi_x}{\partial x} + \frac{1}{2}\left(\varepsilon\frac{\partial\psi_y}{\partial x}\right)^2 + O(\varepsilon^3)\right). \tag{11.131}$$

El término de orden $\varepsilon$ de (11.131) se cancela al integrar en $x$, de modo que

$$V_{\text{sup}} = \frac{1}{2}T W\varepsilon^2 k^2\int_0^{\pi/k} dx\,\sin^2 kx\,\sinh^2 kL\,\cos^2\omega t + \cdots = \frac{\pi}{4k}T W\varepsilon^2 k^2\sinh^2 kL\,\cos^2\omega t + \cdots. \tag{11.132}$$

#### Energía cinética

La energía cinética se obtiene integrando $\frac{1}{2}mv^2$ sobre todo el volumen del líquido:

$$KE = \frac{\rho}{2}\int dV\,\vec{v}^2 = \frac{\rho W}{2}\int_0^{\pi/k} dx\int_0^L dy\left[(\varepsilon\partial\psi_x/\partial t)^2 + (\varepsilon\partial\psi_y/\partial t)^2\right]$$

$$= \frac{\rho W\varepsilon^2}{2}\int_0^{\pi/k} dx\int_0^L dy\,\omega^2\sin^2\omega t\left[\cos^2 kx\,\sinh^2 ky + \sin^2 kx\,\cosh^2 ky\right]$$

$$= \frac{\pi}{4k}\rho W\varepsilon^2\int_0^L dy\,\omega^2\sin^2\omega t\,\cosh 2ky = \frac{\pi}{8k^2}\rho W\varepsilon^2\omega^2\sinh 2kL\,\sin^2\omega t. \tag{11.135}$$

#### Relación de dispersión

El total de (11.127)-(11.135) es

$$V_{\text{grav}} + V_{\text{sup}} + KE = \frac{\pi}{4k}\rho g W\varepsilon^2\sinh^2 kL\,\cos^2\omega t + \frac{\pi}{4k}T W\varepsilon^2 k^2\sinh^2 kL\,\cos^2\omega t + \frac{\pi}{8k^2}\rho W\omega^2\varepsilon^2\sinh 2kL\,\sin^2\omega t + \cdots. \tag{11.136}$$

Esto debe ser constante en el tiempo, lo que implica

$$\omega^2 = \frac{2\sinh^2 kL\left(gk + \frac{T}{\rho}k^3\right)}{\sinh 2kL} = \left(gk + \frac{T}{\rho}k^3\right)\tanh kL, \tag{11.137}$$

donde $\tanh$ es la «tangente hiperbólica», definida por

$$\tanh x \equiv \frac{\sinh x}{\cosh x} = \frac{e^x - e^{-x}}{e^x + e^{-x}}. \tag{11.138}$$

Nótese que, en el doble límite de longitud de onda larga y agua poco profunda, las ondas en el agua se vuelven no dispersivas: para $kL \ll 1$ y $\rho g k \gg T k^3$, $\tanh kL \to kL$ y

$$\omega^2 \approx gL\,k^2. \tag{11.139}$$

#### Gravedad frente a tensión superficial

La relación de dispersión (11.137) implica una competición entre la gravedad y la tensión superficial. Para longitudes de onda largas domina la gravedad y el término $gk$ es el más importante. Para longitudes de onda cortas domina la tensión superficial y el término $Tk^3/\rho$ es el más importante. El cruce ocurre para números de onda del orden de

$$k_0 = \sqrt{\frac{\rho g}{T}}. \tag{11.140}$$

La longitud de onda de cruce es en realidad una distancia familiar. Hay un proceso mucho más familiar que implica una competición similar entre gravedad y tensión superficial. Considere una gota de agua sobre una superficie de baja fricción, como una sartén de teflón. Una gota muy pequeña es casi esférica. Pero al aumentar el tamaño de la gota, empieza a aplanarse. Y cuando la gota crece por encima de un tamaño crítico, la altura de la gota deja de aumentar: se extiende con una altura fija, $h$, como se muestra en sección en la figura 11.25.

*(Figura 11.25: sección de una gota de agua sobre una superficie sin fricción.)*

Como con la relación de dispersión, podemos entender lo que ocurre considerando la energía. La energía total de la gota es la suma de la energía potencial gravitatoria y la energía debida a la tensión superficial:

$$V_{\text{grav}} \approx \rho\,g\,h\,v, \tag{11.141}$$

donde $v$ es el volumen de la gota, y

$$V_{\text{sup}} \approx \frac{T v}{h}. \tag{11.142}$$

El volumen es fijo, así que el valor de equilibrio de $h$ minimiza la suma

$$V_{\text{grav}} + V_{\text{sup}} \approx \rho g h v + \frac{T v}{h}. \tag{11.143}$$

El mínimo ocurre para

$$T \approx \rho\,g\,h^2. \tag{11.144}$$

La tensión superficial medida del agua es $T \approx 72$ dinas/cm. Esto da la altura familiar de una gota de agua, $h \approx 0.4$ cm. Esta altura está relacionada con $k_0$ por

$$h \approx \sqrt{\frac{T}{\rho g}} = \frac{1}{k_0}. \tag{11.145}$$

## 11.6 Lentes y óptica geométrica

### Óptica geométrica

La idea de la óptica geométrica es entender los efectos de la refracción y la reflexión sobre haces de luz, ignorando los efectos de la difracción. En realidad, esto es solo la ley de Snell y geometría. Una aplicación de estas ideas será la discusión del arcoíris en la sección siguiente. Allí usaremos lo que se llama «trazado de rayos», que, como su nombre indica, consiste simplemente en seguir la pista de lo que hace cada rayo de luz al atravesar la gota. Una gota esférica es una «lente gruesa»: evidentemente, no tiene sentido considerar «delgada» una esfera. En esta sección vamos a ver cómo dar una descripción aproximada más sencilla de lo que hace una «lente delgada». De hecho, si estuviéramos diseñando un instrumento óptico de mucha precisión, seguiríamos usando el trazado de rayos para afinar los detalles. Pero el análisis de lente delgada es un buen punto de partida aproximado y nos ayudará a entender lo que ocurre en algunas situaciones importantes.

Técnicamente, lo que significa «delgada» en este contexto es que, si un haz estrecho de luz aproximadamente perpendicular al plano de la lente entra en la lente por algún punto de un lado, sale más o menos por el mismo punto del otro lado. Si ignoramos el pequeño cambio de posición, esto simplifica el análisis y nos da la fórmula de la lente delgada.

### Lentes esféricas delgadas

Antes en este capítulo dedujimos la fórmula del cambio angular de un haz estrecho de luz (estamos ignorando la difracción) debido a un prisma. El análisis usa la construcción geométrica de la figura 11.26 y da

$$\delta = \theta_{in} + \theta_{out} - \theta_1 - \theta_2 \approx n(\theta_1 + \theta_2) - \phi \approx (n - 1)\phi \tag{11.146}$$

donde la primera igualdad es exacta y la segunda se sigue en el límite en que los ángulos $\theta$ son pequeños. En ese límite, la desviación angular es independiente del ángulo de entrada.

*(Figura 11.26: la geometría del prisma, de nuevo.)*

### Lentes delgadas y ángulos pequeños

Podemos usar este resultado para entender cómo enfoca la luz una lente. Una lente es un dispositivo en el que el cambio angular que se da al haz es proporcional a la distancia al eje, para ángulos y distancias pequeños:

$$\delta \approx h/f \tag{11.147}$$

donde $f$ es una longitud. Esto es aproximadamente cierto para un trozo de vidrio con superficies que son partes de esferas. En la figura 11.27 hay un diagrama que muestra cómo funciona esto para una lente que es plana por un lado y una porción de esfera de radio $r_1$ por el otro. En el diagrama, $\theta_1$ es el ángulo del «prisma efectivo» que ve la parte del haz que está a distancia $h$ del eje. Debería quedar claro por la figura que, si $\theta_1$ es pequeño, es proporcional a $h$:

$$\theta_1 \approx \sin\theta_1 = \frac{h}{r_1}. \tag{11.148}$$

*(Figura 11.27: lente plana por un lado y esférica de radio $r_1$ por el otro.)*

Más a menudo, la lente es curva por ambos lados. Si los radios son $r_1$ y $r_2$, el resultado tiene el aspecto de la figura 11.28. La figura 11.28 muestra el haz justo en la punta de la lente por comodidad pero, como debería dejar claro el diagrama anterior, $\theta_1 + \theta_2$ es el ángulo del «prisma efectivo» para cualquier $h$. La figura exagera también la curvatura de los dos lados, de modo que la lente dibujada no es realmente «delgada»: una lente delgada de verdad tiene las caras mucho menos curvadas. Esto es importante porque, si la lente es gruesa, la altura $h$ no está muy bien definida: si la luz dentro de la lente no es horizontal, podríamos tener una $h$ donde la luz entra en la lente y una $h$ muy distinta donde sale. Pero si la lente es delgada y los rayos no están muy lejos de la perpendicular, esta ambigüedad en $h$ puede ignorarse igual que las demás correcciones a las relaciones de ángulos pequeños (como $\sin\theta \approx \theta$).

*(Figura 11.28: lente curva por ambos lados, con radios $r_1$ y $r_2$.)*

Juntando la geometría de la figura 11.28 con la fórmula de $\delta$ para un prisma, obtenemos la constante $f$ para una lente esférica delgada:

$$\delta = (n - 1)(\theta_1 + \theta_2) = (n - 1)\left(\frac{h}{r_1} + \frac{h}{r_2}\right) = \frac{h}{f} \tag{11.149}$$

y, por tanto,

$$\frac{1}{f} = (n - 1)\left(\frac{1}{r_1} + \frac{1}{r_2}\right). \tag{11.150}$$

Esta es la llamada «fórmula del fabricante de lentes».

Una lente de este tipo enfoca los rayos paralelos de luz, como se muestra en la figura 11.30. Esto funciona porque $\delta \approx h/f$, como se muestra en la figura 11.31. Los rayos paralelos con cualquier ángulo se enfocan sobre un «plano focal» a una distancia $f$ de la lente, como se muestra en la figura 11.32. La manera analítica de explicar cómo funciona esto es notar que la diferencia entre las pendientes de los rayos a ambos lados de la lente es proporcional a la altura. Así, en este caso, como las pendientes de un lado son las mismas, la diferencia de pendientes del otro lado es proporcional a la diferencia de alturas, y eso significa que todos convergen en la misma $x$.

*(Figura 11.30: una lente enfoca rayos paralelos.)*

*(Figura 11.31: la desviación es proporcional a la altura.)*

*(Figura 11.32: rayos paralelos con cualquier ángulo se enfocan sobre el plano focal.)*

Otra forma de ver que este enfoque debe funcionar se ilustra en las figuras 11.33 y 11.34. Nótese que, si los rayos paralelos llegan con un ángulo $\delta_i$, el rayo que está a una distancia $h_i = \delta_i f$ por encima del centro de la lente se desvía hasta la horizontal, como se muestra en la figura 11.33 con la línea continua. Entonces, para los rayos a ambos lados de ese (mostrados con líneas discontinuas), como la dependencia de la desviación con la altura en la lente es lineal, la desviación angular total, $\delta_i + \delta_o$, es $1/f$ multiplicada por la distancia total al centro, $h_i + h_o$; pero entonces $h_o = \delta_o f$, que es la condición de enfoque. Esto se ilustra en la figura 11.34.

*(Figura 11.33: el rayo a la altura $h_i = \delta_i f$ se desvía hasta la horizontal.)*

*(Figura 11.34: la condición de enfoque.)*

Para un haz de rayos paralelos con cualquier ángulo, puede determinar dónde inciden en el plano focal trazando cualquier rayo; el más fácil es el que pasa por el centro de la lente, que no se desvía en absoluto, como se muestra en la figura 11.35. Los rayos paralelos (una parte de una onda plana; sabemos que eso es imposible, pero estamos ignorando la difracción) pueden pensarse como procedentes de una fuente puntual en el infinito. Si hay una fuente puntual más cerca de la lente, esta enfoca más lejos. Ahora juegue con la animación LENS.EXE.

*(Figura 11.35: el rayo que pasa por el centro de la lente no se desvía.)*

*(Figura 11.36: una fuente puntual a distancia $d_1$ se enfoca a distancia $d_2$.)*

Para hallar la relación entre $d_1$ y $d_2$, considere el diagrama de la figura 11.37: la suma de los ángulos de desviación a ambos lados es igual a $\delta$:

$$\delta_1 + \delta_2 = \delta,$$

lo que, para ángulos pequeños, equivale a

$$\frac{h}{d_1} + \frac{h}{d_2} = \frac{h}{f}$$

o

$$\frac{1}{d_1} + \frac{1}{d_2} = \frac{1}{f}. \tag{11.153}$$

Esta es la llamada «fórmula de la lente delgada».

*(Figura 11.37: la suma de las desviaciones a ambos lados es $\delta$.)*

Hasta ahora hemos discutido lentes «convergentes» o «convexas», para las que $f$ es positiva, pero también hay lentes «divergentes» o «cóncavas», para las que $f$ es negativa. En ese caso, los rayos paralelos no se enfocan, sino que se desenfocan, y parecen divergir de un plano situado a una distancia $-f$ (que es un número positivo) más allá de la lente, como se muestra en la figura 11.38. El punto del que divergen los rayos salientes se llama «imagen virtual». En este caso es una imagen virtual del punto en el infinito. En la figura 11.39 se muestra el efecto de una lente cóncava sobre una fuente puntual. De nuevo hay una imagen virtual. Aquí la fórmula de la lente delgada se sigue satisfaciendo, pero tanto $f$ como $d_2$ son negativas.

*(Figura 11.38: una lente divergente y su imagen virtual del punto en el infinito.)*

*(Figura 11.39: efecto de una lente cóncava sobre una fuente puntual.)*

### Imágenes

La propiedad de enfoque de una lente puede usarse para proyectar la imagen de un objeto sobre una superficie, como se muestra en la figura 11.40. Lo que ocurre es que la luz que se abre desde cada punto del objeto se vuelve a enfocar en un único punto de la pantalla. Como en las figuras 11.36 y 11.37, las distancias satisfacen la fórmula de la lente delgada,

$$\frac{1}{d_1} + \frac{1}{d_2} = \frac{1}{f}. \tag{11.153}$$

Esto le dice dónde poner la pantalla. Nótese además que es fácil ver en qué punto de la pantalla aparece la imagen de un punto concreto del objeto, porque el rayo de luz que pasa justo por el centro de la lente no se desvía en absoluto (esto lo usamos también para los rayos paralelos, arriba de la figura 11.35). Esto, más geometría sencilla, implica que la razón entre el tamaño de la imagen y el del objeto es $d_2/d_1$:

$$\frac{\text{tamaño de la imagen}}{\text{tamaño del objeto}} = \frac{d_2}{d_1}. \tag{11.154}$$

*(Figura 11.40: proyección de la imagen de un objeto sobre una pantalla.)*

Si se retira la pantalla de la figura 11.40, puede verse que la luz a la derecha de donde estaba la pantalla es una copia de la luz que viene del objeto, pero al revés y con el tamaño cambiado en $d_2/d_1$. Si ha jugado con lentes, ya lo sabe.

Nótese que (11.153) implica que ni $d_1$ ni $d_2$ pueden ser menores que $f$. Si acerca demasiado el objeto a la lente, no obtiene una imagen real al otro lado. En su lugar, $d_2$ se hace negativa y se obtiene una «imagen virtual» al mismo lado de la lente que el objeto, y la luz a la derecha de la lente diverge como si viniera de la imagen virtual. Esta situación se ilustra en la figura 11.41. Como discutiremos más abajo, así es como funciona una lupa.

*(Figura 11.41: imagen virtual cuando el objeto está más cerca que la distancia focal.)*

La formación de imágenes ilustrada en la figura 11.40 es lo que ocurre en una cámara y en su propio globo ocular. La lente enfoca la luz de puntos exteriores sobre puntos de la película, o de su retina. Por supuesto, la retina no es realmente un plano. Por la misma razón, el cristalino de su ojo no es una lente esférica, sino de una forma más complicada. El trazado de rayos lo ha hecho la evolución, sin embargo, de modo que los objetos en un plano se enfocan correctamente sobre la retina.

Como la distancia del cristalino a la retina está fijada por la geometría de su ojo, usted debe poder ajustar la forma del cristalino. Al hacerlo, puede cambiar la distancia focal de su cristalino y, con ella, la distancia a la que los puntos están perfectamente enfocados (esto se llama «acomodación»).

La formación de una imagen en la retina se ilustra en el diagrama de la figura 11.42. De nuevo, como en la figura 11.40, la imagen está invertida. No puede enfocar objetos demasiado cercanos al cristalino porque la cantidad de acomodación que puede hacer es limitada. Si acerca el objeto más de la distancia focal más pequeña que su cristalino puede producir, la imagen real queda más allá de la retina y el objeto se verá borroso, como se muestra en la figura 11.43.

*(Figura 11.42: formación de una imagen en la retina.)*

*(Figura 11.43: objeto demasiado cercano: la imagen queda más allá de la retina.)*

Una lupa funciona permitiéndole producir una imagen mayor del objeto sobre su retina. Lo hace de dos maneras, ambas ilustradas en el diagrama de la figura 11.44 (con menos rayos dibujados ahora, porque los diagramas se están volviendo demasiado recargados).

Obviamente, la imagen es mayor. Pero nótese además que la lupa cambia la cantidad de acomodación que su cristalino necesita. Su ojo está enfocando en realidad la imagen virtual, que está mucho más lejos, y eso es más fácil. Así, cuando mira un objeto con una lupa puede acercárselo mucho más al ojo de lo que podría sin ella. Esto aumenta aún más el efecto de aumento, porque los objetos más cercanos se ven más grandes. En este diagrama puede verse también un tercer efecto beneficioso de la lupa: llega más luz del objeto a su ojo.

*(Figura 11.44: cómo funciona una lupa.)*

Uno de los efectos de aumento de una lente puede obtenerse sin lente de una manera muy sencilla: con un agujero de alfiler. Si mira un objeto cercano a través de un agujero de alfiler, puede acercárselo mucho más al ojo. La razón es que solo pasa un haz estrecho de luz por el agujero desde cada punto del objeto que mira, así que no hace falta mucho enfoque. El tamaño de la imagen en su retina no aumenta cuando mira el objeto a través de un agujero de alfiler a la misma distancia que sin él pero, con el agujero, puede acercárselo mucho más al ojo sin que se vea borroso y, por tanto, hacer que parezca más grande.

Puede que también haya jugado con cámaras estenopeicas, en las que se forma una imagen sobre una pantalla dentro de una caja oscura sin lente, como se muestra en la figura 11.45.

*(Figura 11.45: una cámara estenopeica.)*

Una desventaja de la cámara estenopeica es que hace falta un objeto muy brillante: se desecha la mayor parte de la luz que viene del objeto. Puede conseguir más luz haciendo el agujero más grande, pero eso hace la imagen más borrosa. En realidad, sin embargo, tampoco puede hacer el agujero demasiado pequeño. En última instancia, como veremos en el capítulo 13, la difracción limita la resolución de una cámara estenopeica. Si intenta hacer la imagen muy nítida haciendo el agujero muy diminuto, el haz que obtiene dentro de la cámara se ensancha por difracción. Lo mejor que puede hacer es elegir el tamaño del agujero de modo que el ensanchamiento en la pantalla por difracción iguale justo el tamaño del agujero.

Ya que estamos, nótese que la difracción y el tamaño finito de su pupila limitan la resolución angular de su ojo. Como entenderemos en detalle en el capítulo 13, el tamaño finito $s$ de su pupila introduce una dispersión angular del orden de $\lambda/s$ para luz de longitud de onda $\lambda$. A menos que tenga ojos enormes, $s$ es menor que 0.25 cm, así que para luz verde de longitud de onda 500 nanómetros (550 está aproximadamente en mitad del espectro visible), la resolución angular es mayor que unos $2\times10^{-4}$. A una distancia de 10 metros, por ejemplo, incluso si sus ojos son perfectos, no será capaz de resolver dos objetos separados menos de unos pocos milímetros.

Puede usar un agujero de alfiler para estudiar sus ojos de maneras bastante interesantes. Ponga el agujero cerca del ojo y mire una fuente de luz difusa y brillante. Lo haremos en clase, pero puede fabricarse su propio agujero perforando un pequeño orificio en una lámina de papel de aluminio con un alfiler y probarlo. Si lleva gafas, quíteselas: no las necesitará. Debería ver una mancha circular de luz. Es la imagen de su pupila sobre la retina, como se muestra en la figura 11.46.

*(Figura 11.46: la imagen de su pupila sobre la retina.)*

Puede ver cómo cambia el tamaño de su pupila con este montaje. Basta con que tape o cierre el otro ojo: como ahora recibe menos luz, ambas pupilas se dilatarán. Destape el otro ojo, mire de nuevo la luz brillante y las pupilas se contraerán. ¿Nota un pequeño retardo temporal?

Ahora acerque con cuidado la punta de un bolígrafo o un lápiz desde abajo, entre el agujero y su ojo, hasta que justo empiece a tapar la vista. ¿Qué ve? Esto debería convencerle, si no estaba seguro, de que la imagen en su retina está invertida, como se muestra en la figura 11.47. Falta la mitad inferior de la imagen en su retina. Su cerebro, acostumbrado a ver las imágenes de la retina invertidas, ¡lo interpreta como un objeto que baja desde arriba!

*(Figura 11.47: la mitad inferior de la imagen retiniana queda tapada.)*

### Aumento, telescopios, microscopios y todo eso

Combinando lentes de diversas maneras se pueden construir todo tipo de instrumentos ópticos interesantes. La manera más sencilla de pensar en el aumento es considerar el tamaño angular de la imagen observada, comparado con el tamaño angular que se vería sin el instrumento.

En la figura 11.48 se ilustra un telescopio sencillo. Las distancias están algo distorsionadas: en un telescopio real, el objeto estaría mucho más lejos y los tamaños de las lentes serían mucho menores. Cuando mira un objeto lejano (con $L$ grande) con su telescopio, la luz llega a la primera lente (el «objetivo») como un haz de rayos casi paralelos. Sabemos, por la fórmula de la lente delgada,

$$\frac{1}{d_1} + \frac{1}{d_2} = \frac{1}{f},$$

con $d_1 = L \gg f$, que se forma una imagen real a una distancia del objetivo $d_2$ apenas mayor que su distancia focal $f_1$. El «ocular» se coloca entonces a una distancia apenas mayor que su distancia focal, $f_2$, de la imagen real, para convertir de nuevo la luz de la imagen en un haz casi paralelo. Esencialmente, lo que hace con el ocular es mirar la luz de la imagen real con una lupa.

*(Figura 11.48: un telescopio sencillo.)*

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

*(Figura 11.49: un microscopio.)*

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

$$\sin\phi = \frac{\sin\theta}{n} \qquad \text{o} \qquad \phi = \sin^{-1}\left(\frac{\sin\theta}{n}\right). \tag{11.164}$$

*(Figura 11.50: refracción de un rayo en una gota esférica.)*

Parte de la luz también se refleja en la gota. Nótese que la luz reflejada se refleja especularmente. Para $\theta = 0$, la luz se refleja directamente hacia atrás. Al aumentar $\theta$ desde 0, el rayo reflejado gira en sentido antihorario respecto del rayo incidente un ángulo $\pi - 2\theta$, hasta que en $\theta = \pi/2$ apenas roza la esfera y no gira nada.

El hecho geométrico importante que hace el problema bastante sencillo es que el ángulo entre el rayo y la perpendicular a la superficie es el mismo cuando sale de la gota que cuando entra. La ley de Snell funciona a la inversa, y el rayo que sale de la gota forma un ángulo $\theta$ con la perpendicular. Como puede verse en la figura 11.51, esto significa que el rayo refractado que sale de la gota es simplemente una versión del rayo reflejado de la figura 11.50 girada $\pi - 2\phi$. Eso significa que está girado

$$\theta_1 = (\pi - 2\phi) - (\pi - 2\theta) = 2\theta - 2\phi \tag{11.165}$$

respecto de la dirección original de la luz incidente.

*(Figura 11.51: el rayo refractado que sale de la gota.)*

El problema con esto es que no tiene nada que ver con el arcoíris. El problema es que la dirección del rayo refractado es básicamente hacia delante y depende de $\theta$, de modo que no se destaca ningún valor concreto de $\theta$. Hay tres cosas misteriosas del arcoíris que este efecto no puede explicar:

i. el arcoíris primario ocurre a un ángulo definido;

ii. el ángulo es en la dirección hacia atrás —a un ángulo de unos 41° (unos 0.7 radianes) del rayo de luz incidente, es decir, girado unos 2.4 radianes respecto de la dirección original—; y

iii. hay un segundo arcoíris fuera del primero, ¡en el que los colores van en orden opuesto!

*(Figura 11.52: gráfica de $\theta_1$ frente a $\theta$ para luz roja y azul.)*

Entonces, ¿qué hace esta refracción? La respuesta es: ¡casi nada! El rayo refractado se reparte sobre un amplio rango de ángulos, como se muestra en la gráfica de la figura 11.52. A un ángulo de salida cualquiera, la luz de este efecto es muy tenue y apenas se nota. No solo los colores no se separan mucho, sino que además todos se reparten de forma más o menos uniforme sobre el ángulo de salida, de modo que no se ve ningún arcoíris por esta refracción.

Entonces, ¿de dónde viene el arcoíris? La respuesta es que, además de refractarse en la superficie interior de la gota, el rayo también puede reflejarse y salir después a un ángulo todavía mayor. El resultado tiene el aspecto de la figura 11.53.

*(Figura 11.53: el rayo que se refleja una vez dentro de la gota.)*

Comparando la figura 11.51, la figura 11.53 y la ecuación (11.165), está claro que en este camino la luz gira

$$\theta_2 = 2(\pi - 2\phi) - (\pi - 2\theta) = 2\theta + \pi - 4\phi. \tag{11.166}$$

Y aquí está el punto crítico. Si representamos este $\theta_2$ frente a $\theta$, ¡la gráfica tiene un mínimo! Esto se muestra en la figura 11.54.

*(Figura 11.54: gráfica de $\theta_2$ frente a $\theta$ para luz roja y azul.)*

Ahora el ángulo de salida tiene un mínimo para $\theta \approx 1.05$ (que es el valor de $\theta$ ilustrado en los diagramas). El ángulo de salida $\theta_2 \equiv \theta_{out}$ correspondiente a ese $\theta$ da la posición angular del arcoíris. Aquí, como $\theta_2$ no cambia mucho ante un cambio pequeño de $\theta$, se ve la suma de la luz refractada procedente de un rango de $\theta$ alrededor del mínimo. El ángulo es aproximadamente el que esperamos: $\theta_{out} \approx \pi - 0.7$, donde 0.7 radianes ≈ 41° es el ángulo entre el vector que va de la gota al Sol y el que va de esa misma gota a su ojo, como se muestra en la figura 11.55. El signo negativo de $\pi - 0.7$ significa que la luz no ha girado 180° completos, así que la luz que llega a su ojo entró en la gota refractante por el lado más alejado de usted.

*(Figura 11.55: geometría del Sol, la gota y el ojo.)*

También puede verse en la gráfica de la figura 11.54 que los colores están separados. La luz roja está en el exterior (más lejos de $2\pi$) y la azul en el interior.

Matemáticamente, ¿por qué se acumula la luz en el borde? La energía de la luz solar que cae sobre una parte pequeña de la superficie de la gota entre $\theta$ y $\theta + d\theta$ es proporcional a $I\,d\theta$ (hay otros factores, como $\cos\theta$, pero varían lentamente, así que olvidémoslos). El ángulo del rayo saliente, $\theta_{out}$, es una función de $\theta$, y la energía $\propto I_i\,d\theta$ se reparte sobre una región angular entre $\theta_{out}$ y $\theta_{out} + d\theta_{out}$. Así, la intensidad saliente es proporcional a

$$I_o \propto \frac{I_i\,d\theta}{d\theta_{out}} = \frac{I_i}{\dfrac{d\theta_{out}}{d\theta}}. \tag{11.167}$$

¡Cuando $d\theta_{out}/d\theta = 0$, la intensidad se va a infinito! El borde es infinitamente más brillante que el interior. ¡Por eso lo vemos!

Podemos comprobar ahora esta imagen viendo cómo explica el segundo arcoíris. Como cabe suponer, procede de una reflexión más, como se muestra en la figura 11.56.

*(Figura 11.56: el rayo que se refleja dos veces dentro de la gota.)*

Ahora el rayo de luz gira

$$\theta_3 = 3(\pi - 2\phi) - (\pi - 2\theta) = 2\theta + 2\pi - 6\phi. \tag{11.168}$$

Esto se muestra, junto con $\theta_2$, en la gráfica de la figura 11.57. El mínimo de $\theta_3$ es la posición del segundo arcoíris. Pero ahora, como el ángulo es mayor que $\pi$, la luz llega a su ojo por el lado de la gota que está más cerca de usted, y está doblándose completamente alrededor.

*(Figura 11.57: gráfica de $\theta_2$ y $\theta_3$ frente a $\theta$ para luz roja y azul.)*

Por eso los colores están invertidos. De nuevo, el azul se refracta más, pero esta vez eso significa que el azul queda en el exterior, mientras que el rojo queda en el interior.

Por casualidad, los mínimos de $\theta_2$ y $\theta_3$ están desplazados de $\pi$ casi lo mismo (dentro de unos 0.13 radianes), aunque en lados opuestos. Por eso los dos arcoíris están bastante juntos en el cielo.

Otra predicción de esta imagen que puede verse a menudo es la «banda oscura de Alejandro», que aparece entre los arcoíris. La luz que no se concentra en el valor mínimo de $\theta$ se reparte dentro del primer arcoíris pero fuera del segundo; así, la región entre los dos arcoíris (o fuera del primero, si el segundo no se ve) es más oscura. Si representamos la distancia angular respecto de $\pi$ en función del ángulo con el que la luz solar entra en la gota, el primer y el segundo arcoíris tienen el aspecto de la figura 11.58 (como de costumbre, he exagerado la diferencia de índice de refracción entre el rojo y el azul). Aquí se ve claramente que el ángulo del primer arcoíris es menor, y la banda oscura entre los dos.

*(Figura 11.58: los dos arcoíris.)*

## 11.8 Ondas esféricas

Considere ondas sonoras en una sala muy grande con paredes absorbentes. En el centro de la sala (tomaremos el centro como origen de nuestro sistema de coordenadas, $\vec{r} = 0$) hay un altavoz esférico, una esfera que produce en su superficie (de radio $R$) una presión oscilante de la forma $p_0\cos\omega t$. ¿Qué tipo de ondas sonoras se producen? Parece bastante tonto usar nuestras soluciones de onda plana con invariancia bajo traslación espacial para este problema, porque el sistema tiene simetría bajo rotaciones alrededor del origen. En su lugar, miremos directamente la ecuación de ondas y aprovechemos la naturaleza esférica del problema. Es decir, supongamos que la solución tiene la forma $\psi(\vec{r}, t) = \chi(|\vec{r}|, t)$. Sustituyendo esto en la ecuación de ondas se obtiene

$$\vec{\nabla}^2\chi(r, t) = \frac{\partial^2}{\partial r^2}\chi(r, t) + \frac{2}{r}\frac{\partial}{\partial r}\chi(r, t). \tag{11.172}$$

Podemos reescribir esto de la siguiente forma útil:

$$\vec{\nabla}^2\chi(r, t) = \frac{1}{r}\frac{\partial^2}{\partial r^2}\left[r\,\chi(r, t)\right]. \tag{11.173}$$

Así, $r\chi(r, t)$ satisface la ecuación de ondas unidimensional.

Ahora podemos resolver el problema que planteamos arriba. Las soluciones para $r\chi$ tienen la forma $\sin(kr \pm \omega t)$ y $\cos(kr \pm \omega t)$, donde $k = \omega/v$. Como la presión en $r = R$ es $p_0\cos\omega t$, nos interesan las combinaciones $\cos(kr - kR - \omega t)$ y $\cos(kr - kR + \omega t)$. Estas describen ondas que salen del origen y que van hacia él, respectivamente. La condición de contorno apropiada en el infinito es tomar la onda saliente, de modo que la perturbación la produzca enteramente el altavoz. Así,

$$\chi(r, t) = \frac{p_0 R}{r}\cos(kr - kR - \omega t). \tag{11.174}$$

Las características generales de la solución (11.174) son fáciles de entender. Los frentes de onda, a lo largo de los cuales la fase de oscilación es constante, son esferas centradas en el origen, como debe ser por la simetría rotacional. Las ondas se alejan del origen con velocidad $v$. Al alejarse, su intensidad local debe disminuir, porque la misma cantidad de energía se reparte sobre un área mayor. Esa es la razón del $1/r$ de (11.174). Si la amplitud cae como $1/r$, la intensidad de la onda cae como $1/r^2$, como debe ser. Aunque la física está clara, la forma precisa de esta solución es engañosamente sencilla. En dos dimensiones, por ejemplo, no es posible hallar una solución de un problema análogo usando las funciones que conoce del instituto. En dos dimensiones, la amplitud de la onda debe decrecer aproximadamente como $1/\sqrt{r}$. Las soluciones de la ecuación de ondas bidimensional con esa propiedad se llaman funciones de Bessel. Aprenderá sobre ellas en cursos más avanzados.

## Repaso del capítulo

Ahora debería ser capaz de:

i. Interpretar las ondas planas en el espacio de dos y tres dimensiones en términos de un vector $\vec{k}$, el número de onda angular;

ii. Analizar la dispersión de una onda plana en un contorno plano entre regiones con relaciones de dispersión distintas;

iii. Deducir y usar la ley de Snell;

iv. Comprender el fenómeno de la reflexión total interna, junto con el enunciado general de la condición de contorno en el infinito para $\vec{k}$ complejo;

v. Comprender la física y las matemáticas de los fenómenos de efecto túnel;

vi. Comprender cómo afecta la degeneración de las frecuencias de los modos normales al problema de la oscilación forzada, y hallar los patrones de arena en placas de Chladni cuadradas;

vii. Comprender la propagación de ondas en guías de onda, usando la separación de variables para construir los modos e interpretar el resultado en términos de ondas en zigzag;

viii. Ser capaz de analizar las ondas en el agua, ignorando la viscosidad y el momento angular;

ix. Resolver problemas con ondas esféricas donde el desplazamiento solo depende de $r$ y $t$.

## Problemas

**11.1.** Considere las oscilaciones transversales libres de la cuerda bidimensional con cuentas mostrada en la figura 11.59. Todas las cuerdas horizontales tienen tensión $T_h$, todas las verticales tienen tensión $T_v$, y todos los círculos macizos son cuentas de masa $m$. El marco cuadrado está fijo en el plano $z = 0$.

**a.** Halle los modos normales y sus frecuencias correspondientes.

**b.** Suponga que $T_v = 100\,T_h$. Dibuje nueve diagramas, uno para cada modo normal, en orden de frecuencia creciente, indicando qué cuentas se mueven hacia arriba (con un signo $+$), cuáles hacia abajo (con un signo $-$) y cuáles no se mueven (con un 0). Puede intercambiar $+$ y $-$ y seguir teniendo la respuesta correcta, cambiando el origen de tiempos o multiplicando su vector de modo normal por $-1$. Haga el resto y ponga el orden correcto. Debería poder hacerlo incluso si se lió con los detalles del apartado a.

*(Figura 11.59: una cuerda bidimensional con cuentas.)*

**11.2.** Considere las oscilaciones transversales forzadas de la cuerda bidimensional con cuentas mostrada en la figura 11.60. Todas las cuerdas tienen tensión $T$ y todos los círculos macizos son cuentas de masa $m$. El marco se mantiene fijo en el plano $z = 0$. Los círculos huecos se mueven arriba y abajo fuera del plano del papel con el mismo desplazamiento transversal,

$$z_1(t) = z_2(t) = z_3(t) = d\cos\omega t$$

donde

$$\omega = \sqrt{\frac{T}{ma}}.$$

Halle el desplazamiento de cada una de las cuentas. Puede hacerlo resolviendo para el desplazamiento $z_{jk}(t)$ de la cuenta cuya posición horizontal es $x = kL/4$, $y = jL/4$, para todos los $j$ y $k$ relevantes. Todos los desplazamientos serán proporcionales a $d\cos\omega t$, así que escriba su respuesta en forma de tabla de los coeficientes de $d\cos\omega t$ para cada $j$ y $k$.

*(Figura 11.60: una cuerda bidimensional con cuentas, forzada.)*

**11.3.** Considere las oscilaciones transversales forzadas de la cuerda bidimensional semiinfinita con cuentas mostrada en la figura 11.61. Todas las cuerdas tienen tensión $T$, todos los círculos macizos son cuentas de masa $m$ y las separaciones de equilibrio de los bloques son todas $a$. El marco en $y = 0$ e $y = 4a$ se mantiene fijo en el plano $z = 0$. Los círculos huecos en $x = 0$ se mueven arriba y abajo fuera del plano del papel con desplazamiento transversal

$$z_1(t) = z_3(t) = \frac{d}{\sqrt{2}}\cos\omega t, \qquad z_2(t) = -d\cos\omega t,$$

para los valores de $\omega$ dados abajo. Para cada $\omega$, halle el desplazamiento de cada cuenta en función de su posición de equilibrio. Es decir, determine $\psi(x, y, t)$. Suponga que todo el sistema oscila con frecuencia $\omega$ y que el desplazamiento se comporta bien en $x = +\infty$.

*(Figura 11.61: una cuerda bidimensional semiinfinita con cuentas.)*

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

*(Figura 11.62: un problema de oscilación forzada en una membrana elástica.)*

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

*(Figura 11.63: amplitud de la oscilación de presión frente a $r$.)*

**11.9.** Considere un contorno entre dos membranas semiinfinitas tensadas en el plano $x$-$y$. La membrana para $x < 0$ tiene tensión superficial $\tau_s$ y densidad superficial de masa $\rho_s$. La membrana para $x > 0$ tiene la misma tensión superficial $\tau_s$ pero densidad superficial de masa distinta, $\rho_s'$. A lo largo del contorno hay un dispositivo (no sé exactamente cómo funciona) que produce una fuerza de fricción vertical proporcional a menos la velocidad vertical de la membrana en el contorno. Dicho de otro modo, si $\psi(x, y, t)$ es el desplazamiento $z$ de la membrana en función de $(x, y)$, la fuerza (en la dirección $z$) sobre un trocito del contorno que va del punto $(0, y)$ al $(0, y + dy)$ es

$$dF = -dy\,\gamma\,\frac{\partial}{\partial t}\psi(0, y, t).$$

En la membrana hay una onda plana de la forma siguiente:

$$\psi(x, y, t) = A e^{i(kx\cos\theta + ky\sin\theta - \omega t)}$$

para $x < 0$, y

$$\psi(x, y, t) = A e^{i(k'x\cos\theta' + k'y\sin\theta' - \omega t)}$$

para $x > 0$. El montaje se muestra en la figura 11.64.

*(Figura 11.64: dispersión en un contorno de una membrana elástica.)*

Halle $k'$. Halle $\theta'$. Halle $\gamma$. Debería obtener $\gamma \to 0$ para $\rho_s \to \rho_s'$; explique por qué.

**11.10.** En vez de un océano abierto, considere un sistema con un fondo en $y = 0$ y una tapa fija en $y = 2L$, medio lleno de agua y medio lleno de disolvente de pintura, otro fluido casi incompresible más ligero que el agua, que flota en la mitad superior sin mezclarse con ella.

Muestre que las ondas de este sistema tienen la forma de (11.122) para $y \leq L$ (en el agua) y

$$\psi_x(x, y, t) = \mp i\,e^{\pm ikx - i\omega t}\cosh[k(2L - y)], \qquad \psi_y(x, y, t) = e^{\pm ikx - i\omega t}\sinh[k(2L - y)] \tag{11.175}$$

para $L \leq y \leq 2L$ (en el disolvente), argumentando que (11.175) y (11.122) satisfacen las condiciones de contorno apropiadas en $y = 0$ y $y = 2L$ y (para desplazamientos pequeños) en $y = L$, y muestre que (11.175), como (11.125), es coherente con la incompresibilidad ($\vec{\nabla}\cdot\vec{\psi} = 0$).

Muestre que $\psi_x$ es discontinua en $y = L$ y explique físicamente qué está ocurriendo en ese contorno y por qué. Cuando lo haya hecho, mire el programa 11-4, en el que se anima este sistema. Si mira con atención, notará el efecto de la ruptura de la linealidad para desplazamientos grandes.

Suponga ahora que los líquidos están contenidos entre paredes verticales en $x = 0$ y $x = X$. ¿Qué condiciones de contorno se satisfacen en los contornos verticales?

Halle la forma de los desplazamientos de los modos normales de este sistema.

Muestre que la relación de dispersión de este sistema es

$$\omega^2 = \left(\frac{\rho_W - \rho_P}{\rho_W + \rho_P}\,gk + \frac{k^3\tau_S}{\rho_W + \rho_P}\right)\tanh kL, \tag{11.176}$$

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

$$\vec{J}(\vec{r}, t) = \sigma\vec{E}(\vec{r}, t). \tag{11.177}$$

Supondremos que el material no tiene ninguna otra propiedad eléctrica —en particular, que no hay polarización ni magnetización— y que no se acumula carga en ningún sitio, de modo que $\rho = 0$. Considere la propagación de una onda plana electromagnética en este universo. Como este universo es perfectamente invariante bajo traslación espacial y bajo rotaciones, y como (11.177) es lineal, cabría esperar que hubiera soluciones de onda plana en las que los campos eléctrico y magnético fueran proporcionales a $e^{i(\vec{k}\cdot\vec{r} - \omega t)}$ para $\vec{k}^2$ y $\omega$ relacionados por alguna relación de dispersión. En particular, considere la propagación en la dirección $+z$ con el campo eléctrico en la dirección $x$ y el magnético en la $y$.

**a.** Muestre, a partir de las ecuaciones de Maxwell relevantes, que tal onda plana puede existir si

$$k^2 = \mu_0\varepsilon_0\omega^2 + i\mu_0\sigma\omega.$$

**b.** Suponga que $\omega$ es real y positiva y que la parte real de $k$ es positiva. Halle el signo de la parte imaginaria de $k$ e interprete físicamente su resultado. Es decir, explique por qué el signo tenía que salir como salió.

**11.13.** Considere una onda sonora esférica que llega desde muy lejos y es absorbida completamente por un amortiguador de sonido esférico de radio $r = \ell$, como se muestra en la figura 11.65. La presión en este sistema se describe mediante la parte real de la onda viajera compleja siguiente, que depende solo del radio y del tiempo:

$$p(r, t) - p_0 = \frac{\varepsilon}{r}e^{-i(kr + \omega t)}$$

*(Figura 11.65: un amortiguador esférico de sonido.)*

**a.** Halle la potencia promediada en el tiempo absorbida por el amortiguador esférico en $r = \ell$.

**b.** Explique cualitativamente el factor $1/r$ de la presión.

Suponga ahora que hay un contorno esférico sin masa y flexible entre dos gases distintos, de radio $r = r_b$, mostrado como el círculo discontinuo del diagrama de la figura 11.66. La presión de equilibrio, $p_0$, es la misma a ambos lados del contorno. Suponga también que $\gamma$ es el mismo para los dos gases y que la única diferencia son las densidades: dentro la densidad es $\rho$ y fuera es $\rho'$. Ahora, para $\ell < r < r_b$, la presión sigue viniendo dada como antes, pero en la región exterior al círculo discontinuo hay una onda reflejada además de la incidente.

*(Figura 11.66: un amortiguador esférico de sonido con un contorno reflectante.)*

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

---

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*
