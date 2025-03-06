
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

# keha2vaihtoehto = 0 # parillinen tarkoittaa ala2 ja pariton ala1
# keha3vaihtoehto = 0
# keha4vaihtoehto = 0
# keha5vaihtoehto = 0
yritykset = 0
maxOikeatSarakkeet = 0

#tulosEnnenMuutosta = 0
#Jos ala1 on käytössä, niin tällöin se on lukittu aikaisempaan ylä kehän samaan indexiin, ei voi liikuttaa vapaasti.

def MuodostaYmpyra(ylalista, alalista, alaeka = False):
    yhdistettyLista = []
    i = 0
    print('---')
    if alaeka == False:
        for a in range(8):

            yhdistettyLista.append(ylalista[i])
            yhdistettyLista.append(alalista[i])
            i += 1
        print(yhdistettyLista)
        return yhdistettyLista
    else:
        for a in range(8):

            yhdistettyLista.append(alalista[i])
            yhdistettyLista.append(ylalista[i])
            i += 1
        print(yhdistettyLista)
        return yhdistettyLista


def MoveFirstNumberToLast(lista):
    talteen = lista[0]
    lista.pop(0)
    lista.append(talteen)


# def TarkistaSarakkeet(keha2ympyraKaytossa= 0, keha3ympyraKaytossa = 0, keha4ympyraKaytossa = 0, keha5ympyraKaytossa = 0):
#     oikeat_sarakkeet = 0
#     # 16 saraketta yhteensä, kaikkiin pitää saada summa 46
#     # while oikeat_sarakkeet != 16:
#     global yritykset
#
#     oikeaTulos = 46
#
#     yritykset += 1
#     print('Yritykset: ', yritykset)
#     sarake = 0
#     sarakeTulos = {}
#     alaI = 0  # käytetään arrayn läpi käymiseen
#     ylaI = 0  # käytetään arrayn läpi käymiseen
#     parillinenSarake = 1
#
#     for a in range(8):
#         # print('sarake:' + str(sarake + 1))
#         # if parillinenSarake % 2 == 1:
#         #     sarakeTulos[sarake] = 0
#         #     sarakeTulos[sarake] = a
#         #     sarakeTulos[sarake] += keha2yla[ylaI]
#         #     sarakeTulos[sarake] += keha3yla[ylaI]
#         #     sarakeTulos[sarake] += keha4yla[ylaI]
#         #     sarakeTulos[sarake] += keha5yla[ylaI]
#         #     ylaI += 1
#         # else:           #Tällä hetkellä tarkastetaan niin että ylä sarakkeet on parillisilla sarakkeilla ala parittomilla, KORJAA
#         sarakeTulos[sarake] = 0
#         sarakeTulos[sarake+1] = 0
#         sarakeTulos[sarake] = keha1[sarake]
#         sarakeTulos[sarake+1] = keha1[sarake+1]
#         if keha2ympyraKaytossa % 2 == 0:
#
#             sarakeTulos[sarake] += keha2yla[ylaI]
#             sarakeTulos[(sarake + 1)] += keha2ala2[alaI]
#         else:
#             sarakeTulos[sarake] += keha2ala1[alaI]
#             sarakeTulos[sarake+1] += keha2yla[ylaI]
#
#         if keha3ympyraKaytossa % 2 == 0:
#
#             sarakeTulos[sarake] += keha3yla[ylaI]
#             sarakeTulos[sarake + 1] += keha3ala2[alaI]
#         else:
#             sarakeTulos[sarake] += keha3ala1[alaI]
#             sarakeTulos[sarake + 1] += keha3yla[ylaI]
#
#         if keha4ympyraKaytossa % 2 == 0:
#
#             sarakeTulos[sarake] += keha4yla[ylaI]
#             sarakeTulos[sarake + 1] += keha4ala2[alaI]
#         else:
#             sarakeTulos[sarake] += keha4ala1[alaI]
#             sarakeTulos[sarake + 1] += keha4yla[ylaI]
#
#         if keha5ympyraKaytossa % 2 == 0:
#
#             sarakeTulos[sarake] += keha5yla[ylaI]
#             sarakeTulos[sarake + 1] += keha5ala2[alaI]
#         else:
#             sarakeTulos[sarake] += keha5ala1[alaI]
#             sarakeTulos[sarake + 1] += keha5yla[ylaI]
#         alaI += 1
#         ylaI += 1
#         # print(f'sarakkeen {sarake} summa: {str(sarakeTulos[sarake])}')
#         parillinenSarake += 1
#         sarake +=2
#
#
#     print(sarakeTulos)
#
#     oikeat_sarakkeet = 0 # 16 saraketta pitää saada
#     for summa in sarakeTulos:
#         if sarakeTulos[summa] == 46:
#
#             oikeat_sarakkeet += 1
#     print('oikeat sarakkeet: ',oikeat_sarakkeet)
#     global maxOikeatSarakkeet
#     if maxOikeatSarakkeet < oikeat_sarakkeet:
#         maxOikeatSarakkeet = oikeat_sarakkeet
#
#     if oikeat_sarakkeet == 16: # Lopetetaan looppi jos 16 oikein
#         # break
#         print('Oikein!')
#         exit()



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
        # break
        print('Oikein!')
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

                # TarkistaSarakkeet(keha5ympyraKaytossa=keha5vaihtoehto, keha4ympyraKaytossa=keha4vaihtoehto, keha3ympyraKaytossa=keha3vaihtoehto, keha2ympyraKaytossa=keha2vaihtoehto)
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