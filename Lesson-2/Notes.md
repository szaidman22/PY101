## Errors

"Errors" and "exceptions" are used interchangeably. So is *throw* and *rasise*.

### Name Error

- when you attempt to use a variable or function that has not been defined.

### Type Error

- when a value of the wrong type is used in an expression.
    - using an argument for a function that is the wrong type
    - calling an object that isn't callable e.g. treating something that isn't a function as though it were a function with parentheses.

### Syntax Error

- when Python encounters code that doesn't meet the syntax rules. (typos)

### Value Error

- when a function gets an argument of the correct type, but the value isn't appropriate for the operation.

Example:

```python
number = int("abc")
# ValueError: invalid literal for int() with base 10: 'abc'
```

### Index Error

- when trying to access an index of a sequence that is outside the range of valid indexes.

### Key Error

- similar to index error, when trying to access a key that doesn't exist in a dictionary.

### Zero Division Error

- when trying to divide a number by 0, or using the modulus with 0 on the right side.

## Exception Handling

**try**, **except**, **else**, **finally** statements

1. **Try Block**: place the code that might raise an exception in the **try** block.

2. **Except Block**: if an exception is raised within the **try** block, Python looks for a matching **except** block for that error. If a match is found, the code in the corresponding except block runs.

3. **Else Block**: optional - executed only if no exceptions occurred in the **try** block. Should run when no errors are raised.

4. **Finally Block**: optional - always executed, regardless of whether an exception was raised. 

Example:

```Python
try:
    num_str = input("Enter a number: ")
    num = int(num_str)

    result = 10 / num
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result: {result}")
finally:
    print("Exception handling complete.")
```