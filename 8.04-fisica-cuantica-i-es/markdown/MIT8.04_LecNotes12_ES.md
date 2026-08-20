# Clase 12

## Vídeos de esta clase (YouTube)

**Lección 12: Properties of 1D energy eigenstates. Qualitative properties of wavefunctions. Shooting method.**

- [Nondegeneracy of bound states in 1D. Real solutions](https://www.youtube.com/watch?v=EdXaUfRynx8)
- [Potentials that satisfy V(-x) = V(x)](https://www.youtube.com/watch?v=AtjMKPzNIXQ)
- [Qualitative insights: Local de Broglie wavelength](https://www.youtube.com/watch?v=QMeKIiufg5s)
- [Correspondence principle: amplitude as a function of position](https://www.youtube.com/watch?v=79GY-hI_emE)
- [Local picture of the wavefunction](https://www.youtube.com/watch?v=fWCGM2auQPs)
- [Energy eigenstates on a generic symmetric potential. Shooting method](https://www.youtube.com/watch?v=45M-BtYAcwg)

------------------------------------------------------------------------

*B. Zwiebach* *20 de marzo de 2016*

## Contenido

1.  Propiedades generales
2.  Estados ligados en potenciales que varían lentamente
3.  Esbozo del comportamiento de la función de onda en distintas regiones
4.  Método de disparo

## 1. Propiedades generales

Demostrarás los siguientes hechos en tu tarea:

1.  Dada la ecuación de Schrödinger con potencial $V(x)$

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + (V(x) - E)\psi = 0 \qquad \text{(1.1)}$$

no existen estados propios de energía con $E < \min_x V(x)$. En otras palabras, la situación indicada en la Figura 1 no puede ocurrir.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig1.png)

Figura 1: No existen soluciones con energía $E$ menor que el mínimo del potencial $V(x)$.

1.  Para un potencial unidimensional definido sobre $-\infty \le x \le \infty$, no existen estados ligados degenerados. Recordemos que un estado ligado es un estado propio de energía normalizable. Dado esto, $\lim_{x\to\infty}\psi = 0$.

Mostraremos ahora que el hecho de que $V(x)$ sea real nos permite trabajar con funciones de onda $\psi(x)$ reales. Aunque existen soluciones complejas, podemos elegir soluciones reales sin pérdida de generalidad.

**Teorema 1.** Los estados propios de energía $\psi(x)$ pueden elegirse reales.

**Demostración.** Consideremos nuestra ecuación principal para la función de onda compleja $\psi(x)$:

$$\psi'' + \frac{2m}{\hbar^2}(E - V(x))\psi = 0 . \qquad \text{(1.2)}$$

Dado que $(\psi'')^* = (\psi^*)''$ y $V(x)$ es real, la conjugación compleja de la ecuación anterior da

$$(\psi^*)'' + \frac{2m}{\hbar^2}(E - V(x))\psi^* = 0 . \qquad \text{(1.3)}$$

Vemos que $\psi^*(x)$ es otra solución de la ecuación de Schrödinger con la misma energía. La solución $\psi^*(x)$ es distinta de $\psi(x)$ si no existe una constante $c$ tal que $\psi^* = c\psi$. En ese caso $\psi^*$ y $\psi$ representan dos soluciones degeneradas y, por superposición, podemos obtener dos soluciones reales degeneradas:

$$\psi_r \equiv \frac{1}{2}(\psi + \psi^*) , \qquad \psi_{im} \equiv \frac{1}{2i}(\psi - \psi^*) . \qquad \text{(1.4)}$$

Estas son, por supuesto, las partes real e imaginaria de $\psi$. Si $\psi^* = c\psi$, las partes real e imaginaria producen la misma solución real. En cualquier caso podemos trabajar con una solución real. $\blacksquare$

Si nos ocupamos de estados ligados de potenciales unidimensionales, se puede afirmar algo más fuerte: no es que podamos elegir trabajar con soluciones reales, sino que cualquier solución es, de entrada, esencialmente real.

**Corolario 1.** Cualquier estado ligado $\psi(x)$ de un potencial unidimensional es real, salvo una fase constante global.

**Demostración.** Recordemos que en potenciales unidimensionales no existen estados ligados degenerados. Esto significa que las dos soluciones reales $\psi_r$ y $\psi_{im}$ consideradas arriba deben ser iguales salvo una constante, que solo puede ser real:

$$\psi_{im}(x) = c\,\psi_r(x) , \quad \text{con } c \in \mathbb{R} . \qquad \text{(1.5)}$$

De aquí se sigue que $\psi = \psi_r + i\psi_{im} = (1+ic)\psi_r$. Escribiendo $1+ic = \sqrt{1+c^2}\, e^{i\beta}$ con $\beta$ real, se muestra que $\psi$ es, salvo una fase constante $\beta$, igual a una solución real. $\blacksquare$

Nuestro siguiente resultado muestra que, para un potencial que es una función simétrica de $x$, podemos trabajar con estados propios de energía que sean funciones simétricas o antisimétricas de $x$.

**Teorema 2.** Si $V(-x) = V(x)$, los estados propios de energía pueden elegirse pares o impares bajo $x \to -x$.

**Demostración.** Nuevamente, partimos de nuestra ecuación principal

$$\psi'' + \frac{2m}{\hbar^2}(E - V(x))\psi = 0 . \qquad \text{(1.6)}$$

Recordemos que las primas denotan aquí derivada respecto del argumento, de modo que $\psi''(x)$ significa la función “segunda-derivada-de-$\psi$” evaluada en $x$. De igual manera $\psi''(-x)$ significa la función “segunda-derivada-de-$\psi$” evaluada en $-x$. Así podemos cambiar $x$ por $-x$ sin problema en la ecuación anterior, obteniendo

$$\psi''(-x) + \frac{2m}{\hbar^2}(E - V(x))\psi(-x) = 0 , \qquad \text{(1.7)}$$

donde usamos que $V$ es par. Ahora queremos dejar claro que la ecuación anterior implica que $\psi(-x)$ es otra solución de la ecuación de Schrödinger con la misma energía. Para esto definamos una función $\varphi(x)$ y tomemos dos derivadas de ella:

$$\varphi(x) \equiv \psi(-x) \;\;\to\;\; \frac{d}{dx}\varphi(x) = \psi'(-x)\cdot(-1) , \quad \frac{d^2}{dx^2}\varphi(x) = \psi''(-x) . \qquad \text{(1.8)}$$

Usando esto, la ecuación (1.7) se convierte en

$$\frac{d^2}{dx^2}\varphi(x) + \frac{2m}{\hbar^2}(E - V(x))\varphi(x) = 0 . \qquad \text{(1.9)}$$

lo que muestra que $\varphi(x) = \psi(-x)$ es una solución degenerada de la ecuación de Schrödinger. Con las soluciones degeneradas $\psi(x)$ y $\psi(-x)$ podemos ahora formar combinaciones simétrica (s) y antisimétrica (a) que son, respectivamente, pares e impares bajo $x \to -x$:

$$\psi_s(x) \equiv \frac{1}{2}\big(\psi(x) + \psi(-x)\big) , \qquad \psi_a(x) \equiv \frac{1}{2}\big(\psi(x) - \psi(-x)\big) . \qquad \text{(1.10)}$$

Estas son las soluciones que se afirmaba que existían. $\blacksquare$

Notemos que la demostración anterior no funcionaría para el caso de potenciales impares $V(-x) = -V(x)$. ¡No podemos decir mucho en ese caso!

Nuevamente, si nos centramos en estados ligados de potenciales pares unidimensionales, la ausencia de degeneración tiene una implicación más fuerte: las soluciones son automáticamente pares o impares.

**Corolario 2.** Cualquier estado ligado de un potencial par unidimensional es par o impar.

**Demostración.** La ausencia de degeneración implica que las soluciones $\psi(x)$ y $\psi(-x)$ deben ser la misma solución. Por el corolario 1, podemos elegir $\psi(x)$ real y así debemos tener

$$\psi(-x) = c\,\psi(x) , \quad \text{con } c \in \mathbb{R} . \qquad \text{(1.11)}$$

Haciendo $x \to -x$ en la ecuación anterior obtenemos $\psi(x) = c\,\psi(-x) = c^2\,\psi(x)$, de donde aprendemos que $c^2 = 1$. Las únicas posibilidades son $c = \pm 1$. Así, $\psi(x)$ es automáticamente par o impar bajo $x \to -x$. $\blacksquare$

Usamos el resultado de este teorema para hallar los estados ligados del pozo cuadrado finito. Puesto que ese potencial es par, pudimos restringir nuestro trabajo a la búsqueda de estados ligados pares y estados ligados impares. ¡El potencial no puede tener estados ligados que no sean ni pares ni impares!

## 2. Estados ligados en potenciales que varían lentamente

Consideraremos ahora algunas ideas que la física clásica nos aporta sobre el comportamiento de los estados propios de energía. Esto se denomina a veces la **aproximación semiclásica**, porque la física clásica a veces puede dar una descripción aproximada de la física cuántica.

Comenzamos con un ejemplo que ya entendemos. Consideramos la energía total $E$ de una partícula, que es la suma de una energía potencial $V$ y una energía cinética $K$. Cuando $V$ es función de la posición, $K$ también debe ser función de la posición para que la suma $E$ se conserve, como debe ocurrir. En nuestro primer ejemplo, mostrado en la Figura 2, el potencial $V$ es constante y la energía $E$ es mayor que $V$. Una partícula en tal potencial tendrá una energía cinética $K$ constante y por tanto un momento constante $p = \sqrt{2mK}$. Es un hecho que la onda que representa a la partícula cuántica tiene una longitud de onda de de Broglie $\lambda$ igual a la constante de Planck $h$ dividida entre el momento clásico.

En efecto, a partir de la ecuación de Schrödinger

$$\psi'' = -\frac{2m}{\hbar^2}(E-V)\psi = -\frac{2mK}{\hbar^2}\psi = -\frac{p^2}{\hbar^2}\psi , \qquad \text{(2.1)}$$

que lleva a soluciones reales de la forma

$$\psi \sim \cos\left(\frac{p}{\hbar}x\right) = \cos\left(\frac{2\pi}{h/p}x\right) , \qquad \text{(2.2)}$$

donde vemos que la longitud de onda de $\psi$ es la longitud de onda de de Broglie de una partícula con momento $p$. Esta función de onda es real y por tanto no es un estado propio de momento. Representa una superposición de un estado con momento $p$ y un estado de momento $-p$. Incluso en el caso clásico, la energía cinética $K$ solo determina $p^2$ y no el signo de $p$. Nuestro interés aquí está en funciones de onda reales $\psi(x)$, apropiadas para estados propios de energía, y lo que hemos visto es que, para un potencial constante, la longitud de onda de $\psi(x)$ es la longitud de onda de de Broglie asociada al momento clásico.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig2.png)

Figura 2: A la izquierda, un ejemplo de potencial constante, $V = V_0 < E$, donde $K$ es la energía cinética y $E = K + V_0$ es la energía total. A la derecha, un esbozo de la función de onda para una partícula en este potencial. $V$ constante $\Rightarrow$ $K$ constante, por tanto el momento también es constante.

Consideremos ahora la situación mostrada en la Figura 3, donde imaginamos una partícula clásica moviéndose en un potencial $V(x)$ linealmente creciente. Esta vez la energía cinética $K(x)$ también depende de la posición. Como resultado, el momento de la partícula clásica $p(x) = \sqrt{2mK(x)}$ también depende de la posición. La idea ahora es que, si el potencial varía lentamente, en buena aproximación la función de onda tendrá una longitud de onda de de Broglie dependiente de la posición $\lambda(x)$ dada por

$$\lambda(x) = \frac{h}{p(x)} . \qquad \text{(2.3)}$$

Con esto queremos decir que $\psi$ es alguna combinación de funciones

$$\cos\left(\frac{2\pi x}{\lambda(x)}\right), \quad \sin\left(\frac{2\pi x}{\lambda(x)}\right) . \qquad \text{(2.4)}$$

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig3.png)

Figura 3: Un potencial que varía linealmente, $V(x) = \alpha x$. La energía $E = K + V(x)$ es fija, y al aumentar $x$, $K(x)$ disminuye, $p(x)$ disminuye y $\lambda(x)$ aumenta, resultando en una función de onda de longitud de onda creciente.

Como vemos en la Figura 3, debido al crecimiento lineal de $V(x)$, una partícula con energía total $E$ tendrá una energía cinética $K(x)$ decreciente al aumentar $x$. Así, el momento clásico disminuirá, y anticipamos que la función de onda tendrá una longitud de onda de de Broglie local $\lambda(x)$ creciente al aumentar $x$. Esto se ilustra a la derecha de la figura. Discutiremos más adelante qué esperamos que ocurra con la amplitud de la función de onda.

La aproximación semiclásica —igualar la longitud de onda de $\psi(x)$ a la longitud de onda de de Broglie de la partícula clásica— es precisa cuando el potencial cambia lentamente. Por “lentamente” queremos decir que el cambio en el potencial a lo largo de una distancia comparable a la longitud de onda de de Broglie local es muy pequeño comparado con el propio potencial:

$$\lambda(x)\left|\frac{dV}{dx}\right| \ll |V(x)| . \qquad \text{(2.5)}$$

El lado izquierdo de la desigualdad es una estimación del cambio de $V$ a lo largo de una distancia $\lambda(x)$, y por tanto esta cantidad debe ser muy pequeña comparada con el potencial para que la aproximación semiclásica sea válida. Esta desigualdad es la condición clave para la aproximación semiclásica. De hecho, es la condición que permite establecer el análisis WKB de la ecuación de Schrödinger (¡asunto de 8.06!).

En la Figura 4 mostramos un potencial arbitrario $V(x)$ y consideramos el movimiento clásico de una partícula de energía total $E$. Para cualquier punto $x_0$, tenemos $V(x_0) + K(x_0) = E$. La energía cinética máxima ocurre en el valor mínimo del potencial. Clásicamente una partícula no puede tener energía cinética negativa, por lo que la partícula no puede encontrarse en puntos donde $V(x)$ es mayor que la energía $E$. En la figura, esto ocurre para $x > x_R$ y para $x < x_L$, y estas regiones se llaman **regiones clásicamente prohibidas**. Una partícula de energía $E$ oscilará de $x_L$ a $x_R$ y de vuelta. Al moverse, su velocidad cambia, siendo una función $v(x)$ de la posición. Los puntos $x_L$ y $x_R$ se llaman **puntos de retorno**, porque en ellos el movimiento de la partícula se invierte.

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig4.png)

Figura 4: Un potencial arbitrario que muestra los puntos de retorno $x_L$ y $x_R$. La región a la derecha de $x_R$ y la región a la izquierda de $x_L$ son regiones clásicamente prohibidas. En cualquier punto $x \in [x_L, x_R]$ la suma de la energía potencial $V(x)$ y la energía cinética $K(x)$ es igual a la energía total $E$.

La partícula clásica que oscila pasa más tiempo en las regiones donde su velocidad es pequeña y menos tiempo en las regiones donde su velocidad es grande. Esto tiene implicaciones cuánticas. En efecto, en la aproximación semiclásica encontramos que la amplitud de la función de onda es mayor en los lugares donde la partícula pasa más tiempo y menor en los lugares donde pasa menos tiempo. Esto puede cuantificarse. Consideremos la probabilidad $|\psi(x)|^2 dx$ de encontrar la partícula dentro de la región infinitesimal $dx$ alrededor de $x$. Esto se establece proporcional a la fracción de tiempo que la partícula pasa en $dx$:

$$|\psi(x)|^2 dx \simeq \frac{dt}{T} , \qquad \text{(2.6)}$$

donde $dt$ es el tiempo requerido para recorrer $dx$ y $T$ es el semiperiodo de oscilación, el tiempo para ir del punto de retorno izquierdo al punto de retorno derecho. Con $v(x)$ la velocidad local de la partícula, tenemos

$$|\psi(x)|^2 dx \simeq \frac{dx}{v(x)T} = \frac{m}{T}\frac{1}{p(x)}dx \;\;\to\;\; |\psi(x)|^2 \sim \frac{1}{p(x)} . \qquad \text{(2.7)}$$

Esta relación debe interpretarse con cuidado. Recordemos que $\psi(x)$ tiene longitud de onda muy pequeña para $p(x)$ grande. Así $|\psi(x)|^2$ oscila entre cero y algún valor máximo en distancias muy cortas a lo largo de $x$. Por otro lado, el momento $p(x)$ que aparece en el lado derecho no presenta tales oscilaciones. Por tanto, con $|\psi(x)|^2$ en la relación anterior en realidad queremos decir el promedio de $|\psi(x)|^2$ sobre unas pocas oscilaciones cerca de $x$, en otras palabras, el cuadrado de la amplitud de la onda $\psi(x)$. Escribiendo la amplitud (un número real positivo, por supuesto) como $\mathrm{Amp}(\psi(x))$, tenemos

$$\mathrm{Amp}(\psi(x)) \sim \frac{1}{\sqrt{p(x)}} \sim \sqrt{\lambda(x)} . \qquad \text{(2.8)}$$

La amplitud de la onda es proporcional a la raíz cuadrada de la longitud de onda de de Broglie. Así, en la Figura 5, el momento de la partícula disminuye y $\lambda(x)$ aumenta al aumentar $x$. Por tanto esperamos que la amplitud de la onda aumente, como se esboza a la derecha.

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig5.png)

Figura 5: Un potencial $V(x)$ y una energía cinética que disminuye al aumentar $x$. Entonces la longitud de onda de de Broglie aumenta con $x$. La ecuación 2.8 implica entonces que la amplitud de $\psi(x)$ también aumenta con $x$.

Como ilustración sencilla de la importancia de promediar $|\psi|^2$, consideremos un estado de energía grande en el potencial de pozo infinito, como se muestra en la Fig. 6. Dentro de la caja, la partícula clásica “rebota” entre las paredes con velocidad constante. Como resultado, la partícula pasa la misma cantidad de tiempo en cada intervalo $dx$ de igual tamaño dentro de la caja. La distribución de probabilidad clásica $P_{cl}$ dentro de la caja es uniforme:

$$P_{cl}(x)dx = \frac{1}{a}dx \;\;\to\;\; P_{cl}(x) = \frac{1}{a} , \qquad \text{(2.9)}$$

ya que la integral sobre la caja $x \in [0,a]$ de $P_{cl}(x)dx$ da uno. Consideremos ahora un estado propio de energía $\psi_n(x)$ con $n$ grande:

$$\psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi x}{a}\right) \;\;\to\;\; |\psi_n(x)|^2 = \frac{2}{a}\sin^2\left(\frac{n\pi x}{a}\right) . \qquad \text{(2.10)}$$

