def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

string = "Exemplo de string"
print(f"String invertida: {inverter_string(string)}")
