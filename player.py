import random


class Player:
    def __init__(self, strategy):
        self.strategy = strategy
        self.name = 'boy' if strategy == 'random' else 'computer'

    def __str__(self):
        return '{self.name}'.format(self=self)

    def take(self, remaining_stones):
        if self.strategy == 'optimal':
            number_to_take = max(remaining_stones % 6, 1)
        else:
            number_to_take = random.randint(1, 5) if remaining_stones > 5 else remaining_stones
        return number_to_take
