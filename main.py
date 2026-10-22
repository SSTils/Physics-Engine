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
circle_location = pygame.math.Vector2(900.0,440.0)
circle_xlocation = circle_location[0]
circle_ylocation = circle_location[1]
circle_y_velocity = 0
circle_x_velocity = 10
circle_radius = 70.0
gravity = g = 0.17
heightt = screen.get_height()
bouncing_coefficent = kb = 0.7
wid = screen.get_width()
friction_coefficient_ = mu = 0.2


class entity:
    def __init__(self,mass,x_velocity,y_velocity,x_location,y_location):
        self.mass = mass
        self.location = pygame.math.Vector2(x_location,y_location)
        self.velocity = pygame.math.Vector2(x_velocity,y_velocity)
    def get_ffriction(self, gravity, friction_co):
        friction_force = self.mass*gravity*friction_co
        return friction_force
    def get_acceleration(self,net_force):
        acceleration = net_force/self.mass
        return acceleration
    

class particle(entity):
    def __init__(self, x_location,y_location,x_velocity,y_velocity,mass,radius,color):
        super().__init__(mass,x_velocity,y_velocity,x_location,y_location)
        self.radius = radius
        self.color = color
    def get_bounds(self):
        lowest_point = self.location.y + self.radius
        x_right = self.location.x + self.radius
        x_left = self.location.x - self.radius
        return lowest_point,x_right,x_left

    def update(self,height, width, gravity,bounce_coefficient,friction_coefficient):
        if self.location.y + self.radius < height:
            self.velocity.y += gravity
        self.location.y += self.velocity.y
        if self.location.y + self.radius >= height:
            self.location.y = height -self.radius
            self.velocity.y = (-self.velocity.y)
            self.velocity.y = bounce_coefficient*self.velocity.y
            if (abs(self.velocity.y) <= (gravity+0.2)) and (self.location.y + self.radius == height):
                self.velocity.y = 0
                gravity = 0
        gravity = g
        self.location.x += self.velocity.x
        if (self.location.x +self.radius >= width):
            self.location.x = width - self.radius
            self.velocity.x = (-self.velocity.x)
            self.velocity.x = bounce_coefficient*self.velocity.x
            if (abs(self.velocity.x) <= (0.37)) and ((self.location.x + self.radius == width) or (self.location.x - self.radius == 0)):
                self.velocity.x = 0
        if not(self.location.x+self.radius>= width) or not(self.location.x - self.radius <= 0):
            friction_force = self.get_ffriction(gravity,friction_coefficient)
            acceleration = self.get_acceleration(friction_force)
            if self.velocity.x>0 and self.location.y + self.radius >= height:
                self.velocity.x -= acceleration
            if self.velocity.x<0 and self.location.y + self.radius >= height:
                self.velocity.x += acceleration
            if abs(self.velocity.x) <=0.37 and self.location.y + self.radius >= height:
                self.velocity.x = 0 

        if (self.location.x - self.radius <= 0):
            self.location.x = self.radius
            self.velocity.x = (-self.velocity.x)
            self.velocity.x = bounce_coefficient*self.velocity.x
            if (abs(self.velocity.x) <= (0.37)) and ((self.location.x + self.radius == width) or self.location.x - self.radius == 0):
                self.velocity.x = 0
        

    def draw(self, surface ):
        pygame.draw.circle(surface, self.color, (int(self.location.x),int(self.location.y)), float(self.radius))
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