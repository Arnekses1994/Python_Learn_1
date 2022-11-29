
name = "Kamil"

print (name[0:3])

# Wpisujemy "0" ponieważ według python to pierwszy znak 
# wpisywany w tekscie - Tak jest kodowany

# Po : podajemy do jakiego znaku chcemy aby było podane

name1 = "Artur"
print (name1[0:4])

channel = "Jak nauczyć sie programować"
print (channel.split(" "))

# Ta funkcja rodziela słowa - .split

join_string = "-"
print (join_string.join(['Jak', 'nauczyć', 'sie', 'programownia']))

#Funkcja łaczaca słowa - .joint ['Podawane', 'Słowa']

print(name.startswith("K"))
print(name.startswith("k"))

# Sprawdza czy dana funckja ZACZYNA sie na litere - Wielkośc liter ma znaczenie

print(name.endswith('L'))
print(name.endswith('l'))

# Sprawdza czy dana funckja KOŃCZY sie na litere - Wielkośc liter ma znaczenie

print(name.rstrip("l"))
print(name.lstrip("K"))

# Funkcja pozwalajaca usuwanie znaków z słowa - Wielkośc ma znaczenie 
# rstrip - To prawa strona
# lstrip - To lewa strona

print(name.strip("a"))

# strip - samo bez "l" lub "r" usuwa każdy znak w słowie
# Ta funkcja może byc także używan do usuwania spacji !!!




