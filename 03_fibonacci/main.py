def fibonacci(position):
    if position in (1, 2):
        return 1
    return fibonacci(position - 1) + fibonacci(position - 2)


user_position = int(input('Введите позицию числа в ряде Фибоначчи: '))
print(fibonacci(user_position))
