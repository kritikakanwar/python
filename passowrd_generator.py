import random
password_len = int(input("How many letters would you like in your password? "))
symbols = int(input("How many symbols would you like? "))
numbers = int(input("How many numbers would you like? "))

symb = ['~', '@', '!', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '>']
letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQURSTUVWXYZ'
# Generating random symbols
random_symbols = ''.join(random.choice(symb) for _ in range(symbols))

# Generating random numbers
random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(numbers))

# Generating random letters
random_letters = ''.join(random.choice(letters) for _ in range(password_len - symbols - numbers))

# Combine all parts and shuffle the password
password = list(random_symbols + random_numbers + random_letters)
random.shuffle(password)
password = ''.join(password)

print("Generated Password:", password)





