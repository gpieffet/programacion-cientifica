# r=1
# v=((4*3.1416*(r*r*r)/3))
# r=raw_input()
# v=(4*3.1416)*float(r)*float(r)*float(r)/3

# print "el volumen es:", v

########

# def imprimir_letras():
# 	print "yo se que no he sido un santo"
# 	print "pero lo puedo arreglar.."

# imprimir_letras()

# def imprimir_2veces():
# 	imprimir_letras()
# 	imprimir_letras()

# imprimir_2veces()

# def nombre(carlos):
# 	print carlos

# nombre ("joel")

#####

def volumen_esf(r):
	
	v=(4*3.1416)*float(r)*float(r)*float(r)/3 
	return v    # return 4*math.pi directamente


r=raw_input()   # 1. convertir a float de una vez: r = float(raw_input())
                # así la converción se hace una sola vez
                # 2. indicar lo que está esperando el programa
print "el volumen es:", volumen_esf(r)  # utilizar un formato de cadena (para poder poner unidades)






