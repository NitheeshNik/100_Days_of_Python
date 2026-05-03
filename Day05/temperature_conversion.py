print("Temperature Conversion Program")
print("C. Celsius to Fahrenheit")
print("F. Fahrenheit to Celsius")
choice = input("Is the temp in Celsius (C) or Fahrenheit (F): ")
if choice == 'c' or choice == 'C':
    c = float(input("Enter the temperature in Celsius: "))
    f = c * 9 / 5 + 32
    print(f"{c:.2f}\u00B0C Celsius is equal to {f:.2f}\u00B0F Fahrenheit")
elif choice == 'f' or choice == 'F':
    f = float(input("Enter the temperature in fahrenheit: "))
    c = (f - 32) * 5 / 9
    print(f"{f:.2f}\u00B0F fahreheit is equal to {c:.2f}\u00B0C Celsius")
else:
    print("Invalid choice")