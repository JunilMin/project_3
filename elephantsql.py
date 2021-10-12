import psycopg2

conn = psycopg2.connect(
    host="fanny.db.elephantsql.com",
    database="yowummal",
    user="yowummal",
    password="kE9KWhUhHhZt83Cl-z1waJE9HIG0bgbP")

cur = conn.cursor()
