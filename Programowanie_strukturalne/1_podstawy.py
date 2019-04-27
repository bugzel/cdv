print("CDV")
print(2)

'''
komentarz w wielu liniach - BLOKOWY

'''

'''
#potegowanie - komentarz jednoliniowy

potega = 2 ** 10
print (potega)

#pobieranie danych z klawiatury

imie = input("Podaj imie: ")
#konkatenacja

print("Twoje imie podane z klawiatury: " + imie)
nazwisko = input("Podaj nazwisko: ")

#Twoje imie: ..., Twoje nazwisko: ...
print ("Twoje imie: " + imie + " Twoje naziwkos " + nazwisko)


print ("Podaj swoj wiek: ", end="")
wiek = input()
print("Twój wiek: " + wiek)

wiek1 = 30

print(type(wiek1))#int

#print("Twój wiek: " + wiek1)
print("Twój wiek:", wiek1)

nazwisko = "Kowalski"
pierwszyZnak = nazwisko[0]
print(pierwszyZnak)

dlugosc = len(nazwisko)
print(dlugosc)

ostatniZnak = nazwisko[len(nazwisko)-1]
print(ostatniZnak)

ostatniZnak = nazwisko[-1]
print(ostatniZnak)

'''

#konwersja

x = "5"
print(type(x))#str

x = int(x)
print(type(x)) #int

y = 4
print(type(y)) #int

y = y / 2
print(type(y)) #float
print(y)#2.0

nazwisko = "Kowalski"
print(nazwisko[0]) #K
print(nazwisko[0:3]) #Kow
print(nazwisko[-2]) #k
print(nazwisko[-2:]) #ki
print(nazwisko[:-2]) #Kowals
print(nazwisko[:-2:2]) #Kwl
