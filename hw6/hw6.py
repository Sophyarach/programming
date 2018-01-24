import random
#Второй вариант. Только стихи немного ОСМЫСЛЕННЫ и очень жизненны

def random_word(file_name):
    with open(file_name,encoding="utf-8") as file:
        words=file.readlines()
        word = words[random.randint(0, len(words) - 1)]
        word=word.strip()
    return word

def verse1nouns():
    w1=random_word("verse1noun.txt")
    w2=random_word("verse1noun.txt")
    if w1==w2: #чтобы не было вариантов вроде "дурак дурак" в первой строчке. Ну и чуть-чуть повысить вероятность варианта "студент лингвист"
        if w2!="студент":
            w2="студент"
        else:
            w2="лингвист"
    return w1+" "+w2

def verse1end():
    if random.randint(0,1)==1:
        w1=random_word("verse1verb1.txt")
        w2=random_word("verse1object1.txt")
    else:
        w1=random_word("verse1verb2.txt")
        w2=random_word("verse1object2.txt")
    return w1+" "+w2

def verse1():
    return verse1nouns()+" "+verse1end()

def verse2end1():
    return random_word("verse2where.txt")+" "+random_word("verse2verb1.txt")
def verse2end2():
    return random_word("verse1object2.txt")+" "+random_word("verse2verb2.txt")

def verse2():
    n=random.randint(0,70)
    if n<=10: #на два слова заводить отдельный файл немного бессмысленно, да и сочетание "всерьез он ботать" на запчасти было влом разбирать
        w="всерьез он ботать" +" "+random_word("verse3verb1.txt") #в названии файла случайно verse3 и переименовывать неохота
    elif n<=40:
        w1="затем"
    else:
        w1="потом"
    if n>10:
        if n%2:
            w2=verse2end1()
        else:
            w2=verse2end2()
        w=w1+" "+w2
    return w

#у студента лентяя за час до дедлайна закончилась фантазия и последние две строчки генерируются совсем просто
def verse3():
    return random_word("verse3suffering.txt")+" "+random_word("verse3suffering.txt")+" "+random_word("verse3syllable.txt")+" "+random_word("verse3object.txt")

def verse4():
    return random_word("verse4onesyllable.txt")+" "+random_word("verse4noun.txt")+" "+random_word("verse4verb1.txt")+" "+random_word("verse4verb2.txt")

    
print(verse1())
print(verse2())
print(verse3())
print(verse4())
