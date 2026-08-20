# Lección 5

## Vídeos de esta clase (YouTube)

**Lección 5: Momentum operator, Schrödinger equation, and interpretation of the wavefunction.**

- [Momentum operator, energy operator, and a differential equation](https://www.youtube.com/watch?v=ELBh60GU5yE)
- [Free Schrödinger equation](https://www.youtube.com/watch?v=7euh_iwzSGo)
- [The general Schrödinger equation. x, p commutator](https://www.youtube.com/watch?v=rwzg8iEOc8s)
- [Commutators, matrices, and 3-dimensional Schrödinger equation](https://www.youtube.com/watch?v=m7UT2Hr465o)
- [Interpretation of the wavefunction](https://www.youtube.com/watch?v=R-5hjmV-bdY)

------------------------------------------------------------------------

*B. Zwiebach*

*21 de febrero de 2016*

## Contenido

1.  Ecuaciones para una función de onda
2.  Ecuación de Schrödinger para una partícula en un potencial
3.  Interpretación de la función de onda

## 1. Ecuaciones para una función de onda

Determinamos que la función de onda o onda de de Broglie para una partícula con momento $p$ y energía $E$ está dada por

$$\Psi(x, t) = e^{i(kx-\omega t)} , \qquad \text{(1.1)}$$

donde $\omega$ y $k$ están determinados a partir de

$$p = \hbar k, \quad E = \hbar \omega , \quad E = \frac{p^2}{2m} \qquad \text{(1.2)}$$

La función de onda (1.1) representa un estado de momento definido. Resulta entonces interesante encontrar un operador que extraiga esa información de la función de onda. El operador debe ser, en términos generales, una derivada con respecto a $x$, ya que esto haría bajar un factor de $k$. De hecho, de forma más precisa, tomamos

$$\frac{\hbar}{i} \frac{\partial}{\partial x} \Psi(x, t) = \frac{\hbar}{i} (ik)\Psi(x, t)$$

$$= \hbar k \Psi(x, t) \qquad \text{(1.3)}$$

$$= p \Psi(x, t)$$

donde el factor $p$ en el último miembro derecho es justamente el momento. Identificamos así el operador $\frac{\hbar}{i}\frac{\partial}{\partial x}$ como el operador momento $\hat{p}$

$$\hat{p} \equiv \frac{\hbar}{i} \frac{\partial}{\partial x} . \qquad \text{(1.4)}$$

y hemos verificado que, al actuar sobre la función de onda $\Psi(x, t)$ de una partícula de momento $p$, da $p$ veces la función de onda:

$$\hat{p} \, \Psi = p \, \Psi . \qquad \text{(1.5)}$$

El operador momento actúa sobre funciones de onda, que son funciones del espacio y el tiempo, para dar otra función de $x$ y $t$. Puesto que $\hat{p}$ actuando sobre $\Psi$ da un número ($p$, de hecho) multiplicado por $\Psi$, decimos que $\Psi$ es un autoestado (o estado propio) de $\hat{p}$. La analogía con el álgebra de matrices es útil: las matrices son los operadores y los vectores columna son los estados. Las matrices actúan por multiplicación sobre vectores columna. Un autovector de una matriz es un vector especial. La matriz, al actuar sobre un autovector, da un número multiplicado por el autovector. Tras la acción de la matriz, la dirección del vector no cambia, pero su magnitud puede escalarse. Lo mismo ocurre con los autoestados de operadores: un operador actuando sobre un autoestado da el autoestado multiplicado por una constante. También decimos que $\Psi$ es un estado de momento definido.

Consideremos ahora la extracción de la información de energía a partir de la función de onda de la partícula libre. Esta vez debemos recurrir a la derivada temporal:

$$i\hbar \, \frac{\partial}{\partial t} \Psi(x, t) = i\hbar(-i\omega)\Psi(x, t) = \hbar \omega \, \Psi(x, t) = E \, \Psi(x, t) . \qquad \text{(1.6)}$$

Sería razonable decir que la derivada temporal $i\hbar \frac{\partial}{\partial t}$ es un operador de energía, pero, para una partícula libre, la energía está dada en términos del momento, de modo que podemos construir el operador de energía relevante trabajando sobre el miembro derecho anterior

$$E\Psi = \frac{p^2}{2m} \Psi = \frac{p}{2m} p \Psi = \frac{p}{2m} \frac{\hbar}{i}\frac{\partial}{\partial x} \Psi , \qquad \text{(1.7)}$$

donde usamos la ecuación (1.5) para escribir $p\Psi$ como el operador momento actuando sobre $\Psi$. Como $p$ es una constante, podemos mover el factor $p$ en el último miembro derecho cerca de la función de onda y luego reemplazarlo por el operador momento:

$$E\Psi = \frac{1}{2m} \frac{\hbar}{i}\frac{\partial}{\partial x} \, p\Psi = \frac{1}{2m} \frac{\hbar}{i}\frac{\partial}{\partial x} \frac{\hbar}{i}\frac{\partial}{\partial x} \Psi . \qquad \text{(1.8)}$$

Esto puede escribirse como

$$E\Psi = \frac{1}{2m} \hat{p}\,\hat{p}\, \Psi = \frac{\hat{p}^2}{2m} \Psi , \qquad \text{(1.9)}$$

lo cual sugiere la siguiente definición del operador de energía $\hat{E}$:

$$\hat{E} \equiv \frac{\hat{p}^2}{2m} = -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} . \qquad \text{(1.10)}$$

En efecto, para nuestra función de onda de partícula libre, (1.9) muestra que $E\Psi = \hat{E}\Psi$.

Nuestro trabajo también nos permite hallar una ecuación diferencial para la cual nuestra función de onda de de Broglie es solución. Consideremos (1.6) y reemplacemos el miembro derecho $E\Psi$ por $\hat{E}\Psi$, lo que nos da

$$i\hbar \, \frac{\partial}{\partial t} \Psi(x, t) = -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} \Psi(x, t) . \qquad \text{(1.11)}$$

Esta es la ecuación de Schrödinger para la partícula libre. De forma más esquemática, usando el operador de energía, puede escribirse como

$$i\hbar \, \frac{\partial}{\partial t} \Psi(x, t) = \hat{E} \, \Psi(x, t) . \qquad \text{(1.12)}$$

Vale la pena volver a comprobar que nuestra función de onda de de Broglie satisface la ecuación de Schrödinger (1.11). En efecto, para $\Psi = e^{i(kx-\omega t)}$ encontramos

$$i\hbar(-i\omega)\Psi = -\frac{\hbar^2}{2m}(ik)^2 \Psi \qquad \text{(1.13)}$$

lo cual es una solución, ya que los factores $\Psi$ se cancelan y todo lo que se necesita es la igualdad

$$\hbar \omega = \frac{\hbar^2 k^2}{2m} , \qquad \text{(1.14)}$$

que se reconoce como la familiar relación $E = \frac{p^2}{2m}$.

Nótese que la ecuación de Schrödinger admite soluciones más generales que la función de onda de de Broglie para una partícula de momento y energía definidos. Puesto que la ecuación es lineal, cualquier superposición de soluciones de ondas planas con distintos valores de $k$ es también una solución. Tomemos por ejemplo

$$\Psi(x, t) = e^{i(k_1 x - \omega_1 t)} + e^{i(k_2 x - \omega_2 t)} \qquad \text{(1.15)}$$

Esta es una solución, y nótese que, aunque cada sumando corresponde a un estado de momento definido, la solución total no es un estado de momento definido. En efecto

$$\hat{p} \, \Psi(x, t) = \hbar k_1 \, e^{i(k_1 x - \omega_1 t)} + \hbar k_2 \, e^{i(k_2 x - \omega_2 t)} , \qquad \text{(1.16)}$$

y el miembro derecho no puede escribirse como un número multiplicado por $\Psi$. El estado completo tampoco es un estado de energía definida. La solución general de la ecuación de Schrödinger libre es la superposición más general de ondas planas:

$$\Psi(x, t) = \int_{-\infty}^{\infty} dk \, \Phi(k) \, e^{i(kx - \omega(k)t)} , \qquad \text{(1.17)}$$

donde $\Phi(k)$ es una función arbitraria de $k$ que controla la superposición, y hemos escrito $\omega(k)$ para enfatizar que $\omega$ es una función del momento, como en (1.14).

**Ejercicio.** Verifique que $\Psi$ en (1.17) resuelve la ecuación de Schrödinger libre.

Ahora tenemos las herramientas para evolucionar en el tiempo cualquier función de onda inicial. Es decir, dada la función de onda inicial $\Psi(x, 0)$ de cualquier paquete en el instante cero, podemos obtener $\Psi(x, t)$. En efecto, mediante la transformación de Fourier, podemos escribir

$$\Psi(x, 0) = \int dk \, \Phi(k) \, e^{ikx} , \qquad \text{(1.18)}$$

donde $\Phi(k)$ es la transformada de Fourier de $\Psi(x, 0)$. Pero entonces, la evolución temporal consiste simplemente en añadir la exponencial $e^{-i\omega(k)t}$ a la integral, de modo que la respuesta para la evolución temporal está dada efectivamente por (1.17).

Como hemos discutido antes, la velocidad de un paquete de ondas descrito por (1.17) está dada por la velocidad de grupo evaluada para el valor dominante de $k$. Confirmamos que esto es efectivamente razonable

$$v_g \equiv \frac{\partial \omega}{\partial k} = \frac{\partial \hbar \omega}{\partial \hbar k} = \frac{\partial E}{\partial p} = \frac{\partial}{\partial p}\left(\frac{p^2}{2m}\right) = \frac{p}{m} , \qquad \text{(1.19)}$$

que es la velocidad esperada para una partícula libre no relativista con momento $p$ y masa $m$.

La ecuación de Schrödinger tiene una $i$ explícita en el miembro izquierdo. Esta $i$ muestra que es imposible encontrar una solución para $\Psi$ real. Si $\Psi$ fuera real, el miembro derecho de la ecuación sería real, pero el miembro izquierdo sería imaginario. Por lo tanto, la ecuación de Schrödinger nos obliga a trabajar con funciones de onda complejas.

Nótese también que la ecuación de Schrödinger no tiene la forma de una ecuación de onda convencional. Una ecuación de onda convencional para una variable $\phi$ toma la forma

$$\frac{\partial^2 \phi}{\partial x^2} - \frac{1}{V^2} \frac{\partial^2 \phi}{\partial t^2} = 0 . \qquad \text{(1.20)}$$

Las soluciones generales de esta ecuación lineal son $f_{\pm}(x \pm Vt)$. Esto sí permitiría soluciones reales, las cuales no son aceptables en la teoría cuántica. La ecuación de Schrödinger no tiene derivadas temporales de segundo orden. ¡Es de primer orden en el tiempo!

## 2. Ecuación de Schrödinger para una partícula en un potencial

Supongamos ahora que nuestra partícula cuántica no es libre, sino que se mueve en algún potencial externo $V(x, t)$. En este caso, la energía total de la partícula ya no es simplemente cinética, sino la suma de las energías cinética y potencial:

$$E = \frac{p^2}{2m} + V(x, t) , \qquad \text{(2.1)}$$

Esto sugiere naturalmente que el operador de energía debería tomar la forma

$$\hat{E} = \frac{\hat{p}^2}{2m} + V(x, t) . \qquad \text{(2.2)}$$

El primer término, como ya sabemos, involucra segundas derivadas con respecto a $x$. El segundo término actúa multiplicativamente: al actuar sobre cualquier función de onda $\Psi(x, t)$, simplemente la multiplica por $V(x, t)$. Postulamos ahora que la ecuación de Schrödinger para una partícula en un potencial toma la forma (1.12) con $\hat{E}$ reemplazado por el operador de energía anterior:

$$i\hbar \, \frac{\partial}{\partial t} \Psi(x, t) = \left[ -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} + V(x, t) \right] \Psi(x, t) . \qquad \text{(2.3)}$$

El operador de energía $\hat{E}$ se llama habitualmente operador hamiltoniano $\hat{H}$, de modo que se tiene

$$\hat{H} \equiv -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} + V(x, t) , \qquad \text{(2.4)}$$

y la ecuación de Schrödinger toma la forma

$$i\hbar \, \frac{\partial}{\partial t} \Psi(x, t) = \hat{H} \, \Psi(x, t) . \qquad \text{(2.5)}$$

Reconsideremos la forma en que el potencial $V(x, t)$ es un operador. Podemos hacerlo introduciendo un operador posición $\hat{x}$ que, al actuar sobre funciones de $x$, da otra función de $x$ de la siguiente manera:

$$\hat{x} f(x) \equiv x f(x) . \qquad \text{(2.6)}$$

Nótese que de esta ecuación y de aplicaciones sucesivas de la misma se sigue que

$$\hat{x}^k f(x) \equiv x^k f(x) . \qquad \text{(2.7)}$$

Si el potencial $V(x, t)$ puede escribirse como alguna expansión en serie en términos de $x$, entonces se sigue que

$$V(\hat{x}, t)\Psi(x, t) \equiv V(x, t)\Psi(x, t) . \qquad \text{(2.8)}$$

Los operadores con los que estamos tratando (momento, posición, hamiltoniano) se declaran todos operadores lineales. Un operador lineal $\hat{A}$ satisface

$$\hat{A}(a\phi) = a \, \hat{A}\phi , \qquad \hat{A}(\phi_1 + \phi_2) = \hat{A}\phi_1 + \hat{A}\phi_2 , \qquad \text{(2.9)}$$

donde $a$ es una constante. Dos operadores lineales $\hat{A}$ y $\hat{B}$ que actúan sobre el mismo conjunto de objetos siempre pueden sumarse $(\hat{A}+\hat{B})\phi \equiv \hat{A}\phi + \hat{B}\phi$. También pueden multiplicarse; el producto $\hat{A}\hat{B}$ es un operador lineal definido por $\hat{A}\hat{B}\phi \equiv \hat{A}(\hat{B}\phi)$, lo que significa que se actúa primero con $\hat{B}$, que es el más cercano a $\phi$, y luego se actúa sobre el resultado con $\hat{A}$. El orden de multiplicación importa, y por lo tanto $\hat{A}\hat{B}$ y $\hat{B}\hat{A}$ pueden no ser los mismos operadores. Para cuantificar esta posible diferencia se introduce el conmutador $[A, B]$ de dos operadores, definido como el operador lineal

$$[\, \hat{A} , \hat{B} \,] \equiv \hat{A}\hat{B} - \hat{B}\hat{A} . \qquad \text{(2.10)}$$

Si el conmutador se anula, se dice que los dos operadores conmutan. También es claro que $[\hat{A}, \hat{A}] = 0$ para cualquier operador $\hat{A}$.

Tenemos los operadores $\hat{x}$ y $\hat{p}$, que están claramente relacionados de alguna manera. Nos gustaría conocer su conmutador $[\, \hat{x}\, , \hat{p}\, ]$. Para ello dejamos que $[\, \hat{x}\, , \hat{p}\, ]$ actúe sobre alguna función arbitraria $\phi(x)$ y luego intentamos simplificar. Hagámoslo.

$$[\, \hat{x} , \hat{p} \,]\phi(x) = (\hat{x}\hat{p} - \hat{p}\hat{x})\phi(x) = \hat{x}\hat{p}\, \phi(x) - \hat{p}\hat{x}\, \phi(x)$$

$$= \hat{x}(\hat{p}\phi(x)) - \hat{p}(\hat{x}\phi(x))$$

$$= \hat{x}\left(\frac{\hbar}{i}\frac{\partial \phi(x)}{\partial x}\right) - \hat{p}(x\phi(x))$$

$$= x\,\frac{\hbar}{i}\frac{\partial \phi(x)}{\partial x} - \frac{\hbar}{i}\frac{\partial}{\partial x}(x\phi(x)) \qquad \text{(2.11)}$$

$$= x\,\frac{\hbar}{i}\frac{\partial \phi(x)}{\partial x} - x\,\frac{\hbar}{i}\frac{\partial \phi(x)}{\partial x} - \frac{\hbar}{i}\phi(x)$$

$$= -\frac{\hbar}{i}\phi(x) = i\hbar\, \phi(x) ,$$

de modo que, en definitiva, hemos mostrado que para $\phi(x)$ arbitraria se tiene

$$[\, \hat{x} , \hat{p} \,]\phi(x) = i\hbar\, \phi(x) . \qquad \text{(2.12)}$$

Puesto que esta ecuación se cumple para cualquier $\phi$, en realidad representa la igualdad de dos operadores. Siempre que tengamos $\hat{A}\phi = \hat{B}\phi$ para $\phi$ arbitraria, simplemente decimos que $\hat{A} = \hat{B}$. Los operadores son los mismos porque dan el mismo resultado al actuar sobre cualquier cosa. Hemos descubierto entonces la relación de conmutación más fundamental de la mecánica cuántica:

$$[\, \hat{x} , \hat{p} \,] = i\hbar . \qquad \text{(2.13)}$$

El miembro derecho es un número, pero debe considerarse como un operador (al actuar sobre cualquier función, la multiplica por dicho número). Esta relación de conmutación puede usarse para demostrar el principio de incertidumbre de Heisenberg, que establece que el producto de la incertidumbre en la posición y la incertidumbre en el momento debe siempre exceder $\hbar/2$.

La idea de que los operadores pueden no conmutar puede recordarnos la multiplicación de matrices, que tampoco es conmutativa. Tenemos así las siguientes correspondencias:

$$\begin{aligned}
\text{operadores} &\leftrightarrow \text{matrices} \\
\text{funciones de onda} &\leftrightarrow \text{vectores} \\
\text{autoestados} &\leftrightarrow \text{autovectores}
\end{aligned} \qquad \text{(2.14)}$$

De hecho, se puede formular la Mecánica Cuántica usando matrices, de modo que estas correspondencias son realmente concretas y funcionales.

Como ejemplo de matrices útiles que no conmutan, consideremos las matrices de Pauli, tres matrices de dos por dos dadas por

$$\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} , \quad \sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} , \quad \sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} . \qquad \text{(2.15)}$$

