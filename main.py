from os import system
from sys import exit
import requests

import library.functions

system('cls')

worked = []      # Funcionou
dworked = []     # Não funcionou
nauthorized = [] # Não autorizado

showWorked            = True
showNotWorked         = True
showNotAuthorized     = True
clearScreenAfterTests = False
pauseProgramOnFinal   = False

while True:
    system('cls')
    
    link = input('Digite a pagina (insira o link completo, "configs" para configurações):\n')

    if link == 'configs' or link == "CONFIGS":
        while True:
            system('cls')

            print('[0] Sair')
            print(f'[1] Mostrar páginas que funcionaram     ({showWorked})')
            print(f'[2] Mostrar páginas que não funcionaram ({showNotWorked})')
            print(f'[3] Mostrar páginas não autorizadas     ({showNotAuthorized})')
            print(f'[4] Limpar tela após testes             ({clearScreenAfterTests})')
            print(f'[5] Pausar o programa no final          ({pauseProgramOnFinal})')

            choice = int(input())

            match choice:
                case 0:
                    break
                case 1:
                    showWorked = library.functions.switchBool(showWorked)
                case 2:
                    showNotWorked = library.functions.switchBool(showNotWorked)
                case 3:
                    showNotAuthorized = library.functions.switchBool(showNotAuthorized)
                case 4:
                    clearScreenAfterTests = library.functions.switchBool(clearScreenAfterTests)
                case 5:
                    pauseProgramOnFinal = library.functions.switchBool(pauseProgramOnFinal)
                case _:
                    continue
    else:
        break

page = requests.get(link)

print(f'Status da página: {page.status_code}')

print('')

print('Teste na página inicial:')

if page.status_code >= 200 and page.status_code <= 299:
    print('=> Página acessada com sucesso!')
else:
    print('Um erro ocorreu: página principal deu uma resposta diferente de 200')

    exit()

print('<- teste na página inicial feito.\n')

print('Testes com subpáginas:')

with open ('texts/wordlist.txt', 'r') as reader:
    lines = reader.readlines()
    lines = [l.strip('\n') for l in lines]
    
    i = 0

    while True:
        try:
            test = str(link + lines[i])
            page = requests.get(test)

            if page.status_code >= 100 and page.status_code <= 199:
                print(f'&> {test}: info ({page.status_code})')
            elif page.status_code >= 200 and page.status_code <= 299:
                print(f'=> {test}: funcionou ({page.status_code})')
            
                worked.append(test)
            elif page.status_code >= 300 and page.status_code <= 399:
                print(f'~> {test}: redirecionamento ({page.status_code})')
            elif page.status_code == 403:
                print(f'<> {test}: não autorizado ({page.status_code})')

                nauthorized.append(test)
            else:
                print(f'-> {test}: não funcionou ({page.status_code})')

                dworked.append(test)
        
            i += 1
        except IndexError:
            break

print('<- Testes com subpáginas.\n')

if clearScreenAfterTests:
    system('cls')

library.functions.show(showNotWorked, dworked, 'Links que não funcionaram:', '<- Links que não funcionaram.\n')
library.functions.show(showNotAuthorized, nauthorized, 'Links não autorizados:', '<- Links não autorizados.\n')
library.functions.show(showWorked, worked, 'Páginas que funcionaram:', '<- Páginas que funcionaram.\n')

print('Fim do programa')

if pauseProgramOnFinal:
    system('pause')

exit()
