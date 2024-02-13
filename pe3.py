# install packages
import string
from datetime import date, timedelta

#define encode(input_text, shift)
def encode(input_text: str, shift:int):
    
    input_characters = [*input_text.lower()]
    all_eng_cha = [*string.ascii_lowercase]
    encoded = []

    for letter in input_characters:
      if letter in string.punctuation or letter == " ":
        encoded.append(letter)
      else:
        encoded.append(all_eng_cha[(all_eng_cha.index(letter) + shift)%26])
      
    
    return (
        (all_eng_cha, "".join(encoded))
    )

#define decode(input_text, shift)

def decode(input_text: str, shift:int):
        
    input_characters = [*input_text]
    all_eng_cha = [*string.ascii_lowercase]
    decoded = []

    for letter in input_characters:
      if letter in string.punctuation or letter == " ":
        decoded.append(letter)
      else:
        decoded.append(all_eng_cha[(all_eng_cha.index(letter) - shift)%26])
     
    return ("".join(decoded))

# Classes
# A. BankAccount
# B. SavingsAccount
# C. CheckingAccount



class BankAccount:
    def __init__(self, name="Rainy", ID="1234", creation_date=date.today(), balance=0):
        
        # Default values set
        self.name = name
        self.ID = ID
        self.creation_date = creation_date 
        self.balance = balance

        # Validate creation_date
        if self.creation_date > date.today():
            raise Exception("The creation date is invalid. Cannot be a future date.")

    def deposit(self, amount):
        if amount < 0:
            self.balance = self.balance
        else:
           self.balance += amount

        print(self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print( self.balance)

    def view_balance(self):
        print(self.balance)


class SavingsAccount(BankAccount):
    def withdraw(self, amount):

        if (date.today() - self.creation_date).days < 180 or self.balance - amount < 0:
            self.balance = self.balance
        else:
            self.balance -= amount
        
        print( self.balance)


class CheckingAccount(BankAccount):
    def withdraw(self, amount):

        if self.balance - amount < 0:
            self.balance -= 30  # Overdraft fee for CheckingAccount
            self.balance -= amount
        else:
            self.balance -= amount
        return self.balance


