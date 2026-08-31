# 4.Tulis fungsi Python bernama sama(f, g, n)
# yang menerima dua fungsi Boolean dengan n peubah
# dan mengembalikan True apabila keduanya memiliki
# tabel kebenaran identik. Uji fungsi tersebut pada
# pasangan ekspresi dari Latihan nomor 1.
# from itertools import product

# Coba 3
from itertools import product

# Fungsi pertama dari nomor 1
def f(a, b, c):
    return (a or b) and ((not a) or c)

# Fungsi kedua, hasil penyederhanaan nomor 1
def g(a, b, c):
    return ((not a) and b) or (a and c)

# Fungsi untuk mengecek apakah dua fungsi ekuivalen
def sama(f, g, n):
    for nilai in product([False, True], repeat=n):
        if f(*nilai) != g(*nilai):
            return False
    return True

# Pengujian
print("Apakah f dan g sama?", sama(f, g, 3))

# Dari sini ke atas adalah kode yang saya gunakan


# # coba 2
# from itertools import product

# # Fungsi awal dari nomor 1
# def f(a, b, c):
#     return (a or b) and ((not a) or c)

# # Fungsi hasil penyederhanaan dari nomor 1
# def g(a, b, c):
#     return (a and c) or ((not a) and b)

# # Fungsi untuk mengecek apakah dua fungsi identik
# def sama(f, g, n):
#     for input in product([0, 1], repeat=n):
#         if f(*input) != g(*input):
#             return False
#     return True

# # Pengujian
# hasil = sama(f, g, 3)
# print("Apakah f dan g sama?", hasil)

# def sama(f, g, n):
#     for nilai in product([0, 1], repeat=n):

#         hasil_f = f(*nilai)
#         hasil_g = g(*nilai)

#         if bool(hasil_f) != bool(hasil_g):
#             return False
#     return True

# # Fungsi asli dari latihan nomor 1
# def f1(a, b, c):
#     return (a or b) and ((not a) or c)

# # Fungsi hasil penyederhanaan
# def g1(a, b, c):
#     return (a and c) or ((not a) and b)

# print("\nLATIHAN 4")
# print("Apakah kedua fungsi identik?", sama(f1, g1, 3))
