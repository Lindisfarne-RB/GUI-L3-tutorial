'''Private vs. public attributes
In Python, we have public attributes and private attributes. Public attributes can be accessed by any code anywhere in the program. Private attributes, however, should only be accessed within the class itself. This could be, for example, to make sure they don't get modified when they shouldn't.

Private attributes are shown by putting an underscore in front of the name:
def __init__(self):
  self.type = "dog"
  self._food_need = 3
Adding the underscore doesn't prevent the _food_need value from being accessed, but it lets developers know that the attribute shouldn't be used outside of the class. It is a naming convention.

CREATE
Let's have a look at our Avengers class

Which do you think is the first attribute that should be private in this class?
Add the underscore prefix to this attribute in each place that it appears in the code.
Which do you think is the second attribute that should be private in this class?
Add the underscore prefix to this attribute in each place that it appears in the code.
Click RUN and you'll see that we can still print out private attributes, but this is not how we should access them.
'''


class Avenger:
  def __init__(self, code_name, real_name, power, catchphrase):
    self.code_name = code_name
    self._real_name = real_name
    self.power = power
    self.catchphrase = catchphrase
    self._password = "codingIsAwesome"

  def introduce_self(self):
    return "Hi! My name is {} and my specialty is {}!".format(self.code_name, self.power)

  def say_phrase(self):
    return self.catchphrase

  def reveal_identity(self):
    for i in range(3):
      password = input("Enter the password: ").strip()
      if password == self.password:
        return "{}'s real name is... {}.  But don't tell anyone!".format(self.code_name, self.real_name)
      else:
        print("Sorry, you have to know the password to learn {}'s identity".format(self.code_name))
    else:
      return "You ran out of guesses"


# Create an instance of the Avenger class
avenger1 = Avenger("D-Bug", "Josh", "Debugging code", "I declare this code... Bug free!")
avenger2 = Avenger("Refactron", "Aaron", "Refactoring code", "Hmm, I'll just put this over here")

# Print out some attributes
print(avenger1.code_name)
print(avenger2.real_name)

# Run some of the methods
print(avenger1.introduce_self())
print(avenger2.say_phrase())
print(avenger2.reveal_identity())
