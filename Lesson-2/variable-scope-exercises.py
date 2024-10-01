# Q1

num = 5

def my_func():
    print(num)

my_func()

# will print 5, because the num variable was initiated 
# with value 5 in the global scope, and it can be accessed in 
# the my_func() function's scope.

# Q2

num = 5

def my_func():
    num = 10

my_func()
print(num)

# will print 5. num is initialized to the number 5 in the global scope.
# within my_func(), a new variable num was initialized to 10.
# my_func() was called, but that does not impact the num variable
# in the global scope, so the global num variable remains 5.

# Q3

num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)

# num is initialized to 5 in the global scope. Within the my_func()
# function, the global variable num is reassigned to 10.
# my func is then called, which reassigns the global variable num
# to 10, so 10 is printed.

# Q4

def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

# 'Hello World'. The outer function has variable outer_var initated
# as "Hello" within it's scope. The inner function has variable
# inner_var initiated to "World" within it's scope. It also prints
# outer_var and inner_var. This is perfectly fine to do, because the
# inner function can access the outer function's outer_var variable.

# Q5

def my_func():
    num = 10

my_func()
print(num)

# this will output a name error (I think) because the variable
# num was only assigned within the local scope of my_func. 

#Q6

def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()

# will print "Inner 1: 25" then "Inner 2: 15".
# inner_func1 has a local x variable initialized as 25,
# while inner_func2 doesn't have a local x variable, so 
# it uses the non-local x variable initiated in my_func
# to 15.