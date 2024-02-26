from services import ComplexCalculator, setup_logging
import tkinter as tk
from tkinter import ttk, messagebox


class CalculatorGUI:
    """
    Класс для создания пользовательского интерфейса калькулятора
    """
    def __init__(self, master):
        """
        Конструктор

        :param master: Основное окно
        """
        self.master = master
        master.title("Калькулятор")

        # Установка темы
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Калькулятор
        self.calculator = ComplexCalculator()

        # Создание виджетов
        self.create_widgets()

    def create_widgets(self):
        """
        Создание виджетов

        :return: None
        """
        mainframe = ttk.Frame(self.master, padding="10 10 10 10")
        mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.real_part1 = ttk.Entry(mainframe, width=10)
        self.real_part1.grid(row=0, column=1, padx=5, pady=5)
        self.imag_part1 = ttk.Entry(mainframe, width=10)
        self.imag_part1.grid(row=0, column=3, padx=5, pady=5)

        self.real_part2 = ttk.Entry(mainframe, width=10)
        self.real_part2.grid(row=1, column=1, padx=5, pady=5)
        self.imag_part2 = ttk.Entry(mainframe, width=10)
        self.imag_part2.grid(row=1, column=3, padx=5, pady=5)

        # Метки для пользовательского интерфейса
        ttk.Label(mainframe, text="Реальная часть 1:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(mainframe, text="Мнимая часть 1:").grid(row=0, column=2, padx=5, pady=5)
        ttk.Label(mainframe, text="Реальная часть 2:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(mainframe, text="Мнимая часть 2:").grid(row=1, column=2, padx=5, pady=5)

        # Кнопки
        self.add_button = ttk.Button(mainframe, text="+", command=self.add)
        self.add_button.grid(row=2, column=0, padx=5, pady=5)
        self.subtract_button = ttk.Button(mainframe, text="-", command=self.subtract)
        self.subtract_button.grid(row=2, column=1, padx=5, pady=5)
        self.multiply_button = ttk.Button(mainframe, text="*", command=self.multiply)
        self.multiply_button.grid(row=2, column=2, padx=5, pady=5)
        self.divide_button = ttk.Button(mainframe, text="/", command=self.divide)
        self.divide_button.grid(row=2, column=3, padx=5, pady=5)

        # Результат
        self.result_label = ttk.Label(mainframe, text="Результат: ")
        self.result_label.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

        # Добавление отступов к каждому элементу управления
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Фокус на первое текстовое поле
        self.real_part1.focus()

    def get_numbers(self):
        """
        Метод для получения чисел из полей ввода

        :return: real1, imag1, real2, imag2 - числа из полей ввода
        """
        try:
            real1 = float(self.real_part1.get())
            imag1 = float(self.imag_part1.get())
            real2 = float(self.real_part2.get())
            imag2 = float(self.imag_part2.get())
            return real1, imag1, real2, imag2
        except ValueError:
            # Если преобразование не удалось, показываем сообщение об ошибке
            messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные числа.")
            return None, None, None, None  # Возвращаем кортеж из None

    def add(self):
        """
        Метод для выполнения сложения

        :return: None
        """
        real1, imag1, real2, imag2 = self.get_numbers()
        result = self.calculator.add(complex(float(real1), float(imag1)), complex(float(real2), float(imag2)))
        self.result_label.config(text=f"Результат: {result}")

    def subtract(self):
        real1, imag1, real2, imag2 = self.get_numbers()
        result = self.calculator.subtract(complex(float(real1), float(imag1)), complex(float(real2), float(imag2)))
        self.result_label.config(text=f"Результат: {result}")

    def multiply(self):
        real1, imag1, real2, imag2 = self.get_numbers()
        result = self.calculator.multiply(complex(float(real1), float(imag1)), complex(float(real2), float(imag2)))
        self.result_label.config(text=f"Результат: {result}")

    def divide(self):
        real1, imag1, real2, imag2 = self.get_numbers()
        try:
            result = self.calculator.divide(complex(float(real1), float(imag1)), complex(float(real2), float(imag2)))
            self.result_label.config(text=f"Результат: {result}")
        except ZeroDivisionError:
            messagebox.showerror("Ошибка", "Деление на ноль!")


def main():
    """
    Главная функция, запускающая пользовательский интерфейс

    :return: None
    """
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
