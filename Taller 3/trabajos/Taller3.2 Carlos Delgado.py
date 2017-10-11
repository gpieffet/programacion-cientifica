# def imprimir_letras():
#     print 'yo se que no e sido un santo '
#     print 'pero lo puedo arreglar'
# # imrpimir letras
# def imprimir_2veces():
# 	imprimir_letras()
# 	imprimir_letras()
# imprimir_2veces()
# # 
# def	nombre (carlos):
# 	print carlos
#nombre('joel')

#ejercicio 1
import math
print "vamos a calcular el volumen de una esfera"
print "ingrese el valor del radio"
r=raw_input()
v= 4*(3.1416)*float(r)*float(r)*float(r)/3
#print "el volumen es %.3f cm3" %v
def volumen_es(radio):
	v=4*(math.pi)*float(r)*float(r)*float(r)/3  # => NO!!!!!!!! radio es el argumento, no r
	return v                                    # => a que clase de error corresponde?  
print volumen_es(raw_input())


