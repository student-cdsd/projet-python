import random
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

# Fonction pour créer les index associés à un opérateur
def creation_index(operateur):
    index_max = 3  
    index_min = 1  
    print(f"Ajout des index pour l'opérateur : {operateur}")
    index_operateurs = []

    while len(index_operateurs) < index_max:
        index = input(f"Entrer un index (2 chiffres) pour l'opérateur {operateur} (ou tapez 'stop' pour terminer) : ")

        if index.lower() == "stop":  # Arrêter l'ajout d'index
            if len(index_operateurs) >= index_min:  # Vérifie qu'au moins un index a été ajouté
                break  # Sortir de la boucle principale
            else:
                print(f"Erreur : Vous devez ajouter au moins {index_min} index.")
                continue

        if index.isdigit() and len(index) == 2 and 30 <= int(index) <= 78:
            index = int(index)
            if index not in index_operateurs:
                index_operateurs.append(index)
                remaining = index_max - len(index_operateurs)
                print(f"Index {index} ajouté avec succès. Il vous reste {remaining} index à ajouter.")
            else:
                print(f"L'index {index} a déjà été ajouté.")
        else:
            print("Erreur : Entrez un index valide (2 chiffres entre 30 et 78) ou tapez 'stop'.")

        # Propose de continuer ou non
        if len(index_operateurs) < index_max:
            continuer = input(f"Voulez-vous ajouter un autre index ? (oui/non) : ").lower()
            if continuer != "oui":
                if len(index_operateurs) >= index_min:
                    break  # Sortir de la boucle principale
                else:
                    print(f"Erreur : Vous devez ajouter au moins {index_min} index.")
                    continue

    # Appel de la fonction pour générer les numéros
    if index_operateurs:
        numeros = generer_numeros(index_operateurs)
        print(f"Numéros générés pour l'opérateur {operateur} :")
        for numero in numeros:
            print(numero)

    return index_operateurs

# Fonction pour générer 100 numéros uniques à 7 chiffres pour chaque index
def generer_numeros(index_operateurs):
    numeros = []
    id_compteur = 1  # Début des IDs à 1
    
    for index in index_operateurs:
        print(f"Génération des numéros pour l'index {index}...")
        for _ in range(100):  # 100 numéros par index
            while True:
                numero = f"{index}{random.randint(1000000, 9999999)}"
                if numero not in numeros:  # Vérifie l'unicité
                    break
            
            # Ajout de l'ID et du numéro formaté
            numeros.append(f"({id_compteur:03}) {numero}")
            id_compteur += 1  # Incrément de l'ID
    
    return numeros

# Fonction pour ajouter uniquement le nom de l'opérateur dans le fichier
def ecrire_operateur(nouveau_operateur):
    with open(fichier_operateurs, "a") as f:
        f.write(f"{nouveau_operateur}\n")

# Fonction principale pour créer un opérateur
def creation_operateur():
    while True:
        nouveau_operateur = input("Entrez le nom d'un nouveau opérateur (entre 3 et 15 caractères) : ").strip()

        if 3 <= len(nouveau_operateur) <= 15:
            with open(fichier_operateurs, "r") as f:
                lignes = [ligne.strip() for ligne in f.readlines()]

            # Vérifie si l'opérateur existe déjà dans le fichier
            operateurs_existants = [ligne.split(" | ")[0] for ligne in lignes]
            if nouveau_operateur in operateurs_existants:
                print(f"L'opérateur {nouveau_operateur} existe déjà.")
            else:
                # Appelle la fonction pour créer des index
                index_operateurs = creation_index(nouveau_operateur)

                # Enregistre les index dans le fichier correspondant à l'opérateur
                fichier_index = f"BD/index_{nouveau_operateur.lower()}.txt"
                with open(fichier_index, "w") as f_index:
                    for index in index_operateurs:
                        f_index.write(f"{index}\n")

                # Appelle la fonction pour générer les numéros pour les index
                numeros = generer_numeros(index_operateurs)

                # Enregistre les numéros dans le fichier correspondant à l'opérateur
                fichier_numeros = f"BD/numeros_{nouveau_operateur.lower()}.txt"
                with open(fichier_numeros, "w") as f_numeros:
                    for numero in numeros:
                        f_numeros.write(f"{numero}\n")

                # Enregistre uniquement le nom de l'opérateur dans le fichier des opérateurs
                ecrire_operateur(nouveau_operateur)

                print(f"L'opérateur {nouveau_operateur} avec ses index et numéros a été ajouté avec succès.")

                # Demander si l'utilisateur souhaite ajouter un autre opérateur
                while True:
                    choix = input("Voulez-vous ajouter un autre opérateur ? (oui/non) : ").strip().lower()
                    if choix == "oui":
                        break  # Retourne au début de la boucle principale
                    elif choix == "non":
                        print("Fin du programme. À bientôt !")
                        return
                    else:
                        print("ERREUR ! Veuillez répondre par 'oui' ou 'non'.")
        else:
            print("ERREUR ! Le nom de l'opérateur doit contenir entre 3 et 15 caractères.")
            
