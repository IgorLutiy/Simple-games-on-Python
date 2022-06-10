# Гра "Вгадай число"

from random import *

while True:
    question = input("""Ви хочете зіграти у гру 'Вгадай число'?
Якщо хочете, напишіть 'так', якщо ні, натисніть enter: """)
    if question == 'так':
        print("-----------------------")

        x = randint(1, 100)
        sprobi = 1

        my_number = int(input("Спробуйте вгадати число (від 1 до 100): "))
        print("-----------------------")
        while my_number != x:
            if my_number > x:
                print("Спробуйте менше число\n")
            elif my_number < x:
                print("Спробуйте більше число\n")
            elif my_number == x:
                print("Все вірно, ви вгадали! Це справді", my_number)
                print("Вам для цього знадобилося", sprobi, "спроб")
                print("***********************")
                break
            my_number = int(input("Спробуйте вгадати число: "))
            print("-----------------------")
            sprobi += 1
        else:
            print("Все вірно, ви вгадали! Це справді", my_number)
            print("Кількість спроб:", sprobi)
            print("***********************")
    else:
        break
