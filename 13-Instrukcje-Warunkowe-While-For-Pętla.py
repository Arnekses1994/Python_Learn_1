
number = 2


while number < 6:
    print(number)
    number += 1
    
# Pętla będzie sie wykonywać dopuki będzie spełniony warunek
# W nieskończoność !!


for numer in range (1,10,2):
    if numer == 5:
        break
    print(numer)
    
# Pętla będzie sie wykonywać jedynie w danym zakresie jaki 
# okreslimy.Możemy także podać krok o ile bedzie zakreś liczbowy
# przeskakiwał - Trzecie miejsce w nawiasie (1,2,3) krok to 3

# Funkcja "break" kończy daną pętle gdy odnajdzie wskazaną wartość

for numerr in range (1,10,):
    if numerr == 5:
        continue
    print(numerr)

# Funkcja "continue" przyrywa aktualna pętla i przechodzi dalej


