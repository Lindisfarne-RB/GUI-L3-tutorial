 '''Adding methods to the Account class
We saw in the introduction that a class also has methods. These are usually functions that would be common to all instances of a class - things that every Account object would need to be able to do.

We want to be able to deposit and withdraw from each account, and also update progress towards the savings goal for the account. So, in this lesson we will write 3 methods that do these things.

CREATE
Let's write the deposit method first.

Under the relevant comment in the editor, define a new method called deposit() which takes 2 parameters self and the amount to deposit.
Inside the function, add an if statement to check if the amount is greater than 0.
If so, add the amount to the account's balance and return True. Remember to use the attributes of a class you need to use the self prefix.
Add an else branch and return False if the deposit was unsuccessful.
Test the deposit method at the end of the program by calling it and depositing $50, then printing the savings balance again.
'''

