num=[2,1,2,3,4,5,6,9,7]
prod=num[:]
prod_max=num[:]
for i in range(len(num)):
    current=num[i]
    for ii in range(len(num)):
        if i!=ii:
            prod[ii]=num[i]*num[ii]
            prod_max[i]=max(prod)
            
            
print('max product is ',max(prod_max))