# casting = merubah dari satu tipe data ke tipe data lain
# tipe data: string, integer, float, boolean

## integer
print("====INTEGER====")
data_int=9
print("data=", data_int, "tipe=", type(data_int))

data_float=float(data_int)
data_str=str(data_int)
data_bool=bool(data_int) #akan false jika nilai int=0
print("data=", data_float, "tipe=", type(data_float))
print("data=", data_str, "tipe=", type(data_str))
print("data=", data_bool, "tipe=", type(data_bool))

## float
print("====FLOAT====")
data_float=9.6
print("data=", data_float, "tipe=", type(data_float))

data_int=int(data_float) #akan dibulatkan ke bawah
data_str=str(data_float)
data_bool=bool(data_float) #akan false jika nilai float=0
print("data=", data_int, "tipe=", type(data_int))
print("data=", data_str, "tipe=", type(data_str))
print("data=", data_bool, "tipe=", type(data_bool))

## boolean (true/false)
print("====BOOLEAN====")
data_bool=False
print("data=", data_bool, "tipe=", type(data_bool))

data_int=int(data_bool)
data_str=str(data_bool)
data_float=float(data_bool)
print("data=", data_int, "tipe=", type(data_int))
print("data=", data_str, "tipe=", type(data_str))
print("data=", data_float, "tipe=", type(data_float))

## string
print("====STRING====")
data_str="10"
print("data=", data_str, "tipe=", type(data_str))

data_int=int(data_str) 
data_float=float(data_str)
data_bool=bool(data_str) 
print("data=", data_int, "tipe=", type(data_int))
print("data=", data_float, "tipe=", type(data_float))
print("data=", data_bool, "tipe=", type(data_bool))