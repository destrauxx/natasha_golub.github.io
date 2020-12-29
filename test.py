# my_list = []

# my_list = list()

# my_list = ['apple', 'orange', 'banana', 'syr_kosichka']

# fruit = 'apple' in my_list
# print(fruit)

# # Свойства
# len(my_list)

# # Методы
# my_list.reverse()
# print(my_list)

# sorted_list = sorted(my_list)

# my_list.sort(key=lambda x: x[-1]) # Можно задать ключ для сортировки
# print(my_list)

# my_list.append('Pumpkin pie')
# my_list.insert(900, 'Watermelon')

# my_list.remove('apple')

# my_list.pop(0)

# my_list.clear()

# new_list = [0]*5
# print(new_list)

# comp_list = [i for i in range(5)]
# print(comp_list)

# double_list = [i * 2 for i in range(5)]
# print(double_list)


# # Кортежи

# my_tuple = 'apple', 'banana', 'orange'

# my_tuple = ('apple', 'banana', 'orange')

# my_tuple = tuple('apple')

# my_tuple.count('p')

# my_tuple.index('p')


# my_tuple = 'Syr_kosichka', 'Minecraft', 'Professor'
# name, city, proffesion = my_tuple
# print(name)
# print(city)
# print(proffesion)

# my_tuple = (1, 2, 3, 4, 5, 6, 7)
# first, *rest, last = my_tuple
# print(first)
# print(rest)
# print(last)

# *any_first, prev, last = my_tuple
# print(any_first)
# print(prev)
# print(last)


# foo = 'abcd'
# f, *m, l = foo
# print(f, m, l)


# bar = {'first_key' : 1, 'second_key': 2}
# f, l = bar
# print(f, l)

# my_dict = {'key_1': 1, 'key_2': 2}

# my_dict = dict(key_1=1, key_2=2)

# value = my_dict['key_1']

# my_dict['new_key'] = 3

# del my_dict['key_1']

# removed_value = my_dict.pop('key_2')

# last_value = my_dict.popitem()

# my_dict = {'key_1': 1, 'key_2': 2}

# for k in my_dict.keys():
#     print(k)
# for v in my_dict.values():
#     print(v)
# for k, v in my_dict.items():
#     print(k, v)

# my_list = [1, 2, 3]
# other_list = my_list 
# other_list[0] = 4
# print(my_list[0])


# my_dict = {'key_1': 1, 'key_2': 2}

# other_dict = my_dict
# other_dict['key_1'] = 4

# print(my_dict['key_1'])

# my_list  = [1, 2, 3]
# other_list = my_list.copy()
# other_list = list(my_list)

# other_list[0] = 4
# print(my_list[0])


# my_dict = {'key_1': 1, 'key_2': 2}
# other_dict = my_dict.copy()
# other_dict = dict(my_dict)

# other_dict['key_1'] = 4
# print(my_dict['key_1'])


# my_set = {1, 2, 3, 4}
# my_set = set([1, 2, 3, 4])

# my_set = {1, 1, 2, 2}
# print(my_set)

# unique = set('syr kosichka')
# print(unique)
# my_set = {1, 2}

# my_set.add(3)
# print(my_set)

# my_set = {1, 2, 3, 4}

# my_set.remove(3)
# print(my_set)

# my_set.discard(3)
# my_set.discard(2)
# print(my_set)

# removed_data = my_set.pop()
# print(removed_data)

# my_set.clear()
# print(my_set)

# my_set = {1, 2, 3}
# for i in my_set:
#     print(i)


# evens = {2, 8, 10}
# odds = {1, 3, 7}
# primes = {2, 3, 5}

# union = evens.union(odds)
# print(union)

# intersection = evens.intersection(primes)
# print(intersection)


# my_string = 'qu'
# my_string = 'Hello \'world\' \\'
# print(my_string)

# my_string = '        Hello, world!     '
# no_spaces = my_string.strip()
# print(no_spaces)

# to_list = my_string.split()
# print(to_list)

# upper = my_string.upper()
# lower = my_string.lower()

# first_string = 'hi, world'
# second_string = 'Display beautiful'

# collection = [first_string, second_string]

# for s in collection:
#     print(s.rjust(20, '#'))

# some_string = 'Im string'
# some_number = 14
# my_string = f'String data: {some_string} -- Number data: {some_number}'
# print(my_string)

# some_float = 24.1244
# my_string = f'String data: {some_string} -- Number data: {some_float:.2f}'
# print(my_string)

# some_data = [('banana', 5), ('potato', 2), ('tomato', 15)]

# for veg, price in some_data:
#     print(f'name: {veg:<10} price: {price:03d} $')

# from datetime import datetime
# today = "Today's date is {:%Y-%m-%d %H:%M}".format(datetime.now())
# print(today)

# my_string = 'h, worlllld'

# my_string.startswith('hi')
# my_string.endswith('world')

# print(my_string.find('i'))
# print(my_string.count('l'))

