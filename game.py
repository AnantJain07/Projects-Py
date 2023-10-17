import random

compRes = random.randint(0,100)

response = int(input('Enter your number: '))
print("Computer no. ",compRes)
if(compRes>=response):
    print('your number is lesser or equal.')
else:
    print('your number is bigger.')


