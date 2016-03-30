import sfml as sf
import time
import random
from player import *
from button import Button
global_speed = 2


def init_rectangle(size, position, color):
    rectangle = sf.RectangleShape()
    rectangle.size = size
    rectangle.position = position
    rectangle.fill_color = color
    return rectangle


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
window = sf.RenderWindow(sf.VideoMode(800, 600), "pySFML Window")

# play the music
# music.play()
font = sf.Font.from_file("abc.ttf")
p1 = Player(init_rectangle((100,50),(10,20),sf.Color.RED), 0, 'Hans')
button1 = Button(init_rectangle((200,100),(300,20),sf.Color.GREEN),'function not implemented yet','Test 1')
button2 = Button(init_rectangle((200,100),(300,220),sf.Color.GREEN),'function not implemented yet','Test 2')
button3 = Button(init_rectangle((200,100),(300,420),sf.Color.GREEN),'function not implemented yet','Test 3')
text = sf.Text("0")
text.font = font
text.character_size = 20
text.style = sf.Text.BOLD
text.color = sf.Color.RED
start = time.time()  # dunno with windows
timer = 0
circle = new_point()
pause = False

while window.is_open and not pause:  # menu
    for event in window.events:
        if type(event) is sf.KeyEvent:
           pause = True
        if type(event) is sf.CloseEvent:
            window.close()

    window.clear()
    window.draw(button1.rect)
    window.draw(button2.rect)
    window.draw(button3.rect)
    window.display()


# start the game loop
while window.is_open:
    # process events
    for event in window.events:
        # close window: exit
        # if type(event) is sf.CloseEvent:
        #   window.close()
        if type(event) is sf.KeyEvent:
            p1.rect.position = handle_key_event(p1.rect)
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
