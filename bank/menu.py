#from allcode import *

def menu(self):
       while True: 
        print("\n welcome to our banking system")
        print("1. create account")
        print("2.view account")
        print("3.deposit money")
        print("4.withdraw money")
        print("5.check balance ") 
        print("6.exit")       

choice=int(input("enter your choice"))
if choice=="1":
    createAccount()
elif choice=="2":
    viewAccount()
elif choice=="3":
    depositMoney()
elif choice =="4" : 
    withdrawMoney()
elif choice == "5":
    checkBalance()
elif choice=="6":
    print("exit")
else :
    print ("enter vaild input")
    
    


    

