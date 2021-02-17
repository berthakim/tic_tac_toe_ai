# final
# cells = '_XXOO_OX_'
cells = input("Enter the cells: ")
a = ' '.join(cells[:3]).split()
b = ' '.join(cells[3:6]).split()
g = ' '.join(cells[6:10]).split()

field = []
field = [a] + [b] + [g]

# func for replace '_' by ' '
def modif(a):
    if a == '_':
        return ' '
    return a
# replace
for i in range(3):
    field[i] = [modif(j) for j in field[i]]


def print_table(matrix):
    print("---------")
    for i in range(3):
        print('|', end=' ')
        for j in range(3):
            print(matrix[i][j], end=' ')
        print('|')
    print("---------")
    return

def check_input(matrix):
    coord = list(input("Enter the coordinates: ").split())
    while True:
        if coord == []:
            print("Can't be empty")
            coord = list(input("Enter the coordinates: ").split())
            return check_input(matrix)
        try:
            int(coord[0])
        except ValueError:
            print("You should enter numbers!")
            return check_input(matrix)

        if len(coord) != 2:
            print("Coordinates should consist of two numbers")
            return check_input(matrix)

        x = int(coord[0]) - 1
        y = int(coord[1]) - 1
                         
        if (x+1 > 3) or (y+1 > 3):
            print("Coordinates should be from 1 to 3!")
        elif matrix[x][y] != ' ':
            print("This cell is occupied! Choose another one!")
        else:
            return make_the_move(matrix, x, y)
        return check_input(matrix)
    
def make_the_move(matrix, coord1, coord2):
    number_of_x = len([i for sublist in matrix for i in sublist if i == "X"])
    number_of_o = len([i for sublist in matrix for i in sublist if i == "O"])
    if number_of_x <= number_of_o:
        matrix[coord1][coord2] = "X"
        return matrix
    else:
        matrix[coord1][coord2] = "O"
        return matrix

def state(matrix):
    # who win, X or O?
    if any([i for i in matrix if i == ['X', 'X', 'X']]):
        return "X wins"
    elif any([i for i in matrix if i == ['O', 'O', 'O']]):
        return "O wins"
    
    for j in range(3):
        if [field[0][j], field[1][j], field[2][j]] == ['X', 'X', 'X']:
            return "X wins"
        elif [field[0][j], field[1][j], field[2][j]] == ['O', 'O', 'O']:
            return "O wins"
        
    if [field[0][0], field[1][1], field[2][2]] == ['X', 'X', 'X']:
        return "X wins"
    elif [field[2][0], field[1][1], field[0][2]] == ['X', 'X', 'X']:
        return "X wins"
    elif [field[0][0], field[1][1], field[2][2]] == ['O', 'O', 'O']:
        return "O wins"
    elif [field[2][0], field[1][1], field[0][2]] == ['O', 'O', 'O']:
        return "O wins"
    
    # True if the table still has empty cells
    elif any([i for i in matrix if ' ' in i]):
        return "Game not finished"
    else:  # the matrix is complete
        return "Draw"
    
    
def state_v2(a):
    rule = [a[:3], a[3:6], a[6:], a[0:9:3], a[1:9:3], a[2:9:3], a[0:9:4], a[2:7:2]]
    if (['X', 'X', 'X'] in rule and ['O', 'O', 'O'] in rule) or abs(a.count("X") - a.count("O")) >= 2:
        return "Impossible"
    elif ['X', 'X', 'X'] in rule:
        return "X wins"
    elif ['O', 'O', 'O'] in rule:
        return "O wins"
    elif a.count(" ") == 0:
        return "Draw"
    elif a.count(" ") != 0:
        return "Game not finished"

print_table(field)
check_input(field)
print_table(field)
print(state_v2(field))
