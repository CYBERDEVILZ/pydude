import pygame
pygame.init()

screen_width = 1000
screen_height = 400
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PYDUDE")
clock  = pygame.time.Clock()

## moving left
leftmove = [pygame.image.load('C:/Program Files/pydude/movement/small_1.png'), pygame.image.load('C:/Program Files/pydude/movement/small_2.png'), pygame.image.load('C:/Program Files/pydude/movement/small_3.png'), pygame.image.load('C:/Program Files/pydude/movement/small_4.png'), pygame.image.load('C:/Program Files/pydude/movement/small_5.png'), pygame.image.load('C:/Program Files/pydude/movement/small_6.png'), pygame.image.load('C:/Program Files/pydude/movement/small_7.png'), pygame.image.load('C:/Program Files/pydude/movement/small_8.png'), pygame.image.load('C:/Program Files/pydude/movement/small_9.png'), pygame.image.load('C:/Program Files/pydude/movement/small_10.png')]

## moving right
rightmove = [pygame.image.load('C:/Program Files/pydude/movement/small 1.png'), pygame.image.load('C:/Program Files/pydude/movement/small 2.png'), pygame.image.load('C:/Program Files/pydude/movement/small 3.png'), pygame.image.load('C:/Program Files/pydude/movement/small 4.png'), pygame.image.load('C:/Program Files/pydude/movement/small 5.png'), pygame.image.load('C:/Program Files/pydude/movement/small 6.png'), pygame.image.load('C:/Program Files/pydude/movement/small 7.png'), pygame.image.load('C:/Program Files/pydude/movement/small 8.png'), pygame.image.load('C:/Program Files/pydude/movement/small 9.png'), pygame.image.load('C:/Program Files/pydude/movement/small 10.png')]

## background image
bg = pygame.image.load('C:/Program Files/pydude/background_image/bgsprite.jpg')

## rest image***************************** to be debugged *******************
char_r = pygame.image.load('C:/Program Files/pydude/movement/rest_r.png')
char_l = pygame.image.load('C:/Program Files/pydude/movement/rest_l.png')
## jumping right
j1_r = pygame.image.load('C:/Program Files/pydude/movement/j1_r.png')
j2_r = pygame.image.load('C:/Program Files/pydude/movement/j2_r.png')
j3_r = pygame.image.load('C:/Program Files/pydude/movement/j3_r.png')
jpeak_r = pygame.image.load('C:/Program Files/pydude/movement/jpeak_r.png')
j3__r = pygame.image.load('C:/Program Files/pydude/movement/j3__r.png')
j2__r = pygame.image.load('C:/Program Files/pydude/movement/j2__r.png')

### jumping left
j1_l = pygame.image.load('C:/Program Files/pydude/movement/j1_l.png')
j2_l = pygame.image.load('C:/Program Files/pydude/movement/j2_l.png')
j3_l = pygame.image.load('C:/Program Files/pydude/movement/j3_l.png')
jpeak_l = pygame.image.load('C:/Program Files/pydude/movement/jpeak_l.png')
j3__l = pygame.image.load('C:/Program Files/pydude/movement/j3__l.png')
j2__l = pygame.image.load('C:/Program Files/pydude/movement/j2__l.png')





