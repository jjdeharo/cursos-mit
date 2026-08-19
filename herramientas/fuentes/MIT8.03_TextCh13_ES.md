---
title: "Capítulo 13: Interferencia y difracción — 8.03SC Física III: Vibraciones y Ondas"
author: "Yen-Jie Lee (traducción al español)"
lang: es
---

# Capítulo 13: Interferencia y difracción

Un «haz» de luz nos resulta muy familiar. Un puntero láser, por ejemplo, produce un patrón de luz que se parece bastante a una sección transversal de una onda plana. Pero no del todo: el haz láser se ensancha al viajar. Podría pensar que eso se debe simplemente a las imperfecciones del láser pero, de hecho, por mucho que se esfuerce en perfeccionarlo, no puede evitar cierto ensanchamiento. El problema es la «difracción».

La interferencia es una parte crucial de la física de la difracción. Ya la hemos visto en situaciones unidimensionales, como los interferómetros y la reflexión en películas delgadas. Aquí empezamos a ver las cosas asombrosas que hace en más de una dimensión.

<h2 id="vídeos-de-esta-clase-youtube">Vídeos de esta clase (YouTube)</h2>
<ul>
<li class="video-item">
<button type="button" class="video-play" data-vid="VkbtIDSHfSc" data-title="Clase 20: Interferencia, pompa de jabón">
<span class="video-play-icon">▶</span> <strong>Clase 20: Interferencia, pompa de jabón</strong>
</button>
<a class="video-ext" href="https://www.youtube.com/watch?v=VkbtIDSHfSc" target="_blank" rel="noopener">YouTube ↗</a>
</li>
<li class="video-item">
<button type="button" class="video-play" data-vid="mqhO9GT8hD4" data-title="Clase 21: Radar en fase, interferencia de un solo electrón">
<span class="video-play-icon">▶</span> <strong>Clase 21: Radar en fase, interferencia de un solo electrón</strong>
</button>
<a class="video-ext" href="https://www.youtube.com/watch?v=mqhO9GT8hD4" target="_blank" rel="noopener">YouTube ↗</a>
</li>
<li class="video-item">
<button type="button" class="video-play" data-vid="FY6iXM9X5Fo" data-title="Clase 22: Difracción, resolución">
<span class="video-play-icon">▶</span> <strong>Clase 22: Difracción, resolución</strong>
</button>
<a class="video-ext" href="https://www.youtube.com/watch?v=FY6iXM9X5Fo" target="_blank" rel="noopener">YouTube ↗</a>
</li>
</ul>

## Resumen previo

En este capítulo mostramos cómo los fenómenos de interferencia y difracción surgen de la física del problema de oscilación forzada y de las matemáticas de la transformación de Fourier.

i. Empezamos discutiendo la interferencia de una doble rendija. Este es el ejemplo clásico de interferencia. Damos una discusión heurística de la física y la generalizamos para obtener el resultado fundamental de la óptica de Fourier.

ii. Continuamos después nuestro análisis cuantitativo de la interferencia y la difracción discutiendo de nuevo el problema general como un problema de oscilación forzada. Mostramos la conexión con la formación de un haz. Hallamos la condición de contorno relevante en el infinito y expresamos la solución en forma de integral.

iii. Mostramos cómo la integral se simplifica en dos regiones extremas: muy cerca de la fuente del haz, donde de verdad parece un haz, y muy lejos, donde la difracción se impone y la intensidad de la onda está relacionada con una transformada de Fourier del patrón de onda en la fuente, el mismo resultado que encontramos en nuestra discusión heurística de la interferencia.

iv. Aplicamos estas técnicas a ejemplos con haces formados por una o más rendijas y por regiones rectangulares.

v. Demostramos un resultado útil, el teorema de convolución, para combinar transformadas de Fourier.

vi. Mostramos cómo los patrones periódicos dan lugar a patrones de difracción nítidos, y discutimos en detalle el ejemplo de la red de difracción.

vii. Aplicamos las mismas ideas al ejemplo tridimensional de la difracción de rayos X en cristales.

viii. Describimos un holograma como un patrón de difracción bastante complicado.

ix. Discutimos las franjas de interferencia y las placas zonales.

## 13.1 Interferencia

### 13.1.1 La doble rendija

La disposición clásica del experimento de la doble rendija se ilustra en la figura 13.1. Hay una pantalla opaca con dos rendijas estrechas en el plano $z = 0$ (mostrada en sección en el plano $x$-$z$; las rendijas salen del papel en la dirección $y$), separadas una pequeña distancia $s$. La pantalla opaca está iluminada por una fuente de luz «puntual». Podría ser, por ejemplo, una bombilla de vidrio transparente con un filtro de color para seleccionar un rango estrecho de frecuencias, muy lejos en la dirección $-z$. Un haz láser expandido con una lente serviría igual de bien. Lo importante es producir en la pantalla opaca una iluminación cuya frecuencia esté en un rango estrecho y en la que la fase de la luz que llega a las dos rendijas esté correlacionada. Eso será ciertamente así si la iluminación para $z < 0$ es casi una onda plana.

*(Figura 13.1: el experimento de la doble rendija.)*

Ahora ocurre algo interesante en la segunda pantalla, en $z = Z$. Esa «pantalla» podría ser una placa fotográfica, una pantalla translúcida o incluso su retina. Lo que aparece en ella es una serie de líneas brillantes paralelas en la dirección $y$ (paralelas a las rendijas). Si se tapa una de las rendijas, las líneas desaparecen.

Lo que está ocurriendo es interferencia entre los dos caminos rectilíneos posibles por los que la luz puede llegar a la pantalla. En esta sección daremos una discusión heurística y física de la interferencia. Después, en la sección siguiente, deduciremos el mismo resultado usando los argumentos de oscilación forzada y condiciones de contorno que ya conoce de nuestro estudio de las ondas unidimensionales.

La imagen física es esta. El campo eléctrico en $z = Z$ es la suma de los campos que vienen de las dos rendijas. En $x = 0$, en la disposición simétrica de la figura 13.1, los dos caminos posibles de la luz tienen la misma longitud. Por tanto, las dos componentes del campo tienen la misma fase y, en consecuencia, interfieren «constructivamente»: hay una línea brillante en $x = 0$. Al variar $x$, en $z = Z$, cambia la longitud relativa de los dos caminos. Obtenemos entonces posiciones alternas de interferencia constructiva y destructiva, lo que da lugar a las líneas brillantes.

Podemos entender el efecto cuantitativamente calculando explícitamente la longitud de camino. Considere un punto de la pantalla en $x = X$, como se muestra en la figura 13.2. La longitud de la línea de puntos de la figura 13.2 es

$$\sqrt{X^2 + Z^2}. \tag{13.1}$$

Para la rendija superior y la inferior, las longitudes de camino son ligeramente menor y mayor, respectivamente. La diferencia total de longitud de camino es

$$\Delta\ell = \sqrt{(X + s/2)^2 + Z^2} - \sqrt{(X - s/2)^2 + Z^2}. \tag{13.2}$$

Para $Z \gg s$, podemos desarrollar $\Delta\ell$ de (13.2) en serie de Taylor,

$$\Delta\ell \approx \frac{sX}{Z}. \tag{13.3}$$

*(Figura 13.2: longitudes de camino.)*

Por tanto, si el número de onda angular de la luz es $k$, la diferencia de fase entre los dos caminos es

$$\frac{ksX}{Z}. \tag{13.4}$$

Obtenemos un máximo de intensidad cada vez que la fase es un múltiplo de $2\pi$, es decir, cuando

$$\frac{ksX}{Z} = 2n\pi. \tag{13.5}$$

En términos de la longitud de onda, $\lambda = 2\pi/k$, esto es

$$\frac{X}{Z} = \frac{n\lambda}{s}. \tag{13.6}$$

### 13.1.2 Óptica de Fourier

Supongamos que, en vez de un simple patrón de dos rendijas, hay en la pantalla opaca algún patrón más complicado. En general, podemos describir la perturbación ondulatoria en el plano $z = 0$ mediante alguna función de $x$ e $y$:[^polariz]

$$f(x, y)\,e^{-i\omega t}. \tag{13.7}$$

[^polariz]: Estamos ignorando la polarización.

Nuestra estrategia consistirá en pensar en la onda producida para $z > 0$ por esta función general como una suma de los efectos de agujeros diminutos en todos los valores de $x$ e $y$ para los que $f(x, y)$ es no nula. Para cada trocito de la función podemos calcular la longitud de camino hasta un punto de la pantalla en $z = Z$. Después podemos sumar todos los trozos.

Supongamos, por simplicidad, que $f(x, y)$ solo es no nula en una región pequeña alrededor del origen, de modo que $x$ e $y$ serán pequeños,

$$|x|, |y| \ll |X|, |Y|, Z \tag{13.8}$$

para todos los valores relevantes de $x$ e $y$. Ahora bien, la longitud de camino desde el punto $(x, y, 0)$ de la pantalla en $z = 0$ hasta el punto $(X, Y, Z)$ de la pantalla en $z = Z$ es

$$\sqrt{(X - x)^2 + (Y - y)^2 + Z^2}. \tag{13.9}$$

Usando (13.8), podemos desarrollar esto como

$$R + \Delta\ell(x, y) + \cdots, \tag{13.10}$$

donde

$$R = \sqrt{X^2 + Y^2 + Z^2} \tag{13.11}$$

y

$$\Delta\ell(x, y) = -\frac{xX + yY}{R}. \tag{13.12}$$

Así, la onda en el camino de $(x, y, 0)$ a $(X, Y, Z)$ adquiere una fase de aproximadamente

$$e^{ik(R + \Delta\ell)}. \tag{13.13}$$

Ahora podemos volver a juntar las piezas de la onda para ver cómo funciona la interferencia en el punto $(X, Y, Z)$. Simplemente sumamos sobre todos los valores de $x$ e $y$, con un factor que es la fase por la función $f(x, y)$. Como $x$ e $y$ son variables continuas, la suma es en realidad una integral:

$$\int dx\int dy\, f(x, y)\,e^{ik(R + \Delta\ell)} = e^{ikR}\int dx\int dy\, f(x, y)\,e^{-i(xX + yY)k/R}. \tag{13.14}$$

Como veremos con más detalle abajo, esto es una transformada de Fourier bidimensional de la función $f(x, y)$.

La ecuación (13.14) es el resultado fundamental de la óptica de Fourier. Contiene buena parte de la física de la difracción. Hemos hecho al deducirla una serie de suposiciones que merecen más discusión. En la sección siguiente la deduciremos de otra manera, tratando la onda para $z > 0$ como el resultado de una oscilación forzada, producida por la onda en el plano $z = 0$. Eso nos dará una descripción física alternativa de la difracción. Pero será útil tener presente la imagen sencilla de sumar todos los caminos posibles conforme nos adentremos en los fenómenos de interferencia y difracción.

