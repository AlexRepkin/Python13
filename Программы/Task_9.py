#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def calculating_garmonical(*args):
    """
    Вычисление среднего гармонического полученных аргументов.
    Если аргументов нет, то выводится None.
    """

    if args:
        garmony = 0
        for value in args:
            garmony += 1 / value
        return round(len(args)/garmony, 2)
    else:
        return "None"


if __name__ == "__main__":
    elements = [round(random.uniform(1, 25), 2)
                for _ in range(random.randint(2, 7))]
    print("Elements are:", *elements)
    print("Answer is - ", calculating_garmonical(*elements))
    print(calculating_garmonical())
