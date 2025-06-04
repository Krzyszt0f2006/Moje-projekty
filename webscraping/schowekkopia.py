import datetime
nowy_plik=False
nazwa_pliku=input("Podaj nazwę pliku")+".txt"
try:
    #Sprawdzenie czy plik istnieje
    try:
        with open(nazwa_pliku, "x") as tymczasowy:
            #gdy x sprawdzi że plik istnieje to wysyła error
            #Gdy plin nie istnieje, stwórz nowy
            print(f"Plik {nazwa_pliku} został utworzony.")
            data_stworzenia=str(datetime.datetime.now())
            #otwórz plik
            with open(nazwa_pliku, "a+") as plik:
                #a+ dodaje linijki na koniec pliku
                print("Gdy skończysz wpisywanie, napisz koniec by zakończyc pisanie")
                plik.write(("Data utworzenia pliku " + data_stworzenia + "\n"))
                #"\n" nowa linia
                while True:
                    linia=input()
                    if linia.lower() == "koniec":
                        break
                    plik.write(linia+"\n")
                decyzja_zrodlo=input("Dodać źródło?(t/n):")
                if decyzja_zrodlo.lower() == "t":
                    zrodlo=input("Podaj je:")
                    plik.write("Źródła:/"+zrodlo+"/\n")
            print(f"Dane zostały zapisane do pliku {nazwa_pliku}.")
    except:
        #wybierz czy edytować  plik
        decyzja=input(f"Plik {nazwa_pliku} już istnieje.Chcesz go edytować?(t/n): ")
        #decyzja=input("Plik {nazwa_pliku} już istnieje.Chcesz go edytować?(t/n): ")
        if decyzja.lower()!="t":
            print("Wybrałeś  nie edytować pliku")
        else:
            #otwórz w a+
            with open(nazwa_pliku,"a+") as plik:
                print("Gdy skończysz wpisywanie, napisz koniec by zakończyc pisanie")
                while True:
                    linia=input()
                    if linia.lower()=="koniec":
                        break
                    plik.write(linia+"\n")
                decyzja_zrodlo=input("Dodać źródło?(t/n):")
                if decyzja_zrodlo.lower()=="t":
                    zrodlo=input("Podaj je:")
                    plik.write("Źródła:/"+zrodlo+"/\n")
            print(f"Dane zostały zapisane do pliku {nazwa_pliku}.")
            #print("Dane zostały zapisane do pliku {nazwa_pliku}.")
except:
    print("błąd")
