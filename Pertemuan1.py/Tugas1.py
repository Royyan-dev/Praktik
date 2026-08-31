# 1.Susun tabel kebenaran untuk fungsi f(a,b,c) = (a+b)(a’+c)
# menggunakan itertools.product, kemudian sederhanakan 
# ekspresinya dengan simplify_logic dan jelaskan berapa 
# jumlah gerbang yang dihemat.
from itertools import product
from sympy import symbols, simplify_logic
from sympy.logic.boolalg import And, Or, Not

# Fungsi Boolean menggunakan Python
def f(a, b, c):
    return (a or b) and ((not a) or c)

# Menampilkan tabel kebenaran
print("a b c | f")
for a, b, c in product([0, 1], repeat=3):
    print(a, b, c, "|", int(bool(f(a, b, c))))

# Penyederhanaan menggunakan SymPy
a, b, c = symbols('a b c')
ekspresi = And(Or(a, b),Or(Not(a), c))

print("Ekspresi asli  :", ekspresi)
print("Hasil sederhana:", simplify_logic(ekspresi))

# Dari sini ke atas adalah kode yang saya gunakan
# Code di bawah ini belum mau saya hapus karena saya ingin menyimpannya sebagai arsip percobaan saya.

# Coba 2
# from itertools import product
# from sympy import symbols, simplify_logic

# # Membuat variabel Boolean
# a, b, c = symbols('a b c')

# # Fungsi Boolean
# def f(a, b, c):
#     return (a or b) and ((not a) or c)

# # Membuat tabel kebenaran
# print("a b c | f")
# for nilai in product([0, 1], repeat=3):
#     hasil = f(*nilai)
#     print(*nilai, "|", int(hasil))


# # Penyederhanaan menggunakan SymPy
# ekspresi = (a | b) & (~a | c)

# hasil_sederhana = simplify_logic(ekspresi, form='dnf')

# print("\nEkspresi awal     :", ekspresi)
# print("Hasil sederhana   :", hasil_sederhana)
