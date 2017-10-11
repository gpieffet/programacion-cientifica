# -*- coding: utf-8 -*-
# Integrantes:
# BREYNER JOEL QUIÑONES
# ANDREA CAMARGO
# CARLOS ROMERO VASQUEZ


# Ejercicio clase
# from TurtleWorld import *
# world=TurtleWorld()
# bob=Turtle()
# print bob
# fd(bob,100)
# lt(bob)
# fd(bob,100)
# lt(bob)
# fd(bob,100)
# lt(bob)
# fd(bob,100)
# lt(bob)

# PROGRAMA(TALLER 4.3)23|1|1|>
from TurtleWorld import * 

world = TurtleWorld()
Shaira = Turtle()
# print Shaira
# for i in range (4):
# 	fd(bob, 100),lt(bob)

# wait_for_user()

#PUNTO 6

# def cuadrado(t, l):
# 	for i in range (4):
# 		fd(t, l)
# 		lt(t)
# cuadrado(leonardi, 100)

# PUNTO 7
Shaira.delay=0.01
def poligono(t,n,l,a):
	for i in range (n):
		lt(t,a/n)
		fd(t,l)

#poligono(Shaira,8,45)

#PUNTO 8

# def circulo(t,r):
# 	longitud=20
# 	n=(2*(3.1416)*r/longitud)
# 	poligono(t,longitud,n)
# 	print "Observa el numero de lados que usa el programa para hacer el circulo"
# 	print n
# circulo(Shaira,10)
# circulo(Shaira,20)
# circulo(Shaira,30)
# circulo(Shaira,40)
# circulo(Shaira,50)
# circulo(Shaira,60)
# circulo(Shaira,70)
# circulo(Shaira,80)
# circulo(Shaira,90)
# circulo(Shaira,100)
# circulo(Shaira,15)
# circulo(Shaira,25)
# circulo(Shaira,35)
# circulo(Shaira,45)
# circulo(Shaira,55)
# circulo(Shaira,65)
# circulo(Shaira,75)
# circulo(Shaira,85)
# circulo(Shaira,95)
# circulo(Shaira,105)
# circulo(Shaira,12.5)
# circulo(Shaira,22.5)
# circulo(Shaira,32.5)
# circulo(Shaira,42.5)
# circulo(Shaira,52.5)
# circulo(Shaira,62.5)
# circulo(Shaira,72.5)
# circulo(Shaira,82.5)
# circulo(Shaira,92.5)
# circulo(Shaira,102.5)
# wait_for_user()

def circulo(t,r,a):
 	n=30
 	longitud=(2*(3.1416)*r/n)
 	poligono(t,n, longitud,a)

# circulo(Shaira,80)

def arco(t,r,angulo):
	arco=angulo*2*3.1416*r/360
	circulo(t,r,angulo)
	print arco

# arco(Shaira,25,270)
arco(Shaira,25,90)

wait_for_user()


# Correcion:
# 1. La funcion arco() es completamente inutil para dibujar el arco y podría ser omitida 
# por completo (y cambiar el nombre de la funcion circulo por arco).
# 2. los valores n y l en la funcion circulo() estan calculadas para un circulo completo de 
# 360 grados, y no se pueden utilizar tal cual en la funcion poligono con un angulo cualquiera.
# Utilizar estos valores de n y l con un angulo diferente de 360 grados tiene como efecto de cambiar 
# (disminuir) la curvatura del circulo y entonces aumentar el radio.
