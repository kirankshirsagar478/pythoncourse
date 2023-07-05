#Function Declaration:
def withdraw():
    global pin
    pinck=int(input("Enter pin:"))
    if pin==pinck:
        
                while True:
                    global bal
                    wd=int(input("ENter Amount to Withdraw:"))
                    if wd<bal and wd>0:
                        #global bal
                        bal=bal-wd
                        print("Withdraw Successful")
                        print("Balance is:",bal)
                        break
                    else:
                        print("Amout is out of range")
    else:
        print("Incorrect pin")

def deposite():
    global bal
    dp=int(input("ENter Deposite Amout:"))
    bal=bal+dp
    print("Amount Deposit Successful")
    print("Balance is:",bal)
#########################################################
name=input("Enter Name:")
bal=int(input("Enter Balance:"))
while True:
    pin=int(input("Enter 4 digit Pin:"))
    pin1=int(input("Confirm Pin:"))
    if pin==pin1:
        print("Pin Created")
        break
    else:
        print("Wrong Pin!")
print("----------------------------")
print("-------------INFO-----------")
print("Name:"+name)
print("Balance:",bal)
while True:
    print("----------------------------")
    print("-------------MENU-----------")
    print("1.Withdraw \n2.Deposit \n3.Check Balance \n4.Exit")
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        withdraw()            
    elif ch==2:
         deposite()
            
    elif ch==3:
        print("Balance=",bal)
        
    elif ch==4:
        print("Thank You")
        break
    else:
        print("Invalid Input!!\n Please ENter Correct Input:")
        break
        