De hecho, estas matrices son exactamente lo que se necesita para describir partículas de espín un medio. El operador de espín $S$ tiene tres componentes $S_i = \frac{\hbar}{2}\sigma_i$. Veamos ahora si $\sigma_1$ y $\sigma_2$ conmutan.

$$\sigma_1 \sigma_2 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}$$

$$\sigma_2 \sigma_1 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix} \qquad \text{(2.16)}$$

Entonces vemos que

$$[\sigma_1, \sigma_2] = \begin{pmatrix} 2i & 0 \\ 0 & -2i \end{pmatrix} = 2i \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = 2i\sigma_3 \qquad \text{(2.17)}$$

De hecho, también se tiene $[\sigma_2, \sigma_3] = 2i\sigma_1$ y $[\sigma_3, \sigma_1] = 2i\sigma_2$.

La mecánica matricial fue desarrollada en 1925 por Werner Heisenberg y aclarada por Max Born y Pascual Jordan. Nótese que, si quisiéramos escribir los operadores $\hat{x}$ y $\hat{p}$ en forma matricial, requerirían matrices de dimensión infinita. Puede demostrarse que no existen matrices de tamaño finito que conmuten para dar un número multiplicado por la matriz identidad, como se requiere en (2.13). Esto no debería sorprendernos: en la recta real hay un número infinito de funciones de onda linealmente independientes, y en vista de las correspondencias en (2.14) esto sugeriría un número infinito de vectores de base. Las matrices relevantes deben ser, por lo tanto, de dimensión infinita.

