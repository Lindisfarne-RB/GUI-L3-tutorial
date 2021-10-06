import random
import time

car1, car2, car3, car4, car5, car6 = 0, 0, 0, 0, 0, 0


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        error = "Please enter yes / no"

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print(error)

def user_choice1(question):
    valid = False
    while not valid:

        error = "Please enter a whole number from 1 to 6\n"

        try:
            response = int(input(question))

            if 1 <= response <= 6:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


def user_choice2(question):
    valid = False
    while not valid:

        error = "Please enter a whole number from 5 to 15\n"

        try:
            response = int(input(question))

            if 5 <= response <= 15:
                return response

            else:
                print(error)

        except ValueError:
            print(error)

played_before = yes_no("Have you played this game before? ")
print(("You chose {}\n").format(played_before))
if played_before == "no":
    print("--------------- Intructions ---------------")
    print("First, choose the car number you think will win.")
    print("Second, choose a distance for the race, this will determine how many times the die are rolled.")
    print("Each time the die lands on a car number, it will move forward 100m - The car that goes the furthest wins.")
    print("Once you have completed these inputs, the race results will be displayed!\n")

car_number = user_choice1("Enter your car number (1-6): ")
print("You have chosen Car No. {}\n".format(car_number))

race_distance = user_choice2("Enter a race distance (5-15): ")
print("You have chosen a Race distance of {}\n".format(race_distance))


for i in range(0, race_distance):
    rolling_dice = random.randint(1, 6)
    if rolling_dice == 1:
        car1 += 100

    elif rolling_dice == 2:
        car2 += 100

    elif rolling_dice == 3:
        car3 += 100

    elif rolling_dice == 4:
        car4 += 100

    elif rolling_dice == 5:
        car5 += 100

    elif rolling_dice == 6:
        car6 += 100

    else:
        pass

time.sleep(1)
print(("Car 1 went {}m").format(car1))
time.sleep(1)
print(("Car 2 went {}m").format(car2))
time.sleep(1)
print(("Car 3 went {}m").format(car3))
time.sleep(1)
print(("Car 4 went {}m").format(car4))
time.sleep(1)
print(("Car 5 went {}m").format(car5))
time.sleep(1)
print(("Car 6 went {}m\n").format(car6))
time.sleep(1)
print(". . .\n")

car_list = [car1, car2, car3, car4, car5, car6]

time.sleep(3)

print(("The car that won went {}m").format(max(car_list)))

'''
Create an empty list called grocery_list on line 2.
Replace the ??? on line 10 with the correct value to check if the user has finished inputting their list.
Replace the ??? on line 11 with the correct value to stop the loop.
On line 14, replace the ??? with a correct line of code to check if the item is in the list using count().
On line 25, sort the list into order.
RUN the code and check that it works correctly by adding some items out of order, and then typing done.


# Create an empty grocery_list
grocery_list = []

# Start a loop to ask user to enter their grocery list
repeat = True
while repeat == True:
   item = input("Please enter an item or 'done' to end input: ").strip().lower()

   # Check if user has entered done so that loop can be stopped if so
   if item == "done":
       repeat = False
   else:
       # Check if item is already in list
       count = grocery_list.count(item)

       # If so, give user error message, otherwise add the item and give success message
       if count > 0:
           print("Sorry {} is already on the list!".format(item))
       else:
           grocery_list.append(item)
           print("{} has been added!".format(item))

# Once user is done, sort the list then print out their list for them
grocery_list.sort()
#print("Your grocery list is:",grocery_list)

print(grocery_list)
# address of the first element of grocery_list 0x0000BF... dynamic


for item in grocery_list:
   print(item.title())  # Add a capital letter

'''



'''# Student lists
students_present = ["tommy", "dahlia", "manaia", "isaac", "jamila", "britt", "patrick", "jessika", "chantal", "rocio"]
students_absent = ["iliana", "olympia", "juan", "kelsey"]

# Sort the students present list and print
print("Students present: ")

students_present.sort()

for student in students_present:
    print(student.title())

# Sort the students absent list and print
students_absent.sort()
print("Students absent: ")
for student in students_absent:
    print(student.title())


'''