La densidad de probabilidad mecánico-cuántica asociada $P_{qm}$ es

$$P_{qm}(x) = |\psi_n(x)|^2 = \frac{2}{a}\sin^2\left(\frac{n\pi x}{a}\right) , \qquad \text{(2.11)}$$

y es, para $n$ grande, una función que oscila rápidamente, aparentemente muy distinta de la probabilidad clásica $P_{cl} = 1/a$. Mientras que la probabilidad clásica nunca se anula, ¡la probabilidad cuántica tiene muchos ceros! Aun así, sobre distancias arbitrarias mayores que $a/n$ (que se presume pequeña ya que $n$ es muy grande), el promedio de la densidad de probabilidad cuántica se aproxima a la densidad de probabilidad clásica. Recordemos que el promedio de $\sin^2$ sobre cualquier número entero de oscilaciones es $1/2$, de modo que su promedio sobre cualquier intervalo que incluya un número grande de oscilaciones (no necesariamente entero) es aproximadamente igual a $1/2$. Tenemos entonces

$$\mathrm{Promedio}_x(P_{qm}(x)) \simeq \frac{2}{a}\cdot\frac{1}{2} = \frac{1}{a} = P_{cl}(x) . \qquad \text{(2.12)}$$

![Figura 6](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig6.png)

