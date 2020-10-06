import pyglet
import FadeText
from pyglet.window import key

class ClassScreen:


    def __init__(self, textlabel, alphacolor): 
        self.textlabel = textlabel
        self.alphacolor = alphacolor
        fader = FadeText.FadeText(textlabel, alphacolor)
        fader.fadeText(textlabel)


    
    @staticmethod
    def SelectClass(label):
        #FadeText.fadeText(self, label)
        label.text = "Hello Adventurer! "
 

