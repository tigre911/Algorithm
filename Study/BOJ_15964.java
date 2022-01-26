package backjoon.bronze;

import java.util.Scanner;

public class BOJ_15964 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		//int형보다 큰 값을 출력할 수도 있으므로 long형(8byte)을 사용하여 출력한다.
		long a, b;
		a = sc.nextLong();
		b = sc.nextLong();
		
		System.out.println((a+b)*(a-b));
		sc.close();	
	}
}
