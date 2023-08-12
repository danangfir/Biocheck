daftar_buku = ['seven habits', 'how to influence people', 'first things first', '4DX']
print('tampilkan daftar variable daftar_buku')
print(daftar_buku)

print('\nproses semua dengan for in')
for buku in daftar_buku :
    print(buku)
print('Tampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[1])

print("\n Tampilkan dengan for in range")
for i in range (0, len(daftar_buku)) :
    print(daftar_buku[i])

daftar_buku = [1, 'Kenji Volume 2', -313, 3.14]
print("\n Tampilkan dengan for in range, diman tipe data tiap elemen berbeda beda")
for i in range (0, len(daftar_buku)) :
    print(daftar_buku[i])

print('kembalikan nilai awal yang daftar_buku')
daftar_buku = ['seven habits', 'how to influence people', 'first things first', '4DX']
print('Tambahkan 1 buku baru')
daftar_buku.append('Dunia matematika Kelas 5')
for i in range (0, len(daftar_buku)) :
    print(daftar_buku[i])