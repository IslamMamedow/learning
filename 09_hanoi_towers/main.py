def move(n, x=1, y=3):
    if n == 1:
        print(f'Переложить диск 1 со стержня {x} на стержень {y}')
    else:
        temp = 6 - x - y
        move(n - 1, x, temp)
        print(f'Переложить диск {n} со стержня {x} на стержень {y}')
        move(n - 1, temp, y)


disks_amt = int(input('Введите количество дисков: '))
move(disks_amt)
