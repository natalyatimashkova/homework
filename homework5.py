immutable_var = (1, 2, 3, True, 'String')
print(immutable_var)
immutable_var[1] = 5 #кортеж является неизменяемым (immutable) типом
print(immutable_var)
mutable_list = ['orange', 'pear', 'banana', 'kiwi']
print(mutable_list)
mutable_list[1:2] = 'cat', 'dog'
print(mutable_list)