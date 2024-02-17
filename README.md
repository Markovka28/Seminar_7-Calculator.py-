''''
    Паттерн Command представлен в методе execute_operation класса CalculatorWithHistory. Этот метод выполняет различные операции (команды), такие как сложение, вычитание, умножение и деление, в зависимости от входных данных. Операции инкапсулированы в виде вызовов методов.
'''
    Паттерн Memento реализован через функциональность отмены (undo), позволяя возвращаться к предыдущим состояниям калькулятора. История операций и результатов сохраняется, что позволяет восстанавливать предыдущие состояния.
'''
Принципы SOLID:
Single Responsibility Principle (Принцип единственной ответственности): Каждый класс имеет четко определенную ответственность. Calculator отвечает за выполнение арифметических операций, CalculatorWithHistory расширяет базовый калькулятор, добавляя функциональность истории и отмены действий.

Open/Closed Principle (Принцип открытости/закрытости): Классы калькулятора открыты для расширения, но закрыты для изменения. Можно добавить новые операции в Calculator без изменения кода, расширяя его функциональность.

Liskov Substitution Principle (Принцип подстановки Барбары Лисков): CalculatorWithHistory подтип Calculator и может заменять его без влияния на программу.
'''