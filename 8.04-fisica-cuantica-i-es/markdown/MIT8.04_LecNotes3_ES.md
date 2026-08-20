# Naturaleza corpuscular de la luz y naturaleza ondulatoria de la materia

## Vídeos de esta clase (YouTube)

**Lección 3: Photoelectric effect, Compton scattering, and de Broglie wavelength.**

- [The photoelectric effect](https://www.youtube.com/watch?v=byEaU9ILHmw)
- [Units of h and Compton wavelength of particles](https://www.youtube.com/watch?v=S9RjSQro2e0)
- [Compton Scattering](https://www.youtube.com/watch?v=WR88_Vzfcx4)
- [de Broglie’s proposal](https://www.youtube.com/watch?v=dnuZx9fZHsU)

------------------------------------------------------------------------

*B. Zwiebach* *16 de febrero de 2016*

## Contenido

1.  Efecto fotoeléctrico
2.  Dispersión de Compton
3.  Ondas de materia

## 1. Efecto fotoeléctrico

El efecto fotoeléctrico fue observado por primera vez por Heinrich Hertz en 1887. Cuando se irradian placas metálicas pulidas, observó, estas pueden emitir electrones, entonces llamados “foto-electrones”. Los electrones emitidos producen así una corriente fotoeléctrica. Las observaciones clave fueron:

- Existe una frecuencia umbral $\nu_0$. Solo para frecuencias $\nu > \nu_0$ hay corriente fotoeléctrica. La frecuencia $\nu_0$ depende del metal y de la configuración de los átomos en la superficie. También se ve afectada por las inhomogeneidades.

- La magnitud de la corriente fotoeléctrica es proporcional a la intensidad de la fuente de luz.

- La energía de los fotoelectrones es independiente de la intensidad de la fuente de luz.

Una explicación natural de las características de este efecto no llegó hasta 1905, cuando Einstein explicó las propiedades anteriores postulando que la energía de la luz es transportada por cuantos discretos (llamados posteriormente fotones) con energía $h\nu$. Aquí $h$ es la constante de Planck, la constante que Planck utilizó para ajustar la energía del cuerpo negro en función de la frecuencia.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes3_ES/fig1.png)

Figura 1: Los electrones en un metal están ligados. Si la energía del fotón es mayor que la función de trabajo $W$, un electrón puede ser expulsado.

Un material dado tiene una energía característica $W$, llamada función de trabajo, que es la energía mínima requerida para expulsar un electrón. Esta no es fácil de calcular porque es el resultado de la interacción de muchos electrones con el trasfondo de átomos. Sin embargo, es fácil de medir. Cuando se irradia la superficie del material, los electrones del material absorben la energía de los fotones incidentes. Si la energía impartida a un electrón por la absorción de un solo fotón es mayor que la función de trabajo $W$, entonces el electrón es expulsado con energía cinética $E_{e^-}$ igual a la diferencia entre la energía del fotón y la función de trabajo:

$$E_{e^-} = \frac{1}{2}mv^2 = h\nu - W = E_\gamma - W. \qquad \text{(1.1)}$$

Esta ecuación, escrita por Einstein, explica las características experimentales señaladas anteriormente, una vez que suponemos que los cuantos actúan sobre electrones individuales para expulsarlos. La frecuencia umbral se define mediante

$$h\nu_0 = W, \qquad \text{(1.2)}$$

ya que da lugar a un fotoelectrón con energía cero. Para $\nu > \nu_0$ los electrones serán expulsados. Aumentar la intensidad de la fuente de luz incrementa la tasa de llegada de fotones, lo cual incrementará la magnitud de la corriente, pero no cambiará la energía de los fotoelectrones porque no cambia la energía de cada cuanto incidente.

La ecuación (1.2) permitió a Einstein hacer una predicción: la energía cinética de los fotoelectrones aumenta linealmente con la frecuencia de la luz. La predicción de Einstein fue confirmada experimentalmente por Millikan (1915), quien midió cuidadosamente las energías de los fotoelectrones y confirmó su dependencia lineal con la energía. El cuidadoso trabajo de Millikan le permitió determinar el valor de la constante de Planck $\hbar$ con una precisión mejor que el 1%. Aun así, persistía el escepticismo y los físicos todavía no estaban convencidos de la naturaleza corpuscular de estos cuantos de luz.

**Ejemplo:** Considere luz ultravioleta con longitud de onda $\lambda = 290\,\text{nm}$ incidente sobre un metal con función de trabajo $W = 4.05\,\text{eV}$. ¿Cuál es la energía del fotoelectrón y cuál es su velocidad?

**Solución:** Es útil resolver estos problemas sin tener que buscar constantes. Para ello, conviene recordar esta relación útil

$$\hbar c = 197.33\ \text{MeV·fm}, \qquad \hbar \equiv \frac{h}{2\pi}, \qquad \text{(1.3)}$$

donde $\text{MeV} = 10^6\,\text{eV}$ y $\text{fm} = 10^{-15}\,\text{m}$. Usemos esto para calcular la energía del fotón. En este caso,

$$E_\gamma = h\nu = \frac{2\pi\hbar c}{\lambda} = \frac{2\pi \cdot 197.33\ \text{MeV·fm}}{290 \times 10^{-9}\,\text{m}} = \frac{2\pi \cdot 197.33}{290}\ \text{eV} \approx 4.28\ \text{eV}, \qquad \text{(1.4)}$$

y por tanto

$$E_{e^-} = E_\gamma - W = 0.23\ \text{eV}. \qquad \text{(1.5)}$$

Para calcular la energía escribimos

$$0.23\ \text{eV} = \frac{1}{2}m_e v^2 = \frac{1}{2}(m_e c^2)\left(\frac{v}{c}\right)^2 \qquad \text{(1.6)}$$

Recordando que $m_e c^2 \simeq 511{,}000\ \text{eV}$ se obtiene

$$\frac{0.46}{511000} = \left(\frac{v}{c}\right)^2 \quad \Rightarrow \quad \frac{v}{c} = 0.0009488. \qquad \text{(1.7)}$$

Con $c = 300{,}000\ \text{Km/s}$ finalmente obtenemos $v \simeq 284.4\ \text{Km/s}$.

Este es un buen momento para considerar las unidades, en particular las unidades de $h$. Podemos preguntarnos: ¿existe una cantidad física que tenga las unidades de $h$? La respuesta es sí, como veremos ahora. De la ecuación $E = h\nu$, tenemos

$$[h] = \frac{[E]}{[\nu]} = \frac{ML^2/T^2}{1/T} = L \cdot M\frac{L}{T}, \qquad \text{(1.8)}$$

donde $[\cdot]$ da las unidades de una cantidad, y $M$, $L$, $T$ son las unidades de masa, longitud y tiempo, respectivamente. Hemos escrito la expresión más a la derecha como un producto de unidades de longitud y momento. Por lo tanto

$$[h] = [r \times p] = [L]. \qquad \text{(1.9)}$$

¡Vemos que $h$ tiene unidades de momento angular! De hecho, para una partícula de espín un medio, la magnitud del momento angular de espín es $\frac{1}{2}\hbar$.

Con $[h] = [r][p]$ vemos también que se tiene una manera canónica de asociar una longitud a cualquier partícula de una masa dada $m$. En efecto, usando la velocidad de la luz, podemos construir el momento $p = mc$, y entonces la longitud $\ell$ se obtiene de la razón $h/p$. Esta es de hecho la longitud de onda Compton $\lambda_C$ de una partícula:

$$\lambda_C = \frac{h}{mc} \qquad \text{(1.10)}$$

que tiene unidades de longitud; esto se llama la longitud de onda Compton de una partícula de masa $m$. Nótese que esta longitud es independiente de la velocidad de la partícula. ¡La longitud de onda de de Broglie de la partícula usa el momento verdadero de la partícula, no $mc$! Por lo tanto, las longitudes de onda Compton y de de Broglie no deben confundirse.

Es posible obtener cierta intuición física para la longitud de onda Compton $\lambda_C$ de una partícula. Afirmamos que $\lambda_C$ es la longitud de onda de un fotón cuya energía es igual a la energía en reposo de la partícula. En efecto, tendríamos

$$mc^2 = h\nu = h\frac{c}{\lambda} \quad \Rightarrow \quad \lambda = \frac{h}{mc}, \qquad \text{(1.11)}$$

confirmando la afirmación. Supongamos que se intenta localizar una partícula puntual de masa $m$. Si se usa luz, la precisión posible en la posición de la partícula es aproximadamente la longitud de onda de la luz. Una vez que usamos luz con $\lambda < \lambda_C$, los fotones transportan más energía que la energía en reposo de la partícula. Es posible entonces que la energía de los fotones se convierta en la creación de más partículas de masa $m$, dificultando, si no imposibilitando, la localización de la partícula. La longitud de onda Compton es la escala de longitud en la cual necesitamos la teoría cuántica de campos relativista para tomar en cuenta los posibles procesos de creación y aniquilación de partículas.

Calculemos la longitud de onda Compton del electrón:

$$\lambda_C(e) = \frac{h}{m_e c} = \frac{2\pi\hbar c}{m_e c^2} = \frac{2\pi \cdot 197.33\ \text{MeV·fm}}{0.511\ \text{MeV}} = 2426\ \text{fm} = 2.426\ \text{pm}. \qquad \text{(1.12)}$$

Esta longitud es unas 20 veces más pequeña que el radio de Bohr (53 pm) y unas dos mil veces el tamaño de un protón (1 fm). La longitud de onda Compton del electrón aparece en la fórmula del cambio de longitud de onda del fotón en el proceso llamado dispersión de Compton.

## 2. Dispersión de Compton

Originalmente Einstein no dejó claro que el cuanto de luz significara una partícula de luz. En 1916, sin embargo, postuló que el cuanto transportaría también momento además de energía, dejando el caso mucho más claro a favor de una partícula. En relatividad, la energía, el momento y la masa en reposo de una partícula están relacionados mediante

$$E^2 - p^2 c^2 = m^2 c^4. \qquad \text{(2.13)}$$

(Compárese esto con la ecuación clásica $E = p^2/2m$.) Por supuesto, también se pueden expresar la energía y el momento de la partícula en términos de la velocidad:

$$E = \frac{mc^2}{\sqrt{1 - \frac{v^2}{c^2}}}, \qquad p = \frac{mv}{\sqrt{1 - \frac{v^2}{c^2}}}. \qquad \text{(2.14)}$$

Debería usar estas expresiones para confirmar que (2.13) se cumple (donde $|\vec{p}| = p$). Una partícula que se mueve con la velocidad de la luz, como el fotón, debe tener masa en reposo nula, ya que de lo contrario su energía y momento serían infinitos debido a los denominadores que se anulan. Con la masa en reposo fijada en cero, la ecuación (2.13) da la relación entre la energía del fotón $E_\gamma$ y el momento del fotón $p_\gamma$:

$$E_\gamma = p_\gamma c. \qquad \text{(2.15)}$$

Luego, usando $\lambda\nu = c$, llegamos a

$$p_\gamma = \frac{E_\gamma}{c} = \frac{h\nu}{c} = \frac{h}{\lambda}. \qquad \text{(2.16)}$$

Volveremos a ver esta relación más adelante cuando discutamos las ondas de materia.

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes3_ES/fig2.png)

Figura 2: Luz no polarizada incidente sobre un electrón se dispersa en un ángulo $\theta$. Clásicamente, esto se describe mediante la dispersión de Thomson. La luz no cambia de frecuencia durante este proceso.

Compton llevó a cabo experimentos (1923–1924) dispersando rayos X en un blanco de carbono. Los rayos X corresponden a energías de fotón en el rango de 100 eV a 100 KeV. El objetivo era dispersar fotones de rayos X en electrones libres, y con cierta salvedad, los electrones en los átomos se comportan de esa manera.

La contraparte clásica del experimento de Compton es la dispersión de ondas electromagnéticas en electrones libres, llamada dispersión de Thomson. Aquí una onda electromagnética incide sobre un electrón. El campo eléctrico de la onda sacude al electrón, que oscila con la frecuencia del campo incidente. La oscilación del electrón produce un campo radiado, de la misma frecuencia que la radiación incidente. En la dispersión de Thomson clásica, la sección eficaz diferencial de dispersión viene dada por

$$\frac{d\sigma}{d\Omega} = \left(\frac{e^2}{mc^2}\right)^2 \frac{1}{2}\left(1 + \cos^2\theta\right), \qquad \text{(2.17)}$$

donde $\theta$ es el ángulo entre la onda incidente y la onda dispersada, con la energía radiada a la misma frecuencia que la luz incidente. Esto se muestra en la Figura 2. La sección eficaz tiene unidades de longitud al cuadrado, o área, como debe ser. Representa el área que extraería de la onda plana incidente la cantidad de energía que dispersa el electrón. En efecto, la cantidad $e^2/(mc^2)$ se llama el radio clásico del electrón y es de aproximadamente 2.8 fm, ¡no mucho más grande que un protón!

Si tratamos la luz como fotones, el proceso elemental que ocurre es una colisión entre dos partículas: un fotón incidente y un electrón aproximadamente estacionario. Se pueden demostrar rápidamente dos hechos:

- El fotón no puede ser absorbido por el electrón. Esto es inconsistente con la conservación de energía y momento (ejercicio).

- El fotón debe perder algo de energía y por lo tanto la longitud de onda final del fotón $\lambda_f$ debe ser mayor que la longitud de onda inicial del fotón $\lambda_i$. Esto es claro en el sistema de referencia del laboratorio, donde el electrón inicialmente estacionario debe retroceder y así adquirir cierta energía cinética.

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes3_ES/fig3.png)

Figura 3: Los resultados del experimento de dispersión de Compton. La longitud de onda del fotón incidente es $\lambda_i$, y la longitud de onda del fotón dispersado es $\lambda_f \simeq \lambda_i + \ell_C$, correspondiente a $\theta = 90°$.

En efecto, las observaciones de Compton no concordaban con las predicciones de la dispersión de Thomson: los rayos X cambiaban de frecuencia tras la dispersión. Un cálculo usando la conservación de energía y momento muestra que el cambio de longitud de onda está correlacionado con el ángulo entre el fotón dispersado y el fotón original:

$$\lambda_f = \lambda_i + \frac{h}{m_e c}(1 - \cos\theta) = \lambda_i + \lambda_C(1 - \cos\theta). \qquad \text{(2.18)}$$

Nótese la aparición de la longitud de onda Compton del electrón, la partícula de la cual dispersa el fotón. La pérdida máxima de energía para el fotón ocurre en $\theta = \pi$, donde

$$\lambda_f(\theta = 180°) = \lambda_i + 2\lambda_C. \qquad \text{(2.19)}$$

El cambio máximo posible de longitud de onda es $2\lambda_C$. Para $\theta = \frac{\pi}{2}$ el cambio de longitud de onda es exactamente $\lambda_C$

$$\lambda_f(\theta = 90°) = \lambda_i + \lambda_C. \qquad \text{(2.20)}$$

El experimento de Compton usó rayos X de molibdeno con energía y longitud de onda

$$E_\gamma \approx 17.5\ \text{keV}, \qquad \lambda_i = 0.0709\ \text{nm}, \qquad \text{(2.21)}$$

incidiendo sobre un blanco de carbono. Colocando el detector en un ángulo $\theta = 90°$, la gráfica de la intensidad (o número de fotones dispersados) en función de la longitud de onda se muestra en la Figura 2. Se encuentra un pico para $\lambda_f = 0.0731\ \text{nm}$, pero también un segundo pico en la longitud de onda original $\lambda_i = 0.0709\ \text{nm}$.

El pico en $\lambda_f$ es el esperado: $\lambda_f - \lambda_i \simeq 2.2\ \text{pm}$, que es aproximadamente la longitud de onda Compton de 2.4 pm. Dado que los fotones tienen energías de 17 KeV y las energías de los estados ligados del carbono son de aproximadamente 300 eV, el pico esperado representa instancias en las que el átomo es ionizado por la colisión y es una buena aproximación considerar los electrones expulsados. El pico en $\lambda_i$ representa un proceso en el que un electrón recibe algo de momento del fotón pero permanece ligado. Esto no es muy improbable: el momento típico de un electrón ligado es en realidad comparable al momento del fotón. En este caso el fotón se dispersa a 90° y el momento de retroceso lo lleva todo el átomo. La longitud de onda Compton relevante es entonces la del átomo. Dado que la masa del átomo de carbono es varios miles de veces mayor que la masa del electrón, la longitud de onda Compton del átomo es mucho menor que la longitud de onda Compton del electrón y no debería haber cambio detectable en la longitud de onda del fotón.[1]

## 3. Ondas de materia

Como hemos visto, la luz se comporta tanto como partícula como onda. Este tipo de comportamiento se suele denominar dualidad: la realidad completa del objeto se captura usando tanto las características ondulatorias como las corpusculares del objeto. El fotón es una partícula de energía $E_\gamma$, pero tiene frecuencia $\nu$, que es un atributo ondulatorio, con $E = h\nu$. Es una partícula con momento $p_\gamma$ pero también tiene una longitud de onda $\lambda$, un atributo ondulatorio, dado por (2.16)

$$\lambda = \frac{h}{p_\gamma}. \qquad \text{(3.22)}$$

En 1924, Louis de Broglie propuso que la dualidad onda/partícula del fotón era universal, y por lo tanto válida también para las partículas materiales. De esta manera conjeturó la naturaleza ondulatoria de la materia. Inspirado por (3.22), de Broglie postuló que, asociada a una partícula material con momento $p$, existe una onda plana de longitud de onda $\lambda$ dada por

$$\lambda = \frac{h}{p}. \qquad \text{(3.23)}$$

Esta es una propiedad plenamente cuántica: si $h \to 0$, entonces $\lambda \to 0$, y las partículas no tienen propiedades ondulatorias. Una consecuencia interesante de esto es que las partículas materiales pueden difractarse o interferir. En el famoso experimento de Davisson-Germer (1927), los electrones inciden sobre una superficie metálica y se encuentra que a ciertos ángulos hay picos en la intensidad de los electrones dispersados. Los picos mostraban el efecto de interferencia constructiva de la dispersión en la red de átomos del metal, demostrando la naturaleza ondulatoria de los electrones. También se puede hacer interferencia de doble rendija con electrones, y el experimento se puede realizar disparando un electrón a la vez. Un experimento reciente \[arXiv:1310.8343\] de Eibenberger et al. reporta interferencia usando moléculas con 810 átomos y una masa que excede las 10 000 uma (¡eso es 20 millones de veces la masa del electrón!).

La longitud de onda de de Broglie se puede calcular para estimar si los efectos cuánticos son importantes. Considere para este propósito una partícula de masa $m$ y momento $p$ incidente sobre un objeto de tamaño $x$, como se ilustra en la Figura 3. Sea $\lambda = h/p$ la longitud de onda de de Broglie de la partícula. La naturaleza ondulatoria de la partícula no es importante si $\lambda$ es mucho menor que $x$. Así, la “aproximación clásica”, en la que los efectos ondulatorios son despreciables, requiere

$$\text{Efectos ondulatorios despreciables:} \quad \frac{\lambda}{x} \ll 1. \qquad \text{(3.24)}$$

Usando $\lambda = h/p$, esto da

$$\text{Efectos ondulatorios despreciables:} \quad xp \gg h, \qquad \text{(3.25)}$$

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes3_ES/fig4.png)

