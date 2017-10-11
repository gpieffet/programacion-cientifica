#punto4
print 'alinear el nombre a la derecha en un rango de 70 espacios'

def alinear_derecha(s):
	s=raw_input()
	x=" "*(70-len(s))+s
	n=len(s) 
	print(x)
	
alinear_derecha(raw_input)

# => donde estan los ejemplos tenia que utilizar con la funcion?
# => para que sirve la linea 11?
# => en la linea 10 no utiliza raw_input correctamente (como funcion)