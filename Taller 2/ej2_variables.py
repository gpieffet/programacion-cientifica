# -*- coding: utf-8 -*-

my_name = 'Gilles'
my_age = 25
my_height = 1.72    # metros
my_weight = 68.000    # kg
my_eyes = 'brown'
my_hair = 'brown'

# print "Let's talk about", my_name
# print "He/she has a height (in meter) of", my_height
# print "He/she has a weight (in kg)", my_weight
# print "Actually that's not too heavy."
# print "His/her eyes are", my_eyes
# print "and his/her hair is", my_hair
# print "If I add my age, my height and my weight it all add up to", my_age + my_height + my_weight

print "Let's talk about %s." % my_name
print "He's %.2f m tall." % my_height
print "He's %d year old." % my_age
print "He's %.1f kg heavy." % my_weight
print "Actually that's not too heavy."
print "His weight to height ratio is %.2f kg/m" % (my_weight/my_height)
print "He has %s eyes and %s hair." % (my_eyes, my_hair)
# this line is tricky, be careful
print "If I add %d, %r, and %r I get %r." % (my_age, my_height, my_weight, my_age
         + my_height + my_weight)
