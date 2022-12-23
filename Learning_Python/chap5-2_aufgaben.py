def main():
    menue_anzeigen()
    
def menue_anzeigen():
    while True:
        print("==================")
        print(" Menü")
        print("==================")
        print(" 1. Aufgabe: 1")
        print(" 2. Aufgabe: 2")
        print(" 3. Aufgabe: 3")
        print(" 4. Aufgabe: 4")
        print(" 5. Aufgabe: 5")
        print(" 6. Aufgabe: 6")
        print(" 7. Aufgabe: 7")
        print(" 8. Aufgabe: 8")
        print(" 9. Aufgabe: 9")
        print("10. Aufgabe:10")
        print(" Programm beenden: 0")
        eingabe = int(input(("Geben Sie eine Zahl ein: ")))
        print("\n")
        if eingabe == 1:
            aufgabe1()
        elif eingabe == 2:
            aufgabe2()
        elif eingabe == 3:
            aufgabe3()
        elif eingabe == 4:
            aufgabe4()

            val = int (input("Bitte geben Sie eine Zahl ein:"))
            print("Fakultät:", fak(val) )
                             
                             
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
        if eingabe != 0:
            print("\n")
            input("Drücken Sie ENTER, um das Programm fortzusetzen ...")
            print("\n")
        elif eingabe == 0:
            break


""" -------------------------------------------------------
Aufgabe 1
Entwickeln Sie ein Programm, das alle geraden Zahlen von 1 bis 2o ausgibt.
Beispiel: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
----------------------------------------------------------- """
def aufgabe1():
    print("----- Lösung Aufgabe 1 -----")
    for i in range (0, 21, 2):
        print(i, end = " ")


""" --------------------------------------------------------
Aufgaben 2
Der Benutzer gibt eine ganze Zahl ein und es werden alle ganzen Zahlen
von dies Zahler Zahl bis 0 durch ein Programm ausgegeben.
Beispiel:
Eingabe: 5
Ausgabe: 5, 4, 3, 2, 1, 0
------------------------------------------------------- """
def aufgabe2():
    print("----- Lösung Aufgabe 2 -----")
    eingabe = int(input("Eingabe: "))
    for i in range (eingabe, -1, -1):
        print(i, end = " ")


""" --------------------------------------------------------
Aufgabe 3
Schreiben Sie ein Programm, in das der Anwender eine ganze Zahl
eingibt und das die Summe aller ganzen Zahlen von 0 bis zu dieser
Zahl berechnet und ausgibt.
Beispiel:
Eingabe: 4
Summe: 10 (Rechnung: 4+3+2+1+0)
-------------------------------------------------------- """
def aufgabe3():
    print("----- Lösung Aufgabe 3 -----")
    eingabe = int(input("Eingabe: "))
    summe = 0
    for i in range (0, eingabe+1):
#    for i in range (eingabe,-1, -1):
        summe = summe + i
    print("Summe:", summe)
   

""" --------------------------------------------------------
Aufgabe 4
Der Benutzer gibt eine ganze Zahl ein und das Programm soll die
Fakultät dieser Zahl (Zahl!) berechnen (Hinweis: 0! = 1)
Beispiel:
Eingabe: 4
Fakultät: 24 (Rechnung: 4*3*2*1)
-------------------------------------------------------- """
def aufgabe4():
    print("----- Lösung Aufgabe 4 -----")
    eingabe = int(input("Eingabe: "))
    fakultaet = 1
    for i in range (1, eingabe+1):
        fakultaet = fakultaet * i
    print("Fakultät:", fakultaet)

# --- Alternaive durch eine rekursive Funktion
def fak(value):
    if (value == 0):
        return 1
    else:
        return value * fak(value - 1)
   
   
""" --------------------------------------------------------
Aufgabe 5
Schreiben Sie ein Programm, welches Ihnen nach Eingabe eines
Anlagebetrages und eines Zinssatzes ausgibt, wie lange (in Jahren)
Sie das Geld anlegen müssen, um über eine Million Vermögen zu kommen.
Hinweis: Die erwirtschafteten Zinsen werden wieder angelegt
und im nöchsten Jahr mitverzinst.
Beispiel:
Eingabe: 700000.00
Zinssazu in %: 10
Ausgabe:
Mindestanzahl Jahre: 4
----------------------------------------------------------- """
def aufgabe5():
    print("----- Lösung Aufgabe 5 -----")
    jahre = 0
    betrag = float(input("Anlagebetrag in Euro: "))
    zinssatz = float(input("Zinssatz in %: "))
    while betrag <= 1000000:
        jahre = jahre + 1
        betrag = betrag + (betrag * zinssatz / 100)
        #print ("{0:3d}.tes Jahr -> Betrag: {1:10.2f}".format(jahre, betrag))
    print("Mindestanzahl Jahre:", jahre)
   

