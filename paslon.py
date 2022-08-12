import mysql.connector # Melakukan Connector Pada SQL
import time
db=mysql.connector.connect(host="localhost",user="root",passwd="",database="epemira") # Menghubungkan pada tabel epemira

class Paslon: # Superclass Paslon "Pasangan Calon"

    def __init__(self,nopaslon,namaketua,nimketua,kelasketua,namawakil,nimwakil,kelaswakil,visi,misi): # Melakukan Penambahan parameter pada superclass
        self.nopaslon = nopaslon  
        self.namaketua = namaketua
        self.nimketua = nimketua
        self.kelasketua = kelasketua
        self.namawakil = namawakil
        self.nimwakil = nimwakil
        self.kelaswakil = kelaswakil
        self.visi = visi
        self.misi = misi

    def info_paslon(self): # Menampilkan data
        cursor=db.cursor() # Mengkoneksikan SQL untuk di eksekusi
        sql= "SELECT *FROM paslon" # Memilih Tabel paslon
        cursor.execute(sql) # Perintah eksekusi
        result = cursor.fetchall() # Perintah ambil semua data dan di ubah menjadi list
        for paslon in result: # Melakukan perulangan Data selama data ada didalam result
            x = list(paslon) # Membuat objeck x menjadi list paslon
            print("========DATA PASLON NO URUT ",x[0],"=========")
            print("no urut: ",x[0])
            print("=============CALON KETUA ",x[0],"============")
            print("Nama : ",x[1])
            print("NIM  : ",x[2])
            print("Kelas: ",x[3])
            print("==========CALON WAKIL KETUA ",x[0],"=========")
            print("Nama : ",x[4])
            print("NIM  : ",x[5])
            print("Kelas: ",x[6])
            print("============ VISI & MISI ",x[0],"============")
            print("Visi : ",x[7])
            print("Misi : ",x[8])
            print("==========================================\n")

class admin_paslon(Paslon): # Subclass admin paslon dari superclass paslon

    def __init__(self,nopaslon,namaketua,nimketua,kelasketua,namawakil,nimwakil,kelaswakil,visi,misi): # Penamaan parameter
        super().__init__(nopaslon,namaketua,nimketua,kelasketua,namawakil,nimwakil,kelaswakil,visi,misi) # Pemanggilan Superclass

    def input_paslon(self): # method dari class admin paslon
        cursor=db.cursor() # Mengkoneksikan SQL untuk di eksekusi
        val= (self.nopaslon,self.namaketua,self.nimketua,self.kelasketua,self.namawakil,self.nimwakil,self.kelaswakil,self.visi,self.misi) # Velue atau nilai untuk mengisi data ke dalam database
        sql= "INSERT INTO paslon (nopaslon,nama_ketua,nim_ketua,kelas_ketua,nama_wakil,nim_wakil,kelas_wakil,visi,misi,jumlah_suara) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,0)" # Melakukan input data ke database dengan velue nama, nim kelas
        cursor.execute(sql,val) # Perintah eksekusi
        db.commit() # Perintah menyimpan data
       
        print("{} data ditambahkan".format(cursor.rowcount)) # Tampilan perintah data telah ditambahkan
        time.sleep(2)

    def delete_paslon(self,del_key): # Method menghapus data dari admin_paslon
        cursor=db.cursor() # Mengkoneksikan SQL untuk di eksekusi
        sql= "DELETE FROM paslon WHERE nopaslon = %s" # Tabel yang dituju pada database untuk dihapus dengan konfirmasinya adalah nopaslon
        cursor.execute(sql,[del_key]) # Perintah eksekusi
        db.commit() # Perintah menyimpan data

        print("{} data dihapus".format(cursor.rowcount)) # Tampilan perintah data telah dihapus
        time.sleep(2)

    def update_paslon(self,update_key): # Method update_data dari admin paslon
        cursor=db.cursor() # Mengkoneksikan SQL untuk di eksekusi
        sql= "UPDATE paslon SET nopaslon=%s, nama_ketua=%s, nim_ketua=%s, kelas_ketua=%s, nama_wakil=%s, nim_wakil=%s, kelas_wakil=%s, visi=%s, misi=%s WHERE nopaslon = %s" # Tabel yang dituju untuk diupdate data dengan velue yang ada. Konfirmasinya adalah nopaslon
        cursor.execute(sql,[(self.nopaslon),(self.namaketua),(self.nimketua),(self.kelasketua),(self.namawakil),(self.nimwakil),(self.kelaswakil),(self.visi),(self.misi),(update_key)]) # Eksekusi data yang di update 
        db.commit() # Perintah menyimpan data

        print("{} data diupdate".format(cursor.rowcount)) # Tampilan perintah data telah diupdate
        time.sleep(2)

    def reset_suara(self): # Method reset semua data status pada admin_paslon
        cursor=db.cursor() # Mengkoneksikan SQL untuk di eksekusi
        sql="UPDATE paslon SET jumlah_suara=%s" # Meengupdate seluruh jumlah_suara yang di reset
        cursor.execute(sql,[0]) # Perintah eksekusi
        db.commit() # Perintah Menyimpan data
        print("semua data berhasil di reset!!") # Tampilan Perintah data telah dihapus
        time.sleep(2)
        
    def hapus_all(self): # Method reset semua data pada data paslon
        cursor=db.cursor() # Mengkoneksikan SQL untuk di eksekusi
        sql="DELETE FROM paslon" # Tabel pemilih yang akan di hapus semua data
        cursor.execute(sql) # Perintah eksekusi
        db.commit() # Perintah menyimpan data
        print("semua data berhasil di hapus!!") # Tampilan perintah data telah dihapus semua
        time.sleep(2)