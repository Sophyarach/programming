print("Введите температуру в градусах Цельсия")
c=input()
if c=="":
    print("Пустая строка")
else:
    c=float(c)
    print("Температура по Фаренгейту", c*1.8+32)
    print("Температура по Кельвину", c+273.15)
