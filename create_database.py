import mysql.connector
from mysql.connector import errorcode
import pandas as pd

# Informations de connexion à la base de données
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'port': 3306,
    'database': 'immojasper'
}

# Fichiers CSV
csv_files = {
    'dvf_stat_communes': './data/dvf_stat_communes.csv',
    'dvf_stat_departement': './data/dvf_stat_departement.csv'
}

# Définir les schémas de table
table_schemas = {
    'dvf_stat_communes': """
        CREATE TABLE dvf_stat_communes (
            code_geo VARCHAR(255),
            libelle_geo VARCHAR(255),
            code_departement VARCHAR(255),
            echelle_geo VARCHAR(255),
            nb_ventes_whole_appartement INT,
            moy_prix_m2_whole_appartement FLOAT,
            med_prix_m2_whole_appartement FLOAT,
            nb_ventes_whole_maison INT,
            moy_prix_m2_whole_maison FLOAT,
            med_prix_m2_whole_maison FLOAT,
            nb_ventes_whole_apt_maison INT,
            moy_prix_m2_whole_apt_maison FLOAT,
            med_prix_m2_whole_apt_maison FLOAT,
            nb_ventes_whole_local INT,
            moy_prix_m2_whole_local FLOAT,
            med_prix_m2_whole_local FLOAT
        )
    """,
    'dvf_stat_departement': """
        CREATE TABLE dvf_stat_departement (
            code_geo VARCHAR(255),
            libelle_geo VARCHAR(255),
            echelle_geo VARCHAR(255),
            nb_ventes_whole_appartement INT,
            moy_prix_m2_whole_appartement FLOAT,
            med_prix_m2_whole_appartement FLOAT,
            nb_ventes_whole_maison INT,
            moy_prix_m2_whole_maison FLOAT,
            med_prix_m2_whole_maison FLOAT,
            nb_ventes_whole_apt_maison INT,
            moy_prix_m2_whole_apt_maison FLOAT,
            med_prix_m2_whole_apt_maison FLOAT,
            nb_ventes_whole_local INT,
            moy_prix_m2_whole_local FLOAT,
            med_prix_m2_whole_local FLOAT
        )
    """
}

# Connexion au serveur MySQL
try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # Supprimer les tables si elles existent
    for table in table_schemas.keys():
        cursor.execute(f"DROP TABLE IF EXISTS {table}")
    
    # Créer les tables
    for table, schema in table_schemas.items():
        cursor.execute(schema)
    
    # Charger les données des fichiers CSV dans les tables
    for table, csv_file in csv_files.items():
        df = pd.read_csv(csv_file, delimiter=';')
        for i, row in df.iterrows():
            sql = f"INSERT INTO {table} VALUES ({', '.join(['%s'] * len(row))})"
            cursor.execute(sql, tuple(row))
    
    cnx.commit()
    print("Les tables ont été créées et les données ont été chargées avec succès.")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Erreur : Mauvais utilisateur ou mot de passe")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Erreur : La base de données n'existe pas")
    else:
        print(err)
finally:
    cursor.close()
    cnx.close()
