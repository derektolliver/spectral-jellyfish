public class RectangleArea {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int areaOne = (C - A) * (D - B);
        int areaTwo = (G - E) * (H - F);
        if (A >= G || B >= H || C <= E || D <= F) {
            return areaOne + areaTwo;
        }
        int length = Math.min(C, G) - Math.max(A, E);
        int width = Math.min(D, H) - Math.max(B, F);
        return areaOne + areaTwo - length * width;
    }
}
