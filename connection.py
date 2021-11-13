import psycopg2

connection = psycopg2.connect(
  dbname="password_python",
  user="postgres",
  password="viana1920"
)

cursor = connection.cursor()