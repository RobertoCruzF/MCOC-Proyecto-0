#Se definen dos numeros casi iguales, los cuales al restarlos
#dan como resulado 0, lo cual es erroneo, dado que no son iguales

import scipy as sp
import matplotlib.pylab as plt
import sys



# CASO SIN PERDIDA DE SIGNIFICANCIA

a= 2.999999999999999 # 15 decimales
b= 2.999999999999998 # 15 decimales
c= a-b

lista1=[] # Lista que contendra los valores de ambos numeros y su resta

# Agregando valores a la lista

lista1.append(a)
lista1.append(b)
lista1.append(c)


# En este caso no hay perdida de significancia
cols= range(3)
plt.title("n2-n1=1.33226762955e-15/n2=2.999999999999999/n1=2.999999999999998")
plt.plot(cols,lista1,'o')
plt.xlabel("CASO SIN PERDIDA DE SIGNIFICANCIA")
plt.show()

d= 2.9999999999999999 # 16 decimales
e= 2.9999999999999998 # 16 decimales
f= d-e

lista2=[] # lista que contiene los valores de los numeros y su resta

# Agregando valores a la lista

lista2.append(d)
lista2.append(e)
lista2.append(f)


# Caso con perdida de significancia
plt.title("n1-n2=0/n2=2.9999999999999998/n1=2.9999999999999999")
plt.xlabel("CASO CON PERDIDA DE SIGNIFICANCIA")
plt.plot(cols,lista2,'o')
plt.show()

