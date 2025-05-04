# reading a file -text file
""" try:
    with open("D:\Python_MasterClass_Practice_Workspace\Python_Practice\poem.txt", "r") as file:
        for line in file:
            print(line.strip())
except Exception as e:
    print("Error ",e) """

# writing will ovewrite and it's syntax is similar. (it overwrites or creates)
# we will use append to add new content (it creates if doesn't exist)
poem3="""
She strolled in silence before the dawn,
When chains were real, but fear was gone.
No guards, no codes, no mirrored lens—
Just old streetlamps and quiet sense.

Today she walks in brighter light,
Yet every shadow sparks a fight.
We earned a flag, a voice, a name—
But left her safety stuck in flame.
"""

""" try:
    with open("D:\Python_MasterClass_Practice_Workspace\Python_Practice\poem.txt","+a", encoding="utf-8") as file:
        file.write(poem3)
        file.seek(0)
        print(file.read())
except Exception as e:
    print("Error ",e) """
# binary format
# pickle is a module that converts python object into storable byte stream and vice-versa.

try:
    with open("binary","bw") as bin_file:
        for i in bin_file:
            bin_file.write(bytes([i]))
except Exception as e:
    print("Error: ",e)













