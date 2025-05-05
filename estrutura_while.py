
import datetime
escolha = ''
while escolha != 'n':
    ano_nascimento = int(input('Digite o ano de nascimento e tecle enter: '))
    
    idade = datetime.date.today().year -ano_nascimento
    
    print(f'A idade do usuário é {idade} anos.')
    escolha = input('Deseja fazer uma nova verificação? S ou N ').lower()
print('Fim do programa')