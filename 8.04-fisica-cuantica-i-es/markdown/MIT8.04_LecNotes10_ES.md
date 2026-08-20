# Lección 10: Resolución de la ecuación de Schrödinger independiente del tiempo

## Vídeos de esta clase (YouTube)

**Lección 10: Uncertainty (cont.). Stationary states. Particle on a circle.**

- [Uncertainty and eigenstates](https://www.youtube.com/watch?v=1D4VPbhDy_A)
- [Stationary states: key equations](https://www.youtube.com/watch?v=8KQ-yK2xm60)
- [Expectation values on stationary states](https://www.youtube.com/watch?v=M2i8R6kMXKA)
- [Comments on the spectrum and continuity conditions](https://www.youtube.com/watch?v=gMnQ21-pjOA)
- [Solving particle on a circle](https://www.youtube.com/watch?v=2EV1vJAAo8M)

------------------------------------------------------------------------

B. Zwiebach

14 de marzo de 2016

## Contenido

1.  Estados estacionarios
2.  Resolución para los autoestados de energía
3.  Partícula libre en un círculo

## 1. Estados estacionarios

Consideremos la ecuación de Schrödinger para la función de onda $\Psi(x, t)$ bajo el supuesto de que la energía potencial $V$ es independiente del tiempo:

$$i\hbar \frac{\partial \Psi}{\partial t} = \hat{H}\Psi(x, t) = \left( -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x) \right) \Psi(x, t) \qquad \text{(1.1)}$$

donde hemos mostrado la forma del operador hamiltoniano $\hat{H}$ con el potencial independiente del tiempo $V(x)$. Los estados estacionarios son una clase de soluciones muy útil de esta ecuación diferencial. La propiedad distintiva de un estado estacionario es que la dependencia espacial y temporal de la función de onda se factorizan. Es decir,

$$\Psi(x, t) = g(t)\, \psi(x) \qquad \text{(1.2)}$$

para ciertas funciones $g$ y $\psi$. Para que exista una solución separable de este tipo necesitamos que el potencial sea independiente del tiempo, como veremos a continuación. La solución $\Psi(x, t)$ depende del tiempo, pero se denomina estacionaria debido a una propiedad de los observables. El valor esperado de los observables sin dependencia temporal explícita en estados arbitrarios sí depende del tiempo. En un estado estacionario no depende del tiempo, como demostraremos.

Usemos el ansatz (1.2) para $\Psi$ en la ecuación de Schrödinger. Obtenemos entonces

$$i\hbar \left( \frac{dg(t)}{dt} \right) \psi(x) = g(t)\, \hat{H}\psi(x) \qquad \text{(1.3)}$$

porque $g(t)$ puede desplazarse a través de $\hat{H}$. Podemos entonces dividir esta ecuación por $\Psi(x,t) = g(t)\psi(x)$, obteniendo

$$i\hbar \frac{1}{g(t)} \frac{dg(t)}{dt} = \frac{1}{\psi(x)} \hat{H}\psi(x) \qquad \text{(1.4)}$$

El lado izquierdo es una función solo de $t$, mientras que el lado derecho es una función solo de $x$ (un potencial dependiente del tiempo habría arruinado esto). La única forma en que ambos lados pueden ser iguales entre sí para todos los valores de $t$ y $x$ es que ambos lados sean iguales a una constante $E$ con unidades de energía, porque $\hat{H}$ tiene unidades de energía. Obtenemos así dos ecuaciones separadas. La primera es

$$i\hbar \frac{dg}{dt} = E g \qquad \text{(1.5)}$$

Esta se resuelve mediante

$$g(t) = e^{-iEt/\hbar} \qquad \text{(1.6)}$$

y la solución más general es simplemente una constante multiplicada por el lado derecho anterior. Del lado dependiente de $x$ de la igualdad obtenemos

$$\hat{H}\psi(x) = E\psi(x) \qquad \text{(1.7)}$$

Esta ecuación es una ecuación de autovalores para el operador hermítico $\hat{H}$. Hemos mostrado que los autovalores de los operadores hermíticos deben ser reales, por lo que la constante $E$ debe ser real. La ecuación anterior se denomina la ecuación de Schrödinger independiente del tiempo. Más explícitamente se escribe

$$\left( -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x) \right) \psi(x) = E\psi(x) \qquad \text{(1.8)}$$

Nótese que esta ecuación no determina la normalización global de $\psi$. Por lo tanto, podemos escribir la solución completa sin pérdida de generalidad usando la $g(t)$ dada anteriormente:

$$\text{Estado estacionario:}\quad \Psi(x, t) = e^{-iEt/\hbar}\, \psi(x), \quad \text{con } E \in \mathbb{R} \ \text{ y } \ \hat{H}\psi = E\psi \qquad \text{(1.9)}$$

Nótese que no solo $\psi(x)$ es un autoestado del operador hamiltoniano $\hat{H}$, sino que el estado estacionario completo también es un autoestado de $\hat{H}$:

$$\hat{H}\Psi(x, t) = E\Psi(x, t) \qquad \text{(1.10)}$$

ya que la función dependiente del tiempo en $\Psi$ se cancela.

Hemos notado que la energía $E$ debe ser real. Si no lo fuera, también tendríamos problemas para normalizar el estado estacionario de manera consistente. La condición de normalización para $\Psi$, si $E$ no fuera real, daría

$$\begin{aligned}
1 &= \int dx\, \Psi^*(x,t)\Psi(x,t) = \int dx\, e^{iE^*t/\hbar} e^{-iEt/\hbar} \psi^*(x)\psi(x)\\
&= e^{i(E^*-E)t/\hbar} \int dx\, \psi^*(x)\psi(x) = e^{2\,\mathrm{Im}(E)t/\hbar} \int dx\, \psi^*(x)\psi(x) \qquad \text{(1.11)}
\end{aligned}$$

La expresión final tiene una dependencia temporal debida a la exponencial. Por otro lado, la condición de normalización establece que esta expresión debe ser igual a uno. De ello se sigue que el exponente debe ser cero, es decir, $E$ es real. Dado esto, vemos también que la condición de normalización arroja

$$\int_{-\infty}^{\infty} dx\, \psi^*(x)\psi(x) = 1 \qquad \text{(1.12)}$$

¿Cómo interpretamos el autovalor $E$? Usando (1.10) vemos que el valor esperado de $\hat{H}$ en el estado $\Psi$ es efectivamente la energía

$$\langle\langle \hat{H} \rangle\rangle_\Psi = \int dx\, \Psi^*(x,t)\, \hat{H}\Psi(x,t) = \int dx\, \Psi^*(x,t)\, E\Psi(x,t) = E \int dx\, \Psi^*(x,t)\Psi(x,t) = E \qquad \text{(1.13)}$$

Dado que el estado estacionario es un autoestado de $\hat{H}$, la incertidumbre $\Delta H$ del hamiltoniano en un estado estacionario es cero.

Hay dos observaciones importantes sobre los estados estacionarios:

**(1)** El valor esperado de cualquier operador independiente del tiempo $\hat{Q}$ en un estado estacionario $\Psi$ es independiente del tiempo:

$$\langle\langle \hat{Q} \rangle\rangle_{\Psi(x,t)} = \int dx\, \Psi^*(x,t)\, \hat{Q}\Psi(x,t) = \int dx\, e^{iEt/\hbar}\psi^*(x)\, \hat{Q} e^{-iEt/\hbar}\psi(x)$$

$$= \int dx\, e^{iEt/\hbar} e^{-iEt/\hbar} \psi^*(x)\hat{Q}\psi(x) = \int dx\, \psi^*(x)\hat{Q}\psi(x) = \langle\langle \hat{Q} \rangle\rangle_{\psi(x)} \qquad \text{(1.14)}$$

ya que el último valor esperado es manifiestamente independiente del tiempo.

**(2)** La superposición de estados estacionarios con energías diferentes no es estacionaria. Esto es claro porque un estado estacionario requiere una solución factorizada de la ecuación de Schrödinger: si sumamos dos soluciones factorizadas con energías diferentes, estas tendrán dependencias temporales distintas y el estado total no podrá factorizarse. Ahora mostraremos que un observable independiente del tiempo $\hat{Q}$ puede tener un valor esperado dependiente del tiempo en tal estado. Consideremos una superposición

$$\Psi(x, t) = c_1 e^{-iE_1 t/\hbar} \psi_1(x) + c_2 e^{-iE_2 t/\hbar} \psi_2(x) \qquad \text{(1.15)}$$

donde $\psi_1$ y $\psi_2$ son autoestados de $\hat{H}$ con energías $E_1$ y $E_2$, respectivamente. Consideremos un operador hermítico $\hat{Q}$. Con el sistema en el estado (1.15), su valor esperado es

$$\langle\langle \hat{Q} \rangle\rangle_\Psi = \int_{-\infty}^{\infty} dx\, \Psi^*(x,t)\, \hat{Q}\Psi(x,t)$$

$$= \int_{-\infty}^{\infty} dx \left[ c_1^* e^{iE_1 t/\hbar}\psi_1^*(x) + c_2^* e^{iE_2 t/\hbar}\psi_2^*(x) \right] \left[ c_1 e^{-iE_1 t/\hbar}\hat{Q}\psi_1(x) + c_2 e^{-iE_2 t/\hbar}\hat{Q}\psi_2(x) \right]$$

$$= \int_{-\infty}^{\infty} dx \Big[ |c_1|^2 \psi_1^*\hat{Q}\psi_1 + |c_2|^2 \psi_2^*\hat{Q}\psi_2 + c_1^* c_2\, e^{i(E_1-E_2)t/\hbar}\, \psi_1^*\hat{Q}\psi_2 + c_2^* c_1\, e^{-i(E_1-E_2)t/\hbar}\, \psi_2^*\hat{Q}\psi_1 \Big] \qquad \text{(1.16)}$$

Ahora vemos la posible dependencia temporal que surge de los términos cruzados. Los dos primeros términos son valores esperados simples e independientes del tiempo. Usando la hermiticidad de $\hat{Q}$ en el último término obtenemos entonces

$$\langle\langle \hat{Q} \rangle\rangle_\Psi = |c_1|^2 \langle\langle \hat{Q} \rangle\rangle_{\psi_1} + |c_2|^2 \langle\langle \hat{Q} \rangle\rangle_{\psi_2}$$

$$+\, c_1^* c_2\, e^{i(E_1-E_2)t/\hbar} \int_{-\infty}^{\infty} dx\, \psi_1^*\hat{Q}\psi_2 + c_1 c_2^*\, e^{-i(E_1-E_2)t/\hbar} \int_{-\infty}^{\infty} dx\, \psi_1 (\hat{Q}\psi_2)^* \qquad \text{(1.17)}$$

Los dos últimos términos son complejos conjugados entre sí y por lo tanto

$$\langle\langle \hat{Q} \rangle\rangle_\Psi = |c_1|^2 \langle\langle \hat{Q} \rangle\rangle_{\psi_1} + |c_2|^2 \langle\langle \hat{Q} \rangle\rangle_{\psi_2} + 2\,\mathrm{Re}\left[ c_1^* c_2\, e^{i(E_1-E_2)t/\hbar} \int_{-\infty}^{\infty} dx\, \psi_1^*\hat{Q}\psi_2 \right] \qquad \text{(1.18)}$$

Vemos que este valor esperado depende del tiempo si $E_1 \neq E_2$ y $(\psi_1, \hat{Q}\psi_2)$ es distinto de cero. El valor esperado completo $\langle\langle \hat{Q} \rangle\rangle_\Psi$ es real, como debe serlo para cualquier operador hermítico.

## 2. Resolución para los autoestados de energía

Ahora estudiaremos las soluciones de la ecuación de Schrödinger independiente del tiempo

$$\hat{H}\psi(x) = E\, \psi(x) \qquad \text{(2.19)}$$

Dado un hamiltoniano $\hat{H}$, nos interesa encontrar los autoestados $\psi$ y los autovalores $E$, que resultan ser las energías correspondientes. Quizás la característica más interesante de la ecuación anterior es que, en general, el valor de $E$ no puede ser arbitrario. Al igual que las matrices de tamaño finito tienen un conjunto de autovalores, la ecuación de Schrödinger independiente del tiempo anterior puede tener un conjunto discreto de energías posibles. También se permite un conjunto continuo de energías posibles, lo cual a veces es importante. En efecto, hay muchas soluciones para cualquier potencial dado. Suponiendo, por conveniencia, que los autoestados y sus energías pueden contarse, escribimos

$$\psi_1(x)\,, \ E_1 \qquad \psi_2(x)\,, \ E_2 \qquad \dots \qquad \text{(2.20)}$$

Nuestra discusión anterior sobre operadores hermíticos se aplica aquí. Los autoestados de energía pueden organizarse para formar un conjunto completo de funciones ortonormales:

$$\int \psi_i^*(x)\psi_j(x) = \delta_{ij} \qquad \text{(2.21)}$$

Consideremos la ecuación de Schrödinger independiente del tiempo escrita como

$$\frac{d^2\psi}{dx^2} = -\frac{2m}{\hbar^2}\left(E - V(x)\right)\psi \qquad \text{(2.22)}$$

Las soluciones $\psi(x)$ dependen de las propiedades del potencial $V(x)$. Es difícil hacer afirmaciones generales sobre la función de onda a menos que restrinjamos los tipos de potenciales. Sin duda consideraremos potenciales continuos. También consideraremos potenciales que no son continuos pero que son continuos a trozos, es decir, que tienen cierto número de discontinuidades. Nuestros potenciales pueden fácilmente no estar acotados. Permitimos funciones delta en los potenciales unidimensionales, pero no consideramos potencias o derivadas de funciones delta. Permitimos potenciales que se vuelven infinitos positivos más allá de ciertos puntos. Estos puntos representan paredes duras.

Queremos entender las propiedades generales de $\psi$ y el comportamiento de $\psi$ en los puntos donde el potencial $V(x)$ puede tener discontinuidades u otras singularidades. Afirmamos: debemos tener una función de onda continua. Si $\psi$ fuera discontinua, entonces $\psi'$ contendría funciones delta y $\psi''$, en el lado izquierdo de la ecuación anterior, contendría derivadas de funciones delta. Esto requeriría que el lado derecho tuviera derivadas de funciones delta, y estas tendrían que aparecer en el potencial. Dado que hemos declarado que nuestros potenciales no contienen derivadas de funciones delta, debemos tener efectivamente una $\psi$ continua.

Consideremos ahora cuatro posibilidades respecto al potencial:

**(1)** $V(x)$ es continuo. En este caso, la continuidad de $\psi(x)$ y (2.22) implican que $\psi''$ también es continua. Esto requiere que $\psi'$ sea continua.

**(2)** $V(x)$ tiene discontinuidades finitas. En este caso $\psi''$ tiene discontinuidades finitas: incluye el producto de una $\psi$ continua por una $V$ discontinua. Pero entonces $\psi'$ debe ser continua, con derivada no continua.

**(3)** $V(x)$ contiene funciones delta. En este caso $\psi''$ también contiene funciones delta: es proporcional al producto de una $\psi$ continua y una función delta en $V$. Por lo tanto $\psi'$ tiene discontinuidades finitas.

**(4)** $V(x)$ contiene una pared dura. Se dice que un potencial que es finito inmediatamente a la izquierda de $x = a$ y se vuelve infinito para $x > a$ tiene una pared dura en $x = a$. En tal caso, la función de onda se anulará para $x \geq a$. La pendiente $\psi'$ será finita cuando $x \to a$ por la izquierda, y se anulará para $x > a$. Por lo tanto $\psi'$ es discontinua en la pared.

En los dos primeros casos $\psi'$ es continua, y en los dos últimos puede tener una discontinuidad finita. En conclusión

$$\begin{gathered}
\text{Tanto } \psi \text{ como } \psi' \text{ son continuas a menos que el potencial tenga funciones}\\
\text{delta o paredes duras, en cuyo caso } \psi' \text{ puede tener discontinuidades finitas.} \qquad \text{(2.23)}
\end{gathered}$$

Demos un argumento ligeramente distinto para la continuidad de $\psi$ y $\dfrac{d\psi}{dx}$ en el caso de un potencial con una discontinuidad finita, como el escalón mostrado en la Fig. 1.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes10_ES/fig1.png)

Figura 1: Un potencial $V(x)$ con una discontinuidad finita en $x = a$.

Integremos ambos lados de (2.22) de $a - \epsilon$ a $a + \epsilon$, y luego tomemos $\epsilon \to 0$. Encontramos

$$\int_{a-\epsilon}^{a+\epsilon} \frac{d}{dx}\left(\frac{d\psi}{dx}\right) dx = -\frac{2m}{\hbar^2} \int_{a-\epsilon}^{a+\epsilon} dx\, (E - V(x))\psi(x) \qquad \text{(2.24)}$$

El integrando del lado izquierdo es una derivada total, así que tenemos

$$\left. \frac{d\psi}{dx} \right|_{a+\epsilon} - \left. \frac{d\psi}{dx} \right|_{a-\epsilon} = \frac{2m}{\hbar^2} \int_{a-\epsilon}^{a+\epsilon} dx\, (V(x) - E)\psi(x) \qquad \text{(2.25)}$$

Por definición, la discontinuidad de la derivada de $\psi$ en $x=a$ es el límite cuando $\epsilon \to 0$ del lado izquierdo:

$$\Delta_a\!\left(\frac{d\psi}{dx}\right) \equiv \lim_{\epsilon \to 0} \left( \left. \frac{d\psi}{dx} \right|_{a+\epsilon} - \left. \frac{d\psi}{dx} \right|_{a-\epsilon} \right) \qquad \text{(2.26)}$$

Sustituyendo en (2.25) tenemos entonces

$$\Delta_a\!\left(\frac{d\psi}{dx}\right) = \lim_{\epsilon \to 0} \frac{2m}{\hbar^2} \int_{a-\epsilon}^{a+\epsilon} dx\, (V(x) - E)\psi(x) \qquad \text{(2.27)}$$

El potencial $V$ es discontinuo pero no infinito alrededor de $x = a$, tampoco $\psi$ es infinita alrededor de $x = a$ y, por supuesto, se supone que $E$ es finita. A medida que el rango de integración se hace infinitesimalmente pequeño alrededor de $x = a$, el integrando permanece finito y la integral tiende a cero. Tenemos así

$$\Delta_a\!\left(\frac{d\psi}{dx}\right) = 0 \qquad \text{(2.28)}$$

No hay discontinuidad en $\dfrac{d\psi}{dx}$. Esto nos da una de nuestras condiciones de contorno.

Para conocer la continuidad de $\psi$ reconsideramos la primera integral de la ecuación diferencial. La integración que llevó a (2.25), ahora aplicada al rango desde $x_0 < a$ hasta $x$, arroja

$$\left. \frac{d\psi(x)}{dx} \right. = \left. \frac{d\psi}{dx} \right|_{x_0} - \frac{2m}{\hbar^2} \int_{x_0}^{x} (E - V(x'))\, dx' \qquad \text{(2.29)}$$

Nótese que la integral del lado derecho es una función acotada de $x$. Ahora integramos de nuevo desde $a - \epsilon$ hasta $a + \epsilon$. Dado que el primer término del lado derecho es una constante, encontramos

$$\psi(a+\epsilon) - \psi(a-\epsilon) = \left. \frac{d\psi}{dx} \right|_{x_0} \cdot 2\epsilon - \frac{2m}{\hbar^2} \int_{a-\epsilon}^{a+\epsilon} dx \int_{x_0}^{x} dx'\, (E - V(x')) \qquad \text{(2.30)}$$

Tomando el límite $\epsilon \to 0$, el primer término del lado derecho claramente se anula y el segundo término también tiende a cero porque $\int_{x_0}^{x} dx'\,(E - V(x'))$ es una función acotada de $x$. Como resultado tenemos

