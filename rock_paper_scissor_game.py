import random
list=['r','p','s']

Chance=10
no_of_chance=0
Human_points=0
Computer_points=0

while(no_of_chance<Chance):
    print("rock,paper,scissor game\n")
    print("r for rock\np for paper\ns for scissor\n")
    guess=input("enter your chance:")
    _random=random.choice(list)

    if guess==_random:
        print("its a tie 0 point for each")


    elif guess=="r" and _random=="p":
        Computer_points=Computer_points+1
        print(f" your guess is {guess} and computer guess is {_random}\n")
        print("computer wins 1 point:")
        print(f"computer point is {Computer_points} and your point is {Human_points}\n")
        

    elif guess=="r" and _random=="s":
        Human_points=Human_points+1
        print(f" your guess is {guess} and computer guess is {_random}\n")
        print("you win 1 point:")
        print(f"computer point is {Computer_points} and your point is {Human_points}\n")


    elif guess=="p" and _random=="s":
        Computer_points=Computer_points+1
        print(f" your guess is {guess} and computer guess is {_random}\n")
        print("computer wins 1 point:")
        print(f"computer point is {Computer_points} and your point is {Human_points}\n")


    elif guess=="p" and _random=="r":
        Human_points=Human_points+1
        print(f" your guess is {guess} and computer guess is {_random}\n")
        print("you win 1 point:")
        print(f"computer point is {Computer_points} and your point is {Human_points}\n")


    elif guess=="s" and _random=="r":
        Computer_points=Computer_points+1
        print(f" your guess is {guess} and computer guess is {_random}\n")
        print("computer wins 1 point:")
        print(f"computer point is {Computer_points} and your point is {Human_points}\n")

    elif guess=="s" and _random=="p":
        Human_points=Human_points+1
        print(f" your guess is {guess} and computer guess is {_random}\n")
        print("you win 1 point:")
        print(f"computer point is {Computer_points} and your point is {Human_points}\n")

    no_of_chance=no_of_chance+1
    print(f" {Chance-no_of_chance} chance left out of {Chance}\n")
    
    

if Computer_points==Human_points:
    print("Tie")

elif Computer_points > Human_points:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")
    
print("game over\n")
print(f"your point is {Human_points} and computer point is {Computer_points}")      
        

        