## 13.2 Haces

### 13.2.1 Formando un haz

Considere un sistema con una barrera opaca en el plano $z = 0$. Si se ilumina con una onda plana que viaja en la dirección $+z$, la barrera absorbe la onda por completo. Practique ahora un agujero en la barrera. Podría pensar que eso produciría un haz de luz viajando en la dirección de la onda plana inicial. Pero no es tan sencillo. Este es en realidad el mismo problema que consideramos en la sección anterior, (13.7)-(13.14), con la función $f(x, y)$ dada por

$$f(x, y) = \begin{cases} 1 & \text{dentro de la abertura} \\ 0 & \text{fuera de la abertura.} \end{cases} \tag{13.16}$$

De hecho, será útil pensar en el problema más general, porque la función (13.16) es discontinua. Como veremos más adelante, eso lleva a fenómenos de difracción más complicados que los que vemos con una función suave. En particular, supondremos que $f(x, y)$ es significativamente distinta de cero solo para $x$ e $y$ pequeños y tiende a cero para $x$ e $y$ grandes. Entonces podemos hablar de la posición de la «abertura» que produce el haz, cerca de $x = y = 0$.

Podemos pensar en este problema como un problema de oscilación forzada. Es mucho más fácil analizar la física si ignoramos la polarización, así que discutiremos ondas escalares. Podríamos considerar, por ejemplo, las ondas transversales de una membrana flexible o las ondas de presión en un gas. Equivalentemente, podríamos considerar ondas luminosas que dependen solo de dos dimensiones, $x$ y $z$, y polarizadas en la dirección $y$. No nos preocuparemos demasiado por estas sutilezas porque, como de costumbre, las propiedades básicas de los fenómenos ondulatorios están determinadas por propiedades de invariancia bajo traslación que son independientes de qué es lo que está ondulando.

### 13.2.2 Advertencias

Conviene señalar que hay otros enfoques del problema de la difracción además del que discutimos aquí. El montaje físico que estamos considerando es ligeramente distinto del planteamiento estándar de la difracción de Huygens-Fresnel-Kirchhoff, porque estamos estudiando un problema diferente. En la difracción de Huygens-Fresnel-Kirchhoff[^hecht] se considera la difracción de una onda plana por un objeto finito, mientras que nuestra pantalla opaca es infinita en el plano $x$-$y$. En el caso de Huygens-Fresnel, la condición de contorno apropiada es que no hay ondas esféricas entrantes que regresen desde el infinito hacia el objeto que difracta. La difracción produce únicamente ondas esféricas salientes. No discutiremos en detalle este montaje físico alternativo porque lleva más adentro de las funciones de Bessel de lo que nosotros (y probablemente también el lector) estamos dispuestos a ir. La ventaja de nuestra formulación es que podemos plantearla enteramente con las soluciones de onda plana que ya hemos discutido. Simplemente indicaremos las diferencias entre nuestro tratamiento y la difracción de Huygens-Fresnel. Para la difracción en la región frontal, a $z$ grande y no muy lejos del eje $z$, la difracción es la misma en ambos casos.

[^hecht]: Véase, por ejemplo, Hecht, capítulo 10.

El lector debería notar también que no hemos explicado exactamente cómo se produce la oscilación $f(x, y)\,e^{-i\omega t}$ en el plano $z = 0$. No es un problema trivial en absoluto, pero no lo discutiremos en detalle. Nos concentramos en la física para $z > 0$, que ya resultará bastante interesante.

### 13.2.3 El contorno en el infinito

Para determinar la forma de las ondas en la región $z > 0$ (más allá de la barrera) necesitamos condiciones de contorno tanto en $z = 0$ como en $z = \infty$. En $z = 0$ hay una amplitud oscilante dada por (13.15).[^contorno] En $z = \infty$ debemos imponer la condición de que no hay ondas viajando en la dirección $-z$ (de vuelta hacia la barrera) y de que las soluciones se comportan bien en $\infty$. Los modos normales tienen la forma

$$e^{i\vec{k}\cdot\vec{r} - i\omega t}$$

donde $\vec{k}$ satisface la relación de dispersión

$$\omega^2 = v^2\vec{k}^2. \tag{13.18}$$

[^contorno]: Nótese que, en una situación física real, las condiciones de contorno son a menudo mucho más complicadas que (13.16), porque la física del contorno importa. Sin embargo, eso suele significar que la difracción en una situación real es incluso mayor.

Así pues, dadas dos componentes de $\vec{k}$, podemos hallar la tercera usando (13.18). Por tanto, podemos escribir la solución como

$$\psi(\vec{r}, t) = \int dk_x\,dk_y\; C(k_x, k_y)\,e^{i\vec{k}\cdot\vec{r} - i\omega t} \qquad \text{para } z > 0 \tag{13.19}$$

donde

$$k_z = \sqrt{\omega^2/v^2 - k_x^2 - k_y^2}. \tag{13.20}$$

Nótese que (13.20) no determina el signo de $k_z$. Pero la condición de contorno en $\infty$ sí lo hace. Si $k_z$ es real, debe ser positivo para describir una onda que viaja hacia la derecha, alejándose de la barrera. Si $k_z$ es complejo, su parte imaginaria debe ser positiva; de lo contrario, $e^{i\vec{k}\cdot\vec{r}}$ se dispararía cuando $z$ tiende a $\infty$. Así,

$$\text{si } \operatorname{Im}k_z = 0,\ \text{entonces } \operatorname{Re}k_z > 0;\ \text{en caso contrario } \operatorname{Im}k_z > 0. \tag{13.21}$$

Discutimos el significado físico de la condición de contorno (13.21) en nuestra discusión del efecto túnel. Hay física real en la condición de contorno en el infinito. Considere, por ejemplo, la relación entre este análisis y la discusión de longitudes de camino de la sección anterior. En el lenguaje del último capítulo, no podemos describir los efectos de las ondas con $k_z$ imaginario. Sin embargo, la condición de contorno (13.21) garantiza que esas componentes de la onda tenderán a cero rápidamente para $z$ grande.

### 13.2.4 El contorno en $z = 0$

Todo lo que necesitamos para determinar la forma de la onda para $z > 0$ es hallar $C(k_x, k_y)$. Para ello implementamos la condición de contorno en $z = 0$ usando (13.19) y poniendo

$$\psi(\vec{r}, t)\big|_{z=0} = f(x, y)\,e^{-i\omega t} \tag{13.22}$$

para obtener (13.15). Sacando el factor común $e^{-i\omega t}$, esta condición es

$$f(x, y) = \int dk_x\,dk_y\; C(k_x, k_y)\,e^{i(k_x x + k_y y)}. \tag{13.23}$$

Si $f(x, y)$ se comporta bien en el infinito (como ciertamente ocurre si, como hemos supuesto, tiende a cero para $x$ e $y$ grandes), entonces solo pueden contribuir $k_x$ y $k_y$ reales en (13.23). Un $k_x$ complejo produciría una contribución que se dispararía o bien para $x \to +\infty$ o bien para $x \to -\infty$. Así, las integrales de (13.23) recorren $k$ real de $-\infty$ a $\infty$.

(13.23) es sencillamente una transformada de Fourier bidimensional. Usando argumentos análogos a los de nuestra discusión sobre señales, podemos invertirla para hallar $C$:

$$C(k_x, k_y) = \frac{1}{4\pi^2}\int dx\,dy\; f(x, y)\,e^{-i(k_x x + k_y y)}. \tag{13.24}$$

Insertar (13.24) en (13.19), con (13.20) y (13.21), da el resultado para la onda $\psi(\vec{r}, t)$ para $z > 0$. Este resultado es realmente muy general: vale para cualquier $f(x, y)$ razonable.

## 13.3 $z$ pequeña y $z$ grande

Pero ¿qué hacemos con él? La integral de (13.19) es demasiado complicada para hacerla analíticamente. Más abajo daremos algunos ejemplos de cómo funciona haciendo la integral numéricamente. Sin embargo, para $z$ pequeña y para $z$ grande, la integral se simplifica de maneras distintas.

### 13.3.1 $z$ pequeña

Para $z$ suficientemente pequeña esperaríamos, por razones físicas, haber producido realmente un haz y proyectado una imagen de la función $f(x, y)$. Para verlo explícitamente, usaremos el hecho de que, para una $f(x, y)$ concreta (y bien comportada), la transformada de Fourier $C(k_x, k_y)$ es una función que tiende a cero para

$$k \equiv \sqrt{k_x^2 + k_y^2} \gg 1/L \tag{13.25}$$

para algún $L$ mucho mayor que la longitud de onda. La distancia $L$ está determinada por la suavidad de $f(x, y)$. Típicamente, $L$ es el tamaño del detalle importante más pequeño de $f(x, y)$, la distancia más corta en la que $f(x, y)$ cambia apreciablemente. Vimos esto en nuestra discusión de las transformadas de Fourier en relación con las señales, en el capítulo 10. Veremos más ejemplos abajo. Podemos desarrollar $k_z z$ en el exponente en serie de Taylor:

$$k_z z = z\sqrt{\frac{\omega^2}{v^2} - k_x^2 - k_y^2} = \frac{z\omega}{v}\sqrt{1 - \frac{v^2(k_x^2 + k_y^2)}{\omega^2}} \approx \frac{z\omega}{v} - \frac{zv(k_x^2 + k_y^2)}{2\omega}. \tag{13.26}$$

Debido a (13.25), el mayor valor de $\sqrt{k_x^2 + k_y^2}$ que necesitamos en la integral (13.19) es del orden de $1/L$. Para valores mucho mayores, el integrando es cero. Así, el mayor valor posible del segundo término del desarrollo (13.26) que importa en la integral (13.19) es del orden de

$$\frac{zv}{2\omega L^2}. \tag{13.27}$$

Por tanto, si $L$ es finito y $z$ es pequeña ($\ll \omega L^2/v$), el segundo término es pequeño y podemos quedarnos solo con el primero, $z\omega/v$. Llevando esto de vuelta a la integral (13.19), tenemos

$$\psi(\vec{r}, t) \approx \int dk_x\,dk_y\, C(k_x, k_y)\,e^{i(k_x x + k_y y)}\,e^{i(z\omega/v - \omega t)} \approx f(x, y)\,e^{i\omega(z - vt)/v}. \tag{13.28}$$

Esto es justo lo que esperamos: un haz con la forma de la función original, propagándose en la dirección $z$ con velocidad $v$.

El resultado (13.28) empieza a fallar cuando el siguiente término de la serie de Taylor (13.26) se vuelve importante. Eso ocurre cuando

$$\frac{z\,v\,(k_x^2 + k_y^2)}{\omega} \approx 1.$$

Así,

