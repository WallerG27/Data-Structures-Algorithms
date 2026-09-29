x = 5
print (x)
print()

x = "Hello World"                    #String
print (x)
print()

x = 20                                #int
print (x)
print()

x = 20.5                             #float
print (x)
print()

x = 1j                               #Complex number
print (x)
print()

x = ["apple", "banana", "cherry"]   #List is mutable
x[1] = "Grape"
print("Example to show mutability ", x)
y = [1, 'hello', 3.14, True]   # mixed data type
print("Example to mixed data type ", y)
print()

x = ("apple", "banana", "cherry")      #tuple is not mutable
print (x)
y = (1, "Hello", 3.14, True, [1, 2, 3])
print(y)
print()

x = range(6)                            #range
print (x)
print()

x = {"name" : "John", "age" : 36}       # dic
print (x)
print()

x = {"apple", "banana", "cherry"}       #Set, mutable
print (x)
print()

x = frozenset({"apple", "banana", "cherry"})        #int, immutable
print (x)
print()

x = True                             #boolean
print (x)
print()

x = b"Hello"                              #bytes
print (x)
print()

x = bytearray(5)                    #bytearray,bytes and bytearray are both data types used to represent sequences of bytes (integers ranging from 0 to 255).
print (x)
print()

x = memoryview(bytes(5))                #memoryview
print (x)
x = b'Hello, world!'
view = memoryview(x)
print (x)
print()

x = None                          #None, represents absence of a value
print (x)
print()

