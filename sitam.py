import json
def load_data():
    
    with open("new_json.json") as jsonFile:
        jsonObject = json.load(jsonFile)

    list_data=[]
    for i in range(5):
        a={}
        for key, value in jsonObject[i].items():
            a[key] = value
        list_data.append(a)
    return(list_data)
    
            
ab=load_data()
print(ab)
print(len(ab))

