public class BombCheck {
    public static void main (String[] args) {
        checkSafe(args[0], args[1], args[2]);
    }

    public int checkSafe(int n, List<List<Int>> bombs, List<List<Int>> queries) {
        int numSafe = 0;
        for (int i = 0; i < queries.size(); i++) {
            boolean unsafe = false;
            int x = queries.get(i).get(0);
            int y = queries.get(i).get(1);
            for (int j = 0; j < bombs.size(); j++) {
                int bombx = bombs.get(j).get(0);
                int bomby = bombs.get(j).get(1);
                if (!(((x - 1) <= bombx && bombx <= (x + 1)) && ((y - 1) <= bomby && bomby <= (y + 1)))) {
                    // Not within range of defusal
                    int xDistance = Math.abs(x - bombx);
                    int yDistance = Math.abs(y - bomby);
                    if (x == bombx || y == bomby || xDistance == yDistance) {
                        unsafe = true;
                    }
                }
                j = bombs.size();
            }
            if (!unsafe) {
                numSafe++;
            }
        }
    }
}
