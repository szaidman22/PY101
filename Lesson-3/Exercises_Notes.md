## To study/remember:

#### Search for a string:

```python
'xyz' in 'abscdefsaxyzfs'
'xyz' in variable_name
```

### endswith and startswith

use these methods to check if the start or end of a string contains a substring.

### capitalize()

string method for sentence capitalization.

### basically just study all the built in string methods.

### List method extend() 

Rather than append() only letting you add one item, extend() lets you add an iterable with multiple items.

### review indexing rules

### review range rules 

i.e. range(1,11) is numbers 1-10

### when checking if an entry (key) is in a dictionary:

you don't have to do 'blank' is in dictionary.keys()

you can just do 'blank' is in dicitionary (simply using the name of the dictionary searches the keys.)

### to add new records to a dictionary

dicitonary.update(another dicitonary with new records)

### while variable_name:

handy thing to know is that you can have a while loop that just looks like this, for example:

```python
numbers = [1,2,3]

while numbers:
    numbers.pop()
```

The "while numbers" is checking for numbers being truthy or falsy. 

### shallow vs. deep copies

- for good explanation, see Practice Problems: Easy 3 question 4

### use the math.isclose() function for comparing floats

### Q7 in medium problems 1

- pass by reference / shallow/deep copies

### augmented assignment

e.g. +=, can be used to assign a new variable, reassign a variable or mutate an existing

### interning

- when python reuses a memory address for certain immutable objects like integers and short strings with the same value.

### review solution to hard problems question 2

- slicing will result in the creation of a copy rather than a reference to the same object

### when asked what a function does

- always mention its output, what it returns, local and non-local variables that it uses.

### describing the implementation of code / a function

- it's not always necessary to describe the implementation i.e. how the code/function works so much as what it does (the user-level description). Pay attention to whether in written assessments launch school asks for the implementation description vs. user-level description. 

### Variables

all of the following are considered variables:

- Variables and constants
- Function names
- Function parameters

"Note in particular that dictionary key names are not variables, nor are the elements of a collection."