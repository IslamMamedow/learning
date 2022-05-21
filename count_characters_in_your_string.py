def count(string):
    return {i_letter: string.count(i_letter) for i_letter in string}


user_string = input()
res = count(user_string)
print(res)