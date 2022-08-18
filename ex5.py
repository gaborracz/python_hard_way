my_name = 'Gabor Racz'
my_age = 333 # not a lie
my_height = 213 # inches
my_height_cm = my_height * 2.54
my_weight = 1800 # lbs
my_weight_kilo = my_weight * 0.45359237
my_eyes = 'Red'
my_teeth = 'Black'
my_hair = 'Aquamarine blue'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("He's teeth are usually %s depending on the coffee." % my_teeth)

#this line is tricky, try to get it exactly right
print("If I add %r, %r and %r I get %r." % (my_age, my_height, my_weight, my_age + my_height + my_weight))
#print(my_height_cm)
print("I am %d centimeters tall." % my_height_cm)
print("My weight is %i kilos." % my_weight_kilo)