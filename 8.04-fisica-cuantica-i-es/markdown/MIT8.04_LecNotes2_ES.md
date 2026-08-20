# Capítulo 2: Experimentos con fotones

## Vídeos de esta clase (YouTube)

**Lección 2: Overview of quantum mechanics (cont.). Interaction-free measurements.**

- [More on superposition. General state of a photon and spin states](https://www.youtube.com/watch?v=0xNmc2tJ-YM)
- [Entanglement](https://www.youtube.com/watch?v=G3HSP3qMgKI) (13:07)
- [Mach-Zehnder interferometers and beam splitters](https://www.youtube.com/watch?v=0USje5vTIKs)
- [Interferometer and interference](https://www.youtube.com/watch?v=37-GdFJGSXs)
- [Elitzur-Vaidman bombs](https://www.youtube.com/watch?v=vFZeh8bMx58) (10:29)

------------------------------------------------------------------------

B. Zwiebach

9 de febrero de 2016

## Contenidos

1.  Interferómetro de Mach-Zehnder
2.  Bombas de Elitzur-Vaidman

## 1. Interferómetro de Mach-Zehnder

Hemos discutido antes el interferómetro de Mach-Zehnder, que mostramos de nuevo en la Figura 1. Contiene dos divisores de haz BS1 y BS2 y dos espejos. Dentro del interferómetro tenemos dos haces, uno que va por la rama superior y otro que va por la rama inferior. Esto se extiende más allá de BS2: la rama superior continúa hacia D0 mientras que la rama inferior continúa hacia D1.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes2_ES/fig1.png)

Figura 1: El interferómetro de Mach-Zehnder.

Los cortes verticales en la figura anterior intersecan los dos haces y podemos preguntarnos cuál es la probabilidad de encontrar un fotón en cada uno de los dos haces en ese corte. Para esto necesitamos dos amplitudes de probabilidad, o dos números complejos, cuyo módulo al cuadrado daría las probabilidades. Podemos codificar esta información en un vector de dos componentes como

$$\begin{pmatrix} \alpha \\ \beta \end{pmatrix}. \qquad \text{(1.1)}$$

Aquí $\alpha$ es la amplitud de probabilidad de estar en el haz superior y $\beta$ la amplitud de probabilidad de estar en el haz inferior. Por lo tanto, $|\alpha|^2$ sería la probabilidad de encontrar el fotón en el haz superior y $|\beta|^2$ la probabilidad de encontrar el fotón en el haz inferior. Dado que el fotón debe encontrarse en uno de los dos haces, debemos tener

$$|\alpha|^2 + |\beta|^2 = 1. \qquad \text{(1.2)}$$

Siguiendo esta notación, tendríamos para los casos en que el fotón está definitivamente en uno u otro haz:

$$\text{fotón en el haz superior:}\ \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \qquad \text{fotón en el haz inferior:}\ \begin{pmatrix} 0 \\ 1 \end{pmatrix}. \qquad \text{(1.3)}$$

Podemos ver el estado (1.1) como una superposición de estos dos estados más simples usando las reglas de la suma y multiplicación de vectores:

$$\begin{pmatrix} \alpha \\ \beta \end{pmatrix} = \begin{pmatrix} \alpha \\ 0 \end{pmatrix} + \begin{pmatrix} 0 \\ \beta \end{pmatrix} = \alpha \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \beta \begin{pmatrix} 0 \\ 1 \end{pmatrix}. \qquad \text{(1.4)}$$

En el interferómetro mostrado en la Figura 1 incluimos en la rama inferior un “desfasador”, una pieza de

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes2_ES/fig2.png)

Figura 2: Un desfasador de factor de fase $e^{i\delta}$. La amplitud se multiplica por la fase.

material cuyo único efecto es multiplicar la amplitud de probabilidad por una fase fija $e^{i\delta}$ con $\delta \in \mathbb{R}$. Como se muestra en la Figura 2, la amplitud de probabilidad $\alpha$ a la izquierda del dispositivo se convierte en $e^{i\delta}\alpha$ a la derecha del dispositivo. Dado que la norma de una fase es uno, el desfasador no cambia la probabilidad de encontrar el fotón. Cuando la fase $\delta$ es igual a $\pi$, el efecto del desfasador es cambiar el signo de la función de onda, ya que $e^{i\pi} = -1$.

Consideremos ahora en detalle el efecto de los divisores de haz. Si el fotón incidente golpea un divisor de haz desde arriba, consideramos que este fotón pertenece a la rama superior y lo representamos por $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$. Si el fotón incidente golpea el divisor de haz desde abajo, consideramos que este fotón pertenece a la rama inferior, y lo representamos por $\begin{pmatrix} 0 \\ 1 \end{pmatrix}$. Mostramos los dos casos en la Figura 3. El efecto del divisor de haz es dar una función de onda de salida para cada uno de los dos casos:

$$\text{BS izquierdo:}\ \begin{pmatrix} 1 \\ 0 \end{pmatrix} \to \begin{pmatrix} s \\ t \end{pmatrix}, \qquad \text{BS derecho:}\ \begin{pmatrix} 0 \\ 1 \end{pmatrix} \to \begin{pmatrix} u \\ v \end{pmatrix}. \qquad \text{(1.5)}$$

Como se puede ver en el diagrama, para el fotón que incide desde arriba, $s$ puede pensarse como una amplitud de reflexión y $t$ como un coeficiente de transmisión. De manera similar, para el fotón que incide desde abajo, $v$ puede pensarse como una amplitud de reflexión y $u$ como un coeficiente de transmisión. Los cuatro números $s, t, u, v$, por linealidad, caracterizan completamente al divisor de haz. Pueden usarse para predecir la salida dado cualquier fotón incidente, que puede tener amplitudes para golpear tanto desde arriba como desde abajo. En efecto, un estado de fotón incidente $\begin{pmatrix} \alpha \\ \beta \end{pmatrix}$ daría

$$\begin{pmatrix} \alpha \\ \beta \end{pmatrix} = \alpha \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \beta \begin{pmatrix} 0 \\ 1 \end{pmatrix} \to \alpha \begin{pmatrix} s \\ t \end{pmatrix} + \beta \begin{pmatrix} u \\ v \end{pmatrix} = \begin{pmatrix} \alpha s + \beta u \\ \alpha t + \beta v \end{pmatrix} = \begin{pmatrix} s & u \\ t & v \end{pmatrix} \begin{pmatrix} \alpha \\ \beta \end{pmatrix}. \qquad \text{(1.6)}$$

En resumen, vemos que el BS produce el siguiente efecto

$$\begin{pmatrix} \alpha \\ \beta \end{pmatrix} \to \begin{pmatrix} s & u \\ t & v \end{pmatrix} \begin{pmatrix} \alpha \\ \beta \end{pmatrix}. \qquad \text{(1.7)}$$

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes2_ES/fig3.png)

Figura 3: Izquierda: Un fotón incidente desde arriba; $s$ y $t$ son las amplitudes reflejada y transmitida, respectivamente. Derecha: Un fotón incidente desde abajo; $v$ y $u$ son las amplitudes reflejada y transmitida, respectivamente.

Podemos representar la acción del divisor de haz como una multiplicación matricial sobre la función de onda incidente, con la matriz dos por dos

$$\begin{pmatrix} s & u \\ t & v \end{pmatrix}. \qquad \text{(1.8)}$$

Debemos ahora determinar las restricciones sobre $s, t, u, v$. Debido a que las probabilidades deben sumar uno, la ecuación (1.5) implica que

$$|s|^2 + |t|^2 = 1, \qquad \text{(1.9)}$$

$$|u|^2 + |v|^2 = 1. \qquad \text{(1.10)}$$

El tipo de divisores de haz que usamos se llaman balanceados, lo que significa que las probabilidades de reflexión y transmisión son iguales. Así que las cuatro constantes deben tener el mismo módulo al cuadrado:

$$|s|^2 = |t|^2 = |u|^2 = |v|^2 = \tfrac{1}{2}. \qquad \text{(1.11)}$$

Probemos una conjetura para los valores. ¿Podríamos tener

$$\begin{pmatrix} s & u \\ t & v \end{pmatrix} = \begin{pmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{pmatrix}\ ? \qquad \text{(1.12)}$$

Esto falla si al actuar sobre funciones de onda normalizadas (o vectores columna) no se obtienen funciones de onda normalizadas. Así que probamos con un par de funciones de onda

$$\begin{pmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix}, \qquad \begin{pmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{pmatrix} \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}. \qquad \text{(1.13)}$$

Mientras que el primer ejemplo funciona, el segundo no, ya que $|1|^2 + |1|^2 = 2 \neq 1$. Una solución sencilla se logra cambiando el signo de $v$:

$$\begin{pmatrix} s & u \\ t & v \end{pmatrix} = \begin{pmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}. \qquad \text{(1.14)}$$

Comprobemos que esta matriz funciona en general. Así, al actuar sobre un estado $\begin{pmatrix} \alpha \\ \beta \end{pmatrix}$ con $|\alpha|^2 + |\beta|^2 = 1$ encontramos

$$\frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} \alpha \\ \beta \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} \alpha + \beta \\ \alpha - \beta \end{pmatrix}. \qquad \text{(1.15)}$$

En efecto, el estado resultante está bien normalizado. La probabilidad total es lo que esperamos

$$\begin{aligned}
& \tfrac{1}{2}|\alpha+\beta|^2 + \tfrac{1}{2}|\alpha-\beta|^2\\
& \quad = \tfrac{1}{2}\big(|\alpha|^2 + |\beta|^2 + \alpha\beta^* + \alpha^*\beta\big) + \tfrac{1}{2}\big(|\alpha|^2 + |\beta|^2 - \alpha\beta^* - \alpha^*\beta\big)\\
& \quad = |\alpha|^2 + |\beta|^2 = 1. \qquad \text{(1.16)}
\end{aligned}$$

El signo menos en la entrada inferior derecha de (1.14) significa que un fotón incidente desde abajo, al ser reflejado, tendrá su amplitud cambiada por un signo, o equivalentemente por un desfase de $\pi$ (¡compruébelo!). Este efecto, por supuesto, se realiza en la práctica. Un divisor de haz típico consiste en una placa de vidrio con un recubrimiento dieléctrico reflectante en un lado. El índice de refracción del recubrimiento se elige de manera que sea intermedio entre el del vidrio y el del aire. Una reflexión causa un desfase solo cuando la luz encuentra un material de mayor índice de refracción. Este es el caso en la transición de aire a recubrimiento, pero no en la transición de vidrio a recubrimiento. Por lo tanto, el divisor de haz representado por (1.14) tendría su recubrimiento en el lado inferior. Las ondas transmitidas no tienen desfase.

Otra posibilidad para una matriz de divisor de haz es

$$\frac{1}{\sqrt{2}} \begin{pmatrix} -1 & 1 \\ 1 & 1 \end{pmatrix}, \qquad \text{(1.17)}$$

que se realizaría mediante un recubrimiento dieléctrico en el lado superior. Puede comprobar rápidamente que, al igual que la matriz anterior, su acción también conserva la probabilidad. Llamaremos BS1 al divisor de haz de la izquierda y BS2 al de la derecha, y sus respectivas matrices serán

$$\text{BS1}:\ \frac{1}{\sqrt{2}} \begin{pmatrix} -1 & 1 \\ 1 & 1 \end{pmatrix}, \qquad \text{BS2}:\ \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}. \qquad \text{(1.18)}$$

