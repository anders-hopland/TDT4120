package Sorting;

import java.util.Random;

/**
 * Created by Anders-Hopland on 22.08.2017.
 */
public class MergeSort {

    public static void main(String[] args) {
        Random random = new Random();

        int[] arr = new int[100];
        for (int i = 0; i < 100; i++) {
            arr[i] = random.nextInt(200);
        }

        int[] res = mergeSort(arr);

        for (int i: res) {
            System.out.print(i + ", ");
        }

    }

    public static int[] mergeSort(int[] arr) {
        if (arr.length < 2) {
            return arr;
        }

        int mid = arr.length / 2;
        int[] right = new int[mid];
        for (int i = 0; i < mid; i++) {
            right[i] = arr[i];
        }

        int[] left = new int[arr.length - mid];
        for (int i = mid; i < arr.length; i++) {
            left[i - mid] = arr[i];
        }

        int[] resultLeft = mergeSort(left);
        int[] resultRight = mergeSort(right);

        return merge(resultLeft, resultRight);
    }

    public static int[] merge(int[] left, int[] right) {
        int i = 0, l = 0, r = 0;
        int[] result = new int[left.length + right.length];

        while (l < left.length && r < right.length) {
            if (left[l] < right[r]) {
                result[i] = left[l];
                l++;
                i++;
            }
            else {
                result[i] = right[r];
                r++;
                i++;
            }
        }
        while (l < left.length) {
            result[i] = left[l];
            i++;
            l++;
        }

        while (r < right.length) {
            result[i] = right[r];
            r++;
            i++;
        }

        return result;
    }

}
