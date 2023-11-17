class MusicTracker():
    def __init__(self):
        self.musiclistened = []
    def add(self,music):
        self.musiclistened.append(music)
    def musiclist(self):
        #returns a list of music listened to
        return self.musiclistened