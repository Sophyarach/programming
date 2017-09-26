c=input()
alpha='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
res=""
for x in c:
    if x=='ю':
        res+='a'
        continue
    if x=='я':
        res+='б'
        continue
    if x==' ':
        res+=' '
    b=alpha.find(x)
    if b==-1:
        continue
    res+=alpha[b+2]
print(res)
    
