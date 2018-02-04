def askfilename():
    print("Введите название файла")
    name=input()
    try:
        file=open(name)
    except FileNotFoundError:
        print("Такого файла нет или введена пустая строка вместо названия")
        name=-1
    return name

def nessfreq(name):
    freq ={}
    with open(name, "r", encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                if word.endswith("ness"):
                    if word in freq:
                        freq[word]+=1
                    else:
                        freq[word]=1
    return freq

def maxfreq(freq):
    maximum=max(freq.values())
    for word in freq:
        if freq[word]==maximum:
            print(word)

name=askfilename()
if name!=-1:
    freq=nessfreq(name)
    print("Различных слов с суффиксом -ness:", len(freq))
    print("Слова с наибольшей частотностью:")
    maxfreq(freq)
    
        
        
