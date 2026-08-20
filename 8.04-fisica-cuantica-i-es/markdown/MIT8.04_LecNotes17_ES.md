# Capítulo 17: Transmisión resonante y efecto Ramsauer–Townsend

## Vídeos de esta clase (YouTube)

**Lección 17: Ramsauer-Townsend effect. Scattering in 1D.**

- [Waves on the finite square well](https://www.youtube.com/watch?v=EdRkQmmq7vk)
- [Resonant transmission](https://www.youtube.com/watch?v=KkSr0SvXfNY)
- [Ramsauer-Townsend phenomenology](https://www.youtube.com/watch?v=5u-9lFhCl5w) (10:16)
- [Scattering in 1D. Incoming and outgoing waves](https://www.youtube.com/watch?v=twdF0EIbFds)
- [Scattered wave and phase shift](https://www.youtube.com/watch?v=w49WAat6ymk)

------------------------------------------------------------------------

*B. Zwiebach* *26 de abril de 2016*

## Contenido

1.  Transmisión resonante en un pozo cuadrado
2.  El efecto Ramsauer–Townsend

## 1. Transmisión resonante en un pozo cuadrado

Consideremos el pozo cuadrado finito

$$V(x) =
\begin{cases}
0, & \text{para } |x| > a, \\
-V_0, & \text{para } |x| < a.
\end{cases}
\qquad \text{(1.1)}$$

Aquí $V_0 > 0$ tiene unidades de energía. Consideramos un autoestado de energía, una solución de dispersión con $E > 0$ que representa una función de onda incidente que se aproxima al pozo desde la izquierda. Un ansatz para el autoestado tendrá la forma

$$\psi(x) =
\begin{cases}
Ae^{ikx} + Be^{-ikx}, & x < -a, \\
Ce^{ik_2 x} + De^{-ik_2 x}, & |x| < a, \\
Fe^{ikx}, & x > a.
\end{cases}
\qquad \text{(1.2)}$$

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes17_ES/fig1.png)

Figura 1: El pozo cuadrado con todas las ondas relevantes representadas; la onda con coeficiente $A$ incide desde la izquierda.

Aquí $A$ es el coeficiente de la onda incidente que existe para $x < -a$, y $B$ es el coeficiente de la onda reflejada (véase la Figura 1). Ambas ondas tienen número de onda $k$. En la región del pozo $|x| < a$ tenemos una onda que se mueve hacia la derecha, con coeficiente $C$, y una onda que se mueve hacia la izquierda, con coeficiente $D$. El número de onda en esta región se denomina $k_2$. A la derecha del pozo tenemos solo una onda, que se mueve hacia la derecha, con coeficiente $F$ y número de onda $k$. Nótese que, aunque el potencial es una función par de $x$, un autoestado de energía no normalizable no tiene por qué ser par ni impar. La simetría se rompe por la condición de que la onda incide desde la izquierda. Los valores de $k$ y $k_2$, ambos positivos, quedan determinados por la ecuación de Schrödinger y son

$$k^2 = \frac{2mE}{\hbar^2}, \qquad k_2^2 = \frac{2m(E + V_0)}{\hbar^2}. \qquad \text{(1.3)}$$

Hay cuatro condiciones de contorno: continuidad de $\psi$ y $\psi'$ en $x = -a$ y en $x = a$. Estas cuatro ecuaciones pueden usarse para fijar los coeficientes $B$, $C$, $D$ y $F$ en términos de $A$. Definimos los coeficientes de reflexión y transmisión $R$ y $T$ de la siguiente manera:

$$R \equiv \frac{|B|^2}{|A|^2}, \qquad T \equiv \frac{|F|^2}{|A|^2}. \qquad \text{(1.4)}$$

De la conservación de la corriente de probabilidad sabemos que las corrientes a la izquierda y a la derecha del pozo deben ser iguales, de modo que

$$|A|^2 - |B|^2 = |F|^2. \qquad \text{(1.5)}$$

Esta no es una ecuación independiente; debe deducirse de las condiciones de contorno. Implica que

$$R + T = \frac{|B|^2}{|A|^2} + \frac{|F|^2}{|A|^2} = 1, \qquad \text{(1.6)}$$

lo que muestra que nuestra definición de $R$ y $T$ tiene sentido.

Resolver para $R$ y $T$ es directo pero un poco laborioso. Citemos simplemente el resultado que se obtiene. El coeficiente de transmisión es la siguiente función de la energía $E$ del autoestado:

$$\frac{1}{T} = 1 + \frac{1}{4}\frac{V_0^2}{E(E+V_0)}\sin^2(2k_2 a). \qquad \text{(1.7)}$$

Dado que el segundo término del lado derecho es manifiestamente positivo, tenemos $T \le 1$. Cuando $E \to 0$, tenemos $\frac{1}{T} \to 1 + \infty$, lo que significa que $T \to 0$. Cuando $E \to \infty$, tenemos $T \to 1$.

Podemos eliminar todas las unidades de este resultado definiendo

$$e \equiv \frac{E}{V_0}, \qquad z_0^2 \equiv \frac{2ma^2 V_0}{\hbar^2}. \qquad \text{(1.8)}$$

Entonces,

$$(k_2 a)^2 = \frac{2ma^2(E+V_0)}{\hbar^2} = \frac{2ma^2 V_0}{\hbar^2}(1+e) \;\; \to \;\; 2k_2 a = 2z_0\sqrt{1+e}, \qquad \text{(1.9)}$$

de modo que tenemos

$$\frac{1}{T} = 1 + \frac{1}{4e(1+e)}\sin^2\!\left(2z_0\sqrt{1+e}\right). \qquad \text{(1.10)}$$

Ahora podemos ver que el pozo se vuelve transparente, haciendo $T = 1$, para ciertos valores de la energía. Todo lo que necesitamos es que el argumento de la función seno sea un múltiplo de $\pi$:

$$2z_0\sqrt{1+e} = n\pi, \quad n \in \mathbb{Z}. \qquad \text{(1.11)}$$

No todos los enteros están permitidos. Como $e > 0$, el lado izquierdo es mayor o igual que $2z_0$ y, por lo tanto,

$$n \ge \frac{2z_0}{\pi}. \qquad \text{(1.12)}$$

Llamemos $E_n = e_n V_0$ a las energías asociadas. Entonces

$$e_n + 1 = \frac{n^2\pi^2}{4z_0^2} = \frac{n^2\pi^2\hbar^2}{2m(2a)^2 V_0}, \qquad \text{(1.13)}$$

de modo que

$$E_n + V_0 = \frac{n^2\pi^2\hbar^2}{2m(2a)^2}. \qquad \text{(1.14)}$$

Nótese que $E_n + V_0$ es la energía del estado de dispersión medida respecto al fondo del pozo cuadrado. El lado derecho es la energía del $n$-ésimo estado ligado del pozo cuadrado infinito de anchura $2a$. Obtenemos así un resultado bastante sorprendente: obtenemos transmisión total para aquellas energías $E_n > 0$ que están en el espectro de la extensión de pozo cuadrado infinito de nuestro pozo cuadrado finito. La desigualdad $n \ge \frac{2z_0}{\pi}$ garantiza que $E_n > 0$. Dado que los estados ligados del pozo cuadrado infinito se caracterizan por ajustar un número entero de semilongitudes de onda, tenemos una situación de tipo resonancia en la que la transmisión perfecta ocurre cuando las ondas de dispersión encajan perfectamente dentro del pozo cuadrado finito. El fenómeno que hemos observado se denomina ¡transmisión resonante!

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes17_ES/fig2.png)

Figura 2: Obtenemos transmisión resonante a través del pozo finito en las energías de estado ligado positivas de un supuesto pozo infinito.

El ajuste de un número exacto de semilongitudes de onda también puede verse directamente a partir de la anulación de la función seno en (1.7), que da $k_2(2a) = n\pi$, lo que implica

$$\frac{2\pi}{\lambda}(2a) = n\pi \;\; \to \;\; 2a = n\,\frac{\lambda}{2}. \qquad \text{(1.15)}$$

Mostramos en la Figura 3 el coeficiente de transmisión $T$ en función de $e = E/V_0$ para un pozo cuadrado con $z_0 = 13\pi/4$. En este caso debemos tener $n \ge \frac{13}{2}$, es decir, $n \ge 7$.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes17_ES/fig3.png)

Figura 3: El coeficiente de transmisión $T$ en función de $e$ para un pozo cuadrado con $z_0 = 13\pi/4$. En las energías en las que $T = 1$ tenemos dispersión resonante. Los valores de $E_7, E_8, \ldots$ se indican en la figura. Hay tres casos de transmisión resonante para $0 < E < V_0$. Nótese que el espaciado entre los puntos donde $T = 1$ crece a medida que $e$ crece.

## 2. El efecto Ramsauer–Townsend

Carl Ramsauer y John Sealy Townsend publicaron por separado sus investigaciones en 1921. Estaban estudiando la dispersión elástica de electrones de baja energía por átomos de gases nobles. Estos gases tienen sus capas electrónicas completamente llenas y son a la vez muy poco reactivos y poseen altas energías de ionización. El potencial es creado por el núcleo y se hace visible a medida que el electrón incidente penetra en la nube electrónica. Este potencial es un potencial atractivo esféricamente simétrico para los electrones: una especie de pozo esférico finito. En el experimento, algunos electrones colisionan con los átomos y se dispersan, la mayoría rebotando hacia atrás. ¡Podemos así considerar el coeficiente de reflexión $R$ como un indicador (proxy) de la sección eficaz de dispersión!

Ramsauer y Townsend reportaron un fenómeno muy inusual. A energías muy bajas, la sección eficaz de dispersión era alta. Pero la dependencia con la energía resultaba sorprendente. A medida que la energía aumentaba, la dispersión disminuía hasta acercarse a cero, para volver a aumentar cuando la energía se incrementaba aún más. Tal comportamiento misterioso no tenía una explicación clásica razonable. Lo que está en juego es la dispersión resonante cuántica. ¡Que la sección eficaz tienda a cero significa que el coeficiente de reflexión tiende a cero, y el coeficiente de transmisión tiende a uno! La primera transmisión resonante ocurre para electrones de alrededor de un electronvoltio (tales electrones tienen una velocidad de aproximadamente 600 km/s). La Figura 4 proporciona un esquema tanto de $R$ como de $T$ en función de la energía. Nuestro potencial de pozo cuadrado unidimensional no proporciona una buena correspondencia cuantitativa con los datos, pero ilustra el fenómeno físico. Se necesita un pozo cuadrado esférico tridimensional para un análisis cuantitativo.

*Andrew Turner transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes17_ES/fig4.png)

Figura 4: Los coeficientes de reflexión y transmisión en función de la energía para el efecto Ramsauer–Townsend. Nótese que $R + T = 1$. En la flecha, tenemos $R = 0$, por lo que no hay dispersión. ¡Todos los electrones pasan directamente a través de los átomos del gas noble! Experimentan transmisión resonante. Esto ocurre por primera vez alrededor de 1 eV.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.*
