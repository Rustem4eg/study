import itertools

SUITS = ['♠', '♥', '♣', '♦']
RANKS = [str(i) for i in range(2,11)] + list('JQKA')

cards = [rank + suit for rank in RANKS for suit in SUITS]
q_combinations = 3
combinations = itertools.combinations(cards, q_combinations)

with open('Module_5/les_11_pract3/card_combinations.txt', 'w', encoding='utf-8') as file:
    for combination in combinations:
        line = ', '.join(combination) + '\n'
        file.write(line)

print("Комбинации карт сохранены в файл card_combinations.txt")