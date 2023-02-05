import random
from functools import reduce

class BoardGame():
    """
    Class for the game.
    """

    def __init__(self):
        """
        Initialize the game grid size and total number of players.
        """
        self.players_details = dict()
        self.grid = 0

    def set_players(self, total_players):
        """
        Setter for the player.
        :param total_players: Interger Value.
        :return:
        """
        for i in range(1, total_players+1):
            self.players_details[f"Player_{i}"] = [1]

    def set_grid(self, number):
        """
       Setter fot grid value.
        :param number: Interger Value.
        :return: None
        """
        self.grid = number**2

    def dice_throw(self):
        """
        Functino to replicate the dice throw.
        :return: Random integer between 1 to 6.
        """
        return random.randint(1,6)

    def update_player_position(self, player_name, points):
        """
        Function to update player points.
        :param player_name: Player name
        :param points: Interger
        :return: None
        """
        self.players_details[player_name].append(points)

    def check_player_current_position(self, player_name):
        """
        Function to check the player current postion.
        :param player_name: Name of the player.
        :return: Current position of the player.
        """
        return reduce(lambda a,b: a+b, self.players_details[player_name])

    def check_winner(self):
        """
        Function to check if any of the player is win the game.
        :return: palyer_name if any player wins or return None if nobody wins.
        """
        for player_name in self.players_details.keys():
            if self.grid == self.check_player_current_position(player_name):
                return player_name
        return

    def show_player_positions(self):
        """
        Function to Display all players current postions.
        :return: Dictionary of player name their positions.
        """
        return {player_name: self.check_player_current_position(player_name) for player_name in self.players_details.keys()}

    def show_player_history(self):
        """
        Function to show each player position history.
        :return: player_details dictionary.
        """
        return self.players_details

    def start(self, grid_size, total_players):
        """
        Function to Start game
        :param grid_size: Grid size of the board.
        :param total_players: Total number of players.
        :return: Winner name.
        """
        self.set_grid(grid_size)
        self.set_players(total_players)
        winner = None
        while True:
            if winner:
                break
            for player in self.players_details.keys():
                winner = self.check_winner()
                if winner:
                    break
                while True:
                    points = self.dice_throw()
                    if self.check_player_current_position(player) + points <= self.grid:
                        self.update_player_position(player, points)
                        break
        return f"{winner} wins."


game = BoardGame()
print(game.start(5,4))
print(game.show_player_positions())
print(game.show_player_history())
