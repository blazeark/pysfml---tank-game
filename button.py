import sfml as sf


class Button:
    def __init__(self, my_rect, function, name):
        self.rect = my_rect
        self.function = function
        self.name = name