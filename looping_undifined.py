# Program perulangan membaca buku dengan while
jumlah_buku = 10
print("ibu berkata , 'baca semua bukumu'")
jumlah_baca = 0

buku_sudah_dibaca_dan_dipahami = 0
print(f"jumlah buku yang sudah dibaca dan dipahami {buku_sudah_dibaca_dan_dipahami}")

while jumlah_baca < jumlah_buku * 2 :
    jumlah_baca = jumlah_baca + 1
    if buku_sudah_dibaca_dan_dipahami == 9 :
        print(f"Buku ke {buku_sudah_dibaca_dan_dipahami + 1} belum paham")
    else:
        buku_sudah_dibaca_dan_dipahami = buku_sudah_dibaca_dan_dipahami + 1
        print(f"Buku ke {buku_sudah_dibaca_dan_dipahami} Sudah Dibaca dan dipahami ")

print(f"jumlah buku yang sudah dibaca {buku_sudah_dibaca_dan_dipahami}")
if buku_sudah_dibaca_dan_dipahami == jumlah_buku :
    print("Bu, semua buku sudah dibaca dan dipahami")
else:
    print(f"Bu, Tidak semua buku bisa dipahami, Budi hanya bisa memahami {buku_sudah_dibaca_dan_dipahami} buku")