Figura 4: Una partícula de momento $p$ incidente sobre un obstáculo de tamaño $x$.

una relación en la que ambos lados tienen unidades de momento angular.

El comportamiento clásico es un límite sutil de la mecánica cuántica: un campo electromagnético clásico requiere un gran número de fotones. Sin embargo, cualquier estado con un número exacto y fijo de fotones, incluso si es grande, no es clásico. Los estados electromagnéticos clásicos son los llamados estados coherentes, en los que el número de fotones fluctúa.

------------------------------------------------------------------------

Andrew Turner transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.

------------------------------------------------------------------------

MIT OpenCourseWare https://ocw.mit.edu

8.04 Física Cuántica I Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

# Apéndice: Lista de problemas 1 (Problem Set 1, 2016)

**Física Cuántica I (8.04), Primavera de 2016** **Tarea 1**

*Instituto Tecnológico de Massachusetts* *Departamento de Física* *4 de febrero de 2016*

*Fecha de entrega: jueves, 11 de febrero de 2016, 5:00pm*

**Avisos**

- Por favor, ponga su nombre y el número de su sección en la parte superior de su lista de problemas, y colóquela en la casilla de 8.05 etiquetada con el número de su sección cerca de 8-395 antes de las 5:00pm.

- Puede resultarle entretenido leer las primeras páginas del libro de Dirac sobre Mecánica Cuántica.

