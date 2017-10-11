#ejercicio 2
import math
print "vamos a calcular el volumen de una esfera"
print "ingrese el valor del radio"
r=raw_input()                                   # Porque estas dos lineas
v= 4*(math.pi)*float(r)*float(r)*float(r)/3     # están aquí? o sin comentar
#print "el volumen es %.3f cm3" %v
def volumen_es(radio):
	v= 4*(math.pi)*float(radio)*float(radio)*float(radio)/3
	return v
print volumen_es(raw_input())

