import sqlite3
from datetime import date
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

conn = sqlite3.connect('diligence.db')

c = conn.cursor()

c.execute("SELECT date FROM diligence")
res = []
x = c.fetchall()
for el in x:
    for e in el:
        res.append(date(year=int(e[0:4]), month=int(e[4:6]), day=int(e[6:8])))
        
c.execute("SELECT prod from diligence")
y1 = c.fetchall()

c.execute("SELECT worth from diligence")
y2 = c.fetchall()

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.gcf().canvas.set_window_title('Diligence')
plt.title('Diligence Graph')
plt.xlabel('Dates')
plt.ylabel('Minutes')
plt.plot(res, y1, label = 'Productive', marker = 'o')
plt.plot(res, y2, label = 'Worthless', marker = 'o')
plt.legend()
plt.gcf().autofmt_xdate()
plt.show()
