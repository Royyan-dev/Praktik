# 3.Buktikan hukum penyerapan bentuk kedua,
# yaitu a(a+b) = a, dengan dua cara: penurunan
# aljabar menggunakan aksioma Huntington yang
# ditulis tangan, dan verifikasi komputasional
# menggunakan SymPy. Jelaskan perbedaan status
# kedua pembuktian tersebut.

# Tes 4
from sympy import symbols, simplify_logic

# variabel Boolean
a, b = symbols('a b')

# ekspresi a(a+b)
ekspresi = a & (a | b)

# Sederhanakan
hasil = simplify_logic(ekspresi)

# hasil
print("Ekspresi awal :", ekspresi)
print("Hasil sederhana :", hasil)

 # Dari sini ke atas adalah kode yang saya gunakan

# Verifikasi
# print("Terbukti :", hasil == a)

# from sympy import symbols, simplify_logic
# from sympy.logic.boolalg import And, Or

# a, b = symbols('a b')
# ekspresi = And(a, Or(a, b))

# print("Ekspresi asli  :", ekspresi)
# print("Hasil sederhana:", simplify_logic(ekspresi))

# tes 2
# from sympy import symbols, simplify_logic

# a, b = symbols('a b')
# expr = a & (a | b)

# hasil = simplify_logic(expr, force=True)
# print(hasil)

# tes 3
# from sympy import symbols, simplify_logic

# a, b = symbols('a b')

# ekspresi = a & (a | b)

# hasil = simplify_logic(ekspresi)

# print("Ekspresi awal :", ekspresi)
# print("Hasil sederhana:", hasil)
