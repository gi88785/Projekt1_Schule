def main():
    menue_anzeigen()

def menue_anzeigen():
    print("=====================")
    print("Menü")
    print("=====================")
    print("Aufgabe  1 Lieferkosten    :  1")
    print("Aufgabe  2 kleinste Zahl   :  2")
    print("Aufgabe  3 Bonus           :  3")
    print("Aufgabe  4 Festgeldanlage  :  4")
    print("Aufgabe  5: Lohn           :  5")
    print("Aufgabe  6: Logik-Rechner  :  6")
    print("Aufgabe  7: Gerade Zahl    :  7")
    print("Aufgabe  8: groesste Zahl  :  8")
    print("Aufgabe  9: Schaltjahr     :  9")
    print("Aufgabe 10: Bankautomat    : 10")
    print("=====================")
    eingabe = int (input("Geben Sie eine Zahl ein: "))
    print("\n")
    if eingabe == 1:
        aufgabe1()
    elif eingabe == 2:
        aufgabe2()
    elif eingabe == 3:
        aufgabe3()
    elif eingabe == 4:
        aufgabe4()
    elif eingabe == 5:
        aufgabe5()
    elif eingabe == 6:
        aufgabe6()
    elif eingabe == 7:
        aufgabe7()
    elif eingabe == 8:
        aufgabe8()
    elif eingabe == 9:
        aufgabe9()
    elif eingabe == 10:
        aufgabe10()
    else:
        print ("ungültige Menüauswahl")


""" --------------------------------------------------------
Aufgabe 1
Eine Firma liefert bei einem Bestellwert ab 100,00€ die Ware ohne
Versandkosten aus. Für Aufträge unter 100,00 € betragen die
Versandkosten pauschal 5,50 €. Schreiben Sie ein Programm, das den
Rechnungsbetrag in Abhängigkeit vom Bestellwert ausgibt.
Beispiel:
> Bestellwert in Euro: 50.00
> Rechnnungsbetrag: 55.50 Euro
oder
> Bestellwert in Euro: 250.00
> Rechnnungsbetrag: 250.00 Euro
------------------------------------------------------------ """
def aufgabe1():
    print ("Aufgabe 1: Lieferkosten")
    bestellwert = float (input("Bitte geben Sie den Bestellwert ein: "))
    if bestellwert < 100.0:
        lieferkosten = 5.50
    else:
        lieferkosten = 0.00

    rechnungsbetrag = bestellwert + lieferkosten

    # Ausgabe
    print("Bestellwert         : {0:8.2f}".format(bestellwert))
    print("+ Lieferkosten      : {0:8.2f}".format(lieferkosten))
    print("Rechnungsbetrag     : {0:8.2f}".format(rechnungsbetrag))

""" --------------------------------------------------------
Aufgabe 2
Schreiben Sie ein Programm, das Ihnen nach Eingabe von zwei
Gleitkommazahlen die kleineste Zahl ausgibt.
Beispiel:
> Zahl1: 52.12
> Zahl2: -55.5
> Die kleinste Zahl ist -55.5.
------------------------------------------------------------"""
def aufgabe2():
    print ("Aufgabe 2 : kleinste Zahl")
    zahl1 = float (input("Bitte geben Sie die erste Zahl ein: "))
    zahl2 = float (input("Bitte geben Sie die zweite Zahl ein: "))
    if zahl1 < zahl2:
        kleinste_zahl = zahl1
    else:
        kleinste_zahl = zahl2
        
    print("Die kleinste Zahl ist = " + str(kleinste_zahl))
    



"""---------------------------------------------------------
Aufgabe 3
Ein Unternehmen gewährt seinen Kunden 5 % Bonus vom Nettoumsatz,
wenn dieser pro Jahr 70000.00 € übersteigt. Schreiben Sie ein Prpogramm,
das den Binus eines Kunden erreichent und ausgibt. Falls der Kunde
den erforderlichenU Umsatz nicht erbringt, soll eine entsprechende
Meldung ausgegeben werden.
Beispiel:
> Nettoumsatz in Euro: 100000.00
> Bonus in Euro: 5000.00
------------------------------------------------------------"""
def aufgabe3():
    print ("Aufgabe 3: Bonus")
    nettoumsatz = float (input("Bitte geben Sie den Nettoumsatz ein: "))
    if nettoumsatz > 70000.0:
        bonus = nettoumsatz * 0.05    
        print ("Nettoumsatz in Euro: {0:8.2f}".format(nettoumsatz))
        print ("      Bonus in Euro: {0:8.2f}".format(bonus))
    else:
        print ("Nettoumsatz in Euro: {0:8.2f}".format(nettoumsatz))
        print("Der Kunde erhält keinen Bonus")

