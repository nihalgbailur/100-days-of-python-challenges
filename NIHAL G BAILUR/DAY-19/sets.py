# un ordered collection
# adding or removing only u can do in sets
# Python displays the elements in arbitrary order—not the order you added them, and not sorted order.
x=set()
s={4,32,536,5}
s.add(10)
print(s)

# Absolutely! Here’s a **structured set of notes** summarizing only the *doubts you asked about sets, lists, and related topics* in Python, each with clear explanations, examples, and takeaway points.

# ---

# # 📝 Python: Doubts & Clarifications (Sets, Lists, and Related)

# ---

# ## 1. **Why does set print elements in “random” order?**

# * **Sets are unordered collections**; their elements are stored based on hash values, not insertion order.
# * When you `print(s)`, the order of elements is unpredictable and may appear “random” (especially before Python 3.7, but do not rely on order even in newer versions).
# * **If you need order**, use a list or print a sorted set: `print(sorted(s))`.

# ---

# ## 2. **Lists: Ordered, Allow Duplicates, Unhashable Elements Example**

# * **Lists** preserve insertion order, allow duplicate values, and can contain unhashable types (like other lists or dicts).
# * **Example:**

#   ```python
#   my_list = [1, 2, [3, 4], {'a': 5}, 2, [3, 4]]
#   print(my_list)
#   # Output: [1, 2, [3, 4], {'a': 5}, 2, [3, 4]]
#   ```
# * **Sets**, in contrast, cannot contain unhashable types.

# ---

# ## 3. **Can a set contain a list? Why or why not?**

# * **No, sets cannot contain lists.**
# * **Reason:**
#   Sets require elements to be hashable (immutable with a stable hash value).
#   Lists are mutable and unhashable, so adding them to a set raises a `TypeError`.
# * **Example:**

#   ```python
#   s = set()
#   s.add([1, 2, 3])  # Raises: TypeError: unhashable type: 'list'
#   ```

# ---

# ## 4. **Why can’t you add using `set.addd()`?**

# * The method name is **`add()`**, not `addd()`.
# * Using a typo like `set.addd()` will cause an `AttributeError`:

#   ```
#   AttributeError: 'set' object has no attribute 'addd'
#   ```
# * **Tip:** Always check Python method names for exact spelling.

# ---

# ## 5. **`set.add(x)` vs `s.add([1, 2, 3])`**

# * **`set.add(x)`** adds a hashable element `x` to the set.

#   * Works for types like `int`, `str`, `tuple` (of hashables).
# * **`s.add([1, 2, 3])`** tries to add a list (which is unhashable), causing a `TypeError`.

#   * **Key rule:** Only hashable (immutable) objects can be added to sets.

# ---

# ## 6. **Interview Questions on Sets**

# * **What is a set?**
#   Unordered, mutable collection of unique, hashable elements.
# * **Difference between `remove()` and `discard()`?**
#   `remove()` raises an error if element missing, `discard()` does nothing.
# * **Can a set contain a list?**
#   No; lists are unhashable.
# * **What is a `frozenset`?**
#   An immutable set; can be a set element or dictionary key.
# * **How do you remove duplicates from a list while preserving order?**

#   ```python
#   list(dict.fromkeys(mylist))
#   ```

# ---

# ## 7. **Hashable vs. Unhashable Types (Key Table)**

# | Type        | Hashable? | Can be set element? |
# | ----------- | --------- | ------------------- |
# | `int`       | Yes       | ✅                   |
# | `str`       | Yes       | ✅                   |
# | `tuple`     | Yes\*     | ✅                   |
# | `list`      | No        | ❌                   |
# | `dict`      | No        | ❌                   |
# | `frozenset` | Yes       | ✅                   |

# \*`tuple` must contain only hashable types.

# ---

# ## 8. **Aphorisms for Clarity**

# * **On sets:**

#   > “If it can change, it can’t be in a set.”
# * **On method names:**

#   > “Spelling matters; Python methods are case- and spelling-sensitive.”

# ---

# **Would you like to add diagrams, more interview Q\&A, or expand these notes into a printable cheatsheet?**
