'''
Project - 2
The perfect guess
'''

from random import randint

n = randint(1,100)
a = -1

guesses = 1
while(a!=n):
    a= int(input("Guess the number buddy: "))
    if(a>n):
        print("Lower number please")
        guesses +=1
    elif(a<n):
        print("Higher number please")
        guesses +=1

print(f"Hey you guessed it right, it's {n} in {guesses} attempts")