Los dos divisores de haz se combinan para formar el interferómetro mostrado en la Figura 4. Si ahora suponemos una función de onda de fotón de entrada $\begin{pmatrix} \alpha \\ \beta \end{pmatrix}$ desde la izquierda, la función de onda de salida que entra a los detectores se obtiene actuando primero con la matriz BS1 y luego con la matriz BS2:

$$\begin{aligned}
\text{entrada:}\ \begin{pmatrix} \alpha \\ \beta \end{pmatrix} \quad \text{salida:}\ & \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \frac{1}{\sqrt{2}} \begin{pmatrix} -1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} \alpha \\ \beta \end{pmatrix}\\
& = \frac{1}{2}\begin{pmatrix} 0 & 2 \\ -2 & 0 \end{pmatrix}\begin{pmatrix} \alpha \\ \beta \end{pmatrix} = \begin{pmatrix} \beta \\ -\alpha \end{pmatrix}. \qquad \text{(1.19)}
\end{aligned}$$

Con la ayuda de este resultado, para cualquier estado de fotón de entrada podemos escribir inmediatamente el estado de fotón de salida que entra a los detectores.

Si el haz de fotones de entrada es $\begin{pmatrix} 0 \\ 1 \end{pmatrix}$, la salida del interferómetro es $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$, y por lo tanto se detectará un fotón en D0. Esto se muestra en la Figura 5. Podemos hacer una tabla muy sencilla con los posibles resultados y sus respectivas probabilidades $P$:

