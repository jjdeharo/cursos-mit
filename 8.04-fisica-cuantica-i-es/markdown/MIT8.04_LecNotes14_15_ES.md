# Clases 14 y 15: Enfoque algebraico del oscilador armónico simple

## Vídeos de esta clase (YouTube)

**Lección 14: Simple harmonic oscillator II. Creation and annihilation operators.**

- [Recursion relation for the solution](https://www.youtube.com/watch?v=RxWfrE3o-9k)
- [Quantization of the energy](https://www.youtube.com/watch?v=Y6Ma-zn4Olk)
- [Algebraic solution of the harmonic oscillator](https://www.youtube.com/watch?v=8CCFPgd_P1w)
- [Ground state wavefunction](https://www.youtube.com/watch?v=vnyxYtj0mfE)

**Lección 15: Simple harmonic oscillator III. Scattering states and step potential.**

- [Number operator and commutators](https://www.youtube.com/watch?v=kefsxztSX74)
- [Excited states of the harmonic oscillator](https://www.youtube.com/watch?v=xmjvqbYvY9o)
- [Creation and annihilation operators acting on energy eigenstates](https://www.youtube.com/watch?v=BRFekCz4XQY)
- [Scattering states and the step potential](https://www.youtube.com/watch?v=0ABYYJSvkVk)

------------------------------------------------------------------------

*B. Zwiebach* *5 de abril de 2016*

## Contenido

1.  Solución algebraica del oscilador
2.  Manipulación de operadores y el espectro

## 1. Solución algebraica del oscilador

Ya hemos visto cómo calcular los autoestados de energía del oscilador armónico simple resolviendo una ecuación diferencial de segundo orden, la ecuación de Schrödinger independiente del tiempo.

Intentemos ahora factorizar el hamiltoniano del oscilador armónico. Con esto queremos decir, a grandes rasgos, escribir el hamiltoniano como el producto de un operador por su conjugado hermítico. Como primer paso, reescribimos el hamiltoniano como

$$\hat{H} = \tfrac{1}{2} m\omega^2 \left(\hat{x}^2 + \frac{\hat{p}^2}{m^2\omega^2}\right) \qquad \text{(1.1)}$$

Motivados por la identidad $a^2 + b^2 = (a-ib)(a+ib)$, válida para números $a$ y $b$, examinamos si la expresión entre paréntesis se puede escribir como un producto

$$\left(\hat{x} - \frac{i\hat{p}}{m\omega}\right)\left(\hat{x} + \frac{i\hat{p}}{m\omega}\right) = \hat{x}^2 + \frac{\hat{p}^2}{m^2\omega^2} + \frac{i}{m\omega}(\hat{x}\hat{p} - \hat{p}\hat{x}),$$

$$= \hat{x}^2 + \frac{\hat{p}^2}{m^2\omega^2} - \frac{\hbar}{m\omega}\mathbb{1}, \qquad \text{(1.2)}$$

donde los términos adicionales surgen porque $\hat{x}$ y $\hat{p}$, a diferencia de los números, no conmutan. Definimos ahora el factor situado más a la derecha en el producto anterior como $V$:

$$V \equiv \hat{x} + \frac{i\hat{p}}{m\omega}, \qquad \text{(1.3)}$$

Dado que $\hat{x}$ y $\hat{p}$ son operadores hermíticos, tenemos entonces

$$V^\dagger = \hat{x} - \frac{i\hat{p}}{m\omega}, \qquad \text{(1.4)}$$

¡y este es el factor situado más a la izquierda en el producto! Por lo tanto podemos reescribir (1.2) como

$$\hat{x}^2 + \frac{\hat{p}^2}{m^2\omega^2} = V^\dagger V + \frac{\hbar}{m\omega}\mathbb{1}, \qquad \text{(1.5)}$$

y por lo tanto, volviendo al hamiltoniano (1.1), encontramos

$$\hat{H} = \tfrac{1}{2}m\omega^2 V^\dagger V + \tfrac{1}{2}\hbar\omega\mathbb{1}. \qquad \text{(1.6)}$$

Esta es una forma factorizada del hamiltoniano: salvo por una constante aditiva $E_0$, $\hat{H}$ es el producto de una constante positiva por el producto de operadores $V^\dagger V$. Notamos que el conmutador de $V$ y $V^\dagger$ es simple

$$\left[V, V^\dagger\right] = \left[\hat{x} + \frac{i\hat{p}}{m\omega}, \hat{x} - \frac{i\hat{p}}{m\omega}\right] = -\frac{i}{m\omega}[\hat{x},\hat{p}] + \frac{i}{m\omega}[\hat{p},\hat{x}] = \frac{2\hbar}{m\omega}\mathbb{1}. \qquad \text{(1.7)}$$

Esto implica que

$$\left[\sqrt{\frac{m\omega}{2\hbar}}\, V,\ \sqrt{\frac{m\omega}{2\hbar}}\, V^\dagger\right] = \mathbb{1}. \qquad \text{(1.8)}$$

Esto sugiere la definición de los operadores adimensionales $\hat{a}$ y $\hat{a}^\dagger$:

$$\hat{a} \equiv \sqrt{\frac{m\omega}{2\hbar}}\, V,$$

$$\hat{a}^\dagger \equiv \sqrt{\frac{m\omega}{2\hbar}}\, V^\dagger. \qquad \text{(1.9)}$$

Debido al reescalamiento tenemos

$$\left[\hat{a}, \hat{a}^\dagger\right] = 1. \qquad \text{(1.10)}$$

El operador $\hat{a}$ se denomina operador de aniquilación y $\hat{a}^\dagger$ se denomina operador de creación. La justificación de estos nombres se verá más adelante. A partir de las definiciones anteriores leemos las relaciones entre $(\hat{a}, \hat{a}^\dagger)$ y $(\hat{x}, \hat{p})$:

$$\hat{a} = \sqrt{\frac{m\omega}{2\hbar}}\left(\hat{x} + \frac{i\hat{p}}{m\omega}\right),$$

$$\hat{a}^\dagger = \sqrt{\frac{m\omega}{2\hbar}}\left(\hat{x} - \frac{i\hat{p}}{m\omega}\right). \qquad \text{(1.11)}$$

Las relaciones inversas también son útiles muchas veces,

$$\hat{x} = \sqrt{\frac{\hbar}{2m\omega}}\left(\hat{a} + \hat{a}^\dagger\right),$$

$$\hat{p} = i\sqrt{\frac{m\omega\hbar}{2}}\left(\hat{a}^\dagger - \hat{a}\right). \qquad \text{(1.12)}$$

Aunque ni $\hat{a}$ ni $\hat{a}^\dagger$ son hermíticos (son conjugados hermíticos el uno del otro), las ecuaciones anteriores son consistentes con la hermiticidad de $\hat{x}$ y $\hat{p}$. Ahora podemos escribir el hamiltoniano en términos de los operadores $\hat{a}$ y $\hat{a}^\dagger$. Usando (1.9) tenemos

$$V^\dagger V = \frac{2\hbar}{m\omega}\hat{a}^\dagger \hat{a}, \qquad \text{(1.13)}$$

y por lo tanto, volviendo a (1.6), obtenemos

$$\hat{H} = \hbar\omega\left(\hat{a}^\dagger \hat{a} + \tfrac{1}{2}\right) = \hbar\omega\left(\hat{N} + \tfrac{1}{2}\right), \qquad \hat{N} \equiv \hat{a}^\dagger \hat{a}. \qquad \text{(1.14)}$$

La forma anterior del hamiltoniano está factorizada: salvo por una constante aditiva, $\hat{H}$ es el producto de una constante positiva por el producto de operadores $\hat{a}^\dagger \hat{a}$. Aquí hemos omitido el operador identidad, lo cual suele sobreentenderse. También hemos introducido el operador número $\hat{N}$. Este es, por construcción, un operador hermítico, y es, salvo una escala y una constante aditiva, igual al hamiltoniano. Un autoestado de $\hat{H}$ es también un autoestado de $\hat{N}$, y de la relación anterior se sigue que los correspondientes autovalores $E$ y $N$ están relacionados por

$$E = \hbar\omega\left(N + \tfrac{1}{2}\right). \qquad \text{(1.15)}$$

Mostremos ahora las poderosas conclusiones que surgen del hamiltoniano factorizado. Sobre cualquier estado $\psi$ normalizado tenemos

$$\langle \hat{H} \rangle_\psi = (\psi, \hat{H}\psi) = \hbar\omega\, (\psi, \hat{a}^\dagger \hat{a}\psi) + \tfrac{1}{2}\hbar\omega\,(\psi,\psi), \qquad \text{(1.16)}$$

y trasladando el $\hat{a}^\dagger$ a la primera entrada, obtenemos

$$\langle \hat{H} \rangle_\psi = \hbar\omega\, (\hat{a}\psi, \hat{a}\psi) + \tfrac{1}{2}\hbar\omega \geq \tfrac{1}{2}\hbar\omega. \qquad \text{(1.17)}$$

La desigualdad se sigue del hecho de que cualquier expresión de la forma $(\varphi,\varphi)$ es mayor o igual que cero. Esto muestra que para cualquier autoestado de energía con energía $E$: $\hat{H}\psi = E\psi$ tenemos

$$\text{Autoestados de energía: } E \geq \tfrac{1}{2}\hbar\omega. \qquad \text{(1.18)}$$

Este importante resultado sobre el espectro se sigue directamente de la factorización del hamiltoniano. Pero también obtenemos la información necesaria para hallar la función de onda del estado fundamental. La energía mínima $\tfrac{1}{2}\hbar\omega$ se realizará para un estado $\psi$ si el término $(\hat{a}\psi, \hat{a}\psi)$ en (1.17) se anula. Para que esto se anule, $\hat{a}\psi$ debe anularse. Por lo tanto, la función de onda del estado fundamental $\varphi_0$ debe satisfacer

$$\hat{a}\, \varphi_0 = 0. \qquad \text{(1.19)}$$

El operador $\hat{a}$ aniquila el estado fundamental, y esta es la razón por la que $\hat{a}$ se llama operador de aniquilación. Usando la definición de $\hat{a}$ en (1.11) y la representación en el espacio de posiciones de $\hat{p}$, esto se convierte en

$$\left(x + \frac{i}{m\omega}\frac{\hbar}{i}\frac{d}{dx}\right)\varphi_0(x) = 0 \ \longrightarrow\ \left(x + \frac{\hbar}{m\omega}\frac{d}{dx}\right)\varphi_0(x) = 0. \qquad \text{(1.20)}$$

Notablemente, esta es una ecuación diferencial de primer orden para el estado fundamental. No es una ecuación de segundo orden, como la ecuación de Schrödinger que determina los autoestados de energía en general. Esta es una simplificación drástica que ofrece la factorización del hamiltoniano en un producto de operadores diferenciales de primer orden. La ecuación anterior se reordena como

$$\frac{d\varphi_0}{dx} = -\frac{m\omega}{\hbar}\, x\, \varphi_0. \qquad \text{(1.21)}$$

Resolviendo esta ecuación diferencial se obtiene

$$\varphi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4} e^{-\frac{m\omega}{2\hbar}x^2}, \qquad \text{(1.22)}$$

donde hemos incluido una constante de normalización para garantizar que $(\varphi_0, \varphi_0) = 1$. Nótese que $\varphi_0$ es en efecto un autoestado de energía con energía $E_0$:

$$\hat{H}\varphi_0 = \hbar\omega\left(\hat{a}^\dagger \hat{a} + \tfrac{1}{2}\right)\varphi_0 = \tfrac{1}{2}\hbar\omega\,\varphi_0 \ \longrightarrow\ E_0 = \tfrac{1}{2}\hbar\omega. \qquad \text{(1.23)}$$

Antes de continuar con el análisis de los estados excitados, examinemos las propiedades de la factorización de manera más general. Factorizar un hamiltoniano significa hallar un operador $\hat{A}$ tal que podamos reescribir el hamiltoniano como $\hat{A}^\dagger \hat{A}$ salvo una constante aditiva. Aquí $\hat{A}^\dagger$ es el conjugado hermítico de $\hat{A}$, un operador que se define mediante

$$(\psi, \hat{A}^\dagger \varphi) = (\hat{A}\psi, \varphi). \qquad \text{(1.24)}$$

Decimos que hemos factorizado un hamiltoniano $\hat{H}$ si podemos encontrar un $\hat{A}$ para el cual

$$\hat{H} = \hat{A}^\dagger \hat{A} + E_0\, \mathbb{1}, \qquad \text{(1.25)}$$

donde $E_0$ es una constante con unidades de energía que multiplica al operador identidad. Esta constante no complica nuestra tarea de hallar los autoestados del hamiltoniano ni sus energías: cualquier autofunción de $\hat{A}^\dagger \hat{A}$ es una autofunción de $\hat{H}$. De la factorización (1.25) se siguen dos propiedades clave.

1.  Cualquier autoestado de energía debe tener una energía mayor o igual que $E_0$. Primero notemos que para un $\psi(x)$ normalizado arbitrario tenemos

$$(\psi, \hat{H}\psi) = (\psi, \hat{A}^\dagger \hat{A}\psi) + E_0 (\psi,\psi) = (\hat{A}\psi, \hat{A}\psi) + E_0, \qquad \text{(1.26)}$$

Dado que el solapamiento $(\hat{A}\psi, \hat{A}\psi)$ es mayor o igual que cero, hemos demostrado que

$$(\psi, \hat{H}\psi) \geq E_0. \qquad \text{(1.27)}$$

Si tomamos $\psi$ como un autoestado de energía con energía $E$: $\hat{H}\psi = E\psi$, la relación anterior nos da

$$E \geq E_0. \qquad \text{(1.28)}$$

Esto demuestra, como se afirmó, que todas las energías posibles son mayores o iguales que $E_0$.

1.  Una función de onda $\psi_0$ que satisface

$$\hat{A}\, \psi_0 = 0, \qquad \text{(1.29)}$$

es un autoestado de energía que satura la desigualdad (1.28). En efecto,

$$\hat{H}\psi_0 = \hat{A}^\dagger \hat{A}\, \psi_0 + E_0 \psi_0 = \hat{A}^\dagger (\hat{A}\, \psi_0) + E_0 \psi_0 = E_0 \psi_0. \qquad \text{(1.30)}$$

El estado $\psi_0$ que satisface $\hat{A}\, \psi_0 = 0$ es el estado fundamental. Para hamiltonianos convencionales esta es una ecuación diferencial de primer orden para $\psi_0$, y mucho más fácil de resolver que la ecuación de Schrödinger.

## 2. Manipulación de operadores y el espectro

Hemos visto que todos los autoestados de energía son autoestados del operador número hermítico $\hat{N} = \hat{a}^\dagger \hat{a}$. Esto se debe a que $\hat{H} = \hbar\omega\left(\hat{N} + \tfrac{1}{2}\right)$. Nótese que, como $\hat{a}\varphi_0 = 0$, también tenemos

$$\hat{N}\varphi_0 = 0. \qquad \text{(2.1)}$$

Podemos comprobar rápidamente que

$$\left[\hat{N}, \hat{a}\right] = \left[\hat{a}^\dagger \hat{a}, \hat{a}\right] = \left[\hat{a}^\dagger, \hat{a}\right]\hat{a} = -\hat{a},$$

$$\left[\hat{N}, \hat{a}^\dagger\right] = \left[\hat{a}^\dagger \hat{a}, \hat{a}^\dagger\right] = \hat{a}^\dagger \left[\hat{a}, \hat{a}^\dagger\right] = \hat{a}^\dagger, \qquad \text{(2.2)}$$

que resumimos como

$$\left[\hat{N}, \hat{a}\right] = -\hat{a},$$

$$\left[\hat{N}, \hat{a}^\dagger\right] = \hat{a}^\dagger. \qquad \text{(2.3)}$$

Usando estas identidades y por inducción se debería poder demostrar que:

$$\left[\hat{N}, (\hat{a})^k\right] = -k(\hat{a})^k,$$

$$\left[\hat{N}, (\hat{a}^\dagger)^k\right] = k(\hat{a}^\dagger)^k. \qquad \text{(2.4)}$$

Estas relaciones sugieren por qué $\hat{N}$ se llama operador número. Al actuar por conmutación sobre potencias de operadores de creación o de aniquilación, se obtiene el mismo objeto multiplicado por (más o menos) el número de operadores de creación o de aniquilación, $k$ en lo anterior. Los siguientes conmutadores relacionados también son útiles:

$$\left[\hat{a}^\dagger, (\hat{a})^k\right] = -k(\hat{a})^{k-1}$$

$$\left[\hat{a}, (\hat{a}^\dagger)^k\right] = k(\hat{a}^\dagger)^{k-1}. \qquad \text{(2.5)}$$

Estos conmutadores son análogos a $[\hat{p}, (\hat{x})^k]$ y $[\hat{x}, (\hat{p})^k]$. También haremos uso del siguiente lema, que ayuda en las evaluaciones donde tenemos un operador $\hat{A}$ que anula un estado $\psi$ y queremos simplificar la acción de $\hat{A}\hat{B}$, donde $\hat{B}$ es otro operador, actuando sobre $\psi$. Este es el resultado

$$\text{Si } \hat{A}\,\psi = 0, \text{ entonces } \hat{A}\hat{B}\,\psi = \left[\hat{A}, \hat{B}\right]\psi. \qquad \text{(2.6)}$$

Esto se demuestra fácilmente. Primero notemos que

$$\hat{A}\hat{B} = \left[\hat{A}, \hat{B}\right] + \hat{B}\hat{A}, \qquad \text{(2.7)}$$

como se puede comprobar rápidamente expandiendo el lado derecho. De ahí se sigue que

$$\hat{A}\hat{B}\,\psi = \left(\left[\hat{A}, \hat{B}\right] + \hat{B}\hat{A}\right)\psi = \left[\hat{A}, \hat{B}\right]\psi, \qquad \text{(2.8)}$$

porque $\hat{B}\hat{A}\,\psi = \hat{B}(\hat{A}\psi) = 0$. Esto es lo que queríamos demostrar. Esto es todo lo que necesitamos saber sobre conmutadores, y ahora podemos proceder a construir los estados del oscilador armónico.

Dado que $\hat{a}$ aniquila $\varphi_0$, consideremos actuar sobre el estado fundamental con $\hat{a}^\dagger$. Es claro que $\hat{a}^\dagger$ no puede también aniquilar $\varphi_0$. Si esto sucediera, actuar con ambos lados de la identidad del conmutador $\left[\hat{a}, \hat{a}^\dagger\right] = 1$ sobre $\varphi_0$ llevaría a una contradicción: el lado izquierdo se anularía pero el lado derecho no. Por lo tanto, consideremos la función de onda

$$\varphi_1 \equiv \hat{a}^\dagger \varphi_0. \qquad \text{(2.9)}$$

Vamos a demostrar que este es un autoestado de energía. Para ello actuamos sobre él con el operador número:

$$\hat{N}\varphi_1 = \hat{N}\hat{a}^\dagger \varphi_0 = \left[\hat{N}, \hat{a}^\dagger\right]\varphi_0, \qquad \text{(2.10)}$$

donde notamos que $\hat{N}\varphi_0 = 0$ y usamos el lema (2.6). Dado que $\left[\hat{N}, \hat{a}^\dagger\right] = \hat{a}^\dagger$, obtenemos

$$\hat{N}\varphi_1 = \hat{a}^\dagger \varphi_0 = \varphi_1. \qquad \text{(2.11)}$$

Por lo tanto $\varphi_1$ es un autoestado del operador $\hat{N}$ con autovalor $N=1$. Dado que $\varphi_0$ tiene autovalor de $\hat{N}$ igual a cero, el efecto de actuar sobre $\varphi_0$ con $\hat{a}^\dagger$ fue aumentar el autovalor del operador número en una unidad. El operador $\hat{a}^\dagger$ se llama operador de creación porque crea un estado a partir del estado fundamental. Alternativamente, se le llama operador de subida (o ascenso), porque sube (en una unidad) el autovalor de $\hat{N}$. Dado que $N=1$ para $\varphi_1$, se sigue que $\varphi_1$ es un autoestado de energía con energía $E_1$ dada por

$$E_1 = \hbar\omega\left(1 + \tfrac{1}{2}\right) = \tfrac{3}{2}\hbar\omega. \qquad \text{(2.12)}$$

Resulta también que $\varphi_1$ está correctamente normalizado:

$$(\varphi_1, \varphi_1) = (\hat{a}^\dagger \varphi_0, \hat{a}^\dagger \varphi_0) = (\varphi_0, \hat{a}\hat{a}^\dagger \varphi_0), \qquad \text{(2.13)}$$

donde usamos la propiedad de conjugación hermítica para trasladar el $\hat{a}^\dagger$ que actúa sobre la entrada izquierda hacia la entrada derecha, donde se convierte en $(\hat{a}^\dagger)^\dagger = \hat{a}$. Tenemos entonces

$$(\varphi_1, \varphi_1) = (\varphi_0, \hat{a}\hat{a}^\dagger \varphi_0) = (\varphi_0, \left[\hat{a}, \hat{a}^\dagger\right]\varphi_0) = (\varphi_0, \varphi_0) = 1, \qquad \text{(2.14)}$$

donde usamos (2.6) en la evaluación de $\hat{a}\hat{a}^\dagger \psi_0$. En efecto, el estado $\varphi_1$ está correctamente normalizado.

A continuación consideremos el estado

$$\varphi_2' \equiv \hat{a}^\dagger \hat{a}^\dagger \varphi_0. \qquad \text{(2.15)}$$

Este tiene

$$\hat{N}\varphi_2' = \hat{N}\hat{a}^\dagger \hat{a}^\dagger \varphi_0 = \left[\hat{N}, \hat{a}^\dagger \hat{a}^\dagger\right]\varphi_0 = 2\hat{a}^\dagger \hat{a}^\dagger \varphi_0 = 2\varphi_2', \qquad \text{(2.16)}$$

de modo que $\varphi_2$ es un estado con número $N=2$ y energía $E_2 = \tfrac{5}{2}\hbar\omega$. ¿Está correctamente normalizado? Encontramos

$$(\varphi_2', \varphi_2') = (\hat{a}^\dagger \hat{a}^\dagger \varphi_0, \hat{a}^\dagger \hat{a}^\dagger \varphi_0) = (\varphi_0, \hat{a}\hat{a}\hat{a}^\dagger \hat{a}^\dagger \varphi_0) = (\varphi_0, \hat{a}\left[\hat{a}, \hat{a}^\dagger\right]\hat{a}^\dagger \varphi_0)$$

$$= (\varphi_0, 2\hat{a}\hat{a}^\dagger \varphi_0) = 2(\varphi_0, \varphi_0) = 2. \qquad \text{(2.17)}$$

La función de onda correctamente normalizada es entonces

$$\varphi_2 \equiv \frac{1}{\sqrt{2}}\,\hat{a}^\dagger \hat{a}^\dagger \varphi_0. \qquad \text{(2.18)}$$

Afirmamos ahora que el $n$-ésimo estado excitado del oscilador armónico simple es

$$\varphi_n \equiv \frac{1}{\sqrt{n!}}\underbrace{\hat{a}^\dagger \cdots \hat{a}^\dagger}_{n}\,\varphi_0 = \frac{1}{\sqrt{n!}}\left(\hat{a}^\dagger\right)^n \varphi_0. \qquad \text{(2.19)}$$

**Ejercicio.** Verifique que este estado tiene autovalor de $\hat{N}$ igual a $n$.

**Ejercicio.** Verifique que el estado $\varphi_n$ está correctamente normalizado.

Dado que el autovalor de $\hat{N}$ de $\varphi_n$ es $n$, su energía $E_n$ está dada por

$$E_n = \hbar\omega\left(n + \tfrac{1}{2}\right). \qquad \text{(2.20)}$$

Dado que los distintos estados $\varphi_n$ son autoestados de un operador hermítico (el hamiltoniano $\hat{H}$) con autovalores diferentes, son ortonormales

$$(\varphi_n, \varphi_m) = \delta_{m,n}. \qquad \text{(2.21)}$$

Notamos ahora que $\hat{a}\varphi_n$ es un estado con $n-1$ operadores $\hat{a}^\dagger$ actuando sobre $\varphi_0$, porque el $\hat{a}$ elimina uno de los operadores de creación en $\varphi_n$. Así pues, esperamos que $\hat{a}\varphi_n \sim \varphi_{n-1}$. Podemos precisar esto

$$\hat{a}\, \varphi_n = \hat{a}\, \frac{1}{\sqrt{n!}}\left(\hat{a}^\dagger\right)^n \varphi_0 = \frac{1}{\sqrt{n!}}\left[\hat{a}, \left(\hat{a}^\dagger\right)^n\right]\varphi_0 = \frac{n}{\sqrt{n!}}\left(\hat{a}^\dagger\right)^{n-1}\varphi_0. \qquad \text{(2.22)}$$

En este punto usamos (2.19) con $n$ reemplazado por $n-1$ y así obtenemos

$$\hat{a}\,\varphi_n = \frac{n}{\sqrt{n!}}\sqrt{(n-1)!}\,\varphi_{n-1} = \sqrt{n}\,\varphi_{n-1}. \qquad \text{(2.23)}$$

Mediante la acción de $\hat{a}^\dagger$ sobre $\varphi_n$ obtenemos

$$\hat{a}^\dagger \varphi_n = \frac{1}{\sqrt{n!}}\left(\hat{a}^\dagger\right)^{n+1}\varphi_0 = \frac{1}{\sqrt{n!}}\sqrt{(n+1)!}\,\varphi_{n+1} = \sqrt{n+1}\,\varphi_{n+1}. \qquad \text{(2.24)}$$

Recopilando los resultados, tenemos

$$\hat{a}\,\varphi_n = \sqrt{n}\,\varphi_{n-1},$$

$$\hat{a}^\dagger \varphi_n = \sqrt{n+1}\,\varphi_{n+1}. \qquad \text{(2.25)}$$

Estas relaciones dejan claro que $\hat{a}$ reduce en una unidad el número de cualquier autoestado de energía, excepto el vacío $\varphi_0$, al cual aniquila. El operador de subida $\hat{a}^\dagger$ aumenta en una unidad el número de cualquier autoestado.

**Ejercicio.** Calcule la incertidumbre $\Delta x$ de la posición en el $n$-ésimo autoestado de energía.

**Solución.** Por definición,

$$(\Delta x)_n^2 = \langle \hat{x}^2 \rangle_{\varphi_n} - \langle \hat{x} \rangle_{\varphi_n}^2. \qquad \text{(2.26)}$$

El valor esperado $\langle \hat{x} \rangle$ se anula para cualquier autoestado de energía, ya que estamos integrando $x$, que es impar, frente a $|\varphi_n(x)|^2$, que siempre es par. Aun así, es instructivo ver cómo sucede esto explícitamente:

$$\langle \hat{x} \rangle_{\varphi_n} = (\varphi_n, \hat{x}\varphi_n) = \sqrt{\frac{\hbar}{2m\omega}}\,(\varphi_n, (\hat{a} + \hat{a}^\dagger)\varphi_n), \qquad \text{(2.27)}$$

usando la fórmula de $\hat{x}$ en términos de $\hat{a}$ y $\hat{a}^\dagger$. El solapamiento anterior se anula porque $\hat{a}\varphi_n \sim \varphi_{n-1}$ y $\hat{a}^\dagger \varphi_n \sim \varphi_{n+1}$, y tanto $\varphi_{n-1}$ como $\varphi_{n+1}$ son ortogonales a $\varphi_n$. Ahora calculamos el valor esperado de $\hat{x}^2$

$$\langle \hat{x}^2 \rangle_{\varphi_n} = (\varphi_n, \hat{x}^2 \varphi_n) = \frac{\hbar}{2m\omega}\,(\varphi_n, (\hat{a} + \hat{a}^\dagger)(\hat{a} + \hat{a}^\dagger)\varphi_n)$$

$$= \frac{\hbar}{2m\omega}\,(\varphi_n, (\hat{a}\hat{a} + \hat{a}\hat{a}^\dagger + \hat{a}^\dagger \hat{a} + \hat{a}^\dagger \hat{a}^\dagger)\varphi_n). \qquad \text{(2.28)}$$

Dado que $\hat{a}\hat{a}\varphi_n \sim \varphi_{n-2}$ y $\hat{a}^\dagger \hat{a}^\dagger \varphi_n \sim \varphi_{n+2}$, y tanto $\varphi_{n-2}$ como $\varphi_{n+2}$ son ortogonales a $\varphi_n$, los términos $\hat{a}\hat{a}$ y $\hat{a}^\dagger \hat{a}^\dagger$ no contribuyen. Nos queda

$$\langle \hat{x}^2 \rangle_{\varphi_n} = \frac{\hbar}{2m\omega}\,(\varphi_n, (\hat{a}\hat{a}^\dagger + \hat{a}^\dagger \hat{a})\varphi_n). \qquad \text{(2.29)}$$

En este punto reconocemos que $\hat{a}^\dagger \hat{a} = \hat{N}$ y que $\hat{a}\hat{a}^\dagger = \left[\hat{a}, \hat{a}^\dagger\right] + \hat{a}^\dagger \hat{a} = 1 + \hat{N}$. Como resultado

$$\langle \hat{x}^2 \rangle_{\varphi_n} = \frac{\hbar}{2m\omega}\,(\varphi_n, (1 + 2\hat{N})\varphi_n) = \frac{\hbar}{2m\omega}(1 + 2n). \qquad \text{(2.30)}$$

Por lo tanto tenemos

$$(\Delta x)_n^2 = \frac{\hbar}{m\omega}\left(n + \tfrac{1}{2}\right). \qquad \text{(2.31)}$$

La incertidumbre en la posición crece linealmente con el número.

------------------------------------------------------------------------

*Sarah Geller y Andrew Turner transcribieron las notas manuscritas de Zwiebach para crear la primera versión en LaTeX de este documento.*

------------------------------------------------------------------------

MIT OpenCourseWare https://ocw.mit.edu

8.04 Física Cuántica I Primavera de 2016

Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: https://ocw.mit.edu/terms.

# Apéndice: Lista de problemas 6 (Problem Set 6, 2016)

**Departamento de Física del MIT — Física Cuántica I (8.04), primavera de 2016**

**Fecha de publicación:** 17 de marzo de 2016. **Fecha de entrega:** viernes 1 de abril de 2016, 12:00 del mediodía.

**Lectura:** Griffiths, sección 2.6. Para la semana siguiente, secciones 2.5 y 2.3.

## Problema 1

**Partícula en un pozo cuadrado. \[10 puntos\]**

Una partícula de masa $m$ se mueve en un pozo cuadrado infinito de anchura $a$. Su función de onda en el instante $t=0$ es

$$\Psi(x,0) = \sqrt{\frac{1}{3}}\sqrt{\frac{2}{a}}\sin\left(\frac{2\pi x}{a}\right) + \sqrt{\frac{2}{3}}\sqrt{\frac{2}{a}}\sin\left(\frac{3\pi x}{a}\right).$$

1.  ¿Es $\Psi$ un autoestado de energía? Encuentre $\Psi(x,t)$.

2.  ¿Cuáles son las probabilidades de que una medida de la energía en el instante $t$ dé cada uno de los siguientes valores?

$$\frac{\hbar^2\pi^2}{2ma^2},\qquad \frac{4\hbar^2\pi^2}{2ma^2},\qquad \frac{9\hbar^2\pi^2}{2ma^2}.$$

1.  ¿Cuál es el valor esperado de $x$ en el instante $t$?

2.  ¿Cuál es el valor esperado de $p$ en el instante $t$?

## Problema 2

**No degeneración de los estados ligados en una dimensión \[10 puntos\]**

Problema 2.45 de Griffiths, p. 87.

## Problema 3

**Pozo rectangular infinito en el plano \[10 puntos\]**

Considere una partícula de masa $m$ que se mueve en el plano $x,y$ con un potencial que es nulo dentro de la caja rectangular formada por todos los puntos $(x,y)$ para los cuales

$$0 \le x \le L_x,\qquad 0 \le y \le L_y,$$

y es infinito en cualquier otro punto.

1.  Use la ecuación de Schrödinger bidimensional para hallar los autoestados de energía. Dé las energías y las autofunciones normalizadas.

2.  Considere el caso $L_x = L_y = L$. Verá que hay degeneraciones en el espectro de energía. Algunas degeneraciones tienen una explicación de simetría sencilla; identifíquelas y explique por qué ocurren. Algunas degeneraciones son accidentales; parecen aleatorias. Muestre algunos ejemplos. \[Pista: $49+1 = 25+25$\].

3.  Demuestre que siempre que $(L_x/L_y)^2$ sea irracional no hay degeneraciones.

## Problema 4

**Un pozo cuadrado infinito con un escalón \[10 puntos\]**

Una partícula de masa $m$ se mueve en una dimensión, sometida al potencial $V(x)$:

$$V(x) =
\begin{cases}
\infty, & \text{para } x < 0, \\
0, & \text{para } 0 < x < a, \\
V_0, & \text{para } a < x < 2a,\quad (V_0 > 0) \\
\infty, & \text{para } x > 2a.
\end{cases}$$

1.  Encuentre las ecuaciones que determinan los estados estacionarios con energías $0 < E < V_0$. Para ello definimos

$$k^2 \equiv \frac{2mE}{\hbar^2},\qquad \kappa^2 \equiv \frac{2m(V_0-E)}{\hbar^2},\qquad z_0^2 = \frac{2ma^2V_0}{\hbar^2},\qquad \eta \equiv ka,\qquad \xi \equiv \kappa a.$$

(Usamos $k$ para las regiones clásicamente permitidas y $\kappa$ para las regiones clásicamente prohibidas). Sus ecuaciones deberían poder escribirse en términos de $\xi$, $\eta$ y $z_0$.

1.  Como aplicación numérica, considere $z_0 = 2\pi$. ¿Cuántos estados obtiene con $E < V_0$? Halle los valores posibles de la energía $E$ en términos de $V_0$ (use al menos 4 cifras significativas).

## Problema 5

**Método de disparo (shooting method) y aplicación \[15 puntos\]**

Para una partícula en un potencial cuártico $V(x) \sim x^4$, tras reescalar $x$ en una variable adimensional $u$, la ecuación de Schrödinger toma la forma

$$-\frac{1}{2}\frac{d^2\psi}{du^2} + (u^4 - e)\psi = 0,$$

donde $e$ es una medida adimensional del autovalor de energía. A continuación se dan las instrucciones de Mathematica que permiten hallar los valores de $e$ para las soluciones pares de este potencial. Estas instrucciones producen una gráfica de la solución $\psi(u)$, para $u \in [0, 3.5]$, con unas condiciones iniciales adecuadas y para el valor elegido de la energía $e$.

    Clear[e, psi]
    v[x_]:= x^4
    e=0.65;
    psi = psi/. NDSolve[{-(1/2)psi''[u] + (v[u]-e)psi[u]==0, psi[0]==1,
      psi'[0]==0}, psi, {u, 0, 3.5}][[1]];
    Plot[psi[u], {u, 0, 3.5}]

Tras ejecutar estas instrucciones, si escribe `psi[0.5]`, por ejemplo, el programa devolverá el valor de $\psi$ en $u=0.5$.

Juegue con esto para familiarizarse. El valor inicial de $e$ fijado arriba es 0.65, pero la energía del estado fundamental, como puede averiguar por prueba y error, es un poco más alta.

Retomamos ahora el problema anterior: una partícula de masa $m$ en un pozo cuadrado infinito con un escalón. De nuevo, tomamos $z_0 = 2\pi$. Encontró dos estados ligados con $E < V_0$:

$$E_1 = 0.\#\#436\, V_0,\qquad E_2 = 0.\#\#747\, V_0.$$

1.  Use $x = au$, con $u \in [0,2]$ adimensional, y escriba $V = V_0 f(u)$ para una función $f(u)$ adecuadamente definida, con el fin de obtener una ecuación diferencial para los autoestados de energía en la que no aparezcan unidades y el autovalor de energía quede codificado por el número puro $e = E/V_0$. Ponga a prueba su ecuación diferencial con el método de disparo para recuperar los valores anteriores de $E_1$ y $E_2$. Halle los dos siguientes niveles de energía $E_3$ y $E_4$.

2.  Discutimos en clase el hecho de que, para potenciales que varían lentamente, la amplitud de la función de onda es aproximadamente proporcional a la raíz cuadrada de la longitud de onda de de Broglie “local”. Nuestro potencial, al tener un escalón, no varía realmente de forma lenta, pero aun así podemos ver numéricamente hasta qué punto se cumple esta propiedad.

Construya el autoestado de energía con 8 nodos (el octavo estado excitado) y determine su energía. Sean $A_L$ y $A_R$ las amplitudes de su función de onda en los lados izquierdo y derecho del pozo cuadrado. Lea el cociente $A_L/A_R$ de su función de onda y compárelo con la predicción para este cociente usando la longitud de onda de de Broglie.

## Problema 6

**Ion de hidrógeno usando el modelo del pozo cuadrado. \[10 puntos\]**

La última vez modelamos el tamaño del átomo de hidrógeno y la energía de su estado fundamental

$$a_0 = \frac{\hbar^2}{me^2},\qquad E_0 = -\frac{e^2}{2a_0} = -13.6\ \text{eV},$$

usando el potencial de pozo cuadrado

$$V(x) =
\begin{cases}
-V_0, & \text{para } |x| < a_0,\quad V_0 > 0, \\
0, & \text{para } |x| > a_0.
\end{cases}$$

Anteriormente encontró que este pozo tiene

$$z_0 = 1.3192,\qquad V_0 = z_0^2 |E_0| = 1.7402\, |E_0| = 23.67\ \text{eV}.$$

El potencial de pozo cuadrado imita el potencial creado por el protón, y la energía del estado fundamental es la energía del electrón en dicho potencial.

Para simular el ion de hidrógeno $H_2^+$ (2 protones, 1 electrón) construiremos un potencial par con dos modelos idénticos de pozo cuadrado de hidrógeno separados por una pequeña distancia $2\gamma a_0$, donde $\gamma$ es una constante positiva adimensional pequeña. El potencial es por tanto

$$V(x) =
\begin{cases}
0, & \text{para } |x| < \gamma a_0, \\
-V_0, & \text{para } \gamma a_0 < |x| < (2+\gamma)a_0,\quad V_0 > 0, \\
0, & \text{para } |x| > (2+\gamma)a_0.
\end{cases}$$

Para concretar, trabaje con $\gamma = 0.2$.

1.  Use el método de disparo para hallar la energía del autoestado de menor energía, es decir, la energía del estado ligado de un electrón compartido por los dos protones. Muestre la función de onda del electrón a partir de la gráfica de su solución.

2.  La energía de enlace del ion se obtiene sumando la energía positiva debida a la repulsión de los dos protones a la energía del estado fundamental anterior. ¿Qué energía de enlace obtiene? ¿Cómo se compara con el valor experimental?

------------------------------------------------------------------------

*MIT OpenCourseWare* *<https://ocw.mit.edu>*

*8.04 Física Cuántica I* *Primavera de 2016*

*Para obtener información sobre cómo citar estos materiales o sobre nuestras condiciones de uso, visite: <https://ocw.mit.edu/terms>.*
