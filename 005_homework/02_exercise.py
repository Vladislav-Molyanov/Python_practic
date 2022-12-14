'''Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""'''

import random as rnd


def get_candies() -> int:
    candies_cnt = int(input('Введите количество конфет: '))
    while candies_cnt > 28 or candies_cnt < 1 or candies_cnt > number_of_candies:
        print('Вы взяли неправильное количество конфет, попробуйте снова!')
        candies_cnt = int(input('Введите количество конфет: '))
    return candies_cnt


print('ИГРА С КОНФЕТАМИ.\n\n'
      'МЕНЮ:\n'
      '1. Игра на двоих.\n'
      '2. Игра против бота.\n'
      '0. Выход из игры.')
key = ''
while key != '0':
    number_of_candies = 2021
    key = input('Выберите пункт меню: ')
    match key:
        case '1':
            player_1 = input('Введите имя первого игрока: ')
            player_2 = input('Введите имя второго игрока: ')
            order = 1 if rnd.randint(1, 2) == 1 else 2
            while number_of_candies:
                match order:
                    case 1:
                        print(f'Ходит игрок №1 - {player_1}!')
                        count_candies = get_candies()
                        number_of_candies -= count_candies
                        print(f'{player_1} взял {count_candies} конфет. Осталось {number_of_candies} конфет')
                        if not number_of_candies:
                            print(f'Игрок №1 - {player_1} победил!')
                            break
                        order = 2
                    case 2:
                        print(f'Ходит игрок №2 - {player_2}!')
                        count_candies = get_candies()
                        number_of_candies -= count_candies
                        print(f'{player_2} взял {count_candies} конфет. Осталось {number_of_candies} конфет')
                        if not number_of_candies:
                            print(f'Игрок №2 - {player_2} победил!')
                            break
                        order = 1
        case '2':
            player_1 = input('Введите имя игрока: ')
            player_2 = 'Bot'
            order = 1 if rnd.randint(1, 2) == 1 else 2
            while number_of_candies:
                match order:
                    case 1:
                        print(f'Ходит игрок {player_1}!')
                        count_candies = get_candies()
                        number_of_candies -= count_candies
                        print(f'{player_1} взял {count_candies} конфет. Осталось {number_of_candies} конфет')
                        if not number_of_candies:
                            print(f'Игрок №1 - {player_1} победил!')
                            break
                        order = 2
                    case 2:
                        print(f'Ходит {player_2}!')
                        candies_cnt = number_of_candies if number_of_candies <= 28 else rnd.randint(1, 28)
                        number_of_candies -= candies_cnt
                        print(f'{player_2} взял {candies_cnt} конфет. Осталось {number_of_candies} конфет')
                        if not number_of_candies:
                            print(f'{player_2} победил!')
                            break
                        order = 1
        case '0':
            print('Выход из игры!')
        case _:
            print('Такого пункта меню не существует! Пожалуйста выберите значения 0-2')