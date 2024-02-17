import logging

logging.basicConfig(level=logging.INFO)

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            logging.info("Деление на ноль не допускается")
            return None
        return x / y

class CalculatorWithHistory(Calculator):
    def __init__(self):
        super().__init__()
        self.history = []
        self.results = []
''''
Паттерн Command представлен в методе execute_operation класса CalculatorWithHistory. Этот метод выполняет различные операции (команды), такие как сложение, вычитание, умножение и деление, в зависимости от входных данных. Операции инкапсулированы в виде вызовов методов.
'''
    def execute_operation(self, operation, x, y):
        if operation == '+':
            result = self.add(x, y)
        elif operation == '-':
            result = self.subtract(x, y)
        elif operation == '*':
            result = self.multiply(x, y)
        elif operation == '/':
            result = self.divide(x, y)
        else:
            logging.info("Неизвестная операция")
            return

        self.history.append((operation, x, y))
        self.results.append(result)
        logging.info(f"В результате {operation} {x} и {y}, получится {result}")
        return result

    def undo(self, steps):
        if steps > len(self.history):
            logging.info("Невозможно отменить действие, начиная с начала истории.")
            return
        for _ in range(steps):
            self.history.pop()
            self.results.pop()
        logging.info(f"Отменено {steps} шагов")
'''
        Паттерн Memento реализован через функциональность отмены (undo), позволяя возвращаться к предыдущим состояниям калькулятора. История операций и результатов сохраняется, что позволяет восстанавливать предыдущие состояния.
'''
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Вы ввели неприменимый символ, пожалуйста, введите число.")

def main():
    calculator = CalculatorWithHistory()
    while True:
        print("\nДоступные операции: Сложение: (+), Вычитание: (-), Умножение: (*), Деление: (/), Отмена: (q), Выход: (e).")
        operation = input("Введите операцию: ").strip()

        if operation == 'e':
            break

        if operation == 'q':
            steps = get_number("Сколько шагов отменить? ")
            calculator.undo(int(steps))
            continue

        x = get_number("Введите первое число: ")
        y = get_number("Введите второе число: ")

        calculator.execute_operation(operation, x, y)

if __name__ == "__main__":
    main()
    
    
'''
Принципы SOLID:
Single Responsibility Principle (Принцип единственной ответственности): Каждый класс имеет четко определенную ответственность. Calculator отвечает за выполнение арифметических операций, CalculatorWithHistory расширяет базовый калькулятор, добавляя функциональность истории и отмены действий.

Open/Closed Principle (Принцип открытости/закрытости): Классы калькулятора открыты для расширения, но закрыты для изменения. Можно добавить новые операции в Calculator без изменения кода, расширяя его функциональность.

Liskov Substitution Principle (Принцип подстановки Барбары Лисков): CalculatorWithHistory подтип Calculator и может заменять его без влияния на программу.
'''