Figura 6: Partícula en una caja unidimensional. La partícula rebota con velocidad constante.

La aproximación semiclásica es una realización explícita de lo que se llama libremente el “principio de correspondencia”, la idea de que existen límites de los estados cuánticos en los que sus propiedades pueden entenderse mediante un análisis clásico del sistema.

## 3. Esbozo del comportamiento de la función de onda en distintas regiones

Examinemos el comportamiento de un estado propio de energía para el caso de un potencial general $V(x)$. Reescribimos la ecuación de Schrödinger independiente del tiempo dividiendo por $\psi$ para obtener:

$$\frac{\psi''(x)}{\psi(x)} = -\frac{2m}{\hbar^2}(E - V(x)) , \qquad \text{(3.1)}$$

lo cual es conveniente porque no aparece la función de onda en el lado derecho. Consideraremos la ecuación en dos regiones y en algunos puntos especiales.

- $E - V(x) < 0$, **región clásicamente prohibida**, porque la energía total es menor que el potencial. En este caso el lado derecho de la ec. (3.1) es positivo. Esto significa que hay dos posibilidades: tanto $\psi$ como $\psi''$ son positivas, o tanto $\psi$ como $\psi''$ son negativas. Estas posibilidades se muestran aquí:

![Figura 7](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig7.png)

