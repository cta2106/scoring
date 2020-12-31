from game import Game


class MonteCarlo:
    def __init__(self, n_sim):
        self.game = None
        self.n_sim = n_sim
        self.boy_wins = 0
        self.computer_wins = 0

    def run_simulation(self):
        for _ in range(self.n_sim):
            self.game = Game()
            self.game.play_game()
            if self.game.winner.name == self.game.boy.name:
                self.boy_wins += 1
            else:
                self.computer_wins += 1