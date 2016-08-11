public class PlusOne {
    public int[] plusOne(int[] digits) {
        if (digits[digits.length - 1] < 9) {
            digits[digits.length - 1]++;
        } else {
            int index = digits.length - 1;
            while (index > 0 && digits[index] == 9) {
                digits[index] = 0;
                index--;
            }
            if (index != 0 || digits[index] < 9) {
                digits[index]++;
            } else {
                // Increase number of digits
                int newLength = digits.length + 1;
                digits = new int[newLength];
                digits[0] = 1;
            }
        }
        return digits;
    }
}
