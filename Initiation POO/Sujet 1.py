nom = None
prenom = None
note_ajotuer = None
note = []
Etudiant = (nom,prenom,note)
index_etudiants = []

def creerEtudiant(nom,prenom):
    note = []
    Etudiant = (nom,prenom,note)
    index_etudiants.append(Etudiant)
    return(index_etudiants)

def enregistrerNote(nom, prenom, note_ajouter):
    for i, etudiant in enumerate(index_etudiants):
        if nom == etudiant[0] and prenom == etudiant[1]:
            Etudiant_edit = etudiant[:3] + (etudiant[3] + [int(note_ajouter)])
            index_etudiants[i] = Etudiant_edit
            print(f"Note {note_ajouter} ajoutée pour {prenom} {nom}.")
            break