$$\begin{array}{ll}
\text{Resultado} & P \\
\text{fotón en D0} & 1 \\
\text{fotón en D1} & 0
\end{array} \qquad \text{(1.20)}$$

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes2_ES/fig4.png)

Figura 4: El interferómetro de Mach-Zehnder con las funciones de onda de entrada y salida indicadas.

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes2_ES/fig5.png)

Figura 5: Un fotón incidente desde abajo irá hacia D0.

Ahora bloqueemos el camino inferior, como se indica en la Figura 6. ¿Qué sucede entonces? Es mejor seguir el proceso sistemáticamente. El haz de entrada, actuado por BS1, da

$$\frac{1}{\sqrt{2}} \begin{pmatrix} -1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix}. \qquad \text{(1.21)}$$

Esto se indica en la figura, a la derecha de BS1. Luego se detiene la rama inferior, mientras que la rama superior continúa. La rama superior llega a BS2, y aquí la entrada es $\begin{pmatrix} \frac{1}{\sqrt{2}} \\ 0 \end{pmatrix}$, porque no llega nada de la rama inferior. Por lo tanto obtenemos una salida

$$\frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} \frac{1}{\sqrt{2}} \\ 0 \end{pmatrix} = \begin{pmatrix} \frac{1}{2} \\ \frac{1}{2} \end{pmatrix}. \qquad \text{(1.22)}$$

