// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

public class Equi {
    public int solution(int[] A) {
        // write your code in Java SE 8
        int[] forward = fillForward(A);
        int[] backward = fillBackward(A);
        boolean found = false;
        int index = -1;
        for (int i = 0; i < A.length && !found; i++) {
            if (forward[i] == backward[i]) {
                found = true;
                index = i;
            }
        }
        return index;
    }

    private int[] fillForward(int[] arr) {
        int[] forward = new int[arr.length];
        int sum = 0;
        for (int i = 1; i < arr.length - 1; i++) {
            sum += arr[i];
            forward[i] = sum;
        }
        return forward;
    }

    private int[] fillBackward(int[] arr) {
        int[] backward = new int[arr.length];
        int sum = 0;
        for (int i = arr.length - 1; i >= 0; i--) {
            sum += arr[i];
            backward[i] = sum;
        }
        return backward;
    }
}
