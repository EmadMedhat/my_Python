#Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers
num=[2,1,2,3,4,5,6,9,7,8]
prod=num[:]
prod.sort()
print('the two numbers are:',prod[len(prod)-1],'&',prod[len(prod)-2],'and there product is ',prod[len(prod)-1]*prod[len(prod)-2])