word=input("Введите слово: ")
i=0
for letter in word:
    i+=1
    if i%2==1 and (letter=="о" or letter=="п" or letter=="е"):
        print(letter)
