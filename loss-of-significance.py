#Se definen dos numeros casi iguales, los cuales al restarlos
#dan como resulado 0, lo cual es erroneo, dado que no son iguales

import scipy as sp
import matplotlib.pylab as plt
import sys


# Cuando se restan dos numeros parecidos pero no iguales, si 
# sus decimales son 15, no hay perdida de significancia,  y el
#programa entregará la solución correctamente, pero si son mas de
# 15 decimales se probocara perdida de significancia


a= 2.999999999999999
b= 2.999999999999998
d= 2.9999999999
c= a-b

print c
print float(a-b)

lista1=[]

lista1.append(a)
lista1.append(b)
lista1.append(c)

print lista1
print d

# 