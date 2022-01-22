package BOJ;

import java.util.Arrays;
import java.util.Scanner;

public class BOJ_2577 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int mul = a*b*c;
        int[] arr = new int[10]; //0-9까지 숫자의 배열
//        System.out.println(mul);

        while(mul > 0) {
            arr[mul % 10]++;
            //0부터 세기 때문에 바로 10을 나눈 나머지값이 배열의 현재 위치이기 때문에
            // 배열의 현재위치를 하나씩 더해주면, 그 숫자가 얼만큼 나왔는지 알 수 있다.
            mul /= 10;
            // 다음 숫자 비교를 위해 10으로 나누어줌
//            System.out.println(Arrays.toString(arr));
        }
        for(int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }


    }
}