$$z \approx \frac{\omega L^2}{v} = \frac{2\pi L^2}{\lambda} \tag{13.29}$$

marca la transición de un simple haz al comienzo de efectos de difracción importantes.

Si $L = 0$, que es la situación en el ejemplo de una rendija sencilla de anchura $2a$ que analizaremos en detalle más adelante, los efectos de difracción importantes empiezan de inmediato, porque la rendija tiene bordes afilados. Sin embargo, el haz mantiene cierta apariencia de su tamaño original hasta

$$z \approx \frac{\omega a^2}{v}.$$

Para $z$ mayor que $\omega L^2/v$, la dependencia en $k_x$ y $k_y$ del factor $e^{ik_z z}$ no puede ignorarse. En general, evaluar la integral (13.19) es muy difícil. Sin embargo, para $z$ muy grande, $z \gg L$, podemos usar un argumento físico para hallar el resultado de la integral.

### 13.3.2 $z$ grande

Supongamos que está muy lejos, en un punto $\vec{R} = (X, Y, Z)$, con

$$Z \gg \frac{\omega L^2}{v}. \tag{13.31}$$

Entonces no puede ver los detalles de la forma de la abertura, ni otros detalles de $f(x, y)$, sino solo su posición. La onda que detecta en algún punto lejano tiene que haber venido de la abertura y, si está suficientemente lejos, es casi una onda plana. A esto se le llama difracción de «Fraunhofer» o de «campo lejano». Si no se satisface esta condición, el problema se llama difracción de «Fresnel» o de «campo cercano». Para que la luz llegue efectivamente a su ojo en la situación de campo lejano, el vector de propagación debe apuntar de la abertura hacia usted. La situación se representa en el diagrama de la figura 13.3. En la región de campo cercano, el ensanchamiento debido a la difracción es del mismo orden que el tamaño de la abertura. Para $Z$ mucho mayor, en la región de campo lejano, el vector $\vec{k}$ debe apuntar de vuelta a la abertura.

*(Figura 13.3: el problema básico de la difracción — formar un haz.)*

Así pues, la única contribución a la integral (13.19) que cuenta es la proporcional a $e^{i\vec{k}\cdot\vec{R}}$, donde $\vec{k}$ apunta de la abertura a su ojo. Como el integrando de (13.19) tiene un factor $C(k_x, k_y)$, la amplitud de la onda es proporcional a $C(k_x, k_y)$, donde

$$(k_x, k_y, k_z) = \left(k_x, k_y, \sqrt{\omega^2/v^2 - k^2}\right) \propto (X, Y, Z). \tag{13.32}$$

La amplitud es además inversamente proporcional a

$$R = \sqrt{X^2 + Y^2 + Z^2}, \tag{13.33}$$

porque la intensidad debe decaer como $R^{-2}$, como en una onda esférica, por conservación de la energía. Hay otros factores que contribuyen a la variación de la amplitud además de $C(k_x, k_y)$ (veremos uno más abajo). Sin embargo, típicamente todos esos otros factores varían muy despacio y pueden ignorarse. Así, esperamos que la intensidad para $Z$ grande sea aproximadamente

$$I \propto \frac{|C(k_x, k_y)|^2}{R^2}, \tag{13.34}$$

donde $\vec{k}$ y $\vec{R}$ están relacionados por (13.32), lo que implica

$$\frac{k_x}{X} = \frac{k_y}{Y} = \frac{k_z}{Z} = \frac{k}{R} = \frac{\omega/v}{R} \tag{13.35}$$

o

$$k_x = \frac{kX}{R}, \qquad k_y = \frac{kY}{R}. \tag{13.36}$$

¡Y aquí está la clave! Insertando (13.36) en (13.24) se obtiene la integral de (13.14), la que salió de nuestro argumento físico sobre la interferencia. Así pues, nuestra descripción de la onda para $z > 0$ como un problema de oscilación forzada contiene el mismo factor que describe la interferencia de todos los caminos que la onda puede tomar desde la abertura hasta $\vec{R}$. La ventaja de nuestro enfoque actual es que es una deducción de verdad.

También podemos escribir este resultado en términos de ángulos:

$$\sin\theta_x = \frac{X}{R} = \frac{k_x v}{\omega}, \qquad \sin\theta_y = \frac{Y}{R} = \frac{k_y v}{\omega} \tag{13.37}$$

donde $\theta_x$ y $\theta_y$ son los ángulos del vector $\vec{r}$ respecto de la línea $X = Y = 0$ en las direcciones $x$ e $y$. O, equivalentemente,

$$X = \frac{Z\,k_x}{\sqrt{\omega^2/v^2 - k_x^2 - k_y^2}}, \qquad Y = \frac{Z\,k_y}{\sqrt{\omega^2/v^2 - k_x^2 - k_y^2}}. \tag{13.38}$$

Esto se ilustra en el diagrama de la figura 13.4.

*(Figura 13.4: relación entre el vector $\vec{k}$ y los ángulos.)*

### 13.3.3 * Fase estacionaria

Matemáticamente, (13.32) surge para $Z$ grande porque la fase de la exponencial de (13.19) varía muy rápidamente en función de $k_x$ y $k_y$, salvo para valores especiales de $k_x$ y $k_y$ en los que se anulan las derivadas de la fase respecto de $k_x$ y $k_y$. Si la función está centrada en $x = y = 0$ y es suave, las derivadas de $C(k_x, k_y)$ respecto de $k$ son del orden de $L$ y son irrelevantes. Así, la contribución viene de los $k_x$, $k_y$ tales que

$$\frac{\partial}{\partial k_x}\left(X k_x + Y k_y + Z\sqrt{\omega^2/v^2 - k_x^2 - k_y^2}\right) = X - \frac{Z\,k_x}{\sqrt{\omega^2/v^2 - k_x^2 - k_y^2}} = 0$$

$$\frac{\partial}{\partial k_y}\left(X k_x + Y k_y + Z\sqrt{\omega^2/v^2 - k_x^2 - k_y^2}\right) = Y - \frac{Z\,k_y}{\sqrt{\omega^2/v^2 - k_x^2 - k_y^2}} = 0$$

lo que equivale a (13.38). Una evaluación cuidadosa de la integral, teniendo en cuenta la dependencia en $k_x$ y $k_y$ en el entorno del valor crítico determinado por (13.38), da un factor adicional en la amplitud de la onda de

$$\frac{\cos\theta}{r}$$

donde $\theta$ es el ángulo del vector $\vec{r}$ con el eje $z$. Esperábamos el factor $1/r$ por el ensanchamiento de la onda difractada con la distancia. El factor $\cos\theta$ es en realidad el único sitio donde los detalles de la condición de contorno en el infinito, (13.21), entran en nuestra expresión para la onda difractada. Este factor garantiza que la onda difractada se anula al acercarnos a la superficie de la pantalla opaca lejos de la abertura. Es análogo al factor de «oblicuidad» $(1 + \cos\theta)/2$ de la teoría de difracción de Fresnel-Kirchhoff. La diferencia entre ambos se debe a las distintas condiciones de contorno (nuestra barrera plana infinita frente a la ausencia de ondas esféricas entrantes). Normalmente ignoraremos este factor y, de hecho, no suele suponer mucha diferencia allí donde la difracción es importante en la dirección frontal. Lo importante es que todo lo demás sobre la difracción en la región de campo lejano queda determinado únicamente por la linealidad, la invariancia bajo traslación y las interacciones locales.

### 13.3.4 Tamaño de la mancha

Una manera útil de pensar en la transición de la difracción de campo cercano (Fresnel) a la de campo lejano (Fraunhofer) es considerar el tamaño de la mancha formada por el haz de la figura 13.3 en función de $z$. Es una competición entre dos efectos. Aumentar el tamaño de la abertura hace la mancha más grande a $z$ pequeña. Sin embargo, disminuir el tamaño de la abertura aumenta la anchura en $k_x$, con lo que aumenta la difracción y la mancha se hace más grande a $z$ grande. Para un $z$ dado, lo mejor que puede hacer es elegir el tamaño de la abertura de modo que ambos efectos sean del mismo orden de magnitud. Suponga que el tamaño de su abertura es $\ell$. Entonces la anchura en $k_x$ es del orden de $2\pi/\ell$. A $z$ grande, el haz se abre en un cono con un ángulo de abertura del orden de

$$\theta \approx \frac{\lambda}{\ell}. \tag{13.40}$$

Así, cuando

$$\ell \approx \frac{\lambda z}{\ell}, \qquad \text{es decir} \qquad \ell \approx \sqrt{\lambda z}, \tag{13.41}$$

el ensanchamiento de la mancha por difracción es del mismo orden de magnitud que el tamaño de la abertura. Concluimos que, para minimizar el tamaño de la mancha a un $z$ dado, debe elegir una abertura de tamaño $\ell \approx \sqrt{\lambda z}$.

La relación (13.41), salvo factores de $\pi$, es lo que define la región de difracción de Fresnel en la figura 13.3. Otra manera de resumir el resultado de esta discusión es que, para

$$z \gg \frac{\ell^2}{\lambda},$$

el ensanchamiento debido a la difracción es mucho mayor que el debido al tamaño de la abertura. Esto define la región de campo lejano, o difracción de Fraunhofer.

### 13.3.5 Ángulos

¿Qué ocurre si la onda plana de (13.15) llega a la barrera opaca con un ángulo, en vez de de frente? Concretamente, suponga que el vector $\vec{k}$ de la onda forma un ángulo $\theta$ con la perpendicular en el plano $x$-$z$, de modo que

$$k_z = k\cos\theta, \qquad k_x = k\sin\theta.$$

Entonces es razonable suponer que el análogo de (13.15), la amplitud de la onda en el plano $z = 0$, es[^angulos]

$$f_\theta(x, y) = f(x, y)\,e^{ixk\sin\theta} \tag{13.46}$$

donde la dependencia adicional en $x$ se ha heredado simplemente de la dependencia en $x$ de la onda incidente.

[^angulos]: De nuevo, esto es simplista: ignora las complicaciones de los contornos igual que (13.15).

Podemos escribir la transformada de Fourier de $f_\theta$ en términos de la de $f$ como sigue:

$$f_\theta(x, y) = \int dk_x\,dk_y\, C(k_x, k_y)\,e^{i(k_x x + k_y y)}e^{ixk\sin\theta} = \int dk_x\,dk_y\, C(k_x - k\sin\theta, k_y)\,e^{i(k_x x + k_y y)},$$

lo que implica

$$C_\theta(k_x, k_y) = C(k_x - k\sin\theta, k_y). \tag{13.48}$$