'''favorite_foods = []

# Start a loop to ask user to enter their favorite foods
repeat = True
while repeat:
    food = input("Please enter a favorite food or 'done' to end input: ").strip().lower()

    # Check if user has entered done so that loop can be stopped if so
    if food == 'done':
        repeat = False
    else:
        # Check if food is already in list
        count =favorite_foods.count(food)
        # If so, give user error message, otherwise add the food and give success message
        if count > 0:
            print("Sorry {} is already on the list!".format(food))
        else:
            favorite_foods.append(food)
            print("{} has been added!".format(food))

# Once user is done, print out their list for them
print("Your favorite foods are: ")

for food in favorite_foods:
    print(food.title())  # Add a capital letter

Read the code in the editor. Replace the ??? to add a condition on line 5 that will run the while loop.
    On line 13, use count() to find how many times the food the user has entered is in the list. Store this number in a variable called count.
Replace the ??? on line 19 to add the use
r's input to the favorite_foods list.
Replace the ??? on line 25 to loop through and print out each food in the list on a new line.'''

'''
#List of weapons available
weapons_available = ["Dagger", "Lance", "Flail", "Medieval Sword", "Broadsword", "Falchion sword", "Greatsword", "Longsword"]

#Print the position of the Broadsword
print(weapons_available.index("Broadsword"))

#Find the position of the Flail and store as index
i=weapons_available.index("Flail")

#Print the index of the Flail in the sentence.
print (i, "is the index of Flail")


Print the position of the Broadsword in the list of weapons available for the Knights who say Ni!
Find the position of the Flail and store in a variable called index.
Print the index variable in the sentence The Flail is in position { } using .format().


#List of weapons available
weapons_available = ["Dagger", "Lance", "Flail", "Medieval Sword", "Broadsword", "Falchion sword", "Greatsword", "Longsword"]

#Print the list with commas separating
print(", ".join(weapons_available))

#Print the list with spaces separating
print(" ".join(weapons_available))

#Print the list with tildes separating ~
print("~ ".join(weapons_available))

#Print the list with roses separating @-->--
print("@-->--".join(weapons_available))

The text you want to join each value with goes first, inside quotes, then the name of the list goes in the brackets of join().
Click RUN to see how the print statement on line 5 comes out, printing the list of weapons separated with commas ,.
On line 8, write code to print the list of weapons separated with single spaces.
On line 11, print the weapons separated with tildes ~.
On line 14, just for fun, separate the weapons with roses @-->--.


'''

''''#Student lists
students_present = ["tommy", "dahlia", "manaia", "isaac", "jamila", "britt", "patrick", "jessika", "chantal", "rocio"]
students_absent = ["iliana", "olympia", "juan", "kelsey"]
#Print out students present:
#Print number of students present
for x in students_present:
    print (x.title())

print("Total students present: {}.".format(len(students_present)))
#Print out students absent
for x in students_absent:
    print (x.title())
#Print number of students absent
print("Total students absent: {}.".format(len(students_absent)))
'''


'''Use a for loop on line 6 to print out each student that is present on a new line.
Replace the ??? in the print statement on line 10 with a function that will insert the number of students present.
Use a for loop to print out each student that is absent on a new line under the relevant comment.
Replace the ??? in the last print statement with a function that will insert the number of students absent.
(Optional) Use .title() to print out each student's name with a capital letter at the start.
'''



'''myname=['P','Y','T','H','O','N', 1,2,3,4.6,6.89 , 'Hello', "world"]


newlist=[1,2,3,4]
print(newlist[0:4])
print(newlist)

print(myname[2:10:2]) # 2 is inclusive and 5 in exclusive- 2,3,4

#[P, 'T', 'o' , 1 ,3,6.89, "world"]
#print(myname[0:len(myname):2])

print(myname[::3])
'''



'''

list1 = [34, 56, 12, 67, 22]
# Largest
Largest = 0
for x in list1:
    if x > Largest:
        Largest = x

print(Largest)


# Smallest
small = 100
for x in list1:
    if x < small:
        small = x

print(small)

print("-----------------------------")
# Double the values in a list


newlist=[] # create an empty list
for x in list1:
    x = x * 2
    newlist.append(x) # to add a new value to the list
print(newlist)

'''
