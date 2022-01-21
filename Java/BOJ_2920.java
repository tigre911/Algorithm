package backjoon.bronze;

//import java.util.Arrays;
import java.util.Scanner;


public class BOJ_2920 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] list = new int[8];
		for (int i = 0; i < list.length; i++) {
			list[i] = sc.nextInt();
		}
		
		String output = "";
		for (int i = 0; i < list.length - 1; i++) {
			if (list[i+1]==list[i] +1) {
				output = "ascending";
			}else if (list[i+1]==list[i]-1) {
				output = "descending";
			}else {
				output = "mixed";
				break;
			}
		}
		System.out.println(output);
		
		sc.close();
	}
}
/*요소 확인
		System.out.println(Arrays.toString(list));
		*/