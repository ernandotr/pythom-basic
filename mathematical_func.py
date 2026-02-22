import sympy as sp
from IPython.display import display

a, b, c = sp.symbols('a b c')
f = (-b + sp.sqrt(b**2 - 4*a*c)) / (2*a)

display(sp.Eq(sp.Symbol("solve(a, b, c)"), f))
