import pyglet
import FadeText
from pyglet.window import key

class ClassScreen:


    def __init__(self, textlabel, alphacolor): 

        self.textlabel = textlabel
        self.alphacolor = alphacolor

        self.fader = FadeText.fadeTextClass(textlabel)
        self.fader.fadeText(False, textlabel.text)


    def SelectClass(self):
        self.textlabel.color = (255,255,255,0)
        self.textlabel.text = "Select a class"
        self.fader.fadeText(True, self.textlabel.text)
       


    
   

