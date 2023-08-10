# contoh project

print("ibu memberi perintah beli 1 botol susu")
print("anak menjawab ok")
print("anak pergi ke toko")
print("apakah susu ada?")
print("|||||||||||||||")
bottle_milk_count = 1
egg_count = 6
print(f"jumlah botol {bottle_milk_count} botol")
print(f"jumlah telur {egg_count} telur")
if bottle_milk_count > 0:
    print("ada, anak mengecek harganya, cukup")
    if egg_count > 0:
        print("ada, anak membeli 6 butir telur")
    else:
        print("tidak ada telur, anak membeli 1 botol susu")
else:
    print("tidak ada, anak tidak jadi membeli susu")
print("anak pulang kerumah")
print("menyerahkan hasil belanjanya ke ibu")
print("selesai")

