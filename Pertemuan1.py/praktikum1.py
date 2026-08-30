# PRAKTIKUM

# Praktikum 1.1 Membangun Tabel Kebenaran
from itertools import product

def f(x, y, z):
    return (x and y) or ((not x) and z)

print("x y z | f")
for x, y, z in product([0, 1], repeat=3):
    print(x, y, z, "|", int(bool(f(x, y, z))))

# Praktikum 1.2 Verifikasi Hukum Penyerapan
from sympy import symbols, simplify_logic
from sympy.logic.boolalg import And, Or, Not

x, y = symbols('x y')

e1 = Or(x, And(x, y))
print("Ekspresi asli  :", e1)
print("Hasil sederhana:", simplify_logic(e1))

e2 = And(Or(x, y), Or(x, Not(y)))
print("Ekspresi asli  :", e2)
print("Hasil sederhana:", simplify_logic(e2))

# Praktikum 1.3 Sintesis Fungsi dari Tabel Kebenaran
from sympy import symbols
from sympy.logic.boolalg import SOPform, POSform

a, b, c = symbols('a b c')
minterm = [[0, 0, 1], [0, 1, 1], [1, 0, 1],
           [1, 1, 0], [1, 1, 1]]

print("SOP:", SOPform([a, b, c], minterm))
print("POS:", POSform([a, b, c], minterm))

# Praktikum 1.4 Verifikasi Hukum De Morgan
from sympy import symbols, simplify_logic
from sympy.logic.boolalg import And, Or, Not, Equivalent

a, b = symbols('a b')
kiri = Not(And(a, b))
kanan = Or(Not(a), Not(b))

print("Ekivalen?", simplify_logic(Equivalent(kiri, kanan)))

# Praktikum 1.5 Tabel Kebenaran Simbolik
from sympy import symbols
from sympy.logic.boolalg import And, Or, Not, truth_table

a, b, c = symbols('a b c')
f = Or(And(a, b), And(Not(a), c))

print("a b c | f")
for baris, hasil in truth_table(f, [a, b, c]):
    print(*baris, "|", int(bool(hasil)))