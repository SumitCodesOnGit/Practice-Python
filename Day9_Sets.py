# set - unordered and doesn't allow duplicate.
# very useful for cleaning data.
""" farm_animals={"sheep","goat","horse","mule"} # we can create set like this
print(farm_animals)

for animal in farm_animals:
    print(animal)

print(type(farm_animals))
print('*'*100)
wild_animals=set(['lion',"tiger","wolf","elephant","rhino"]) # set() to create set
print(type(wild_animals))
print(wild_animals)
farm_animals.add("cow")
wild_animals.add('crocodile') # add() to add elements to set
print(farm_animals)
print(wild_animals) # there is no inherent order so proves unordered. """

empty_set=set()
empty_set2={} # it may look like set but it's actually a dictionary
empty_set.add("a")
#empty_set2.add("b") 
print(type(empty_set2))






