def print_evenOrodd():
    i=1 
    while i!=0:
        n=input("please input your number ")
        if int(n)%2==0:
            print("your number is even")
        else:
            print("your number is odd")    
        x=input("write 0, if you want to exit the program ")
        if x=="0":
            i=0

print_evenOrodd() 