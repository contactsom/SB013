class Lab4:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40
        self.e = 50
        self.f = 60

    def data(self):
        print("Value of a : ",self.a)
        print("Value of b : ", self.b)
        print("Value of c : ", self.c)
        print("Value of d : ", self.d)
        print("Value of e : ", self.e)
        print("Value of f : ", self.f)

lab4=Lab4()
lab4.data()
print(lab4.__dict__)