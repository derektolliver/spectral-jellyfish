public class PascalTriangleTwo {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> rowList = new ArrayList<Integer>();
        if (rowIndex == 0) {
            rowList.add(1);
        } else {
            rowList.add(1);
            rowList.add(1);
            for (int i = 1; i < rowIndex; i++) {
                List<Integer> tempList = new ArrayList<Integer>();
                tempList.add(1);
                for (int j = 0; j < rowList.size() - 1; j++) {
                    tempList.add(rowList.get(j) + rowList.get(j + 1));
                }
                tempList.add(1);
                rowList = tempList;
            }
        }
        return rowList;
    }
}
