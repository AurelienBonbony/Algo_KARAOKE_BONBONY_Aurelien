class player:
    def __init__(self, playername, identifiant, score, scoremoyen, scoretotal):
        self.__playername = playername
        self.__identifiant = identifiant
        self.__score = score
        self.__scoremoyen = scoremoyen
        self.__scoretotal = scoretotal
    def GetPlayername(self):
        return self.__playername
    def GetIdentifiant(self):
        return self.__identifiant    
    def GetScore(self):
        return self.__score
    def GetScoremoyen(self):
        return self.__scoremoyen
    def GetScoreTotal(self):
        return self.__scoretotal



    def ScoreInitial(self,score):
        self.__score = 0 
        return self.__score
    def GagneScore(self,score):
        self.__score += score
        return  self.__score
    def IdentifiantMusique(self, identifiant):
        self.__identifiant = [0,1,2,3,4]

Joueur = input("Quel est votre nom ? :\n")
Playername = player(Joueur)

print(" Très bien ", Joueur.GetPlayername(), "allons chercher ta musique !")

Identifiant = input("Quelle musique choississez-vous entre 0 et 4 ? :\n")
ChoixJoueur = player(Identifiant)

defaite = False
victoire = False
