from livre import Livre
from utilisateur import Utilisateur
from bibliotheque import Bibliotheque

livre1 = Livre("Python Facile", "Alice")
utilisateur1 = Utilisateur("Yassine", 1)

biblio = Bibliotheque()
biblio.ajouter_livre(livre1)
biblio.ajouter_utilisateur(utilisateur1)
biblio.afficher_livres()
biblio.afficher_utilisateurs()
