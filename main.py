import pygame

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1800, 880))
window_size = (1800,880)

pygame.display.set_caption("Engine Version 1")

# circleee = pygame.image.load(r'C:\Users\MSI\Downloads\circleee.png')

moving_right = False
moving_left = False

# player_location = [50,50]
player_y_momentum = 0

# player_rect = pygame.Rect(player_location[0],player_location[1],circleee.get_width(),circleee.get_height())
# test_rect = pygame.Rect(100,100,100,50)
circle_xlocation = (900)
circle_ylocation = (440)
circle_y_velocity = 0
circle_x_velocity = 0
circle_radius = 70.0
gravity = g = 0.1635

running = True
while running:
    # if player_location[1] > window_size[1]-circleee.get_height():
    #     player_y_momentum = -player_y_momentum
    # else:
    #     player_y_momentum += 0.2
    # player_location[1] += player_y_momentum
    screen.fill((23, 35, 61))
    # if moving_right:
    #     player_location[0]+=4
    # if moving_left:
    #     player_location[0]-=4

    # player_rect.x = player_location[0]
    # player_rect.y = player_location[1]

    point_circle = pygame.draw.circle(screen,(75, 145, 145),(circle_xlocation,circle_ylocation),circle_radius)
    if circle_ylocation + circle_radius < screen.get_height():
        circle_y_velocity += g
    if circle_ylocation + circle_radius >= screen.get_height():
        circle_y_velocity = (-circle_y_velocity)
    if circle_y_velocity > 0:
        circle_ylocation += circle_y_velocity
    if circle_y_velocity < 0:
        circle_ylocation += circle_y_velocity
    # if player_rect.colliderect(test_rect):
    #     pygame.draw.rect(screen,(255,0,0),test_rect)
    # else:
    #     pygame.draw.rect(screen,(0,0,0),test_rect)
    # screen.blit(circleee,player_location)     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         moving_right = True
        #     if event.key == pygame.K_LEFT:
        #         moving_left = True
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_RIGHT:
        #         moving_right = False
        #     if event.key == pygame.K_LEFT:
        #         moving_left = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit()