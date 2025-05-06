import requests
import json

cntr = input("Enter country name: ")
cntr.lower()

url = 'https://restcountries.com/v3.1/name/' + cntr 
x = requests.get(url)
r = x.text
y = json.loads(r)
if type(y) == dict:
    if y["status"] == 404:
        raise Exception("Country not found")
elif type(y) == list:
    #print(x.json())
    num = int(input("Choose option: \n 1.Population \n 2.Capital city \n 3.Languages \n 4.Code \n 5.Independence \n"))
    match num:
        case 1:
            print("Population: ", y[0]["population"])
        case 2:
            print("Capital city: ", y[0]["capital"])
        case 3:
            print("Languages: ", y[0]["languages"])
        case 4:
            print("Country code: ", y[0]["ccn3"])
        case 5:
            print("Independece: ", y[0]["independent"])
        case _:
            raise Exception("Invalid option")














