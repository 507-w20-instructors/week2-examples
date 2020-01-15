
s1 = "hello"
s2 = s1.upper()
print(s1, s2)

def try_to_mutate(s, d):
    s2 = s # new local variable assigned to s
    s = "new string" # can't change s, can only reassign
    d2 = d # new local variable assigned to d
    d = {'key3': 'val3'} # d is now a key/val dict
    d2['key4'] = 'val4' # d2 now has 3 key/val pairs
    print('in func, s =', s)
    print('in func, s2 =', s2)
    print('in func, d =', d)
    print('in func, d2 =', d2)
    
gs = "old string"
gd = {'key1': 'val1', 'key2': 'val2'}
try_to_mutate(gs, gd)
print('in global, gs =', gs)
print('in global, gd =', gd)


my_list = [1, 2, 3, 4] # create a new list object and assign it to my_list
my_list.append(5) # add a new element, thus CHANGING the list object
print(my_list)


my_dict = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
my_dict['c'] = 'canteloupe'
print(my_dict['c'])



x = 5
y = x 
print(x) # prints 5
print(y) # prints 5
x = 6
print(x) # prints 6
print(y) # prints 5


s = "hello"
s2 = s 
print(s) # prints "hello"
print(s2) # prints "hello"
s = "world"
print(s) # prints "world"
print(s2) # prints "hello"

a = [1, 2, 3]
b = a
print(a) # prints "[1, 2, 3]"
print(b) # prints "[1, 2, 3]"
a = [4, 5, 6]
print(a) # prints "[4, 5, 6]"
print(b) # prints "[1, 2, 3]"


a = [1, 2, 3]
b = a
print(a) # prints "[1, 2, 3]"
print(b) # prints "[1, 2, 3]"
a.append(4)
b.append(5)
print(a) # prints "[1, 2, 3, 4, 5]"
print(b) # prints "[1, 2, 3, 4, 5]"
a = [4, 5, 6]
print(a) # prints "[4, 5, 6]"
print(b) # prints "[1, 2, 3, 4, 5]"


def change_it(the_list):
    the_list.append('d')

g_list = ['a', 'b', 'c']
change_it(the_list)
print(g_list)


def dict_update(local_dict):
    local_dict['g'] = 'grapefruit'
    local_dict['n'] = 'nectarine'

global_dict = {'g': 'grape', 'p': 'plum', 'o': 'orange'}
dict_update(global_dict)
print(global_dict['g'])
print(global_dict['n'])
print(global_dict['p'])




def list_remind(message, data):
    print('2', message, data[-1])
    message = 'don\'t forget!'
    data.append('eggs')
    print('3', message, data[-1])


groceries = ['milk', 'bread']
reminder = 'please pick up'
print('1', reminder, groceries[-1])
list_remind(reminder, groceries)
print('4', reminder, groceries[-1])
 