## Problema 1

**Colapso radiativo de un átomo clásico.** \[10 puntos\]

En un universo clásico, podríamos intentar construir un átomo de hidrógeno colocando un electrón en una órbita circular alrededor de un protón. Sabemos, sin embargo, que un electrón no relativista y acelerado radia energía a una tasa dada por la fórmula de Larmor:

$$\frac{dE}{dt} = -\frac{2}{3}\frac{e^2 a^2}{c^3}.$$

Aquí $e$ es la carga del electrón y $a$ es la magnitud de la aceleración del electrón. Así que el átomo clásico puede tener un problema de estabilidad. Queremos averiguar cuán grande es este efecto. En las unidades con las que trabajamos, la energía potencial del electrón en presencia del protón es $V = -e^2/r$ y la magnitud de la fuerza de atracción es $e^2/r^2$.

1.  Demuestre que, para un electrón no relativista, la energía $\Delta E$ perdida por revolución es pequeña comparada con la energía cinética $K$ del electrón. Hágalo calculando el cociente $\Delta E/K$. Por lo tanto, es posible considerar la órbita como circular en cualquier instante, aunque el electrón acabe cayendo en espiral hacia el protón.

2.  Una buena estimación del tamaño del átomo de hidrógeno es 50 pm (pico-metros), y una buena estimación del tamaño del núcleo es 1 fm (femto-metro). Compare la velocidad del electrón calculada clásicamente con la velocidad de la luz para un radio orbital de 50 pm, 1 pm y 1 fm.