""" --------------------------------------------------------
Aufgabe 6
Schreiben Sie ein Programm, in welches der Anwender 10 Zahlen eingeben
kann und das die größte und die kleinste Zahl anzeigt.
Beispiel:
Eingbabe: 10,5, 23, 5, 44, 3, 41, -2, 44,3
Ausgaben: größte Zahl: 44, kleinste Zahl: -2
----------------------------------------------------------- """
def aufgabe6():
    print("----- Lösung Aufgabe 6 -----")
    groessteZahl = 0
    kleinsteZahl = 0
    zahl = 0
    print("Geben Sie bitte 10 Zahlen ein!")
    for i in range (1, 11):
        zahl = float(input(str(i) + ". Zahl: "))
        if i == 1:
            groessteZahl = zahl
            kleinsteZahl = zahl
        if zahl > groessteZahl:
            groessteZahl = zahl
        if zahl < kleinsteZahl:
            kleinsteZahl = zahl
    print("größte Zahl: {0}, kleinste Zahl: {1}".format(groessteZahl, kleinsteZahl))
  
""" --------------------------------------------------------
Aufgabe 7
Schreiben Sie ein Programm, das alle Teiler einer einzulesenden Zhal ausgibt.
Hinweis: Nutzen Sie den Modulo-Operator.
Beispiel:
Zahl: 63
63 ist durch 1,3,7,9, 21, 63 teilbar.
----------------------------------------------------------- """
def aufgabe7():
    print("----- Lösung Aufgabe 7 -----")
    zahl = int(input("Zahl: "))
    print(str(zahl) + " ist teilbar durch: ")
    for i in range (1, zahl+1):    # Musterlösung: zahl+2 ???
        if zahl % i == 0:
            print(i, end = " ")
  

""" --------------------------------------------------------
Aufgabe 8
Schreiben Sie ein Programm, welches nach einer ganzen Zahl fragt und nach Eingabe
alle Primzahlen bis zu dieser Zahl ausgibt.
Hinweis: Nutzen Sie den Modluio-Operator.
Beispiel:
EIngabe: 10
Ausgabe; 2, 3, 5, 7
-------------------------------------------------------- """
def aufgabe8():
    print("----- Lösung Aufgabe 8 -----")
    primzahl = True
    zahl = int(input("Zahl: "))
    print("Primzahlen bis ", zahl)
    for i in range (2, zahl+1):
        primzahl = True
        for j in range (2, i):
            if i % j == 0:
                primzahl = False
        if primzahl == True:
            print(i, end = " ")
  
""" --------------------------------------------------------
Aufgabe 9
Geben Sie mithilfe von Schleifn folgende Figur aus Sternen auf
dem Bildschirm aus.
Hinweis: Pro Schreibvorgang darf jeweils nur ein Stern ausgegeben werden.
    *******     7 Sterne
     *****      5 Sterne
      ***       3 Sterne
       *        1 Stern
----------------------------------------------------------- """
def aufgabe9():
    print("----- Lösung Aufgabe9 -----")
    for i in range (0, 4):
        for j in range (0, 7-i):
            if j < i:
                print(" ", end=" ")
            else:
                print("*", end = " ")
        print()
  
""" --------------------------------------------------------
Aufgabe 10
J. Wallis hat eie andere Methode gefunden, um PI zu berechnen.
Schreiben Sie ein Prigramm, welches nach diesem Verfahren PI berechnet
und das Ergebnis ausgibt. Die Anzahl der Rechenschritte wird eingegeben.
Pi/2 = (2/1)*(2/3)*(4/3)*(4/5)*(6/5)*(6/7)*(8/7)*(8/9)* ...
Anzahl Rechenschritte: 2
PI = 2.6666666666666t65

-------------------------------------------------------- """
def aufgabe10():
    print("----- Lösung Aufgabe10 -----")
    zahl = int(input("Anzahl Rechenschritte: "))
    x = 2.0
    y = 1.0
    pi = 1.0
    for i in range (0, zahl):
        pi = pi * x / y
        if i % 2 != 0:
            x = x + 2
        else:
            y = y + 2
    print("PI =", (pi*2))
  
# ----------------------------------------------------------

main()
  
