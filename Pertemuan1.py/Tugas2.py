# 2.Sebuah sistem alarm memiliki tiga sensor.
# Alarm berbunyi apabila sekurang-kurangnya dua sensor aktif.
# Tentukan bentuk normal disjungtif fungsi alarm tersebut,
# sederhanakan, lalu implementasikan sebagai fungsi Python
# bernama alarm(s1, s2, s3).

# Coba 3
from itertools import product

# Fungsi Alarm menggunakan Python
def alarm(s1, s2, s3):
    return (s1 and s2) or (s1 and s3) or (s2 and s3)

# Menampilkan tabel kebenaran
print("s1 s2 s3 | alarm")
for s1, s2, s3 in product([0, 1], repeat=3):
    print(s1, s2, s3, "|", int(bool(alarm(s1, s2, s3))))
    
 # Dari sini ke atas adalah kode yang saya gunakan


# coba 2
# from itertools import product

# def alarm(s1, s2, s3):
#     return (s1 and s2) or (s1 and s3) or (s2 and s3)
# # lalu kita bisa mencobanya untuk mengetahui hasilnya true/false
# print(alarm(0, 1, 1))  # Output: True
# print(alarm(1, 0, 1))  # Output: True
# print(alarm(1, 1, 0))  # Output: True
# print(alarm(1, 1, 1))  # Output: True

# coba 1
# from itertools import product

# def alarm(s1, s2, s3):
#     return (s1 and s2) or (s1 and s3) or (s2 and s3)

# print("s1 s2 s3 | Alarm")
# for s1, s2, s3 in product([0, 1], repeat=3):
#     print( s1, s2, s3, "|", int(bool(alarm(s1, s2, s3))))


# 2.0
# from itertools import product
# from sympy import symbols
# from sympy.logic.boolalg import SOPform

# # --- 1. Tentukan minterm (kombinasi input yang membuat alarm = 1) ---
# # Alarm aktif jika minimal 2 dari 3 sensor bernilai 1
# s1_sym, s2_sym, s3_sym = symbols('s1 s2 s3')
# minterms = [list(combo) for combo in product([0, 1], repeat=3) if sum(combo) >= 2]

# print("Minterm (kombinasi sensor yang membuat alarm berbunyi):")
# for m in minterms:
#     print(m)

# # --- 2. Bentuk normal disjungtif (SOP) dan penyederhanaan otomatis ---
# sop_alarm = SOPform([s1_sym, s2_sym, s3_sym], minterms)
# print("\nBentuk normal disjungtif (SOP) awal (dari minterm):")
# print("F(s1,s2,s3) =", " + ".join(
#     f"({'s1' if not m[0] else 's1'}...)" for m in []
# ) or "(s1' & s2 & s3) + (s1 & s2' & s3) + (s1 & s2 & s3') + (s1 & s2 & s3)")

# print("\nSetelah disederhanakan:")
# print("F(s1,s2,s3) =", sop_alarm)   # hasil: (s1 & s2) | (s1 & s3) | (s2 & s3)

# # --- 3. Implementasi fungsi Python ---
# def alarm(s1, s2, s3):
#     return (s1 and s2) or (s1 and s3) or (s2 and s3)

# # --- 4. Verifikasi dengan tabel kebenaran lengkap (8 kombinasi) ---
# print("\ns1 s2 s3 | Alarm")
# for s1, s2, s3 in product([0, 1], repeat=3):
#     print(s1, s2, s3, "|", int(bool(alarm(s1, s2, s3))))
