import urllib.request, json 



def get_model_names_by_manufacturer(manufacturer):
    with urllib.request.urlopen(f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{manufacturer}?format=json") as url:
        return set([v['Model_Name'] for v in json.load(url)['Results']])
    


def get_manufacturers_names_list():
    with urllib.request.urlopen("https://vpic.nhtsa.dot.gov/api/vehicles/GetMakesForVehicleType/car?format=json") as url:
        return set([v['MakeName'] for v in json.load(url)['Results']])

print(get_model_names_by_manufacturer('volvo'))
print(get_manufacturers_names_list())

