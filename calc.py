Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
... 
... filename, num1, op, num2 = sys.argv
... num1, num2 = float(num1), float(num2)
... 
... if op == '+':
...     print(num1 + num2)
... elif op == '-':
...     print(num1 - num2)
... elif op == 'x':
...     print(num1 * num2)
... elif op == '/':
...     print(num1 / num2)
... elif op == '^':
...     print(num1 ** num2)
... else:
...     print(0)
