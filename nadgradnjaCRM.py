
stranke={}
stevilo_strank=0
stevilo_kontaktov=0
stevilo_aktivnosti=0
stevilo_pogodb=0
deluje=True
while (deluje==True):
    izbira=input("Vnesite 1 za DODAJANJE STRANK, 2 za IZPIS PODATKOV STRANK, 3 za IZBRIS STRANK, 4 za UREJANJE PODATKOV STRANK ali pa za 5 ISKANJE PODATKOV O STRANKAH: ")

#DODAJANJE STRANK
    if (izbira=="1"):
        podatki_o_stranki=input("Vnesi podatke stranke (primer: naziv; maticna_stevilka; naslov): ")
        naziv, maticna_stevilka, naslov = [x.strip() for x in podatki_o_stranki.split(";") or podatki_o_stranki.split(",")]
                                           
        nova_stranka = {
            "id": stevilo_strank+1 ,
            "naziv": naziv,
            "maticna_stevilka": maticna_stevilka,
            "naslov": naslov,
            }
        
        stranke[naziv] = nova_stranka
        stevilo_strank +=1

        dodajanje_kontakta = input("Pritisnite 1, če bi radi DODALI KONTAKT te osebe. Drugače pritisnite katerikoli drugi gumb: ")
        stranke[naziv]["kontakti"] = []
        while (dodajanje_kontakta=="1"):
            podatki_o_kontaktu = input("Vnesi podatke kontakta (primer: ime in priimek; email; telefonska stevilka): ")
            ime_in_priimek, email, telefonska_stevilka = [x.strip() for x in podatki_o_kontaktu.split(";") or podatki_o_kontaktu.split(",")]

            nov_kontakt = {
                "id_kontakta": stevilo_kontaktov + 1,
                "ime_in_priimek": ime_in_priimek,
                "email": email,
                "telefonska_stevilka": telefonska_stevilka
            }
               
            stranke[naziv]["kontakti"].append(nov_kontakt)
            stevilo_kontaktov = stevilo_kontaktov + 1
            nadaljevanje_dodajanja_kontaktov=input("Pritisnite 1, če želite DODATI ŠE EN KONTAKT. Drugače pritisnite katerikoli drugi gumb: ")
            if not (nadaljevanje_dodajanja_kontaktov == "1"):
                dodajanje_kontakta=""
        


        dodajanje_aktivnosti = input("Pritisnite 1, če bi radi DODALI AKTIVNOST, ki jo delaš za stranko. Drugače pritisnite katerikoli drugi gumb: ")
        stranke[naziv]["aktivnosti"] = []
        while (dodajanje_aktivnosti=="1"):
            podatki_o_aktivnosti = input("Vnesi podatke aktivnosti (primer: ime aktivnosti; opis aktivnosti; tip aktivnosti): ")
            ime_aktivnosti, opis_aktivnosti, tip_aktivnosti = [x.strip() for x in podatki_o_aktivnosti.split(";") or podatki_o_aktivnosti.split(",")]

            nova_aktivnost = {
                "id_aktivnosti": stevilo_aktivnosti + 1,
                "ime_aktivnosti": ime_aktivnosti,
                "opis_aktivnosti": opis_aktivnosti,
                "tip_aktivnosti": tip_aktivnosti
            }
               
            stranke[naziv]["aktivnosti"].append(nova_aktivnost)
            stevilo_aktivnosti = stevilo_aktivnosti+ 1
            nadaljevanje_dodajanja_aktivnosti=input("Pritisnite 1, če želite DODATI ŠE ENO AKTIVNOST. Drugače pritisnite katerikoli drugi gumb: ")
            if not (nadaljevanje_dodajanja_aktivnosti == "1"):
                dodajanje_aktivnosti=""



        
        dodajanje_pogodb = input("Pritisnite 1, če bi radi DODALI POGODBE, ki jo imaš z stranko. Drugače pritisnite katerikoli drugi gumb: ")
        stranke[naziv]["pogodbe"] = []
        while (dodajanje_pogodb=="1"):
            podatki_o_pogodbah = input("Vnesi podatke pogodbe (primer: ime pogodbe; datum začetka; datum konca): ")
            ime_pogodbe, datum_zacetka, datum_konca = [x.strip() for x in podatki_o_pogodbah.split(";") or podatki_o_pogodbah.split(",")]

            nova_pogodba = {
                "id_pogodbe": stevilo_pogodb + 1,
                "ime_pogodbe": ime_pogodbe,
                "datum_zacetka": datum_zacetka,
                "datum_konca": datum_konca
            }
               
            stranke[naziv]["pogodbe"].append(nova_pogodba)
            stevilo_pogodb = stevilo_pogodb + 1
            nadaljevanje_dodajanja_pogodb=input("Pritisnite 1, če želite DODATI ŠE ENO POGODBO. Drugače pritisnite katerikoli drugi gumb: ")
            if not (nadaljevanje_dodajanja_pogodb == "1"):
                dodajanje_pogodb=""


