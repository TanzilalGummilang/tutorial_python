data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string
'''
    1. menggunakan single quote '...'
    2. menggunakan double quote "..."
'''

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print('"salam sejahtera"')
print("'salam sejahtera'")
print('"',"sekarang hari jum'at",'"')


# 2. menggunakan tanda \

# membuat tanda ' jadi string
print('"mari shalat jum\'at"')
print('g\'day, isn\'t?')

# backslash
print("C:\\user\\aing\\")

# tab
print("aing \tmaneh, ngajauhan")

# backspace
print("aing \bmaneh, ngadekeutan")

# newline
print("baris pertama. \nbaris kedua.") # LF -> line feed (unix, macos, linux)
print("baris pertama. \rbaris kedua.") # CR -> carriage return (commodore, acorn, lisp)
print("baris pertama. \r\nbaris kedua.") # CRLF (windows)

# hati-hati!
print("C:\new folder") # SALAH
# menggunakan RAW string
print(r"C:\new folder\aing") 

# multiline literal string
print("""
Nama    : Aing
Kelas   : teu sakola
""")

# multiline literal string dan RAW
print(r"""
Nama    : Aing
Kelas   : teu sakola\new normal
""")