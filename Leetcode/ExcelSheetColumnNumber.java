public class ExcelSheetColumnNumber {

    public static final int ASCII_VAL = 65 - 1;
    public static final int ALPHA_SIZE = 26;

    public int titleToNumber(String s) {
        int colNum = 0;
        int counter = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
            int charVal = (int) s.charAt(i);
            charVal -= ASCII_VAL;
            colNum += Math.pow(ALPHA_SIZE, counter) * charVal;
            counter++;
        }

        return colNum;
    }
}
