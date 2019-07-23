import characters
#import challenge as challenge
from random import randint
import time 




print()
print("Welcome to Escape Earth!")
print()
print("Just imagine... the year is 431my (that's million years) and the sun is starting to expand.")
print("People are panicking and are doing everything they can to leave the Earth.")
print("You must first get a spaceship. You've got a decision to make.")
print("Are you going to buy a ship or challenge someone for a ship?")
first = input("So, what's it going to be? (C)hallenge or (B)uy?  ")
first = first.upper()
if first == "C":
    ship = challenge()
elif first == "B":
    print("What?")

print("Now, lets get the names of your crew.")

# sets up each crew member
crew = ["captain", "doctor", "mechanic", "scientist", "soldier"]
#description = ["The captain must remain alive for the adventure to continue:  ", "The doctor is the only one who can administer medical kits:  "]
#crew = ["captain", "doctor", "mechanic", "scientist", "soldier"]
description = ["The captain must remain alive for the adventure to continue:  ", "The doctor is the only one who can administer medical kits:  ", "The mechanic is the only one who can fix the ship with repair kits:  ", "The scientist helps determine if food and water are safe to consume:  ", "The soldier is the only one who can do battle with space pirates:  "]
    
for title in crew:
    #print(crew.index(member))
    name = input("Enter the name for the " + title + ". " + description[crew.index(title)])
    #print(crew[crew.index(title)])
    if crew[crew.index(title)] == "captain":
        captain = characters.character(name, title, randint(75,100), 0)
        print("The health level of the captain is: " + str(captain.gethealth()))
    elif crew[crew.index(title)] == "doctor":
        doctor = characters.character(name, title, randint(75,100), 0)
        print("The health level of the doctor is: " + str(doctor.gethealth()))
    elif crew[crew.index(title)] == "mechanic":
        mechanic = characters.character(name, title, randint(75,100), 0)
        print("The health level of the mechanic is: " + str(mechanic.gethealth()))
    elif crew[crew.index(title)] == "scientist":
        scientist = characters.character(name, title, randint(75,100), 0)
        print("The health level of the scientist is: " + str(scientist.gethealth()))
    elif crew[crew.index(title)] == "soldier":
        soldier = characters.character(name, title, randint(75,100), 0)
        print("The health level of the soldier is: " + str(soldier.gethealth()))

print("Again, the health of the captain is: " + str(captain.gethealth()))
print("The health level of the doctor is: " + str(doctor.gethealth()))
print("The health level of the mechanic is: " + str(mechanic.gethealth()))
print("The health level of the scientist is: " + str(scientist.gethealth()))
print("The health level of the soldier is: " + str(soldier.gethealth()))
    
#print("again, the health level of the captain is: " + str(captain.gethealth()))


def main():
    
    return 0


main()
