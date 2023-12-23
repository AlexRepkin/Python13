#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def summ_after_min(*args):
    """
    Вычисление суммы аргументов после минимального.
    Если аргументов нет, то выводится None.
    """

    if args:
        summ = 0
        found = False
        minimal = min(args)
        for value in args:
            if found:
                summ += value
            elif minimal == value:
                found = True
        return "Summ of elements after",  minimal, "is", summ
    else:
        return "None"


if __name__ == "__main__":
    elements = [random.randint(1, 100) for _ in range(random.randint(2, 20))]
    print("Elements are:", *elements)
    print(summ_after_min(*elements))
    print(*summ_after_min(*elements))  # Экспериментирование с распаковкой
    print("Result for empty list:", summ_after_min())
