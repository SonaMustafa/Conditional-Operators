mesafe=float(input("Məsafəni daxil edin: "))
saat=int(input("Saatı daxil edin: (00-23)"))
qiymet=2+(mesafe*0.80)
if saat>=23 or saat<6:
    qiymet=qiymet*1.2
if qiymet<3:
    qiymet=3
print("Gediş haqqı: ",qiymet,"AZN")