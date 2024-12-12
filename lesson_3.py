# №1
n=int(input('введите n: '))
if n <= 100:
  for n in range(1, n+1):
    print(n**3)
else:
  print('n > 100')

# №2
for i in range(9, 0, -1):
    strochka = [i*j for j in range(1, 10)]
    for j in range(len(strochka)):
        if len(str(strochka[j])) == 1 and j != 8:
             print(f'{strochka[j]}  ', end='')
        elif len(str(strochka[j])) != 1 and j != 8:
             print(f'{strochka[j]} ', end='')
        else:
             print(f'{strochka[j]}', end='\n')
