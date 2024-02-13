string = input("Escreva duas frases separadas por um espaço:\n")
newString1 = string.split(" ")[0].replace(string.split(" ")[0][0:2],string.split(" ")[1][0:2])
newString2 = string.split(" ")[1].replace(string.split(" ")[1][0:2],string.split(" ")[0][0:2])

print("\n\n")
print(f"String original:\n{string}\n")
print(f"Nova string:{newString1} {newString2}")