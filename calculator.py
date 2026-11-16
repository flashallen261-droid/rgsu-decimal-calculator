"""Decimal CLI calculator with explicit operations and input validation."""
import argparse
from decimal import Decimal, InvalidOperation, localcontext
import operator

OPERATIONS = {'+': operator.add, '-': operator.sub,
              '*': operator.mul, '/': operator.truediv}


def calculate(left: str, operation: str, right: str) -> Decimal:
    if operation not in OPERATIONS:
        raise ValueError('Допустимые операции: + - * /')
    try:
        a, b = Decimal(left), Decimal(right)
    except InvalidOperation as exc:
        raise ValueError('Введите два числа') from exc
    if not (a.is_finite() and b.is_finite()):
        raise ValueError('Числа должны быть конечными')
    if operation == '/' and b == 0:
        raise ValueError('Деление на ноль недопустимо')
    with localcontext() as context:
        context.prec = 28
        try:
            return OPERATIONS[operation](a, b)
        except ArithmeticError as exc:
            raise ValueError('Результат вне допустимого диапазона') from exc


def main():
    parser = argparse.ArgumentParser(description='Калькулятор с Decimal')
    parser.add_argument('left')
    parser.add_argument('operation', choices=OPERATIONS)
    parser.add_argument('right')
    args = parser.parse_args()
    try:
        print(calculate(args.left, args.operation, args.right))
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == '__main__':
    main()