En este experimento hay tres resultados posibles: el fotón puede ser absorbido por el bloqueo, o puede ir hacia cualquiera de los dos detectores.

![Figura 6](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes2_ES/fig6.png)

Figura 6: La probabilidad de detectar el fotón en D1 puede cambiarse bloqueando uno de los caminos.

Como vemos en el diagrama, las probabilidades son:

$$\begin{array}{ll}
\text{Resultado} & P \\
\text{fotón en el bloqueo} & \tfrac{1}{2} \\
\text{fotón en D0} & \tfrac{1}{4} \\
\text{fotón en D1} & \tfrac{1}{4}
\end{array} \qquad \text{(1.23)}$$

Es notable que antes de bloquear el camino inferior no podíamos conseguir que un fotón llegara a D1. La probabilidad de llegar a D1 ahora es 1/4 y aumentó al bloquear un camino.

## 2. Bombas de Elitzur-Vaidman

Para ver que permitir que el fotón llegue a D1 bloqueando un camino es algo muy extraño, consideramos una situación imaginaria propuesta por los físicos Avshalom Elitzur y Lev Vaidman, de la Universidad de Tel Aviv, en Israel. Ellos imaginaron bombas con un tipo especial de disparador: un detector de fotones. Un tubo estrecho atraviesa cada bomba y en el medio del tubo hay un detector de fotones. Para detonar la bomba se envía un fotón dentro del tubo. El fotón es entonces detectado por el detector de fotones y la bomba explota. Si el detector de fotones está defectuoso, sin embargo, el fotón no es detectado en absoluto. Se propaga libremente a través del tubo y sale de la bomba. La bomba no explota.

