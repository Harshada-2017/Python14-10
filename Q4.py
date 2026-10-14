f = open("file.txt", "r")

content = f.read()

words = content.split()

print("Total number of words:",len(words))

unique = set(words)

print("all unique words:",unique)

f.close()