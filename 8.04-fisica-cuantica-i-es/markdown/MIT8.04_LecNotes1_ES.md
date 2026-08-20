*B. Zwiebach* *9 de febrero de 2016*

# Capítulo 1: Características clave de la mecánica cuántica

## Vídeos de esta clase (YouTube)

**Lección 1: An overview of quantum mechanics.**

- [Quantum mechanics as a framework. Defining linearity](https://www.youtube.com/watch?v=jANZxzetPaQ)
- [Linearity and nonlinear theories. Schrödinger’s equation](https://www.youtube.com/watch?v=kiuwtaprFjk)
- [Necessity of complex numbers](https://www.youtube.com/watch?v=f079K1f2WQk)
- [Photons and the loss of determinism](https://www.youtube.com/watch?v=8OsUQ1yXCcI)
- [The nature of superposition. Mach-Zehnder interferometer](https://www.youtube.com/watch?v=CR-eOhdxbes)

------------------------------------------------------------------------

La mecánica cuántica tiene ya casi cien años, pero todavía estamos descubriendo algunas de sus sorprendentes características y sigue siendo objeto de mucha investigación y especulación. El marco de la mecánica cuántica es una extensión rica y elegante del marco de la física clásica. También es contraintuitivo y casi paradójico.

La física cuántica ha reemplazado a la física clásica como la descripción fundamental correcta de nuestro universo físico. Se usa rutinariamente para describir la mayoría de los fenómenos que ocurren a distancias cortas. La física cuántica es el resultado de aplicar el marco de la mecánica cuántica a diferentes fenómenos físicos. Así, tenemos la Electrodinámica Cuántica, cuando la mecánica cuántica se aplica al electromagnetismo; la Óptica Cuántica, cuando se aplica a la luz y a los dispositivos ópticos; o la Gravedad Cuántica, cuando se aplica a la gravitación. La mecánica cuántica proporciona, en efecto, un marco notablemente coherente y elegante. La era de la física cuántica comienza en 1925, con los descubrimientos de Schrödinger y Heisenberg. Las semillas de estos descubrimientos fueron sembradas por Planck, Einstein, Bohr, de Broglie y otros. Es un tributo a la imaginación humana que hayamos sido capaces de descubrir el conjunto de reglas contraintuitivo y abstracto que define la mecánica cuántica. Aquí pretendemos explicar y ofrecer cierta perspectiva sobre las características principales de este marco.

Comenzaremos discutiendo la propiedad de linealidad, que la mecánica cuántica comparte con la teoría electromagnética. Esta propiedad nos dice qué tipo de teoría es la mecánica cuántica y por qué, podría argumentarse, es más simple que la mecánica clásica. A continuación pasamos a los fotones, las partículas de luz. Usamos fotones y polarizadores para explicar por qué la física cuántica no es determinista y, en contraste con la física clásica, los resultados de algunos experimentos no pueden predecirse. La mecánica cuántica es un marco en el que solo podemos predecir las probabilidades de los distintos resultados de un experimento dado. Nuestro siguiente tema son las superposiciones cuánticas, en las que un objeto cuántico de alguna manera consigue existir simultáneamente en dos estados mutuamente incompatibles. Una bombilla cuántica, por ejemplo, podría estar en un estado en el que está encendida y apagada al mismo tiempo.

## 1. Linealidad de las ecuaciones de movimiento

En física, una teoría se describe habitualmente mediante un conjunto de ecuaciones para ciertas cantidades llamadas variables dinámicas de la teoría. Tras escribir una teoría, la tarea más importante es encontrar soluciones de las ecuaciones. Una solución de las ecuaciones describe una realidad posible, según la teoría. Como un universo en expansión es una solución de las ecuaciones gravitacionales de Albert Einstein, por ejemplo, se sigue que un universo en expansión es posible, según esta teoría. Una única teoría puede tener muchas soluciones, cada una describiendo una realidad posible.

Hay teorías lineales y teorías no lineales. Las teorías no lineales son más complejas que las lineales. En una teoría lineal ocurre un hecho notable: si se tienen dos soluciones, se obtiene una tercera solución de la teoría simplemente sumando las dos soluciones. Un ejemplo de una hermosa teoría lineal es la teoría de Maxwell del electromagnetismo, una teoría que gobierna el comportamiento de los campos eléctrico y magnético. Un campo, como probablemente ya sabe, es una cantidad cuyos valores pueden depender de la posición y del tiempo. Una solución simple de esta teoría describe una onda electromagnética que se propaga en una dirección dada. Otra solución simple podría describir una onda electromagnética propagándose en una dirección distinta. Debido a que la teoría es lineal, tener las dos ondas propagándose simultáneamente, cada una en su propia dirección y sin afectarse mutuamente, es una solución nueva y consistente. La suma es una solución en el sentido de que el campo eléctrico en la nueva solución es la suma del campo eléctrico en la primera solución más el campo eléctrico en la segunda solución. Lo mismo ocurre con el campo magnético: el campo magnético en la nueva solución es la suma del campo magnético en la primera solución más el campo magnético en la segunda solución. De hecho, se puede sumar cualquier número de soluciones y seguir obteniendo una solución. Aunque esto suene esotérico, usted está totalmente familiarizado con ello. El aire a su alrededor está lleno de ondas electromagnéticas, cada una propagándose ajena a las demás. Están las ondas de miles de teléfonos móviles, las ondas que transportan cientos de mensajes de internet inalámbrico, las ondas de multitud de emisoras de radio, canales de televisión, y muchas, muchas más. Hoy en día, un único cable transatlántico puede transportar simultáneamente millones de llamadas telefónicas, junto con enormes cantidades de vídeo y datos de internet. Todo ello gracias a la linealidad.

Más concretamente, decimos que las ecuaciones de Maxwell son ecuaciones lineales. Una solución de la ecuación de Maxwell se describe mediante un campo eléctrico $E$, un campo magnético $B$, una densidad de carga $\rho$ y una densidad de corriente $J$, todos denotados colectivamente como $(E, B, \rho, J)$. Esta colección de campos y fuentes satisface las ecuaciones de Maxwell. La linealidad implica que si $(E, B, \rho, J)$ es una solución, también lo es $(\alpha E, \alpha B, \alpha \rho, \alpha J)$, donde todos los campos y fuentes han sido multiplicados por la constante $\alpha$. Dadas dos soluciones

$$(E_1, B_1, \rho_1, J_1), \quad \text{y} \quad (E_2, B_2, \rho_2, J_2), \qquad \text{(1.1)}$$

la linealidad también implica que podemos obtener una nueva solución sumándolas

$$(E_1 + E_2, B_1 + B_2, \rho_1 + \rho_2, J_1 + J_2). \qquad \text{(1.2)}$$

La nueva solución puede llamarse la superposición de las dos soluciones originales.

No es difícil explicar qué es, en general, una ecuación lineal o un conjunto lineal de ecuaciones. Consideremos la ecuación

$$Lu = 0, \qquad \text{(1.3)}$$

donde, esquemáticamente, $u$ denota la incógnita. La incógnita puede ser un número, o una función del tiempo, una función del espacio, una función del tiempo y del espacio, esencialmente cualquier cosa desconocida. De hecho, $u$ podría representar una colección de incógnitas, en cuyo caso reemplazaríamos $u$ por $u_1, u_2, \ldots$. El símbolo $L$ denota un operador lineal, un objeto que satisface las dos propiedades siguientes

$$L(u_1 + u_2) = Lu_1 + Lu_2, \qquad L(au) = aLu, \qquad \text{(1.4)}$$

donde $a$ es un número. Nótese que estas condiciones implican que

$$L(\alpha u_1 + \beta u_2) = \alpha Lu_1 + \beta Lu_2, \qquad \text{(1.5)}$$

lo que muestra que si $u_1$ es una solución ($Lu_1 = 0$) y $u_2$ es una solución ($Lu_2 = 0$), entonces $\alpha u_1 + \beta u_2$ también es una solución. Llamamos a $\alpha u_1 + \beta u_2$ la superposición general de las soluciones $u_1$ y $u_2$. Un ejemplo puede ayudar. Consideremos la ecuación

$$\frac{du}{dt} + \frac{1}{\tau} u = 0, \qquad \text{(1.6)}$$

donde $\tau$ es una constante con unidades de tiempo. Esta es, de hecho, una ecuación diferencial lineal, y toma la forma $Lu = 0$ si definimos

$$Lu \equiv \frac{du}{dt} + \frac{1}{\tau} u \qquad \text{(1.7)}$$

**Ejercicio 1.** Verifique que (1.7) satisface las condiciones para un operador lineal.

La teoría de la relatividad general de Einstein es una teoría no lineal cuya variable dinámica es un campo gravitacional, el campo que describe, por ejemplo, cómo se mueven los planetas alrededor de una estrella. Al ser una teoría no lineal, sencillamente no se pueden sumar los campos gravitacionales de distintas soluciones para hallar una nueva solución. Esto hace que la teoría de Einstein sea bastante complicada, según todos los indicios mucho más complicada que la teoría de Maxwell. De hecho, ¡la mecánica clásica, tal como fue inventada principalmente por Isaac Newton, también es una teoría no lineal! En mecánica clásica las variables dinámicas son las posiciones y velocidades de las partículas, sobre las que actúan fuerzas. No existe una forma general de usar dos soluciones para construir una tercera.

En efecto, consideremos la ecuación de movimiento para una partícula en una línea bajo la influencia de un potencial independiente del tiempo $V(x)$, que en general es una función arbitraria de $x$. La variable dinámica en este problema es $x(t)$, la posición en función del tiempo. Denotando por $V'$ la derivada de $V$ respecto a su argumento, la segunda ley de Newton toma la forma

$$m \frac{d^2 x(t)}{dt^2} = -V'(x(t)). \qquad \text{(1.8)}$$

El lado izquierdo es la masa por la aceleración y el lado derecho es la fuerza experimentada por la partícula en el potencial. Probablemente vale la pena resaltar que el lado derecho es la función $V'(x)$ evaluada en $x$ igualado a $x(t)$:

$$V'(x(t)) \equiv \left. \frac{\partial V(x)}{\partial x} \right|_{x = x(t)}. \qquad \text{(1.9)}$$

Aunque aquí podríamos haber usado una derivada ordinaria, escribimos una derivada parcial, como es habitual para el caso general de potenciales dependientes del tiempo. La razón por la que la ecuación (1.8) no es una ecuación lineal es que la función $V'(x)$ no es lineal. En general, para funciones arbitrarias $u$ y $v$ esperamos

$$V'(au) \neq aV'(u), \quad \text{y} \quad V'(u+v) \neq V'(u) + V'(v). \qquad \text{(1.10)}$$

Como resultado, dada una solución $x(t)$, no se espera que la solución escalada $\alpha x(t)$ sea también una solución. Dadas dos soluciones $x_1(t)$ y $x_2(t)$, tampoco está garantizado que $x_1(t) + x_2(t)$ sea una solución.

**Ejercicio.** ¿Cuál es el potencial $V(x)$ más general para el cual la ecuación de movimiento de $x(t)$ es lineal?

La mecánica cuántica es una teoría lineal. La ecuación distintiva de esta teoría, la llamada ecuación de Schrödinger, es una ecuación lineal para una cantidad llamada función de onda, y determina su evolución temporal. La función de onda es la variable dinámica en mecánica cuántica pero, curiosamente, su interpretación física no estaba clara para Erwin Schrödinger cuando escribió la ecuación en 1925. Fue Max Born quien, meses después, sugirió que la función de onda codifica probabilidades. Esta fue la interpretación física correcta, pero fue profundamente rechazada por muchos, incluido el propio Schrödinger, quien permaneció descontento con ella el resto de su vida. La linealidad de la mecánica cuántica implica una profunda simplicidad. En cierto sentido, la mecánica cuántica es más simple que la mecánica clásica. En mecánica cuántica las soluciones pueden sumarse para formar nuevas soluciones.

La función de onda $\Psi$ depende del tiempo y también puede depender del espacio. La ecuación de Schrödinger (ES) es una ecuación diferencial parcial que toma la forma

$$i\hbar \frac{\partial \Psi}{\partial t} = \hat{H}\Psi, \qquad \text{(1.11)}$$

donde el hamiltoniano (u operador de energía) $\hat{H}$ es un operador lineal que puede actuar sobre funciones de onda:

$$\hat{H}(a\Psi) = a\hat{H}\Psi, \qquad \hat{H}(\Psi_1 + \Psi_2) = \hat{H}(\Psi_1) + \hat{H}(\Psi_2), \qquad \text{(1.12)}$$

con $a$ una constante que, de hecho, no necesita ser real; puede ser un número complejo. Por supuesto, ¡$\hat{H}$ en sí mismo no depende de la función de onda! Para comprobar que la ecuación de Schrödinger es lineal, la escribimos en la forma $L\Psi = 0$ con $L$ definido como

$$L\Psi \equiv i\hbar \frac{\partial \Psi}{\partial t} - \hat{H}\Psi \qquad \text{(1.13)}$$

Ahora es sencillo verificar que $L$ es un operador lineal. Físicamente, esto significa que si $\Psi_1$ y $\Psi_2$ son soluciones de la ecuación de Schrödinger, entonces también lo es la superposición $\alpha\Psi_1 + \beta\Psi_2$, donde $\alpha$ y $\beta$ son ambos números complejos, es decir, $(\alpha, \beta \in \mathbb{C})$.

## 2. Los números complejos son esenciales

La mecánica cuántica es la primera teoría física que realmente hace uso de los números complejos. Los números que la mayoría usamos en la vida cotidiana (enteros, fracciones, decimales) son números reales. El conjunto de los números complejos se denota por $\mathbb{C}$ y el conjunto de los números reales se denota por $\mathbb{R}$. Los números complejos aparecen cuando combinamos números reales con la unidad imaginaria $i$, definida como igual a la raíz cuadrada de menos uno: $i \equiv \sqrt{-1}$. Al ser la raíz cuadrada de menos uno, significa que $i$ al cuadrado debe dar menos uno: $i^2 = -1$. Los números complejos son fundamentales en matemáticas. Una ecuación como $x^2 = -4$, para una incógnita $x$, no puede resolverse si $x$ ha de ser real. Ningún número real al cuadrado da menos uno. Pero si permitimos números complejos, tenemos las soluciones $x = \pm 2i$. Los matemáticos han demostrado que todas las ecuaciones polinómicas pueden resolverse en términos de números complejos.

Un número complejo $z$, en toda su generalidad, es un número de la forma

$$z = a + ib \in \mathbb{C}, \qquad a, b \in \mathbb{R}. \qquad \text{(2.1)}$$

Aquí $a$ y $b$ son números reales, e $ib$ denota el producto de $i$ con $b$. El número $a$ se llama parte real de $z$ y $b$ se llama parte imaginaria de $z$:

$$\text{Re}\, z = a, \qquad \text{Im}\, z = b. \qquad \text{(2.2)}$$

El conjugado complejo $z^*$ de $z$ se define como

$$z^* = a - ib. \qquad \text{(2.3)}$$

Puede verificar rápidamente que un número complejo $z$ es real si $z^* = z$, y que es puramente imaginario si $z^* = -z$. Para cualquier número complejo $z = a + ib$ se puede definir la norma $|z|$ del número complejo como un número real positivo dado por

$$|z| = \sqrt{a^2 + b^2}. \qquad \text{(2.4)}$$

Puede comprobar rápidamente que

$$|z|^2 = zz^*, \qquad \text{(2.5)}$$

donde $z^* \equiv a - ib$ se llama el conjugado complejo de $z = a + ib$. Los números complejos se representan como vectores en un «plano complejo» bidimensional. La parte real del número complejo es la componente $x$ del vector y la parte imaginaria del número complejo es la componente $y$. Si consideramos el vector de longitud unidad en el plano complejo que forma un ángulo $\theta$ con el eje $x$, tiene componente $x$ igual a $\cos\theta$ y componente $y$ igual a $\sin\theta$. El vector es, por tanto, el número complejo $\cos\theta + i\sin\theta$. La identidad de Euler relaciona esto con la exponencial de $i\theta$:

$$e^{i\theta} = \cos\theta + i\sin\theta. \qquad \text{(2.6)}$$

Un número complejo de la forma $e^{i\chi}$, con $\chi$ real, se llama fase pura.

Aunque los números complejos son a veces útiles en mecánica clásica o en la teoría de Maxwell, no son estrictamente necesarios. Ninguna de las variables dinámicas, que corresponden a cantidades medibles, es un número complejo. De hecho, los números complejos no pueden medirse en absoluto: todas las mediciones en física dan como resultado números reales. En mecánica cuántica, sin embargo, los números complejos son fundamentales. La ecuación de Schrödinger involucra números complejos. Más aún, la función de onda, la variable dinámica de la mecánica cuántica, es en sí misma un número complejo:

$$\Psi \in \mathbb{C}. \qquad \text{(2.7)}$$

Dado que los números complejos no se pueden medir, la relación entre la función de onda y una cantidad medible debe ser de alguna manera indirecta. La idea de Born de identificar las probabilidades, que son siempre números reales positivos, con el cuadrado de la norma de la función de onda, resultó muy natural. Si escribimos la función de onda de nuestro sistema cuántico como $\Psi$, las probabilidades de los posibles eventos se calculan a partir de $|\Psi|^2$. El marco matemático necesario para expresar las leyes de la mecánica cuántica consiste en espacios vectoriales complejos. En cualquier espacio vectorial tenemos objetos llamados vectores que pueden sumarse entre sí. En un espacio vectorial complejo, un vector multiplicado por un número complejo sigue siendo un vector. Como veremos en nuestro estudio de la mecánica cuántica, muchas veces es útil pensar en la función de onda $\Psi$ como un vector en algún espacio vectorial complejo.

## 3. Pérdida del determinismo

El mayor logro de Maxwell fue darse cuenta de que sus ecuaciones del electromagnetismo permitían la existencia de ondas propagantes. En particular, en 1865 conjeturó que la luz era una onda electromagnética, una fluctuación propagante de campos eléctrico y magnético. Los experimentos posteriores le dieron la razón. Hacia finales del siglo XIX los físicos estaban convencidos de que la luz era una onda. Sin embargo, la certeza no duró mucho. Los experimentos sobre la radiación de cuerpo negro y sobre la fotoemisión de electrones sugerían que el comportamiento de la luz debía ser más complicado que el de una simple onda. Max Planck y Albert Einstein fueron los contribuyentes más destacados a la resolución de los enigmas planteados por esos experimentos.

Para explicar las características del efecto fotoeléctrico, Einstein postuló (1905) que en un haz de luz la energía viene en cuantos: el haz está compuesto de paquetes de energía. Einstein implicaba esencialmente que la luz estaba hecha de partículas, cada una portando una cantidad fija de energía. Él mismo encontraba esta idea inquietante, convencido, como la mayoría de sus contemporáneos, de que, como había demostrado Maxwell, la luz era una onda. Anticipó que una entidad física, como la luz, que pudiera comportarse tanto como partícula como onda, podría provocar el fin de la física clásica y requeriría una teoría física completamente nueva. De hecho, tenía razón. Aunque nunca llegó a apreciar realmente la mecánica cuántica, sus ideas sobre las partículas de luz, más tarde llamadas fotones, ayudaron a construir esta teoría.

Los físicos tardaron hasta 1925 en aceptar que la luz podía comportarse como una partícula. Los experimentos de Arthur Compton (1923) terminaron por convencer a la mayoría de los escépticos. Hoy en día, las partículas de luz, o fotones, se manipulan rutinariamente en laboratorios de todo el mundo. Aunque sigan siendo misteriosos, nos hemos acostumbrado a ellos. Cada fotón de luz visible transporta muy poca energía: un pequeño pulso de láser puede contener miles de millones de fotones. Nuestro ojo, sin embargo, es un muy buen detector de fotones: en total oscuridad, somos capaces de ver luz cuando tan solo diez fotones inciden sobre nuestra retina. Cuando decimos que la luz se comporta como una partícula, nos referimos a una partícula mecánico-cuántica: un paquete de energía y momento que no está compuesto de paquetes más pequeños. No nos referimos a una partícula puntual clásica o corpúsculo newtoniano, que es un objeto de tamaño nulo con posición y velocidad definidas.

Resulta que la energía de un fotón depende únicamente del color de la luz. Como descubrió Einstein, la energía $E$ y la frecuencia $\nu$ de un fotón están relacionadas por

$$E = h\nu \qquad \text{(3.1)}$$

La frecuencia de un fotón determina la longitud de onda $\lambda$ de la luz mediante la relación $\nu\lambda = c$, donde $c$ es la velocidad de la luz. Todos los fotones verdes, por ejemplo, tienen la misma energía. Para aumentar la energía en un haz de luz manteniendo el mismo color, simplemente se necesitan más fotones.

Como explicaremos ahora, la existencia de fotones implica que la mecánica cuántica no es determinista. Con esto queremos decir que el resultado de un experimento no puede determinarse, como ocurriría en física clásica, mediante las condiciones que están bajo el control del experimentador.

Consideremos un polarizador cuya dirección preferencial está alineada a lo largo de la dirección $\hat{x}$, como se muestra en la Figura 1. La luz linealmente polarizada a lo largo de la dirección $\hat{x}$, es decir, luz cuyo campo eléctrico apunta en esa dirección, atraviesa el polarizador. Si la polarización de la luz incidente es ortogonal a la dirección $\hat{x}$, la luz no pasará en absoluto. Así, la luz polarizada linealmente en la dirección $\hat{y}$ será absorbida totalmente por el polarizador. Consideremos ahora luz polarizada a lo largo de una dirección que forma un ángulo $\alpha$ con el eje $x$, como se muestra en la Figura 2. ¿Qué ocurre?

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes1_ES/fig1.png)

Figura 1: Un polarizador que transmite luz linealmente polarizada a lo largo de la dirección $\hat{x}$.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes1_ES/fig2.png)

Figura 2: Luz linealmente polarizada a lo largo de la dirección que forma un ángulo $\alpha$ incidiendo sobre el polarizador.

Pensando en la luz como una onda propagante, el campo eléctrico incidente $E_\alpha$ forma un ángulo $\alpha$ con el eje $x$ y por lo tanto toma la forma

$$E_\alpha = E_0 \cos\alpha\, \hat{x} + E_0 \sin\alpha\, \hat{y}. \qquad \text{(3.2)}$$

Este es un campo eléctrico de magnitud $E_0$. Aquí estamos ignorando la dependencia temporal y espacial de la onda; no son relevantes para nuestra discusión. Cuando este campo eléctrico incide sobre el polarizador, la componente a lo largo de $\hat{x}$ pasa y la componente a lo largo de $\hat{y}$ es absorbida. Así,

$$\text{Más allá del polarizador:} \quad E = E_0 \cos\alpha\, \hat{x}. \qquad \text{(3.3)}$$

Probablemente recuerde que la energía de una onda electromagnética es proporcional al cuadrado de la magnitud del campo eléctrico. Esto significa que la fracción de la energía del haz que pasa a través del polarizador es $(\cos\alpha)^2$. También es bien sabido que la luz que emerge del polarizador tiene la misma frecuencia que la luz incidente.

Hasta aquí todo bien. Pero ahora, intentemos entender este resultado pensando en los fotones que componen la luz incidente. La premisa aquí es que todos los fotones del haz incidente son idénticos. Además, los fotones no interactúan entre sí. Podríamos incluso imaginar enviar toda la energía del haz de luz incidente un fotón a la vez. Puesto que toda la luz que emerge del polarizador tiene la misma frecuencia que la luz incidente, debemos concluir que cada fotón individual, o bien pasa, o bien es absorbido. Si una fracción de un fotón pasara, sería un fotón de menor energía y, por tanto, de menor frecuencia, algo que no ocurre.

Pero ahora tenemos un problema. Como sabemos por el análisis ondulatorio, aproximadamente una fracción $(\cos\alpha)^2$ de los fotones debe pasar, ya que esa es la fracción de la energía que se transmite. En consecuencia, una fracción $1 - (\cos\alpha)^2$ de los fotones debe ser absorbida. Pero si todos los fotones son idénticos, ¿por qué lo que le ocurre a un fotón no les ocurre a todos ellos?

La respuesta de la mecánica cuántica es que, en efecto, hay una pérdida de determinismo. Nadie puede predecir si un fotón pasará o será absorbido. Lo mejor que cualquiera puede hacer es predecir probabilidades. En este caso, habría una probabilidad $(\cos\alpha)^2$ de pasar y una probabilidad $1 - (\cos\alpha)^2$ de no pasar.

Se sugieren dos vías de escape. Quizás el polarizador no es realmente un objeto homogéneo y, dependiendo exactamente de dónde incide el fotón, o bien se absorbe o bien pasa. Los experimentos demuestran que no es así. Una posibilidad más intrigante fue sugerida por Einstein y otros. Una posible salida, afirmaban, era la existencia de variables ocultas. Los fotones, aunque aparentemente idénticos, tendrían otras propiedades ocultas, actualmente no comprendidas, que determinarían con certeza qué fotón pasa y cuál es absorbido. Las teorías de variables ocultas parecerían ser imposibles de comprobar, pero sorprendentemente sí pueden ponerse a prueba. Mediante el trabajo de John Bell y otros, los físicos han diseñado experimentos ingeniosos que descartan la mayoría de las versiones de las teorías de variables ocultas. Nadie ha logrado averiguar cómo restaurar el determinismo en la mecánica cuántica. Parece ser una tarea imposible.

Cuando intentamos describir fotones cuánticamente, podríamos usar funciones de onda, o de forma equivalente, el lenguaje de estados. Un fotón polarizado a lo largo de la dirección $\hat{x}$ no se representa mediante un campo eléctrico, sino que simplemente le damos un nombre a su estado:

$$|\text{fotón}; x\rangle. \qquad \text{(3.4)}$$

Aprenderemos las reglas necesarias para manipular tales objetos, pero por el momento puede pensar en ello como un vector en algún espacio todavía por definir. Otro estado de un fotón, o vector, es

$$|\text{fotón}; y\rangle, \qquad \text{(3.5)}$$

que representa un fotón polarizado a lo largo de $\hat{y}$. Estos estados son las funciones de onda que representan al fotón. Afirmamos ahora que los fotones del haz que está polarizado a lo largo de la dirección $\alpha$ están en un estado $|\text{fotón}; \alpha\rangle$ que puede escribirse como una superposición de los dos estados anteriores:

$$|\text{fotón}; \alpha\rangle = \cos\alpha\, |\text{fotón}; x\rangle + \sin\alpha\, |\text{fotón}; y\rangle. \qquad \text{(3.6)}$$

Esta ecuación debe compararse con (3.2). Aunque hay algunas similitudes —ambas son superposiciones—, una se refiere a campos eléctricos y la otra a «estados» de un único fotón. Cualquier fotón que emerja del polarizador estará necesariamente polarizado en la dirección $\hat{x}$ y, por lo tanto, estará en el estado

$$\text{Más allá del polarizador:} \quad |\text{fotón}; x\rangle. \qquad \text{(3.7)}$$

Esto puede compararse con (3.3), que con el factor $\cos\alpha$ lleva información sobre la amplitud de la onda. Aquí, para un único fotón, no hay lugar para tal factor.

En la famosa Quinta Conferencia Internacional Solvay de 1927, los físicos más notables del mundo se reunieron para discutir la teoría cuántica recién formulada. Diecisiete de los veintinueve asistentes fueron o llegaron a ser ganadores del Premio Nobel. Einstein, disgustado con la incertidumbre de la mecánica cuántica, pronunció la ahora famosa frase: «Dios no juega a los dados», a lo que Niels Bohr respondió, según se cuenta: «Einstein, deja de decirle a Dios lo que tiene que hacer». Bohr estaba dispuesto a aceptar la pérdida del determinismo; Einstein no.

## 4. Superposiciones cuánticas

Ya hemos discutido el concepto de linealidad: la idea de que la suma de dos soluciones que representan realidades físicas representa una nueva realidad física permitida. Esta superposición de soluciones tiene un significado directo en física clásica. En el caso del electromagnetismo, por ejemplo, si tenemos dos soluciones, cada una con su propio campo eléctrico y magnético, la solución «suma» se entiende de manera sencilla: su campo eléctrico es la suma de los campos eléctricos de las dos soluciones y su campo magnético es la suma de los campos magnéticos de las dos soluciones. En mecánica cuántica, como hemos explicado, la linealidad se cumple. La interpretación de una superposición, sin embargo, es muy sorprendente.

Un ejemplo interesante lo proporciona un interferómetro de Mach-Zehnder: un arreglo de divisores de haz, espejos y detectores usado por Ernst Mach y Ludwig Zehnder en la década de 1890 para estudiar la interferencia entre dos haces de luz.

Un divisor de haz, como su nombre indica, divide un haz incidente en dos haces, uno que se refleja en el divisor y otro que lo atraviesa. Nuestros divisores de haz estarán equilibrados: dividen un haz dado en dos haces de igual intensidad (Figura 3). La luz que rebota se llama haz reflejado, la luz que atraviesa se llama haz transmitido. El haz incidente puede incidir sobre el divisor desde arriba o desde abajo.

La configuración de Mach-Zehnder, mostrada en la Figura 4, tiene un divisor de haz izquierdo (BS1) y un divisor de haz derecho (BS2). En medio tenemos los dos espejos, M1 arriba y M2 abajo. Un haz entrante desde la izquierda es dividido por BS1 en dos haces, cada uno de los cuales incide sobre un espejo y luego es enviado a BS2. En BS2 los haces se recombinan y se envían a dos haces salientes que van hacia los detectores de fotones D0 y D1.

Es relativamente sencillo disponer los divisores de haz de modo que el haz entrante, tras dividirse en BS1 y recombinarse en BS2, emerja en el haz superior, que va hacia D0. En este arreglo, no llega luz en absoluto a D1. Esto requiere un efecto de interferencia preciso en BS2. Nótese que tenemos dos haces incidiendo sobre BS2; el haz superior se llama ‘a’ y el haz inferior se llama ‘b’. Dos contribuciones van hacia D0: la reflexión de ‘a’ en BS2 y la transmisión de ‘b’ en BS2. Estas dos contribuciones interfieren constructivamente para dar un haz que va hacia D0. También van dos contribuciones hacia D1: la transmisión de ‘a’ en BS2 y la reflexión de ‘b’ en BS2. Estas dos, en efecto, pueden disponerse para interferir destructivamente y así no dar ningún haz hacia D1.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes1_ES/fig3.png)

Figura 3: Un haz incidente que incide sobre un divisor de haz da como resultado un haz reflejado y un haz transmitido. Izquierda: haz incidente proveniente de arriba. Derecha: haz incidente proveniente de abajo.

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes1_ES/fig4.png)

Figura 4: Un interferómetro de Mach-Zehnder consta de dos divisores de haz BS1 y BS2, dos espejos M1 y M2, y dos detectores D0 y D1. Un haz incidente se divide en dos haces mediante BS1. Un haz recorre la rama superior, que contiene M1; el otro haz recorre la rama inferior, que contiene M2. Los haces de las dos ramas se recombinan en BS2 y luego se envían a los detectores. La configuración está preparada para producir una interferencia tal que todos los fotones incidentes terminen en el detector D0, y ninguno en D1.

Es instructivo pensar en el haz entrante como una secuencia de fotones que enviamos al interferómetro, uno a la vez. Esto muestra que, a nivel de fotones, la interferencia no es interferencia de un fotón con otro fotón. Cada fotón debe interferir consigo mismo para dar el resultado. En efecto, la interferencia entre dos fotones no es posible: la interferencia destructiva, por ejemplo, requeriría que dos fotones dieran como resultado ningún fotón, lo cual es imposible por conservación de la energía.

Por lo tanto, cada fotón hace la cosa muy extraña de atravesar ambas ramas del interferómetro. Cada fotón está en una superposición de dos estados: un estado en el que el fotón está en el haz superior o rama superior, sumado a un estado en el que el fotón está en el haz inferior o rama inferior. Así, el estado del fotón en el interferómetro es un estado curioso en el que el fotón parece estar haciendo dos cosas incompatibles al mismo tiempo.

La ecuación (3.6) es otro ejemplo de superposición cuántica. El estado del fotón tiene una componente a lo largo de un fotón polarizado en $x$ y una componente a lo largo de un fotón polarizado en $y$.

Cuando hablamos de una función de onda, también la llamamos a veces estado, porque la función de onda especifica el «estado» de nuestro sistema cuántico. También nos referimos a veces a los estados como vectores. Un estado cuántico puede no ser un vector como los vectores familiares en el espacio tridimensional, pero es un vector de todos modos, porque tiene sentido sumar estados y multiplicar estados por números. Del mismo modo que los vectores pueden sumarse, la linealidad garantiza que sumar funciones de onda o estados es algo con sentido. Al igual que cualquier vector puede escribirse como suma de otros vectores de muchas maneras distintas, haremos lo mismo con nuestros estados. Al escribir nuestro estado físico como sumas de otros estados, podemos aprender sobre las propiedades de nuestro estado.

Consideremos ahora dos estados $|A\rangle$ y $|B\rangle$. Supongamos, además, que al medir cierta propiedad $Q$ en el estado $|A\rangle$ la respuesta es siempre $a$, y que al medir la misma propiedad $Q$ en el estado $|B\rangle$ la respuesta es siempre $b$. Supongamos ahora que nuestro estado físico $|\Psi\rangle$ es la superposición

$$|\Psi\rangle = \alpha |A\rangle + \beta |B\rangle, \qquad \alpha, \beta \in \mathbb{C}. \qquad \text{(4.1)}$$

¿Qué ocurre ahora si medimos la propiedad $Q$ en el sistema descrito por el estado $|\Psi\rangle$? Podría parecer razonable que se obtuviera algún valor intermedio entre $a$ y $b$, pero eso no es lo que ocurre. Una medición de $Q$ dará como resultado $a$ o $b$. No hay una respuesta cierta, el determinismo clásico se pierde, pero la respuesta es siempre uno de estos dos valores y no uno intermedio. Los coeficientes $\alpha$ y $\beta$ en la superposición anterior afectan a las probabilidades con las que podemos obtener los dos valores posibles. De hecho, las probabilidades de obtener $a$ o $b$ son

$$\text{Probabilidad}(a) \sim |\alpha|^2, \qquad \text{Probabilidad}(b) \sim |\beta|^2. \qquad \text{(4.2)}$$

Puesto que las únicas dos posibilidades son medir $a$ o $b$, las probabilidades reales deben sumar uno y, por lo tanto, vienen dadas por

$$\text{Probabilidad}(a) = \frac{|\alpha|^2}{|\alpha|^2 + |\beta|^2}, \qquad \text{Probabilidad}(b) = \frac{|\beta|^2}{|\alpha|^2 + |\beta|^2}. \qquad \text{(4.3)}$$

Si obtenemos el valor $a$, mediciones repetidas inmediatas seguirían dando $a$, por lo que el estado tras la medición debe ser $|A\rangle$. Lo mismo ocurre para $b$, de modo que tenemos

$$\text{Tras medir } a \text{ el estado se convierte en } |\Psi\rangle = |A\rangle,$$

$$\text{Tras medir } b \text{ el estado se convierte en } |\Psi\rangle = |B\rangle. \qquad \text{(4.4)}$$

En mecánica cuántica se hace la siguiente suposición: superponer un estado consigo mismo no cambia la física, ni cambia el estado de manera no trivial. Puesto que superponer un estado consigo mismo simplemente cambia el número global que lo multiplica, tenemos que $\Psi$ y $\alpha\Psi$ representan la misma física para cualquier número complejo $\alpha$ distinto de cero. Así, dejando que $\cong$ represente equivalencia física,

$$|A\rangle \cong 2|A\rangle \cong i|A\rangle \cong -|A\rangle. \qquad \text{(4.5)}$$

Esta suposición es necesaria para verificar que el estado de polarización de un fotón tiene el número esperado de grados de libertad. La polarización de una onda plana, tal como se estudia en electromagnetismo, se describe mediante dos números reales. Para esto, consideremos una onda polarizada elípticamente, como se muestra en la Figura 5. En un punto dado, el vector de campo eléctrico traza una elipse cuya forma queda codificada por la razón $a/b$ de los semiejes (el primer parámetro real) y una inclinación codificada por el ángulo $\theta$ (el segundo parámetro real). Consideremos para ello un estado general de fotón formado por la superposición de los dos estados de polarización independientes $|\text{fotón}; x\rangle$ y $|\text{fotón}; y\rangle$:

$$\alpha|\text{fotón}; x\rangle + \beta|\text{fotón}; y\rangle, \qquad \alpha, \beta \in \mathbb{C}. \qquad \text{(4.6)}$$

A primera vista parece que tenemos dos parámetros complejos $\alpha$ y $\beta$, o de manera equivalente, cuatro parámetros reales. Pero como el factor global no importa, podemos multiplicar este estado por $1/\alpha$ para obtener el estado equivalente que codifica toda la física

$$|\text{fotón}; x\rangle + \frac{\beta}{\alpha}|\text{fotón}; y\rangle, \qquad \text{(4.7)}$$

lo que muestra que en realidad tenemos un único parámetro complejo, la razón $\beta/\alpha$. Esto equivale a dos parámetros reales, como se esperaba.

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes1_ES/fig5.png)

