import mysql.connector
import time


db=mysql.connector.connect(host="localhost",user="root",passwd="",database="epemira") # Menghubungkan pada tabel epemira
class access: # Superclass access 
    akses_log =' ' 
    def __init__(self,user,Pass): # Melakukan Penambahan parameter pada superclass
        self.user = user
        self.Pass = Pass
    def login(self): # Method login dari superclass access
        cursor = db.cursor() # Mengkoneksikan SQL untuk di eksekusi
        username = self.user
        password = self.Pass
        sql = "SELECT * FROM pemilih WHERE nama = %s AND nim = %s" # Memilih Tabel pemilih dengan konfirmasinya adalah nama nim
        cursor.execute(sql,[(username),(password)]) # Perintah eksekusi
        results = cursor.fetchall() # Perintah ambil semua data dan di ubah menjadi list
        if self.user=="admin" and self.Pass =="admin": # Percabangan login khusus admin
            print("\t\tLogin berhasil...") # Tampilan perintah login telah berhasil 
            time.sleep(2)
            access.akses_log = '2'
            
        elif results: # Percabangan login sebagai pemilih
            for data in results: # Melakukan perulangan Data selama data ada didalam result
                cursor=db.cursor() # Mengkoneksikan SQL untuk di eksekusi
                sql= "SELECT status FROM pemilih WHERE nim=%s" # Memilih status dalam tabel pemilih dengan konfirmasi adalah nim
                cursor.execute(sql,[self.Pass]) # perintah eksekusi
                hasil = cursor.fetchall() # Perintah ambil semua data dan di ubah menjadi list
                for status in hasil: # Melakukan perulangan Data selama data ada didalam hasil
                    x=list(status) # objeck x sama dengan list status
                    print(x)
                    if x[0] == 1: # Percabangan status sama dengan 1
                        print("\t\tMaaf Anda sudah Memilih!!")
                        access.akses_log ='3' 
                        time.sleep(2)
                        break
                    elif x[0] ==0: # Percabangan status sama dengan 0
                        print("\t\tlogin Berhasil...")
                        time.sleep(2)
                        access.akses_log = '1'
                        break

        else:   
            print("\t\tMaaf username atau password yang anda masukan salah")
            access.akses_log ='3'

    def logout(self): # Method logout dari class access
        if self.user =="admin" and self.Pass=="admin":
            print("logout Berhasil...")
            time.sleep(2)
            
        else:
            print("Pemilihan berhasil...")
            print("Terimakasih sudah berpartisipasi di pemilihan raya HMTK")
            time.sleep(2)