# r=1
# v=((4*3.1416*(r*r*r)/3))
# r=raw_input()
# v=(4*3.1416)*float(r)*float(r)*float(r)/3

# print "el volumen es:", v


# def imprimir_letras():
# 	print 'yo se que no he sido un santo'
# 	print 'pero lo puedo arreglar..'

# imprimir_letras()

# def imprimir_2veces():
# 	imprimir_letras()
# 	imprimir_letras()

# imprimir_2veces()

# def nombre(carlos):
# 	print carlos

# nombre ('joel')


def volumen_esf(r):
   
	v=((4*3.1416)*float(r)*float(r)*float(r))/3
	return v
    
r=raw_input()
print "el volumen es:", volumen_esf(r)


