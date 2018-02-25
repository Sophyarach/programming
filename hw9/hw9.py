import re

def askfilename():
    print("Введите название файла")
    name=input()
    try:
        file=open(name)
    except FileNotFoundError:
        print("Такого файла нет или введена пустая строка вместо названия")
        name=-1
    return name

def find_find(text):
    verb_forms=r'(?:найти|найд(?:у|(?:ё|е)(?:шь|т|м|те|нн(?:ы(?:й|м|е|х|ми)|о(?:го|му|м|й|е|ая|ую)))|я|ите|и)|наш(?:(?:ё|е)л|л(?:а|о|и)|едш(?:и|и(?:й|м|е|х|ми)|е(?:го|му|м|й|е)|ая|ую)))'
    return re.findall(verb_forms,text)

def print_find(text):
    res=find_find(text)
    if res:
        print(*set(res), sep=", ")
    else:
        print("В этом тексте нет форм глагола 'найти'")



name=askfilename()
if name!=-1:
    with open(name, encoding='utf-8') as f:
        text=f.read()
    text=text.lower()
    print_find(text)
