import pyglet
import FadeText
from pyglet.window import key

class ClassScreen:
    thisscreen = None

    def __init__(self, textlabel, alphacolor): 

        self.textlabel = textlabel
        self.alphacolor = alphacolor
        print(self.textlabel.text)
        self.fader = FadeText.fadeTextClass(textlabel)
        self.fader.fadeText(False, textlabel)
        global thisscreen
        thisscreen = self


    def SelectClass(self):
        global thisscreen
        thisscreen.fader.fadeText(True, thisscreen.textlabel)
       


    
   

