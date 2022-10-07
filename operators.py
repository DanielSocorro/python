
is_student = True
is_student
True

work = False
work
False

is_student and work
False

is_student or work
True

not is_student
False

not work
True


number1 = 5
number2 = 5


number1 == number2
True 

number3 = 7


number1 == number3
False


number1 != number3
True


number1 >= number3
False


number1 >= number2
True

        # ---------------------------------------------------------------------------- #


name = input("¿What is your name?: ")
# ¿What is your name?: Dan
name
'Dan '

name.upper()
'DAN '

name.capitalize()
'Dan '

name = name.capitalize()
'Dan '

name = name.strip()
'Dan'

name = name.lower()
'dan'

name = name.replace('a', 'o')
'don'

name[0]
'd'

name[1]
'a'

name[2]
'n'

len(name)
3

# ------------------------------------------------------------------

name = "Christensen"
name[0]
'C'

name[1]
'h'

name[2]
'r'

name[0:4]
'Chri'

name[:4]
'Chri'

name[4:]
'stensen'

name[1:6]
'hrist'

name[1:9]
'hristens'

name[1:6:2]    # one to six two for two
'hit'

name[::]       # zero to the end one in one
'Christensen'

name[1::3]      # one to the end tree in tree
'hsnn'

name[::-1]      # from the end one by one less
'nesnetsirhC'