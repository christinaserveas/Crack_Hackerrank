#game
from numpy import random
my_click = ("rock", "paper", "sissor")
random.choice(my_click)
print(i)
random_number = random.randint(1,10,1)[0]
print(f"you have clicked: {random_number}")
guess = 25
while guess != random_number:
 if guess > 0:
    if guess > random_number:
        print(f"your choice {guess} is greater")
    elif guess < random_number:
        print(f"your choice {guess} is lesser")
    else:
        print("sorry, better luck next time")
        break
    random_number = random.randint(1,10,1)[0]
    print(f"random number is {random_number}")
else:
  print("you win")
