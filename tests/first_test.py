from bebidas import nuevaBebida

#Test para probar diferentes inputs
def testInputs():
    #Input vacio
    assert nuevaBebida("") == False
    #Input acabando en , sin tamaños
    assert nuevaBebida("SuperJugo,") == False
    #Input sin nombre
    assert nuevaBebida(",56") == False
    #Solo una , en el input
    assert nuevaBebida(",") == False
    #Tamaños primero y luego nombre
    assert nuevaBebida("3, 7, 9, Pepsi") == False
    #Solo nombre
    assert nuevaBebida("Coca") == False
    #El input acaba en ,
    assert nuevaBebida("Pepsi, 5, 7, 10, 12,") == False
    #Input correcto con muchos espacios (para probar que los espacios se ignoran)
    assert nuevaBebida("    Manzanita Sol,   3,    6,    12") == True
    #Input correcto
    assert nuevaBebida("Pepsi, 10, 20, 30") == True

#Tests para probar la introduccion del nombre
def testNames():
    #Nombre de menos de 2 caracteres
    assert nuevaBebida("K, 2, 4, 6, 8") == False
    #Nombre de 2 caracteres
    assert nuevaBebida("KO, 3, 5, 8") == True
    #Nombre de muchos caracteres (>15)
    assert nuevaBebida("The Super powerful elixir of the gods, 1, 2, 3, 4") == False
    #Nombre de 16 caracteres
    assert nuevaBebida("Powerful Beverage, 10, 20, 30") == False
    #Nombre de 15 caracteres
    assert nuevaBebida("Powerful Elixirs, 10, 15, 20, 25, 30") == True
    #Nombre con caracteres alfanumericos
    assert nuevaBebida("4 Loko, 4, 8, 12, 16, 20") == False
    #Nombre con caracteres numericos
    assert nuevaBebida("24, 2, 6, 9, 13") == False
    #Nombre con caracteres alfabeticos
    assert nuevaBebida("Four Loko, 4, 8, 12, 16, 20") == True

#Tests para probar los tamaños
def testSizes():
    #Bebida sin tamaños
    assert nuevaBebida("No size") == False
    #Bebida con 4 tamaños
    assert nuevaBebida("Four Loko, 4, 8, 12, 16") == True
    #Bebida con 5 tamaños
    assert nuevaBebida("Cinco Pezo, 1, 2, 3, 4, 5") == True
    #Bebida con 6 tamaños
    assert nuevaBebida("Miami, 2, 4, 6, 8, 10, 12") == False
    #Bebida con mas de 6 tamaños
    assert nuevaBebida("Pepsi, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 30") == False
    #Bebida con tamaños no enteros
    assert nuevaBebida("Sprite, 2.4, 3.1416, 5.879") == False
    #Bebida con tamaños menores a 1
    assert nuevaBebida("Neo Sprite, 0, 5, 15") == False
    assert nuevaBebida("Fantdont, -5, 5, 15") == False
    #Bebida con tamaño de 1
    assert nuevaBebida("One, 1") == True
    #Bebida con tamaño de 49 o mayor
    assert nuevaBebida("Cuarenta y nueve, 40, 45, 49") == False
    assert nuevaBebida("Mas de eso, 52, 68, 94") == False
    #Bebida con tamaño de 48
    assert nuevaBebida("Cuarenta y ocho, 23, 36, 41, 48") == True
    #Tamaños ingresados de manera descendente
    assert nuevaBebida("Deep Down, 20, 14, 7, 3") == False
    #Tamaños ingresados sin orden
    assert nuevaBebida("Loco y poco, 7, 15, 4, 24") == False
    #Tamaños ingresados de forma ascendente
    assert nuevaBebida("Mexicano, 5, 15, 21") == True