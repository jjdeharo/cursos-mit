# Teorema de Levinson y Resonancias

## Vídeos de esta clase (YouTube)

**Lección 19: Resonances and Breit-Wigner distribution. The complex k-plane.**

- [Time delay and resonances](https://www.youtube.com/watch?v=mnvYIEbJXlM)
- [Effects of resonance on phase shifts, wave amplitude and time delay](https://www.youtube.com/watch?v=VY-_xLxHQbA)
- [Modelling a resonance](https://www.youtube.com/watch?v=8Dxo4LPK_9w)
- [Half-width and time delay](https://www.youtube.com/watch?v=OQMczXtDnpU)
- [Resonances in the complex k plane](https://www.youtube.com/watch?v=0T83-47Vi-M)

------------------------------------------------------------------------

*B. Zwiebach* *28 de abril de 2016*

## 1. El teorema de Levinson

El teorema de Levinson relaciona el número $N_b$ de estados ligados de un potencial dado con la excursión del desfasaje $\delta(E)$ a medida que la energía va de cero a infinito:

$$N_b = \frac{1}{\pi}\left(\delta(0) - \delta(\infty)\right) . \qquad \text{(1.1)}$$

Para demostrar este resultado consideremos un potencial arbitrario $V(x)$ de alcance $R$, con una pared en $x = 0$. Este potencial, mostrado a la izquierda en la Figura 1, tiene un número de estados ligados, todos no degenerados, que pueden contarse. Existe también un conjunto de autoestados de energía positiva: los estados de dispersión que, al pertenecer a un continuo, no pueden contarse. Nuestra demostración requiere la posibilidad de contar estados, así que introduciremos una segunda pared infinita, colocada en $x = L$ para $L$ grande. Por supuesto, esto cambiará el espectro, pero a medida que $L$ se hace cada vez más grande los cambios se vuelven cada vez más pequeños. Pensamos en $L$ como un regulador del potencial que discretiza el espectro y así nos permite enumerar los estados. Lo hace porque, con dos paredes, el potencial se convierte en un pozo infinito ancho y todos los estados pasan a ser estados ligados. El potencial con la pared reguladora se muestra a la derecha en la Figura 1.

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes19_ES/fig1.png)

Figura 1: Izquierda: un potencial unidimensional arbitrario $V(x)$ de alcance $R$. Derecha: el mismo potencial con una pared reguladora colocada en $x = L$.

La clave de la demostración será comparar el conteo de estados en el potencial regulado $V \neq 0$ con el conteo de estados en el potencial $V = 0$, también regulado con una segunda pared en $x = L$. Consideremos entonces el potencial regulado $V = 0$ y los autoestados de energía positiva. Estos corresponden a la función de onda $\phi(x) = \sin kx$, con la segunda pared exigiendo $\phi(x = L) = 0$. Así obtenemos

$$kL = n\pi, \quad \text{con } n = 1, 2, \ldots \qquad \text{(1.2)}$$

Los valores de $k$ están ahora cuantizados. Sea $dk$ un intervalo infinitesimal en el número de onda, con $dn$ el número de estados en $dk$ cuando $V = 0$. Así,

$$dk\, L = dn\, \pi \ \to \ dn = \frac{L}{\pi}\, dk . \qquad \text{(1.3)}$$

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes19_ES/fig2.png)

Figura 2: Con la pared reguladora el número de onda $k$ toma valores discretos. $dk$ es un intervalo infinitesimal en el espacio de $k$.

Cuando $V(x) \neq 0$, las soluciones para $x > R$, todas ellas soluciones de energía positiva, tienen la forma

$$\psi(x) = e^{i\delta} \sin(kx + \delta) . \qquad \text{(1.4)}$$

La condición de frontera $\psi(L) = 0$ implica una cuantización

$$kL + \delta(k) = n'\pi , \qquad \text{(1.5)}$$

con $n'$ entero. Podemos nuevamente diferenciar para determinar el número de estados de energía positiva $dn'$ en el intervalo $dk$, con $V \neq 0$:

$$dk\, L + \frac{d\delta}{dk}\, dk = dn'\, \pi \ \to \ dn' = \frac{L}{\pi}\, dk + \frac{1}{\pi}\frac{d\delta}{dk}\, dk . \qquad \text{(1.6)}$$

El número de soluciones de energía positiva que se pierden en el intervalo $dk$ al encender el potencial $V$ está dado por $dn - dn'$, que puede evaluarse usando (1.3) y (1.6):

$$dn - dn' = -\frac{1}{\pi}\frac{d\delta}{dk}\, dk . \qquad \text{(1.7)}$$

El número total de soluciones de energía positiva que se pierden a medida que se enciende el potencial $V$ está dado integrando la expresión anterior sobre todo el rango de $k$:

$$\begin{gathered}
\text{núm. de soluciones de energía positiva perdidas al encender } V\\
= -\int_0^{\infty} \frac{1}{\pi}\frac{d\delta}{dk}\, dk = -\frac{1}{\pi}\left(\delta(\infty) - \delta(0)\right) . \qquad \text{(1.8)}
\end{gathered}$$

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes19_ES/fig3.png)

Figura 3: Los estados de energía positiva de la configuración con V = 0 se desplazan al encender el potencial, y algunos pueden convertirse en estados ligados.

Aunque perdemos un número de soluciones de energía positiva al encender el potencial $V$, los estados no desaparecen. Al encender el potencial de manera continua desde cero hasta $V$, podemos seguir la pista de cada autoestado de energía y ¡ningún estado puede desaparecer! Si perdemos algunos estados de energía positiva, esos estados deben reaparecer ahora como estados de energía negativa, ¡es decir, estados ligados! Denotando con $N_b$ el número de estados ligados en el potencial $V \neq 0$, el resultado en (1.8) implica que

$$N_b = \frac{1}{\pi}\left(\delta(0) - \delta(\infty)\right) . \qquad \text{(1.9)}$$

¡Esto es lo que queríamos demostrar!

## 2. Resonancias

Hemos calculado el retraso temporal $\Delta t = 2\hbar\,\delta'(E)$ asociado al paquete de ondas reflejado que emerge de los potenciales de alcance $R$ que hemos considerado. Si el retraso temporal es negativo, el paquete de ondas reflejado emerge antes de tiempo. Podemos preguntar: ¿podemos obtener un retraso temporal negativo arbitrariamente grande? La respuesta es no. Un retraso temporal muy grande sería una violación de la causalidad. Significaría que el paquete entrante se refleja incluso antes de alcanzar $x = R$, lo cual es imposible. De hecho, el mayor retraso temporal negativo se realizaría (al menos clásicamente) si tuviéramos reflexión perfecta cuando el paquete entrante llega a $x = R$. Si esto ocurre, el retraso temporal sería $-\frac{2R}{v_0}$, donde $v_0$ es la velocidad del paquete. En efecto, $\frac{2R}{v_0}$ es el tiempo que se ahorra el paquete que no tuvo que entrar y salir del alcance. Así, esperamos

$$\text{retraso temporal} = 2\hbar\frac{d\delta}{dE} \ge -\frac{2R}{v_0} . \qquad \text{(2.1)}$$

Esto puede simplificarse un poco usando derivadas respecto a $k$

$$2\hbar\frac{d\delta}{dE} = 2\hbar\frac{1}{\frac{dE}{dk}}\frac{d\delta}{dk} = \frac{2}{v_0}\frac{d\delta}{dk} \ge -\frac{2R}{v_0} , \qquad \text{(2.2)}$$

lo que a su vez da la restricción

$$\frac{d\delta}{dk} \ge -R . \qquad \text{(2.3)}$$

El argumento no fue riguroso, pero el resultado es bastante preciso, recibiendo correcciones que se anulan para paquetes de energía grande.

Alternativamente, podemos preguntar: ¿podemos obtener un retraso temporal positivo arbitrariamente grande? La respuesta es sí. Esto puede ocurrir si el paquete de ondas queda temporalmente atrapado en el potencial. En ese caso esperaríamos que la amplitud de probabilidad se vuelva grande en la región $0 < x < R$. Si el paquete de ondas queda atrapado durante un tiempo largo tenemos una resonancia. El estado se parece un poco a un estado ligado en el sentido de que se localiza en el potencial, al menos por un tiempo. Para obtener una resonancia ayuda tener un potencial atractivo y una barrera de energía positiva. Podemos lograr esto con el potencial

$$V(x) =
\begin{cases}
\infty & \text{para } x \le 0 \\
-V_0 & \text{para } 0 < x < a \\
V_1 & \text{para } a < x < 2a \\
0 & \text{para } x > 2a .
\end{cases} \qquad \text{(2.4)}$$

El potencial, con $V_0, V_1 > 0$, se muestra en la Figura 4. Para tener una resonancia exploramos energías en el rango de cero a $V_1$. En ese rango de energías podemos esperar encontrar algunos valores particulares que conducen a un comportamiento resonante, es decir, gran retraso temporal y gran amplitud para la función de onda en el pozo.

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes19_ES/fig4.png)

Figura 4: Buscamos resonancias con energía $E$ en el rango $(0, V_1)$. En este rango la barrera $V_1$ produce una región clásicamente prohibida $x \in (a, 2a)$, que puede ayudar a localizar la amplitud alrededor del pozo.

Dadas las tres regiones relevantes en el potencial, definimos

$$k'^2 = \frac{2m(E + V_0)}{\hbar^2}, \qquad \kappa^2 = \frac{2m(V_1 - E)}{\hbar^2}, \qquad k^2 = \frac{2mE}{\hbar^2} . \qquad \text{(2.5)}$$

En la región $0 < x < a$ debemos usar funciones trigonométricas de $k'x$. En la región $a < x < 2a$ usamos funciones hiperbólicas de $\kappa a$ y en la región $x > 2a$ usamos la solución canónica con desfasaje y número de onda $k$. En la región intermedia $a < x < 2a$ podríamos usar una combinación de soluciones

$$\{e^{\kappa x}, e^{-\kappa x}\}, \quad \text{o} \quad \{\cosh \kappa x, \sinh \kappa x\}, \quad \text{o} \quad \{\cosh \kappa(x-a), \sinh \kappa(x-a)\} . \qquad \text{(2.6)}$$

El último par es el más adecuado para implementar directamente la continuidad de la función de onda en $x = a$. Así podemos escribir para la función de onda $\psi(x)$:

$$\psi(x) =
\begin{cases}
A \sin(k'x) & 0 < x < a \\
A \sin(k'a) \cosh\kappa(x-a) + B \sinh\kappa(x-a) & a < x < 2a \\
e^{i\delta}\sin(kx+\delta) & x > 2a
\end{cases} \qquad \text{(2.7)}$$

Tras implementar las condiciones de frontera restantes podemos resolver para el desfasaje $\delta$. Después de un trabajo moderado se obtiene:

$$\tan(2ka + \delta) = \frac{k}{\kappa} \cdot \frac{\sin k'a \cosh\kappa a + \frac{k'}{\kappa}\cos k'a \sinh\kappa a}{\sin k'a \sinh\kappa a + \frac{k'}{\kappa}\cos k'a \cosh\kappa a} . \qquad \text{(2.8)}$$

Esta expresión es bastante intrincada, por lo que es mejor hacer un trabajo numérico. Para ello definimos

$$z_0^2 = \frac{2mV_0 a^2}{\hbar^2}, \qquad z_1^2 = \frac{2mV_1 a^2}{\hbar^2}, \qquad u \equiv ka . \qquad \text{(2.9)}$$

lo que nos permite expresar tanto $k'a$ como $\kappa a$ como funciones de $u$

$$(k'a)^2 = z_0^2 + u^2, \qquad (\kappa a)^2 = z_1^2 - u^2 . \qquad \text{(2.10)}$$

En este punto (2.8) puede usarse para determinar $\delta$ en función de $u = ka$ y las constantes $z_0, z_1$. Supongamos que elegimos valores para nuestros parámetros que controlan las ecuaciones. En la Figura 5 mostramos resultados para $z_0^2 = 1$ y $z_1^2 = 5$.

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes19_ES/fig5.png)

Figura 5: Gráfico de varias cantidades en función de $u = ka$, con el potencial caracterizado por $z_0^2 = 1$ y $z_1^2 = 5$. (a) $\delta(E)$ aumenta rápidamente alrededor de $u_* = 1.85$, o equivalentemente $E = 0.69\,V_1$, cruzando $-\pi/2$ y señalando comportamiento resonante. (b) Gráfico de $|A_s|^2 = \sin^2\delta$, mostrando picos cada vez que $|\delta| = \pi/2$. (c) El coeficiente $|A|$ de la función de onda en el pozo alcanza su pico en la resonancia, mostrando alta probabilidad de encontrar la partícula en el pozo. (d) El retraso temporal es positivo y alcanza su pico en la resonancia.

Consideremos la parte (a) de la figura, que muestra $\delta(ka)$. Al comienzo $\delta$ disminuye linealmente, señal de un retraso temporal negativo, ya que las ondas de baja energía se reflejan en el borde $x = 2a$ de la barrera $V_1$. Cuando $\delta$ cruza $-\pi/2$ no hay resonancia, aunque $|A_s|^2 = \sin^2\delta$ sea igual a uno. En efecto, no vemos ningún pico en la amplitud $|A|$. A medida que aumenta la energía y $u = u_* = 1.8523$ obtenemos una resonancia. Esta vez $\delta$ está aumentando rápidamente y $\delta$ cruza $-\pi/2$ nuevamente, haciendo que $|A_s|^2 = 1$. La señal de resonancia es el muy alto $|A|$, el pico en el retraso temporal. Este retraso temporal alcanza un valor de aproximadamente 14, lo que significa que el retraso es catorce veces el tiempo de tránsito libre $4a/v_0$.

## 3. Modelando la resonancia

Nos gustaría tener más comprensión sobre la naturaleza de las resonancias. En particular, queremos apreciar las características generales del fenómeno. Además, hasta ahora podemos identificar resonancias observando el comportamiento de $\delta$, pero ¿podemos encontrar una ecuación que defina las resonancias?

Como primer paso, modelamos el comportamiento de un desfasaje cerca de la resonancia. Recordando que una resonancia requiere que $|\delta|$ cruce el valor $\pi/2$ y que $\delta$, físicamente, es lo mismo que $\delta$ aumentado o disminuido en múltiplos de $\pi$, podemos elegir que $\delta$ varíe de casi cero a casi $\pi$. Podemos lograr esto con la siguiente función simple.

$$\delta = \tan^{-1}\left(\frac{\beta}{\alpha - k}\right), \quad \text{con } \beta > 0, \ \alpha > 0 . \qquad \text{(3.1)}$$

aquí $\alpha$ y $\beta$ son constantes positivas con las mismas unidades que $k$. Para ver lo que hace esta función, primero graficamos el argumento de la arcotangente en la parte superior de la Figura 6. Nótese que el argumento varía rápidamente en la región $(\alpha - \beta, \alpha + \beta)$. La variación de la fase asociada $\delta$ se muestra en la figura de abajo. Para tener un aumento pronunciado en la fase, debemos tener $\beta$ pequeño en comparación con $\alpha$.

![Figura 6](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes19_ES/fig6.png)

Figura 6: La constante $\beta$ debe ser pequeña en comparación con $\alpha$ para obtener una variación pronunciada. Una resonancia, como se muestra aquí, requiere que $\delta$ aumente con la energía.

Dos cálculos relativamente cortos nos dan más comprensión:

$$\left.\frac{d\delta}{dk}\right|_{k=\alpha} = \frac{1}{\beta}, \qquad |A_s|^2 = \sin^2\delta = \frac{\beta^2}{\beta^2 + (\alpha - k)^2} . \qquad \text{(3.2)}$$

El primero nos informa que, en igualdad de condiciones, el retraso es grande si $\beta$ es pequeño. El segundo nos da la norma al cuadrado de la amplitud de dispersión en función de $k$, con un pico en $k = \alpha$. Esta ecuación se expresa de manera más célebre en términos de la energía. Para esto notamos que

$$E - E_\alpha = \frac{\hbar^2}{2m}(k^2 - \alpha^2) = \frac{\hbar^2}{2m}(k+\alpha)(k-\alpha) \simeq \frac{\hbar^2}{2m}(2\alpha)(k-\alpha) , \qquad \text{(3.3)}$$

cuando trabajamos con $k \approx \alpha$. De esto se sigue que

$$(k-\alpha)^2 \simeq \frac{m^2}{\hbar^4 \alpha^2}(E - E_\alpha)^2 , \qquad \text{(3.4)}$$

y por lo tanto

$$|\psi_s|^2 \simeq \frac{\beta^2}{\beta^2 + \frac{m^2}{\hbar^4\alpha^2}(E-E_\alpha)^2} = \frac{\frac{1}{4}\Gamma^2}{(E-E_\alpha)^2 + \frac{1}{4}\Gamma^2} , \qquad \text{(3.5)}$$

Donde hemos definido la constante $\Gamma$ con unidades de energía:

$$\frac{1}{4}\Gamma^2 = \frac{\hbar^4\beta^2\alpha^2}{m^2} \ \to \ \Gamma = \frac{2\alpha\beta\hbar^2}{m} . \qquad \text{(3.6)}$$

La dependencia en la energía de $|\psi_s|^2$ sigue la llamada distribución de Breit-Wigner,

$$|\psi_s|^2 \simeq \frac{\frac{1}{4}\Gamma^2}{(E-E_\alpha)^2 + \frac{1}{4}\Gamma^2} . \qquad \text{(3.7)}$$

La distribución se muestra en la Figura 8. El valor pico para $|\psi_s|^2$ se alcanza en $E = E_\alpha$ y vale uno. Llamamos a $\Gamma$ el ancho a media altura porque el valor de $|\psi_s|^2$ en $E = E_\alpha \pm \frac{1}{2}\Gamma$ es un medio. Un $\Gamma$ pequeño corresponde a un ancho estrecho, o una resonancia estrecha.

![Figura 7](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes19_ES/fig7.png)

Figura 7: La distribución de Breit-Wigner. $\Gamma$ es el ancho de la distribución a media altura.

Para comprender mejor el significado de $\Gamma$ definimos el tiempo asociado $\tau$, llamado el tiempo de vida de la resonancia:

$$\tau \equiv \frac{\hbar}{\Gamma} = \frac{m}{2\alpha\beta\hbar} . \qquad \text{(3.8)}$$

Como probablemente esperaría, el tiempo de vida está estrechamente relacionado con el retraso temporal asociado a un paquete de ondas de energía media igual a la energía resonante. En efecto, podemos evaluar el retraso temporal $\Delta t$ para $k = \alpha$ y obtener

$$\Delta t = \left.2\hbar\frac{d\delta}{dE}\right|_{k=\alpha} = 2\hbar\frac{dk}{dE}\frac{d\delta}{dk} = \frac{2\hbar}{\frac{\hbar^2}{m}k}\cdot\frac{1}{\beta} = \frac{2m}{\hbar\alpha\beta} = 4\tau . \qquad \text{(3.9)}$$

Por lo tanto, concluimos que el tiempo de vida y el retraso temporal son la misma cantidad, salvo un factor de cuatro.

$$\tau = \frac{\hbar}{\Gamma} = \frac{1}{4}\Delta t . \qquad \text{(3.10)}$$

Las partículas inestables a veces se llaman resonancias. El bosón de Higgs, descubierto en 2012, es una partícula inestable con masa de 125 GeV. Puede desintegrarse en dos fotones, o en dos leptones tau, o en un par $b\bar{b}$, entre pocas otras posibilidades. El ancho $\Gamma$ asociado a la partícula es de 4.07 MeV ($\pm 4\%$). ¡Su tiempo de vida $\tau$ es de aproximadamente $1.62 \times 10^{-22}$ segundos!

Ahora intentamos comprender las resonancias de manera más matemática. Vimos que, en la resonancia, la norma de $A_s$ alcanza un valor máximo de uno. Exploremos cuándo $A_s$ es grande. Tenemos

$$A_s = \sin\delta\, e^{i\delta} = \frac{\sin\delta}{e^{-i\delta}} = \frac{\sin\delta}{\cos\delta - i\sin\delta} = \frac{\tan\delta}{1 - i\tan\delta} . \qquad \text{(3.11)}$$

En la resonancia $\delta = \pi/2$ y $A_s = i$, usando la primera igualdad. Por otro lado, si bien normalmente pensamos en $\delta$ como un número real, la expresión final de arriba indica que $A_s$ se vuelve infinito para

$$\tan\delta = -i , \qquad \text{(3.12)}$$

¡lo que sea que eso signifique! Si recordamos que $\tan iz = i\tanh z$ deducimos que la condición anterior requiere $\delta \to -i\infty$, un resultado bastante extraño. En todo caso, $A_s$ se vuelve infinito, o tiene un polo, en $\tan\delta = -i$. Veremos que el gran valor $|A_s| = 1$ en la resonancia puede considerarse como la “sombra” del valor infinito que $A_s$ alcanza cerca en el plano complejo.

![Figura 8](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes19_ES/fig8.png)

Figura 8: En el plano complejo de $k$, las resonancias se identifican como polos de la amplitud de dispersión $A_s$ ubicados ligeramente por debajo del eje real. Los estados ligados aparecen como polos sobre el eje imaginario positivo.

En efecto, podemos ver cómo se comporta $A_s$ cerca de la resonancia insertando el comportamiento cercano a la resonancia (3.1) de $\delta$ en (3.11):

$$A_s = \frac{\frac{\beta}{\alpha-k}}{1 - i\frac{\beta}{\alpha-k}} = \frac{\beta}{(\alpha - i\beta) - k} . \qquad \text{(3.13)}$$

Cuando $k = \alpha$, es decir, en la energía resonante, obtenemos $A_s = i$, como se esperaba. Si ahora pensamos en el número de onda $k$ como una variable compleja, vemos que el polo de $A_s$ es un polo en $k = k_* = \alpha - i\beta$. La parte real de $k_*$ es la energía resonante, y la parte imaginaria $\beta$ codifica el tiempo de vida. Para $\beta$ pequeño la resonancia es un polo cercano al eje real, como se ilustra en la Figura 8. Cuanto menor es $\beta$, más aguda es la resonancia. Como podemos ver, el valor de $|A_s|$ sobre la línea real se vuelve grande para $k = \alpha$ porque en realidad es infinito un poco por debajo del eje.

La lección de todo esto es que podemos, en efecto, tomar en serio (3.12) y buscar resonancias resolviendo para los valores complejos de $k$ para los cuales

$$\text{Condición de resonancia: } \tan\delta(k) = -i . \qquad \text{(3.14)}$$

La parte real de esos valores de $k$ son las energías resonantes. Las partes imaginarias nos dan el tiempo de vida.

La idea de un plano complejo de $k$ es muy poderosa. Supongamos que consideramos valores puramente imaginarios de $k$ de la forma $k = i\kappa$, con $\kappa > 0$. Entonces la energía toma la forma

$$E = -\frac{\hbar^2\kappa^2}{2m} < 0 , \qquad \text{(3.15)}$$

que es adecuada para estados ligados. En efecto, se puede demostrar que los estados ligados aparecen como polos de $A_s$ a lo largo del eje imaginario positivo, como se muestra en la Figura 8. ¡El plano complejo de $k$ tiene espacio para acomodar estados de dispersión, resonancias, y estados ligados!

*Sarah Geller transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare https://ocw.mit.edu

8.04 Física Cuántica I Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

# Apéndice: Lista de problemas 8 (Problem Set 8, 2016)

*Departamento de Física del MIT* *13 de abril de 2016 — Fecha de entrega: viernes 22 de abril de 2016, 12:00 del mediodía*

**Lecturas recomendadas:** Griffiths, páginas 73-76, 81-82 (sobre estados de dispersión). Ohanian, Capítulo 11: Dispersión y resonancias.

## Problema 1: Estados del oscilador armónico \[15 puntos\]

Considere el estado $\psi_\alpha$ definido por

$$\psi_\alpha \equiv N \exp(\alpha \hat{a}^\dagger)\, \varphi_0 ,$$

con $\alpha \in \mathbb{C}$ un número complejo. Para las dos primeras preguntas siguientes puede ser útil simplemente expandir la exponencial anterior.

1.  Encuentre la constante $N$ necesaria para que el estado $\psi_\alpha$ esté normalizado.

2.  Demuestre que el estado $\psi_\alpha$ es un autoestado del operador de aniquilación $\hat{a}$. ¿Cuál es el autovalor?

3.  Encuentre el valor esperado del hamiltoniano en el estado $\psi_\alpha$.

4.  Encuentre la incertidumbre en la energía en el estado $\psi_\alpha$.

5.  Use la ecuación de autovalores, vista como una ecuación diferencial, para calcular la forma explícita de la función de onda normalizada $\psi_\alpha$.

## Problema 2: Dos funciones delta — otra vez \[15 puntos\]

Considere de nuevo el problema de una partícula de masa $m$ moviéndose en un potencial de doble pozo unidimensional

$$V(x) = -g\,\delta(x-a) - g\,\delta(x+a) , \qquad g > 0 .$$

En la tarea anterior encontró el valor de la energía del estado ligado $E$ para el estado par en términos de la energía $E_0 = \hbar^2/(2ma^2)$. Había definido $\xi = \kappa a$,

$$\frac{E}{E_0} = -\xi^2 \quad \text{donde} \quad \frac{\xi}{1+e^{-2\xi}} = \lambda , \qquad \lambda \equiv \frac{mag}{\hbar^2} ,$$

con $\lambda$ adimensional, y que codifica la intensidad $g$ de las funciones delta, si $a$ es constante, o bien la separación entre las funciones delta, si $g$ es constante. Podemos entonces escribir

$$\lambda = \frac{a}{a_0} , \qquad a_0 \equiv \frac{\hbar^2}{mg} ,$$

siendo $a_0$ una escala de longitud natural del problema una vez fijado $g$. Introduzcamos también la energía $E_\infty$ asociada a una única función delta:

$$E_\infty \equiv \frac{mg^2}{2\hbar^2} .$$

Suponga ahora que este es un modelo de una molécula diatómica con distancia interatómica $2a$. El electrón del estado ligado ayuda a superar la energía repulsiva entre los iones. Sea la energía potencial repulsiva $V_r(x)$, con $x$ la distancia entre los átomos, dada por

$$V_r(x) = \frac{\beta g}{x} , \qquad \beta > 0 ,$$

donde $\beta$ es un número pequeño. La energía potencial total $V_{\text{tot}}$ de la configuración es la suma de la energía negativa $E$ del estado ligado y la energía repulsiva positiva:

$$V_{\text{tot}} = E + V_r(2a) .$$

1.  Escriba $E$ como $E = -E_\infty f(\xi,\lambda)$ donde $f$ es una función que debe determinar. Grafique $E$ como función de $a/a_0 = \lambda$ para entender cómo varía la energía del estado fundamental en función de la separación entre las moléculas. ¿Cuáles son los valores de $E$ para $a \to 0$ y para $a \to \infty$?

2.  Escriba $V_r$ en términos de $E_\infty$, $\beta$ y $\lambda$.

3.  Considere ahora la energía potencial total $V_{\text{tot}}$ y grafíquela como función de $a/a_0 = \lambda$ para varios valores de $\beta$. Debería encontrar un punto crítico estable del potencial para $\beta$ suficientemente pequeño. Para $\beta = 0.31$, ¿cuál es el valor aproximado de $a/a_0$ en el punto crítico del potencial?

## Problema 3: El pozo cuadrado finito convirtiéndose en el pozo cuadrado infinito \[5 puntos\]

Considere el potencial de pozo cuadrado estándar

$$V(x) = \begin{cases} -V_0 , & \text{para } |x| \le a,\ V_0 > 0 , \\ 0 & \text{para } |x| > a , \end{cases} \qquad (1)$$

y la función de onda para un estado par

$$\psi(x) = \begin{cases} \dfrac{1}{\sqrt{a}}\cos kx , & \text{para } |x| \le a, \\[4pt] \dfrac{A}{\sqrt{a}}\, e^{-\kappa|x|} , & \text{para } |x| > a , \end{cases} \qquad (2)$$

donde incluimos el prefactor $\frac{1}{\sqrt{a}}$ para tener unidades consistentes para $\psi$.

Queremos comprender mejor el límite $V_0 \to \infty$ y entender por qué la discontinuidad en $\psi'$ del pozo infinito no genera problemas. Mantener $m$ y $a$ constantes mientras $V_0$ crece equivale a dejar que $z_0$ crezca.

Un análisis previo demostró que para el estado fundamental, en la situación de $z_0$ grande, el ansatz (2) está normalizado con precisión y

$$\eta = ka \simeq \frac{\pi}{2}\left(1 - \frac{1}{z_0}\right) , \qquad \xi = \kappa a \simeq z_0 , \qquad A \simeq \frac{\pi}{2 z_0}\, e^{z_0} .$$

Queremos ver si el valor esperado del hamiltoniano recibe una contribución singular desde la región prohibida. Dado que el potencial $V(x)$ se anula allí, solo debemos preocuparnos por la contribución del operador de energía cinética $\hat{K} = \hat{p}^2/2m$. Calcule la contribución al valor esperado de $\hat{K}$ desde la región prohibida $x > a$:

$$\langle \hat{K} \rangle_{x>a} \equiv \int_a^\infty dx\, \psi^*(x)\, \hat{K}\, \psi(x) .$$

La respuesta debe darse en términos de $z_0$. Interprete su resultado.

## Problema 4: Reflexión de un paquete de ondas contra un potencial escalón \[20 puntos\]

Considere un potencial escalón con altura $V_0$:

$$V(x) = \begin{cases} V_0 , & \text{para } x > 0 \\ 0 , & \text{para } x < 0 . \end{cases} \qquad (1)$$

Enviamos desde $x = -\infty$ un paquete de ondas cuyas componentes de momento tienen todas energías menores que la energía $V_0$ del escalón. Para esto necesitamos modos con $k$ que satisfagan

$$k \le \hat{k} , \qquad \hat{k}^2 = \frac{2mV_0}{\hbar^2} . \qquad (2)$$

Escribiremos entonces el paquete de ondas incidente como

$$\Psi_{\text{inc}}(x) = \sqrt{a} \int_0^{\hat{k}} dk\, \Phi(k)\, e^{ikx}\, e^{-iE(k)t/\hbar} , \qquad x < 0 . \qquad (3)$$

Aquí $a$ es la constante con unidades de longitud, determinada de manera única por las constantes $m$, $V_0$, $\hbar$ de este problema, y $\Phi(k)$ es una función real, adimensional, con un máximo en $k_0 < \hat{k}$:

$$a \equiv \frac{\hbar}{\sqrt{mV_0}} , \qquad \Phi(k) = e^{-\beta^2 a^2 (k-k_0)^2} . \qquad (4)$$

La constante real $\beta$, que se fijará más abajo, controla el ancho de la distribución de momento. Las unidades de $\Psi_{\text{inc}}$ son $L^{-1/2}$, y por eso incluimos el prefactor $\sqrt{a}$ en (3). Recuerde que $dk$ tiene unidades de $L^{-1}$.

1.  Escriba la función de onda reflejada (válida para $x<0$) como una integral similar a (3). Esta integral involucra el desfasaje $\delta(E)$ calculado en clase.

Introduzca una versión adimensional $K$ del número de onda $k$, una versión adimensional $u$ de la coordenada $x$, y una versión adimensional $\tau$ del tiempo $t$, de la siguiente manera:

$$k \equiv \frac{K}{a} , \qquad x \equiv au , \qquad t \equiv \frac{\hbar}{V_0}\tau . \qquad (5)$$

Naturalmente, escribiremos $k_0 = K_0/a$. Note que $kx = Ku$.

1.  Demuestre que la velocidad de grupo y la relación de incertidumbre para el paquete entrante toman la forma

$$\frac{du}{d\tau} = \#\, K_0 , \qquad \Delta u\, \Delta K \ge \# ,$$

donde $\#$ representa constantes numéricas que debe determinar (¡constantes distintas!). Use la aproximación de que se tiene la gaussiana completa $|\Phi(K)|^2$ para determinar la incertidumbre $\Delta K$ en el paquete entrante en términos de $\beta$. Suponiendo de nuevo que se tiene una gaussiana completa, ¿cuál sería (en términos de $\beta$) el valor mínimo posible de la incertidumbre $\Delta u$ para la distribución de probabilidad asociada en el espacio de coordenadas?

1.  Complete las siguientes ecuaciones fijando las constantes representadas por $\#$:

$$E(k) = \#\, V_0 K^2 , \qquad e^{2i\delta(E)} = \# + \#K^2 + iK\sqrt{\# + \#K^2} \equiv w(K) .$$

1.  Demuestre que el retraso $\Delta t = 2\hbar\,\delta'(E)$ experimentado por la onda reflejada implica un $\Delta\tau$ dado por

$$\Delta\tau = \frac{\#}{K_0\sqrt{\# + \#K_0^2}} ,$$

donde debe fijar las constantes.

1.  Demuestre que la función de onda completa $\Psi(x,t)$, válida para $x<0$ y todo tiempo, que ahora vemos como $\Psi(u,\tau)$ válida para $u<0$ y todo $\tau$, toma la forma

$$a^{\frac{1}{2}}\Psi(u,\tau) = \int_0^{\#} dK\, e^{-\beta^2 (K-K_0)^2}\, e^{-i\#K^2\tau}\left( e^{iKu} - e^{-iKu}\, w(K) \right)$$

y determine las dos constantes faltantes.

1.  Fije $\beta = 4$ y $K_0 = 1$. ¿Cuáles son los valores de $\Delta K$ y $\Delta u$? ¿Cuál es el retraso temporal $\Delta\tau$ predicho? (No se califica: ¿puede hacer una conjetura informada sobre si el paquete cambiará de forma rápidamente?)

Ahora use Mathematica para calcular y graficar la densidad de probabilidad $|a^{1/2}\Psi(u,\tau)|^2$. Dé la gráfica de la función de onda para $\tau = -20, -5$ y $0$, usando $u \in [-30,0]$. Examine la gráfica para $\tau = 20$ y determine el retraso temporal $\Delta\tau$ observando la posición del máximo del paquete. Su respuesta debería acercarse razonablemente al valor analítico determinado previamente.

## Problema 5: Dispersión en una barrera rectangular \[10 puntos\]

Basado en Griffiths 2.33, p. 83.

Resuelva solamente los casos $E < V_0$ y $E = V_0$.

¿Puede obtener $T = 1$ para $E < V_0$?

Encuentre la respuesta para $E > V_0$ en algún libro (o hágalo usted mismo). ¿Cuándo se obtiene $T=1$ para $E > V_0$?

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*
