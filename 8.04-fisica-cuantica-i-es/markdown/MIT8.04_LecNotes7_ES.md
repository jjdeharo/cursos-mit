# Lección 7

## Vídeos de esta clase (YouTube)

**Lección 7: Wavepackets and uncertainty. Time evolution and shape change time evolutions.**

- [Wavepackets and Fourier representation](https://www.youtube.com/watch?v=dzI5PddY6eE)
- [Reality condition in Fourier transforms](https://www.youtube.com/watch?v=DvFb-D1zJTA)
- [Widths and uncertainties](https://www.youtube.com/watch?v=vWGP5dogNm8)
- [Shape changes in a wave](https://www.youtube.com/watch?v=50Tla309i7o)
- [Time evolution of a free particle wavepacket](https://www.youtube.com/watch?v=ipXNYnO7yRk)

------------------------------------------------------------------------

B. Zwiebach

28 de febrero de 2016

## Contenidos

1.  Paquetes de onda e incertidumbre
2.  Cambios de forma del paquete de onda
3.  Evolución temporal de un paquete de onda libre

## 1. Paquetes de onda e incertidumbre

Un paquete de onda es una superposición de ondas planas $e^{ikx}$ con diversas longitudes de onda. Trabajemos con paquetes de onda en $t = 0$. Un paquete de onda de este tipo tiene la forma

$$\Psi(x, 0) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi(k) e^{ikx}\, dk. \qquad \text{(1.1)}$$

Si conocemos $\Psi(x, 0)$ entonces $\Phi(k)$ se puede calcular. De hecho, por el teorema de inversión de Fourier, la función $\Phi(k)$ es la transformada de Fourier de $\Psi(x, 0)$, por lo que podemos escribir

$$\Phi(k) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Psi(x, 0) e^{-ikx}\, dx. \qquad \text{(1.2)}$$

Nótese la simetría entre las dos ecuaciones anteriores. Nuestro objetivo aquí es entender cómo se relacionan las incertidumbres en $\Psi(x, 0)$ y en $\Phi(k)$. En la interpretación cuántica de las ecuaciones anteriores recordamos que una onda plana con momento $\hbar k$ tiene la forma $e^{ikx}$. Así, la representación de Fourier de la onda $\Psi(x, 0)$ nos da la manera de representar la onda como una superposición de ondas planas de diferentes momentos.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes7_ES/fig1.png)

Figura 1: Una $\Phi(k)$ centrada en $k = k_0$ y con anchura $\Delta k$.

Consideremos una $\Phi(k)$ definida positiva, real, simétrica respecto a un máximo en $k = k_0$, y con una anchura o incertidumbre $\Delta k$, como se muestra en la Fig. 1. La función de onda resultante $\Psi(x, 0)$ está centrada en $x = 0$. Esto se sigue directamente del argumento de fase estacionaria aplicado a (1.1). La función de onda tendrá cierta anchura $\Delta x$, como se muestra en la Fig. 2. Nótese que allí graficamos el valor absoluto $|\Psi(x, 0)|$ del paquete de onda. Dado que $\Psi(x, 0)$ es compleja, la otra opción habría sido graficar las partes real e imaginaria de $\Psi(x, 0)$.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes7_ES/fig2.png)

Figura 2: La $\Psi(x, 0)$ correspondiente a la $\Phi(k)$ mostrada en la Fig. 1, centrada en $x = 0$ con anchura $\Delta x$.

En efecto, en nuestro caso $\Psi(x, 0)$ ¡no es real! Podemos demostrar que

$$\Psi(x, 0) \text{ es real si y solo si } \Phi^*(-k) = \Phi(k). \qquad \text{(1.3)}$$

Comencemos tomando el complejo conjugado de la expresión (1.1) para $\Psi(x, 0)$:

$$\Psi^*(x, 0) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi^*(k) e^{-ikx}\, dk = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi^*(-k) e^{ikx}\, dk. \qquad \text{(1.4)}$$

En el segundo paso hicimos $k \to -k$ en la integral, lo cual está permitido porque integramos sobre todo $k$, y los dos cambios de signo, uno proveniente de la medida $dk$ y otro de intercambiar los límites de integración, se cancelan mutuamente. Si $\Phi^*(-k) = \Phi(k)$ entonces

$$\Psi^*(x, 0) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi(k) e^{ikx}\, dk = \Psi(x, 0), \qquad \text{(1.5)}$$

tal como queríamos comprobar. Si, por otro lado, sabemos que $\Psi(x, 0)$ es real, entonces la igualdad de $\Psi^*$ y $\Psi$ da

$$\frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi^*(-k) e^{ikx}\, dk = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi(k) e^{ikx}\, dk. \qquad \text{(1.6)}$$

Esto es equivalente a

$$\frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \underbrace{\left[\Phi^*(-k) - \Phi(k)\right]}_{} e^{ikx}\, dk = 0. \qquad \text{(1.7)}$$

Esta ecuación en realidad significa que el objeto bajo la llave debe anularse. En efecto, la integral está calculando la transformada de Fourier del objeto entre corchetes, y nos dice que es cero. Pero una función con transformada de Fourier nula debe ser ella misma nula (por el teorema de Fourier). Por lo tanto, la realidad implica $\Phi^*(-k) = \Phi(k)$, tal como queríamos mostrar.

La condición $\Phi^*(-k) = \Phi(k)$ implica que siempre que $\Phi$ sea distinta de cero para algún $k$, también debe ser distinta de cero para $-k$. Esto no es cierto para nuestra $\Phi(k)$ elegida: hay una protuberancia alrededor de $k_0$ pero no hay una protuberancia correspondiente alrededor de $-k_0$. Por lo tanto $\Psi(x, 0)$ no es real y $\Psi(x, 0)$ tendrá tanto una parte real como una imaginaria, ambas centradas en $x = 0$, como se muestra en la Fig. 3.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes7_ES/fig3.png)

Figura 3: Las partes real e imaginaria de $\Psi(x, 0)$.

Abordemos ahora la cuestión de la anchura. Consideremos la integral para $\Psi(x, 0)$

$$\Psi(x, 0) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi(k) e^{ikx}\, dk, \qquad \text{(1.8)}$$

y cambiemos la variable de integración haciendo $k = k_0 + \tilde{k}$, donde la nueva variable de integración $\tilde{k}$ parametriza la distancia al pico en la distribución de momentos. Entonces tenemos

$$\Psi(x, 0) = \frac{1}{\sqrt{2\pi}} e^{ik_0 x} \int_{-\infty}^{\infty} \Phi(k_0 + \tilde{k}) e^{i\tilde{k}x}\, d\tilde{k}. \qquad \text{(1.9)}$$

A medida que integramos sobre $\tilde{k}$, la región más relevante es

$$\tilde{k} \in \left(-\frac{\Delta k}{2}, \frac{\Delta k}{2}\right), \qquad \text{(1.10)}$$

porque es allí donde $\Phi(k)$ es grande. Al recorrer esta región, la fase $\tilde{k}x$ en la exponencial varía en el intervalo

$$\tilde{k}x \in \left(-\frac{\Delta k}{2}x, \frac{\Delta k}{2}x\right) \quad \text{(para } x > 0\text{)}, \qquad \text{(1.11)}$$

y la excursión total de fase es $\Delta k\, x$. Obtendremos una contribución sustancial a la integral para una excursión de fase total pequeña; si la excursión es grande, la integral se anulará por cancelación. Así, obtenemos una contribución significativa para $\Delta k |x| \lesssim 1$, y contribuciones que se cancelan para $\Delta k |x| \gg 1$.

De esto concluimos que $\Psi(x, 0)$ será distinta de cero para $x \in (-x_0, x_0)$ donde $x_0$ es una constante para la cual $\Delta k\, x_0 \approx 1$. Identificamos la anchura de $\Psi(x, 0)$ con $\Delta x := 2x_0$ y por lo tanto tenemos $\Delta k \cdot \tfrac{1}{2}\Delta x \approx 1$. Dado que los factores de dos son claramente poco fiables en este argumento, simplemente registramos

$$\Delta x\, \Delta k \approx 1. \qquad \text{(1.12)}$$

Esto es lo que queríamos mostrar. El producto de la incertidumbre en la distribución de momentos y la incertidumbre en la posición es una constante de orden uno. Este producto de incertidumbres no es de naturaleza cuántica; como hemos visto, se sigue de las propiedades de las transformadas de Fourier.

La contribución cuántica aparece cuando identificamos $\hbar k$ como el momento $p$. Esta identificación nos permite relacionar las incertidumbres del momento y de $k$:

$$\Delta p = \hbar \Delta k. \qquad \text{(1.13)}$$

Como resultado, podemos multiplicar la ecuación (1.12) por $\hbar$ para obtener:

$$\Delta x\, \Delta p \approx \hbar. \qquad \text{(1.14)}$$

Esta es la versión aproximada del producto de incertidumbre de Heisenberg. La versión precisa requiere definir $\Delta x$ y $\Delta p$ con precisión. Se puede demostrar entonces que

$$\text{Producto de incertidumbre de Heisenberg:} \quad \Delta x\, \Delta p \geq \frac{\hbar}{2}. \qquad \text{(1.15)}$$

El producto de las incertidumbres tiene una cota inferior.

**Ejemplo.** Consideremos el caso en que $\Phi(k)$ es un escalón finito de anchura $\Delta k$ y altura $1/\sqrt{\Delta k}$, como se muestra en la Fig. 4. Hallar $\Psi(x, t)$ y estimar el valor de $\Delta x$.

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes7_ES/fig4.png)

Figura 4: Una distribución de momentos.

Nótese que la $\Psi(x, 0)$ que buscamos calcular debe ser real porque $\Phi^*(-k) = \Phi(k)$. A partir de la representación integral,

$$\begin{aligned}
\Psi(x, 0) &= \frac{1}{\sqrt{2\pi}} \int_{-\Delta k/2}^{\Delta k/2} \frac{1}{\sqrt{\Delta k}} e^{ikx}\, dk \\
&= \frac{1}{\sqrt{2\pi \Delta k}} \left. \frac{e^{ikx}}{ix} \right|_{-\Delta k/2}^{\Delta k/2} \\
&= \frac{1}{\sqrt{2\pi \Delta k}} \frac{e^{i\Delta k x/2} - e^{-i\Delta k x/2}}{ix} \\
&= \frac{1}{\sqrt{2\pi \Delta k}} \frac{2}{x} \sin\left(\frac{\Delta k x}{2}\right) = \sqrt{\frac{\Delta k}{2\pi}} \frac{\sin(\Delta k x/2)}{\Delta k x/2}.
\end{aligned}
\qquad \text{(1.16)}$$

Mostramos $\Psi(x, 0)$ en la Fig. 5. Estimamos

$$\Delta x \approx \frac{2\pi}{\Delta k} \quad \Rightarrow \quad \Delta x\, \Delta k \approx 2\pi. \qquad \text{(1.17)}$$

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes7_ES/fig5.png)

