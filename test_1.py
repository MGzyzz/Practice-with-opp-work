class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        perimetr = self.length + self.width
        return perimetr

    def area_rectangle(self):
        area = self.length * self.width
        return area

    def data_view(self):
        return print(f"Длина прямоугольника: {self.length}\n"
                     f"Ширина прямоугольника: {self.width}\n"
                     f"Периметр прямоугольного: {self.perimeter()}\n"
                     f"Площадь прямоугольника: {self.area_rectangle()}")


number_one = input("Напишите длину\n")
number_two = input("Напишите ширину\n")

rectangle = Rectangle(int(number_one), int(number_two))

rectangle.data_view()