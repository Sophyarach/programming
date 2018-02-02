n=0
s=0
x=input()
if x!="":
    a=float(x)
    minimum=a
    maximum=a
while x!="":
    a=float(x)
    s+=a
    n+=1
    if a<minimum:
        minimum=a
    if a>maximum:
        maximum=a
    x=input()
if n==0:
    print("Вы не ввели ни одного числа")
else:
    print("Среднее арифметическое:", s/n)
    print("минимум:", minimum)
    print("максимум:",maximum)
