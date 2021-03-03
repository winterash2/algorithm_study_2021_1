package unionfind;

import java.util.Scanner;

public class 공항 {
    static int n;
    static int m;
    static int[] p;

    static int find(int x){
        if(x != p[x]){
            return p[x] = find(p[x]);
        }
        return p[x];
    }

    static void union(int a, int b){
        a = find(a);
        b = find(b);
        if(a < b){
            p[b] = a;
        } else {
            p[a] = b;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int gates = sc.nextInt();
        int planes = sc.nextInt();
        p = new int[gates + 1];
        for(int i = 0; i <= gates; ++i){
            p[i] = i;
        }
        int answer = 0;
        for(int i = 0; i < planes; ++i){
            int plane = sc.nextInt();
            if(find(plane) != 0){
                union(find(plane), find(plane) - 1);
                answer++;
            } else {
                break;
            }
        }

        System.out.println(answer);
    }
}
