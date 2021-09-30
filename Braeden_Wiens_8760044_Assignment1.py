print("welcome to Abby's Merchandizing")
shirt = (input("Please select 1 for polo or 2 for t-shirt: "))
shirt = int(shirt)


if shirt == 1:
    print("You selected polo")
elif shirt == 2:
    print("You selected t-shirt")


n1 = float(input("how many shirts would you like: "))
n2 = 9.99
n3 = 0.13
n4 = (n1*n2*n3)


print("You have the choice of blue, red, and yellow. How many of each would you like?")
b = float(input("Blue: "))
r = float(input("Red: "))
y = float(input("Yellow: "))


c1 = str(b)
c2 = str(r)
c3 = str(y)


print("You chose " + c1.rstrip('0').rstrip('.')+ " Blue " + c2.rstrip('0').rstrip('.') + " Red and " + c3.rstrip('0').rstrip('.') + " Yellow shirts")


print("Your shirts cost ", n1*n2)
print("Your taxes ", round(n1*n2*n3, 2))
print("Your total ", round(n1*n2+n4, 2))


print("Thank you for your order")