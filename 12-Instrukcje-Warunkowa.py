
light = input("Jakie jest światło? ( red , green, yellow ) ")

if light == 'red':
    print ("Czekaj !")
        
elif light == 'yellow':
    print ("Przygotuj się")
    
elif light == 'green':
    print ("Jedz")
    
else:     
    print ("Błedne dane")
    
        
# Funkcja else oznacza "jeśli" - jeśli jest inaczej
# podaje nam co ma byc dalej 

# Funkcja elif daje możliowść odpisania kolejnej zmiennej '''
# do zmiennej 

print("Jedz") if light == 'green' else print("Czekaj")

# Bardziej prosta forma gdy mamy TYLKO DWIE ZMIENNE







