string = input("Escreva uma frase:\n")

print("\n\n")
print(f"Sua string:\n{string}\n")
print(f"String sem caracteres repetidos:\n{string.replace(string[0], "$")}")
