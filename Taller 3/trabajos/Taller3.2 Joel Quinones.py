def imprimir_letras():
    print "yo se que no he sido un santo"
    print "pero lo puedo arreglar"
#imprimir_letras()

def imprimir_2veces():
	imprimir_letras()
	imprimir_letras()
#imprimir_2veces()
def nombre(carlos):
	print carlos
#nombre("joel")

#EJERCICIO 2
import math
print "Vamos a calcular el volumen de una esfera"
print "Ingrese el valor del radio"
# r=raw_input()
# v=4*(math.pi)*float(r)*float(r)*float(r)/3
# print "El volumen es %.2f cm3"%v
def volumen_es(radio):
	v=4*(math.pi)*float(radio)*float(radio)*float(radio)/3
	return v
print volumen_es(raw_input())





