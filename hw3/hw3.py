#Вариант 2
print("Введите слово:")
word=input()
if word=="":
    print("Вы ввели пустую строку")
else:    
    for i in range(len(word)+1):
        print(word[0:i])