Figura 5: La $\Psi(x, 0)$ correspondiente a la $\Phi(k)$.

## 2. Cambios de forma del paquete de onda

Para apreciar las características generales del movimiento de un paquete de onda estudiamos la solución general de la ecuación de Schrödinger

$$\Psi(x, t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi(k) e^{i(kx - \omega(k)t)}\, dk, \qquad \text{(2.18)}$$

y, bajo el supuesto de que $\Phi(k)$ presenta un pico en torno a cierto valor $k = k_0$, expandimos la frecuencia $\omega(k)$ en una serie de Taylor alrededor de $k = k_0$. Manteniendo los términos hasta e incluyendo $(k - k_0)^2$ tenemos

$$\omega(k) = \omega(k_0) + (k - k_0) \left.\frac{d\omega}{dk}\right|_{k_0} + \frac{1}{2}(k - k_0)^2 \left.\frac{d^2\omega}{dk^2}\right|_{k_0}. \qquad \text{(2.19)}$$

El segundo término desempeñó un papel en la determinación de la velocidad de grupo, y el término siguiente, con las segundas derivadas de $\omega$, es responsable de la distorsión de forma que ocurre con el paso del tiempo. Las derivadas se calculan fácilmente,

$$\frac{d\omega}{dk} = \frac{dE}{dp} = \frac{p}{m} = \frac{\hbar k}{m}, \qquad \frac{d^2\omega}{dk^2} = \frac{\hbar}{m}. \qquad \text{(2.20)}$$

Dado que todas las derivadas de orden superior se anulan, la expansión en (2.19) es en realidad exacta tal como está escrita. ¿Qué tipo de contribución de fase estamos despreciando al ignorar el último término en (2.19)? Tenemos

$$e^{-i\omega(k)t} = e^{\cdots - \frac{i}{2}(k - k_0)^2 \frac{\hbar}{m}t}. \qquad \text{(2.21)}$$

Supongamos que partimos del paquete en $t = 0$ y evolucionamos en el tiempo hasta $t > 0$. Esta fase será despreciable siempre que su magnitud sea significativamente menor que uno:

$$(k - k_0)^2 \frac{\hbar}{m} t \ll 1. \qquad \text{(2.22)}$$

Podemos estimar $(k - k_0)^2 \approx (\Delta k)^2$ ya que los valores relevantes de $k$ deben estar dentro de la anchura de la distribución de momentos. Además, dado que $\Delta p = \hbar \Delta k$ obtenemos

$$\frac{(\Delta p)^2 t}{m \hbar} \ll 1. \qquad \text{(2.23)}$$

Así, la condición para un cambio de forma mínimo es

$$t \ll \frac{m \hbar}{(\Delta p)^2}. \qquad \text{(2.24)}$$

Podemos expresar la desigualdad en términos de la incertidumbre en la posición usando $\Delta x\, \Delta p \approx \hbar$. Obtenemos entonces

$$t \ll \frac{m}{\hbar} (\Delta x)^2. \qquad \text{(2.25)}$$

También, a partir de (2.24) podemos escribir

$$\frac{\Delta p}{m} t \ll \frac{\hbar}{\Delta p}, \qquad \text{(2.26)}$$

lo cual da

$$\frac{\Delta p}{m} t \ll \Delta x. \qquad \text{(2.27)}$$

Esta desigualdad tiene una interpretación clara. Primero notemos que $\Delta p/m$ representa la incertidumbre en la velocidad del paquete. Habrá cambio de forma cuando esta incertidumbre de velocidad, a lo largo del tiempo, produzca incertidumbres de posición comparables a la anchura $\Delta x$ del paquete de onda.

En todas las desigualdades anteriores usamos $\ll$ y esto nos da la condición para un cambio de forma despreciable. Si reemplazamos $\ll$ por $\approx$ estamos dando una estimación de algún cambio de forma medible.

**Ejercicio.** Supongamos que hemos localizado un electrón dentro de $\Delta x = 10^{-10}$ m. Estimar el tiempo máximo $t$ durante el cual puede permanecer localizado a ese nivel.

Usando (2.25) tenemos

$$t \approx \frac{m(\Delta x)^2}{\hbar} = \frac{mc^2 (\Delta x)^2}{\hbar c \cdot c} = \frac{0.5\ \text{MeV} \cdot 10^{-20}\ \text{m}^2}{200\ \text{MeV}\,\text{fm} \cdot 3 \times 10^8\ \text{m/s}} \approx 10^{-16}\ \text{s}. \qquad \text{(2.28)}$$

Si originalmente tuviéramos $\Delta x = 10^{-2}$ m, ¡habríamos obtenido $t \approx 1$ s!

## 3. Evolución temporal de un paquete de onda libre

Supongamos que conocemos la función de onda $\Psi(x, 0)$ en el instante cero. Nuestro objetivo es hallar $\Psi(x, t)$. Esto se logra en unos pocos pasos sencillos.

1.  Usar $\Psi(x, 0)$ para calcular $\Phi(k)$:

$$\Phi(k) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} dx\, \Psi(x, 0) e^{-ikx}. \qquad \text{(3.1)}$$

