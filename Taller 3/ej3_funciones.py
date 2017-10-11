########### Punto 1
# print "Cual es el radio r de la esfera (en cm)?"
# r = float(raw_input())
# v = 4*3.14*r*r*r/3
# print "El volumen de la esfera es: %.1f cm3" % v



########### Punto 2
# from math import pi
# def volumen_esf(r):
#     return 4 * pi * r * r * r / 3
# v1
# print "Cual es el radio r de la esfera (en cm)? r = ",
# r = float(raw_input())
# print "El volumen de la esfera es: %.1f cm3" % volumen_esf(r)

# v2
# r = float(raw_input("Cual es el radio r de la esfera (en cm)? r = "))
# print "El volumen de la esfera es: %.1f cm3" % volumen_esf(r)

# v3
# print "El volumen de la esfera es: %.1f cm3" % \
    # volumen_esf(float(raw_input("Cual es el radio r de la esfera (en cm)? r = ")))

# volumen_esf(0.1)    = 0.004189 cm3
# volumen_esf(2)      = 33.5 cm3
# volumen_esf(15)     = 14137.2 cm3


########### Punto 3
# def grados(rad):
#     return rad/pi*180
#
# def radianes(grad):
#     return grad/180.0*pi
#
# print 'pi = %.3f radianes = %.1f grados' % (pi, grados(pi))
# print grados(pi/2)
# print grados(pi/6)
# print radianes(180)
# print radianes(360)
# print grados(radianes(180))
# print grados(radianes(30))
# print radianes(grados(pi))
# print radianes(grados(pi/2))
# print ""



########### Punto 4
def alinear_derecha(s):
    print ' '*(70 - len(s)) + s

print 'b' * 70
alinear_derecha('Allen')
alinear_derecha('Tim Burton')
alinear_derecha('James Rodriguez')
alinear_derecha('El conejito magico')
alinear_derecha(raw_input())



# ########### Punto 5
# v1
# def duplicar(f):
#     f()
#     f()
# def imprimir_spam():
#     print 'spam'
# duplicar(imprimir_spam)

# v2
# def imprimir_2veces(s):
#     print s
#     print s
#
# def duplicar(f, a):     # disymmetry between duplicar and cuadruplicar because
#     f(a)                # f is general (could be any function), while duplicar
#     f(a)                # is always going to be duplicar
#
# def cuadruplicar(f, a):
#     duplicar(f, a)
#     duplicar(f, a)
#
# print "Utilizando duplicar"
# duplicar(imprimir_2veces, 'spam')
# print ""
# print "Utilizando cuadruplicar"
# cuadruplicar(imprimir_2veces, 'spam')