Figura 5: Parámetros que definen un estado polarizado elípticamente.

Hagamos otro ejemplo de superposición usando electrones. Los electrones son partículas con espín. Clásicamente, los imaginamos como pequeñas bolas girando alrededor de un eje que pasa por la propia partícula. Una vez fijado un eje, el electrón tiene dos y solo dos opciones: su rotación puede ser en sentido horario o antihorario alrededor del eje, pero en ambos casos gira a la misma velocidad fija. Estas formas opuestas de girar se llaman espín arriba y espín abajo a lo largo del eje (véase la Figura 6). El arriba y el abajo se refieren a la dirección del momento angular asociado con la rotación, y se indica mediante una flecha. Según la mecánica cuántica, y como se ha verificado en múltiples experimentos, surgen las mismas posibilidades, arriba o abajo, sea cual sea el eje que usemos para medir el espín del electrón.

Los físicos habitualmente configuran sistemas de coordenadas en el espacio eligiendo tres direcciones ortogonales, las direcciones de los ejes $x$, $y$ y $z$. Elijamos describir nuestros electrones con espín usando el eje $z$. Un posible estado de un electrón es tener espín arriba a lo largo del eje $z$. Tal estado se describe como $|\!\uparrow; z\rangle$, con una flecha apuntando hacia arriba, y la etiqueta $z$ indicando que la flecha de espín apunta a lo largo de la dirección creciente de $z$. Otro posible estado de un electrón es espín abajo a lo largo del eje $z$. Tal estado se describe como $|\!\downarrow; z\rangle$, con una flecha apuntando hacia abajo, indicando esta vez que el espín apunta a lo largo de la dirección decreciente de $z$. Si estas dos son realidades posibles, también lo sería el estado $|\Psi\rangle$ que representa la suma

