#Test for a Sudoku puzzle where every cell is filled

#Test each row contains every digit 1-9 exactly
#Test each columns contains every digit 1-9 exactly
#Test each boxes contains every digit 1-9 exactly
#Test board has correct dimensions 9 * 9

# def is_puzzle_correct_size(puzzle):
#     try:
#         for i in range(9):
#             for j in range(9):
#                 cell_entry = puzzle[i][j]

    
#     return True
#     except IndexError as e:
#         pass
#         return False


def is_puzzle_correct_size(puzzle):
    try:
        if(len(puzzle) != 9):
            # print("inside puzzle loop")
            # print(len(puzzle))
            return False

        for line in puzzle:
            # print("inside line loop")
            # print(len(line))
            if(len(line) != 9):
                # print("inside line loop if statement")
                return False
    
        return True
    except IndexError as e:
        pass
        return False


correct_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
correct_row_strings = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def row_contains_correct_digits(puzzle_row):
    print(puzzle_row)
    print(sorted(puzzle_row))
    if(sorted(puzzle_row) == correct_row):
        return True
    
    elif(sorted(puzzle_row) == correct_row_strings):
        return True
    
    return False