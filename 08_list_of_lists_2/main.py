def add_list(user_list):
    new_list = []
    for i_elem in user_list:
        if isinstance(i_elem, int):
            new_list.append(i_elem)
        else:
            new_list.extend(add_list(i_elem))

    return new_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print('Ответ:', add_list(nice_list))

