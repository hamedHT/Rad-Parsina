# i = 0
# while i <10:
#     print(i)
#     i += 1

# while True:
#   user_input = input("Enter a command (quit to exit): ")
#   if user_input == "quit":
#     break
#   print(f"You entered: {user_input}")

import random

# secret_number = random.randint(1, 100)
# guess = 0
# attempts = 0

# while guess != secret_number:
#   guess = int(input("Guess a number between 1 and 100: "))
#   attempts += 1
#   if guess < secret_number:
#     print("Too low.")
#   elif guess > secret_number:
#     print("Too high.")

# print(f"Congratulations! You guessed the number in {attempts} attempts.")


# n = ''
# while n != 1:
#     print('\n')
#     print('\n')
#     n = int(input("enter number of multiplication table: "))
#     hoop = int(input('enter number of hope: '))
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if i*j % hoop == 0:
#                 print("H",end='\t')
#             else:
#                 print(i*j,end='\t')

number = int(input("enter a number: "))
order = len(str(number))
sum = 0

temp = number
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if number == sum:
    print(number, "is an Armstrong number")
else:
  print(number, "is not an Armstrong number")



