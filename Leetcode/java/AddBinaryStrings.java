public class AddBinaryStrings {
    public static String addBinary(String a, String b) {
        int diff = Math.abs(a.length() - b.length());
        if (a.length() < b.length()) {
            StringBuffer aNew = new StringBuffer();
            for (int i = 0; i < diff; i++) {
                aNew.append(0);
            }
            for (int i = 0; i < a.length(); i++) {
                aNew.append(a.charAt(i));
            }
            a = aNew.toString();
        } else if (a.length() > b.length()) {
            StringBuffer bNew = new StringBuffer();
            for (int i = 0; i < diff; i++) {
                bNew.append(0);
            }
            for (int i = 0; i < b.length(); i++) {
                bNew.append(b.charAt(i));
            }
            b = bNew.toString();
        }
        StringBuffer result = new StringBuffer();
        int carry = 0;
        for (int i = a.length() - 1; i >= 0; i--) {
            int first = Character.getNumericValue(a.charAt(i));
            int second = Character.getNumericValue(b.charAt(i));
            int sum = (first ^ second ^ carry);
            result.insert(0, sum);
            carry = (first & second) | (second & carry) | (first & carry);
        }
        if (carry > 0) {
            result.insert(0, 1);
        }
        return result.toString();
    }
}