# replaced = my_string.replace('hi', 'bye')
# print(replaced)

# some_iterable = ['a','b','c']
# my_string = ''.join(some_iterable)
# print(my_string)

# my_lambda = lambda x, y: x+y

# print(my_lambda(5, 2))

# unsorted_list = [(10, -1), (5, 12), (-5, 2)]

# sorted_list = sorted(unsorted_list, key=lambda x: x[0])
# sorted_list = sorted(unsorted_list, key=lambda x: x[1])

# my_string = '12345'

# to_list_of_ints = list(map(lambda x: int(x), my_string))
# print(to_list_of_ints)

# my_list = [1, 2, 5, 4, '6']
# convert_list = list(map(lambda x: int(x), my_list))
# print(convert_list)

# filter_list = list(filter(lambda x: type(x) is str, my_list))
# print(filter_list)

# from functools import reduce
# my_list = [1, 2, 3, 4, 5]

# reduced_list = reduce(lambda x, y: x + y, my_list)
# print(reduced_list)


# list_to_string = ['g', 'a', 'b', 'e', 'l', 'l', 'a']
# reduced = reduce(lambda x, y: x + y, list_to_string)
# print(reduced)

# only_evens = [i ** 2 for i in range(10) if i ** 2 % 2 == 0]
# print(only_evens)

# some_value = False
# my_ternary = 10 if some_value else 20

# print(my_ternary)

# only_chet = [i for i in range(100) if i ** 3 % 3 == 0]
# print(only_chet)


# def my_func(a):
#     print(a)
# my_func('hello')

# def my_func(a, b, *args, **kwargs):
#     print(a, b)
#     print(args)
#     print(kwargs)

# my_func(1, 2, 3, 4, 5, foo=6, bar=7)

# def my_func(a, b, c):
#     print(a, b, c)

# some_dict = {'a': 1, 'b': 2, 'c': 3}
# my_func(**some_dict)

# def decorator(func):
#     def wrapper():
#         print('before')
#         func()
#         print('After')
#     return wrapper

# def print_name():
#     print('Mike')

# print_name()

# @decorator
# def print_name():
#     print('Mike')

# print_name()

# def square_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result*result
#     return wrapper

# @square_decorator
# def add_some(x):
#     return x+5

# print(add_some(10))

# def repeater(times):
#     def decorator_repeat(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat

# @repeater(times=3)
# def say_hello():
#     print('Hello, world')

# say_hello()

# def e_f(argument, user):
#     return argument + 10 if user else argument - 10

# user = 'admin'
# print(e_f(10, user))

# def check_permission(func):
#     def wrapper(*args, **kwargs):
#         arguments = args[0]
#         user = args[1]
#         if user == 'admin':
#             return func(arguments, user)
#         else:
#             return 'Denied'
#     return wrapper

# @check_permission
# def e_f(argument, user):
#     return argument + 10 if user else argument - 10

# user = 'admin'
# print(e_f(15, user))

# num = 0
# def counter(func):
#     def wrapper(*args, **kwargs):
#         global num
#         func()
#         num += 1
#         print(f'Было выполненно раз: {num}')
#     return wrapper


# @counter
# def some_func():
#     print('Hello')

# some_func()
# some_func()
# some_func()

# from collections import Counter

# my_string = 'aaaabbccccdddd'

# my_counter = Counter(my_string)
# print(my_counter)

# print(dir(my_counter))
# print(my_counter.most_common(1))
# print(my_counter.elements())


# from collections import namedtuple
# Some_class = namedtuple('Name', 'a, b')
# foo = Some_class(1, 2)

# print(foo)
# print(foo.a, foo.b)

# def my_gen():
#     yield 1
#     yield 2
#     yield 3

# gen = my_gen()

# first_call = next(gen)
# print(first_call)
# sec_call = next(gen)
# print(sec_call)
# th_call = next(gen)
# print(th_call)

# def timer(n):
#     print('Starting')
#     while n > 0:
#         yield n
#         n -= 1

# countdown = timer(3)
# print(next(countdown))

# import json

# my_dict = {'class': 'Mage', 'level': 5, 'items': ['sword', 'potion']}

# with open('c_d.json', 'w') as f:
#     json.dump(my_dict, f, indent=4)


# my_list = [1, 2, 3, 4, 5]

# if (n := len(my_list)) < 10:
#     print(f'l i t s ({n} e e >= 10)')



from datetime import datetime
def logger(func):
    def wrapper(*args, **kwargs):
        today = "Date and time: {:%Y-%m-%d %H:%M}".format(datetime.now())
        result = func(*args, **kwargs)
        with open('./python_is_cool.txt', 'w') as f:
            f.write(today)
            f.write(func.__name__)
            f.write(*args)
            f.write(result)
        return result
    return wrapper

@logger
def add_one(*num):
    return sum(num) + 1

@logger
def another_func(x, y, z):
    return x * y + z

add_one(2, 4, 5)
another_func(1, 2, 3)