**Dos propiedades básicas de la ecuación de Schrödinger**

1.  La ecuación diferencial es de primer orden en el tiempo. Esto significa que, para una condición inicial, basta con conocer completamente la función de onda en algún instante inicial $t_0$, y la ecuación de Schrödinger determina entonces la función de onda para todo tiempo. Esto puede entenderse de manera muy explícita. Si conocemos $\Psi(x, t_0)$ para todo $x$, entonces el miembro derecho de la ecuación de Schrödinger, que solo involucra derivadas respecto de $x$ y multiplicación, puede evaluarse en cualquier punto $x$. Esto significa que en cualquier punto $x$ conocemos la derivada temporal de la función de onda (miembro izquierdo de la ecuación de Schrödinger), y esto nos permite calcular la función de onda un poco más tarde.

2.  Linealidad y superposición. La ecuación de Schrödinger es una ecuación lineal para funciones de onda complejas. Por lo tanto, dadas dos soluciones $\Psi_1$ y $\Psi_2$, podemos formar nuevas soluciones como combinaciones lineales $\alpha\Psi_1 + \beta\Psi_2$ con coeficientes complejos $\alpha$ y $\beta$.

Hemos escrito la ecuación de Schrödinger para una partícula en un potencial unidimensional. ¿Qué ocurre en el caso de una partícula en un potencial tridimensional? Como veremos ahora, esto se logra fácilmente una vez que nos damos cuenta de que en tres dimensiones los operadores de posición y momento tienen ¡varias componentes! Recordemos que la función de onda de de Broglie

