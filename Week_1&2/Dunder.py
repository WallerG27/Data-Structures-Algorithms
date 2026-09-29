from typing import Self


class Car:
    def __init__(self, brand:str, power:int) -> None:
        self.brand = brand
        self.power = power

    def __str__(self) ->str:
        return f'{self.brand},{self.power}hp'

    def __add__(self,other:Self) -> str:
        return f'{self.brand} and {other.brand}'

Toyota: Car = Car('RAV4',150)
BMW: Car = Car('BMW',240)

print(Toyota +BMW)
