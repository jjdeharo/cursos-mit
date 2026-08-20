# Clases 20 y 21: Mecánica Cuántica en 3D y Potenciales Centrales

## Vídeos de esta clase (YouTube)

**Lección 20: Central potentials and angular momentum.**

- [Translation operator. Central potentials](https://www.youtube.com/watch?v=sPsDI0dICtc)
- [Angular momentum operators and their algebra](https://www.youtube.com/watch?v=xoCHe0mtxu0)
- [Commuting observables for angular momentum](https://www.youtube.com/watch?v=Mh8vUEStCQ8)
- [Simultaneous eigenstates and quantization of angular momentum](https://www.youtube.com/watch?v=lWTUcojZ_gQ)

**Lección 21: Legendre equation. Radial equation. Hydrogen atom 2-body problem.**

- [Associated Legendre functions and spherical harmonics](https://www.youtube.com/watch?v=Lt2Y6fLJ09Q)
- [Orthonormality of spherical harmonics](https://www.youtube.com/watch?v=gKSRrTik1SA)
- [Effective potential and boundary conditions at r=0](https://www.youtube.com/watch?v=_XDm2cxC-UU)
- [Hydrogen atom two-body problem](https://www.youtube.com/watch?v=7q32Wnm4dEw)

------------------------------------------------------------------------

*B. Zwiebach* *3 de mayo de 2016*

## Contenidos

1.  Ecuación de Schrödinger en 3D y momento angular
2.  El operador de momento angular
3.  Autoestados del momento angular
4.  La ecuación de onda radial

## 1. Ecuación de Schrödinger en 3D y momento angular

Hasta ahora hemos considerado varios operadores hermíticos: el operador de posición, el operador de momento y el operador de energía, o hamiltoniano. Estos operadores son observables y sus autovalores son los posibles resultados de medirlos sobre los estados. Aquí discutiremos otro operador: el momento angular. Es un operador vectorial, igual que el momento. Dará lugar a tres componentes, cada una de las cuales es un operador hermítico y por tanto una magnitud medible. La definición del operador de momento angular, como veremos, surge de su contraparte en mecánica clásica. Sin embargo, las propiedades del operador serán bastante nuevas y sorprendentes.

Habrá notado que el operador de momento tiene algo que ver con las traslaciones. En efecto, el operador de momento es una derivada en el espacio de coordenadas, y las derivadas están relacionadas con las traslaciones. La forma precisa en que esto ocurre es mediante la exponenciación. Consideremos una exponencial adecuada del operador de momento:

$$e^{\frac{i\hat{p}a}{\hbar}} , \qquad \text{(1.1)}$$

donde $a$ es una constante con unidades de longitud, lo que hace que el argumento de la exponencial sea adimensional. Consideremos ahora que este operador actúa sobre una función de onda $\psi(x)$

$$e^{\frac{i\hat{p}a}{\hbar}} \psi(x) = e^{a \frac{d}{dx}} \psi(x) , \qquad \text{(1.2)}$$

donde hemos simplificado el exponente. Expandiendo la exponencial obtenemos

$$e^{\frac{i\hat{p}a}{\hbar}} \psi(x) = \left( 1 + a\frac{d}{dx} + \frac{a^2}{2!}\frac{d^2}{dx^2} + \frac{a^3}{3!}\frac{d^3}{dx^3} + \ldots \right)\psi(x) ,$$

$$= \psi(x) + a\frac{d\psi}{dx} + \frac{a^2}{2!}\frac{d^2\psi}{dx^2} + \frac{a^3}{3!}\frac{d^3\psi}{dx^3} + \ldots = \psi(x+a) , \qquad \text{(1.3)}$$

ya que reconocemos la familiar expansión de Taylor. Este resultado significa que el operador $e^{\frac{i\hat{p}a}{\hbar}}$ desplaza la función de onda. De hecho la desplaza una distancia $-a$, ya que $\psi(x+a)$ es el desplazamiento de $\psi(x)$ por una distancia $-a$. Decimos que el operador de momento genera traslaciones. De manera similar, podremos mostrar que el operador de momento angular genera rotaciones. De nuevo, esto significa que exponenciales adecuadas del operador de momento angular actuando sobre funciones de onda las rotarán en el espacio.

El momento angular puede ser de tipo orbital, que es el caso familiar que ocurre cuando una partícula rota alrededor de algún punto fijo. Pero también puede ser momento angular de espín. Este es un tipo de momento angular bastante diferente y puede ser portado por partículas puntuales. Buena parte de la matemática del momento angular es válida tanto para el momento angular orbital como para el de espín.

Comencemos nuestro análisis del momento angular recordando que en tres dimensiones los operadores usuales $\hat{x}$ y $\hat{p}$ son operadores vectoriales:

$$\hat{p} = (\hat{p}_x, \hat{p}_y, \hat{p}_z) = \frac{\hbar}{i}\nabla = \frac{\hbar}{i}\left( \frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z} \right) .$$

$$\hat{x} = (\hat{x}, \hat{y}, \hat{z}) . \qquad \text{(1.4)}$$

Las relaciones de conmutación son las siguientes:

$$[\hat{x}, \hat{p}_x] = i\hbar ,$$

$$[\hat{y}, \hat{p}_y] = i\hbar , \qquad \text{(1.5)}$$

$$[\hat{z}, \hat{p}_z] = i\hbar .$$

¡Todos los demás conmutadores que involucran las tres coordenadas y los tres momentos son cero!

Consideremos una partícula representada por una función de onda tridimensional $\psi(x,y,z)$ que se mueve en un potencial tridimensional $V(\mathbf{r})$. La ecuación de Schrödinger toma la forma

$$-\frac{\hbar^2}{2m}\nabla^2 \psi(\mathbf{r}) + V(\mathbf{r})\psi(\mathbf{r}) = E\psi(\mathbf{r}) . \qquad \text{(1.6)}$$

Tenemos un potencial central si $V(\mathbf{r}) = V(r)$. Un potencial central no tiene dependencia angular, el valor del potencial depende únicamente de la distancia $r$ al origen. Un potencial central es esféricamente simétrico; las superficies de potencial constante son esferas centradas en el origen y por tanto es invariante bajo rotaciones. La ecuación anterior para un potencial central es

$$-\frac{\hbar^2}{2m}\nabla^2 \psi(\mathbf{r}) + V(r)\psi(\mathbf{r}) = E\psi(\mathbf{r}) . \qquad \text{(1.7)}$$

Esta ecuación será el objeto principal de nuestro estudio. Notemos que la función de onda es una función completa de $\mathbf{r}$; solo será invariante bajo rotaciones para los tipos más simples de soluciones. Dada la simetría rotacional del potencial, nos vemos llevados a expresar la ecuación de Schrödinger y las autofunciones de energía usando coordenadas esféricas.

En coordenadas esféricas, el laplaciano es

$$\nabla^2 \psi = (\nabla \cdot \nabla)\psi = \frac{1}{r}\frac{\partial^2}{\partial r^2}(r\psi) + \frac{1}{r^2}\left[ \frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left( \sin\theta \frac{\partial}{\partial\theta} \right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\varphi^2} \right]\psi . \qquad \text{(1.8)}$$

Por lo tanto la ecuación de Schrödinger para una partícula en un potencial central se convierte en

$$-\frac{\hbar^2}{2m}\left\{ \frac{1}{r}\frac{\partial^2}{\partial r^2}(r\psi) + \frac{1}{r^2}\left[ \frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left( \sin\theta \frac{\partial}{\partial\theta} \right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\varphi^2} \right] \right\}\psi + V(r)\psi = E\psi . \qquad \text{(1.9)}$$

En lo que sigue, nuestro objetivo será establecer dos hechos:

1.  La parte con dependencia angular del operador $\nabla^2$ puede identificarse como el cuadrado de la magnitud del operador de momento angular

$$\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left( \sin\theta \frac{\partial}{\partial\theta} \right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\varphi^2} = -\frac{L^2}{\hbar^2} \qquad \text{(1.10)}$$

donde

$$L^2 = \hat{L}_x \hat{L}_x + \hat{L}_y \hat{L}_y + \hat{L}_z \hat{L}_z . \qquad \text{(1.11)}$$

Esto implicará que la ecuación de Schrödinger se convierte en

$$-\frac{\hbar^2}{2m}\left[ \frac{1}{r}\frac{\partial^2}{\partial r^2}(r) - \frac{1}{r^2}\frac{L^2}{\hbar^2} \right]\psi + V(r)\psi = E\psi \qquad \text{(1.12)}$$

o desarrollando

$$-\frac{\hbar^2}{2m}\frac{1}{r}\frac{\partial^2}{\partial r^2}(r\psi) + \frac{L^2}{2mr^2}\psi + V(r)\psi = E\psi . \qquad \text{(1.13)}$$

1.  La ecuación (1.7) es la ecuación relevante para el problema de dos cuerpos cuando el potencial satisface

$$V(\mathbf{r}_1, \mathbf{r}_2) = V(|\mathbf{r}_1 - \mathbf{r}_2|) , \qquad \text{(1.14)}$$

es decir, si la energía potencial es simplemente una función de la distancia entre las partículas. Esto es cierto para la energía potencial electrostática entre el protón y el electrón que forman un átomo de hidrógeno. Por lo tanto, podremos tratar el átomo de hidrógeno como un problema de potencial central.

## 2. El operador de momento angular

Clásicamente estamos familiarizados con el momento angular, definido como el producto vectorial de $\mathbf{r}$ y $\mathbf{p}$: $\mathbf{L} = \mathbf{r} \times \mathbf{p}$. Por lo tanto tenemos

$$\mathbf{L} = (L_x, L_y, L_z) \equiv \mathbf{r} \times \mathbf{p} ,$$

$$L_x = yp_z - zp_y ,$$

$$L_y = zp_x - xp_z , \qquad \text{(2.1)}$$

$$L_z = xp_y - yp_x .$$

Usamos las relaciones anteriores para definir el operador cuántico de momento angular $\hat{\mathbf{L}}$ y sus componentes, los operadores $(\hat{L}_x, \hat{L}_y, \hat{L}_z)$:

$$\hat{\mathbf{L}} = (\hat{L}_x, \hat{L}_y, \hat{L}_z) ,$$

$$\hat{L}_x = \hat{y}\hat{p}_z - \hat{z}\hat{p}_y ,$$

$$\hat{L}_y = \hat{z}\hat{p}_x - \hat{x}\hat{p}_z , \qquad \text{(2.2)}$$

$$\hat{L}_z = \hat{x}\hat{p}_y - \hat{y}\hat{p}_x .$$

Al elaborar esta definición no encontramos ambigüedades de ordenamiento. Cada operador de momento angular es la diferencia de dos términos, cada término consistente en el producto de una coordenada y un momento. Pero notemos que en todos los casos se trata de una coordenada y un momento a lo largo de ejes distintos, por lo que conmutan. Si hubiéramos escrito $\hat{L}_x = \hat{p}_z\hat{y} - \hat{p}_y\hat{z}$, no habría importado, es lo mismo que el $\hat{L}_x$ de arriba. Es sencillo comprobar que los operadores de momento angular son hermíticos. Tomemos $\hat{L}_x$, por ejemplo. Recordando que para dos operadores cualesquiera $(AB)^\dagger = B^\dagger A^\dagger$ tenemos

$$(\hat{L}_x)^\dagger = (\hat{y}\hat{p}_z - \hat{z}\hat{p}_y)^\dagger = (\hat{y}\hat{p}_z)^\dagger - (\hat{z}\hat{p}_y)^\dagger = \hat{p}_z^\dagger \hat{y}^\dagger - \hat{p}_y^\dagger \hat{z}^\dagger . \qquad \text{(2.3)}$$

Dado que todas las coordenadas y momentos son operadores hermíticos, tenemos

$$(\hat{L}_x)^\dagger = \hat{p}_z\hat{y} - \hat{p}_y\hat{z} = \hat{y}\hat{p}_z - \hat{z}\hat{p}_y = \hat{L}_x , \qquad \text{(2.4)}$$

donde hemos movido los momentos a la derecha de las coordenadas en virtud de conmutadores nulos. Los otros dos operadores de momento angular también son hermíticos, así que tenemos

$$\hat{L}_x^\dagger = \hat{L}_x , \qquad \hat{L}_y^\dagger = \hat{L}_y , \qquad \hat{L}_z^\dagger = \hat{L}_z . \qquad \text{(2.5)}$$

Todos los operadores de momento angular son observables.

Dado un conjunto de operadores hermíticos, es natural preguntarse cuáles son sus conmutadores. Este cálculo nos permite ver si podemos medirlos simultáneamente. Calculemos el conmutador de $\hat{L}_x$ con $\hat{L}_y$:

$$[\hat{L}_x, \hat{L}_y] = [\hat{y}\hat{p}_z - \hat{z}\hat{p}_y, \hat{z}\hat{p}_x - \hat{x}\hat{p}_z] \qquad \text{(2.6)}$$

Vemos ahora que estos términos dejan de conmutar solo porque $\hat{z}$ y $\hat{p}_z$ no conmutan. De hecho, el primer término de $\hat{L}_x$ solo deja de conmutar con el primer término de $\hat{L}_y$. Igualmente, el segundo término de $\hat{L}_x$ solo deja de conmutar con el segundo término de $\hat{L}_y$. Por lo tanto

$$[\hat{L}_x, \hat{L}_y] = [\hat{y}\hat{p}_z, \hat{z}\hat{p}_x] + [\hat{z}\hat{p}_y, \hat{x}\hat{p}_z]$$

$$= [\hat{y}\hat{p}_z, \hat{z}]\hat{p}_x + \hat{x}[\hat{z}\hat{p}_y, \hat{p}_z]$$

$$= \hat{y}[\hat{p}_z, \hat{z}]\hat{p}_x + \hat{x}[\hat{z}, \hat{p}_z]\hat{p}_y \qquad \text{(2.7)}$$

$$= \hat{y}(-i\hbar)\hat{p}_x + \hat{x}(i\hbar)\hat{p}_y$$

$$= i\hbar(\hat{x}\hat{p}_y - \hat{y}\hat{p}_x) .$$

Ahora reconocemos que el operador en el lado derecho final es $\hat{L}_z$ y por tanto,

$$[\hat{L}_x, \hat{L}_y] = i\hbar \hat{L}_z . \qquad \text{(2.8)}$$

Las relaciones de conmutación básicas son completamente cíclicas, como se ilustra en la figura 1. En cualquier relación de conmutación podemos ciclar los operadores de posición como en $\hat{x} \to \hat{y} \to \hat{z} \to \hat{x}$ y los operadores de momento como en $\hat{p}_x \to \hat{p}_y \to \hat{p}_z \to \hat{p}_x$ y obtendremos otra relación de conmutación consistente. También puede verse que este ciclado lleva $\hat{L}_x \to \hat{L}_y \to \hat{L}_z \to \hat{L}_x$, observando (2.2). Por lo tanto afirmamos que no necesitamos calcular conmutadores de momento angular adicionales, y (2.8) conduce a

$$[\hat{L}_x, \hat{L}_y] = i\hbar \hat{L}_z ,$$

$$[\hat{L}_y, \hat{L}_z] = i\hbar \hat{L}_x , \qquad \text{(2.9)}$$

$$[\hat{L}_z, \hat{L}_x] = i\hbar \hat{L}_y .$$

Este es el conjunto completo de conmutadores de los operadores de momento angular. El conjunto se conoce como el álgebra del momento angular. Notemos que si bien los operadores $\hat{\mathbf{L}}$ se definieron en términos de coordenadas y momentos, la respuesta final para los conmutadores no involucra ni coordenadas ni momentos: ¡los conmutadores de momentos angulares dan momentos angulares! Los operadores $\hat{\mathbf{L}}$ a veces se denominan momento angular orbital, para distinguirlos de los operadores de momento angular de espín. Los operadores de momento angular de espín $\hat{S}_x$, $\hat{S}_y$ y $\hat{S}_z$ no pueden escribirse en términos de coordenadas y momentos. Son entidades más abstractas; de hecho su representación más simple es como ¡matrices de dos por dos! Aun así, al ser momentos angulares, satisfacen exactamente la misma álgebra que sus primos orbitales. Tenemos

$$[\hat{S}_x, \hat{S}_y] = i\hbar \hat{S}_z ,$$

$$[\hat{S}_y, \hat{S}_z] = i\hbar \hat{S}_x , \qquad \text{(2.10)}$$

$$[\hat{S}_z, \hat{S}_x] = i\hbar \hat{S}_y .$$

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes20_21_ES/fig1.png)

Figura 1: Las relaciones de conmutación del momento angular satisfacen la ciclicidad.

Hemos visto que el conmutador $[\hat{x}, \hat{p}] = i\hbar$ está asociado al hecho de que no podemos tener autoestados simultáneos de posición y de momento. Veamos ahora qué nos dicen los conmutadores de los operadores $\hat{\mathbf{L}}$. En particular: ¿podemos tener autoestados simultáneos de $\hat{L}_x$ y $\hat{L}_y$? Resulta que la respuesta es no, no podemos. Lo demostramos de la siguiente manera. Supongamos que existe una función de onda $\varphi_0$ que es simultáneamente autoestado de $\hat{L}_x$ y $\hat{L}_y$,

$$\hat{L}_x \varphi_0 = \lambda_x \varphi_0 ,$$

$$\hat{L}_y \varphi_0 = \lambda_y \varphi_0 . \qquad \text{(2.11)}$$

Haciendo actuar la primera identidad de conmutación de (2.9) sobre $\varphi_0$ tenemos

$$i\hbar \hat{L}_z \varphi_0 = [\hat{L}_x, \hat{L}_y]\varphi_0 = \hat{L}_x \hat{L}_y \varphi_0 - \hat{L}_y \hat{L}_x \varphi_0$$

$$= \hat{L}_x \lambda_y \varphi_0 - \hat{L}_y \lambda_x \varphi_0 \qquad \text{(2.12)}$$

$$= (\lambda_x \lambda_y - \lambda_y \lambda_x)\varphi_0 = 0 ,$$

lo que muestra que $\hat{L}_z \varphi_0 = 0$. Pero esto no es todo; mirando los otros conmutadores del álgebra de momento angular vemos que también se anulan al actuar sobre $\varphi_0$ y, como resultado, $\lambda_x$ y $\lambda_y$ deben ser cero:

$$[\hat{L}_y, \hat{L}_z]\varphi_0 = i\hbar \underbrace{\hat{L}_x \varphi_0}_{0} = i\hbar\, \lambda_x \varphi_0 = 0 \implies \lambda_x = 0 ,$$

$$[\hat{L}_z, \hat{L}_x]\varphi_0 = i\hbar \underbrace{\hat{L}_y \varphi_0}_{0} = i\hbar\, \lambda_y \varphi_0 = 0 \implies \lambda_y = 0 . \qquad \text{(2.13)}$$

En definitiva, suponer que $\varphi_0$ es un autoestado simultáneo de $\hat{L}_x$ y $\hat{L}_y$ ha llevado a $\hat{L}_x \varphi_0 = \hat{L}_y \varphi_0 = \hat{L}_z \varphi_0 = 0$. El estado es aniquilado por todos los operadores de momento angular. Esta situación trivial no es muy interesante. Hemos aprendido que es imposible encontrar estados que sean autoestados simultáneos no triviales de dos cualesquiera de los operadores de momento angular.

Para operadores hermíticos que conmutan, no hay problema en encontrar autoestados simultáneos. De hecho, los operadores hermíticos que conmutan siempre tienen un conjunto completo de autoestados simultáneos. Supongamos que elegimos $\hat{L}_z$ como uno de los operadores que queremos medir. ¿Podemos ahora encontrar un segundo operador hermítico que conmute con él? La respuesta es sí. Resulta que $L^2$, definido en (1.11), conmuta con $\hat{L}_z$ y es una elección interesante para un segundo operador. En efecto, comprobamos rápidamente

$$[\hat{L}_z, L^2] = [\hat{L}_z, \hat{L}_x\hat{L}_x] + [\hat{L}_z, \hat{L}_y\hat{L}_y]$$

$$= [\hat{L}_z, \hat{L}_x]\hat{L}_x + \hat{L}_x[\hat{L}_z, \hat{L}_x] + [\hat{L}_z, \hat{L}_y]\hat{L}_y + \hat{L}_y[\hat{L}_z, \hat{L}_y]$$

$$= i\hbar \hat{L}_y \hat{L}_x + i\hbar \hat{L}_x \hat{L}_y - i\hbar \hat{L}_x \hat{L}_y - i\hbar \hat{L}_x \hat{L}_y \qquad \text{(2.14)}$$

$$= 0 .$$

Así que deberíamos poder encontrar autoestados simultáneos tanto de $\hat{L}_z$ como de $L^2$. Haremos esto en breve. El operador $L^2$ es un operador de Casimir, lo que significa que conmuta con todos los operadores de momento angular. Al igual que conmuta con $\hat{L}_z$, también conmuta con $\hat{L}_x$ y $\hat{L}_y$.

Para entender mejor los operadores de momento angular, escribámoslos en coordenadas esféricas. Para esto necesitamos la relación entre $(r,\theta,\varphi)$ y las coordenadas cartesianas $(x,y,z)$:

$$x = r\sin\theta\cos\varphi , \qquad r = \sqrt{x^2+y^2+z^2} , \qquad \theta = \cos^{-1}\left(\frac{z}{r}\right) ,$$

$$y = r\sin\theta\sin\varphi , \qquad \varphi = \tan^{-1}\left(\frac{y}{x}\right) , \qquad \text{(2.15)}$$

$$z = r\cos\theta .$$

Hemos insinuado el hecho de que los operadores de momento angular generan rotaciones. En coordenadas esféricas, las rotaciones en torno al eje $z$ son las más simples: cambian $\varphi$ pero dejan invariante $\theta$. Ambas rotaciones en torno a los ejes $x$ e $y$ cambian tanto $\theta$ como $\varphi$. Por tanto podemos esperar que $\hat{L}_z$ sea simple en coordenadas esféricas. Usando la definición $\hat{L}_z = \hat{x}\hat{p}_y - \hat{y}\hat{p}_x$ tenemos

$$\hat{L}_z = \frac{\hbar}{i}\left( x\frac{\partial}{\partial y} - y\frac{\partial}{\partial x} \right) . \qquad \text{(2.16)}$$

Notemos que esto está relacionado con $\frac{\partial}{\partial\varphi}$ ya que, por la regla de la cadena,

$$\frac{\partial}{\partial\varphi} = \frac{\partial y}{\partial\varphi}\frac{\partial}{\partial y} + \frac{\partial x}{\partial\varphi}\frac{\partial}{\partial x} + \frac{\partial z}{\partial\varphi}\frac{\partial}{\partial z} = x\frac{\partial}{\partial y} - y\frac{\partial}{\partial x} , \qquad \text{(2.17)}$$

donde usamos (2.15) para evaluar las derivadas parciales. Usando las últimas dos ecuaciones podemos identificar

$$\hat{L}_z = \frac{\hbar}{i}\frac{\partial}{\partial\varphi} . \qquad \text{(2.18)}$$

Esta es una representación muy simple y útil. Confirma la interpretación de que $\hat{L}_z$ genera rotaciones alrededor del eje $z$, ya que tiene que ver con cambios en $\varphi$. Notemos que $\hat{L}_z$ es como un momento a lo largo del “círculo” definido por la coordenada $\varphi$ ($\varphi = \varphi + 2\pi$). Los demás operadores de momento angular son un poco más complicados. Un cálculo más largo muestra lo que sugerimos antes, que

$$-\frac{\hat{L}^2}{\hbar^2} = \frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left( \sin\theta \frac{\partial}{\partial\theta} \right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\varphi^2} . \qquad \text{(2.19)}$$

## 3. Autoestados del momento angular

Demostramos antes que los operadores hermíticos $\hat{L}_z$ y $L^2$ conmutan. Nuestro objetivo ahora es construir las autofunciones simultáneas de estos operadores. Serán funciones de $\theta$ y $\varphi$ y las llamaremos $\psi_{\ell m}(\theta,\varphi)$. Las condiciones para que sean autofunciones son

$$\hat{L}_z \psi_{\ell m} = \hbar m\, \psi_{\ell m} , \qquad m \in \mathbb{R}$$

$$\hat{L}^2 \psi_{\ell m} = \hbar^2 \ell(\ell+1)\, \psi_{\ell m} , \qquad \ell \in \mathbb{R} . \qquad \text{(3.1)}$$

Como corresponde a operadores hermíticos, los autovalores son reales. Tanto $m$ como $\ell$ son adimensionales; hay un $\hbar$ en el autovalor de $\hat{L}_z$ porque el momento angular tiene unidades de $\hbar$. Para el autovalor de $\hat{L}^2$ tenemos un $\hbar^2$. Notemos que hemos escrito el autovalor de $\hat{L}^2$ como $\ell(\ell+1)$ y para $\ell$ real esto siempre es mayor o igual que $-1/4$. De hecho, $\ell(\ell+1)$ va de cero a infinito conforme $\ell$ va de cero a infinito. Podemos mostrar que los autovalores de $\hat{L}^2$ no pueden ser negativos. Para esto primero afirmamos que

$$\langle \psi, \hat{L}^2 \psi \rangle \geq 0 , \qquad \text{(3.2)}$$

y tomando $\psi$ como una autofunción normalizada con autovalor $\lambda$ de $\hat{L}^2$ vemos inmediatamente que lo anterior da $\langle \psi, \lambda\psi \rangle = \lambda \geq 0$, como deseábamos. Para probar la ecuación anterior simplemente expandimos y usamos hermiticidad

$$\langle \psi, \hat{L}^2 \psi \rangle = \langle \psi, \hat{L}_x^2 \psi \rangle + \langle \psi, \hat{L}_y^2 \psi \rangle + \langle \psi, \hat{L}_z^2 \psi \rangle$$

$$= \langle \hat{L}_x \psi, \hat{L}_x \psi \rangle + \langle \hat{L}_y \psi, \hat{L}_y \psi \rangle + \langle \hat{L}_z \psi, \hat{L}_z \psi \rangle \geq 0 , \qquad \text{(3.3)}$$

porque cada uno de los tres sumandos es mayor o igual que cero.

Resolvamos ahora la primera ecuación de autovalores en (3.1) usando la representación en coordenadas (2.18) del operador $\hat{L}_z$:

$$\frac{\hbar}{i}\frac{\partial \psi_{\ell m}}{\partial \varphi} = \hbar m \psi_{\ell m} \;\; \to \;\; \frac{\partial \psi_{\ell m}}{\partial \varphi} = im\, \psi_{\ell m} . \qquad \text{(3.4)}$$

Esto determina la dependencia en $\varphi$ de la solución y escribimos

$$\psi_{\ell m}(\theta,\varphi) = e^{im\varphi}\, P_\ell^m(\theta) , \qquad \text{(3.5)}$$

donde la función $P_\ell^m(\theta)$ recoge la dependencia en $\theta$, todavía no determinada, de la autofunción $\psi_{\ell m}$. Exigiremos que $\psi_{\ell m}$ esté definida de forma única como función de los ángulos, y esto requiere que

$$\psi_{\ell m}(\theta, \varphi + 2\pi) = \psi_{\ell m}(\theta,\varphi) . \qquad \text{(3.6)}$$

*(Se podría haber intentado exigir que, tras un incremento de $2\pi$ en $\varphi$, la función de onda cambiara de signo, pero esto no conduce a un conjunto consistente de $\psi_{\ell m}$.)*

No hay una condición análoga para $\theta$. La condición anterior requiere que

$$e^{im(\varphi+2\pi)} = e^{im\varphi} \;\; \to \;\; e^{2\pi i m} = 1 . \qquad \text{(3.7)}$$

Esta ecuación implica que $m$ debe ser un entero:

$$m \in \mathbb{Z} . \qquad \text{(3.8)}$$

Esto completa nuestro análisis de la primera ecuación de autovalores. La segunda ecuación de autovalores en (3.1), usando nuestra expresión (2.19) para $\hat{L}^2$, da

$$-\hbar^2 \left[ \frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left( \sin\theta \frac{\partial}{\partial\theta} \right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\varphi^2} \right] \psi_{\ell m} = \hbar^2 \ell(\ell+1) \psi_{\ell m} . \qquad \text{(3.9)}$$

Multiplicamos por $\sin^2\theta$ y cancelamos $\hbar^2$ para obtener

$$\left[ \sin\theta \frac{\partial}{\partial\theta}\left( \sin\theta \frac{\partial}{\partial\theta} \right) + \frac{\partial^2}{\partial\varphi^2} \right]\psi_{\ell m} = -\ell(\ell+1)\sin^2\theta\, \psi_{\ell m} . \qquad \text{(3.10)}$$

Usando $\psi_{\ell m} = e^{im\varphi}P_\ell^m(\theta)$ podemos evaluar la acción de $\frac{\partial^2}{\partial\varphi^2}$ sobre $\psi_{\ell m}$ y luego cancelar el factor común $e^{im\varphi}$ para llegar a la ecuación diferencial

$$\sin\theta \frac{d}{d\theta}\left( \sin\theta \frac{dP_\ell^m}{d\theta} \right) - m^2 P_\ell^m = -\ell(\ell+1) P_\ell^m \sin^2\theta , \qquad \text{(3.11)}$$

o, equivalentemente,

$$\sin\theta \frac{d}{d\theta}\left( \sin\theta \frac{dP_\ell^m}{d\theta} \right) + \left[ \ell(\ell+1)\sin^2\theta - m^2 \right] P_\ell^m = 0 . \qquad \text{(3.12)}$$

Queremos dejar claro ahora que podemos ver a $P_\ell^m$ como una función de $\cos\theta$ escribiendo la ecuación diferencial en términos de $x = \cos\theta$. En efecto, esto da

$$\frac{d}{d\theta} = \frac{dx}{d\theta}\frac{d}{dx} = -\sin\theta \frac{d}{dx} \;\; \to \;\; \sin\theta \frac{d}{d\theta} = -(1-x^2)\frac{d}{dx} . \qquad \text{(3.13)}$$

La ecuación diferencial se convierte en

$$(1-x^2) \frac{d}{dx}\left[ (1-x^2) \frac{dP_\ell^m}{dx} \right] + \left[ \ell(\ell+1)(1-x^2) - m^2 \right] P_\ell^m(x) = 0 , \qquad \text{(3.14)}$$

y dividiendo por $1-x^2$ obtenemos la forma final:

$$\frac{d}{dx}\left[ (1-x^2) \frac{dP_\ell^m}{dx} \right] + \left[ \ell(\ell+1) - \frac{m^2}{1-x^2} \right] P_\ell^m(x) = 0 . \qquad \text{(3.15)}$$

Las $P_\ell^m(x)$ se llaman funciones asociadas de Legendre. No son polinomios. Todo lo que sabemos en este punto es que $m$ es un entero. Pronto descubriremos que $\ell$ es un entero no negativo y que, para un valor dado de $\ell$, hay un rango de valores posibles de $m$.

Para averiguar sobre $\ell$ consideramos la ecuación anterior para $m=0$. En ese caso escribimos $P_\ell(x) \equiv P_\ell^0(x)$ y las $P_\ell(x)$ deben satisfacer

$$\frac{d}{dx}\left[ (1-x^2)\frac{dP_\ell}{dx} \right] + \ell(\ell+1) P_\ell(x) = 0 . \qquad \text{(3.16)}$$

Esta es la ecuación diferencial de Legendre. Intentamos encontrar una solución en serie escribiendo

$$P_\ell(x) = \sum_{k=0}^{\infty} a_k x^k , \qquad \text{(3.17)}$$

suponiendo que $P_\ell(x)$ es regular en $x=0$, como conviene que sea. Sustituyendo esto en la ecuación diferencial obtenemos que la anulación del coeficiente de $x^k$ requiere:

$$(k+1)(k+2)a_{k+2} + \left[ \ell(\ell+1) - k(k+1) \right] a_k = 0 . \qquad \text{(3.18)}$$

Equivalentemente, tenemos

$$\frac{a_{k+2}}{a_k} = -\frac{\ell(\ell+1)-k(k+1)}{(k+1)(k+2)} . \qquad \text{(3.19)}$$

El comportamiento de los coeficientes para $k$ grande es tal que, a menos que la serie termine, $P_\ell$ diverge en $x=\pm 1$ (dado que $x=\cos\theta$, esto corresponde a $\theta = 0, \pi$). Para que la serie termine, debemos tener $\ell(\ell+1) = k(k+1)$ para algún entero $k \geq 0$. Simplemente podemos elegir $\ell = k$ de modo que $a_{k+2}=0$, haciendo de $P_k(x)$ un polinomio de grado $k$. Hemos aprendido así que los valores posibles de $\ell$ son

$$\ell = 0, 1, 2, 3, \ldots \qquad \text{(3.20)}$$

¡Esto es cuantización! Al igual que los valores de $m$ están cuantizados, también lo están los valores de $\ell$. Los polinomios de Legendre $P_\ell(x)$ están dados por la fórmula de Rodrigues:

$$P_\ell(x) = \frac{1}{2^\ell \ell!} \frac{d^\ell}{dx^\ell}\left( x^2 - 1 \right)^\ell . \qquad \text{(3.21)}$$

Los polinomios de Legendre tienen una función generatriz agradable

$$\sum_{\ell=0}^{\infty} P_\ell(x)\, s^\ell = \frac{1}{\sqrt{1-2xs+s^2}} . \qquad \text{(3.22)}$$

Algunos ejemplos son

$$P_0(x) = 1 , \qquad P_1(x) = x , \qquad P_2(x) = \frac{1}{2}\left( 3x^2 - 1 \right) . \qquad \text{(3.23)}$$

$P_\ell(x)$ es un polinomio de grado $\ell$ de paridad definida.

Habiendo resuelto la ecuación para $m=0$, debemos ahora discutir la ecuación general para $P_\ell^m(x)$. La ecuación diferencial involucra $m^2$ y no $m$, así que podemos tomar las soluciones para $m$ y $-m$ como iguales. Se puede mostrar que tomar $|m|$ derivadas de los polinomios de Legendre da una solución para $P_\ell^m(x)$:

$$P_\ell^m(x) = (1-x^2)^{|m|/2} \frac{d^{|m|}}{dx^{|m|}} P_\ell(x) . \qquad \text{(3.24)}$$

Como $P_\ell$ es un polinomio de grado $\ell$, la expresión anterior da un resultado no nulo solo para $|m| \leq \ell$. Así tenemos soluciones para

$$-\ell \leq m \leq \ell . \qquad \text{(3.25)}$$

Es posible probar que no existen otras soluciones. Se puede pensar en las autofunciones $\psi_{\ell m}$ como determinadas primero por el entero $\ell$ y, para un $\ell$ fijo, hay $2\ell+1$ elecciones de $m$: $-\ell, -\ell+1, \ldots, \ell$.

Nuestras autofunciones $\psi_{\ell m}$, con una normalización adecuada, se llaman los armónicos esféricos $Y_{\ell m}(\theta,\varphi)$. Los armónicos esféricos correctamente normalizados para $m \geq 0$ son

$$Y_{\ell,m}(\theta,\varphi) \equiv \sqrt{ \frac{2\ell+1}{4\pi} \frac{(\ell-m)!}{(\ell+m)!} } (-1)^m e^{im\varphi} P_\ell^m(\cos\theta) . \qquad \text{(3.26)}$$

Para $m<0$, usamos

$$Y_{\ell,m}(\theta,\varphi) = (-1)^m \left[ Y_{\ell,-m}(\theta,\varphi) \right]^* . \qquad \text{(3.27)}$$

Así tenemos

$$\hat{L}_z Y_{\ell m} = \hbar m\, Y_{\ell m} ,$$

$$\hat{L}^2 Y_{\ell m} = \hbar^2 \ell(\ell+1)\, Y_{\ell m} . \qquad \text{(3.28)}$$

Los primeros armónicos esféricos son

$$Y_{0,0}(\theta,\varphi) = \frac{1}{\sqrt{4\pi}} \qquad \text{(3.29)}$$

$$Y_{1,\pm 1}(\theta,\varphi) = \mp \sqrt{\frac{3}{8\pi}}\, e^{\pm i\varphi}\sin\theta = \mp \sqrt{\frac{3}{8\pi}}\, \frac{x\pm iy}{r} \qquad \text{(3.30)}$$

$$Y_{1,0}(\theta,\varphi) = \sqrt{\frac{3}{4\pi}}\cos\theta = \sqrt{\frac{3}{4\pi}}\, \frac{z}{r} . \qquad \text{(3.31)}$$

Al ser autoestados de operadores hermíticos con autovalores distintos, los armónicos esféricos con subíndices $\ell$ y $m$ diferentes son automáticamente ortogonales. El complicado factor de normalización es necesario para que tengan norma unitaria. Los armónicos esféricos forman un conjunto ortonormal con respecto a la integración sobre el ángulo sólido. Esta integración puede escribirse de varias formas:

$$\int d\Omega \cdots = \int_0^{2\pi} d\varphi \int_{\theta=0}^{\pi} d\theta \sin\theta \cdots = \int_0^{2\pi} d\varphi \int_{-1}^{1} d(\cos\theta) \cdots \qquad \text{(3.32)}$$

La afirmación de que los armónicos esféricos forman un conjunto ortonormal con respecto a esta integración significa que

$$\int d\Omega\, Y_{\ell',m'}^*(\theta,\varphi)\, Y_{\ell,m}(\theta,\varphi) = \delta_{\ell,\ell'}\, \delta_{m,m'} . \qquad \text{(3.33)}$$

## 4. La ecuación de onda radial

Escribamos ahora un ansatz para la solución de la ecuación de Schrödinger. Para esto tomamos el producto de una función puramente radial $R_{E\ell}(r)$ y un armónico esférico

$$\psi(r,\theta,\varphi) = R_{E\ell}(r)\, Y_{\ell,m}(\theta,\varphi) . \qquad \text{(4.1)}$$

Hemos puesto subíndices $E$ y $\ell$ para la función radial. No incluimos $m$, porque, como veremos, la ecuación para $R$ no depende de $m$. Podemos ahora insertar esto en la ecuación de Schrödinger (1.13)

$$-\frac{\hbar^2}{2m}\frac{1}{r}\frac{\partial^2}{\partial r^2}\left( r R_{E\ell} Y_{\ell m} \right) + \frac{\hat{L}^2}{2mr^2} R_{E\ell} Y_{\ell m} + V(r) R_{E\ell} Y_{\ell m} = E R_{E\ell} Y_{\ell m} . \qquad \text{(4.2)}$$

Dado que los armónicos esféricos son autoestados de $\hat{L}^2$ podemos simplificar la ecuación para obtener

$$-\frac{\hbar^2}{2m}\frac{1}{r}\frac{d^2(rR_{E\ell})}{dr^2} Y_{\ell m} + \frac{\hbar^2 \ell(\ell+1)}{2mr^2} R_{E\ell} Y_{\ell m} + V(r) R_{E\ell} Y_{\ell m} = E R_{E\ell} Y_{\ell m} . \qquad \text{(4.3)}$$

Cancelando el armónico esférico común y multiplicando por $r$ obtenemos una ecuación puramente radial

$$-\frac{\hbar^2}{2m}\frac{d^2(rR_{E\ell})}{dr^2} + \frac{\hbar^2 \ell(\ell+1)}{2mr^2}(rR_{E\ell}) + V(r)(rR_{E\ell}) = E(rR_{E\ell}) , \qquad \text{(4.4)}$$

Ahora es conveniente definir

$$u_{E\ell}(r) \equiv r R_{E\ell}(r) . \qquad \text{(4.5)}$$

Esto nos permite reescribir toda la ecuación diferencial como

$$-\frac{\hbar^2}{2m}\frac{d^2 u_{E\ell}}{dr^2} + \left[ V(r) + \frac{\hbar^2 \ell(\ell+1)}{2mr^2} \right] u_{E\ell} = E u_{E\ell} . \qquad \text{(4.6)}$$

Esto se llama la ecuación radial. Se parece a la familiar ecuación de Schrödinger independiente del tiempo en una dimensión, pero con un potencial efectivo

$$V_{\text{eff}}(r) = V(r) + \frac{\hbar^2 \ell(\ell+1)}{2mr^2} , \qquad \text{(4.7)}$$

que presenta el potencial original complementado por un término centrífugo, un potencial repulsivo proporcional al cuadrado del momento angular. Debido a este término, la ecuación radial es ligeramente diferente para cada valor de $\ell$. Como se anticipó, el número cuántico $m$ no aparece en la ecuación diferencial. La misma solución radial $u_{E\ell}(r)$ debe usarse para todos los valores permitidos de $m$.

Recordemos nuestra descomposición de la función de onda:

$$\psi(r,\theta,\varphi) = R_{E\ell}(r)\, Y_{\ell,m}(\theta,\varphi) = \frac{u_{E\ell}(r)}{r}\, Y_{\ell,m}(\theta,\varphi) . \qquad \text{(4.8)}$$

La condición de normalización requiere

$$1 = \int d^3x\, |\psi|^2 = \int r^2\, dr\, d\Omega\, \frac{|u_{E\ell}|^2}{r^2}\, Y_{\ell,m}^* Y_{\ell,m} . \qquad \text{(4.9)}$$

La integral angular da uno, los factores explícitos de $r$ se cancelan y obtenemos

$$\int_0^\infty dr\, |u_{E\ell}|^2 = 1 . \qquad \text{(4.10)}$$

En efecto, $u_{E\ell}(r)$ juega el papel de una función de onda unidimensional para una partícula que se mueve en el potencial efectivo a lo largo de $r$. Dado que solo se permite $r>0$, debemos considerar el posible comportamiento de la función de onda para $r=0$.

Podemos aprender sobre el comportamiento de la solución radial en el origen bajo la suposición razonable de que la barrera centrífuga domina el potencial cuando $r \to 0$. En este caso, los términos más singulares de la ecuación diferencial radial deben cancelarse entre sí, dejando términos menos singulares que podemos ignorar en este cálculo de orden principal. Así que ponemos:

$$-\frac{\hbar^2}{2m}\frac{d^2 u_{E\ell}}{dr^2} + \frac{\hbar^2 \ell(\ell+1)}{2mr^2} u_{E\ell} = 0 , \qquad \text{cuando } r \to 0 . \qquad \text{(4.11)}$$

o equivalentemente

$$\frac{d^2 u_{E\ell}}{dr^2} = \frac{\ell(\ell+1)}{r^2}\, u_{E\ell} . \qquad \text{(4.12)}$$

Las soluciones de esto pueden tomarse como $u_{E\ell} = r^s$ con $s$ una constante a determinar. Entonces encontramos

$$s(s-1) = \ell(\ell+1) \;\; \to \;\; s = \ell+1, \quad s = -\ell , \qquad \text{(4.13)}$$

lo que lleva a dos comportamientos posibles cerca de $r=0$:

$$u_{E\ell} \sim r^{\ell+1} , \qquad \text{o bien} \qquad u_{E\ell} \sim \frac{1}{r^\ell} . \qquad \text{(4.14)}$$

Para $\ell>0$, el segundo comportamiento no es consistente con la normalización, la función de onda diverge demasiado rápido cuando $r \to 0$. Para $\ell=0$, el segundo comportamiento, que lleva a $R \sim 1/r$, de hecho no es una solución de la ecuación de Schrödinger. Por lo tanto hemos establecido que para todo $\ell \geq 0$ debemos tener

$$u_{E\ell} \sim c\, r^{\ell+1} , \qquad \text{cuando } r \to 0 . \qquad \text{(4.15)}$$

Notemos que $u_{E\ell}$ se anula en $r=0$. Incluso para $\ell=0$, tenemos $u \sim r$ y $u$ se anula en $r=0$. En efecto hay una pared infinita en $r=0$, consistente con la imposibilidad de extender $r$ a valores negativos.

Recordemos que la dependencia radial completa de la función de onda se obtiene dividiendo $u_{E\ell}$ por $r$, de modo que

$$R_{E\ell} \sim c\, r^\ell . \qquad \text{(4.16)}$$

Esto permite una función de onda constante no nula en el origen solo para $\ell=0$. Solo para $\ell=0$ una partícula puede estar en el origen. Para $\ell \neq 0$ la “barrera” de momento angular impide que la partícula alcance el origen.

*Sarah Geller y Andrew Turner transcribieron las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare

https://ocw.mit.edu

8.04 Física Cuántica I

Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

# Apéndice: Lista de problemas 9 (Problem Set 9, 2016)

**Física Cuántica I (8.04) — Primavera de 2016** **Departamento de Física del MIT** **Tarea 9** *Fecha de entrega: viernes 29 de abril de 2016, 12:00 del mediodía* *21 de abril de 2016*

**Lectura:**

- Griffiths, sección 4.1.

## Problema 1

**Una comprobación numérica de la fase estacionaria. \[10 puntos\]**

Hemos utilizado la fase estacionaria para determinar la dependencia temporal de la posición de los picos en paquetes de ondas construidos a partir de representaciones integrales. De manera más general, la aproximación de fase estacionaria puede ayudarnos a obtener el valor de la propia integral.

Consideremos la integral de una gaussiana centrada en $x=2$ multiplicada por un factor de fase:

$$f(\lambda) = \int_{-\infty}^{\infty} dx\, e^{-100(x-2)^2} e^{i\varphi(\lambda,x)} , \qquad \varphi(\lambda,x) = 50\left(x-\tfrac{1}{32}\lambda x^4\right) , \quad \lambda \in \mathbb{R} .$$

Queremos confirmar que $|f(\lambda)|$ presenta un máximo en un valor $\lambda_*$ seleccionado por la fase estacionaria, y obtener el valor de $f(\lambda_*)$.

1.  ¿Cuál es la anchura $\Delta$ a media altura de la gaussiana? Es decir, ¿cuál es el mayor $\Delta$ tal que, para todo $x$ con $|x-2| \leq \tfrac{1}{2}\Delta$, la gaussiana sea mayor que la mitad de su máximo? Si tuviera que realizar la integral numéricamente, ¿sería seguro integrar entre 1 y 3? Explique su respuesta.

2.  Use la fase estacionaria para hallar el valor crítico $\lambda_*$ de $\lambda$ para el cual $f(\lambda)$ tendría la mayor magnitud. Para $\lambda_*$, escriba $\varphi(\lambda_*,x)$ como un desarrollo de Taylor alrededor de $x=2$ hasta e incluyendo los términos cuadráticos en $(x-2)$.

3.  ¿Cuál es la excursión de la fase $\varphi(\lambda_*,x)$ para $|x-2| < \tfrac{1}{2}\Delta$? Su resultado, expresado en unidades de $\pi$, debería indicar que es una buena aproximación ignorar la variación de la fase en el valor crítico. Hágalo así y realice a continuación la integral resultante de forma analítica. La respuesta es un número complejo. Escriba su resultado como una fase multiplicada por una magnitud.

4.  Realice la integral analíticamente usando la aproximación cuadrática para la fase. Escriba su resultado como una fase multiplicada por una magnitud.

5.  Realice la integral numéricamente en función de $\lambda$ para el intervalo $\lambda \in [0,1]$. Represente gráficamente el valor absoluto $|f(\lambda)|$. ¿Cuál es el valor de $f(\lambda)$ para el $\lambda$ crítico? Compárelo con sus estimaciones anteriores. ¿Cuál es el valor de $\lambda$ que produce el mayor $|f(\lambda)|$?

## Problema 2

**Comprobación del teorema de Levinson en un ejemplo \[10 puntos\]**

Para el potencial $V(x) = -V_0$ para $0<x<a$, $V(x)=0$ para $x>a$, y $V(x)=\infty$ para $x<0$, calculamos en clase el desfase $\delta(E)$, obteniendo

$$\tan\delta = \frac{1 - \dfrac{k'}{k}\cot k'a \, \tan ka}{\tan ka + \dfrac{k'}{k}\cot k'a} ,$$

con

$$k^2 = \frac{2mE}{\hbar^2} , \qquad k'^2 = \frac{2m(E+V_0)}{\hbar^2} , \qquad z_0^2 = \frac{2mV_0 a^2}{\hbar^2} .$$

1.  A medida que la energía $E$ tiende a cero, $ka \to 0$. ¿Qué ocurre con $k'a$? Demuestre que $\tan\delta$ tiende a cero, y por tanto podemos tomar $\delta \to 0$ cuando $ka \to 0$.

2.  ¿Cuál es el límite de $\tan\delta$ cuando $E \to \infty$? Explíquelo con detalle.

3.  Llame $u \equiv ka$ y escriba $\tan\delta$ como una función de $u$ y $z_0$:

$$\tan\delta = f(u; z_0) \quad \to \quad \delta = \operatorname{ArcTan}\big[f(u; z_0)\big] .$$

Escriba la función $f(u; z_0)$.

Para construir las gráficas con Mathematica, resultó difícil usar $\operatorname{ArcTan}[\ldots]$ porque utiliza el rango $(-\pi/2, \pi/2)$ y las gráficas presentan discontinuidades. Una opción (sugerida por W. Taylor) consiste en derivar la función $\operatorname{ArcTan}$ ¡y luego integrarla de nuevo! Puesto que $\delta=0$ para $u=0$, podemos escribir:

$$\delta(u; z_0) = \int_0^u du' \, \frac{d}{du'} \operatorname{ArcTan}\big[f(u'; z_0)\big] .$$

Deje que el ordenador derive e integre. Si encuentra una forma más sencilla de hacerlo, ¡háganoslo saber!

1.  Represente las fases $\delta(u,z_0)$ en función de $u$ para $z_0 = 2, 5, 9$. Para $z_0=2$ use $u \in [0,15]$, para $z_0=5$ use $u \in [0,20]$ y para $z_0=9$ use $u \in [0,30]$. En cada caso, explique cómo el resultado es consistente con el teorema de Levinson e indique cuán cerca está $\delta$ en el valor superior de $u$ del valor esperado de $\delta(E=\infty)$.

## Problema 3

**Dispersión por un escalón y una pared \[10 puntos\]**

Consideremos el potencial

$$V(x) = \begin{cases} V_0 , & 0<x<a , \quad V_0>0 , \\ 0 , & x>a , \\ \infty , & x \leq 0 . \end{cases}$$

Calcule el desfase $\delta(k)$ en función de $k$. Tendrá que considerar dos casos:

1.  $E(k) > V_0$. Llame $k'$ al número de onda para $x<a$. Puede intentar hacerlo desde el principio (a modo de práctica). También puede intentar usar el ejemplo resuelto en clase (y el problema 2 de esta lista), donde en lugar de un escalón teníamos un pozo de profundidad $V_0$, y modificar la respuesta adecuadamente. Deje su respuesta en la forma $\cot\delta = \ldots$.

2.  $E(k) < V_0$. Puede intentar hacerlo desde el principio (a modo de práctica). También puede intentar alguna continuación analítica del resultado del apartado (a). Deje su respuesta en la forma $\cot\delta = \ldots$.

3.  Represente $\delta(k)$ en función de $u = ka \in [0,\infty]$ para un potencial con $z_0 = 5$ (recuerde que $z_0^2 = \dfrac{2mV_0 a^2}{\hbar^2}$).

## Problema 4

**Dispersión por una delta de Dirac y una pared. \[15 puntos\]**

Consideremos nuestro habitual potencial unidimensional con $V(x) = \infty$ para $x \leq 0$, y con

$$V(x) = g\, \delta(x-a) , \qquad g>0 , \qquad x>0 .$$

Dispersamos partículas de masa $m$ y energía $E>0$ contra este potencial. Tenemos

$$(ka)^2 = \frac{2mEa^2}{\hbar^2} , \qquad \lambda \equiv \frac{mag}{\hbar^2} , \quad \text{sin unidades} .$$

1.  Calcule el desfase $\delta(k)$. Escriba la respuesta en la forma

$$\tan\delta = -\frac{\sin^2(ka)}{h(ka;\lambda)} ,$$

donde $h(ka;\lambda)$ es una función que debe determinar. Explique cómo, conocido $\delta$, se obtiene fácilmente la amplitud $A(k)$ que multiplica a la función ‘seno’ en la función de onda para $0<x<a$.

1.  Para comprender las características de $\tan\delta$, calcule la aproximación de orden principal para $ka \ll 1$. Discuta la dependencia del resultado en $\lambda$. Para $ka$ arbitrario, ¿en qué se convierte $\tan\delta$ cuando $\lambda \to \infty$?

2.  Represente $\delta$, el retraso temporal $\dfrac{1}{a}\dfrac{d\delta}{dk}$, y $|A|$ en función de $ka \in [0,10]$ para $\lambda=5$. ¿Observa resonancias? En caso afirmativo, identifique los valores de $ka$, el retraso temporal $\dfrac{1}{a}\dfrac{d\delta}{dk}$ y la magnitud de $|A|$. ¿Es la gráfica de $\delta$ consistente con el teorema de Levinson?

## Problema 5

**Algunos conmutadores y algunos valores esperados. \[10 puntos\]**

1.  Calcule los conmutadores

$$[L_z, x] , \qquad [L_z, y] , \qquad \text{y} \qquad [L_z, z] .$$

1.  Calcule los conmutadores

$$[L_z, p_x] , \qquad [L_z, p_y] , \qquad \text{y} \qquad [L_z, p_z] .$$

1.  Suponga que $\psi_0$ es una autofunción de $L_z$. Demuestre que $p_y$ y $p_x$ tienen valor esperado nulo en el estado $\psi_0$.

2.  Suponga que $\psi_0$ es una autofunción de $L_z$. Demuestre que $y$ y $x$ tienen valor esperado nulo en el estado $\psi_0$.

## Problema 6

**Momento angular en coordenadas esféricas. \[10 puntos\]**

1.  Calcule las nueve derivadas parciales de las coordenadas esféricas $(r,\theta,\varphi)$ respecto de las coordenadas cartesianas $(x,y,z)$, expresando sus respuestas en términos de las coordenadas esféricas.

2.  Use los resultados anteriores para escribir $L_x$, $L_y$ y $L_z$ como operadores diferenciales en coordenadas esféricas.

3.  Calcule $L_x^2$, $L_y^2$ y $L_z^2$ como operadores diferenciales en coordenadas esféricas y use sus resultados para deducir la forma esperada de $L^2$ como operador diferencial en coordenadas esféricas.

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*
