#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def calculating_multiply(*args):
    """
    Вычисление среднего геометрического полученных аргументов.
    Если аргументов нет, то выводится None.
    """

    if args:
        multiply = 1.0
        for value in args:
            multiply *= value
        return round(pow(multiply, 1/len(args)), 2)
    else:
        return "None"


if __name__ == "__main__":
    elements = [round(random.uniform(1, 25), 2)
                for _ in range(random.randint(2, 7))]
    print("Elements are:", *elements)
    print("Answer is - ", calculating_multiply(*elements))
    print(calculating_multiply())
