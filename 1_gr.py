from random import shuffle
from os import system


'''
Карты:
    имя
    цена
    масть

Колода: всего карт = цены * масти
    в 1 масти: 6, 7, 8, 9, 10, валет, дама, король, туз

Игроки - от 2 штук

Колода перемешивается

Кажому игроку выдается по 2 карты из колоды

Игрок видит только свои карты

Задача - цены всех карт игрока = 21

Ход игрока:
    оставить свои карты и больше не набирать
    или взять еще карту (сколько угодно раз)

Все игроки должны закончить ход

Если у игрока сумма цен всех карт > 21, он проиграл
Если у всех игроков проигрыш, то это ничья

Выигрывает тот, у кого больше очков и тот, кто не проиграл
'''


def get_deck() -> list[dict]:
    suits = ['бубны', 'черви', 'пики', 'крести']
    names = ['6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
    deck = []

    for suit in suits:
        for name in names:
            if name in ('валет', 'дама', 'король'):
                value = 10
            elif name == 'туз':
                value = 11
            else:
                value = int(name)
            card = {
                'имя': name,
                'цена': value,
                'масть': suit
            }
            deck.append(card)
    return deck

def get_players():
    player_1 = {
        'человек': True,
        'имя': 'вася',
        'карты': [],
        'счет': 10
    }
    player_2 = {
        'человек': True,
        'имя': 'ася',
        'карты': [],
        'счет': 10
    }
    return [player_1, player_2]

def deal_cards(num: int) -> None:
    for player in players:
        for i in range(num):
            player['карты'].append(deck.pop(-1))

def show_cards() -> None:
    for card in player['карты']:
        print(card['имя'], card['масть'])

deck = get_deck()
shuffle(deck)
players = get_players()
deal_cards(2)

for player in players:
    while True:
        system('cls')
        show_cards()
        player_option = input('взять карту? y/n:')
        if player_option == 'y':
            player['карты'].append(deck.pop(-1))
        else:
            break
for player in players:
    total = 0
    for card in player['карты']:
        total += card['цена']
    print('-' * 20)
    print(player['имя'], total)
    print('-' * 20)