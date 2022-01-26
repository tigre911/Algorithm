package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_1157 {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();		// 문자열을 입력받고
        str = str.toUpperCase();		// 전체를 다 대문자로 변환해준다. ( 대소문자의 구분이 없어야 하므로 )

        int[] arr = new int[26];		// 알파벳은 총 26개 이므로 26개의 배열 선언 ( 각 알파벳 개수를 세기 위한 배열 )
        int max=0;					// 가장 많이 나온 알파벳의 개수
        int index=0;				// 가장 많이 나온 알파벳 인덱스
        for(int i = 0 ; i < str.length(); i ++)
        {
            int alpha = str.charAt(i);		// alpha변수에 한문자씩 넣기
            arr[alpha-65]++;		// 대문자 A의 ASCII code 값은 65임. 입력받은 문자가 a,A(toUpperCase 함수로 인해 대문자로 변환)라고 치면
        }							// 65 - 65 = 0 이므로 위의 arr 배열의 0번째에는 a부터 순차적으로 개수를 샌다. A ~ Z 까지( 이해 꼭 해야함 )

        for(int i = 0 ; i < arr.length; i ++)	// 배열의 길이만큼 반복
        {
            if(max < arr[i])
            {
                max = arr[i];		// 가장 많은 알파벳을 max로 지정
                index = i+65;			// 가장 많은 알파벳의 수가 있는 배열의 index번호 + 65 를 하면 그 알파벳의 ASCII code가 나옴
            }
            else if(max == arr[i])	// 만약 가장 많은 알파벳의 개수의 합이 같다면 idx는 ? 로 지정
                index = '?';
        }

        System.out.println((char)index);		// idx 출력


    }
}
/*
대문자로 출력의 문제이기에 편리를 위해 입력값도 모두 대문자로 변환
	-> String.toUpperCase(); 모두 대문자로 변경, 소문자는 String.toLowerCase();

알파벳 'A ~ Z'는 총 26개
	-> int[] count = new int[26], 26크기의 배열 선언

입력 문자열 길이만큼 반복문 실행
	-> 입력 문자열 한 글자씩, 해당 알파벳 순서의 int배열 count 값 증가
    -> 'A'일 경우
    	ex) 'A'-'A' => 65-65 => 0으로 count배열 0번째 값 증가

알파벳 개수(배열크기)만큼 반복문 실행
	-> 가장 중복값이 큰지 비교하며 max에 저장
    -> 해당 위치 알파벳 알아내기 위해 (index + 'A')
    	ex) 1+'A' => 1+65 => 66, 66은 'B'에 해당
 */