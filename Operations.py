

# ==================== LIST OPERATIONS ====================
print("\n--- LIST OPERATIONS ---")
my_list = ["Wake up", "Eat breakfast", "Study Virtually", "Eat lunch", "Play Online Games"]

# Add 1 new item
my_list.append("Binge Watch")
print("After adding new task:", my_list)

# Remove 1 item (remove first occurrence)
my_list.remove("Eat lunch")
print("After removing one task:", my_list)

# Sort the list
my_list.sort()
print("After sorting the list:", my_list)

# ==================== TUPLE OPERATIONS ====================
print("\n--- TUPLE OPERATIONS ---")
my_tuple = ("apple", "avocado", "banana", "mango", "orange")

print("Original tuple:", my_tuple)

# Try modifying one element → This will cause an error
try:
    my_tuple[0] = "jackfruit"   # Tuples are immutable
except TypeError as e:
    print("Error when trying to modify tuple:", e)
    print("Explanation: Tuples are **immutable**. You cannot change, add, or remove elements after creation.")

# ==================== SET OPERATIONS ====================
print("\n--- SET OPERATIONS ---")
my_set = {7, 11, 13, 14, 21}

# Add a value
my_set.add(10)
print("After adding 10:", my_set)

# Remove a value
my_set.remove(7)
print("After removing 7:", my_set)

# Print the updated set
print("Final set:", my_set)

# Demonstrate no duplicates (sets automatically remove duplicates)
my_set.add(7)
print("After trying to add duplicate 7:", my_set)

# ==================== DICTIONARY OPERATIONS ====================
print("\n--- DICTIONARY OPERATIONS ---")
my_dict = {
    "name": "Wench",
    "age": 18,
    "course": "Information Technology"
}

# Add a new key "grade"
my_dict["grade"] = "A"
print("After adding 'grade':", my_dict)

# Update "age"
my_dict["age"] = 18
print("After updating age to 18:", my_dict)

# Print all keys
print("All keys:", list(my_dict.keys()))

# Print all keys and values
print("\nAll keys and values:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