# 2.Fonction pour renommer un opérateur
def renommer_operateur():
    # Lecture des opérateurs existants
    with open(fichier_operateurs, "r") as f:
        lignes = f.read().splitlines()

    if not lignes:  
        print("Aucun opérateur n'existe dans le fichier.")
        return

    # Affichage des opérateurs existants
    print("Liste des opérateurs existants :")
    operateurs_existants = [ligne.split(" | ")[0] for ligne in lignes]
    for i in range(len(operateurs_existants)):
        print(f"{i + 1}. {operateurs_existants[i]}")

    # Demande de l'opérateur à renommer 
    while True:
        choix = input("Entrez le nom de l'opérateur à renommer : ").strip()
        if choix in operateurs_existants:
            break
        print(f"Erreur : L'opérateur '{choix}' n'existe pas. Veuillez réessayer.")

    # Demande du nouveau nom 
    while True:
        nouveau_nom = input("Entrez le nouveau nom de l'opérateur : ").strip()
        if len(nouveau_nom) < 3 or len(nouveau_nom) > 15:
            print("Erreur : Le nom doit contenir entre 3 et 15 caractères.")
        elif nouveau_nom in operateurs_existants:
            print(f"Erreur : Un opérateur nommé '{nouveau_nom}' existe déjà.")
        else:
            break 

    # Modification et sauvegarde
    with open(fichier_operateurs, "w") as f:
        for ligne in lignes:
            elements = ligne.split(" | ")
            operateur = elements[0]
            rest = elements[1:]
            if operateur == choix:
                f.write(f"{nouveau_nom} | {' | '.join(rest)}\n")
            else:
                f.write(ligne + "\n")

    print(f"L'opérateur '{choix}' a été renommé en '{nouveau_nom}' avec succès.")

# 3.Fontion qui nous permet de lister les operateurs et leurs index
def afficher_operateurs_et_index():
    # Lecture du fichier
    with open(fichier_operateurs, "r") as f:
        lignes = f.read().splitlines()

    # Vérification si le fichier est vide
    if not lignes:
        print("Aucun opérateur n'existe dans le fichier.")
        return

    # Construction du tableau
    print(f"{'Opérateur':<15} {'Index':<10}")
    print("-" * 25)
    for ligne in lignes:
        elements = ligne.split(" | ")
        operateur = elements[0]
        indices = elements[1]  # Les index sont dans la deuxième position
        print(f"{operateur:<15} {indices}")

# 4.Fonction pour Lister les numéros d’un opérateur existant
def lister_numeros_generes():
    # Demander le nom de l'opérateur
    operateur = input("Entrez le nom de l'opérateur : ").strip()

    # Lire le fichier
    with open(fichier_operateurs, "r") as f:
        lignes = f.read().splitlines()

    # Vérifier et afficher les numéros générés pour l'opérateur
    for ligne in lignes:
        elements = ligne.split(" | ")
        if elements[0] == operateur:
            numeros = elements[2]  # Les numéros générés
            print(f"Numéros générés pour {operateur}:")
            print(numeros)  # Affiche tous les numéros générés sur une ligne
            return  # Sortir après avoir trouvé et affiché les numéros

    # Si l'opérateur n'est pas trouvé
    print(f"Opérateur '{operateur}' non trouvé.")

