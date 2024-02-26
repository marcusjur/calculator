import logging


class ComplexCalculator:
    """
    Класс для работы с комплексными числами
    """
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def add(self, a, b):
        """
        Метод сложения двух комплексных чисел

        :param a:
        :param b:
        :return:
        """
        self.logger.info("Adding two complex numbers: %s, %s", a, b)
        return a + b

    def multiply(self, a, b):
        self.logger.info("Multiplying two complex numbers: %s, %s", a, b)
        return a * b

    def divide(self, a, b):
        if b.real == 0 and b.imag == 0:
            self.logger.error("Attempt to divide by zero")
            raise ValueError("Cannot divide by zero")
        self.logger.info("Dividing two complex numbers: %s, %s", a, b)
        return a / b

    def subtract(self, a, b):
        self.logger.info("Subtracting two complex numbers: %s, %s", a, b)
        return a - b
