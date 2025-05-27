class Utilisateur:
    def __init__(self, nom, id_utilisateur):
        self.nom = nom
        self.id_utilisateur = id_utilisateur

    def __str__(self):
        return f"{self.nom} (ID: {self.id_utilisateur})"
