import pyglet
from pyglet.window import key
from ClassScreen import ClassScreen

window = pyglet.window.Window()
label = pyglet.text.Label("Welcome, adventurer. Let us begin your journey. Press any key to continue.", font_name = 'Times New Roman', font_size = 20, x = 75, y = 300)
 
 
@window.event
def on_draw():
    window.clear()
    label.draw()

@window.event
def on_key_press(symbol, modifiers):
   ClassScreen().printthing()

pyglet.app.run()



