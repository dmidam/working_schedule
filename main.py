import psycopg2 as pg2

conn = pg2.connect(database='Work schedule',user='postgres',password='Damdamdam123!')
cur = conn.cursor()