Esto es enteramente razonable. Si el máximo de $C(k_x, k_y)$ ocurre en $k_x \approx 0$, el máximo de $C_\theta(k_x, k_y)$ ocurre en $k_x = k\sin\theta$. Así, el patrón de difracción aparece donde una línea que pasa por la abertura en la dirección de la onda plana incidente cruza la pantalla, justo como esperaríamos de un haz oblicuo.

## 13.4 Ejemplos

### 13.4.1 La rendija sencilla

Suponga

$$f(x, y) = \begin{cases} 1 & \text{para } -a \leq x \leq a \\ 0 & \text{para } |x| > a \end{cases} \tag{13.49}$$

independientemente de $y$. Este es en realidad un problema bidimensional, porque podemos mantener $k_y = 0$ e ignorarlo (salvo por un factor $2\pi$, del que no nos preocuparemos) eliminando la integral en $k_y$ de (13.19). Entonces (13.24) queda (con el $2\pi$ corregido para hacerlo unidimensional)[^sinc]

$$C(k_x) = \frac{1}{2\pi}\int dx\, f(x)\,e^{-ik_x x} = \frac{1}{2\pi}\int_{-a}^{a} dx\, e^{-ik_x x} = \left.\frac{e^{-ik_x x}}{-2i\pi k_x}\right|_{-a}^{a} = \frac{\sin k_x a}{\pi k_x}. \tag{13.51}$$

[^sinc]: Nótese que $\sin ka/k$ está bien definida ($= a$) en $k = 0$.

Así, esperamos que la intensidad de la onda a $z$ grande sea proporcional a $|C(k_x)|^2$, es decir,

$$I \propto \frac{\sin^2(k_x a)}{k_x^2}, \tag{13.52}$$

donde

$$\frac{k_x}{k} = \frac{x}{r} = \frac{k_x}{\omega/v} \qquad \text{o} \qquad k_x = \frac{\omega}{v}\frac{x}{r}. \tag{13.53}$$

Así, si medimos la intensidad del haz difractado a una distancia $r$ de la abertura, la intensidad va como sigue:[^angulopeq]

$$I \propto \frac{\sin^2(2\pi a x/r\lambda)}{x^2} \tag{13.54}$$

donde $\lambda$ es la longitud de onda de la luz. En la figura 13.5 se muestra $I$ en función de $x$.

[^angulopeq]: Aquí estamos suponiendo ángulos pequeños, de modo que $\sin\theta \approx \tan\theta$. En nuestra discusión de las redes de difracción, más abajo, veremos qué ocurre cuando la diferencia es importante.

Esto se llama un patrón de difracción. En el caso importante de la luz que pasa por una abertura pequeña, el patrón de difracción puede observarse fácilmente proyectando el haz difractado sobre una pantalla. Las características de este patrón que merece la pena señalar son el gran máximo en $x = 0$, con el doble de anchura que todos los demás máximos, y los ceros periódicos en $x = nr\lambda/2a$. Nótese también que, conforme la anchura $a$ de la rendija disminuye, el tamaño del patrón de difracción aumenta.

*(Figura 13.5: la intensidad del patrón de difracción en función de $x$.)*

**Moraleja:** esta relación inversa entre el tamaño de la rendija y el tamaño del patrón de difracción es otra ilustración de la propiedad general de las transformadas de Fourier discutida en el capítulo 10.

### 13.4.2 Difracción de campo cercano

Nos detendremos aquí para discutir la región de $z$ intermedia, la difracción de Fresnel, donde el problema de la difracción es complicado. Todo lo que podemos hacer es evaluar la integral (13.19) numéricamente, por ordenador, y hallar aproximadamente la intensidad a distintos valores de $z$. Suponga, por ejemplo, que tomamos

$$\frac{\omega a}{c} = \frac{2\pi a}{\lambda} = 200,$$

que corresponde a una rendija bastante pequeña, con una anchura de solo $100/\pi \approx 32$ veces la longitud de onda de la onda. Usaremos entonces (13.19) para calcular la intensidad de la onda a distintos valores de $z$, en unidades de $a$. Para $z$ pequeña, el resultado se muestra en la figura 13.6. Puede verse que la forma básica del haz se mantiene durante un tiempo, como esperábamos de (13.28). Sin embargo, aparecen ondulaciones de inmediato. La difracción ondulante bastante grande se debe a los bordes afilados. Más abajo daremos otro ejemplo en el que la difracción es mucho más suave. Para $z$ intermedia, mostrada en la figura 13.7, las ondulaciones empiezan a fundirse y a cambiar drásticamente la forma global del haz. Al mismo tiempo, el haz empieza a ensancharse.

*(Figura 13.6: la intensidad de una onda que pasa por una rendija, para $z$ pequeña.)*

*(Figura 13.7: la intensidad de una onda que pasa por una rendija, para $z$ intermedia.)*

Por último, en la figura 13.8 mostramos la aproximación a la región de $z$ grande, donde la difracción se impone por completo y aparece el patrón de difracción de campo lejano, (13.54).

*(Figura 13.8: la intensidad de una onda que pasa por una rendija, conforme $z$ se hace grande.)*

Puede resultar interesante un ejemplo más. Suponga que, en vez de ser un simple agujero en la pantalla opaca, la abertura está sombreada de tal manera que la perturbación ondulatoria en $z = 0$ tiene la forma

$$f(x, y) = e^{-|x|/a}. \tag{13.56}$$

La transformada de Fourier se hizo en el capítulo 10, en (10.49)-(10.56). Sustituyendo $\omega \to k_x$ y $\Gamma \to 1/a$ en (10.56) se obtiene

$$C(k_x) = \frac{1}{\pi}\frac{a}{1 + a^2 k_x^2}. \tag{13.57}$$

Esto determina la distribución de intensidad a $z$ grande. Sin embargo, a diferencia del ejemplo anterior, este patrón da una difracción muy suave. Para $z$ pequeña, el patrón de intensidad se muestra en la figura 13.9. El pico agudo de (13.56) desaparece, pero por lo demás el cambio es muy gradual, porque el patrón inicial es muy suave excepto en $x = 0$. Para $z$ intermedia y grande, los patrones de intensidad se muestran en las figuras 13.10 y 13.11.

*(Figura 13.9: la distribución de intensidad de (13.56) para $z$ pequeña.)*

*(Figura 13.10: la distribución de intensidad de (13.56) para $z$ intermedia.)*

*(Figura 13.11: la distribución de intensidad de (13.56) para $z$ grande.)*

### 13.4.3 El rectángulo

Suponga

$$f(x, y) = \begin{cases} 1 & \text{para } -a_x \leq x \leq a_x \text{ y } -a_y \leq y \leq a_y, \\ 0 & \text{en caso contrario.} \end{cases} \tag{13.58}$$

Este es el producto de un patrón de rendija sencilla en $x$ por un patrón de rendija sencilla en $y$. La transformada de Fourier es el producto de las transformadas de Fourier unidimensionales:

$$C(k_x, k_y) = \frac{1}{4\pi^2}\int_{-a_x}^{a_x} dx\, e^{-ik_x x}\int_{-a_y}^{a_y} dy\, e^{-ik_y y} = \frac{\sin(k_x a_x)}{\pi k_x}\frac{\sin(k_y a_y)}{\pi k_y}. \tag{13.59}$$

Así, la intensidad se parece aproximadamente a

$$I \propto \frac{\sin^2(2\pi a_x x/r\lambda)}{x^2}\frac{\sin^2(2\pi a_y y/r\lambda)}{y^2}. \tag{13.60}$$

Por supuesto, una vez más, por las propiedades generales de la transformada de Fourier, si el rectángulo es estrecho en $x$, el patrón de difracción se ensancha en $k_x$, y análogamente para $y$.

### 13.4.4 «Funciones» $\delta$

Conforme la rendija de (13.49) se estrecha, el patrón de difracción se ensancha. Por supuesto, la intensidad también disminuye. La intensidad en $k_x = 0$ está relacionada con la transformada de Fourier de $f$ en cero, que es simplemente la integral de $f$ sobre todo $x$. Conforme la rendija se estrecha, esa integral disminuye. Pero suponga que aumentamos la intensidad del haz incidente, conforme $a$ disminuye, para mantener fija la intensidad del máximo del patrón de difracción. Ignorando la dependencia en $y$, exigimos

$$f_a(x) = \begin{cases} \dfrac{1}{2a} & \text{para } -a \leq x \leq a, \\[6pt] 0 & \text{para } |x| > a. \end{cases} \tag{13.61}$$

El límite de $f_a$ cuando $a \to 0$ no existe realmente como función. Es cero en todas partes salvo en $x = 0$. Pero tiende a $\infty$ muy deprisa en $x = 0$, de modo que

$$\lim_{a \to 0}\int dx\, f_a(x) = 1. \tag{13.62}$$

Resulta extraordinariamente cómodo inventar un objeto con estas propiedades, llamado «función $\delta$». Es decir, $\delta(x)$ tiene la propiedad de ser cero salvo en $x = 0$, y de que

$$\int dx\,\delta(x) = 1. \tag{13.63}$$

De hecho, este objeto tiene una especie de sentido matemático, siempre que no se eleve al cuadrado. Las funciones $\delta$ pueden manipularse como funciones ordinarias, sumarse, multiplicarse por constantes o por funciones suaves —incluso pueden multiplicarse funciones $\delta$ de variables distintas—; ¡solo hay que evitar elevarlas al cuadrado! Por ejemplo, una función delta puede multiplicarse por una función continua ordinaria:

$$f(x)\,\delta(x) = f(0)\,\delta(x) \tag{13.64}$$

donde la igualdad se sigue de que la función delta se anula salvo en $x = 0$, de modo que solo importa el valor de $f$ en 0.

Ahora debería estar claro, de (13.63) y (13.64), que la transformada de Fourier de $\delta(x)$ es simplemente una constante:

$$\frac{1}{2\pi}\int dx\, e^{-ikx}\,\delta(x) = \frac{1}{2\pi}. \tag{13.65}$$

El patrón de difracción de esta cosa es, por tanto, muy aburrido: hay iluminación uniforme en todos los ángulos.

Por supuesto, en física no podemos fabricar funciones $\delta$. Sin embargo, si $a$, en (13.61), es mucho menor que la longitud de onda de la onda, entonces bien podría ser una función $\delta$, porque solo importa cuánto vale $C(k_x)$ para $k_x < k = 2\pi/\lambda$. Los $k_x$ mayores corresponden a ondas exponenciales que se extinguen rápidamente con $z$. Pero para tales $k_x$, el producto $k_x a$ es muy pequeño, así que

$$C(k_x) = \frac{1}{2\pi}\frac{\sin k_x a}{k_x a} \approx \frac{1}{2\pi}\left(1 - \frac{(k_x a)^2}{6} + \cdots\right) \approx \frac{1}{2\pi} \tag{13.66}$$

y seguimos obteniendo difracción uniforme en todos los ángulos.

