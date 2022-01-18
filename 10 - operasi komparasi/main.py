# operasi komparasi
# setiap hasil dari operasi komparasi adalah boolean
# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# lebih besar dari (>)
print("===== LEBIH BESAR DARI (>) =====")

hasil = a > 3
print(a, ">", 3, "=", hasil)

hasil = b > 3
print(b, ">", 3, "=", hasil)

hasil = b > 2
print(b, ">", 2, "=", hasil)


# lebih kecil dari (<)
print("===== LEBIH KECIL DARI (>) =====")

hasil = a < 3
print(a, "<", 3, "=", hasil)

hasil = b < 3
print(b, "<", 3, "=", hasil)

hasil = b < 2
print(b, "<", 2, "=", hasil)


# kurang dari (<)
print("===== LEBIH BESAR SAMA DENGAN (>=) =====")

hasil = a >= 3
print(a, ">=", 3, "=", hasil)

hasil = b >= 3
print(b, ">=", 3, "=", hasil)

hasil = b >= 2
print(b, ">=", 2, "=", hasil)


# lebih kecil sama dengan (<)
print("===== LEBIH KECIL SAMA DENGAN (>) =====")

hasil = a <= 3
print(a, "<=", 3, "=", hasil)

hasil = b <= 3
print(b, "<=", 3, "=", hasil)

hasil = b <= 2
print(b, "<=", 2, "=", hasil)


# sama dengan
print("===== SAMA DENGAN (>) =====")

hasil = a == 4
print(a, "==", 4, "=", hasil)

hasil = a == 2
print(a, "==", 2, "=", hasil)


# bukan sama dengan
print("===== BUKAN SAMA DENGAN (>) =====")

hasil = a != 4
print(a, "!=", 4, "=", hasil)

hasil = a != 2
print(a, "!=", 2, "=", hasil)


print("===== OBJECT IDENTITY 'IS' =====")
# 'is' sebagai komparasi object identity
x = 5 # ini adalah assigment sebuah object
y = 5
print('nilai x =', x, 'id =', hex(id(x)))
print('nilai x =', y, 'id =', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

x = 5 # ini adalah assigment sebuah object
y = 6
print('nilai x =', x, 'id =', hex(id(x)))
print('nilai x =', y, 'id =', hex(id(y)))
hasil = x is y
print('x is y =', hasil)


print("===== OBJECT IDENTITY 'IS NOT' =====")
# 'is' sebagai komparasi object identity
x = 5 # ini adalah assigment sebuah object
y = 5
print('nilai x =', x, 'id =', hex(id(x)))
print('nilai x =', y, 'id =', hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)

x = 5 # ini adalah assigment sebuah object
y = 6
print('nilai x =', x, 'id =', hex(id(x)))
print('nilai x =', y, 'id =', hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)