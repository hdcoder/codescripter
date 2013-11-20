#Running CodeSkulptor Link !
#http://www.codeskulptor.org/#user23_ePlWtu2yPB_14.py


# Implementation of classic arcade game Pong


#for left bar use 
#	w-up
#    s-down

#for right bar use
#	up arraow key-up
#    down arow key-down
    
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 10
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

paddle1_point_0=[2,0]					#Initial point 1 for paddle 1
paddle1_point_1=[2,PAD_HEIGHT]			#Initial point 2 for paddle 1

paddle2_point_0=[WIDTH-2,0]				#Initial point 1 for paddle 2
paddle2_point_1=[WIDTH-2,PAD_HEIGHT]	#Initial point 2 for paddle 2


paddle1_vel=[0,0]	#initial velocity for paddle1 
paddle2_vel=[0,0]	#initial velocity for paddle2 

score1=0
score2=0

inc=1.1		#velocity increment

speed=3		#speed of paddle

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH / 2, HEIGHT / 2]
x = -(random.randrange(120, 240)/60)
y = -(random.randrange(60, 180)/60)
ball_vel = [x, y]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    x = random.randrange(120, 240)/60
    y = -(random.randrange(60, 180)/60)
    
    if(direction=="RIGHT"):
        ball_vel = [x, y]
    else:
        ball_vel = [-x, y]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2,ball_pos,paddle1_point_0,paddle1_point_1
    global paddle2_point_0,paddle2_point_1 # these are ints
    score1=0
    score2=0
    spawn_ball("LEFT")
    paddle1_point_0=[2,0]					#Initial point 1 for paddle 1
    paddle1_point_1=[2,PAD_HEIGHT]			#Initial point 2 for paddle 1
    
    paddle2_point_0=[WIDTH-2,0]				#Initial point 1 for paddle 2
    paddle2_point_1=[WIDTH-2,PAD_HEIGHT]	#Initial point 2 for paddle 2


    paddle1_vel=[0,0]	#initial velocity for paddle1 
    paddle2_vel=[0,0]	#initial velocity for paddle2 
    
   

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
#-------------------------------------------------------------         
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
#-------------------------------------------------------------         
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
#-------------------------------------------------------------    
    #update paddles

    #update paddle 1
    paddle1_point_0[1] +=paddle1_vel[1]
    paddle1_point_1[1] +=paddle1_vel[1]
   
    #update paddle 2
    paddle2_point_0[1] +=paddle2_vel[1]
    paddle2_point_1[1] +=paddle2_vel[1]
    
#-------------------------------------------------------------     
    #bouncing the balls of padde1
    
    #left most point
    if(ball_pos[0] <= BALL_RADIUS+PAD_WIDTH ):
        if (ball_pos[1] >= paddle1_point_0[1] and ball_pos[1] <= paddle1_point_1[1]):   
            ball_vel[0] = - ball_vel[0]*inc
        else:
            spawn_ball("RIGHT")
            score2 +=1
    
    #right most point
    if(ball_pos[0]+BALL_RADIUS >=  WIDTH-PAD_WIDTH ):
        if (ball_pos[1] >= paddle2_point_0[1] and ball_pos[1] <= paddle2_point_1[1]):   
            ball_vel[0] = - ball_vel[0]*inc
        else:
            spawn_ball("LEFT")
            score1 +=1
    
    
#-------------------------------------------------------------     
 
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

#-------------------------------------------------------------     
   
    #bouncing off the ball on vertical walls
    if ( ball_pos[1] <= BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    elif( ball_pos[1] + BALL_RADIUS >= HEIGHT ):
        ball_vel[1] = -ball_vel[1]
            
            
#-------------------------------------------------------------        
    #checking extreme conditions for paddle  
    
    #paddle 1
    #for top most coordinate
    if paddle1_point_0[1] <= 0:		#y coordinate of paddle1 postion of first point
        paddle1_point_0[1] =0
        paddle1_point_1[1] =PAD_HEIGHT

  
    #for bottom most coordinate
    if paddle1_point_1[1] >= HEIGHT  :		#extreme width of the frame
        paddle1_point_0[1] =HEIGHT-PAD_HEIGHT
        paddle1_point_1[1] =HEIGHT
        
    #paddle 2
    
    #for top most coordinate
    if paddle2_point_0[1] <= 0 :		#y coordinate of paddle1 postion of first point
        paddle2_point_0[1] =0
        paddle2_point_1[1] =PAD_HEIGHT

  
    #for bottom most coordinate
    if paddle2_point_1[1] >= HEIGHT :		#extreme width of the frame
        paddle2_point_0[1] =HEIGHT-PAD_HEIGHT
        paddle2_point_1[1] =HEIGHT   
        
#-------------------------------------------------------------    
    
    # draw paddles
    
    #paddle 1
    c.draw_line(paddle1_point_0,paddle1_point_1, PAD_WIDTH, 'Yellow')
    
    #paddle 2
    c.draw_line(paddle2_point_0,paddle2_point_1, PAD_WIDTH, 'Red')
    
#-------------------------------------------------------------     
    
    # draw scores
    c.draw_text(str(score1), (200, 50), 30, 'Blue', 'serif')
    c.draw_text(str(score2), (400, 50), 30, 'Blue', 'serif')

#-------------------------------------------------------------         

def keydown(key):
    global paddle1_vel, paddle2_vel
    
    #velocity for paddles
    
    #for paddle 1
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1] =speed		
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] =-speed

    #for paddle 2
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] =speed
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] =-speed
   
#------------------------------------------------------------- 
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    #for paddle 1
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1] =0
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] =0
    
    #for paddle 2
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] =0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] =0

#------------------------------------------------------------- 

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button2 = frame.add_button('RESET', new_game, 100)


# start frame
new_game()
frame.start()
