import re

#от слова "викинг" нет прилагательных и прочих производных, не знаю, почему нельзя обойтись простым реплейсом, но пусть будет саб
def hordes_of_angry_chipmunks_invading_wikipedia(text):
    text=re.sub('(викинг)','бурундук', text)
    text=re.sub('(Викинг)','Бурундук', text)
    text.replace('Ви́кинги','Бурундуки́')
    return text

def askfilename():
    print("Введите название файла")
    name=input()
    try:
        file=open(name)
    except FileNotFoundError:
        print("Такого файла нет или введена пустая строка вместо названия")
        name=-1
    return name

def now_with_pictures(text):
    index=text.find('<div class="thumb tright">')
    text= text[:index] +'<img src="https://c2.staticflickr.com/4/3262/3219859456_4ba908c46b_z.jpg?zz=1" style="float:right;width:212px;height:209px;">'+text[index:]
    index=text.find('</div>Датчане вторгаются в Англию.')
    text= text[:index] +'<img src="https://i.pinimg.com/originals/8a/38/74/8a38741e2489b5a78654fd48e91f44f4.jpg" style="float:left;width:212px;height:209px;">'+text[index:]
    index=text.find('</div>Макеты')
    text= text[:index] +'<img src="https://files.5funfacts.com/images/402660/17244560-Q2GKGkC-1511430097-650-09e500a13c-1511526140.jpg" style="float:right;width:212px;height:209px;">'+text[index:]
    return text
#через замену сложно. У вики очень сложный код для вставки картинок. Поэтому просто вставляю примерно там где были картинки в оригинале  

name=askfilename()
if name!=-1:
    with open(name, encoding='utf-8') as f:
        text=f.read()
    with open('result.html','w', encoding='utf') as f:
        text=hordes_of_angry_chipmunks_invading_wikipedia(text)
        print('Пссс... Хочешь картинок с викингами-бурундуками? Введи "да" если хочешь, если нет то пиши что угодно.')
        ask=input()
        if ask=='да':
            text=now_with_pictures(text)
        f.write(text)
        print('Результат программы в файле result.html')
