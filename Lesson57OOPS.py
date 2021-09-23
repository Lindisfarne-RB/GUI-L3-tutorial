'''Public vs. Private methods
Just like attributes, methods in a class can be public or private.

A public method can be accessed from anywhere in the program, inside or outside the class.

A private method, however, should only be accessed from within the class itself, which means it will be called by another method inside the class. Private methods have underscores _ before the name as well:
def MyClass:
  def public_method(self):
    # Code

  def _private_method(self):
    # Code
Our Account class doesn't really have any need for private methods other than our __init__ method, so let's see an example where it is useful.

In the editor is some partial code for a Patient class, say for some kind of medical program.

Are there any private attributes in the class?
No
Is the method for calculating the user's age public or private?
Private
Is the method for updating the immunization status public or private?
Public
Is the method for updating the user's details public or private?
Public
'''

import datetime
class Patient:
    """A class for storing and updating patient details including immunisation status"""

    def __init__(self, name, address, phone, dob, age, weight, height):
        self.name = name
        self.address = address
        self.phone = phone
        self.dob = dob
        self.age = self._get_age()
        self.weight = weight
        self.height = height

        patient_list.append(self)

    def _get_age(self):
        # Calculate the user's age based on DOB
        birth_date = datetime.strptime(self.dob, '%m/%d/%Y')
        age = int((datetime.today() - birth_date).days / 365)
        return age

    def update_immunisations(self):
        # Update patient's immunisation status
        pass

    def update_details(self):
        # Update patient's personal details
        pass




