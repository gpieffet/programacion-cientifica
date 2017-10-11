###### punto1
import math
r=1.0
#r=1.0
#v=(4*3.1416 * r * r * r)/3
#print "volumen", vcd
#r= raw_input ()
#v=(4*3.14* float(r)* float(r)* float(r))/3
# print "volumen: %f cm3" % (v)
def volumen_es(radio):
	print radio
	r=radio                     # para que sirve?
	v= 4*(math.pi)*float(radio)*float(radio)*float(radio)/3
	return v
print volumen_es(raw_input())   # debería indicar los que espera el programa y que es lo que se calcula



