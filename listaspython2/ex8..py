#Criando uma lista de números
numeros = [10, 20, 30, 40, 50]

#Inicializando a variável que irá armazenar o maior número
maior_numero = numeros[0]

#usando um loop FOR pra percorrer a lista e encontrar o maior número
for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero
        
#Imprimindo o resultado
print('O maior número da lista é: ', maior_numero)