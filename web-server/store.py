import requests

def get_categories():
    r = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(r.status_code)
    print(r.text)   ##Returns the info as a string
    print(type(r.text))

    categories = r.json() ##Returns the info as a json (dict)
    for category in categories:
        print(category["name"])
        

