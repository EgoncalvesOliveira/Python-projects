#Quebra de linha
print('Giraffe \nAcademy') 

# String variable
phrase = 'Giraffe Academy'
print(phrase, 'is cool')
print(phrase + ' is cool')

#converte string em letras maisculas 
print(phrase.upper()) 

#Checa se a string está toda maiuscula se sim retorna TRUE
print(phrase.upper().isupper())

#Contagem quantidade de caracteres string
print(len(phrase))

#Trabalhando com caracteres individuais de uma string
print(phrase[0]) # index 0 indica a posiçao de acesso

#Obetendo o numero do index (posição) dentro de uma string
print(phrase.index('a')) # retorna posição 3

#Substituindo valores dentro de uma string
phrase1 = 'Giraffe Academy'
print(phrase1.replace('Giraffe','Elephant')) 

