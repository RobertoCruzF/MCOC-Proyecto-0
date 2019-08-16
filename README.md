# MCOC-Proyecto-0
Proyecto 0, Metodos Computacionales en IOC

Introducción
==============

Cuando se restan dos numeros que son parecidos, pero no iguales, dependiendo de la cantidad de decimales que tengan los numeros, se puede probocar o no perdida de significancia. En este codigo se presenta un ejemplo sobre este caso, mostrando cual es el limite de decimales que tiene que tener un numero de tal forma de que se provoque una perdida de significancia o no


Este ejemplo
==============

Se ejemplifican dos casos, en los que se restan dos numeros parecidos pero no iguales, y dependiendo de la cantidad de decimales que tienen los numeros, se proboca o no perdida de significancia.

Caso sin perdida de significancia (Numeros con 15 decimales):

Numero1:2.999999999999999
Numero2:2.999999999999998

Caso con perdida de significancia (Numeros con 16 decimales):

Numero1:2.9999999999999999
Numero2:2.9999999999999998



Resultados
==============

Se define el error relativo como 

	ERROR = (Promedio_Calculado - Resultado_Exacto) / Resultado_Exacto

Para el caso con numeros con 15 decimales, el computador calculó la resta correctamente, en cambio para el caso con los numeros de 16 decimales, la resta se aproximó a 0, provocandose una perdida de significancia.

Caso sin perdida de significancia (Numeros con 15 decimales):

Numero1: 2.999999999999999
Numero2: 2.999999999999998
Numero1 - Numero2: 1.33226762955e-15

Caso con perdida de significancia (Numeros con 16 decimales):

Numero1: 2.9999999999999999
Numero2: 2.9999999999999998
Numero1 - Numero2: 0.0