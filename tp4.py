# Créé par Utilisateur, le 24/09/2024 en Python 3.7
####################
#TP4               #
#Martin MAUTOUCHET #
#1ere4             #
####################

### Definitons des constantes ###

ecole = [ # format [nom_eleve,classe,maths,francais,lv1,histoire,sport]
['Jack','1B',12,15,11,17,17],
['Etienne','1A',12,15,7,9,18],
['Fred','1A',8,11,19,10,16],
['Celia','1A',11,9,15,10,9],
['Simon','1B',8,5,10,9,14],
['Eva','1B',11,15,14,11,17],
['Lea','1A',10,9,5,11,13],
['Taoufik','1A',11,16,16,12,17],
['Gedeon','1B',17,9,13,11,16],
['Ludo','1B',9,10,7,12,14],
['Titeuf','1A',7,12,11,13,9],
['Olive','1A',14,17,18,14,17],
['Yann','1B',12,12,15,10,15],
['Frank','1B',12,10,10,14,17],
['Tulio','1B',12,10,7,16,12],
['Marie','1B',10,11,12,13,14],
['Assa','1B',9,12,6,17,15],
['Xavier','1A',10,10,15,8,16],
['Nul','1A',2,4,3,1,6],
['Fort','1B',20,19,20,18,19]
]
matiereIndex = {"nom" : 0,"classe" : 1,"maths":2,"francais":3,"lv1":4,
"histoire":5,"sport":6,0 : "nom",1 : "classe",
2:"maths",3:"francais",4:"lv1",5:"histoire",6:"sport"}

### Definition des fonctions ###
def afficherListeEleve():
    """Afficher la liste des eleves de l'ecole
    param : aucun
    return : None
    """
    for eleve in ecole :
        print(eleve[0])

def afficherEleveClasse(classe):
    """Afficher la liste des eleves d'une classe
    param : classe:str
    return : None
    """
    for eleve in ecole :
        if eleve[1] == classe :
            print(eleve[0])

def afficherNotesEleve(eleveChoisi) :
    """Afficher les notes d'un eleve
    param : eleveChoisi:str
    return : None
    """
    for eleve in ecole :
        if eleve[0] == eleveChoisi :
            for i,elem in enumerate(eleve) :
                if i in [0,1] :
                    pass
                else :
                    print(f"L'eleve a {elem} en {matiereIndex[i]}")

def afficherNoteEleveMatiere(matiere) :
    """Afficher les notes de tous les eleves dans une matiere
    param : matiere:str
    return : None
    """
    index_ = matiereIndex[matiere]
    for eleve in ecole :
        print(f"{eleve[0]} : {eleve[index_]}")

def getNotes(eleveChoisi) :
    """renvoyer les notes de l'eleve choisi
    param : eleveChoisi:str
    return : notes:list
    """
    for eleve in ecole :
        if eleve[0] == eleveChoisi:
            return eleve[2:]

def moyenne(notesList):
    """renvoyer la moyenne d'une liste de notes
    param : notesList:list
    return : moyenne:float
    """
    sommenote = 0
    len_ = len(notesList)
    for note in notesList : #sum() est possible
        sommenote += note
    return sommenote/len_

def minNote(notesList) :
    """renvoyer la notes minimale d'une liste
    param : notesList:list
    return : min:int
    """
    min = 99999
    for note in notesList : #min() est possible
        if note<min :
            min = note
    return min

def maxNote(notesList) :
    """renvoyer la notes maximale d'une liste
    param : notesList:list
    return : max:int
    """
    max = -9999
    for note in notesList : #max() est possible
        if note>max :
            max = note
    return max

def variables(eleveChoisi) :
    """renvoyer les stats d'un eleve
    param : eleveChoisi:str
    return : stats:list
    """
    notes = getNotes(eleveChoisi)
    return [moyenne(notes),minNote(notes),maxNote(notes)]


def moyenneClasse(classe,matiere) :
    """renvoyer la moyenne d'une classe dans une matiere
    param : classe:str ; matiere:str
    return : moy:list
    """
    notes = []
    for eleve in ecole :
        if eleve[1] == classe.upper() :
            notes.append(eleve[matiereIndex[matiere.lower()]])
    return [moyenne(notes),classe.upper(),matiere.lower()]

