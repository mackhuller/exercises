numero = int(input("Digite um numero inteiro:"))

for i in range(numero + 1):
    if i % 2 != 0:
        print(f"{i}:impar")
    else:
        print(f"{i}:par")

for i in range(numero + 1):
    print(i)
    result = ""
    if i % 3 == 0:
        result += "FIZ"
    if i % 5 == 0:
        result += "BUZ"
    if len(result) > 0:
        print(result)
