
""" ----------------------------------------------------------------------------
Aufgabe 4-1
Schreiben Sie ein Programm, in dem Sie zwei Zahlen eingeben können und das dann
die Differenz dieser Zahlen berechnet und ausgibt.
Beispiel:
> Zah11: 15
> Zahl2: 6
> Ergebnis: 9
---------------------------------------------------------------------------- """
def aufgabe_1() :
    print ("--- --- Aufgabe 1 --- --- ")
    zahl_1 = float(input("Bitte geben Sie die erste Zahl ein: "))
    zahl_2 = float(input("Bitte geben Sie die zweite Zahl ein: "))
    print("Ergebnis: {0:f} - {1:f} = {2:f}".format(zahl_1,zahl_2, zahl_1-zahl_2))
    print("--- --- Ende Aufgabe 1 --- ---\n")


""" ----------------------------------------------------------------------------
Aufgabe 4-2
Schreiben Sie ein Programm, in das Sie drei Gleitkommazahlen eingeben können und
das nach der unten stehenden Formel das Ergebnis berechnet und ausgibt.
FormeL. Die erstenbeiden Zahlen werden addiert und das Ergebnis dann mit der
dritten Zahl multipliziert.
Beispiel:
> Zahl1: 1.5
> Zahl2: 1.3
> Zahl3: 2.2
> Das Ergebnis ist 6.16
---------------------------------------------------------------------------- """
def aufgabe_2() :
    print ("--- --- Aufgabe 2 --- --- ")
    zahl_1 = float(input("Bitte geben Sie die erste Zahl ein: "))
    zahl_2 = float(input("Bitte geben Sie die zweite Zahl ein: "))
    zahl_3 = float(input("Bitte geben Sie die dritte Zahl ein: "))
    ergebnis = (zahl_1+zahl_2) * zahl_3
    print("Ergebnis: ({0:f} + {1:f}) * {2:f} = {3:f}".format(zahl_1,zahl_2, zahl_3, ergebnis))
    print("--- --- Ende Aufgabe 2 --- ---\n")


""" ----------------------------------------------------------------------------#
Aufgabe 4-3
Schreiben Sie ein Programm, welches den Durchschnitt von vier Gleitkommazahlen
berechnetund ausgibt. Die Zahlen werden vom Benutzer ins Programm eingegeben.
Beispiel:
> Zahl: 10.0
> Zahl: 2.5
> Zahl: 4,7
> Zahl: 15.0
> Der Durchschnitt der vier Zahlen ist 8.05
---------------------------------------------------------------------------- """
def aufgabe_3() :
    print ("--- --- Aufgabe 3 --- --- ")
    zahl_1 = float(input("Bitte geben Sie die erste Zahl ein: "))
    zahl_2 = float(input("Bitte geben Sie die zweite Zahl ein: "))
    zahl_3 = float(input("Bitte geben Sie die dritte Zahl ein: "))
    zahl_4 = float(input("Bitte geben Sie die vierte Zahl ein: "))

    ergebnis = (zahl_1 + zahl_2 + zahl_3 + zahl_4) / 4
    
    print("Ergebnis: {0:f}".format(ergebnis))
    print("--- --- Ende Aufgabe 3 --- ---\n")

""" ----------------------------------------------------------------------------
Aufgabe 4-4
Schreiben Sie ein Programm, welches Ihnen nach Eingabe der Spannung U in Volt
und der Stromstärke I in Ampere den elektrischen Widerstand  R in Ohm und
die elektrische Leistung P in Watt ausrechnet und ausgibt.
Beispiel:
> Spannung U in Volt        : 10.00
> Stromstärke I in Ampere   : 2.00
> Der elektrische Widerstand R beträgt 5.00 Ohm
> Die elektrische Leistung P beträgt 20.00 Watt
---------------------------------------------------------------------------- """
def aufgabe_4() :
    print ("--- --- Aufgabe 4 --- --- ")
    U = float(input("Bitte geben Sie Spannung in V ein: "))
    I = float(input("Bitte geben Sie die Stromstärke in A ein: "))
    R = U / I
    P = U * I
    print("Der Widerstand beträgt {0:f} Ohm".format(R))
    print("Die Leistung beträgt  {0:f} W".format(P))



""" ----------------------------------------------------------------------------
Aufgabe 4-5
Ermitteln Sie mithilfe eines Programms den ganzzahligen Rest einer Division.
Dabei werden der ganzzahlige Dividend und der ganzzahlige Divisor eingegeben
und der Rest ausgegeben. Benutzen Sie dafür den Modulo-Operator.
Beispiel;:
> Dividend: 17
> Divisor: 3
> Das Ergebnis von 17 modulo 3 ist 2
---------------------------------------------------------------------------- """
def aufgabe_5 ():
    print ("--- --- Aufgabe 5 --- --- ")
    divident = int(input("Bitte geben Sie den Divident ein: "))
    divisor  = int(input("Bitte geben Sie den Divisor ein: "))
    
    print("Das Ergebis ist {0:5d} Rest {1:5d}".format(int(divident/divisor), divident%divisor))


