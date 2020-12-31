from player import Player


class Game:
    def __init__(self):
        self.remaining_stones = 14
        self.boy = Player(strategy='random')
        self.computer = Player(strategy='optimal')
        self.current_player = self.boy
        self.winner = None

    def _update_remaining_stones(self, number_to_take):
        self.remaining_stones -= number_to_take

    def _update_current_player(self):
        if self.current_player == self.boy:
            self.current_player = self.computer
        else:
            self.current_player = self.boy

    def play_game(self):
        while self.remaining_stones > 0:
            number_to_take = self.current_player.take(self.remaining_stones)
            self._update_remaining_stones(number_to_take)

            if self.remaining_stones > 0:
                self._update_current_player()

        self.winner = self.current_player
        # print('{} won the game'.format(self.winner))
