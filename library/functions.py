from os import system
from sys import exit
def showArray(array):
    for i in range(0, len(array)):
        print(array[i])
def show(what, array, firstMessage, finalMessage):  
    print(firstMessage)
    if what:
        if len(array) == 0:
            print('Nenhum.')
        else:
            showArray(array)
    print(finalMessage)
def switchBool(value):
    match value:
        case True:
            return False
        case False:
            return True
        case _:
            return None
def firstTest(status):
    print('\nTestes com a primeira página:')
    if status == 200:
        print(f'=> Acessada com sucesso! ({status})')
    else:
        print(f'-> Página não acessada... ({status})')
    print('<- Testes com a primeira página.\n')
    system('pause')
    if (status != 200):
        exit()
