class Rectangle:

    def __init__(self, initial_width, initial_height):
        self.width = initial_width
        self.height = initial_height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2* self.width) + (2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2) + (self.height ** 2)) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""
        for count in range(self.height):
            picture += ("*" * self.width) + "\n"
        return picture

    def get_amount_inside(self, other_shape):
        area_self = int(self.get_area())
        area_other = int(other_shape.get_area())

        return area_self // area_other


class Square(Rectangle):

    def __init__(self, initial_side):
        self.width = initial_side
        self.height = initial_side
        self.side = initial_side

    def __str__(self):
        return f"Square(side={self.side})"

    def set_side(self, new_side):
        self.side = new_side
        self.width = new_side
        self.height = new_side

    def set_width(self, new_width):
        self.set_side(new_width)

    def set_height(self, new_height):
        self.set_side(new_height)
