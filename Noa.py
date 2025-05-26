
x_koordinate = input("Gib die X-Koordinate des Mülltonnes ein: ")
y_koordinate = input("Gib die Y-Koordinate des Mülleimers ein: ")
stadt = input("Gib die Stadt an in der, der Mülleimer steht: ")
strasse = input("Gib die Straße an in der, der Mülleimer steht: ")
hausnummer = input("Gib dein Hausnummer an:")

fuellstand = int(input("Gib den Füllstand der Mülltonne in cm ein: "))  

if fuellstand < 30 :
    status = ("  Der Mülleimer ist Leer und muss aktuell nicht abgeholt werden :)")
elif 30 <= fuellstand <= 69:
    status = ("Der Mülleimer ist Mittelvoll und sollte in nächster Zeit abgeholt werden :|")
else:
    status = ("Der Mülleimer ist Voll und muss dringend abgeholt werden :(")
    

fuellstand_prozent = fuellstand / 1.5

muelltonnenart =input("Welche Art hat der Mülleimer(Papier,Plastik,Bio oder Restmüll)?:")


ausgabe2 = f"Der {muelltonnenart}-Mülleimer steht in {stadt} in der Straße {strasse} bei der Hausnummer {hausnummer} und hat die Koordinaten {x_koordinate} x {y_koordinate} y mit dem Füllstand von {fuellstand}cm welches umgerechnet {fuellstand_prozent}% sind.{status}"
print(ausgabe2)


eingabe = input("Schreibe 'Senden' wenn die endgültigen Daten an die App geschickt werden sollen, um den Mülleimer zu registrieren: ")

if eingabe.lower() == "senden":      #zeile mit KI gemacht https://copilot.microsoft.com/chats/1wdhbpr2TwPnaJC6YMdbH
    print("Daten wurden erfolgreich gesendet ")
else:
    print("Registrierung abgebrochen. Grünes Startsymbol muss oben links am Bildschirm gedrückt werden, um die Daten zu ändern.")

        
        
        
