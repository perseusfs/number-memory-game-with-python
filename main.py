import pygame
import random
import sys
from pygame.locals import *

BGCOLOR = (57, 62, 70)
WHITE = (255, 255, 255)
WIDTH = 700
HEIGHT = 400
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Number Memory Game")
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
font = pygame.font.SysFont("None", 20)


def draw_text(text, fonts, color, surface, x, y):
    textobj = fonts.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def draw_numbers(text, fonts, color, surface, x, y):
    textobj = fonts.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def draw_list(numberlist):
    length = len(numberlist)
    #for i in range(length):
    draw_numbers(numberlist, font, (255, 255, 255), screen, randomx(), randomy())


def randomer(pattern):
    number = ""
    patternn = int(pattern)
    for item in range(0, patternn):
        randomnumber = random.randint(0, 9)
        number += str(randomnumber)
    return number


def randomx():
    x = random.randint(20, 580)
    return x


def randomy():
    y = random.randint(145, 380)
    return y


def check(inputnumbers, numberlist, userinput):
    if inputnumbers == numberlist:
        draw_text("Correct", font, (255, 255, 255), screen, 260, 120)
        numberinput = int(userinput)
        numberinput += 1
        userinput = str(numberinput)
        ingame(userinput)
    else:
        draw_text("Does not match", font, (255, 255, 255), screen, 260, 120)
        gameover()


def main_menu():
    click = False
    while True:

        screen.fill(BGCOLOR)
        draw_text("Main Menu", font, (255, 255, 255), screen, 20, 20)
        draw_text("Press ESC to Quit", font, (255, 255, 255), screen, 440, 20)
        draw_text("By Utku Faruk Şen", font, (255, 255, 255), screen, 440, 380)

        mx, my = pygame.mouse.get_pos()

        button1 = pygame.Rect(50, 100, 200, 50)
        button2 = pygame.Rect(50, 200, 200, 50)
        button3 = pygame.Rect(50, 300, 200, 50)

        if button1.collidepoint((mx, my)):
            if click:
                game()
        if button2.collidepoint((mx, my)):
            if click:
                settings()
        if button3.collidepoint((mx, my)):
            if click:
                howtoplay()
        pygame.draw.rect(screen, (126, 116, 116), button1)
        pygame.draw.rect(screen, (126, 116, 116), button2)
        pygame.draw.rect(screen, (126, 116, 116), button3)

        draw_text("Play", font, (255, 255, 255), screen, 130, 120)
        draw_text("Settings", font, (255, 255, 255), screen, 120, 220)
        draw_text("How to Play", font, (255, 255, 255), screen, 100, 320)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def game():
    userinput = ''
    running = True
    click = False
    while running:
        screen.fill(BGCOLOR)
        draw_text("Game", font, (255, 255, 255), screen, 20, 20)
        draw_text("Press ESC to Go Back", font, (255, 255, 255), screen, 440, 20)
        draw_text("Choose a Number Between 0-10 and Click Start : ", font, (255, 255, 255), screen, 20, 60)

        mx, my = pygame.mouse.get_pos()
        button4 = pygame.Rect(50, 200, 200, 50)
        pygame.draw.rect(screen, (126, 116, 116), button4)
        draw_text("Start", font, (255, 255, 255), screen, 130, 220)

        if button4.collidepoint((mx, my)):
            if click:
                ingame(userinput)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_0]:
                    userinput += "0"
                elif pressed[pygame.K_1]:
                    userinput += "1"
                elif pressed[pygame.K_2]:
                    userinput += "2"
                elif pressed[pygame.K_3]:
                    userinput += "3"
                elif pressed[pygame.K_4]:
                    userinput += "4"
                elif pressed[pygame.K_5]:
                    userinput += "5"
                elif pressed[pygame.K_6]:
                    userinput += "6"
                elif pressed[pygame.K_7]:
                    userinput += "7"
                elif pressed[pygame.K_8]:
                    userinput += "8"
                elif pressed[pygame.K_9]:
                    userinput += "9"
        text = str(userinput)
        draw_text(text, font, (255, 255, 255), screen, 338, 60)

        pygame.display.update()
        mainClock.tick(60)


