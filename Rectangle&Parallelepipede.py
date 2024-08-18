class rectangle():
    def __init__(self,L,W):
        self.L=L
        self.W=W
    def Area(self):
        return self.L*self.W
    def Parameter(self):
        return (self.L+self.W)*2
    def display(self):
        print(f"LENGTH IS: {self.L}")
        print(f"WIDTH IS: {self.W}")
        print(f"AREA IS: {self.Area()}")
        print(f"Parameter IS: {self.Parameter()}")
class Parallelepipede(rectangle):
    def __init__(self, H,L,W):
        super().__init__(L,W)
#        rectangle.__init__(self,L,W)
        self.H=H
    def volume(self):
        return self.Area() * self.H
    def display(self):
        print(f"Height: {self.H}")
        print(f"Volume: {self.volume()}")
r1=rectangle(3,4)
r1.display()
r2=Parallelepipede(2,3,4)
r2.display()
