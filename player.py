import sfml as sf


class Player:
    def __init__(self, my_rect, points, name):
        self.rect = my_rect
        self.points = points
        self.name = name

    def hello(self):
        print "I am ", self.name, " with ", self.points, " points "
