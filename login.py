mail="mustafasona28@gmail.com"
sifre="abcd"

m=input("Mailinizi daxil edin: ")
s=input("Şifrənizi daxil edin: ")
if m != mail:
  print("Hesab tapılmadı")

if m == mail and s != sifre:
  print("Şifrə yanlışdır")

if m == mail and s == sifre:
  print("Xoş gəldiniz!")