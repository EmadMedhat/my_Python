#Write a function that will take a given string and reverse the order of words.
string="HELLO SAD WORLD"
s = string.split() #to split the string to list of the words between spaces
s=s[:: -1] #to reverse the list
x=" ".join(s) #to make the list a string of words and add a space between them
print(x)