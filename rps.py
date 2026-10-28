oyunçu1=input("daş, kağız yoxsa qayçı? ")
oyunçu2=input("daş, kağız yoxsa qayçı? ")
if oyunçu1==oyunçu2:
    print("Heç-heçə!")
if oyunçu1=="daş" and oyunçu2=="qayçı":
    print("Oyunçu 1 qazandı!")
if oyunçu1=="qayçı" and oyunçu2=="daş":
    print("Oyunçu 2 qazandı!")
if oyunçu1=="qayçı" and oyunçu2=="kağız":
    print("Oyunçu 1 qazandı!")  
if oyunçu1=="kağız" and oyunçu2=="qayçı":
    print("Oyunçu 2 qazandı!")  
if oyunçu1=="kağız" and oyunçu2=="daş":
    print("Oyunçu 1 qazandı!")
if oyunçu1=="daş" and oyunçu2=="kağız":
    print("Oyunçu 2 qazandı!")
if oyunçu1!="daş" and oyunçu1!="kağız" and oyunçu1!="qayçı" or oyunçu2!="daş" and oyunçu2!="kağız" and oyunçu2!="qayçı":
    print("Xahiş olunur düzgün seçim edin!")