3.  Calcule cuánto tiempo tardaría el electrón en caer en espiral desde 50 pm hasta 1 pm. ¿Está justificado ignorar las correcciones relativistas? ¿Cambiaría mucho la respuesta usando la aproximación no relativista para una espiral desde 50 pm hasta 1 fm?

4.  A medida que el electrón se aproxima al protón, ¿qué le ocurre a su energía? ¿Existe un valor mínimo de la energía que puede tener el electrón?

## Problema 2

**Energías cuantizadas.** \[5 puntos\]

Considere un electrón en movimiento circular alrededor de un protón fijo (pesado) como modelo del átomo de hidrógeno. Sea $V = -e^2/r$ la energía potencial del electrón.

1.  Suponiendo una órbita circular, encuentre las relaciones entre la energía cinética $K$ del electrón, su energía potencial $V$ y la energía total $E$.

2.  Suponga que la magnitud $L$ del momento angular del electrón está cuantizada y es igual a $n\hbar$, donde $n$ es un entero positivo. Encuentre los valores cuantizados $E_n$ de la energía total y los radios orbitales asociados $r_n$. Exprese sus respuestas en términos de $n$, la energía en reposo $E_e = m_e c^2$ del electrón, su longitud de onda Compton $\bar\lambda = \dfrac{\hbar}{m_e c}$, y la constante de estructura fina $\alpha = \dfrac{e^2}{\hbar c}$.

