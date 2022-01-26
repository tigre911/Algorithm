package backjoon.bronze;

import java.math.BigInteger;
import java.util.Scanner;

public class BOJ_1271 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		BigInteger n = scan.nextBigInteger();
		BigInteger m = scan.nextBigInteger();
		
		System.out.println(n.divide(m));
		System.out.println(n.remainder(m));
		scan.close();
	}

}