$$|\Psi\rangle = |\!\uparrow; z\rangle + |\!\downarrow; z\rangle.$$

El estado $|\Psi\rangle$ está en una superposición de un estado de espín arriba y uno de espín abajo. ¿Qué tipo de física representa esta suma $|\Psi\rangle$? Representa un estado en el que una medición del espín a lo largo del eje $z$ daría como resultado dos posibles desenlaces con igual probabilidad: un electrón con espín arriba o un electrón con espín abajo. Puesto que solo podemos hablar de probabilidades, cualquier experimento debe implicar repetición hasta que las probabilidades puedan determinarse. Supongamos que tuviéramos un gran conjunto de tales electrones, todos ellos en el estado $|\Psi\rangle$ anterior. Al medir su espín a lo largo de $z$, uno a la vez, encontraríamos que aproximadamente la mitad de ellos giran hacia arriba a lo largo de $z$ y la otra mitad gira hacia abajo a lo largo de $z$. No hay manera de predecir qué opción se realizará al medir cada electrón. No es fácil imaginar la superposición, pero se puede intentar de la siguiente manera. Un electrón en el estado anterior se encuentra en un tipo de existencia diferente en la que es capaz tanto de girar hacia arriba a lo largo de $z$ como de girar hacia abajo a lo largo de $z$ simultáneamente. Se encuentra en un estado fantasmal e inquietante de este tipo, haciendo cosas incompatibles simultáneamente, hasta que se mide su espín. Una vez medido, el electrón debe elegir inmediatamente una de las dos opciones; siempre encontramos electrones girando hacia arriba o girando hacia abajo.

