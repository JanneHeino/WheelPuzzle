
#Kehä 1 uloin ja 5 sisin

keha1 = [0,12,4,0,11,3,6,1,6,4,1,3,11,12,4,3]
keha2ala1 = [9,13,18,10,10,7,18,9]
keha2ala2 = [11,10,10,10,15,19,2,27]
keha2yla = [9,6,10,8,10,9,8,8] # Jos ala 2 valittu niin silloin 9ja 5 ovat kiinni toisissaan, 6ja5, 10ja24 jne.
keha3ala1 = [5,5,24,10,7,12,10,22]# Kiinni
keha3ala2 = [8,1,8,20,20,1,12,0]
keha3yla = [10,0,11,8,8,8,10,11]
keha4ala1 = [0,20,19,15,12,13,0,19]# Kiinni
keha4ala2 = [5,8,10,20,20,13,22,10]
keha4yla = [14,11,8,12,11,3,8,10]
keha5ala1 = [8,4,4,4,1,10,10,6] # Kiinni
keha5ala2 = [13,16,14,5,14,17,5,14] # Jos kehaxyla alku pisteessä niin silloin on ala 2 ensin näkyvillä, ala1 jää ylemmän kehän alle
keha5yla = [6,8,8,16,19,8,13,6]

yritykset = 0
maxOikeatSarakkeet = 0

#Jos ala1 on käytössä, niin tällöin se on lukittu aikaisempaan ylä kehän samaan indexiin, ei voi liikuttaa vapaasti.

def MuodostaYmpyra(ylalista, alalista, alaeka = False):
    yhdistettyLista = []
    i = 0
    if alaeka == False:
        for a in range(8):

            yhdistettyLista.append(ylalista[i])
            yhdistettyLista.append(alalista[i])
            i += 1

        return yhdistettyLista
    else:
        for a in range(8):

            yhdistettyLista.append(alalista[i])
            yhdistettyLista.append(ylalista[i])
            i += 1

        return yhdistettyLista


def MoveFirstNumberToLast(lista):
    talteen = lista[0]
    lista.pop(0)
    lista.append(talteen)



def LaskeSarakkeet(keha2, keha3, keha4, keha5):
    global yritykset

    yritykset += 1
    print('Yritykset: ', yritykset)
    sarake = 0
    sarakeTulos = {}
    i = 0
    for a in keha1:
        sarakeTulos[sarake] = keha1[i]
        sarakeTulos[sarake] += keha2[i]
        sarakeTulos[sarake] += keha3[i]
        sarakeTulos[sarake] += keha4[i]
        sarakeTulos[sarake] += keha5[i]
        i += 1
        sarake += 1
    print(sarakeTulos)

    oikeat_sarakkeet = 0  # 16 saraketta pitää saada
    for summa in sarakeTulos:
        if sarakeTulos[summa] == 46:
            oikeat_sarakkeet += 1
    print('oikeat sarakkeet: ', oikeat_sarakkeet)
    global maxOikeatSarakkeet
    if maxOikeatSarakkeet < oikeat_sarakkeet:
        maxOikeatSarakkeet = oikeat_sarakkeet

    if oikeat_sarakkeet == 16:  # Lopetetaan looppi jos 16 oikein
        print('Oikein!')
        print('kehä1: ', keha1)
        print('kehä2: ', keha2lista)
        print('keha3: ', keha3lista)
        print('keha4: ', keha4lista)
        print('keha5: ', keha5lista)
        exit()



for b in range(16):
    if b % 2 == 0:
        keha2lista = MuodostaYmpyra(keha2yla, keha2ala2, False)
    else:
        keha2lista = MuodostaYmpyra(keha2yla, keha2ala1, True)

    for c in range(16):
        if c % 2 == 0 and b % 2 == 0:
            keha3lista = MuodostaYmpyra(keha3yla, keha3ala2, False)
        elif c % 2 == 1 and b % 2 == 1:
            keha3lista = MuodostaYmpyra(keha3yla, keha3ala2, True)
        elif c % 2 == 0 and b % 2 == 1:
            keha3lista = MuodostaYmpyra(keha3yla, keha3ala1, False)
        elif c % 2 == 1 and b % 2 == 0:
            keha3lista = MuodostaYmpyra(keha3yla, keha3ala1, True)


        for d in range(16):
            if d % 2 == 0 and c % 2 == 0:
                keha4lista = MuodostaYmpyra(keha4yla, keha4ala2, False)
            elif d % 2 == 1 and c % 2 == 0:
                keha4lista = MuodostaYmpyra(keha4yla, keha4ala1, True)
            elif d % 2 == 0 and c % 2 == 1:
                keha4lista = MuodostaYmpyra(keha4yla, keha4ala1, False)
            elif d % 2 == 1 and c % 2 == 1:
                keha4lista = MuodostaYmpyra(keha4yla, keha4ala2, True)

            for e in range(16):
                if e % 2 == 0:
                    if d % 2 == 0:
                        keha5lista = MuodostaYmpyra(keha5yla, keha5ala2, False)

                    else:
                        keha5lista = MuodostaYmpyra(keha5yla, keha5ala1, False)
                    MoveFirstNumberToLast(keha5yla)
                else:
                    if d % 2 == 0:
                        keha5lista = MuodostaYmpyra(keha5yla, keha5ala1, True)
                    else:
                        keha5lista = MuodostaYmpyra(keha5yla, keha5ala2, True)
                LaskeSarakkeet(keha2lista, keha3lista, keha4lista, keha5lista)


                print('-------------')

            if d % 2 == 0:
                MoveFirstNumberToLast(keha4yla)
                MoveFirstNumberToLast(keha5ala1)
            else:
                MoveFirstNumberToLast(keha5ala2)

        if c % 2 == 0:
            MoveFirstNumberToLast(keha3yla)
            MoveFirstNumberToLast(keha4ala1)
        else:
            MoveFirstNumberToLast(keha4ala2)


    if b % 2 == 0:
        MoveFirstNumberToLast(keha2yla)
        MoveFirstNumberToLast(keha3ala1)
    else:
        MoveFirstNumberToLast(keha3ala2)


print('max oikeat sarakkeet: ', maxOikeatSarakkeet)