# Define a variavel letter para cada letra da sting imprimi a letra
for letter in "Giraffe Academy":
    print (letter)

    # Outro exemplo: para cada amigo dentro do array de amigos imprime
    # faz um loop e imprime o nome do amigo

friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
        print(friend)

    # Outro exemplo: imprime os valore em um ranger de 3 a 9
#for index in range(3, 10):
 #   print(index) 

    # Outro exemplo, pega o tamanho do array  
    # ex: friends = ["Jim", "Karen", "Kevin"]
    # tamanho do array  = 3
    # faz um for e imprime todos elementos 
    #  friends[0], friends[1], friends[2]
    # até tamanho maximo que está contido em index,
    # A cada ciclo index vale um valor ex: index =1
for index in range(len(friends)):
    print(friends[index])