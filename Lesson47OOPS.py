'''11.2
Giving a class attributes
What do we mean when we say classes group related data and functions? Well, if we think of a user of, say, a gaming or social networking site, there are a bunch of pieces of information we would need to store for all users such as:

Username
Actual name
Date of birth
Password
And so on.

You might recognise these as things we might usually use variables for. By putting them in a class, we can create an object for each user, and then we can store their own details without having to rewrite all of the code for every user.

Variables like this inside a class are called attributes. They are set the same way as normal variables, but are accessed by using dot notation:

print(bob.name)
CREATE
Inside the class, delete the pass  keyword.
Add an attribute to the class called code_name and set it to D-Bug.
Add another attribute for real_name and set it to your own name or a name of your choice.
Underneath the line where avenger1 is instantiated, print avenger1.code_name.
Click RUN to see the output.
Now below that, print out the real name too.

'''


class Avenger:
    code_name = "D-Bug"
    real_name = "RB"


# Create an instance of the Avenger class
avenger1 = Avenger()

# Print out some attributes
print(avenger1.code_name)
print(avenger1.real_name)