file = open('Equation1.txt')
expsArr = file.readlines()
file.close()

for exp in expsArr:
    parenthesis = '' 
    for i in exp:
        if i in ('(', ')'):
            parenthesis = parenthesis + i
            if i == ')':
                if len(parenthesis) >= 2:
                    if parenthesis[-1] == ')' and parenthesis[-2] == '(':
                        parenthesis = parenthesis[:-2]
    if parenthesis:
        print('У виразі ', exp, ' неправильно розтавлені дужки.')
    else:
        print('У виразі ', exp, ' правильно розтавлені дужки.')
