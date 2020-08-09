import pygame
pygame.init()
# SCREEN

scr = pygame.display.set_mode((800,600))

#Icon And Name
pygame.display.set_caption("Snake")
icon=pygame.image.load("snakke.png")
pygame.display.set_icon(icon)

# A Random Square
def Square( x , y ):
    obj = pygame.draw.rect(scr, (0 , 0 , 255), pygame.Rect( x , y , 30, 30))

x = 375
y = 550
#Actual Game Loop
running = True
while running:
    scr.fill((0 , 0 , 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 5
            elif event.key == pygame.K_RIGHT:
                x += 5
            elif event.key == pygame.K_UP:
                y -= 5
            elif event.key == pygame.K_DOWN:
                y += 5



    # Displaying the Square
    Square(x , y)                           
    pygame.display.update()


