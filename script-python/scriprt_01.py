nome= input('Qual é seu nome: ')
sobrenome = input('e seu sobrenome: ')
idade = input('Nos informe sua idade: ')
signo = input('Informe seu signo: ')

print('\n\nSeja benvindo ', nome, sobrenome, '\n\nestamos felizes por te-lo aqui conosco')

print('\nPrecisamos coletar mais algiuns dados. Então vamos lá.')

dia=input('Qual o dia do seu nascimento? \n')
mes=input('Qual o mês do seu nascimento? \n')
ano=input('Qual o ano de seu nascimento? \n')

print('\n\nQue otimo sr(a) ', nome)
print('A data de seu nascimento é ', dia, ' de ', mes, ' de ', ano)
print('e voce tem ', idade, ' anos. Também é do signo de ', signo, '\n')
print('Alem de voce mais quantas pessoas residem na maesma casa \n')

nm =input('O total de pessoas que moram aqui é: ')

idf=input('A idade de minha filha é: ')
ide=input('A idade de minha esposa é: ')

idadepai = int(idade)
idadefilho = int(idf)
idademae = int(ide)

totalidade = idadepai + idademae + idadefilho

mediaidade = totalidade/3

difidpai = idadepai - idadefilho
difidmae = idademae - idadefilho

print('\n\nOlha só que dados interessantes: ')
print('O total da idade de sua familia é de: ', totalidade)
print('A média de idade de suas família é de: ', mediaidade)
print('A diferença de idade entre voce e seu filho é de: ', difidpai)
print('A diferença de idade entre a mãe e o filho é de: ', difidmae)