**Moraleja:** las funciones $\delta$ son simplemente una comodidad. Cuando los físicos hablan de una función $\delta$, quieren decir (o al menos deberían querer decir) una función como $f_a(x)$, donde $a$ es menor que cualquier distancia física que importe en el problema. Una vez que $a$ se hace así de pequeña, a menudo es más fácil seguir la pista de las matemáticas si se va hasta el límite no físico, $a = 0$.

### 13.4.5 Algunas propiedades de las funciones $\delta$

La transformada de Fourier de una función $\delta$ es una exponencial compleja:

$$\text{si } f(x) = \delta(x - a), \text{ entonces } C(k) = \frac{1}{2\pi}e^{-ika}. \tag{13.67}$$

La transformada de Fourier de una exponencial compleja es una función $\delta$:

$$\text{si } f(x) = e^{-i\ell x}, \text{ entonces } C(k) = \delta(k - \ell). \tag{13.68}$$

Se puede llegar a una función $\delta$ como límite de diversas maneras. Por ejemplo, de (13.68) esperaríamos que, cuando $a \to \infty$, la transformada de Fourier de (13.49) se aproximara a una función $\delta$:

$$\lim_{a \to \infty}\frac{\sin k_x a}{\pi k_x} = \delta(k_x). \tag{13.69}$$

### 13.4.6 Una dimensión a partir de dos

Usando funciones $\delta$ podemos decir con más elegancia qué se quiere decir con la afirmación que hicimos antes de que, si $f(x, y)$ no depende de $y$, el problema es unidimensional. Si miramos el límite de (13.58) cuando $a_y \to \infty$, pasa a (13.49). Dicho de otro modo, cuando un rectángulo es infinitamente largo, es una rendija. En este límite, la transformada de Fourier (13.59) pasa a

$$C(k_x, k_y) = \frac{\sin(k_x a_x)}{\pi k_x}\,\delta(k_y). \tag{13.70}$$

Este es el significado real de (13.50). Es unidimensional en el sentido de que $k_y$ está fijado en 0. No hay difracción en la dirección $y$.

### 13.4.7 Muchas rendijas estrechas

Una aplicación interesante de las funciones $\delta$ es el patrón de difracción de varias rendijas estrechas. Lo usaremos después de varias maneras. Considere una función $f(x, y)$ de la forma

$$f(x, y) = \sum_{j=0}^{n-1}\delta(x - jb). \tag{13.71}$$

Esto describe una serie de $n$ rendijas estrechas[^estrechas] en $x = 0$, $x = b$, $x = 2b$, etc., hasta $x = (n-1)b$.

[^estrechas]: «Estrechas» significa aquí estrechas comparadas con la longitud de onda de la luz; véase la moraleja anterior.

La transformada de Fourier de (13.71) es una suma de contribuciones de las funciones $\delta$ individuales; de (13.67) y (13.68),

$$C(k_x, k_y) = \delta(k_y)\sum_{j=0}^{n-1} e^{-ijbk_x}. \tag{13.72}$$

Pero la suma es una serie geométrica que puede hacerse explícitamente:

$$\sum_{j=0}^{n-1} e^{-ijbk_x} = \frac{1 - e^{-inbk_x}}{1 - e^{-ibk_x}} = \frac{e^{-inbk_x/2}\left(e^{inbk_x/2} - e^{-inbk_x/2}\right)}{e^{-ibk_x/2}\left(e^{ibk_x/2} - e^{-ibk_x/2}\right)} = e^{-i(n-1)bk_x/2}\,\frac{\sin nbk_x/2}{\sin bk_x/2}. \tag{13.73}$$

Así, la intensidad del patrón de difracción es proporcional a

$$\frac{\sin^2 nbk_x/2}{\sin^2 bk_x/2}. \tag{13.74}$$

Para $n = 2$, (13.74) es simplemente

$$4\cos^2\frac{bk_x}{2} = 2(1 + \cos bk_x). \tag{13.75}$$

Este es el problema con el que empezamos el capítulo. Cuando $bk_x = 2m\pi$ para $m$ entero, la onda de una rendija recorre más camino que la de la otra en $m\lambda$, donde $\lambda = 2\pi/k$ es la longitud de onda. Así, para $bk_x = 2m\pi$ la interferencia es constructiva, como se ilustra en la figura 13.12.

*(Figura 13.12: si $bk_x/k = n\lambda$, la interferencia es constructiva.)*

Para $n$ mayor seguimos obteniendo interferencia constructiva para $bk_x = 2m\pi$, pero los máximos son más agudos, porque con más rendijas hay más posibilidades de interferencia destructiva en otros ángulos. En las figuras 13.13 y 13.14 representamos (13.74) frente a $bk_x$ (de $-\pi$ a $3\pi$, para que pueda ver dos periodos completos) para $n = 3$ y 6. Nótese la aparición de $n - 2$ máximos secundarios entre los máximos principales de la intensidad. Volveremos a estas relaciones cuando discutamos las redes de difracción.

*(Figura 13.13: el patrón de difracción de tres rendijas estrechas.)*

*(Figura 13.14: el patrón de difracción de 6 rendijas estrechas.)*

## 13.5 Convolución

Hay un teorema bastante sencillo, conocido como teorema de convolución, que resulta extremadamente útil al tratar con transformadas de Fourier. Suponga que tenemos dos funciones, $f_1(x)$ y $f_2(x)$. Definimos la función $f_1 \circ f_2$ como sigue:

$$f_1 \circ f_2(x) = \int dy\, f_1(x - y)\,f_2(y). \tag{13.76}$$

Esta integral estará bien definida si $f_1(x)$ y $f_2(x)$ decaen suficientemente deprisa en el infinito (y desde luego si son no nulas solo en una región finita de $x$). Nótese que $f_1 \circ f_2$ es una función de una sola variable. Es además simétrica bajo el intercambio de las dos funciones, porque mediante un simple cambio de variables ($y \to x - y$)

$$f_1 \circ f_2(x) = \int dy\, f_1(x - y)\,f_2(y) = \int dy\, f_1(y)\,f_2(x - y) = f_2 \circ f_1(x). \tag{13.77}$$

Ahora el teorema dice que la transformada de Fourier de la convolución es $2\pi$ veces el producto de las transformadas de Fourier de las dos funciones. La demostración es inmediata (todas las integrales van de $-\infty$ a $\infty$):

$$C_{f_1 \circ f_2}(k) = \frac{1}{2\pi}\int dx\, e^{ikx}\, f_1 \circ f_2(x) = \frac{1}{2\pi}\int dx\, e^{ikx}\int dy\, f_1(x - y)\,f_2(y). \tag{13.78}$$

Ahora sustituimos $x \to y + z$ y escribimos la integral sobre $y$ y $z$:

$$= \frac{1}{2\pi}\int dz\int dy\, e^{ik(y+z)} f_1(z)\,f_2(y) = 2\pi\,C_{f_1}(k)\,C_{f_2}(k). \tag{13.79}$$

La versión bidimensional de (13.79) es una extensión directa. La convolución bidimensional es

$$f_1 \circ f_2(x, y) = \int dx'\,dy'\, f_1(x - x', y - y')\,f_2(x', y') \tag{13.80}$$

y

$$C_{f_1 \circ f_2}(k_x, k_y) = 4\pi^2\,C_{f_1}(k_x, k_y)\,C_{f_2}(k_x, k_y). \tag{13.81}$$

### 13.5.1 Patrones repetidos

El teorema de convolución puede usarse para entender muchas situaciones interesantes. Considere el siguiente patrón, muy instructivo, de dos rendijas anchas:

$$f(x, y) = \begin{cases} 1 & \text{para } -a \leq x \leq a \\ 1 & \text{para } -a \leq x - b \leq a \\ 0 & \text{en caso contrario} \end{cases} \tag{13.82}$$

para $b > 2a$. En la figura 13.15 se muestra un fragmento del patrón para $b = 3.5a$.

*(Figura 13.15: un fragmento de la barrera opaca con dos rendijas anchas.)*

Esto puede considerarse la convolución de dos funciones, $f = f_1 \circ f_2$, donde

$$f_1(x, y) = \begin{cases} 1 & \text{para } -a \leq x \leq a \\ 0 & \text{en caso contrario} \end{cases} \tag{13.84}$$

y

$$f_2(x, y) = \delta(x)\,\delta(y) + \delta(x - b)\,\delta(y). \tag{13.85}$$

Las transformadas de Fourier correspondientes son, de (13.70),

$$C_{f_1}(k_x, k_y) = \frac{\sin(k_x a)}{\pi k_x}\,\delta(k_y) \tag{13.86}$$

y, de (13.73),

$$C_{f_2}(k_x, k_y) = \frac{1}{4\pi^2}\,e^{-ibk_x/2}\,\cos\frac{bk_x}{2}\cdot 2. \tag{13.87}$$

Aplicando ahora el teorema de convolución se obtiene

$$C_{f_1 \circ f_2}(k_x, k_y) = \cos\frac{bk_x}{2}\;e^{-ibk_x/2}\;\frac{\sin(k_x a)}{\pi k_x}\;\delta(k_y). \tag{13.88}$$

Como $b > 2a$, esto describe un patrón que oscila rápidamente en la escala fijada por $1/b$, con una amplitud que varía siguiendo el patrón de difracción de una sola rendija caracterizado por el tamaño $1/a$. El patrón de intensidad sobre una pantalla lejana se muestra en la figura 13.16, para $b = 3.5a$. La línea de puntos es el patrón de una sola rendija ancha (compárese con (13.5)).

*(Figura 13.16: el patrón de difracción de dos rendijas anchas.)*

## 13.6 $f(x, y)$ periódica

Suponga que $f(x, y)$ es periódica en $x$ con periodo $a$, es decir,

$$f(x + a, y) = f(x, y). \tag{13.89}$$

Entonces $C(k_x, k_y)$ solo puede ser no nula si

$$k_x = \frac{2\pi n}{a}. \tag{13.90}$$

Para verlo, inserte (13.89) en (13.24):

$$C(k_x, k_y) = \frac{1}{4\pi^2}\int dx\,dy\, f(x + a, y)\,e^{i(k_x x + k_y y)}. \tag{13.91}$$

Si cambiamos de variable $x \to x - a$, (13.91) es

$$C(k_x, k_y) = \frac{1}{4\pi^2}\int dx\,dy\, f(x, y)\,e^{i(k_x x - k_x a + k_y y)} = e^{-ik_x a}\,C(k_x, k_y) \tag{13.92}$$

porque el factor de fase constante puede sacarse fuera de la integral. (13.90) se sigue porque (13.92) implica que, o bien $C(k_x, k_y) = 0$, o bien $e^{-ik_x a} = 1$.

