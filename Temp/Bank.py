#Defining  a class with name Bank_Account
#Defining  a class with name Bank_Account
class Bank_Account:
    #Defining a function with name __init__
    #Defining a function with name __init__
    def __init__(self):
        #Initialize variables like balance for performing functionality
        #Initialize variables like balance for performing functionality
        self.balance = 0
        #Trigger Function 'print' with parameters
        #Trigger Function 'print' with parameters
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

#Defining a function with name deposit

#Defining a function with name deposit

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        #Trigger Function 'print' with parameters
        #Trigger Function 'print' with parameters
        print("\n Amount Deposited:", amount)

#Defining a function with name withdraw

#Defining a function with name withdraw

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        #Use conditional statement on parameters/check the options
        #Use conditional statement on parameters/check the options
        if self.balance >= amount:
            self.balance -= amount
            #Trigger Function 'print' with parameters
            #Trigger Function 'print' with parameters
            print("\n You Withdrew:", amount)
        else:
            #Trigger Function 'print' with parameters
            #Trigger Function 'print' with parameters
            print("\n Insufficient balance ")


#Defining a function with name display

#Defining a function with name display

    def display(self):
        #Trigger Function 'print' with parameters
        #Trigger Function 'print' with parameters
        print("\n Net Available Balance=", self.balance)

s = Bank_Account()
s.deposit()
s.withdraw()
s.display()

start = 11
end = 25
#Trigger Function 'range' with parameters
#Repeat action till iterator completes
#Trigger Function 'range' with parameters
#Repeat action till iterator completes
for i in range(start, end + 1):
    #Use conditional statement on parameters/check the options
    #Use conditional statement on parameters/check the options
    if (i > 1):
        #Trigger Function 'range' with parameters
        #Repeat action till iterator completes
        #Trigger Function 'range' with parameters
        #Repeat action till iterator completes
        for j in range(2, i):
            #Use conditional statement on parameters/check the options
            #Use conditional statement on parameters/check the options
            if (i % j == 0):
                break
        else:
            #Trigger Function 'print' with parameters
            #Trigger Function 'print' with parameters
            print(i)


#Defining  a class with name Bank_Account
#Defining  a class with name Bank_Account
class Bank_Account:
    #Defining a function with name __init__
    #Defining a function with name __init__
    def __init__(self):
        #Initialize variables like balance for performing functionality
        #Initialize variables like balance for performing functionality
        self.balance = 0
        #Trigger Function 'print' with parameters
        #Trigger Function 'print' with parameters
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

#Defining a function with name deposit

#Defining a function with name deposit

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        #Trigger Function 'print' with parameters
        #Trigger Function 'print' with parameters
        print("\n Amount Deposited:", amount)

#Defining a function with name withdraw

#Defining a function with name withdraw

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        #Use conditional statement on parameters/check the options
        #Use conditional statement on parameters/check the options
        if self.balance >= amount:
            self.balance -= amount
            #Trigger Function 'print' with parameters
            #Trigger Function 'print' with parameters
            print("\n You Withdrew:", amount)
        else:
            #Trigger Function 'print' with parameters
            #Trigger Function 'print' with parameters
            print("\n Insufficient balance ")


#Defining a function with name display

#Defining a function with name display

    def display(self):
        #Trigger Function 'print' with parameters
        #Trigger Function 'print' with parameters
        print("\n Net Available Balance=", self.balance)

s = Bank_Account()
s.deposit()
s.withdraw()
s.display()

start = 11
end = 25
#Trigger Function 'range' with parameters
#Repeat action till iterator completes
#Trigger Function 'range' with parameters
#Repeat action till iterator completes
for i in range(start, end + 1):
    #Use conditional statement on parameters/check the options
    #Use conditional statement on parameters/check the options
    if (i > 1):
        #Trigger Function 'range' with parameters
        #Repeat action till iterator completes
        #Trigger Function 'range' with parameters
        #Repeat action till iterator completes
        for j in range(2, i):
            #Use conditional statement on parameters/check the options
            #Use conditional statement on parameters/check the options
            if (i % j == 0):
                break
        else:
            #Trigger Function 'print' with parameters
            #Trigger Function 'print' with parameters
            print(i)
