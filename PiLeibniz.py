
# PiLeibniz.py
# Approximate the value of Pi using the Leibniz formula

#  π=4×k=0∑∞​2k+1(−1)k​

terms = 1000000
pi = 0.0
for k in range(terms):
    pi += ((-1)**k) / (2*k + 1)
pi *= 4

print(f"Approximation of Pi using {terms} terms: {pi}")
