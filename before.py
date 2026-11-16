"""Исходная версия для самостоятельного сравнения и улучшения."""
import argparse


def calculate(a, operation, b):
    a, b = float(a), float(b)
    if operation == '+':
        return a + b
    if operation == '-':
        return a - b
    if operation == '*':
        return a * b
    if operation == '/':
        return a / b
    raise ValueError('Unknown operation')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('a')
    parser.add_argument('operation')
    parser.add_argument('b')
    args = parser.parse_args()
    print(calculate(args.a, args.operation, args.b))