$$\Psi(\mathbf{x}, t) = e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)} = e^{i(k_x x + k_y y + k_z z - \omega t)} \qquad \text{(2.18)}$$

corresponde a una partícula que porta momento $\mathbf{p} = \hbar \mathbf{k}$, con $\mathbf{k} = (k_x, k_y, k_z)$. Tal como hicimos en (1.3), podemos intentar extraer el momento vectorial usando un operador diferencial. El operador relevante es el gradiente:

$$\nabla = \left( \frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z} \right) , \qquad \text{(2.19)}$$

con el cual intentamos

$$\frac{\hbar}{i} \nabla \Psi(\mathbf{x}, t) = \frac{\hbar}{i} \left( ik_x, ik_y, ik_z \right) \Psi(\mathbf{x}, t) = \hbar \mathbf{k} \, \Psi(\mathbf{x}, t) = \mathbf{p} \, \Psi(\mathbf{x}, t) . \qquad \text{(2.20)}$$

Definimos entonces el operador momento $\hat{\mathbf{p}}$ de la siguiente manera:

$$\hat{\mathbf{p}} = \frac{\hbar}{i} \nabla . \qquad \text{(2.21)}$$

Si llamamos a las componentes del momento $(p_1, p_2, p_3) = (p_x, p_y, p_z)$ y a las coordenadas $(x_1, x_2, x_3) = (x, y, z)$, entonces las componentes de la ecuación anterior son

