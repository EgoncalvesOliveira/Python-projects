# definição de matriz

from telnetlib import WONT


number_grid = [
[1, 2, 3],  # linha [0]
[4, 5, 6],  # limha [1]
[7, 8, 9],  # linha [2]
[0]         # linha [3]
]

# acesso de um elemento detro da matriz utiliza-se linha e coluna
# ex: [0][0] linha zero e coluna zero resultado  = 1
#print(number_grid[0][0])

# ex: [2][2] linha zero e coluna zero resultado  = 9
#print(number_grid[2][2])

for row in number_grid:
    for col in row:
        print(col)