""" counter = 0
print('2 elevates to ' + str(counter) + ' is equal to: ' + str(2**counter))

counter = 1
print('2 elevates to ' + str(counter) + ' is equal to: ' + str(2**counter))

counter = 2
print('2 elevates to ' + str(counter) + ' is equal to: ' + str(2**counter)) """


def run():
    LIMIT = 1000000

    counter = 0
    exponential_2 = 2**counter
    while exponential_2 < LIMIT:
        print('2 elevates to ' + str(counter) + ' is equal to: ' +  str(exponential_2))
        counter = counter + 1
        exponential_2 = 2**counter

if __name__ == '__main__':
    run()


    