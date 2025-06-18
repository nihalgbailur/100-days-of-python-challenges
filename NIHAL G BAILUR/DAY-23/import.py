'''import module '''
# This script imports the sys module and prints the list of directories 
# Python searches for modules.

import sys
import os

print(os.__doc__)
# print(sys.path)

'''
| Attribute     | Description                   |
| ------------- | -------------------------------- |
| `__name__`    | Module name when imported or run |
| `__doc__`     | Docstring of the module          |
| `__file__`    | Path to the module file          |
| `__package__` | Package the module belongs to    |'''


"""🧠 “Dunder Attribute” (short for Double Underscore Attribute)
More formally, it's known as a:

Special built-in module attribute

"""