import random

length = int(input("Enter the password legnth : "))

pswd = ""

for i in range(length):

    digit = random.randint(1, 9)

    pswd += str(digit)


print(f"Your password is : {pswd}")