countires_information = {}
countires_information["Polska"] = ("Warszawa", 37.97)
countires_information["Niemcy"] = ("Berlin", 83.02)
countires_information["Słowacja"] = ("Bratysława", 5.45)

def show_country_info(country):
    countires_information = countires_information.get(country)

    print ( )
    print (country)
    print ("----------")
    print ("Stolica:" + countires_information[0])
    print ("Liczba mieszkańców (mln):" + str(countires_information[1]))

for country in countires_information.keys():
    print (country)
    
country = input("Informacje o jakim kraju chcesz wyświetlic: ")
show_country_info (country)
# countires_information = countires_information.get(country)





