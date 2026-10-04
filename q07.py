import random
class Temperature:
    def __init__(self,celcius):
        self.celcius=celcius

    def to_fahrenheit(self):
        return (self.celcius-32)*5/9
    def to_kelvin(self):
        return self.celcius+273.15
    def __repr__(self):
        return f"Temperature({random.randint(-40,60)})"

day_1 = Temperature(45)

print(repr(day_1))