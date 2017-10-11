#ejercicio04
print 'vamos a alinear nombres a la derecha'
print 'su nombre sera alineado sin pasar el rango de 70 espacios'
print 'ingrese el nombre que desea alinear'

def alinear_derecha(s):
	s=raw_input()
	x=" "*(70-len(s))+s
	n=len(s)                # => para que sirve esta linea?
	print(x)

alinear_derecha(raw_input)  # => funcion?


# => donde estan los ejemplos tenia que utilizar con la funcion 
# => para que sirve la linea 9?
# => en la linea 12 no utiliza raw_input correctamente (como funcion)