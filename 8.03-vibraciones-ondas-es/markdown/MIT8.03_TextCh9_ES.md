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