1.  Usar $\Phi(k)$ para reescribir $\Psi(x, 0)$ como una superposición de ondas planas:

$$\Psi(x, 0) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi(k) e^{ikx}\, dk. \qquad \text{(3.2)}$$

Esto es útil porque sabemos cómo evolucionan las ondas planas en el tiempo. Lo anterior se denomina la representación de Fourier de $\Psi(x, 0)$.

1.  Una onda plana $\psi_k(x, 0) = e^{ikx}$ evoluciona en el tiempo hacia $\psi_k(x, t) = e^{i(kx - \omega(k)t)}$ con $\hbar\omega = \dfrac{\hbar^2 k^2}{2m}$. Usando la superposición tenemos que (3.2) evoluciona hacia

$$\Psi(x, t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi(k) e^{i(kx - \omega(k)t)}\, dk. \qquad \text{(3.3)}$$

Esta es, de hecho, la respuesta para $\Psi(x, t)$. Se puede confirmar fácilmente que esto es así porque: (i) resuelve la ecuación de Schrödinger (¡compruébelo!) y (ii) al fijar $t = 0$ en $\Psi(x, t)$ obtenemos la función de onda inicial (3.2) que representaba la condición inicial.

1.  Si es posible, realizar la integral sobre $k$ para hallar una expresión en forma cerrada para $\Psi(x, t)$. Si resulta demasiado difícil, la integral siempre puede realizarse numéricamente.

**Ejemplo: Evolución de un paquete de onda gaussiano libre.** Tomemos

$$\psi_a(x, 0) = \frac{1}{(2\pi)^{1/4} \sqrt{a}}\, e^{-x^2/4a^2}. \qquad \text{(3.4)}$$

Este es un paquete de onda gaussiano en $t = 0$. La constante $a$ tiene unidades de longitud y $\Delta x \approx a$. El estado $\psi_a$ está correctamente normalizado, como se puede comprobar que $\int dx\, |\psi_a(x, 0)|^2 = 1$.

No realizaremos aquí los cálculos, pero podemos imaginar que este paquete cambiará de forma a medida que evolucione el tiempo. ¿Cuál es la escala temporal $\tau$ para los cambios de forma? La ecuación (2.25) nos da una pista. El lado derecho representa una escala temporal para el cambio de forma. Así que debemos tener

$$\tau \approx \frac{m}{\hbar} a^2. \qquad \text{(3.5)}$$

Esto es, de hecho, correcto. Descubrirá, al hacer evolucionar la gaussiana, que el intervalo de tiempo relevante es en realidad el doble del tiempo anterior:

$$\tau \equiv \frac{2ma^2}{\hbar}. \qquad \text{(3.6)}$$

Si consideramos la norma al cuadrado de la función de onda

$$|\Psi_a(x, 0)|^2 = \frac{1}{\sqrt{2\pi}} \frac{1}{a} e^{-x^2/2a^2}, \qquad \text{(3.7)}$$

encontrará que, tras la evolución temporal, se tiene

$$|\Psi_a(x, t)|^2 = \frac{1}{\sqrt{2\pi}} \frac{1}{a(t)} e^{-x^2/2a(t)^2}, \qquad \text{(3.8)}$$

donde $a(t)$ es una anchura dependiente del tiempo. El objetivo de su cálculo será determinar $a(t)$ y ver cómo interviene $\tau$ en $a(t)$.

*Andrew Turner transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare

https://ocw.mit.edu

8.04 Física Cuántica I

Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

# Apéndice: Lista de problemas 3 (Problem Set 3, 2016)

**Física Cuántica I (8.04) — Primavera de 2016**

**Departamento de Física del MIT — Tarea 3**

*Fecha de entrega: jueves 25 de febrero de 2016, 5:00 pm*

*18 de febrero de 2016*

**Anuncios**

- Lectura recomendada: Griffiths, secciones 1.1, 1.2, 1.4 y 1.5.

## Problema 1: Ejercicios con conmutadores \[10 puntos\]

Sean $A$, $B$ y $C$ operadores lineales.

1.  Demuestre que $[A, BC] = [A, B]C + B[A, C]$.

2.  Demuestre que $[AB, C] = A[B, C] + [A, C]B$.

3.  Demuestre que $[A, [B, C]] + [B, [C, A]] + [C, [A, B]] = 0$.

4.  Calcule $[\hat{x}^n, \hat{p}]$ y $[\hat{x}, \hat{p}^n]$ para $n$ un número entero arbitrario mayor que cero.

5.  Calcule $[\hat{x}\hat{p}, \hat{x}^2]$ y $[\hat{x}\hat{p}, \hat{p}^2]$.

## Problema 2: Pruebas sencillas de la aproximación de fase estacionaria \[10 puntos\]

Consideremos aquí integrales de la forma

$$\Psi(x) = \int_{-\infty}^{\infty} dk\, \Phi(k) e^{ikx},$$

donde $\Phi(k)$ es una función marcadamente localizada alrededor de $k = k_0$. En cada uno de los siguientes casos, use el argumento de fase estacionaria para predecir la ubicación del pico de $|\Psi(x)|$. A continuación calcule la integral de manera exacta para hallar $\Psi(x)$, $|\Psi(x)|$, y confirmar su predicción.

1.  $\Phi(k) = e^{-L^2(k-k_0)^2}$, donde $L$ es una constante con unidades de longitud.

2.  $\Phi(k) = e^{-L^2(k-k_0)^2} e^{-ikx_0}$, donde $x_0$ y $L$ son constantes con unidades de longitud.

Integral útil: válida para constantes complejas $a$ y $b$, con la parte real de $a$ positiva:

$$\int_{-\infty}^{\infty} e^{-ax^2 + bx}\, dx = \sqrt{\frac{\pi}{a}} \exp\left(\frac{b^2}{4a}\right), \quad \text{cuando } \operatorname{Re}(a) > 0.$$

## Problema 3: Invariancia galileana de la ecuación de Schrödinger libre \[15 puntos\]

Demuestre que la ecuación de Schrödinger unidimensional de partícula libre para la función de onda $\Psi(x, t)$:

$$i\hbar \frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m} \frac{\partial^2 \Psi}{\partial x^2},$$