#IZPIS PODATKOV STRANKE
    elif (izbira=="2"):
        izpis_izbira=input("Vnesi 1, če želiš IZPISATI VSE STRANKE ali pa 2 če želiš IZPIS ZA DOLOČENO STRANKO: ")
        if (izpis_izbira=="1"):
            for id_stranke, podatki in stranke.items():
                print(f"ID: {id_stranke} → {podatki}")
        
        elif(izpis_izbira=="2"):
            izpis_izbira_id=input("Vnesi naziv stranke, ki si jo želiš pogledati: ")
            izbira_zelenih_podatkov=input( "1 = VSE PODATKE, 2 = SAMO KONTAKTE, 3 = SAMO AKTIVNOSTI, 4 = SAMO POGODBE: ")
            #Izpis strank
            if izbira_zelenih_podatkov=="1" :
                print(stranke[izpis_izbira_id])
            #Izpis kontaktov
            elif izbira_zelenih_podatkov == "2":
                print(stranke.get(izpis_izbira_id, {}).get("kontakti"))
            #Izpis aktivnosti
            elif izbira_zelenih_podatkov == "3":
                print(stranke.get(izpis_izbira_id, {}).get("aktivnosti"))
            #Izpis pogodb
            elif izbira_zelenih_podatkov == "4":
                print(stranke.get(izpis_izbira_id, {}).get("pogodbe"))

            else:
                print("Vnesli ste neveljavno izbiro. Prosimo poskusite ponovno.")

        else:
            print("Vnesli ste neveljavno izbiro. Prosimo poskusite ponovno.")


#IZBRIS PODATKOV STRANKE
    elif (izbira=="3"):
        izbris_izbira=input("Vnesi 1, če želiš IZBRISATI VSE STRANKE ali 2, če želiš IZBRISATI DOLOČENE PODATKE PRI DOLOČENI STRANKI: ")
        if izbris_izbira=="1":
            stranke={}
        elif izbris_izbira=="2":
            izbris_izbira_id=input("Vnesi NAZIV STRANKE pri kateri želiš NEKAJ IZBRISATI: ")
            izbris_zelenih_podatkov=input( "1 = VSE PODATKE, 2 = SAMO DOLOČENE KONTAKTE, 3 = SAMO DOLOČENE AKTIVNOSTI, 4 = SAMO DOLOČENE POGODBE: ")
            #Brisanje strank
            if izbris_zelenih_podatkov=="1":
                del stranke[izpis_izbira_id]
            #Brisanje kontaktov
            elif izbris_zelenih_podatkov=="2":
                print(stranke[izpis_izbira_id]["kontakti"])
                izbira_izbrisa_id=int(input("Vnesi id kontakta, ki ga želiš izbrisati: "))
                del stranke[izpis_izbira_id]["kontakti"][izbira_izbrisa_id]
            #Brisanje aktivnosti
            elif izbris_zelenih_podatkov=="3":
                print(stranke[izpis_izbira_id]["aktivnosti"])
                izbira_izbrisa_id=int(input("Vnesi id aktivnosti, ki ga želiš izbrisati: "))
                del stranke[izpis_izbira_id]["aktivnosti"][izbira_izbrisa_id]
            #Brisanje pogodb
            elif izbris_zelenih_podatkov=="4":
                print(stranke[izpis_izbira_id]["pogodbe"])
                izbira_izbrisa_id=int(input("Vnesi id pogodbe, ki ga želiš izbrisati: "))
                del stranke[izpis_izbira_id]["pogodbe"][izbira_izbrisa_id]

            else:
                print("Vnesli ste neveljavno izbiro. Prosimo poskusite ponovno.")

        else:
            print("Vnesli ste neveljavno izbiro. Prosimo poskusite ponovno.")