Un ejemplo de este principio general es (13.74). En el límite $n \to \infty$, (13.74) tiende a 0 salvo para $k_x = 2\pi m/b$ con $m$ entero (donde es infinita). Este ejemplo es sencillo porque las rendijas son estrechas, de modo que la intensidad es independiente de $m$. Sin embargo, con rendijas anchas repetidas, o con algún patrón más complicado, podríamos usar el teorema de convolución y (13.74) para ver que (13.90) emerge cuando $n \to \infty$. Los detalles del patrón de cada rendija determinan entonces la intensidad relativa del patrón de difracción para los distintos $m$.

Así, cualquier patrón regular infinito produce una sucesión discreta de $k$. Por ejemplo, una red de difracción por transmisión, que consiste en muchas líneas igualmente espaciadas en la dirección $y$ con separación $a$ en $x$ sobre un sustrato transparente, produce un $C(k_x, k_y)$ que solo es no nulo para $k_y = 0$ (porque no hay dependencia alguna en $y$) y $k_x = 2n\pi/a$. Entonces (13.19) queda

$$\psi \propto \sum_n C_n\, e^{i\left(2n\pi x/a + z\sqrt{\omega^2/v^2 - (2n\pi/a)^2} - \omega t\right)}. \tag{13.93}$$

Esto describe una superposición lineal de ondas planas que se abren en abanico con ángulos en la dirección $x$ dados por

$$\sin\theta_n = \frac{2\pi n v}{a\omega} = \frac{n\lambda}{a} \tag{13.94}$$

como se muestra en la figura 13.17.

*(Figura 13.17: una red de difracción por transmisión desdobla un haz de una sola frecuencia.)*

Típicamente, en una red de transmisión la mayor parte de la luz va a la línea central, lo que equivale a decir que se puede ver a través de la red. Nótese que el espaciado uniforme en $\sin\theta_n$ de (13.94) corresponde a un espaciado creciente de las líneas proyectadas sobre una pantalla a $z$ grande fijo (por ejemplo, ¡una pantalla como su retina!), porque la distancia a lo largo de la pantalla está determinada por

$$\tan\theta_n = \frac{n\lambda/a}{\sqrt{1 - n^2\lambda^2/a^2}}. \tag{13.95}$$

Hay un valor máximo de $n$ por encima del cual no se produce onda propagante (porque corresponde a $\sin\theta > 1$ y, por tanto, a $k_z$ imaginario).

Nótese también la dependencia de (13.94) con la longitud de onda. Cuanto mayor es la longitud de onda de la luz, mayores son los ángulos del patrón de la red de difracción. Esto es, por supuesto, lo que hace útil a la red de difracción: puede separar luz de frecuencias distintas. Los distintos colores del arcoíris se despliegan a lo largo de una línea, para cada valor de $n$. Esto se ilustra en la figura 13.18 para tres frecuencias: luz azul de longitud de onda 4300 Å, luz verde de 5200 Å y luz roja de 6300 Å, incidiendo sobre una red de difracción de 10 000 líneas por pulgada. Hemos representado (13.95) para $n = -3$ a 3 y etiquetado los colores del máximo secundario $n = 1$. Como puede ver, en una red realista los ángulos de difracción pueden ser grandes, y es muy mala idea usar una aproximación de ángulos pequeños.

*(Figura 13.18: el patrón de tres frecuencias de luz producido por una red.)*

### 13.6.1 Girando la red

Algunos ejemplos interesantes de los efectos discutidos en (13.48) se dan cuando la onda luminosa incidente llega a la red formando un ángulo con la perpendicular. Partiendo de las líneas de la red en la dirección $y$ y de la red en el plano $x$-$y$, hay dos efectos distintos.

**1: giro alrededor del eje $y$.** Suponga que la luz llega con un ángulo $\theta_{in}$ respecto de la perpendicular en el plano $x$-$z$. Entonces, de (13.48),

$$C_{\theta_{in}}(k_x, k_y) = C(k_x - k\sin\theta_{in}, k_y)$$

donde $C$ es la transformada de Fourier de la red perpendicular,

$$C(k_x, k_y) \neq 0 \quad \text{para } k_y = 0,\ k_x = \frac{2\pi n}{a}.$$

Así,

$$C_{\theta_{in}}(k_x, k_y) \neq 0 \quad \text{para } k_y = 0,\ k_x = k\sin\theta_{in} + \frac{2\pi n}{a}$$

o

$$\sin\theta = \frac{k_x}{k} = \sin\theta_{in} + \frac{n\lambda}{a}. \tag{13.99}$$

Dicho de otro modo, $\sin\theta$ simplemente se desplaza en $\sin\theta_{in}$. Esto significa, por ejemplo, que si $\sin\theta_{in} = \lambda/a$, el patrón es exactamente el mismo, pero el máximo central se ha desplazado, como se muestra en la figura 13.19.

*(Figura 13.19: el patrón para un haz que llega con un ángulo $\theta_{in} = \arcsin\lambda/a$.)*

**2: giro alrededor del eje $x$.** Suponga que la luz llega con un ángulo $\theta_{in}$ respecto de la perpendicular en el plano $y$-$z$. Entonces, de (13.48),

$$C_{\theta_{in}}(k_x, k_y) = C(k_x, k_y - k\sin\theta_{in}).$$

Ahora, en vez de ser 0, $k_y$ está fijado en $k\sin\theta_{in}$:

$$k_y = k\sin\theta_{in}, \qquad k_x = \frac{2\pi n}{a}.$$

Ahora las ondas difractadas forman ángulos no triviales con la perpendicular tanto en $x$ como en $y$:

$$\sin\theta_y = \frac{k_y}{\sqrt{k_y^2 + k_z^2}} = \frac{\sin\theta_{in}}{\sqrt{1 - n^2\lambda^2/a^2}} \tag{13.101}$$

y

$$\sin\theta_x = \frac{k_x}{\sqrt{k_x^2 + k_z^2}} = \frac{n\lambda}{a\cos\theta_{in}}. \tag{13.102}$$

De nuevo, como en (13.95), lo que vemos si proyectamos el patrón sobre una pantalla perpendicular a $z$ fijo son las tangentes,

$$(x, y)_{\text{pantalla}} = z\,(\tan\theta_x, \tan\theta_y), \tag{13.103}$$

donde

$$\tan\theta_x = \frac{k_x}{k_z}, \qquad \tan\theta_y = \frac{k_y}{k_z}.$$

Así, el patrón de difracción aparece curvado. Lo que se ve en una pantalla o en la retina son los colores del arcoíris desplegados a lo largo de una línea curva. Esto se muestra en la figura 13.20, donde representamos $\tan\theta_x$ frente a $\tan\theta_y$ para una fuente de luz y una red como las de la figura 13.18, pero con $\sin\theta_{in} = 0.5$. Nótese que el patrón no solo se ha curvado: también se ha ensanchado respecto del de la figura 13.18. Aquí se ve realmente el vector $\vec{k}$ tridimensional en acción. Conforme $\tan\theta_y$ aumenta, para $k_x$ fijo, $\tan\theta_x$ aumenta también, porque $k_z$ disminuye.

*(Figura 13.20: el patrón de difracción de una red girada.)*

### 13.6.2 Poder de resolución

La discusión hasta aquí ha supuesto que la red de difracción es verdaderamente periódica. Pero eso solo es posible si la red es infinita. En una red finita, solo la parte central es periódica: los bordes rompen la periodicidad. En una red que consta solo de un número finito de surcos, $n$, los picos de difracción no son infinitamente agudos: no son funciones delta. Sin embargo, como se discutió al principio de esta sección, en realidad ya sabemos qué aspecto tienen en el caso finito, porque hemos resuelto el problema de la difracción por $n$ rendijas estrechas igualmente espaciadas, en (13.74). En la situación general de $n$ surcos idénticos, la intensidad se parece a (13.74) multiplicada por alguna función que varía lentamente y que depende de la forma de los surcos (por el teorema de convolución, (13.79)). La consecuencia importante de esto es que la forma de un pico de difracción para una red de $n$ rendijas viene dada aproximadamente por (13.74).

La forma del pico de difracción es importante por la siguiente cuestión práctica. Suponga que tiene un haz de luz que consta de una superposición de luz de dos frecuencias distintas. ¿Cómo de próximas tienen que estar las frecuencias para que sus picos de difracción no triviales se fundan, de modo que no pueda usar su red de difracción para distinguirlas? Cuanto mayor es el número de surcos de la red, más agudos son los picos de difracción y más fácil resulta distinguir frecuencias distintas.

El criterio de Rayleigh es una manera históricamente importante de responder a esta pregunta. Rayleigh supuso que sería posible distinguir los máximos de difracción de ondas igualmente intensas de longitudes de onda ligeramente distintas si el máximo de una frecuencia coincide con el primer mínimo de la otra. Para una red de 6 líneas, este criterio se ilustra en la figura 13.21. La línea continua es la intensidad total de una onda formada por dos frecuencias ligeramente distintas. Las contribuciones de las componentes de frecuencia separadas se indican con las líneas de puntos y de trazos.

*(Figura 13.21: el criterio de Rayleigh para una red de 6 líneas.)*

Cualquier criterio fijo de este tipo para el poder de resolución no debería considerarse un hecho sobre la naturaleza, sino una definición convencional que facilita la comunicación entre experimentadores. Siempre es posible hacerlo mejor que cualquier definición dada acumulando datos precisos sobre la forma de la línea y modelando los detalles.

### 13.6.3 Redes «blazed» (con surcos inclinados)

Como espectroscopio, la red de difracción por transmisión tiene una desventaja frente a un prisma. La dificultad está en que, como señalamos antes, la mayor parte de la luz que incide sobre la red la atraviesa directamente y no se separa en sus frecuencias componentes. Es un problema muy serio en dispositivos en los que la cantidad total de luz es limitada. A menudo es importante que el grueso de la luz vaya a un único valor no nulo de $n$ en (13.94). Entonces casi todos los fotones pueden aprovecharse para la medida, en vez de desperdiciarse en el máximo $n = 0$ (que no lleva información sobre la frecuencia). Como argumentamos antes, no hay ninguna razón teórica por la que no pueda hacerse tal cosa: los principios generales de invariancia bajo traslación e interacciones locales determinan los ángulos de difracción posibles, pero no cuánta luz va a cada ángulo.

De hecho, existe un método práctico y muy usado en las redes de reflexión. Una superficie reflectante con una serie de líneas paralelas igualmente espaciadas grabadas en ella actúa como una red de reflexión, como se ilustra en la figura 13.22. Ahí se muestra una red de reflexión en la que la reflexión predominante de un haz que llega perpendicular al plano de la red es también perpendicular. Lo que queremos, en cambio, es lo que se muestra en la figura 13.23. Para construir una red así, se puede dar forma a los surcos de la red de modo que la reflexión especular en cada surco dirija el haz hacia el máximo de difracción no trivial, como se muestra en la figura 13.24.

