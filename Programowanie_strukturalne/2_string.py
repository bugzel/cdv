tekst = "Anna, paweł, julIA"

lista = tekst.split(", ")
print(tekst)
print(lista)
print(type(lista))

imie1 = lista[0]
imieDuze = imie1.upper()

imieMale = imie1.lower()
print(imieMale)

#sprawdzenie zawartosci
print("\nPodaj swoje nazwisko: ",end="")
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc) #True False

text1 = "\nJulia\n"
text2 = "Nowak"
print(text1 + text2)

text1 = text1.rstrip()
print(text1 + text2)
print(text1 + " " + text2)

#wszystkie wersje Pythona
text = "%s, Java i %s" % ("PHP", "Python")
print(text)

#nowzse wersje Pythona >2.6

text = "[1], Java i [0]".format("PHP", "Python")
print(text)

#help(text.replace)

new = text.replace("PHP", "C#")
print(new)

#wypisanie danych
rok = 2019
miesiac = "kwiecien"
dzien = 27
print("\nData: ", end="")
print(dzien,miesiac,rok)

print("nData: ", end="")
print(dzien,miesiac,rok,sep="-")


