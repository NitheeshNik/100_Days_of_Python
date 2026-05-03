print("WEIGHT CONVERSION CALCULATOR")
choice = int(input("Enter your choice (1 or 2): "))
if choice == 1:
    kg = float(input("Enter your weight on kg: "))
    kg *= 2.205
    print(f"{kg:.2f}")
else:
    lb = float(input("Enter your weight on lb: "))
    lb *= 0.451
    print(f"{lb:.2f}")