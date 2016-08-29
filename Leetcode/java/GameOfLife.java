public class GameOfLife {
    public void gameOfLife(int[][] board) {
        int[][] numLiveNeighbors = new int[board.length][board[0].length];
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) {
                // go through each cell and find number of live neighbors
                int liveNeighbors = 0;
                for (int i = -1; i <= 1; i++) {
                    for (int j = -1; j <= 1; j++) {
                        int row = r + i;
                        int col = c + j;
                        if (row >= 0 && row < board.length && col >= 0 && col < board[0].length && !(i == 0 && j == 0)) {
                            // valid cell
                            if (board[row][col] == 1) {
                                liveNeighbors++;
                            }
                        }
                    }
                }
                numLiveNeighbors[r][c] = liveNeighbors;
            }
        }
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) {
                if (board[r][c] == 0 && numLiveNeighbors[r][c] == 3) {
                    board[r][c] = 1;
                } else if (board[r][c] == 1 && (numLiveNeighbors[r][c] < 2 || numLiveNeighbors[r][c] > 3)) {
                    board[r][c] = 0;
                }
            }
        }
    }
}
