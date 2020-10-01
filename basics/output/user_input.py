#Ask the user what their name is      
print("What is your name human?")
name = input()
print("It's nice to meet you {}.".format(name))
print("How old are you (in years)?")
age = int(input())
print("Ok, so you're " +str(age))
print("How tall are you (in meters)?")
height = float(input())
print("And how much do you way (in kilograms)?")
weight = float(input())
message="So, {} you are {} and have a BMI of {:.2f} "
print(message.format(name, age, weight/height**2))