*(Figura 13.22: una red de difracción por reflexión desdobla un haz de una sola frecuencia.)*

*(Figura 13.23: una red «blazed» dirige el haz hacia un máximo de difracción no trivial.)*

*(Figura 13.24: los surcos de una red «blazed».)*

Para hacer esto, se puede elegir el ángulo del «blaze» como la mitad del ángulo del primer máximo, $\theta_1 = 2\pi v/a\omega$, en (13.94), como se muestra en la ampliación de un surco de la figura 13.25.

*(Figura 13.25: $\theta \approx \theta_1/2$.)*

## 13.7 * Difracción de rayos X

Un hermoso ejemplo tridimensional de difracción por una función periódica es la difracción de rayos X en cristales. Un cristal es una disposición regular de átomos cuyas posiciones pueden describirse mediante una función periódica

$$f(\vec{r}) = f(\vec{r} + \vec{a}) \tag{13.106}$$

donde $\vec{a}$ es cualquier vector que va de un punto de la red a otro. Matemáticamente, podemos definir la red como el conjunto de todos esos vectores. Nótese que la red incluye siempre el vector cero, el punto en el origen. La transformada de Fourier tridimensional de $f(\vec{r})$ es no nula solo para vectores de número de onda de la forma

$$2\pi\sum_j n_j\,\vec{\ell}_j \tag{13.107}$$

donde $\vec{\ell}_j$ son los vectores base de la red «dual» o «recíproca», que satisface

$$\vec{a}\cdot\vec{\ell}_j = \text{entero, para todo } \vec{a}. \tag{13.108}$$

La idea aquí es la misma que en la discusión unidimensional de la red de difracción, $k_x = 2\pi n/a$, (13.90). La deducción de (13.107) es precisamente análoga a la de (13.90).

Podemos visualizar la relación entre la red y la red dual más fácilmente para «cristales» bidimensionales. Considere, por ejemplo, una red de la forma

$$\vec{a} = n_x a_x\,\hat{x} + n_y a_y\,\hat{y} \tag{13.109}$$

mostrada en la figura 13.26 (para $a_x = 2a_y$).

*(Figura 13.26: una red cristalina.)*

Está claro que los vectores de la forma

$$\vec{\ell}_1 = \frac{1}{a_x}\hat{x}, \qquad \vec{\ell}_2 = \frac{1}{a_y}\hat{y} \tag{13.110}$$

satisfacen (13.108). Además, pensándolo un poco se convencerá de que son el par más corto de vectores linealmente independientes con esa propiedad. Así, podemos tomar (13.110) como los vectores base de la red dual, de modo que la red dual tiene el aspecto

$$\vec{d}_m = \frac{m_x}{a_x}\hat{x} + \frac{m_y}{a_y}\hat{y} \tag{13.111}$$

como se muestra en la figura 13.27. Nótese que los ejes largo y corto se intercambian, como es habitual en un proceso de difracción.

*(Figura 13.27: la red dual.)*

Suponga ahora que una onda plana atraviesa la red infinita,

$$e^{i\vec{k}\cdot\vec{r} - i\omega t}.$$

La onda que resulta de la interacción de la onda plana con la red tiene entonces la forma

$$e^{i\vec{k}\cdot\vec{r} - i\omega t}\,g(\vec{r}), \tag{13.113}$$

donde $g(\vec{r})$ es una función periódica, como $f(\vec{r})$ en (13.106). Para hallar las ondas refractadas posibles, debemos escribir esto en la forma

$$e^{i\vec{k}\cdot\vec{r} - i\omega t}\,g(\vec{r}) = \sum_{\text{ondas difractadas},\,\alpha} C_\alpha\, e^{i\vec{k}_\alpha\cdot\vec{r} - i\omega t}. \tag{13.114}$$

Pero también sabemos, por la discusión anterior, que la transformada de Fourier de $g$ es no nula solo para valores de $\vec{k}$ de la forma (13.107). Así, (13.114) toma la forma

