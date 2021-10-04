user = int(input("Please Enter a number from 1-10 here ")) 
comp = 0
output = 0

while comp <= user:
    output += comp**2
    comp += 2

print(output)

input("press ENTER")