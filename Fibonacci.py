def Fibonacci_max(x):
    if x==1:
        return 0
    if x==2:
        return 1
    y=Fibonacci_max(x-1)+Fibonacci_max(x-2)
    return y
      
def Fibonacci(x):
    if x < 1:
        return "Incorrect input"
    #z=[0 for j in range(x)]  #initalize a list of x size
    z=[0]*x  #same but without for loop
    for i in range(x):
        z[i]=Fibonacci_max(i+1)
    return z

print(Fibonacci(7))