print("введите что-нибудь на русском")
words=input()
if words=="":
    print("Вы ничего не ввели")
result=""
for letter in words:
    result+=letter
    if letter.lower() in "аяэеоёиыую":
        result=result+"с"+letter.lower()
print(result)
