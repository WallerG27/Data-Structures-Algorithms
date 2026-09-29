class SimpleHashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)] # List of lists (buckets)

    def hash_function(self, key):
        """Simple hash function using Python's built-in hash() and modulo."""
        return hash(key) % self.size

    def put(self, key, value):
        """Inserts or updates a key-value pair."""
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value) # Update existing key
                return
        bucket.append((key, value)) # Add new key-value pair

    def get(self, key):
        """Retrieves a value by key."""
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None # Key not found

    def remove(self, key):
        """Removes a key-value pair."""
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

# Example usage of the custom hashmap:
my_map = SimpleHashMap(size=10)
my_map.put("name", "Alice")
my_map.put("age", 30)

print(f"Name: {my_map.get('name')}")
print(f"Age: {my_map.get('age')}")

my_map.remove("age")
print(f"Age after removal: {my_map.get('age')}") # Output: None