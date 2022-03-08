from random import randint


def corretor_cpf():    
    cpf = input('Digite o CPF a ser checado: ')
    if len(cpf) == 14:
        cpf = cpf.replace('.', '')
        cpf = cpf.replace('-', '')
    copia_cpf = cpf
    if len(cpf) == 11:
        cpf = cpf[:-2]
    soma, timer = 0, 10
    for i in range(0, 9):
        soma = soma + (int(cpf[i]) * timer)
        timer = timer - 1
    digito_1 = 11 - (soma % 11)
    if digito_1 > 9:
        digito_1 = 0
    cpf = cpf + str(digito_1)
    soma, timer = 0, 11
    for i in range(0, 10):
        soma = soma + (int(cpf[i]) * timer)
        timer = timer - 1
    digito_2 = 11 - (soma % 11)
    cpf = cpf + str(digito_2)
    if cpf == copia_cpf:
        print(f'CPF {cpf} válido.\n')
    elif cpf != copia_cpf:
        print(f'CPF {copia_cpf} inválido.')
        print(f'CPF válido = {cpf}\n')




def cpf_gen():
    cpf = ''
    while len(cpf) != 11:
        cpf = str(randint(111111111, 999999999))
        soma, timer = 0, 10
        for i in range(0, 9):
            soma = soma + (int(cpf[i]) * timer)
            timer = timer - 1
        digito_1 = 11 - (soma % 11)
        if digito_1 > 9:
            digito_1 = 0
        cpf = cpf + str(digito_1)
        soma, timer = 0, 11
        for i in range(0, 10):
            soma = soma + (int(cpf[i]) * timer)
            timer = timer - 1
        digito_2 = 11 - (soma % 11)
        cpf = cpf + str(digito_2)
    print(f'CPF = {cpf}\n')


entry = 1
while entry != 0:
    entry = int(input('Para checar e corrigir um CPF, digite : (1)\nPara gerar um CPF, digite: (2)\nPara sair, digite: (0)\n> '))
    if entry == 1:
        corretor_cpf()
    elif entry == 2:
        cpf_gen()