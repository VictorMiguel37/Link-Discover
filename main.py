from sys import exit
import requests

worked = []      # Funcionou
dworked = []     # Não funcionou
nauthorized = [] # Não autorizado
link = input('Digite a pagina (insira o link completo):')
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

print('Links que não funcionaram:')

for i in range(0, len(dworked)):
    print(dworked[i])

print('<- Links que não funcionaram.')

print('')

print('Não autorizados:')

for i in range(0, len(nauthorized)):
    print(nauthorized[i])

print('<- Não autorizados.')

print('')

print('Links que funcionaram:')

for i in range(0, len(worked)):
    print(worked[i])

print('<- Programa finalizado.')

exit()
