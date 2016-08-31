public class ValidParentheses {
    public boolean isValid(String s) {
        Stack st = new Stack();
        for (int i = 0; i < s.length(); i++) {
            char val = s.charAt(i);
            if (val == '(' || val == '[' || val == '{') {
                st.push(val);
            } else {
                if (st.empty()) {
                    return false;
                }
                char popped = (char) st.pop();
                if (val == ')' && popped != '(') {
                    return false;
                } else if (val == ']' && popped != '[') {
                    return false;
                } else if (val == '}' && popped != '{') {
                    return false;
                }
            }
        }
        if (!st.empty()) {
            return false;
        }
        return true;
    }
}
