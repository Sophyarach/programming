print("введите что-нибудь на английском")
words=input()
if words=="":
    print("Вы ничего не ввели")
words=words.split()
result=[]
for word in words:
    x=len(word)
    if word[0].lower() not in "aeiou": #"y" в начале слова согласная, не считая иностранных имен собственных
        while x>0 and word[0].lower() not in "aeiouy": #в середине слова "y" согласная только после гласных
            word=word[1:]+word[0]
            x-=1 #чтобы не зациклиться, если в слове не окажется гласных
    result.append(word+"ay")
print(" ".join(result))
