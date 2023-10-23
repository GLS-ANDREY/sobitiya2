import pygame
import time
import random

pygame.init()
b = pygame.font.SysFont("arial", 30, True, True)
e = pygame.display.set_mode([1000, 700])

while True:
    g = random.randint(0, 100)
    loc = random.randint(0, 250)
    col = random.randint(0, 250)
    rgb = random.randint(0, 250)
    rk = random.randint(100, 900)
    kr = random.randint(100, 600)
    s = pygame.event.get()

    for a in s:
        if a.type == pygame.QUIT:
            exit()

        if a.type == pygame.KEYDOWN and a.key != pygame.K_SPACE:
            q = a.key
            t = str(q)
            r = b.render("klavisha" + t, True, [loc, col, rgb])
            e.blit(r, [rk, kr])

        if a.type == pygame.KEYDOWN and a.key == pygame.K_SPACE:
            rr = b.render("probel", True, [200, 200, 201])
            e.blit(rr, [500, 350])

        if a.type == pygame.MOUSEBUTTONDOWN and a.button != 4 and a.button != 5:
            t = str(a.pos[0])
            t2 = str(a.pos[1])
            rrr = b.render("click:  x = " + t + " y = " + t2, True, [loc, col, rgb])
            if a.button == 1:
                p = pygame.transform.scale(rrr, [200, 20])
                e.blit(p, [a.pos[0], a.pos[1]])
            if a.button == 2:
                p = pygame.transform.scale(rrr, [200, 40])
                e.blit(p, [a.pos[0], a.pos[1]])
            if a.button == 3:
                p = pygame.transform.scale(rrr, [200, 60])
                e.blit(p, [a.pos[0], a.pos[1]])

        if a.type == pygame.MOUSEMOTION:
            k = a.pos
            c = pygame.draw.circle(e, [loc, col, rgb], k, 3)

        if a.type == pygame.MOUSEMOTION and a.buttons == (1,0,0):
            c2 = pygame.draw.circle(e, [loc, col, rgb], k, 10)

        if a.type == pygame.MOUSEBUTTONDOWN and a.button == 4:
            rrr = b.render("verx", True, [loc, col, rgb])
            e.blit(rrr, [a.pos[0], a.pos[1]])

        if a.type == pygame.MOUSEBUTTONDOWN and a.button == 5:
            rrr = b.render("vniz", True,
                           [random.randint(0, 250), random.randint(0, 250), random.randint(0, 250)])
            e.blit(rrr, [a.pos[0], a.pos[1]])

        if a.type == pygame.KEYDOWN:
            print(a.key)
        if a.type == pygame.MOUSEBUTTONDOWN:
            print(a.button)
        if a.type == pygame.KEYDOWN or a.type == pygame.MOUSEBUTTONDOWN:
            print(a.type)

    pygame.display.flip()
