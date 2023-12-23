import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "gQfAs8HAGjGfEl4t8nGqqYRQsAXDAV6W"

while True:

    print ("")
    print ("")
    print ("")
    print ("De: Grupo Concepcion")
    print ("")
    print ("Para salir presione S")
    print ("") 
    orig = input("Ingrese Cuidad de Origen: ")
    if orig == "s" or orig == "S":
        break

    dest = input("Ingrese Cuidad de Destino: ")
    if orig == "s" or orig == "S":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) 
    print ("")
    print("Datos de viaje desde",orig,"a",dest)
    
    json_data = requests.get(url).json()     
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status:       " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Dirección desde   " + (orig) + " a " + (dest))
        print("Duración Viaje:   " + (json_data["route"]["formattedTime"]))
        print("Kilometros:       " + str("{:.1f}".format((json_data["route"]["distance"])*1.61)))
        print("Combustible usado (litros): Ya no está la variable fuelUsed")
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.1f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
