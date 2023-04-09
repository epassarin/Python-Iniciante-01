#testando se o numero é PAR ou IMPAR
vResultado = ""
vNum = int(input('Entre com um numero para verificação'))
if vNum % 2 == 0:
vResultado = "PAR"
else:
vResultado = "IMPAR"
print("O que voce digitou foi: ", vNum, "e esse  numero é ", vRResultado)
#Apresenta resultado se o numero é PAR ou IMPAR
vExplica  = ""
vConta = "0.0"
if vResultado = "PAR":
    vExplica = "Isso quer dizer que o numero que voce digitou é divisivel por 2 e o resultado final é 0"
    vConta = vNum % 2
    print(vConta)
else:
    vExplica = "Seu numero é impar porque se tentar dividi-lo o resultado sempre será diferente de 0"
    vConta = vNum % 2
    print(vConta)
print("O numero que voce digitou foi: ", vNum, " e ele é um numero ", vResultado)
print("O que isso quer dizer: ", vExplica, "ou seja", vConta)