Figura 7: En la región clásicamente prohibida, o bien $\psi > 0$, $\psi'' > 0$, o bien $\psi < 0$, $\psi'' < 0$. En ambos casos la función de onda es convexa hacia el eje $x$.

Estos posibles comportamientos se resumen diciendo que la función de onda es **convexa hacia el eje**. Cuando las regiones clásicamente prohibidas se extienden hasta $x = -\infty$ o $x = \infty$, el comportamiento es del tipo mostrado a continuación:

![Figura 8](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig8.png)

Figura 8: Funciones de onda que se acercan a $x = -\infty$ o $x = \infty$ dentro de regiones clásicamente prohibidas.

- $E - V > 0$, **región clásicamente permitida**: el lado derecho de la ec. 3.1 es negativo. Así, o bien $\psi > 0$, $\psi'' < 0$, o bien $\psi < 0$, $\psi'' > 0$. Ambas opciones se muestran a continuación y se resumen diciendo que la función de onda es **cóncava hacia el eje**:

![Figura 9](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig9.png)

Figura 9: $\psi > 0$, $\psi'' < 0$, o $\psi < 0$, $\psi'' > 0$. La función de onda es cóncava hacia el eje $x$.

Una región clásicamente permitida que sea grande tendría las partes superior e inferior de la figura anterior alternándose para formar una función que se asemeja a un seno o un coseno.

