class Kwadrat():
    def __init__(self, bok): 
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
            
class NiebieskiKwadrat(Kwadrat):
    def sketch_niebieski(self, x, y):
        fill(0,0,255)
        Kwadrat.sketch(self, x, y)

def setup():
    size(400, 400)
    niebieski_kwadrat_mniejszy = NiebieskiKwadrat(30)
    niebieski_kwadrat_wiekszy = NiebieskiKwadrat(100)
    niebieski_kwadrat_mniejszy.sketch_niebieski(300, 300)
    niebieski_kwadrat_wiekszy.sketch_niebieski(100, 270)
