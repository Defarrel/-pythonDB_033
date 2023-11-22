import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
import sqlite3
from PIL import Image, ImageTk


def create_database_table():
    conn = sqlite3.connect("Test.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa1 (
            Nama_siswa VARCHAR(50) NOT NULL,
            Biologi int,
            Fisika int,
            Inggris int,
            Prediksi_Fakultas VARCHAR(50)
        )
    ''')

    conn.commit()
    conn.close()
    
def hasil_prediksi():
    nama_siswa = NAMA.get()
    nilai_biologi = (BIOLOGI.get())
    nilai_fisika = (FISIKA.get())
    nilai_inggris = (BAHASA_INGGRIS.get())
    
    if not all([nama_siswa, BIOLOGI.get(), FISIKA.get(), BAHASA_INGGRIS.get()]):
        showerror("Error", "Harap isi semua field!")
        return
    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        prediksi_fakultas = "Ketokteran" 
        output_label.config(text=prediksi_fakultas)
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        prediksi_fakultas = "Teknik" 
        output_label.config(text=prediksi_fakultas)
    elif nilai_inggris > nilai_biologi and nilai_inggris > nilai_fisika:
        prediksi_fakultas = "Bahasa" 
        output_label.config(text=prediksi_fakultas)
    elif nilai_biologi == nilai_fisika or nilai_biologi == nilai_inggris or nilai_inggris == nilai_fisika:
        prediksi_fakultas = "Bisa Memilih"
    else:
        showerror("Error", "Harap isi dengan angka yang benar")
        return

    showinfo("Hasil Prediksi", f"Hasil prediksi untuk {nama_siswa}: {prediksi_fakultas}")
    try:
        conn = sqlite3.connect("Test.db")
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO nilai_siswa1 (Nama_Siswa, Biologi, Fisika, Inggris, Prediksi_Fakultas)
        VALUES (?, ?, ?, ?, ?)
        ''', (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi_fakultas))

        conn.commit()
        conn.close()

        showinfo("Selamat", "Data berhasil disimpan!")
    except sqlite3 as err:
        showerror("Error", f"Error: {err}")
        
window = tk.Tk()
window.configure(bg="gray")
window.geometry("900x900")
window.title("Test Program")

BIOLOGI=tk.IntVar()
NAMA=tk.StringVar()
FISIKA=tk.IntVar()
BAHASA_INGGRIS=tk.IntVar()
PREDIKSI=tk.StringVar()

#frame input
input_frame = ttk.Frame(window)
input_frame1 = ttk.Frame(window)
input_frame2  = ttk.Frame(window)
#Penempatan grid,pack,place
input_frame.pack(padx=250,pady=10,fill="x")
input_frame2.pack(padx=10,pady=10)
input_frame1.pack(padx=10,pady=10,fill="x")
#1. label 
judul_label = ttk.Label(input_frame, text="Prediksi Nilai Siswa")
judul_label.pack(padx=10,pady=10,fill="x")
#gambar
gambar = Image.open("download.jpeg")  
resized_gambar = gambar.resize((100, 100))  
tk_image = ImageTk.PhotoImage(resized_gambar)

label_image = ttk.Label(input_frame2, image=tk_image)
label_image.pack()
#Nama Siswa
Matkul_AIK3 = ttk.Label(input_frame1, text="Nama Siswa")
Matkul_AIK3.pack(padx=10,pady=1,fill="x")
#Entry 1
judul_entry = ttk.Entry(input_frame1,textvariable=NAMA)
judul_entry.pack(padx=10,pady=10,fill="x")
#Biologi
Matkul_Kewarganegaraan = ttk.Label(input_frame1, text="Biologi")
Matkul_Kewarganegaraan.pack(padx=10,pady=1,fill="x")
#Entry 2
judul_entry = ttk.Entry(input_frame1,textvariable=BIOLOGI)
judul_entry.pack(padx=10,pady=10,fill="x")
#Fisika
Matkul_AIK3 = ttk.Label(input_frame1, text="Fisika")
Matkul_AIK3.pack(padx=10,pady=1,fill="x")
#Entry 3
judul_entry = ttk.Entry(input_frame1,textvariable=FISIKA)
judul_entry.pack(padx=10,pady=10,fill="x")
#Bahasa Inggris
Matkul_Kewarganegaraan = ttk.Label(input_frame1, text="Inggris")
Matkul_Kewarganegaraan.pack(padx=10,pady=1,fill="x")
#Entry 4
judul_entry = ttk.Entry(input_frame1,textvariable=BAHASA_INGGRIS)
judul_entry.pack(padx=10,pady=10,fill="x")

#Tombol
tombol_hasil = ttk.Button(input_frame1,text="Submit Nilai",command=hasil_prediksi)
tombol_hasil.pack(padx=10,pady=10,fill="x")

output_label = ttk.Label(window, text="", font=("Arial", 12))
output_label.pack()

create_database_table()
    
window.mainloop()