He aquí la situación que queremos abordar. Supongamos que tenemos una cierta cantidad de bombas de Elitzur-Vaidman (EV), pero sabemos que algunas de ellas se han vuelto defectuosas. ¿Cómo podríamos saber si una bomba es operativa sin detonarla? Supongamos, a efectos del problema, que no podemos examinar el detector sin destruir la bomba.

Parece que nos enfrentamos a una situación imposible. Si enviamos un fotón al tubo del detector y no sucede nada, sabemos que la bomba está defectuosa, pero si la bomba es operativa, simplemente explotaría. Parece imposible confirmar que el detector de fotones de la bomba está funcionando sin probarlo. En efecto, es imposible en la física clásica. Sin embargo, no es imposible en la mecánica cuántica. Como veremos, ¡podemos realizar lo que puede llamarse una medición libre de interacción!

Ahora colocamos una bomba EV en el camino inferior del interferómetro, con el tubo del detector adecuadamente alineado. Supongamos que enviamos un fotón como se muestra. Si la bomba está defectuosa es como si no hubiera detector, la rama inferior del interferómetro está libre y todos los fotones que enviemos terminarán en D0,

![Figura 7](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes2_ES/fig7.png)

Figura 7: Un interferómetro de Mach-Zehnder y una bomba de Elitzur-Vaidman insertada en la rama inferior, con el tubo del detector adecuadamente alineado. Si la bomba está defectuosa, todos los fotones incidentes terminarán en D0. Si un fotón termina en D1 sabemos que la bomba es operativa, ¡aunque el fotón nunca entró en el detector de la bomba!

igual que lo hicieron en la Figura 5.

$$\begin{array}{ll}
\text{Resultado} & P \\
\text{fotón en D0, sin explosión} & 1 \\
\text{fotón en D1, sin explosión} & 0 \\
\text{la bomba explota} & 0
\end{array} \qquad \text{(2.24)}$$

Si la bomba funciona, por otro lado, tenemos la situación que teníamos en la Figura 6, donde colocamos un bloqueo en la rama inferior del interferómetro:

$$\begin{array}{ll}
\text{Resultado} & P \\
\text{la bomba explota} & \tfrac{1}{2} \\
\text{fotón en D0, sin explosión} & \tfrac{1}{4} \\
\text{fotón en D1, sin explosión} & \tfrac{1}{4}
\end{array} \qquad \text{(2.25)}$$

Supongamos que la bomba está funcionando. Entonces el 50% de las veces el fotón la golpeará y explotará, el 25% de las veces el fotón terminará en D0 y no podremos saber si está defectuosa o no. Pero el 25% de las veces el fotón terminará en D1, y dado que esto era imposible para una bomba defectuosa, ¡hemos aprendido que la bomba es operativa! Hemos aprendido esto aunque el fotón nunca haya pasado por la bomba; terminó en D1. Si piensa en esto, seguramente se dará cuenta de que es extremadamente sorprendente y contraintuitivo. Pero es cierto, y los experimentos (¡sin usar bombas!) han confirmado que este tipo de medición libre de interacción es efectivamente posible.

Sarah Geller transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.

------------------------------------------------------------------------

MIT OpenCourseWare https://ocw.mit.edu

8.04 Física Cuántica I Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.
