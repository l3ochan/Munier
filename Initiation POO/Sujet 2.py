class etudiant: #La classe étudiant va permettre de définir les attributs relatifs aux étudiant d'une promo
    def __init__(self,nom,prenom):  #Ici on va donc définir l'identité de l'étudiant et créer un tableau 
        self.nom = nom              #vide qui servira plus tard à stocker ses notes
        self.prenom = prenom
        self.notes = []
    
    def ajouterNote(self,note,coef): #Ici on va donc pouvoir ajouter une note au trableau de notes de l'étudiant
        noteWcoef = (note,coef)
        self.notes.append(noteWcoef)
        print(f"La note {note} qui a pour coefficient {coef} à bien été ajoutée au tableau de notes de {self.nom} {self.prenom}.")
        
    def nbNote(self): #Cette méthode (action) permet de compter les notes de l'étudiant
        return(f"Il y a {len(self.notes)} notes pour {self.nom} {self.prenom}.")
    
    def listNote(self): #cette méthode permet d'énumérer les notes et les coefs pour un étudiant donné 
        for NoteCoef in self.notes:
            print(f"{NoteCoef}\n")
    
    def moyenne(self): #Cette méthode permet de calculer la moyenne pondérée d'un étudiant. 
        TotalNote = 0
        TotalCoef = 0
        if not self.notes: 
            print("Aucune note pour cet étudiant")
        else:
            for NoteCoef in self.notes:
                TotalNote += NoteCoef[0]*NoteCoef[1]
                TotalCoef += NoteCoef[1]
            moyenne = round(TotalNote/TotalCoef,2)
            return (f"La moyenne de {self.nom} {self.prenom} est de {moyenne}")

class promotion:
    def __init__(self, nomPromo):
        self.nomPromo = nomPromo
        self.indexEtudiant = []

    def ajouterEtudiant(self, etudiant):
        self.indexEtudiant.append(etudiant)
        return(f"{etudiant.nom} {etudiant.prenom} ajouté avec succès à la promotion intitulée {self.nomPromo}.")
        
    def nbEtudiant(self): #Cette méthode (action) permet de compter les notes de l'étudiant
        return(f"Il y a {len(self.indexEtudiant)} dans la promotion intitulée {self.nomPromo}")
    
    def moyennePromo(self):
        