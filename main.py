import Test.CompletedSudokuTests

result = False

test_puzzle = [["5","3",".",".","7",".",".",".","."],
               ["6",".",".","1","9","5",".",".","."],
               [".","9","8",".",".",".",".","6","."],
               ["8",".",".",".","6",".",".",".","3"],
               ["4",".",".","8",".","3",".",".","1"],
               ["7",".",".",".","2",".",".",".","6"],
               [".","6",".",".",".",".","2","8","."],
               [".",".",".","4","1","9",".",".","5"],
               [".",".",".",".","8",".",".","7","9"]]
test_puzzle_2 = [["6",".",".","1","9","5",".",".","."],
               [".","9","8",".",".",".",".","6","."],
               ["8",".",".",".","6",".",".",".","3"],
               ["4",".",".","8",".","3",".",".","1"],
               ["7",".",".",".","2",".",".",".","6"],
               [".","6",".",".",".",".","2","8","."],
               [".",".",".","4","1","9",".",".","5"],
               [".",".",".",".","8",".",".","7","9"],
               [".",".",".",".","8",".",".","7","9"],
               [".",".",".",".","8",".",".","7","9"],
               [".",".",".",".","8",".",".","7","9"]]



test_completed_puzzle= [[9, 2, 1, 6, 3, 7, 5, 8, 4],
                        [6, 7, 4, 5, 1, 8, 9, 2, 3],
                        [5, 8, 3, 4, 9, 2, 1, 6, 7],
                        [2, 6, 9, 8, 5, 4, 3, 7, 1],
                        [7, 4, 5, 3, 6, 1, 2, 9, 8],
                        [1, 3, 8, 7, 2, 9, 6, 4, 5],
                        [8, 5, 6, 2, 7, 3, 4, 1, 9],
                        [4, 1, 2, 9, 8, 5, 7, 3, 6]]

test_row = [3, 9, 7, 1, 4, 6, 8, 5, 2]
test_row_strings = ["3", "9", "7", "1", "4", "6", "8", "5", "2"]
# result = run_tests_on_puzzle.start_tests(puzzle)
# print(Test.CompletedSudokuTests.is_puzzle_correct_size(test_puzzle_2))



print(Test.CompletedSudokuTests.row_contains_correct_digits(test_row_strings))
print(result)