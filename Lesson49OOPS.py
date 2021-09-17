'''class Avenger:
  def __init__(self, code_name, real_name, power, catchphrase):
    self.code_name = code_name
    self.real_name = real_name
    self.power = power
    self.catchphrase = catchphrase
    self.password = "codingIsAwesome"

  def introduce_self(self):
    return "Hi! My name is {} and my specialty is {}!".format(self.code_name, self.power)

  def say_phrase(???):
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
avenger2 = Avenger("Refactron", "Aaron", "Refactoring code", ???)

# Print out some attributes
print(avenger1.code_name)
print(avenger2.real_name)

# Run some of the methods


Lesson11.4
Giving a class methods
If we think about our User example, there are also common tasks we would want to do with all users such as: edit preferences, change passwords, or post messages. So, classes also usually contain functions that would be used by all objects of that class.

Functions in a class are called methods. They work in exactly the same way as regular functions, we just have to pass in the self parameter:
def change_password(self):
  new_password = input("Enter your new password").strip()
  self.password = new_password
  print("Your password has been changed")
To run them we just use dot notation to call them: user1.change_password()

We have added a few more attributes and methods to the Avenger class for you to test out.

Replace the ??? on line 12 with the missing parameter.
Replace the ??? on line 28 to give avenger2 a catch phrase, you can make this anything you like.
On line 35, call avenger1's introduce_self() method and print the output.
On line 36, call avenger2's say_phrase() method and print the output.
On line 37, call avenger2's reveal_identity() method and print the output.
Click RUN to test it out!

'''


class Avenger:
    def __init__(self, code_name, real_name, power, catchphrase):
        self.code_name = code_name
        self.real_name = real_name
        self.power = power
        self.catchphrase = catchphrase
        self.password = "codingIsAwesome"

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
avenger2 = Avenger("Refactron", "Aaron", "Refactoring code", "Fly this helicopter")

# Print out some attributes
print(avenger1.code_name)
print(avenger2.real_name)

# Run some of the methods
print(avenger1.introduce_self())
print(avenger2.say_phrase())
print(avenger2.reveal_identity())


