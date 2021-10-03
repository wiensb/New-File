word=input("Select any letters from A-Z ")
word1=''
for i in word:
    if(i.isupper())==True:
        word1+=(i.lower())
    elif(i.islower())==True:
        word1+=(i.upper())
    elif(i.isspace())==True:
        word1+=i
print(word1)

input("press Enter to exit")