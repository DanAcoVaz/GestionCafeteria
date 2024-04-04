from bebidas import nuevaBebida

def testInputs():
    assert nuevaBebida("") == False
    assert nuevaBebida("SuperJugo,") == False
    assert nuevaBebida(",56") == False
    assert nuevaBebida(",") == False
    assert nuevaBebida("3, 7, 9, Pepsi") == False
    assert nuevaBebida("Coca") == False
    assert nuevaBebida("Pepsi, 5, 7, 10, 12, 15, 18, 22") == False
    assert nuevaBebida("     Manzanita Sol,   3,    6,    12") == False