import java.util.*;

public class Test1 {
    public static void main(String[] args) {
        try {
            int numTests = Integer.parseInt(args[0]);
            Scanner scan = new Scanner();
            for (int i = 0; i < numTests; i++) {
                String title = scan.nextLine();
            }
        } catch (Exception Ex) {
            System.out.println("Input Error");
        }
    }

    private static String titleMaker(String title) {
        if (title.contains(" ")) {
            return title + ": Age of Darkness";
        }
        return title + " Returns";
    }
}
