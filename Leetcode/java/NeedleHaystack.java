public class NeedleHaystack {    
    public static int strStr(String haystack, String needle) {
        int needleLength = needle.length();
        int possIndex = haystack.length() - needleLength;
        for (int i = 0; i <= possIndex; i++) {
            String possNeedle = haystack.substring(i, i + needleLength);
            if (needle.equals(possNeedle)) {
                return i;
            }
        }
        return -1;
    }
}
