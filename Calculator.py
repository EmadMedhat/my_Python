class calc():
    def __init__(self,n) -> None:
        self.n=n
    def Factorial(self,f="1st"):
        if f=="1st":
            f=self.n
        for i in range(1,self.n):
            f=(f)* i
        return f
    
    def sum(self,s="1st"):
        if s=="1st":
            s=self.n
        for i in range(1,self.n):
            s=s+i
        return s
    
    def testprim(self,p="1st"):
        if p=="1st":
            p=self.n
        if p <=2:
            return "not prime"
        for i in range (2,p):
            if p % i ==0:
             return "not prime"
        return "prime"
    
    def testprims(self,x):
        p=[x,self.n]
        p.sort()
        k=0
        o=[]
        for j in range(p[0]+1,p[1]):
            z=self.testprim(j)
            if z is "prime":
                o.append(j)
        return o        
    
    def tableMult(self,m="1st"):
        if m=="1st":
            m=self.n
        k=[]
        for i in range(11):
            k.append(m*i)
        return k
    
    def alltablesMult(self):
        o=[]
        for i in range(11):
            o.append(self.tableMult(i))
        return o
    
    def listDiv(self,d="1st"):
        if d=="1st":
            d=self.n
        o=[]
        for i in range(1,d+1):
            if d%i==0:
                o.append(i)    
        return o        

    def listDivPrim(self):
        k=[]
        o=self.listDiv()
        for i in range(len(o)):
            if self.testprim(o[i]) is "prime":
                k.append(o[i])
        return k
        
c1=calc(6)
print(c1.Factorial())    
print(c1.sum())  
print(c1.testprim())  
print(c1.testprims(15))  
print(c1.tableMult())
print(c1.alltablesMult())
print(c1.listDiv())
print(c1.listDivPrim())

