#game
from numpy import random
Clicks = ("rock", "paper", "sissor")
random.choice(Clicks)
print(i)
random_number = random.randint(1,10,1)[0]
print(f"randomn number is {random_number}")
guess = 25
while guess != random_number:
 if guess > 0:
    if guess > random_number:
        print(f"guess number {guess} is bigger")
    elif guess < random_number:
        print( "guess numer {guess} is lesser")
    else:
        print("sorry that you're given up")
        break
    random_number = random.randint(1,10,1)[0]
    print(f"random number is {random_number}")
else:
  print("congrats you win")