class BookReader:
    country = 'South Korea'
    def __init__(self,name):
        self.name = name
    def read_book(self):
        print(self.name + 'is reading Book!')

class DrumPlayer:
    country = 'South Korea'
    def __init__(self, name):
        self.name = name

    def play_drum(self):
        print(self.name + 'is playing Drum!')

