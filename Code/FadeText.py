import ClassScreen
import time
import pyglet

class fadeTextClass:

    def __init__(self, label):
        self.label = label
        self.alphacolor = 255
    

    def fadeText(self, fadingin, labeltext):
        fadetime = 0.073
        if not fadingin:
            pyglet.clock.schedule_interval(self.fadeOut, fadetime)
        else:
    
            pyglet.clock.schedule_interval(self.fadeIn, fadetime)
            self.label.color = (255, 255, 255, 0)



    def fadeOut(self, interval):
       if(self.alphacolor <= 0):
            pyglet.clock.unschedule(self.fadeOut)
            return

       self.alphacolor -= 50
       textholder = self.label.text
       self.label.text = ""
       self.label.text = textholder
       self.label.color = (255,255,255,self.alphacolor)


    def fadeIn(self, interval):
        
        if self.alphacolor >= 255:
            pyglet.clock.unschedule(self.fadeIn)
            return
        self.alphacolor += 5
        textholder = self.label.text
        self.label.text = textholder
        self.label.color = (255,255,255, self.alphacolor)

       
 
   
         



    

    

 