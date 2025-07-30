import sqlite3

con = sqlite3.connect("arq.db")

cur = con.cursor()

cur.execute("CREATE TABLE jogo(RESIDENT EVIL4)")

