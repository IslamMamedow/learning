import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}


def find_key(struct, key, value):
    if key in struct:
        struct[key] = value

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            find_key(sub_struct, key, value)


def print_dict(some_dict, count=1, spaces='    '):
    for k_key in some_dict:
        print(spaces * count, f'"{k_key}":')

        if isinstance(some_dict[k_key], dict):
            print_dict(some_dict[k_key], count + 1)
        else:
            print(spaces * (count + 2), '"' + ''.join(some_dict[k_key]) + '"')


sites_dict = dict()
site_amt = int(input('Сколько сайтов? '))
for i in range(site_amt):
    product = input('Введите название продукта для нового сайта: ')
    key_template = {'title': f'Куплю/продам {product} недорого', 'h2': f'У нас самая низкая цена на {product}'}
    for i_key, i_value in key_template.items():
        find_key(site, i_key, i_value)

    new_site = copy.deepcopy(site)
    sites_dict[product] = new_site
    for j_key, j_value in sites_dict.items():
        print(f'Сайт для {j_key}:')
        print('site = {')
        print_dict(j_value)
        for h in range(2, -1, -1):
            print(h * '    ' + '}')
