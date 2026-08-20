# Clase 16: Estados de dispersión y el potencial escalón

## Vídeos de esta clase (YouTube)

**Lección 16: Step potential reflection and transmission coefficients. Phase shift, wavepackets and time delay.**

- [Step potential probability current](https://www.youtube.com/watch?v=z79v39lMR3k)
- [Reflection and transmission coefficients](https://www.youtube.com/watch?v=bX-k26w-tsU)
- [Energy below the barrier and phase shift](https://www.youtube.com/watch?v=EkpbxgEslE4)
- [Wavepackets](https://www.youtube.com/watch?v=NXPvXI603RA) (20:51)
- [Wavepackets with energy below the barrier](https://www.youtube.com/watch?v=yqrMAZkQOwI)
- [Particle on the forbidden region](https://www.youtube.com/watch?v=lA8-N_ARHTw)

------------------------------------------------------------------------

B. Zwiebach

19 de abril de 2016

## Contenido

1.  El potencial escalón
2.  Potencial escalón con $E > V_0$
3.  Potencial escalón con $E < V_0$
4.  Paquetes de onda en el potencial escalón

## 1. El potencial escalón

![Figura 1](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes16_ES/fig1.png)

Figura 1: El potencial escalón.

Comenzamos ahora nuestro estudio detallado de los estados de dispersión. Estos son estados propios de energía no normalizables. Sencillamente no pueden normalizarse, igual que los estados propios de momento. Estos estados propios de energía no son estados de partículas; hay que superponer estados de dispersión para producir estados normalizables que puedan representar una partícula sometida a dispersión en algún potencial. Aquí examinamos el potencial escalón (Figura 1), definido por

$$V(x) = \begin{cases} 0, & x < 0, \\ V_0, & x \geq 0. \end{cases} \qquad \text{(1.1)}$$

Nuestras soluciones a la ecuación de Schrödinger con este potencial serán estados de dispersión de energía definida $E$. Podemos considerar dos casos: $E > V_0$ y $E < V_0$. En ambos casos la función de onda se extiende infinitamente hacia la izquierda y no es normalizable. Comencemos con el caso $E > V_0$.

## 2. Potencial escalón con $E > V_0$

![Figura 2](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes16_ES/fig2.png)

Figura 2: La energía $E$ del estado estacionario es mayor que el escalón $V_0$. Todo el eje $x$ es clásicamente permitido.

El estado estacionario con energía $E$ tiene la forma

$$\Psi(x,t) = \psi(x) e^{-iEt/\hbar}, \qquad \text{(2.2)}$$

y nos centraremos primero en la función desconocida $\psi(x)$. Para escribir un ansatz adecuado para $\psi(x)$ visualizamos un proceso físico en el que tenemos una onda incidente sobre la barrera escalón desde la izquierda. Dada tal onda que viaja en la dirección de $x$ creciente, esperaríamos una onda reflejada y una onda transmitida. La onda reflejada, moviéndose en la dirección de $x$ decreciente, existiría para $x < 0$. La onda transmitida, moviéndose en la dirección de $x$ creciente, existiría para $x > 0$. El ansatz para el estado propio de energía debe contener por tanto las tres partes:

$$\psi(x) = \begin{cases} A e^{ikx} + B e^{-ikx}, & x < 0, \\ C e^{i\bar{k}x}, & x > 0. \end{cases} \qquad \text{(2.3)}$$

Recordemos que $e^{ikx}$, con $k > 0$, representa una onda que se mueve en la dirección de $x$ creciente, dada la dependencia temporal universal anterior. Por tanto $A$ es el coeficiente de la onda incidente, $B$ es el coeficiente de la onda reflejada, y $C$ es el coeficiente de la onda transmitida. Las ondas para $x < 0$ tienen número de onda $k$ y la onda para $x > 0$ tiene número de onda $\bar{k}$. Estos números de onda quedan fijados por la ecuación de Schrödinger

$$k^2 = \frac{2mE}{\hbar^2}, \qquad \bar{k}^2 = \frac{2m(E - V_0)}{\hbar^2}. \qquad \text{(2.4)}$$

Hay dos ecuaciones que restringen nuestros coeficientes $A$, $B$ y $C$: tanto la función de onda como su derivada deben ser continuas en $x = 0$. Con estas dos condiciones podemos resolver $B$ y $C$ en términos de $A$. Esto es todo lo que podríamos esperar hacer: debido a la linealidad, la escala global de estos tres coeficientes debe permanecer indeterminada. De hecho, podemos pensar en $A$ como el valor de entrada y en $B$ y $C$ como valores de salida. Comencemos:

- $\psi(x)$ debe ser continua en $x = 0$. Por tanto

$$A + B = C. \qquad \text{(2.5)}$$

- $\psi'(x)$ debe ser continua en $x = 0$. Por tanto

$$ikA - ikB = i\bar{k}C \quad \Rightarrow \quad A - B = \frac{\bar{k}}{k} C. \qquad \text{(2.6)}$$

Resolviendo $B$ y $C$ en términos de $A$, obtenemos

$$\frac{B}{A} = \frac{k - \bar{k}}{k + \bar{k}}, \qquad \frac{C}{A} = \frac{2k}{k + \bar{k}}. \qquad \text{(2.7)}$$

Si $A$ es real, $B$ y $C$ son reales. Para $E = V_0$, tenemos $\bar{k} = 0$ y las ecuaciones (2.7) dan $B = A$ y $C = 2A$. Por tanto, para $E = V_0$ el estado propio de energía es

$$E = V_0: \qquad \psi(x) = \begin{cases} 2A \cos(kx), & x < 0, \\ 2A, & x > 0, \end{cases} \qquad \text{(2.8)}$$

y tiene el siguiente aspecto:

![Figura 3](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes16_ES/fig3.png)

Figura 3: Estado propio de energía para $E = V_0$.

Obtenemos mayor comprensión de la solución evaluando la corriente de probabilidad a la izquierda y a la derecha del escalón en $x = 0$. Recordemos la forma de la corriente de probabilidad para una función de onda $\psi$:

$$J = \operatorname{Im}\left(\psi^* \frac{\hbar}{m} \frac{\partial \psi}{\partial x}\right) \qquad \text{(2.9)}$$

Un cálculo breve muestra que la corriente $J_L$ a la izquierda del escalón es

$$J_L = \frac{\hbar k}{m}\left(|A|^2 - |B|^2\right) = J_A - J_B, \qquad J_A = \frac{\hbar k}{m}|A|^2, \qquad J_B = \frac{\hbar k}{m}|B|^2. \qquad \text{(2.10)}$$

No hay interferencia entre la onda incidente y la reflejada. La corriente total a la izquierda del escalón es simplemente la corriente $J_A$ asociada a la onda incidente menos la corriente $J_B$ asociada a la onda reflejada. La corriente $J_R$ a la derecha del escalón es

$$J_R = \frac{\hbar \bar{k}}{m}|C|^2 = J_C. \qquad \text{(2.11)}$$

En cualquier solución estacionaria no puede haber acumulación de probabilidad en ninguna región del espacio porque la densidad de probabilidad $\rho$ es manifiestamente independiente del tiempo. Aunque la probabilidad fluye continuamente en las soluciones de dispersión, debe conservarse. A partir de la ecuación de conservación $\dfrac{\partial J}{\partial x} + \dfrac{\partial \rho}{\partial t} = 0$, la independencia temporal de $\rho$ implica que la corriente $J$ debe ser independiente de $x$. En particular, nuestra solución (2.7) debe implicar que $J_L = J_R$. Verifiquémoslo:

$$\begin{aligned}
J_L &= \frac{\hbar k}{m}\left(|A|^2 - |B|^2\right) = \frac{\hbar k}{m}\left(1 - \left(\frac{k - \bar{k}}{k + \bar{k}}\right)^2\right)|A|^2\\
&= \frac{\hbar k}{m}\frac{4k\bar{k}}{(k+\bar{k})^2}|A|^2 = \frac{\hbar \bar{k}}{m}\underbrace{\frac{4k^2}{(k+\bar{k})^2}|A|^2}_{|C|^2} = \frac{\hbar \bar{k}}{m}|C|^2 = J_R, \qquad \text{(2.12)}
\end{aligned}$$

como se esperaba. La igualdad de $J_L$ y $J_R$ implica que

$$J_A - J_B = J_C \quad \Rightarrow \quad J_A = J_B + J_C \quad \Rightarrow \quad 1 = \frac{J_B}{J_A} + \frac{J_C}{J_A}. \qquad \text{(2.13)}$$

Definimos ahora el coeficiente de reflexión $R$ como el cociente entre el flujo de probabilidad en la onda reflejada y el flujo de probabilidad en la onda entrante:

$$R \equiv \frac{J_B}{J_A} = \frac{|B|^2}{|A|^2} = \left(\frac{k - \bar{k}}{k + \bar{k}}\right)^2 \leq 1. \qquad \text{(2.14)}$$

Este cociente resulta ser el módulo al cuadrado del cociente $B/A$, y es manifiestamente menor que uno, como debe ser. Definimos también el coeficiente de transmisión $T$ como el cociente entre el flujo de probabilidad en la onda transmitida y el flujo de probabilidad en la onda entrante:

$$T \equiv \frac{J_C}{J_A} = \frac{\bar{k}\,|C|^2}{k\,|A|^2} = \frac{\bar{k}}{k}\frac{4k^2}{(k+\bar{k})^2} = \frac{4k\bar{k}}{(k+\bar{k})^2}. \qquad \text{(2.15)}$$

Las definiciones anteriores son razonables porque $R$ y $T$, dados en términos de cocientes de corrientes, suman uno:

$$R + T = 1, \qquad \text{(2.16)}$$

como se deduce por inspección de (2.13). Nótese que $T \neq |C|^2/|A|^2$ porque los números de onda a la derecha y a la izquierda del escalón no son iguales.

Recordemos que para $E = V_0$ encontramos $\bar{k} = 0$. En ese caso tenemos reflexión total: $R = 1$ y $T = 0$. En efecto, la corriente de probabilidad asociada a la función de onda constante que existe para $x > 0$ (véase (2.8)) es cero. Adicionalmente podemos dar un argumento de continuidad. Los coeficientes $R$ y $T$ deben ser funciones continuas de la energía $E$. Para $E < V_0$ esperamos $T = 0$ ya que la región prohibida es todo $x > 0$ y una función de onda que decae exponencialmente no puede transportar flujo de probabilidad. Si $T = 0$ para cualquier $E < V_0$, debe seguir siendo cero para $E = V_0$, por continuidad.

## 3. Potencial escalón con $E < V_0$

![Figura 4](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes16_ES/fig4.png)

Figura 4: La barrera del potencial escalón.

Cuando $E < V_0$ la región $x > 0$ es una región clásicamente prohibida. Intentemos resolver el estado propio de energía sin rehacer todo el trabajo involucrado en resolver $B$ y $C$ en términos de $A$. Para este propósito notamos primero que el ansatz (2.3) para $x < 0$ puede quedar sin cambios. Por otro lado, para $x > 0$ la solución anterior

$$\psi(x) = C e^{i\bar{k}x}, \qquad \bar{k}^2 = \frac{2m(E - V_0)}{\hbar^2}, \qquad \text{(3.17)}$$

debe convertirse en una exponencial decreciente

$$\psi(x) = C e^{-\kappa x}, \qquad \kappa^2 = \frac{2m(V_0 - E)}{\hbar^2}. \qquad \text{(3.18)}$$

Notamos que la primera se convierte en la segunda mediante la sustitución

$$\bar{k} \to i\kappa. \qquad \text{(3.19)}$$

Esto significa que podemos simplemente realizar esta sustitución en nuestras expresiones anteriores para $B/A$ y $C/A$ y obtenemos las nuevas expresiones. En particular, a partir de (2.7) obtenemos

$$\frac{B}{A} = \frac{k - i\kappa}{k + i\kappa} \qquad \text{(3.20)}$$

Por tanto

$$\frac{B}{A} = \frac{i(k - i\kappa)}{i(k+i\kappa)} = -\frac{\kappa + ik}{\kappa - ik} = -e^{2i\delta(E)}, \qquad \text{(3.21)}$$

con

$$\delta(E) = \tan^{-1}\left(\frac{k}{\kappa}\right) = \tan^{-1}\sqrt{\frac{E}{V_0 - E}}. \qquad \text{(3.22)}$$

Dado que el módulo de $A$ es igual al módulo de $B$, tenemos $J_A = J_B$ y $J_C = 0$. Por tanto $T = 0$ y $R = 1$. Como se señaló antes, el cociente $B/A$ es una fase pura. La fase del numerador $\kappa + ik$ es $\delta(E)$ y la fase del denominador $\kappa - ik$ es $-\delta(E)$, dando así la fase total $2\delta(E)$ para el cociente. No absorbimos el signo negativo en la fase; de esta manera $\delta(E) \to 0$ cuando $E \to 0$. Nótese que $\delta(E)$ es positiva y no excede $\pi/2$. De hecho, un esquema de $\delta(E)$ se muestra en la Figura 5.

![Figura 5](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes16_ES/fig5.png)

Figura 5: La fase $\delta(E)$ en función de la energía $E < V_0$.

La función de onda total para $x < 0$ es interesante:

$$\begin{aligned}
\psi(x) &= A e^{ikx} + (-A e^{2i\delta(E)}) e^{-ikx} \\
&= A e^{i\delta(E)}\left(e^{-i\delta(E)} e^{ikx} - e^{i\delta(E)} e^{-ikx}\right) \\
&= 2iA e^{i\delta(E)} \sin(kx - \delta(E))
\end{aligned} \qquad \text{(3.23)}$$

Esto significa que la densidad de probabilidad es

$$|\psi|^2 = 4A^2 \sin^2(kx - \delta(E)). \qquad \text{(3.24)}$$

El punto $x_0 > 0$ determinado por la condición $kx_0 = \delta(E)$ es el punto en la región prohibida donde se anularía la extrapolación de la solución de la región permitida. Por supuesto, en la región prohibida $x > 0$, la densidad de probabilidad $|\psi|^2$ es una exponencial decreciente.

![Figura 6](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes16_ES/fig6.png)

Figura 6: Norma al cuadrado del estado propio de energía cuando $E < V_0$. Para $x > 0$ la densidad de probabilidad decae exponencialmente con $x$. El punto $x_0$ es el punto donde se anularía la extrapolación de la densidad de probabilidad de $x < 0$.

Para uso posterior registramos la derivada de la fase $\delta(E)$ respecto de la energía

$$\delta'(E) \equiv \frac{d\delta(E)}{dE} = \frac{1}{2}\sqrt{\frac{1}{E(V_0 - E)}}. \qquad \text{(3.25)}$$

Nótese que esta derivada se hace infinita tanto para $E \to 0$ como para $E \to V_0$.

![Figura 7](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes16_ES/fig7.png)

Figura 7: La derivada $\delta'(E)$ en función de la energía $E < V_0$.

## 4. Paquetes de onda en el potencial escalón

Examinamos ahora el escenario más físico. Como hemos visto con la partícula libre, los estados estacionarios no son normalizables, y las partículas físicas se representan en realidad mediante paquetes de onda construidos con una superposición infinita de estados propios de momento. Podemos hacer algo similar con nuestros estados propios de energía. Consideraremos estados propios de energía con $E > V_0$, o equivalentemente con $k^2 > \hat{k}^2$, donde

$$k^2 = \frac{2mE}{\hbar^2} > \frac{2mV_0}{\hbar^2} \equiv \hat{k}^2, \qquad \text{(4.26)}$$

y los superpondremos. Para comenzar escribimos los estados propios de energía en una forma ligeramente distinta, incluyendo la dependencia temporal. Fijando $A = 1$ y usando los valores de los cocientes $B/A$ y $C/A$, encontramos la solución

$$\Psi(x,t) = \begin{cases} \left(e^{ikx} + \dfrac{k - \bar{k}}{k + \bar{k}} e^{-ikx}\right) e^{-iE(k)t/\hbar}, & x < 0, \\[2mm] \dfrac{2k}{k + \bar{k}} e^{i\bar{k}x} e^{-iE(k)t/\hbar}, & x > 0. \end{cases} \qquad \text{(4.27)}$$

Podemos formar una superposición de estas soluciones multiplicando por una función $f(k)$ e integrando sobre $k$:

$$\Psi(x,t) = \begin{cases} \displaystyle\int_{\hat{k}}^{\infty} dk\, f(k) \left(e^{ikx} + \dfrac{k - \bar{k}}{k + \bar{k}} e^{-ikx}\right) e^{-iE(k)t/\hbar}, & x < 0, \\[3mm] \displaystyle\int_{\hat{k}}^{\infty} dk\, f(k) \dfrac{2k}{k + \bar{k}} e^{i\bar{k}x} e^{-iE(k)t/\hbar}, & x > 0. \end{cases} \qquad \text{(4.28)}$$

Aquí $f(k)$ es una función real de $k$ que es esencialmente cero excepto por un pico estrecho en $k = k_0$. Nótese que solo hemos incluido componentes de momento con energía mayor que $V_0$ fijando el límite inferior de la integral igual a $\hat{k}$. La integral solo se extiende sobre $k$ positivo porque solo en ese caso las ondas $e^{ikx}$ se mueven hacia $x$ positivo, y son por tanto ondas incidentes genuinas. Lo anterior está garantizado que sea una solución de la ecuación de Schrödinger.

Podemos dividir la solución en ondas incidente, reflejada y transmitida, como sigue.

$$\Psi(x,t) = \begin{cases} \Psi_{\text{inc}}(x,t) + \Psi_{\text{ref}}(x,t), & x < 0, \\ \Psi_{\text{trans}}(x,t), & x > 0. \end{cases} \qquad \text{(4.29)}$$

Naturalmente, tanto $\Psi_{\text{inc}}(x,t)$ como $\Psi_{\text{ref}}(x,t)$ existen para $x < 0$ y $\Psi_{\text{trans}}(x,t)$ existe para $x > 0$. Tenemos entonces, explícitamente,

$$\Psi_{\text{inc}}(x<0,t) = \int_{\hat{k}}^{\infty} dk\, f(k) e^{ikx} e^{-iE(k)t/\hbar},$$

$$\Psi_{\text{ref}}(x<0,t) = \int_{\hat{k}}^{\infty} dk\, f(k) \left(\frac{k - \bar{k}}{k + \bar{k}}\right) e^{-ikx} e^{-iE(k)t/\hbar}, \qquad \text{(4.30)}$$

$$\Psi_{\text{trans}}(x>0,t) = \int_{\hat{k}}^{\infty} dk\, f(k) \left(\frac{2k}{k + \bar{k}}\right) e^{i\bar{k}x} e^{-iE(k)t/\hbar}.$$

¿Cómo se mueve el pico de $\Psi_{\text{inc}}(x,t)$? Para esto buscamos la contribución principal a la integral asociada, que ocurre cuando la fase total en el integrando es estacionaria para $k \approx k_0$. Requerimos por tanto

$$\frac{d}{dk}\left(kx - \frac{\hbar^2 k^2}{2m}\frac{t}{\hbar}\right)\bigg|_{k_0} = 0 \quad \Rightarrow \quad x - \frac{\hbar k_0}{m} t = 0 \quad \Rightarrow \quad x = \frac{\hbar k_0}{m} t. \qquad \text{(4.31)}$$

Esta es la relación entre $t$ y $x$ que satisface el pico de $\Psi_{\text{inc}}$. Describe un pico que se mueve con velocidad constante $\hbar k_0/m > 0$. Dado que $\Psi_{\text{inc}}(x,t)$ requiere que $x < 0$, la condición anterior muestra que obtenemos el pico solo para $t < 0$. El pico del paquete llega a $x = 0$ en $t = 0$. Para $t > 0$, $\Psi_{\text{inc}}(x,t)$ no es cero, pero debe ser bastante pequeño, ya que la condición de fase estacionaria no puede satisfacerse para ningún $x$ en el dominio $x < 0$.

Consideremos ahora $\Psi_{\text{ref}}(x,t)$. Esta vez la condición de fase estacionaria es

$$\frac{d}{dk}\left(-kx - \frac{\hbar^2 k^2}{2m}\frac{t}{\hbar}\right)\bigg|_{k_0} = 0 \quad \Rightarrow \quad x + \frac{\hbar k_0}{m} t = 0 \quad \Rightarrow \quad x = -\frac{\hbar k_0}{m} t. \qquad \text{(4.32)}$$

La relación representa un pico que se mueve con velocidad constante negativa $-\hbar k_0/m$. Dado que $\Psi_{\text{ref}}(x,t)$ requiere que $x < 0$, la condición anterior muestra que obtenemos el pico solo para $t > 0$, como corresponde a una onda reflejada. Para $t > 0$, $\Psi_{\text{ref}}(x,t)$ no es cero, pero debe ser bastante pequeño, ya que la condición de fase estacionaria no puede satisfacerse para ningún $x$ en el dominio $x < 0$.

Finalmente, consideremos $\Psi_{\text{trans}}$. La condición de fase estacionaria dice:

$$\frac{d}{dk}\left(\bar{k}x - \frac{\hbar^2 k^2}{2m}\frac{t}{\hbar}\right)\bigg|_{k_0} = 0 \quad \Rightarrow \quad \frac{d\bar{k}}{dk}\bigg|_{k_0} x - \frac{\hbar k_0}{m} t = 0 \qquad \text{(4.33)}$$

Usando

$$\bar{k}^2 = k^2 - \frac{2mV_0}{\hbar^2} \quad \Rightarrow \quad \frac{d\bar{k}}{dk} = \frac{k}{\bar{k}}, \qquad \text{(4.34)}$$

y volviendo a la ecuación anterior encontramos rápidamente que

$$\text{Pico de la onda transmitida:} \qquad x = \frac{\hbar \bar{k}}{m} t, \qquad \text{(4.35)}$$

con $\bar{k}$ evaluado en $k = k_0$. Dado que $x > 0$ es el dominio de $\Psi_{\text{trans}}$, esto describe un pico que se mueve hacia la derecha con velocidad $\hbar \bar{k}/m$ para $t > 0$. Para $t < 0$, $\Psi_{\text{trans}}(x,t)$ no es cero, pero debe ser bastante pequeño, ya que la condición de fase estacionaria no puede satisfacerse para ningún $x$ en el dominio $x > 0$.

En resumen, para tiempos muy negativos $\Psi_{\text{inc}}$ domina y tanto $\Psi_{\text{ref}}$ como $\Psi_{\text{trans}}$ son muy pequeños. Para tiempos muy positivos, tanto $\Psi_{\text{ref}}$ como $\Psi_{\text{trans}}$ dominan y $\Psi_{\text{inc}}$ se hace muy pequeño. Estas situaciones se esquematizan en las figuras 8 y 9. Por supuesto, para tiempos pequeños, positivos o negativos, las tres ondas existen y juntas describen el complejo proceso de colisión con el escalón en el que se generan una onda reflejada y una onda transmitida.

![Figura 8](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes16_ES/fig8.png)

Figura 8: En tiempos muy negativos un paquete de onda entrante viaja en la dirección $+x$.

![Figura 9](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes16_ES/fig9.png)

Figura 9: En tiempos muy positivos tenemos un paquete de onda reflejado que viaja en la dirección $-\hat{x}$ y el paquete de onda transmitido que viaja en la dirección $+\hat{x}$.

Examinemos ahora un paquete de onda construido con energías $E < V_0$. Recordemos que en esta situación $B/A = -e^{2i\delta(E)}$. Por tanto, para una onda incidente, cuyas componentes de momento tienen todas energía menor que $V_0$,

$$\Psi_{\text{inc}}(x<0,t) = \int_0^{\hat{k}} dk\, f(k) e^{ikx} e^{-iEt/\hbar}, \qquad \text{(4.36)}$$

la función de onda reflejada asociada es

$$\Psi_{\text{ref}}(x<0,t) = -\int_0^{\hat{k}} dk\, f(k)\, e^{2i\delta(E)} e^{-ikx} e^{-iEt/\hbar}. \qquad \text{(4.37)}$$

Usando de nuevo el método de la fase estacionaria para encontrar la evolución del pico,

$$\frac{d}{dk}\left(2\delta(E) - kx - \frac{Et}{\hbar}\right)\bigg|_{k_0} = 0 \quad \Rightarrow \quad 2\delta'(E)\frac{\hbar^2 k_0}{m} - x - \frac{\hbar k_0 t}{m} = 0. \qquad \text{(4.38)}$$

De aquí encontramos rápidamente

$$x = -\frac{\hbar k_0}{m}\left(t - 2\hbar\, \delta'(E)\right), \qquad \text{(4.39)}$$

donde la derivada se evalúa en $E(k_0)$. El paquete de onda reflejado se mueve hacia valores más negativos de $x$ a medida que el tiempo crece positivamente. Esto es como debe ser. Pero hay un retraso temporal asociado al paquete reflejado, evidente al comparar la ecuación anterior con $x = -\dfrac{\hbar k_0}{m} t$. El retraso temporal viene dado por

$$\text{retraso temporal} = 2\hbar\, \delta'(E). \qquad \text{(4.40)}$$

La derivada $\delta'(E)$ fue evaluada en (3.25) y es positiva. Vemos que el retraso es particularmente grande para paquetes de onda de poca energía o para aquellos con energías justo por debajo de $V_0$.

Concluimos el análisis del potencial escalón discutiendo qué significa observar la partícula en la región prohibida. Sería contradictorio que el observador pudiera hacer las dos afirmaciones siguientes:

1.  La partícula está localizada en la región prohibida.
2.  La partícula tiene energía menor que $V_0$.

Ambas afirmaciones, tomadas como válidas simultáneamente, implicarían que la partícula tiene energía cinética negativa, algo inconsistente. En particular, con $E < V_0$ tendríamos una energía cinética negativa de magnitud $V_0 - E$.

![Figura 10](https://jjdeharo.github.io/cursos-mit/8.04-fisica-cuantica-i-es/html/figuras/MIT8.04_LecNotes16_ES/fig10.png)

Figura 10: El potencial escalón con energía potencial $V_0$. Si pudiéramos observar una partícula en la región prohibida con energía $E$, entonces la energía cinética sería negativa.

Notemos primero que en la solución la partícula penetra en la región prohibida una distancia de aproximadamente $1/\kappa$, donde, recordemos,

$$\kappa^2 = \frac{2m(V_0 - E)}{\hbar^2}. \qquad \text{(4.41)}$$

Para asegurar que la partícula esté en la región prohibida, su incertidumbre de posición $\Delta x$ debe ser menor que la profundidad de penetración:

$$\Delta x \leq \frac{1}{\kappa}. \qquad \text{(4.42)}$$

La partícula adquiere cierto momento $p$ debido a la medición de posición:

$$p \geq \frac{\hbar}{\Delta x} \geq \hbar \kappa. \qquad \text{(4.43)}$$

Debido a este momento inducido por la medición de posición, hay alguna contribución adicional $E'$ a la energía cinética

$$E' = \frac{p^2}{2m} \geq \frac{\hbar^2 \kappa^2}{2m} = V_0 - E, \qquad \text{(4.44)}$$

donde usamos (4.41). A partir de esta desigualdad encontramos que la energía total excederá $V_0$

$$E_{\text{tot}} = E + E' \geq E + (V_0 - E) = V_0. \qquad \text{(4.45)}$$

Aunque el argumento es heurístico, aporta cierta evidencia de que no se detectará energía cinética negativa para una partícula que se encuentre en la región prohibida.

*Sarah Geller transcribió las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare https://ocw.mit.edu

8.04 Física Cuántica I Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

# Apéndice: Lista de problemas 7 (Problem Set 7, 2016)

**Física Cuántica I (8.04), Primavera de 2016**

**Tarea 7**

Departamento de Física del MIT — Entrega: viernes 8 de abril de 2016, 12:00 del mediodía

1 de abril de 2016

**Lectura:** Griffiths, secciones 2.5 y 2.3.

## Problema 1

**Dos funciones delta** \[15 puntos\]

Considere una partícula de masa $m$ moviéndose en un potencial de doble pozo unidimensional

$$V(x) = -g\,\delta(x - a) - g\,\delta(x + a), \qquad g > 0.$$

1.  Encuentre las ecuaciones trascendentes para los valores propios de energía de los estados ligados del sistema. Represente gráficamente los niveles de energía en unidades de $\hbar^2/(ma^2)$ en función del parámetro adimensional $\lambda \equiv mag/\hbar^2$. Explique las características de la gráfica.

2.  En el límite de gran separación $2a$ entre los pozos, encuentre una fórmula sencilla para el desdoblamiento (splitting) entre el estado fundamental y el primer estado excitado.

## Problema 2

**Esbozando funciones de onda.** Griffiths 2.47, p. 87. \[10 puntos\]

En este problema debe intentar averiguar intuitivamente el aspecto de las soluciones. Es buena idea comprobar después su intuición con el método de disparo (shooting method) y el planteamiento del ion H$_2^+$.

## Problema 3

**Osciladores armónicos más allá de los puntos de retorno** \[10 puntos\]

Para los estados propios de energía del oscilador armónico simple con $n = 0, 1$ y $2$, calcule la probabilidad de que la coordenada $x$ tome un valor mayor que la amplitud de un oscilador clásico de la misma energía.

## Problema 4

**Cálculos con el oscilador armónico** \[15 puntos\]

1.  Calcule el valor esperado de $x^4$ en el estado propio de energía con número $n$.

2.  Calcule $\Delta x$ y $\Delta p$ en el estado propio de energía con número $n$. ¿Cuál es el valor del producto $\Delta x \, \Delta p$?

3.  Considere los polinomios $H_n(\xi)$ definidos por la función generatriz

$$e^{-s^2 + 2s\xi} = \sum_{n=0}^{\infty} H_n(\xi) \frac{s^n}{n!}.$$

Verifique que $H_n(\xi) = (2\xi)^n + \ldots$, donde los puntos suspensivos representan términos con potencias menores de $\xi$. Demuestre que los polinomios $H_n(\xi)$ así definidos satisfacen la ecuación diferencial de Hermite:

$$H_n'' - 2\xi H_n' + 2n H_n = 0.$$

## Problema 5

**Oscilador armónico y una pared.** Problema 2.42 de Griffiths, p. 86. \[5 puntos\]

## Problema 6

**¡El oscilador armónico oscilando!** \[10 puntos\]

Una partícula de masa $m$ en un oscilador armónico de frecuencia $\omega$ tiene una función de onda inicial, en el instante cero,

$$\Psi(x,0) = \frac{1}{\sqrt{2}}\Big(\varphi_0(x) + \varphi_1(x)\Big),$$

donde $\varphi_0$ y $\varphi_1$ son los estados propios normalizados del hamiltoniano con número propio cero y uno, respectivamente.

1.  Escriba $\Psi(x,t)$ y $|\Psi(x,t)|^2$. Puede dejar sus expresiones en términos de $\varphi_0$ y $\varphi_1$.

2.  Encuentre $\langle x \rangle$ en función del tiempo. ¿Cuál es la amplitud de esta oscilación y cuál es su frecuencia?

3.  Encuentre $\langle p \rangle$ en función del tiempo.

4.  Demuestre que, para cualquier estado del oscilador armónico, la distribución de probabilidad $|\Psi(x,t)|^2$ es igual a $|\Psi(x,t+T)|^2$ para $T = \dfrac{2\pi}{\omega}$.

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*
