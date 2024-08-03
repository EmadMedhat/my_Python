#Given an integer x, return true if x is a palindrome, and false otherwise.
x=100001
if x<0:
    print("False")
num=[int(i) for i in str(x)]  #n1n2 to [n1,n2]
num2=num[::-1]
print ("True") if num2==num else print("false")

#OR
#y=0
#for i in str(x):
#    num[y]=int(i)
#    y=y+1
#if num2==num:
#     print("true")
#else:
#    print("False")     
