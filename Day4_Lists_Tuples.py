panagram = "The quick brown fox jumps over the lazy dog"
words=panagram.split()
print(words)

panagram1 = """the quick brown fox
jumps over
the lazy dog."""
words1=panagram1.split()
print(words1)

numbers="9,223,547,56,91,807,34,67"
print(numbers.split(","))


## Tuples
 # mathematical name for an ordered set of data.
 # different from list coz they are immutable.
t = "abc","def","ghi"
print(t)
tuple = ("abc","def","ghi")
print(tuple) # always use parenthesis irrespective of it's mandatory
name='Sumit'
age=27
print(name,age,"Pyhton",2025)
print((name,age,"Pyhton",2025)) # tuple 
# tuples are immutable
metallica="rided the waves","Metallica",2020
print(metallica)
print(metallica[0])
print(metallica[1]) # indexing works the same way
#metallica[0]="master of puppets"
# print(metallica) # error, they are immutable
 # tuples use less memory than lists
 # u can save memory
 # to protect the integrity of data
metallica2=list(metallica)
print(metallica2)
metallica2[2]=2025
print(metallica2) # lists are mutable
#unpacking a tuple
a=b=c=d=e=f=42
print(c)
x,y,z =1,2,3
print(x,y,z)
print(z)
print("unpacking a tuple")
data=1,2,76 # data reresents tuple
x,y,z=data
print(x)
print(y)
print(z)

