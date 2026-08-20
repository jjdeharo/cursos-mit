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
