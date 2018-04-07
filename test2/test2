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

def count_se(name):
    with open(name, 'r', encoding="utf-8") as file:
        n=0
        found=False
        for line in file:
            if found:
                if "</se>" in line:
                    break
                n+=1
            if "<se>" in line:
                found=True
        fout=open('linecount.txt','w',encoding='utf-8')
        fout.write(str(n))
        fout.close()
    return n

def dict_create(name):
    dict={}
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            if "<w>" in line:
                morf=re.findall('gr="(.*)"',line)
                if morf[0] in dict:
                    dict[morf[0]]+=1
                else:
                    dict[morf[0]]=1
    fout=open('dict.txt','w',encoding='utf-8')
    for key in dict:
        fout.write(key)
        fout.write(",")
        fout.write(str(dict[key]))
        fout.write("\n")
    fout.close()
    return dict

def find_fem_a(name):
    res=""
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            if '"A=' in line:
                if ",жен" in line:
                    word=re.findall('>([А-Яа-яЁё]+)<',line)
                    res+=word[0]+", "
        fout=open('femaadj.txt','w',encoding='utf-8')
        fout.write(res)
        fout.close()
    return res

def clear_tags(name):
    with open(name, 'r',encoding='utf-8') as file:
        fout=open('result.csv','w',encoding='utf-8')
        for line in file:
            if "<w>" in line:
                lex=re.findall('lex="([А-Яа-яЁё]+)"',line)
                morf=re.findall('gr="(.*)"',line)
                word=re.findall('>([А-Яа-яЁё]+)<',line)
                newline=lex[0]+","+morf[0]+","+word[0]+"\n"
                fout.write(newline)
        fout.close()

name=askfilename()
if name!=-1:
    print("Результат первого задания в файле linecount.txt, второго в dict.txt третьего в femaagj.txt, третьего в result.csv")
    count_se(name)
    dict_create(name)
    find_fem_a(name)
    clear_tags(name)
