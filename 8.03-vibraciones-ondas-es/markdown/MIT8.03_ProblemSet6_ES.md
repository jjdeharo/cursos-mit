*Massachusetts Institute of Technology*

**Física 8.03SC — Otoño de 2016**

**Tarea 6**

## Problemas

**Problema 6.1 (25 pts)**

Considere ondas sonoras propagándose a lo largo del eje $x$ en un tubo de órgano, descritas por la ecuación de ondas para el desplazamiento longitudinal, $\psi$, de un elemento de volumen de aire,

$$\frac{\partial^2 \psi}{\partial t^2} = A\, \frac{\partial^2 \psi}{\partial x^2}$$

donde la constante $A = 90000\ \text{m}^2/\text{s}^2$. El tubo de órgano está cerrado en un extremo, $x=0$, y abierto en el otro, $x=L=1.5\ \text{m}$.

1.  Dibuje los tres primeros modos normales en el intervalo $0 \le x \le L$ (es decir, esboce $\psi$ en función de $x$ en el instante de máximo desplazamiento), y escriba las frecuencias de modo normal para cada uno. Este problema no requiere cálculos elaborados ni resolver la ecuación anterior; solo necesita comprensión física de cómo se determinan los modos normales y algo de aritmética muy sencilla.
2.  Para los tres primeros modos normales, esboce la presión en función de $x$ en su amplitud máxima.
3.  Si el tubo se cambia para que esté abierto por ambos extremos, ¿qué longitud debe tener para conservar la frecuencia del modo fundamental?

**Problema 6.2 (25 pts)**

Durante la clase discutimos la solución de onda de las ecuaciones de Maxwell, pero no terminamos la deducción de la ecuación de ondas para el campo magnético.

1.  Demuestre que $\vec\nabla \times (\vec\nabla \times \vec A) = \vec\nabla(\vec\nabla \cdot \vec A) - (\vec\nabla \cdot \vec\nabla)\vec A$, donde $\vec A$ es un vector.
2.  Demuestre que, en el vacío, $\nabla^2 \vec B = \mu_0 \epsilon_0 \dfrac{\partial^2 \vec B}{\partial t^2}$, usando las ecuaciones de Maxwell.

**Problema 6.3 (25 pts)**

El objetivo de este problema es demostrar que un pulso plano —un pulso que viaja en cierta dirección sin variación (en un instante dado) perpendicular a esa dirección— es solución de las ecuaciones de Maxwell. Elegiremos la dirección de propagación a lo largo del eje $x$:

$$\vec E(\vec r, t) = E_0\, \hat y\, f(x - ct)$$

donde $f(\xi)$ es una función arbitraria, suficientemente regular.

1.  Demuestre que este campo satisface la ecuación de ondas electromagnética.
2.  Demuestre que el campo satisface $\vec\nabla \cdot \vec E = 0$. ¿Qué otras direcciones del vector $\vec E$ son compatibles con esta ecuación de Maxwell (ley de Gauss)?
3.  Encuentre una expresión para el campo magnético asociado a este pulso.

**Problema 6.4 (25 pts)**

En un lugar muy alejado de la Tierra, dos ondas planas EM sinusoidales, ambas de frecuencia $\nu$ y amplitud de campo eléctrico $E_0$ a lo largo de $\hat y$, viajan en direcciones opuestas en este espacio vacío a lo largo de la dirección $\hat x$. En $t=0$, se observa que el campo eléctrico es 0 en $x=0$.

1.  Escriba el campo eléctrico de una onda viajera sinusoidal que se propaga en la dirección $x$ positiva. (Pista: véanse los apuntes de la clase 12, página 6, y el ejemplo discutido en clase. En general, el campo eléctrico de una onda EM sinusoidal progresiva puede escribirse como $\vec E(\vec r, t) = \text{Re}(\vec E_0\, e^{j(\vec k \cdot \vec r - \omega t)})$, donde $\vec r = x\hat x + y\hat y + z\hat z$ y $\hat k = \vec k/|\vec k|$ es la dirección de propagación.)
2.  Encuentre el campo total $\vec E(\vec r,t)$ de las dos ondas planas y el promedio temporal de $E^2(\vec r, t)$ (promediado en un periodo).
3.  Encuentre el campo $\vec B(\vec r, t)$ correspondiente de las dos ondas planas y el promedio temporal de $B^2(\vec r,t)$ (promediado en un periodo).
4.  Encuentre la densidad de energía $U(\vec r, t)$ y su promedio temporal (promediado en un periodo).
5.  Encuentre el vector de Poynting $\vec S(\vec r, t)$ y su promedio temporal (promediado en un periodo).

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.
