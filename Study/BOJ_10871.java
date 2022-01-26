package BOJ;

import java.util.Arrays;
import java.util.Scanner;

public class BOJ_10871 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i<arr.length; i++){
            arr[i] = sc.nextInt();
        }
        System.out.println((Arrays.toString(arr)));
        for (int i = 0; i<arr.length; i++){
            if (arr[i] < x){
                System.out.print(arr[i] + " ");
            }
        }
    }
}