$$\Delta_a \psi = 0 \qquad \text{(2.31)}$$

lo que muestra que la función de onda es continua en $x = a$. Esta es nuestra segunda condición de contorno.

## 3. Partícula libre en un círculo

Consideremos ahora el problema de una partícula confinada a un círculo de circunferencia $L$. La coordenada a lo largo del círculo se denomina $x$ y podemos ver el círculo como el intervalo $x \in [0, L]$ con los extremos identificados. Quizás sea más claro matemáticamente pensar en el círculo como la recta real completa $x$ con la identificación

$$x \sim x + L \qquad \text{(3.1)}$$

lo que significa que dos puntos cuyas coordenadas están relacionadas de esta manera deben considerarse el mismo punto. De ello se sigue que tenemos la condición de periodicidad

$$\psi(x + L) = \psi(x) \qquad \text{(3.2)}$$

De esto se sigue que no solo $\psi$ es periódica, sino que todas sus derivadas también lo son.

Se supone que la partícula es libre y por lo tanto $V(x) = 0$. La ecuación de Schrödinger independiente del tiempo es entonces

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\, \psi(x) \qquad \text{(3.3)}$$

Antes de resolverla, mostremos que toda solución debe tener $E \geq 0$. Para ello multiplicamos la ecuación anterior por $\psi^*(x)$ e integramos sobre el círculo $x \in [0, L)$. Dado que $\psi$ está normalizada, obtenemos

