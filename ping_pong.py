#importing the pygame module for the game
import pygame
#importing the random module to use random occurences within the game
import random
#we have to initialize pygame to be able to use it
pygame.init()


#Initials
#this is the width and height of the gameboard
WIDTH, HEIGHT = 1480,800

wn = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Reeally Good Ping Pong Game")


run = True
direction = [0, 1]
angle = [0, 1, 2]


#colors
BLUE = (0, 0, 225)
RED = (255, 0 , 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#for the ball
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_vel_x, ball_vel_y = 0.7, 0.7



#paddle dimensions
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH - (100 - paddle_width/2)
right_paddle_vel = left_paddle_vel = 0

# gadgets
left_gadget = right_gadget = 0
left_gadget_remaining = right_gadget_remaining = 5

# Main loop
while run:
    wn.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel = -1.2
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 1.2
            if i.key == pygame.K_RIGHT and right_gadget_remaining > 0:
                right_gadget = 1
            if i.key == pygame.K_w:
                left_paddle_vel = -1.2
            if i.key == pygame.K_s:
                left_paddle_vel = 1.2
            if i.key == pygame.K_d and left_gadget_remaining > 0:
                left_gadget = 1

        if i.type == pygame.KEYUP:
            right_paddle_vel = 0
            left_paddle_vel = 0



    #ball's movement controls
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= -1
    if ball_x >= WIDTH - radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.7, 1.4
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.7, 1.4
        ball_vel_x *= -1
    



    if ball_x <= 0 + radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.0, 0.6
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.6, 0.6
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.6, 1.0
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 1.0, 0.6
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.6, 0.6
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.6, 1.0

    


    #paddle's movement controls
    if left_paddle_y >= HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0

    #paddle collisions
    #left paddle
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_vel_x *= -1

    #right paddle
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x
            ball_vel_x *= -1


    #gadgets in action
    if left_gadget == 1:
        if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
            if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                ball_x = left_paddle_x + paddle_width
                ball_vel_x *= -3.5
                left_gadget = 0
                left_gadget_remaining -= 1

    if right_gadget == 1:
        if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
            if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                ball_x = right_paddle_x
                ball_vel_x *= -3.5
                right_gadget = 0
                right_gadget_remaining -= 1


    #Movements
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel


    #OBJECTS
    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height) )
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height) )
    
    if left_gadget == 1:
        pygame.draw.circle(wn,WHITE, (left_paddle_x + 10, left_paddle_y + 10), 4)
    if right_gadget == 1:
        pygame.draw.circle(wn,WHITE, (right_paddle_x + 10, right_paddle_y + 10), 4)


    pygame.display.update()
pygame.quit()
