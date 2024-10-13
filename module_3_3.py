def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(5, 6, 7)
# print_params(1, 2, 3, 4) # ошибка
print_params(b = 25)
print_params(c = [1,2,3])


values_list = ['Hello', 25, False]
values_dict = {'a': 'Bye', 'b': 27, 'c': 1.5}
print_params(*values_list)
print_params(**values_dict)


values_list_2 = [99, 'Good']
print_params(*values_list_2, 42)