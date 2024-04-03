def nuevaBebida(s):
    s.replace(" ", "")
    if(s.find(',') == -1):
        return("Entrada no valida.")

    if(len(s) == len(s[0:s.find(',')])):
        return("Entrada no valida. Faltan tamaños")

    if(len(s[0:s.find(',') - 1]) < 2):
        return("Nombre de bebida invalido. Nombre muy corto")

    if(len(s[0:s.find(',') - 1]) > 15):
        return("Nombre de bebida invalido. Nombre muy largo")

    if(s.isalpha() == False):
        return("Nombre de bebida invalido.")

    
    return("Bebida agregada")