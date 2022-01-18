# 1. menyambung string (concatenate)
NamaPertama = "aing"
NamaKedua = "D"
NamaTerakhir = "ganz"

NamaLengkap = NamaPertama +" "+ NamaKedua +"'"+ NamaTerakhir
print(NamaLengkap)

# 2. menghitung panjang
panjang = len(NamaLengkap)
print('panjang dari', NamaLengkap, '=', str(panjang), 'karakter')
print('panjang dari ' + NamaLengkap + ' = ' + str(panjang) + ' karakter')

# 3. operator untuk string

# mengecek apakah ada komponen 'char' atau 'string' pada string
d = "d"
status = d in NamaLengkap
print('huruf', "'" + d + "'", 'ada di', NamaLengkap, '=', str(status))

D = "D"
status = D in NamaLengkap
print('huruf', "'" + D + "'", 'ada di', NamaLengkap, '=', str(status))

d = "d"
status = d not in NamaLengkap
print('huruf', "'" + d + "'", 'tidak ada di', NamaLengkap, '=', str(status))

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing
print("index ke-0 :", NamaLengkap[0])
print("index ke-0 :" + NamaLengkap[0])
print("index ke-(-1) :", NamaLengkap[-1])
print("index ke-(-2) :", NamaLengkap[-2])
# ditambah 1
print("index ke-[0:4] :", NamaLengkap[0:4])
print("index ke-[3:7] :", NamaLengkap[3:7])
# selisih 2
print("index ke-(0,2,4,6,8,10) :", NamaLengkap[0:11:2])

# item paing kecil
print("paling kecil =", min(NamaLengkap))
# item paling besar
print("paling besar =", max(NamaLengkap))

# ascii
ascii_spasi = ord(" ")
print("ascii code untuk spasi =" + str(ascii_spasi))

ascii_a = ord("a")
print("ascii code untuk 'a' =", str(ascii_a))

ascii_117 = 117
print("char untuk ascii code 117 =" + chr(ascii_117))

ascii_97 = 97
print("char untuk ascii code 97 =", chr(ascii_97))

# 4. operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah huruf 'o' pada " + data + " = " + str(jumlah))