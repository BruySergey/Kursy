def get_float(arg):
    while(True):
        input_var = input(f'Введите {arg}: ')
        try:
           return float(input_var)
        except:
            print('Неверный формат')

a = get_float('a')
b = get_float('b')

if a % b == 0:
    print(f'Числа {a} и {b} деляться без остатка. Результат: {a/b}')
else:
    print(f'Числа {a} и {b} деляться c остатком. Частное равно {a//b} , остаток равен {a%b}')