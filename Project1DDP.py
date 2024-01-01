import tkinter as tk
from tkinter import messagebox


def tampilkan_informasi_penyakit():
    penyakit = var_penyakit.get()

    if penyakit == "Demam Pada Anak":
        informasi = "Demam pada anak termasuk mudah dipastikan. Orang tua cukup mengukur suhu tubuh anak dengan termometer. Bila hasilnya menandakan temperatur yang tinggi, anak dapat dikatakan mengalami demam. Diagnosis demam jika di atas 37.4'CNamun harus dipastikan terlebih dulu bahwa pemeriksaan suhu tersebut dilakukan ketika anak sedang tenang agar hasilnya akurat.Karena demam hanyalah sebuah gejala dari suatu penyakit, dokter akan melakukan beberapa pemeriksaan untuk mencari penyebabnya. Serangkaian pemeriksaan penunjang yang mungkin meliputi tes darah, tes urine, serta rontgen dan pemeriksaan pencitraan lainnya " \
                    "Obat yang dapat digunakan: Parasetamol."
    elif penyakit == "Flu":
        informasi = "Diagnosis flu (influenza)Dokter akan menanyakan riwayat penyakit, melakukan pemeriksaan fisik, mengidentifikasi gejala flu yang timbul, dan melakukan tes untuk mendeteksi virus influenza.Tes yang paling sering digunakan adalah tes diagnostik influenza cepat. Tes ini mencari zat (antigen) dari belakang hidung atau tenggorokan.Hasil dari tes akan keluar dalam 15 menit. Namun, hasilnya akan bervariasi dan tidak selalu akurat. Dokter dapat mendiagnosis berdasarkan gejala, walaupun hasil tes negatif. " \
                    "Obat yang dapat digunakan: Antivirus, obat flu."
    elif penyakit == "Diare":
        informasi = "Untuk memastikan diagnosis diare, dokter akan melakukan sederet metode pemeriksaan berikut:Tanya jawab Dokter akan menanyakan gejala diare, riwayat medis, riwayat penggunaan obat-obatan, riwayat medis keluarga, serta riwayat bepergian pasien.Pemeriksaan fisik Dokter juga akan memeriksa ada tidaknya tanda-tanda dehidrasi pada pasien.Karena kebanyakan kasus diare membaik tanpa pengobatan, dokter sering bisa mendiagnosis diare tanpa pemeriksaan khusus. Tetapi pada beberapa kasus (seperti diare yang berlangsung lebih dari satu minggu) pemeriksaan lanjutan mungkin akan dilakukan.Pemeriksaan tersebut bisa berupa:Tes darah lengkap Tes darah lengkap bisa mendeteksi kondisi-kondisi tertentu. Contohnya anemia dapat menandakan adanya malnutrisi, perdarahan saluran cerna, atau irritable bowel disease (IBD).Pemeriksaan fungsi hati Pemeriksaan fungsi hati yang dilakukan meliputi tes kadar albumin.Pemeriksaan malabsorpsi (gangguan pencernaan) Pemeriksaan ini dilakukan untuk mendeteksi fungsi cerna kalsium, vitamin B-12, dan folat. Status zat besi dan fungsi kelenjar tiroid juga dapat dinilai.Pemeriksaan antibodi pemeriksaan ini dilakukan untuk mendeteksi penyakit celiac.Tes feses (tinja) Dokter dapat mengidentifikasi adanya parasit, bakteri, dan virus pada kultur tinja. Tes tinja juga dapat mendeteksi darah, sel darah putih, dan sel lain untuk menentukan penyebab diare." \
                    "Obat yang dapat dipakai:Antibiotik dan Antasida."
    else:
        informasi = "Penyakit tidak dikenali."

    messagebox.showinfo("Diagnosis Penyakit Dan Obat", informasi)

# Membuat jendela utama
root = tk.Tk()
root.title("Your Diagnosis Solution")
root.geometry("400x400")

# Membuat variabel StringVar untuk penyakit
var_penyakit = tk.StringVar()

# Membuat label dan opsi penyakit
label_penyakit = tk.Label(root, text="Pilih Penyakit:")
label_penyakit.pack()

options_penyakit = ["Demam Pada Anak", "Flu", "Diare"]
dropdown_penyakit = tk.OptionMenu(root, var_penyakit, *options_penyakit)
dropdown_penyakit.pack()

# Membuat tombol untuk menampilkan informasi
tombol_tampilkan = tk.Button(root, text="Diagnosis Informasi Dan Obat", command=tampilkan_informasi_penyakit)
tombol_tampilkan.pack()

# Menjalankan aplikasi
root.mainloop()