def settings():
    running = True
    while running:
        screen.fill(BGCOLOR)
        draw_text("Settings", font, (255, 255, 255), screen, 20, 20)
        draw_text("Press ESC to Go Back", font, (255, 255, 255), screen, 440, 20)

        draw_text("No Settings Here", font, (255, 255, 255), screen, 50, 100)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def howtoplay():
    running = True
    while running:
        screen.fill(BGCOLOR)
        draw_text("How to Play", font, (255, 255, 255), screen, 20, 20)
        draw_text("Press ESC to Go Back", font, (255, 255, 255), screen, 440, 20)
        draw_text("Select how many numbers will be your starting pattern and press start.", font, (255, 255, 255), screen, 20, 70)
        draw_text("Memorize the numbers appearing on the screen and input the correct pattern.", font, (255, 255, 255), screen, 20, 100)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def ingame(userinput):
    running = True
    while running:
        screen.fill(BGCOLOR)
        draw_text("Game Screen", font, (255, 255, 255), screen, 20, 20)
        draw_text("Press ESC to Go Back", font, (255, 255, 255), screen, 440, 20)

        numberlist = randomer(userinput)
        draw_list(numberlist)
        waitforinput(numberlist, userinput)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
                    running = False
        pygame.display.update()
        mainClock.tick(60)


def waitforinput(numberlist, userinput):
    running = True
    click = False
    inputnumbers = ""
    counter, text = 10, '10'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clock = pygame.time.Clock()
    while running:

        mx, my = pygame.mouse.get_pos()
        button5 = pygame.Rect(50, 100, 200, 50)
        pygame.draw.rect(screen, (126, 116, 116), button5)
        draw_text("Check", font, (255, 255, 255), screen, 130, 120)
        draw_text("Numbers : ", font, (255, 255, 255), screen, 20, 60)
        draw_text("Countdown", font, (255, 255, 255), screen, 430, 65)

        if button5.collidepoint((mx, my)):
            if click:
                check(inputnumbers, numberlist, userinput)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
                    running = False
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_0]:
                    inputnumbers += "0"
                elif pressed[pygame.K_1]:
                    inputnumbers += "1"
                elif pressed[pygame.K_2]:
                    inputnumbers += "2"
                elif pressed[pygame.K_3]:
                    inputnumbers += "3"
                elif pressed[pygame.K_4]:
                    inputnumbers += "4"
                elif pressed[pygame.K_5]:
                    inputnumbers += "5"
                elif pressed[pygame.K_6]:
                    inputnumbers += "6"
                elif pressed[pygame.K_7]:
                    inputnumbers += "7"
                elif pressed[pygame.K_8]:
                    inputnumbers += "8"
                elif pressed[pygame.K_9]:
                    inputnumbers += "9"
            draw_text(inputnumbers, font, (255, 255, 255), screen, 90, 60)
            if event.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else 'time is up'
                if counter == 0:
                    gameover()
            if event.type == pygame.QUIT: break
        else:
            screen.fill((57, 62, 70), (440, 80, 450, 90))
            screen.blit(font.render(text, True, (255, 0, 0)), (444, 80))
            pygame.display.flip()
            clock.tick(60)
            continue


        pygame.display.update()
        mainClock.tick(60)


def gameover():
    click = False
    running = True
    while running:
        screen.fill(BGCOLOR)
        draw_text("Game Over", font, (255, 255, 255), screen, 20, 20)
        draw_text("Wrong Answer...", font, (255, 255, 255), screen, 20, 60)
        draw_text("Press ESC to Go Back", font, (255, 255, 255), screen, 440, 20)

        mx, my = pygame.mouse.get_pos()

        button6 = pygame.Rect(50, 100, 200, 50)
        button7 = pygame.Rect(50, 200, 200, 50)

        pygame.draw.rect(screen, (126, 116, 116), button6)
        pygame.draw.rect(screen, (126, 116, 116), button7)

        draw_text("Play Again", font, (255, 255, 255), screen, 120, 120)
        draw_text("Quit", font, (255, 255, 255), screen, 130, 220)

        if button6.collidepoint((mx, my)):
            if click:
                game()
        if button7.collidepoint((mx, my)):
            if click:
                quit()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()
