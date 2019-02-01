

def get_float(arg):
    while(True):
        input_var = input(f'Введите {arg}: ')
        try:
           return float(input_var)
        except:
            print('Неверный формат')

a = get_float('a')
b = get_float('b')
c = get_float('c')

if a >= b and a >= c:
    print('Максимальное число а =', a)
elif b >= c and b >= a:
    print('Максимальное число b =', b)
else:
    print('Максимальное число c =', c)
