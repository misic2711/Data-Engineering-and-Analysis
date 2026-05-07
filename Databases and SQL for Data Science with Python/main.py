import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

 
# Connecting to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="parkour95",
    database="movies_db"
)

cursor = conn.cursor()
print("Povezan!")
 

query = """
    SELECT zanr.naziv, film.budzet
    FROM film
    JOIN film_zanr ON film.film_id = film_zanr.film_id
    JOIN zanr ON film_zanr.zanr_id = zanr.zanr_id
    WHERE film.budzet > 0
"""

cursor.execute(query)
rezultati = cursor.fetchall()


df = pd.DataFrame(rezultati, columns=["zanr", "budzet"])

prosek = df.groupby("zanr")["budzet"].mean().reset_index()

plt.bar(prosek["zanr"], prosek["budzet"])
plt.title("Prosecni budzet filmova po zanru")
plt.xlabel("Zanr")
plt.ylabel("Budzet")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualization.png")
plt.show()