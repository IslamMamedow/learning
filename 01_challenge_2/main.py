def count_numb(n):
    if n == 1:
        print(1)
        return
    count_numb(n - 1)
    print(n)


numb = int(input('Введите число: '))
count_numb(numb)
