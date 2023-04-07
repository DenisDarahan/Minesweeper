from game.cli.game_field import GameField


class GameProcess:
    game_field: GameField

    def __init__(self, width: int = 10, height: int = 10, mines_amount: int = None):
        try:
            self.game_field = GameField(width, height, mines_amount)
        except Exception as ex:
            print(f'[Error] Cannot start the game: {", ".join(map(str, ex.args))}')

    def run(self):
        print('Commands:\n'
              '1 or open [x] [y] to open the cell\n'
              '2 or flag [x] [y] to mark or unmark cell as mine\n'
              '0 or "exit" to exit\n')

        while True:
            self.game_field.display()

            command = input('> ')
            print()
            command, *params = command.split(' ', 1)

            if command in ('1', 'open'):
                try:
                    end_game, win = self.game_field.open(*map(int, filter(None, params[0].split())))
                except Exception as ex:
                    print(f'[Error] Cannot open cell: {", ".join(map(str, ex.args))}')
                else:
                    if end_game:
                        self.game_field.display()
                        print('You win!' if win else 'You died')
                        print()
                        break

            elif command in ('2', 'flag'):
                try:
                    self.game_field.change_flag(*map(int, filter(None, params[0].split())))
                except Exception as ex:
                    print(f'[Error] Cannot set flag: {", ".join(map(str, ex.args))}')

            elif command in ('0', 'exit'):
                break
