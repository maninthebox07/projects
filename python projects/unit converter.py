# Desenvolva um programa que converta unidades comuns, 
#como temperatura (Celsius para Fahrenheit), comprimento (metros para pés), ou moedas (dólar para euro).

#Temperature functions
def celsius_fahrenheit(C):
    fahrenheit = (C * 9/5) + 32
    print(f"\n{C} °C is {fahrenheit} °F")
    return fahrenheit
def fahrenheit_celsius(F):
    celsius = (F - 32) * (5 / 9)
    print(f"\n{F} °F is {celsius: .2f} °C")
    return celsius

#Length functions
def meter_feet(meter):
    feet = meter * 3.281
    print(f"\n{meter} meter(s) is {feet} ft")
    return feet
def feet_meter(feet):
    meter = feet / 3.281
    print(f"\n{feet} ft is {meter: .2f} meter(s)")

#Currency functions
def dollar_euro(dollar):
    euro = dollar * 0.94
    print(f"\n${dollar} is €{euro: .2f}")
    return euro
def euro_dollar(euro):
    dollar = euro * 1.07
    print(f"\n€{euro} is ${dollar: .2f}")
    return dollar

#Welcome and instructions
print("Welcome to the Python Converter! Look at the options below and choose the one you want:")
print("\n1. Temperature\n" "2. Length\n" "3. Currency\n")
choice = float(input("Write the option number to choose: "))

#Loop for the options
while True:
    if choice == 1:
        print("\nTemperature:\n" "1. Celsius to Fahrenheit\n" "2. Fahrenheit to Celsius\n")
        temp_choice = float(input("Write the option number to choose: "))
        if temp_choice == 1:
            celsius_fahrenheit(float(input("\nType the temperature in Celsius: ")))
        elif temp_choice == 2:
            fahrenheit_celsius(float(input("\nType the temperature in Fahrenheit: ")))
        else:
            print("\nInvalid option! Try again.\n")
            print("\nTemperature:\n" "1. Celsius to Fahrenheit\n" "2. Fahrenheit to Celsius\n")

    elif choice == 2:
        print("\nLength:\n" "1. Meters to Feet\n" "2. Feet to Meters\n")
        length_choice = float(input("Write the option number to choose: "))
        if length_choice == 1:
            meter_feet(float(input("\nType the length in meters: ")))
        elif length_choice == 2:
            feet_meter(float(input("\nType the length in feet: ")))
        else:
            print("\nInvalid option! Try again.\n")

    elif choice == 3:
        print("\nCurrency:\n" "1. Dollar to Euro\n" "2. Euro to dollar\n")
        currency_choice = float(input("Write the option number to choose: "))
        if currency_choice == 1:
            dollar_euro(float(input("\nType the value in dollar:  ")))
        elif currency_choice == 2:
            euro_dollar(float(input("\nType the value in euro:  ")))
        else:
            print("Invalid option! Try again.")

    else:
        print("\nInvalid option! Try again.\n")
        print("\n1. Temperature\n" "2. Length\n" "3. Currency\n")
        choice = float(input("Write the option number to choose: "))