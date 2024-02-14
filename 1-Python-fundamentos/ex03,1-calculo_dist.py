distance = float(input("Escreva a distância da viagem em km:\n"))

if distance > 200:
    print(f"A viagem será longa. O valor da viagem será: R${distance*0.35}")
else:
    print(f"A viagem não será tão longa. O valor da viagem será: R${distance*0.50}")