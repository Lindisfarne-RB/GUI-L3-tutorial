'''Lesson11.1
    Introduction to object-oriented programming
In lessons 11-20 we are going to learn about object-oriented programming or OOP. OOP is about grouping related data and functions into structures called classes. Classes make it easier to write more complex programs without having to repeat code. In other words, we can keep our code DRY!

A class is created using the class keyword and a name that is in CamelCase. An instance of the class is created by calling the class:
class User:
  #Data and functions common to all users

#Create an instance of the class
bob = User()
In this example bob is an instance of the User class or an object, and he'll have all of the data and functions we put inside the class. You can make multiple instances of a class and the word we use to describe creating an instance/object is instantiating.

CREATE
In the editor on line 1, create a class called Avenger
Click RUN and see the error you get.
Inside the class, just write the keyword pass  for now. This just says to skip this for now, since we have no code inside the class.
If you click RUN now, you won't see anything but you also won't see the error.
Outside of the class, under the comment, create an instance of the Avenger class called avenger1.
TIPS
DRY Dont repeat yourself

 '''


class Avenger:
    pass


# Create an instance of the Avenger class
avenger1 = Avenger()



