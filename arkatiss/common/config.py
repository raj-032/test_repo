import psycopg2

def conn():
    try:
        # TODO:: Take host, database, user, password from properties file.
        conn = psycopg2.connect(host="localhost", database="arkatiss", user="postgres", password="postgres")
        return conn
    except Exception as e:
        print(f'config-conn: Error: {e}')
        raise Exception(e)