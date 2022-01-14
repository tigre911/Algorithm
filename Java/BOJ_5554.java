package backjoon.bronze;

import java.util.Scanner;

public class BOJ_5554 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a, b, c, d; // a - 집 학교 , b - 학교 pc방 , c - pc방 학원, d - 학원 집
		
		a = sc.nextInt();
		b = sc.nextInt();
		c = sc.nextInt();
		d = sc.nextInt();
		
		int result = a+b+c+d;
		
		System.out.println(result/60);
		System.out.println(result%60);
		
		sc.close();
	}
}
