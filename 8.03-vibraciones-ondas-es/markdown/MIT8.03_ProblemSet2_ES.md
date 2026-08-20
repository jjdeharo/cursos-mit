*Massachusetts Institute of Technology*

**Física 8.03SC — Otoño de 2016**

**Tarea 2**

## Problemas

**Problema 2.1 (20 pts)**

En el circuito de la figura 1, $C = 2\ \mu\text{F}$, $L = 2\ \text{mH}$ y $R = 20\ \Omega$. Inicialmente, en el instante $t=0$, tenemos $V_C(t=0) = 5\ \text{V}$ y corriente $i(t=0) = 0.5\ \text{A}$.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet2_ES/fig1.png)

Figura 1: circuito RLC con un condensador $C$, una bobina $L$ y una resistencia $R$ en serie, recorridos por la corriente $i(t)$.

1.  Traduzcamos ahora esta situación física a matemáticas. Escriba la ecuación de movimiento en términos de $Q(t)$, la carga almacenada en el condensador.
2.  ¿Qué tipo de oscilador estamos considerando aquí? (¿No amortiguado, subamortiguado, con amortiguamiento crítico o sobreamortiguado?) Explique por qué lo cree así.
3.  Encuentre una expresión analítica para $V_C(t)$ para todo $t>0$.

**Problema 2.2 (20 pts)**

En un laboratorio cercano al Gran Colisionador de Hadrones, un delicado cristal de masa $M$ está sostenido por cuatro muelles sin masa en paralelo, cada uno con constante $k$. Todo el montaje se coloca sobre una mesa. Cuando los estudiantes de posgrado del laboratorio mueven la mesa por el suelo, el tablero vibra, produciendo una fuerza vertical efectiva $F = MA_0\cos(\omega_d t)$ sobre la masa $M$ en el sistema de referencia del tablero.

1.  Sea $x$ el desplazamiento vertical del cristal respecto a su posición de equilibrio. Escriba la ecuación de movimiento del instrumento. (Puede suponer que no hay fuerza de rozamiento en esta parte del problema.)
2.  Encuentre la amplitud de vibración del cristal (la masa $M$) en el estado estacionario. (Suponiendo que hay pérdidas de energía muy pequeñas en este sistema, de modo que la solución homogénea se extingue cuando $t \to \infty$.)
3.  Para reducir en un factor diez la amplitud de vibración del cristal obtenida en (a), ¿cómo propondría modificar los cuatro muelles?, es decir, ¿cuánto más largos (o cortos) deberían ser los nuevos muelles? Suponga $k/M \gg \omega_d^2$. (Pista: la constante de un muelle es proporcional a su área e inversamente proporcional a su longitud.)
4.  Una forma mejor de reducir esta amplitud de vibración en un factor diez respecto a la original es insertar una especie de amortiguador blando y sin masa entre el cristal y la mesa, en paralelo con los muelles. Suponiendo que el amortiguador produce una fuerza resistiva igual a $-b$ veces la velocidad de $M$, deduzca una ecuación que le permita determinar el valor de $b$ en términos de $k$, $M$, $\omega_d$, y resuelva para $b$, suponiendo $k/M \gg \omega_d^2$.

**Problema 2.3 (20 pts)**

Durante un huracán reciente, una física esperaba en un cruce. Observó el semáforo, suspendido sobre la calle por cables, oscilar verticalmente con el viento. Como había cursado 8.03 cuando era estudiante de grado en el MIT, notó de inmediato que el sistema se comportaba como un oscilador masa-muelle amortiguado, con la suspensión de cables desempeñando el papel del muelle. Observó que las perturbaciones de la amplitud tardaban 4 segundos (el tiempo $e^{-1}$) en amortiguarse (es decir, la amplitud pasa de $A$ a $e^{-1}A$ en 4 segundos). De repente, la mitad inferior del semáforo se desprendió y cayó al pavimento. La nueva posición de equilibrio de la mitad restante quedó 0.1 metros más alta que antes.

1.  ¿Cuál es la frecuencia natural no amortiguada (en hercios) del semáforo tras la separación?
2.  Suponga que toda la disipación ocurre en el sistema de suspensión. ¿Cuál es el tiempo de decaimiento (el tiempo $e^{-1}$) de las oscilaciones de amplitud del semáforo tras la separación?
3.  Escriba una expresión analítica para el desplazamiento vertical, $y(t)$, del semáforo respecto a su nueva posición de equilibrio tras la separación. Suponga que el semáforo estaba en reposo ($\dot y = 0$) en la posición de equilibrio anterior en el instante de la separación, $t=0$. Dé valores numéricos, con unidades, para cualquier constante que aparezca en la expresión.