$$-\frac{\hbar^2}{2m} \int_0^L \psi^*(x)\, \frac{d^2\psi}{dx^2}\, dx = E \int \psi^*(x)\psi(x)\, dx = E \qquad \text{(3.4)}$$

El integrando del lado izquierdo puede reescribirse como

$$-\frac{\hbar^2}{2m} \int_0^L \left[ \frac{d}{dx}\left(\psi^* \frac{d\psi}{dx}\right) - \frac{d\psi^*}{dx}\frac{d\psi}{dx} \right] dx = E \qquad \text{(3.5)}$$

y la derivada total se puede integrar

$$-\frac{\hbar^2}{2m} \left[ \left. \psi^* \frac{d\psi}{dx} \right|_{x=L} - \left. \psi^* \frac{d\psi}{dx} \right|_{x=0} \right] + \frac{\hbar^2}{2m} \int_0^L \left| \frac{d\psi}{dx} \right|^2 dx = E \qquad \text{(3.6)}$$

Dado que $\psi(x)$ y sus derivadas son periódicas, las contribuciones de $x = L$ y $x = 0$ se cancelan y quedamos con

$$E = \frac{\hbar^2}{2m} \int_0^L \left| \frac{d\psi}{dx} \right|^2 dx \geq 0 \qquad \text{(3.7)}$$