![Figura 6](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes1_ES/fig6.png)

Figura 6: Un electrón con espín a lo largo del eje $z$. Izquierda: se dice que el electrón tiene espín arriba a lo largo de $z$. Derecha: se dice que el electrón tiene espín abajo a lo largo de $z$. Las flechas hacia arriba y hacia abajo representan la dirección del momento angular asociado al electrón que gira.

Un crítico de la mecánica cuántica podría sugerir una explicación más simple para las observaciones anteriores. Él o ella afirmaría que el siguiente conjunto más simple produce resultados experimentales idénticos. En el conjunto del crítico tenemos un gran número de electrones, con el 50% de ellos en el estado $|\!\uparrow; z\rangle$ y el 50% de ellos en el estado $|\!\downarrow; z\rangle$. Entonces afirmaría, correctamente, que tal conjunto produciría las mismas mediciones de espín a lo largo de $z$ que el conjunto de esos esotéricos estados $|\Psi\rangle$. El nuevo conjunto podría ofrecer una explicación más simple del resultado sin tener que invocar superposiciones cuánticas.

La mecánica cuántica, sin embargo, permite otros experimentos que pueden distinguir entre el conjunto de nuestro amigable crítico y el conjunto de estados $|\Psi\rangle$. Aunque nos llevaría demasiado lejos explicarlo, si midiéramos el espín de los electrones en la dirección $x$, en lugar de la dirección $z$, los resultados serían diferentes en los dos conjuntos. En el conjunto de nuestro crítico encontraríamos el 50% de los electrones hacia arriba a lo largo de $x$ y el 50% de los electrones hacia abajo a lo largo de $x$. En nuestro conjunto de estados $|\Psi\rangle$, sin embargo, encontraríamos un resultado muy simple: todos los estados apuntando hacia arriba a lo largo de $x$. El conjunto del crítico no es equivalente a nuestro conjunto mecánico-cuántico. Así, se demuestra que el crítico está equivocado en su intento de mostrar que las superposiciones cuánticas no son necesarias.

