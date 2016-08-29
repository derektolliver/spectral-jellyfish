/* The guess API is defined in the parent class GuessGame.
   @param num, your guess
   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
      int guess(int num); */

public class GuessingGame extends GuessGame {
    public int guessNumber(int n) {
        if (guess(n) == 0) {
            return n;
        }
        int choice = n / 2;
        int min = 1;
        int max = n;
        while(guess(choice) != 0) {
            if (guess(choice) == 1) {
                min = choice;
            } else {
                max = choice;
            }
            int range = max - min;
            choice = min + (range / 2);
        }
        return choice;
    }
}
