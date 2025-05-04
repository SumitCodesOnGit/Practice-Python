albums=[
    ("Lata Mangeshkar","Hindi Classic", 1975,
     [ "Chura liya tumne jo dil ko",
       "Aye Mere hamsafar",
       "Chaha hai tumko",
       "Jee huzoor"
          ]
     ),
     ("Arijeet Singh", "Hindi All", 2010,
      [ "tere khusboo",
        "tenu samjhawan",
        "citylight",
        "kesariya"
     ]
      ),
    ("Atif Aslam", "Hindi & Urdu", 2006,
     [ "jeene laga hoon",
       "tajdar-e-haram",
       "ayye yooo",
       "chalne do mujhe chalne do"
     ]
      )
]
for index, values in enumerate(albums):
    Artist, Album, Year, Songs = values
    print('-'*10)
    print(Artist)
    print(Year)
    print(Album)
    print('-'*10)
    print("Songs by {}:".format(Artist))
    for song in Songs:
        print(song)


flowers=[
    "Lotus",
    "Lilly",
    "Rose",
    "Petals",
    "Jasmine",
    "Bougenvelia",
]
separator = " | "
output = separator.join(flowers) # we can change separator as per our wish
print(output) 
print(" , ".join(flowers)) # can also be done
for flower in flowers:
    print("")
    print(flower)

numbers = [12,
           34,
           897,
           675,
           987,
           ]
#print(" | ".join(numbers)) # throw error coz it expects str instance only

        