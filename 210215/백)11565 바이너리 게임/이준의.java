/*
틀린 것 ㅜㅠ
 */

import java.util.Scanner;

public class 바이너리게임 {

    static boolean isEven(String str){
        int cnt = 0;
        for(int i = 0; i < str.length(); ++i){
            if(str.charAt(i) == '1') cnt++;
        }
        return cnt % 2 == 0 ? true : false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        String b = sc.nextLine();

        boolean check = true;

        for(int i = 0; i < b.length(); ++i){
            System.out.println(i);
            System.out.println(a);
            System.out.println(b);
            System.out.println("------");
            if(i >= a.length()){
                if(isEven(a)){
                    a += '0';
                } else {
                    a += '1';
                }
                if(a.charAt(i) != b.charAt(i)){
                    check = false;
                    System.out.println("DEFEAT");
                    break;
                } else {
                    continue;
                }
            }
            if(a.charAt(i) == b.charAt(i)) {
                continue;
            } else {
                a = a.substring(1, a.length());
                i = -1;
                continue;
            }
        }
        if(check){
            System.out.println("VICTORY");
        }
    }
}


/*
01011
0110
 */
/*
1111
1110
 */