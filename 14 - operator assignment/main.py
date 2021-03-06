# operasi yg dapat dilakukan dgn penyingkatan
# operasi ditambah dgn assignment

a = 5
print("nilai a =", a)

a += 1 # artinya a = a + 1
print("nilai a += 1, nilai a menjadi =", a)

a -= 2 # artinya a = a - 1
print("nilai a -= 2, nilai a menjadi =", a)

a *= 5 # artinya a = a * 5
print("nilai a *= 5, nilai a menjadi =", a)

a /= 2 # artinya a = a / 2
print("nilai a /= 2, nilai a menjadi =", a)

# modulus
b = 10
print("\nnilai b =", b)

b **= 3
print("nilai b %= 3, nilai b menjadi =", b)

# floor division
b = 10
print("\nnilai b =", b)

b //= 3
print("nilai b //= 3, nilai b menjadi =", b)

# eksponen (pangkat)
a = 5
print("\nnilai a =", a)

a **= 3
print("nilai a **= 3, nilai a menjadi =", a)


# bitwise

# OR
c = True
print("\nnilai c =", c)
c |= False
print("nilai c |= False, nilai c menjadi =", c)

c = False
print("\nnilai c =", c)
c |= False
print("nilai c |= False, nilai c menjadi =", c)

# AND
c = True
print("\nnilai c =", c)
c &= False
print("nilai c &= False, nilai c menjadi =", c)

c = False
print("\nnilai c =", c)
c &= False
print("nilai c &= False, nilai c menjadi =", c)

c = True
print("\nnilai c =", c)
c &= True
print("nilai c &= True, nilai c menjadi =", c)

# XOR
c = True
print("\nnilai c =", c)
c ^= False
print("nilai c ^= False, nilai c menjadi =", c)

c = False
print("\nnilai c =", c)
c ^= False
print("nilai c ^= False, nilai c menjadi =", c)

c = True
print("\nnilai c =", c)
c ^= True
print("nilai c ^= True, nilai c menjadi =", c)


# shifting

d = 0b0100
print("\nnilai d =", format(d, ('04b')))

d >>= 2
print("nilai d >>= 2, nilai b menjadi =", format(d, ('04b')))

d <<= 1
print("nilai d <<= 1, nilai b menjadi =", format(d, ('04b')))
