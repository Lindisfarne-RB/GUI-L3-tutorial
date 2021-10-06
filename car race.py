'''Car Racer – in this game users choose a car (numbered one to 6). Then they choose a ‘race distance’
which should be between 5 and 15. A simulated die is rolled and if the car’s number comes up, it
moves forward one space. The winning car is the one which gets to the race distance the first.
Your game should…
● Allow users to choose a car and a distance
● Race the cars. If you are using a text based programming language like Python, it is not
necessary to show each step but the final outcome should be shown and it should be easy
for users to see which car has won.
● Clearly state which car won and give the ‘time’ (ie: number of steps needed).Al
'''
#This program has some extra functions that are not called.
# This program does not assign any points to the winner cars
# this program does not count leader board correctly - needs to work on second and third position

import random

def points():
    first=5
    sec=3
    third=1

    return

def positions():
    return


def findLargest(listofcars):
    print("in largest")
    secondLargest = listofcars[0]
    largest = listofcars[0]
    for i in range(len(listofcars)):
        if listofcars[i] > largest:
            largest = listofcars[i]

    for i in range(len(listofcars)):
        if listofcars[i] > secondLargest and listofcars[i] != largest:
            secondLargest = listofcars[i]
    print(secondLargest)
    return secondLargest

def roll(dist):
    car1, car2, car3, car4, car5, car6 = 0, 0, 0, 0, 0, 0
    car_dist_1,car_dist_2,car_dist_3,car_dist_4,car_dist_5,car_dist_6= 0, 0, 0, 0, 0, 0
    for i in range(1, dist + 1):
        rolling_dice = random.randint(1, 6)
        print("roll....", i, " - ", rolling_dice)
        if rolling_dice == 1:
            car_dist_1 += 1
            car1 +=1
        elif rolling_dice == 2:
            car_dist_2 += 1
            car2 += 1
        elif rolling_dice == 3:
            car_dist_3 += 1
            car3 += 1
        elif rolling_dice == 4:
            car_dist_4 += 1
            car4 += 1
        elif rolling_dice == 5:
            car_dist_5 += 1
            car5 += 1
        elif rolling_dice == 6:
            car_dist_6 += 1
            car6 += 1
        else:
            pass

    listofcars = [car_dist_1, car_dist_2,car_dist_3, car_dist_4, car_dist_5, car_dist_6]
    print("Dist =", listofcars)
    max_value = None
    max_idx = None

    for i in listofcars:

        if (max_value is None or  i > max_value):
            max_value = i
            max_idx = listofcars.index(max_value)


    #print('Maximum value:', max_value, "At index: ", max_idx+1)
    print("-----------LEADER BORAD ------------")
    print("First position  - car num", max_idx+1 ,"run distance", max_value , " kms")
    #findLargest(listofcars)
    seclar=seclargest(listofcars)
    thirdlar=thirdlargest(listofcars)

    return(max_idx)

def seclargest(listofcars):
    print("Second car is:", sorted(listofcars)[-2])
    return

def thirdlargest(listofcars):
    print("Third car is:", sorted(listofcars)[-3])
    return

def checkcar_distnum(question,low,high):
    error = "Please enter in the specified range "
    valid = False
    while True:
        try:

            car_num = int(input(question))
            if low <= car_num <= high :
                return car_num

            else:
                print(error)
        except ValueError:
            print(error)

    return


def checkdistance(question,low,high):
    error = "Please enter distance between 5-15"
    valid = False
    while True:
        try:

            dist = int(input(question))
            if dist > low and dist < high:
                return dist

            else:
                print(error)
        except ValueError:
            print(error)

    return

def instruction_play():
    print("This is how you play")
    print("Let's start")
    return

def roundsplayed():
    #rounds = int(input("How many rounds 1 - 10 "))
    rounds = checkcar_distnum("How many rounds: Enter between 1-10 ",1,10)
    return rounds

def yes_no():
    played=input("Have you played this game before")
    if played == "No" or played == "NO" or played == "no":
        instruction_play()
    return
""

#main section starts here

yes_no()
rounds=roundsplayed()
ctr = 1


while ctr <= rounds:
    print("--------------Round ", ctr, "--------------------")

    car_num= checkcar_distnum("Enter car num 1-6",1,6)

    print("You are betting on car num ", car_num)
    dist = checkcar_distnum("Enter distance 5-15 ",5,15)
    print("We are going $ ")
    winner_car_num = roll(dist)
    print("Winner = car ", winner_car_num + 1)

    ctr += 1
