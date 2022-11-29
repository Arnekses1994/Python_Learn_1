names_set = {"Kamil", "Mariusz","Kamil" }

print (names_set)


    # Struktura danych set - nie pozwala na powtarzanie się danych,
    # Zawsze jest nie mutowalny ! elemty nie są uporządkowane !!


names_set2 = set()

    # Stworzenie pustego setattr

names_set2.add("Kamil" )
names_set2.add("Artur" )
names_set2.add("Daniel")

    # Dodawanie do pustego seta !
    
names_set2.remove("Kamil")

    # Usuwanie z seta danych - "Musi znajdować sie w zbiorze set
    # inaczej zostanie wyrzucony bład !!!"

names_set2.discard("Artur")

    # Usuwanie z seta danych - 2 "Jeśli podamy nieistniejacy obiekt
    # nic sie nie wydarzy"
    
print(names_set2)    

    # Nie można wyswietlic konkretnych danych w set
    
    
