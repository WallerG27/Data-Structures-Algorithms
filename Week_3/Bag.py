class Bag:
    def __init__(self):
        self.items = {}

    def add(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def remove(self, item):
        if item in self.items:
            self.items[item] -= 1
            if self.items[item] == 0:
                del self.items[item]

    def count(self, item):
        return self.items.get(item, 0)

    def __str__(self):
        return str(self.items)

my_bag = Bag()
my_bag.add("apple")
my_bag.add("banana")
my_bag.add("apple")

print(my_bag)
print(my_bag.count("apple"))
my_bag.remove("apple")
print(my_bag)