""" def press_message():
    print('Special message: ')
    print('¡learning to use funcions in python!')


press_message()
press_message()
press_message()
 """


def talk(message):
    print('Hello')
    print('How you doing')
    print(message)
    print('bye')

option = int(input('Choose an option (1, 2, 3): '))
if option == 1:
    talk('You choose the option 1')
elif option == 2:
    talk('You choose the option 2')
elif option == 3:
    talk('You choose the option 3')   
else:
    print('Choose a valid option')