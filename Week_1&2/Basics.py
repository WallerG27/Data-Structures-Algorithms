name = 'Bob'
age = 25
print(name,age)
print ("my name is", name)

name: str = 'Sue'
age1: int = 'eight'
print(name,age1)

# constant
from typing import Final
VERSION: Final [str] = '1.0.12'
PI: Final [float] = 3.1415

# reusable code
from datetime import datetime

def show_date () -> None:
    print ('This is the current date:')
    print (datetime.now())

show_date()

def greet(name: str) -> None:
    print (f'Hello,{name}!')

greet ('Bob')
greet ('Sue')


def add(a: float, b:float) -> float:
    return a + b

print (add (1,2))