public class NimGame {
    public boolean canWinNim(int n) {
        if (n % 4 == 0 && n > 3) {
            return false;
        } else {
            return true;
        }
    }
}
