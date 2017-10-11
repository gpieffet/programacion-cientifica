import math
#ejercicio 2
print 'vamos a calcular el volumen de una esfera '
print 'ingrese el valor del radio'
# r=raw_input()
# v = 4 * (3.1416) * (float(r)*float(r)*float(r)) /3
# print 'el volumen es %.3f cm3'%v
def volumen_es(radio):
	print radio
	v=4*(math.pi)*float(radio)*float(radio)*float(radio)/3
	return v
print volumen_es(raw_input())


		
