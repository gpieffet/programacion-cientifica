# #EJERCICIO 3
# import math
# print "Vamos a hallar los grados a partir de los radianes"
# print "Ingrese el valor de los radianes" 
# def grados(radianes):
# 	grados= float(radianes)*180/math.pi
# 	return grados

# angulo = float(raw_input())
# print "el valor de %.2f en grados es" % angulo
# print grados(angulo)

#2DA PARTE
import math
print "Vamos a hallar los radianes a partir de los grados"
print "Ingrese el valor de los grados" 
def radianes(grados):
	radianes= float(grados)*math.pi/180
	return radianes

angulo = float(raw_input())
print "el valor de %.2f en radianes es" % angulo
print radianes (angulo)