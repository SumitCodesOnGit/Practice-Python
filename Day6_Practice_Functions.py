# All about functions in python
def multiply(a,b):
    return a*b

def function(*a):
    print("the value are  {}".format(a))

def function1(**a):
    print("the values are {}".format(a))

response= lambda x: x**x
print(response(2))




result=multiply(3.5,10)
print(result)

function(3,5,8,9)
function("bulls","eyes","seen")
