public class ValidSudokuBoard {
    public boolean isValidSudoku(char[][] board) {
        for (int r = 0; r < board.length; r++) {
            ArrayList<Character> rowList = new ArrayList<Character>();
            for (int c = 0; c < board.length; c++) {
                if (board[r][c] != '.') {
                    if (!rowList.contains(board[r][c])) {
                        rowList.add(board[r][c]);
                    } else {
                        return false;
                    }
                }
                if ((r == 1 && (c == 1 || c == 4 || c == 7)) || (r == 4 && (c == 1 || c == 4 || c == 7)) || (r == 7 && (c == 1 || c == 4 || c == 7))) {
                    ArrayList<Character> boxList = new ArrayList<Character>();
                    for (int i = -1; i <= 1; i++) {
                        int newRow = r + i;
                        for (int j = -1; j <= 1; j++) {
                            int newCol = c + j;
                            if (board[newRow][newCol] != '.') {
                                if (!boxList.contains(board[newRow][newCol])) {
                                    boxList.add(board[newRow][newCol]);
                                } else {
                                    return false;
                                }
                            }
                        }
                    }
                }
            }
        }
        for (int c = 0; c < board.length; c++) {
            ArrayList<Character> colList = new ArrayList<Character>();
            for (int r = 0; r < board.length; r++) {
                if (board[r][c] != '.') {
                    if (!colList.contains(board[r][c])) {
                        colList.add(board[r][c]);
                    } else {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
