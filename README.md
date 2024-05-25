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

## Sources de données

- [Prix immobilier et revenu dans les agglomérations françaises](https://www.igedd.developpement-durable.gouv.fr/prix-immobilier-et-revenu-dans-les-agglomerations-a1112.html)

![](/images/img2.png)

## Déploiement BDD

### Pré-requis
- [Wampserver](https://wampserver.aviatechno.net/)

![](/images/img3.png)
  
### Bibliothèques nécessaires
```
pip install mysql-connector-python
pip install pandas mysql-connector-python
```
### Fichiers
- create_database.py 

**Note :** Création de la base de donnée et des tables associées. 

![](/images/img4.png)

### Exécution
```
python create_database.py
```
