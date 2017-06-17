
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('diligence.db')

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS diligence (date integer, prod real, worth real)")
d = int(input("What's today's date? ")) 
p = float(input("How many minutes did you spend doing something productive? "))
w = float(input("How many minutes did you spend doing something worthless? "))
c.execute("INSERT INTO diligence VALUES (?, ?, ?)", (d, p, w))

conn.commit()

c.execute("SELECT date FROM diligence")
x = c.fetchall()
c.execute("SELECT prod from diligence")
y = c.fetchall()


