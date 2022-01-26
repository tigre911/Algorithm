package backjoon.bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_3003 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int a, b, c, d, e, f;
		a =  Integer.parseInt(st.nextToken());
		b =  Integer.parseInt(st.nextToken());
		c =  Integer.parseInt(st.nextToken());
		d =  Integer.parseInt(st.nextToken());
		e =  Integer.parseInt(st.nextToken());
		f =  Integer.parseInt(st.nextToken());

		System.out.print(1-a);
		System.out.print(" ");
		System.out.print(1-b);
		System.out.print(" ");
		System.out.print(2-c);
		System.out.print(" ");
		System.out.print(2-d);
		System.out.print(" ");
		System.out.print(2-e);
		System.out.print(" ");
		System.out.print(8-f);
		System.out.print(" ");
		
	}
}
/*
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a[] = new int[6];
		int b[] = {1,1,2,2,2,8};
		for(int i=0; i<a.length; i++) {
			a[i]=sc.nextInt();
		}
		for(int i =0; i<a.length; i++) {
			System.out.print(b[i]-a[i]+ " ");
		}
	}
}
*/