from bank import *
p=1
y=0
x={}
while p!="0":
    p=input("to initiate an account enter 1, to make a deposit enter 2, to make a withdraw enter 3, to make a transfer enter 4,to show your balance enter 5, to exit enter 0 \n")
    match p:
        case "1":
            x[y]=input("please enter your name\n")
            x[y]=bank_acc(x[y],float(input("please enther the amount\n")))
            y=y+1
        case "2":
            z=input("please enter your name\n")
            for i in range(len(x)):
                if z==x[i].name:
                    break
            x[i].deposit(float(input("please enter the amount you want to deposit\n")))
        case "3":
            z=input("please enter your name\n")
            for ii in range(len(x)):
                if z==x[ii].name:
                    break
            x[ii].withdraw(float(input("please enter the amount you want to withdraw\n")))
        case "4":
            z=input("please enter your name\n")
            for iii in range(len(x)):
                if z==x[iii].name:
                    break
            o=input("please enter the account name you want to tranfer to\n")
            for iiii in range(len(x)):
                if o==x[iiii].name:
                    break
            x[iii].transfer(x[iiii],float(input("please enter the amount you want to withdraw")))           
        case "5":
            z=input("please enter your name\n")
            for j in range(len(x)):
                if z==x[j].name:
                    break
            x[j].get_balance()
