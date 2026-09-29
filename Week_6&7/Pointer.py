#Python doesn't have explicit pointers like C or C++. However, the concept of pointers is present in Python's object model.
#Variables in Python act as references to objects in memory. When you assign a variable to an object,
#you are essentially creating a pointer to that object.

x = 10  # x is a reference to an integer object with value 10
y = x   # y now also refers to the same object as x

print(x)  # Output: 10
print(y)  # Output: 10

y = 20  # y now refers to a new integer object with value 20
print(x)  # Output: 10 (x still refers to the original object)
print(y)  # Output: 20

print()

#When working with mutable objects like lists, the behavior is different
list1 = [1, 2, 3]
list2 = list1  # list2 now refers to the same list as list1

print(list1)  # Output: [1, 2, 3]
print(list2)  # Output: [1, 2, 3]

list2.append(4)  # Modifying the list through list2

print(list1)  # Output: [1, 2, 3, 4] (list1 is also modified)
print(list2)  # Output: [1, 2, 3, 4]

