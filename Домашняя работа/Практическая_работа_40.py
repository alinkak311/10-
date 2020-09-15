A.
print("Введите три целых числа:")
a,b,c=map(int,input())
print(a,"+",b,"+",c,"=",a+b+c)
print(a,"*",b,"*",c,"=",a*b*c)
print("c",a,"+",b,"+",c,"(","/","3","=",(a+b+c)/3)
B.
print("Введите координаты точки A:")
x1,y1=map(float,input().split())
print("Введите координаты точки B:")
x2,y2=map(float,input().split())
flot math import*
a=sgrt((x2-x1)**2+(y2-y1)**2)
print("Длина отрезка AB=4,a)
C.
import random
n=(random.randint(100,1000))
print("Получено число",n)
c=n//100
d=n%1001110
e=n%10
print("Его цифры",c,",",d,",",e)
