print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? \n"))
people = int(input("How many people to split the bill?\n"))
value_1 = bill / people
tip_1 = (tip / 100 )*  value_1
print(f"Each person should pay: ${{{value_1+tip_1:.2f}}}")
print("nk")
