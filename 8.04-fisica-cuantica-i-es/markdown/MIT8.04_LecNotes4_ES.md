# Lección 4

## Vídeos de esta clase (YouTube)

**Lección 4: de Broglie matter waves. Group velocity and stationary phase. Wave for a free particle.**

- [de Broglie wavelength in different frames](https://www.youtube.com/watch?v=8x94EgM2Mpg)
- [Galilean transformation of ordinary waves](https://www.youtube.com/watch?v=YdtHAIh-kas)
- [The frequency of a matter wave](https://www.youtube.com/watch?v=3_qvO8bKGus)
- [Group velocity and stationary phase approximation](https://www.youtube.com/watch?v=-UgQEHHXTRM)
- [Motion of a wave-packet](https://www.youtube.com/watch?v=i81OpQJIH8U)
- [The wave for a free particle](https://www.youtube.com/watch?v=T6TQHNXy5Wg)

------------------------------------------------------------------------

*B. Zwiebach* *18 de febrero de 2016*

## Contenido

1.  Longitud de onda de de Broglie y transformaciones de Galileo
2.  Velocidades de fase y de grupo
3.  Elección de la función de onda para una partícula libre

## 1. Longitud de onda de de Broglie y transformaciones de Galileo

Hemos visto que a toda partícula libre con momento $p$ podemos asociarle una onda plana, o una “onda de materia”, con longitud de onda de de Broglie $\lambda = h/p$, con $p = |\vec{p}|$. La pregunta es, ¿ondas de qué? Bueno, esta onda se reconoce eventualmente como un ejemplo de lo que se llama la función de onda. La función de onda, como veremos, está gobernada por la ecuación de Schrödinger. Como hemos insinuado, la función de onda nos da información sobre probabilidades, e iremos desarrollando esta idea en detalle.

¿Tiene la onda propiedades direccionales o de polarización como los campos eléctrico y magnético en una onda electromagnética? Sí, existe un análogo de esto, aunque no profundizaremos en ello ahora. ¡El análogo de la polarización corresponde al espín! Los efectos del espín son despreciables en muchos casos (velocidades pequeñas, ausencia de campos magnéticos, por ejemplo) y por esta razón usamos simplemente una onda escalar, un número complejo

$$\Psi(x, t) \in \mathbb{C} \qquad \text{(1.1)}$$

que depende del espacio y del tiempo. Surgen de manera natural un par de preguntas obvias. ¿Es medible la función de onda? ¿Qué tipo de objeto es? ¿Qué describe? Para obtener intuición sobre esto, consideremos cómo perciben distintos observadores la longitud de onda de de Broglie de una partícula, lo cual nos ayudará a entender qué tipo de ondas estamos considerando. Recordemos que

$$p = \frac{h}{\lambda} = \frac{h}{2\pi}\frac{2\pi}{\lambda} = \hbar k, \qquad \text{(1.2)}$$

donde $k$ es el número de onda. ¿Cómo se comportaría esta onda bajo un cambio de referencial?

Consideramos entonces dos referenciales $S$ y $S'$ con los ejes $x$ y $x'$ alineados, y con $S'$ moviéndose hacia la derecha a lo largo de la dirección $+x$ de $S$ con velocidad constante $v$. En el instante $t=0$, los orígenes de ambos referenciales coinciden.

Las coordenadas de espacio y tiempo de los dos referenciales están relacionadas por una transformación de Galileo, que establece que

$$x' = x - vt, \qquad t' = t . \qquad \text{(1.3)}$$

En efecto, el tiempo transcurre a la misma velocidad en todos los referenciales galileanos, y la relación entre $x$ y $x'$ es evidente a partir del arreglo mostrado en la Fig. 1.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes4_ES/fig1.png)

Figura 1: El referencial $S'$ se mueve con velocidad $v$ a lo largo de la dirección $x$ del referencial $S$. Una partícula de masa $m$ se mueve con velocidad $\tilde v$, y por lo tanto con momento $p = m\tilde v$, en el referencial $S$.

Supongamos ahora que ambos observadores se centran en una partícula de masa $m$ que se mueve con velocidad no relativista. Llamemos a la velocidad y al momento en el referencial $S$ como $\tilde v$ y $p = m\tilde v$, respectivamente. Se sigue, derivando respecto de $t = t'$ la primera ecuación en (1.3), que

$$\frac{dx'}{dt'} = \frac{dx}{dt} - v, \qquad \text{(1.4)}$$

lo cual significa que la velocidad de la partícula $\tilde v\,'$ en el referencial $S'$ está dada por

$$\tilde v\,' = \tilde v - v . \qquad \text{(1.5)}$$

Multiplicando por la masa $m$ encontramos la relación entre los momentos en los dos referenciales

$$p' = p - mv . \qquad \text{(1.6)}$$

El momento $p'$ en el referencial $S'$ puede ser apreciablemente distinto del momento $p$ en el referencial $S$. Así, los observadores en $S'$ y en $S$ obtendrán longitudes de onda de de Broglie $\lambda'$ y $\lambda$ bastante distintas. En efecto,

$$\lambda' = \frac{h}{p'} = \frac{h}{p - mv} \neq \lambda, \qquad \text{(1.7)}$$

¡Esto es muy extraño! Como repasamos ahora, para las ondas ordinarias que se propagan en el referencial de reposo de un medio (como las ondas sonoras o las ondas en el agua) los observadores galileanos encontrarán cambios de frecuencia pero ningún cambio en la longitud de onda. Esto es intuitivamente claro: para hallar la longitud de onda basta con tomar una fotografía de la onda en un instante dado, y ambos observadores que miren la fotografía coincidirán en el valor de la longitud de onda. Por otro lado, para medir la frecuencia, cada observador debe esperar cierto tiempo para ver pasar un período completo de la onda. Esto tomará un tiempo distinto para los distintos observadores.

Demostremos estas afirmaciones cuantitativamente. Comenzamos con la afirmación de que la fase $\varphi = kx - \omega t$ de tal onda es un invariante galileano. La onda misma puede ser $\cos\varphi$ o $\sin\varphi$ o alguna combinación, pero el hecho es que el valor físico de la onda en cualquier punto y tiempo debe ser acordado por los dos observadores. La onda es un observable. Dado que todas las características de la onda (picos, ceros, etc.) están controladas por la fase, los dos observadores deben coincidir en el valor de la fase.

En el referencial $S$ la fase se puede escribir de la siguiente manera

$$\varphi = kx - \omega t = k\left(x - \frac{\omega}{k} t\right) = \frac{2\pi}{\lambda}(x - Vt) = \frac{2\pi x}{\lambda} - \frac{2\pi V}{\lambda} t, \qquad \text{(1.8)}$$

donde $V = \omega/k$ es la velocidad de la onda. Nótese que la longitud de onda se lee del coeficiente de $x$, y que $\omega$ es menos el coeficiente de $t$. Los dos observadores deben coincidir en el valor de $\varphi$. Es decir, debemos tener

$$\varphi'(x', t') = \varphi(x, t) \qquad \text{(1.9)}$$

donde las coordenadas y tiempos están relacionados por una transformación de Galileo. Por lo tanto

$$\varphi'(x', t') = \frac{2\pi}{\lambda}(x - Vt) = \frac{2\pi}{\lambda}(x' + vt' - Vt') = \frac{2\pi}{\lambda} x' - \frac{2\pi(V - v)}{\lambda} t' . \qquad \text{(1.10)}$$

Dado que el lado derecho está expresado en términos de las variables primadas, podemos leer $\lambda'$ del coeficiente de $x'$ y $\omega'$ como menos el coeficiente de $t'$:

$$\lambda' = \lambda \qquad \text{(1.11)}$$

$$\omega' = \frac{2\pi}{\lambda}(V - v) = \frac{2\pi V}{\lambda}\left(1 - \frac{v}{V}\right) = \omega\left(1 - \frac{v}{V}\right) . \qquad \text{(1.12)}$$

Esto confirma que, como afirmamos, para una onda física que se propaga en un medio, la longitud de onda es un invariante galileano y la frecuencia se transforma.

¿Qué significa entonces que la longitud de onda de las ondas de materia cambie bajo una transformación de Galileo? Significa que las ondas $\Psi$ ¡no son directamente medibles! Su valor no corresponde a una magnitud medible sobre la cual todos los observadores galileanos deban coincidir. Así, la función de onda no necesita ser invariante bajo transformaciones de Galileo:

$$\Psi(x, t) \neq \Psi'(x', t') , \qquad \text{(1.13)}$$

donde $(x, t)$ y $(x', t')$ están relacionados por transformaciones de Galileo y por lo tanto representan el mismo punto y el mismo instante. Ustedes averiguarán en la tarea la relación correcta entre $\Psi(x, t)$ y $\Psi'(x', t')$.

¿Cuál es la frecuencia $\omega$ de la onda de de Broglie para una partícula con momento $p$? Teníamos

$$p = \hbar k \qquad \text{(1.14)}$$

lo cual fija la longitud de onda en términos del momento. La frecuencia $\omega$ de la onda está determinada por la relación

$$E = \hbar \omega , \qquad \text{(1.15)}$$

que también fue postulada por de Broglie y fija $\omega$ en términos de la energía $E$ de la partícula. Nótese que, para nuestro enfoque en partículas no relativistas, la energía $E$ está determinada por el momento a través de la relación

$$E = \frac{p^2}{2m} . \qquad \text{(1.16)}$$

Podemos dar tres evidencias de que (1.15) es una relación razonable.

1.  Si superponemos ondas de materia para formar un paquete de ondas que representa a la partícula, el paquete se moverá con la llamada velocidad de grupo $v_g$, que de hecho coincide con la velocidad de la partícula. La velocidad de grupo se obtiene derivando $\omega$ respecto de $k$, como repasaremos en breve:

$$v_g = \frac{d\omega}{dk} = \frac{dE}{dp} = \frac{d}{dp}\left(\frac{p^2}{2m}\right) = \frac{p}{m} = v . \qquad \text{(1.17)}$$

1.  La relación también está sugerida por la relatividad especial. La energía y las componentes del momento de una partícula forman un cuadrivector:

$$\left(\frac{E}{c}, \vec p\right) \qquad \text{(1.18)}$$

De manera similar, para ondas cuyas fases son invariantes relativistas tenemos otro cuadrivector

$$\left(\frac{\omega}{c}, \vec k\right) \qquad \text{(1.19)}$$

Igualar dos cuadrivectores es una elección consistente: sería válida en todos los referenciales de Lorentz. Como se puede ver, ambas relaciones de de Broglie se siguen de

$$\left(\frac{E}{c}, \vec p\right) = \hbar\left(\frac{\omega}{c}, \vec k\right) . \qquad \text{(1.20)}$$

1.  Para los fotones, (1.15) es consistente con los cuantos de energía de Einstein, ya que $E = h\nu = \hbar\omega$.

En resumen, tenemos

$$p = \hbar k, \qquad E = \hbar \omega . \qquad \text{(1.21)}$$

Estas se llaman las relaciones de de Broglie, y son válidas para todas las partículas.

## 2. Velocidades de fase y de grupo

Para entender la velocidad de grupo formamos paquetes de onda e investigamos con qué rapidez se mueven. Para esto simplemente supondremos que $\omega(k)$ es alguna función arbitraria de $k$. Consideremos una superposición de ondas planas $e^{i(kx-\omega(k)t)}$ dada por

$$\psi(x, t) = \int dk\, \Phi(k) e^{i(kx-\omega(k)t)} . \qquad \text{(2.22)}$$

Suponemos que la función $\Phi(k)$ tiene un pico alrededor de cierto número de onda $k = k_0$, como se muestra en la Fig. 2.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes4_ES/fig2.png)

Figura 2: Se supone que la función $\Phi(k)$ tiene un pico alrededor de $k = k_0$.

Para motivar la siguiente discusión, consideremos el caso en que $\Phi(k)$ no solo tiene un pico alrededor de $k_0$, sino que además es real (dejaremos caer esta suposición más adelante). En este caso, la fase $\phi$ del integrando proviene únicamente de la exponencial:

$$\phi(k) = kx - \omega(k) t . \qquad \text{(2.23)}$$

Deseamos entender para qué valores de $x$ y $t$ el paquete $\psi(x,t)$ toma valores grandes. Usamos el principio de fase estacionaria: dado que solo para $k \sim k_0$ la integral sobre $k$ tiene posibilidad de dar una contribución no nula, el factor de fase debe ser estacionario en $k = k_0$. La idea es simple: si una función se multiplica por una fase que varía rápidamente, la integral se cancela en promedio. Por lo tanto, la fase debe tener derivada nula en $k_0$. Aplicando esta idea a nuestra fase, hallamos la derivada y la igualamos a cero en $k_0$:

$$\left.\frac{d\phi}{dk}\right|_{k_0} = x - \left.\frac{d\omega}{dk}\right|_{k_0} t = 0 . \qquad \text{(2.24)}$$

Esto significa que $\psi(x,t)$ es apreciable cuando $x$ y $t$ están relacionados por

$$x = \left.\frac{d\omega}{dk}\right|_{k_0} t , \qquad \text{(2.25)}$$

lo cual muestra que el paquete se mueve con velocidad de grupo

$$v_g = \left.\frac{d\omega}{dk}\right|_{k_0} . \qquad \text{(2.26)}$$

**Ejercicio.** Si $\Phi(k_0)$ no es real, escriba $\Phi(k) = |\Phi(k)| e^{i\phi(k)}$. Encuentre la nueva versión de (2.25) y muestre que la velocidad de la onda no cambia.

Hagamos ahora un cálculo más detallado que confirme el análisis anterior y aporte cierta comprensión adicional. Notemos primero que

$$\psi(x, 0) = \int dk\, \Phi(k) e^{ikx} . \qquad \text{(2.27)}$$

Expandimos $\omega(k)$ en una serie de Taylor alrededor de $k = k_0$

$$\omega(k) = \omega(k_0) + (k - k_0) \left.\frac{d\omega}{dk}\right|_{k_0} + O\!\left((k-k_0)^2\right) . \qquad \text{(2.28)}$$

Entonces encontramos, despreciando los términos $O((k-k_0)^2)$

$$\psi(x, t) = \int dk\, \Phi(k)\, e^{ikx}\, e^{-i\omega(k_0)t}\, e^{-i(k-k_0)\left.\frac{d\omega}{dk}\right|_{k_0} t} . \qquad \text{(2.29)}$$

Conviene sacar de la integral todos los factores que no dependen de $k$:

$$\psi(x, t) = e^{-i\omega(k_0)t + ik_0 \left.\frac{d\omega}{dk}\right|_{k_0} t} \int dk\, \Phi(k)\, e^{ikx}\, e^{-ik \left.\frac{d\omega}{dk}\right|_{k_0} t}$$

$$= e^{-i\omega(k_0)t + ik_0 \left.\frac{d\omega}{dk}\right|_{k_0} t} \int dk\, \Phi(k)\, e^{ik\left(x - \left.\frac{d\omega}{dk}\right|_{k_0} t\right)} . \qquad \text{(2.30)}$$

Comparando con (2.27) nos damos cuenta de que la integral en la expresión anterior puede escribirse en términos de la función de onda en el instante cero:

$$\psi(x, t) = e^{-i\omega(k_0)t + ik_0 \left.\frac{d\omega}{dk}\right|_{k_0} t}\; \psi\!\left(x - \left.\frac{d\omega}{dk}\right|_{k_0} t\right) . \qquad \text{(2.31)}$$

Los factores de fase que preceden a la expresión no son importantes para rastrear dónde está el paquete de ondas. En particular, podemos tomar la norma de ambos lados de la ecuación para hallar

$$|\psi(x, t)| = \left|\psi\!\left(x - \left.\frac{d\omega}{dk}\right|_{k_0} t,\; 0\right)\right| . \qquad \text{(2.32)}$$

Si $\psi(x, 0)$ tiene un pico en cierto valor $x_0$, resulta claro de la ecuación anterior que $|\psi(x, t)|$ tiene un pico en

$$x - \left.\frac{d\omega}{dk}\right|_{k_0} t = x_0 \quad \longrightarrow \quad x = x_0 + \left.\frac{d\omega}{dk}\right|_{k_0} t , \qquad \text{(2.33)}$$

lo cual muestra que el pico del paquete se mueve con velocidad $v_{gr} = \dfrac{d\omega}{dk}$, evaluada en $k_0$.

## 3. Elección de la función de onda para una partícula libre

¿Cuál es la forma matemática de la onda asociada con una partícula con energía $E$ y momento $p$? Sabemos que $\omega$ y $k$ están determinados a partir de $E = \hbar\omega$ y $p = \hbar k$. Supongamos que queremos que nuestra onda se propague en la dirección $+\hat x$. Todas las siguientes son ejemplos de ondas que podrían ser candidatas para la función de onda de la partícula.

1.  $\sin(kx - \omega t)$

2.  $\cos(kx - \omega t)$

3.  $e^{i(kx-\omega t)} = e^{ikx} e^{-i\omega t}$ — dependencia temporal $\propto e^{-i\omega t}$

4.  $e^{-i(kx-\omega t)} = e^{-ikx} e^{i\omega t}$ — dependencia temporal $\propto e^{+i\omega t}$

En la tercera y cuarta opciones hemos indicado que la dependencia temporal podría venir con cualquiera de los dos signos. ¡Usaremos la superposición para decidir cuál es la correcta! Estamos buscando una función de onda que sea no nula para todos los valores de $x$.

Tomémoslas una por una:

1.  Partiendo de (1), construimos una superposición en la cual la partícula tiene igual probabilidad de encontrarse moviéndose en las direcciones $+x$ y $-x$.

$$\Psi(x, t) = \sin(kx - \omega t) + \sin(kx + \omega t) \qquad \text{(3.1)}$$

Expandiendo las funciones trigonométricas, esto se puede simplificar a

$$\Psi(x, t) = 2\sin(kx)\cos(\omega t) . \qquad \text{(3.2)}$$

Pero este resultado no es razonable. La función de onda se anula idénticamente para todo $x$ en ciertos instantes especiales

$$\omega t = \frac{\pi}{2}, \frac{3\pi}{2}, \frac{5\pi}{2}, \dots \qquad \text{(3.3)}$$

Una función de onda que es cero no puede representar a una partícula.

1.  Construyendo una función de onda a partir de (2) con una superposición de ondas coseno que van hacia la izquierda y hacia la derecha,

$$\Psi(x, t) = \cos(kx - \omega t) + \cos(kx + \omega t) = 2\cos(kx)\cos(\omega t) . \qquad \text{(3.4)}$$

Esta elección no sirve, también se anula idénticamente cuando $\omega t = \dfrac{\pi}{2}, \dfrac{3\pi}{2}, \dots$

1.  Probemos una superposición similar de exponenciales a partir de (3), con ambas teniendo la misma dependencia temporal

$$\Psi(x, t) = e^{i(kx-\omega t)} + e^{i(-kx-\omega t)} \qquad \text{(3.5)}$$

$$= (e^{ikx} + e^{-ikx})\, e^{-i\omega t} \qquad \text{(3.6)}$$

$$= 2\cos(kx)\, e^{-i\omega t} . \qquad \text{(3.7)}$$

¡Esta función de onda cumple con nuestro criterio! Nunca es cero para todos los valores de $x$ porque $e^{-i\omega t}$ nunca es cero.

1.  Una superposición de exponenciales a partir de (4) también cumple con nuestro criterio

$$\Psi(x, t) = e^{-i(kx-\omega t)} + e^{-i(-kx-\omega t)} \qquad \text{(3.8)}$$

$$= (e^{ikx} + e^{-ikx})\, e^{i\omega t} \qquad \text{(3.9)}$$

$$= 2\cos(kx)\, e^{i\omega t} . \qquad \text{(3.10)}$$

Esto nunca es cero para todos los valores de $x$.

Dado que tanto la opción (3) como la (4) parecen funcionar, nos preguntamos: ¿podemos usar tanto (3) como (4) para representar a una partícula que se mueve hacia la derecha (en la dirección $+\hat x$)? Supongamos que sí podemos. Entonces, dado que sumar un estado a sí mismo no debería cambiar el estado, podríamos representar a la partícula que se mueve hacia la derecha usando la suma de (3) y (4)

$$\Psi(x, t) = e^{i(kx-\omega t)} + e^{-i(kx-\omega t)} = 2\cos(kx - \omega t) . \qquad \text{(3.11)}$$

Esto, sin embargo, es lo mismo que (2), lo cual ya mostramos que lleva a dificultades. Por lo tanto debemos elegir entre (3) y (4).

La elección es una cuestión de convención, y todos los físicos usan la misma convención. Tomamos la función de onda de la partícula libre como

$$\text{Función de onda de la partícula libre:} \qquad \Psi(x, t) = e^{i(kx-\omega t)} , \qquad \text{(3.12)}$$

que representa a una partícula con

$$p = \hbar k , \qquad \text{y} \qquad E = \hbar \omega . \qquad \text{(3.13)}$$

En tres dimensiones, la función de onda correspondiente sería

$$\text{Función de onda de la partícula libre:} \qquad \Psi(x, t) = e^{i(\vec k \cdot \vec x-\omega t)} , \qquad \text{(3.14)}$$

que representa a una partícula con

$$p = \hbar k, \qquad \text{y} \qquad E = \hbar \omega . \qquad \text{(3.15)}$$

Andrew Turner y Sarah Geller transcribieron las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.

------------------------------------------------------------------------

MIT OpenCourseWare https://ocw.mit.edu

8.04 Física Cuántica I Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.
