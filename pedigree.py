peoples_amt = int(input('Введите количество человек: '))
pedigree = dict()
height = dict()
for i in range(peoples_amt - 1):
    print(i + 1, '- я пара:', end=' ')
    couple = input().split()
    pedigree[couple[0]] = couple[1]
    height[couple[0]] = 0
    height[couple[1]] = 0

for i_man in pedigree:
    people = i_man
    while people in pedigree:
        people = pedigree[people]
        height[i_man] += 1

print('\nВысота каждого члена семьи:')
for i_people in sorted(height):
    print(i_people, height[i_people])



