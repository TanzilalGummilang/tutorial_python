# konversi termperatur

# konversi celcius ke satuan lain

print("\nKonversi Temperatur CELCIUS\n")

celcius = float(input("masukan suhu dalam celcius :"))
print("suhu adalah", celcius, "C")

# celcius ke reamur
reamur = (4/5) * celcius
print("suhu dalam Reamur =", reamur, "R")

# celcius ke fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam Fahrenheit =", fahrenheit, "F")

# celcius ke kelvin
kelvin = celcius + 273
print("suhu dalam Kelvin =", kelvin, "K")