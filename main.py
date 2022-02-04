import random
import time
import Animals.Cat as cat
import Animals.Dog as dog

animalList = []

def registerAnimals():
    file = open("Contestants/players.txt","r")
    while(1) :
        line = file.readline()
        data = line.split(';')
        if data[0] == "Dog":
            animalList.append(dog.Dog(data[1],data[2], data[0],vote()))
            continue
        if data[0] == "Cat":
            animalList.append(cat.Cat(data[1],data[2], data[0],vote()))
            continue
        else:
            break


def play():
    print("\nCompetitions is happening. Please wait...")
    for i in range(10):
        print(i)
        time.sleep(1)


def vote():
    return random.randint(1,10)


def displayScores():
    for i in animalList:
        print(i)


def main():
    displayWelcomeMessage()
    registerAnimals()
    play()
    displayScores()


def displayWelcomeMessage():
    print("+++ Welcome to animal competition! +++")
    choice = input("\nWould you like to read the rules? (y/N) : ")
    while(1):
        if choice == "Y" or choice == "y":
            displayRules()
            break
        if choice == "N" or choice == "n":
            print("\nOK! Animals will be registered automatically and we will start soon!")
            break
        else:
            print("Try again!\n")
            continue

def displayRules():
    file = open("Rules/rules.txt","r")
    print(file.read())


if __name__ == '__main__':
    main()
else :
    print("Error! Please run the main.py!")