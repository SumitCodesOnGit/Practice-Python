# method 1
"""with open("D:\Python_MasterClass_Practice_Workspace\Python_Practice\poem.txt", "r") as file:
    content = file.read()
    print(content) """
# Method 2 (recomended)
""" with open("D:\Python_MasterClass_Practice_Workspace\Python_Practice\poem.txt","r") as file:
    for line in file:
        print(line.strip()) """
# with try and catch
""" try:
    with open("D:\Python_MasterClass_Practice_Workspace\Python_Practice\poem.txt", "r") as f:
        print(f.read())
except Exception as e:
    print("Error:", e) """

# another method
""" try:
    with open("D:\Python_MasterClass_Practice_Workspace\Python_Practice\poem.txt", "r") as file:
        for f in file:
            print(f.strip())
except Exception as e:
    print("Error! :", e) """

poem2="""
India, you are not just a land, you are a feeling,
A thousand tongues, a million prayers, yet one healing.
From Kashmir’s chill to Kanyakumari’s tide,
You hold us all — no need to hide.

You were born in verses, carved in stone,
In Vedas, in scripts, in whispered tone.
But today you speak in code and screen,
In start-up dreams and cricket scenes.

Your soil bears the weight of tired feet,
Yet feeds the world with every heartbeat.
The village boy with a dusty slate,
Now builds the tech that shapes our fate.

In traffic horns and temple bells,
In metro rides and midnight wells,
You are the chaos that strangely fits,
In chai breaks and Bollywood hits.

You are the mother who waits at night,
The soldier’s whisper under starlight.
The protest sign, the silent tear,
The anthem loud, the silent cheer.

India, you're torn, but never broken,
A country stitched by words unspoken.
From Ambedkar’s pen to Gandhi’s spin,
To youth that refuse to give in.

You're every hand that folds in prayer,
And every fist raised in the air.
You are the pain, the fight, the song —
The truth that rights what's long been wrong.

So rise, my India, not just in might —
But in your heart, your grace, your right.
May your future bloom where love is sown,
In a land that finally calls us home.


"""
""" try:
    with open("D:\Python_MasterClass_Practice_Workspace\Python_Practice\poem.txt","a", encoding="utf-8") as file:
        file.write("\n\n\n"+ poem2)
except Exception as e:
    print("You got error: ",e) """

try:
    with open("D:\Python_MasterClass_Practice_Workspace\Python_Practice\poem.txt", "r") as file:
        for f in file:
            print(f.strip())
except Exception as e:
    print("Error! :", e)