# 5.Fonction pour ajouter un nouvel index à un opérateur existant
def ajouter_index_operateur():
    # Demander à l'utilisateur de choisir un opérateur existant
    with open(fichier_operateurs, "r") as f:
        operateurs_existants = [ligne.strip() for ligne in f.readlines()]
    
    print("Liste des opérateurs existants :")
    for i, operateur in enumerate(operateurs_existants, start=1):
        print(f"{i}. {operateur}")
    
    choix = input("Entrez le nom de l'opérateur auquel vous souhaitez ajouter un index : ").strip()

    if choix not in operateurs_existants:
        print(f"Erreur : L'opérateur '{choix}' n'existe pas.")
        return

    # Demander à l'utilisateur un nouvel index
    nouvel_index = input("Entrez un nouvel index (entre 30 et 78) : ").strip()
    
    if not (nouvel_index.isdigit() and 30 <= int(nouvel_index) <= 78):
        print("Erreur : L'index doit être un nombre entre 30 et 78.")
        return

    # Générer les numéros pour cet index
    nouveaux_numeros = generer_numeros([int(nouvel_index)])

    # Charger les numéros existants pour vérifier les IDs
    fichier_numeros = f"BD/numeros_{choix.lower()}.txt"
    if os.path.exists(fichier_numeros):
        with open(fichier_numeros, "r") as f:
            numeros_existants = [num.strip() for num in f.readlines()]

        # Extraire les IDs existants
        ids_existants = set(num.split(" ")[0][1:-1] for num in numeros_existants)

        # Vérifier les IDs des nouveaux numéros
        for i, numero in enumerate(nouveaux_numeros):
            # Extraire l'ID du numéro généré
            id_num = numero.split(" ")[0][1:-1]
            # Si l'ID est déjà pris, le générer à nouveau (réessayer)
            while id_num in ids_existants:
                id_num = str(int(id_num) + 1)  # Incrémenter l'ID pour garantir l'unicité
                nouveaux_numeros[i] = numero.replace(f"({numero.split(' ')[0][1:-1]})", f"({id_num})")
                ids_existants.add(id_num)  # Ajouter le nouvel ID à la liste des IDs existants

    # Ajouter l'index et les numéros dans les fichiers correspondants
    fichier_index = f"BD/index_{choix.lower()}.txt"
    
    with open(fichier_index, "a") as f_index:
        f_index.write(f"{nouvel_index}\n")

    with open(fichier_numeros, "a") as f_numeros:
        for numero in nouveaux_numeros:
            f_numeros.write(f"{numero}\n")

    print(f"L'index {nouvel_index} et ses numéros ont été ajoutés à l'opérateur '{choix}' avec succès.")

# 6. A revoir pour des modifications Fonction pour supprimer l'index d'un opérateur existant
def supprimer_index_operateur():
    # Demander à l'utilisateur de choisir un opérateur existant
    with open(fichier_operateurs, "r") as f:
        operateurs_existants = [ligne.strip() for ligne in f.readlines()]

    print("Liste des opérateurs existants :")
    for i, operateur in enumerate(operateurs_existants, start=1):
        print(f"{i}. {operateur}")

    choix = input("Entrez le nom de l'opérateur dont vous voulez supprimer un index : ").strip()

    if choix not in operateurs_existants:
        print(f"Erreur : L'opérateur '{choix}' n'existe pas.")
        return

    # Demander à l'utilisateur l'index à supprimer
    fichier_index = f"BD/index_{choix.lower()}.txt"
    with open(fichier_index, "r") as f:
        indices_existants = [ligne.strip() for ligne in f.readlines()]

    if not indices_existants:
        print(f"Aucun index trouvé pour l'opérateur '{choix}'.")
        return

    print("Index existants pour cet opérateur :")
    for i, index in enumerate(indices_existants, start=1):
        print(f"{i}. {index}")

    index_a_supprimer = input("Entrez l'index à supprimer : ").strip()

    if index_a_supprimer not in indices_existants:
        print(f"Erreur : L'index {index_a_supprimer} n'existe pas pour l'opérateur '{choix}'.")
        return

    # Supprimer l'index du fichier d'index
    indices_existants.remove(index_a_supprimer)
    with open(fichier_index, "w") as f:
        for index in indices_existants:
            f.write(f"{index}\n")

    # Supprimer les numéros associés à cet index dans le fichier de numéros
    fichier_numeros = f"BD/numeros_{choix.lower()}.txt"
    with open(fichier_numeros, "r") as f:
        numeros_existants = [ligne.strip() for ligne in f.readlines()]

    # Filtrer les numéros qui ne correspondent pas à l'index supprimé
    nouveaux_numeros = [numero for numero in numeros_existants if not numero.startswith(index_a_supprimer)]

    # Écrire les numéros restants dans le fichier de numéros
    with open(fichier_numeros, "w") as f:
        for numero in nouveaux_numeros:
            f.write(f"{numero}\n")

    print(f"L'index {index_a_supprimer} et ses numéros ont été supprimés de l'opérateur '{choix}' avec succès.")

