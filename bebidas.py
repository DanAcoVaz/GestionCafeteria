def nuevaBebida(s):
    s.replace(" ", "")
    if(s.find(',') == -1):
        return("Entrada no valida")

    if(len(s[0:s.find(',') - 1]) < 2 or len(s[0:s.find(',') - 1]) > 15):
        return("Nombre de bebida invalido")

    if(s.isalpha() == False):
        return("Nombre de bebida invalido")

    
    return("Bebida agregada")