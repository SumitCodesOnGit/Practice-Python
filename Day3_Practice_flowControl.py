# Section -3 : Flow control in Python Practice
for i in range(1,13):
    print("No {} sruared is {} and cubed is {:4}".format(i, i **2, i **3))
print("*" * 80)

name= input("Please enter your name: ")
age = input("How old are you, {0}? ".format(name))
print(age)
print(type(age))
if int(age) >= 18:
    print("{}, you are eligible to vote.".format(name))
else:
    print("{}, you are not eligible to vote.".format(name))
