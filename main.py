from os import system
from sys import exit
import requests

system('cls')

worked = []      # Funcionou
dworked = []     # Não funcionou
nauthorized = [] # Não autorizado

showWorked = True
showNotWorked = True
showNotAuthorized = True
clearScreenAfterTests = False
pauseProgramOnFinal = False

while True:
    system('cls')
    
    link = input('Digite a pagina (insira o link completo, "configs" para configurações):\n')

    if link == 'configs':
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
                case 1:
                    if showWorked == True:
                        showWorked = False
                    else:
                        showWorked = True
                case 2:
                    if showNotWorked == True:
                        showNotWorked = False
                    else:
                        showNotWorked = True
                case 3:
                    if showNotAuthorized == True:
                        showNotAuthorized = False
                    else:
                        showNotAuthorized = True
                case 4:
                    if clearScreenAfterTests == True:
                        clearScreenAfterTests = False
                    else:
                        clearScreenAfterTests = True
                case 5:
                    if pauseProgramOnFinal == True:
                        pauseProgramOnFinal = False
                    else:
                        pauseProgramOnFinal = True
                case _:
                    break
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

print('<- teste na página inicial feito.')

print('')

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

print('<- Testes com subpáginas.')

print('')

if clearScreenAfterTests == True:
    system('cls')

if showNotWorked == True:
    print('Links que não funcionaram:')

    for i in range(0, len(dworked)):
        print(dworked[i])

    print('<- Links que não funcionaram.')

    print('')

if showNotAuthorized == True:
    print('Não autorizados:')

    for i in range(0, len(nauthorized)):
        print(nauthorized[i])

    print('<- Não autorizados.')

    print('')

if showWorked == True:
    print('Links que funcionaram:')

    for i in range(0, len(worked)):
        print(worked[i])

    print('<- Links que funcionaram.\n')

print('Fim do programa')

if pauseProgramOnFinal == True:
    system('pause')

exit()
