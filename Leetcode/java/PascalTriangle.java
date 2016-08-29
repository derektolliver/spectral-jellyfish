public class PascalTriangle {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> rowList = new ArrayList<List<Integer>>();
        if (numRows != 0) {
            ArrayList<Integer> tempList = new ArrayList<Integer>();
            tempList.add(1);
            rowList.add(tempList);
            if (numRows == 1) {
                return rowList;
            }
            for (int i = 1; i < numRows; i++) {
                tempList = new ArrayList<Integer>();
                tempList.add(1);
                for (int j = 0; j < rowList.get(i - 1).size() - 1; j++) {
                    tempList.add(rowList.get(i - 1).get(j) + rowList.get(i - 1).get(j + 1));
                }
                tempList.add(1);
                rowList.add(tempList);
            }
        }
        return rowList;
    }
}
