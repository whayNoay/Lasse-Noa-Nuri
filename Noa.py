def mülltonnen_info():
    x_koordinate = input("Gib die X-Koordinate der Mülltonne ein: ")
    y_koordinate = input("Gib die Y-Koordinate der Mülltonne ein: ")
    stadt = input("Gib die Stadt an in der die Mülltonne steht: ")

    return f"Mülltonne an Koordinaten {x_koordinate}x {y_koordinate}y in der Stadt {stadt}"

def füllstand():
    return int(input("Gib den Füllstand der Mülltonne in Prozent ein: "))  

def prüfe_füllstand(füllstand):
    if füllstand < 30:
        return "Leer  :)"
    elif 30 <= füllstand <= 69:
        return "Mittelvoll  :|"
    else:
        return "Voll  :("


print(mülltonnen_info())  

füllstand_wert = füllstand()  
print(f"Der Füllstand der Mülltonne ist {prüfe_füllstand(füllstand_wert)} ")




      
    
    
    

#leer weniger 30
#mittelvoll 30 69
#voll 70 mehr











