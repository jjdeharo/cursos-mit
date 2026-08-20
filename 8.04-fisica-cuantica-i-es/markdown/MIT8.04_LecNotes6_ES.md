# Lección 6

## Vídeos de esta clase (YouTube)

**Lección 6: Probability density and current. Hermitian conjugation.**

- [Normalizable wavefunctions and the question of time evolution](https://www.youtube.com/watch?v=d4skxu7MpFI)
- [Is probability conserved? Hermiticity of the Hamiltonian](https://www.youtube.com/watch?v=5L4QfjbK87M)
- [Probability current and current conservation](https://www.youtube.com/watch?v=J2ltXyByPJA)
- [Three dimensional current and conservation](https://www.youtube.com/watch?v=Ex_fFlwZoM0)

------------------------------------------------------------------------

B. Zwiebach

23 de febrero de 2016

## Contenido

1.  Normalización y evolución temporal
2.  La función de onda como amplitud de probabilidad
3.  La corriente de probabilidad
4.  Corriente de probabilidad en 3D y conservación de la corriente

## 1. Normalización y evolución temporal

La función de onda $\Psi(x, t)$ que describe la mecánica cuántica de una partícula de masa $m$ moviéndose en un potencial $V(x, t)$ satisface la ecuación de Schrödinger

$$i\hbar \frac{\partial \Psi(x, t)}{\partial t} = \left( -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} + V(x, t) \right) \Psi(x, t) , \qquad \text{(1.1)}$$

o, más brevemente,

$$i\hbar \frac{\partial \Psi(x, t)}{\partial t} = \hat{H} \Psi(x, t) . \qquad \text{(1.2)}$$

La interpretación de la función de onda surge al declarar que $dP$, definido por

$$dP = |\Psi(x, t)|^2 \, dx , \qquad \text{(1.3)}$$

es la probabilidad de encontrar la partícula en el intervalo $dx$ centrado en $x$ en el instante $t$. De ahí se sigue que las probabilidades de encontrar la partícula en todos los puntos posibles deben sumar uno:

$$\int_{-\infty}^{\infty} \Psi^*(x, t) \, \Psi(x, t) \, dx = 1 . \qquad \text{(1.4)}$$

Intentaremos entender cómo esta ecuación es compatible con la evolución temporal prescrita por la ecuación de Schrödinger. Pero antes de eso, examinemos qué tipo de condiciones se requieren de las funciones de onda para satisfacer (1.4).

Supongamos que la función de onda tiene límites bien definidos cuando $x \to \pm\infty$. Si esos límites son distintos de cero, la integral en el entorno del infinito produciría un resultado infinito, lo cual es incompatible con la afirmación de que la integral total vale uno. Por lo tanto, los límites deben ser cero:

$$\lim_{x \to \pm\infty} \Psi(x, t) = 0 . \qquad \text{(1.5)}$$

En principio es posible tener una función de onda que no tenga un límite bien definido en el infinito pero que aun así sea de cuadrado integrable. Pero tales casos no parecen aparecer en la práctica, así que supondremos que (1.5) se cumple. También sería natural suponer que la derivada espacial de $\Psi$ se anula cuando $x \to \pm\infty$ pero, como veremos en breve, basta con suponer que el límite de la derivada espacial de $\Psi$ está acotado

$$\lim_{x \to \pm\infty} \frac{\partial \Psi(x, t)}{\partial x} < \infty . \qquad \text{(1.6)}$$

Hemos enfatizado antes que el factor numérico global que multiplica a la función de onda no es físico. Pero la ecuación (1.4) parece estar en conflicto con esto: ¡si una $\Psi$ dada la satisface, la presuntamente equivalente $2\Psi$ no lo hará! Para dar un sentido preciso a las probabilidades es conveniente trabajar con funciones de onda normalizadas, pero no es necesario, como mostramos ahora. Dado que el tiempo no desempeña ningún papel en el argumento, supongamos en todo lo que sigue que las ecuaciones se refieren a algún instante $t_0$ arbitrario pero fijo. Supongamos que se tiene una función de onda tal que

$$\int dx \, |\Psi|^2 = N \neq 1 . \qquad \text{(1.7)}$$

Entonces afirmo que la probabilidad $dP$ de encontrar la partícula en el intervalo $dx$ en torno a $x$ viene dada por

$$dP = \frac{1}{N} |\Psi|^2 \, dx . \qquad \text{(1.8)}$$

Esto es consistente porque

$$\int dP = \frac{1}{N} \int dx \, |\Psi|^2 = \frac{1}{N} \cdot N = 1 . \qquad \text{(1.9)}$$

Nótese que $dP$ no cambia cuando $\Psi$ se multiplica por cualquier número. Así, esta interpretación deja claro que la escala global de $\Psi$ no contiene física alguna. Mientras la integral $\int |\Psi|^2 \, dx < \infty$ la función de onda se dice normalizable, o de cuadrado integrable. Ajustando el coeficiente global de $\Psi$ podemos entonces hacerla normalizada. En efecto, suponiendo nuevamente (1.7), la nueva función de onda $\Psi'$ definida por

$$\Psi' = \frac{1}{\sqrt{N}} \Psi , \qquad \text{(1.10)}$$

está correctamente normalizada. En efecto

$$\int dx \, |\Psi'|^2 = \frac{1}{N} \int |\Psi|^2 \, dx = 1 . \qquad \text{(1.11)}$$

A veces trabajamos con funciones de onda para las cuales la integral (1.4) es infinita. Tales funciones de onda pueden ser muy útiles. De hecho, la onda plana de de Broglie $\Psi = \exp(ikx - i\omega t)$ para una partícula libre es un buen ejemplo: dado que $|\Psi|^2 = 1$, la integral es de hecho infinita. Lo que esto significa es que $\exp(ikx - i\omega t)$ no representa realmente a una sola partícula. Para construir una función de onda de cuadrado integrable podemos usar una superposición de ondas planas. Es en efecto una sorpresa agradable que ¡la superposición de infinitas ondas no normalizables sea de cuadrado integrable!

## 2. La función de onda como amplitud de probabilidad

Comencemos con una función de onda normalizada en el instante inicial $t_0$

$$\int_{-\infty}^{\infty} \Psi^*(x, t_0) \Psi(x, t_0) \, dx = 1 . \qquad \text{(2.1)}$$

Dado que $\Psi(x, t_0)$ y la ecuación de Schrödinger determinan $\Psi$ para todos los tiempos, ¿tenemos entonces

$$\int_{-\infty}^{\infty} \Psi^*(x, t) \Psi(x, t) \, dx = 1 \, ? \qquad \text{(2.2)}$$

Definamos la densidad de probabilidad $\rho(x, t)$

$$\rho(x, t) \equiv \Psi^*(x, t) \Psi(x, t) = |\Psi(x, t)|^2 . \qquad \text{(2.3)}$$

Definamos también $N(t)$ como la integral de la densidad de probabilidad en todo el espacio:

$$N(t) \equiv \int \rho(x, t) \, dx . \qquad \text{(2.4)}$$

La afirmación en (2.1) de que la función de onda comienza bien normalizada es

$$N(t_0) = 1 , \qquad \text{(2.5)}$$

y la condición de que permanezca normalizada en todos los tiempos posteriores es $N(t) = 1$. Esto quedaría garantizado si mostráramos que para todo tiempo

$$\frac{dN(t)}{dt} = 0 . \qquad \text{(2.6)}$$

A esto lo llamamos conservación de la probabilidad. Comprobemos si la ecuación de Schrödinger garantiza que esta condición se cumpla:

$$\begin{aligned}
\frac{dN(t)}{dt} &= \int_{-\infty}^{\infty} \frac{\partial \rho(x, t)}{\partial t} \, dx \\
&= \int_{-\infty}^{\infty} \left( \frac{\partial \Psi^*}{\partial t} \Psi(x, t) + \Psi^*(x, t) \frac{\partial \Psi(x, t)}{\partial t} \right) dx .
\end{aligned} \qquad \text{(2.7)}$$

A partir de la ecuación de Schrödinger, y su conjugada compleja

$$i\hbar \frac{\partial \Psi}{\partial t} = \hat{H} \Psi \implies \frac{\partial \Psi}{\partial t} = -\frac{i}{\hbar} \hat{H} \Psi , \qquad \text{(2.8)}$$

$$-i\hbar \frac{\partial \Psi^*}{\partial t} = (\hat{H} \Psi)^* \implies \frac{\partial \Psi^*}{\partial t} = \frac{i}{\hbar} (\hat{H} \Psi)^* . \qquad \text{(2.9)}$$

Al conjugar de forma compleja la ecuación de Schrödinger usamos que el conjugado complejo de la derivada temporal de $\Psi$ es simplemente la derivada temporal del conjugado complejo de $\Psi$. Para conjugar el lado derecho simplemente añadimos el asterisco a todo $\hat{H}\Psi$. Ahora usamos (2.8) y (2.9) en (2.7) para obtener

$$\begin{aligned}
\frac{dN(t)}{dt} &= \int_{-\infty}^{\infty} \left( \frac{i}{\hbar} (\hat{H}\Psi)^* \Psi - \frac{i}{\hbar} \Psi^* (\hat{H}\Psi) \right) dx \\
&= \frac{i}{\hbar} \int_{-\infty}^{\infty} (\hat{H}\Psi)^* \Psi \, dx - \frac{i}{\hbar} \int_{-\infty}^{\infty} \Psi^* (\hat{H}\Psi) \, dx .
\end{aligned} \qquad \text{(2.10)}$$

Para mostrar que la derivada temporal de $N(t)$ se anula, basta con mostrar que

$$\int_{-\infty}^{\infty} (\hat{H}\Psi)^* \Psi = \int_{-\infty}^{\infty} \Psi^* (\hat{H}\Psi) . \qquad \text{(2.11)}$$

La ecuación (2.11) es la condición sobre el operador hamiltoniano $\hat{H}$ para la conservación de la probabilidad. De hecho, si $\hat{H}$ es un operador hermítico la condición se satisfará. El operador $\hat{H}$ es un operador hermítico si satisface

$$\text{Operador hermítico:} \qquad \int_{-\infty}^{\infty} (\hat{H}\Psi_1)^* \Psi_2 = \int_{-\infty}^{\infty} \Psi_1^* (\hat{H}\Psi_2) . \qquad \text{(2.12)}$$

Aquí tenemos dos funciones de onda que son arbitrarias, pero que satisfacen las condiciones (1.5) y (1.6). Como se puede ver, un operador hermítico puede trasladarse de actuar sobre la primera función a actuar sobre la segunda función. Cuando las dos funciones son la misma, recuperamos la condición (2.11).

Vale la pena cerrar este círculo de ideas definiendo el conjugado hermítico $T^\dagger$ del operador lineal $T$. Esto se hace de la siguiente manera:

$$\int_{-\infty}^{\infty} \Psi_1^* (T \Psi_2) = \int_{-\infty}^{\infty} (T^\dagger \Psi_1)^* \Psi_2 . \qquad \text{(2.13)}$$

El operador $T^\dagger$, que también es lineal, se calcula partiendo del lado izquierdo y tratando de reescribir la expresión sin ningún operador actuando sobre la segunda función. Se dice que un operador $T$ es hermítico si es igual a su conjugado hermítico:

$$T \text{ es hermítico si } \quad T^\dagger = T . \qquad \text{(2.14)}$$

Los operadores hermíticos son muy importantes en mecánica cuántica. Tienen autovalores reales y siempre se puede encontrar una base del espacio de estados en términos de autoestados ortonormales. Resulta que los observables en mecánica cuántica están representados por operadores hermíticos, y los posibles valores medidos de esos observables vienen dados por sus autovalores. Nuestra búsqueda para mostrar que la normalización se preserva bajo la evolución temporal en mecánica cuántica se ha reducido a mostrar que el operador hamiltoniano es hermítico.

## 3. La corriente de probabilidad

Examinemos más de cerca el integrando de la ecuación (2.10). Usando la expresión explícita para el hamiltoniano tenemos

$$\begin{aligned}
\frac{\partial \rho}{\partial t} &= \frac{i}{\hbar} \left( (\hat{H}\Psi)^* \Psi - \Psi^* (\hat{H}\Psi) \right) \\
&= \frac{i}{\hbar} \left( -\frac{\hbar^2}{2m} \frac{\partial^2 \Psi^*}{\partial x^2} \Psi - \Psi^* \left( -\frac{\hbar^2}{2m} \frac{\partial^2 \Psi}{\partial x^2} \right) + V(x, t) \Psi^* \Psi - \Psi^* V(x, t) \Psi \right) .
\end{aligned} \qquad \text{(3.1)}$$

Las contribuciones del potencial se cancelan y obtenemos entonces

$$\frac{i}{\hbar} \left( (\hat{H}\Psi)^* \Psi - \Psi^* (\hat{H}\Psi) \right) = \frac{\hbar}{2im} \left( \frac{\partial^2 \Psi^*}{\partial x^2} \Psi - \Psi^* \frac{\partial^2 \Psi}{\partial x^2} \right) . \qquad \text{(3.2)}$$

La única posibilidad de mostrar que la integral del lado derecho es cero es mostrar que es una derivada total. ¡Y en efecto lo es!

$$\begin{aligned}
\frac{i}{\hbar} \left( (\hat{H}\Psi)^* \Psi - \Psi^* (\hat{H}\Psi) \right)
&= \frac{\partial}{\partial x} \left[ \frac{\hbar}{2im} \left( \frac{\partial \Psi^*}{\partial x} \Psi - \Psi^* \frac{\partial \Psi}{\partial x} \right) \right] \\
&= -\frac{\partial}{\partial x} \left[ \frac{\hbar}{2im} \left( \Psi^* \frac{\partial \Psi}{\partial x} - \frac{\partial \Psi^*}{\partial x} \Psi \right) \right] \\
&= -\frac{\partial}{\partial x} \left[ \frac{\hbar}{2im} \, 2i \, \mathrm{Im}\!\left( \Psi^* \frac{\partial \Psi}{\partial x} \right) \right] \\
&= -\frac{\partial}{\partial x} \left[ \frac{\hbar}{m} \, \mathrm{Im}\!\left( \Psi^* \frac{\partial \Psi}{\partial x} \right) \right] ,
\end{aligned} \qquad \text{(3.3)}$$

donde usamos que $z - z^* = 2i \, \mathrm{Im}(z)$. Recordemos que el lado izquierdo que hemos evaluado es en realidad $\dfrac{\partial \rho}{\partial t}$, y por lo tanto el resultado obtenido hasta ahora es

$$\frac{\partial \rho}{\partial t} + \frac{\partial}{\partial x} \left[ \frac{\hbar}{m} \, \mathrm{Im}\!\left( \Psi^* \frac{\partial \Psi}{\partial x} \right) \right] = 0 . \qquad \text{(3.4)}$$

Esta ecuación codifica la conservación de la carga y es del tipo

$$\frac{\partial \rho}{\partial t} + \frac{\partial J}{\partial x} = 0 , \qquad \text{(3.5)}$$

donde $J(x, t)$ es la corriente asociada a la densidad de carga $\rho$. Hemos identificado por lo tanto una corriente de probabilidad

$$J(x, t) \equiv \frac{\hbar}{m} \, \mathrm{Im}\!\left( \Psi^* \frac{\partial \Psi}{\partial x} \right) . \qquad \text{(3.6)}$$

Solo hay una componente para esta corriente ya que la partícula se mueve en una dimensión. Las unidades de $J$ son el inverso del tiempo, o probabilidad por unidad de tiempo, como verificamos ahora.

Para una dimensión espacial, $[\Psi] = L^{-1/2}$, lo cual se ve fácilmente a partir del requisito de que $\int dx \, |\Psi|^2$ no tenga unidades. (Cuando se trabaja con $d$ dimensiones espaciales la función de onda tendrá unidades de $L^{-d/2}$). Tenemos entonces

$$\left[ \Psi^* \frac{\partial \Psi}{\partial x} \right] = \frac{1}{L^2} , \qquad [\hbar] = \frac{ML^2}{T} , \qquad \left[ \frac{\hbar}{m} \right] = \frac{L^2}{T} , \qquad \text{(3.7)}$$

$$\implies [J] = \frac{1}{T} = \text{probabilidad por unidad de tiempo} \qquad \text{(3.8)}$$

Ahora podemos mostrar que la derivada temporal de $N$ es cero. En efecto, usando (3.5) tenemos

$$\frac{dN}{dt} = \int_{-\infty}^{\infty} \frac{\partial \rho}{\partial t} \, dx = -\int_{-\infty}^{\infty} \frac{\partial J}{\partial x} \, dx = -\big( J(\infty, t) - J(-\infty, t) \big) . \qquad \text{(3.9)}$$

La derivada se anula si la corriente de probabilidad se anula en el infinito. Recordando que

$$J = \frac{\hbar}{2im} \left( \Psi^* \frac{\partial \Psi}{\partial x} - \Psi \frac{\partial \Psi^*}{\partial x} \right) , \qquad \text{(3.10)}$$

vemos que la corriente en efecto se anula porque nos restringimos a funciones de onda para las cuales $\lim_{x \to \pm\infty} \Psi = 0$ y $\lim_{x \to \pm\infty} \dfrac{\partial \Psi}{\partial x}$ permanece acotado. Por lo tanto tenemos

$$\frac{dN}{dt} = 0 , \qquad \text{(3.11)}$$

como queríamos mostrar.

Para ilustrar cómo funciona la conservación de la probabilidad de manera más general en una dimensión, centrémonos en un segmento $x \in [a, b]$. Entonces la probabilidad $P_{ab}$ de encontrar la partícula en el segmento $[a, b]$ viene dada por

$$P_{ab} = \int_a^b \rho(x, t) \, dx . \qquad \text{(3.12)}$$

Si ahora tomamos la derivada temporal de esto y, como antes, usamos la conservación de la corriente, obtenemos

$$\frac{dP_{ab}}{dt} = -\int_a^b \frac{\partial J(x, t)}{\partial x} \, dx = -J(b, t) + J(a, t) . \qquad \text{(3.13)}$$

Este es el resultado esperado. Si la cantidad de probabilidad en la región $[a, b]$ cambia en el tiempo, debe deberse a la corriente de probabilidad que fluye hacia dentro o hacia fuera en los bordes del intervalo. Suponiendo que las corrientes en $x = b$ y en $x = a$ son positivas, notamos que la probabilidad fluye hacia afuera en $x = b$ y entra en $x = a$. Los signos en el lado derecho anterior reflejan correctamente el efecto de estos flujos sobre la tasa de cambio de la probabilidad total dentro del segmento.

## 4. Corriente de probabilidad en 3D y conservación de la corriente

La determinación de la corriente de probabilidad $J$ para una partícula que se mueve en tres dimensiones sigue la misma ruta tomada antes, pero usamos la versión 3D de la ecuación de Schrödinger. Tras algo de trabajo (tarea) la densidad de probabilidad y la corriente resultan ser

$$\rho(\mathbf{x}, t) = |\Psi(\mathbf{x}, t)|^2 , \qquad J(\mathbf{x}, t) = \frac{\hbar}{m} \, \mathrm{Im}\!\left( \Psi^* \nabla \Psi \right) , \qquad \text{(4.1)}$$

y satisfacen la ecuación de conservación

$$\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{J} = 0 . \qquad \text{(4.2)}$$

En tres dimensiones espaciales, $[\Psi] = L^{-3/2}$ y las unidades de $J$ se determinan rápidamente

$$[\Psi^* \nabla \Psi] = \frac{1}{L^4} , \qquad \left[ \frac{\hbar}{m} \right] = \frac{L^2}{T} , \qquad \text{(4.3)}$$

$$\implies [J] = \frac{1}{T L^2} = \text{probabilidad por unidad de tiempo por unidad de área} \qquad \text{(4.4)}$$

La ecuación de conservación (4.2) resulta particularmente clara en lenguaje integral. Consideremos una región fija $V$ del espacio y la probabilidad $Q_V(t)$ de encontrar la partícula dentro de la región:

$$Q_V(t) = \int_V \rho(\mathbf{x}, t) \, d^3x . \qquad \text{(4.5)}$$

La derivada temporal de la probabilidad se calcula entonces usando la ecuación de conservación

$$\frac{dQ_V}{dt} = \int_V \frac{\partial \rho}{\partial t} \, d^3x = -\int_V \nabla \cdot \mathbf{J} \, d^3x . \qquad \text{(4.6)}$$

Finalmente, usando la ley de Gauss, encontramos

$$\frac{dQ_V}{dt} = -\int_S \mathbf{J} \cdot d\mathbf{a} , \qquad \text{(4.7)}$$

donde $S$ es la frontera del volumen $V$. La interpretación aquí es clara. La probabilidad de que la partícula esté dentro de $V$ puede cambiar en el tiempo si hay un flujo de la corriente de probabilidad a través de la frontera de la región. Cuando el volumen se extiende por todo el espacio, la frontera está en el infinito, y las condiciones sobre la función de onda (que no hemos discutido en el caso 3D) implican que el flujo a través de la frontera en el infinito se anula.

Nuestra densidad de probabilidad, corriente de probabilidad y conservación de la corriente están en perfecta analogía con la densidad de carga electromagnética, la densidad de corriente y la conservación de la corriente. En electromagnetismo las cargas fluyen, en mecánica cuántica la probabilidad fluye. Los términos de la correspondencia se resumen en la siguiente tabla.

|  | Electromagnetismo | Mecánica cuántica |
|------------------------|------------------------|------------------------|
| $\rho$ | densidad de carga | densidad de probabilidad |
| $Q_V$ | carga en un volumen $V$ | probabilidad de encontrar la partícula en $V$ |
| $J$ | densidad de corriente | densidad de corriente de probabilidad |

Sarah Geller transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.

------------------------------------------------------------------------

MIT OpenCourseWare

https://ocw.mit.edu

8.04 Física Cuántica I

Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.
