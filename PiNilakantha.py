terms = 100000000

pi = 3.0
for k in range(1, terms):
    term = 4.0 / (2 * k * (2 * k + 1) * (2 * k + 2))
    if k % 2 == 1:
        pi += term
    else:
        pi -= term
print(f"Approximation of Pi using {terms} terms: {pi}")
