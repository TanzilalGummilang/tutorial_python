# operator dalam bentuk menthods


## merubah case dari string

# merubah semua ke UPPERCASE
salam = "bro!"
print("normal : " + salam)
print("upper : " + salam.upper())
# atau
salam = salam.upper()
print("upper : " + salam)

# merubah ke LOWERCASE
alay = "eLu KeCe bAn9EtzzZZz"
print("normal :" + alay)
print("lower :" + alay.lower())

## pengecekan dalam 'isX' methods

# pengecekan upper dan lower
salam = "sist?"
apakah_lower = salam.islower() # hasilnya akan bool
print(salam + " apakah menggunakan lower? " + str(apakah_lower)) 
apakah_upper = salam.isupper() # hasilnya akan bool
print(salam + " apakah menggunakan upper? " + str(apakah_upper))

saya = "aing"
print("kata", saya, "apakah memakai lower?", saya.islower())
print("kata", saya, "apakah memakai upper?", saya.isupper())

# isalpha() = mengecek semuanya huruf saja
juta10 = "10.000.000 Rupiah"
print(juta10, "is alpha =", juta10.isalpha())
juta = "juta"
print(juta, "is alpha =", juta.isalpha())

# isalnum() = huruf dan angka
juta10 = "10000000Rupiah"
print(juta10, "is alpha =", juta10.isalnum())

# isdecimal() = angka saja
satuduatiga = "123"
print(satuduatiga, "is decimal =", satuduatiga.isdecimal())

# isspace() = spasi, tab, newline(\n)
spasi = "satu dua tiga"
print(spasi, "is space =", spasi.isspace())

# istitle() = semua kata dimulai huruf besar
judul = "The Mentalist"
print(judul, "is title =", judul.istitle())
judul = "The mentalist"
print(judul, "is title =", judul.istitle())
judul = "Red Rose's" # pake kutip akan false
print(judul, "is title =", judul.istitle())

## pengecekan komponen startswith() dan endswith()
cek_starts = "Timo Werner".startswith("Timo") # harus spesifik
print("startswith = " + str(cek_starts))

cek_ends = "Kai Havertz"
print(cek_ends, "endswith =", cek_ends.endswith("Havertz")) # harus spesifik

## penggabungan komponen join() split()
pisah = ['kamu', 'sayang', 'aku']
gabung = " ".join(pisah)
print(pisah)
print(gabung)
gabung = " <3 ".join(pisah)
print(gabung)

gabung = "kamu <3 sayang <3 aku"
print(gabung.split(' <3 '))

## alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,"=")
print("'"+tengah+"'")

# menghilangkan -> strip()
tengah = tengah.strip("=")
print("'"+tengah+"'")

kanan = kanan.strip()
print("'"+kanan+"'")

