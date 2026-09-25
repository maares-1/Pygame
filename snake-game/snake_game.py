import pygame
import random
import sys
from pathlib import Path

pygame.init()

ASSETS_DIR = Path(__file__).parent / "assets"
LEBAR, TINGGI = 1280, 720
UKURAN_SEL = 20
FPS = 7

HITAM = (0, 0, 0)
PUTIH = (255, 255, 255)
MERAH = (255, 0, 0)

FPS_BOOST = FPS * 2
DURASI_BOOST_MS = 4000

JENIS_MAKANAN = {
    "biasa": {"file": "makanan_1.png", "skor": 1, "bobot": 70},
    "bonus": {"file": "makanan_2.png", "skor": 5, "bobot": 15},
    "speed": {"file": "makanan_3.png", "skor": 1, "bobot": 15},
}

layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 24)
font_besar = pygame.font.SysFont("arial", 48)


SPRITE_KEPALA = pygame.transform.smoothscale(
    pygame.image.load(ASSETS_DIR / "snake_head.png").convert_alpha(), (UKURAN_SEL, UKURAN_SEL)
)
SPRITE_BADAN = pygame.transform.smoothscale(
    pygame.image.load(ASSETS_DIR / "snake_body.png").convert_alpha(), (UKURAN_SEL, UKURAN_SEL)
)


SPRITE_MAKANAN = {
    jenis: pygame.transform.smoothscale(
        pygame.image.load(ASSETS_DIR / info["file"]).convert_alpha(),
        (UKURAN_SEL, UKURAN_SEL),
    )
    for jenis, info in JENIS_MAKANAN.items()
}


def buat_background_tersusun(tile):
    hasil = pygame.Surface((LEBAR, TINGGI))
    lebar_tile, tinggi_tile = tile.get_size()
    for y in range(0, TINGGI, tinggi_tile):
        for x in range(0, LEBAR, lebar_tile):
            hasil.blit(tile, (x, y))
    return hasil


BACKGROUND = buat_background_tersusun(
    pygame.image.load(ASSETS_DIR / "grass_bg.jpg").convert()
)

ROTASI_ARAH = {
    (UKURAN_SEL, 0): 0,
    (0, -UKURAN_SEL): 90,
    (-UKURAN_SEL, 0): 180,
    (0, UKURAN_SEL): -90,
}


def posisi_acak():
    x = random.randrange(0, LEBAR // UKURAN_SEL) * UKURAN_SEL
    y = random.randrange(0, TINGGI // UKURAN_SEL) * UKURAN_SEL
    return (x, y)


def buat_makanan(ular):
    while True:
        pos = posisi_acak()
        if pos not in ular:
            break

    jenis = random.choices(
        list(JENIS_MAKANAN.keys()),
        weights=[info["bobot"] for info in JENIS_MAKANAN.values()],
    )[0]

    return {"pos": pos, "jenis": jenis}


def tampilkan_teks_tengah(teks, ukuran_font, warna, y_offset=0):
    render = ukuran_font.render(teks, True, warna)
    rect = render.get_rect(center=(LEBAR // 2, TINGGI // 2 + y_offset))
    layar.blit(render, rect)


def game_loop():
    ular = [(LEBAR // 2, TINGGI // 2)]
    arah = (UKURAN_SEL, 0)
    arah_berikutnya = arah
    makanan = buat_makanan(ular)
    skor = 0
    game_over = False
    boost_aktif_hingga = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_r:
                        return game_loop()
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                else:
                    if event.key in (pygame.K_UP, pygame.K_w) and arah != (0, UKURAN_SEL):
                        arah_berikutnya = (0, -UKURAN_SEL)
                    elif event.key in (pygame.K_DOWN, pygame.K_s) and arah != (0, -UKURAN_SEL):
                        arah_berikutnya = (0, UKURAN_SEL)
                    elif event.key in (pygame.K_LEFT, pygame.K_a) and arah != (UKURAN_SEL, 0):
                        arah_berikutnya = (-UKURAN_SEL, 0)
                    elif event.key in (pygame.K_RIGHT, pygame.K_d) and arah != (-UKURAN_SEL, 0):
                        arah_berikutnya = (UKURAN_SEL, 0)

        if not game_over:
            arah = arah_berikutnya
            kepala_lama = ular[0]
            kepala_baru = (kepala_lama[0] + arah[0], kepala_lama[1] + arah[1])

            if (
                kepala_baru[0] < 0
                or kepala_baru[0] >= LEBAR
                or kepala_baru[1] < 0
                or kepala_baru[1] >= TINGGI
            ):
                game_over = True
            elif kepala_baru in ular:
                game_over = True

            else:
                ular.insert(0, kepala_baru)

                if kepala_baru == makanan["pos"]:
                    info = JENIS_MAKANAN[makanan["jenis"]]
                    skor += info["skor"]

                    if makanan["jenis"] == "speed":
                        boost_aktif_hingga = pygame.time.get_ticks() + DURASI_BOOST_MS

                    makanan = buat_makanan(ular)
                else:
                    ular.pop()

        layar.blit(BACKGROUND, (0, 0))

        layar.blit(SPRITE_MAKANAN[makanan["jenis"]], makanan["pos"])

        for i, segmen in enumerate(ular):
            if i == 0:
                sprite = pygame.transform.rotate(SPRITE_KEPALA, ROTASI_ARAH[arah])
            else:
                sprite = SPRITE_BADAN
            layar.blit(sprite, segmen)

        teks_skor = font.render(f"Skor: {skor}", True, PUTIH)
        layar.blit(teks_skor, (10, 10))

        sisa_boost_ms = boost_aktif_hingga - pygame.time.get_ticks()
        if sisa_boost_ms > 0:
            teks_boost = font.render(f"SPEED BOOST! {sisa_boost_ms / 1000:.1f}s", True, PUTIH)
            layar.blit(teks_boost, (10, 40))

        if game_over:
            overlay = pygame.Surface((LEBAR, TINGGI))
            overlay.set_alpha(180)
            overlay.fill(HITAM)
            layar.blit(overlay, (0, 0))

            tampilkan_teks_tengah("GAME OVER", font_besar, MERAH, -30)
            tampilkan_teks_tengah(f"Skor akhir: {skor}", font, PUTIH, 20)
            tampilkan_teks_tengah("Tekan R untuk main lagi atau Q untuk keluar", font, PUTIH, 60)

        pygame.display.flip()
        kecepatan_saat_ini = FPS_BOOST if pygame.time.get_ticks() < boost_aktif_hingga else FPS
        clock.tick(kecepatan_saat_ini)


if __name__ == "__main__":
    game_loop()
