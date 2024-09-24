import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

rctPaddle1 = pygame.Rect(0,0,100,10)
rctPaddle2 = pygame.Rect(0,20,100,10)

while True:

    #Player inputs

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Logical Updates

    screen.fill("black") #Fills the screen black

    #Render
    pygame.draw.rect(screen, "white" , rctPaddle1)
    pygame.draw.rect(screen, "white" , rctPaddle2)


    pygame.display.flip()
    clock.tick(60)