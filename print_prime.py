def print_prime():
    i=1
    while i!=0:
        n=int(input("please enter your number "))
        if n==1 | n==2:
            print("your number is not prime")
        for i in range(2,n):
            if n%i==0:
                print("your number is not prime")
                break
            else:
                if i==n-1:
                    print("your number is prime")
        x=input("write 0, if you want to exit the program ")
        if x=="0":
            i=0
            
print_prime()
