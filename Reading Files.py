# Para ler um arquivo tenho que passar o caminho completo
# Nesse caso o aquivo encontra-se na mesma pasta que o program  
# está salvo
# Ex: open ("caminho", "r") -> caminho do arquivo e tipo de acesso
# 'r' significa leitura
# 'w' significa escrita
# 'a' significa não pode apagar nei modificar somente escrever
# 'r+' significa que você pode ler e escrever


employee_file = open("C:\employees.txt", "r")

# 1° utilizar uma função que checa se é possivel ler o arquivo
# retorna um valor boleano igual a True
print(employee_file.readable())

# Leitura do arquivo inteiro
#print(employee_file.read())

# Leitura da primera linha somente, aponta para segunda
# O segundo print le a segunda
#print(employee_file.readline())
#print(employee_file.readline())

# Le todos os valores e coloca dentro de um array
# Se quise ler uma linha especifica e só colocar o index
#print(employee_file.readlines()[3])

# Posso também usa o Laço for para ler todos os valores
# A cada execução imprime uma linha do arquivo
for employee in employee_file.readlines():
    print(employee)

employee_file.close()
