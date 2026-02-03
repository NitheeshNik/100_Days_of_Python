import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
start = random.randint(0, 52)
print("Welcome to the PyPassword Generator!")
# Get a input from user
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# store the char to the list password_list

password_list = []
# use loop for making random letters
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

    # Use loop for making random numbers
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

    # Use loop for making random symbols
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

    # print the password_list store into the password_list
print(password_list)

# Use random.shuffle to mix the list char's
random.shuffle(password_list)
print(password_list)

# Use join function to convert list to string
print("".join(password_list))

# manual way to convert list to string using for loop
password = ""
for char in password_list:
    password += char

# print final password
print(f"Your password is: {password}")