- $V(x_0) = E$. **Punto de retorno**: definido como un punto $x_0$ en el cual la energía potencial $V(x_0)$ es igual a la energía total $E$. Los puntos de retorno separan regiones clásicamente permitidas de regiones clásicamente prohibidas. Un punto de retorno es un punto de inflexión en la gráfica de $\psi(x)$, un punto donde la segunda derivada se anula, ya que

$$\psi''(x_0) = -\frac{2m}{\hbar^2}\cdot 0 \cdot \psi(x_0) = 0 , \qquad \text{(3.2)}$$

No todos los puntos de inflexión son puntos de retorno. De hecho, los nodos de la función de onda son puntos de inflexión. Esto es claro a partir de $\psi'' = -\frac{2m}{\hbar^2}(E - V(x))\psi$, ya que si $\psi$ se anula, $\psi''$ también se anula.

Notemos, sin embargo, que no está permitido que $\psi$ y $\psi'$ se anulen simultáneamente en ningún punto del dominio de la función de onda. Esto se debe a que la ecuación de Schrödinger es una ecuación diferencial lineal de segundo orden. Se puede mostrar rápidamente que si $\psi = \psi' = 0$ en algún punto $x_0$, entonces todas las derivadas superiores de $\psi$ se anulan en ese punto. Suponiendo que la función de onda tiene un desarrollo de Taylor, concluimos que la función de onda debe anularse idénticamente.

![Figura 10](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig10.png)

Figura 10: Es imposible que tanto $\psi$ como $\psi'$ se anulen en algún punto $x_0$: la ecuación de Schrödinger obligaría entonces a que $\psi(x)$ se anule idénticamente.

Concluimos esta sección ilustrando la cuantización de los niveles de energía para los estados ligados de un potencial par. Como se muestra en la Figura 11, arriba, tenemos un potencial par y hemos marcado cuatro energías $E_1 < E_2 < E_3 < E_4$. No todas corresponden a estados propios de energía. Imaginamos integrar la ecuación de Schrödinger desde $x = \infty$ hacia $x = 0$. Como se muestra en la pequeña figura ligeramente a la derecha y abajo del potencial, suponemos $\psi > 0$ cuando $x \to \infty$. Dado que cualquier estado ligado es automáticamente par o impar, la imagen en $x \to -\infty$ debe ser o bien la de $\psi > 0$ (la extensión par) o bien la de $\psi < 0$ (la extensión impar).

![Figura 11](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig11.png)

