# Projet python - Gestion des operateurs telephoniques et des abonnes

Ceci est un devoir de fin de semestre 3 pour en PYTHON. Il s'agit de la gestion des operateurs telephoniques et des abonnes.


## Table des matieres

- [Apercu](#overview)
  - [Le challenge](#le-challenge)
  - [Les roles et permissions de chaque utilisateurs](#les-roles-et-permissions-de-chaque-utilisateurs)
  - [Regles de gestions](#regles-de-gestions)
- [Notre processus](#notre-processus)
  - [Technologies utilisee](#technologies-utilisee)
  - [Ce que nous avons appris](#ce-que-nous-avons-appris)
  - [Ressources utiles](#ressources-utiles)
- [Auteurs](#auteurs)


## Apercu

### Le challenge

Proposer une applica.on de ges.on d’opérateurs télécom et leurs clients.
Pour u.liser l’applica.on, on doit se connecter. Il existe trois profils :
- L’administrateur des fichiers
- Les ges.onnaires
- Les clients
- [Apercu](#overview)
  - [Le challenge](#le-challenge)
  - [Les roles et permissions de chaque utilisateurs](#les-roles-et-permissions-de-chaque-utilisateurs)
  - [Regles de gestions](#regles-de-gestions)
- [Notre processus](#notre-processus)
  - [Technologies utilisee](#technologies-utilisee)
  - [Ce que nous avons appris](#ce-que-nous-avons-appris)
  - [Ressources utiles](#ressources-utiles)
- [Auteurs](#auteurs)

### Les roles et permissions de chaque utilisateurs

- L'administrateur des fichiers: Il ne se connecte pas à l’applicayion mais utulise directement les fichiers de
données pour les manipuler. C’est lui qui ajoute les utilisateurs de l’applications
directement dans le fichier.
Ils meAent aussi tous les paramétrages et les constantes de l’application

- Les gestionnaires: Ils gèrent la par.e OPERATEURS. Ils ont les fonc.onnalités suivantes :
  - Se connecter
  - Se déconnecter
  - Créer un operateur
  - Renommer un opérateur
  - Lister les opérateurs et leur index
  - Lister les numéros d’un operateur
  - Ajouter un nouvel index pour un operateur existant
  - Supprimer un index d’un operateur
  - Vendre un numéro
  - Vendre du crédit a un client
  - État de la caisse :
  o État du jour / operateur
  o État du mois / operateur
  o État de l’année / operateur
- Les clients: Ce sont les abonnes des operateus. Ils ont les fonctionnalites suivantes:
  - Se connecter (par numero de telephone et un code pin de 4 chiffres)
  - Consulte son credit: Le client doit confirmer son code pin pour afficher son solde
  - Acheter du credit (chez le gestionnaire)
  - Effectuer un appel
  - Voir l’historique des appels (vocaux) avec une couleur pour les vocaux qui ne sont pas
encore lus.
  - Écouter un vocal
  - Supprimer un vocal
  - Ajouter un contact
  - Supprimer un contact
  - Renommer un contact
  - Ajouter un autre numéro a u contact existant
  - Afficher le répertoire
  - Recherche un contact du répertoire par un mot clé
  - Bloquer / débloquer un contact (Les contacts bloquer sont en rouge dans le
  répertoire)
  - Transférer du crédit

- [Apercu](#overview)
  - [Le challenge](#le-challenge)
  - [Les roles et permissions de chaque utilisateurs](#les-roles-et-permissions-de-chaque-utilisateurs)
  - [Regles de gestions](#regles-de-gestions)
- [Notre processus](#notre-processus)
  - [Technologies utilisee](#technologies-utilisee)
  - [Ce que nous avons appris](#ce-que-nous-avons-appris)
  - [Ressources utiles](#ressources-utiles)
- [Auteurs](#auteurs)

### Regles de gestions

- Les noms des opérateurs sont uniques
- Les noms des opérateurs doivent avoir au minimum 3 caractères et au maximum 15
caractères. 
- Chaque opérateur peut avoir au minimum 1 et au maximum 3 index
- Lors de la créa.on d’un opérateur, par défaut on lui génère 100 numéros pour chaque
index.
- Un index doit être un nombre de 2 chiffres
- Pour un opérateur, chaque numéro est unique
- Un numéro appar.ent à un et un seul client
- Un numéro doit avoir exactement 7 chiffres en plus de l’index de l’opérateur
- Le montant minimal de crédit à acheter est de 100 ainsi que pour le transfert
- Chaque transfert de crédit, le client paye 10% du montant à transférer.
- Chaque opérateur a ses tarifs d’appels :
o Appel entre mêmes operateurs
o Appel entre operateurs différents
- Lors d’un appel, si le numéro existe et que le client a assez de crédit, on doit entendre
l’appareil sonner et un message « appuyer sur D pour enregistrer le vocal »
- Le vocal s’arrête si l’u.lisateur veut raccrocher ou bien que son crédit s’épuise.
- Le transfert de crédit se fait qu’entre numéros de même operateur
- Un contact peut avoir minimum 1 numéro maximum 3 numéros.
- La suppression d’un index d’un operateur est possible que si l’opérateur n’a pas encore
de client pour l’index choisi.
- La suppression d’un index supprime aussi les numéros de l’index
- Deux index ne peuvent pas avoir le même index
- L’ajout de nouvel index à un opérateur, génère automa.quement les 100 numéros
avec cet index.
- Pour vendre un numéro, il faut les étapes suivantes :
o Afficher la liste des operateurs
o Choisir l’opérateur
o Afficher la liste de index de l’opérateur,
o Choisir l’index
o Afficher la liste des numéros
o Choisir le numéro et valider
- Un contact bloqué ne peut pas nous appeler, on ne peut pas le contacter n’ont plus
- Tous les constantes doivent être paramétrables dans des fichiers
- Tous le fichiers de données ont l’extension .txt

- [Apercu](#overview)
  - [Le challenge](#le-challenge)
  - [Les roles et permissions de chaque utilisateurs](#les-roles-et-permissions-de-chaque-utilisateurs)
  - [Regles de gestions](#regles-de-gestions)
- [Notre processus](#notre-processus)
  - [Technologies utilisee](#technologies-utilisee)
  - [Ce que nous avons appris](#ce-que-nous-avons-appris)
  - [Ressources utiles](#ressources-utiles)
- [Auteurs](#auteurs)

## Notre processus

### Technologies utilisee

- python 3.9

### Ce que nous avons appris


### Ressources utiles

## Auteurs

### Joel Gaetan HASSAM OBAH

- Site Web - [joel hassam](https://www.joelhassam.com)
- LinkedIn - [@Joel Gaetan HASSAM OBAH ](https://www.linkedin.com/in/joel-gaetan-hassam-obah/)
- Instagram - [@joel_hassam](https://www.instagram.com/joel_hassam/)
- Facebook - [@joel Gaetan HASSAM OBAH](https://www.facebook.com/joelgaetanhassamobah/)
- WhatsApp - [+221 70 818 40 10](https://wa.me/message/JPOFLGOJMUCWD1)

- [Apercu](#overview)
  - [Le challenge](#le-challenge)
  - [Les roles et permissions de chaque utilisateurs](#les-roles-et-permissions-de-chaque-utilisateurs)
  - [Regles de gestions](#regles-de-gestions)
- [Notre processus](#notre-processus)
  - [Technologies utilisee](#technologies-utilisee)
  - [Ce que nous avons appris](#ce-que-nous-avons-appris)
  - [Ressources utiles](#ressources-utiles)
- [Auteurs](#auteurs)