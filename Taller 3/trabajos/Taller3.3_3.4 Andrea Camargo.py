######punto 3
# import math
# print "convertir angulos en radianes a grados"
# print "ingrese el valor de los radienes a radio"
# def grados(radianes):
#     print radianes
#     grados=(float(radianes)/ math.pi)*180
#     return grados
#     #
# def radianes(grados):
#     	print grados
#     	radianes=(float(grados)/180)* math.pi
#     	return radianes
# # print grados(raw_input())
# # print radianes(raw_input())
# print grados(math.pi)
# print grados(math.pi/2)
# print grados(math.pi/6)
# print radianes(180)
# print radianes(360)
# print grados(radianes(180))
# print grados(radianes(30))
# print radianes(grados(math.pi))
# print radianes(grados(math.pi/2))

#punto 4 

def alinear_derecha(s):
	s= (' '*(70-6))+s
	return s
	
s='Andrea'
print s
print alinear_derecha(s)
print len('Tatiana')


    
# => donde estan los ejemplos tenia que utilizar con la funcion?
# => en la linea 29, el echo de utilizar un valor fijo (6) hace que
# la funcion no es general y no hace lo que deberia