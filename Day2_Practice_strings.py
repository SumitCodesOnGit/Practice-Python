# Section 2: Strings and introduction

print("hey sunny! wassup")
for i in range(1,4):
    print(i)
for i in range(1,12):
    print("#" * i)
print("hey there! " "I am Sunny Singh. " "How may I help you?")
print("hey, thanks! " "I just wanted to know the timelines for project A.")
# string prcatice session

# basics and case conversion
str = "hello world!"
print(str)
print("hello world".capitalize())
print("hello world".upper())
print("HELLO WORLD".lower())
print("hello world".title())
print("Hello World".swapcase())
# formatting functions
print(" hello world   ".strip())
print(" hello ".lstrip())
print(" hello ".rstrip())
print("hello".center(15,'-'))
print("hello".ljust(7,'-'))
print("hello".rjust(7,'-'))
print('45'.zfill(5))
# search and find method
print("hello".find('o'))
print("hello".find('l'))
print("hello world".find('o',3,10))
# index works in the same way but just returns not found error if sub str is not found
print("hello world".rfind('o'))
print("Life is just collection of too many experiences".count('o'))
# string modification and replacements
print("Sumit".replace('S','p'))
print('Sumit'.replace('x','i'))
print("hello\tworld".expandtabs(2))

print("how are you pal!".split(' '))

# format() method - usage
# {} is placeholder and format(value), value is filled in {}
print("My name is {} and I am {} year old".format("Sunny",27))
print("I love {0}, {1}, {2} and {3}.".format("AI","ML","DS","ECE"))
print("{0} is a powerful language and in ML, {0} plays crucial role".format("Python"))
print("My name is {0} and I love {hobby}.".format("Sunny",hobby="cricket"))
print("Number:{:d}".format(123))
print("Number:{:.5f}".format(3.142378))

# negative slicing
print("hello world"[-1]) # d
print("hello world"[-11]) # h
print("hello world"[-5:-2]) # wor
print("hello world"[-11:-6]) # hello
print("hello world"[:5]) # hello
print("Python Programming"[-5:]) # mming
print("Python Programming"[:-5]) # Python Progra
print("Machine Learning"[:-8]) # Machine
print("Machine Learning"[-8:]) # Learning
print("Artificial Intelligence"[:-12]) # Artificial 
print("Artificial Intelligence"[-12:]) # Intelligence
# reverse a string 
print("Generative Artificial Intelligence"[::-1]) # reverse
print("Generative Artificial Intelligence"[::-2]) # reverse with a step of 2



