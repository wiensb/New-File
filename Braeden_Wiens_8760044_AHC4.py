# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE
# 5. MODULUS DIVISION

print("select an operation to preform:")
print("1. for ADD")
print("2. for SUBTRACT")
print("3. for MULTIPLY")
print("4. for DIVIDE")
print("5. for MODULUS DIVISION")

choice = input()

if choice == '1':
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) + int(num2)))
elif choice == '2':
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) - int(num2)))
elif choice == '3':
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) * int(num2)))
elif choice == '4':
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) / int(num2)))
elif choice == '5':
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) % int(num2)))
else:
    print("INVALID CHOICE.")

input("PRESS ENTER TO EXIT: ")

