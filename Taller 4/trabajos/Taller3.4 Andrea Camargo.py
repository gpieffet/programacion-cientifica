##punto 4
print 'vamos a alinear nombres a la derecha'
print 'el nombre va ser alineado sin pasar los 70 espacios'
print 'ingrese el nombre que sera alineado'

def alinear_derecha(s):
	x=" "*(70-len(s))+s
	n=len(s)
	print(x)

#inear_derecha(raw_input)
alinear_derecha('Andrea')
alinear_derecha('Gilles')
alinear_derecha('Tim Buston')
alinear_derecha('James Rodriguez')
alinear_derecha('El conejito magico')


# => para que sirve la linea 8?
# linea 11 (comentada): en la linea 12 no utiliza raw_input correctamente (como funcion)