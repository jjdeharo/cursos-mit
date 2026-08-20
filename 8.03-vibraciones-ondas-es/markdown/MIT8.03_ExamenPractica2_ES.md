# Examen de práctica 2

**Instituto Tecnológico de Massachusetts**

**Física 8.03**

**EXAMEN DE PRÁCTICA 2**

------------------------------------------------------------------------

## Problema 1

Las fluctuaciones de la densidad de carga en un plasma satisfacen la ecuación de ondas que, para distorsiones unidimensionales, se reduce a

$$\frac{\partial^2\rho}{\partial t^2} = c^2\frac{\partial^2\rho}{\partial x^2} - \omega_p^2\rho$$

donde $\rho(x, t)$ es la fluctuación de la densidad de carga, $c$ es la velocidad de la luz y el parámetro fijo $\omega_p$ se conoce como frecuencia de plasma.

**a.** Halle la relación de dispersión $\omega(k)$ para soluciones de onda viajera de la forma $\rho(x, t) = a\sin(kx - \omega t)$.

**b.** Halle $k(\omega)$. Represente gráficamente el vector de ondas $k$ en función de la frecuencia de onda $\omega$. Halle y esboce las velocidades de fase y de grupo.

**c.** Demuestre que la ecuación de ondas también puede satisfacerse mediante una solución exponencialmente decreciente de la forma

$$\rho(x, t) = a\cos(\omega t)e^{-\kappa x}$$

Halle $\kappa(\omega)$ y represéntela gráficamente (puede usar la misma gráfica de la pregunta anterior, pero asegúrese de etiquetarla claramente).

------------------------------------------------------------------------

## Problema 2

Considere una cuerda muy larga unida a un pequeño anillo sin masa en $x = 0$. La cuerda tiene densidad de masa $\mu$ y se mantiene a una tensión $T$. El anillo puede moverse verticalmente sin fricción. Se aplica al anillo una fuerza externa $F(t) = F_0\sin(\omega t)$ que lo mueve arriba y abajo, dando lugar a una onda armónica estacionaria en régimen permanente que viaja hacia $x$ positiva. Suponga que la cuerda es tan larga que no hay que preocuparse por los pulsos reflejados.

**a.** Halle las condiciones de contorno que debe satisfacer una solución de onda $y(x, t)$ en $x = 0$ en términos de los parámetros dados.

**b.** Halle la frecuencia y la longitud de onda de la onda armónica en régimen permanente resultante en función de los parámetros dados.

**c.** Halle la amplitud de la onda armónica en régimen permanente resultante.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenPractica2_ES/fig1.png)

Figura 1: fuerza que crea una onda. La fuerza $F(t) = F_0\sin(\omega t)$ se aplica al anillo situado en el extremo izquierdo de la cuerda, en $x = 0$.

------------------------------------------------------------------------

## Problema 3

Considere una cuerda de longitud $L$ unida a un anillo sin masa en $x = 0$ y a un punto fijo en $x = L$. El anillo puede moverse libremente en dirección perpendicular a la cuerda a lo largo de una varilla sin fricción. La tensión de la cuerda es $T$ y la densidad de masa es $\mu$. La fuerza de la gravedad puede despreciarse frente a las demás fuerzas. En $t = 0$ la cuerda está deformada de modo que presenta un pulso rectangular estrecho de altura $H$, como se muestra en la figura 2. La anchura del pulso $D$ es mucho menor que la longitud de la cuerda $L$, pero es finita. El centro del pulso está en $x_0 = L/4$. La cuerda está inicialmente en reposo, con $\dfrac{\partial y}{\partial t}(x, 0) = 0$.

**a.** Halle la forma funcional, los números de onda $k_m$, las frecuencias $\omega_m$ y los periodos de oscilación $\tau_m$ de todos los modos normales posibles de esta cuerda en función de $L$, $T$, $\mu$ y el entero $m$.

**b.** Halle la expresión de los coeficientes $A_m$ del desarrollo de $y(x, 0)$ en modos normales. Evalúe todas las integrales y simplifique los resultados. Exprese los resultados en función de $L$, $H$, $D$ y $m$. Puede encontrar útiles las expresiones trigonométricas de la hoja de fórmulas.

**c.** Halle cuáles de los coeficientes son iguales a cero, si es que hay alguno.

**d.** Escriba la expresión completa de la descomposición de Fourier dependiente del tiempo del pulso $y(x, t)$ en forma de serie infinita de coeficientes multiplicados por los términos dependientes del tiempo apropiados.