# 7.Fonction pour vendre un numero
def vendre_numero():
    
    fichiers_numeros = {
    "orange": "BD/numeros_orange.txt",
    "free": "BD/numeros_free.txt",
    "expresso": "BD/numeros_expresso.txt"
}

    # Charger les opérateurs
    if not os.path.exists(fichier_operateurs):
        print(f"Erreur : Le fichier '{fichier_operateurs}' est introuvable.")
        return

    with open(fichier_operateurs, "r") as f:
        operateurs = [op.strip().lower() for op in f.readlines()]

    if not operateurs:
        print("Erreur : Aucun opérateur n'est disponible.")
        return

    # Choisir un opérateur
    print("Opérateurs disponibles :", ", ".join(operateurs))
    while True:
        choix = input("Entrez le nom de l'opérateur : ").strip().lower()
        if choix in operateurs:
            break
        print("Erreur : Opérateur invalide.")

    # Charger les numéros pour l'opérateur
    fichier_numeros = fichiers_numeros.get(choix)
    if not fichier_numeros or not os.path.exists(fichier_numeros):
        print(f"Erreur : Fichier des numéros pour l'opérateur '{choix}' introuvable.")
        return

    with open(fichier_numeros, "r") as f:
        numeros = [num.strip() for num in f if "vendu" not in num]

    if not numeros:
        print(f"Aucun numéro disponible pour l'opérateur '{choix}'.")
        return

    # Afficher les numéros disponibles
    print(f"Numéros disponibles pour '{choix}':")
    for num in numeros:
        id_num = num.split(" ")[0][1:-1]  # Extraire l'ID entre parenthèses
        print(f"{id_num}: {num}")

    # Choisir un numéro
    while True:
        choix_id = input("Entrez l'ID du numéro à vendre : ").strip()
        numero_choisi = next((num for num in numeros if f"({choix_id})" in num), None)
        if numero_choisi:
            break
        print("Erreur : ID invalide ou numéro indisponible.")

    # Demander le nom du client
    client = input("Entrez le nom du client : ").strip()
    if not client:
        print("Erreur : Le nom du client est obligatoire.")
        return

    # Demander un code PIN pour le client
    while True:
        code_pin = input("Entrez un code PIN pour le client (4 chiffres) : ").strip()
        if code_pin.isdigit() and len(code_pin) == 4:
            break
        print("Erreur : Le code PIN doit être un nombre à 4 chiffres.")

    print(f"Le numéro {numero_choisi} a été vendu au client {client} avec le code PIN {code_pin}.")

    # Mettre à jour le fichier des numéros
    with open(fichier_numeros, "w") as f:
        for num in numeros:
            if num == numero_choisi:
                f.write(f"{num} (vendu)\n")
            else:
                f.write(f"{num}\n")

    # Enregistrer dans le fichier des clients avec le code PIN
    with open(fichier_clients, "a") as f:
        f.write(f"{client} | {numero_choisi} | Code PIN: {code_pin}\n")

    print("La vente a été enregistrée avec succès.")

#8.Fonction pour vendre du credit
def trouver_client_par_numero(numero_choisi):
    """ Recherche d'un client par son numéro dans le fichier Clients.txt """
    with open(fichier_clients, "r") as f:
        for ligne in f.readlines():
            ligne = ligne.strip()
            if numero_choisi.strip() in ligne:
                client, numero, code_pin = ligne.split('|')
                client = client.strip()
                numero = numero.strip()
                code_pin = code_pin.strip()
                return client, numero, code_pin
    return None, None, None