class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 10
        self.jc = 10
        self.isjump = 0 ## one time space bar initializer
        self.isleft = False ## char_rest detoggler  
        self.isright = False ## char_rest detoggler
        self.Walkcount = 0
        self.jumpcount = 0
        self.isjump_r = False
        self.isjump_l = False
        self.walkleft = True ## toggles only the walk left move
        self.walkright = True ## toggles only the walk right move
        self.walkr = 1 ## char face direction (initially right) 
        self.walkl = 0 ## char face direction
        self.lt = True
        self.rt = True
    def draw(self, win):
        ### if character is not moving and jumping and is facing right
        if not self.isleft and not self.isright and not self.isjump_r and self.walkr and not self.isjump:
            win.blit(char_r, (self.x, self.y))

        ### if character is not moving and jumping and is facing left
        if not self.isleft and not self.isright and not self.isjump_l and self.walkl and not self.isjump:
            win.blit(char_l, (self.x, self.y))
        

    def move(self, win):
        keys = pygame.key.get_pressed()

        ####  walking left
        if self.walkleft:
            if keys[pygame.K_LEFT]:
                self.walkl = 1
                self.walkr = 0
                self.walkright = False       ##### keys[pygame.K_LEFT] returns a value of 1
                if not self.isjump_l:
                    self.isleft = True
                    self.isright = False
                    if self.lt:
                        win.blit(leftmove[self.Walkcount//2], (self.x, self.y))
                        self.Walkcount+=1
                        if self.Walkcount>18:
                            self.Walkcount = 0
                if self.x>= 0:
                    self.x-=self.vel
                if self.x<=0:
                    self.x-=0
            else:
                self.walkright = True


        ####  walking right
        if self.walkright:
            if keys[pygame.K_RIGHT]:
                self.walkleft = False
                self.walkr = 1
                self.walkl = 0                                  ##### returns 1
                if not self.isjump_r:
                    self.isright = True
                    self.isleft = False
                    if self.rt:
                        win.blit(rightmove[self.Walkcount//2], (self.x, self.y))
                        self.Walkcount+=1
                        if self.Walkcount>18:
                            self.Walkcount = 0
                if self.x<= screen_width-50:
                    self.x+=self.vel
                if self.x>=screen_width-50:
                    self.x=screen_width-50
            else: 
                self.walkleft = True
        
        
        ####  one time space bar initialisation
        if not self.isjump_r and not self.isjump_l:
            if keys[pygame.K_SPACE] and keys[pygame.K_RIGHT]:                              #### returns 1
                self.isjump_r = True
            if keys[pygame.K_SPACE] and keys[pygame.K_LEFT]:                              #### returns 1
                self.isjump_l = True
            


        ####  jumping and moving right
        if self.isjump_r:
            self.isleft = False
            self.isright = False
            self.lt = False
            ## parabola def
            if self.jc>=-10:
                if self.jc>=0:                      ##ascending
                    self.y-= int(self.jc**2*0.4)
                    if self.y == 290.0:
                        self.isleft = True
                        self.isright = True
                        win.blit(j1_r, (self.x, self.y))
                    if self.y == 258.0:
                        self.isright = True
                        self.isleft = True
                        win.blit(j1_r, (self.x, self.y))
                    if self.y == 233.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j1_r, (self.x, self.y))
                    if self.y == 214.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j2_r, (self.x, self.y))
                    if self.y == 200.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j2_r, (self.x, self.y))
                    if self.y == 190.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j2_r, (self.x, self.y))
                    if self.y == 184.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3_r, (self.x, self.y))
                    if self.y == 181.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3_r, (self.x, self.y))
                    if self.y == 180.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(jpeak_r, (self.x, self.y))
                    else:
                        self.isleft = False
                        self.isleft = False


                else:                      #### descending
                    self.y+= int(self.jc**2*0.4)
                    if self.y == 719:
                        self.isleft = True
                        self.isright = True
                        win.blit(j2__r, (self.x, self.y))
                    if self.y == 290.0:
                        self.isleft = True
                        self.isright = True
                        win.blit(j2__r, (self.x, self.y))
                    if self.y == 258.0:
                        self.isright = True
                        self.isleft = True
                        win.blit(j3__r, (self.x, self.y))
                    if self.y == 233.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__r, (self.x, self.y))
                    if self.y == 214.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__r, (self.x, self.y))
                    if self.y == 200.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__r, (self.x, self.y))
                    if self.y == 190.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__r, (self.x, self.y))
                    if self.y == 184.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__r, (self.x, self.y))
                    if self.y == 181.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__r, (self.x, self.y))
                    if self.y == 180.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(jpeak_r, (self.x, self.y))
                    else:
                        self.isleft = False
                        self.isleft = False
                        
                    
                self.jc-=1
            
            
            else:                           ##reached the ground, resetting values
                self.jc = 10
                self.isjump_r = False
                self.lt = True


