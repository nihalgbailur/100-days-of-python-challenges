# 2. List Element Access
# Given the list

# animals = ["cat", "dog", "mouse", "lion"]
# Write a loop to print each animal’s name and its position in the list (starting from 0), in the format:
# Index 0: cat
# Index 1: dog


# answers
animals = ["cat", "dog", "mouse", "lion"]
for i in range(len(animals)):
    print(f"Index {i}: {animals[i]}")


# advance pythonic way
# animals = ["cat", "dog", "mouse", "lion"]
# for idx, animal in enumerate(animals):
#     print(f"Index {idx}: {animal}")

