numbers = [1, 2, 3, 4, 5]
# numbers
# [1, 2, 3, 4, 5]


# numbers.append('hello')
# numbers
# [1, 2, 3, 4, 5, 'hello']



# 'Hello' + ' ' + 'World'
# Hello World



numbers2 = [6, 7, 8, 9]
# numbers2
# [6, 7, 8, 9]

final_list = numbers + numbers2
# final_list
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# numbers * 5
# [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


my_tuple = (1, 2, 3, 4, 5)
# my_tuple
# (1, 2, 3, 4, 5)


# my_tuple.append(5)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: 'tuple' object has no attribute 'append'


# my_tuple.pop(2)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: 'tuple' object has no attribute 'pop'

for number in my_tuple:
    print(number)
# 1
# 2
# 3
# 4   
# 5