import re
from string import punctuation

def askfilename():
    print("Введите название файла")
    name=input()
    try:
        file=open(name)
    except FileNotFoundError:
        print("Такого файла нет или введена пустая строка вместо названия")
        name=-1
    return name

def get_sentences(filename):
    with open(filename,encoding='utf-8') as f:
        text=f.read()
    sentences=re.split('[.!?]',text)
    del_punct=[sentence.replace(a,'') for a in punctuation for sentence in sentences]
    return del_punct

def print_capitalized_from_long_sentences(sentences):
    words=[sentence.split() for sentence in sentences]
    for sentence in range(len(sentences)):
        if len(words[sentence])>10:
            for word in words[sentence]:
                if word[0].isupper():
                    print(word)

name=askfilename()
if name!=-1:
    sentences=get_sentences(name)
    print_capitalized_from_long_sentences(sentences)