es invariante bajo transformaciones de Galileo

$$x' = x - vt, \qquad t' = t.$$

Con esto queremos decir que existe una $\Psi'(x', t')$ de la forma

$$\Psi'(x', t') = f(x, t)\, \Psi(x, t),$$

donde la función $f(x, t)$ involucra a $x$, $t$, $\hbar$, $m$ y $v$, y tal que $\Psi'$ satisface la ecuación de Schrödinger correspondiente en las variables primadas.

$$i\hbar \frac{\partial \Psi'}{\partial t'} = -\frac{\hbar^2}{2m} \frac{\partial^2 \Psi'}{\partial x'^2}.$$

1.  Halle la función $f(x, t)$. \[Pista: note que la función $f(x, t)$ no puede depender de ningún observable de $\Psi$; es una función universal que se usa para transformar cualquier $\Psi$. Así, si $\Psi$ es una (única) onda plana, $f$ no puede depender de su momento ni de su energía.\]

2.  Demuestre que la solución de onda plana

$$\Psi(x, t) = A\, e^{i(kx - \omega t)}$$

se transforma como se espera. Es decir, dé $\Psi'$ y muestre que representa, en el sistema de referencia primado, una partícula con el momento y la energía esperados.

## Problema 4: Repetir la conservación de la corriente en 3D \[10 puntos\]