lo que establece nuestra afirmación. También vemos que $E = 0$ requiere que $\psi$ sea constante (¡y no nula!).

Habiendo mostrado que todas las soluciones deben tener $E \geq 0$, volvamos a la ecuación de Schrödinger, que puede reescribirse como

$$\frac{d^2\psi}{dx^2} = -\frac{2mE}{\hbar^2}\, \psi \qquad \text{(3.8)}$$

Podemos entonces definir $k$ mediante

$$k^2 \equiv \frac{2mE}{\hbar^2} \geq 0 \qquad \text{(3.9)}$$

Dado que $E \geq 0$, la constante $k$ es real. Nótese que esta definición es muy natural, ya que hace que

$$E = \frac{\hbar^2 k^2}{2m} \qquad \text{(3.10)}$$

lo cual significa que, como es habitual, $p = \hbar k$. Usando $k^2$, la ecuación diferencial se convierte en la familiar

$$\frac{d^2\psi}{dx^2} = -k^2\psi \qquad \text{(3.11)}$$

Podríamos escribir la solución general en términos de senos y cosenos de $kx$, pero usemos exponenciales complejas:

$$\psi(x) \sim e^{ikx} \qquad \text{(3.12)}$$

Esto resuelve la ecuación diferencial y, además, es un autoestado de momento. La condición de periodicidad (3.2) requiere

