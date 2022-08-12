import mysql.connector # Melakukan Connector Python ke Database SQL
import datetime
import time
db=mysql.connector.connect(host="localhost",user="root",passwd="",database="epemira") # menguhubngkan ke database sql pada tabel epemira


class Pemilih: # Super Class
    def __init__(self,nama,nim,kelas):          # Melakukan Penambahan Parameter Pada Superclass
        self.nama=nama
        self.nim=nim
        self.kelas=kelas

    def get_info(self):   # Menampilkan Data
        cursor=db.cursor()  # Mengkoneksi sql untuk di eksekusi
        sql= "SELECT * FROM pemilih WHERE status=%s"
        cursor.execute(sql,[0])   # Mengeksekusi Database SQL
        result = cursor.fetchall()  # merubah menjadi list
        for status in result: 
            print(status)
                
class Vote(Pemilih):    # Subclass Vote dari Pemilih
    jumlah_suara_paslon =0

    def __init__(self,nama,nim,kelas,vote): # Method Parameter
        super().__init__(nama,nim,kelas)    # Pemanggilan Superclass
        self.vote = vote  # Pemanggilan Parameter

    def pilih (self): # Method dari class Vote
        n=self.vote   
        if self.vote == n: # Percabangan Vote
            Vote.jumlah_suara_paslon +=1    
            cursor=db.cursor()    # Mengkoneksi sql untuk di eksekusi
            sql="SELECT jumlah_suara FROM paslon WHERE nopaslon=%s"   # Memilih tabel jumlah suara dengan konfirmasinya adalah nomor paslon
            cursor.execute(sql,[n])
            result = cursor.fetchall()
            for data in result:   # Data mengulang Sejumlah Data Yang Data Ada Didalam Result
                suara=list(data)
                Vote.jumlah_suara_paslon +=suara[0]
            sql1= "UPDATE pemilih SET status =%s WHERE nim=%s"    # Untuk Update Status Menggunakan Konfirmasi NIM
            cursor.execute(sql1,[1,self.nim])     # Perintah Mengeksekusi SQL 1
            sql2= "UPDATE paslon SET jumlah_suara =%s WHERE nopaslon=%s"    # Mengupdate Status Jumlah Suara dengan konfirmasi nopaslon "Nomor Paslon"
            cursor.execute(sql2,[Vote.jumlah_suara_paslon,n])   # Mengeksekusi SQL 2 Untuk Update
            db.commit()     # Menyimpan Data
            Vote.jumlah_suara_paslon =0. # Mengembalikan Kondisi Awal = 0
        
        else:
            print("paslon tidak terdaftar")

    def perolehan_suara(self):      # Method Dari Kelas Suara
        cursor=db.cursor()          # Mengkoneksi sql untuk di eksekusi
        sql= "SELECT * FROM paslon "  # Memilih tabel Paslon
        cursor.execute(sql)   # perintah eksekusi
        result = cursor.fetchall()  # perintah merubah menjadi list
        print("===========PEROLEHAN SUARA PEMIRA PER ",datetime.date.today(),"============")
        for paslon in result: # Melakukan perulangan Data selama data ada didalam result
            hasil =list(paslon)   # 
            print("No urut    : ",hasil[0])
            print("Nama paslon: ",hasil[1],"& ",hasil[4])
            print("Total Suara: ",hasil[9])
            print("=================================================")

class admin_pemilih(Pemilih):     # Subclass admin pemilih dari superclass pemilih

    def __init__(self,nama,nim,kelas):       # Method Parameter
        super().__init__(nama,nim,kelas)    # Pemanggilan Superclass

    def Input_data(self):   # method dari class admin pemilih
        cursor=db.cursor()    # Untuk Mengeksekusi Perintah SQL
        val= (self.nama,self.nim,self.kelas)    # Velue atau nilai untuk mengisi data ke dalam database
        sql= "INSERT INTO pemilih (nama,nim,kelas,status) VALUES (%s,%s,%s,0)"    # Melakukan input data ke database dengan velue nama, nim kelas
        cursor.execute(sql,val)   # Melakukan Eksekusi
        db.commit()   # Menyimpan Data

        print("{} data ditambahkan".format(cursor.rowcount))    # Menampilkan nilai yang ditambahkan
        time.sleep(2)

    def delete_data(self,del_key):  # Method menghapus data dari admin_pemilih

        cursor=db.cursor()    # Mengkoneksi sql untuk di eksekusi
        sql= "DELETE FROM pemilih WHERE nim = %s"   # Tabel yang dituju pada database untuk dihapus dengan konfirmasinya adalah NIM
        cursor.execute(sql,[del_key])   # perintah eksekusi menghapus data
        db.commit()   # perintah untuk menyimpan data

        print("{} data dihapus".format(cursor.rowcount))    # tampilan jika data sudah di hapus
        time.sleep(2)

    def update_data(self,update_key):   # Method update_data dari admin pemilih
        cursor=db.cursor()    # Mengkoneksikan SQL untuk di eksekusi
        sql= "UPDATE pemilih SET nama=%s, nim=%s, kelas=%s WHERE nim = %s"  # Tabel yang dituju untuk diupdate data dengan velue nama nim kelas. Konfirmasinya adalah NIM
        cursor.execute(sql,[(self.nama),(self.nim),(self.kelas),(update_key)])    # Eksekusi data yang di update nama, nim, kelas
        db.commit()     # perintah menyimpan data
        print("{} data diupdate".format(cursor.rowcount)) # Tampilan data yang telah di update
        time.sleep(2)

    def reset_all_data(self):   # Method reset semua data status pada admin_pemilih
        cursor=db.cursor()    # Mengkoneksikan SQL agar bisa di eksekusi
        sql="UPDATE pemilih SET status=%s"    # Meengupdate seluruh status yang di reset
        cursor.execute(sql,[0]) # Perintah eksekusi
        db.commit() # Menyimpan Data
        print("semua data berhasil di reset!!")
        time.sleep(2)

    def hapus_all_data(self):   # Method reset semua data pada data pemilih
        cursor=db.cursor()    # Mengkoneksikan SQL agar bisa di eksekusi
        sql="DELETE FROM pemilih"   # Tabel pemilih yang akan di hapus semua data
        cursor.execute(sql)   # Perintah eksekusi
        db.commit()   # Perintah Menyimpan Data
        print("semua data berhasil di hapus!!")   # Tampilan perintah data telah dihapus
        time.sleep(2)