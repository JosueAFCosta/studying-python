gamesList = ["Fifa23", "Star Wars", "The Legend of Zelda", "Red Dead 2"]

# Usado para mostrar o tamanho da lista: len(lista)
print(len(gamesList))

# Retorna o índice de um elemento: lista.index(item)
print(gamesList.index("Star Wars"))

# Adiciona um elemento ao final da lista: lista.append(item)
gamesList.append("GTA V")
print(gamesList)

# Ordena a lista: lista.sort()
gamesList.sort()
print(gamesList)

# Ordena ao contrário: lista.reverse()
gamesList.reverse()
print(gamesList)

# Copia a lista para outra: novaLista = lista.copy()
copyList = gamesList.copy()
copyList.remove("GTA V")
copyList.remove("Fifa23")
print(copyList)

# Remove todos os itens de uma lista: lista.clear()
copyList.clear()
print(copyList)