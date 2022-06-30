# Create a class called Circle. Upon initialization, it should receive a radius (number). Create a class attribute
# called pi which should be equal to 3.14. Create 3 instance methods:
# -	set_radius(new_radius) - changes the radius
# -	get_area() - returns the area of the circle
# -	get_circumference() - returns the circumference of the circle

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        area = self.pi * self.radius ** 2
        return area

    def get_circumference(self):
        circumference = 2 * self.radius * self.pi
        return circumference


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())

