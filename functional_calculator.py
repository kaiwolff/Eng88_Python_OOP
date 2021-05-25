from oop_calculator import SimpleCalculator

class FunctionalCalculator(SimpleCalculator):
    #add mroe functionality compared to the simple calculator
    def __init__(self):
        super().__init__()

    def inchtocm(self, value1):
        return value1 * 2.54

    def triangle_area(self, height, width):
        return height*width/2

    def divisible(self, value1, value2):
        if value2 == 0:
            return False
        elif value1 % value2 == 0:
            return True
        else:
            return False


my_calc = FunctionalCalculator()
print(my_calc.add(2,2))
print(my_calc.divisible(2,3))
print(my_calc.divisible(4,2))