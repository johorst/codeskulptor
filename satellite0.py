# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui
import math

time = 0
drift = 0
speed = 0

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_image(double_ship, (45, 45), (90, 90), get_coordinates(), (35, 35), -time%(math.pi*2) + drift)
    canvas.draw_circle((150, 100), 15, 30, 'Blue')
    canvas.draw_circle(get_coordinates(), 2, 4, 'Green')

def tick():
    global time
    time = time + 0.1    
    
def get_coordinates():
    global time
    global speed
    xcoord = 50 * (math.sin(time)) + 150
    ycoord = 50 * (math.cos(time)) + 100
    xcoord += speed * math.cos(-time%(math.pi*2) + drift)
    ycoord += speed * math.sin(-time%(math.pi*2) + drift)
    #speed += 0.2
    return (xcoord%300, ycoord%200)

def key_handler(key):
    global drift
    global speed
    if key == simplegui.KEY_MAP['space']:
        speed += 1
        print(speed)
    #if key == simplegui.KEY_MAP['up']:
    if key == simplegui.KEY_MAP['down']:
        speed -= 1
    if key == simplegui.KEY_MAP['left']:
        drift -= 0.1
    if key == simplegui.KEY_MAP['right']:
        drift += 0.1
    
# Create a frame and assign callbacks to event handlers
double_ship = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png')
frame = simplegui.create_frame("Home", 300, 200)
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_handler)
timer = simplegui.create_timer(80, tick)
timer.start()

# Start the frame animation
frame.start()