class Rectangle:
  shape_type = "Rectangle"

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def get_width(self, width):
    self.width = width

  def get_height(self, height):
    self.height = height

  def calculate_area(self):
    return self.width * self.height

  def calculate_perimeter(self):
    return 2 * (self.width + self.height)

  def calculate_diagonal(self):
    return (self.height**2 + self.width**2)**0.5

  def generate_picture(self):
    if self.height > 50 or self.width > 50:
      raise ValueError("Dimensions too large for picture.")
    else:
      return ("*" * self.width + "\n") * self.height

  def calculate_amount_inside(self, other_shape):
    main_area = self.calculate_area()
    inside_area = other_shape.calculate_area()
    times = int(main_area / inside_area)
    return times

  def __str__(self):
    return f"{self.shape_type}(width={self.width}, height={self.height})"


class Square(Rectangle):
  shape_type = "Square"

  def __init__(self, side_length):
    super().__init__(side_length, side_length)

  def get_side_length(self, side_length):
    super().get_height(side_length)
    super().get_width(side_length)

  def get_height(self, height):
    super().get_height(height)
    super().get_width(height)

  def get_width(self, width):
    super().get_height(width)
    super().get_width(width)

  def __str__(self):
    return f"{self.shape_type}(side={self.width})"


# Example usage
rect = Rectangle(10, 5)
print(rect.calculate_area())
rect.get_height(3)
print(rect.calculate_perimeter())
print(rect)
print(rect.generate_picture())

sq = Square(9)
print(sq.calculate_area())
sq.get_side_length(4)
print(sq.calculate_diagonal())
print(sq)
print(sq.generate_picture())

rect.get_height(8)
rect.get_width(16)
print(rect.calculate_amount_inside(sq))
