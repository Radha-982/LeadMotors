""" Calculator
----------------------------------------
"""


#Defining a function with name addition
#Defining a function with name addition
def addition():
    #Trigger Function 'print' with parameters
    #Trigger Function 'print' with parameters
    print("Addition")
    n = float(input("Enter the number: "))
    t = 0
    ans = 0
    #Repeat action till ###iterator### completes
    #Repeat action till ###iterator### completes
    while n != 0:
        ans = ans + n
        t += 1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans, t]


#Defining a function with name subtraction
#Defining a function with name subtraction
def subtraction():
    #Trigger Function 'print' with parameters
    #Trigger Function 'print' with parameters
    print("Subtraction")
    n = float(input("Enter the number: "))
    t = 0
    sum = 0
    #Repeat action till ###iterator### completes
    #Repeat action till ###iterator### completes
    while n != 0:
        ans = ans - n
        t += 1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans, t]


#Defining a function with name multiplication
#Defining a function with name multiplication
def multiplication():
    #Trigger Function 'print' with parameters
    #Trigger Function 'print' with parameters
    print("Multiplication")
    n = float(input("Enter the number: "))
    t = 0
    ans = 1
    #Repeat action till ###iterator### completes
    #Repeat action till ###iterator### completes
    while n != 0:
        ans = ans * n
        t += 1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans, t]


#Defining a function with name average
#Defining a function with name average
def average():
    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans, t]


#Repeat action till ###iterator### completes
#Repeat action till ###iterator### completes
while True:
    list = []
    #Trigger Function 'print' with parameters
    #Trigger Function 'print' with parameters
    print(" My first python program!")
    #Trigger Function 'print' with parameters
    #Trigger Function 'print' with parameters
    print(" Simple Calculator in python by Malik Umer Farooq")
    #Trigger Function 'print' with parameters
    #Trigger Function 'print' with parameters
    print(" Enter 'a' for addition")
    #Trigger Function 'print' with parameters
    #Trigger Function 'print' with parameters
    print(" Enter 's' for substraction")
    #Trigger Function 'print' with parameters
    #Trigger Function 'print' with parameters
    print(" Enter 'm' for multiplication")
    #Trigger Function 'print' with parameters
    #Trigger Function 'print' with parameters
    print(" Enter 'v' for average")
    #Trigger Function 'print' with parameters
    #Trigger Function 'print' with parameters
    print(" Enter 'q' for quit")
    c = input(" ")
    #Use conditional statement on parameters/check the options
    #Use conditional statement on parameters/check the options
    if c != 'q':
        #Use conditional statement on parameters/check the options
        #Use conditional statement on parameters/check the options
        if c == 'a':
            list = addition()
            #Trigger Function 'print' with parameters
            #Trigger Function 'print' with parameters
            print("Ans = ", list[0], " total inputs ", list[1])
#Use conditional statement on parameters/check the options
#Use conditional statement on parameters/check the options
        elif c == 's':
            list = subtraction()
            #Trigger Function 'print' with parameters
            #Trigger Function 'print' with parameters
            print("Ans = ", list[0], " total inputs ", list[1])
#Use conditional statement on parameters/check the options
#Use conditional statement on parameters/check the options
        elif c == 'm':
            list = multiplication()
            #Trigger Function 'print' with parameters
            #Trigger Function 'print' with parameters
            print("Ans = ", list[0], " total inputs ", list[1])
#Use conditional statement on parameters/check the options
#Use conditional statement on parameters/check the options
        elif c == 'v':
            list = average()
            #Trigger Function 'print' with parameters
            #Trigger Function 'print' with parameters
            print("Ans = ", list[0], " total inputs ", list[1])
        else:
            #Trigger Function 'print' with parameters
            #Trigger Function 'print' with parameters
            print("Sorry, invilid character")
    else:
        break
