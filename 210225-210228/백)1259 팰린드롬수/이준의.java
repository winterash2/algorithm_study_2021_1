package adhoc;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 팰린드롬수 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        while(true){
            String input = br.readLine();
            if(input.charAt(0) == '0') break;
            int left = 0, right = input.length() - 1;
            int iter = input.length() % 2 == 0 ? input.length() / 2 : input.length() / 2 + 1;
            boolean check = true;
            for(int i = 0; i < iter; ++i){
                if(input.charAt(left) != input.charAt(right)){
                    System.out.println("no");
                    check = false;
                    break;
                } else {
                    left++;
                    right--;
                }
            }
            if(check)
                System.out.println("yes");
        }
    }
}
/*
121
1231
12421
0
 */