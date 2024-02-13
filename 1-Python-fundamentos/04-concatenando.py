name = input("Digite o nome do Jogo:\n")
yearLaunched = int(input("Escreva o ano de lançamento do jogo:\n"))
gamePrice = float(input("Escreva o valor do jogo:\n"))
planIncluded = bool(input("Está incluso no plano:\n"))

print("###Dados do Jogo####")
print("====================")
# Alternativa 1
# print("Nome do Jogo:", name)
# print("Ano do Jogo:", yearLaunch)
# print("Preço do Jogo:", gamePrice)
# print("Está incluído no plano?", planIncluded)

# Alternativa 2
# print("Nome do Jogo:", name, "\nAno de lançamento:", yearLaunch,
#       "\nPreço do Jogo:", gamePrice, "\nEstá incluso no serviço?", planIncluded)

# Alternativa 3
print(f"Nome do Jogo: {name}\nAno de lançamento do Jogo: {yearLaunched}\nPreço do jogo: {gamePrice}\nEstá incluso no plano?: {"sim" if planIncluded else "não"}")