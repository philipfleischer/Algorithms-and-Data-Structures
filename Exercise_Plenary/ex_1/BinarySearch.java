import java.util.Scanner;

class BinarySearch {

    public static boolean binarySearch(int[] arr, int x) {
        int low = 0;
        int high = arr.length - 1;

        while (low <= high) {
            int i = (low + high) / 2;
            if (arr[i] == x) {
                return true;
            } else if (arr[i] < x) {
                low = i + 1;
            } else if (arr[i] > x) {
                high = i - 1;
            }
        }
        return false;
    }

    public static boolean linearSearch(int[] arr, int x) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == x) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Start reading");

        int arrN = sc.nextInt();
        int[] arr = new int[arrN];

        for (int i = 0; i < arrN; i++) {
            arr[i] = sc.nextInt();
        }

        System.out.println("read array");
        int queriesN = sc.nextInt();
        int[] queries = new int[queriesN];

        for (int i = 0; i < queriesN; i++) {
            queries[i] = sc.nextInt();
        }

        System.out.println("read queries");
        int answersN = sc.nextInt();
        boolean[] answers = new boolean[answersN];

        for (int i = 0; i < answersN; i++) {
            answers[i] = sc.nextBoolean();
        }
        System.out.println("read answers");

        // Do binarysearch
        for (int i = 0; i < queriesN; i++) {
            System.out.println(binarySearch(arr, queries[i]) == answers[i]);
        }
    }
}
