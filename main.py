from sys import exit
import requests

link = input('Digite a pagina:')
page = requests.get(link)

print(f'Status da página: {page.status_code}')

print('')

print('Teste na página inicial')

if page.status_code >= 200 and page.status_code <= 299:
    print('=> Página acessada com sucesso!')
else:
    print('Um erro ocorreu: página principal deu uma resposta diferente de 200')

    exit()

print('<- teste na página inicial feito')

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

            if page.status_code >= 200 and page.status_code <= 299:
                print(f'=> {test}: funcionou')
            else:
                print(f'-> {test}: não funcionou')
        
            i += 1
        except IndexError:
            break

print('<- Programa finalizado')
