#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def summ_after_min(*args):
    """Вывод рисунка, исходя из полученных чисел"""

    if args:
        patterns = {
            1: "*"*10,
            2: "҉"*10,
            3: "֍"*10,
            4: "美"*10,  # Означает "Красота", согласно словарю
            5: "⊛"*10,
            6: "⌛"*10,
            7: "☕"*10,
            8: "☯"*10,
            9: "⛏"*10,
            10: "✿"*10,
            11: "✨"*10
        }
        for i in args:
            print(patterns.get(i))
    else:
        print("None - list is empty!")


if __name__ == "__main__":
    elements = [random.randint(1, 11) for _ in range(random.randint(2, 30))]
    print("Elements are:", *elements)
    summ_after_min(*elements)
    summ_after_min()