## Problema 3

**Relaciones de De Broglie y la escala de los efectos cuánticos.** \[10 puntos\]

**(a) Partículas materiales como ondas**

Si se puede asociar una longitud de onda a toda partícula en movimiento, ¿por qué no somos forzosamente conscientes de esta propiedad en nuestra experiencia cotidiana? Para responder, calcule la longitud de onda de de Broglie $\lambda = h/p$ (con $h = 6.6 \times 10^{-34}\ \text{J·s}$) de cada una de las siguientes partículas:

1.  un automóvil de masa 2000 kg que viaja a una velocidad de 50 mph (22 m/s)

2.  una canica de masa 10 g que se mueve con una velocidad de 10 cm/s

3.  una partícula de humo de 100 nm de diámetro y masa 1 fg agitada por moléculas de aire a temperatura ambiente ($T = 300\,\text{K}$) (suponga que la partícula tiene la misma energía cinética de traslación que el promedio térmico de las moléculas de aire, $KE = \frac{3}{2}k_B T$, con $k_B = 1.38 \times 10^{-23}\ \text{J/K}$)

4.  un átomo de $^{87}\text{Rb}$ enfriado por láser hasta una temperatura de $T = 100\,\mu\text{K}$. De nuevo, suponga $KE = \frac{3}{2}k_B T$.

