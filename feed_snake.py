''' This is a Simple Python Game written using Python 2.7 and uses pygame module.
pygame module should be installed before being imported - use pip install pygame'''

import sys
import random
import time

import pygame

#This will result in a output (6,0) indicating 6 successful task & 0 errors
check_errors = pygame.init()

if(check_errors[1]>0):
    print "pyGame expereinced {0} errors..Exiting".format(check_errors[1])
    sys.exit(-1) #exit code is not mandatory, can leave it blank
else:
    print "Successfully initialzed pyGame!!"

#Play surface creation
#display function creates a play screen
playSurface = pygame.display.set_mode((720,460))
pygame.display.set_caption('Snake Game!')

#Adding colors
#Every pixel will have 3 or 4 colors (R/G/B/A)
#color(r,g,b) each will range from 0 to 255.

red_c = pygame.Color(255,0,0)
green_c = pygame.Color(0,255,0)
blue_c = pygame.Color(0,0,255)
black_c = pygame.Color(0,0,0) # Black is absence of color
white_c = pygame.Color(255,255,255)
brown_c = pygame.Color(165,42,42)


#Frame Controller - FPS Controller (Frames Per Second)

fps_controller = pygame.time.Clock()

#Important Variables

snakePosition = [100,50] #Make sure it lies between PlaySurface
snakeBody = [[100,50],[90,50],[80,50]] #Initial SnakeBody length:3 blocks

foodPosition = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True #To check if we have initialized new food each time

direction = 'RIGHT'
change_to = direction

score = 0 

#Game Over Function
def gameOver():
    myFont = pygame.font.SysFont('Arial',70)
    #4th argument(optional) which is used for background
    GO_surface = myFont.render('Game Over!',True,red_c) 
    GO_rectangle = GO_surface.get_rect()
    GO_rectangle.midtop = (360,15)
    playSurface.blit(GO_surface, GO_rectangle)
    showScore(0)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

def showScore(choice=1):
    myFont = pygame.font.SysFont('Arial',22)
    GO_surface = myFont.render('Score: {0}'.format(score),True,black_c)
    GO_rectangle = GO_surface.get_rect()
    if(choice == 1):
        GO_rectangle.midtop = (50,10)
    else:
        GO_rectangle.midtop = (360,120)
    playSurface.blit(GO_surface, GO_rectangle)

    
#Game's Main Logic
while(True):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
        elif(event.type == pygame.KEYDOWN):
            #ord converts letters to its ASCII value
            if(event.key == pygame.K_RIGHT or event.key == ord('d')): 
                change_to = 'RIGHT'
            if(event.key == pygame.K_LEFT or event.key == ord('a')):
                change_to = 'LEFT'
            if(event.key == pygame.K_UP or event.key == ord('w')):
                change_to = 'UP'
            if(event.key == pygame.K_DOWN or event.key == ord('s')):
                change_to = 'DOWN'
            if(event.key == pygame.K_ESCAPE):
                #Now we create an event
                pygame.event.post(pygame.event.Event(pygame.QUIT)) 
                
    #Validation of Directions
    '''Here we check if we are going in right, 
       we can't shift our direction to LEFT in the next step'''
    if(change_to == 'RIGHT' and not direction == 'LEFT'):
        direction = 'RIGHT'
    if(change_to == 'LEFT' and not direction == 'RIGHT'):
        direction = 'LEFT'
    if(change_to == 'DOWN' and not direction == 'UP'):
        direction = 'DOWN'
    if(change_to == 'UP' and not direction == 'DOWN'):
        direction = 'UP'
    
    #Updating snake position [x,y]
    if(direction == 'RIGHT'):
        snakePosition[0] += 10
    if(direction == 'LEFT'):
        snakePosition[0] -= 10
    if(direction == 'UP'):
        snakePosition[1] -= 10
    if(direction == 'DOWN'):
        snakePosition[1] += 10
    
    #Updating Snake Body
    snakeBody.insert(0,list(snakePosition))
    
    if(snakePosition[0] == foodPosition[0] and snakePosition[1] == foodPosition[1]):
        score +=1
        foodSpawn = False
    else:
        snakeBody.pop() 
        
    #If food is consumed, create new food
    if(foodSpawn == False):
        foodPosition = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawn = True
    
    playSurface.fill(white_c)
    
    for pos in snakeBody:
        pygame.draw.rect(playSurface,green_c, pygame.Rect(pos[0],pos[1],10,10))
                                                                                        
    pygame.draw.rect(playSurface,brown_c,pygame.Rect(foodPosition[0],foodPosition[1],10,10))
    
    if(snakePosition[0] > 710 or snakePosition[0] < 0):
        gameOver()
    if(snakePosition[1] > 450 or snakePosition[1] < 0):
        gameOver()
    
    for block in snakeBody[1:]:
        if(snakePosition[0] == block[0] and snakePosition[1] == block[1]):
            gameOver()
    
    #Common Stuffs required for the Game
    showScore()
    pygame.display.flip() #flip or update for updating the playsurface
    fps_controller.tick(10)
   
