class Bank_Account: 
	def __init__(self): 
		self.balance=0
		print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 

	def deposit(self): 
		amount=float(input("Enter amount to be Deposited: ")) 
		self.balance += amount 
		print("\n Amount Deposited:",amount) 

	def withdraw(self): 
		amount = float(input("Enter amount to be Withdrawn: ")) 
		if self.balance>=amount: 
			self.balance-=amount 
			print("\n You Withdrew:", amount) 
		else: 
			print("\n Insufficient balance ") 

	def display(self): 
		print("\n Net Available Balance=",self.balance) 


s = Bank_Account() 
s.deposit() 
s.withdraw() 
s.display() 


start = 11
end = 25
for i in range(start,end+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)



class Bank_Account: 
	def __init__(self): 
		self.balance=0
		print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 

	def deposit(self): 
		amount=float(input("Enter amount to be Deposited: ")) 
		self.balance += amount 
		print("\n Amount Deposited:",amount) 

	def withdraw(self): 
		amount = float(input("Enter amount to be Withdrawn: ")) 
		if self.balance>=amount: 
			self.balance-=amount 
			print("\n You Withdrew:", amount) 
		else: 
			print("\n Insufficient balance ") 

	def display(self): 
		print("\n Net Available Balance=",self.balance) 


s = Bank_Account() 
s.deposit() 
s.withdraw() 
s.display() 


start = 11
end = 25
for i in range(start,end+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)
