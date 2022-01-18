# misal: a=10, a adalah variabel dengan nilai 10

# tipe data: angka satuan tanpa koma (integer)
data_integer=1
print("data:", data_integer)
print("bertipe:", type(data_integer)) 
#atau
print("atau")
print("data:", data_integer, "bertipe:", type(data_integer))

print("lalu")

# tipe data: angka pake koma (float)
data_float=1.5
print("data:", data_float)
print("bertipe:", type(data_float))
#atau
print("atau")
print("data:", data_float, "bertipe:", type(data_float))

print("lalu")

# tipe data: kumpulan karakter (string)
data_string="balmon"
print("data:", data_string)
print("bertipe:", type(data_string))
#atau
print("atau")
print("data:", data_string, "bertipe:", type(data_string))

print("lalu")

# tipe data: biner true/false (boolean)
data_bool=False
print("data:", data_bool)
print("bertipe:", type(data_bool))
#atau
print("atau")
print("data:", data_bool, "bertipe:", type(data_bool))

## tipe data khusus

# bilangan kompleks
data_complex=complex(5,4)
print("data:", data_complex)
print("bertipe:", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double
data_c_double=c_double(10.5)
print("data:", data_c_double)
print("bertipe:", type(data_c_double))