$$\hat{p}_k = \frac{\hbar}{i} \frac{\partial}{\partial x_k} , \qquad k = 1, 2, 3 . \qquad \text{(2.22)}$$

Del mismo modo que definimos un operador posición $\hat{x}$, ahora tenemos tres operadores posición $(\hat{x}_1, \hat{x}_2, \hat{x}_3)$ que conforman $\hat{\mathbf{x}}$. Con tres operadores posición y tres operadores momento, debemos ahora enunciar las nueve relaciones de conmutación posibles. Si recuerdan nuestra derivación de $[\hat{x}, \hat{p}] = i\hbar$, notarán que el conmutador se anula a menos que los superíndices en $\hat{x}$ y $\hat{p}$ sean iguales. Esto significa que tenemos

$$[\, \hat{x}_i , \hat{p}_j \,] = i\hbar \, \delta_{ij} , \qquad \text{(2.23)}$$

donde la delta de Kronecker se define por

$$\delta_{ij} = \begin{cases} 1 & \text{si } i = j , \\ 0 & \text{si } i \neq j . \end{cases} \qquad \text{(2.24)}$$

Para escribir ahora la ecuación de Schrödinger general, necesitamos considerar el operador de energía cinética, o el hamiltoniano:

$$\hat{H} = \frac{\hat{p}^2}{2m} + V(\mathbf{x}, t) , \qquad \text{(2.25)}$$

