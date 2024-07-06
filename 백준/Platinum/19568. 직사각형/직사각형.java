public class Main {
    public static void main(String[] args) {
        int[][] arr = new int[30][30];

        for (int i = 0; i < 30; i++) {
            for (int j = 0; j < 30; j++) {
                if (i == 15) {
                    if (j < 15) {
                        arr[i][j] = 1;
                    } else if (j > 15) {
                        arr[i][j] = 15;
                    }
                } else if (j == 15) {
                    if (i < 15) {
                        arr[i][j] = 225;
                    } else if (i > 15) {
                        arr[i][j] = 3375;
                    }
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int[] row : arr) {
            for (int value : row) {
                sb.append(value).append(' ');
            }
            sb.append('\n');
        }
        System.out.print(sb);
    }
}
