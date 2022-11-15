# Mr Walker's feedback
# Good start, program looks very similar to mine! Would have been nice to see some originality

print("Welcome to Rap Libs - Answer the following questions to create your rap libs")

name = input("what is your name:")
school_subject = input("what is your favourite subject:")
animal = input("what is your favourite animal (singular):")
location = input("where is your favourite location:")
celebrity = input("who is your favourite celebrity:")
singer = input("who is your favourite singer:")

# You could have added your own variables such as:
size = input("Please enter a size with est at the end (e.g. smallest): ")

# You don't need the str(variableName), this is only needed if the variable is another type such as int or float
print("Y'all know me by now, " + str(name))

# Then use this variable in your print with concatenation (Use +)
print("I'm the " + size + " rapper in the game, ")
print("The " + school_subject + " god")
print("King of " + location)
print("Rapping bout " + animal + "s till I die")
print("And at the end of the day, you know I can bring it like " + celebrity)
print("Droppin' classics harder than " + singer)
print("--------RAPLIBS END--------")