$$e^{i\vec{k}\cdot\vec{r} - i\omega t}\int d^3k'\, e^{i\vec{k}'\cdot\vec{r}}\,C_g(\vec{k}') = e^{i\vec{k}\cdot\vec{r} - i\omega t}\sum_{n_j} C_{n_j}\, e^{2\pi i\sum_j n_j\vec{\ell}_j\cdot\vec{r}}. \tag{13.115}$$

Por tanto, los $\vec{k}_\alpha$ de (13.114) deben tener la forma

$$\vec{k}_\alpha = \vec{k} + 2\pi\sum_j n_j\,\vec{\ell}_j. \tag{13.116}$$

Pero esto solo es posible si $\vec{k}_\alpha$ satisface la relación de dispersión en el material, lo que significa, si el material es invariante bajo rotaciones de modo que $\omega^2$ depende solo de $|\vec{k}|^2$, que

$$|\vec{k}_\alpha|^2 = |\vec{k}|^2. \tag{13.117}$$

Así, obtenemos una onda difractada solo para los $n_j$ tales que se satisface (13.117). La difracción de rayos X en un cristal puede, por tanto, dar información directa sobre la red dual y, con ella, sobre la propia red cristalina.

Hay una manera más física de pensar en la red dual. Considere cualquier vector de la red dual que no sea múltiplo de otro,

$$\vec{d} = \sum_j n_j\,\vec{\ell}_j.$$

Ahora mire el subconjunto de vectores de la red que satisfacen

$$\vec{d}\cdot\vec{a} = 0. \tag{13.119}$$

Este subconjunto es el conjunto de puntos de la red que están en el plano $\vec{d}\cdot\vec{r} = 0$, es decir, el plano perpendicular a $\vec{d}$ que pasa por el origen. Considere ahora el subconjunto

$$\vec{d}\cdot\vec{a} = 1. \tag{13.120}$$

Este subconjunto es el conjunto de puntos de la red que están en el plano $\vec{d}\cdot\vec{r} = 1$, paralelo al plano $\vec{d}\cdot\vec{r} = 0$ en la red. Ese plano también es perpendicular a $\vec{d}$ y pasa por el punto (que puede no ser un punto de la red)

$$\frac{\vec{d}}{|\vec{d}|^2}.$$

Por tanto, la distancia perpendicular (es decir, en la dirección de $\vec{d}$) entre los dos planos es $1/|\vec{d}|$.

Podemos continuar esta discusión para concluir que el subconjunto de puntos de la red que satisfacen

$$\vec{d}\cdot\vec{a} = m \quad \text{para } m \text{ entero, de } -\infty \text{ a } \infty \tag{13.123}$$

es el conjunto de puntos de la red que están en planos paralelos perpendiculares a $\vec{d}$, con planos adyacentes separados por $1/|\vec{d}|$. ¡Pero ese conjunto debe ser el de todos los puntos de la red! Esto es así porque $\vec{d}\cdot\vec{a}$ es un entero para todos los puntos de la red, por la definición de red dual. Así, todos los puntos de la red están en uno de los planos de (13.123).

Estas consideraciones se ilustran en el cristal bidimensional de las figuras siguientes. Si el vector $\vec{d}$ de la red dual es el mostrado en la figura 13.28, entonces los planos perpendiculares de la red son los de la figura 13.29.

*(Figura 13.28: un vector de la red dual.)*

*(Figura 13.29: los planos correspondientes de la red.)*

Suponga ahora que $\vec{d}$ es uno de los puntos especiales de la red dual que dan lugar a una onda refractada, de modo que

$$|\vec{k} + 2\pi\vec{d}|^2 = |\vec{k}|^2 \implies \vec{d}\cdot\left(\vec{k} + \pi\vec{d}\right) = 0. \tag{13.124}$$

Esta relación se muestra en la figura 13.30. Muestra que el vector $k$ de la onda refractada, $\vec{k} + 2\pi\vec{d}$, es simplemente $\vec{k}$ reflejado en un plano perpendicular a $\vec{d}$. Hemos visto que hay un número infinito de tales planos en la red, separados por $1/|\vec{d}|$. La contribución a la onda dispersada de cada uno de esos planos se suma constructivamente a la onda refractada. Para verlo, considere la diferencia de fase entre la onda incidente, $e^{i\vec{k}\cdot\vec{r} - i\omega t}$, y la onda difractada $e^{i\vec{k}_\alpha\cdot\vec{r} - i\omega t}$ para $\vec{k}_\alpha = \vec{k} + 2\pi\vec{d}$. Evidentemente, la diferencia de fase en cualquier punto $\vec{r}$ es

$$2\pi\,\vec{d}\cdot\vec{r}. \tag{13.125}$$

*(Figura 13.30: la condición de dispersión de Bragg.)*

Esta diferencia de fase es un múltiplo entero de $2\pi$ en todos los planos

$$\vec{d}\cdot\vec{r} = m \quad \text{para } m \text{ entero, de } -\infty \text{ a } \infty. \tag{13.126}$$

Así, la contribución a la dispersión de todos los planos de puntos de la red se suma constructivamente, porque la relación de fase entre la onda incidente y la difractada es la misma en todos ellos. Recíprocamente, si $\vec{k}_\alpha \neq \vec{k} + 2\pi\vec{d}$, las contribuciones de los distintos planos interferirán destructivamente y no resultará ninguna onda difractada.

Esta interpretación física va asociada al nombre de «dispersión de Bragg». Los planos de (13.123) (o (13.126)) son los planos de Bragg del cristal. Nótese que, conforme el vector $\vec{d}$ de la red dual se alarga, los planos de Bragg correspondientes se acercan entre sí, pero son también menos densos, con menos centros dispersores por unidad de área. Generalmente, la dispersión es más débil para $|\vec{d}|$ grande.

## 13.8 Holografía

Nada nos impide analizar el patrón de difracción de una función $f(x, y)$ más complicada que la discutida en (13.16). Un holograma es precisamente uno de esos patrones de difracción. Una de las versiones más sencillas de holograma es aquella en la que un objeto se ilumina con un láser, que proporciona esencialmente una onda plana. La luz reflejada, y una parte del haz láser (extraída mediante alguna técnica de división de haz), inciden sobre una placa fotográfica con ángulos ligeramente distintos, como se muestra esquemáticamente en la figura 13.31. La onda incidente sobre la placa fotográfica tiene la forma

$$e^{-i\omega t}\left(e^{ikz} + \int dk_x\,dk_y\, C(k_x, k_y)\,e^{i\vec{k}\cdot\vec{r}}\right) \tag{13.127}$$

donde

$$k = |\vec{k}| = \omega/v. \tag{13.128}$$

*(Figura 13.31: cómo se hace un holograma.)*

(13.127) describe las dos partes coherentes de la onda luminosa incidente sobre la placa fotográfica. Por simplicidad, supondremos que la señal que realmente nos interesa, la onda reflejada con transformada de Fourier $C(k_x, k_y)$, es pequeña comparada con la onda de referencia $e^{ikz}$. Esta señal es lo que veríamos si se retirara la placa fotográfica y pusiéramos los ojos en el camino de la onda reflejada, pero fuera del camino del haz láser, como se muestra en la figura 13.32.

*(Figura 13.32: viendo el objeto.)*

La placa fotográfica (supondremos que está en $z = 0$) registra solo la intensidad de la onda total, proporcional a

$$1 + 2\operatorname{Re}\int dk_x\,dk_y\, C(k_x, k_y)\,e^{i(k_x x + k_y y)} + O(C^2). \tag{13.129}$$

Descartaremos los términos de orden $C^2$, suponiendo que $C$ es pequeña, aunque más adelante podremos ver que en realidad no supondrán ninguna diferencia aunque $C$ sea grande. Si ahora hacemos una diapositiva positiva a partir de la placa y la iluminamos con un haz láser de la misma frecuencia $\omega$, la onda «pasa» donde la intensidad luminosa sobre la placa era grande y se absorbe donde la intensidad era pequeña. Así, tenemos un problema de oscilación forzada exactamente del tipo que hemos discutido antes, con (13.129) haciendo el papel de $f(x, y)$. La solución para $z > 0$ (de (13.19)-(13.24)) es

$$e^{-i\omega t}\left(e^{ikz} + \int dk_x\,dk_y\, C(k_x, k_y)\,e^{i\vec{k}\cdot\vec{r}} + \text{c.c.}\right) \tag{13.130}$$

donde c.c. es la onda compleja conjugada, obtenida tomando el complejo conjugado de la señal y cambiando el signo de la dependencia en $z$ para obtener una onda que viaja en la dirección $+z$.

Lo importante que hay que notar sobre la onda compleja conjugada es que **representa un haz que viaja en una dirección distinta tanto de la señal como del haz de referencia**, porque la conjugación compleja ha cambiado el signo de $k_x$ y $k_y$.

El sistema resultante se muestra esquemáticamente en la figura 13.33. Su ojo ve una versión reconstruida de la onda reflejada que habría visto sin la placa fotográfica, como en la figura 13.32. Nótese que ni el haz de referencia ni el haz complejo conjugado se interponen en su visión, porque salen con ángulos ligeramente distintos. Esto es un holograma. Como no es una fotografía, sino una reconstrucción de la onda real que usted habría visto en la figura 13.32, tiene esa sorprendente propiedad de tridimensionalidad que hace llamativo a un holograma.

*(Figura 13.33: viendo la imagen holográfica.)*

Cabe preguntarse por qué elegimos que el ángulo entre el haz de referencia y la señal sea pequeño. Un ángulo grande tendría la ventaja de apartar más el haz de referencia, pero tendría una desventaja importante. Considere el patrón de intensidad sobre la placa fotográfica que registra el holograma. Es un patrón oscilante con un número de onda típico dado por el valor típico de $k_x$ o $k_y$, que son del orden de $k\sin\theta$, donde $\theta$ es el ángulo entre el haz de referencia y la señal. Pero entonces la distancia entre máximos vecinos sobre la placa fotográfica es del orden de

$$\frac{2\pi}{k\sin\theta} = \frac{\lambda}{\sin\theta}$$

donde $\lambda$ es la longitud de onda de la luz. Como $\lambda$ es una distancia muy pequeña, conviene tomar $\theta$ pequeño para desplegar el patrón sobre la placa fotográfica.

Nótese, además, que los términos de orden $C^2$ que descartamos realmente no hacen ningún daño aunque $C$ no sea pequeña. Como su dependencia en $x$ e $y$ es proporcional a la de la señal por su complejo conjugado, los $k_x$ y $k_y$ típicos de esos términos son cero y viajan aproximadamente en la dirección del haz de referencia. No llegan a su ojo en la figura 13.33.

## 13.9 Franjas y placas zonales

### 13.9.1 La imagen holográfica de un punto

Una de las imágenes holográficas más sencillas es la imagen de un solo punto. Si una onda plana encuentra en su camino un objeto muy pequeño, el objeto producirá una onda esférica. Si la onda plana y la onda esférica son absorbidas después por una placa fotográfica, como se muestra en la figura 13.34, se produce un patrón de interferencia en forma de círculos concéntricos, o franjas.

Concretamente, suponga que la onda plana se propaga en la dirección $z$, que la placa fotográfica está en el plano $x$-$y$ en $z = z_0$ y que ponemos el origen de nuestro sistema de coordenadas en la posición de la fuente de la onda esférica, como se muestra en la figura 13.34. Entonces la combinación lineal de onda plana más onda esférica tiene la forma (ignorando la polarización)

$$A e^{ikz} + \frac{B}{r}e^{ikr} \tag{13.132}$$

donde $r = \sqrt{x^2 + y^2 + z^2}$. Supondremos, por simplicidad, que $A$ y $B$ son reales, lo que significa que las dos ondas están en fase en el objeto. La intensidad de la onda en $z = z_0$, sobre la placa fotográfica, es por tanto

$$A^2 + \frac{B^2}{r_0^2} + \frac{2AB}{r_0}\cos\left[k(r_0 - z_0)\right] \tag{13.133}$$

donde $r_0$ es la distancia al objeto para un punto del plano $z = z_0$,

$$r_0 = \sqrt{R^2 + z_0^2} \tag{13.134}$$

y

$$R = \sqrt{x^2 + y^2} \tag{13.135}$$

es la distancia al eje $z$ en el plano $x$-$y$. La intensidad depende solo de $R$, como debe ser por la simetría del sistema bajo rotaciones alrededor del eje $z$.

*(Figura 13.34: franjas.)*

Normalmente nos interesa la región $z_0 \gg R$ porque, como veremos, el patrón de intensidad es más interesante para $R$ pequeña. En esa región, la distancia $r_0$ es muy próxima a $z_0$. Podemos ignorar la variación de $r_0$ en la amplitud $B/r_0$. Sin embargo, hay una dependencia interesante en el término del coseno de (13.133). En ese término podemos desarrollar $r_0$ en serie de Taylor,

$$r_0 = z_0\sqrt{1 + R^2/z_0^2} \approx z_0 + \frac{R^2}{2z_0}. \tag{13.136}$$

Poniendo todo junto, la intensidad viene dada aproximadamente, para $z_0 \gg R$, por

$$A^2 + \frac{B^2}{z_0^2} + \frac{2AB}{z_0}\cos\frac{kR^2}{2z_0}. \tag{13.137}$$

El patrón de intensidad (13.137) describe «zonas» circulares concéntricas de variación de intensidad. Las zonas pueden etiquetarse por los máximos y mínimos del coseno, en

$$\frac{kR^2}{2z_0} = n\pi \tag{13.138}$$

o

$$R^2 = n\lambda z_0 \tag{13.139}$$

donde $\lambda$ es la longitud de onda de la onda. Para $n$ par, el coseno tiene un máximo y, para $n$ impar, un mínimo. La variación de intensidad es máxima si la onda plana y la onda esférica tienen aproximadamente la misma amplitud en la placa,

$$A \approx \frac{B}{z_0}. \tag{13.140}$$

Entonces la amplitud llega efectivamente a cero en los mínimos. La distribución de intensidad en función de $R$ se muestra en la figura 13.35. Las posiciones de los máximos y mínimos, o «zonas», se muestran en el eje $R$. Sobre la placa fotográfica, esta distribución de intensidad da lugar a franjas circulares.

*(Figura 13.35: la distribución de intensidad.)*

Si la placa se revela y se ilumina con una onda plana, se reproduce la onda esférica original junto con otra onda esférica que se mueve hacia dentro, hacia un punto del eje $z$ a una distancia $z_0$ más allá de la placa, como se muestra en la figura 13.36. Esta onda es la imagen real de la figura 13.33. Cuando una onda plana (líneas de puntos) ilumina la placa fotográfica producida en la figura 13.34, se producen ondas esféricas divergentes (líneas de puntos) y convergentes (líneas continuas).

*(Figura 13.36: una onda plana iluminando la placa fotográfica.)*

### 13.9.2 Placas zonales

El holograma de la figura 13.34 puede usarse para enfocar parte de una onda plana. La onda esférica convergente mostrada en la figura 13.36 es mucho más intensa que el resto de la perturbación ondulatoria en el foco, $z = 2z_0$, $x = y = 0$, porque la amplitud de esa parte de la onda aumenta al acercarse al foco. Tiene la forma

$$\frac{1}{r'}e^{ikr'} \tag{13.141}$$

donde

$$r' = \sqrt{(z - 2z_0)^2 + x^2 + y^2}. \tag{13.142}$$

El mismo efecto puede producirse con una versión caricaturesca de la placa fotográfica, hecha tomando una placa transparente y ennegreciendo las zonas correspondientes a los $n$ negativos de (13.138), donde la distribución de intensidad es menor que la mitad del máximo. Por ejemplo, la primera zona negativa es la región $\lambda z_0/2 < R^2 < 3\lambda z_0/2$; la segunda es la región $5\lambda z_0/2 < R^2 < 7\lambda z_0/2$, etc. El resultado es una «placa zonal». En la figura 13.37 se muestra un ejemplo, producido ennegreciendo las primeras 4 zonas negativas. Estas cosas son bastante útiles, porque pueden producirse fácilmente y adaptarse a cualquier longitud de onda.

*(Figura 13.37: una placa zonal.)*

## Repaso del capítulo

Ahora debería ser capaz de:

i. Plantear un problema de difracción como un problema de oscilación forzada y escribir la onda difractada como una integral de Fourier;

ii. Interpretar la integral de Fourier en la región de campo lejano y hallar el patrón de difracción;

iii. Analizar los patrones de difracción de haces formados con una o más rendijas y con rectángulos;

iv. Usar el teorema de convolución para simplificar el cálculo de transformadas de Fourier;

v. Analizar la dispersión por una red de difracción y la difracción de rayos X en cristales;

vi. Interpretar un holograma como un patrón de difracción;

vii. Entender cómo una placa zonal puede enfocar una onda plana.

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

*(Figura 13.38: problema 13.2.)*

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

*(Figura 13.39: cuatro patrones de difracción.)*

Los cuatro objetos que produjeron estos patrones fueron, en orden aleatorio:

i. Una rendija sencilla de 1 mm de anchura;

ii. Una rendija sencilla de 0.6 mm de anchura;

iii. Dos rendijas, cada una de 0.6 mm de anchura, con los centros separados 1.5 mm;

iv. Seis rendijas, cada una de 0.6 mm de anchura, con centros adyacentes separados 1.5 mm.

**a.** ¿Cuál es cuál?

**b.** ¿Cómo lo sabe?

---

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*
