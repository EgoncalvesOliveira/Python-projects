# Adicionando valores na lista de employees
# Ex 1:  Altero o argumento da função para "a"
# Ex 2: Se utilizar o argumeto da função "w" irá
# sobreescrever arquivo todo. OBS: se utiliza o argumeto"w"
# com o nome de um arquivo que não existe ele cria o arquivo


employee_files = open("C:\Projetos_Python\employees.txt_01", "w")
employee_files.write("\nMaria - Customer service")


employee_files.close()