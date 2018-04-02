#в папке с программой файлы с городами с часовым поясом с плюсом (например, Питер), с минусом (Алофи), с двузначным числом (Алофи), с нецелым поясом (Тегеран), с переходом на летнее (Копенгаген)
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

def find_time(name):
    with open(name,'r',encoding="utf-8") as file:
        found=False
        time=-1
        for line in file:
            if found:
                time = re.findall('title="UTC([\−\+][0-9\.]+)">',line)
                break
            if 'Часовой пояс' in line:
                found=True
        return time

def find_cityname(name):
    with open(name,'r',encoding="utf-8") as file:
        found=False
        cityname=-1
        for line in file:
            cityname=re.findall('>([А-ЯЁа-яё\(\) \-\.]+) +— Википедия<',line)
            if cityname:
                break
    return cityname

def print_time(text):
    time=find_time(text)
    if time:
        n=len(time)
        if n==1:
            print('UTC',time[0])
        if n==2:
            print('UTC',time[0],', летом UTC', time[1], sep='')
    else:
        print('Информации о часовом поясе не нашлось')

def save_result(text):
    cityname=find_cityname(text)
    time=find_time(text)
    timeresult=''
    if time!=-1:
        n=len(time)
        if n==1:
            timeresult='UTC'+time[0]
        else:
            timeresult='UTC'+time[0]+', летом UTC'+time[1]
    else:
        timeresult='Информации не нашлось'
    fout=open('timeinfo.txt','w',encoding='utf-8')
    if cityname:
        fout.write('Часовой пояс города '+cityname[0]+': '+timeresult)
    else:
        fout.write('Неправильный входной файл')
    fout.close()

name=askfilename()
if name!=-1:
    with open(name, encoding='utf-8') as f:
        text=f.read()
    find_cityname(name)
    save_result(name)
