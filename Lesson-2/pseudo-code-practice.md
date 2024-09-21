### a function that returns the sum of two numbers

- define a function with two numeric inputs
- within the function, add the numbers
- return the result of the addition

```python
START

DEFINE function(number1, number2)
    RETURN number1 + number2

END
```

#### a function that takes a list of strings, and returns a string that is all those strings concatenated together

- define a function with one input (list of strings)
- within the function, concatenate the list of strings into one string (no separator)
- return the single string

```python
START

DEFINE function(list of strings):
    new_string = join strings in list
    return new_string

END
```

#### a function that takes a list of integers, and returns a new list with every other element from the original list, starting with the first element. 

- define a function with one input (list of integers)
- within the function, iterate through every other element of the original list and add to a new list
- return the new list

```python
START

DEFINE function(list of integers):
    SET new_list = []
    SET index = 0
    FOR integer in list:
        IF index is even:
            append integer to new_list
        index += 1
    RETURN new_list

END
```

#### a function that determines the index of the 3rd occurrence of a given character in a string. For instance, if the given character is 'x' and the string is 'axbxcdxex', the function should return 6 (the index of the 3rd 'x'). If the given character does not occur at least 3 times, return None.

- define a function with two inputs: a string and a given character
- within the function, count the occurrences of the given character until 3 is reached
- retrieve the index of the 3rd instance of the character
- if 3 is never reached, return none

```python
START

DEFINE function(string, character):
    SET index = 0
    SET count = 0
    
    FOR x in string
        IF x == character:
            SET count += 1
        SET index += 1
        IF count == 3
            BREAK
    
    IF count == 3:
        RETURN index
```