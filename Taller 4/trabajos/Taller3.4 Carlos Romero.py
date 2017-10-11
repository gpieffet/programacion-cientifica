#EJERCICIO 4
print "Vamos a alinear algunos nombres a la derecha"
print ""
print "(Recuerde que su nombre sera alineado sin pasar el margen de 70 espacios)"
print ""
print "Ingrese el nombre de interes"
def alinear_derecha(s):
	s=raw_input()
	x=" "*(70-len(s))+s
	n=len(s) 
	print(x)

alinear_derecha(raw_input)

# => donde estan los ejemplos tenia que utilizar con la funcion 
# => para que sirve la linea 10?
# => en la linea 13 no utiliza raw_input correctamente (como funcion)