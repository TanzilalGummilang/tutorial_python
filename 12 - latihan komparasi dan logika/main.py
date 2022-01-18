"""
# membuat gabungan area dari rentang angka

# ++++++++++3----------10++++++++++

print('\n=====')
InputUser = float(input("masukan angka bernilai \nlebih kecil dari 3 \natau \nlebih besar dari 10 \n:"))

# ++++++++++3-----
# memeriksa angka lebil kecil dari 3
isLebihKecil = (InputUser < 3)
print("lebih keci dari 3     =", isLebihKecil)

# -----10++++++++++
# memeriksa angka lebil lebih besar dari 10
isLebihBesar = (InputUser > 10)
print("lebih besar dari 10   =", isLebihBesar)

# ++++++++++3----------10++++++++++
isCorrect = isLebihKecil or isLebihBesar
print("angka yg anda masukan =", isCorrect)


# ----------3++++++++++10----------

print('\n',5*'=')
InputUser = float(input("masukan angka bernilai \nlebih besar dari 3 \ndan \nlebih kecil dari 10 \n:"))

isLebihBesar = (InputUser > 3)
print("lebih besar dari 3    =", isLebihBesar)

isLebihKecil = (InputUser < 10)
print("lebih keci dari 10    =", isLebihKecil)

isCorrect = isLebihKecil and isLebihBesar
print("angka yg anda masukan =", isCorrect)


# -----0+++++5-----8+++++11-----

print('\n',10*'=')
InputUser = float(input("masukan angka bernilai \nlebih besar dari 0 \nDAN \nlebih kecil dari 5 \nATAU \nlebih besar dari 8 \nDAN \nlebih kecil dari 11 \n:"))

isLebihBesar_0 = InputUser > 0
print("lebih besar dari 0    =", isLebihBesar_0)

isLebihKecil_5 = InputUser < 5
print("lebih kecil dari 5    =", isLebihKecil_5)

isLebihBesar_8 = InputUser > 8
print("lebih besar dari 8    =", isLebihBesar_8)

isLebihKecil_11 = InputUser < 11
print("lebih kecil dari 11   =", isLebihKecil_11)

isCorrect = (isLebihBesar_0 and isLebihKecil_5) or (isLebihBesar_8 and isLebihKecil_11)
print("angka yg anda masukan =", isCorrect)

print(10*'=','\n')
"""

# +++++0-----5+++++8-----11+++++

print('\n',10*'=')
InputUser = float(input("masukan angka bernilai \nlebih kecil dari 0 \nATAU \nlebih besar dari 5 \nDAN \nlebih kecil dari 8 \nATAU \nlebih besar dari 11 \n:"))

isLK_0 = InputUser < 0
print("lebih kecil dari 0    =", isLK_0)

isLB_5 = InputUser > 5
print("lebih besar dari 5    =", isLB_5)

isLK_8 = InputUser < 8
print("lebih kecil dari 8    =", isLK_8)

isLB_11 = InputUser > 11
print("lebih besar dari 11   =", isLB_11)

isCorrect = (isLK_0 or isLB_5) and (isLK_8 or isLB_11)
print("angka yg anda masukan =", isCorrect)

print(10*'=','\n')