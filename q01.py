class Dog:
    def __init__(self,name:str,age:float):
        self.name=name
        self.age=age

    def bark(self):
        print(f"{self.name} says Woof!")

tomy=Dog("Tomy",8)
tomy.bark()
sheero=Dog("Sheero",2)
sheero.bark()