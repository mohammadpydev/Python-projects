# Random Module

The `random` module provides a variety of functions for generating random numbers and performing randomization tasks in Python.

## Importing the Module
To use the random module, you need to import it at the beginning of your Python script or program:
```py
import random
```

## Common Functions
1. ### random():
   `random.random()` returns a random float in the range [0.0, 1.0).

   Example:
   ```py
    import random

    num = random.random() # => 0.9387409377242042

    # To get random float number between 0 and 5 

    num2 = random.random()*5 # => 4.1644829712179785
   ```
2. ### randint():
   `random.randint(a, b)`  returns a random integer in the range [a, b], including both endpoints.

   Example:
    ```py
    import random
    rand_num = random.randint(1, 10)  
    # Returns a random integer between 1 and 10.
    ```
3. ### randrange():
 - `random.randrange(stop)`:
   returns a randomly selected element from the range range(stop).
 - `random.randrange(start, stop, step):`
   returns a randomly selected element from the range range(start, stop, step).

   Example:
   ```py
   import random
    rand_num = random.randrange(1, 10)  
    # Returns a random integer between 1 and 9.
   ```
4. ###  choice():
   `random.choice(seq)` returns a randomly selected element from the non-empty sequence seq.

   Example:
   ```py
    import random
    options = ["rock", "paper", "scissors"]
    choice = random.choice(options)  
    # Returns a random element from the list.
   ```
5. ###  shuffle():
   `random.shuffle(x)` shuffles the elements of a list x in place.

   Example:
   ```py
   import random
   my_list = [1, 2, 3, 4, 5]
   random.shuffle(my_list)  
   # Shuffles the list randomly.
   ```
6. ### sample():
   `random.sample(population, k)` returns a list of k unique elements randomly chosen from the population.

   Example:
   ```py
   import random
   deck = list(range(1, 53))  # Create a deck of cards
   hand = random.sample(deck, 5)  # Draw 5 random cards from the deck.
   ```  
## Random Module Limitations
The random module is not suitable for cryptographic purposes. For cryptographic security, you should use the secrets module.

This documentation provides an overview of the random module in Python. For detailed information and additional functions, you can refer to the official Python documentation.

> :bulb: **Official Python random module documentation**: https://docs.python.org/3/library/random.html


Please note that the random numbers generated using the random module are pseudorandom and are not truly random. They are generated based on an initial seed value and a deterministic algorithm.    