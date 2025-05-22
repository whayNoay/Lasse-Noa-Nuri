
x_koordinate = input("Gib die X-Koordinate der Mülltonne ein: ")
y_koordinate = input("Gib die Y-Koordinate der Mülltonne ein: ")
stadt = input("Gib die Stadt an in der die Mülltonne steht: ")
strasse = input("Gib deine Straße an: ")
hausnummer = input("Gib dein Hausnummer an:")

fuellstand = int(input("Gib den Füllstand der Mülltonne in cm ein: "))  

if fuellstand < 30 :
    status = ("  Die Mülltonne ist Leer und muss aktuell nicht abgeholt werden :)")
elif 30 <= fuellstand <= 69:
    status = ("Die Mülltonne ist Mittelvoll und sollte in nächster Zeit abgeholt werden :|")
else:
    status = ("Die Mülltonne ist Voll und muss dringend abgeholt werden :(")
    

fuellstand_cm = fuellstand / 1.5

muelltonnenart =input("Welche Art hat die Muelltonnen(Papier,Plastik,Bio oder Restmüll)?:")

ausgabe2 = f"Die {muelltonnenart}-Mülltonne steht in {stadt} in der Straße {strasse} bei der Hausnummer {hausnummer} und hat die Koordinaten {x_koordinate} x {y_koordinate} y mit dem Füllstand von {fuellstand}cm welches umgerechnet {fuellstand_cm}% sind.{status}"
print(ausgabe2)


eingabe = input("Schreibe 'Senden' wenn du deine endgültigen Daten an die App schicken möchtest, um deine Mülltonne zu registrieren: ")

if eingabe.lower() == "senden":      #zeile mit KI gemacht https://copilot.microsoft.com/chats/1wdhbpr2TwPnaJC6YMdbH
    print("Daten wurden erfolgreich gesendet")
else:
    print("Registrierung abgebrochen. Drücken Sie erneut das grüne Startsymbol oben links am Bildschirm, um Ihre Daten zu ändern.")

        
        
        
#zeile mit KI gemacht https://copilot.microsoft.com/chats/1wdhbpr2TwPnaJC6YMdbH