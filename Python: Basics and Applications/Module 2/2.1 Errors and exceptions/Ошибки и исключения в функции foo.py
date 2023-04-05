"""
Вашей программе будет доступна функция foo, которая может бросать исключения.

Вам необходимо написать код, который запускает эту функцию, затем ловит исключения ArithmeticError, AssertionError, ZeroDivisionError и выводит имя пойманного исключения.

Пример решения, которое вы должны отправить на проверку.

try:
    foo()
except Exception:
    print("Exception")
except BaseException:
    print("BaseException")
"""

try:
    foo()
except ZeroDivisionError as z:
    print('ZeroDivisionError')
except ArithmeticError as ar:
    print('ArithmeticError')
except AssertionError as ass:
    print('AssertionError')
