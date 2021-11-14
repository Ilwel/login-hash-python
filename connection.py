import psycopg2
from dotenv import dotenv_values

# config = {"USER": "foo", "EMAIL": "foo@example.org"}
config = dotenv_values(".env")

connection = psycopg2.connect(
    dbname=config['DB_NAME'],
    user=config['USER'],
    password=config['PASSWORD'],
    port=config['PORT'],
    host=config['HOST']
)

cursor = connection.cursor()