$$e^{ik(x+L)} = e^{ikx} \ \Rightarrow\ e^{ikL} = 1 \ \Rightarrow\ kL = 2\pi n\,, \ n \in \mathbb{Z} \qquad \text{(3.13)}$$

Vemos que el momento está cuantizado porque el número de onda está cuantizado. El número de onda tiene los valores discretos posibles

$$k_n \equiv \frac{2\pi n}{L}\,, \quad n \in \mathbb{Z} \qquad \text{(3.14)}$$

Todos los enteros, positivos y negativos, están permitidos y de hecho son necesarios porque todos corresponden a valores distintos del momento $p_n = \hbar k_n$. Las soluciones de la ecuación de Schrödinger pueden entonces indexarse mediante el entero $n$:

$$\psi_n(x) = N e^{ik_n x} \qquad \text{(3.15)}$$

donde $N$ es una constante de normalización real. Su valor se determina a partir de

$$1 = \int_0^L \psi_n^*(x)\psi_n(x)\, dx = \int_0^L N^2\, dx = N^2 L \ \Rightarrow\ N = \frac{1}{\sqrt{L}} \qquad \text{(3.16)}$$

así que tenemos

$$\psi_n(x) = \frac{1}{\sqrt{L}}\, e^{ik_n x} = \frac{1}{\sqrt{L}}\, e^{\frac{2\pi i n x}{L}} \qquad \text{(3.17)}$$

