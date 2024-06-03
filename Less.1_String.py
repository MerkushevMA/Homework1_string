example = 'Синхофазотрон'
a = len(example)
print('1.Строка:',example)
print('2.Первый символ строки:',example[0])
print('3.Крайний символ строки:',example[-1])
b = a / 2
print('4.Вторая половина строки (большая):',example[int(b):])
print('5.Наоборот:',example[::-1])
print('6.Каждый второй символ:',example[::2])
