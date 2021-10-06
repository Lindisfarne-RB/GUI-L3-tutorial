'''Using the __init__ function to set custom attributes
Hmm, no doubt you can see that hard-coding the values for the attributes is not that helpful if we want our code to be reusable–we don't want every Avenger object to be called D-Bug!

Attributes are usually set in a built-in method called __init__ which is run as soon as the object is created (or instantiated) and takes a parameter called self. We can add other parameters, and then set values for them when we instantiate an object.

You can run this in the example code. We don't have to pass in anything for self when we create an object, just the other parameters in the correct order. We then add the self. prefix to any attributes.
We've added the __init__ method for you to work with.

Add a parameter for code_name to the __init__ method and set the self.code_name attribute equal to it inside the method.
Add a parameter for real_name and set the self.real_name attribute equal to it.
Edit the line where avenger1 is instantiated and pass in values for code_name and real_name.
Create a second Avenger called avenger2 and pass in different values for both names.
Print out avenger1's code name.
Print out avenger2's real name.
Click RUN to see the output.
Note: __init__ is pronounced as dunder init, as the double underscore character is often referred to as a dunder.'''


class Avenger:
    def __init__(self, code_name, real_name):
        self.code_name = code_name
        self.real_name = real_name


# Create an instance of the Avenger class
avenger1 = Avenger("Bob", "Tom")
avenger2 = Avenger("Dob", "Dom")

# Print out some attributes
print(avenger1.code_name)
print(avenger2.real_name)



