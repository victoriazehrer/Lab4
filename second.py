file = open('lab1.txt')
expsArr = file.readlines()
file.close()

for exp in expsArr:
    ops = ['+', '-', '*', '/']
    counter = 0

    for op in ops:
        counter = counter + exp.count(op)

    print('Вираз:', exp)
    print('Кількість операцій:', counter)
    print('Результат обчислення:', eval(exp))
    print()
