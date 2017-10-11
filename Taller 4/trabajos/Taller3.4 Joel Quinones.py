#EJERCICIO 4
print "Vamos a alinear nombres a la derecha"
print ""
print "NOTA"
print "(Recuerde que su nombre sera alineado sin pasar el margen de 70 espacios)"
print ""
print "Ingrese el nombre de interes"
def alinear_derecha(s):
	s=raw_input()
	x=" "*(70-len(s))+s
	n=len(s) 
	print(x)

alinear_derecha(raw_input)

# => donde estan los ejemplos tenia que utilizar con la funcion?
# => para que sirve la linea 11?
# => en la linea 14 no utiliza raw_input correctamente (como funcion)