####  jumping and moving left
        if self.isjump_l:
            self.isleft = False
            self.isright = False
            self.rt = False
            ## parabola def
            if self.jc>=-10:

                if self.jc>=0:                      ##ascending
                    self.y-= int(self.jc**2*0.4)
                    if self.y == 290.0:
                        self.isleft = True
                        self.isright = True
                        win.blit(j1_l, (self.x, self.y))
                    if self.y == 258.0:
                        self.isright = True
                        self.isleft = True
                        win.blit(j1_l, (self.x, self.y))
                    if self.y == 233.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j1_l, (self.x, self.y))
                    if self.y == 214.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j2_l, (self.x, self.y))
                    if self.y == 200.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j2_l, (self.x, self.y))
                    if self.y == 190.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j2_l, (self.x, self.y))
                    if self.y == 184.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3_l, (self.x, self.y))
                    if self.y == 181.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3_l, (self.x, self.y))
                    if self.y == 180.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(jpeak_l, (self.x, self.y))
                    else:
                        self.isleft = False
                        self.isleft = False


                else:                      #### descending
                    self.y+= int(self.jc**2*0.4)
                    if self.y == 329:
                        self.isleft = True
                        self.isright = True
                        win.blit(j2__l, (self.x, self.y))
                    if self.y == 290.0:
                        self.isleft = True
                        self.isright = True
                        win.blit(j2__l, (self.x, self.y))
                    if self.y == 258.0:
                        self.isright = True
                        self.isleft = True
                        win.blit(j3__l, (self.x, self.y))
                    if self.y == 233.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__l, (self.x, self.y))
                    if self.y == 214.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__l, (self.x, self.y))
                    if self.y == 200.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__l, (self.x, self.y))
                    if self.y == 190.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__l, (self.x, self.y))
                    if self.y == 184.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__l, (self.x, self.y))
                    if self.y == 181.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__l, (self.x, self.y))
                    if self.y == 180.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(jpeak_l, (self.x, self.y))
                    else:
                        self.isleft = False
                        self.isleft = False
                    
                self.jc-=1
            
            
            else:                           ##reached the ground, resetting values
                self.jc = 10
                self.isjump_l = False
                self.rt = True


        if self.isjump == 0:
            if not self.isleft and not self.isright and not self.isjump_r and not self.isjump_l:
                if self.walkr:
                    if keys[pygame.K_SPACE]:
                        self.isjump = 1
                elif self.walkl:
                    if keys[pygame.K_SPACE]:
                        self.isjump = 2

        if self.isjump == 1:
            self.isleft = False
            self.isright = False
            self.lt = False
            self.walkleft = False
            self.walkright = False
            ## parabola def
            if self.jc>=-10:

                if self.jc>=0:                      ##ascending
                    self.y-= int(self.jc**2*0.4)
                    if self.y == 290.0:
                        self.isleft = True
                        self.isright = True
                        win.blit(j1_r, (self.x, self.y))
                    if self.y == 258.0:
                        self.isright = True
                        self.isleft = True
                        win.blit(j1_r, (self.x, self.y))
                    if self.y == 233.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j1_r, (self.x, self.y))
                    if self.y == 214.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j2_r, (self.x, self.y))
                    if self.y == 200.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j2_r, (self.x, self.y))
                    if self.y == 190.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j2_r, (self.x, self.y))
                    if self.y == 184.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3_r, (self.x, self.y))
                    if self.y == 181.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3_r, (self.x, self.y))
                    if self.y == 180.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(jpeak_r, (self.x, self.y))
                    else:
                        self.isleft = False
                        self.isleft = False


                else:                      #### descending
                    self.y+= int(self.jc**2*0.4)
                    if self.y == 719:
                        self.isleft = True
                        self.isright = True
                        win.blit(j2__r, (self.x, self.y))
                    if self.y == 290.0:
                        self.isleft = True
                        self.isright = True
                        win.blit(j2__r, (self.x, self.y))
                    if self.y == 258.0:
                        self.isright = True
                        self.isleft = True
                        win.blit(j3__r, (self.x, self.y))
                    if self.y == 233.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__r, (self.x, self.y))
                    if self.y == 214.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__r, (self.x, self.y))
                    if self.y == 200.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__r, (self.x, self.y))
                    if self.y == 190.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__r, (self.x, self.y))
                    if self.y == 184.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__r, (self.x, self.y))
                    if self.y == 181.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__r, (self.x, self.y))
                    if self.y == 180.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(jpeak_r, (self.x, self.y))
                    else:
                        self.isleft = False
                        self.isleft = False
                        
                    
                self.jc-=1
            
            
            else:                           ##reached the ground, resetting values
                self.jc = 10
                self.isjump = 0
                self.lt = True
                self.walkright = True
                self.walkleft =True

        if self.isjump == 2:
            self.isleft = False
            self.isright = False
            self.rt = False
            self.walkright = False
            self.walkleft = False
            ## parabola def
            if self.jc>=-10:

                if self.jc>=0:                      ##ascending
                    self.y-= int(self.jc**2*0.4)
                    if self.y == 290.0:
                        self.isleft = True
                        self.isright = True
                        win.blit(j1_l, (self.x, self.y))
                    if self.y == 258.0:
                        self.isright = True
                        self.isleft = True
                        win.blit(j1_r, (self.x, self.y))
                    if self.y == 233.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j1_r, (self.x, self.y))
                    if self.y == 214.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j2_l, (self.x, self.y))
                    if self.y == 200.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j2_r, (self.x, self.y))
                    if self.y == 190.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j2_r, (self.x, self.y))
                    if self.y == 184.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3_l, (self.x, self.y))
                    if self.y == 181.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3_l, (self.x, self.y))
                    if self.y == 180.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(jpeak_l, (self.x, self.y))
                    else:
                        self.isleft = False
                        self.isright = False


                else:                      #### descending
                    self.y+= int(self.jc**2*0.4)
                    if self.y == 719:
                        self.isleft = True
                        self.isright = True
                        win.blit(j2__l, (self.x, self.y))
                    if self.y == 290.0:
                        self.isleft = True
                        self.isright = True
                        win.blit(j2__l, (self.x, self.y))
                    if self.y == 258.0:
                        self.isright = True
                        self.isleft = True
                        win.blit(j3__l, (self.x, self.y))
                    if self.y == 233.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__l, (self.x, self.y))
                    if self.y == 214.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__l, (self.x, self.y))
                    if self.y == 200.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__l, (self.x, self.y))
                    if self.y == 190.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__l, (self.x, self.y))
                    if self.y == 184.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__l, (self.x, self.y))
                    if self.y == 181.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(j3__l, (self.x, self.y))
                    if self.y == 180.0:
                        self.isright = True
                        self.isleft = True                        
                        win.blit(jpeak_l, (self.x, self.y))
                    else:
                        self.isleft = False
                        self.isright = False
                        
                    
                self.jc-=1
            
            
            else:                           ##reached the ground, resetting values
                self.jc = 10
                self.isjump = 0
                self.walkleft = True
                self.walkright = True
                self.rt = True
        




        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.isleft = False
            self.isright = False

        

                

#########################  MAIN GAME LOOP  ##############################        
      
x = Player(50, 330, 50, 50, (255, 0, 0))
run = True
while run:
    clock.tick(35)
    win.blit(bg, (0,0))
    x.move(win)
    x.draw(win)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
pygame.quit()