**e.** Halle la forma de la cuerda en $t = \tau_1/2$, donde $\tau_1$ es el periodo de oscilación del modo normal más bajo. No es necesario que utilice el desarrollo de Fourier: cualquier argumento lógico será aceptable.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenPractica2_ES/fig2.png)

Figura 2: cuerda deformada. Sobre una cuerda que va de $x = 0$ a $x = L$ se levanta un pulso rectangular de altura $H$ y anchura $D$, centrado en $x = L/4$.

------------------------------------------------------------------------

## Problema 4

Considere dos cuerdas con densidades de masa $\mu_1 = \mu$ y $\mu_2 = \mu/2$ y tensiones $T_1 = T$ y $T_2 = T/2$, unidas por un anillo sin masa en $x = 0$. El anillo puede moverse a lo largo de una varilla sin fricción. La cuerda 1 se extiende hacia la izquierda, mucho más allá de $x = -L$, y la cuerda 2 está unida a un punto fijo de la pared en $x = L$. Inicialmente, un pulso triangular de anchura $L/4$ se mueve por la cuerda 1 de izquierda a derecha. En $t = 0$ el borde delantero del triángulo está en $x = -7L/8$, como se muestra en la figura 3.

**a.** Escriba las ecuaciones de ondas a ambos lados del anillo y especifique las condiciones de contorno en $x = 0$.

**b.** ¿Espera ondas reflejadas en $x = 0$ y en $x = L$? ¿Tendrá la onda reflejada el mismo signo que la onda incidente o el opuesto, en $x = 0$ y en $x = L$?

**c.** Suponga que el pulso incidente es de la forma $f_1(x, t) = f_1(x/v_1 - t)$. Halle la forma funcional de los pulsos transmitido $g(x, t)$ y reflejado $f_2(x, t)$ en $x = 0$ y $x = L$. Considere únicamente tiempos $t \leq 2L\sqrt{\dfrac{\mu}{T}}$.

**d.** Haga un esbozo de las deformaciones de la cuerda en $t = L\sqrt{\dfrac{\mu}{T}}$ y en $t = 2L\sqrt{\dfrac{\mu}{T}}$.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenPractica2_ES/fig3.png)

Figura 3: triángulo viajero. El pulso triangular de anchura $L/4$ avanza por la cuerda 1, de parámetros $T_1$ y $\mu_1$, hacia el anillo situado en $x = 0$; a la derecha, la cuerda 2, de parámetros $T_2$ y $\mu_2$, llega hasta la pared en $x = L$.

------------------------------------------------------------------------

## Problema 5

Una cuerda de longitud $L$, masa $M$ y tensión $T$ está fija por ambos extremos.

**a.** ¿Cuál es la longitud de onda $\lambda_1$ del modo normal más bajo posible, y cuál es la frecuencia asociada $\omega_1$?

**b.** ¿Cuál es la longitud de onda $\lambda_n$ del $n$-ésimo modo normal, y cuál es la frecuencia asociada $\omega_n$?

Deformamos la cuerda como se muestra en la figura 5 (el triángulo es equilátero). El desplazamiento vertical está muy exagerado en la figura. En el intervalo $0 < x < L$ la forma de la cuerda viene dada por $y = f(x)$. Según Fourier:

$$y(x) = \sum_{n=1}^{\infty} B_n\sin\frac{n\pi x}{L}\qquad\text{(1)}$$

con

$$B_n = \frac{2}{L}\int_0^L f(x)\sin\frac{n\pi x}{L}\,dx\qquad\text{(2)}$$

**c.** ¿Qué valores de $B_n$ serán cero? Razone su respuesta. ¡NO intente realizar ninguna integración!

Soltamos la cuerda pulsada con velocidad cero.

**d.** ¿Cuál es el tiempo mínimo que hay que esperar para que la cuerda tenga el aspecto de la figura 4 ($y(x) = 0$), y cuál es el tiempo mínimo para que la cuerda vuelva a tener el aspecto de la figura 5? Razone su respuesta.

**e.** Haga un esbozo de la cuerda $\dfrac{1}{4}\sqrt{\dfrac{ML}{T}}$ segundos después de soltarla.

