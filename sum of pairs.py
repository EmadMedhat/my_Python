#Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

value=3
num=[2,0,1,2,3,4,5,6,8,77]
num.sort()
num1=num[:]
for i in range(len(num1)):
    num1.remove(num[i])    
    for ii in range(len(num1)):
        if num1[ii]<=value:
            x=num[i]+num1[ii]
            if x==value:
                print(num[i],num1[ii])