Las energías asociadas son

$$E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{\hbar^2\, 4\pi^2 n^2}{2mL^2} = \frac{2\pi^2 \hbar^2 n^2}{mL^2} \qquad \text{(3.18)}$$

Hay infinitos autoestados de energía. Tenemos estados degenerados porque $E_n$ es simplemente una función de $|n|$ y por lo tanto es la misma para $n$ y $-n$. En efecto, $\psi_n$ y $\psi_{-n}$ tienen ambos energía $E_n$. El único autoestado no degenerado es $\psi_0 = \dfrac{1}{\sqrt{L}}$, que es una función de onda constante con energía cero.

Cada vez que encontramos autoestados de energía degenerados debemos preguntarnos qué hace diferentes a esos estados, dado que tienen la misma energía. Para responder a esto hay que encontrar un observable que tome valores distintos en los estados. Afortunadamente, en nuestro caso conocemos la respuesta. Nuestros estados degenerados pueden distinguirse por su momento: $\psi_n$ tiene momento $\dfrac{2\pi n \hbar}{L}$ y $\psi_{-n}$ tiene momento $\left(-\dfrac{2\pi n \hbar}{L}\right)$.

Dados dos autoestados de energía degenerados, cualquier combinación lineal de estos estados es un autoestado con la misma energía. En efecto, si

