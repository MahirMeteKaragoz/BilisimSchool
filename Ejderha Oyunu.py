import pygame,random,time

pygame.init()
# değişkenler
genislik = 1000
yukseklik = 600
FPS = 30
saat = pygame.time.Clock()
karakter_ilk_cani = 5
karakter_hizi = 10
para_ilk_hizi = 10
para_ivmesi = 0.5
tampon_mesafesi = 100

skor = 0

karakter_cani = karakter_ilk_cani
para_hizi = para_ilk_hizi

yesil = (0,255,0)
koyu_yesil = (10,50,10)
beyaz = (255,255,255)
siyah = (0,0,0)

font = pygame.font.Font("AttackGraffiti.ttf",32)

skor_metni = font.render("SKOR:" + str(skor),True,yesil,beyaz)
skor_metni_koordinati = skor_metni.get_rect()
skor_metni_koordinati.topleft = (10,10)

oyun_basligi = font.render("Ejderha Yem Yeme Oyun",True,koyu_yesil,beyaz)
oyun_basligi_koordinati = oyun_basligi.get_rect()
oyun_basligi_koordinati.centerx = genislik//2
oyun_basligi_koordinati.top = 10

kalan_cani = font.render("CAN:" + str(karakter_cani), True, yesil,beyaz )
kalan_cani_koordinati = kalan_cani.get_rect()
kalan_cani_koordinati.topright  = (genislik-10,10)

oyun_bitti = font.render("OYUN BITTI",True,siyah,yesil)
oyun_bitti_koordinati = oyun_bitti.get_rect()
oyun_bitti_koordinati.center = (genislik//2,yukseklik//2)


yeniden_giris = font.render("HERHANGI BIR TUSA BASINIZ",True,siyah,yesil)
yeniden_giris_koordinati = yeniden_giris.get_rect()
yeniden_giris_koordinati.center = (genislik//2,yukseklik//2 +50)

para_sesi = pygame.mixer.Sound("kazanma.wav")
yanma_sesi = pygame.mixer.Sound("yanma.wav")
pygame.mixer.music.load("arkaplan ses.mp3")
pygame.mixer.music.play(-1,0.0)

goruntu_yuzeyi = pygame.display.set_mode((genislik,yukseklik))

karakter = pygame.image.load("ejderha.png")
karakter_koordinati = karakter.get_rect()
karakter_koordinati.topleft = (100,100)

para = pygame.image.load("para")
para_koordinati = para.get_rect()
para_koordinati.center = (genislik//2,yukseklik//2-50)

durum = True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            durum = False

    tus = pygame.key.get_pressed()
    if tus[pygame.K_UP] and karakter_koordinati.top > 64:
        karakter_koordinati.y = karakter_koordinati.y - karakter_hizi

    elif tus[pygame.K_DOWN] and karakter_koordinati.bottom<yukseklik:
        karakter_koordinati.y = karakter_koordinati.y + karakter_hizi

    if para_koordinati.x < 0:
        karakter_cani = karakter_cani - 1
        yanma_sesi.play()
        para_koordinati.x = genislik + tampon_mesafesi
        para_koordinati.y = random.randint(64, yukseklik-30)
        kalan_cani = font.render("CAN:" + str(karakter_cani), True, yesil, beyaz)
    else:
        para_koordinati.x = para_koordinati.x - para_hizi

    if karakter_koordinati.colliderect(para_koordinati):
        skor = skor + 1
        para_sesi.play()
        para_koordinati.x = genislik + tampon_mesafesi
        para_koordinati.y = random.randint(64,yukseklik-30)
        para_hizi = para_hizi + para_ivmesi
        skor_metni = font.render("SKOR:" + str(skor), True, yesil, beyaz)
        kalan_cani = font.render("CAN:" + str(karakter_cani), True, yesil, beyaz)


    if karakter_cani == 0:
        goruntu_yuzeyi.blit(oyun_bitti, oyun_bitti_koordinati)
        time.sleep(1)
        goruntu_yuzeyi.blit(yeniden_giris, yeniden_giris_koordinati)
        pygame.display.update()
        pygame.mixer.music.stop()
        durdu = True
        while durdu:
            for etkinlik in pygame.event.get():
                if etkinlik.type == pygame.KEYDOWN:
                    skor = 0
                    karakter_cani = karakter_ilk_cani
                    para_hizi = para_ilk_hizi
                    karakter_koordinati.y = (yukseklik //2)
                    pygame.mixer.music.play(-1,0.0)
                    durdu = False
                if etkinlik.type == pygame.QUIT:
                    durum = False
                    durdu = False




    goruntu_yuzeyi.fill(siyah)
    goruntu_yuzeyi.blit(skor_metni,skor_metni_koordinati)
    goruntu_yuzeyi.blit(oyun_basligi,oyun_basligi_koordinati)
    goruntu_yuzeyi.blit(kalan_cani,kalan_cani_koordinati)
    pygame.draw.line(goruntu_yuzeyi,beyaz,(0,64),(genislik,64),2)

    goruntu_yuzeyi.blit(karakter,karakter_koordinati)
    goruntu_yuzeyi.blit(para,para_koordinati)
    pygame.display.update()
    saat.tick(FPS)
pygame.quit()
