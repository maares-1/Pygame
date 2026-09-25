# Game Design Document (GDD) - "Snake"

## Gameplay Utama
Tujuan:
Makan sebanyak banyaknya untuk memperoleh skor tertinggi

## Alur Game
Generate Level:
- Posisi spawn bocah random atau di tengah
- Jumlah makanan  = tak terhingga 
- Posisi spawn makanan = random.

Loop Berlanjut:
- Tidak ada batas level → game terus berlanjut sampai pemain menutup game atau menabrak.
- Penjelasan kontrol: Arrow untuk bergerak, atau bisa menggunakan WASD

Gameplay Utama:
- Posisi spawn ular dan makanan random
- Pemain menggerakkan ular dengan arrow ke arah makanan
- Makanan dapat menambah panjang ular dan makanan tertentu menambahkan efek spesial pada ular.
- Ular bergerak menghindari tabrakan dari badan ular sendiri atau batas map

## Mekanik Game
Gerakan:
- Ular : WASD / Arrow Keys

Makanan:
Ada 3 jenis makanan : 1.normal 2.speed boost 3.bonus skor

Collision & Batas Map:
- Menabrak badan ular  → langkah batal → GameOver
- Menabrak batas map → langkah batal → Game Over

Animasi:
- Pergerakan ular 7 fps

  ## Sistem Skor/Progress
  Skor dihitung dari total jumlah makanan yang dimakan