$$\hat{H}\psi_1 = E\psi_1\,, \qquad \hat{H}\psi_2 = E\psi_2 \qquad \text{(3.19)}$$

entonces

$$\hat{H}(a\psi_1 + b\psi_2) = a\hat{H}\psi_1 + b\hat{H}\psi_2 = aE\psi_1 + bE\psi_2 = E(a\psi_1 + b\psi_2) \qquad \text{(3.20)}$$

Por lo tanto podemos formar dos combinaciones lineales de los autoestados degenerados $\psi_n$ y $\psi_{-n}$ para obtener otra descripción de los autoestados de energía:

$$\psi_n + \psi_{-n} \sim \cos(k_n x)\,,$$

$$\psi_n - \psi_{-n} \sim \sin(k_n x)\,. \qquad \text{(3.21)}$$

Aunque estos son autoestados de energía reales, no son autoestados de momento. Solo nuestras exponenciales son autoestados simultáneos tanto de $\hat{H}$ como de $\hat{p}$.

Los autoestados de energía $\psi_n$ son automáticamente ortonormales, ya que son autoestados de $\hat{p}$ sin degeneraciones (y, como recordarán, los autoestados de un operador hermítico con autovalores distintos son automáticamente ortogonales):

$$\int_0^L \psi_n^*(x)\psi_m(x)\, dx = \frac{1}{L} \int_0^L e^{\frac{2\pi i (m-n) x}{L}}\, dx = \delta_{mn} \qquad \text{(3.22)}$$

También son completos: podemos entonces construir una función de onda general como una superposición que es de hecho una serie de Fourier. Para cualquier $\Psi(x,0)$ que satisfaga la condición de periodicidad, podemos escribir

$$\Psi(x, 0) = \sum_{n \in \mathbb{Z}} a_n \psi_n(x) \qquad \text{(3.23)}$$

donde, como debe comprobarse, los coeficientes $a_n$ se determinan mediante las integrales

$$a_n = \int_0^L dx\, \psi_n^*(x)\, \Psi(x, 0) \qquad \text{(3.24)}$$

El estado inicial $\Psi(x, 0)$ se evoluciona entonces fácilmente en el tiempo:

$$\Psi(x, t) = \sum_{n \in \mathbb{Z}} a_n \psi_n(x)\, e^{-\frac{iE_n t}{\hbar}} \qquad \text{(3.25)}$$

[1]

------------------------------------------------------------------------

MIT OpenCourseWare

https://ocw.mit.edu

8.04 Física Cuántica I

Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

[1] Andrew Turner transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.
