daftar_buku = ['Seven Habits', 'Bertani Modern', 'Neo-Paleon', 'skibidi']
print('Tampilkan variabel daftar_buku')
print(daftar_buku)

print('proses semua dengan for in')
for buku in daftar_buku :
    print(buku)

print('\n Tampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print("\n Tampilkan dengan for in range")
for i in  range (0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'danjoi', -313, 3.14]
print('\n proses semua dengan for in range, dimana tipe data elemen berbeda beda')
for buku in daftar_buku :
    print(buku)

print('Kembalikan nilai awal daftar buku')
daftar_buku = ['Seven Habits', 'Bertani Modern', 'Neo-Paleon', 'skibidi']
daftar_buku.append('Dunia Matematik kelas 5')
