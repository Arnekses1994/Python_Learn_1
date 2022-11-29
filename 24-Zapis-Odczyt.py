file = open("countries_and_capitals.txt","w+")

# Argument "r" plik do zapisu
# Argumnt "w" plik do odczytu 
# Argument "w+" plik do odczytu i zapisu

countries_and_capitals = {'Poland': 'Warsaw',
'Czechia': 'Prague','Germany': 'Berlin'}

for country, capital in countries_and_capitals.items():
    file.write (country + "-" + capital + "\n")

file.close    

# Przykład zapisania pliku oraz jego odczytu

# Na końcu zapisujemy "file.close"

file = open ("countries_and_capitals.txt")

for line in file.readlines():
    print(line.strip())

file.close
# Przykład odczytania pliku z systemu oraz pokazania go w konsoli 