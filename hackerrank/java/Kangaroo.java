import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Kangaroo {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int x1 = in.nextInt();
        int v1 = in.nextInt();
        int x2 = in.nextInt();
        int v2 = in.nextInt();

        boolean result = false;
        if (x1 == x2) {
            result = true;
        } else if ((x1 > x2 && v1 < v2) || (x2 > x1 && v2 < v1)) {
            int fast;
            int slow;
            int farJump;
            int shortJump;
            if (x1 > x2) {
                fast = x2;
                slow = x1;
                farJump = v2;
                shortJump = v1;
            } else {
                fast = x1;
                slow = x2;
                farJump = v1;
                shortJump = v2;
            }
            while (fast < slow) {
                fast += farJump;
                slow += shortJump;
            }
            if (fast == slow) {
                result = true;
            }
        }
        if (result) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
