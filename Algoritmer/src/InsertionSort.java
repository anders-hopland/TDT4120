package Sorting;

/**
 * Created by Anders-Hopland on 22.08.2017.
 */
public class InsertionSort {
    public static void main(String[] args) {
        int[] arr = {3, 6, 3, 4, 9, 2, 0, 9, 8, 53, 34, 5,4, 67, 445, 45, 32};

        for (int i = 1; i < arr.length; i++) {
            int temp = arr[i];

            int j = i - 1;
            while (j >= 0 && arr[j] > temp) {
                arr[j + 1] = arr[j];
                j--;
            }

            arr[j + 1] = temp;
        }

        for (int num: arr) {
            System.out.print(num + ", ");
        }
    }
}
