class Erreur(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return repr(self.txt)


class Matrice(object):
    def __init__(self, mat):  # lignes : chaque ligne est une liste
        self.lignes = len(mat)  # le format de la matrice, pour detecter des erreurs
        self.colonnes = len(mat[0])  # on suppose que l'utilisateur est intelligent
        self.matrice = mat  # future liste de liste

    def __mul__(self, autreMatrice):  # multiplication matricielle
        if self.colonnes != autreMatrice.lignes:
            raise Erreur("format !!!")
        M = [[0 for k in range(autreMatrice.colonnes)] for k in range(self.lignes)]
        for i in range(self.lignes):
            for j in range(autreMatrice.colonnes):
                s = 0
                for k in range(self.colonnes):
                    s += self.matrice[i][k] * autreMatrice.matrice[k][j]
                M[i][j] = s

        return Matrice(M)  # on renvoie une Matrice et pas une liste (astuce !!!)
