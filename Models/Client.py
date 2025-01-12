import os

fichier_operateurs = "BD/Operateur.txt"
fichier_clients = "BD/Clients.txt"
fichier_index_orange = "BD/index_orange"
fichier_index_free = "BD/index_free"
fichier_index_expresso = "BD/index_expresso"
fichier_numeros_orange = "BD/numeros_orange"
fichier_numeros_free = "BD/numeros_free"
fichier_numeros_expresso = "BD/numeros_expresso"
fichier_credits = "BD/Credits.txt"


# 1.Fonction pour consulter du credit
def consulter_credit():
    """Permet au client de consulter son crédit en confirmant son code PIN."""
    
    # Demander le numéro de téléphone et le code PIN
    numero = input("Entrez votre numéro de téléphone : ").strip()
    code_pin = input("Entrez votre code PIN : ").strip()

    # Vérifier l'existence du fichier Clients.txt
    if not os.path.exists(fichier_clients):
        print(f"Erreur : Le fichier '{fichier_clients}' est introuvable.")
        return

    # Vérifier l'existence du fichier Credits.txt
    if not os.path.exists(fichier_credits):
        print(f"Erreur : Le fichier '{fichier_credits}' est introuvable.")
        return

    # Rechercher le client dans Clients.txt
    client_nom = None
    with open(fichier_clients, "r") as f_clients:
        for ligne in f_clients:
            ligne = ligne.strip()
            if numero in ligne and f"Code PIN: {code_pin}" in ligne:
                client_nom = ligne.split(" | ")[0]
                break

    if not client_nom:
        print("Erreur : Numéro ou code PIN incorrect.")
        return

    # Rechercher le crédit du client dans Credits.txt
    with open(fichier_credits, "r") as f_credits:
        for ligne in f_credits:
            ligne = ligne.strip()
            if ligne.startswith(client_nom):
                credit_actuel = ligne.split(":")[-1].strip()
                print(f"Bonjour {client_nom}, votre crédit actuel est de {credit_actuel} FCFA.")
                return

    # Si le crédit n'est pas trouvé
    print(f"Aucun crédit trouvé pour le client {client_nom}.")
