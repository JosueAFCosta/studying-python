num1 = int(input("Digite o Primeiro Número:\n"))
num2 = int(input("Digite o Segundo Número:\n"))

# Operações
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
expo = num1 ** num2

print(f"{sum}\n{sub}\n{div}\n{mult}\n{mod}\n{expo}")

# Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
diff = num1 != num2
biggerEqual = num1 >= num2
smallerEqual = num1 <= num2

print(f"Os números {num1} e {num2} são iguais? {equal}")
print(f"O número {num1} é maior ou igual a {num2}? {biggerEqual}")

# Atribuição
num1 += 1 # num1 = num1 + 1
num1 -= 1 # num1 = num1 - 1
num1 *= 1 # num1 = num1 * 1
num1 /= 1 # num1 = num1 / 1