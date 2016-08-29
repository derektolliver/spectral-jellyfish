public class RomanToInt {
    public int romanToInt(String s) {
        HashMap<String, Integer> numerals = new HashMap<String, Integer>();
        numerals.put("I", 1);
        numerals.put("V", 5);
        numerals.put("X", 10);
        numerals.put("L", 50);
        numerals.put("C", 100);
        numerals.put("D", 500);
        numerals.put("M", 1000);
        numerals.put("IV", 4);
        numerals.put("IIX", 8);
        numerals.put("IX", 9);
        numerals.put("XL", 40);
        numerals.put("XC", 90);
        numerals.put("CD", 400);
        numerals.put("CM", 900);

        int result = 0;
        for (int i = 0; i < s.length(); i++) {
            String letter = Character.toString(s.charAt(i));
            int val = numerals.get(letter);
            if (val == 1) {
                if (i < s.length() - 1) {
                    String nextLetter = Character.toString(s.charAt(i + 1));
                    if (nextLetter.equals("V") || nextLetter.equals("X")) {
                        val = numerals.get(letter + nextLetter);
                        i++;
                    } else if (i < s.length() - 2 && nextLetter.equals("I") && s.charAt(i + 2) == 'X') {
                        val = numerals.get(letter + nextLetter + Character.toString(s.charAt(i + 2)));
                        i += 2;
                    }
                }
            } else if (val == 10) {
                if (i < s.length() - 1 && (s.charAt(i + 1) == 'L' || s.charAt(i + 1) == 'C')) {
                    val = numerals.get(letter + Character.toString(s.charAt(i + 1)));
                    i++;
                }
            } else if (val == 100) {
                if (i < s.length() - 1 && (s.charAt(i + 1) == 'M' || s.charAt(i + 1) == 'D')) {
                    val = numerals.get(letter + Character.toString(s.charAt(i + 1)));
                    i++;
                }
            }
            result += val;
        }
        return result;
    }
}