## 5. Entrelazamiento

Cuando consideramos la superposición de estados de dos partículas podemos obtener el notable fenómeno llamado entrelazamiento mecánico-cuántico. Los estados entrelazados de dos partículas son aquellos en los que no podemos hablar por separado del estado de cada partícula. Las partículas están ligadas en un estado común en el que están entrelazadas entre sí.

Consideremos dos partículas que no interactúan. La partícula 1 podría estar en cualquiera de los estados

$$\{|u_1\rangle, |u_2\rangle, \ldots\}, \qquad \text{(5.1)}$$

mientras que la partícula 2 podría estar en cualquiera de los estados

$$\{|v_1\rangle, |v_2\rangle, \ldots\} \qquad \text{(5.2)}$$

Podría parecer razonable concluir que el estado del sistema completo, incluyendo la partícula 1 y la partícula 2, quedaría especificado indicando el estado de la partícula 1 y el estado de la partícula 2. Si ese fuera el caso, los posibles estados se escribirían como

$$|u_i\rangle \otimes |v_j\rangle, \qquad i, j \in \mathbb{N}, \qquad \text{(5.3)}$$

para alguna elección específica de $i$ y $j$ que especifican el estado de la partícula uno y de la partícula dos, respectivamente. Aquí hemos usado el símbolo $\otimes$, que significa producto tensorial, para combinar los dos estados en un único estado para todo el sistema. Estudiaremos $\otimes$ más adelante, pero por ahora podemos pensarlo como una especie de producto que se distribuye sobre la suma y obedece reglas simples, tal como sigue

