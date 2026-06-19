import psycopg2
 
conn=psycopg2.connect(
        host = "localhost",
        database="company",
        user="postgres",
        password="Suman2005@#",
        port="5432"
    )

cur =conn.cursor()
cur.execute("select customer_name  from customer where balance =50000",)
print(cur.fetchone())
cur.close()
conn.close()

