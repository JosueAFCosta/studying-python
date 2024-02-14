gamesSets = { "Fifa23", "Red Dead 2", "Star Wars", "The Legend of Zelda", "Red Dead 2" }
print(gamesSets)

# Ele não considera valores iguais

# True e 1 são considerados a mesma coisa

exampleSet = {1, True, 90.5, "Mario Odyssey"}
print(exampleSet)

# Adiciona um elemento ao set: set.add(item)

exampleSet.add(False)
exampleSet.add(0)
print(exampleSet)

# Adiciona os elementos de um set a outro: setRecebedor.update(setlistaEnviador)

gamesSets.update(exampleSet)
print(gamesSets)

# Remove um elemento de um set: set.remove(elemento)

gamesSets.remove(0)
gamesSets.remove(90.5)
gamesSets.remove(1)
print(gamesSets)