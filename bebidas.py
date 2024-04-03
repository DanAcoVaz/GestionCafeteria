def nuevaBebida(s):
    s.replace(" ", "")
    if(s.find(',') == -1):
        return("Entrada no valida")
    if(s[0:s.find(',')] < 2 or s[0:s.find(',')] > 15):
        return("Nombre de bebida invalido")
    return("Bebida agregada")