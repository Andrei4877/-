print("Решение квадратного уравнения через дискриминант")
print('Введите значения a,b,c') 
a=int(input())
b=int(input())
c=int(input())
D=b**2-4*a*c
import math
print('Дискрименант D='+str(D))# приведение числа к виду строки с помощью str
if D>0:
        X1=(-b-math.sqrt(D))/(2*a)
        print('X1='+str(X1))
        X2=(-b+math.sqrt(D))/(2*a)
        print('X2='+str(X2))
elif D==0:
        X=-(b/2*a)
        print('X=X1=X2='+str(X))
else: print('Решение уравнения лежит в поле комплексных чисел')



