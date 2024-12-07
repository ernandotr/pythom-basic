# Estrutura de decisão (if, elif, else)

nota = 85

if nota >= 90:
    print("Nota: A")
elif nota >= 80:
    print("Nota: B")
elif nota >= 70:
    print("Nota: C")
else:
    print("Nota: D")


# Estrutura de Repetição 
# For
frutas = ["Maçã", "Banana", "Laranja"]

for fruta in frutas:
    print(fruta)

# While
contator = 1
while contator <= 5:
    print("Convidados:", contator)
    contator  += 1

# Comandos de controle de fluxo
# Break
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for numero in numeros:
    if numero == 7:
        print("Número 7 encontrado: ")
        break
    print(numero)

# Continue
for numero in range(1, 10):
    if numero % 2 == 0:
        continue # pula os nímeros pares
    print("Número impar", numero)