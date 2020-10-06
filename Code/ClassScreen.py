import pyglet
import FadeText
from pyglet.window import key

class ClassScreen:


    def __init__(self, textlabel, alphacolor): 

        self.textlabel = textlabel
        self.alphacolor = alphacolor
        fader = FadeText.fadeText(textlabel)
        fader.fadeText()


    
   

