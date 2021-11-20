import pygame
import random
pygame.init()

# set up main variables
clock = pygame.time.Clock() 
#speed = 30  # in frames per second
display_width = 500
display_height = 300

x = 100
y = 100
radius = 10 # defines the ball
dx = 3 # movement on x axis
dy = 3 # movement on y axis

paddle_x = 10
paddle_y = 10
paddle_width = 3
paddle_height = 40 # defines the paddle

play_score = 0 #scorekeeping

# set up functions
def randomize_start():   # randomise the start location
    global x,y,dy  # import global variables
    x = random.randint(int(display_width/4), int(display_width * 0.75))  # randomise x to something reasonable
    y = random.randint(int(display_height/4), int(display_height * 0.75)) # randomise y to something reasonable
    if random.randint(0, 2) % 2 == 0:
        dy *= -1   # apparently changing direction this way is fairer

def hit_back():
    if x + radius > display_width: 
        return True
    return False

def hit_sides():
    if y - radius < 0:
        return True
    if y + radius > display_height:
        return True
    return False

def hit_paddle():
    global play_score # import the global play_score variable
    global speed # and the speed variable
    if x - radius <= paddle_x + paddle_width and y > paddle_y and y < paddle_y + paddle_height:
        play_score += 100 # score goes up by 100 every time the paddle hits the ball 
        speed += 5 # and a bit faster!
        return True
    return False

def game_over():
    global play_score #import the play_score global variable
    end_game = True
    display.fill((0,0,0)) # wipes the screen before filling with text
    font_title = pygame.font.Font(None, 36)
    font_score = pygame.font.Font(None, 24)
    font_instructions = pygame.font.Font(None, 24)
    announcement = font_title.render("GAME OVER!", True, (255, 255, 255))
    announcement_rect = announcement.get_rect(center = (int(display_width/2), int(display_height/4)))
    display.blit(announcement, announcement_rect) # places text and location
    final_score = "Final score: " + str(play_score)   # need to put numeric score in a string
    show_score = font_score.render(final_score, True, (255,255,255))
    show_score_rect = show_score.get_rect(center = (int(display_width/2), int(display_height/2)))
    display.blit(show_score, show_score_rect) # places test and location
    qinstructions = font_instructions.render("Press q to quit or r to replay", True, (255,255,255))
    qinstructions_rect = qinstructions.get_rect(center = (int(display_width/2), int(display_height * 0.75)))
    display.blit(qinstructions, qinstructions_rect) # places text and location
    pygame.display.flip() # flips the blit to the screen so user can see it
    while (end_game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: #quit
                    exit()  
                if event.key == pygame.K_r: #resume
                    play_score = 0 # reset score to 0
                    end_game = False          

display = pygame.display.set_mode((display_width, display_height))

#set initial speed to slow, this will increase if successful
speed = 10

#welcome screen
pygame.display.set_caption("Pong!")
display.fill((0,0,0)) 
welcome_screen = pygame.font.Font(None,30)
welcome = welcome_screen.render("Welcome to PONG!", True, (255,255,255))
welcome_rect = welcome.get_rect(center = (int(display_width/2), int(display_height/3)))
display.blit(welcome, welcome_rect)
pygame.display.flip()
pygame.time.set_timer(pygame.USEREVENT, 5000) # ... wait 5 seconds ...
timer_active = True
while (timer_active):
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            timer_active = False

randomize_start() #random start location of ball

while True:   # main game will execute in this loop
    clock.tick(speed)
    
    pressed_key = pygame.key.get_pressed() # watching out for key presses
    if pressed_key[pygame.K_DOWN] or pressed_key[pygame.K_s]:
        if paddle_y + paddle_height + 10 <= display_height:
            paddle_y += 10   #allows control of paddle while also ensuring paddle doesnt cross walls
    if pressed_key[pygame.K_UP] or pressed_key[pygame.K_w]:
        if paddle_y - 10 >= 0:
            paddle_y -= 10
           
    for event in pygame.event.get(): # looking out for events eg QUIT event
        if event.type == pygame.QUIT:
            pygame.quit()

    display.fill((0,0,0))
    x += dx # moves the ball
    y += dy
    
    pygame.draw.rect(display, (255,255,255), (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(display, (255,255,255), (x,y), radius) # draws the ball - 255,255,255 is the colour
    if x < radius:
        game_over()
        randomize_start() # tells it to randomise start locations should game be resumed
        #x = 250  # this was a hardcoded start x initially
        #y = 150  # this was a hardcoded start y initially
        dx = abs(dx) # sets x direction to positive so ball heading to back wall
    if hit_back() or hit_paddle(): #(x < radius or x > display_width - radius):
        dx *= -1 # checks for collisions with back wall or paddle, then changes direction
    if hit_sides(): #(y < radius) or (y > display_height - radius):
        dy *= -1 # checks for collisions with sides, then changes direction

    pygame.display.update() #updates the display

while True:
    stayopen = True