#UREDBA PODATKOV STRANKE
    elif (izbira=="4"):
        uredba_izbira_id=input("Vnesi NAZIV STRANKE pri kateri želiš NEKAJ UREDITI: ")
        uredba_zelenih_podatkov=input( "1 = OSNOVNE PODATKE, 2 = SAMO DOLOČENE KONTAKTE, 3 = SAMO DOLOČENE AKTIVNOSTI, 4 = SAMO DOLOČENE POGODBE: ")
        #Urejanje osnovnih podatkov
        if uredba_zelenih_podatkov=="1":
            print(stranke[uredba_izbira_id])
            stranke[uredba_izbira_id].update({"naziv": input("Vnesi nov naziv stranke."), "maticna_stevilka": input("Vnesi novo matično številko stranke."), "naslov": input("Vnesi nov naslov stranke.")})
        #Urejanje kontaktov
        elif uredba_zelenih_podatkov=="2":
            print(stranke[uredba_izbira_id]["kontakti"])
            izbira_ureditve_id=int(input("Vnesi id kontakta, ki ga želiš urediti: "))
            stranke[uredba_izbira_id]["kontakti"][izbira_ureditve_id].update({
                "ime_in_priimek": input("Vnesi nov ime in priimek: "),
                "email": input("Vnesi nov email: "),
                "telefonska_stevilka": input("Vnesi novo telefonsko: ")
                })
        #Urejanje aktivnosti   
        elif uredba_zelenih_podatkov=="3":
            print(stranke[uredba_izbira_id]["aktivnosti"])
            izbira_ureditve_id=int(input("Vnesi id aktivnosti, ki jo želiš urediti: "))
            stranke[uredba_izbira_id]["aktivnosti"][izbira_ureditve_id].update({
                "ime_aktivnosti": input("Vnesi novo ime aktivnosti: "),
                "opis_aktivnosti": input("Vnesi novi opis aktivnosti: "),
                "tip_aktivnosti": input("Vnesi novi tip aktivnosti: ")
                })
        #Urejanje pogodb    
        elif uredba_zelenih_podatkov=="4":
            print(stranke[uredba_izbira_id]["pogodbe"])
            izbira_ureditve_id=int(input("Vnesi id pogodbe, ki jo želiš urediti: "))
            stranke[uredba_izbira_id]["pogodbe"][izbira_ureditve_id].update({
                "ime_pogodbe": input("Vnesi novo ime pogodbe: "),
                "datum_zacetka": input("Vnesi nov datum začetka: "),
                "datum_konca": input("Vnesi nov datum konca: ")
                })

        else:
            print("Vnesli ste neveljavno izbiro. Prosimo poskusite ponovno.")

#ISKANJE PODATKOV STRANKE
    elif (izbira == "5"):
        izbira_iskanja = input("ISKANJE PO : 1 = NAZIVIH, 2 = EMAILIH, 3 = MATIČNIH ŠTEVILKAH, 4 = IMENU IN PRIIMKU KONTAKTA: ")
        vnos_iskanja = input("Vnesi besede/številke, ki jih želiš poiskati: ")

        popolna_ujemanja = []
        delna_ujemanja = []

        def preveri_ujemanje(vrednost, podatki_stranke):
            if vrednost.lower() == vnos_iskanja.lower():
                popolna_ujemanja.append(podatki_stranke)
            elif vnos_iskanja.lower() in vrednost.lower():
                delna_ujemanja.append(podatki_stranke)

        # po nazivu
        if izbira_iskanja == "1":  
            for naziv, podatki in stranke.items():
                preveri_ujemanje(naziv, podatki)

        # po emailih
        elif izbira_iskanja == "2":  
            for naziv, podatki in stranke.items():
                for kontakt in podatki.get("kontakti", []):
                    preveri_ujemanje(kontakt["email"], podatki)

        # po matični številki
        elif izbira_iskanja == "3":  
            for naziv, podatki in stranke.items():
                preveri_ujemanje(podatki.get("maticna_stevilka", ""), podatki)

        # po imenu in priimku
        elif izbira_iskanja == "4":  
            for naziv, podatki in stranke.items():
                for kontakt in podatki.get("kontakti", []):
                    preveri_ujemanje(kontakt["ime_in_priimek"], podatki)
        else:
            print("Neveljavna izbira iskanja.")

        # Izpis rezultatov
        if popolna_ujemanja:
            print("\n Popolna ujemanja:")
            for stranka in popolna_ujemanja:
                print(stranka)

        elif delna_ujemanja:
            print("\n Delna ujemanja:")
            for stranka in delna_ujemanja:
                print(stranka)

        elif not popolna_ujemanja and not delna_ujemanja:
            print("Ni zadetkov.")
        else:
            print("Vnesel si napačno možnost! Prosimo POSKUSITE PONOVNO.")
    else:
        print("Vnesel si napačno možnost! Prosimo POSKUSITE PONOVNO.")
