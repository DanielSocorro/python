import random

def pass_generate():
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
    'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
     'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
    'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p',
     'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', 
    '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    char = uppercase + lowercase + numbers + symbols

    password = []

    for i in range(15):
        random_char = random.choice(char)
        password.append(random_char)

    password = "".join(password)
    return password

def run():
    password = pass_generate()
    print('you new password is: ' + password)    # type: ignore



if __name__ == '__main__':
    run()


    # you new password is: MSkE*4-lJ#c][Cx
    # you new password is: 75gsffkvh}eAgñd