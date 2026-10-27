ceki=float(input("Çəkini daxil edin: "))
biletNovu=input("Bilet novu daxil edin (Ekonom/Business): ")
if biletNovu=="Ekonom":
    if ceki<=23:
        print("Əlavə ödəniş yoxdur.")
    else:
        if ceki>23 and ceki<=32:  
            print("Əlavə ödəniş: 30 AZN")
        else:
            print("Heç bir biletlə qəbul edilmir.")
else:
    if biletNovu=="Business":
        if ceki<=32:
            print("Əlavə ödəniş yoxdur.")
        else:
            print("Heç bir biletlə qəbul edilmir.")
    else:
        print("Bilet novunu düzgün daxil edin.")