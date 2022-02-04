from Animals.Animal import Animal


class Cat(Animal):
    def __init__(self, name, age, type, point):
        super().__init__(type, name, age)
        self.point = point

    def makeSound(self):
        print("MEOOOOWW")

    def __str__(self):
        return "\nType : "+str(self.type)+\
               "\nName : "+str(self.name)+\
               "\nAge  : "+str(self.age)+\
               "Point: "+str(self.point)