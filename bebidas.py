def nuevaBebida(s):
    #Quitamos los espacios en blanco
    s.replace(" ", "")
    #Nos aseguramos de que haya , en el string
    if(s.find(',') == -1):
        return(False)

    #Nos aseguramos que el string no acabe en ,
    if(s[-1] == ','):
        return(False)

    #Nos aseguramos que el nombre sea mayor a 2 caracteres
    if(len(s[0:s.find(',') - 1]) < 2):
        return(False)

    #Nos aseguramos que el nombre sea menor a 15 caracteres
    if(len(s[0:s.find(',') - 1]) > 15):
        return(False)

    #Nos aseguramos que el nombre sea completamente alfabetico
    if(s.isalpha() == False):
        return(False)

    #contamos cuantas , hay en el string
    commaCount = s.count(',')

    #Checamos que haya hasta un maximo de 5 tamaños
    if(commaCount > 5):
        return(False)
    
    #Variable para saber cual fue el ultimo size ingresado (para saber que se agregue en orden ascendente)
    lastSize = 0
    #Creamos un index para saber en donde estamos en el string
    index = s.find(',')
    
    #Un ciclo para checar los tamaños
    for i in range(commaCount):
        #Checamos si este es el ultimo tamaño
        if(commaCount == (i + 1)):
            number = int(s[index + 1])
            #Checamos si el tamaño esta dentro del rango
            if(number < 1 or number > 48):
                return(False)
            #Checamos si este nuevo valor es mayor que el anterior
            if(number < lastSize):
                return(False)
        else:
            number = int(s[index + 1: s.find(',', index + 1)])
            #Checamos si el tamaño esta dentro del rango
            if(number < 1 or number > 48):
                return(False)
            #Checamos si este nuevo valor es mayor que el anterior
            if(number < lastSize):
                return(False)
            #Actualizamos el ultimo size agregado
            lastSize = number
            #Actualizamos el index
            index = s.find(',', index + 1)
    
    #Si llegamos aqui, es valida la entrada
    return(True)