# operasi logika/boolean atau tabel kebenaran
# NOT, OR, AND, XOR

# NOT
print('\n===== NOT =====')
a = False
c = not a
print('data a =', a)
print('NOT')
print('data c =', c)

# OR (jika salah satu atau lebih bernilai 'TRUE', maka hasilnya 'TRUE')
print('\n===== OR =====')
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, ' =', c)
a = True
b = False
c = a or b
print(a, ' OR', b, '=', c)
a = True
b = True
c = a or b
print(a, ' OR', b, ' =', c)

# AND (jika salah satu atau lebih bernilai 'FALSE', maka hasilnya 'FALSE')
print('\n===== AND =====')
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = True
c = a and b
print(a, 'AND', b, ' =', c)
a = True
b = False
c = a and b
print(a, ' AND', b, '=', c)
a = True
b = True
c = a and b
print(a, ' AND', b, ' =', c)

# XOR (jika dua nilai sama maka 'FALSE', jika dua nilai berbeda maka 'TRUE')
print('\n===== XOR =====')
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, ' =', c)
a = True
b = False
c = a ^ b
print(a, ' XOR', b, '=', c)
a = True
b = True
c = a ^ b
print(a, ' XOR', b, ' =', c)