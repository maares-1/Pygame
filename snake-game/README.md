# Snake Game

Game Snake klasik yang dibuat dengan Python dan [pygame](https://www.pygame.org/), dengan tampilan yang sudah dikustomisasi: sprite ular sendiri, variasi makanan dengan efek berbeda, dan background environment rumput.

## Fitur

- **Kontrol ular** dengan arrow keys atau WASD, bergerak di layar 1280x720.
- **Sprite kustom** untuk kepala (dengan mata & lidah, otomatis berputar mengikuti arah gerak) dan badan ular, terpisah dari sprite makanan.
- **3 jenis makanan** dengan bobot kemunculan, skor, dan efek berbeda:
  | Jenis | Skor | Efek |
  |---|---|---|
  | Biasa | +1 | - |
  | Bonus | +5 | - |
  | Speed | +1 | Speed boost 4 detik (kecepatan game 2x lipat) |
- **Background environment** rumput-tanah-batu yang di-tile otomatis menutupi seluruh layar, berapa pun ukuran file gambarnya.
- **Skor & indikator speed boost** ditampilkan real-time di layar.
- **Layar Game Over** dengan opsi main lagi (`R`) atau keluar (`Q`).

## Cara menjalankan

Pastikan Python dan pygame sudah terpasang:

```bash
pip install pygame
```

Lalu jalankan:

```bash
python snake_game.py
```

## Kontrol

| Tombol | Aksi |
|---|---|
| ↑ / W | Gerak ke atas |
| ↓ / S | Gerak ke bawah |
| ← / A | Gerak ke kiri |
| → / D | Gerak ke kanan |
| R | Main lagi (saat Game Over) |
| Q | Keluar (saat Game Over) |

## Struktur proyek

```
snake_game.py       # kode utama game
assets/
  snake_head.png     # sprite kepala ular
  snake_body.png      # sprite badan ular
  makanan_1.png       # sprite makanan biasa
  makanan_2.png        # sprite makanan bonus
  makanan_3.png        # sprite makanan speed boost
  grass_bg.jpg         # tekstur background (di-tile otomatis)
```

Semua sprite dan konfigurasi (ukuran layar, kecepatan, bobot kemunculan makanan, dll) bisa diganti dengan mengganti file di folder `assets/` atau mengubah konstanta di bagian atas `snake_game.py`.
