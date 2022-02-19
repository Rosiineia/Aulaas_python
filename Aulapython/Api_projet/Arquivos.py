import json

with open("Dic_resp.json","r") as biblioteca_json:
    dic =json.load(biblioteca_json)
    for chave,dados in dic.items():
        print(chave + " " + str(dados))


        def prop(list, text):
            print(text)
            for item in list:
                print("\t" + str(list.index(item)) + " - " + item)




        attribute = ["$.", "$", "//"]
        operator = ["="]
        value = ["", int]
        objeto = {
            "attribute": attribute[prop(list, "Digite o atributo:\n ")],
            "operator": operator[prop(list, "Digite operador:\n ")],
            "value": input("value")}


