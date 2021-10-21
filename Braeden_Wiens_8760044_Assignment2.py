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

r = float(input("Red: "))
p = float(input("Purple: "))
nb = float(input("Navy Blue: "))

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