**f.** Sea $t = 0$ el instante en que la cuerda tiene por primera vez (tras soltarla) el aspecto de la figura 4 ($y(x) = 0$). Sea $B_5$ el valor de $B$ del quinto modo normal ($n = 5$). ¡No intente calcular $B_5$! ¿Cuál es la evolución temporal de este quinto modo? Es decir, ¿cuánto vale $y_5(x, t)$? El índice 5 indica el quinto modo. Exprese su respuesta en términos de $T$, $M$, $L$ y $B_5$.

Suponga ahora que alguien (¡NO usted!) ha calculado todos los valores de $B_n$. Esa persona le muestra orgullosa, en su portátil, que sumando los 20 modos permitidos más bajos la coincidencia con la forma mostrada en la figura 5 es casi perfecta. Por curiosidad, usted quiere ver la forma de la cuerda para valores de $x$ desde $L$ hasta $3L$. La cuerda no existe ahí, pero la ecuación (1) no lo sabe.

**g.** Esboce $f(x)$ en el intervalo de $0$ a $3L$.

Dejamos ahora que el extremo de la cuerda ($x = L$) se mueva libremente sin fricción. Mantenemos la misma tensión mediante un anillo «sin masa» que desliza sin fricción a lo largo de una barra vertical.

**h.** Responda a la pregunta **a** en esta nueva configuración.

**i.** Responda a la pregunta **b** en esta configuración.

Deformamos ahora la cuerda como se muestra en la figura 5. Su amiga le muestra de nuevo, orgullosa, los resultados de su análisis de Fourier en la nueva configuración. De nuevo siente curiosidad por el intervalo de $L$ a $3L$.

**j.** Esboce $f(x)$ en el intervalo de $0$ a $3L$.

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenPractica2_ES/fig4.png)

Figura 4: cuerda fija por ambos extremos, de tensión $T$, masa $M$ y longitud $L$.

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenPractica2_ES/fig5.png)

Figura 5: triángulo sobre la cuerda. La cuerda se deforma en un triángulo de altura $A$ con el vértice en $x = L/2$.

![Figura 6](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ExamenPractica2_ES/fig6.png)

Figura 6: cuerda con un extremo libre. Igual que la figura 4, pero el extremo en $x = L$ termina en un anillo que desliza por una barra vertical.

------------------------------------------------------------------------

## Problema 6

Considere dos planos perfectamente conductores en $z = 0$ y $z = L$. Entre los planos hay una onda electromagnética estacionaria con el campo $E$ siempre a lo largo del eje $y$. La onda se describe mediante un campo eléctrico $\vec{E}(z, t) = E_y(z, t)\hat{y}$ y un campo magnético $\vec{B}(z, t) = B_x(z, t)\hat{x}$.

**a.** Usando las condiciones de contorno del campo eléctrico en los planos conductores, escriba la expresión de $E_y(z, t)$ en el $n$-ésimo modo normal.

**b.** Usando las ecuaciones de Maxwell, o de otro modo, halle el campo magnético correspondiente $B_x(z, t)$ en el $n$-ésimo modo normal. (Pista: puede considerar una onda estacionaria como la superposición de dos ondas progresivas.)

**c.** Deduzca las expresiones del vector de Poynting $\vec{S}$ y de las densidades $U_E$ del campo eléctrico y $U_B$ del campo magnético, así como los promedios temporales de las tres magnitudes.

**d.** Para el segundo modo ($n = 2$), esboce la variación espacial de $\vec{E}$, $\vec{B}$, $U_E$ y $U_B$ entre los dos planos en $t = 0$.

------------------------------------------------------------------------

# Soluciones

## Solución del problema 1

**a.**

$$\frac{\partial^2\rho}{\partial t^2} = c^2\frac{\partial^2\rho}{\partial x^2} - \omega_p^2\rho\qquad\text{(1)}$$

Sustituyendo $\rho(x, t) = a\sin(kx - \omega t)$, obtenemos

$$-\omega^2 = -c^2k^2 - \omega_p^2\qquad\text{(2)}$$

Por tanto,

$$\omega = \sqrt{c^2k^2 + \omega_p^2}\qquad\text{(3)}$$

**b.**

$$k(\omega) = \frac{1}{c}\sqrt{\omega^2 - \omega_p^2}\qquad\text{(4)}$$

La velocidad de fase:

$$v = \frac{\omega}{k} = \frac{c}{\sqrt{1 - \dfrac{\omega_p^2}{\omega^2}}}\qquad\text{(5)}$$

La velocidad de grupo:

$$v = \left(\frac{dk}{d\omega}\right)^{-1} = c\sqrt{1 - \frac{\omega_p^2}{\omega^2}}\qquad\text{(6)}$$

