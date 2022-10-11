numbers = [1, 3, 6, 8, 9, 45, 80]

objects = ['hello', 3, 4.5, True]


objects[2] 
#3

objects[3] 
#True

objects[4]
#Traceback (most recent call last):
 # File "<stdin>", line 1, in <module>
# IndexError: list index out of range


objects.append(False)
objects = ['hello', 3, 4.5, True, False]

objects.append(1)
objects = ['hello', 3, 4.5, True, False, 1]


objects.pop(1)
objects = ['hello', 4.5, True, False, 1]

for element in objects:
    print(element)

# hello
# 4.5
# True
# False

objects[::-1]
objects = [1, False, True, 4.5, 'hello']


objects[1:3]
objects = [False, True, 4.5]