$$(\alpha_1|u_1\rangle + \alpha_2|u_2\rangle) \otimes (\beta_1|v_1\rangle + \beta_2|v_2\rangle) = \alpha_1\beta_1 |u_1\rangle\otimes|v_1\rangle + \alpha_1\beta_2 |u_1\rangle\otimes|v_2\rangle$$

$$+ \alpha_2\beta_1 |u_2\rangle\otimes|v_1\rangle + \alpha_2\beta_2 |u_2\rangle\otimes|v_2\rangle. \qquad \text{(5.4)}$$

Los números pueden desplazarse a través del $\otimes$, pero el orden de los estados debe conservarse. El estado del lado izquierdo —desarrollado en el lado derecho— sigue siendo del tipo en el que combinamos un estado de la primera partícula $(\alpha_1|u_1\rangle + \alpha_2|u_2\rangle)$ con un estado de la segunda partícula $(\beta_1|v_1\rangle + \beta_2|v_2\rangle)$. Al igual que cualquiera de los estados listados en (5.3), este estado no está entrelazado.

Usando los estados en (5.3), sin embargo, podemos construir superposiciones más intrigantes. Consideremos la siguiente

$$|u_1\rangle \otimes |v_1\rangle + |u_2\rangle \otimes |v_2\rangle. \qquad \text{(5.5)}$$

