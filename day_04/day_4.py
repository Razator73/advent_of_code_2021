with open('day_04/bingo.txt') as f:
    bingo_data = f.read()


class BingoBoard:
    def __init__(self, numbers, starting_pull=None):
        if len(numbers) == 25:
            self.board = numbers
        else:
            raise ValueError('Not enough numbers for a board')
        self.matches = []
        self.winning = False
        if starting_pull:
            for num in starting_pull:
                self.check_num(num)

    def check_num(self, num):
        try:
            match_index = self.board.index(num)
            self.matches.append((match_index // 5, match_index % 5))
            return self.check_win()
        except ValueError:
            return False

    def check_win(self):
        for k in range(5):
            self.winning = len(self.matches) > 5 and \
                           (len([match for match in self.matches if match[0] == k]) == 5 or
                            len([match for match in self.matches if match[1] == k]) == 5)
            if self.winning:
                return True

    def clear_board(self):
        self.matches = []
        self.winning = False

    def __str__(self):
        board_str = ''
        for i in range(5, 26, 5):
            board_str += ' '.join([f'{x:2}' for x in self.board[i - 5: i]])
            board_str += '\n'
        return board_str[:-1]

    def __repr__(self):
        return str(self)


# parse the data
pulled_nums = [int(num) for num in bingo_data.split('\n')[0].split(',')]
boards = '\n'.join(bingo_data.split('\n')[1:]).strip().split('\n\n')
boards = [b.split('\n') for b in boards]
parsed_boards = []
for board in boards:
    parsed_board = []
    for row in board:
        parsed_board += [int(num.strip()) for num in [row[:2], row[3:5], row[6:8], row[9:11], row[12:]]]
    parsed_boards.append(BingoBoard(parsed_board, pulled_nums[:5]))

# part 1
i = 4
winning_boards = [b for b in parsed_boards if b.winning]
while not winning_boards and i < len(pulled_nums):
    i += 1
    for board in parsed_boards:
        won = board.check_num(pulled_nums[i])
        if won:
            winning_boards.append(board)

winning_board = winning_boards[0]
print(sum([x for x in winning_board.board if x not in pulled_nums[:i + 1]]) * pulled_nums[i])

# part 2, keep going to find last board
losing_boards = [b for b in parsed_boards if not b.winning]
last_won = winning_board
while losing_boards:
    i += 1
    for board in losing_boards[:]:
        won = board.check_num(pulled_nums[i])
        if won:
            last_won = losing_boards.pop(losing_boards.index(board))

print(sum([x for x in last_won.board if x not in pulled_nums[:i + 1]]) * pulled_nums[i])