En clase dedujimos la expresión para la corriente de probabilidad unidimensional $J(x, t)$ partiendo de $\rho(x, t) = |\Psi(x, t)|^2$ y usando la ecuación de Schrödinger unidimensional para escribir

$$\frac{\partial \rho}{\partial t} + \frac{\partial J}{\partial x} = 0.$$

Repita los mismos pasos partiendo de

$$\rho(x, t) = |\Psi(x, t)|^2,$$

y usando la ecuación de Schrödinger tridimensional para deducir la forma de la corriente de probabilidad $J(x, t)$ que debe aparecer en la ecuación de conservación

$$\frac{\partial \rho}{\partial t} + \nabla \cdot J = 0.$$

## Problema 5: Evolución temporal del solapamiento entre dos estados \[10 puntos\] (Merzbacher)

Consideremos una función de onda que en el instante $t = 0$ es la superposición de dos paquetes de onda estrechos y muy separados, $\Psi_1$ y $\Psi_2$:

$$\Psi(x, 0) = \Psi_1(x, 0) + \Psi_2(x, 0).$$

Cada paquete es normalizable por separado. Definimos la integral de solapamiento $\gamma(t)$ como

$$\gamma(t) \equiv \int_{-\infty}^{\infty} \Psi_1^*(x, t) \Psi_2(x, t)\, dx.$$

En el instante $t = 0$ el valor de $|\gamma(0)|$ es muy pequeño. A medida que los paquetes evolucionan y se ensanchan, ¿qué le sucederá al valor de $|\gamma(t)|$? ¿Aumentará a medida que los paquetes se superponen?

## Problema 6: Corriente de probabilidad en una dimensión \[10 puntos\]

Calcule la corriente de probabilidad $J(x)$ para las siguientes funciones de onda, todas ellas referidas a $t = 0$:

1.  $\Psi(x) = A\, e^{\gamma x}$. Aquí $A$ es una constante compleja y $\gamma$ es una constante real.

2.  $\Psi(x) = N(x) e^{iS(x)/\hbar}$. Aquí $N(x)$ y $S(x)$ son reales.

3.  $\Psi(x) = A e^{ikx} + B e^{-ikx}$. Aquí $A$, $B$ son constantes complejas y $k$ es real.

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*
