thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 1990,
  "colors": ["red", "white", "blue"]

}
print(thisdict)
print()
# create dictionary using { }
d1 = {1: 'I', 2: 'love', 3: 'computer science'}
print(d1)

# create dictionary using dict() constructor
d2 = dict(a = "I", b = "love", c = "computer science")
print(d2)

print()
d = { "name": "Alice", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(d["name"])

# Access using get()
print(d.get("name"))
print()

# Adding a new key-value pair
d["age"] = 22
print(d)
# Using del to remove an item
del d["age"]
print(d)

# Using pop() to remove an item and return the value
val = d.pop(1)
print(val)

print(d)
