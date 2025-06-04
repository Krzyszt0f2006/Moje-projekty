from selenium import webdriver
import time
import datetime
print("Podaj link do produktu na amazonie")
link_strony=input()
try:
    przegladarka = webdriver.Chrome()
    przegladarka.get(link_strony)
    pobierz_cene = przegladarka.find_element('css selector', 'span.a-price-whole')
    pobierz_grosze = przegladarka.find_element('css selector', 'span.a-price-fraction')
    #print(pobierz_grosze)
    #print(pobierz_cene)
    zlote=pobierz_cene.text
    grosze = pobierz_grosze.text
    cena = f"{zlote}"+","+f"{grosze}"
    #print(zlote)
    #print(grosze)
    print("Cena produktu to: ",cena)
    przegladarka.close()
    print("Czy zapisać cene do pliku?T/N")
    decyzja=input()
    decyzja=decyzja.lower()
    if decyzja=="t":
        try:
            nowy_plik = False
            nazwa_pliku = input("Podaj nazwę pliku") + ".txt"
            try:
                    with open(nazwa_pliku, "x") as tymczasowy:
                        print(f"Plik {nazwa_pliku} został utworzony.")
                        data_stworzenia = str(datetime.datetime.now())
                        # otwórz plik
                        with open(nazwa_pliku, "a+") as plik:
                            plik.write(("Data utworzenia pliku " + data_stworzenia + "\n"))
                            plik.write(cena+" Czas sprawdzenia: "+str(datetime.datetime.now())+"\n")
                            plik.close()
            except:
                with open(nazwa_pliku, "a+") as plik:
                    plik.write(cena + " Czas sprawdzenia: " + str(datetime.datetime.now()) + "\n")
                    plik.close()
        except:
            print("Wystąpił błąd.")
except:
    print('Wystąpił błąd')