Figura 11: Un potencial par (figura superior) y el resultado de integrar la ecuación desde $x = \infty$ hacia cero para varios valores de la energía. Obtenemos una solución cuando $\psi(x)$ para $x \ge 0$ puede empalmarse con $\psi$ y $\psi'$ continuas a una extensión par o impar válida para $x < 0$. No hay solución para $E_1$ y $E_3$. El estado fundamental surge para $E_2$ y el primer estado excitado surge para $E_4$.

Para tener una solución, la imagen desde la derecha debe empalmar correctamente en $x = 0$ con una de las dos posibles extensiones para $x < 0$.

Consideremos, por ejemplo, la integración de la ecuación para $E = E_1$. Llegando desde $x = \infty$, la solución tiene un punto de inflexión y se vuelve cóncava hacia el eje. Más allá de este punto, la primera derivada $\psi'$ disminuye. Aun así, como se muestra en la imagen, $\psi'$ no se anula en $x = 0$, de modo que la extensión par para $x < 0$ no empalma correctamente con la solución de $x > 0$ en $x = 0$, porque $\psi'$ no es continua. Empalmar con la extensión impar no es una posibilidad porque entonces $\psi$ no sería continua en $x = 0$. Así, $E_1$ no es una energía permitida.

Al aumentar la energía a $E = E_2$, el punto de retorno ocurre en un $x$ mayor y $\psi'$ logra llegar exactamente a cero en $x = 0$, empalmando $\psi$ y $\psi'$ con la extensión par. Esta vez tenemos una solución. Por supuesto, esto ocurre precisamente para $E = E_2$; un poco más o un poco menos de energía y la derivada no es continua en $x = 0$.

Al aumentar la energía a $E_3$, el punto de retorno se mueve a un $x$ aún mayor y $\psi'$ es negativa en el momento en que llegamos a $x = 0$, mientras que $\psi$ sigue siendo positiva. La solución no puede empalmarse con la extensión par debido a la discontinuidad de la derivada.

Si ahora aumentamos aún más la energía hasta cierto valor $E_4$, en el momento en que llegamos a $x = 0$ la derivada $\psi'$ será negativa y $\psi$ será exactamente cero. Como se puede ver en la figura, obtenemos un buen empalme con la extensión impar para $x < 0$. Este es el primer estado excitado. Es una función de onda impar con un único nodo en $x = 0$.

## 4. Método de disparo

El **método de disparo** es un método numérico para hallar la forma de la solución de estado ligado de la ecuación de Schrödinger

$$\frac{d^2\psi}{dx^2} + \frac{2m}{\hbar^2}(E - V(x))\psi = 0 . \qquad \text{(4.1)}$$

El método se implementa fácilmente para potenciales pares $V(x)$, en cuyo caso podemos buscar estados ligados pares y estados ligados impares.

Consideremos primero los estados ligados pares. Intentaremos integrar la ecuación diferencial desde $x = 0$ hasta $x = \infty$. Para comenzar en $x = 0$ necesitamos fijar $\psi$ y $\psi'$ en este punto. Dado que la normalización del estado ligado no está determinada por la ecuación, podemos elegir

$$\psi(x=0) = 1 . \qquad \text{(4.2)}$$

La derivada también debe ser cero en este punto: si la derivada no es cero, la función de onda par tendrá una derivada discontinua en $x = 0$ (¿puedes ver por qué?). Por tanto debemos fijar

$$\psi'(x=0) = 0 . \qquad \text{(4.3)}$$

Para integrar la ecuación diferencial ahora necesitamos elegir alguna energía. Elijamos algún valor arbitrario $E_0$. Ya sabemos que valores arbitrarios de la energía no producen estados ligados. Entonces, ¿qué sale mal si ahora integramos la ecuación diferencial? Lo que ocurre típicamente es que se obtiene una solución que no puede normalizarse. Al trabajar con el ordenador se observa que más allá de cierto punto a lo largo de $x$ la solución diverge, quizás con $\psi \to \infty$, es decir, $\psi$ tendiendo hacia arriba.

Debes entonces cambiar el valor de la energía hasta encontrar algún valor $E_1$ para el cual la solución también diverge, pero esta vez con $\psi \to -\infty$, o $\psi$ tendiendo hacia abajo. Esta es una señal de que existe alguna energía en el intervalo entre $E_0$ y $E_1$ para la cual existe una solución normalizable. Entonces intentas reducir el intervalo. Si $E_0 < E_1$ puedes hacerlo hallando valores mayores que $E_0$ para los cuales la divergencia sigue siendo hacia arriba, y valores menores que $E_1$ para los cuales la divergencia sigue siendo hacia abajo. A medida que reduces el intervalo seguirás encontrando estas divergencias, pero ocurrirán para valores de $x$ cada vez mayores. Al hacer esto, obtienes una aproximación cada vez mejor a la energía del estado ligado (ver Fig. 12).

Para las soluciones impares, el procedimiento es el mismo, pero las condiciones de frontera en $x = 0$ son:

$$\psi(x=0) = 0 , \qquad \psi'(x=0) = 1 . \qquad \text{(4.4)}$$

La primera es necesaria para una función impar continua. La segunda es arbitraria, salvo por la normalización.