**(b) Ondas de luz como partículas**

El efecto fotoeléctrico sugiere que la luz de frecuencia $\nu$ puede considerarse formada por fotones de energía $E = h\nu$, con $h = 6.6 \times 10^{-34}\ \text{J·s}$.

1.  La luz visible tiene una longitud de onda en el rango de 400-700 nm. ¿Cuáles son la energía y la frecuencia de un fotón de luz visible?

2.  El microondas de mi cocina funciona aproximadamente a 2.5 GHz con una potencia máxima de 300 W. ¿Cuántos fotones por segundo puede emitir? ¿Y un láser de baja potencia (10 mW a 633 nm), o un teléfono móvil (0.25 W a 850 MHz)?

3.  ¿Cuántos fotones de microondas de ese tipo hacen falta para calentar 200 ml de agua en 10 °C? (La capacidad calorífica del agua es aproximadamente 4 J/g·K, y la densidad es 1 g/ml.)

4.  Para una potencia dada de una onda electromagnética, ¿espera que una descripción de onda clásica funcione mejor para frecuencias de radio, o para rayos X?

## Problema 4

**Práctica con números complejos.** \[15 puntos\]

Un número complejo puede escribirse tanto en forma cartesiana como en forma polar

$$z = a + ib = r e^{i\theta}, \qquad |z| \equiv \sqrt{a^2 + b^2}.$$

