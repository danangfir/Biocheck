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
print('\n Tambahkan satu buku baru')
daftar_buku.append('Dunia Matematik kelas 5')
for i in  range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n Clear List')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n Ganti Elemen Pertama')
daftar_buku = ['Seven Habits', 'Bertani Modern', 'Neo-Paleon', 'skibidi']
daftar_buku[0] = 'Paleon Modern'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n ambil elemen tertentu')
buku = daftar_buku.pop(3)
print(buku)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n Buku yang diambil tadi')
print(buku)


print('\n Pop Tertentu |||')
daftar_buku = ['Seven Habits', 'Bertani Modern', 'Neo-Paleon', 'skibidi']
daftar_buku.pop(-3)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n Perintah Del')
daftar_buku = ['Seven Habits', 'Bertani Modern', 'Neo-Paleon', 'skibidi']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n Perintah del dengan list comprehension (Hapus Semua) ')
daftar_buku = ['Seven Habits', 'Bertani Modern', 'Neo-Paleon', 'skibidi']
del  daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n Perintah del dengan list comprehension start')
daftar_buku = ['-Seven Habits', '-Bertani Modern', '-Neo-Paleon', '-skibidi']
del  daftar_buku[0:-2] # Start : Mulai dari end / Jumlah terakhir
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n Perintah del dengan list comprehension start (Step)')
daftar_buku = ['-Seven Habits', '-Bertani Modern', '-Neo-Paleon', '-skibidi']
del  daftar_buku[0::2] # Start-End : Step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])