""" --------------------------------------------------------
Aufgabe 4
Ein Bank gewährt ihren Kunden bei einer Festgeldanlage folgede Zinsen pro Jahr:
Anlagebetrag in Euro | Zinsen in %
bis   5000.00          | 2.00
bis  10000.00          | 2.25
bis  50000.00          | 2.50
über 50000.00          | 2.75
Berechnen Sie durch ein Programm die Zinsen bei verschiedenen Anlagebeträgen.
Beispiel:
> Anlagebetrag    : 10000.00 EUR
> Zinsen pro Jahr :   225.00 EUR
------------------------------------------------------------"""
def aufgabe4():
    print ("Aufgabe 4: Festgeld")
    anlagebetrag  = float (input("Bitte geben Sie den Anlagebetrag ein: "))
    zinszsatz = 0.0
    if anlagebetrag > 50000.0:
        zinssatz = 2.75
    elif anlagebetrag > 10000.0:
        zinssatz = 2.50
    elif anlagebetrag > 5000.0:
        zinssatz = 2.25
    else:
        zinssatz = 2.00
        
    zinsen = anlagebetrag * (zinssatz / 100.0)
    print ("Anlagebetrag    : {0:8.2f} EUR".format(anlagebetrag))
    #print ("Zinssatz        : {0:8.2f}".format(zinssatz))
    print ("Zinsen pro Jahr : {0:8.2f} EUR".format(zinsen))
    
""" --------------------------------------------------------
Aufgabe 5
Ermitteln Sie den Wochen-Bruttolohn eines Arbeiters durch die Eingabe
der geleisteten Arbeitsstunden pro Woche sowie des Stundenlohns. Für
jede über 35 WOchenstunden hinausgehende abgeleistete Stunde wird ein
Zuschlag von 50.00 % gewährt. Eingaben über 80 Stunden und Stundenlöhne
über 50.00 Euro soll das Programm nicht verarbeiten.
Beispiel:
> Stunde: 40
> Stundenlohn in Euro: 20.00
> Bruttoarbeitslohn: 850.00 Euro
------------------------------------------------------------"""
def aufgabe5():     
    print ("Aufgabe 5: Stundenlohn")

    arbeitsstunden = int (input("Arbeitsstunden: "))
    stundenlohn =    int (input("Stundenlohn: ") )

    if arbeitsstunden <= 80 and stundenlohn <= 50:
        if arbeitsstunden > 35:
            uestunden = arbeitsstunden - 35
        else:
            uestunden = 0

        lohn = arbeitsstunden * stundenlohn + uestunden * stundenlohn / 2.0

        print ("Bruttolohn : {0:8.2f}".format(lohn))
    else:
        print ("ungültige Eingabe")



""" ----------------------------------------------------------------------------
Aufgabe 6
Schreiben Sie ein Programm, welches die Auswahl einer logischen Verknüpfung und
die Eingabe zweier Werte (x,y) ermöglicht und entsprechend der ausgewählten
Verknüpfung eine "0" oder eine "1" ausgibt.
x | y |  OR  |  AND | NAND |  XOR |
1 | 1 |  1   |   1  |   0  |   0  |
1 | 0 |  1   |   0  |   1  |   1  |
0 | 1 |  1   |   0  |   1  |   1  |
0 | 0 |  0   |   0  |   1  |   0  |
Beispiel:
> Wählen Sie einen logischen Oerator aus:
> UND  : 1
> ODER : 2
> NAND : 3
> XOR  : 4
> Auswahl: 4
> Geben Sie die Werte für x und y ein:
> X:1
> Y:1
> Das Ergebnis ist: 0
---------------------------------------------------------------------------- """
def aufgabe6():
    print("----- Aufgabe 6 -----")
    print("Wählen Sie ein en logischen Operator aus:")
    print("UND : 1 ")
    print("ODER: 2 ")
    print("NAND: 3 ")
    print("XOR : 4 ")

    auswahl = int(input("Auswahl: "))

    if auswahl > 0 and auswahl < 5:
        print("Geben Sie die Werte für x und y ein: ")
        x = int(input("x: "))
        y = int(input("y: "))
        
        if auswahl == 1:
            print("Das Ergebnis ist", x and y)

        if auswahl == 2:
            print("Das Ergebnis ist", x or y)

        if auswahl == 3:
            print("Das Ergebnis ist", not(x and y))

        if auswahl == 4:
            print("Das Ergebnis ist", x ^ y)
    else:
        print("Zahl nicht im Bereich!")
        print("Geben Sie eine Zahl von 1 bis 4 ein.")
   
""" ----------------------------------------------------------------------------
Aufgabe 7
Schreiben Sie ein Programm,, das Ihnen nach Eingabe einer positiven Zahl ausgibt,
ob es sich um eine gerade oder eine ungerade Zahl handelt.
Hinweis: Verwenden SIe den Modulo-Operator.
Beispiel:
> Zahl: 4
> Die Zahl 4 ist eine gerade Zahl.
---------------------------------------------------------------------------- """
def aufgabe7():
    print("----- Aufgabe 7 -----")
    zahl = int(input("Zahl: "))
    if (zahl % 2) == 0:
        print("Die Zahl " + str(zahl) + " ist eine gerade Zahl.")
    else:
       print("Die Zahl " + str(zahl) + " ist eine ungerade Zahl.")

