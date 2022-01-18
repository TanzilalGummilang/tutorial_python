# diketahui:
a=10
b=3

# operasi penambahan +
hasil=a+b
print(a,"+",b,"=",hasil)

#operasi pengurangan -
hasil=a-b
print(a,"-",b,"=",hasil)

# operasi perkalian *
hasil=a*b
print(a,"*",b,"=",hasil)

# operasi pembagian /
hasil=a/b
print(a,"/",b,"=",hasil)

# operasi eksponen (pangkat) **
hasil=a**b
print(a,"**",b,"=",hasil)

# operasi modulus &
hasil=a%b
print(a,"%",b,"=",hasil)

# operasi floor division
# (pembagian jika hasilnya desimal akan dibulatkan ke bawah) //
hasil=a//b
print(a,"//",b,"=",hasil)

# prioritas operasi / operational precedence
"""
    1. ()
    2. eksponen **
    3. * / ** & // (sama aja)
    4. + -
"""

x=3
y=2
z=4

hasil=x**y*z+x/y-y%z//x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = (x + y) * z
print('(',x,'+',y,')','*',z,'=',hasil)