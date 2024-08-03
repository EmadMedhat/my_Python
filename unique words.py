#Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings.
mylist=['name1','name0','name2','name5','name5','name1','name2','name3','name4','name5']
i=0 
unique=mylist[:] #copy a list
while i<=len(unique)-1:
    first=unique[i]
    c=mylist.count(first)
    if c==1:   
        print ('this word is unique: ',first)  
        unique.remove(first)         
    elif c>=2:   
        print ('this word frequency of occurrence is: ',str(c),' and the word is: ', first)
        for x in range(c):
            unique.remove(first)
    i=0    
           
       
