print('Ibu berkata, \"Pergi ke toko\"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab , "Beli satu botol susu, dan jika ada telur beli 6"')
print("maka budi berangkat ke toko")
print("dan mulai berbelanja")
print("||||||||||||||||||||||||")

# percabangan
milk_bottle_count = 1
egg_count = 6
print(f"jumlah telur {egg_count} telur")
print(f"Jumlah botol {milk_bottle_count} botol ")

if milk_bottle_count > 0:
    print("budi mengecek harganya, dan ternyata uangnya cukup")
    if egg_count == 0:
        print("budi membeli 1 botol susu")
    else:
        print("budi membeli 6 botol susu")
else:
    print("budi tidak jadi membeli1 botol susu")

print("budi pulang kerumah")
print("menyampaikan hasilnya kepada ibu")
