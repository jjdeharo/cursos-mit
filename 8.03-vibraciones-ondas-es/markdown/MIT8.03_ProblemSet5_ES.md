*Massachusetts Institute of Technology*

**Física 8.03SC — Otoño de 2016**

**Tarea 5**

## Problemas

**Problema 5.1 (20 pts)**

En un laboratorio, un estudiante de posgrado estudiaba una cuerda de longitud $L$, fija en ambos extremos.

1.  Encuentre la energía total de una vibración de la cuerda oscilando en su $n$-ésimo modo normal con amplitud $A$. La tensión en la cuerda es $T$ y su masa total es $M$. (Pista: considere la energía cinética integrada en el instante en que la cuerda está recta, de modo que la energía potencial debida a la vibración es cero.)
2.  Calcule la energía total de vibración de la misma cuerda si vibra en la siguiente superposición de modos normales. Suponga que es la suma de las energías de los dos modos tomados por separado.

$$\psi(x,t) = A_1 \sin\!\left(\frac{\pi x}{L}\right)\cos(\omega_1 t) + A_3 \sin\!\left(\frac{3\pi x}{L}\right)\cos(\omega_3 t - \pi/4)$$

**Problema 5.2 (20 pts)**

Una cuerda de longitud $L$, tensión $T$ y masa por unidad de longitud $\rho_L$, fija en ambos extremos, se deforma como se muestra en la figura 1. La altura del pulso cuadrado es $h$. La cuerda está obligada a vibrar solo en la dirección vertical. En $t=0$, la cuerda se suelta cuidadosamente de modo que su velocidad inicial es 0.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet5_ES/fig1.png)

Figura 1: pulso cuadrado de altura $h$ en el centro de una cuerda de longitud $L$ fija en ambos extremos.

1.  ¿Cuál es la velocidad de una onda progresiva en esta cuerda?
2.  Dibuje a escala la forma de la cuerda en $t = \dfrac{L}{4}\sqrt{\rho_L/T}$.
3.  Dibuje a escala la forma de la cuerda en $t = L\sqrt{\rho_L/T}$.

**Problema 5.3 (20 pts)**

Considere una cuerda de densidad de masa $\rho$ bajo tensión $T$. Un pulso viaja por la cuerda, produciendo un desplazamiento vertical dado por:

$$y(x,t) = y_0\, e^{-\frac{1}{2}\left(\frac{x-vt}{\sigma}\right)^2}$$

La energía de la onda es la suma de la energía cinética de la cuerda en movimiento y la energía potencial de la deformación de la cuerda, integradas a lo largo de toda su longitud.

1.  Para el desplazamiento dado arriba, encuentre una expresión para la densidad de energía cinética de la cuerda en un instante $t$ y esboce el resultado en función de $x$.
2.  Encuentre una expresión para la densidad de energía potencial de la cuerda. Compárela con la densidad de energía cinética.
3.  Encuentre una expresión para la energía total del pulso en términos de $T$, $y_0$ y $\sigma$. Compruebe las unidades. Recuerde que la energía debe variar como el cuadrado de la amplitud. (Pista: puede necesitar la integral gaussiana $\int_{-\infty}^{\infty} x^2 e^{-ax^2}\,dx = \dfrac{1}{2a}\sqrt{\pi/a}$.)
4.  Encuentre una expresión para la potencia (en vatios) que atraviesa el punto $x=x_0$ en función del tiempo. Esboce el resultado.

**Problema 5.4 (20 pts)**

Considere una cuerda con densidad lineal $\rho_L$ dividida en dos tramos. Las dos mitades están unidas a un anillo sin masa que desliza verticalmente sin fricción por una varilla en $x=0$, como se muestra en la figura 2. Una de las dos mitades está estirada en la dirección $x$ negativa con tensión $T_L$, y la otra en la dirección $x$ positiva con tensión $T_R$. Note que la varilla vertical es necesaria para equilibrar las fuerzas horizontales sobre la cuerda sin masa que surgen de los dos tramos con tensiones distintas.

Suponga que hay una onda viajera de amplitud $A$ que llega desde la dirección $x$ negativa.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet5_ES/fig2.png)

Figura 2: cuerda dividida en $x=0$ mediante un anillo sin masa que desliza por una varilla vertical; el tramo izquierdo tiene tensión $T_L$ y el derecho tensión $T_R$.

1.  Suponiendo que la onda incidente tiene la forma funcional $\psi(x,t) = \alpha\cos(kx-\omega t)$, escriba la expresión general para el desplazamiento de la cuerda $\psi(x,t)$ a ambos lados del anillo.
2.  Escriba las expresiones para las condiciones de contorno en $x=0$. (Pista: como el anillo no tiene masa, la fuerza total sobre él es 0.)
3.  Encuentre los coeficientes de reflexión ($R$) y transmisión ($T$) para este sistema.
4.  Demuestre que la energía se conserva en la unión.
5.  ¿Cuáles son los coeficientes de reflexión y transmisión en los siguientes tres casos: $T_R = T_L$, $T_R \gg T_L$ y $T_R \ll T_L$? ¿Tiene sentido su resultado?

**Problema 5.5 (20 pts)**

Una cuerda de densidad de masa $\rho_L$ bajo tensión $T$ está unida mediante un anillo sin masa a un alambre cubierto de grasa viscosa. El anillo experimenta una fuerza de arrastre vertical $F_y = -b\,\partial y/\partial t$ cuando el extremo de la cuerda se mueve.

![Figura](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet5_ES/figs1.png)

Figura: cuerda de tensión $T$ unida a un anillo sin masa que desliza por un alambre vertical cubierto de grasa.

1.  Aplique la segunda ley de Newton al anillo para encontrar la condición de contorno en el extremo de la cuerda, como una relación entre las derivadas parciales de $y(x,t)$ en ese punto. (Pista: hay tres fuerzas actuando sobre el anillo: la tensión de la cuerda, la fuerza normal del alambre y la fuerza de arrastre vertical.)
2.  Demuestre que la condición de contorno se satisface con un pulso incidente $f(t-x/v)$ y un pulso reflejado $g(t+x/v)$. Encuentre $g$ en términos de $f$.
3.  Demuestre que su resultado tiene el comportamiento adecuado en los límites $b\to 0$ (deslizamiento libre) y $b\to\infty$ (cuerda fija).

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.
