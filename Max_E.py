# Mr Walker's feedback
# Great program, lots of detail! Great use of variables and concatenation. I've made some changes below

print("Welcome to Rap Libs - Answer the following questions to create your rap libs")

name = input("Enter a footballers name:")
colour = input("Enter a colour:")
family_figure = input('Enter a family figure e.g mum:')
stadium = input('Enter a football stadium')
country = input("Enter a country:")
trophy = input("Enter a trophy:")
city = input("Enter a city:")
nationality = input("Enter your footballers nationality:")
ex_footballer = input('Enter a ex footballers name:')

print("--------RAPLIBS START--------")
print(name + '!')
print(name + '!')
# You don't need brackets around your variables.
# Only need this if you were changing from another type to str e.g. str(variableName)
print("he's a " + colour + " just like his " + family_figure)
# Remember spaces so it is readable when printed
print("now he's at " + stadium)
print("HA HA HA HA HA " + name + ' HEY!')
print(name + '!')
print(name + '!')
print('came to us from ' + country)
# If you need an apostrophe, can use \
print('he\'s here to win the ' + trophy)
print("HA HA HA HA HA " + name + ' HEY!')
print(city + ' born ' + nationality + ' lad')
# This line below was causing the break, you just missed some brackets
print(ex_footballer + ' tried to kill his ' + family_figure)
print("HA HA HA HA HA " + name + ' HEY!')
print("--------RAPLIBS END--------")

