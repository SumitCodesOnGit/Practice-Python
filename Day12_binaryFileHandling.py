""" # writing to a binary file
with open("binary","bw") as bin_file:
    for i in range(17):
        bin_file.write(bytes([i]))
# reading from a binary file
with open("binary","br") as binFile:
    for b in binFile:
        print(b) """



