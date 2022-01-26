package BOJ;

import java.util.Scanner;

public class BOJ_1546 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int total = 0;
        int max = 0;
        int score;
        //최대값 도출하는 알고리즘
        for (int i = 0; i < n; ++i) {
            score = sc.nextInt();
            total += score;
            if (score > max) {
                max = score;
            }
        }
        sc.close();
        //평균 구하기
        double avg = 0;
        avg = 100.0 * total / max / n;
        System.out.printf("%.2f", avg);
    }
}
