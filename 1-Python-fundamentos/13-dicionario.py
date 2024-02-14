game = {
    "name": "Elden Ring",
    "price": 199.99,
    "yearLaunched": 2023,
    "rate": 9.9,
    "genre": ["fantasy", "RPG"]
}

print(game)
print(len(game))
print(type(game))

# 1 - Recuperando um elemento do dicionário: dict[key] or dict.get(key)

print(game["name"])
print(game.get("genre"))

# 2 - Buscando apenas as chaves: dict.keys()

print(game.keys())

# 3 - Buscando apenas os valores: dict.values()

print(game.values())

# 4 - Retorna itens do dicionário como uma listade tuplas: dict.items()

print(game.items())

# 5 - Adicionando itens no dicionário: dict[newItem]

game["playTimeInHours"] = 120
print(game)

# 6 - Atualizando itens no dicionário: dict.update(key: new Value)

game.update({"playTimeInHours": 130})
print(game)

# 7 - Removendo item no dicionário: dict.pop(key)

game.pop("playTimeInHours")
print(game)