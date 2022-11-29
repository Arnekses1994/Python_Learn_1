
countries_and_capitals = {"Poland": "Warsaw", "Germany": "Berlin"}
countries_and_capitals['Czech'] = "Prague"

# Dodawnie do słownik kolejnych danych ! - Czech-Prague

        #print(countries_and_capitals)



for countries in countries_and_capitals.keys():
    print(countries)
    
    
# Wyświetlenie klucza danego słownika "keys"

print("---")

for capitals in countries_and_capitals.values():
    print(capitals)
    
print("---")

# Wyświetlenie wartości danego słownika "values"

for country, capital in countries_and_capitals.items():
    print(country + "-" + capital)
    
print("---")

# Wyświetlenie danych z słownika razem "items"

print(countries_and_capitals["Poland"])
print(countries_and_capitals.get("USA"))

print("---")



print(countries_and_capitals.setdefault("USA","Washington DC"))
print(countries_and_capitals)

print("---")

# Wyszukanie konkretego klucza dwoma metodami

# - Podstawowa jeśli klucz będzie błedny wyrzuci nam błąd
# - Dodatkowa "get" jeśli klucz będzie błedy wyrzuci nam jedynie infomacje
# - "None"

# Metoda "setdefault" - Pobiera wartośc z klucza i wtedy wstawia tą wartość
# do słownika - Gdy klucz sie powtarza to nie zostanie wyświetlony !!!

print(countries_and_capitals.pop("Czech"))
print("---")
print(countries_and_capitals)

print("---")

# Metoda "pop" usuwa daną wartośc klucza z słownika

print(countries_and_capitals.popitem())

print("---")

# Metoda "popitem" usuwa ostatnia dodaną informcje do słownik 

if "USA" in countries_and_capitals.keys():
    print("Znaleziono brawo !")
else:
    print("Nie ma")


# Metoda na znalezienie danych w słowniku oraz wyświeltenie informacji