""" ----------------------------------------------------------------------------
Aufgabe 4-6
Der Computer soll nach Eingabe des Listenpreises in Euro und des
Lieferantenrabatts in Prozent den Einkaufspreis berechnen und ausgeben.
Beispiel:
> Listenpreis in Euro: 100.00
> Lieferantenrabatt in Prozent: 3.25
> Der Einkaufspreis beträgt 96.75 Euro
---------------------------------------------------------------------------- """
def aufgabe_6() :
    print ("--- --- Aufgabe 6 --- --- ")
    listenpreis = float(input("Bitte geben Sie den Listenpreis ein: "))
    lieferantenrabatt = float (input("Bitte geben SIe den Lieferantenrabatt ein: "))
    einkaufspreis = listenpreis * ((100.0 - lieferantenrabatt)/100.0)
    print ("Der Einkaufspreis beträgt {0:.2f} Euro)".format(einkaufspreis))
           

""" ----------------------------------------------------------------------------
Aufgabe 4-7
Der BMI einer Person soll nach derEingabe des Gewichts in Kilogramm und der
Größe in in Metern berechnet und ausgegeben werden.
Formel: BMI = Gewicht / (Größe * Größe)
Beispiel:
> Gewicht in kg :  80.00
> Größe in m    :   1.80
> Der BMI der Person ist 24.69
---------------------------------------------------------------------------- """
def aufgabe_7() :
    print ("--- --- Aufgabe 7 --- --- ")
    gewicht  = float(input("Bitte geben Sie ihr Gewicht ein: "))
    groesse = float (input("Bitte geben Sie ihre Größe in m ein: "))
    bmi = gewicht / (groesse *groesse)
    bmi2 = gewicht / pow(groesse,2)
    print ("Ihr BMI geträgt {0:.2f} ".format(bmi))
    print ("Ihr BMI geträgt {0:.2f} ".format(bmi2))

""" ----------------------------------------------------------------------------
Aufgabe 4-8
Schreiben Sie ein Prigramm, das nach Eingabe einer Speichergröße in Byte die
Größe in Megabyte (MB) und in MebiByte (MiB) berechnet und ausgibt.
Beispiel:
> Speichergröße in Byte: 84000000
> Speichergröße in MB  : 84.0
> Speichergröße in MiB : 80.1
---------------------------------------------------------------------------- """
def aufgabe_8():
    print ("--- --- Aufgabe 8 --- --- ")
    speichergroesse  = int(input("Bitte geben Sie die Speichergroesse in Byte ein: "))
    inMB = speichergroesse /(1000 * 1000)
    inMiB = speichergroesse /(1024 * 1024)

    print ("Speichergröße in MB  {0:.2f} ".format(inMB))
    print ("Speichergröße in MiB {0:.2f} ".format(inMiB))

""" ----------------------------------------------------------------------------
Aufgabe 4-9
Es sollen die x- und y-Werte für zwei Punkte eingebenen werden,
P1(x1,y1) und P2(x2,y2). Danach sollen der Abstand zwischen diesen beiden Punkten
berechnet und ausgegeben werden.
Hinweis: Wurzel in Python
 import math
 math.sqrt(...)

Beispiel:
> x1 : 6
> y1 : 4
> x2 : 10
> y2 : 1
> Der Abstand zwischen den Punkten is 5.0
---------------------------------------------------------------------------- """
def aufgabe_9():
    import math
    print ("--- --- Aufgabe 9 --- --- ")
    
    x1  = int(input("Bitte geben Sie x1 ein: "))
    y1  = int(input("Bitte geben Sie y1 ein: "))
    x2  = int(input("Bitte geben Sie x2 ein: "))
    y2  = int(input("Bitte geben Sie y2 ein: "))

    distance = math.sqrt( pow( (x2-x1),2) + pow( (y2-y1),2) )

    print ("Der Abstand zwischen den Punkten ist {0:.2f} ".format(distance))


""" ----------------------------------------------------------------------------
Aufgabe 4-10
Es sollen die Höhe und die Breite eiens Bildes in Pixeln eingegeben werden.
Außerdem soll der Benutzer den Speicherbedarf für einen Pixel in Byte eingeben und
die Anzahl der Bilder, welche er speichern möchte.Die Ausgabe soll der Speicherplatz
der Bilder in MiB sein.
Beispiel:
> Höhe   in Pixel: 1024
> Breite in Pixel: 768
> Speicherbedarf pro Pixel in Byte: 1
> Anzahl Bilder: 20
> Speicherbedarf in MiB. 15.0
---------------------------------------------------------------------------- """

def aufgabe_10():
    print ("--- --- Aufgabe 10 --- --- ")
    hoehe  = int(input("Bitte geben Sie die Höhe in Pixel ein: "))
    breite  = int(input("Bitte geben Sie dei Breite in Pixel ein: "))
    speicherbedarf_pp  = int(input("Bitte geben Sie den Speicherbedarf pro Pixel in Byte ein: "))
    anzahl  = int(input("Bitte geben Sie die Anzahl Bilder  ein: "))

    speicherbedarf = hoehe * breite * speicherbedarf_pp * anzahl
    print ("Speicherbedarf in   B: {0:12.2f} ".format(speicherbedarf))
    speicherbedarf /=1024.0
    print ("Speicherbedarf in KiB: {0:12.2f} ".format(speicherbedarf))
    speicherbedarf /=1024.0
    print ("Speicherbedarf in MiB: {0:12.2f} ".format(speicherbedarf))
    
    


# --- --- --- --- ---
# main-Funktion
# --- --- --- --- ---

def main():
    #aufgabe_1()
    #aufgabe_2()
    #aufgabe_3()
    #aufgabe_4()
    #aufgabe_5()
    #aufgabe_6()
    #aufgabe_7()
    #aufgabe_8()
    #aufgabe_9()
    aufgabe_10()

# --- --- --- --- ---
# hier get es los ... Aufruf der main-Funktion 
# --- --- --- --- ---
    
main()
