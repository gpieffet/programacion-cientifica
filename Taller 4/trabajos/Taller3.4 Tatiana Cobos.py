#Punto 4
def alinear_derecha(s):
	s=(' '*(70-7)) + s 
	return s

s='Tatiana'
print s
print alinear_derecha(s)
print len ('Tatiana')

print alinear_derecha('Gilles')
print alinear_derecha('Tim Burton')                                                      
print alinear_derecha('James Rodriguez')
print alinear_derecha('El conejito magico')
print alinear_derecha(raw_input())


# => en la linea 3, el echo de utilizar un valor fijo (7) hace que
# la funcion no es general y no hace lo que deberia