En este caso

$$\hat{p}^2 = \hat{\mathbf{p}} \cdot \hat{\mathbf{p}} = \frac{\hbar}{i}\nabla \cdot \frac{\hbar}{i}\nabla = -\hbar^2 \nabla^2 \qquad \text{(2.26)}$$

donde $\nabla^2$ es el operador laplaciano

$$\nabla^2 \equiv \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2} . \qquad \text{(2.27)}$$

La ecuación de Schrödinger toma finalmente la forma

$$i\hbar \, \frac{\partial}{\partial t} \Psi(\mathbf{x}, t) = \left[ -\frac{\hbar^2}{2m} \nabla^2 + V(\mathbf{x}, t) \right] \Psi(\mathbf{x}, t) . \qquad \text{(2.28)}$$

## 3. Interpretación de la función de onda

Schrödinger pensaba que la función de onda $\Psi$ representaba una partícula que podía extenderse y desintegrarse. La fracción de la partícula que se encontraría en $x$ sería proporcional a la magnitud de $|\Psi|^2$. Esto resultaba problemático, como señaló Max Born (1882-1970). Born resolvió la ecuación de Schrödinger para la dispersión de una partícula en un potencial, hallando una función de onda que decaía como $1/r$, siendo $r$ la distancia al centro de dispersión. Pero Born también notó que en el experimento no se encuentran fracciones de partículas viajando en muchas direcciones, sino que las partículas permanecen enteras. Born propuso una interpretación probabilística. En su propuesta,

> La función de onda $\Psi(x, t)$ no nos indica cuánta cantidad de la partícula se encuentra en la posición $x$ en el instante $t$, sino más bien la probabilidad de que, al realizar una medición en el instante $t$, encontremos la partícula en la posición $x$.

Para precisar esto, usamos un elemento de volumen infinitesimal de volumen $d^3x$ centrado en algún punto arbitrario $x$. La probabilidad $dP$ de encontrar la partícula dentro del elemento de volumen $d^3x$ en el instante $t$ es

$$dP = |\Psi(x, t)|^2 \, d^3x . \qquad \text{(3.1)}$$

