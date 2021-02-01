class Television:
    def __init__(self, ligada, channel):
        self.ligada = ligada 
        self.channel = channel

    def changes_chanel_down(self):
        self.channel -= 1
        return self.channel

    
tv = Television(True,3)
tv.channel
tv.changes_chanel_down()
tv.channel