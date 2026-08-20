# Observables, operadores hermíticos e incertidumbre

## Vídeos de esta clase (YouTube)

**Lección 9: Observables, Hermitian operators, measurement and uncertainty. Particle on a circle.**

- [Expectation value of Hermitian operators](https://www.youtube.com/watch?v=qP6y2edM6Ms)
- [Eigenfunctions of a Hermitian operator](https://www.youtube.com/watch?v=K3WI62VJqVo)
- [Completeness of eigenvectors and measurement postulate](https://www.youtube.com/watch?v=XF6FAEi_54I)
- [Consistency condition. Particle on a circle](https://www.youtube.com/watch?v=_jPVD45YYlk)
- [Defining uncertainty](https://www.youtube.com/watch?v=rCRH9CTThlo)

------------------------------------------------------------------------

B. Zwiebach

3 de marzo de 2016

## Contenido

1.  Observables y operadores hermíticos
2.  Incertidumbre

## 1. Observables y operadores hermíticos

Comencemos recordando la definición de un operador hermítico. El operador $\hat{Q}$ es hermítico si, para la clase de funciones de onda $\Psi$ con las que trabajamos,

$$\int dx\, \Psi_1^* \hat{Q}\Psi_2 = \int dx\, (\hat{Q}\Psi_1)^* \Psi_2 \, . \qquad \text{(1.1)}$$

A veces usaremos una notación más breve para las integrales de pares de funciones:

$$(\Psi_1, \Psi_2) \equiv \int dx\, \Psi_1^*(x)\Psi_2(x) \, . \qquad \text{(1.2)}$$

Nótese que para cualquier constante $a$

$$(a\Psi_1, \Psi_2) = a^*(\Psi_1, \Psi_2) \, , \qquad (\Psi_1, a\Psi_2) = a\,(\Psi_1, \Psi_2) \, . \qquad \text{(1.3)}$$

Con esta notación, la condición de hermiticidad se enuncia de forma más breve como

$$\hat{Q} \text{ es hermítico:} \qquad (\Psi_1, \hat{Q}\Psi_2) = (\hat{Q}\Psi_1, \Psi_2) \, . \qquad \text{(1.4)}$$

El valor esperado de $\hat{Q}$ se definió como

$$\langle Q \rangle_\Psi = \int dx\, \Psi^* \hat{Q}\Psi = (\Psi, \hat{Q}\Psi) \, . \qquad \text{(1.5)}$$

Para que esta fórmula tenga sentido, el estado $\Psi$ debe estar normalizado.

**Afirmación 1.** El valor esperado de un operador hermítico es real. Para demostrar esto, tomamos el complejo conjugado de la definición anterior. El complejo conjugado de la integral es la integral del complejo conjugado del integrando, por lo tanto

$$\langle Q \rangle_\Psi^* = \left( \int dx\, \Psi^* \hat{Q}\Psi \right)^* = \int dx\, \Psi (\hat{Q}\Psi)^* = \int dx\, (\hat{Q}\Psi)^* \Psi \, . \qquad \text{(1.6)}$$

Nótese que $\hat{Q}\Psi$ es una función de onda, así que tiene sentido tomar su complejo conjugado (nunca tenemos que pensar en conjugar $\hat{Q}$). Usando la hermiticidad del operador, lo trasladamos hacia $\Psi$ para obtener

$$\langle Q \rangle_\Psi^* = \int dx\, \Psi^* \hat{Q}\Psi = \langle Q \rangle_\Psi \, , \qquad \text{(1.7)}$$

demostrando así que el valor esperado es efectivamente real.

**Afirmación 2.** Los autovalores de un operador hermítico son reales. Supongamos que el operador $\hat{Q}$ tiene un autovalor $q_1$ asociado a una autofunción normalizada $\psi_1(x)$:

$$\hat{Q}\psi_1(x) = q_1 \psi_1(x) \, . \qquad \text{(1.8)}$$

Ahora calculemos el valor esperado de $\hat{Q}$ en el estado $\psi_1$:

$$\langle \hat{Q} \rangle_{\psi_1} = (\psi_1, \hat{Q}\psi_1) = (\psi_1, q_1 \psi_1) = q_1 (\psi_1, \psi_1) = q_1 \, . \qquad \text{(1.9)}$$

Por la afirmación 1, el valor esperado es real, y por tanto también lo es el autovalor $q_1$, como queríamos demostrar. Obsérvese el hecho interesante de que el valor esperado de $\hat{Q}$ en un autoestado está dado precisamente por el autovalor correspondiente.

Consideremos ahora el conjunto de autofunciones y autovalores del operador hermítico $\hat{Q}$:

$$\hat{Q}\, \psi_1(x) = q_1 \psi_1(x) \, , \qquad \text{(1.10)}$$

$$\hat{Q}\, \psi_2(x) = q_2 \psi_2(x) \, , \qquad \text{(1.11)}$$

$$\ldots$$

La lista puede ser finita o infinita.

**Afirmación 3.** Las autofunciones pueden organizarse de manera que satisfagan la ortonormalidad:

$$(\psi_i, \psi_j) = \int dx\, \psi_i^*(x)\psi_j(x) = \delta_{ij} \, . \qquad \text{(1.12)}$$

Para $i = j$, esto es simplemente cuestión de normalizar adecuadamente cada autofunción, lo cual podemos hacer fácilmente. La ecuación también establece que autofunciones distintas son ortogonales, es decir, tienen solapamiento nulo. Expliquemos ahora por qué esto es así para $i \neq j$ con $q_i \neq q_j$. En efecto, para ello evaluamos $(\psi_i, \hat{Q}\psi_j)$ de dos maneras distintas. Primero

$$(\psi_i, \hat{Q}\psi_j) = (\psi_i, q_j \psi_j) = q_j (\psi_i, \psi_j) \, , \qquad \text{(1.13)}$$

y segundo, usando la hermiticidad de $\hat{Q}$ y la realidad de los autovalores,

$$(\psi_i, \hat{Q}\psi_j) = (\hat{Q}\psi_i, \psi_j) = (q_i \psi_i, \psi_j) = q_i (\psi_i, \psi_j) \, . \qquad \text{(1.14)}$$

Igualando los lados derechos finales de las dos evaluaciones obtenemos

$$(q_j - q_i)(\psi_i, \psi_j) = 0 \, . \qquad \text{(1.15)}$$

Dado que los autovalores se supusieron distintos, esto demuestra que $(\psi_i, \psi_j) = 0$, como se afirmó. Esta no es aún una demostración completa de (1.12) porque es posible tener degeneraciones en el espectro, es decir, autofunciones distintas con el mismo autovalor. En ese caso, el argumento anterior no funciona. Entonces hay que demostrar que es posible elegir combinaciones lineales de las autofunciones degeneradas que sean mutuamente ortogonales (la ortogonalidad con las autofunciones fuera del espacio degenerado es automática). Esto se hace en 8.05.

**Afirmación 4.** Las autofunciones de $\hat{Q}$ forman un conjunto completo de funciones base. Cualquier $\Psi$ razonable puede escribirse como una superposición de autofunciones de $\hat{Q}$. (Este es el llamado teorema espectral, que se demuestra en 8.05 en el caso de dimensión finita.) Esto significa que

$$\Psi(x) = \alpha_1 \psi_1(x) + \alpha_2 \psi_2(x) + \cdots = \sum_i \alpha_i \psi_i(x) \, , \qquad \text{(1.16)}$$

con coeficientes calculables $\alpha_i$. En efecto, si conocemos las autofunciones tenemos que $\alpha_i$ se calcula haciendo la integral de $\psi_i^*$ contra $\Psi$:

$$\alpha_i = (\psi_i, \Psi) \, . \qquad \text{(1.17)}$$

Demostramos esto rápidamente haciendo la integral

$$\int dx\, \psi_i^*(x)\Psi(x) = \int dx\, \psi_i^*(x) \sum_j \alpha_j \psi_j(x) = \sum_j \alpha_j \int dx\, \psi_i^*(x)\psi_j(x) = \sum_j \alpha_j \delta_{ij} = \alpha_i \, . \qquad \text{(1.18)}$$

La condición de que $\Psi$ esté normalizada implica una condición sobre los coeficientes $\alpha_i$. Tenemos

$$\int dx\, \Psi^*(x)\Psi(x) = \int dx\, \sum_i \alpha_i^* \psi_i^*(x) \sum_j \alpha_j \psi_j(x)$$

$$= \sum_{i,j} \alpha_i^* \alpha_j \int dx\, \psi_i^*(x)\psi_j(x) \qquad \text{(1.19)}$$

$$= \sum_{i,j} \alpha_i^* \alpha_j \delta_{ij} = \sum_i \alpha_i^* \alpha_i \, ,$$

de modo que la normalización de $\Psi$ implica que

$$\sum_i |\alpha_i|^2 = 1 \, . \qquad \text{(1.20)}$$

Ya estamos en condiciones de enunciar el postulado de la medición. Esta es la forma en que entendemos que los operadores hermíticos representan observables y aprendemos las reglas que estos siguen.

**Postulado de la medición:** Si medimos el operador hermítico $\hat{Q}$ en el estado $\Psi$, los posibles resultados de la medición son los autovalores $q_1, q_2, \ldots$. La probabilidad $p_i$ de medir $q_i$ está dada por

$$p_i = |\alpha_i|^2 \, , \qquad \text{(1.21)}$$

donde $\Psi(x) = \sum_i \alpha_i \psi_i(x)$. Después del resultado $q_i$, el estado del sistema pasa a ser

$$\Psi(x) = \psi_i(x) \, . \qquad \text{(1.22)}$$

Esto se denomina el colapso de la función de onda.

El colapso de la función de onda implica que, inmediatamente después de la medición que arrojó $q_i$, una medición repetida de $\hat{Q}$ dará $q_i$ sin incertidumbre. Ocurre una pequeña sutileza si tenemos autoestados degenerados. Supongamos que la función de onda contiene una parte

$$\Psi = (\alpha_i \psi_i + \alpha_k \psi_k) + \ldots \qquad \text{(1.23)}$$

donde $\psi_i$ y $\psi_k$ tienen el mismo autovalor $q$, y los puntos suspensivos representan otros términos. Entonces, si medimos $q$, el estado tras la medición colapsa a la suma de esos dos términos

$$\Psi = \frac{\alpha_i \psi_i + \alpha_k \psi_k}{\sqrt{|\alpha_i|^2 + |\alpha_j|^2}} \, , \qquad \text{(1.24)}$$

con el denominador de raíz cuadrada incluido para proporcionar la normalización adecuada de $\Psi$. Como verificación de consistencia, nótese que las probabilidades $p_i$ de encontrar los diversos autovalores como resultados suman correctamente uno:

$$\sum_i p_i = \sum_i |\alpha_i|^2 = 1 \, , \qquad \text{(1.25)}$$

por la condición de normalización para $\Psi$ dada en (1.20). El postulado de la medición sigue la interpretación de Copenhague de la mecánica cuántica.

Nótese que el postulado de la medición usa la propiedad de que cualquier vector en un espacio vectorial puede escribirse como una suma de vectores distintos de un número infinito de maneras. Si vamos a medir $\hat{Q}_1$ expandimos el estado en autoestados de $\hat{Q}_1$; si vamos a medir $\hat{Q}_2$ expandimos el estado en autoestados de $\hat{Q}_2$, y así sucesivamente. Cada descomposición es adecuada para una medición particular. Cada descomposición revela las diversas probabilidades para los resultados del observable específico.

**Ejercicio.** Use la expansión $\Psi = \sum_i \alpha_i \psi_i$ para calcular el valor esperado $\langle Q \rangle$. Encontramos

$$\langle \hat{Q} \rangle = \int dx\, \sum_i \alpha_i^* \psi_i^*(x)\, \hat{Q} \sum_j \alpha_j \psi_j(x)$$

$$= \sum_{i,j} \alpha_i^* \alpha_j \int dx\, \psi_i^*(x) \hat{Q}\psi_j(x)$$

$$= \sum_{i,j} \alpha_i^* \alpha_j q_j \int dx\, \psi_i^*(x)\psi_j(x) \qquad \text{(1.26)}$$

$$= \sum_{i,j} \alpha_i^* \alpha_j q_j \delta_{ij} = \sum_i |\alpha_i|^2 q_i = \sum_i p_i q_i \, .$$

Esto concuerda con nuestras expectativas: el valor esperado de $\hat{Q}$ es la suma de los posibles resultados $q_i$ multiplicados por las probabilidades correspondientes $p_i$. Esta es una buena verificación de consistencia de nuestra definición de valores esperados.

**Ejemplo.** Partícula libre en el círculo $x \in [0, L]$.

Imaginamos que los puntos $x = 0$ y $x = L$ están identificados para formar un círculo de circunferencia $L$. Una función de onda $\Psi(x)$ en el círculo debe satisfacer la condición de periodicidad

$$\Psi(x + L) = \Psi(x) \, , \qquad \text{(1.27)}$$

Supongamos que en cierto instante fijo tenemos la función de onda

$$\Psi(x) = \sqrt{\frac{2}{L}}\, \frac{1}{\sqrt{3}} \sin\left(\frac{2\pi x}{L}\right) + \sqrt{\frac{2}{L}}\, \sqrt{\frac{2}{3}} \cos\left(\frac{6\pi x}{L}\right) \, . \qquad \text{(1.28)}$$

Esta función de onda satisface la condición de periodicidad, como debería comprobar. Queremos saber cuáles son los valores posibles del momento y sus probabilidades correspondientes.

Dada nuestra discusión, debemos encontrar el conjunto de autoestados de momento y reescribir la función de onda como una superposición de tales estados. Los autoestados de momento son exponenciales de la forma $e^{ikx}$. En el círculo ocurren dos cosas que no ocurren en el espacio libre. Primero, el momento estará cuantizado como consecuencia de la condición de periodicidad (1.27). Segundo, dado que el espacio aquí es de longitud finita, las funciones de onda de momento serán normalizables. Consideremos la condición de periodicidad aplicada a $e^{ikx}$. Necesitamos

$$e^{ikx} = e^{ik(x+L)} \;\rightarrow\; e^{ikL} = 1 \;\rightarrow\; kL = 2\pi m \, , \quad m \in \mathbb{Z} \, . \qquad \text{(1.29)}$$

Nótese que $m$ puede ser cualquier entero, positivo, negativo o cero. Escribimos entonces para los autoestados de momento, etiquetados por $m$

$$\psi_m(x) = N\, e^{\frac{2\pi i m x}{L}} \, , \qquad \text{(1.30)}$$

con $N$ una constante de normalización real. La condición de normalización da

$$1 = \int_0^L |\psi_m(x)|^2\, dx = N^2 \int_0^L dx = N^2 L \;\rightarrow\; N = \frac{1}{\sqrt{L}} \, . \qquad \text{(1.31)}$$

Por lo tanto, nuestros autoestados de momento son

$$\psi_m(x) = \frac{1}{\sqrt{L}}\, e^{\frac{2\pi i m x}{L}} \, , \qquad \text{(1.32)}$$

y estos son estados con momento $p_m$, que se calcula de la siguiente manera

$$\hat{p}\, \psi_m = \frac{\hbar}{i} \frac{\partial}{\partial x} \psi_m = \frac{2\pi m \hbar}{L} \psi_m \;\rightarrow\; p_m = \frac{2\pi m \hbar}{L} \, . \qquad \text{(1.33)}$$

Ahora que contamos con los autoestados de momento, debemos simplemente reescribir la función de onda (1.28) como una superposición de tales estados:

$$\Psi(x) = \sqrt{\frac{2}{3}}\, \frac{1}{2i}\, \frac{1}{\sqrt{L}}\left(e^{\frac{2\pi i x}{L}} - e^{-\frac{2\pi i x}{L}}\right) + \frac{2}{\sqrt{3}}\, \frac{1}{2}\, \frac{1}{\sqrt{L}}\left(e^{\frac{6\pi i x}{L}} + e^{-\frac{6\pi i x}{L}}\right) \, . \qquad \text{(1.34)}$$

Reconocemos entonces que tenemos

$$\Psi(x) = \sqrt{\frac{2}{3}}\, \frac{1}{2i}\, \psi_1(x) - \sqrt{\frac{2}{3}}\, \frac{1}{2i}\, \psi_{-1}(x) + \frac{1}{\sqrt{3}}\, \psi_3(x) + \frac{1}{\sqrt{3}}\, \psi_{-3}(x) \, . \qquad \text{(1.35)}$$

Este es nuestro resultado clave: la función de onda original escrita como una superposición de autoestados de momento $\psi_m(x)$. Ahora podemos dar los valores posibles $p$ del momento y sus probabilidades correspondientes $P$:

$$p = \frac{2\pi \hbar}{L} \, , \quad P = \left(\sqrt{\frac{2}{3}}\, \frac{1}{2i}\right)^2 = \frac{1}{6} \, ,$$

$$p = -\frac{2\pi \hbar}{L} \, , \quad P = \left(-\sqrt{\frac{2}{3}}\, \frac{1}{2i}\right)^2 = \frac{1}{6} \, ,$$

$$p = \frac{6\pi \hbar}{L} \, , \quad P = \left(\frac{1}{\sqrt{3}}\right)^2 = \frac{1}{3} \, , \qquad \text{(1.36)}$$

$$p = -\frac{6\pi \hbar}{L} \, , \quad P = \left(\frac{1}{\sqrt{3}}\right)^2 = \frac{1}{3} \, .$$

## 2. Incertidumbre

Para variables aleatorias, la incertidumbre es la desviación estándar: la raíz cuadrada del valor esperado del cuadrado de las desviaciones respecto al valor medio. Sea $Q$ una variable aleatoria que toma valores $Q_1, \ldots, Q_n$ con probabilidades $p_1, \ldots, p_n$, respectivamente. El valor esperado es

$$\overline{Q} = \sum_i p_i Q_i \, , \qquad \text{(2.37)}$$

y la varianza (el cuadrado de la desviación estándar) es

$$(\Delta Q)^2 \equiv \sum_i p_i (Q_i - \overline{Q})^2 \, . \qquad \text{(2.38)}$$

Esta definición deja claro que si $\Delta Q = 0$, entonces la variable aleatoria es constante: cada término en la suma anterior debe anularse, haciendo que $Q_i = \overline{Q}$ para todo $i$. Encontramos otra expresión útil expandiendo la definición anterior

$$(\Delta Q)^2 = \sum_i p_i Q_i^2 - 2 \sum_i p_i Q_i \overline{Q} + \sum_i p_i \overline{Q}^2$$

$$= \overline{Q^2} - 2\overline{Q}\,\overline{Q} + \overline{Q}^2 = \overline{Q^2} - \overline{Q}^2 \, , \qquad \text{(2.39)}$$

donde usamos $\sum_i p_i = 1$. Por lo tanto

$$(\Delta Q)^2 = \overline{Q^2} - \overline{Q}^2 \, . \qquad \text{(2.40)}$$

Dado que, por definición, $(\Delta Q)^2 \geq 0$, tenemos la interesante desigualdad

$$\overline{Q^2} \geq \overline{Q}^2 \, . \qquad \text{(2.41)}$$

Consideremos ahora el caso mecánico-cuántico. Ya hemos definido los valores esperados de operadores hermíticos, así que ahora podemos imitar la definición (2.40) y declarar que la incertidumbre $\Delta Q_\Psi$ de un operador en un estado $\Psi$ es un número real cuyo cuadrado está dado por

$$(\Delta Q)_\Psi^2 = \langle Q^2 \rangle_\Psi - (\langle Q \rangle_\Psi)^2 \, . \qquad \text{(2.42)}$$

A veces, por brevedad, omitimos la etiqueta del estado,

$$(\Delta Q)^2 = \langle Q^2 \rangle - \langle Q \rangle^2 \, . \qquad \text{(2.43)}$$

**Afirmación 1.** La incertidumbre también puede escribirse como el valor esperado del cuadrado de la diferencia entre el operador y su valor esperado:

$$(\Delta Q)^2 = \left\langle \left(\hat{Q} - \langle \hat{Q} \rangle\right)^2 \right\rangle \, . \qquad \text{(2.44)}$$

En efecto, expandiendo el lado derecho tenemos

$$\left\langle \hat{Q}^2 - 2\hat{Q}\langle \hat{Q} \rangle + \langle \hat{Q} \rangle^2 \right\rangle = \langle \hat{Q}^2 \rangle - 2\langle \hat{Q} \rangle \langle \hat{Q} \rangle + \langle \hat{Q} \rangle^2 = \langle \hat{Q}^2 \rangle - \langle \hat{Q} \rangle^2 \, . \qquad \text{(2.45)}$$

**Afirmación 2.** La incertidumbre puede escribirse como la integral del cuadrado de la norma de $(\hat{Q} - \langle Q \rangle)\Psi$:

$$(\Delta Q)^2 = \int_{-\infty}^{\infty} dx\, \left| \left(\hat{Q} - \langle Q \rangle\right) \Psi(x) \right|^2 \, . \qquad \text{(2.46)}$$

En efecto, para demostrar esto comenzamos con (2.44). Mediante una demostración muy similar, podemos mostrar que esto es equivalente a

$$(\Delta Q)^2 = \left\langle \left(\hat{Q} - \langle Q \rangle\right)^2 \right\rangle = \int dx\, \Psi^* \left(\hat{Q} - \langle Q \rangle\right)^2 \Psi \, . \qquad \text{(2.47)}$$

Usando la hermiticidad de $\hat{Q}$ y la realidad de $\langle \hat{Q} \rangle$, podemos trasladar uno de los dos factores para que actúe sobre $\Psi^*$:

$$(\Delta Q)^2 = \int dx\, \left[\left(\hat{Q} - \langle Q \rangle\right) \Psi\right]^* \left(\hat{Q} - \langle Q \rangle\right) \Psi = \int dx\, \left|\left(\hat{Q} - \langle Q \rangle\right)\Psi\right|^2 \, . \qquad \text{(2.48)}$$

Esto completa la demostración de la afirmación 2.

Si $\Delta Q = 0$, entonces, por la afirmación 2, debemos tener que para todo $x$:

$$(\hat{Q} - \langle Q \rangle)\Psi(x) = 0 \, , \quad \rightarrow \quad \hat{Q}\Psi(x) = \langle Q \rangle \Psi(x) \, . \qquad \text{(2.49)}$$

Vemos que $\Psi$ es un autoestado de $\hat{Q}$, lo cual efectivamente significa que no hay incertidumbre en la medición. Por supuesto, si $\Psi$ es un autoestado de $\hat{Q}$, entonces $\hat{Q}\Psi = \langle Q \rangle \Psi$ y la incertidumbre se anula. En resumen, hemos establecido la equivalencia

$$\Delta \hat{Q}_\Psi = 0 \iff \Psi \text{ es un autoestado de } \hat{Q} \, . \qquad \text{(2.50)}$$

*Andrew Turner transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare

https://ocw.mit.edu

8.04 Física Cuántica I

Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

# Apéndice: Lista de problemas 4 (Problem Set 4, 2016)

**Física Cuántica I (8.04), Primavera de 2016** **Tarea 4**

Departamento de Física del MIT — Entrega: viernes 4 de marzo de 2016, 12:00 del mediodía 25 de febrero de 2016

**Anuncios**

- Lectura recomendada: Griffiths, secciones 1.5, 1.6, 2.4.

## Problema 1. Ejercicios sobre paquetes que cambian de forma \[5 puntos\]

1.  Un protón libre está localizado dentro de $\Delta x = 10^{-10}$ m. Estime el tiempo $t_s$ que tarda el paquete en dispersarse apreciablemente. Repita el cálculo para un protón localizado dentro de 1 cm.

2.  Considere un paquete de ondas que satisface la relación $\Delta x \Delta p \sim \hbar$. Demuestre que la condición $\Delta p \ll p$ garantiza que el paquete no se dispersa apreciablemente en el tiempo que tarda en pasar por una posición fija.

## Problema 2. Corriente de probabilidad en tres dimensiones \[10 puntos\]

En la dispersión elástica de partículas en el espacio tridimensional, la función de onda toma la forma

$$\Psi(\mathbf{x}) = e^{ikz} + \frac{f(\theta)}{r} e^{ikr} \, , \quad \text{válida para } r \text{ grande} .$$

Se ha suprimido la dependencia temporal; se trata simplemente de una fase global dependiente del tiempo $e^{-iEt/\hbar}$ con $E = \hbar^2 k^2/(2m)$. No jugará ningún papel aquí.

El primer término representa las partículas incidentes, moviéndose en la dirección $+z$. El blanco se encuentra en el origen $r = 0$ y el segundo término representa la amplitud de las partículas que se mueven radialmente hacia afuera —las partículas dispersadas—. Esta amplitud depende de $\theta$ pero se supone independiente de $\varphi$; $f(\theta)$ es una función compleja de $\theta$ que contiene la información sobre la dispersión. Recuerde que $\theta$ es el ángulo polar y $z = r\cos\theta$.

Cuando se calcula la corriente de probabilidad $\mathbf{J}(\mathbf{x})$ asociada a $\Psi$, habrá una contribución $\mathbf{J}_1$ debida al primer término (la onda plana), una contribución $\mathbf{J}_2$ debida al segundo término (las ondas esféricas), y una contribución $\mathbf{J}_{12}$ debida a la interferencia entre el primer y el segundo término:

$$\mathbf{J}(\mathbf{x}) = \mathbf{J}_1(\mathbf{x}) + \mathbf{J}_2(\mathbf{x}) + \mathbf{J}_{12}(\mathbf{x}) \, .$$

1.  Calcule la corriente de probabilidad $\mathbf{J}_1$ y el flujo total de esta corriente sobre una esfera grande de radio $R$ centrada en el origen $r = 0$.

2.  Calcule la componente radial $\hat{r} \cdot \mathbf{J}_2$ de la corriente de probabilidad $\mathbf{J}_2$. Aquí $\hat{r}$ es el vector unitario en la dirección radial. Calcule el flujo de esta corriente sobre una esfera de radio $R$ centrada en el origen, en el límite $R \to \infty$. Su respuesta debe dejarse como una integral sobre el ángulo sólido $\int d\Omega$, o sobre $\int d\theta$, si lo prefiere.

3.  Calcule la componente radial del término de interferencia $\mathbf{J}_{12}$, pero quédese solo con la parte dominante en $1/r$ (es decir, ignore los términos en $1/r^2$). Demuestre que la respuesta puede escribirse en la forma

$$\hat{r} \cdot \mathbf{J}_{12} = \frac{\hbar k}{mr} \, \text{Im}\left[i (\ldots)\right] \, ,$$

donde $(\ldots)$ representa términos que su cálculo debe determinar. Estos términos dependen de $f(\theta)$, $\cos\theta$, y el producto $kr$ en exponenciales. Calcular el flujo de esta corriente sobre la esfera grande es delicado, así que lo dejaremos para más adelante (¡el resultado final es el llamado teorema óptico!).

## Problema 3. Evolución del paquete de ondas gaussiano \[15 puntos\]

Considere el paquete de ondas normalizado que representa el estado de una partícula de masa $m$ en $t = 0$:

$$\Psi_a(x, 0) = \frac{1}{(2\pi)^{1/4}\sqrt{a}} \exp\left(-\frac{x^2}{4a^2}\right) \, .$$

Aquí $a$ es un parámetro de longitud que representa la anchura del paquete en el instante inicial.

1.  Confirme que $\Psi_a(x, 0)$ está correctamente normalizada.

2.  Encuentre la representación de Fourier de $\Psi_a(x, 0)$, es decir, determine la función $\Phi_a(k)$ tal que

$$\Psi_a(x, 0) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \Phi_a(k) e^{ikx} \, dk \, .$$

1.  Suponiendo que la partícula es libre, encuentre la función de onda $\Psi_a(x, t)$ para $t > 0$ arbitrario. La respuesta es un poco engorrosa, pero puede escribirse de manera más clara usando la constante de tiempo $\tau$ construida a partir de las constantes del problema:

$$\tau \equiv \frac{2ma^2}{\hbar} \, .$$

1.  En el instante inicial la densidad de probabilidad es

$$|\Psi_a(x, 0)|^2 = \frac{1}{\sqrt{2\pi}\, a} \exp\left(-\frac{x^2}{2a^2}\right) \equiv G(x; a) \, ,$$

donde hemos definido la gaussiana $G(x; a)$ con parámetro de anchura $a$. ¿Cuál es la densidad de probabilidad $|\Psi_a(x, t)|^2$ para $t > 0$? Exprese su respuesta en términos de la gaussiana $G$ con un parámetro de anchura dependiente del tiempo $a(t)$. Dé $a(t)$.

Integral útil: válida para constantes complejas $a$ y $b$, con parte real de $a$ positiva:

$$\int_{-\infty}^{\infty} e^{-ax^2 + bx} \, dx = \sqrt{\frac{\pi}{a}} \exp\left(\frac{b^2}{4a}\right) \, , \quad \text{cuando } \text{Re}(a) > 0 \, .$$

## Problema 4. Identidad de Parseval en 1D y 3D, y aplicación \[10 puntos\]

1.  Considere el par de Fourier $(\Psi(x), \Phi(p))$ relevante para las funciones de onda unidimensionales (1D) y el par de Fourier $(\Psi(\mathbf{x}), \Phi(\mathbf{p}))$ relevante para las funciones de onda tridimensionales (3D). Use las relaciones de Fourier y la forma integral de la función delta para demostrar las versiones 1D y 3D de la identidad de Parseval:[1]

$$\int_{-\infty}^{\infty} dx\, |\Psi(x)|^2 = \int_{-\infty}^{\infty} dp\, |\Phi(p)|^2 \, ,$$

$$\int d^3x\, |\Psi(\mathbf{x})|^2 = \int d^3p\, |\Phi(\mathbf{p})|^2 \, .$$

1.  En el átomo de hidrógeno, la función de onda del estado fundamental toma la forma $\Psi(\mathbf{x}) = N e^{-r/a_0}$, donde $r = |\mathbf{x}|$, $a_0$ es el radio de Bohr, y $N$ es una constante de normalización. Encuentre $N$. La transformada de Fourier (que no necesita derivar) toma la forma

$$\Phi(\mathbf{p}) = \frac{N'}{\left(1 + \dfrac{a_0^2 p^2}{\hbar^2}\right)^{2}} \, ,$$

para alguna constante $N'$ y con $p \equiv |\mathbf{p}|$. Encuentre $N'$ (puede usar un manipulador algebraico para hacer la integral). Calcule la probabilidad de que el electrón se encuentre con un momento cuya magnitud excede $\hbar/a_0$. (Escriba sus integrales explícitamente, pero puede evaluarlas con un ordenador). \[La distribución de momento fue medida mediante ionización de hidrógeno atómico por un haz de electrones de alta energía; véase Lohan, B. y Weigold, E. (1981) “Direct measurement of the Electron Momentum Probability Distribution in Atomic Hydrogen,” Phys. Lett. 86A, 139-141.\]

## Problema 5. Teorema de Ehrenfest \[10 puntos\]

Considere una partícula que se mueve en una dimensión con hamiltoniano $H$ dado por

$$H = \frac{p^2}{2m} + V(x) \, .$$

Demuestre que los valores esperados $\langle x \rangle$ y $\langle p \rangle$ son funciones dependientes del tiempo que satisfacen las siguientes ecuaciones diferenciales:

$$\frac{d}{dt}\langle x \rangle = \frac{1}{m}\langle p \rangle \, ,$$

$$\frac{d}{dt}\langle p \rangle = -\left\langle \frac{\partial V}{\partial x} \right\rangle \, .$$

## Problema 6. Incertidumbre del momento \[5 puntos\]

Demuestre que, en un paquete de ondas de partícula libre, la incertidumbre del momento $\Delta p$ no cambia en el tiempo.

## Problema 7. Encontrando el significado de la fase de la función de onda \[10 puntos\]

Suponga que $\psi_o(x)$ es una función de onda correctamente normalizada con $\langle x \rangle_{\psi_o} = x_o$ y $\langle p \rangle_{\psi_o} = p_o$, donde $x_o$ y $p_o$ son constantes. Defina el operador de impulso (boost) $\hat{B}_q$ como el operador que actúa sobre funciones arbitrarias de $x$ multiplicándolas por una fase dependiente de $q$:

$$\hat{B}_q f(x) = e^{iqx/\hbar} f(x) \, .$$

Aquí $q$ es un número real con las unidades apropiadas. Considere ahora una nueva función de onda obtenida aplicando el impulso a la función de onda inicial:

$$\psi_{\text{new}}(x) = \hat{B}_q \, \psi_o(x) \, .$$

1.  ¿Cuál es el valor esperado $\langle x \rangle_{\psi_{\text{new}}}$ en el estado dado por $\psi_{\text{new}}(x)$?

2.  ¿Cuál es el valor esperado $\langle p \rangle_{\psi_{\text{new}}}$ en el estado dado por $\psi_{\text{new}}(x)$?

3.  Con base en sus resultados, ¿cuál es el significado físico de añadir un factor global $e^{iqx/\hbar}$ a una función de onda?

4.  Calcule $[\hat{p}, \hat{B}_q]$ y $[\hat{x}, \hat{B}_q]$.

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*

[1] En matemáticas esto se llama teorema de Plancherel. El resultado de Parseval es el análogo para series de Fourier.
