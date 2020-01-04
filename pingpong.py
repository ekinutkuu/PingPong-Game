import pygame
import sys
pygame.init()

pencere= pygame.display.set_mode((800,600))
pygame.display.set_caption("Ping Pong")
pygame.display.set_icon(pygame.image.load("data/icon.png"))
clock=pygame.time.Clock()

bounce_sound = pygame.mixer.Sound("data/bounce.wav")
score_sound = pygame.mixer.Sound("data/score.wav")

#skor bilgileri
font=pygame.font.SysFont(None,35)
text=font.render("1. Oyuncu : 0        2. Oyuncu : 0", True, (255,255,255))
textRect=text.get_rect()
textRect.center=(400,20)

#değişkenler
oyuncu1=0
oyuncu2=0

sol_y=255
sağ_y=255
top_x=400
top_y=275
top_kontrol_x=1
top_kontrol_y=1


while True:
    #clock.tick(60)
    #pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:sys.exit()

    pencere.fill((0,0,0))
    sol_çubuk = pygame.draw.rect(pencere, (255,255,255), (10,sol_y,20,100))
    sağ_çubuk = pygame.draw.rect(pencere, (255,255,255), (770,sağ_y,20,100))
    top = pygame.draw.rect(pencere, (255,255,255), (top_x,top_y,20,20))


    #skor
    pencere.blit(text, textRect)



    #tuş basımları
    keys=pygame.key.get_pressed()

    if keys[pygame.K_w]:
        sol_y -= 0.5

    if keys[pygame.K_UP]:
        sağ_y -= 0.5

    if keys[pygame.K_s]:
        sol_y += 0.5

    if keys[pygame.K_DOWN]:
        sağ_y += 0.5


    #çubuklar için alan sınırlaması
    if sol_y>490:
        sol_y -= 0.5

    if sol_y<10:
        sol_y += 0.5

    if sağ_y>490:
        sağ_y -= 0.5

    if sağ_y<10:
        sağ_y += 0.5



    top_x+=0.4  * top_kontrol_x
    top_y-=0.4 * top_kontrol_y
    #top için alan sınırlaması ve dışarı çıkma durumları
    if top_y<0:
        top_kontrol_y *= -1
        #pygame.mixer.Sound.play(bounce_sound)

    if top_y>580:
        top_kontrol_y *= -1
        #pygame.mixer.Sound.play(bounce_sound)

    if top_x<0:
        top_x=400
        top_y=275
        top_kontrol_x *= -1
        #print("top dışarıya çıktı")
        oyuncu2+=1
        text=font.render("1. Oyuncu : {}        2. Oyuncu : {}".format(oyuncu1, oyuncu2), True, (255,255,255))
        #print("\n1. Oyuncu : {}        2.Oyuncu : {}".format(oyuncu1, oyuncu2))
        pygame.mixer.Sound.play(score_sound)


    if top_x>800:
        top_x=400
        top_y=275
        top_kontrol_x *= -1
        #print("top dışarıya çıktı")
        oyuncu1 += 1
        text=font.render("1. Oyuncu : {}        2. Oyuncu : {}".format(oyuncu1, oyuncu2), True, (255,255,255))
        #print("\n1. Oyuncu : {}        2.Oyuncu : {}".format(oyuncu1, oyuncu2))
        pygame.mixer.Sound.play(score_sound)


    #topun çubuklara değme durumu
    if top_x>740 and top_x<750 and top_y<sağ_y + 100 and top_y>sağ_y-50:
        #print("top sekti")
        top_x=740
        top_kontrol_x *= -1
        #top_kontrol_y *= -1
        pygame.mixer.Sound.play(bounce_sound)


    if top_x<40 and top_x>30 and top_y<sol_y + 100 and top_y>sol_y-50:
        #print("top sekti")
        top_x=40
        top_kontrol_x *= -1
        #top_kontrol_y *= 1
        pygame.mixer.Sound.play(bounce_sound)


    pygame.display.update()
