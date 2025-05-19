def mülltonnen_info():
    x_koordinate = input("Gib die X-Koordinate der Mülltonne ein: ")
    y_koordinate = input("Gib die Y-Koordinate der Mülltonne ein: ")
    stadt = input("Gib die Stadt an in der die Mülltonne steht: ")

    return f"Mülltonne an Koordinaten {x_koordinate}x {y_koordinate}y in der Stadt {stadt}"


def mülltonnenart():
    typ = input("Welchen Typ hat die Mülltonne?(Papier,Restmüll,Bio oder Plastik): ")
    
    return f" Der Typ der Mülltonne ist{typ}"


def füllstand():
    return int(input("Gib den Füllstand der Mülltonne in Prozent ein: "))  


   


def prüfe_füllstand(füllstand):
    if füllstand < 30:
        return "Leer und muss aktuell nicht abgeholt werden :)"
    elif 30 <= füllstand <= 69:
        return "Mittelvoll und sollte in nächster Zeit abgeholt werden :|"
    else:
        return "Voll und muss dringend abgeholt werden :("


print(mülltonnen_info())  

print(mülltonnenart())

mülltonnenart_wert = typ
füllstand_wert = füllstand()

print(f"Der Füllstand der {typ}mülltonne ist {prüfe_füllstand(füllstand_wert)} ")






      
    
    
    

#leer weniger 30
#mittelvoll 30 69
#voll 70 mehr