La consistencia exige que la probabilidad total de encontrar la partícula en algún lugar de todo el espacio sea la unidad. Por lo tanto, la integral de $dP$ sobre todo el espacio debe dar uno:

$$\int_{\text{todo el espacio}} d^3x \, |\Psi(x, t)|^2 = 1 \qquad \text{(3.2)}$$

La próxima vez exploraremos la consistencia de esta ecuación con la evolución temporal.

*Sarah Geller transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare https://ocw.mit.edu

8.04 Física Cuántica I Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

# Apéndice: Lista de problemas 2 (Problem Set 2, 2016)

*Massachusetts Institute of Technology — Departamento de Física* *8.04 Física Cuántica I, primavera de 2016* *Fecha de entrega: jueves 18 de febrero de 2016, 5:00 pm* *(Publicado el 11 de febrero de 2016)*

## Problema 1: Longitud de onda de de Broglie \[20 puntos\]

**(a)** La longitud de onda de de Broglie de un electrón no relativista (nr) con energía cinética $E_{kin}$ puede escribirse como

$$\lambda_{nr} = \frac{\delta}{\sqrt{E_{kin}}} \ \text{Å} .$$

En esta fórmula $\delta$ es una constante sin unidades, y el valor de la energía $E_{kin}$ se introduce en eV como un número puro. El resultado se obtiene en angstroms ($\text{Å} = 10^{-10}\,\text{m}$). Dé el valor de la constante adimensional $\delta$.

**(b)** La longitud de onda de de Broglie de un electrón relativista (r) con energía $E$ puede calcularse en términos del factor $\gamma$ del electrón: $E = \gamma m_e c^2$. Se obtiene

$$\lambda_r = \frac{\ell}{\sqrt{\gamma^2 - 1}} .$$

¿Cuál es el valor de $\ell$ en fm $= 10^{-15}\,\text{m}$? ¿Es esta una longitud bien conocida?

**(c)** Reescriba la expresión para $\lambda_{nr}$ del apartado (a) en términos de $\ell$ y $\gamma$, usando $E_{kin} = (\gamma - 1) m_e c^2$. Demuestre que $\lambda_r < \lambda_{nr}$ para cualquier valor de la energía.

**(d)** Algunos cálculos numéricos:

    **i.** ¿Cuál es la energía de un electrón cuya longitud de onda de de Broglie es igual a su longitud de onda Compton? ¿Es ese electrón relativista? ¿Se mueve más rápido que $0.2\,c$?

    **ii.** La longitud de onda de de Broglie de una partícula da una idea aproximada de la escala de distancias que puede explorar en un experimento de colisión. El International Linear Collider, que podría construirse en un futuro próximo, está pensado para acelerar electrones hasta $1\,\text{TeV} = 1000\,\text{GeV}$. ¿Cuál es la longitud de onda de de Broglie de tales electrones? Compárela con la longitud de onda de de Broglie de protones de $7\,\text{TeV}$ en el LHC de Ginebra.

    **iii.** ¿Cuál es la energía cinética máxima del electrón, y el correspondiente $\beta = v/c$, para la cual el valor no relativista de $\lambda$ (en (a) o en (c)) tiene un error menor o igual al 10 %?

## Problema 2: Radio de Bohr, longitud de onda Compton del electrón y radio clásico del electrón \[10 puntos\]

El radio clásico del electrón $r_0$ es el radio que se obtiene al igualar (salvo factores constantes) la energía electrostática asociada a una bola cargada de radio $r_0$ con la energía en reposo del electrón

$$\frac{e^2}{r_0} = m_e c^2 \quad \longrightarrow \quad r_0 = \frac{e^2}{m_e c^2} .$$

Aquí $e$ es la carga del electrón. La longitud de onda Compton reducida $\bar{\lambda}_C$ del electrón es

$$\bar{\lambda}_C = \frac{\hbar}{m_e c} .$$

Finalmente, la constante de estructura fina $\alpha$, que mide la intensidad del acoplamiento electromagnético, es

$$\alpha = \frac{e^2}{\hbar c} \simeq \frac{1}{137} .$$

**(a)** El radio de Bohr $a_0$ es la escala de longitud que puede construirse a partir de $e^2$, $\hbar$ y $m_e$ sin constantes numéricas adicionales. Encuentre la fórmula del radio de Bohr mediante un análisis dimensional. Evalúe esta longitud en fm.

**(b)** Muestre que las tres longitudes forman una progresión geométrica de razón $\alpha$:

