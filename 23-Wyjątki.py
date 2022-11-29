countries_and_capitals = {'Polnad':'Warsaw',
'Czechia':'Prague','Germany':'Berlin'}


# W bloku tray podajemy gdzie może pojawić się błąd

try:
    print(countries_and_capitals['USA'])
except KeyError:
    print ("Klucz nie został znaleziony")
    
print ("Test")
    
    
# W bloku except podajemy co dalej ma sie stać 
# Tutaj warto dodać typ błedu - KeyError

# W tym miejscu kończy sie aplikacja !!!
# Jest to błąd i dalej kod juz nie działa

try:
    print(2/0)
except ZeroDivisionError:
    print("Nie można dzielic przez zero")
finally:
    print("Wykonuje sie zawsze")
    
# Blok "finally" wykona sie zawsze 
# bez różnicy czy będzie bład czy też nie    
    

# Tutaj była próba dzielenia przez 0 oraz 
# Pokazanie innego typu błedu oraz opisanie go przy
# Przy pozycji except


