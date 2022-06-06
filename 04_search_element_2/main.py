site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(struct, key, depth=3):
    if depth == 0:
        return None
    if key in struct:
        return struct[key]
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, depth - 1)
            if result:
                break
    else:
        result = None

    return result


user_key = input('Введите искомый ключ: ')
depth_answer = input('Хотите ввести максимальную глубину? y/n: ')
if depth_answer == 'n':
    value = find_key(site, user_key)
    print('Значение ключа:', value)
elif depth_answer == 'y':
    user_depth = int(input('Введите максимальную глубину: '))
    value = find_key(site, user_key, user_depth)
    print('Значение ключа:', value)

