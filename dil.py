import sqlite3
from datetime import date
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

conn = sqlite3.connect('diligence.db')

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS diligence (date text, prod real, worth real)")
d = input("What's today's date? ") 
p = float(input("How many minutes did you spend doing something productive? "))
w = float(input("How many minutes did you spend doing something worthless? "))
c.execute("INSERT INTO diligence VALUES (?, ?, ?)", (d, p, w))

conn.commit()

c.execute("SELECT date FROM diligence")
res = []
x = c.fetchall()
for el in x:
    for e in el:
        res.append(date(year=int(e[0:4]), month=int(e[4:6]), day=int(e[6:8])))
        
c.execute("SELECT prod from diligence")
y = c.fetchall()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(res, y)
plt.gcf().autofmt_xdate()
plt.show()

