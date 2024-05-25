import mysql.connector
from mysql.connector import errorcode

# Informations de connexion à la base de données
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'port' : 3306
}

# Nom de la base de données
database_name = 'immojasper'

# Connexion au serveur MySQL
try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    
    # Supprimer la base de données si elle existe
    cursor.execute(f"DROP DATABASE IF EXISTS {database_name}")
    
    # Créer la base de données
    cursor.execute(f"CREATE DATABASE {database_name}")
    
    # Utiliser la nouvelle base de données
    cursor.execute(f"USE {database_name}")
    
    # Créer la table 'test' avec les colonnes 'nom' et 'prenom'
    create_table_query = """
    CREATE TABLE test (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nom VARCHAR(255),
        prenom VARCHAR(255)
    )
    """
    cursor.execute(create_table_query)
    
    print(f"La base de données '{database_name}' a été créée avec la table 'test'.")
    
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
