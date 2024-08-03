# Python function to print permutations of a given list
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = [] 
    for i in range(len(lst)):
        m=[lst[i]]
        remLst = lst[:i] + lst[i+1:]
        y=permutation(remLst)
        for j in y:
            l.append(m + j)
    return l
data = [0,1,2]
print (permutation(data))	
