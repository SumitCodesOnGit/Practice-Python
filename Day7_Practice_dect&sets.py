branches={
    "CSE":"a hobby branch",
    "IT":"little sister of hobby branch",
    "ECE":"branch for which our country is not ready",
    "Civil":"Mother of all branches",
    "ME":"Father of all branches"
}
print(branches)
for branch, description in branches.items():
        print(branch,":",description)

print('*' * 40)

fruits={
    "apple": "a fruit that keeps doctor away",
    "grape": "small sweet fruit when riped gives fun",
    "orange": "best for detox and it's juicy and tangy",
    "lemon": "always go for lemonade once you get it",
    "banana": "instant energy, recommended to everyone",
    "lime": "sour, green, citrous fruit"
}
print(fruits)
ordered_keys=list(fruits.keys())
ordered_keys.sort()
print(ordered_keys)

fruits['tomato'] = "not a fruit, may be used in sauce"
print(fruits.keys())



           