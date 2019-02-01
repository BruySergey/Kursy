massiv = [543, 534, 543, 765, 745, 437, 653, 43, 765, 44]

summa = 0
proiz = 1

for item in massiv:
    if item % 2 == 0:
        summa += item
        proiz *= item

print(f'Summa = {summa}')
print(f'Proizvedenie = {proiz}')
