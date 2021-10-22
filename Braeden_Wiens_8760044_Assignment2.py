print("Welcome to Abby's merchandizing.")
print("Today we have an assortment of polos and t-shirts as well as jeans!")
print("Our shirts cost 9.99 each and our jeans are 19.99 each.\n")

print("Would you like to purchase t-shirts or polos today?")

while True:
    shirt = int(input("Please make sure you select 1 for polo or 2 for t-shirt: "))
    if shirt == 1:
        print("You selected polo!\n")
        break
    elif shirt == 2:
        print("You selected t-shirt!\n")
        break
 
print("We have a selection of colors for your shirts.")
print("We have red, purple, and navy blue, please input how many of each you would like.\n")

r = float(input("Red: "))
p = float(input("Purple: "))
nb = float(input("Navy Blue: "))

c1 = str(r)
c2 = str(p)
c3 = str(nb)

print()

print("You chose " + c1.rstrip('0').rstrip('.')+ " red " + c2.rstrip('0').rstrip('.') + " purple and " + c3.rstrip('0').rstrip('.') + " navy blue shirts.\n")


print("You also have some jean choices!")

while True:
    jeans = int(input("Please select 3 for regular style or 4 for slim style jeans: "))
    if jeans == 3:
        print("You have selected regular style jeans.\n")
        break
    elif jeans == 4:
        print("You have selected slim style jeans.\n")
        break

print("We have a selections of washes for you to choose from as well!")
print("We have dark wash, medium wash, and light wash please choose how many of each you would like.\n")

dw = float(input("Dark wash: "))
mw = float(input("medium wash: "))
lw = float(input("Light wash: "))

print()

c4 = str(dw)
c5 = str(mw)
c6 = str(lw)

print("You chose " + c4.rstrip('0').rstrip('.') + " dark wash " + c5.rstrip('0').rstrip('.') + " medium wash and " + c6.rstrip('0').rstrip('.') + " light wash.\n")

print("Before we move on to your total are you a student or senior citizen?")

while True:
    answer = input("Please input student or senior if they apply to you otherwise input no: ")
    if answer == 'student':
        print("The 10% student discount will be applied to your total.\n")
        break
    elif answer == 'senior':
        print("The 10% senior discount will be applied to you total.\n")
        break
    elif answer == 'no':
        print("Don't worry we have a 15% quantity discount if you purchase more then 10 items!\n")
        break

print("SUMMARY\n")
print("As review you have ordered.\n")

print(c1.rstrip('0').rstrip('.') + " red shirts.")
print(c2.rstrip('0').rstrip('.') + " purple shirts.")
print(c3.rstrip('0').rstrip('.') + " navy blue.\nAt 9.99 each.\n")
print(c4.rstrip('0').rstrip('.') + " dark wash jeans.")
print(c5.rstrip('0').rstrip('.') + " medium wash jeans.")
print(c6.rstrip('0').rstrip('.') + " light wash jeans.\nAt 19.99 each.\n")

n1 = 9.99
n2 = 19.99
a1 = 29.98
n3 = (((r+p+nb)*n1+(dw+mw+lw)*n2)/100*90)
n4 = (((r+p+nb)*n1+(dw+mw+lw)*n2)/100*85)

print("RECEIPT\n")

print("shirts:", (r+p+nb)*n1)
print("pants:", (dw+mw+lw)*n2)
print("clothing total:", (r+p+nb)*n1+(dw+mw+lw)*n2)

total = (r+p+nb+dw+mw+lw)

while True:
    if answer == 'student':
        print("Your final total with student discount", (n3*100/88.5))
        break
    elif answer == 'senior':
        print("Your final total with senior discount", (n3*100/88.5))
        break
    elif answer == 'no' and total >= 10:
        print("Your final total with purchases of over 10 items:", (n4*100/88.5))
        break
    elif answer == 'no' and total <=10:
        print("Your final total is:", ((r+p+nb)*n1+(dw+mw+lw)*n2)*100/88.5)
        break 

input("Press ENTER to confirm")