import random

field = [[' ']*3 for i in range(3)]

def print_field(matrix):
    print("---------")
    for i in range(3):
        print('|', end=' ')
        for j in range(3):
            print(matrix[i][j], end=' ')
        print('|')
    print("---------")
    return

def user_move(matrix, count_move):
    coord = list(input("Enter the coordinates: ").split())
    while True:
        if coord == []:
            print("Can't be empty")
            coord = list(input("Enter the coordinates: ").split())
            return user_move(matrix, count_move)
        try:
            int(coord[0])
        except ValueError:
            print("You should enter numbers!")
            return user_move(matrix, count_move)

        if len(coord) != 2:
            print("Coordinates should consist of two numbers")
            return user_move(matrix, count_move)

        x = int(coord[0]) - 1
        y = int(coord[1]) - 1
                         
        if (x+1 > 3) or (y+1 > 3):
            print("Coordinates should be from 1 to 3!")
        elif matrix[x][y] != ' ':
            print("This cell is occupied! Choose another one!")
        else:
            if state(matrix):
                print(state(matrix))
                return
            matrix[x][y] = "X"
            count_move += 1
            print_field(matrix)
            return make_moves(matrix, count_move)
        return user_move(matrix, count_move)

def computer_move(matrix, count_move):
    # base case. maybe something count < 9?
    # if it return True, we have the result, stop
    if state(matrix):
        print(state(matrix))
        return
    pc_x, pc_y = random.choice([0, 1, 2]), random.choice([0, 1, 2])
    if matrix[pc_x][pc_y] == ' ':
        print('Making move level "easy"')
        matrix[pc_x][pc_y] = 'O'
        count_move += 1
        print_field(matrix)
        return make_moves(matrix, count_move)
    return computer_move(matrix, count_move)
     
def make_moves(matrix, count_move):
    if state(matrix):
        print(state(matrix))
        return
    if count_move % 2 != 0:
        return user_move(matrix, count_move)
    return computer_move(matrix, count_move)

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
    elif not any([i for i in matrix if ' ' in i]):  # matrix is complete
        return "Draw"
    # matrix is not complete. game not finished
    else:  # any([i for i in matrix if ' ' in i]):
        return False
    

print_field(field)
count_m = 1
make_moves(field, count_m)
