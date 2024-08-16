import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0' , '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '&', '(', ')', '*', '+']

nr_letters = int(input("How many letters would you like in your password: "))
nr_symbols = int(input("How many symbols would you like: "))
nr_numbers = int(input("How many numbers would you like: "))

password = []

for letter in range(0, nr_letters):
  password.append(letters[random.randint(0, len(letters) - 1)])

for symbol in range(0, nr_symbols):
  password.append(symbols[random.randint(0, len(symbols) - 1)])

for number in range(0, nr_numbers):
  password.append(numbers[random.randint(0, len(numbers) - 1)])

random.shuffle(password)
password_string = ''.join(map(str, password))
print(password_string)