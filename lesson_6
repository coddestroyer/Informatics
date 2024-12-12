# №1
n=3 
a=[]
for i in range (n) : 
    b = [] 
    for j in range (n):
           print ('Введите [',i,', ',j,'] элемент')
           b. append (int (input 0))) 
     a. append (b) 
for i in range (n) : 
     for j in range (n):
           print (a[i][i], end=' ')
     print ()
maximum=a [0] [2] 
for i in range (n) :
     for j in range (n):
            if maximum<a [i] [2]:
            maximum=a[i] [2]
print ('Максимальный в 3 столбце: ', maximum)
maximum=a [1] [0]
for i in range (n) :
      for j in range (n):
            if maximum<a[1][j]:
                maximum=a[1][j] 

# №2
m = int(input('Введите кол-во строк'))
n = int(input('Введите кол-во столбцов'))
a = []
for i in range(m):
    b = []
    for j in range(n):
        print('Введите[',i,',',j,'] элемент')
        b.append(int(input()))
    a.append(b)
print('Исходный массив: ')
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
for i in range(m):
    if j ia[i][j] < 0:
        a[i][j] = 0
    elif a[i][j] > 0:
        a[i][j] = 1
print('новый массив: ')
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()

# №3
def is_magic(matrix):
    summ = sum(matrix[0])
    for i in range(len(matrix)):
        temp = 0
        for j in range(len(matrix)):
            temp += matrix[j][i]
        if temp != summ or sum(matrix[i]) != summ:
            return False
    return True
mat = [[4, 3, 3], [3, 4, 3], [3, 3, 4]]
print(is_magic(mat))
mat = [[4, 3, 4], [3, 4, 3], [3, 3, 4]]
print(is_magic(mat))

# №4
import random
n = int(input('Введите кол-во строк и столбцов матрицы: '))
h = ('')
matrix = [[random.randrange(10) for i in range(n)] for j in range(n)]
for elem in matrix:
    print(elem)
for k in range(n):
    for l in range(1,n):
        if matrix[k][l]!= matrix[l][k]:
            h = ('False')
            break
if h != ('False'):
    print('Матрица симметрична')
else:
    print('Обычная матрица')

# №5
from random import randint
m, n = randint(2, 10), randint(2, 10)
arr = list()
for i in range(m):
    brr = list()
    for j in range(n):
        brr.append(randint(-10, 10))
    arr.append(brr)
print(arr)
summi = {}
for i in arr:
    summi.update({sum(i):i})
print(f'максимальная сумма {max(summi.keys())} у строчки {summi.get(max(summi.keys()))}')
print(f'минимальная сумма {min(summi.keys())} у строчки {summi.get(min(summi.keys()))}')

# №6
from random import sample, randint
m, n = randint(2, 10), randint(2, 10)
arr = list()
for i in range(n):
    brr = sample(range(-30, 30), m)
    arr.append(brr)
print(arr)
for i in arr:
    if i[i.index(min(i))] % 2 == 0:
        i[i.index(min(i))] = 0
    else:
        i[i.index(min(i))] = 1
print(arr)
