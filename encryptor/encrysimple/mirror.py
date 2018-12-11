"""The module reverses the message from end to start word by word. It is a method of simple encryption. """

class Mirror:
    def __init__(self,text):
        try: 
            self.text = text

            if len(str(text)) <1:
                
                raise ValueError
        except ValueError:
            print("This is empty")
        else:
            pass
        finally:
            print('first')
          
    def text_revmirror(self):
        try:
            words = self.text.split()
            text_rev1 = " ".join(reversed(words))
            return text_rev1
        except AttributeError:
            print("attribute error")
        else:
            pass
        finally:
            print('Finish')