# Crie um programa que permita ao usuário realizar operações matemáticas básicas,
# como adição, subtração, multiplicação e divisão.

#Welcomes the user and shows the calculator options
print("Welcome to the Python Calculator!\n")

#Loop for the calculator options
while True:
    print("Choose one of the options below:")
    print("1. Sum" "\n2. Subtraction" "\n3. Multiplication" "\n4. Division" "\n5. Stop")
    options = float(input("\nChoose the option here: "))

#Option 1 conditional (sum)
    if options == 1:
        print("\nYou chose the Sum option")
        f_sum_num = float(input("Write the first number: "))
        s_sum_num = float(input("Write the second number: "))
        sum = f_sum_num + s_sum_num
        print(f"\nThe result is: {sum}\n")

#Option 2 conditional (subtraction)
    elif options == 2:
        print("\nYou chose the Subtraction option ")
        f_sub_num = float(input("Write the first number: "))
        s_sub_num = float(input("Write the second number: "))
        sub = f_sub_num - s_sub_num
        print(f"\nThe result is: {sub}\n")

#Option 3 conditional (multiplication)
    elif options == 3:
        print("\nYou chose the Multiplication option ")
        f_mult_num = float(input("Write the first number: "))
        s_mult_num = float(input("Write the second number: "))
        mult = f_mult_num * s_mult_num
        print(f"\nThe result is: {mult}\n")

#Option 4 conditional (division)
    elif options == 4:
        print("\nYou chose the Division option ")
        f_div_num = float(input("Write the first number: "))
        s_div_num = float(input("Write the second number: "))
        sub = f_div_num / s_div_num
        print(f"\nThe result is: {sub}\n")

#Option 5 conditional (stops the calculator)
    elif options == 5:
        break
    
    else:
        print("\nInvalid option! Try again.\n")