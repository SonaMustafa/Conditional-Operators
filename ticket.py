yas=int(input("Yaşınızı daxin edin: "))
telebe= input("Telebe olub olmadiginizi daxil edin (beli/xeyr): ")
if yas<7:
    print("Bilet pulsuzdur")
else: 
    if yas>65:  
        print("Bilet 4 AZN-dir")
    else:
        if telebe=="beli":
            print("Bilet 5 AZN-dir")
        else:
            print("Bilet 8 AZN-dir")