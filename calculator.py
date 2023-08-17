def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "divisao por zero nao permitida"

print("Selecione uma operação:")
print("1. adicionar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

choice = input("Escolha (1/2/3/4): ")

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))

if choice == '1':
    print(num1, "+", num2, "=", adicionar(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtrair(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiplicar(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", dividir(num1, num2))
else:
    print("Saida invalida")