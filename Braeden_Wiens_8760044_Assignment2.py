print ("Wlecome to Abby's merchandizing.")
print("Today we have an assortment of polos and t-shirts as well as jeans!")
print("Our shirts cost 9.99 each and our jeans are 19.99 each.")

print("Would you like to purchase t-shirts or polos today?")


while True:
    shirt = int(input("Please make sure you select 1 for polo or 2 for t-shirt: "))
    if shirt == 1:
        print("You selected polo!")
        break
    elif shirt == 2:
        print("You selected t-shirt!")
        break
 
print("We have a selection of colors for your shirts.")
print("We have red, purple, and navy blue, please input how many of each you would like.")

r = float(int(input("Red: ")))
p = float(int(input("Purple: ")))
nb = float(int(input("Navy Blue: ")))

c1 = str(r)
c2 = str(p)
c3 = str(nb)

print("You chose " + c1.rstrip('0').rstrip('.')+ " red " + c2.rstrip('0').rstrip('.') + " purple and " + c3.rstrip('0').rstrip('.') + " navy blue shirts.")


print("You also have some jean choices!")

while True:
    jeans = int(input("Please select 3 for regular style or 4 for slim style jeans: "))
    if jeans == 3:
        print("You have selected regular style jeans.")
        break
    elif jeans == 4:
        print("You have selected slim style jeans.")
        break

print("We have a selections of washes for you to choose from as well!")
print("We have dark wash, medium wash, and light wash please choose how many of each you would like.")

dw = float(input("Dark wash: "))
mw = float(input("medium wash: "))
lw = float(input("Light wash: "))

c4 = str(dw)
c5 = str(mw)
c6 = str(lw)

print("You chose " + c4.rstrip('0').rstrip('.') + " dark wash " + c5.rstrip('0').rstrip('.') + " medium wash and " + c6.rstrip('0').rstrip('.') + " light wash.")

print("Before we move on to your total are you a student of senior citizen?")

while True:
    answer = input("Please input student or senior if they apply to you otherwise input no: ")
    if answer == 'student':
        print("The 15% student discount will be applied to your total.")
        break
    elif answer == 'senior':
        print("The 15% senior discount will be applied to you total.")
        break
    elif answer == 'no':
        print("Don't worry we have a 10% quantity discount if you purchase more then 10 items!")
        break

input("press ENTER")