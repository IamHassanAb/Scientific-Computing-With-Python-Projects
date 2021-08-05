class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f'''Rectangle(width={self.width}, height={self.height})'''

    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:

            return "Too big for picture."

        picture = ""
        star = ""
        for lines in range(self.height):
            star = ""
            for stars in range(self.width):
                star += "*"
            picture += star + "\n"


        return (picture)

    def get_amount_inside(self, shape):
        if self.width < shape.width or self.height < shape.height:

            return False

        width_multiple = int(self.width / shape.width)
        height_mutliple = int(self.height / shape.height)

        return width_multiple * height_mutliple


class Square(Rectangle):
    def __init__(self, side):
        super(Square, self).__init__(width=side, height=side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def __repr__(self):
        return f'''Square(side={self.width})'''

