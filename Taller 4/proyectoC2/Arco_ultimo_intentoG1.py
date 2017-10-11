# -*- coding: utf-8 -*-
# integrantes: Paloma cuenca Arias, Tatiana Cobos, Carlos Delgado
from TurtleWorld import*
world=TurtleWorld()
dona=Turtle()
print dona

print 'el arco se basa en 3 partes: el radio de la circunferencia y un angulo respectivo para longitud del arco'
print 'para poder dibujar el arco hemos definido 3 variables, donde t=tortuga, r=radio de la circunferencia y a=angulo de amplitud del arco'
print 'primero aparecera el angulo dado del arco y luego con la funcion circulo se observa la seccion de la circunferencia a la cual corresponde el arco'
print 'el radio que toma la variable r de la funcion arco es el despeje de la ecuacion definida como longitud=(2* 3.1416*r)/n en la funcion circulo'
print 'Ahora dibujaremos el angulo que se quiere para el dibujar el arco'


def angulo(t,r,a):

	lt(dona)
	lt(dona,180-a)
	fd (dona,r)
	lt(dona,180-a)
	fd (dona,r)
	lt(dona)
print angulo (dona,107,11.25)

dona.delay=0.001

print 'para trazar el arco del angulo dibujado anteriormente se debe jugar con las variables longitud y n'
print u'teniendo en cuenta que si n=45 para una circunferencia de 360°'
print u'varia los datos de la siguiente forma:'
print u'para 360° n=45 y te da un circulo con el angulo del arco marcada'
print u'para 180° n= 22.5'
print u'para 90° n= 11.25'
print u'para 45° n=5.625'
print u'para 22.5° n= 2.812'
print u'para 11.25° n=1.406'


def arco(t,r):
	n=1.406
	longitud=(2* 3.1416*r)/n
	for i in range (int(n)):
		fd(t,r)
		lt(t,11.25/n)

# print arco (dona,14.5)
print arco (dona,90)
wait_for_user()


# Correccion
# 1. El programa no corre por el uso de caracteres no estanderes:
# => Utilizar \# -*- coding: utf-8 -*-
# 2. El programa no dibuja un arco
# 3. La funcion arco() deberia recibir un angulo como argumento
# 4. La funcion arco utiliza valores fijas/pre-calculadas. 
# Porque, si esta escribiendo un programa que puede hacer todos los calculos
# que requieren?