Los números reales $a$ y $b$ son, respectivamente, la parte real y la parte imaginaria de $z$. Los números reales $r$ y $\theta$ son, respectivamente, la magnitud y la fase de $z$. Llamamos a $|z|$ la norma de $z$. Use esta definición de $z$ en lo que sigue:

1.  Use desarrollos de Taylor para derivar la fórmula de Euler

$$e^{i\theta} = \cos\theta + i\sin\theta.$$

1.  Escriba $a$ y $b$ en términos de $r$ y $\theta$, y viceversa.

2.  Los números complejos se ven como vectores en un “plano complejo” bidimensional. La multiplicación de un número complejo por una fase (un número complejo de magnitud unidad) equivale a una rotación en el plano complejo.

<!-- -->

1.  Demuestre que la multiplicación por $i$ equivale a una rotación de 90°: $iz = r e^{i(\theta + \pi/2)}$.

2.  Escriba $iz$ en términos de $a$ y $b$. ¿Cuál es la parte real de $iz$?

3.  Demuestre que la multiplicación por $e^{i\phi}$ equivale a una rotación en $\phi$.

<!-- -->

1.  El conjugado complejo $z^*$ de un número complejo $z = a + ib$ es $z^* = a - ib$. Un número complejo $z$ es realmente real si $z = z^*$, lo que significa que su parte imaginaria es cero. Un número complejo $z$ es realmente imaginario si $z = -z^*$, lo que implica que su parte real es cero.

<!-- -->

1.  ¿Existe un número que sea a la vez real y puramente imaginario?

2.  ¿Qué es $(z^*)^*$? Demuestre que $z^* = r e^{-i\theta}$.

3.  Exprese la parte real y la parte imaginaria de $z$ en términos de $z$ y $z^*$.

4.  Demuestre que $zz^*$ es real y evalúelo para expresarlo en términos de $a$ y $b$, en términos de $r$, y en términos de $|z|$.

<!-- -->

1.  Usando la fórmula de Euler, derive fórmulas para $\cos 2\theta$, $\sin 2\theta$, $\cos 3\theta$ y $\sin 3\theta$, todas en términos de $\sin\theta$ y $\cos\theta$. Derive fórmulas para $\cos(A+B)$ y $\sin(A+B)$, ambas en términos de senos y cosenos de $A$ y $B$.

## Problema 5

**¿Absorción?** \[5 puntos\]

Un fotón colisiona con un electrón libre. Explique por qué el fotón no puede ser absorbido por completo.

## Problema 6

**Interferómetro de Mach-Zehnder.** \[10 puntos\]

Considere el interferómetro de Mach-Zehnder y suponga un haz de entrada de la forma $\begin{pmatrix}\alpha\\ \beta\end{pmatrix}$. Llame $P_0$ y $P_1$ a las probabilidades de detección en $D_0$ y $D_1$.

1.  Calcule $P_0$ y $P_1$ suponiendo que insertamos un desfasador con fase $\delta_l$ en el brazo inferior del interferómetro.

2.  Calcule $P_0$ y $P_1$ suponiendo que insertamos un desfasador con fase $\delta_u$ en el brazo superior del interferómetro.

3.  Calcule $P_0$ y $P_1$ suponiendo que insertamos los dos desfasadores simultáneamente.

## Problema 7

**¡Bombas de Elitzur-Vaidman!** \[10 puntos\]

1.  Suponga que decide probar bombas con un interferómetro de Mach-Zehnder repetidamente hasta que el estado de una bomba dada sea cierto más allá de toda duda razonable. ¿Qué fracción de las bombas que funcionan se certifica sin detonación?

2.  Suponga que el 80% de las bombas en su posesión son defectuosas. Elige una al azar y la prueba con un interferómetro de Mach-Zehnder enviando un fotón. Detecta el fotón en $D_0$. ¿Cuál es la probabilidad de que la bomba sea defectuosa?

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*

[1] Gracias a V. Vuletic por una aclaración sobre este punto.
