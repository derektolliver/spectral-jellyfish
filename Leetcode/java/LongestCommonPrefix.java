public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        StringBuffer result = new StringBuffer();
        if (strs.length == 0) {
            return result.toString();
        }
        for (int i = 0; i < strs[0].length(); i++) {
            result.append(strs[0].charAt(i));
        }
        for (int i = 1; i < strs.length; i++) {
            String compare = strs[i];
            if (result.length() > compare.length()) {
                int temp = result.length() - 1;
                for (int j = temp; j >= compare.length(); j--) {
                    result.deleteCharAt(j);
                }
            }
            int length = result.length();
            int common = 0;
            for (int j = 0; j < length; j++) {
                if (result.charAt(j) == compare.charAt(j)) {
                    common++;
                } else {
                    j = length;
                }
            }
            while (common < result.length()) {
                result.deleteCharAt(common);
            }
            if (result.length() == 0) {
                return result.toString();
            }
        }
        return result.toString();
    }
}
