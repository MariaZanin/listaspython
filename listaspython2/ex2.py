#Criando uma lista

minha_lista = [1, 2, 3, 4, 5]

#Usando um loop FOR para percorrer a lista e imprimir cada elento
for i in range(len(minha_lista)):
    print('O elemento', i+1, 'da lista é: ', minha_lista[i])
    
    
#Criando uma lista de números
numeros = [1, 2, 3, 4, 5]

#Usando um loop para percorrer a lista e imprimir cada elemento
for numero in numeros:
    print(numero, ' - Com For')
    
#Usando um loop WHILE para percorrer a lista e imprimir cada elemento
i = 0
while i < len(numeros):
    print(numeros[i], ' - Com While')
    i += 1
    

# Usar o LEN para contar o numero de elementos numa lista #