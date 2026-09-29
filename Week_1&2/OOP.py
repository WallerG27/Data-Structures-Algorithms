
class Car:
    def __init__(self, color:str, power:int) -> None:
        self.color = color
        self.power = power

Toyota: Car = Car('White',200)
print (Toyota.color)
print (Toyota.power)

BMW: Car = Car ('Blue', 250)
print (BMW.color)
print (BMW.power)