**c.** Sustituyendo $\rho(x, t) = a\cos(\omega t)e^{-\kappa x}$ en la ecuación de ondas, obtenemos

$$-\omega^2 = c^2\kappa^2 - \omega_p^2\qquad\text{(7)}$$

Por tanto,

$$\kappa = \frac{1}{c}\sqrt{\omega_p^2 - \omega^2}\qquad\text{(8)}$$

## Solución del problema 2

**a.** La fuerza de tensión de la cuerda en la dirección vertical

$$T_y = T\left.\frac{dy}{dx}\right|_{x=0}\qquad\text{(9)}$$

equilibra la fuerza externa $F(t)$. Por tanto, la condición de contorno es

$$F_0\sin(\omega t) + T\left.\frac{dy}{dx}\right|_{x=0} = 0\qquad\text{(10)}$$

**b.** La onda debe satisfacer la ecuación de ondas:

$$\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2 y}{\partial t^2}\qquad\text{(11)}$$

donde $v^2 = \dfrac{T}{\mu}$. La solución compleja general con una sola frecuencia es

$$y = f\cos\left(\omega'\left(t - \frac{x}{v}\right) + \phi_1\right) + g\cos\left(\omega'\left(t + \frac{x}{v}\right) + \phi_2\right)\qquad\text{(12)}$$

Para que la solución en régimen permanente satisfaga la condición de contorno para $t$ arbitrario, esta $\omega'$ debe ser igual a $\omega$. Por tanto, la solución en régimen permanente tiene frecuencia angular $\omega$ y longitud de onda

$$\lambda = \frac{2\pi v}{\omega}\qquad\text{(13)}$$

**c.** No necesitamos conservar el término del pulso reflejado, así que basta con sustituir

$$y = f\cos\left(\omega\left(t - \frac{x}{v}\right) + \phi_1\right)\qquad\text{(14)}$$

en la condición de contorno

$$F_0\sin(\omega t) + T\frac{\partial y}{\partial x} = 0\qquad\text{(15)}$$

con lo que tenemos

$$F_0\sin(\omega t) + \frac{Tf\omega}{v}\sin(\omega t + \phi_1) = 0\qquad\text{(16)}$$

Podemos tomar $\phi_1 = \pi$, $f = \dfrac{F_0 v}{T\omega}$, de modo que la onda armónica resultante en régimen permanente tiene la forma

$$y = \frac{F_0 v}{T\omega}\cos\left(\omega\left(t - \frac{x}{v}\right) + \pi\right)\qquad\text{(17)}$$

con amplitud

$$A = \frac{F_0 v}{T\omega}\qquad\text{(18)}$$

## Solución del problema 3

**a.** La condición de contorno es

$$\left.\frac{\partial y}{\partial x}\right|_{x=0} = 0\qquad\text{(19)}$$

$$y(L, t) = 0\qquad\text{(20)}$$

Los modos normales tienen entonces la forma

$$y(x) = \cos(kx)\qquad\text{(21)}$$

con la condición

$$\cos(kL) = 0\qquad\text{(22)}$$

Por tanto, el modo normal $m$ es

$$y_m = \cos(k_m x)\ ,\qquad k_m = \left(m - \frac{1}{2}\right)\frac{\pi}{L} \quad (m = 1, 2, \ldots)\qquad\text{(23)}$$

La frecuencia de un modo normal está relacionada con $k$ mediante

$$\omega = kv = k\sqrt{\frac{T}{\mu}}\qquad\text{(24)}$$

Por tanto,

$$\omega_m = \left(m - \frac{1}{2}\right)\frac{\pi}{L}\sqrt{\frac{T}{\mu}}\qquad\text{(25)}$$

$$\tau_m = \frac{2\pi}{\omega_m} = \frac{2L}{m - \frac{1}{2}}\sqrt{\frac{\mu}{T}}\qquad\text{(26)}$$

**b.**