Si un potencial no es par pero tiene una pared dura, esto proporciona un buen punto de partida para la integración de la ecuación de Schrödinger. En ese punto la función de onda se fija en cero y la derivada se fija en uno. Si el potencial tiene dos paredes duras, podemos integrar comenzando desde una pared y luego exigir que la solución llegue exactamente a cero al llegar a la segunda pared.

Una nota práctica: al trabajar con ordenadores para llevar a cabo estas integraciones numéricas, primero es necesario “eliminar” las unidades de la ecuación diferencial. El primer paso en este proceso es reemplazar $x$ por una variable adimensional $u$. La relación entre ellas es de la forma $x = bu$, donde $b$ es una cantidad con unidades de longitud construida a partir de los parámetros del problema.

![Figura 12](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes12_ES/fig12.png)

Figura 12: La integración numérica de la ecuación de Schrödinger conduce a soluciones que divergen hacia arriba ($\psi \to \infty$) o hacia abajo ($\psi \to -\infty$) más allá de cierto valor de $x$. Los estados ligados se encuentran para los valores de energía en los cuales la divergencia cambia de hacia arriba a hacia abajo, o de hacia abajo a hacia arriba.

*Sarah Geller transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare https://ocw.mit.edu

8.04 Física Cuántica I Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

# Apéndice: Lista de problemas 5 (Problem Set 5, 2016)

*Física Cuántica I (8.04), Primavera de 2016* *Departamento de Física del MIT — Fecha de entrega: viernes 18 de marzo de 2016, 12:00 del mediodía*

**Lectura:** Griffiths: 3.2, 3.3, 3.4, 2.1 y 2.2.

## Problema 1. Gaussianas y saturación del producto de incertidumbre \[5 puntos\]

Consideremos la función de onda gaussiana

$$\psi(x) = N \exp\left(-\frac{x^2}{2a^2}\right) ,$$

donde $N \in \mathbb{R}$ y $a$ es una constante real positiva con unidades de longitud. Las integrales

$$\int_{-\infty}^{\infty} dx\, e^{-\alpha x^2 + \beta x} = \sqrt{\frac{\pi}{\alpha}}\exp\left(\frac{\beta^2}{4\alpha}\right) , \qquad \operatorname{Re}(\alpha) > 0 ,$$

$$\int_{-\infty}^{\infty} dx\, x^2 e^{-\alpha x^2} = \frac{1}{2\alpha}\int_{-\infty}^{\infty} dx\, e^{-\alpha x^2}$$

pueden ser útiles.

1.  Usa la función de onda en representación de posiciones dada arriba para calcular las incertidumbres $\Delta x$ y $\Delta p$. Confirma que tu respuesta satura el producto de incertidumbre de Heisenberg

$$\Delta x \, \Delta p \geq \frac{\hbar}{2} .$$

(Pistas: ¡estos cálculos son en realidad bastante breves si se hacen de la manera correcta! Usando la segunda de las integrales anteriores ni siquiera necesitas determinar $N$. Para evaluar $\langle \hat p^2 \rangle$ en el espacio de posiciones, traslada uno de los factores de $\hat p$ hacia $\psi^*$.)

1.  Calcula la transformada de Fourier $\phi(p)$ de $\psi(x)$. Usa el teorema de Parseval para confirmar tu respuesta y luego recalcula $\Delta p$ usando el espacio de momentos.

## Problema 2. Gaussianas complejas y el producto de incertidumbre \[10 puntos\]

Consideremos la función de onda gaussiana

$$\psi(x) = N \exp\left(-\frac{x^2}{2\Delta^2}\right) , \qquad \Delta \in \mathbb{C} , \quad \operatorname{Re}(\Delta^2) > 0 ,$$

donde $N$ es una constante de normalización real y $\Delta$ es ahora un número complejo: $\Delta^* \neq \Delta$. Las integrales del Problema 1 también son útiles aquí, así como la siguiente relación, válida para cualquier número complejo no nulo $z$,

$$\operatorname{Re}\left(\frac{1}{z}\right) = \frac{\operatorname{Re}(z)}{|z|^2} \qquad (\text{¡demuéstralo!})$$

1.  Usa la representación en el espacio de posiciones de la función de onda dada arriba para calcular las incertidumbres $\Delta x$ y $\Delta p$. Deja tu respuesta en términos de $|\Delta|$ y $\operatorname{Re}(\Delta^2)$. ($\Delta x$ dependerá de ambos[1], mientras que $\Delta p$ dependerá solo de $\operatorname{Re}(\Delta^2)$.)

2.  Calcula la transformada de Fourier $\phi(p)$ de $\psi(x)$. Usa el teorema de Parseval para confirmar tu respuesta y luego recalcula $\Delta p$ usando el espacio de momentos.

3.  Parametrizamos $\Delta$ usando una fase $\varphi_\Delta \in \mathbb{R}$ de la siguiente manera

$$\Delta = |\Delta|\, e^{i\varphi_\Delta} .$$

Calcula el producto $\Delta x \, \Delta p$ y confirma que la respuesta puede escribirse en términos de una función trigonométrica de $\varphi_\Delta$, y que $|\Delta|$ desaparece del resultado. ¿Es razonable tu respuesta para $\varphi_\Delta = 0$ y para $\varphi_\Delta = \pi/4$?

