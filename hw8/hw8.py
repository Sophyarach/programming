import random

def create_dict(file_name):
    questions={}
    with open(file_name,encoding="utf-8") as file:
        for line in file:
            word,hint=str(line.strip()).split(",")
            questions.setdefault(hint,word)
    return(questions)

def random_line(file_name):
    with open(file_name,encoding="utf-8") as file:
        lines=file.readlines()
        randline=lines[random.randint(0, len(words)-1)]
    return randline

def question(questions):
    word=random.choice(list(questions.keys()))
    l=len(word)
    dothint=""
    for i in range (l):
        dothint+="."
    print(questions[word],dothint)
    print ("Ваш ответ:")
    answer=str(input())
    if answer!=word:
        return "Не угадали"
    else:
        return "Угадали!"

print("Введите имя файла:")
file_name=input()
d=create_dict(file_name)
print(question(d))

