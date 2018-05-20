# SION

Initial:
1. Buat folder SION di directory kamu
2. buka cmd ke directory SION
3. ketikkan git init
4. ketikkan git clone https://github.com/hanifaarrumaisha/SION.git
5. ketikkan git remote add origin https://github.com/hanifaarrumaisha/SION
3. ketikkan python -m venv env
4. ketikkan env\Scripts\activate.bat
5. ketikkan pip install -r requirements.txt


http://colorhunt.co/c/101436

import di views
from django.db import connection



buat instance cursor
cur=connection.cursor()

lakukan execute dari sql query apa aja
cur.execute('SET SEARCH_PATH TO SION')
cur.execute('SELECT * FROM DONATUR')
one = cur.fetchone() 
all = cur.fetchall()

untuk pass ke templates pakai ini: 

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

dictfetchall(cur)

kalau mau ngubah isi table, harus pakai connection.commit()
cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s)", (10, 'hello@dataquest.io', 'Some Name', '123 Fake St.')) conn.commit()


fetchone() method returns the first result or None
fetchall() method returns a list of each row in the table or an empty list [] if there are no rows.