1.  Considera la evolución libre de un paquete de ondas gaussiano estudiada en el Problema 3 de la Tarea 4. ¿Cuál es $\Delta p$ en el instante $t=0$? Examina la evolución temporal de la gaussiana (¡a partir de la solución!) y lee el valor de la constante compleja dependiente del tiempo $\Delta^2$. Confirma que $\Delta p$, hallado en el apartado (a), da un resultado independiente del tiempo.

## Problema 3. Ejercicios con una partícula en una caja \[15 puntos\]

Consideremos un problema unidimensional para una partícula de masa $m$ que puede moverse libremente en el intervalo $x \in [0,a]$. El potencial $V(x)$ es nulo en este intervalo e infinito fuera de él. Para este sistema consideramos una solución de la ecuación de Schrödinger de la forma

$$\Psi_n(x,t) = N \sin\left(\frac{n\pi}{a}x\right) e^{-i\varphi_n(t)} , \qquad x \in [0,a] ,$$

y $\Psi_n(x,t) = 0$ para $x<0$ y $x>a$. Aquí $n \geq 1$ es un número entero.

1.  Encuentra la expresión de la fase (real) $\varphi_n(t)$ para que la función de onda anterior resuelva la ecuación de Schrödinger. Encuentra la constante de normalización $N$.

2.  Usa $\Psi_n(x,0)$ para calcular $\langle x \rangle$, $\langle x^2 \rangle$ y $\Delta x$.

3.  Usa $\Psi_n(x,0)$ para calcular $\langle p \rangle$, $\langle p^2 \rangle$ y $\Delta p$.

4.  ¿Se satisface la desigualdad de incertidumbre? ¿Está saturada?

5.  ¿Qué respuestas de (b) y (c) cambian para $\Psi_n(x,t)$? Explica por qué.

## Problema 4. Una pared dura \[5 puntos\]

Una partícula de masa $m$ se mueve en una dimensión, sujeta al potencial $V(x)$:

$$V(x) = \begin{cases} 0, & \text{para } x > 0, \\ \infty, & \text{para } x \leq 0 . \end{cases}$$

Encuentra los estados estacionarios y sus energías. Estos estados no pueden normalizarse.

## Problema 5. Un escalón en la recta infinita \[10 puntos\]

Una partícula de masa $m$ se mueve en una dimensión, sujeta al potencial $V(x)$:

$$V(x) = \begin{cases} V_0, & \text{para } x > 0, \\ 0, & \text{para } x \leq 0 . \end{cases}$$

Encuentra los estados estacionarios que existen para energías $0 < E < V_0$.

## Problema 6. Una pared y la mitad de un pozo finito \[10 puntos\]

Una partícula de masa $m$ se mueve en una dimensión, sujeta al potencial $V(x)$:

$$V(x) = \begin{cases} \infty, & \text{para } x < 0, \\ -V_0, & \text{para } 0 < x < a \quad (V_0 > 0), \\ 0, & \text{para } x > a . \end{cases}$$

Encuentra los estados estacionarios que corresponden a estados ligados ($E<0$ en este caso). ¿Existe siempre un estado ligado? Encuentra el valor mínimo de $z_0$

$$z_0^2 = \frac{2ma^2 V_0}{\hbar^2} ,$$

para el cual existen tres estados ligados. Explica la relación precisa de este problema con el problema del pozo cuadrado finito de anchura $2a$.

## Problema 7. Imitando el hidrógeno con un pozo cuadrado unidimensional \[5 puntos\]

El átomo de hidrógeno tiene un radio de Bohr $a_0$ y una energía del estado fundamental $E_0$ dados por

$$a_0 = \frac{\hbar^2}{me^2} \simeq 0.529 \times 10^{-10}\ \text{m} , \qquad E_0 = -\frac{e^2}{2a_0} = -13.6\ \text{eV}.$$

El estado fundamental es un estado ligado y el potencial tiende a cero en el infinito. Queremos diseñar un pozo cuadrado finito unidimensional

$$V(x) = \begin{cases} -V_0, & \text{para } |x| < a_0, \quad V_0 > 0, \\ 0, & \text{para } |x| > a_0, \end{cases}$$

que simule al átomo de hidrógeno. Calcula el valor de $V_0$ en eV para que el estado fundamental de la caja se encuentre a la profundidad correcta.

## Problema 8. No hay estados con $E < V(x)$ \[5 puntos\]

Consideremos un estado estacionario real $\psi(x)$ con energía $E$:

$$-\frac{\hbar^2}{2m}\psi''(x) + [V(x)-E]\psi(x) = 0 .$$

1.  Demuestra que $E$ debe superar el valor mínimo de $V(x)$, observando que $E = \langle H \rangle$.

2.  Explica esta afirmación intentando (y fracasando) esbozar una función de onda consistente con estar en la región clásicamente inaccesible para todos los valores de $x$.

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*

[1] De hecho, $\Delta x$ puede escribirse solamente en términos de $\operatorname{Re}(1/\Delta^2)$.
