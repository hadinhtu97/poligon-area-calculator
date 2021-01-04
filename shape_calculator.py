class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        pass

    def __str__(self):
        return 'Rectangle(width='+str(self.width)+', height='+str(self.height)+')'

    def set_width(self, width):
        self.width = width
        pass

    def set_height(self, height):
        self.height = height
        pass

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*(self.width + self.height)

    def get_diagonal(self):
        return pow(pow(self.width, 2) + pow(self.height, 2), 0.5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture'
        else:
            picture = str()
            for j in range(int(self.height)):
                for i in range(int(self.width)):
                    picture += '*'
                picture += '\n'
            return picture

    def get_amount_inside(self, shape):
        return int(self.get_area()/shape.get_area())


class Square(Rectangle):

    def __init__(self, length):
        self.width = length
        self.height = length
        pass

    def __str__(self):
        return 'Square(side='+str(self.width)+')'

    def set_side(self, length):
        self.width = length
        self.height = length
        pass

    def set_width(self, length):
        self.width = length
        self.height = length
        pass

    def set_height(self, length):
        self.width = length
        self.height = length
        pass
