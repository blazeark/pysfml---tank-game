import sfml as sf
import time
import random
from player import *

global_speed = 2


def new_point():
    x = random.randint(0, 640)  #
    y = random.randint(0, 480)
    circle = sf.CircleShape()
    circle.radius = 20
    circle.outline_color = sf.Color.GREEN
    circle.position = (x, y)
    return circle


def handle_key_event(rectangle):
    if sf.Keyboard.is_key_pressed(sf.Keyboard.LEFT):
        return (rectangle.position.x - global_speed, rectangle.position.y)
    if sf.Keyboard.is_key_pressed(sf.Keyboard.RIGHT):
        return (rectangle.position.x + global_speed, rectangle.position.y)
    if sf.Keyboard.is_key_pressed(sf.Keyboard.DOWN):
        return (rectangle.position.x, rectangle.position.y + global_speed)
    if sf.Keyboard.is_key_pressed(sf.Keyboard.UP):
        return (rectangle.position.x, rectangle.position.y - global_speed)

    return (rectangle.position.x, rectangle.position.y)


# create the main window
window = sf.RenderWindow(sf.VideoMode(640, 480), "pySFML Window")

# play the music
# music.play()
font = sf.Font.from_file("abc.ttf")
rectangle = sf.RectangleShape()
rectangle.size = (100, 50)
rectangle.outline_color = sf.Color.RED
rectangle.outline_thickness = 5
rectangle.position = (10, 20)
p1 = Player(rectangle, 0, 'Hans')
text = sf.Text("0")
text.font = font
text.character_size = 20
text.style = sf.Text.BOLD
text.color = sf.Color.RED
start = time.time()  # dunno with windows
timer = 0
circle = new_point()

#while window.is_open:  # menu
    #window.draw(button1)
    #window.draw(button2)
    #window.draw(button3)

# start the game loop
while window.is_open:
    # process events
    for event in window.events:
        # close window: exit
        # if type(event) is sf.CloseEvent:
        #   window.close()
        if type(event) is sf.KeyEvent:
            p1.rect.position = handle_key_event(rectangle)
        if type(event) is sf.CloseEvent:
            window.close()
    if time.time() - start > 1:
        start = time.time()
        timer = timer + 1
        text = sf.Text((str(timer)), font, 20)
    # text.color = sf.Color.RED

    window.clear()  # clear screen
    window.draw(text)
    window.draw(p1.rect)
    window.draw(circle)
    # window.draw(sprite) # draw the sprite
    # window.draw(text) # draw the string
    window.display()  # update the window
