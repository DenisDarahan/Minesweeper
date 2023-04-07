# run from Minesweeper directory with "python3 -m game.cli" command


from game.cli.game_process import GameProcess


def main():
    while True:
        print('Menu:\n'
              '1 or game to start the game\n'
              '! note that you can pass width, height and mines amount to game:\n'
              '! game 20 20 34\n'
              '0 or "exit" to exit\n')

        command = input('>>> ')
        print()
        command, *params = command.split(' ', 1)

        if command in ('1', 'game'):
            if params:
                params = params[0].split()

            try:
                GameProcess(*map(int, filter(None, params))).run()
            except ValueError:
                print(f'[Error] Wrong arguments')

        elif command in ('0', 'exit'):
            break


if __name__ == '__main__':
    main()