def vendre_credit():
    """ Fonction pour vendre du crédit à un client """
    # Saisie du numéro de téléphone pour la vente
    numero_choisi = input("Entrez le numéro du client pour lequel vous souhaitez vendre du crédit : ").strip()

    # Recherche du client correspondant
    client, numero, code_pin = trouver_client_par_numero(numero_choisi)

    if not client:
        print(f"Erreur : Aucun client trouvé pour le numéro {numero_choisi}.")
        return

    # Saisie du montant du crédit
    montant = input("Entrez le montant du crédit à acheter (min 100) : ").strip()

    # Vérification que le montant est un nombre valide
    if not montant.replace('.', '', 1).isdigit() or montant.count('.') > 1:
        print("Erreur : Le montant doit être un nombre valide.")
        return

    montant = float(montant)

    if montant < 100:
        print("Erreur : Le montant minimal est de 100.")
        return

    # Vérifier le crédit existant du client
    credit_existant = 0
    with open(fichier_credits, "r") as f:
        for ligne in f.readlines():
            if ligne.startswith(client):
                parts = ligne.split('|')
                credit_existant = float(parts[1].strip().split(' ')[-1])  # Crédit existant

    # Ajouter le nouveau crédit
    credit_total = credit_existant + montant

    # Mettre à jour le fichier des crédits avec le nouveau solde
    with open(fichier_credits, "r") as f:
        lines = f.readlines()

    with open(fichier_credits, "w") as f:
        for ligne in lines:
            if ligne.startswith(client):
                f.write(f"{client} | Crédit actuel : {credit_total}\n")
            else:
                f.write(ligne)

    # Enregistrer la vente de crédit dans le fichier des clients
    with open(fichier_credits, "a") as f:
        f.write(f"{client} | Crédit acheté : {montant} | Numéro vendu : {numero_choisi}\n")

    print(f"La vente de crédit pour le numéro {numero_choisi} a été enregistrée avec succès.")
    print(f"Nouveau solde du client {client} : {credit_total:.2f} (après ajout du crédit)")

    # Demander si le client souhaite effectuer un transfert
    transferer = input("Souhaitez-vous effectuer un transfert de crédit ? (oui/non) : ").strip().lower()

    if transferer == "oui":
        # Saisie du numéro du destinataire
        numero_destinataire = input("Entrez le numéro du destinataire : ").strip()

        # Vérifier si le destinataire existe
        client_destinataire, numero, code_pin = trouver_client_par_numero(numero_destinataire)

        if not client_destinataire:
            print(f"Erreur : Aucun client trouvé pour le numéro {numero_destinataire}.")
            return

        # Demander le montant à transférer
        montant_transfert = input(f"Entrez le montant du crédit à transférer au client {client_destinataire} : ").strip()

        # Vérification que le montant du transfert est un nombre valide
        if not montant_transfert.replace('.', '', 1).isdigit() or montant_transfert.count('.') > 1:
            print("Erreur : Le montant du transfert doit être un nombre valide.")
            return

        montant_transfert = float(montant_transfert)

        if montant_transfert <= 0:
            print("Erreur : Le montant du transfert doit être supérieur à zéro.")
            return

        # Vérifier si le montant à transférer est inférieur ou égal au crédit disponible
        if montant_transfert > credit_total:
            print("Erreur : Le montant à transférer est supérieur au crédit disponible.")
            return

        # Mettre à jour les crédits de l'expéditeur et du destinataire
        credit_total_expediteur = credit_total - montant_transfert
        credit_total_destinataire = 0

        # Mettre à jour le crédit de l'expéditeur
        with open(fichier_credits, "r") as f:
            lines = f.readlines()

        with open(fichier_credits, "w") as f:
            for ligne in lines:
                if ligne.startswith(client):
                    f.write(f"{client} | Crédit actuel : {credit_total_expediteur}\n")
                else:
                    f.write(ligne)

        # Mettre à jour le crédit du destinataire
        with open(fichier_credits, "r") as f:
            lines = f.readlines()

        with open(fichier_credits, "w") as f:
            for ligne in lines:
                if ligne.startswith(client_destinataire):
                    parts = ligne.split('|')
                    credit_destinataire = float(parts[1].strip().split(' ')[-1])
                    credit_total_destinataire = credit_destinataire + montant_transfert
                    f.write(f"{client_destinataire} | Crédit actuel : {credit_total_destinataire}\n")
                else:
                    f.write(ligne)

        print(f"Le transfert de crédit de {montant_transfert} a été effectué avec succès.")
        print(f"Le nouveau solde de l'expéditeur {client} est de {credit_total_expediteur:.2f}.")
        print(f"Le nouveau solde du destinataire {client_destinataire} est de {credit_total_destinataire:.2f}.")

# 9. Fonction pour voir l'Etat de la caisse
def etat_caisse():
    # Demander à l'utilisateur de saisir l'opérateur
    operateur = input("Entrez le nom de l'opérateur : ").strip().lower()

    # Demander à l'utilisateur le montant de départ de la caisse
    montant_depart = input(f"Entrez le montant de départ de la caisse pour l'opérateur '{operateur}' : ").strip()

    # Vérifier que le montant est un nombre valide
    if not montant_depart.isdigit():
        print("Erreur : Le montant de départ doit être un nombre.")
        return

    montant_depart = float(montant_depart)

    # Demander le montant de la vente de crédit
    montant_vente = input(f"Entrez le montant de la vente de crédit pour l'opérateur '{operateur}' : ").strip()

    # Vérifier que le montant de la vente est un nombre valide
    if not montant_vente.isdigit():
        print("Erreur : Le montant de la vente doit être un nombre.")
        return

    montant_vente = float(montant_vente)

    # Calculer l'état de la caisse après la vente
    nouvel_etat_caisse = montant_depart + montant_vente

    # Afficher le nouveau solde de la caisse
    print(f"L'état de la caisse pour l'opérateur '{operateur}' après la vente est de : {nouvel_etat_caisse:.2f}")
