import java.util.*;

public class RollingMedian {
    public static void main(String[] args) {
        int[] param = {1, 2, 3, 4, 5};
        System.out.println(Arrays.toString(findMedian(param)));
    }

    public static int[] findMedian(int[] list) {
        Comparator<Integer> max = new MaxHeapComparator();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>(5, max);
        PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();
        int[] medianList = new int[list.length];
        for (int i = 0; i < list.length; i++) {
            int val = list[i];
            minHeap.add(val);
            int maxSize = maxHeap.size();
            int minSize = minHeap.size();
            if (minSize == maxSize + 2) {
                maxHeap.add(minHeap.poll());
            }
            int result = 0;
            if ((maxSize + minSize) % 2 == 0) {
                result = (minHeap.peek() + maxHeap.peek()) / 2;
            } else {
                result = minHeap.peek();
            }
            medianList[i] = result;
        }
        return medianList;
    }

    private static class MaxHeapComparator implements Comparator<Integer> {
        public int compare(Integer x, Integer y) {
            if (x > y) {
                return 1;
            } else if (x < y) {
                return -1;
            } else {
                return 0;
            }
        }
    }
}
