def print_grid(grid):
    """Print the Sudoku grid."""
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
    print()

def is_valid(grid, row, col, num):
    """Check if it's valid to place num in grid[row][col]."""
    # Check if num is not repeated in the current row
    if num in grid[row]:
        return False
    
    # Check if num is not repeated in the current column
    for r in range(9):
        if grid[r][col] == num:
            return False
    
    # Check if num is not repeated in the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False
    
    return True

def solve_sudoku(grid):
    """Solve the Sudoku puzzle using backtracking."""
    empty = find_empty_location(grid)
    if not empty:
        return True  # Puzzle solved
    
    row, col = empty
    
    for num in range(1, 10):  # Try numbers 1-9
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            
            if solve_sudoku(grid):
                return True  # Solution found
            
            grid[row][col] = 0  # Reset the cell and backtrack
    
    return False  # Trigger backtracking

def find_empty_location(grid):
    """Find the next empty location in the grid (returns row, col)."""
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return (r, c)
    return None  # No empty location found

def get_user_input():
    """Prompt the user to input a Sudoku grid."""
    grid = []
    print("Enter the Sudoku grid (9 rows, each with 9 numbers, use 0 for empty cells):")
    for i in range(9):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1}: ").strip().split()))
                if len(row) != 9:
                    raise ValueError("Each row must have exactly 9 numbers.")
                if any(num < 0 or num > 9 for num in row):
                    raise ValueError("Numbers must be between 0 and 9.")
                grid.append(row)
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter the row again.")
    return grid

def main():
    # Get Sudoku grid from user
    sudoku_grid = get_user_input()
    
    print("\nOriginal Sudoku Puzzle:")
    print_grid(sudoku_grid)
    
    if solve_sudoku(sudoku_grid):
        print("Solved Sudoku Puzzle:")
        print_grid(sudoku_grid)
    else:
        print("No solution exists")

if __name__ == "__main__":
    main()
