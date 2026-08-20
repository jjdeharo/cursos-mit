# Clases 21 y 22: El Átomo de Hidrógeno

## Vídeos de esta clase (YouTube)

**Lección 21: Legendre equation. Radial equation. Hydrogen atom 2-body problem.**

- [Associated Legendre functions and spherical harmonics](https://www.youtube.com/watch?v=Lt2Y6fLJ09Q)
- [Orthonormality of spherical harmonics](https://www.youtube.com/watch?v=gKSRrTik1SA)
- [Effective potential and boundary conditions at r=0](https://www.youtube.com/watch?v=_XDm2cxC-UU)
- [Hydrogen atom two-body problem](https://www.youtube.com/watch?v=7q32Wnm4dEw)

**Lección 22: Hydrogen atom (cont.). Differential equation, series solution and quantum numbers**

- [Center of mass and relative motion wavefunctions](https://www.youtube.com/watch?v=dVWKsiaAZ14)
- [Scales of the hydrogen atom](https://www.youtube.com/watch?v=GWMeYKUvj7Y)
- [Schrödinger equation for hydrogen](https://www.youtube.com/watch?v=KfbvrGt3MlI)
- [Series solution and quantization of the energy](https://www.youtube.com/watch?v=3VXLIF2DpHI)
- [Energy eigenstates of hydrogen](https://www.youtube.com/watch?v=Z4CSAWrzguY)

------------------------------------------------------------------------

*B. Zwiebach* *4 de mayo de 2016*

## Contenido

1.  El átomo de hidrógeno
2.  Espectro del átomo de hidrógeno

## 1. El átomo de hidrógeno

Nuestro objetivo aquí es mostrar que el problema cuántico de dos cuerpos del átomo de hidrógeno puede reformularse como uno en el que tenemos grados de libertad del centro de masas que se comportan como una partícula libre, y grados de libertad del movimiento relativo cuya dinámica está controlada por un potencial central.

El átomo de hidrógeno consiste en un protón y un electrón moviéndose en tres dimensiones. Denotamos los operadores de posición y momento del protón como $\hat{x}_p$, $\hat{p}_p$, y los del electrón como $\hat{x}_e$, $\hat{p}_e$. Estas son variables canónicas, es decir, satisfacen las relaciones de conmutación canónicas:

$$[(\hat{x}_p)_i, (\hat{p}_p)_j] = i\hbar \delta_{ij}, \qquad [(\hat{x}_e)_i, (\hat{p}_e)_j] = i\hbar \delta_{ij}. \qquad \text{(1.1)}$$

Aquí los subíndices $i, j = 1, 2, 3$ denotan las distintas componentes de los operadores vectoriales. Además, las variables del protón conmutan con las variables del electrón. Tenemos dos pares de variables canónicas independientes.

La función de onda del sistema es una función de las posiciones de ambas partículas:

$$\Psi(x_p, x_e), \qquad \text{(1.2)}$$

y la cantidad

$$|\Psi(x_p, x_e)|^2 \, d^3x_p \, d^3x_e, \qquad \text{(1.3)}$$

es la probabilidad de encontrar al protón dentro de una ventana $d^3x_p$ de $x_p$ y al electrón dentro de una ventana $d^3x_e$ de $x_e$. El hamiltoniano del sistema viene dado por

$$\hat{H} = \frac{\hat{p}_p^2}{2m_p} + \frac{\hat{p}_e^2}{2m_e} + V(|x_e - x_p|). \qquad \text{(1.4)}$$

Nótese que la energía cinética es simplemente la suma de la energía cinética del protón y la energía cinética del electrón. El potencial depende únicamente de la magnitud de la separación entre las dos partículas, no de sus posiciones individuales.

Para simplificar el problema, introduciremos dos nuevos pares de variables canónicas independientes. El primer par está asociado al movimiento del centro de masas (CM). Introducimos el operador de momento total $\hat{P}$ y el operador de posición del CM $\hat{X}$, dados por

$$\hat{P} = \hat{p}_p + \hat{p}_e, \qquad \hat{X} = \frac{m_e \hat{x}_e + m_p \hat{x}_p}{m_e + m_p}. \qquad \text{(1.5)}$$

El operador $\hat{X}$ viene dado por la expresión habitual del centro de masas del sistema, pero con las posiciones sustituidas por operadores de posición. Usando las relaciones de conmutación (1.1), podemos mostrar que $\hat{X}$ y $\hat{P}$ son conjugados canónicos:

$$\begin{aligned}
\left[(\hat{X})_i, (\hat{P})_j\right] &= \left[\frac{m_e (\hat{x}_e)_i + m_p (\hat{x}_p)_i}{m_e + m_p}, (\hat{p}_p)_j + (\hat{p}_e)_j\right] \\
&= \frac{m_e}{m_e + m_p}[(\hat{x}_e)_i, (\hat{p}_e)_j] + \frac{m_p}{m_e + m_p}[(\hat{x}_p)_i, (\hat{p}_p)_j] \\
&= \frac{m_e}{m_e + m_p} i\hbar \delta_{ij} + \frac{m_p}{m_e + m_p} i\hbar \delta_{ij},
\end{aligned} \qquad \text{(1.6)}$$

lo que da como resultado esperado

$$\left[(\hat{X})_i, (\hat{P})_j\right] = i\hbar \delta_{ij}. \qquad \text{(1.7)}$$

Para el segundo par de variables canónicas definiremos operadores de posición y momento relativos. El operador de posición relativa es la variable natural implicada por la forma del potencial:

$$\hat{x} = \hat{x}_e - \hat{x}_p. \qquad \text{(1.8)}$$

Puesto que el segundo par de variables canónicas debe conmutar con el primer par, debemos comprobar que $x$, definido arriba, conmuta con $X$ y con $P$. La conmutación con $X$ es automática, y la conmutación con $P$ funciona gracias al signo menos en la definición anterior. Ahora debemos construir un operador de momento relativo $\hat{p}$ que sea canónicamente conjugado a $x$. Debe construirse a partir de los operadores de momento de las dos partículas, así que escribimos

$$\hat{p} = \alpha \hat{p}_e - \beta \hat{p}_p, \qquad \text{(1.9)}$$

con $\alpha$ y $\beta$ coeficientes a determinar. Para ser canónicamente conjugados, los operadores relativos deben satisfacer

$$[(\hat{x})_i, (\hat{p})_j] = i\hbar \delta_{ij} \ \Rightarrow \ \alpha + \beta = 1, \qquad \text{(1.10)}$$

usando las definiciones anteriores de $\hat{x}$ y $\hat{p}$ y los conmutadores del protón y del electrón. Finalmente, el momento relativo debe conmutar con la coordenada del CM

$$\left[(\hat{X})_i, (\hat{p})_j\right] = 0 \ \Rightarrow \ m_e \alpha - m_p \beta = 0. \qquad \text{(1.11)}$$

Las dos ecuaciones para $\alpha$ y $\beta$ pueden resolverse para encontrar

$$\alpha = \frac{m_p}{m_e + m_p}, \qquad \beta = \frac{m_e}{m_e + m_p}. \qquad \text{(1.12)}$$

Definimos la masa total $M$ y la masa reducida $\mu$ como sigue

$$M = m_e + m_p, \qquad \mu = \frac{m_e m_p}{m_e + m_p}. \qquad \text{(1.13)}$$

La masa reducida de un par de partículas con masas muy diferentes es aproximadamente igual a la masa de la partícula de menor masa. Usando estas definiciones

$$\alpha = \frac{\mu}{m_e}, \qquad \beta = \frac{\mu}{m_p}. \qquad \text{(1.14)}$$

Así, recopilando las variables relativas tenemos

$$\hat{p} = \mu \left(\frac{\hat{p}_e}{m_e} - \frac{\hat{p}_p}{m_p}\right) = \frac{m_p}{M}\hat{p}_e - \frac{m_e}{M}\hat{p}_p, \qquad \hat{x} = \hat{x}_e - \hat{x}_p. \qquad \text{(1.15)}$$

Nótese que el momento relativo $p$ puede escribirse en términos de velocidades como $p = \mu(v_e - v_p)$. El momento relativo se anula si el movimiento es puramente movimiento del CM, en cuyo caso las velocidades de las dos partículas son iguales.

Ahora podemos reescribir el hamiltoniano en términos de las nuevas variables. Despejando los operadores de momento originales en términos de $\hat{P}$ y $\hat{p}$, encontramos

$$\hat{p}_p = \frac{m_p}{M}\hat{P} - \hat{p}, \qquad \hat{p}_e = \frac{m_e}{M}\hat{P} + \hat{p}. \qquad \text{(1.16)}$$

Podemos entonces reescribir los términos cinéticos del hamiltoniano en la forma

$$\begin{aligned}
\frac{\hat{p}_p^2}{2m_p} + \frac{\hat{p}_e^2}{2m_e} &= \frac{1}{2m_p}\left(\frac{m_p^2}{M^2}\hat{P}^2 - \frac{2m_p}{M}\hat{P}\cdot\hat{p} + \hat{p}^2\right) \\
&\quad + \frac{1}{2m_e}\left(\frac{m_e^2}{M^2}\hat{P}^2 + \frac{2m_e}{M}\hat{P}\cdot\hat{p} + \hat{p}^2\right) \\
&= \frac{\hat{P}^2}{2M} + \frac{\hat{p}^2}{2\mu}.
\end{aligned} \qquad \text{(1.17)}$$

Afortunadamente el término que acopla los dos momentos se anula. Así, los grados de libertad del centro de masas y los grados de libertad relativos dan contribuciones independientes a la energía cinética. El hamiltoniano puede entonces escribirse como

$$\hat{H} = \frac{\hat{P}^2}{2M} + \frac{\hat{p}^2}{2\mu} + V(|\hat{x}|). \qquad \text{(1.18)}$$

En el espacio de posiciones, los operadores de momento total y relativo pueden expresarse como gradientes

$$\hat{P} \to \frac{\hbar}{i}\nabla_X, \qquad \hat{p} \to \frac{\hbar}{i}\nabla_x. \qquad \text{(1.19)}$$

Cada $\nabla$ lleva un subíndice que indica el tipo de coordenada respecto a la cual tomamos las derivadas. Del mismo modo que teníamos una función de onda $\Psi(x_e, x_p)$, las nuevas variables canónicas exigen que ahora pensemos en la función de onda como una función $\Psi(X, x)$ de las nuevas coordenadas.

Resolvemos la ecuación de Schrödinger independiente del tiempo mediante separación de variables

$$\Psi(X, x) = \Psi_{CM}(X)\Psi_{rel}(x). \qquad \text{(1.20)}$$

Sustituyendo esto en la ecuación de Schrödinger independiente del tiempo $\hat{H}\Psi = E\Psi$, llegamos a

$$\left[\frac{\hat{P}^2}{2M}\Psi_{CM}(X)\right]\Psi_{rel}(x) + \left[\frac{\hat{p}^2}{2\mu}\Psi_{rel}(x) + V(|\hat{x}|)\Psi_{rel}(x)\right]\Psi_{CM}(X) = E\Psi_{CM}(X)\Psi_{rel}(x). \qquad \text{(1.21)}$$

Dividiendo por la función de onda total $\Psi_{CM}(X)\Psi_{rel}(x)$, esto se convierte en

$$\frac{1}{\Psi_{CM}(X)}\left[\frac{\hat{P}^2}{2M}\Psi_{CM}(X)\right] + \frac{1}{\Psi_{rel}(x)}\left[\frac{\hat{p}^2}{2\mu} + V(|\hat{x}|)\right]\Psi_{rel}(x) = E. \qquad \text{(1.22)}$$

El primer término del lado izquierdo es una función únicamente de $X$, y el segundo término del lado izquierdo es una función únicamente de $x$. Su suma es igual a la constante $E$, y puesto que $x$ y $X$ son variables independientes, cada término debe ser individualmente constante. Igualamos entonces el primer término a la constante $E_{CM}$ y el segundo término a la constante $E_{rel}$, obteniendo las siguientes ecuaciones:

$$\frac{\hat{P}^2}{2M}\Psi_{CM}(X) = E_{CM}\Psi_{CM}(X), \qquad \text{(1.23)}$$

$$\left[\frac{\hat{p}^2}{2\mu} + V(|x|)\right]\Psi_{rel}(x) = E_{rel}\Psi_{rel}(x), \qquad \text{(1.24)}$$

$$E = E_{CM} + E_{rel}. \qquad \text{(1.25)}$$

Obtenemos dos ecuaciones de Schrödinger. La primera ecuación nos dice que el centro de masas se mueve como una partícula libre de masa $M$. Así, la energía del CM no está cuantizada y obtenemos soluciones de onda plana. La segunda ecuación corresponde al movimiento relativo, y como queríamos mostrar, se describe como un movimiento en un potencial central. La tercera ecuación nos dice que la energía total es la suma de la energía del centro de masas y la energía del movimiento relativo.

## 2. Espectro del átomo de hidrógeno

Ahora tenemos las herramientas para estudiar el átomo de hidrógeno, que tiene un potencial central dado por

$$V(r) = -\frac{Ze^2}{r}, \qquad \text{(2.1)}$$

donde $Z$ es el número de protones en el núcleo. Para el hidrógeno tenemos $Z = 1$. Pero conviene considerar $Z > 1$, en cuyo caso estamos describiendo el movimiento de un electrón alrededor del núcleo de algún otro átomo. También definiremos las siguientes constantes físicas.

- La constante de estructura fina $\alpha$: $\alpha = \dfrac{e^2}{\hbar c} \simeq \dfrac{1}{137}$.

- El radio de Bohr $a_0$. Esta es la escala de longitud característica del problema. Puede calcularse igualando las energías cinética y potencial expresadas en términos de $a_0$ e ignorando todas las constantes numéricas:

$$\frac{\hbar^2}{m_e a_0^2} = \frac{e^2}{a_0}. \qquad \text{(2.2)}$$

Aquí la masa debería ser la masa reducida, que en este caso puede tomarse con bastante precisión como la masa del electrón. Entonces tenemos explícitamente,

$$\begin{aligned}
a_0 &= \frac{\hbar^2}{m e^2} = \frac{\hbar^2 c^2}{e^2 m c^2} = \frac{\hbar c}{\dfrac{e^2}{\hbar c} m c^2} = \frac{\hbar c}{\alpha m c^2} \\
&= \frac{197\ \text{MeV fm}}{0.51 \times 10^6\ \text{eV}} \times 137 = \frac{1970\ \text{eV Angstrom}}{0.51 \times 10^6\ \text{eV}} \times 137 \\
&= 0.529\ \text{Angstroms} \simeq 53\ \text{pm}.
\end{aligned} \qquad \text{(2.3)}$$

Para la estimación de la escala de energía tenemos

$$\frac{e^2}{a_0} = e^2 \left(\frac{m e^2}{\hbar^2}\right) = \left(\frac{e^4}{\hbar^2 c^2}\right) m c^2 = \alpha^2 m c^2 = \frac{1}{(137)^2} \times (511\,000\ \text{eV}) \simeq 27.2\ \text{eV}. \qquad \text{(2.4)}$$

Hay otras longitudes características interesantes:

$$\alpha a_0 = \text{longitud de onda Compton del electrón} = \bar\lambda_e \simeq 390\ \text{fm}, \qquad \text{(2.5)}$$

$$\alpha^2 a_0 = \text{radio clásico del electrón} \simeq 2.8\ \text{fm}.$$

¡Pasemos ahora a trabajar! La ecuación radial de Schrödinger para estados ligados $E < 0$ es

$$\left[-\frac{\hbar^2}{2m}\frac{d^2}{dr^2} + \frac{\hbar^2 \ell(\ell+1)}{2mr^2} - \frac{Ze^2}{r}\right] u = E u. \qquad \text{(2.6)}$$

Podríamos denotar la función de onda $u$ como $u_{E\ell}$, ya que las soluciones dependerán ciertamente de $\ell$ y de la energía $E$. Como es habitual, nos gusta trabajar con una coordenada adimensional. Esto podría lograrse escribiendo $r = a_0 x$, con $x$ adimensional y $a_0$ portando las unidades de longitud de $r$. Será más conveniente usar una ligera variante para eliminar $Z$ de la ecuación y algunos factores de dos. Tomaremos la nueva coordenada adimensional $x$ definida por

$$r \equiv \frac{a_0}{2Z} x. \qquad \text{(2.7)}$$

La ecuación de Schrödinger se convierte entonces en

$$\begin{aligned}
&-\frac{\hbar^2}{2m}\frac{4Z^2}{a_0^2}\frac{d^2}{dx^2} + \frac{4Z^2\hbar^2}{a_0^2}\frac{\ell(\ell+1)}{2mx^2} - \frac{2Z^2 e^2}{a_0}\frac{1}{x}\Bigg] u = Eu \\
&\Rightarrow \ \frac{2\hbar^2 Z^2}{ma_0^2}\left[-\frac{d^2}{dx^2} + \frac{\ell(\ell+1)}{x^2}\right] u - \frac{2Z^2 e^2}{a_0}\frac{1}{x}\, u = Eu.
\end{aligned} \qquad \text{(2.8)}$$

Nótese que

$$\frac{2\hbar^2 Z^2}{ma_0^2} = \left(\frac{2\hbar^2 Z}{ma_0}\right)\left(\frac{me^2}{\hbar^2}\right) = \frac{2Ze^2}{a_0}, \qquad \text{(2.9)}$$

lo que reduce nuestra ecuación diferencial a

$$\left[-\frac{d^2}{dx^2} + \frac{\ell(\ell+1)}{x^2} - \frac{1}{x}\right] u = \frac{E}{\dfrac{2Ze^2}{a_0}} u. \qquad \text{(2.10)}$$

Definimos ahora el parámetro adimensional $\kappa$ que codifica la energía:

$$\kappa^2 = -\frac{E}{\dfrac{2Ze^2}{a_0}} > 0. \qquad \text{(2.11)}$$

$\kappa$ es una versión adimensional de la energía del estado ligado. La ecuación diferencial es entonces

$$\left[-\frac{d^2}{dx^2} + \frac{\ell(\ell+1)}{x^2} - \frac{1}{x}\right] u = -\kappa^2 u. \qquad \text{(2.12)}$$

Podemos simplificar aún más esta ecuación antes de resolverla examinando los casos límite. En el límite $x \to \infty$, los términos dominantes son la segunda derivada y el término del lado derecho, lo que da

$$\frac{d^2 u}{dx^2} = \kappa^2 u \implies u \sim e^{\pm \kappa x}. \qquad \text{(2.13)}$$

Puesto que $\kappa$ es adimensional, podemos hacer que el exponente anterior sea igual a una nueva coordenada adimensional $\rho$:

$$\rho \equiv \kappa x = \frac{2\kappa Z}{a_0} r. \qquad \text{(2.14)}$$

Esta vez obtenemos

$$\left[-\frac{d^2}{d\rho^2} + \frac{\ell(\ell+1)}{\rho^2} - \frac{1}{\kappa\rho}\right] u = -u. \qquad \text{(2.15)}$$

Nótese que no logramos que $\kappa$ desaparezca de la ecuación. Esto es una buena noticia: la ecuación debería fijar los valores posibles de $\kappa$ (o las energías posibles). La ecuación anterior no está del todo lista para una solución en serie: encontraríamos una relación de recurrencia de tres términos, que es bastante complicada. Para avanzar, discutimos el comportamiento para $\rho$ pequeño y grande.

Para $\rho \to \infty$ ahora obtenemos $u \sim e^{\pm\rho}$ y, por supuesto, esperamos que $u = e^{-\rho}$ por normalizabilidad. Como discutimos antes, para $\rho \to 0$ la solución radial debe tener la forma $u \sim \rho^{(\ell+1)}$. Esta información sobre el comportamiento para $\rho$ pequeño y grande sugiere un buen ansatz para $u(\rho)$

$$u(\rho) = \rho^{\ell+1} W(\rho) e^{-\rho}. \qquad \text{(2.16)}$$

donde $W(\rho)$ es una función aún por determinar, que esperamos que satisfaga una ecuación diferencial más sencilla. Para derivar esta ecuación diferencial para $W(\rho)$, sustituimos nuestro ansatz en la Ec. (2.15). Como ayuda intermedia para el cálculo, damos un resultado intermedio:

$$-u'' + \frac{\ell(\ell+1)}{\rho^2} u + u = \left[-W'' - \frac{2(\ell+1)}{\rho}W' + \frac{2(\ell+1)}{\rho}W + 2W'\right]\rho^{\ell+1} e^{-\rho}. \qquad \text{(2.17)}$$

Con un poco más de trabajo finalmente obtenemos la ecuación diferencial para $W$:

$$\rho \frac{d^2 W}{d\rho^2} + 2(\ell+1-\rho)\frac{dW}{d\rho} + \left[\frac{1}{\kappa} - 2(\ell+1)\right] W = 0. \qquad \text{(2.18)}$$

Esto parece un poco más complicado que la ecuación diferencial con la que comenzamos, pero conduce a una relación de recurrencia de un solo paso muy agradable. Como es habitual, escribimos $W$ como una expansión en serie

$$W = \sum_{k=0}^{\infty} a_k \rho^k, \qquad \text{(2.19)}$$

y sustituyendo de nuevo en (2.18), agrupamos términos de orden $\rho^k$ para derivar una relación de recurrencia

$$a_{k+1}\left[k(k+1) + 2(\ell+1)(k+1)\right] - 2k a_k + \left[\frac{1}{\kappa} - 2(\ell+1)\right] a_k = 0,$$

$$\Rightarrow \ a_{k+1}\left(k(k+1) + 2(\ell+1)(k+1)\right) = a_k\left[2(k+\ell+1) - \frac{1}{\kappa}\right], \qquad \text{(2.20)}$$

lo que da

$$\frac{a_{k+1}}{a_k} = \frac{2(k+\ell+1) - \dfrac{1}{\kappa}}{(k+1)(k+2\ell+2)}. \qquad \text{(2.21)}$$

Un examen detallado muestra que, para funciones de onda normalizables, la serie debe terminar. Para ver esto, examinamos el comportamiento para $k$ grande de la razón anterior:

$$\frac{a_{k+1}}{a_k} \simeq \frac{2k}{k^2} = \frac{2}{k}. \qquad \text{(2.22)}$$

Nótese que $\dfrac{2}{k+1} < \dfrac{2}{k}$; así, si la razón $\dfrac{2}{k}$ conduce a una divergencia, también lo hará la razón $\dfrac{2}{k+1}$. Tomando

$$\frac{a_{k+1}}{a_k} = \frac{2}{k+1} \ \Rightarrow \ a_{k+1} = \frac{2}{k+1} a_k, \qquad \text{(2.23)}$$

y esto se resuelve mediante

$$a_k = \frac{2^k}{k!} a_0. \qquad \text{(2.24)}$$

Por lo tanto, la suma

$$W = \sum_{k=0}^{\infty} a_k \rho^k \simeq a_0 \sum_{k=0}^{\infty} \frac{2^k \rho^k}{k!} = a_0 e^{2\rho}. \qquad \text{(2.25)}$$

Esto es precisamente suficiente para hacer que el ansatz en (2.16) sea no normalizable.

Para obtener una solución normalizable, la serie para $W$ debe terminar. Supongamos que $W$ es un polinomio de grado $N$, de modo que los coeficientes satisfacen

$$a_N \neq 0 \quad \text{y} \quad a_{N+1} = 0. \qquad \text{(2.26)}$$

De la Ec. (2.21) esto implica

$$\frac{1}{\kappa} = 2(N+\ell+1). \qquad \text{(2.27)}$$

¡La cuantización ha ocurrido! El parámetro que codifica la energía, $\kappa$, está ahora relacionado con números enteros. Nótese que $\ell$ puede tomar valores $\ell = 0, 1, 2, \ldots$, como corresponde a un número cuántico de momento angular. Además, $N$ puede tomar valores $N = 0, 1, 2, \ldots$, ya que existe un polinomio de grado cero, que es igual a una constante. Definimos el número cuántico principal $n$ como sigue:

$$n \equiv N + \ell + 1 = \frac{1}{2\kappa}, \quad \text{con } \ell = 0, 1, 2, \ldots, \ N = 0, 1, 2, \ldots, \ \text{y } n = 1, 2, 3, \ldots \qquad \text{(2.28)}$$

Es importante notar que, para $n$ fijo, debemos tener

$$0 \le \ell \le n-1, \qquad \text{y} \qquad 0 \le N \le n-1. \qquad \text{(2.29)}$$

Si $n$ y $\ell$ son conocidos, $N$ queda determinado a partir de $N + \ell + 1 = n$. Así, los números cuánticos independientes hasta ahora son $n$ y $\ell$. Es interesante notar que las energías dependen únicamente de $n$, ya que $\kappa$ depende únicamente de $n$. Usando la Ec. (2.11), la dependencia de la energía respecto al número cuántico principal viene dada por

$$E = -\frac{2Z^2 e^2}{a_0}\kappa^2, \qquad \text{(2.30)}$$

y usando $\kappa = \dfrac{1}{2n}$ obtenemos

$$E = -\frac{Z^2 e^2}{2a_0}\frac{1}{n^2}. \qquad \text{(2.31)}$$

¡Estos son los niveles de energía del átomo de hidrógeno! Puesto que para cualquier valor fijo de $n > 1$ hay varios valores posibles de $\ell$, el espectro es altamente degenerado. Aún más, cada valor de $\ell$ corresponde a $2\ell+1$ estados, dados los valores posibles de $m$. Una manera de visualizar el espectro se muestra en la Figura 1. Todos los puntos enteros en el cuadrante positivo $(N, \ell)$ representan estados. Los estados con un valor común de $n$ se encuentran sobre las líneas discontinuas.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes22_ES/fig1.png)

Figura 1: Todos los puntos con $N \ge 0$ entero y $\ell \ge 0$ entero representan estados del átomo de hidrógeno. La figura nos ayuda a contar el número de estados posibles para un valor dado de $n$. Cada punto a lo largo de la línea diagonal para un $n$ dado representa un estado posible.

La Figura 1 nos ayuda a contar el número de estados ligados para un valor dado de $n$. Recordemos que para cada $n$, $\ell$ puede tomar valores desde $0, \ldots, n-1$, y para cada valor de $\ell$, $m$ toma valores desde $-\ell$ hasta $\ell$. La siguiente tabla cuenta los estados para los primeros valores del número cuántico principal $n$. Un estado dado se especifica por sus valores de $(n, \ell, m)$, todos los cuales se conocen como los números cuánticos de los estados de hidrógeno. Cada número tiene un significado físico muy importante: $n$ nos informa sobre el autovalor de energía, $\hbar^2 \ell(\ell+1)$ es el autovalor del cuadrado del momento angular, y $\hbar m$ es el autovalor de la componente $z$ del momento angular.

**Número de estados**

| Valor de $n$ | Valores de $\ell$ | Valores de $m$  | Estados totales |
|--------------|-------------------|-----------------|-----------------|
| $n=1$        | $\ell=0$          | $m=0$           | 1 estado        |
| $n=2$        | $\ell=0$          | $m=0$           | 1               |
|              | $\ell=1$          | $m=-1,0,1$      | $+3$            |
|              |                   |                 | $= 4$ estados   |
| $n=3$        | $\ell=0$          | $m=0$           | 1               |
|              | $\ell=1$          | $m=-1,0,1$      | $+3$            |
|              | $\ell=2$          | $m=-2,\ldots,2$ | $+5$            |
|              |                   |                 | $= 9$ estados   |

El número total de estados para un número cuántico principal $n$ arbitrario puede calcularse ahora:

$$\#\ \text{de estados para } n = \sum_{\ell=0}^{n-1}(2\ell+1) = \frac{2(n-1)n}{2} + n = n^2 - n + n = n^2. \qquad \text{(2.32)}$$

Esto concuerda con los resultados parciales de la tabla. Una representación más familiar de los estados del hidrógeno se muestra en la Figura 2. Las distintas columnas indican los distintos valores de $\ell$. También hemos indicado en la figura los valores de $N$, el grado del polinomio que aparece en la solución radial. Nótese que, para un $\ell$ dado, es decir, para una ecuación radial fija, el valor de $N$ aumenta a medida que subimos por la columna. El número $N$ corresponde al número de nodos de la solución.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes22_ES/fig2.png)

Figura 2: Gráfico de los niveles de energía $E \sim -1/n^2$ indicando también el número cuántico angular $\ell$ y el grado $N$ del polinomio. El espectro es altamente degenerado.

Recordemos que definimos $\rho = \dfrac{2\kappa Z}{a_0} r$. Junto con $\kappa = \dfrac{1}{2n}$ esto da

$$\rho = \frac{Zr}{na_0}. \qquad \text{(2.33)}$$

Los estados propios están etiquetados por los números cuánticos $(n, \ell, m)$ y las funciones de onda son

$$\psi_{n\ell m} = N \frac{u_{n\ell}(r)}{r} Y_{\ell m}(\theta,\phi) = N \frac{\rho^{\ell+1}}{\rho} W_{n\ell}(\rho) e^{-\rho} Y_{\ell m}(\theta,\phi) = N \rho^{\ell} \underbrace{W_{n\ell}(\rho)}_{\substack{\text{polinomio de grado} \\ N=n-(\ell+1)}} e^{-\rho} Y_{\ell m}(\theta,\phi), \qquad \text{(2.34)}$$

donde $N$ es una constante de normalización. Por lo tanto, usando la expresión para $\rho$ y absorbiendo constantes en $N$ tenemos

$$\psi_{n\ell m}(r,\theta,\phi) = N \left(\frac{r}{a_0}\right)^{\ell} \underbrace{\left[\text{polinomio en } \frac{r}{a_0}\right]}_{\text{de grado } N=n-(\ell+1)} \ e^{-\frac{Zr}{na_0}} \ Y_{\ell m}(\theta,\phi). \qquad \text{(2.35)}$$

Para el estado fundamental del hidrógeno ($Z=1$), tenemos $(n,\ell,m) = (1,0,0)$. Al tener momento angular nulo, la función de onda asociada no tiene dependencia angular. La función de onda normalizada es

$$\psi_{100}(r,\theta,\phi) = \frac{1}{\sqrt{\pi a_0^3}} e^{-r/a_0}. \qquad \text{(2.36)}$$

Para las funciones de onda normalizadas del hidrógeno en $n=2$ y $n=3$, véase http://hyperphysics.phy-astr.gsu.edu/hbase/quantum/hydwf.html

*Sarah Geller y Andrew Turner transcribieron las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare

https://ocw.mit.edu

8.04 Física Cuántica I

Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

# Apéndice: Lista de problemas 10 (Problem Set 10, 2016)

**Departamento de Física del MIT — Física Cuántica I (8.04), Primavera de 2016**

*Lectura: Griffiths, secciones 4.1, 4.2 y 4.3.*

*Publicado el 29 de abril de 2016. Fecha de entrega: viernes 6 de mayo de 2016, 12:00 del mediodía.*

## Problema 1. Estados ligados a partir de un número de onda imaginario \[5 puntos\]

Considere la solución de dispersión para un potencial unidimensional de rango finito:

$$\psi_>(x) = e^{i\delta(k)}\sin(kx+\delta(k)), \qquad x > R.$$

Muestre que tener un estado ligado significa que $A_s = e^{i\delta}\sin\delta$ tiene un polo en $k = i\kappa$ con $\kappa > 0$.

## Problema 2. Autofunciones simultáneas \[5 puntos\]

Considere dos operadores hermíticos $\hat{A}$ y $\hat{B}$ que conmutan. Suponga que al menos uno de los operadores, digamos $\hat{A}$, no tiene degeneraciones en su espectro. Muestre que las autofunciones de $\hat{A}$ son también autofunciones de $\hat{B}$.

## Problema 3. Valores esperados en una función de onda particular \[10 puntos\]

(Basado en Ohanian, Cap. 7, problema 17).

Suponga que una partícula tiene la función de onda

$$\psi(r,\theta,\phi) = \frac{1}{4}\sqrt{\frac{5}{\pi}}\,\sin^2\theta\left(1+\sqrt{14}\cos\theta\right)\cos 2\phi \; f(r),$$

con $f(r)$ una función de onda radial normalizada.

1.  Reescriba esta función de onda en términos de armónicos esféricos. ¿Cuáles son los posibles resultados de la medición de $L^2$ y $L_z$? ¿Cuáles son las probabilidades correspondientes?

2.  ¿Cuáles son los valores esperados de $L^2$ y $L_z$?

3.  Determine las incertidumbres $\Delta L^2$ y $\Delta L_z$.

## Problema 4. Pozos esféricos \[10 puntos\]

1.  Considere estados con $\ell = 0$ de una partícula que se mueve en el pozo esférico *infinito*

$$V(r) = \begin{cases} 0, & \text{si } r < a \\ \infty, & \text{si } r > a. \end{cases}$$

Resuelva la ecuación radial para la función de onda radial $u(r)$ y encuentre los niveles de energía posibles. Recuerde que $u$ debe anularse en $r=0$. Intente relacionar este espectro con $\ell=0$ con el de un potencial de pozo infinito unidimensional $V(x)$.

1.  Considere ahora estados de una partícula que se mueve en un pozo esférico *finito* con $V_0 > 0$:

$$V(r) = \begin{cases} -V_0, & \text{si } r < a \\ 0, & \text{si } r > a. \end{cases}$$

Muestre que no hay estado ligado si

$$V_0 a^2 < \frac{\pi^2 \hbar^2}{8m}.$$

## Problema 5. Átomo de hidrógeno con momento total \[10 puntos\]

Basado en Ohanian.

Cuando se tiene en cuenta el movimiento del núcleo, el estado del átomo de hidrógeno puede representarse mediante una función de onda $\psi(\mathbf{X}, \mathbf{x})$, con $\mathbf{X}$ la coordenada del centro de masas y $\mathbf{x} = \mathbf{x}_e - \mathbf{x}_p$ la coordenada relativa que apunta del protón al electrón.

Suponga que el átomo se encuentra en un estado tal que el momento *total* tiene probabilidades iguales para los valores $\mathbf{p}_0$ y $-\mathbf{p}_0$. Además, los estados internos son $\phi_{1,0,0}(\mathbf{x})$ o $\phi_{2,1,1}(\mathbf{x})$ con probabilidades $1/4$ y $3/4$ respectivamente (usamos la notación $\phi_{n\ell m}$). Estas probabilidades no están correlacionadas con el momento total.

1.  Escriba una expresión para $\psi(\mathbf{X}, \mathbf{x})$ ignorando la fase global pero incluyendo factores de fase constantes arbitrarios donde sea posible.

2.  ¿Cuál es el valor esperado de la energía total?

## Problema 6. Teorema del virial y aplicaciones \[15 puntos\]

1.  Considere cualquier operador independiente del tiempo $\Omega$ y la derivada temporal de su valor esperado, dada por

$$i\hbar \frac{d}{dt}\langle\Omega\rangle = \langle[\Omega, H]\rangle,$$

donde $H$ es el hamiltoniano. Explique cuidadosamente por qué el lado derecho se anula si el sistema se encuentra en un estado estacionario.

1.  Tome ahora $\Omega = \mathbf{r}\cdot\mathbf{p}$ y muestre que, para cualquier estado estacionario del hamiltoniano del átomo de hidrógeno, se cumple la siguiente relación

$$\langle T\rangle = -\tfrac{1}{2}\langle V\rangle.$$

Aquí $T$ es el operador de energía cinética y $V$ es el operador de energía potencial.

1.  Para cualquier autoestado del átomo de hidrógeno, escriba $\langle T\rangle = \tfrac{1}{2}m\langle v^2\rangle$, donde $m$ es, con bastante precisión, la masa del electrón. Exprese el cociente

$$\frac{\sqrt{\langle v^2\rangle}}{c}$$

en términos de la constante de estructura fina $\alpha = \dfrac{e^2}{\hbar c} \simeq \dfrac{1}{137}$ y el número cuántico principal $n$. ¿Es el electrón relativista? Dé los resultados correspondientes para el estado fundamental cuando el núcleo tiene $Z$ protones.

1.  ¿Cuánto vale $\left\langle \dfrac{1}{r} \right\rangle$ en un autoestado de energía general del átomo de hidrógeno?

## Problema 7. Ejercicios sobre el átomo de hidrógeno y algunas generalizaciones \[10 puntos\]

1.  Encuentre $\langle r\rangle$ y $\langle r^2\rangle$ en el estado fundamental del hidrógeno. ¿Cuál es el valor más probable de $r$ en el estado fundamental?

2.  Suponga que el núcleo del hidrógeno tiene un radio de un femtómetro. Calcule la probabilidad de que el electrón del estado fundamental se encuentre dentro del núcleo. ¡Haga aproximaciones para simplificar su trabajo y aun así obtener una respuesta muy precisa!

3.  El positronio es un estado ligado de un electrón y un positrón (¡partículas de igual masa!). ¿Cuáles son los niveles de energía? ¿Cómo se compara el tamaño del positronio con el tamaño de un átomo de hidrógeno?

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*
