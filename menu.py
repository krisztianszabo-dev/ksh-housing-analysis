import time
from analyzer import HousingDataAnalyzer


def start_menu():
    my_analyzer = HousingDataAnalyzer("adatok.csv")
    menu_options = {
        "1": "Kiadott lakásépítési engedély",
        "2": "Épített lakás",
        "3": "Új és használt lakások összevont lakáspiaci árindexe, 2015 = 100%",
        "4": "Lakáspiaci tranzakció",
        "5": "Lineáris regresszió",
        "6": "Kiadott és épített lakások összevetve",
        "0": "Kilépés"
    }


    while True:
        print("\n--- KSH LAKÁSPIACI ADATFELDOLGOZÓ ---")
        for key , text in menu_options.items():
            print(f"{key}. {text}")

        choice = input("\n Adja meg a megtekinteni kívánt adatokhoz tartozó sorszámot!")


        if choice == "0":
            print("Kilépés..")
            time.sleep(1)
            print("Viszontlátásra!")
            time.sleep(1)
            break
        elif choice in ["1", "2", "3", "4"]:
            my_analyzer.tablazat_es_grafikon(menu_options[choice])
        elif choice == "5":
            my_analyzer.lin_regression()
        elif choice == "6":
            oszlop1 = menu_options["1"]
            oszlop2 = menu_options["2"]
            my_analyzer.kiadott_es_epitett(oszlop1, oszlop2)
        else:

            print("\n Hibás bevitel kérem használja a számokat 1 és 6 között vagy lépjen ki a 0 lenyomásával.")
            time.sleep(1)
