# Sayısal(Aritmetik Operatörler)

# Ekleme (+)
# Örnek: x + y
x = 5
y = 3
print(x + y) # 8 çıktısını verir.

# Çıkarma (-)
# Örnek: x - y
x = 5
y = 3
print(x - y) # 2 çıktısını verir.

# Çarpma (*)
# Örnek: x * y
x = 5
y = 3
print(x * y) # 15 çıktısını verir.

# Bölme (/)
# Örnek: x / y
x = 12
y = 3
print(x / y) # 4 çıktısını verir.

# Kalan/Modulus (%)
# Örnek: x % y
x = 5
y = 2
print(x % y) # 1 çıktısını verir.

# Üs (**)
# Örnek: 	x ** y
x = 2
y = 5
print(x ** y) #2*2*2*2*2 ile eşdeğerdir. 32 çıktısını verir.

# Bölüm (//)
# Örnek: x // y
x = 15
y = 2
print(x // y) # 7 çıktısını verir. Sonucu en yakın tam sayıya yuvarlar.

#____________________________________________________________________
# Atama Operatörleri

# =
x = 5 # x, 5'e eşit.
print(x)

# +=
x = 5
x += 3 # x'e 3 ekle.
print(x)

# -=
x = 5
x -= 3 # x'ten 3 çıkar.
print(x)

# *=
x = 5
x *= 3 # x'i 3'le çarp.
print(x)

# /=
x = 5
x /= 3 # x'i 3'e böl.
print(x)

# %=
x = 5
x%=3 # x'in 3 ile bölümünden kalan.
print(x)

# //=
x = 5
x//=3 # 5'i 3'e böl ve bölümü en yakın tam sayıya yuvarla.
print(x)

# **=
x = 5
x **= 3 # 5 üssü 3
print(x)

# &=
x = 5
x &= 3 # Bitwise AND uygular ve değeri sol işlenene atar.
print(x)

# |=
x = 5
x |= 3 # Bitwise OR uygular ve değeri sol işlenene atar.
print(x)

# ^=
x = 5
x ^= 3 # Bitwise XOR uygular ve değeri sol işlenene atar.
print(x)

# >>=
x = 5
x >>= 3 # Bitwise sağa kaydırma uygular ve değeri sol işlenene atar.
print(x)

# <<=
x = 5
x <<= 3 # Bitwise sola kaydırma uygular ve değeri sol işlenene atar.
print(x)

#____________________________________________________________________
# Karşılaştırma Operatörleri

# Eşit (==)
# Örnek: x == y
x = 5
y = 3
print(x == y) # false çıktısını verecek çünkü x ve y birbirine eşit değil.

# Eşit Değildir (!=)
# Örnek: x != y
x = 5
y = 3
print(x != y) # true çıktısını verecek çünkü x ve y birbirine eşit değil.

# Büyüktür (>)
# Örnek: x > y
x = 5
y = 3
print(x > y) # true çıktısını verecek çünkü x, y'den büyük.

# Küçüktür (<)
# Örnek: x < y
x = 5
y = 3
print(x < y) # false çıktısını verecek çünkü x, y'den küçük değil.

# Büyük Eşittir (>=)
# Örnek: x >= y
x = 5
y = 3
print(x >= y) # true çıktısını verecek çünkü x, y'den büyük veya eşittir.

# Küçük Eşittir (<=)
# Örnek: x <= y
x = 5
y = 3
print(x <= y) # false çıktısını verecek çünkü x, y'ye eşit veya ondan küçük değil.
