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
circle_x_velocity = 10
circle_radius = 70.0
gravity = g = 0.17
heightt = screen.get_height()
bouncing_coefficent = kb = 0.7
wid = screen.get_width()
friction_coefficient_ = mu = 0.7


class entity:
    def __init__(self,mass,x_velocity,y_velocity,x_location,y_location):
        self.mass = mass
        self.x_velocity = x_velocity
        self.x_location = x_location
        self.y_velocity = y_velocity
        self.y_location = y_location
    def get_ffriction(self, gravity, friction_co):
        friction_force = self.mass*gravity*friction_co
        return friction_force
    def get_acceleration(self,net_force):
        acceleration = net_force/self.mass
        return acceleration
    

class particle(entity):
    def __init__(self, x_location,y_location,x_velocity,y_velocity,mass,radius,color):
        self.x_location = x_location
        self.y_location = y_location
        self.mass = mass
        self.radius = radius
        self.color = color

        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
    def get_bounds(self):
        lowest_point = self.y_location + self.radius
        x_right = self.x_location + self.radius
        x_left = self.x_location - self.radius
        return lowest_point,x_right,x_left

    def update(self,height, width, gravity,bounce_coefficient,friction_coefficient):
        if self.y_location + self.radius < height:
            self.y_velocity += gravity
        self.y_location += self.y_velocity
        if self.y_location + self.radius >= height:
            self.y_location = height -self.radius
            self.y_velocity = (-self.y_velocity)
            self.y_velocity = bounce_coefficient*self.y_velocity
            if (abs(self.y_velocity) <= (gravity+0.2)) and (self.y_location + self.radius == height):
                self.y_velocity = 0
                gravity = 0
        gravity = g
        self.x_location += self.x_velocity
        if (self.x_location +self.radius >= width):
            self.x_location = width - self.radius
            self.x_velocity = (-self.x_velocity)
            self.x_velocity = bounce_coefficient*self.x_velocity
            if (abs(self.x_velocity) <= (0.37)) and ((self.x_location + self.radius == width) or (self.x_location - self.radius == 0)):
                self.x_velocity = 0
        if not(self.x_location+self.radius>= width) or not(self.x_location - self.radius <= 0):
            friction_force = entity.get_ffriction(self.mass,gravity,friction_coefficient)
            acceleration = entity.get_acceleration(particle,friction_force)

        if (self.x_location - self.radius <= 0):
            self.x_location = self.radius
            self.x_velocity = (-self.x_velocity)
            self.x_velocity = bounce_coefficient*self.x_velocity
            if (abs(self.x_velocity) <= (0.37)) and ((self.x_location + self.radius == width) or self.x_location - self.radius == 0):
                self.x_velocity = 0
        

    def draw(self, surface ):
        pygame.draw.circle(surface, self.color, (int(self.x_location),int(self.y_location)), float(self.radius))
par1 = particle(circle_xlocation, circle_ylocation,circle_x_velocity,circle_y_velocity, 10, circle_radius,(75, 145, 145))

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
    par1.update(heightt,wid,g,kb,mu)
    par1.draw(screen)

    # *********************************************FIRST VERSION********************************************************

    # point_circle = pygame.draw.circle(screen,(75, 145, 145),(circle_xlocation,circle_ylocation),circle_radius)
    # if circle_ylocation + circle_radius < screen.get_height():
    #     circle_y_velocity += g
    # if circle_ylocation + circle_radius >= screen.get_height():
    #     circle_y_velocity = (-circle_y_velocity)
    # if circle_y_velocity > 0:
    #     circle_ylocation += circle_y_velocity
    # if circle_y_velocity < 0:
    #     circle_ylocation += circle_y_velocity

    # *********************************************FIRST VERSION********************************************************

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