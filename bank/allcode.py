from db_config import connect

def createAccount():
    name =input("enter your name= ")
    email=input("emterr your email")
    balance=float(input("enter your balance"))
    db=connect()
    cursor=db.cursor()
    sql= "insert into customer(name email,balance)values(%s,%s,%s)"
    values=(name,email,balance)
    cursor.execute(sql,values)
    db.commit()
    print("account create succesfully")
    db.close()


def viewAccount():
    db=connect()
    cursor=db.cursor()
    cursor.execute("select from customer")
    account=cursor.fetchall()
    print("all account")
    for acc in account :
         print(f"id:{customer[0]},name:{customer[1]},email:{customer[2]},balance:{customer[3]},")
    db.close()

def depositMoney():
    pass 
def withdrawMoney():
    pass
def checkBalance():
    pass
