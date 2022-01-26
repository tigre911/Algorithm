package backjoon.bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_17496 {
	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n, t, c, p;
		
		n = Integer.parseInt(st.nextToken());	//여름일 수
		t = Integer.parseInt(st.nextToken());	//성장일 수
		c = Integer.parseInt(st.nextToken());	//심을수 있는 칸
		p = Integer.parseInt(st.nextToken());	//스타후르츠 가격
		
		if (n%t==0) {
			System.out.println(((n/t)-1)*c*p);
		}
		else {
			System.out.println((n/t)*c*p);
		}
	}
}
