import pygame
import math
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1800, 880))

pygame.display.set_caption("Engine Version 1")

circle_location = pygame.math.Vector2(900.0,440.0)
circle_xlocation = circle_location.x
circle_ylocation = circle_location.y
circle_y_velocity = 0
circle_x_velocity = 12
circle_radius = 70.0
gravity = g = 0.2
heightt = screen.get_height()
bouncing_coefficent = kb = 0.7
wid = screen.get_width()
friction_coefficient_ = mu = 0.2
dt = 1/ 60.0
accumulator = 0.0
class entity:
    def __init__(self,mass,x_velocity,y_velocity,x_location,y_location):
        self.mass = mass
        self.location = pygame.math.Vector2(x_location,y_location)
        self.velocity = pygame.math.Vector2(x_velocity,y_velocity)
        self.is_being_dragged = False
    def get_ffriction(self, gravity, friction_co):
        friction_force = self.mass*gravity*friction_co
        return friction_force
    def get_acceleration(self,net_force):
        acceleration = net_force/self.mass
        return acceleration

class particle(entity):
    def __init__(self, x_location,y_location,x_velocity,y_velocity,mass,radius,color,previous_mouse): # IMPORTANT ************************************************************
        super().__init__(mass,x_velocity,y_velocity,x_location,y_location)
        self.radius = radius
        self.color = color
        self.previous_mouse = previous_mouse # IMPORTANT ************************************************************

    # IMPORTANT ************************************************************
    def in_or_not(self,mouse_location): 
        inside = False
        if (((mouse_location.y-self.location.y)**2) + ((mouse_location.x - self.location.x)**2) <= self.radius**2):
            inside = True
        return inside 
    # IMPORTANT ************************************************************
    def get_bounds(self):
        lowest_point = self.location.y + self.radius
        x_right = self.location.x + self.radius
        x_left = self.location.x - self.radius
        return lowest_point,x_right,x_left

    def update(self,height, width, gravity,bounce_coefficient,friction_coefficient,current_mouse): # IMPORTANT ************************************************************
        if self.is_being_dragged: # IMPORTANT ************************************************************
            drag = current_mouse - self.previous_mouse # IMPORTANT ************************************************************
            self.location += drag # IMPORTANT ************************************************************
            self.previous_mouse = current_mouse # IMPORTANT ************************************************************
        else:

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

        

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.location.x),int(self.location.y)), float(self.radius))
par1 = particle(circle_xlocation, circle_ylocation,circle_x_velocity,circle_y_velocity, 10, circle_radius,(75, 145, 145),None) # IMPORTANT ************************************************************

running = True
while running:
    frame_time = clock.tick()/1000.0
    accumulator += frame_time

    # VERY IMPORTANT ************************************************************
    while accumulator >= dt:
        live_cursor = pygame.math.Vector2(pygame.mouse.get_pos())
        par1.update(heightt, wid, g, kb, mu, live_cursor)
        accumulator -= dt
    # VERY IMPORTANT ************************************************************

    screen.fill((23, 35, 61))
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
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            par1.previous_mouse = pygame.math.Vector2(pygame.mouse.get_pos()) # VERY IMPORTANT ************************************************************
            if event.button == 1 and par1.in_or_not(pygame.math.Vector2(pygame.mouse.get_pos())) : # IMPORTANT ************************************************************
                par1.is_being_dragged = True # IMPORTANT ************************************************************
        if event.type == pygame.MOUSEBUTTONUP: # IMPORTANT ************************************************************
            par1.is_being_dragged = False # IMPORTANT ************************************************************

    pygame.display.flip()

pygame.quit()