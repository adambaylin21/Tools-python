import json
def encodejson():
    my_object = {}
    my_object["name"] = "Pham Van Hai"
    my_object["age"] = "21"
    print (json.dumps(my_object))
def decodejson():
    my_string = """{"name": "Pham Van Hai", "age": "21"}"""
    my_decode = json.loads(my_string)
    print (my_decode["name"])
    print (my_decode["age"])
if __name__ == "__main__":
#    encodejson()
    decodejson()
