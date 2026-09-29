class Car:
    def __init__(self, brand:str, power:int) -> None:
        self.brand = brand
        self.power = power

    def drive (self)-> None:
        print (f'{self.brand} is driving!')
    def get_info (self, var:int)-> None:
        print(var)
        print (f'{self.brand} with {self.power} power!')

Toyota: Car = Car('RAV4',150)
Toyota.drive()
Toyota.get_info(10)

print()

BMW: Car = Car('BMW',240)
BMW.drive()
BMW.get_info(20)

