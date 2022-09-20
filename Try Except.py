# Tratamento de exeções é usado para verificar se o 
# usuario digitou o valor certo, informar uma mensagem
# para ele e não gerar erros na execução do programa
# protege o programa de entradas invalidas

try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)

# Cria uma excessão para divisão por zero
# Cria uma variavel para armazenar o erro camada: err
# Imprime a mensagem contida na variavel: err
except ZeroDivisionError as err:
     print(err)
     # Cria uma excessão para valores de entrada errado
     # diferente de inteiros
except ValueError:
    print("Invalide input")