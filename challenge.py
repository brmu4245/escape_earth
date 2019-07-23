import time
from random import randint

def challenge():
    say = open('scripts/challenge.txt', 'r')
    content = say.read()
    print(content)
    ready = input("Are you ready? (Y)es or (N)o   ")
    if ready.upper() == "N":
        comeon()
    elif ready.upper() == "Y":
        ship = prob()
        return ship
    else:
        print()
        print("What?? I don't think you're even trying. This will continue to repeat until you cooperate.")
        challenge()


def comeon():
    print()
    print("Well, okay Pokee Joe... Are you scared?")
    input("Just hit return to repeat this, I guess.")
    challenge()

def prob():
    var_1 = randint(1, 500)
    var_2 = randint(1, 500)
    op = ["*", "/", "+", "-"]
    rndop = op[randint(0,3)]
    if rndop == 0:
        prob = str(var_1) + " * " + str(var_2)
        answer = var_1 * var_2
    elif rndop == 1:
        prob = str(var_1) + " / " + str(var_2)
        answer = var_1 / var_2
    elif rndop == 2:
        prob = str(var_1) + " + " + str(var_2)
        answer = var_1 + var_2
    else:
        prob = str(var_1) + " - " + str(var_2)
        answer = var_1 - var_2
    return timed_prob(prob, answer)

def timed_prob(problem, answer):
    time1 = time.time()    
    print("time 1 = " + str(time1))
    print()
    print("Your problem is: " + problem)
    trial = int(input("Enter your answer quickly:  "))
    if trial == answer:
        print()
        print("You got it! Congratulations!")
        time2 = time.time()
        winning_time = time2 - time1
        print(winning_time)
        return ship_won(winning_time)
    else: 
        print()
        print("Oh, too bad! You got the wrong answer!")
        print("You get the slowest ship... Class 1.")
        print()
        return("Class 1")

def ship_won(player_time):
    if player_time <= 5:
        print()
        print("You got the fastest ship... the Class 5 Elite!!!")
        print()
        return("Class 5 Elite")
    elif player_time <= 7:
        print()
        print("You got the 2nd fastest ship... the Class 4 Super!!!")
        print()
        return("Class 4 Super")
    elif player_time <= 9:
        print()
        print("You got the 3rd fastest ship... the Class 3 Average!!!")
        print()
        return("Class 3 Average")
    elif player_time <= 11:
        print()
        print("You got the 4th fastest ship... the Class 4.")
        print()
        return("Class 4")
    else:
        print()
        print("You got the slowest ship... the Class 1.")
        print()
        return("Class 1")