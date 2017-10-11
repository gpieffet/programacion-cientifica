# PROYECTO CORTE 2
# Version 1
def poligono(t, longitud, n, angulo):
        for i in range(n):
            fd(t, longitud)
            lt(t, float(angulo)/n)


def arco(t, r, angulo):
    longitud = 10
    # perimetro = 2*pi*r
    n = int(2*pi*r/longitud) + 1
    # arco = r*angulo*2*pi/360
    # n_arco = int (arco/longitud) + 1
    poligono(t, longitud, n, angulo)    # => using the same n is wrong

# def poligono(t, longitud, n):
#         for i in range(n):
#             fd(t, longitud)
#             lt(t, 360.0/n)
#
# def circulo(t, r):
#     longitud = 10
#     n = 2*pi*r/longitud
#     # poligono(t, longitud, int(round(n,0)))
#     poligono(t, longitud, int(n)+1)
#
# circulo(bob, 100)
#
# def arco(t, r, angulo):
#     longitud = 10
#     perimetro = 2*pi*r
#     n = 2*pi*r/longitud
#     arco = r*angulo*2*pi/360
#     n_arco = int (arco/longitud) + 1
#     for i in range(n_arco):
#         fd(t, longitud)
#         lt(t, angulo/n_arco)

# arco(bob, 100, 30)
# arco(bob, 100, 45)
# arco(bob, 30, 90)
arco(bob, 15, 180)
wait_for_user()