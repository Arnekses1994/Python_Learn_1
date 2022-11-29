
names_set = set()

names_set.add("Kamil")
names_set.add("Dominik")

names_set2={"Mariusz","Tytus","Kamil"}

#  names_set.update(names_set2)

names_set3 = names_set.union(names_set2)

names_set4 = names_set.difference(names_set2)

names_set5 = names_set.intersection(names_set2)

# names_set.clear()

for name in names_set3:
    print(name)

print("---")    
    
for name in names_set:
    print(name)

print("---")   
    
for name in names_set4:
    print(name)
    
print("---")   

for name in names_set5:
    print(name)
    
print("---") 
    
# Nie można połączyc dwóch rodzajów struktur danych - Mozna to ominąć
# Stosując w danych "union"

# Funkcja "update" dodaje cos do istniejacego seta

# Można także sprawdzić różnice między setami opcja "difference"

# Można także sprawdzic czesci wspolne miedzy setami opcja "intersection

# Można także wyczyscic set metodą "clear"