def addmatiere():
    """Ajouter une matiere
    params : aucun
    return : aucun"""
    matierenom = str(input("nom de la matiere : ")).lower()
    index_ = len(ecole[0])
    matiereIndex[matierenom] = index_
    matiereIndex[index_] = matierenom
    for eleve in ecole :
        localNote = float()
        while 1 :
            try :
                localNote = float(input(f"Note pour {eleve[0]} : "))
                if not -1 <localNote< 21 :
                    raise Exception
                else : break
            except :
                print("Valeur incorrect, veuillez réessayez")
        eleve.append(localNote)


def addeleve():
    """Ajouter un eleve
    params : aucun
    return : aucun"""
    try :
        #utiliser une liste pour stocker au cas ou on leve une err au milieu du proc
        neweleve = list()
        nom = str(input("Entrez le nom du nouvel eleve : ")).capitalize()
        neweleve.append(nom)
        classe = str(input("Entrez la classe du nouvel eleve : ")).upper()
        neweleve.append(classe)
        for i in range(2,len(ecole[0])) :
            locnote = float()
            while 1 :
                try :
                    locnote = float(input(f"Entrez la note de l'eleve en {matiereIndex[i]} : "))
                    if not -1 <locnote< 21 :
                        raise Exception
                    else : break
                except :
                    print("Valeur incorrect, veuillez réessayez")
            neweleve.append(locnote)
    except Exception as err :
        print(f"Erreur inconnue lors de l'ajout de l'eleve : {err}")
    finally :
        ecole.append(neweleve)

def modfEleve():
    """Modifier les infos d'un eleve
    params : aucun
    return : aucun"""
    nom = str(input("Entrez le nom de l'eleve a modifier : ")).capitalize()
    modfeleve = list()
    eleveIndex = int()
    for i,eleve in enumerate(ecole) :
        if eleve[0] == nom :
            modfeleve = eleve
            eleveIndex = i
            break
    print("Informations de l'eleve : (Entrez le numero a modifier) ")
    print(f"0) Nom : {modfeleve[0]}")
    print(f"1) Classe : {modfeleve[1]}")
    for i,note in enumerate(eleve[2:]) :
        print(f"{i}) Note de {matiereIndex[i]} : {note}")
    choixmodf = int(input("Numero de la modification : "))
    nommodf = matiereIndex[choixmodf]
    if choixmodf == 0 or choixmodf == 1:
        new = str(input(f"Nouvelle valeur pour {nommodf} : "))
    else :
        new = float(input(f"Noouvelle note de {nommodf} : "))
    modfeleve[choixmodf] = new
    print(modfeleve)
    eleve[eleveIndex] = modfeleve
    print(ecole)




def menu():
    print("-"*50)
    print("""TP4 : Des listes de niveau supérieur
    1) Afficher la liste des eleves
    2) Afficher la liste d'une classe
    3) Afficher les notes d'un eleve
    4) Afficher les notes des eleves dans une matiere
    5) Afficher les stats d'un eleve moyenne generale, note min et max
    6) Afficher les stats de tous les eleves
    7) Afficher la moyenne de classe dans une matiere
    8) Afficher les eleves avec moins de 10 de moyennes
    9) Pour chaque eleve, afficher les matieres ou ils ont moins de 10
    10) Ajouter une matiere
    11) Ajouter un eleve
    12) modifier les informations d'un eleve
0) sortir
""")
    returner = str(input("Choix > ")).lower()
    return returner

### Programme principal ###

