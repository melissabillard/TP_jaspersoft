# Datavisualisation
Projet Datavisualisation / Reporting

**Intervenant :** Benoit Gérald

## Outil de reporting
- [Jasper](https://www.jaspersoft.com/)

![](/images/img1.jpg)

## Groupe 3
- BILLARD Mélissa
- BRACCIALE-COMBAS Lola
- CARRILHO LAMEIRA Rita

## Description
Ce projet de datavisualisation a pour objectif d'identifier les zones à fort rendement locatif en Occitanie dans le secteur immobilier, en utilisant des graphiques et des tableaux pour présenter de manière claire et professionnelle les données collectées.

## Sources de données (<img src="/images/img2.png" width="100">)

- [Prix immobilier et revenu dans les agglomérations françaises](https://www.igedd.developpement-durable.gouv.fr/prix-immobilier-et-revenu-dans-les-agglomerations-a1112.html)

## Déploiement BDD

### Pré-requis

<img src="/images/img3.png" width="150">

- [Wampserver](https://wampserver.aviatechno.net/)
  
### Bibliothèques nécessaires
```
pip install mysql-connector-python
pip install pandas mysql-connector-python
```
### Fichiers

<img src="/images/img4.png" width="200">

- create_database.py 

**Note :** Création de la base de donnée et des tables associées. 

### Exécution
```
python create_database.py
```
<img src="/images/bdd.png">

### Rapport Jasper

### Connexion du dataset
Connecter le rapport Jasper à l'adaptateur de données MySQL.

<div style="display: flex; gap: 10px;">
    <img src="/images/data-adapter-sql1.png" alt="Connexion dataset étape 1" width="200">
    <img src="/images/data-adapter-sql2.png" alt="Connexion dataset étape 2 test" width="200">
</div>