$$a_0 : \bar{\lambda}_C : r_0 = 1 : \alpha : \alpha^2 .$$

Use esto para dar los valores de $\bar{\lambda}_C$ y $r_0$ en fm.

## Problema 3: Matrices de dos por dos y dispositivos lineales \[10 puntos\]

Considere el interferómetro de Mach-Zehnder de dos haces y un haz representado por el vector columna de dos componentes $u$:

$$u = \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} , \qquad \text{con } |u_1|^2 + |u_2|^2 = 1 .$$

Cualquier elemento óptico lineal del interferómetro puede representarse mediante una matriz de dos por dos $R$ tal que, para un haz de entrada $u$, el haz de salida $u'$ está dado por

$$u' = R\, u .$$

Demuestre que la conservación de la probabilidad para $u$ arbitrario exige que $R$ sea una matriz unitaria. Se dice que una matriz $R$ (de tamaño finito) es unitaria si $R^{\dagger} R = 1$, donde la daga denota la operación de transposición y conjugación compleja.

## Problema 4: Mejorando la detección de bombas \[15 puntos\]

Modificamos el interferómetro de Mach-Zehnder para aumentar el porcentaje de bombas de Elitzur-Vaidman que pueden certificarse como funcionales sin detonarlas. Para ello construimos un divisor de haz con reflectividad $R$ y transmisividad $T$. Un fotón incidente (desde cualquiera de los dos puertos) tiene una probabilidad $R$ de ser reflejado y una probabilidad $T$ de ser transmitido ($R + T = 1$). Sean $r$ y $t$ las raíces cuadradas positivas:

$$r \equiv \sqrt{R} , \qquad t \equiv \sqrt{T} .$$

**(a)** Construya la matriz de dos por dos $U$ que representa el divisor de haz. Para ello, considere lo que ocurre cuando un fotón incide sobre el divisor de haz desde el lado superior (entrada $\begin{pmatrix}1\\0\end{pmatrix}$) y cuando incide desde el lado inferior (entrada $\begin{pmatrix}0\\1\end{pmatrix}$). Para fijar convenciones, $U$ tendrá todos sus elementos positivos (y reales) excepto el elemento inferior derecho (el elemento 2,2). Confirme que $U$ es unitaria.

*(El interferómetro, con los detectores $D_0$ y $D_1$, utiliza dos copias idénticas del divisor de haz. El fotón incidente llega por el lado superior.)*

**(b)** Se inserta una bomba defectuosa en la rama inferior del interferómetro. ¿Cuáles son las probabilidades de detección $P_0$ y $P_1$ en $D_0$ y $D_1$ respectivamente? Se inserta ahora una bomba en funcionamiento en la rama inferior del interferómetro. ¿Cuál es la probabilidad de detonación $P_{boom}$ y las probabilidades de detección $P_0$ y $P_1$? Exprese sus respuestas en términos de $R$ y $T$.

**(c)** Se prueban bombas hasta estar razonablemente seguros de que fallan o de que son funcionales. ¿Qué fracción $f$ de las bombas funcionales puede certificarse como buenas sin detonarlas? Dé su respuesta en términos de $R$. ¿Cuál es el valor máximo posible de $f$?

## Problema 5: Ondas planas para partículas materiales \[10 puntos\]

Suponga que queremos representar la onda de una partícula material que se mueve en la dirección $x$ con momento $p = \hbar k$. Una propuesta razonable para dicha onda es

$$\Psi(x, t) = \cos(kx - \omega t) + \gamma \sin(kx - \omega t) ,$$

donde $\gamma$ es una constante. Un requisito físico es que un desplazamiento arbitrario de $x$ o un desplazamiento arbitrario de $t$ no debe alterar el carácter de la onda. Exigiremos por tanto que, tras el desplazamiento, cuyo efecto es cambiar la fase en una constante $\epsilon$, se tenga

$$\cos(kx - \omega t + \epsilon) + \gamma \sin(kx - \omega t + \epsilon) = a \big[ \cos(kx - \omega t) + \gamma \sin(kx - \omega t) \big]$$

para alguna constante $a$ que puede depender de $\epsilon$.

Escriba las ecuaciones que se derivan del requisito anterior. Encuentre las dos soluciones posibles para $\gamma$ y el valor de $a$ asociado a cada una. ¿Cuál es la solución que corresponde a nuestra descripción convencional de una onda material?

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*
