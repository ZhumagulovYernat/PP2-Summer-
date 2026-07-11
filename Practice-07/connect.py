import psycopg2
from config import host, database, user, password, port


try:
    connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )

    print("Connected to PostgreSQL")

    connection.close()

except Exception as e:
    print("Error:", e)