$$\begin{aligned}
A_m &= \frac{2}{L}\int_0^L y(x, 0)\cos\left(\left(m - \frac{1}{2}\right)\frac{\pi x}{L}\right)dx \\[4pt]
&= \frac{2}{L}\int_{L/4 - D/2}^{L/4 + D/2} H\cos\left(\left(m - \frac{1}{2}\right)\frac{\pi x}{L}\right)dx \\[4pt]
&= \frac{2H}{\pi\left(m - \frac{1}{2}\right)}\left[\sin\left(\left(m - \frac{1}{2}\right)\pi\left(\frac{1}{4} + \frac{D}{2L}\right)\right) - \sin\left(\left(m - \frac{1}{2}\right)\pi\left(\frac{1}{4} - \frac{D}{2L}\right)\right)\right] \\[4pt]
&= \frac{4H}{\pi\left(m - \frac{1}{2}\right)}\cos\frac{\left(m - \frac{1}{2}\right)\pi}{4}\,\sin\frac{\left(m - \frac{1}{2}\right)\pi D}{2L}
\end{aligned}\qquad\text{(27)}$$

**c.** $A_m = 0$ cuando

$$\cos\frac{\left(m - \frac{1}{2}\right)\pi}{4} = 0\qquad\text{(28)}$$

o bien

$$\sin\frac{\left(m - \frac{1}{2}\right)\pi D}{2L} = 0\qquad\text{(29)}$$

La primera condición no puede darse nunca para $m$ entero. Esto se debe a que ningún modo normal tiene $y_m(L/4) = 0$.

La segunda condición puede darse si existe algún $m$ tal que

$$\frac{\left(m - \frac{1}{2}\right)D}{2L} = p\qquad\text{(30)}$$

sea un número entero.

**d.**

$$\begin{aligned}
y(x, t) = \sum_{m=1}^{\infty} & \frac{4H}{\pi\left(m - \frac{1}{2}\right)}\cos\frac{\left(m - \frac{1}{2}\right)\pi}{4}\,\sin\frac{\left(m - \frac{1}{2}\right)\pi D}{2L}\\
& \cos\left(\left(m - \frac{1}{2}\right)\frac{\pi x}{L}\right)\cos\left(\left(m - \frac{1}{2}\right)\frac{v\pi}{L}t\right)\qquad\text{(31)}
\end{aligned}$$

Los factores temporales de cada componente se eligen como $\cos(\omega_m t)$, de modo que la derivada temporal $\dfrac{\partial y}{\partial t}(x, 0) = 0$.

**e.**

$$\tau_1 = \frac{4L}{v}\ ,\qquad t = \frac{\tau_1}{2} = \frac{2L}{v}\qquad\text{(32)}$$

La configuración inicial de la cuerda estática puede descomponerse en dos pulsos cuadrados que viajan en direcciones opuestas, cada uno con velocidad $v$, anchura $D$ y altura $\dfrac{H}{2}$. Al cabo del tiempo $t$, cada uno de ellos ha viajado de vuelta a la posición original, habiendo chocado una vez con la pared. Puesto que chocar con la pared añade un desfase de $\pi$, es decir, invierte el pulso, mientras que chocar con el anillo sin masa no cambia la forma del pulso, cada uno de los dos pulsos viajeros queda invertido al cabo del tiempo $t$.

Por tanto, la forma de la cuerda en el instante $t = \dfrac{\tau_1}{2}$ es la del pulso original invertido.

## Solución del problema 4

**a.** La ecuación de ondas a la izquierda:

$$\frac{\partial^2 y_L}{\partial x^2} = \frac{\mu}{T}\frac{\partial^2 y_L}{\partial t^2}\qquad\text{(33)}$$

La ecuación de ondas a la derecha:

$$\frac{\partial^2 y_R}{\partial x^2} = \frac{\mu}{T}\frac{\partial^2 y_R}{\partial t^2}\qquad\text{(34)}$$

La condición de contorno en $x = 0$: la componente vertical de la tensión de la cuerda a izquierda y derecha debe equilibrarse, por lo que

$$T\left.\frac{\partial y_L}{\partial x}\right|_{x=0^-} = \frac{T}{2}\left.\frac{\partial y_R}{\partial x}\right|_{x=0^+}\qquad\text{(35)}$$

Tenemos además la condición de continuidad:

$$y_L\big|_{x=0^-} = y_R\big|_{x=0^+}\qquad\text{(36)}$$

**b.** Hay ondas reflejadas en $x = 0$ y en $x = L$. La onda reflejada en $x = 0$ no cambia de signo, ya que la impedancia $\sqrt{T\mu}$ de la izquierda es mayor que la impedancia de la derecha. La onda reflejada en $x = L$ sí cambia de signo, porque en $x = L$ la condición de contorno es de extremo fijo. Por tanto, estas ondas reflejadas tienen signos opuestos.

**c.** Denotamos

$$v = v_1 = \sqrt{\frac{T}{\mu}}\qquad\text{(37)}$$

