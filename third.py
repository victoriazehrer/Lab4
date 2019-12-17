from sympy import *
from sympy.solvers.solveset import linsolve

def swap_symbol(eq):
    s = ''
    for c in range(len(eq) - 1):
        if eq[c] == '^':
            s += '**'
            continue

        s += eq[c]

        if eq[c + 1] == 'x' and eq[c] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            s += '*'

    s += eq[-1]
    return s


file = open('lab11.txt')
expsArr = file.readlines()
file.close()


for exp in expsArr:
    exp = exp.strip()
    print('-----------------------------------------')

    if '<' in exp or '>' in exp:
        rivnanya = 0
        print(exp, '-', 'нерівність')
    else:
        rivnanya = 1
        print(exp, '-', 'рівняння')

    if '^' in exp:
        maxPow = 0
        for c in range(len(exp) - 1):
            if exp[c] == '^':
                if int(exp[c + 1]) > maxPow:
                    maxPow = int(exp[c + 1])

        print('Максимальна степінь:', maxPow)

    exp = swap_symbol(exp)

    if rivnanya:
        exp = exp.split('=')[0]
    else:
        if '<' in exp:
            exp = exp.split('<')[0]
        elif '>':
            exp = exp.split('>')[0]
            
    x = symbols('x')
    a = Poly(exp, x)
    print('Коефіцієнти:', a.coeffs())
    
    answer = solve(exp, x)

    if str(answer) in ['True', 'False']:
        if answer:
            print('Відповідь:', 'вся множина розв\'язків')
        else:
            print('Відповідь:', 'немає розв\'язків')
    else:
        print('Відповідь:', answer)