Se dice que un estado de dos partículas está entrelazado si no puede escribirse en la forma factorizada $(\cdots)\otimes(\cdots)$, que nos permitiría describir el estado simplemente indicando el estado de cada partícula. Podemos ver fácilmente que el estado (5.5) no puede factorizarse. Si pudiera, tendría que ser con un producto como el indicado en (5.4). Claramente, involucrar estados como $|u_3\rangle$ o $|v_3\rangle$ que no aparecen en (5.5) no ayudaría. Para determinar las constantes $\alpha_1, \alpha_2, \beta_1, \beta_2$ comparamos el lado derecho de (5.4) con nuestro estado y concluimos que necesitamos

$$\alpha_1\beta_1 = 1, \quad \alpha_1\beta_2 = 0, \quad \alpha_2\beta_1 = 0, \quad \alpha_2\beta_2 = 1. \qquad \text{(5.6)}$$

Está claro que no hay solución aquí. La segunda ecuación, por ejemplo, requiere que $\alpha_1$ o $\beta_2$ sean cero. Tener $\alpha_1 = 0$ contradice la primera ecuación, y tener $\beta_2 = 0$ contradice la última ecuación. Esto confirma que el estado (5.5) es, en efecto, un estado entrelazado. No hay manera de describir el estado especificando un estado para cada una de las partículas.

