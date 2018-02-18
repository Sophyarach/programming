import random


def dict_from_file(filename):
    words = {}
    with open(filename, encoding='utf-8') as f:
        for line in f:
            if line == 'Word,Hint\n':
                continue
            line = str(line.strip())
            word, hint = line.split(',')
            words.setdefault(word, hint)
    return words


def dots(word):
    dots = ''
    for i in range(len(word)):
        dots += '.'
    return dots


def guessing_game(words):
    word = random.choice(list(words.keys()))
    print(words[word], dots(word))
    print('Input your guess: ')
    guess = str(input())
    if guess != word:
        return 'YOU LOST ;('
    elif guess == word:
        return'YOU WON ^-^'


print('Input filename:')
filename = input()
print(guessing_game(dict_from_file(filename)))



