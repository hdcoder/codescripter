#Running CodeSkulptor Link !
#http://www.codeskulptor.org/#user21_neS4pCvPWHDa2zQ_0.py 

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


#SAMPLE OUTPUT :
#====================================================

#New Game, Range is from 0 to 100
#Number of Remaining Guesses is  7

#Guess was  12
#Number of Remaining Guesses is  6
#Higher!

#Guess was  50
#Number of Remaining Guesses is  5
#Lower!

#Guess was  25
#Number of Remaining Guesses is  4
#Higher!

#Guess was  35
#Number of Remaining Guesses is  3
#Lower!

#Guess was  30
#Number of Remaining Guesses is  2
#Higher!

#Guess was  32
#Number of Remaining Guesses is  1
#Correct!

#New Game, Range is from 0 to 100
#Number of Remaining Guesses is  7

#====================================================

import simplegui
import random

# initialization of global variables 
a=0
count=0
flag=0

#------------------------------------------------------
# helper function to start and restart the game
def new_game():
    global flag
    if(flag==0):
        range100()
    else:
        range1000()

#-------------------------------------------------------
# define event handlers for control panel

# button that changes range to range [0,100) and restarts
def range100():
    
    global a,count,flag
    flag=0
    a=random.randrange(100)
   
    print "\nNew Game, Range is from 0 to 100"
    count=7
    print "Number of Remaining Guesses is ",count

#-------------------------------------------------------

# button that changes range to range [0,1000) and restarts
def range1000():
    
    global a,count,flag
    flag=1
    a=random.randrange(1000)
   
    print "\nNew Game, Range is from 0 to 1000"
    count=10
    print "Number of Remaining Guesses is ",count

#--------------------------------------------------------    

# main game logic goes here	
def input_guess(guess):
    
    global a,count
    count -=1
    
    #converting the string guess into float type
    val=int(guess) 
    
    print "\nGuess was ",val
    print "Number of Remaining Guesses is ",count    
    if(count>0):
        if(val==a):
            print "Correct!"
            new_game()
        elif(val>a):
            print "Lower!"
        elif(val<a):
            print "Higher!"
    else:
        if(val==a):
            print "Correct!" 
        else:
            print"You ran out of Guesses,The Number was ",a
        new_game()
#--------------------------------------------------------
    
# create frame
frame = simplegui.create_frame('Guess the Number', 200, 200)
frame.set_canvas_background('Red')


# register event handlers for control elements
frame.add_button('Range is (0,100)', range100, 200)
frame.add_button('Range is (0,1000)', range1000,200)
frame.add_input('Enter a a Guess ', input_guess, 200)


# call new_game and start frame
new_game()
frame.start()


#EAT-CODE-SLEEP ! 
#HAPPY CODING !
