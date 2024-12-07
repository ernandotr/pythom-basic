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

# map() function
# map(function, interable)

initial_values = [1000, 1500, 2000, 3000]
print("Initial values", initial_values)
# interest_calc = lambda value: value * 1.02
# values_with_interest = list(map(interest_calc, initial_values))
values_with_interest = list(map(lambda value: value * 1.02, initial_values))
print("Values with 2% interest applied", values_with_interest)