""" ----------------------------------------------------------------------------
Aufgabe 8
Nach Eingabe von vier Zaheln soll das Programm Ihnen die größte Zahl ausgeben.
Beispiel:
> Zahl1: 4
> Zahl2: 12
> Zahl3: 55
> Zahl4: 7
> Die größte Zahl ist 55.
---------------------------------------------------------------------------- """
def aufgabe8():
    print("----- Aufgabe8 -----")
    zahl1 = float(input("Zahl1: "))
    größte_zahl = zahl1

    zahl2 = float(input("Zahl2: "))
    if zahl2 > größte_zahl:
        größte_zahl = zahl2

    zahl3 = float(input("Zahl3: "))
    if zahl3 > größte_zahl:
        größte_zahl = zahl3

    zahl4 = float(input("Zahl4: "))
    if zahl4 > größte_zahl:
        größte_zahl = zahl4

    print("Die größte Zahl ist:", größte_zahl)

""" ----------------------------------------------------------------------------
Aufgabe 9
Schreiben Sie ein Programm, welches Ihnen nach Eingabe einer Jahreszahl ausgibt,
ob es sich um ein Schaltjahr handelt oder nicht. EIn Jahr ist ein Schaltjahr,
wenn die Jahreszahl durch 4 und nicht durch 100 teilbar ist. Ausnahme: EIn Jahr
ist ein Schaltjahr, wenn es durch 4 und durch 100 und durch 400 teilbar ist.
Hinweis: Nutzen Sie den Modulo-Operator.
Beispiel:
> Jahr: 2000
> Das Jahr 2000 ist ein Schaltjahr
---------------------------------------------------------------------------- """
def aufgabe9():
    print("----- Aufgabe 9 -----")
    jahr = int(input("Jahr: "))
    if jahr % 400 == 0 or (jahr % 100 != 0 and jahr % 4 == 0):
        print("Das Jahr " + str(jahr) + " ist ein Schaltjahr.")
    else:
        print("Das Jahr " + str(jahr) + " ist kein Schaltjahr.")

""" ----------------------------------------------------------------------------
Aufgabe 10
Schreiben Sie ein Programm "Bankautomat. Es soll folgendes Startmenü ausgeben:
> Wählen Sie bitte einen Betrag aus dem Menü aus
> und geben Sie die entsprechende Zahl ein.
>
> Auswahlmenü
>  1.Auszahlung 100,- Euro
>  2.Auszahlung 200,- Euro
>  3.Auszahlung 500,- Euro
>  4.anderer Betrag

Bei der Eingabe einer 1,2 oder 3 soll folgende Meldung ausgegeben werden
(hier bei eine 1):
> Sie bekommen 100,- Euro ausgezahlt.
> Wir wünschen Ihnen noch einen guten Tag

Bei der Eigabe einer 4 erhält der Anwender die Aufforderung, einen Betrag
zwischen 10,- und 1000,- einzugeben. Danach folgt wieder der Hinweis, dass
der entsprechende Betrag ausgezahlt wird.
Bei falschen EIngabewerten soll eine Fehlermeldung ausgegeben werden.

> Geben Sie einen Betrag zwischen 10,- und 1000,- Euro ein!
>
> Betrag: _

Hinweis: der kleinste Geldschein, der ausgegeben werden kann, ist der
10-Euro-Schein
---------------------------------------------------------------------------- """
def aufgabe10():
    print("----- Aufgabe 10 -----")
    print("Wählen Sie bitte einen Betrag aus dem Menü aus und geben Sie die entsprechende Zahl ein.")
    print("Auswahlmenü ")
    print("1. Auszahlung 100,- Euro ")
    print("2. Auszahlung 200,- Euro ")
    print("3. Auszahlung 500,- Euro ")
    print("4. anderer Betrag ")
    betrag = 0
    eingabe = int(input("Eingabe: "))
    if eingabe == 1:
        betrag = 100
    elif eingabe == 2:
        betrag = 200
    elif eingabe == 3:
        betrag = 300
    elif eingabe == 4:
        print("Geben Sie einen Betrag zwischen 10,00 und 1000,00 Euro ein!")
        betrag = int(input("Betrag: "))

    if betrag < 10.00 or betrag > 1000.00 or betrag % 10 != 0:
        print("Ungültiger Betrag")
    else:
        print("Sie bekommen {0:.2f} Euro ausgezahlt.".format(betrag))
    print("Wir wünschen Ihnen noch einen schönen Tag.")

# ------------------------------------------------------------------------------    
main()  # Ausführen des Programms
