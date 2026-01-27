print("Welcome to Python Pizza Deliveries!")
size = str(input("What size pizza do you want? S, M or L: "))
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size == 's':
    bill += 15
    if pepperoni == 'y':
        bill += 2
        if extra_cheese == 'y':
            bill += 1
elif size == "m":
    bill += 20
    if pepperoni == 'y':
        bill += 3
        if extra_cheese == 'y':
            bill += 1

elif size == "l":
    bill += 25
    if pepperoni == 'y':
        bill += 3
        if extra_cheese == 'y':
            bill += 1
else:
    print(bill)


print(f"Your final bill is : ${bill}.")




