print('введите название файла')
name=input()
#захотелось усложнить себе жизнь немного, надеюсь я правильно использую исключения
try:
    file=open(name)
except FileNotFoundError:
    print('Такого файла нет или введена пустая строка вместо названия')
else:
    max=0
    min=float('inf')
    with open(name, encoding='utf-8') as f:
        for line in f:
            if len(line)-1<min:
                min=len(line)-1
            if len(line)-1>max:
                max=len(line)-1
    if min==0:
        print('В файле есть строки длины 0 (пустые)')
    else:
        print(max/min)
