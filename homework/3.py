def get_int():
    while(True):
        input_var = input(f'Введите целое положительное число: ')
        if input_var.isdigit():
            return int(input_var)
        print('Неверный формат. Введите только целое положительное число')

a = get_int()
bytes_or_kb = None
while(True):
    bytes_or_kb = input('Перевод в байты (1), в килобайты (2): ')
    if bytes_or_kb == '1' or bytes_or_kb == '2':
        break
    print('Неверные формат')

if bytes_or_kb == '1':
    print(f'{a} = {a//8} Б')
elif bytes_or_kb == '2':
    print(f'{a} = {a//(8*1024)} кБ')