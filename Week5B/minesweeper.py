__author__ = 'KoicsD'


# Minesweeper is a really popular game. The rule is there is a 10x10 table and there are 10 mines and we have to find
# out where the mines are. We have a mine detector which can detect if there are one or more mines in some of the
# neighbour fields. Your goal is to write a function which takes a list of lists (matrix) as a parameter which includes
# only dots and Xs and returns another matrix where the neighbours of Xs are numbers and each of them means how many Xs
# are in the neibours (except it is zero). Dots represent empty fields and Xs represent mines.

# Sorry. I tried to index-assign a str. It is impossible. Not enough time to repair it.


limit = 10


def is_there_miner(matrix, ind):
    i, j = ind
    if i in range(0, limit) and j in range(0, limit):
        if matrix[i][0][j] == 'X':
            return True
        else:
            return False
    else:
        return False


def detect_one(matrix, ind):
    i, j = ind
    indexes = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    ans = 0
    for m, n in indexes:
        ans += int(is_there_miner(matrix, (m, n)))
    return ans


def detect(matrix: list):
    if type(matrix) is not list or not all(type(row) is list for row in matrix)\
            or not all(type(row[0]) is str for row in matrix):
        raise TypeError()
    if len(matrix) != limit or any(len(row[0]) != limit for row in matrix):
        raise TypeError()

    ans = matrix.copy()

    for i in range(limit):
        for j in range(limit):
            if matrix[i][0][j] != 'X':
                first = ans[i][0][0:j]
                second = ans[i][0][j + 1:]
                ch = detect_one(matrix, (i, j))
                ans[i][0] = str(ch).join([first, second])
    return ans


if __name__ == '__main__':
    assert detect([ ['X.........'],
                    ['......X...'],
                    ['..........'],
                    ['...X......'],
                    ['..........'],
                    ['XX........'],
                    ['.......X..'],
                    ['....X.....'],
                    ['..X.......'],
                    ['...X.....X'] ]) == \
           [ ['X1...111..'],
             ['11...1X1..'],
             ['..111111..'],
             ['..1X1.....'],
             ['22211.....'],
             ['XX1...111.'],
             ['2211111X1.'],
             ['.112X1111.'],
             ['.1X321..11'],
             ['.12X1...1X'] ]