def calculating_math_func(data, factorials=dict()):
    if data in factorials:
        result = factorials[data]
    elif len(list(factorials)) != 0 and data > max(list(factorials)):
        max_in_fact = max(list(factorials))
        result = factorials[max_in_fact]
        for index in range(max_in_fact + 1, data + 1):
            result *= index
            factorials[index] = result
    else:
        result = 1
        for index in range(1, data + 1):
            result *= index
            factorials[index] = result
    result /= data ** 3
    result = result ** 10
    return result


print(calculating_math_func(6))
print(calculating_math_func(10))
print(calculating_math_func(6))
print(calculating_math_func(14))