Por tanto, la onda a la izquierda de $x = 0$:

$$y_L = f_1(x/v - t) + f_2(x, t)\qquad\text{(38)}$$

donde la onda reflejada es

$$f_2(x, t) = r\,f_1(-x/v - t)\qquad\text{(39)}$$

La onda a la derecha de $x = 0$:

$$y_R = g(x, t) + g_2(x, t)\qquad\text{(40)}$$

Aquí $g(x, t)$ es la onda transmitida a través de $x = 0$:

$$g(x, t) = \mathrm{t}\,f_1(x/v - t)\qquad\text{(41)}$$

y $g_2(x, t)$ es la onda reflejada desde $x = L$:

$$g_2(x, t) = r_2\,f_1((2L - x)/v - t)\qquad\text{(42)}$$

Entonces la condición de contorno en $x = 0$ da:

$$\frac{T}{v}f_1'(-t) - \frac{rT}{v}f_1'(-t) = \frac{\mathrm{t}T}{2v}f_1'(-t) - \frac{r_2 T}{2v}f_1'(2L/v - t)\qquad\text{(43)}$$

Puesto que

$$f_1(t \geq 0) \equiv 0\qquad\text{(44)}$$

y solo consideramos tiempos $t \leq 2L/v$, el último término de (43) se anula, con lo que tenemos

$$1 - r = \frac{\mathrm{t}}{2}\qquad\text{(45)}$$

y

$$1 + r = \mathrm{t}\qquad\text{(46)}$$

Por tanto,

$$r = \frac{1}{3}\ ,\qquad \mathrm{t} = \frac{4}{3}\qquad\text{(47)}$$

En el contorno $x = L$ tenemos

$$g(L, t) + g_2(L, t) = 0\qquad\text{(48)}$$

de donde

$$r_2 = -\mathrm{t} = -\frac{4}{3}\qquad\text{(49)}$$

**d.** En el instante $t = \dfrac{L}{v}$, la mitad derecha del pulso ha pasado $x = 0$ y también se ha reflejado hacia la izquierda. La mitad izquierda del pulso sigue propagándose hacia la derecha. Denotando por 1 la altura del borde derecho del pulso inicial, la forma de la cuerda en $t = \dfrac{L}{v}$ presenta escalones de alturas $\frac{1}{3}$, $\frac{2}{3}$ y $\frac{4}{3}$ en torno a $x = 0$.

En el instante $t = \dfrac{2L}{v}$, el pulso reflejado $f_2$ ha viajado de vuelta hasta $x = -L$ y el pulso transmitido $g$ ha alcanzado $x = L$. La mitad derecha de $g$ ya se ha reflejado, mientras que la mitad izquierda sigue propagándose hacia la derecha. La forma de la cuerda en $t = \dfrac{2L}{v}$ muestra el pulso de altura $\frac{1}{3}$ a la izquierda y el pulso invertido de altura $-\frac{4}{3}$ junto a $x = L$.

## Solución del problema 5

**a.** El modo más bajo tiene la forma

$$y_1 = \sin(k_1 x)\ ,\qquad k_1 = \frac{\pi}{L}\qquad\text{(50)}$$

La longitud de onda

$$\lambda_1 = 2L\qquad\text{(51)}$$

y la frecuencia

$$\omega_1 = vk_1 = k_1\sqrt{\frac{TL}{M}} = \frac{\pi}{L}\sqrt{\frac{TL}{M}}\qquad\text{(52)}$$

**b.** El $n$-ésimo modo tiene la forma

$$y_n = \sin(k_n x)\ ,\qquad k_n = \frac{n\pi}{L}\qquad\text{(53)}$$

La longitud de onda

$$\lambda_n = \frac{2L}{n}\qquad\text{(54)}$$

y la frecuencia

$$\omega_n = vk_n = k_n\sqrt{\frac{TL}{M}} = \frac{n\pi}{L}\sqrt{\frac{TL}{M}}\qquad\text{(55)}$$

**c.** Los modos con $y_n(L/2) = 0$ serán cero, porque son antisimétricos respecto de $x = L/2$:

$$y_n(L/2 - x) = -y_n(L/2 + x)\qquad\text{(56)}$$

No debería haber ninguna contribución de estos modos. Por tanto, se anulan los modos $n = 2m$.

**d.** En $t = 0$ la cuerda tiene velocidad nula. La función completa $y(x, t)$:

