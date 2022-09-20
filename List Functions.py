lucky_numbers = [42, 23, 15, 16, 8, 4]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

#exemplo imprimi as duas listas de elementos juntas
friends.extend(lucky_numbers)
print(friends)

######################################################
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

#exemplo adiciona um elemento ao final da lista
friends.append("Creed")
print(friends)

########################################################
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

#adiciona um elemento em uma posição especifica 
# no meio da lista. ex adiciona elemento na posição 1
friends.insert(1, "Kelly")
print(friends)

#########################################################
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

#Remoção de elementos 
friends.remove("Jim")
print(friends)

###########################################################
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

#Remoção de todos os elementos de uma lista
friends.clear()
print(friends)

###########################################################
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop()

#remove o ultimo elemento da lista
print(friends)

############################################################
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

#Verifica se o elemento exite e retorna o index dele
print(friends.index("Karen"))

###########################################################
friends = ["Kevin", "Karen", "Jim", "Jim", "Toby"]

#Conta quantas vezes o elemento aparece na lista
print(friends.count("Jim"))

###########################################################
friends = ["Kevin", "Karen", "Jim", "Jim", "Toby"]
lucky_numbers = [42, 23, 15, 16, 8, 4]

#coloca listas em ordem alfabetica
friends.sort()
lucky_numbers.sort()

print(friends)
print(lucky_numbers)

###########################################################
friends = ["Kevin", "Karen", "Jim", "Jim", "Toby"]
lucky_numbers = [42, 23, 15, 16, 8, 4]

#reversão das listas

lucky_numbers.reverse()
friends.reverse()

print(lucky_numbers)
print(friends)


