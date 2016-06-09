from matrice import *

# premier chiffrement de Hill, basique

A = Matrice([[1, 0], [0,
                      -1]])  # la matrice CLEF, une involution classique (p projecteur ssi 2p-Id est une symetrie), dans Z/256Z (nombres de caracteres ascii)


def encode(X):  # X est un vecteur ligne, deja de type Matrice
    return X * A


def decode(Y):
    return Y * A


def texteToVectList(texte):
    txt = list(texte)
    listeVecteurs = []
    v = []  # petit vecteur de taille 2 qu'on agrandit a chaque etape, et qu'on reinitialise quand il est plein
    n = len(txt)
    for k in range(n + 1):

        if k == n and k % 2 == 1:  # cas ou n est impair et qu'il reste une lettre, auquel cas on la met dans un vecteur (lettre, .)
            v = [[ord(txt[k - 1]), ord(".")]]
            listeVecteurs.append(Matrice(v))
        elif k == n and k % 2 == 0:  # on a fini, mettre un break eventuellement
            lol = 0
        elif k % 2 == 0:  # on reinitialise v
            v = [[ord(txt[k])]]
        else:
            v[0].append(ord(txt[k]))
            listeVecteurs.append(Matrice(v))
    return listeVecteurs


def vectListToText(vectList):  # self-explanatory
    texte = ""
    for k in range(len(vectList)):
        texte = texte + chr(vectList[k].matrice[0][0] % 255) + chr(vectList[k].matrice[0][1] % 255)
    return texte


def encodeTexte(texte):  # idem
    vecteurs = texteToVectList(texte)
    vecteursEncodes = [encode(X) for X in vecteurs]
    return vectListToText(vecteursEncodes)


def decodeTexte(texte):  # idem
    vecteurs = texteToVectList(texte)
    vecteursDecodes = [decode(X) for X in vecteurs]
    return vectListToText(vecteursDecodes)


"""PARTIE DE TESTS

testInput = open("/Users/JF/PycharmProjects/tipe/Hill/Tests/input.txt","r")
testOutput = open("/Users/JF/PycharmProjects/tipe/Hill/Tests/output.txt","r+")
testOutputDecode = open("/Users/JF/PycharmProjects/tipe/Hill/Tests/outputDecode.txt","w")
input = testInput.read()
output = encodeTexte(input)
testOutput.write(output)

inpute = testOutput.read()
outpute= decodeTexte(inpute)
testOutputDecode.write(outpute)"""
