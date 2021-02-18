# three
# cells = '_XXOO_OX_'
cells = input("Enter the cells: ")
a = ' '.join(cells[:3]).split()
b = ' '.join(cells[3:6]).split()
g = ' '.join(cells[6:10]).split()
field = [a] + [b] + [g]

# lambda func for replace '_' by ' '
replace_underscore = lambda x: ' ' if x == '_' else x
for i in range(3):
    field[i] = [replace_underscore(j) for j in field[i]]

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
    m = [val for sublist in field for val in sublist]  # from 2d to 1d array
    # all patterns of possbile winning cases 
    rule = [m[:3], m[3:6], m[6:], m[0:9:3], m[1:9:3], m[2:9:3], m[0:9:4], m[2:7:2]]
    if (['X', 'X', 'X'] in rule and ['O', 'O', 'O'] in rule) or abs(matrix.count("X") - matrix.count("O")) >= 2:
        return "Impossible"
    elif ['X', 'X', 'X'] in rule:
        return "X wins"
    elif ['O', 'O', 'O'] in rule:
        return "O wins"
    elif any([i for i in matrix if ' ' in i]):  # return bool
        return "Game not finished"
    else:  # the matrix is complete
        return "Draw"

print_table(field)
check_input(field)
print_table(field)
print(state(field))
