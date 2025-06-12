courses = ["history", "ramayan", "mahabhrata"]
# indices:      0          1           2  
# negative:    -3         -2          -1  
print(courses[-3])  # “history”


# Negative indices count from the end. –1 is the last element,
# –2 the one before, and so on. Trying courses[-4] would be out of range,
#  since the list has only 3 items.



courses.append("veda")
# Adds "veda" as a new element at the end. Now courses is
# ["history", "ramayan", "mahabhrata", "veda"].

# Quick recap:

# Indexing: positive starts at 0; negative from -1 backwards.

# append(x): adds a single element x at the end.

# insert(i, x): places x at position i.

# extend(iterable): concatenates all elements from iterable onto your list
# (must pass something iterable).

