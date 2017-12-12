task=input ("Номер задания? Введите 1, 2, или 3\n")
if task=="1":
    with open ("Extinct_languages.tsv" , encoding="utf-8") as f:
        for line in f:
            if len(line)>36:
                print(line)
elif task=="2":
    with open ("Extinct_languages.tsv" , encoding="utf-8") as f:
        n=0
        for line in f:
            sline=line.split("\t")
            if sline[2]=="Critically endangered\n":
                n=n+1
        print("Число языков со статусом Critically endangered:", n)
elif task=="3": #ищу точное совпадение с первой колонкой, вместе с пояснениями в скобках
    lang=input ("Название языка?\n")
    while lang!="":
        flag=0; #флаг того, что язык найден
        with open ("Extinct_languages.tsv" , encoding="utf-8") as f:
            for line in f:
                sline=line.split("\t")
                if sline[0]==lang:
                    print(sline[0]," - ",sline[1]," - ", sline[2])
                    flag=1
                    break
            if flag==0:
                print("Такого языка нет")
            lang=input ("Название языка?\n")
else:
    print("Вы ввели что-то не то")
