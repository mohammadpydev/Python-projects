# Regular Expression

![Python RegEx](regex.png)

A regular expression, often abbreviated as *`regex`* or *`regexp,`* is a powerful tool for text pattern matching and manipulation in Python. It's a sequence of characters that defines a search pattern. Regular expressions are widely used for tasks like text search, data validation, data extraction, and text manipulation.

In Python, you can work with regular expressions using the **`re module`**, which provides functions and classes for regular expression operations.

Here are some common operations you can perform with regular expressions in Python using the re module:

### 1.  Search for a pattern in a string:
   ```py
   import re

    text = "This is a sample text"
    pattern = r"sample"
    if re.search(pattern, text):
        print("Pattern found.")

   ```
### 2. Match patterns at the beginning of a string:

   ```py
   import re

    text = "Python is powerful"
    pattern = r"^Python"
    if re.match(pattern, text):
        print("Pattern matched at the beginning.")

   ```   
### 3. Find all occurrences of a pattern in a string:
   ```py
   import re

    text = "The quick brown fox and the brown dog."
    pattern = r"brown"
    matches = re.findall(pattern, text)
    print(matches)  # Output: ['brown', 'brown']

   ```   
### 4. Split a string using a pattern:
   ```py
   import re

    text = "apple,banana,orange"
    pattern = r","
    parts = re.split(pattern, text)
    print(parts) 
    # Output: ['apple', 'banana', 'orange']

   ```
### 5. Replace patterns in a string:
   ```py 
   import re

    text = "I like cats and dogs."
    pattern = r"cats"
    replacement = "horses"
    new_text = re.sub(pattern, replacement, text)
    print(new_text)  
    # Output: "I like horses and dogs."

   ```


> :bulb: **Tip:** If you want to learn more about Using special characters in patterns visit : [PCRE Regex Cheatsheet](https://www.debuggex.com/cheatsheet/regex/pcre)

> :bulb: **Tip:** If you want to test or know how it works[regex101](https://regex101.com/)

> :bulb: **Tip:** For more ideas and examples [Python RegEx](https://www.w3schools.com/python/python_regex.asp)



