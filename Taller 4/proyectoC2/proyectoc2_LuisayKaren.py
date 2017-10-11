from TurtleWorld import *
world=TurtleWorld()
flor=Turtle()
flor.delay=0.01
# print bob
# for i in range (4):
# 	fd(bob,60)
# 	lt(bob)


# def cuadrado (t):
# 	for i in range (4):
# 		fd(t,longitud)
# 		lt(t)

# print cuadrado (flor,100)

# def poligono (t,l,n):
# 	for i in range (n):
# 		fd(t,l)
# 		lt(t,(360/n))

# print poligono (flor,60,6)

# def circulo (t,r):
# 	l=20
# 	n=((2*int (3.1416)*r)/l)
# 	poligono (t,l,n)
# 	print n

# print circulo (flor,100)

# def circulo_n (t,r):
# 	n=90
# 	l=((2*int (3.1416)*r)/n)
# 	poligono (t,l,n)
# 	print l

# print circulo_n (flor,100)
# circulo_n (flor,60)
# circulo_n (flor,50)
# circulo_n (flor,40)
# circulo_n (flor,30)
# circulo_n (flor,20)
# circulo_n (flor,10)
# wait_for_user()

def poligono_n (t,l,n,angulo):
	for i in range (n):
		fd(t,l)
		lt(t,(angulo/n))

def arco (t,r,a):
	angulo=90
	n=(30)
	l=(((2* int(3.1416)*r)/(n)))
	poligono_n (t,l,n,a)
	print l

print arco (flor,30,360)
print arco (flor,30,180)
wait_for_user()


# Correcion
# 1. l54: la variable angulo no sirve para nada
# 2. los valores n y l en la funcion circulo() estan calculadas para un circulo completo de 
# 360 grados, y no se pueden utilizar tal cual en la funcion poligono con un angulo cualquiera.
# Utilizar estos valores de n y l con un angulo diferente de 360 grados tiene como efecto de cambiar 
# (disminuir) la curvatura del circulo y entonces aumentar el radio.
