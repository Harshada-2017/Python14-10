f= open ("file.txt","r")
ct=f.read()

count=0

for ch in ct:
    if ch.lower() in "aeiou":
        count=count+1
            
print("Total vowels:",count)
f.close()
    
    
    