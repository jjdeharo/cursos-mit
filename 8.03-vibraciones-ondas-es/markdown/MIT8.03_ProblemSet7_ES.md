*Massachusetts Institute of Technology*

**Física 8.03SC — Otoño de 2016**

**Tarea 7**

## Problemas

**Problema 7.1 (40 pts)**

En sus *Lectures on Physics*, Richard Feynman escribe: «las ondas de agua, que todo el mundo ve fácilmente y que se suelen usar como ejemplo de ondas en cursos elementales, son el peor ejemplo posible; tienen todas las complicaciones que las ondas pueden tener». Este problema explora la complicación principal: las propiedades dispersivas de las ondas de agua.

Considere ondas en la superficie del agua (también llamadas ondas de gravedad superficiales). Suponga que las deformaciones de la superficie están influidas por la gravedad $g$ (en la Tierra) y por la tensión superficial $T$ del agua (expresada en newtons por metro). Si la densidad del agua es $\rho$ y la profundidad no perturbada es $h$, puede demostrarse que la velocidad de fase de las ondas superficiales viene dada por

$$v_p^2(k) = \left(\frac{g}{k} + \frac{Tk}{\rho}\right)\tanh(kh)$$

donde $k = 2\pi/\lambda$ es el número de onda, $\tanh(kh)$ es la tangente hiperbólica, y se desprecia la viscosidad. Para el agua, $\rho = 1\ \text{g}\,\text{cm}^{-3}$.

1.  En términos de las cantidades dadas, ¿a qué longitud de onda aproximada $\lambda_{\text{crítica}}$ el efecto de la tensión superficial se vuelve comparable al de la gravedad? Para agua a 20 °C, la longitud de onda crítica es $\lambda_{\text{crítica}} = 2\ \text{cm}$. ¿Cuál es la tensión superficial $T$ del agua?
2.  Suponga que $\lambda \gg \lambda_{\text{crítica}}$, de modo que la tensión superficial es despreciable. ¿Cuáles son la velocidad de fase y la velocidad de grupo para ondas de agua en aguas poco profundas ($\lambda \gg h$)? ¿Son dispersivas las ondas en esta condición?
3.  Suponga que $\lambda \gg \lambda_{\text{crítica}}$, de modo que la tensión superficial es despreciable. ¿Cuáles son la velocidad de fase y la velocidad de grupo para ondas en aguas profundas ($\lambda \ll h$)? ¿Son dispersivas las ondas en esta condición?
4.  Suponga que el agua es profunda, $\lambda \ll h$, y que las longitudes de onda son tan cortas que $\lambda \ll \lambda_{\text{crítica}}$, de modo que domina la tensión superficial y la gravedad es despreciable. Estas ondas se llaman ondas capilares. ¿Cuáles son su velocidad de fase y de grupo? ¿Son dispersivas las ondas capilares?

**Problema 7.2 (30 pts)**

La figura 1 muestra la curva de dispersión de cierto medio. (No haga ninguna suposición sobre la forma matemática de esta curva.)

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet7_ES/fig1.png)

Figura 1: relación de dispersión $\omega$ frente a $k$ de un medio genérico, con una forma curva no especificada.

1.  ¿Para qué frecuencia(s) angular(es) $\omega$, aproximadamente, son iguales la velocidad de fase y la velocidad de grupo ($v_p$ y $v_g$)?
2.  ¿Qué frecuencia angular media elegiría para transmitir un pulso a la mayor velocidad posible? ¿Cuánto vale esa velocidad?
3.  ¿Cuál será la respuesta del medio si lo excita en $\omega = \omega_0 = 1\times10^4\ \text{s}^{-1}$? (Pista: para $\omega \to \omega_0$, ¿cuáles son los valores de $v_p$ y $v_g$?)

**Problema 7.3 (30 pts)**

Considere una cuerda infinita de densidad lineal $\rho_L$ bajo tensión $T$. Un pulso de forma gaussiana viaja por la cuerda, produciendo un desplazamiento vertical dado por:

$$y(x,t) = \exp\!\left[-\frac{1}{2}\left(\frac{x-vt}{\sigma}\right)^2\right]$$

1.  Encuentre la distribución de frecuencias $C(\omega)$ que contribuyen a este pulso calculando la «transformada inversa de Fourier» (ec. 10.37 de Georgi). Esta es una integral muy conocida; $C(\omega)$ es también una gaussiana de anchura $\sigma_\omega$, puede usar herramientas en línea para encontrarla. Asegúrese de que todas las constantes sean correctas.
2.  Calcule el producto de las anchuras de las dos gaussianas, $\sigma \cdot \sigma_\omega$.
3.  Esboce la forma del pulso $y(x,0)$ en $t=0$ para $\sigma=1$ y $\sigma=5$.
4.  Esboce la forma de $C(\omega)$ en $x=0$ para $\sigma=1$ y $\sigma=5$ (no para $\sigma_\omega=1$ y $\sigma_\omega=5$).
5.  Compare las formas obtenidas de $y(x,0)$ y $C(\omega)$ para distintos valores de $\sigma$. ¿Observa alguna tendencia interesante?

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.
