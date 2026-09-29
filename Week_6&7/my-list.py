Values = [1,2,3,4,5]
print(Values)
print()
# Modifying an element
Values[2] = 10
print(Values)
print()
#append
Values.append(4)
print(Values)
print(Values.count(4))
Values.extend([6, 7])
print(Values)
# Insert 2 at index 1
Values.insert(1, 9)
print(Values)
print()
#Copy
Values = [1, 2, 3]
# Create a copy of the list
Values1 = Values.copy()
print(Values1)
print()

for val in Values:
    print(val, end=' ')

    a = ["This is a", "for", " Data Structure Class"]
    print(' '.join(a))





