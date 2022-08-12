import mysql.connector        # Mengkoneksi ke SQL
from login import access      # Mengimport Data acces
from paslon import Paslon     # Import Data Paslon
from pemilih import Vote      # Import data vote
from paslon import admin_paslon   # import data admin_paslon
from pemilih import admin_pemilih # import data admin_pemilih
from pemilih import Pemilih   # import data pemilih
import os   # fungsi clear screen
         
def main():   # Method
    print("\t\t==========================================")
    print("\t\t Selamat Datang di Aplikasi E-Pemira HMTK")
    print("\t\t===================LOGIN==================")
    username=input("\t\tUsername: ")    # Input Username dengan nama
    password=input("\t\tPassword: ")    # Input password dengan NIM
    akses = access(username,password)   # pembentukan obyek akses
    print("\t\t==========================================")
    akses.login()   # mengakses data login
    os.system('cls')  # clear screen
    if akses.akses_log == '1':    # Akses login sebagai Pemilih
        print("======Selamat datang di aplikasi Epemira===")
        print("silahkan gunakan hak pilih anda untuk menentukan\npemimpin HMTK 1 tahun kedepan.\n")
        datapaslon=Paslon(" "," "," "," "," "," "," "," "," ")
        datapaslon.info_paslon()
        vote = int(input("Masukan no pasangan calon pilihan: "))
        konfirm =input("masukan nim untuk konfirmasi:")
        pemilihan =Vote(" ",konfirm," ",vote)
        pemilihan.pilih()
        akses.logout()    # akses logout
        os.system('cls')    # Clear screen
        main()
    elif akses.akses_log == '2':  # Akses login sebagai admin
        status='Y'    
        while status =='Y':   # Perulangan jika status 'Y'
            print("=================MENU UTAMA======================")
            print("1.DATA PEMILIH\n2.DATA PASLON\n3.HASIL PEMILIHAN\n4.Logout") # Tampilan pilihan menu
            pilih = int(input("====>")) # masukan nomor menu yang ingin di pilih
            os.system('cls')    # clear screen
            if pilih ==1:   # percabangan jika memilih menu nomor 1 "Data Pemilih"
                status1 ='Y' # status1 sama dengan Y
                while status1 =='Y':    # Perulangan jika status 'Y'
                    print("=================MENU DATA PEMILIH=====================")
                    print("1.Input data\n2.Hapus data\n3.Edit data\n4.info status memilih\n5.reset_pemilih\n6.kembali ke Menu Utama") # Tampilan menu pilihan
                    pilih1 = int(input("====>"))  #perintah memasukan data pilihan menu
                    os.system('cls')    # clear screen
                    if pilih1 == 1:   # percabangan menu pilhan nomor 1 "Input Data"
                        print("=================INPUT DATA PEMILIH================")
                        nama=input("Nama:")   # Masukkan Nama
                        nim=input("NIM:")   # Masukan NIM
                        kelas=input("Kelas:") # Masukan Kelas
                        datapemilih=admin_pemilih(nama,nim,kelas) # eksekusi data yang ada di admin_pemilih "nama,nim,kelas"
                        datapemilih.Input_data()
                        print("===================================================")
                        print("apakah ingin kembali ke menu?(Y/T):")  # tampilan jika kembali ke menu
                        status1 = input("===>") # input data status Y atau T
                        os.system('cls')    # clear screen

                    elif pilih1 == 2: # Percabangan menu pilihan 2 "Data Paslon"
                        print("=================HAPUS DATA PEMILIH================")
                        print("1.Hapus 1 data\n2.hapus seluruh data") # tampilan menu pilihan
                        pilih2=int(input("===>"))   # input pilihan menu
                        if pilih2 ==1:  # percabangan pilihan menu dengan nomor 1 "Hapus satu Data Pemilih"
                            print("=================HAPUS 1 DATA PEMILIH===============")
                            del_key = input("Masukan nim untuk menghapus data:")    # Memasukkan NIM untuk penghapusan data 
                            datapemilih=admin_pemilih(" "," "," ")
                            datapemilih.delete_data(del_key)  # eksekusi hapus data
                            print("===================================================")
                            status1='Y' # status Y langsung kembali pada menu pemilih
                            os.system('cls')    # clear screen
                        elif pilih2 ==2:    # percabangan dengan pilihan menu nomor 2 "Hapus semua data"
                            print("================HAPUS ALL DATA PEMILIH==============")
                            datapemilih=admin_pemilih(" "," "," ")
                            datapemilih.hapus_all_data()
                            print("===================================================")
                            status1='Y' # status Y langsung kembali pada menu pemilih
                            os.system('cls')    # clear screen

                    elif pilih1 == 3: # Percabangan menu pilihan nomor 3 "Edit data"
                        print("==================EDIT DATA PEMILIH================")
                        update_key = input("masukan nim untuk mengupdate data:") # nim sebagai konfirmasi data yang ingin di update
                        nama=input("Nama baru:") # masukan nama data baru
                        nim=input("NIM baru:")  # masukan data nim baru
                        kelas=input("Kelas baru:")  # masukan data kelas baru
                        datapemilih=admin_pemilih(nama,nim,kelas)   # data yang di eksekusi "nama,nim,kelas"
                        datapemilih.update_data(update_key) # perintah update data pada data base
                        print("===================================================")
                        print("apakah ingin kembali ke menu?(Y/T):")
                        status1 = input("===>") # inputan pilihan jika kembali ke menu
                        os.system('cls')    # clear screen

                    elif pilih1 == 4 :  # Percabangan menu pilihan nomor 4 "melihat data yang belum memilih"
                        print("=============DAFTAR YANG BELUM MEMILIH=============")
                        pemilih = Pemilih(" "," "," ")  # memanggil data pemilih
                        pemilih.get_info() # menampilkan info data pemilih yang belum memilih
                        print("===================================================")
                        print("apakah ingin kembali ke menu?(Y/T):")
                        status1 = input("===>") # inputan pilihan jika kembali ke menu
                        os.system('cls')  # clear screen

                    elif pilih1 ==5: # percabangan menu pilihan nomor 5 "menghapus seluruh data pemilih di database"
                        datapemilih=admin_pemilih(" "," "," ")
                        datapemilih.reset_all_data()  # perintah menghapus seluruh data pemilih di database
                        status1='Y' # status Y langsung kembali pada menu pemilih
                        os.system('cls')  # clear screen
                    elif pilih1 == 6: # percabangan menu nomor 6 "Kembali ke menu utama"
                        status1='T'
                        status ='Y'
                        os.system('cls')  # clear screen
                    else:
                        print("tidak terdapat dalam menu!!")
                        status ='Y' # status Y langsung kembali pada menu pemilih
                        os.system('cls')  # clear screen

            elif pilih ==2: # percabangan menu utama dengan nomor 2 "Data Paslon"
                status2 ='Y'  # status2 sama dengan Y
                while status2 =='Y':  # perulangan jika status Y kembali ke menu data paslon
                    print("=================MENU DATA PASLON======================")
                    print("1.Input data\n2.Hapus data\n3.Edit data\n4.Reset JML suara\n5.Kembali ke Menu Utama") # menu data paslon
                    pilih2 = int(input("====>"))  # input pilihan menu
                    os.system('cls')  # clear screen

                    if pilih2 == 1: # percabangan menu nomor 1 " Input data paslom"
                        # Tampilan memasukan data paslon
                        print("=================INPUT DATA PASLON================") 
                        print("\nNo Urut Peserta Pasangan Calon")
                        nopaslon=input("No Peserta Pasangan Calon: ")
                        print ("Data Identitas Ketua Pasangan Calon")
                        namaketua=input("Nama Ketua\t\t: ")
                        nimketua=input("Nim Ketua\t\t: ")
                        kelasketua=input("Kelas Ketua\t\t: ")
                        print ("\nData Identitas Wakil Pasangan Calon")
                        namawakil=input("Nama Wakil\t\t: ")
                        nimwakil=input("Nim Wakil\t\t: ")
                        kelaswakil=input("Kelas Wakil\t\t: ")
                        print ("\nVisi & Misi Pasangan Calon")
                        visi=input("Visi Paslon\t\t: ")
                        misi=input("Misi Paslon\t\t: ")
                        datapaslon=admin_paslon(nopaslon,namaketua,nimketua,kelasketua,namawakil,nimwakil,kelaswakil,visi,misi) # data yang di eksekusi
                        datapaslon.input_paslon()
                        print("===================================================")
                        print("apakah ingin kembali ke menu?(Y/T):")
                        status2 = input("===>") # memasukan status kembali ke menu data paslon
                        os.system('cls')    # clear screen

                    elif pilih2 == 2:   # percabangan menu dengan nomor 2 "Hapus data paslon"
                        print("=================HAPUS DATA PASLON=================")
                        print("1.Hapus 1 data\n2.hapus seluruh data") # menu hapus data paslon
                        pilih4=int(input("===>")) # input pilihan menu

                        if pilih4 ==1:  # menu pilihan 1 "Hapus satu data"
                            print("=================HAPUS 1 DATA PASLON==============")
                            del_key = input("Masukan nopaslon untuk menghapus data:") # nomor paslon sebagai konfirmasi penghapusan data
                            datapaslon=admin_paslon(" "," "," "," "," "," "," "," "," ")
                            datapaslon.delete_paslon(del_key) # eksekusi dataabse penghapusan data
                            print("===================================================")
                            status2='Y' # status Y kembali ke menu data paslon
                            os.system('cls')  # clear screen

                        elif pilih4 ==2:  # menu pilihan nomor 2 "mengapus seluru data paslon"
                            print("================HAPUS ALL DATA PASLON==============")
                            datapaslon=admin_paslon(" "," "," "," "," "," "," "," "," ")
                            datapaslon.hapus_all() # eksekusi database untuk penghapusan seluruh data 
                            print("===================================================")
                            status2='Y'   # status Y kembali ke menu data paslon
                            os.system('cls')  # clear screen

                    elif pilih2 == 3: # percabangan menu nomor 3 "edit data paslon yang ingin di update"
                        print("==================EDIT DATA PASLON=================")
                        update_key = input("masukan nopaslon untuk mengupdate data:") # nomor paslon sebagai konfirmasi data yang ingin di update
                        print("\nNo Urut Peserta Pasangan Calon")
                        nopaslon=input("No Peserta Pasangan Calon: ")
                        print ("Data Identitas Ketua Pasangan Calon")
                        namaketua=input("Nama Ketua\t\t: ")
                        nimketua=input("Nim Ketua\t\t: ")
                        kelasketua=input("Kelas Ketua\t\t: ")
                        print ("\nData Identitas Wakil Pasangan Calon")
                        namawakil=input("Nama Wakil\t\t: ")
                        nimwakil=input("Nim Wakil\t\t: ")
                        kelaswakil=input("Kelas Wakil\t\t: ")
                        print ("\nVisi & Misi Pasangan Calon")
                        visi=input("Visi Paslon\t\t: ")
                        misi=input("Misi Paslon\t\t: ")
                        datapaslon=admin_paslon(nopaslon,namaketua,nimketua,kelasketua,namawakil,nimwakil,kelaswakil,visi,misi)   # data yang di eksekusi pada admin paslon
                        datapaslon.update_paslon(update_key)  # eksekusi penyimpanan update data
                        print("===================================================")
                        print("apakah ingin kembali ke menu?(Y/T):")
                        status2 = input("===>") # input status kembali ke menu
                        os.system('cls')  # clear screen

                    elif pilih2 == 4: # percabangan menu nomor 4 " Mereset jumlah voting suara paslon"
                        datapaslon=admin_paslon(" "," "," "," "," "," "," "," "," ")
                        datapaslon.reset_suara() # eksekusi penghapusan jumlah suara
                        status2 ='Y'    # status Y langsung kembali pada menu pemilih
                        os.system('cls')  # clear screen

                    elif pilih2 == 5: # menu pilihan kembali ke menu utama
                        status2 ='T'  # otomatis logout
                        status ='Y' # status Y langsung kembali pada menu pemilih
                        os.system('cls')  # clear screen
                    else:
                        print("tidak terdapat dalam menu!!")
                        status2='Y' # status Y langsung kembali pada menu pemilih
                        os.system('cls')  # clear screen

            elif pilih ==3: # percabangan menu utama pilihan nomor 3 "Melihat Hasil voting suara"
                hasil=Vote(" "," "," "," ")
                hasil.perolehan_suara() # penampilan hasil voting suara pada paslon
                status=input("Kembali ke menu(Y/T) : ") # input status kembali ke menu atau tidak
                if status =='Y':  # jika status Y
                    status ='Y' # maka kembali ke menu utama
                    os.system('cls')  # clear screen
                else: # jika input selain Y, maka program otomatis logout
                    akses.logout()  # akses logout
                    os.system('cls')  # clear screen
                    main()

            elif pilih ==4: # percabangan menu utama jika ingin logout
                akses.logout()
                os.system('cls')  # clear screen
                main()
            else:
                pass
    elif akses.akses_log =='3':
        os.system('cls')  # clear screen
        main()
main()