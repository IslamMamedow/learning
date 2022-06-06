def advanced_sum(*args):
    def add_list(k_list):
        new_list = []
        for i_elem in k_list:
            if isinstance(i_elem, int) or isinstance(i_elem, float):
                new_list.append(i_elem)
            else:
                new_list.extend(add_list(i_elem))
        return new_list

    print(sum(add_list(args)))


# advanced_sum([[1, 2, [3]], [1], 3])
# advanced_sum(1, 2, 3, 4, 5)
