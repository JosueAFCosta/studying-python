salary = float(input("Escreva o salário atual do funcionário:\n"))

if salary > 1250.00:
    aumento = salary/100 * 10
    print(f"O salário atual está baixo. O valor do aumento do salário será: R${aumento:.2f}\nResultando em um salário de: R${salary+aumento:.2f}")
else:
    aumento = salary/100 * 15
    print(f"O salário atual já está alto. O valor do aumento do salário será: R${aumento:.2f}\nResultando em um salário de: R${salary+aumento:.2f}")