import pygame

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1800, 880))
window_size = (1800,880)

pygame.display.set_caption("Engine Version 1")

circleee = pygame.image.load(r'C:\Users\MSI\Downloads\circleee.png')

moving_right = False
moving_left = False

player_location = [50,50]
player_y_momentum = 0

player_rect = pygame.Rect(player_location[0],player_location[1],circleee.get_width(),circleee.get_height())
test_rect = pygame.Rect(100,100,100,50)

running = True
while running:
    if player_location[1] > window_size[1]-circleee.get_height():
        player_y_momentum = -player_y_momentum
    else:
        player_y_momentum += 0.2
    player_location[1] += player_y_momentum
    screen.fill((10, 10, 20))
    if moving_right:
        player_location[0]+=4
    if moving_left:
        player_location[0]-=4

    player_rect.x = player_location[0]
    player_rect.y = player_location[1]

    if player_rect.colliderect(test_rect):
        pygame.draw.rect(screen,(255,0,0),test_rect)
    else:
        pygame.draw.rect(screen,(0,0,0),test_rect)
    screen.blit(circleee,player_location)     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_LEFT:
                moving_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_LEFT:
                moving_left = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit()