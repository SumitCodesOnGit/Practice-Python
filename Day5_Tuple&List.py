data_list=[12,14,56]
p,q,r=data_list
print("unpacking a list")
print(p)
print(q)
print(r)
data_list.append(69)
p,q,r,s=data_list
print(data_list)
print(p)
print(q)
print(r)
print(s)
#advantage of tuples= can always be unpacked.
# enumerate is very useful when u need to iterate and also need an index
for index, character in enumerate("abcdefghijklmnopqrstuvwxyz"):
    print(index,character)

for x in enumerate("abcdefgh"):
    print(x) # returns a tuple

albums=[
    ("Lata Mangeshkar","chale hi jana hai",1968),
    ("Kishor Kumar","bade achche lagte hai",1975),
    ("Muhammad Rafi","Oo haseena julfon wali",1970),
    ("Arijeet","Tere Khushboo aur tere sansein",2018),
    ("Shreya Ghosal","Tujhme rab dikhta hai",2011)
]

for name,artist,year in albums: # here we unpacked the nested tuple in list
    print("Album: {}, Artist: {}, Year: {}".format(name,artist,year))
# both are fine
for album in albums:
    print("Album:{}, Artist:{}, Year:{}".format(album[0],album[1],album[2]))

for name, artist, year in albums:
    print("Artist:{}".format(name))

# u can't append to a tuple because tuples are immutable
tuple=(123,"Sumit",34.56)
print(tuple)
print(str(tuple))
print(type(tuple))

# nesting of tuples and lists
# for heterogeneous data tuple is a good choice
# based on requirements and mutability and immutability we need to decide 
 


