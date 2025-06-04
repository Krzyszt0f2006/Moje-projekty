def nazwa_pliku():
    nazwa_pliku_do_pisania=input("Podaj nazwe pliku ktory chcesz stworzyc")+".txt"
    try:
        with open(nazwa_pliku_do_pisania,"w") as plik:
            while True:
                linia=input()
                if linia.lower()=="koniec":
                    break
                plik.write(linia + "\n")
        print(f"Dane zostały zapisane do pliku {nazwa_pliku_do_pisania}.")
    except:
        print("błąd")