Ilustremos la discusión anterior usando electrones y sus estados de espín. Consideremos un estado de dos electrones denotado como $|\!\uparrow\rangle \otimes |\!\downarrow\rangle$. Como indica la notación, el primer electrón, descrito por la primera flecha, está hacia arriba a lo largo de $z$, mientras que el segundo electrón, descrito por la segunda flecha, está hacia abajo a lo largo de $z$ (omitimos la etiqueta $z$ en el estado por brevedad). Este no es un estado entrelazado. Otro estado posible es aquel en el que hacen exactamente lo contrario: en $|\!\downarrow\rangle \otimes |\!\uparrow\rangle$ el primer electrón está hacia abajo y el segundo está hacia arriba. Este segundo estado tampoco está entrelazado. Se sigue entonces que, por superposición, podemos considerar el estado

$$|\!\uparrow\rangle \otimes |\!\downarrow\rangle + |\!\downarrow\rangle \otimes |\!\uparrow\rangle. \qquad \text{(5.7)}$$

Este es un estado entrelazado del par de electrones.

**Ejercicio.** Demuestre que el estado anterior no puede factorizarse y, por lo tanto, está efectivamente entrelazado.

En el estado (5.7), el primer electrón está hacia arriba a lo largo de $z$ si el segundo electrón está hacia abajo a lo largo de $z$ (primer término), o el primer electrón está hacia abajo a lo largo de $z$ si el segundo electrón está hacia arriba a lo largo de $z$ (segundo término). Hay una correlación entre los espines de las dos partículas; siempre apuntan en direcciones opuestas. Imaginemos que los dos electrones entrelazados están muy lejos el uno del otro: Alicia tiene un electrón del par en el planeta Tierra y Roberto tiene el otro electrón en la Luna. Nada de lo que conocemos conecta estas partículas, pero, sin embargo, los estados de los electrones están vinculados. Las mediciones que hacemos sobre las partículas separadas exhiben correlaciones. Supongamos que Alicia mide el espín del electrón en la Tierra. Si lo encuentra hacia arriba a lo largo de $z$, significa que se realiza el primer sumando de la superposición anterior, porque en ese sumando la primera partícula está hacia arriba. Como se discutió antes, el estado de las dos partículas se convierte inmediatamente en el del primer sumando. Esto significa que el electrón en la Luna pasará instantáneamente a la configuración de espín hacia abajo a lo largo de $z$, algo que podría confirmar Roberto, que está sentado en la Luna con esa partícula en su laboratorio. Este efecto sobre el electrón de Roberto ocurre antes de que un mensaje, transportado a la velocidad de la luz, pudiera llegar a la Luna informándole de que Alicia ha realizado una medición sobre la partícula terrestre y que el resultado fue espín hacia arriba. Por supuesto, los experimentos deben realizarse con un conjunto que contenga muchos pares de partículas, cada par en el mismo estado entrelazado anterior. La mitad de las veces el electrón en la Tierra se encontrará hacia arriba, con el electrón en la Luna hacia abajo, y la otra mitad de las veces el electrón en la Tierra se encontrará hacia abajo, con el electrón en la Luna hacia arriba.

Nuestro amigable crítico podría decir ahora, correctamente, que tales correlaciones entre las mediciones de espín a lo largo de $z$ podrían haberse producido preparando un conjunto convencional en el que el 50% de los pares están en el estado $|\!\uparrow\rangle \otimes |\!\downarrow\rangle$ y el otro 50% de los pares están en el estado $|\!\downarrow\rangle \otimes |\!\uparrow\rangle$. Tales objeciones fueron resueltas de manera concluyente en 1964 por John Bell, quien demostró que si Alicia y Roberto son capaces de medir el espín en tres direcciones arbitrarias, las correlaciones predichas por el estado cuántico entrelazado son diferentes de las correlaciones clásicas de cualquier conjunto convencional concebible. Las correlaciones cuánticas en estados entrelazados son muy sutiles y se necesitan experimentos sofisticados para mostrar que no son reproducibles como correlaciones clásicas. En efecto, los experimentos con estados entrelazados han confirmado la existencia de correlaciones cuánticas. El tipo de acción instantánea a distancia asociado con las mediciones sobre partículas entrelazadas bien separadas no conduce a paradojas ni, como podría parecer, a contradicciones con las ideas de la relatividad especial. No se pueden usar estados entrelazados mecánico-cuánticos para enviar información más rápido que la velocidad de la luz.

------------------------------------------------------------------------

*Sarah Geller transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

*Traducción al español generada con asistencia de IA a partir del original en inglés.*

------------------------------------------------------------------------

MIT OpenCourseWare

<https://ocw.mit.edu>

8.04 Física Cuántica I

Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.
