import mysql.connector
#silahkan jalankan kode program berikut untuk membuat database dengan sql
#setelah membuat database silahkan jadikan comment code line bagian Database
#BAGIAN DATABASE
'''db=mysql.connector.connect(host="localhost",user="root",passwd="")

if db.is_connected():
    print("Berhasil terhubung ke database")

cursor=db.cursor()
cursor.execute("CREATE DATABASE epemira")
print("Database Berhasil dibuat!")'''
#AKHIR PEMBUATAN DATABASE

#Jalankan kode program dibawah ini untuk membuat tabel pemilih dan tabel paslon di databae Epemira
#BAGIAN PEMBUATAN TABEL
'''db=mysql.connector.connect(host="localhost",user="root",passwd="",database="epemira")

cursor=db.cursor()
sql="""CREATE TABLE pemilih(user_id INT AUTO_INCREMENT PRIMARY KEY,nama VARCHAR(255),nim VARCHAR(20),kelas VARCHAR(20),status TINYINT(1))"""
cursor.execute(sql)

print("Tabel pemilih berhasil dibuat!")
cursor=db.cursor()
sql="""CREATE TABLE paslon(nopaslon INT PRIMARY KEY,nama_ketua VARCHAR(255),nim_ketua VARCHAR(20),kelas_ketua VARCHAR(20),nama_wakil VARCHAR(255),nim_wakil VARCHAR(20),kelas_wakil VARCHAR(20),visi VARCHAR(1000),misi VARCHAR(1500),jumlah_suara INT)"""
cursor.execute(sql)
print("Tabel Paslon Berhasil dibuat")
#AKHIR PEMBUATAN TABEL'''
