class Rectangle:
    # Constructor method to initialize width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Setter methods for width and height
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    # Method to calculate the area
    def get_area(self):
        return self.width * self.height

    # Method to calculate the perimeter
    def get_perimeter(self):
        return 2 * (self.width + self.height)

    # Method to calculate the diagonal
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    # Method to create a picture of the rectangle with asterisks
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    # Method to calculate how many smaller shapes fit inside this rectangle
    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

    # String representation of the rectangle
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    # Constructor method for Square, using inheritance from Rectangle
    def __init__(self, side):
        super().__init__(side, side)

    # Method to set the side length (also updates width and height)
    def set_side(self, side):
        self.width = side
        self.height = side

    # Overriding set_width and set_height to maintain square properties
    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    # String representation of the square
    def __str__(self):
        return f"Square(side={self.width})"
