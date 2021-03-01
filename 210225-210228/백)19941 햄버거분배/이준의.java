package greedy;

import java.util.Scanner;

public class 햄버거분배 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        sc.nextLine();

        String input = sc.nextLine();
        char[] hamburgs = new char[n];
        for(int i = 0; i < n; ++i){
            hamburgs[i] = input.charAt(i);
        }
        boolean[] check = new boolean[n];
        int answer = 0;
        for(int i = 0; i < n; ++i){
            boolean isHamburg = false;
            if(hamburgs[i] == 'P'){
                for(int a = i - k < 0 ? 0 : i - k; a < i && a >= 0; ++a){
                    if(!check[a] && hamburgs[a] == 'H'){
                        isHamburg = true;
                        check[a] = true;
                        break;
                    }
                }
                if(isHamburg){
                    answer++;
                } else {
                    for(int a = i; a <= i + k && a < n; ++a){
                        if(!check[a] && hamburgs[a] == 'H'){
                            isHamburg = true;
                            check[a] = true;
                            answer++;
                            break;
                        }
                    }
                }
            }
        }
        System.out.println(answer);
    }
}
/*
20 1
HHPHPPHHPPHPPPHPHPHP
4 1
PHPH
4 2
HHPP
8 3
PPHHHHPP
 */