# pretty print
---
pprint stands for "pretty-print," and it's a module in Python's standard library that provides a way to print data structures in a more human-readable format. It's particularly useful when dealing with complex data structures like dictionaries or lists. Here's a quick guide on how to use pprint:
### 1. Import the pprint Module:
First, you need to import the pprint module.
```py
from pprint import pprint
```
### 2. Use pprint Function:
Once you've imported pprint, you can use the pprint() function to pretty-print your data.
```py
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'Example City',
    'skills': ['Python', 'JavaScript', 'SQL']
}

pprint(data)
```
This will print the dictionary data in a more structured and readable way.
### 3. Parameters of function:
- #### Depth (depth parameter):
  The depth parameter controls the maximum depth to which the data structure is printed. If the data structure has nested elements, you can limit how deep the printing goes.

  ```py
  from pprint import pprint

  data = {
    'name': 'John Doe',
    'details': {
        'age': 30,
        'city': 'Example City',
        'skills': ['Python', 'JavaScript', 'SQL']
    }
  }

  pprint(data, depth=1)
  ```
  In this example, only the top-level keys and values are printed, and the nested dictionary under the 'details' key is truncated.
- #### ndentation (indent parameter):
  The indent parameter controls the number of spaces used for each level of indentation in the pretty-printed output.

  ```py
  from pprint import pprint

  data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'Example City',
    'skills': ['Python', 'JavaScript', 'SQL']
  }

  pprint(data, indent=4)
  ```
  This example sets the indentation to 4 spaces per level.
- #### Line Width (width parameter):
  The width parameter controls the maximum number of characters per line in the output. If a line exceeds this width, it wraps to the next line.

  ```py
  from pprint import pprint

  data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'Example City',
    'skills': ['Python', 'JavaScript', 'SQL']
  }

  pprint(data, width=30)
  ```
  In this example, the output is limited to 30 characters per line.
- #### Compact Output (compact parameter):
  The compact parameter, when set to True, produces more compact output by putting multiple items on a single line.

  ```py
  from pprint import pprint

  data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'Example City',
    'skills': ['Python', 'JavaScript', 'SQL']
  }

  pprint(data, compact=True)
  ```
  This can be useful for saving space in the output.
- #### Sort Dictionaries (sort_dicts parameter):
  The sort_dicts parameter, when set to True, sorts dictionary keys in lexicographical order.

  ```py
  from pprint import pprint

  data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'Example City',
    'skills': ['Python', 'JavaScript', 'SQL']
  }

  pprint(data, sort_dicts=True)
  ```
  This produces output with dictionary keys sorted alphabetically.
- #### Underscore Numbers (_numalign and _numwidth parameters):
  The pprint module also provides parameters to control the alignment and width of numeric values.
  
  ```py
  from pprint import pprint

  data = {
    'count': 1000,
    'amount': 250000.75
  }

  pprint(data, _numalign='right', _numwidth=10)
  ```
  This example aligns numeric values to the right and sets the width for numeric values to 10 characters.

These parameters give you flexibility in customizing the output of pprint based on the specific requirements of your code and the structure of your data.  