**Problema 2.4 (20 pts)**

Considere una masa $m$ que se mueve sobre un carril de aire horizontal. La masa está unida por ambos lados a dos muelles idénticos, cada uno con constante $k$ y longitud relajada $\ell_0$ (véase la figura 2). El extremo del primer muelle está fijo. El extremo del segundo muelle está conectado a un motor eléctrico que le hace realizar un movimiento armónico con amplitud $\Delta$ y frecuencia angular $\omega$. En $t=0$ los muelles están relajados, con $\ell = \ell_0$, y la masa está en reposo, $\dot x(0) = 0$. Defina el origen del sistema de coordenadas en la posición de la masa en $t=0$, de modo que $x(0)=0$.

En $t=0$ se enciende el motor, de forma que el extremo del muelle empieza a moverse según la ecuación

$$x_{\text{ext}} = \Delta \sin(\omega t) + \ell_0$$

Suponga que el movimiento de la masa está afectado por una pequeña fricción del aire dependiente de la velocidad, $-b\dot x$.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet2_ES/fig2.png)

Figura 2: masa $m$ sobre un carril de aire, unida a la izquierda a un muelle fijo de constantes $k, \ell_0$ y a la derecha a otro muelle idéntico cuyo extremo se mueve como $\Delta\sin(\omega t)$.

1.  Plantee cuidadosamente la ecuación de movimiento unidimensional para la masa $m$, incluyendo todas las fuerzas. Organice la ecuación de forma que se distingan claramente los términos del oscilador y los términos relacionados con la fuerza externa.
2.  Postule, sin resolver, la solución completa para el movimiento de la masa $x(t) = x_{\text{libre}}(t) + x_{\text{forzada}}(t)$. Indique qué constantes de la solución dependen solo de las propiedades del oscilador, cuáles de las propiedades de la fuerza externa y cuáles deben determinarse a partir de las condiciones iniciales.
3.  Encuentre la amplitud y la fase del movimiento estacionario de la masa. Esboce su dependencia con la frecuencia de la fuerza impulsora $\omega$ y con los parámetros dados.
4.  Encuentre la frecuencia $\omega_{\text{máx}}$ para la que la amplitud es máxima.
5.  Use las condiciones iniciales para encontrar la solución específica, incluyendo tanto el oscilador libre como la solución estacionaria, con la elección adecuada de todos los parámetros.

**Problema 2.5 (20 pts)**

Considere un sistema de tres muelles y dos masas como se muestra en la figura 3, donde las masas están obligadas a moverse solo en la dirección vertical. El sistema se prepara en un laboratorio en la Tierra, con la fuerza gravitatoria apuntando hacia abajo. Las constantes de los muelles son $K_A = 78$, $K_B = 60$ y $K_C = 24$, medidas en N/m. Las dos masas son $m_1 = 4$ y $m_2 = 12$, medidas en kg. Las longitudes naturales de los muelles A y B son iguales a la longitud natural de C.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.03-vibraciones-ondas-es/html/figuras/MIT8.03_ProblemSet2_ES/fig3.png)

Figura 3: dos masas colgando verticalmente; el muelle $K_A$ conecta un soporte fijo con $m_2$, el muelle $K_C$ conecta $m_2$ con otro soporte fijo lateral, y el muelle $K_B$ conecta $m_2$ con $m_1$, colgando esta última en el extremo inferior.

1.  Defina el/los sistema(s) de coordenadas y escriba las ecuaciones de movimiento de las dos masas.
2.  Escriba la ecuación de movimiento en forma matricial. Muestre claramente la matriz $M^{-1}K$ tal como se define en el libro de texto.
3.  Encuentre los modos normales de oscilación y sus frecuencias angulares asociadas.
4.  Si la masa $m_1$ se desplaza 1 cm hacia arriba desde su posición de equilibrio y $m_2$ se mantiene en su posición de equilibrio original, y ambos bloques se sueltan desde el reposo en $t=0$, escriba las expresiones para el movimiento posterior de ambos bloques.

------------------------------------------------------------------------

*MIT OpenCourseWare* *https://ocw.mit.edu*

*8.03SC Physics III: Vibrations and Waves* *Otoño de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite:* <https://ocw.mit.edu/terms>.