$$y(x, t) = \sum_{n=1}^{\infty} B_n\sin\frac{n\pi x}{L}\cos\frac{n\pi vt}{L}\qquad\text{(57)}$$

Al cabo del tiempo $T = \dfrac{2L}{v}$, todos los factores dependientes del tiempo $\cos\dfrac{n\pi vt}{L}$ vuelven a valer 1. Este es el tiempo mínimo, ya que $B_1 \neq 0$.

**e.** La configuración inicial puede descomponerse en dos pulsos que viajan en direcciones opuestas con velocidad $v$, altura $A/2$ y la misma anchura que la configuración inicial. Al chocar con el contorno izquierdo o derecho, cambian de signo tras reflejarse. Por tanto, en el instante $t = \dfrac{L}{4v}$ la configuración de la cuerda es una línea recta.

**f.** Este instante es $t = \dfrac{L}{4v}$ en la expresión (57). Desplazando el origen de tiempos a este instante, tenemos la expresión del quinto modo:

$$y_5(x, t) = B_5\sin\frac{5\pi x}{L}\cos\frac{5\pi v(t + L/4v)}{L} = B_5\sin\frac{5\pi x}{L}\cos\left(5\pi t\sqrt{\frac{T}{ML}} + \frac{5\pi}{4}\right)\qquad\text{(58)}$$

**g.** Puesto que todos los modos no nulos corresponden a $n$ impar, la función $f(x)$ en el intervalo de $L$ a $2L$ debe ser la opuesta de la función $f(x)$ en el intervalo de $0$ a $L$:

$$f(x + L) = \sum_{m=1}^{20} B_m\sin\frac{(2m-1)\pi(x + L)}{L} = -\sum_{m=1}^{20} B_m\sin\frac{(2m-1)\pi x}{L} = -f(x)\qquad\text{(59)}$$

mientras que la función $f(x)$ en el intervalo de $2L$ a $3L$ debe ser igual a la función $f(x)$ en el intervalo de $0$ a $L$:

$$f(x + 2L) = \sum_{m=1}^{20} B_m\sin\frac{(2m-1)\pi(x + 2L)}{L} = \sum_{m=1}^{20} B_m\sin\frac{(2m-1)\pi x}{L} = f(x)\qquad\text{(60)}$$

*\[Nota de la traducción: el PDF original cierra la ecuación (60) con $= -f(x)$, en contradicción con el propio desarrollo que la precede y con el texto que la introduce («debe ser igual a»). Como $\sin\frac{(2m-1)\pi(x+2L)}{L} = \sin\left(\frac{(2m-1)\pi x}{L} + 2(2m-1)\pi\right) = \sin\frac{(2m-1)\pi x}{L}$, el resultado correcto es $f(x + 2L) = f(x)$.\]*

**h.** En esta nueva configuración, el modo más bajo tiene la forma

$$y_1 = \sin(k_1 x)\ ,\qquad k_1 = \frac{\pi}{2L}\qquad\text{(61)}$$

La longitud de onda

$$\lambda_1 = 4L\qquad\text{(62)}$$

y la frecuencia

$$\omega_1 = vk_1 = k_1\sqrt{\frac{TL}{M}} = \frac{\pi}{2L}\sqrt{\frac{TL}{M}}\qquad\text{(63)}$$

**i.** El $n$-ésimo modo tiene la forma

$$y_n = \sin(k_n x)\ ,\qquad k_n = \frac{(2n-1)\pi}{2L}\qquad\text{(64)}$$

La longitud de onda

$$\lambda_n = \frac{4L}{2n-1}\qquad\text{(65)}$$

y la frecuencia

$$\omega_n = vk_n = k_n\sqrt{\frac{TL}{M}} = \frac{(2n-1)\pi}{2L}\sqrt{\frac{TL}{M}}\qquad\text{(66)}$$

**j.** En este caso, la función $f(x)$ en el intervalo de $L$ a $2L$ debe ser igual a la función $f(x)$ en el intervalo de $0$ a $L$:

$$f(2L - x) = \sum_{m=1}^{20} B_m\sin\frac{(2m-1)\pi(2L - x)}{2L} = \sum_{m=1}^{20} B_m\sin\frac{(2m-1)\pi x}{2L} = f(x)\qquad\text{(67)}$$

mientras que la función $f(x)$ en el intervalo de $2L$ a $3L$ debe ser la opuesta de la función $f(x)$ en el intervalo de $0$ a $L$:

