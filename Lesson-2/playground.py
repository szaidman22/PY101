strings = ['abc','def','ghi']

''.join(strings)


test_list = [1,2,3,4,5,00,2352,53,135]



def every_other(list):
    new_list = []
    index = 0
    for integer in list:
        print(index)
        if index % 2 == 0:
            new_list.append(integer)
        index += 1
    return new_list

every_other(test_list)

test_string = 'would you like to eat a banana'

def three_count(string, character):
    index = 0
    count = 0
    for x in string:
        if x == character:
            count += 1
        index += 1
        if count == 3:
            index -= 1
            break
    if count == 3:
        return index

three_count(test_string, 'x')


my_var = [1]

def my_func(my_var):
    my_var = [2]
    print(my_var)

my_func(my_var)
print(my_var) 