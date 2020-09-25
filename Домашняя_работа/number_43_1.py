print ("Введите три числа")
a, b, c = map (int(input().split())
if a==b==c:
    print ("Все числа одинаковые")
else:
    if a==b or a==c or b==c:
        print ("Два числа одинаковые")
else:
    print ("Нет одинаковых чисел")