$$f(x + 2L) = \sum_{m=1}^{20} B_m\sin\frac{(2m-1)\pi(x + 2L)}{2L} = -\sum_{m=1}^{20} B_m\sin\frac{(2m-1)\pi x}{2L} = -f(x)\qquad\text{(68)}$$

## Solución del problema 6

**a.** Las condiciones de contorno del campo eléctrico son

$$\vec{E}(0, t) = \vec{E}(L, t) = 0\qquad\text{(69)}$$

Por tanto, el $n$-ésimo modo normal es

$$E_y^{(n)}(z) = \sin\frac{n\pi z}{L}\qquad\text{(70)}$$

$$E_y^{(n)}(z, t) = \sin\frac{n\pi z}{L}\cos\frac{n\pi ct}{L}\qquad\text{(71)}$$

**b.** La onda estacionaria puede descomponerse en

$$E_y^{(n)}(z, t) = \sin\frac{n\pi z}{L}\cos\frac{n\pi ct}{L} = \operatorname{Re}\left[\frac{1}{2}e^{i\frac{n\pi}{L}(z - ct) - \frac{i\pi}{2}} + \frac{1}{2}e^{i\frac{n\pi}{L}(z + ct) - \frac{i\pi}{2}}\right]\qquad\text{(72)}$$

Para una componente de onda viajera con vector de ondas unitario $\hat{k}$,

$$\vec{B} = \frac{1}{c}\hat{k} \times \vec{E}\qquad\text{(73)}$$

Por tanto,

$$\vec{B} = \operatorname{Re}\left[\hat{z} \times \hat{y}\,\frac{1}{2}e^{i\frac{n\pi}{L}(z - ct) - \frac{i\pi}{2}} - \hat{z} \times \hat{y}\,\frac{1}{2}e^{i\frac{n\pi}{L}(z + ct) - \frac{i\pi}{2}}\right] = \frac{\hat{x}}{c}\cos\frac{n\pi z}{L}\sin\frac{n\pi ct}{L}\qquad\text{(74)}$$

**c.**

$$\vec{S} = \frac{1}{\mu_0}\vec{E} \times \vec{B} = -\frac{\hat{z}}{\mu_0 c}\sin\frac{n\pi z}{L}\cos\frac{n\pi z}{L}\cos\frac{n\pi ct}{L}\sin\frac{n\pi ct}{L}\qquad\text{(75)}$$

$$\langle\vec{S}\rangle = 0\qquad\text{(76)}$$

$$U_E = \frac{1}{2}\varepsilon_0\vec{E}^2 = \frac{1}{2}\varepsilon_0\sin^2\frac{n\pi z}{L}\cos^2\frac{n\pi ct}{L}\qquad\text{(77)}$$

$$\langle U_E\rangle = \frac{1}{4}\varepsilon_0\sin^2\frac{n\pi z}{L}\qquad\text{(78)}$$

$$U_B = \frac{1}{2\mu_0}\vec{B}^2 = \frac{1}{2\mu_0 c^2}\cos^2\frac{n\pi z}{L}\sin^2\frac{n\pi ct}{L} = \frac{1}{2}\varepsilon_0\cos^2\frac{n\pi z}{L}\sin^2\frac{n\pi ct}{L}\qquad\text{(79)}$$

$$\langle U_B\rangle = \frac{1}{4}\varepsilon_0\cos^2\frac{n\pi z}{L}\qquad\text{(80)}$$

*\[Nota de la traducción: el PDF original etiqueta la ecuación (80) como $\langle U_E\rangle$; por el contexto y por la expresión (79) que la precede, se trata de $\langle U_B\rangle$.\]*

Obsérvese que

$$\langle U_E + U_B\rangle = \frac{1}{4}\varepsilon_0\qquad\text{(81)}$$

que está distribuida uniformemente. La amplitud del modo normal se ha fijado en 1 (sin unidades).

**d.** En el instante $t = 0$ elegido, $\vec{B}$ y $U_B$ se anulan idénticamente: $E_y$ presenta la variación espacial $\sin\frac{2\pi z}{L}$, con un nodo en $z = L/2$, y $U_E$ es proporcional a $\sin^2\frac{2\pi z}{L}$, con máximos en $z = L/4$ y $z = 3L/4$. En otro instante en el que $\vec{B}$ y $U_B$ no se anulen, $B_x$ varía como $\cos\frac{2\pi z}{L}$ y $U_B$ como $\cos^2\frac{2\pi z}{L}$, con máximos en $z = 0$, $z = L/2$ y $z = L$.

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*
