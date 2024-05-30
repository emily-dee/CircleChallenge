from math import pi


class Circle:
    def __init__(self, radius: float):
        self.radius = radius
        self.circle_diameter = 0.0
        self.circle_circumference = 0.0
        self.circle_area = 0.0

    def calculate_diameter(self):
        self.circle_diameter = 2 * self.radius
        # print(f'Diameter: {self.circle_diameter}')
        return self.circle_diameter

    def calculate_circumference(self):
        self.circle_circumference = round((2 * pi * self.radius), 2)
        # print(f'Circumference: {self.circle_circumference}')
        return self.circle_circumference

    def calculate_area(self):
        self.circle_area = round((pi * (self.radius ** 2)), 2)
        return self.circle_area

    def grow(self):
        self.radius *= 2

    def get_radius(self):
        return self.radius


print('Welcome to the Circle Calculator')
while True:
    try:
        user_radius = round(float(input('Enter a radius >> ')), 2)
        if user_radius <= 0:
            print('Please use a positive number greater than zero')
        else:
            break
    except ValueError:
        print('Please use a valid number')

circle1 = Circle(user_radius)
print(f'Diameter: {circle1.calculate_diameter()}')
print(f'Circumference: {circle1.calculate_circumference()}')
print(f'Area: {circle1.calculate_area()}')

while True:
    grow_circle = input('Would you like to grow your circle? y or n >> ')
    if grow_circle == 'y':
        print('Calculating...')
        circle1.grow()
        print(f'Diameter: {circle1.calculate_diameter()}')
        print(f'Circumference: {circle1.calculate_circumference()}')
        print(f'Area: {circle1.calculate_area()}')
    else:
        print(f'Goodbye, circle radius is: {circle1.get_radius()}.')
        break
