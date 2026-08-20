# Clase 8[1]

## Vídeos de esta clase (YouTube)

**Lección 8: Uncovering momentum space. Expectation values and their time dependence.**

- [Fourier transforms and delta functions](https://www.youtube.com/watch?v=8abBLKEZLaI)
- [Parseval identity](https://www.youtube.com/watch?v=i-bP2OkQxUI)
- [Three-dimensional Fourier transforms](https://www.youtube.com/watch?v=MJM1AzpB6Y4) (06:04)
- [Expectation values of operators](https://www.youtube.com/watch?v=XQKV-hpsurs)
- [Time dependence of expectation values](https://www.youtube.com/watch?v=AnzhigYawy8)

------------------------------------------------------------------------

B. Zwiebach

29 de febrero de 2016

## Contenido

1.  Descubriendo el espacio de momentos
2.  Valores esperados de operadores
3.  Dependencia temporal de los valores esperados

## 1. Descubriendo el espacio de momentos

Comenzamos ahora una serie de desarrollos que conducen a la idea del espacio de momentos como contrapartida o dual del espacio de posiciones. En esta sección la dependencia temporal de las funciones de onda no jugará ningún papel. Por lo tanto, simplemente suprimiremos la dependencia temporal. Se puede imaginar que todas las funciones de onda están evaluadas en el tiempo igual a cero o en algún tiempo arbitrario $t_0$.

Comenzamos recordando las identidades clave del teorema de Fourier:

$$\Psi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi(k) e^{ikx}\, dk \,,$$

$$\Phi(k) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Psi(x) e^{-ikx}\, dx \,. \qquad \text{(1.1)}$$

La transformada de Fourier $\Phi(k)$ contiene toda la información que porta la función de onda $\Psi(x)$. Esto es evidente porque conocer $\Phi(k)$ equivale a conocer $\Psi(x)$. La función $\Phi(k)$ actúa también como el peso con el que sumamos las ondas planas de momento $\hbar k$ para formar $\Psi(x)$.

Ahora veremos que la consistencia de las ecuaciones anteriores puede usarse para deducir una representación integral de la función delta. Dicha representación es una herramienta necesaria para nuestra discusión posterior. La idea es reemplazar $\Phi(k)$ en la primera ecuación por el valor dado en la segunda ecuación. Para mantener la notación clara, debemos usar $x'$ como variable muda de integración en la segunda ecuación. Tenemos

$$\Psi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} dk\, e^{ikx} \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} dx'\, e^{-ikx'}\Psi(x')$$

$$= \int_{-\infty}^{\infty} dx'\, \Psi(x') \underbrace{\frac{1}{2\pi}\int_{-\infty}^{\infty} dk\, e^{ik(x-x')}}_{} \,. \qquad \text{(1.2)}$$

Observemos el tipo de integral. El factor indicado por la llave reduce la integral en $x'$ a una evaluación en $x$. Sabemos que $\delta(x'-x)$ es la función tal que, para una $f(x)$ general,

$$\int_{-\infty}^{\infty} dx'\, f(x')\, \delta(x'-x) = f(x)\,, \qquad \text{(1.3)}$$

y por lo tanto concluimos que el factor indicado por la llave es una función delta

$$\delta(x'-x) = \frac{1}{2\pi}\int_{-\infty}^{\infty} dk\, e^{ik(x-x')}\,. \qquad \text{(1.4)}$$

En esta integral se puede hacer $k \to -k$, y como $dk$ es invariante bajo este cambio, encontramos que $\delta(x'-x) = \delta(x-x')$, o más sencillamente, $\delta(x) = \delta(-x)$. Registraremos la representación integral de la función delta usando el otro signo:

$$\delta(x-x') = \frac{1}{2\pi}\int_{-\infty}^{\infty} dk\, e^{ik(x-x')}\,. \qquad \text{(1.5)}$$

Otra propiedad útil de las funciones delta es

$$\delta(ax) = \frac{1}{|a|}\delta(x)\,. \qquad \text{(1.6)}$$

Llegados a este punto preguntamos: ¿cómo se ve la condición de normalización de $\Psi(x)$ en términos de $\Phi(k)$? Simplemente debemos calcular. Tenemos

$$\int_{-\infty}^{\infty} dx\, \Psi^*(x)\Psi(x) = \int_{-\infty}^{\infty} dx\, \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \Phi^*(k) e^{-ikx}\, dk\, \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \Phi(k') e^{ik'x}\, dk' \,. \qquad \text{(1.7)}$$

Reordenando las integrales para hacer primero la integral en $x$ escribimos

$$\int_{-\infty}^{\infty} dx\, \Psi^*(x)\Psi(x) = \int_{-\infty}^{\infty} dk \int_{-\infty}^{\infty} dk'\, \Phi^*(k)\Phi(k') \frac{1}{2\pi}\int_{-\infty}^{\infty} dx\, e^{i(k'-k)x}$$

$$= \int_{-\infty}^{\infty} dk\, dk'\, \Phi^*(k)\Phi(k') \delta(k'-k)$$

$$= \int_{-\infty}^{\infty} dk\, \Phi^*(k)\Phi(k)\,, \qquad \text{(1.8)}$$

donde reconocimos la presencia de una función delta y realizamos la integral sobre $k'$. Nuestro resultado final es entonces

$$\int_{-\infty}^{\infty} dx\, |\Psi(x)|^2 = \int_{-\infty}^{\infty} dk\, |\Phi(k)|^2\,. \qquad \text{(1.9)}$$

Esto se conoce como el teorema de Parseval, o más generalmente, el teorema de Plancherel. Esta ecuación relaciona la normalización de $\Psi(x)$ con una normalización bastante análoga para $\Phi(k)$. Esto sugiere que, al igual que para $|\Psi(x)|^2$, podríamos tener una interpretación probabilística para $|\Phi(k)|^2$.

Puesto que físicamente asociamos nuestras ondas planas con autoestados de momento, reescribamos el teorema de Parseval usando el momento $p = \hbar k$. En lugar de integrales sobre $k$ tendremos integrales sobre $p$. Definiendo $\tilde\Phi(p) = \Phi(k)$, las ecuaciones (1.1) se convierten en

$$\Psi(x) = \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^{\infty} \tilde\Phi(p)\, e^{ipx/\hbar}\, dp \,,$$

$$\tilde\Phi(p) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Psi(x) e^{-ipx/\hbar}\, dx \,. \qquad \text{(1.10)}$$

Para obtener un par de ecuaciones más simétrico podemos redefinir la función $\tilde\Phi(p)$. Haremos $\tilde\Phi(p) \to \Phi(p)\sqrt{\hbar}$ en las ecuaciones (1.10). Obtenemos entonces la forma final de las relaciones de Fourier en términos del momento:

$$\Psi(x) = \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^{\infty} \Phi(p)\, e^{ipx/\hbar}\, dp \,,$$

$$\Phi(p) = \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^{\infty} \Psi(x) e^{-ipx/\hbar}\, dx \,. \qquad \text{(1.11)}$$

Análogamente, el teorema de Parseval (1.9) se convierte en

$$\int_{-\infty}^{\infty} dx\, |\Psi(x)|^2 = \int_{-\infty}^{\infty} dp\, |\Phi(p)|^2\,. \qquad \text{(1.12)}$$

**Ejercicio.** Verifique que las redefiniciones que hicimos para llegar a (1.11) efectivamente producen (1.12) partiendo de (1.9).

Nuestra interpretación de la ecuación superior en (1.11) es que $\Phi(p)$ denota el peso con el que sumamos el estado de momento $e^{ipx/\hbar}$ en la superposición que representa a $\Psi(x)$. Este estado de momento $e^{ipx/\hbar}$ es un autoestado del operador de momento $\hat p$ con autovalor $p$. Así como decimos que $\Psi(x)$ es la función de onda en el espacio de posiciones $x$, podemos pensar en $\Phi(p)$ como la función de onda en el espacio de momentos $p$. La identidad de Parseval (1.12) sugiere que $\Phi(p)$ tiene también una interpretación probabilística. Dado que una $\Psi(x)$ correctamente normalizada conduce a una $\Phi(p)$ que satisface $\int dp\, |\Phi(p)|^2 = 1$, postulamos que:

$$\begin{gathered}
|\Phi(p)|^2\, dp \ \text{es la probabilidad de encontrar la partícula}\\
\text{con momento en el rango } (p, p+dp)\,. \qquad \text{(1.13)}
\end{gathered}$$

Esto completa bastante bien la analogía entre el espacio de posiciones y el espacio de momentos.

Consideremos la generalización a 3D. El teorema de Fourier en el lenguaje del espacio de momentos (es decir, usando $p$ en lugar de $k$) toma la forma

$$\Psi(\mathbf{x}) = \frac{1}{(2\pi\hbar)^{3/2}} \int_{-\infty}^{\infty} d^3p\, \Phi(\mathbf{p})\, e^{i\mathbf{p}\cdot\mathbf{x}/\hbar} \,,$$

$$\Phi(\mathbf{p}) = \frac{1}{(2\pi\hbar)^{3/2}} \int_{-\infty}^{\infty} d^3x\, \Psi(\mathbf{x})\, e^{-i\mathbf{p}\cdot\mathbf{x}/\hbar} \,. \qquad \text{(1.14)}$$

Tal como hicimos en el caso 1D, si insertamos la transformada de Fourier en la expresión para $\Psi(\mathbf{x})$, encontramos una representación integral de la función $\delta$ en 3D

$$\Psi(\mathbf{x}) = \frac{1}{(2\pi\hbar)^3} \int d^3p\, e^{i\mathbf{p}\cdot\mathbf{x}/\hbar} \int d^3x'\, \Psi(\mathbf{x}')\, e^{-i\mathbf{p}\cdot\mathbf{x}'/\hbar}$$

$$= \int d^3x'\, \Psi(\mathbf{x}')\, \frac{1}{(2\pi\hbar)^3} \int d^3p\, e^{i\mathbf{p}\cdot(\mathbf{x}-\mathbf{x}')/\hbar}$$

$$= \int d^3x'\, \Psi(\mathbf{x}')\, \frac{1}{(2\pi)^3} \int d^3k\, e^{i\mathbf{k}\cdot(\mathbf{x}-\mathbf{x}')} \,, \qquad \text{(1.15)}$$

lo que lleva a la identificación

$$\delta^3(\mathbf{x}-\mathbf{x}') = \frac{1}{(2\pi)^3} \int d^3k\, e^{i\mathbf{k}\cdot(\mathbf{x}-\mathbf{x}')} \,. \qquad \text{(1.16)}$$

Entonces es directo deducir la identidad de Parseval (¡ejercicio!). Encontramos

$$\int_{-\infty}^{\infty} d^3x\, |\Psi(\mathbf{x})|^2 = \int d^3p\, |\Phi(\mathbf{p})|^2\,. \qquad \text{(1.17)}$$

Usamos en el espacio de momentos 3D la misma interpretación probabilística: $|\Phi(\mathbf{p})|^2\, d^3p$ es la probabilidad de encontrar la partícula con momento en el rango $d^3p$ alrededor de $\mathbf{p}$.

## 2. Valores esperados de operadores

Consideremos una variable aleatoria $Q$ que toma valores en el conjunto $\{Q_1, \ldots, Q_n\}$ con probabilidades respectivas $\{p_1, \ldots, p_n\}$. El valor esperado $\langle Q \rangle$ (o valor esperado) de $Q$ es el valor promedio que esperamos encontrar tras una observación repetida de $Q$, y viene dado por la fórmula

$$\langle Q \rangle = \sum_{i=1}^{n} Q_i\, p_i \,. \qquad \text{(2.18)}$$

Como hemos visto, en un sistema cuántico la probabilidad de que una partícula se encuentre en $[x, x+dx]$ en el instante $t$ está dada por

$$\Psi^*(x,t)\Psi(x,t)\, dx\,. \qquad \text{(2.19)}$$

Así, el valor esperado de $x$, denotado por $\langle \hat x \rangle$, viene dado por

$$\langle \hat x \rangle \equiv \int_{-\infty}^{\infty} x\, \Psi^*(x,t)\Psi(x,t)\, dx\,. \qquad \text{(2.20)}$$

Nótese que este valor esperado depende de $t$. ¿A qué corresponde físicamente $\langle \hat x \rangle$? Si consideramos muchas copias del sistema físico, y medimos la posición $x$ en el instante $t$ en todas ellas, entonces el valor promedio registrado convergerá a $\langle \hat x \rangle$ a medida que el número de medidas se aproxime a infinito.

Discutamos ahora el valor esperado del momento. Puesto que hemos establecido que

$$\Phi^*(p,t)\Phi(p,t)\, dp \qquad \text{(2.21)}$$

es la probabilidad de encontrar la partícula con momento en el rango $[p, p+dp]$ en el instante $t$, definimos el valor esperado $\langle \hat p \rangle$ del operador de momento como

$$\langle \hat p \rangle \equiv \int_{-\infty}^{\infty} p\, \Phi^*(p,t)\Phi(p,t)\, dp\,. \qquad \text{(2.22)}$$

Ahora manipularemos esta expresión para ver qué forma toma en el espacio de configuración. Usando (1.11) y su versión compleja conjugada tenemos

$$\langle \hat p \rangle = \int_{-\infty}^{\infty} p\, \Phi^*(p,t)\Phi(p,t)\, dp$$

$$= \int_{-\infty}^{\infty} dp\, p \int_{-\infty}^{\infty} \frac{dx}{\sqrt{2\pi\hbar}}\, e^{ipx/\hbar}\Psi^*(x,t) \int_{-\infty}^{\infty} \frac{dx'}{\sqrt{2\pi\hbar}}\, e^{-ipx'/\hbar}\Psi(x',t)$$

$$= \frac{1}{2\pi\hbar} \int_{-\infty}^{\infty} dx\, \Psi^*(x,t) \int_{-\infty}^{\infty} dx'\, \Psi(x',t) \int_{-\infty}^{\infty} dp\, p\, e^{ipx/\hbar}e^{-ipx'/\hbar} \qquad \text{(2.23)}$$

$$= \frac{1}{2\pi\hbar} \int_{-\infty}^{\infty} dx\, \Psi^*(x,t) \int_{-\infty}^{\infty} dx'\, \Psi(x',t) \int_{-\infty}^{\infty} dp\, \left(\frac{\hbar}{i}\frac{\partial}{\partial x}\right) e^{ipx/\hbar}e^{-ipx'/\hbar}$$

$$= \int_{-\infty}^{\infty} dx\, \Psi^*(x,t) \int_{-\infty}^{\infty} dx'\, \Psi(x',t) \frac{\hbar}{i}\frac{\partial}{\partial x} \frac{1}{2\pi\hbar}\int_{-\infty}^{\infty} dp\, e^{ipx/\hbar}e^{-ipx'/\hbar}\,.$$

Haciendo $p = \hbar u$ en la integral final tenemos

$$\frac{1}{2\pi\hbar} \int_{-\infty}^{\infty} dp\, e^{ipx/\hbar}e^{-ipx'/\hbar} = \frac{1}{2\pi}\int_{-\infty}^{\infty} du\, e^{iu(x-x')} = \delta(x-x')\,. \qquad \text{(2.24)}$$

Como resultado, tenemos

$$\langle \hat p \rangle = \int_{-\infty}^{\infty} dx\, \Psi^*(x,t) \int_{-\infty}^{\infty} dx'\, \Psi(x',t) \frac{\hbar}{i}\frac{\partial}{\partial x} \delta(x-x')$$

$$= \int_{-\infty}^{\infty} dx\, \Psi^*(x,t) \frac{\hbar}{i}\frac{\partial}{\partial x} \int_{-\infty}^{\infty} dx'\, \Psi(x',t)\delta(x'-x)\,, \qquad \text{(2.25)}$$

donde cambiamos el orden de integración. La integral en $x'$ se realiza ahora fácilmente y encontramos

$$\langle \hat p \rangle = \int_{-\infty}^{\infty} dx\, \Psi^*(x,t) \left(\frac{\hbar}{i}\frac{\partial}{\partial x}\right) \Psi(x,t)\,, \qquad \text{(2.26)}$$

Hemos así demostrado que

$$\langle \hat p \rangle = \int_{-\infty}^{\infty} dx\, \Psi^*(x,t)\, \hat p\, \Psi(x,t)\,, \qquad \hat p = \frac{\hbar}{i}\frac{\partial}{\partial x}\,. \qquad \text{(2.27)}$$

Nótese la posición del operador $\hat p$: actúa sobre $\Psi(x)$. Esto motiva la siguiente definición para el valor esperado $\langle \hat Q \rangle$ de cualquier operador $\hat Q$:

$$\langle \hat Q \rangle = \int_{-\infty}^{\infty} dx\, \Psi^*(x,t)\, \hat Q\, \Psi(x,t)\,. \qquad \text{(2.28)}$$

**Ejemplo:** Consideremos el operador de energía cinética $\hat T$ para una partícula que se mueve en 1D:

$$\hat T = \frac{\hat p^2}{2m} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}\,. \qquad \text{(2.29)}$$

La definición da

$$\langle \hat T \rangle = -\frac{\hbar^2}{2m} \int dx\, \Psi^*(x,t)\, \frac{\partial^2}{\partial x^2}\Psi(x,t)\,. \qquad \text{(2.30)}$$

La energía cinética es un operador positivo (por ser proporcional al cuadrado del operador de momento). Por lo tanto es de interés hacer manifiesta esta positividad. Integrando por partes una de las derivadas en $x$ e ignorando los términos de frontera, que se supone que se anulan, encontramos

$$\langle \hat T \rangle = \frac{\hbar^2}{2m} \int dx\, \left| \frac{\partial \Psi(x,t)}{\partial x} \right|^2\,. \qquad \text{(2.31)}$$

¡Esto es manifiestamente positivo! El valor esperado de $\hat T$ también puede calcularse en el espacio de momentos usando la interpretación probabilística que dio lugar a (2.22):

$$\langle \hat T \rangle = \int dp\, \frac{p^2}{2m}\, |\Phi(p,t)|^2\,. \qquad \text{(2.32)}$$

Otros ejemplos de operadores cuyos valores esperados podemos ahora calcular son el operador de momento $\hat p \to \frac{\hbar}{i}\nabla$ en 3D, el operador de energía potencial $V(\hat{\mathbf{x}})$, y el operador de momento angular

$$\hat{\mathbf L} = \hat{\mathbf r} \times \hat{\mathbf p} = \left( \hat y \hat p_z - \hat z \hat p_y,\ \hat z \hat p_x - \hat x \hat p_z,\ \hat x \hat p_y - \hat y \hat p_x \right)$$

$$= \frac{\hbar}{i}\left( y\frac{\partial}{\partial z} - z\frac{\partial}{\partial y},\ z\frac{\partial}{\partial x} - x\frac{\partial}{\partial z},\ x\frac{\partial}{\partial y} - y\frac{\partial}{\partial x} \right)\,. \qquad \text{(2.33)}$$

## 3. Dependencia temporal de los valores esperados

Los valores esperados de los operadores son, en general, dependientes del tiempo porque las funciones de onda que representan los estados dependen del tiempo. Consideraremos aquí operadores que no tienen dependencia temporal explícita, es decir, operadores que no la tienen:

$$i\hbar \frac{d}{dt}\langle Q \rangle = i\hbar \frac{d}{dt} \int_{-\infty}^{\infty} d^3x\, \Psi^*(\mathbf{x},t)\, \hat Q\, \Psi(\mathbf{x},t)$$

$$= i\hbar \int_{-\infty}^{\infty} d^3x\, \left[ \frac{\partial \Psi^*}{\partial t}\, \hat Q\, \Psi + \Psi^*\, \hat Q\, \frac{\partial \Psi}{\partial t} \right]$$

$$= i\hbar \int_{-\infty}^{\infty} d^3x\, \left[ \frac{i}{\hbar}(\hat H\Psi)^*\, \hat Q\, \Psi - \frac{i}{\hbar}\Psi^*\, \hat Q\,(\hat H\Psi) \right] \qquad \text{(3.34)}$$

$$= \int_{-\infty}^{\infty} d^3x\, \left[ \Psi^*\, \hat Q\hat H\, \Psi - (\hat H\Psi^*)\, \hat Q\, \Psi \right]$$

Recordamos ahora la hermiticidad de $\hat H$, lo que implica que

$$\int_{-\infty}^{\infty} dx\, (\hat H\Psi_1)^*\, \Psi_2 = \int_{-\infty}^{\infty} dx\, \Psi_1^*\, \hat H \Psi_2\,. \qquad \text{(3.35)}$$

Esto puede aplicarse al segundo término del último lado derecho de (3.34) para trasladar $\hat H$ hacia la otra función de onda

$$i\hbar \frac{d}{dt}\langle Q \rangle = \int_{-\infty}^{\infty} d^3x\, \left[ \Psi^*\, \hat Q\hat H\, \Psi - \Psi^*\, \hat H\hat Q\, \Psi \right]$$

$$= \int_{-\infty}^{\infty} d^3x\, \Psi^*\, \left[ \hat Q, \hat H \right] \Psi\,, \qquad \text{(3.36)}$$

donde observamos la aparición del conmutador. En definitiva, hemos demostrado que para operadores $\hat Q$ que no dependen explícitamente del tiempo,

$$i\hbar \frac{d}{dt}\langle \hat Q \rangle = \left\langle \left[ \hat Q, \hat H \right] \right\rangle\,. \qquad \text{(3.37)}$$

Nótese que el conmutador satisface las siguientes propiedades (tarea):

$$[A,B] = -[B,A] \qquad \text{(3.38)}$$

$$[A,A] = 0 \qquad \text{(3.39)}$$

$$[A, B+C] = [A,B] + [A,C] \qquad \text{(3.40)}$$

$$[A, BC] = [A,B]\, C + B\, [A,C] \qquad \text{(3.41)}$$

$$[AB, C] = A\, [B,C] + [A,C]\, B \qquad \text{(3.42)}$$

$$0 = [A,[B,C]] + [B,[C,A]] + [C,[A,B]]\,. \qquad \text{(3.43)}$$

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.*

[1] Andrew Turner transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.
