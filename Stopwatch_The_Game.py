#Running CodeSkulptor Link !
#http://www.codeskulptor.org/#user22_PrnCerTeLnVxkqT_0.py

# INCLUDE <EAT-CODE-SLEEP !!>
# INCLUDE <HAPPY CODING !!>

# template for "Stopwatch: The Game"
import simplegui
import math

# define global variables
t = 0
tenths = 0
seconds = 0
mins = 0

success = 0
attempts = 0

playing = 1

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def formatTime():
    global t, tenths, seconds, mins

    tenths = int(t % 10)
    seconds = int(math.floor((t / 10)%60))
    mins = int(math.floor(t / 600))
    
    if seconds < 10:
        seconds = "0" + str(seconds)
    return str(mins) + ":" + str(seconds) + "." + str(tenths)

# define event handlers
def changeTime(): # function to add tenth of a second
    global t
    t += 1     

def start():
    # reset t to zero and start the game
    global playing
    timer.start()
    playing = 1
    
def stop():
    # stop the timer from moving
    global t, success, attempts, playing
    timer.stop()
    if playing == 1:
        if str(t)[-1] == "0":
            success += 1
        attempts += 1
    playing = 0
    
def reset():
    global t, tenths, seconds, mins, success, attempts
    t = 0
    tenths = 0
    seconds = 0
    minutes = 0
    success = 0
    attempts = 0
    
def theScore():
    global success, stops
    return str(success) + "/" + str(attempts)

# define draw handler
def draw_handler(canvas):
    str="STOPWATCH"
    str1="THE GAME"
    canvas.draw_text(str,(75,30), 25, "White")
    canvas.draw_text(str1,(85,50), 25, "White")
    canvas.draw_text(theScore(), [250, 40], 30, "Yellow")
    canvas.draw_text(formatTime(), [100, 120], 40, "Red")

# create frame
frame = simplegui.create_frame("Stopwatch Game!", 300, 200)

# register event handlers	
timer = simplegui.create_timer(100, changeTime)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()

# INCLUDE </EAT-CODE-SLEEP >
# INCLUDE </HAPPY CODING >