while 1: # executer le programme tant que possible

    choix = menu() # demander le choix de l'utilisateur

    if "0" == choix: # quitter la boucle si le choix est 0
        print("-"*50)
        print("Programme terminé.")
        break

    if choix == "1":
        print("###[Liste des eleves]###")
        #Afficher la liste des eleves
        try : afficherListeEleve()
        except Exception as err: print(f"Saisie invalide : {err}")

    elif choix == "2":
        #Afficher des eleves d une classe
        classe = str(input("Entrer une classe (1A ou 1B) : ")).upper()
        try :
            print(f"###[Liste de la classe {classe}]###")
            afficherEleveClasse(classe)
        except Exception as err: print(f"Saisie invalide : {err}")

    elif choix == "3":
        print("###[Notes d'un eleve]###")
        #Afficher les notes d'un eleve
        eleveChoisi = str(input("Entrez le nom d'un eleve : ")).capitalize()
        try :
            afficherNotesEleve(eleveChoisi)
        except Exception as err: print(f"Saisie invalide : {err}")

    elif choix == "4":
        print("###[Liste des notes dans une matiere]###")
        #Afficher les prenoms et la note dans une matiere
        matiere = str(input("Entrez une matiere : ")).lower()
        try :
            afficherNoteEleveMatiere(matiere)
        except Exception as err: print(f"Saisie invalide : {err}")

    elif choix == "5" :
        print("###[Statistiques d'un eleve]###")
        # Afficher les stats d'un eleve
        eleveChoisi = str(input("Entrez le nom d'un eleve : ")).capitalize()
        try :
            var = variables(eleveChoisi)
            print(f"{eleveChoisi} a une moyenne generale de {var[0]}")
            print(f"{eleveChoisi} a une note minimale de {var[1]}")
            print(f"{eleveChoisi} a une note maximale de {var[2]}")
        except Exception as err: print(f"Saisie invalide : {err}")

    elif choix == "6" :
        print("###[Statistiques des eleves]###")
        # Afficher les stats de tous les eleves
        try :
            for eleve in ecole :
                var = variables(eleve[0])
                print(f"{eleve[0]} a une moyenne generale de {var[0]}")
                print(f"{eleve[0]} a une note minimale de {var[1]}")
                print(f"{eleve[0]} a une note maximale de {var[2]}")
                print()
        except Exception as err: print(f"Saisie invalide : {err}")


    elif choix == "7" :
        print("###[Moyenne d'une classe dans une matiere]###")
        # Afficher la moyenne d'une classe dans une matiere
        classe = str(input("Entrez une classe (1A ou 1B) : ")).upper()
        matiere = str(input("Entrez une matiere : ")).lower()
        try :
            moyclass = moyenneClasse(classe,matiere)
            print(f"La moyenne de la {moyclass[1]} en {moyclass[2]} \
    est de {moyclass[0]}")
        except Exception as err: print(f"Saisie invalide : {err}")


    elif choix == "8" :
        print("###[Eleves avec un moyenne général < 10]###")
        # Afficher les eleves avec un moyenne <10
        try :
            for eleve in ecole :
                notes = eleve[2:]
                if moyenne(notes)<10 :
                    print(f"{eleve[0]} a moins de 10 de moyenne")
        except Exception as err: print(f"Saisie invalide : {err}")

    elif choix == "9" :
        print("###[Pour chaque eleve, liste des matieres ou il a moins de 10]###")
        #Pour chaque eleve, afficher les matieres ou il a moins de 10
        try :
            for eleve in ecole :
                for i in range(2,len(eleve)) :
                    if eleve[i] < 10:
                        print(f"{eleve[0]} a moins de 10 en {matiereIndex[i]}")
        except Exception as err: print(f"Saisie invalide : {err}")

    elif choix == "10" :
        print("###[Ajout d'une matiere]###")
        try :
            addmatiere()
        except Exception as err: print(f"Saisie invalide : {err}")

    elif choix == "11" :
        print("###[Ajout d'un eleve]###")
        try :
            addeleve()
        except Exception as err: print(f"Saisie invalide : {err}")

    elif choix == "12" :
        print("###[Modifier les infos d'un eleve]###")
        try :
            raise NotImplementedError("A faire !!!!!!")
            modfEleve()
        except Exception as err :
            print(f"Erreur inconnue lors de la modification des infos d'un eleve : {err}")

    else : #renvoyer une erreur si la valeur entree est incorrect
        print("Entrée incorrect, entrez une valeur valide !")



























































