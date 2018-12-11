"""The module reverses the message from end to start word by word and also letter by letter. It is also a method of 
simple encryption."""

class MirrorSquared:
    def __init__(self,text):
        self.text = text
    def text_revsquared(self):
        words = self.text
        text_rev1 = " ".join(reversed(words)) # " Sorry this is a private message if you do not have a key STOP reading!"
        #print("The encrypted message is:",text_rev1)
        return text_rev1