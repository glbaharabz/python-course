x = input("isminizi giriniz :")
a = int(input("ara sınav notunuz:"))
b = int(input("proje notunuz:"))
c = int(input("final notunuz:"))
d = (a*0.3 + b*0.3 + c*0.4)
print("gecme notunuz :", d )

gecme_notları = {x :d}

x = input("isminizi giriniz :")
a = int(input("ara sınav notunuz:"))
b = int(input("proje notunuz:"))
c = int(input("final notunuz:"))
d = (a*0.3 + b*0.3 + c*0.4)
print("gecme notunuz :", d )

gecme_notları2 = gecme_notları | {x :d}

x = input("isminizi giriniz :")
a = int(input("ara sınav notunuz:"))
b = int(input("proje notunuz:"))
c = int(input("final notunuz:"))
d = (a*0.3 + b*0.3 + c*0.4)
print("gecme notunuz :", d )

gecme_notları3 =gecme_notları2 | {x :d}

x = input("isminizi giriniz :")
a = int(input("ara sınav notunuz:"))
b = int(input("proje notunuz:"))
c = int(input("final notunuz:"))
d = (a*0.3 + b*0.3 + c*0.4)
print("gecme notunuz :", d )

gecme_notları4 =gecme_notları3 | {x :d}

x = input("isminizi giriniz :")
a = int(input("ara sınav notunuz:"))
b = int(input("proje notunuz:"))
c = int(input("final notunuz:"))
d = (a*0.3 + b*0.3 + c*0.4)
print("gecme notunuz :", d )

gecme_notları5 =gecme_notları4 | {x :d}


t = list(gecme_notları5.values())
t.sort()
t.reverse()
print(t)


