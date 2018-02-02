print("введите что-нибудь на английском")
words=input()
result=""
y=1 #здесь я пытаюсь отслеживать гласная ли "y", считаю что после согласной гласная, иначе согласная
if words=="":
    print("Вы ничего не ввели")
for letter in words:
    result+=letter
    if letter.lower() in ("qwrtpsdfghjklzxcvbnm") or (letter.lower()=="y" and y==1):
        y=0
        result+="aig"
    else:
        y=1
print(result)
            
            
        
