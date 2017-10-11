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


# def volumen_esf(r):
   
# 	v=((4*3.1416)*float(r)*float(r)*float(r))/3
# 	return v
    
# r=raw_input()
# print "el volumen es:", volumen_esf(r)
import math
math.pi

# def grados(radianes):
# 	# grados= (math.pi*radianes)/180
# 	return (radianes/math.pi)*180

# def radianes(grados):
# 	# radianes= (radianes/math.pi)*180 
# 	return (math.pi*grados)/180

# print grados(math.pi)
# print grados(math.pi/2)
# print grados(math.pi/6)
# print radianes(180)
# print radianes(360)
# print grados(radianes(180))
# print grados(radianes(30))
# print radianes(grados(math.pi))
# print radianes(grados(math.pi/2))

def alinear_derecha(s):
    nueva_s = (' '*(70-len (s)))+ s
    
    return nueva_s
m='karen'
print m
print alinear_derecha(m) 
 
 