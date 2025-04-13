import sqlite3


db = sqlite3.connect("our.db")
cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Urunler (URUN_ADI TEXT, URUN_ACIKLAMASI TEXT, URUN_BARKODU INT, URUN_RESIM_PATIKASI TEXT, URUN_ADEDI INT)")
db.commit()

cursor.execute("INSERT INTO Urunler VALUES (?,?,?,?,?)",("Supangle","Eşsiz lezzetteki Supangle",86823111,"/path/to/",68))
db.commit()

urun_adlari = cursor.execute("SELECT rowid,URUN_ADI FROM Urunler")
veriler = cursor.fetchall()
for veri in veriler:
    print("Ürün adı: ",veri)

f = ["alperen","1,2,3","4",5]

