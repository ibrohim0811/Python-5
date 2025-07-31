# import sys
pass1 = print("Hozir sizning yangi login va parolingizni taqdim etamiz! ")
ism = input("Ismingizni kiriting: ")
last_name = input("Familiyangizni kiriting: ")
yil = int(input("tug'ilgan yilingizni kiriting: "))
login = ism
parol = yil
yosh = 2025 - yil
if yosh > 18:
    print("siz voyaga yetgansiz!")
else:
    print("Siz voyaga yetmagansiz! , bu davom etishimizga halaqit bermaydi!")

print(f"yodda tuting parol:{parol} login:{login}")
son1 = int(input("taxminiy 1ta son kiriting: "))
if son1 > 0:
    print("siz kiritgan son musbat")
else:
    print("Siz kiritgan son manfiy")

if son1 == 0:
    print("siz kiritgan son 0 ga teng")
else:
    print(" ")

check1 = input("Sizga berilgan loginni kiriting: ")
check2 = int(input("Sizga berilgan parolni kiriting: "))
if check1 == login and check2 == parol:
    print("Login va parol to'g'ri , qabul qilindi!")
else:
    print("Xatolik! login yoki parol xato tekshirib qaytadan urinib ko'ring!")

random = int(input("1 dan 10 gacha baholang: "))
if random < 10 :
    print("Hmmm , yaxshi emas tushunarli!")
else:
    print(f"Baholash tizimi alo! , Rahmat {ism}!")