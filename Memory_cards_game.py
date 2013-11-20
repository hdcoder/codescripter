#Running CodeSkulptor Link !
#http://www.codeskulptor.org/#user24_W8EViZ5zdLI0lji.py

# implementation of card game - Memory
# using images and dictiorary
import simplegui
import random

#global variables and constants
FRAME_WIDTH = 800
FRAME_HEIGTH = 100
NUM_CARDS = 16
CARD_WIDTH = FRAME_WIDTH / NUM_CARDS
cards=[]
state = 0
reverse = [] #list of reversed cards not paired
turns = 0    #the number of tries
number1 = -1 #the number of the first card reversed

#dictionary numbers to text i will put number and text number
cardtext={0:' zero ',1:' one ',2:' two ',3:'three',4:' four ', 5:' five ', 6:' six ', 7:'seven',8:'eight', 9:'nine '}
#image for the back of card
card_back = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png')


# helper function to initialize globals
def new_game():
    global state, turns, cards, number1
    state = 0
    turns = 0
    cards = []
    number1 = -1
    #creating  cards ordered
    for i in range(NUM_CARDS):
        cards.append([i/2,False,False])  #number, reversed, founded
    #randomize cards
    random.shuffle(cards)  

#helper function to draw a card of index i reversed
def draw_numbercard(i, number,canvas):
    p1 = ( (CARD_WIDTH * i  + 1), 1)
    p2 = ( CARD_WIDTH * (i +1), 1 )
    p3 = ( CARD_WIDTH * (i + 1) , FRAME_HEIGTH - 1 )
    p4 = ((CARD_WIDTH * i  + 1) , FRAME_HEIGTH - 1 )
    canvas.draw_polygon([p1,p2,p3,p4],1, "White", "Black")
    canvas.draw_text(str(number), [p1[0]+(p2[0]-p1[0])/3, FRAME_HEIGTH/2], 40, 'White')
    #print number in text moden from the dictironary
    canvas.draw_text(cardtext[number], [p1[0]+(p2[0]-p1[0])/(len(cardtext[number])+3), FRAME_HEIGTH-20], 12, 'White','monospace')

#helper function to draw a card of index i not reversed
def draw_reversedcard(i, number,canvas):
    p1 = ( (CARD_WIDTH * i  + 1), 1)
    p2 = ( CARD_WIDTH * (i +1), 1 )
    p3 = ( CARD_WIDTH * (i + 1) , FRAME_HEIGTH - 1 )
    p4 = ((CARD_WIDTH * i  + 1) , FRAME_HEIGTH - 1 )
    #test if there are an error loading the image
    if card_back.get_width()/2 <1:
        canvas.draw_polygon([p1,p2,p3,p4],1, "Black", "Green")
    else: #image loaded
    #will try and image in the back
        canvas.draw_image(card_back,
                        ( card_back.get_width()/2,card_back.get_height()/2 ) , (card_back.get_width(),card_back.get_height() ),
                        (p1[0] + (p2[0]-p1[0])/2, (p3[1]-p2[1])/2), 
                        ( p2[0]-p1[0],p3[1]-p2[1] ))

     
# define event handlers
def mouseclick(pos):
    global state, reverse, turns, number1
    if cards[ pos[0] / CARD_WIDTH ][1] == False:
        if state == 0:
            # reverse the card
            cards[ pos[0] / CARD_WIDTH ][1] = True
            reverse.append (pos[0] / CARD_WIDTH)
            #change state
            state = 1
            number1 = cards[ pos[0] / CARD_WIDTH ][0]

        elif state == 1:
            # reverse the card
            cards[ pos[0] / CARD_WIDTH ][1] = True
            reverse.append (pos[0] / CARD_WIDTH)
            turns+=1
            #change state
            state = 2
            if cards[ pos[0] / CARD_WIDTH ][0] == number1:  #found a pair
                #mark founded pairs
                for i in reverse:
                    cards[i][2] = True
                reverse = []
                state = 0
                number=-1
        else:
            state = 1
            for i in reverse:
                if cards[i][2] == False:
                    cards[i][1] = False
            reverse = []
            cards[ pos[0] / CARD_WIDTH ][1] = True
            number1 = cards[ pos[0] / CARD_WIDTH ][0]
            reverse.append (pos[0] / CARD_WIDTH)
   
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    #draw cards
    for i in range(NUM_CARDS):
        if cards[i][1]:
            draw_numbercard(i,cards[i][0],canvas)  #not reversed card
        else:
            draw_reversedcard(i,cards[i][0],canvas)  #reversed card
    #update tries
    label.set_text('Turns = ' + str(turns))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", FRAME_WIDTH, FRAME_HEIGTH)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
