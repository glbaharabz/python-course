print("# BAŞKENTLER BİLGİ YARIŞMASI # ")
print("1. soru :")
x = 0
a = ((input("Türkiye'nin başkenti hangi şehirdir? :"))).lower()
if a == "ankara":
    print("tebrikler doğru cevap verdiniz! 10 puan")
    x = x+10
else:
    print("yanlış cevap verdiniz. 0 puan Doğru cevap : Ankara ")

print("2.soru")
b= (input("İran'ın başkenti hangi şehirdir?")).lower()
if b == "tahran":
    print("tebrikler doğru cevap verdiniz! 10 puan")
    x = x+10
else:
    print("yanlış cevap verdiniz.0 puan .Doğru cevap : Tahran ")

print("3.soru")
c = (input("Japonya'nın başkenti hangi şehirdir?")).lower()
if c == "tokyo":
    print("tebrikler doğru cevap verdiniz! 10 puan")
    x = x+10
else:
    print("yanlış cevap verdiniz. 0 puan. Doğru cevap : Tokyo ")

print("4.soru")
d = (input("Suriye'nin başkenti hangi şehirdir? 10 puan")).lower()
if d == "şam":
    print("tebrikler doğru cevap verdiniz! 10 puan")
    x = x+10
else:
    print("yanlış cevap verdiniz. 0 puan. Doğru cevap : Şam ")

print("5.soru")
e = ((input("Kanada'nın başkenti hangi şehirdir? :"))).lower()
if e == "ottawa":
    print("tebrikler doğru cevap verdiniz! 10 puan")
    x = x+10
else:
    print("yanlış cevap verdiniz. 0 puan Doğru cevap : Ottawa")

print("6.soru")
f = ((input("Bulgaristan'ın başkenti hangi şehirdir? :"))).lower()
if f == "sofya":
    print("tebrikler doğru cevap verdiniz! 10 puan")
    x = x+10
else:
    print("yanlış cevap verdiniz. 0 puan Doğru cevap : Sofya ")

print("7.soru")
g = ((input("Bangladeş'in başkenti hangi şehirdir? :"))).lower()
if g == "dakka":
    print("tebrikler doğru cevap verdiniz! 10 puan")
    x = x+10
else:
    print("yanlış cevap verdiniz. 0 puan Doğru cevap : Dakka")

print("8.soru")
h = ((input("Irak'ın başkenti hangi şehirdir? :"))).lower()
if h == "bağdat":
    print("tebrikler doğru cevap verdiniz! 10 puan")
    x = x+10
else:
    print("yanlış cevap verdiniz. 0 puan Doğru cevap : Bağdat")

print("9.soru")
j = ((input("İtalya'nın başkenti hangi şehirdir? :"))).lower()
if j == "roma":
    print("tebrikler doğru cevap verdiniz! 10 puan")
    x = x+10
else:
    print("yanlış cevap verdiniz. 0 puan Doğru cevap : Roma")

print("10.soru")
k = ((input("Ürdün'ün başkenti hangi şehirdir? :"))).lower()
if k == "amman":
    print("tebrikler doğru cevap verdiniz! 10 puan")
    x = x+10
else:
    print("yanlış cevap verdiniz. 0 puan Doğru cevap : Amman")

if x > 50:
    print("TEBRİKLER BAŞARILI BİR YARIŞMA ÇIKARDINIZ!! PUANINIZ:",x)
else :
    print("BAŞARISIZ OLDUNUZ!! PUANINIZ:",x)
