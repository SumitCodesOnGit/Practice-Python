
""" print(fruits)
print('-' * 100)
ordered_keys=list(fruits.keys())
ordered_keys.sort()
print(ordered_keys)
print('-' * 100)
fruits['tomato'] = "not a fruit, may be used in sauce"
print(fruits.keys()) # view keys
print('-' * 100)
print(fruits.items()) # view items
print('-' * 100)
f_tuple=tuple(fruits.items())
print(f_tuple)
print('-' * 100)
for snack in f_tuple:
    item, description = snack
    print(item + " : "+description) """

# two methods: 
fruits={
    "apple": "a fruit that keeps doctor away",
    "grape": "small sweet fruit when riped gives fun",
    "orange": "best for detox and it's juicy and tangy",
    "lemon": "always go for lemonade once you get it",
    "banana": "instant energy, recommended to everyone",
    "lime": "sour, green, citrous fruit"
}
veggies={
    "moringa": "full of nutrients, a powerhouse",
    "peas" : "fits everywhere and matar paneer is lub",
    "sprouts": "yupps, my go to breakfast"
}
print('-'* 100)
print(fruits)
print('-' * 100)
print(veggies)
print('-'* 100)
# update function for dict
# combining two dicts
veggies.update(fruits)
print(veggies)
print('-'* 100)
fruits.update(veggies)
print(fruits)
print('-'* 100)
print(fruits.update(veggies)) # it doesn't return anything
print('*' * 100)
# copy method
mandi_market=veggies.copy()
mandi_market.update(fruits)
print(mandi_market)

# notes: we got update method which basically combines two dictionaries.
# we also got copy() - basically creates a copy of a dictionary




