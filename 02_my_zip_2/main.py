def analog_zip_2(*args):
    min_len = min(len(i_object) for i_object in args)
    zip_list = [tuple() for _ in range(min_len)]
    for j_object in args:
        temp_object = list(j_object)
        for k_index in range(min_len):
            zip_list[k_index] += (temp_object[k_index],)

    return zip_list

#
# a = {'a': 5, 'b': 4, 'c': 3, 'd': 5, 4: 6, 9: 0}
# b = (1, 2, 3, 4, 5, 6)
# c = [1, 3, 4, 5, 2, 2]
# d = (1, 5, 6, 4, 7, 4, 4)
# output_zip = analog_zip_2(a, b, c, d)
# print(output_zip)
