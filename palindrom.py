def palindrom(word):
    word = word.replace(' ', '')
    word = word.lower()
    rev_word = word[::-1]
    if word == rev_word:
        return True
    else:
        return False

def run():
    word = input('Write a word: ')
    is_palindrom = palindrom(word)
    if is_palindrom == True:
        print('Is Palindrom! 🥳 🎉 🎊 🎁 🪅 🍾')
    else:
         print('Is not a Palindrom 😟 ')


if __name__ == '__main__':
    run()